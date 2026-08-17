"""G28 — `Verification Criteria` / `Verification Method` 可執行性量測（R-P49）。

06 §D 之 G28 判準（分析層自裁）：

  可執行  —— 含至少一個具體可操作之條件或動作
              （具名訊號、具名 UI 元件、具體數值、具名工具指令）
  不可執行 —— 僅含泛稱環境陳述而無任何具體條件
              （例：「Vehicle equiped with CAN」）
  空      —— 不適用（G19 已證零空值）

本閘不設期望值，**首次量測即為基線**。

判定分三層：VC 單欄、VM 單欄、二欄合觀（pair）。
Phase 4 之直接輸入為二欄合觀 —— 一欄泛稱而另一欄具體者仍可執行。

具體性訊號為明列之正則（見 SIGNALS），逐 leaf 記錄命中之訊號名稱與依據字串。
邊界個案以 OVERRIDES 人工覆寫（隨腳本版控，附理由），腳本不自行判斷。

用法：
    python features/power/scripts/build_vcvm.py
"""

from __future__ import annotations

import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
DATA = ROOT / "features/power/data"

# 純領域縮寫 —— 命名了一個域或總線，但未陳述任何可設定之條件。
# 依 G28 判準，「Vehicle equiped with CAN」為不可執行之反例，故此類不得單獨成為訊號。
DOMAIN_ONLY_ACRONYMS = {"CAN", "SW", "HW", "UI", "EE", "OEM"}

# 具體性訊號 —— 明列，可逐條檢驗。
# 07 包 B4 依 037 之 VC/VM 全欄 token 形態分布重新推導（R-P57）：
#   全大寫 2–3 字 324、點號分隔 308、$SIGNAL$ 105、底線 72、全大寫 4+ 43、
#   CamelCase 18、字母尾接數字 15（Timeout1 13 / M240 3 / Case1-3）、
#   點號後接數字 1（CS.00244）
# 調校前之識別式漏掉最後三類，故 4 筆偽陰性。
SIGNALS: list[tuple[str, re.Pattern]] = [
    ("具名訊號／參數", re.compile(
        r"\$[A-Za-z_]+\$"                                  # $Telematic_Power$
        r"|\b[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+\b"      # SwitchOff_Timeout_Setting
        r"|\b[A-Za-z][A-Za-z0-9]*\.[A-Za-z0-9][A-Za-z0-9_.]*\b"  # STATUS_BH_BCM1.PowerModeSts / CS.00244
        r"|\b[A-Z]{4,}\b"                                  # PROXI
    )),
    ("具名參數（字母尾接數字）", re.compile(r"\b[A-Za-z]{3,}\d+\b")),  # Timeout1 / Case1 / M240
    ("具體數值", re.compile(r"\b\d+\s*(?:min|minutes|sec|seconds|s|ms|V|volts?|%)\b", re.I)),
    ("引號字面值", re.compile(r"[\"“”'][^\"“”']{2,}[\"“”']")),
    ("具名元件／畫面", re.compile(
        r"\b(?:button|screen|menu|display|icon|splash|panel"
        r"|HMI|HU|TLM|ICS|AMP|FPDM|DCSD|HIL|RVC|TBM|PDO|SOS)\b", re.I)),
    ("具名狀態", re.compile(
        r"\b(?:Ignition\s+(?:On|Off|Cranking|Pre[_\s-]?Start|Pre\s+Off)"
        r"|Full[-\s]?Operation|Partial\s+Operation|Standby|Sleep|Idle|Timed|Bench"
        r"|Logistic|suspend[-\s]?resume)\b", re.I)),
    ("操作動詞", re.compile(
        r"\b(?:press|change|set|select|switch|send|apply|trigger|navigate|enter|exit|reboot"
        r"|perform|observe|disconnect|log)\b", re.I)),
]

# 07 包 B4 調校後，**純正則結果與人工覆寫完全相同**，故 OVERRIDES 清空 ——
# 覆寫率由 5.2%（6/115）降為 **0%（0/115）**（R-P57 / G35）。
OVERRIDES: dict[tuple[str, str], tuple[str, str]] = {}

