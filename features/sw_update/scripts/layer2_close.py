#!/usr/bin/env python3
"""T29a —— Layer 2 之三重閉合驗證（下放包 16 §六，R-SU10 v2）。

(i) 列數閉合 (ii) 群數閉合 (iii) 列 id 集合閉合（聯集 = 311 且兩兩不相交）。
**不符即停並非零碼退出**（沿 anchor_table.py 之自檢慣例）。

Usage: python3 scripts/layer2_close.py
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from framework_survey import (a03_rows, group_by_heading, C_ID, C_CAT,   # noqa: E402
                              C_SUB, C_TITLE, IN_SCOPE)

H = lambda s: f"SWE1-FOTA-{s}"
R = lambda a, b=None: ("R", a, b if b is not None else a)   # 037 列區間（含端點）

# 下放包 16 §4.1 之 21 組。元素為 Heading id（整群）或 R(lo, hi)（037 列區間）。
SETS = [
    ("Wi-Fi Download",         ["038", "055", "058"]),
    ("Update Policy",          ["009", "024"]),
    ("Silent Update",          ["178", R(175, 177)]),
    ("Deployment Flow",        ["137"]),
    ("Session Flows",          ["016", "017", "018", "168", "185", "188", "271", "278", "287"]),
    ("Client Architecture",    ["072", "073", "192", "200", "202", "251", "259", "263",
                                "266", "280", "285"]),
    ("Bearer Selection",       ["291"]),
    ("ROV Installation",       ["085", "086", "091", "096"]),
    ("TBM Reflash",            ["110"]),
    ("HU FOTA via TBM",        ["214"]),
    ("USB Update",             ["020", "074", "076", "078"]),
    ("Update HMI",             ["129"]),
    ("Configurable Parameters", ["125", "127"]),
    ("FOTA Overview",          ["001"]),
    ("Integrity Verification", ["022", R(171, 174), R(310, 312), R(338)]),
    ("Interruption Handling",  [R(313), R(315, 329), R(357), R(360)]),
    ("Status Reporting",       [R(330, 334), R(339), R(358)]),
    ("Deployment Conditions",  [R(336, 337), R(340, 341), R(343, 346)]),
    ("Session Management",     [R(347, 356), R(359), R(361), R(368, 369)]),
    ("Telematics Client",      [R(363, 367)]),
    ("Update Agent",           [R(370, 383)]),
]
WANT_ROWS, WANT_GROUPS = 311, 45


def main():
    rows = a03_rows()
    groups = group_by_heading(rows)[1:]                      # 45 群（去前言偽節）
    gmap = {g["id"]: g for g in groups}
    num = lambda r: int(re.search(r"(\d+)$", str(r[C_ID])).group(1))
    inscope = {num(r): r for r in rows if r[C_CAT] in IN_SCOPE}
    head_of = {}                                             # 037 列號 → 其 Heading id
    for g in groups:
        for r in g["rows"]:
            head_of[num(r)] = g["id"]

    resolved, ok = [], True
    for name, items in SETS:
        ids, heads = set(), set()
        for it in items:
            if isinstance(it, str):
                g = gmap[H(it)]
                heads.add(H(it))
                ids |= {num(r) for r in g["rows"]}
            else:
                _, lo, hi = it
                seg = {n for n in inscope if lo <= n <= hi}
                ids |= seg
                heads |= {head_of[n] for n in seg}
        resolved.append((name, ids, heads, items))

    print("## T29a —— Layer 2 之三重閉合驗證（R-SU10 v2）\n")
    print("> 依 R-SU10 v2：(i) 列數、(ii) 群數、(iii) 列 id 集合，**三者缺一不可**。\n")

    # ── (i) 列數閉合
    print("### (i) 列數閉合\n")
    print("| # | Test Set | 所轄 (Heading id, 列區間) | 列數 | 下放包 16 §4.1 | |")
    print("|---:|---|---|---:|---:|:--:|")
    DECL = [29, 17, 9, 26, 16, 35, 16, 20, 14, 36, 5, 6, 2, 6, 8, 18, 7, 8, 14, 5, 14]
    tot = 0
    for i, ((name, ids, heads, items), want) in enumerate(zip(resolved, DECL), 1):
        tot += len(ids)
        good = len(ids) == want
        ok &= good
        spec = "、".join(it if isinstance(it, str)
                         else (f"`{it[1]}`" if it[1] == it[2] else f"`{it[1]}`–`{it[2]}`")
                         for it in items)
        print(f"| {i} | `{name}` | {spec} | **{len(ids)}** | {want} | {'✅' if good else '❌'} |")
    print(f"| | **合計** | | **{tot}** | {WANT_ROWS} | {'✅' if tot == WANT_ROWS else '❌'} |")
    ok &= tot == WANT_ROWS

    # ── (ii) 群數閉合
    allh = set().union(*(h for _, _, h, _ in resolved))
    miss_h = {g["id"] for g in groups} - allh
    extra_h = allh - {g["id"] for g in groups}
    print(f"\n### (ii) 群數閉合\n")
    print(f"- 21 組所涵蓋之 Heading id 聯集：**{len(allh)}**（應 {WANT_GROUPS}）"
          f" —— {'✅' if len(allh) == WANT_GROUPS else '❌'}")
    print(f"- 45 群中未被任何組涵蓋者：**{len(miss_h)}**"
          + (f" —— {sorted(miss_h)}" if miss_h else " ✅"))
    print(f"- 組中出現而不存在於 45 群者：**{len(extra_h)}**"
          + (f" —— {sorted(extra_h)}" if extra_h else " ✅"))
    ok &= len(allh) == WANT_GROUPS and not miss_h and not extra_h

    # ── (iii) 列 id 集合閉合
    union = set().union(*(s for _, s, _, _ in resolved))
    body = set(inscope)
    print(f"\n### (iii) 列 id 集合閉合\n")
    print(f"- 聯集大小：**{len(union)}**（應 {WANT_ROWS}）"
          f" —— {'✅' if len(union) == WANT_ROWS else '❌'}")
    d1, d2 = sorted(body - union), sorted(union - body)
    print(f"- 母體有而 Layer 2 無（漏）：**{len(d1)}**"
          + (f" —— {['SWE1-FOTA-%03d' % n for n in d1]}" if d1 else " ✅"))
    print(f"- Layer 2 有而母體無（溢）：**{len(d2)}**"
          + (f" —— {['SWE1-FOTA-%03d' % n for n in d2]}" if d2 else " ✅"))
    inter = [(a, b, sorted(x & y)) for i, (a, x, *_) in enumerate(resolved)
             for b, y, *_ in resolved[i + 1:] if x & y]
    print(f"- 相交之組對：**{len(inter)}**"
          + ("".join(f"\n  - `{a}` ∩ `{b}` = {['SWE1-FOTA-%03d' % n for n in c]}"
                     for a, b, c in inter) if inter else " ✅"))
    ok &= len(union) == WANT_ROWS and not d1 and not d2 and not inter

    # ── 跨章群之內部分割（R-SU10 v2(a) 之 (Heading id, 列區間) 鍵）
    print(f"\n### 跨章群之內部分割（R-SU10 v2(a)）\n")
    print("| Heading 群 | 列數 | 分屬之 Test Set | 組數 | 各組列數和 | |")
    print("|---|---:|---|---:|---:|:--:|")
    for gid in (H("309"), H("170")):
        gids = {num(r) for r in gmap[gid]["rows"]}
        parts = [(name, len(ids & gids)) for name, ids, *_ in resolved if ids & gids]
        s = sum(n for _, n in parts)
        good = s == len(gids)
        ok &= good
        print(f"| `{gid}` | {len(gids)} | "
              + "、".join(f"`{n}`({c})" for n, c in parts)
              + f" | {len(parts)} | **{s}** | {'✅' if good else '❌'} |")

    print(f"\n---\n\n**三重閉合結果：{'全部通過 ✅' if ok else '**不通過 ❌**'}**")
    if not ok:
        sys.exit("T29a 三重閉合不通過，停（下放包 16 §六「不符即停並回報」）")
    return resolved, gmap, num


if __name__ == "__main__":
    main()
