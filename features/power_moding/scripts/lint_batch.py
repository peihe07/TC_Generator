#!/usr/bin/env python3
"""Phase 4 batch 之 lint —— profile §3 各欄規則 ＋ canon 條文層 ＋ R-PMH50。

**13 包擴充（R-PMH52）**：原 20 項全為 profile 欄位層與 id 層，
**零項檢查 canon §4.3.1／§5.1／§5.2／§5.5／§8.5／§10.5／§11** ——
而 batch 1 於該七節共六類違規、涉全部八條，lint 仍 20/20 全綠。
本輪新增七項，並於輸出末尾**具名其仍未涵蓋之 canon 節號**。

**R-PMH50 之限度須明說**：本 lint 只驗 `source_clause` **存在且非空**、
且其 `origin` 為 `spec_pdf`。**「是否忠於規格」本身不可機械檢查** ——
須人讀 PDF 原文與 TC 對照。本檢查只保證覆核所需之材料存在，不保證覆核已做。
"""

# R-PMH92 —— 本檢查之 must-hit 註冊。**總表之結果欄由此決定，手寫不採認。**
HAS_MUST_HIT = True
MUST_HIT_NOTE = '外部 fixture 兩份（`batch01_prerework` 21/30、`batch01_r2` 29/30）逐輪實跑並 FAIL'

import argparse
import ast
import json
import re
from functools import lru_cache
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SPEC = "Power Moding HMI Logic and Flow R1 SR24 2A"

# R-PMH99(c)（26 包）—— `-007` 之七項事件層限定，其字串須於 procedure 各出現一次。
LIMIT_TOKENS = [
    "press the ON/OFF key", "turn key-off", "open any door",
    "adjust HVAC hard controls", "press the Mute key",
    "the Headunit Mode key", "change the headunit mode by voice recognition",
]

# **R-PMH58（15 包）—— `COVERED` 不得手寫，須自各檢查點自動彙集。**
#
# 各 `chk(...)` 於其呼叫處以 `canon=` 具名其所檢查之 canon 節號；
# 本常數由 `ast` 掃本檔自身之 `chk(...)` 呼叫彙集而得，
# `canon_coverage.py` 匯入之並自 canon 節號全集求差集。
#
# 依據（14 包 §3.2）：手寫之 `COVERED` 先宣告 `5.2` 而該檢查尚未實作，
# 致未涵蓋清單稱其「已涵蓋」而實際沒有。**宣告與實作分離即會分岔**
# （A-PMH12 之同型）。自動彙集使「宣告」與「檢查點」成為同一處，無從分岔。
#
# 另設**執行期交叉核對**：`main()` 末尾比對「靜態彙集」與「本次實際執行到之
# 檢查點」，二者不同即具名 —— 攔下「宣告於原始碼但該分支從未執行」之情形。
def _covered_from_source() -> set[str]:
    """R-PMH58 —— 自本檔之 `chk(..., canon=...)` 呼叫靜態彙集已涵蓋之節號。"""
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    out: set[str] = set()
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call)
                and getattr(node.func, "id", "") == "chk"):
            continue
        for kw in node.keywords:
            if kw.arg == "canon":
                v = ast.literal_eval(kw.value)
                out.update([v] if isinstance(v, str) else v)
    return out


COVERED = _covered_from_source()

LAYER3 = ROOT / "data" / "layer3_sections.tsv"


