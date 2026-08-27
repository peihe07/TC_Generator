#!/usr/bin/env python3
"""Detect anchors whose clause text is duplicated elsewhere in CFTS019.

Package 24 section 3 (D-B6-01): where two objects carry identical text, both
routes verify against text and both agree, because the text really is the
same. R-AM15's independence cannot discriminate there — only position can.
131 was anchored to 4866489 when 4866466 carries the same sentence in the
Entertainment sequence rather than the Information one.

For every anchor a batch uses, this reports any other object with the same
normalised text, and brackets the leaf by its neighbours' anchors so the
position test is available at a glance.

Usage:
    python features/audio_mgmt/scripts/same_text_anchors.py --batch B6
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

FEATURE = Path(__file__).resolve().parents[1]
ATTRS = re.compile(r"\[(Artifact|State|ECU|Market|Model|Radio|EE)[^\]]*\]")
PAGE = re.compile(r"\d{4}-\d{1,2}-\d{1,2} Page \d+/\d+[^|]*?Audio Management")


def norm(text: str) -> str:
    t = ATTRS.sub("", text)
    t = PAGE.sub("", t)
    return " ".join(t.split()).lower().rstrip(".")


def blocks() -> dict[str, str]:
    raw = (FEATURE / "data" / "cfts019_text.txt").read_text(encoding="utf-8")
    return {m.group(1): m.group(2) for m in re.finditer(
        r"^(48\d{5}): (\[.*?)(?=^\d{7}: \[|\Z)", raw, re.M | re.S)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch", required=True)
    ap.add_argument("--context", action="store_true",
                    help="read the batch context rather than a generated file")
    args = ap.parse_args()

    blk = blocks()
    by_text: dict[str, list[str]] = defaultdict(list)
    for oid, text in blk.items():
        t = norm(text)
        if len(t) > 40:                      # ignore stubs and page furniture
            by_text[t].append(oid)
    dupes = {t: sorted(o) for t, o in by_text.items() if len(o) > 1}

    src = (FEATURE / ("batches" if args.context else "generated") /
           (f"{args.batch}_context.json" if args.context
            else f"{args.batch}.json"))
    data = json.loads(src.read_text(encoding="utf-8"))
    leaves = data if args.context else data["tcs"]

    # The position window must be built from every leaf delivered so far,
    # not this batch alone: 131's neighbours 130 and 132 live in B1, and a
    # per-batch map leaves the window open-ended and useless there.
    used = {}
    for f in sorted((FEATURE / "generated").glob("B*.json")):
        for tc in json.loads(f.read_text(encoding="utf-8"))["tcs"]:
            used.setdefault(tc["req_id"], []).extend(
                re.findall(r"CFTS019-(48\d{5})", tc["spec_reference"]))
    for row in leaves:
        sid = row["swe_id"] if args.context else row["req_id"]
        anchors = (row["anchors"] if args.context else
                   re.findall(r"CFTS019-(48\d{5})", row["spec_reference"]))
        used.setdefault(sid, [])
        used[sid] = sorted(set(used[sid]) | set(anchors))

    flagged = []
    for sid, anchors in sorted(used.items()):
        for a in anchors:
            twins = [o for t, os in dupes.items() if a in os for o in os
                     if o != a]
            if twins:
                flagged.append((sid, a, tuple(sorted(set(twins)))))

    print(f"same-text anchor check over {args.batch}")
    print(f"  objects with a duplicate elsewhere: "
          f"{sum(len(o) for o in dupes.values())} in {len(dupes)} groups")
    print(f"  anchors used by this batch that have a twin: {len(flagged)}")
    if not flagged:
        print("\nnone — the batch's anchors are textually unique")
        return 0
    print("\nEach of these needs the position test; text agreement between "
          "the two routes proves nothing here (package 24 section 3):\n")
    nums = sorted(int(s.split("_")[-1]) for s in used)
    # The position test, automated: the chosen anchor should fall inside the
    # window its neighbouring leaves' anchors open, and the twin should not.
    # Where both fall inside, or the chosen one falls outside, position
    # cannot settle it either and a human has to read.
    verdicts = {"pass": 0, "flag": []}
    for sid, anchor, twins in sorted(set(flagged)):
        n = int(sid.split("_")[-1])
        lo = max((x for x in nums if x < n), default=None)
        hi = min((x for x in nums if x > n), default=None)

        def window(x, pick):
            vals = [int(a) for a in used.get(f"SWE1_AMM_{x:03d}", [])] or [None]
            return pick(v for v in vals if v is not None) if any(
                v is not None for v in vals) else None

        # Tightest window: the highest anchor below and the lowest above.
        # Taking min below and max above widens it and lets twins slip in.
        lo_a = window(lo, max) if lo else None
        hi_a = window(hi, min) if hi else None
        a = int(anchor)
        inside = ((lo_a is None or a > lo_a) and (hi_a is None or a < hi_a))
        twin_in = [t for t in twins
                   if (lo_a is None or int(t) > lo_a)
                   and (hi_a is None or int(t) < hi_a)]
        # A neighbour citing a 1.5.4 Variables object (4867xxx) puts its
        # anchor far from the document position of the requirement itself,
        # which inverts the window. Say so rather than reporting the anchor
        # as misplaced.
        inverted = lo_a is not None and hi_a is not None and lo_a > hi_a
        mark = "pass" if inside and not twin_in and not inverted else "FLAG"
        if mark == "pass":
            verdicts["pass"] += 1
        else:
            verdicts["flag"].append(
                f"  {sid} -> {anchor}  twin(s) {', '.join(twins)}  "
                f"window ({lo_a}, {hi_a})  "
                + ("window inverted — a neighbour cites a variables-section "
                   "object, so position cannot bound this leaf" if inverted
                   else "anchor outside its window" if not inside
                   else f"twin also inside: {', '.join(twin_in)}"))
    print(f"  position test: {verdicts['pass']} pass, "
          f"{len(verdicts['flag'])} need a human read")
    for line in verdicts["flag"]:
        print(line)
    return 1 if verdicts["flag"] else 0


if __name__ == "__main__":
    sys.exit(main())
