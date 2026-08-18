"""G185 —— §12 全九列之條件欄與謂詞核對（R-P266）。

R-P259 查出第 8 列之謂詞取 **tie-break** 之措詞（`≥3 steps`）
而非該列**條件欄**（`≥3 features`）。本檔逐列核對其餘八列是否有同型錯誤。

**§12 之權威原文**（`docs/runtime/ASPICE_SWE6_AI_Instruction.md` §12，第 570–582 行）
逐字：

| Condition | Method |
|---|---|
| Invalid input / illegal op | Negative / Invalid |
| Simulated fault (disconnect, timeout) | Fault Injection |
| State A → State B transition | State Transition |
| Multiple conditions → outcome | Decision Table |
| Input partitioned valid / invalid | Equivalence Partitioning |
| Boundary (=limit, limit±1) | Boundary Value Analysis |
| Multi-parameter combination | Combinatorial |
| End-to-end flow, ≥3 features | Scenario / Use Case |
| Single feature check | Functional Based |

Tie-break: State Transition = state-change focus; Scenario = ≥3 steps crossing
features; Functional = 1–2 steps single feature.

**tie-break 僅三句**（第 3、8、9 列）；**其餘六列無 tie-break**，
故其謂詞不得引用任何 tie-break 措詞（R-P266）。

本檔**只核對不改謂詞** —— 不一致者逐列列出其差異，重判屬其後之處置。

用法：
    python features/power/scripts/audit_row_predicates.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
CANON = ROOT / "docs/runtime/ASPICE_SWE6_AI_Instruction.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))

# （列, 條件欄逐字, tie-break 逐字或 None, 現行謂詞所依之措詞, 是否一致, 說明）
ROWS: list[tuple[int, str, str | None, str, bool, str]] = [
    (1, "Invalid input / illegal op", None,
     "`ROW1_RE` = `attempt to|invalid|illegal|not allowed`", True,
     "`invalid` / `illegal` 直取條件欄之二詞；`attempt to` / `not allowed` "
     "為 `illegal op`（不被允許之操作）之語料措詞。**依條件欄，未引 tie-break。**"),
    (2, "Simulated fault (disconnect, timeout)", None,
     "`ROW2_RE` = `disconnect|inject(ed|ion)? (a )?fault|fault injection`", False,
     "**條件欄之括號明列二例：`disconnect`、`timeout`；現行謂詞只取 `disconnect`，"
     "`timeout` 未納入。** 另 `inject…fault` 為條件欄 `Simulated fault` 之語料措詞。"
     "A-PW178 已知其漏 `Stop the broadcast`；**本次另查出漏 `timeout`。**"),
    (3, "State A → State B transition",
     "State Transition = state-change focus",
     "`POSITIVE_RE` = `passes to|transitions? to|goes to|switches to|"
     "returns to … state|enters? …|leaves? …`", True,
     "皆為「A → B 之轉換」之正向措詞，依條件欄。tie-break（`state-change focus`）"
     "與條件欄同義，未造成分歧。"),
    (4, "Multiple conditions → outcome", None,
     "`substantive_conditions(pre) >= 2` —— **只數 `pre_conditions`**", False,
     "**條件欄未限定條件之所在欄位；現行代理判準只數 `pre_conditions`。** "
     "R-P267 已裁其系統性低估（`…-026` 之第二條件在 `test_procedure`）。"),
    (5, "Input partitioned valid / invalid", None,
     "`ROW5_RE` = `a value other than|other than \"|out of range`", True,
     "條件欄之 `valid` / `invalid` 二詞於語料實測皆為 **0**（36 包）；"
     "現行取語料中之等價切分措詞。**依條件欄之語義，未引 tie-break。**"),
    (6, "Boundary (=limit, limit±1)", None,
     "`ROW6_RE` = `after the date passes|boundary|the day before|limit(\\b|±)|"
     "greater than`", False,
     "**條件欄之 `limit±1` 為「界線值加減一」；現行之 `limit(\\b|±)` 會命中裸詞 "
     "`limit`（如 `the volume limit`）。** 37 包於 `rejudge_axis` 已因同一問題另立 "
     "`BOUNDARY_RE`，**而 `rejudge_design_method` 之 `ROW6_RE` 未同步訂正。**"),
    (7, "Multi-parameter combination", None,
     "**無謂詞**", True,
     "R-P249 已裁其為死列（first-match 序之結果）。無謂詞即無引用錯誤。"),
    (8, "End-to-end flow, ≥3 features",
     "Scenario = ≥3 steps crossing features",
     "`features_of(proc)` 之相異功能族數 ≥ 3", True,
     "**R-P259 已訂正** —— 舊謂詞取 tie-break 之 `≥3 steps`，現依條件欄之 `≥3 features`。"),
    (9, "Single feature check",
     "Functional = 1–2 steps single feature",
     "catch-all（第 1–8 列皆未命中）", False,
     "**條件欄為 `Single feature check`（實質判準）；現行為 catch-all（無判準）。** "
     "二者不同：catch-all 會收納「非單一功能而僅因前列謂詞不足而落底」者。"
     "**惟 R-P231(c) 明訂第 9 列為 catch-all** —— 此為既有裁決與條件欄之分歧，"
     "非謂詞取錯措詞，列出供分析層裁定。"),
]


def main() -> None:
    canon = CANON.read_text(encoding="utf-8")
    # 佐證：條件欄逐字確實見於權威原文
    verified = [(r[0], r[1], r[1] in canon) for r in ROWS]
    tb_ok = "Tie-break: State Transition = state-change focus; Scenario = ≥3 steps crossing" in canon

    bad = [r for r in ROWS if not r[4]]
    out = ["# G185 —— §12 全九列之條件欄與謂詞核對（R-P266）\n",
           "\n> 權威原文：`docs/runtime/ASPICE_SWE6_AI_Instruction.md` §12。\n",
           "> **本檔只核對，不改謂詞。**\n",
           f"\n## 一、條件欄逐字之佐證\n\n"
           f"九列之條件欄逐字**皆見於權威原文**："
           f"{sum(1 for _, _, ok in verified if ok)} / 9。\n"
           f"tie-break 句逐字可見：{'是' if tb_ok else '**否**'}"
           f"（僅三句，對應第 3、8、9 列）。\n",
           f"\n## 二、核對結果 —— **不一致 {len(bad)} / 9**\n\n"
           "| 列 | 條件欄逐字 | tie-break | 現行謂詞所依 | 一致 |\n|---|---|---|---|---|\n"]
    for row, cond, tb, pred, ok, why in ROWS:
        out.append(f"| {row} | `{cond}` | {'`' + tb + '`' if tb else '—'} | "
                   f"{pred} | {'是' if ok else '**否**'} |\n")
    out.append("\n## 三、逐列說明\n")
    for row, cond, tb, pred, ok, why in ROWS:
        out.append(f"\n### 第 {row} 列 —— {'一致' if ok else '**不一致**'}\n\n"
                   f"- **條件欄逐字**：`{cond}`\n"
                   f"- **tie-break**：{'`' + tb + '`' if tb else '**無**'}\n"
                   f"- **現行謂詞所依**：{pred}\n"
                   f"- {why}\n")

    p = DATA / "g185_row_predicate_audit.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"條件欄逐字見於權威原文：{sum(1 for _, _, ok in verified if ok)} / 9；"
          f"tie-break 句可見：{tb_ok}")
    print(f"**不一致 {len(bad)} / 9**：{[r[0] for r in bad]}")
    for row, cond, tb, pred, ok, why in bad:
        print(f"  第 {row} 列：{why[:96]}")


if __name__ == "__main__":
    main()