def _norm_src(s: str) -> str:
    """來源比對用之正規化 —— 只吸收空白、匯出轉義與**引號字形**，**不吸收任何字詞**。

    ⚠ **引號字形之正規化為實測所迫**：`sandbox/spec.txt`（`fitz` 之 text 萃取）
    將 `vehicle’s` 記為直撇 `vehicle's`，而 `gen_batch01.py` 之 `source_clause`
    保有彎撇 —— **二者為同一份 PDF 之兩種萃取**（30 包步驟 4 首次量測到）。
    **該差異只在字形，不在字詞**；本檢查因而於兩側同時正規化。
    **其代價已具名**：若某處之引號本身有意義（如引用之界限），本檢查看不出來。
    """
    s = str(s).replace("_x000D_", " ")
    for a_, b_ in (("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'),
                   ("\u201d", '"'), ("\u2013", "-"), ("\u2014", "-"),
                   ("\u2026", "...")):
        s = s.replace(a_, b_)
    return re.sub(r"\s+", " ", s).strip()


@lru_cache(maxsize=1)
def _pdf_blob() -> str:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import chapter_bidirectional as cb
    return cb.pdf_text()


@lru_cache(maxsize=8)
def _sys1_blob(outline: str) -> str:
    """SYS1 匯出中該 outline 之 `Description` 欄全文。"""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import chapter_bidirectional as cb
    import openpyxl
    wb = openpyxl.load_workbook(cb.SYS1, read_only=True, data_only=True)
    ws = wb["Basic Report"]
    out = ""
    for r in ws.iter_rows(min_row=2, values_only=True):
        if str(r[2] or "") == outline:
            out = str(r[3] or "")
            break
    wb.close()
    return out


def batch_limits(d: dict) -> dict:
    """R-PMH107(b) —— 本批之事件層限定清單。

    **讀該批之 `limits` 宣告**；未宣告者回退為舊之寫死值
    （`-007` × 七項），使既有 fixture 之期望不變。
    """
    if "limits" in d:
        return d["limits"]
    return {t["tc_id"]: LIMIT_TOKENS for t in d.get("tcs", [])
            if t["tc_id"].endswith("007")}


def limit_must_hit() -> int:
    """R-PMH99(c) 之 must-hit —— 刪去任一項須 FAIL、重複任一項須 FAIL。

    **29 包步驟 4（R-PMH107(b)）之一般化**：母體由寫死之 `batch01` × `-007` × 七項
    改為**逐批讀其 `limits` 宣告**，故 batch 2 之十二項自此同受保護。
    **檢查項數不變** —— 本函式為既有檢查之 must-hit，非新檢查。
    """
    import copy
    import subprocess
    tmp = ROOT / "tests" / "fixtures" / "_limit_must_hit.json"

    def run(doc, rule="R-PMH99(c)") -> bool:
        tmp.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                            str(tmp.relative_to(ROOT))],
                           capture_output=True, text=True, cwd=ROOT)
        return r.returncode == 1 and any(
            rule in ln and "FAIL" in ln for ln in r.stdout.splitlines())

    print("=== R-PMH99(c) 之 must-hit（26 包步驟 6；29 包一般化）===")
    print("**限定得合併於同一步驟，故『某項被忽略』與『某項被刪去』"
          "在文本上難以分辨** —— 本錨點即驗其可分辨。\n")
    ok_del = ok_dup = ok_three = True
    n_del = 0
    try:
        # **33 包（R-PMH124）之母體一般化**：批次清單原為寫死之列舉
        # （32 包補為四批仍是列舉），**新批仍須有人記得改**。
        # 改為**掃 `generated/` 之全部批次檔** —— 母體之來源自此與期望值同源。
        # 空 `limits` 之批（如 batch03，其限定在 pre_conditions）明白印出，不冒充通過。
        for bn in sorted(p.stem for p in (ROOT / "generated").glob("batch*.json")):
            base = json.loads((ROOT / "generated" / f"{bn}.json").read_text(encoding="utf-8"))
            lim = batch_limits(base)
            print(f"--- {bn}：{len(lim)} 條／{sum(len(v) for v in lim.values())} 項 ---")
            if not lim:
                print("  （本批之 `limits` 為空 —— 其事件層限定置於 pre_conditions，"
                      "不受 R-PMH99(c) 之字串檢查所管）")
                continue
            for tc_id, toks in lim.items():
                for tok in toks:
                    d = copy.deepcopy(base)
                    for x in d["tcs"]:
                        if x["tc_id"] == tc_id:
                            x["test_procedure"] = x["test_procedure"].replace(tok, "XXXX")
                    hit = run(d)
                    ok_del &= hit
                    n_del += 1
                    print(f"  {tc_id} 刪去 `{tok}` → FAIL 被攔下：{hit}")
            # 重複：取該批之第一條、第一項
            tc_id, toks = next(iter(lim.items()))
            d = copy.deepcopy(base)
            for x in d["tcs"]:
                if x["tc_id"] == tc_id:
                    x["test_procedure"] += f"\n99. Do not {toks[0]} again"
            hit = run(d)
            ok_dup &= hit
            print(f"  {tc_id} 重複 `{toks[0]}` → FAIL 被攔下：{hit}")
            # R-PMH99(a)：一步含三項（僅對限定項 >= 3 之批有意義）
            if len(toks) >= 3:
                d = copy.deepcopy(base)
                for x in d["tcs"]:
                    if x["tc_id"] == tc_id:
                        lines = [y for y in x["test_procedure"].split("\n") if y.strip()]
                        lines[0] = f"1. Do not {toks[0]} and do not {toks[1]} and do not {toks[2]}"
                        x["test_procedure"] = "\n".join(lines)
                hit = run(d, "R-PMH99(a)")
                ok_three &= hit
                print(f"  {tc_id} 一步含三項 → R-PMH99(a) FAIL 被攔下：{hit}")
            else:
                print(f"  {tc_id} 之限定僅 {len(toks)} 項 —— "
                      "**一步含三項之錨點於本批不適用**（不計為 PASS，亦不計為 FAIL）")
    finally:
        tmp.unlink(missing_ok=True)
    print("\n" + "=" * 60)
    print(f"刪去 {n_del}/{n_del} 皆 FAIL: {ok_del}；重複 FAIL: {ok_dup}；"
          f"一步三項 FAIL: {ok_three}")
    return 0 if (ok_del and ok_dup and ok_three) else 1


