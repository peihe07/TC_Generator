"""W-145（77 包 §2）—— 拆分稽核：對 237 個 Functional leaf 逐一施 §8.3 之壓力測試。

**壓力測試（canon §8.3／§8.2.2）**：
    「若只有部分行為 fail，我的 pass/fail 判定是否仍不含糊？」
    兩個**獨立之部分失效**皆經同一 TC 落到 fail → **綑綁 → 拆**。

三類須特別檢：
 (1) **多值列舉** —— 一條 TC 驗多個值；任一值錯即 fail 而不可分辨是哪一值
 (2) **Decision Table** —— 條文列多列真值表，每列為獨立之部分失效
 (3) **§7 之負向配對** —— enumerated supported items 須配至少一條 unsupported 負向 TC

**維持一條者亦列**（§8.2.2：同一控制元件之多列 ER 維持一條），並記其依據。
**不得為使拆分數上升而拆。**
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]

# (1) 多值列舉：條文於同一 token 上列舉 ≥2 個相異值，且其行為對各值不同
ENUM = re.compile(r'\$?(\w+)\$?\s*(?:==|=|passes to)\s*"([^"]+)"')
# (2) Decision Table：**每個 `IF` 即真值表之一列**。
# 初版以 `IF .*? THEN` 之非貪婪配對計數，於單一 leaf 之多條文上低估為 1
# （50 輪 W-145 實測：`IF` 出現 ≥2 者 8 leaf，而初版報 0）。
DTAB = re.compile(r"\bIF\b", re.I)
# (3) 列舉型 leaf（§7）：其驗證標的之訊號**具列舉值域**（基數 ≥3）。
# 初版以「條文內相異狀態名 ≥3」為判準，而條文多只提 1–2 個值 ——
# **列舉性在值域，不在條文之措辭**（50 輪 W-145 實測：初版報 0）。
ENUM_SIGNALS = {"FL_HS_STATSts", "FR_HS_STATSts", "FL_VS_STATSts", "FR_VS_STATSts",
                "Tri_Level_HSW_StatSts"}
SIGREF = re.compile(r"\b[A-Z][A-Z0-9_]+\.(\w+)")


def latest_tcs() -> dict[str, list[dict]]:
    g: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            g[m.group(1)].append((int(m.group(2) or 1), f))
    out: dict[str, list[dict]] = collections.defaultdict(list)
    for _, v in sorted(g.items()):
        for tc in json.loads(max(v)[1].read_text(encoding="utf-8"))["tcs"]:
            out[tc["leaf_id"]].append(tc)
    return out


def audit(leaf: str, text: str, tcs: list[dict]) -> dict:
    """回傳該 leaf 之稽核列。"""
    flat = re.sub(r"\s+", " ", text)
    cur = len(tcs)

    # —— (1) 多值列舉 ——
    vals: dict[str, set[str]] = collections.defaultdict(set)
    for tok, v in ENUM.findall(flat):
        vals[tok].add(v)
    multi = {t: vs for t, vs in vals.items() if len(vs) >= 2}
    # 已生成之 TC 中，單一條**綑綁兩個獨立部分失效**者（§8.3 之壓力測試）。
    #
    # **初版判準過寬**（50 輪 W-145 實測）：其以「TC 內相異狀態值 ≥2」為準，
    # 而把**同一情境之前置步驟**（如先送 `ESS_ENG_ST = 3` 再送 `EngineSts = 2`）
    # 誤判為多值 —— 二者非兩個驗證點，是一個情境之鋪陳。
    # 禁區逐字：「**不得為使拆分數上升而拆**」。
    #
    # 改判準：只數 **ER 之驗證性斷言**（非 `… is sent` 之送出回聲、非 `PENDING`），
    # 其標的相異者 ≥2 方為綑綁。
    # 依 **canon §8.2.2 之明文軸**：
    #   同一物理／邏輯控制元件 → **維持一條**（多列 ER）
    #   **不同控制實體** → 拆為獨立 TC
    # 三版判準之實測（50 輪 W-145，逐版收斂）：
    #   v1「TC 內相異狀態值 ≥2」          → 90 —— 把前置步驟誤為多值
    #   v2「ER 之驗證性斷言標的相異 ≥2」  → 71 —— 把同一轉換之前後態誤為兩失效
    #   v3「ER 所涉之**控制實體** ≥2」    → 本版
    # 禁區逐字：「**不得為使拆分數上升而拆**」。
    ECHO = re.compile(r"\bis sent\b|\bis accepted\b|\bis recorded\b|"
                      r"completes start-up|^\s*\d+\.\s*PENDING")
    ENTITY = {
        "heated seat": r"heated seat",
        "vented seat": r"vented seat",
        "heated steering wheel": r"heated steering wheel",
        "head restraint": r"head restraint|headrest",
        "rear camera": r"rear (view )?camera",
        "touchscreen": r"touchscreen|screen off|display state",
        "audio": r"audio|track",
    }
    bundled = 0
    for tc in tcs:
        ents = set()
        for line in tc["expected_result"].split("\n"):
            if ECHO.search(line):
                continue
            # 畫面名稱 `Heated / Vented Seats screen` 非控制實體 —— 去之，
            # 否則任何提及該畫面之 ER 皆被誤判為「加熱＋通風」兩實體。
            line = re.sub(r"Heated\s*/\s*Vented Seats screen", "«screen»", line, flags=re.I)
            for name, pat in ENTITY.items():
                if re.search(pat, line, re.I):
                    ents.add(name)
        if len(ents) >= 2:
            bundled += len(ents) - 1

    # —— (2) Decision Table ——
    dt_rows = len(DTAB.findall(flat))

    # —— (3) §7 負向配對 —— 以**該 leaf 所驗之列舉型訊號**為單位
    sigs = {m.group(1) for m in SIGREF.finditer(flat)} | {
        m.group(1) for tc in tcs
        for m in SIGREF.finditer(tc["test_procedure"] + tc["expected_result"])}
    enum_sigs = sigs & ENUM_SIGNALS
    enumerated = bool(enum_sigs)
    has_neg = any(tc["design_method"].startswith("負向") for tc in tcs)

    need, axis, basis = cur, "", ""
    if dt_rows >= 2:
        need = max(need, dt_rows)
        axis, basis = "decision-table（每列一條）", "§8.2.2／§8.3"
    if bundled:
        need = max(need, cur + bundled)
        axis = (axis + "；" if axis else "") + "multi-value（一條驗多值）"
        basis = (basis + "／" if basis else "") + "§8.3 壓力測試"
    # **§7 之配對粒度：兩讀並列，不以任一為準**（78 包 §1，51 輪 D-3）。
    #
    # 50 輪本層曾標「Pei 裁定 2026-08-23 取讀法 B」——
    # **該裁定確為 Pei 所裁，惟其出處為執行層 thread 之直接提問**
    # （本層以選項式徵詢，Pei 擇「讀法 B：逐列舉型訊號」），
    # **未經下放／上繳包流通**，故分析層於其 thread 內查無此裁定（A-VS156）。
    # 依 78 包 §1 之裁定「該讀法之採用暫掛」，本函式**不加任何負向補數**，
    # 兩讀之數改由 `main()` 並列輸出。
    #     讀法 A（逐 leaf）  ：if enumerated and not has_neg: need += 1
    #     讀法 B（逐列舉訊號）：0
    if False:
        need += 1
        axis = (axis + "；" if axis else "") + "negative（列舉須配 unsupported）"
        basis = (basis + "／" if basis else "") + "§7"
    if need == cur and not axis:
        axis = "—（維持一條）"
        basis = ("§8.2.2：同一控制元件之多列 ER 維持一條" if cur else
                 "未生成，無 TC 可拆")
    return {"leaf_id": leaf, "current_tc": cur, "target_tc": need,
            "split_axis": axis, "basis": basis,
            "enumerated": ";".join(sorted(enum_sigs)) if enumerated else "no",
            "has_negative": "yes" if has_neg else "no",
            "excerpt": flat[:110]}


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    gen = [r["leaf_id"] for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")]
    tcs = latest_tcs()

    rows = []
    for leaf in gen:
        qs = re.findall(r"\d{7}", (l2r.get(leaf, {}).get("reqid_list") or ""))
        text = " ".join("\n".join(blocks[q]["text"].split("\n")[1:])
                        for q in qs if q in blocks)
        rows.append(audit(leaf, text, tcs.get(leaf, [])))

    p = FEAT / "docs/reports/split_audit.tsv"
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    cur = sum(r["current_tc"] for r in rows)
    tgt = sum(r["target_tc"] for r in rows)
    to_split = [r for r in rows if r["target_tc"] > r["current_tc"] and r["current_tc"]]
    keep = [r for r in rows if r["current_tc"] and r["target_tc"] == r["current_tc"]]
    dt = [r for r in rows if "decision-table" in r["split_axis"]]
    mv = [r for r in rows if "multi-value" in r["split_axis"]]
    neg = [r for r in rows if "negative" in r["split_axis"]]
    enum_leaves = [r for r in rows if r["enumerated"] != "no"]

    print(f"母體 **{len(rows)}** leaf｜現行 TC **{cur}**｜拆後預估 **{tgt}**｜"
          f"與現行 143 之差 **{tgt - 143:+d}**\n")
    print("## 三類特別檢\n")
    print("| 類 | 判準 | 應拆之 leaf 數 |")
    print("|---|---|---:|")
    print(f"| (1) 多值列舉 | 一條 TC 驗多個值，fail 不可分辨是哪一值 | **{len(mv)}** |")
    print(f"| (2) Decision Table | 條文列多列真值表，每列一獨立部分失效 | **{len(dt)}** |")
    print(f"| (3) §7 負向配對 | 列舉型 leaf 未配 unsupported 負向 TC | **{len(neg)}** |")
    print()
    have = sum(1 for v in tcs.values() for t in v
               if t["design_method"].startswith("負向"))
    domains = sorted({d for r in enum_leaves for d in r["enumerated"].split(";")})
    covered = sorted({m.group(1) for v in tcs.values() for t in v
                      if t["design_method"].startswith("負向")
                      for m in SIGREF.finditer(t["test_procedure"] + t["expected_result"])
                      if m.group(1) in ENUM_SIGNALS})
    print(f"列舉型 leaf **{len(enum_leaves)}**｜列舉型訊號 **{len(domains)}**"
          f"（{'／'.join(domains)}）")
    print(f"現有 `負向 / Invalid` TC **{have}**，其覆蓋之列舉型訊號 "
          f"**{len(covered)}**（{'／'.join(covered)}）\n")
    # 兩讀之數獨立計算（`need` 已不含負向補數，見 audit() 之註）
    a_need = [r for r in enum_leaves if r["has_negative"] == "no"]
    b_need = len(domains) - len(covered)
    print("**§7 之配對粒度依 R-VS74（Pei 2026-08-23）定案為讀法 B —— 應補 0**。")
    print("兩讀並列取消；讀法 A 之數僅供對照：")
    print(f"  讀法 A（**逐 leaf**）—— 每個列舉型 leaf 各須一條負向：應補 "
          f"**{len(a_need)}**；拆後總量 **{tgt + len(a_need)}**")
    print(f"  讀法 B（**逐列舉型訊號**）—— 每個值域一條負向即足：應補 "
          f"**{b_need}**；拆後總量 **{tgt + b_need}**")
    print(f"  **兩讀之差 {len(a_need) - b_need} 條**\n")
    print(f"應拆之 leaf **{len(to_split)}**｜維持一條之 leaf **{len(keep)}**"
          f"｜未生成 **{sum(1 for r in rows if not r['current_tc'])}**")


if __name__ == "__main__":
    main()
