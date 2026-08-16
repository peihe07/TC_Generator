#!/usr/bin/env python3
"""Reverse validation of the `equivalent_tc_pairs` invariant (handoff 60 §1.1).

The invariant is satisfied by the corpus the moment it is written, so "OK"
and "the predicate never ran" print identically. Both directions are
asserted here, against `sibling_candidates.check_equivalent_pairs` itself —
no re-typed copy.

Directions:

  1. the three real rows pass  <- and there ARE three, so the check is not
     vacuously scanning an empty column set
  2. a row whose tc_id now belongs to ANOTHER req_id is caught — this is the
     58 §2 failure replayed: both ids still exist, both parse, one lies
  3. a row citing a tc_id that no longer exists is caught (the withdrawal
     case)
  4. a non-empty column with no `req_id:tc_id` citation at all is caught —
     otherwise the old tc_id-only format would pass by being unreadable
  5. an empty column is silent

Usage:
    python3 features/comfort/scripts/verify_equiv_invariant.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sibling_candidates as S


def main() -> int:
    fails = []

    def check(ok, label, detail=""):
        print(f"  {'PASS' if ok else '**FAIL**'} — {label}"
              + (f": {detail}" if detail else ""))
        if not ok:
            fails.append(label)

    rows = S.load_table()
    filled = [r for r in rows if r.get("equivalent_tc_pairs")]
    check(len(filled) >= 3,
          "the column is non-empty on real rows, so the check is not vacuous",
          f"{len(filled)} row(s): "
          f"{[r['outline'] + '<->' + r['sibling_outline'] for r in filled]}")
    check(not S.check_equivalent_pairs(rows),
          "the live table satisfies the invariant")

    sample = filled[0]
    req, tcid = S.EQUIV_CITE.findall(sample["equivalent_tc_pairs"])[0]

    # --- 2. the tc_id now belongs to a different req_id (a SHIFT)
    moved = dict(sample)
    other = "999-99"
    moved["equivalent_tc_pairs"] = sample["equivalent_tc_pairs"].replace(
        f"{req}:{tcid}", f"{other}:{tcid}", 1)
    out = S.check_equivalent_pairs([moved])
    check(out and "now belongs to" in out[0],
          "a citation whose tc_id moved to another req_id FIRES",
          out[0] if out else "silent")

    # --- 3. the tc_id no longer exists at all (a WITHDRAWAL)
    gone = dict(sample)
    gone["equivalent_tc_pairs"] = sample["equivalent_tc_pairs"].replace(
        tcid, "NR1L-ComfortHMI-999", 1)
    out = S.check_equivalent_pairs([gone])
    check(out and "no longer exists" in out[0],
          "a citation to a withdrawn tc_id FIRES",
          out[0] if out else "silent")

    # --- 4. the OLD format (tc_id only) must not pass as "nothing to check"
    old_format = dict(sample)
    old_format["equivalent_tc_pairs"] = (
        "NR1L-ComfortHMI-264↔NR1L-ComfortHMI-165")
    out = S.check_equivalent_pairs([old_format])
    check(out and "no `req_id:tc_id` citation" in out[0],
          "the pre-60 §1.1 format (tc_id only) FIRES rather than passing "
          "silently", out[0] if out else "silent")

    # --- 5. an empty column is not a complaint
    empty = dict(sample)
    empty["equivalent_tc_pairs"] = ""
    check(not S.check_equivalent_pairs([empty]),
          "an empty column stays silent")

    if fails:
        print(f"\n**{len(fails)} case(s) FAILED**")
        return 1
    print("\nall directional cases PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
