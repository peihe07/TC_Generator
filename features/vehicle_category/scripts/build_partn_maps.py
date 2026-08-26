#!/usr/bin/env python3
"""T43 —— 產出 `data/layer3_map.tsv` 與 `data/test_set_map.tsv`。

分組取自 `partn.test_set()`（R-VC16 之規則），不硬編清單。
母體標註（R-VC15）：layer3_map 為 **117 leaf 母體**；
test_set_map 為 **66 section 母體**。
"""
from collections import Counter
from pathlib import Path

from partn import ORDER, load, outline_key

ROOT = Path(__file__).resolve().parents[1]
leaves, _ = load()

p1 = ROOT / "data" / "layer3_map.tsv"
with p1.open("w", encoding="utf-8") as f:
    f.write("req_id\tsection\ttest_set\n")
    for r in sorted(leaves, key=lambda x: (outline_key(x["section"]),
                                           x["req_id"])):
        f.write(f"{r['req_id']}\t{r['section']}\t{r['test_set']}\n")

by_sec = {}
for r in leaves:
    by_sec.setdefault(r["section"], []).append(r)
p2 = ROOT / "data" / "test_set_map.tsv"
with p2.open("w", encoding="utf-8") as f:
    f.write("section\ttest_set\tleaf_count\n")
    for s in sorted(by_sec, key=outline_key):
        f.write(f"{s}\t{by_sec[s][0]['test_set']}\t{len(by_sec[s])}\n")

print(f"{p1.relative_to(ROOT)}  {len(leaves)} 列（117 leaf 母體）")
print(f"{p2.relative_to(ROOT)}  {len(by_sec)} 列（66 section 母體）")
c = Counter(r["test_set"] for r in leaves)
for t in ORDER:
    n = sum(1 for s in by_sec if by_sec[s][0]["test_set"] == t)
    print(f"  {t:<24} {c[t]:>3} leaf / {n:>2} section")