# 判讀紀錄（**不影響判定**，僅供覆核）：兩筆 VC 之不可執行判定，
# 調校後由 DOMAIN_ONLY_ACRONYMS 之排除規則自動得出，不再需要人工覆寫。
NOTES: dict[tuple[str, str], str] = {
    ("SWE-PM-007", "vc"): (
        "「Vehicle not equiped with CAN or engineering line is active」——"
        "`CAN` 為總線泛稱（DOMAIN_ONLY_ACRONYMS），"
        "「engineering line is active」亦無具名訊號或設定值。"
    ),
    ("SWE-PM-008", "vc"): (
        "「Vehicle equiped with CAN」—— **G28 判準所舉之反例本身**。"
    ),
}

# R-P55 回歸斷言（若 B4 改變基線，以新值為準）
EXPECTED_BAD_VC = 2
EXPECTED_BAD_VM = 0
EXPECTED_BAD_PAIR = 0


def find(pattern: str) -> Path:
    return next(f for f in IN.iterdir() if pattern in f.name)


def signals_of(text: str) -> list[tuple[str, str]]:
    """回傳 [(訊號名, 依據字串)]。純領域縮寫之單獨命中不計（見 DOMAIN_ONLY_ACRONYMS）。"""
    hits = []
    for name, rx in SIGNALS:
        for m in rx.finditer(text):
            if m.group(0).upper() in DOMAIN_ONLY_ACRONYMS:
                continue
            hits.append((name, m.group(0)))
            break
    return hits


def verdict(leaf: str, field: str, text: str) -> tuple[str, list[tuple[str, str]], str]:
    hits = signals_of(text)
    if (leaf, field) in OVERRIDES:
        v, reason = OVERRIDES[(leaf, field)]
        return v, hits, reason
    if not text.strip():
        return "空", [], "（G19 已證零空值，不應出現）"
    if hits:
        return "可執行", hits, ""
    return "不可執行", [], NOTES.get((leaf, field), "無任何具體性訊號命中")


