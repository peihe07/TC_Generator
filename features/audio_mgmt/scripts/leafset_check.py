#!/usr/bin/env python3
"""Post-generation leaf-set check: the batch must carry exactly its ruled leaves.

The check that already existed runs before a batch is handed down and asks
whether every one of the 318 leaves is spoken for somewhere. It cannot see a
leaf that was ruled into a batch and then dropped while the batch was being
written, because by then the plan has already passed.

This one compares the generated batch against its own ruled set, element by
element rather than by count:

    {req_id in B{n}.json}  ==  {ruled leaves}  -  {leaves held with a reason}

The ruled set is the batch context, which is built from the handed-down
anchor table and is never edited by hand to remove a leaf. A leaf that
cannot ship stays in the context carrying `held` and a reason; deleting it
instead is what this check exists to make impossible. A held leaf without a
reason fails too — otherwise the flag becomes the same silent hole.

Filed against A-AM17 (293 ruled and never executed) and A-AM19 (221 dropped
from context and generation together, so a context-only comparison agreed
with itself).

Usage:
    python features/audio_mgmt/scripts/leafset_check.py --batch B7
    python features/audio_mgmt/scripts/leafset_check.py --all
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(batch: str) -> list[str]:
    ctx_path = ROOT / "batches" / f"{batch}_context.json"
    gen_path = ROOT / "generated" / f"{batch}.json"
    if not (ctx_path.is_file() and gen_path.is_file()):
        return [f"{batch}: context or generated file missing"]

    ctx = json.loads(ctx_path.read_text(encoding="utf-8"))
    data = json.loads(gen_path.read_text(encoding="utf-8"))

    ruled = {leaf["swe_id"] for leaf in ctx}
    held = {leaf["swe_id"]: (leaf.get("held") or "") for leaf in ctx
            if leaf.get("held")}
    made = {tc["req_id"] for tc in data["tcs"]}
    expected = ruled - set(held)

    problems = []
    for sid in sorted(expected - made):
        problems.append(f"{batch}: {sid} is ruled into this batch, is not "
                        f"held, and has no TC")
    for sid in sorted(made - ruled):
        problems.append(f"{batch}: {sid} has a TC and is not in the ruled set")
    for sid, reason in sorted(held.items()):
        if not str(reason).strip():
            problems.append(f"{batch}: {sid} is held with no reason given")
        elif sid in made:
            problems.append(f"{batch}: {sid} is marked held and has a TC")
    if data["leaves_authored"] != len(made):
        problems.append(
            f"{batch}: leaves_authored says {data['leaves_authored']} against "
            f"{len(made)} distinct req_ids")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    batches = ([f"B{i}" for i in range(1, 8)] if args.all
               else [args.batch] if args.batch else [])
    if not batches:
        ap.error("give --batch or --all")

    problems = []
    for b in batches:
        ctx = ROOT / "batches" / f"{b}_context.json"
        held = 0
        if ctx.is_file():
            held = sum(1 for leaf in json.loads(ctx.read_text(encoding="utf-8"))
                       if leaf.get("held"))
        rows = check(b)
        note = f", {held} held" if held else ""
        print(f"{b}: {'ok' if not rows else str(len(rows)) + ' problem(s)'}{note}")
        problems += rows
    if problems:
        print()
        for p in problems:
            print(f"  {p}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
