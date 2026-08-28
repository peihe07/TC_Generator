#!/usr/bin/env python3
"""T30a／T30b —— 孤島列之 Description 傾印、Priority／SubCat 空白之實測（下放包 17 §六）。

Usage: python3 scripts/islands.py 30a 30b
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from framework_survey import a03_rows, C_ID, C_TITLE, C_DESC, C_CAT, C_SUB, IN_SCOPE  # noqa: E402

C_PRIO = 15                       # `Priority` —— 037 表頭列 7 實測（T30b）

# §四 之 PROVISIONAL-ROW 五列
PROV = ["338", "357", "359", "360", "361"]
# §六 T30a 所令之比較基準列
BASE = {"312": "Integrity 之基準（GT 正解 `4907514`，章 4.8.3）",
        "321": "Interruption 之基準（近義標題群）",
        "325": "Interruption 之基準（近義標題群）",
        "323": "Concurrent NIA（`359` 之疑似同族）",
        "337": "Deployment Flow Initiation（`338` 之前鄰）"}
NUM = lambda r: int(re.search(r"(\d+)$", str(r[C_ID])).group(1))


def t30a():
    rows = {str(r[C_ID]).strip().rsplit("-", 1)[1]: r
            for r in a03_rows() if r[C_CAT] in IN_SCOPE}
    print("## T30a —— 孤島列與其比較基準列之 Description 全文（9 列）\n")
    print("> **僅全文**（下放包 17 §六）：不附分數、不附候選。"
          "**執行層不裁定其歸屬。**\n")

    print("### 甲 —— 五個 `PROVISIONAL-ROW`\n")
    for k in PROV:
        r = rows[k]
        print(f"\n---\n\n#### `SWE1-FOTA-{k}` — {str(r[C_TITLE] or '').strip()}\n")
        print(f"- 現置 Test Set：{_cur(k)}｜Sub Cat：{r[C_SUB] or '(blank)'}"
              f"｜Priority：{r[C_PRIO] or '**(blank)**'}")
        print("\n**Requirement Description 全文**：\n")
        print("> " + (_desc(r) or "(空)") + "\n")

    print("\n### 乙 —— 五個比較基準列\n")
    for k, why in BASE.items():
        r = rows[k]
        print(f"\n---\n\n#### `SWE1-FOTA-{k}` — {str(r[C_TITLE] or '').strip()}\n")
        print(f"- 用途：{why}｜現置 Test Set：{_cur(k)}"
              f"｜Sub Cat：{r[C_SUB] or '(blank)'}｜Priority：{r[C_PRIO] or '**(blank)**'}")
        print("\n**Requirement Description 全文**：\n")
        print("> " + (_desc(r) or "(空)") + "\n")


def _desc(r):
    return re.sub(r"\s+", " ", str(r[C_DESC] or "")).strip()


def _cur(k):
    from layer2_close import SETS, H
    from framework_survey import group_by_heading
    gmap = {g["id"]: g for g in group_by_heading(a03_rows())[1:]}
    n = int(k)
    for name, items in SETS:
        for it in items:
            if isinstance(it, str):
                if any(NUM(r) == n for r in gmap[H(it)]["rows"]):
                    return f"`{name}`"
            elif it[1] <= n <= it[2]:
                return f"`{name}`"
    return "—"


def t30b():
    rows = [r for r in a03_rows() if r[C_CAT] in IN_SCOPE]
    allr = a03_rows()
    print("\n## T30b —— 驗證母體 311 列中 Priority／Sub Cat 空白之實測\n")

    blank_p = [str(r[C_ID]).strip() for r in rows if r[C_PRIO] in (None, "")]
    blank_s = [str(r[C_ID]).strip() for r in rows if r[C_SUB] in (None, "")]
    from collections import Counter
    c = Counter(r[C_PRIO] or "(blank)" for r in rows)

    print("### Priority 之分布 —— 驗證母體 311 vs 全 383 資料列\n")
    call = Counter(r[C_PRIO] or "(blank)" for r in allr)
    print("| Priority | 驗證母體 311 | 全 383 資料列 | 差（= Heading 等非範圍列） |")
    print("|---|---:|---:|---:|")
    for k in ("High", "Medium", "Low", "(blank)"):
        print(f"| `{k}` | **{c[k]}** | {call[k]} | {call[k]-c[k]} |")
    print(f"| **合計** | **{sum(c.values())}** | {sum(call.values())} | "
          f"{sum(call.values())-sum(c.values())} |")
    print(f"\n> 上繳包 01 §之「空白 72」為**全 383 資料列**之數；"
          f"**驗證母體 311 列中之空白為 {c['(blank)']} 列**（R-SU22.3 所令之實測）。\n")

    print(f"### Priority 空白之列（{len(blank_p)}）\n")
    print("；".join(f"`{i}`" for i in blank_p) if blank_p else "**無**")

    print(f"\n\n### Sub Categorization 空白之列（{len(blank_s)}）\n")
    print("；".join(f"`{i}`" for i in blank_s) if blank_s else "**無**")

    both = sorted(set(blank_p) & set(blank_s))
    print(f"\n\n### 二者是否同列\n")
    print(f"- Priority 空白 ∩ SubCat 空白：**{len(both)}** —— "
          + ("；".join(f"`{i}`" for i in both) if both else "**空集**"))
    print(f"- 僅 Priority 空白：**{len(set(blank_p)-set(blank_s))}**")
    print(f"- 僅 SubCat 空白：**{len(set(blank_s)-set(blank_p))}** —— "
          + ("；".join(f"`{i}`" for i in sorted(set(blank_s)-set(blank_p))) or "—"))
    return blank_p, blank_s


if __name__ == "__main__":
    want = set(sys.argv[1:]) or {"30a", "30b"}
    if "30a" in want:
        t30a()
    if "30b" in want:
        t30b()