def main() -> None:
    wb = openpyxl.load_workbook(find("FSM-037"), data_only=True, read_only=True)
    ws = wb["SWE1 Requirements"]
    rows = [
        (str(r[0]).strip(), str(r[16] or "").strip(), str(r[17] or "").strip())
        for r in ws.iter_rows(min_row=8, max_row=145, values_only=True)
        if r[0] and str(r[0]).strip()
    ]
    wb.close()

    test_set = {}
    for line in (DATA / "leaf_testset.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        if line.strip():
            leaf, ts, _ = line.split("\t")
            test_set[leaf] = ts

    results = []
    for leaf, vc, vm in rows:
        v_vc, h_vc, r_vc = verdict(leaf, "vc", vc)
        v_vm, h_vm, r_vm = verdict(leaf, "vm", vm)
        pair = "可執行" if "可執行" in (v_vc, v_vm) else "不可執行"
        results.append({
            "leaf": leaf, "vc": vc, "vm": vm,
            "v_vc": v_vc, "v_vm": v_vm, "pair": pair,
            "h_vc": h_vc, "h_vm": h_vm, "r_vc": r_vc, "r_vm": r_vm,
            "ts": test_set.get(leaf, "（未指派）"),
        })

    bad_vc = [r for r in results if r["v_vc"] == "不可執行"]
    bad_vm = [r for r in results if r["v_vm"] == "不可執行"]
    bad_pair = [r for r in results if r["pair"] == "不可執行"]

    out = [
        "# G28 — `Verification Criteria` / `Verification Method` 可執行性（R-P49）\n",
        "\n> 判準見 06 下放包 §D 之 G28。本閘**不設期望值，首次量測即為基線**。\n",
        "> 具體性訊號為明列正則（見 `scripts/build_vcvm.py` 之 `SIGNALS`）；\n",
        "> 邊界個案以 `OVERRIDES` 人工覆寫，隨腳本版控並附理由。\n",
        "> 產生指令：`python features/power/scripts/build_vcvm.py`\n",
        f"\n## 1. 基線\n\n| 判定層 | 可執行 | 不可執行 | 母體 |\n|---|---|---|---|\n",
        f"| `Verification Criteria` 單欄 | {len(rows) - len(bad_vc)} | **{len(bad_vc)}** | {len(rows)} |\n",
        f"| `Verification Method` 單欄 | {len(rows) - len(bad_vm)} | **{len(bad_vm)}** | {len(rows)} |\n",
        f"| **二欄合觀（Phase 4 之實際輸入）** | {len(rows) - len(bad_pair)} | **{len(bad_pair)}** | {len(rows)} |\n",
        "\n二欄合觀之判定規則：任一欄可執行即為可執行 —— "
        "一欄泛稱而另一欄具體者，TC 作者仍有可操作之依據。\n",
    ]

    for label, bad, field in [("Verification Criteria", bad_vc, "vc"),
                              ("Verification Method", bad_vm, "vm")]:
        out.append(f"\n## 2.{'1' if field == 'vc' else '2'} `{label}` 判定為不可執行者"
                   f"（{len(bad)} 個）\n\n")
        if not bad:
            out.append("（無）\n")
            continue
        out.append("| leaf | Test Set | 欄位全文 | 判定依據 |\n|---|---|---|---|\n")
        for r in bad:
            text = (r[field] or "（空）").replace("\n", " ／ ").replace("|", "\\|")
            reason = (r[f"r_{field}"] or "無任何具體性訊號命中").replace("|", "\\|")
            out.append(f"| `{r['leaf']}` | {r['ts']} | {text} | {reason} |\n")

    out.append(f"\n## 3. 二欄合觀為不可執行者（{len(bad_pair)} 個）\n\n")
    if not bad_pair:
        out.append("**（無）** —— 每個 leaf 至少有一欄含具體性訊號。\n")
    else:
        out.append("| leaf | Test Set | VC | VM |\n|---|---|---|---|\n")
        for r in bad_pair:
            out.append(f"| `{r['leaf']}` | {r['ts']} | {r['vc'][:70]} | {r['vm'][:70]} |\n")

    out.append("\n## 4. 逐 leaf 明細（依據字串）\n\n")
    out.append("| leaf | VC 判定 | VC 命中訊號（依據字串） | VM 判定 | VM 命中訊號（依據字串） |\n")
    out.append("|---|---|---|---|---|\n")
    for r in results:
        def fmt(hits):
            return "；".join(f"{n}=`{s[:24]}`" for n, s in hits) or "—"
        out.append(f"| `{r['leaf']}` | {r['v_vc']} | {fmt(r['h_vc'])} | "
                   f"{r['v_vm']} | {fmt(r['h_vm'])} |\n")

    path = DATA / "g28_vcvm_quality.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print(f"G28 基線：VC 不可執行 {len(bad_vc)} / {len(rows)}；"
          f"VM 不可執行 {len(bad_vm)} / {len(rows)}；"
          f"**二欄合觀不可執行 {len(bad_pair)} / {len(rows)}**")
    for r in bad_vc:
        print(f"  VC 不可執行 {r['leaf']} ({r['ts']}): {r['vc'][:60]!r}")
    for r in bad_vm:
        print(f"  VM 不可執行 {r['leaf']} ({r['ts']}): {r['vm'][:60]!r}")
    print(f"  人工覆寫率（R-P57 / G35）：{len(OVERRIDES)} / {len(rows)}"
          f" = {100 * len(OVERRIDES) / len(rows):.1f}%")

    # R-P55 回歸斷言
    problems = []
    for label, got, want in [("VC 不可執行", len(bad_vc), EXPECTED_BAD_VC),
                             ("VM 不可執行", len(bad_vm), EXPECTED_BAD_VM),
                             ("二欄合觀不可執行", len(bad_pair), EXPECTED_BAD_PAIR)]:
        if got != want:
            problems.append(f"{label} {got} ≠ 期望 {want}")
    if problems:
        print("\n**回歸斷言失敗（R-P55）**：" + "；".join(problems))
        raise SystemExit(1)
    print("回歸斷言（R-P55）：PASS")


if __name__ == "__main__":
    main()
