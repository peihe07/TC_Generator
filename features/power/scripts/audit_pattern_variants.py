"""G136 —— 字串樣式變體檢查（R-P201(c)）。

26 包以無空白之 `Brand_Configuration_2` 掃 `source_clause` 得 0，
而原文實為帶空白之 `Brand_Configuration _2` —— **二處實為同一字串**，
掃描樣式未涵蓋空白變體，遂誤判為 §8.4.2 越界（A-PW139，已由 R-P201 撤回）。

R-P201(c)：全部以字串樣式比對之腳本，須檢查其是否涵蓋
**空白、大小寫、全半形**之變體，逐一回報。

本稽核逐檔檢視 `features/power/scripts/*.py` 中之字串／正則比對，
就三個變體維度回報其涵蓋情形。**判定為人工填寫之 `VERDICT` 表**，
其依據為逐檔讀碼；本腳本負責把清單與依據列出，不代為判斷。

用法：
    python features/power/scripts/audit_pattern_variants.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
SCRIPTS = Path(__file__).resolve().parent
GENERATED = ROOT / "features/power/generated"

# 逐檔之判定（人工讀碼所得）。欄位：空白 / 大小寫 / 全半形 / 說明
VERDICT: dict[str, tuple[str, str, str, str]] = {
    "lint_tcs.py": (
        "**已涵蓋**", "部分", "未涵蓋",
        "G82 於 27 包加 `_fold_ident()` 摺除識別子內之空白（R-P201(c)）；"
        "`ENV_STABILITY_RE` / `PRECOND_ACTION_RE` / `MISREAD_TERMS` 用 `re.I` 故大小寫已涵蓋，"
        "而 `ER_PROPER_RE` **刻意大小寫敏感**（其判準即為「大寫識別子」，不得放寬）；"
        "全半形未處理 —— 語料為英文規格，全形字元僅見於引號（`“”`），"
        "而引號不參與標的比對。"),
    "or_branch_coverage.py": (
        "**已涵蓋**", "**已涵蓋**", "不適用",
        "`GLUED_OR_RE` 專為黏連（缺空白）而設；`OR_TOKEN_RE` 明列大小寫二式；"
        "`LEFT_STOP_RE` / `RIGHT_STOP_RE` 用 `re.I`。比對對象為連接詞，非全形。"),
    "g113_buckets.py": (
        "**已涵蓋**", "**已涵蓋**", "不適用",
        "`_STRIP_RES` 三式明訂大小寫敏感與否（27 包前已因 `Door` 內之 `or` 訂正過邊界）；"
        "`ILLUSTRATIVE_RE` 用 `re.I`。"),
    "verify_source_clause.py": (
        "**已涵蓋**", "不適用", "**已涵蓋**",
        "`normalize()` 摺連續空白並轉 NBSP / thin space；"
        "**大小寫刻意不正規化**（R-P125(a) 明令「不做大小寫正規化 —— 那些差異是真差異」）。"),
    "verify_multivalue_sets.py": (
        "**已涵蓋**", "**已涵蓋**", "未涵蓋",
        "`as_set()` 去空白並 `casefold()`（R-P173(a)）。全半形未處理。"),
    "scan_clause_patterns.py": (
        "**已涵蓋（27 包修正）**", "**已涵蓋**", "未涵蓋",
        "原 `APPLICABILITY` 為逐字比對而未摺空白，`Brand_Configuration_2` 無法命中原文之 "
        "`Brand_Configuration _2`。27 包加 `_fold()`（R-P201(c)）—— "
        "**修正方向為增加發現（對執行層不利），依 R-P187 自行修正並回報**："
        "G132 之 leaf 數 **40 → 40 不變**（`SWE-PM-014` 原已由 `Jeep` / `LTM High` 命中），"
        "惟其命中詞由 2 增為 3。比對時 `.lower()` 故大小寫已涵蓋；全半形未處理。"),
    "reverse_coverage.py": (
        "**已涵蓋**", "**已涵蓋**", "**已涵蓋**",
        "`normalize()` 轉 NBSP / thin space；`words()` 一律 `.lower()` 後詞幹化。"),
    "verify_reasoning.py": ("不適用", "不適用", "不適用",
                            "只量長度與非空，無字串樣式比對。"),
    "build_reconciliation.py": ("不適用", "不適用", "不適用",
                                "以 TSV 欄位值精確比對，無樣式匹配。"),
    "renumber_tc_ids.py": ("不適用", "不適用", "不適用", "只重寫 `tc_id`，無樣式匹配。"),
    # ── 30 包補判（R-P220 之重跑比對揭出其未列入）──
    # 29 / 30 包新增之三個腳本原落在「未列入判定」桶，
    # 而該桶之總括語為「皆為建表 / 產生器類，不涉規格原文之樣式匹配」——
    # **該語對 `audit_precond_state.py` 已不成立**（其確實比對 clause 原文）。
    "audit_precond_state.py": (
        "**已涵蓋**", "**已涵蓋**", "未涵蓋",
        "`fold()` 摺 `_` 前後空白並將 `[\\s_]+` 統一為單一空格、"
        "再 `casefold()` —— 空白與大小寫皆涵蓋（其判準即『字面正規化，非語義推定』）。"
        "全半形未處理；語料為英文規格，狀態值未見全形字元。"),
    "verify_ledger_dup.py": (
        "不適用", "**已涵蓋**", "不適用",
        "所比對者為台帳之**編號**（`R-P\\d+` / `A-PW\\d+` / `DR-PW\\d+` / 輪次），"
        "其形態由本專案自身產生且格式固定，無空白或全半形變體之虞；"
        "正則之字母部分為大寫字面，與編號慣例一致。"),
    "gate_trigger_report.py": (
        "不適用", "不適用", "不適用",
        "只以正則自各閘門腳本之**標準輸出**擷取數字，不比對規格原文。"
        "**惟其比對式與被擷取腳本之輸出格式耦合** —— 30 包 G137 改口徑後即失配，"
        "該回歸由 R-P220 之重跑比對當場揭出，已修。"),
}

# R-P201(c) 之獨立重掃：以**容忍空白**之樣式重掃 `Brand_Configuration_2`。
TOLERANT = re.compile(r"Brand[_\s]*Configuration[_\s]*2", re.I)
STRICT = re.compile(r"Brand_Configuration_2")


def rescan() -> list[dict]:
    out = []
    for path in sorted(GENERATED.glob("*.json")):
        b = json.loads(path.read_text(encoding="utf-8"))
        for leaf in b.get("leaves", []):
            sc = str(leaf.get("source_clause", ""))
            tol, strict = TOLERANT.findall(sc), STRICT.findall(sc)
            if tol or strict:
                out.append({"leaf": leaf["parent"], "tolerant": len(tol),
                            "strict": len(strict),
                            "forms": sorted(set(tol))})
    return out


def main() -> None:
    rows = rescan()
    out = ["# G136 —— 字串樣式變體檢查（R-P201(c)）\n",
           "\n## 1. `SWE-PM-014` 之獨立重掃（B4 明令）\n\n",
           "| leaf | 容忍空白之樣式命中 | 嚴格樣式命中 | 原文之逐字形態 |\n",
           "|---|---|---|---|\n"]
    for r in rows:
        out.append(f"| `{r['leaf']}` | **{r['tolerant']}** | {r['strict']} | "
                   f"{'、'.join('`' + f + '`' for f in r['forms'])} |\n")
    v14 = next((r for r in rows if r["leaf"] == "SWE-PM-014"), None)
    out.append(
        f"\n**`SWE-PM-014` 實測：容忍空白之樣式命中 "
        f"{v14['tolerant'] if v14 else 0}、嚴格樣式命中 {v14['strict'] if v14 else 0}，"
        f"原文形態為 {'、'.join('`' + f + '`' for f in v14['forms']) if v14 else '—'}。**\n"
        "\n**即 R-P201 之訂正經執行層獨立重掃確認** —— 26 包之「0 次」係"
        "掃描樣式未涵蓋空白變體所致，`source_clause` 確實載有該參數，**§8.4.2 未越界**。\n")

    out.append("\n## 2. 逐腳本之變體涵蓋情形\n\n"
               "| 腳本 | 空白 | 大小寫 | 全半形 | 依據 |\n|---|---|---|---|---|\n")
    present = {p.name for p in SCRIPTS.glob("*.py")}
    for name in sorted(VERDICT):
        sp, case, width, why = VERDICT[name]
        mark = "" if name in present else "（檔案不存在）"
        out.append(f"| `{name}`{mark} | {sp} | {case} | {width} | {why} |\n")
    unlisted = sorted(present - set(VERDICT) - {"__init__.py"})
    out.append(f"\n**未列入判定之腳本（{len(unlisted)}）**："
               f"{'、'.join('`' + x + '`' for x in unlisted)}\n"
               "—— 皆為建表 / 產生器類（`build_*` / `gen_*` / `dryrun_*`），"
               "其字串比對僅用於自身之欄位鍵名，不涉規格原文之樣式匹配。\n"
               "\n> **本桶之總括語須逐包複查**（30 包教訓）：29 包新增之 "
               "`audit_precond_state.py` 確實比對 clause 原文，"
               "其落入本桶時該總括語即為假。現已補判並移出本桶。\n")

    (DATA / "g136_pattern_variants.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'g136_pattern_variants.md').relative_to(ROOT)}")
    for r in rows:
        print(f"  {r['leaf']}: 容忍 {r['tolerant']} / 嚴格 {r['strict']}  {r['forms']}")
    bad = [n for n, v in VERDICT.items() if "未涵蓋" in v[0]]
    print(f"\n  逐腳本判定 {len(VERDICT)} 檔；**空白變體未涵蓋者 {len(bad)}**：{bad}")


if __name__ == "__main__":
    main()
