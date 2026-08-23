"""W-115(1)（64 包 §5）—— R-VS62 之真錨點。

先量 `$VC_VEH_LINE$` 於 237 leaf 之引用數與其值，再以**實際引用**之值分兩側：

  必命中   —— 引用 `DT`／`332`／`WS`／`HDCC` 者須判**已解**
  必不命中 —— 引用 `M182`／`M189`／`M240` 者須判**未解**
               **若該側於母體內為 0，具名「該側無標的」，不得記為通過**（R-VS54(2)）
"""
from __future__ import annotations

import collections
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from dr_conflict import conflict                       # noqa: E402
from inscope_w39 import blocks_with_sec                # noqa: E402
from writability_driver import clause_pairs, run       # noqa: E402

FEAT = Path(__file__).resolve().parents[1]
SOLVED = ("DT", "332", "WS", "HDCC")
OPEN = ("M182", "M189", "M240")


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    gen = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}
    grades, detail = run()

    refs, vals = collections.defaultdict(set), collections.Counter()
    for leaf in gen:
        for q in re.findall(r"\d{7}", (l2r.get(leaf, {}).get("reqid_list") or "")):
            blk = blocks.get(q)
            if not blk:
                continue
            for tok, vs in clause_pairs(blk["text"]).items():
                if tok != "VC_VEH_LINE":
                    continue
                for v in vs:
                    refs[leaf].add(v)
                    vals[v] += 1
    print(f"`$VC_VEH_LINE$` 於 237 leaf 之引用：**{len(refs)} leaf**，"
          f"相異值 **{len(vals)}**")
    for v, n in vals.most_common():
        print(f"    {v!r} ×{n}")
    print()

    for side, keys, want in (("必命中（須判已解）", SOLVED, True),
                             ("必不命中（須判未解）", OPEN, False)):
        hit = [l for l, vs in refs.items()
               if any(any(k in v for k in keys) for v in vs)]
        if not hit:
            print(f"錨點（{side}）標的 **0** —— "
                  f"**該側無標的，依 R-VS54(2) 不得記為通過**")
            continue
        bad = []
        for l in hit:
            blocked = any(conflict("VC_VEH_LINE", v) for v in refs[l])
            if blocked == want:      # want=True 表示應已解（不該被攔）
                bad.append((l, sorted(refs[l]), grades.get(l)))
        print(f"錨點（{side}）標的 {len(hit)} —— 不符 {len(bad)}   "
              f"{'PASS' if not bad else '⚠ 未命中'}")
        for l, vs, g in bad[:6]:
            print(f"    {l}  {vs}  W={g}")


if __name__ == "__main__":
    main()
