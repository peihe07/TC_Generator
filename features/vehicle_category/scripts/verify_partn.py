#!/usr/bin/env python3
"""T44 —— framework Part N 之驗算（R-VC16）。

五個 assertion：
  (1) leaf 合計 == 117                       （117 leaf 母體）
  (2) section 合計 == 66                     （66 section 母體）
  (3) 各組之 leaf 數與 section 數與 R-VC16 之驗算目標逐組相符
  (4) 無 leaf 落於二組或零組
  (5) 各組之 `Sub Categorization` 為單一值

分組取自 `partn.test_set()`，即 **R-VC16 之規則**；
**不硬編 leaf 清單** —— 硬編會使驗算退化為抄寫其答案。

任一 assertion 失敗即以非零離開碼終止。只讀不寫。
"""
import sys
from collections import Counter, defaultdict

from partn import ORDER, TARGETS, load

leaves, rows = load()

by_ts = defaultdict(list)
sec_by_ts = defaultdict(set)
for r in leaves:
    by_ts[r["test_set"]].append(r["req_id"])
    sec_by_ts[r["test_set"]].add(r["section"])

results = []


def check(n, name, ok, detail):
    results.append((n, name, ok, detail))
    return ok


# (1)
n_leaf = len(leaves)
check(1, "leaf 合計 == 117（117 leaf 母體）", n_leaf == 117,
      f"measured {n_leaf}")

# (2)
n_sec = len({r["section"] for r in leaves})
check(2, "section 合計 == 66（66 section 母體）", n_sec == 66,
      f"measured {n_sec}")

# (3)
bad3 = []
for t in ORDER:
    el, es = TARGETS[t]
    ml, ms = len(by_ts[t]), len(sec_by_ts[t])
    if (ml, ms) != (el, es):
        bad3.append(f"{t}: expected {el} leaf/{es} section, "
                    f"measured {ml} leaf/{ms} section")
check(3, "各組 leaf 數與 section 數與 R-VC16 驗算目標逐組相符",
      not bad3, "; ".join(bad3) if bad3 else "8 組全部相符")

# (4)
allocated = [r for v in by_ts.values() for r in v]
dupes = [k for k, v in Counter(allocated).items() if v > 1]
missing = sorted({r["req_id"] for r in leaves} - set(allocated))
check(4, "無 leaf 落於二組或零組",
      not dupes and not missing,
      f"二組 {dupes or '無'} / 零組 {missing or '無'}")

# (5)
bad5 = []
for t in ORDER:
    vals = {r["sub_cat"] for r in leaves if r["test_set"] == t}
    if len(vals) != 1:
        bad5.append(f"{t}: {sorted(vals)}")
check(5, "各組 Sub Categorization 為單一值",
      not bad5,
      "; ".join(bad5) if bad5 else
      ", ".join(f"{t}={next(iter({r['sub_cat'] for r in leaves if r['test_set']==t}))}"
                for t in ORDER))

print("verify_partn — framework Part N（R-VC16）")
print(f"{'#':>2}  {'assertion':<48} 判")
print("-" * 78)
failed = 0
for n, name, ok, detail in results:
    if not ok:
        failed += 1
    print(f"{n:>2}  {name:<48} {'PASS' if ok else '**FAIL**'}")
    print(f"    {detail}")
print("-" * 78)
print(f"{len(results)} checked / {failed} failed")
sys.exit(1 if failed else 0)
