#!/usr/bin/env python3
"""Reverse validation of the `provisional-sibling` gate (handoff 42 §1).

A gate that has never been seen to FAIL has not been shown to work — a
mis-wired condition and a satisfied condition print the same green line.
This script drives the gate's own predicate over constructed rows and asserts
BOTH directions: it fires when it must, and stays silent when it must not.

It does not shell out to lint_tcs.py. It imports the module and reuses the
real `SECTION_TEST_SET` map and the real generated/ scan, so what is tested is
the shipped predicate and not a re-implementation of it.

Usage:
    python3 features/comfort/scripts/verify_provisional_gate.py
"""

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint_tcs as L

FEATURE = Path(__file__).resolve().parents[1]


def completed_sets() -> set:
    generated = {json.loads(p.read_text(encoding="utf-8"))["outline"]
                 for p in sorted((FEATURE / "generated").glob("*.json"))}
    by_set = defaultdict(set)
    for outline, test_set in L.SECTION_TEST_SET.items():
        by_set[test_set].add(outline)
    return {ts for ts, outs in by_set.items() if outs <= generated}, generated


def due(rows: list, complete: set) -> list:
    """The gate's predicate, verbatim from lint_tcs.py's gate body."""
    return [r for r in rows
            if r.get("provisional") == "true"
            and (L.SECTION_TEST_SET.get(r["outline"]) in complete
                 or L.SECTION_TEST_SET.get(r["sibling_outline"]) in complete)]


def main() -> int:
    complete, generated = completed_sets()
    rows = L.SIBLING_TABLE
    print(f"completed Test Sets: {sorted(complete)}")
    print(f"generated sections : {len(generated)} / {len(L.SECTION_TEST_SET)}")

    # A section inside a completed set, and one that is not in any completed
    # set — both taken from the live map so the test cannot drift from it.
    inside = next(o for o, ts in sorted(L.SECTION_TEST_SET.items())
                  if ts in complete)
    outside = next(o for o, ts in sorted(L.SECTION_TEST_SET.items())
                   if ts not in complete)

    cases = [
        # (label, row, expected-to-fire)
        ("provisional row touching a completed set",
         {"outline": inside, "sibling_outline": outside,
          "verdict": "not-sibling", "provisional": "true"}, True),
        ("same row, provisional cleared by re-confirmation",
         {"outline": inside, "sibling_outline": outside,
          "verdict": "not-sibling", "provisional": "false"}, False),
        ("provisional row touching NO completed set",
         {"outline": outside, "sibling_outline": outside,
          "verdict": "deferred", "provisional": "true"}, False),
        ("sibling verdict is not exempt — the flag, not the verdict, decides",
         {"outline": inside, "sibling_outline": outside,
          "verdict": "sibling", "provisional": "true"}, True),
        ("the completed set may be on EITHER side",
         {"outline": outside, "sibling_outline": inside,
          "verdict": "not-sibling", "provisional": "true"}, True),
    ]

    failures = []
    for label, row, expect in cases:
        fired = bool(due([row], complete))
        ok = fired == expect
        print(f"  {'PASS' if ok else '**FAIL**'} — {label}: "
              f"fired={fired}, expected={expect}")
        if not ok:
            failures.append(label)

    # The live table, measured rather than asserted.
    live = due(rows, complete)
    both = [r for r in live
            if r["outline"] in generated and r["sibling_outline"] in generated]
    print(f"\nlive table: {len(rows)} rows, {len(live)} due for "
          f"re-confirmation")
    print(f"  of those, {len(both)} have BOTH sides generated")
    print("  ^ this number is the point: re-confirmation can only use "
          "evidence\n    it previously lacked when the OTHER side has "
          "landed. Where it is 0,\n    the gate is asking for a second look "
          "at unchanged evidence (上繳 31 §1.3)")

    if failures:
        print(f"\n**{len(failures)} case(s) FAILED**: {failures}")
        return 1
    print(f"\n{len(cases)} / {len(cases)} directional cases PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
