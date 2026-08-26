#!/usr/bin/env python3
"""R-AM21: cross-batch shared-anchor check, a delivery gate.

Build an anchor -> TC index across every generated batch. Wherever one
CFTS019 object is cited by more than one TC — same batch or not, same
req_id or not — the bracket halves of those TCs must differ. Identical text
is a FAIL.

Why it is separate from the per-batch sibling check: that one groups by
req_id inside one file, so 020 in B4 and 107 in B5 sharing 4866286 is
invisible to it, and was (package 19 section 4).

Usage:
    python features/audio_mgmt/scripts/crossbatch_anchors.py
    python features/audio_mgmt/scripts/crossbatch_anchors.py --batches B1 B2
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bracket_tail(test_item: str) -> str:
    """The authored half, not the first parenthesis in the string."""
    _, sep, tail = test_item.rpartition("\n\n(")
    return tail.rstrip(")") if sep else test_item


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batches", nargs="*",
                    default=["B1", "B2", "B3", "B4", "B5"])
    args = ap.parse_args()

    index: dict[str, list[dict]] = defaultdict(list)
    seen = []
    for b in args.batches:
        f = ROOT / "generated" / f"{b}.json"
        if not f.is_file():
            continue
        seen.append(b)
        for tc in json.loads(f.read_text(encoding="utf-8"))["tcs"]:
            for line in str(tc["spec_reference"]).split("\n"):
                m = re.fullmatch(r"CFTS019-(48\d{5})", line.strip())
                if m:
                    index[m.group(1)].append(
                        {"batch": b, "req_id": tc["req_id"],
                         "tail": bracket_tail(tc["test_item"])})

    shared = {a: rows for a, rows in index.items() if len(rows) > 1}
    cross = {a: rows for a, rows in shared.items()
             if len({r["batch"] for r in rows}) > 1}

    fails = []
    for anchor, rows in sorted(shared.items()):
        tails = [r["tail"] for r in rows]
        if len(set(tails)) != len(tails):
            dupes = {t for t in tails if tails.count(t) > 1}
            for t in dupes:
                who = [f"{r['batch']}/{r['req_id']}" for r in rows
                       if r["tail"] == t]
                fails.append(f"CFTS019-{anchor}: {', '.join(who)} share the "
                             f"bracket {t[:56]!r}")

    print(f"R-AM21 cross-batch shared-anchor check over {', '.join(seen)}")
    print(f"  anchors cited          {len(index)}")
    print(f"  cited by more than one {len(shared)}")
    print(f"  of those, across batches {len(cross)}")
    for anchor, rows in sorted(cross.items()):
        who = ", ".join(f"{r['batch']}/{r['req_id']}" for r in rows)
        print(f"    CFTS019-{anchor}: {who}")
    if fails:
        print(f"\n{len(fails)} FAIL:")
        for f in fails:
            print(f"  {f}")
        return 1
    print("\nno shared anchor carries duplicate bracket halves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
