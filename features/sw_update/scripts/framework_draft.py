#!/usr/bin/env python3
"""T28 —— `309`／`170` 群列標題傾印、45 群 HMI/Service 對照（下放包 15 §五）。

**T28a／T28b 刻意只出三欄，不附分數、不附候選**（下放包 15 §五）：
附分數會使 Layer 2 之切分受路徑 A 影響，而 Layer 2 之切分依 R-SU18(b)
**不依賴逐列錨定**。

Usage: python3 scripts/framework_draft.py 28a 28b 28c
"""

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from framework_survey import (a03_rows, group_by_heading, C_ID, C_TITLE,   # noqa: E402
                              C_CAT, C_SUB, IN_SCOPE)

NUM = lambda r: int(re.search(r"(\d+)$", str(r[C_ID])).group(1))


def _dump(rows, lo, hi, head, title):
    sel = [r for r in rows if r[C_CAT] in IN_SCOPE and lo <= NUM(r) <= hi]
    print(f"## {title}\n")
    print(f"Heading 群 `{head}`｜所轄 in-scope 列 **{len(sel)}**｜"
          f"id 範圍 `{lo}`–`{hi}`\n")
    print("> **僅三欄**（下放包 15 §五）：不附分數、不附候選 —— "
          "Layer 2 之切分依 R-SU18(b) 不依賴逐列錨定。\n")
    print("| # | 037 列 | Requirement Title | Sub Cat |")
    print("|---:|---|---|---|")
    for n, r in enumerate(sel, 1):
        print(f"| {n} | `{str(r[C_ID]).strip()}` | {str(r[C_TITLE] or '').strip()} "
              f"| {r[C_SUB] or '**(blank)**'} |")
    c = Counter(r[C_SUB] or "(blank)" for r in sel)
    print(f"\n**小計 {len(sel)} 列** —— "
          + "／".join(f"{k} {v}" for k, v in sorted(c.items())))
    return sel


def t28a():
    return _dump(a03_rows(), 310, 383, "SWE1-FOTA-309",
                 "T28a —— `SWE1-FOTA-309` 群列標題傾印（70 列）")


def t28b():
    print()
    return _dump(a03_rows(), 171, 177, "SWE1-FOTA-170",
                 "T28b —— `SWE1-FOTA-170` 群列標題傾印（7 列）")


def t28c():
    rows = a03_rows()
    groups = group_by_heading(rows)
    print("\n## T28c —— 全 45 Heading 群之列數與 HMI／Service 對照\n")
    print("| # | Heading id | 標題原文 | 列數 | HMI | Service | blank | 逾 40 |")
    print("|---:|---|---|---:|---:|---:|---:|:--:|")
    tot = Counter()
    for i, g in enumerate(groups):
        if i == 0 and not g["rows"]:
            continue
        c = Counter(r[C_SUB] or "blank" for r in g["rows"])
        n = len(g["rows"])
        tot.update(c)
        tot["列"] += n
        gid = f"`{g['id']}`" if g["id"] else "—（前言偽節）"
        print(f"| {i} | {gid} | {g['title'][:44]} | {n} | {c['HMI']} | "
              f"{c['Service']} | {c['blank']} | {'⚠' if n > 40 else ''} |")
    print(f"| | **合計** | | **{tot['列']}** | **{tot['HMI']}** | "
          f"**{tot['Service']}** | **{tot['blank']}** | |")
    print(f"\n**閉合檢查**：{tot['HMI']} + {tot['Service']} + {tot['blank']} = "
          f"{tot['HMI']+tot['Service']+tot['blank']}；驗證母體（R-SU3）= 311"
          f" —— {'閉合 ✅' if tot['列'] == 311 else '**不閉合 ❌**'}\n")

    hmi = [g for g in groups if any(r[C_SUB] == "HMI" for r in g["rows"])]
    pure = [g for g in groups if g["rows"] and not any(r[C_SUB] == "HMI" for r in g["rows"])]
    big = [g for g in groups if len(g["rows"]) > 40]
    print("### §4.1 原則 3、4 之複核\n")
    print(f"- **原則 3（純 Service 群之健康判準）**：含 ≥1 個 HMI 列之群 "
          f"**{len(hmi)}** 群 —— 下放包 15 §4.1 稱「17 個含 HMI 列之群」，"
          f"{'**與實測一致**' if len(hmi) == 17 else f'**實測為 {len(hmi)}，與該數不符**'}。"
          f"純 Service 群 **{len(pure)}** 群；45 群中另有 "
          f"**{sum(1 for g in groups[1:] if not g['rows'])}** 群無 in-scope 列"
          f"（{len(hmi)} + {len(pure)} + {sum(1 for g in groups[1:] if not g['rows'])}"
          f" = {len(hmi)+len(pure)+sum(1 for g in groups[1:] if not g['rows'])}）")
    print(f"- **原則 4（逾 40 列者須檢視）**：逾 40 列之群 **{len(big)}** 群 —— "
          + ("；".join(f"`{g['id']}`（{len(g['rows'])} 列，{g['title'][:30]}）"
                      for g in big) if big else "無"))
    return groups


if __name__ == "__main__":
    want = set(sys.argv[1:]) or {"28a", "28b", "28c"}
    if "28a" in want:
        t28a()
    if "28b" in want:
        t28b()
    if "28c" in want:
        t28c()