def final_step_must_hit() -> int:
    """R-PMH116(b)(c) —— Final Step 檢查之錨點。

    (b) **must-hit**：batch 3 之五條**修正前**之 Final Step 須 **FAIL**；
    (c) **範圍向**：batch 1／batch 2 之現行 Final Step 須 **PASS**。

    修正前之五句於此**逐字內嵌**（其來源為 `generated/batch03.json` 於 30 包之版本）
    —— 不另建 fixture 檔，使錨點與其所攔之缺陷同處一檔。
    """
    PRE_FIX = [
        ("-017", "3. Interact with the pop-up repeatedly beyond ten minutes and "
                 "record when the radio powers off"),
        ("-018", "3. Read the display for the FOTA via Wi-Fi and Charge Now pop-ups"),
        ("-019", "2. Repeat the test, dismiss the update on the FOTA pop-up instead, "
                 "and read the display"),
        ("-020", "2. Repeat the test, dismiss the Wi-Fi configuration pop-up instead, "
                 "and read the display"),
        ("-021", "3. Read the radio power state"),
    ]
    BOUNDARY = [
        ("-016 之 `Compare … with …`（具名兩造）", True,
         "4. Compare the recorded duration with the stated maximum"),
        ("裸 `Compare the values`（不具名兩造）", False, "4. Compare the values"),
    ]
    VERIFY = (r"\b(check|checks|confirm|confirms|verify|verifies)\s+that\b"
              r"|\bto\s+(verify|check|confirm)\b"
              r"|\bcompare[sd]?\b[^.]*\b(with|against|to)\b")

    def hit(s: str) -> bool:
        return bool(re.search(VERIFY, s, re.I))

    print("=== R-PMH116 —— Final Step 檢查之錨點（31 包步驟 2）===\n")
    print("(b) must-hit —— batch 3 五條**修正前**之 Final Step 須 FAIL：")
    ok_b = True
    for tag, s in PRE_FIX:
        f = not hit(s)
        ok_b &= f
        print(f"  {tag}  FAIL 被攔下：{f}   {s[:64]}")
    print("\n(c) 範圍向 —— batch 1／batch 2 之現行 Final Step 須 PASS：")
    ok_c = True
    n = 0
    for bn in ("batch01", "batch02"):
        d = json.loads((ROOT / "generated" / f"{bn}.json").read_text(encoding="utf-8"))
        for t in d["tcs"]:
            fs = [x for x in t["test_procedure"].split("\n") if x.strip()][-1]
            p_ = hit(fs)
            ok_c &= p_
            n += 1
            if not p_:
                print(f"  ⚠ {t['tc_id']} 被誤攔：{fs}")
    print(f"  {n} 條全部 PASS：{ok_c}")
    print("\n`Compare` 之邊界（R-PMH116 明令具名，其理由一體適用）：")
    ok_d = True
    for tag, want, s in BOUNDARY:
        got = hit(s)
        ok_d &= (got == want)
        print(f"  {tag} → {'通過' if got else '不通過'}（期望 "
              f"{'通過' if want else '不通過'}）：{got == want}")
    print("\n" + "=" * 60)
    print(f"must-hit 5/5 FAIL: {ok_b}；範圍向 {n}/{n} PASS: {ok_c}；"
          f"`Compare` 邊界二例: {ok_d}")
    return 0 if (ok_b and ok_c and ok_d) else 1


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("batch", nargs="?")
    ap.add_argument("--limit-must-hit", action="store_true",
                    help="R-PMH99(c) 之 must-hit（刪去／重複任一限定項須 FAIL）")
    ap.add_argument("--final-step-must-hit", action="store_true",
                    help="R-PMH116 之錨點（本批五條須 FAIL／batch 1-2 須 PASS）")
    a = ap.parse_args()
    if a.limit_must_hit:
        sys.exit(limit_must_hit())
    if a.final_step_must_hit:
        sys.exit(final_step_must_hit())
    if a.batch is None:
        raise SystemExit("須給 batch 檔，或用 --limit-must-hit")
    d = json.loads((ROOT / a.batch).read_text(encoding="utf-8"))
    cfg = yaml.safe_load((ROOT / "feature.yaml").read_text(encoding="utf-8"))
    voc = set(cfg["lint"]["design_method_vocabulary"])
    sets = set(cfg["write_back"]["test_set_values"])
    import csv
    l3 = {r["swe_requirement_id"]: r["outline_number"] for r in
          csv.DictReader(LAYER3.open(encoding="utf-8"), delimiter="\t")}

    checks, fails = [], []

    executed: set[str] = set()

    def chk(name, ok, detail="", canon=()):
        executed.update([canon] if isinstance(canon, str) else canon)
        checks.append((name, ok, detail))
        if not ok:
            fails.append(name)

    tcs = d["tcs"]
    print(f"batch = {d['batch']}；TC 數 = {len(tcs)}；leaf 數 = "
          f"{len({t['leaf_id'] for t in tcs})}\n")

    # --- R-PMH50 ---
    miss = [t["tc_id"] for t in tcs if not str(t.get("source_clause", "")).strip()]
    chk("R-PMH50 每 leaf 有 source_clause 且非空", not miss, str(miss))
    # 30 包步驟 4（R-PMH107）：**期望值由寫死之「必為 `spec_pdf`」改為
    # 「必逐字見於其所宣告之來源」** —— 一般化，非新增檢查項。
    # 其緣由：R-PMH75 令 outline 9.1 之 5 leaf 之來源**反轉為 SYS1**，
    # 原檢查會把「正確遵守 R-PMH75」判為 FAIL。**新形態更強** ——
    # 原檢查只看欄位字串，新檢查實際回原文件比對。
    bad = []
    for t in tcs:
        org = str(t.get("source_clause_origin", ""))
        sc = str(t.get("source_clause", ""))
        if org.startswith("spec_pdf"):
            ok = _norm_src(sc) in _norm_src(_pdf_blob())
        elif org.startswith("sys1_export"):
            ok = _norm_src(sc) in _norm_src(_sys1_blob(org.split()[-1]))
        else:
            ok = False
        if not ok:
            bad.append((t["tc_id"], org or "(空)"))
    chk("R-PMH50／R-PMH75 source_clause 逐字見於其所宣告之來源", not bad, str(bad))

    # --- profile §3.1：test_item 下半括號（硬規則）---
    bad = [t["tc_id"] for t in tcs
           if not re.search(r"\n\n\(.+\)$", t["test_item"], re.S)]
    chk("profile §3.1 test_item 具下半括號（硬規則）", not bad, str(bad))

    # --- profile §3.3：design_method ∈ 9 詞條 ---
    bad = [(t["tc_id"], t["design_method"]) for t in tcs if t["design_method"] not in voc]
    chk("profile §3.3 design_method ∈ 下拉選單 9 詞條", not bad, str(bad))

    # --- profile §3.4：spec_reference 形態 ＋ 與 layer3 對得上 ---
    bad = []
    for t in tcs:
        m = re.fullmatch(re.escape(SPEC) + r"_(\d+(?:\.\d+)*)", t["specification_reference"])
        if not m or l3.get(t["leaf_id"]) != m.group(1):
            bad.append((t["tc_id"], t["specification_reference"], l3.get(t["leaf_id"])))
    chk("profile §3.4 spec_reference 形態且與 layer3_sections.tsv 相符", not bad,
        str(bad), canon="10.7")

    # --- profile §3.5：priority ∈ P0–P3 ---
    bad = [(t["tc_id"], t["priority"]) for t in tcs
           if t["priority"] not in {"P0", "P1", "P2", "P3"}]
    chk("profile §3.5 priority ∈ {P0,P1,P2,P3}（母本 DV）", not bad, str(bad),
        canon="10.2")

    # --- profile §3.6 / §3.8：Q 與 T–Z 留白 ---
    chk("profile §3.6 estimated_test_time 留白",
        all(not str(t.get("estimated_test_time", "")).strip() for t in tcs))
    chk("profile §3.8 vehicle_models 留白",
        all(not str(t.get("vehicle_models", "")).strip() for t in tcs))

    # --- profile §3.7：functional_safety = NA ---
    bad = [t["tc_id"] for t in tcs if t.get("functional_safety") != "NA"]
    chk("profile §3.7 functional_safety = NA", not bad, str(bad))

    # --- profile §5 / R-PMH18：三字串之大小寫 ---
    chk("R-PMH18 test_group = 'Disclaimer screen'（小寫 s）",
        all(t["test_group"] == "Disclaimer screen" for t in tcs))
    # **28 包：由 batch-01 專屬之硬編碼改為讀該批之 `test_set`**
    # （R-PMH104：**一般化既有檢查，非新增檢查**）。其值仍須 ∈ Layer 2 定版 8 組。
    # **32 包（R-PMH107）之一般化**：batch 4 起一批得含**多個 Test Set**
    # （R-PMH120 之收尾計畫）。原讀法為「該批一個值」（`d["test_set"]`），
    # 於兩值之批必 FAIL。改為：**讀該批之宣告**（`test_sets` 為清單，
    # 或 `test_set` 為單值），驗每條之值 ∈ 該宣告。
    # **檢查之種類不變**（各 TC 之 test_set 須合於該批之宣告），只是宣告得為多值。
    decl = d.get("test_sets") or ([d["test_set"]] if d.get("test_set") else [])
    seen = sorted({t["test_set"] for t in tcs})
    chk(f"R-PMH36 各 TC 之 test_set ∈ 該批之宣告（{len(decl)} 值，大小寫敏感）",
        bool(decl) and all(t["test_set"] in decl for t in tcs)
        and set(seen) == set(decl),
        f"批宣告={decl!r}；實測相異值={seen}")
    chk("R-PMH16 tc_id 形態 NR1L-DisclaimerScreen-{NNN}",
        all(re.fullmatch(r"NR1L-DisclaimerScreen-\d{3}", t["tc_id"]) for t in tcs),
        canon="10.3")
    chk("test_set ∈ Layer 2 定版 8 組", all(t["test_set"] in sets for t in tcs))

    # --- profile §11：方括號禁止（本 feature 無例外）---
    bad = [t["tc_id"] for t in tcs
           if re.search(r"\[[^\]]+\]", t["test_item"] + t["pre_conditions"]
                        + t["test_procedure"] + t["expected_result"])]
    chk("canon §11 方括號禁止（本 feature 無 profile 例外）", not bad, str(bad),
        canon="11")

    # --- canon：步數一致、無空欄、無 NA 充當未知 ---
    bad = [(t["tc_id"], len(t["test_procedure"].split("\n")),
            len(t["expected_result"].split("\n"))) for t in tcs
           if len(t["test_procedure"].split("\n")) != len(t["expected_result"].split("\n"))]
    chk("procedure 與 ER 步數一致", not bad, str(bad))
    REQ = ["test_item", "pre_conditions", "test_procedure", "expected_result",
           "specification_reference", "design_method", "priority"]
    bad = [(t["tc_id"], f) for t in tcs for f in REQ if not str(t[f]).strip()]
    chk("必填欄無空", not bad, str(bad))
    bad = [t["tc_id"] for t in tcs if re.search(r"\bNA\b", t["expected_result"])]
    chk("ER 未以 NA 充當未知", not bad, str(bad), canon="8.4.3")

    # ==================== 13 包新增（R-PMH52）====================

    # C1 §10.5 —— 至少 2 步（Single-step TCs are rejected）
    bad = [(t["tc_id"], len([x for x in t["test_procedure"].split("\n") if x.strip()]))
           for t in tcs
           if len([x for x in t["test_procedure"].split("\n") if x.strip()]) < 2]
    chk("canon §10.5 test_procedure >= 2 步", not bad, str(bad), canon="10.5")

    # C2 §5.1 —— 禁用動詞作主動詞
    FORBID = r"\b(observe|see if|check whether|make sure|ensure|watch|look at|try to)\b"
    bad = []
    for t in tcs:
        for ln in t["test_procedure"].split("\n"):
            body = re.sub(r"^\s*\d+[.)]\s*", "", ln)
            for m in re.finditer(FORBID, body, re.I):
                bad.append((t["tc_id"], m.group(0), body[:60]))
    chk("canon §5.1 procedure 無禁用動詞", not bad, f"{len(bad)} 處 {bad[:3]}",
        canon="5.1")

    # C3 §5.2B/§5.5 —— Final Step 須含驗證意圖
    #
    # **31 包（R-PMH116）之強化 —— apparatus 首次解凍，其範圍限於本項。**
    #
    # 病灶：原判準為 `check that|confirm that|verify that|record|compare|read`。
    # **`record`／`read` 是蒐集資料之動詞，不是驗證之動詞** ——
    # `Read the radio power state` 讀了而未言「讀到什麼才算通過」，
    # 其含 `read` 故原判準放行。batch 3 之五條即以此通過（31 包 §2.1 實測）。
    # 裸 `compare` 同病：`Compare the values` 未言與何者比。
    #
    # 強化後之判準：**須有明言其判準之驗證子句**——
    #   `check/confirm/verify that …`／`to verify|check|confirm`／
    #   `compare … with|against|to …`（**兩個運算元皆具名**者方算）。
    #
    # **`Compare` 之處置（R-PMH116 明令具名）**：判**通過**，其理由為
    # `Compare the recorded duration with the stated maximum` **具名了兩造**
    # （`the recorded duration` vs `the stated maximum`），其 pass/fail 判準因而確定；
    # 裸 `Compare the values` 不具名兩造，**不通過**。**該理由一體適用於各批。**
    VERIFY = (r"\b(check|checks|confirm|confirms|verify|verifies)\s+that\b"
              r"|\bto\s+(verify|check|confirm)\b"
              r"|\bcompare[sd]?\b[^.]*\b(with|against|to)\b")
    bad = [t["tc_id"] for t in tcs
           if not re.search(VERIFY,
                            [x for x in t["test_procedure"].split("\n") if x.strip()][-1],
                            re.I)]
    chk("canon §5.2B/§5.5 Final Step 含驗證意圖", not bad, str(bad), canon="5.5")

    # C4 §4.3.1 —— test_item 上半須為 source_clause 之子字串（正規化後）
    def nz(s):
        s = str(s)
        for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
                     ("…", "..."), ("–", "-"), ("—", "-")):
            s = s.replace(a, b)
        # 30 包：`[CRnnnnn]` 為**變更請求標記**而非行為內容，且 canon §11 禁止
        # 方括號出現於交付欄位 —— `test_item` 因而去之，`source_clause` 保留。
        # **本檢查於兩側同時去之**，使二者仍可比對（A-PMH26）。
        s = re.sub(r"\s*\[CR\d+\]", "", s)
        return re.sub(r"\s+", " ", s).strip()
    bad = []
    for t in tcs:
        top = nz(t["test_item"].split("\n\n(")[0])
        if top and top not in nz(t.get("source_clause", "")):
            bad.append(t["tc_id"])
    chk("canon §4.3.1 test_item 上半 ⊆ source_clause（verbatim）", not bad,
        str(bad), canon="4.3.1")

    # C5 交付欄位無 markdown 標記
    DELIV = ["test_item", "pre_conditions", "test_procedure", "expected_result",
             "specification_reference", "remarks"]
    bad = [(t["tc_id"], f) for t in tcs for f in DELIV
           if re.search(r"\*\*|__|`", str(t.get(f, "")))]
    chk("交付欄位無 markdown 標記（**／__／`）", not bad, str(bad[:4]))

    # C6 §11 —— 直雙引號、無彎引號；UI 標籤須加引號
    bad = [(t["tc_id"], f) for t in tcs for f in DELIV
           if re.search(r"[“”‘’]", str(t.get(f, "")))]
    chk("canon §11 無彎引號", not bad, str(bad[:4]), canon="11")
    UI = r"\bthe (Accept|Loading) (button|indicator)\b"
    bad = [t["tc_id"] for t in tcs for f in DELIV
           if re.search(UI, str(t.get(f, "")))]
    chk("canon §11 UI 標籤加直雙引號", not bad, str(sorted(set(bad))), canon="11")

    # C8 §5.2 —— 步驟字數上限（14 包 §5.1）
    #   normal step <= 12 words；**final step <= 18 words**（其得延長以承載
    #   action ＋ check target）。字數以空白切分計，去除行首之編號。
    bad = []
    for t_ in tcs:
        steps = [x for x in t_["test_procedure"].split("\n") if x.strip()]
        for i, ln in enumerate(steps):
            body = re.sub(r"^\s*\d+[.)]\s*", "", ln)
            n_w = len(body.split())
            cap = 18 if i == len(steps) - 1 else 12
            if n_w > cap:
                bad.append((t_["tc_id"], f"step {i+1}", n_w, f"<= {cap}"))
    chk("canon §5.2 步驟字數（normal <=12／final <=18）", not bad, canon="5.2", detail=
        f"{len(bad)} 處 " + str(bad[:4]))

    # C7 R-PMH53 —— 批內交叉引用：存在性 ＋ **語意相容**
    #
    # 語意相容之機械近似：被引用者之 `distinguishing_axis` 須與**引用者自身之
    # axis** 至少共用一個實詞（長度 >= 2 之 CJK 詞或英文字）。
    # `-005`（配備：未配備 lower comfort screen）引 `-004`（變體：Maserati（無逾時））
    # 二者零共用 → FAIL。**無法機械判定者於下方逐處列出供人讀**（R-PMH53 末段）。
    by_suffix = {t["tc_id"][-3:]: t for t in tcs}

    def toks(s):
        s = str(s)
        return {w for w in re.findall(r"[\u4e00-\u9fff]{2,}|[A-Za-z]{3,}", s)}

    bad, refs = [], []
    for t in tcs:
        for f in ("test_item", "reasoning", "distinguishing_axis"):
            for m in re.finditer(r"`-(\d{3})`", str(t.get(f, ""))):
                sfx = m.group(1)
                refs.append((t["tc_id"], f, m.group(0)))
                tgt = by_suffix.get(sfx)
                if tgt is None:
                    bad.append((t["tc_id"], f, m.group(0), "不存在"))
                    continue
                shared = toks(t.get("distinguishing_axis", "")) & \
                    toks(tgt.get("distinguishing_axis", ""))
                if not shared:
                    bad.append((t["tc_id"], f, m.group(0),
                                f"axis 零共用：{t.get('distinguishing_axis','')!r}"
                                f" vs {tgt.get('distinguishing_axis','')!r}"))
    chk("R-PMH53 交叉引用存在且語意相容", not bad,
        f"{len(bad)} 處 " + str([(a, c, d[:40]) for a, _, c, d in bad[:3]]))
    if refs:
        print(f"  （R-PMH53 末段：本批交叉引用 {len(refs)} 處，逐處列出供人讀）")
        for a, f, r in refs:
            print(f"      {a} .{f} → {r}")

    # --- R-PMH99(c)（26 包）：`-007` 之七項事件層限定，其字串須各出現一次 ---
    # R-PMH87／R-PMH94 之七項限定得合併於同一步驟（每步至多兩項，R-PMH99(a)），
    # **惟合併使「某項被忽略」與「某項被刪去」在文本上難以分辨** ——
    # 故逐項驗其字串於 procedure 中**恰出現一次**（0 次或 >= 2 次皆 FAIL）。
    # 29 包步驟 4（R-PMH107(b)）：期望值由**寫死之 `-007` ＋ 七項**改為
    # **讀該批之 `limits` 宣告** —— 一般化，非新增檢查項；檢查項數不變。
    limits = batch_limits(d)
    bad = []
    for t in tcs:
        for tok in limits.get(t["tc_id"], []):
            n = t["test_procedure"].count(tok)
            if n != 1:
                bad.append((t["tc_id"], tok, n))
    n_tok = sum(len(v) for v in limits.values())
    chk(f"R-PMH99(c) 本批之限定字串各出現一次（{len(limits)} 條／{n_tok} 項）",
        not bad, str(bad))

    # --- R-PMH99(a)（27 包步驟 5）：每一 procedure 步驟所含之限定項數 <= 2 ---
    # 26 §12 第 4 項自陳：lint 只驗字串各出現一次，**不驗每步幾項**；
    # 「每步至多兩項」為執行層自行計數之陳述。本檢查使其成為機器判定。
    bad = []
    for t in tcs:
        toks = limits.get(t["tc_id"], [])
        for i, step in enumerate(
                [x for x in t["test_procedure"].split("\n") if x.strip()], 1):
            k = sum(1 for tok in toks if tok in step)
            if k > 2:
                bad.append((t["tc_id"], f"step {i}", k))
    chk(f"R-PMH99(a) 本批每步之限定項數 <= 2（{len(limits)} 條）", not bad, str(bad))

    # --- 15 包步驟 6：procedure 與 ER 之**編號**逐條對齊（人讀覆核之前置）---
    # 只驗機械可查者：編號自 1 起連號、且兩側逐位相同。
    # **「一步一意圖」與「ER 是否真對應該步」不可機械判定** —— 屬人讀。
    bad = []
    for t in tcs:
        def nums(field):
            return [x.split(".", 1)[0].strip()
                    for x in t[field].split("\n") if x.strip()]
        pn, en = nums("test_procedure"), nums("expected_result")
        want = [str(i) for i in range(1, len(pn) + 1)]
        if pn != want or en != want:
            bad.append((t["tc_id"], pn, en))
    chk("procedure／ER 編號自 1 起連號且逐位對齊", not bad, str(bad[:3]))

    # --- tc_id 唯一且連號 ---
    ids = [t["tc_id"] for t in tcs]
    chk("tc_id 唯一", len(set(ids)) == len(ids))
    chk("tc_id_status = provisional", d.get("tc_id_status") == "provisional")

    # --- leaf 覆蓋：本批 leaf 須等於該批所宣告之 `leaf_scope` ---
    # **28 包：由 batch-01 專屬之硬編碼改為讀該批之 `leaf_scope`**（R-PMH104：
    # **一般化既有檢查，非新增檢查**）。batch 1 之 `leaf_scope` 即其原 7 leaf。
    got = {t["leaf_id"] for t in tcs}
    scope = set(d.get("leaf_scope") or [])
    chk("本批 leaf == 其宣告之 leaf_scope（且 leaf_scope 非空）",
        bool(scope) and got == scope,
        f"leaf_scope {'未宣告' if not scope else ''} 多 {sorted(got-scope)} 少 {sorted(scope-got)}")

    w = max(len(n) for n, _, _ in checks)
    for n, ok, det in checks:
        print(f"  {n:<{w}}  {'PASS' if ok else '**FAIL**'}"
              + (f"  {det}" if not ok and det else ""))
    print(f"\n{len(checks)-len(fails)}/{len(checks)} PASS"
          + (f"；FAIL：{fails}" if fails else ""))
    print("\n⚠ **本 lint 未涵蓋之 canon 節號（R-PMH52／R-PMH56）**：")
    print("    由 `scripts/canon_coverage.py` 自 canon 之節號全集減去上方 "
          "`COVERED` 產生，**不手寫**。")
    print("    執行：`python scripts/canon_coverage.py`")
    print(f"    本 lint 宣告涵蓋 {len(COVERED)} 節：{sorted(COVERED)}")
    drift = (COVERED - executed, executed - COVERED)
    if any(drift):
        print(f"    ⚠ **R-PMH58 靜態／執行期不一致**："
              f"宣告未執行 {sorted(drift[0])}；執行未宣告 {sorted(drift[1])}")
    else:
        print("    （R-PMH58：靜態彙集與本次實際執行到之檢查點一致）")
    print("    **以上以外之全部 canon 節皆未由本 lint 檢查，須人讀。**")
    print("    R-PMH52：lint 全綠不得作為 TC 可用之證據。")
    print("\n⚠ R-PMH50 之限度：本 lint 只驗 source_clause **存在且取自 PDF**。"
          "\n  **「是否忠於規格」不可機械檢查** —— 須人讀 PDF 原文與 TC 對照。"
          "\n  本檢查只保證覆核所需之材料存在，不保證覆核已做。")
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
