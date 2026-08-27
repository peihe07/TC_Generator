#!/usr/bin/env python3
"""Package 03 section 3.8 self-check for a generated audio_mgmt batch.

Covers canon 5.1 (forbidden step verbs) and 5.5 (the final step must observe
something), plus an advisory hint on whether step 1 establishes state.

Mechanical checks only — every rule here is one the handoff package states
outright, so a failure is a defect and not a judgement call.

Usage:
    python features/audio_mgmt/scripts/selfcheck_b1.py [--batch B1]
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODALS = re.compile(r"\b(shall|should|must|will|would|can|may|might)\b", re.I)

# Canon 5.1, check A. Copied one-for-one from the canon so the two can be
# diffed by eye — nine entries there, nine here. "observe whether" is
# subsumed by "observe" as a matcher, but a list carrying eight where the
# canon says nine cannot be checked against its own authority.
FORBIDDEN_VERBS = ("observe whether", "observe", "see if", "check whether",
                   "confirm whether", "verify", "watch", "monitor", "inspect")
# Anchored at the step's own start. 5.1 allows `verify` inside a purpose
# clause ("... to verify that ..."), so a substring test would fail legal
# usage, and a gate that fails legal usage teaches authors to route around it
# rather than to fix anything. Longest-first, so the reported verb is the
# fullest phrase that matched.
STEP_HEAD = re.compile(
    r"^\s*\d+\.\s*(" + "|".join(sorted(FORBIDDEN_VERBS, key=len, reverse=True))
    + r")\b", re.I)

# Canon 5.5 — the final step must hold an observable verification target.
# A PROXY, NOT THE CRITERION: the criterion is whether the step names
# something a tester can actually read off the system, and that stays human
# reviewed. This only catches a final step that performs an action and
# observes nothing.
OBSERVATION_VERBS = ("read", "measure", "record", "compare", "confirm")
FINAL_STEP = re.compile(
    r"^\s*\d+\.\s*(" + "|".join(OBSERVATION_VERBS) + r")\b", re.I)
DELIVERY = ("test_item", "pre_conditions", "input_test_data",
            "test_procedure", "expected_result", "remarks")



def bracket_tail(test_item: str) -> str:
    """The authored bracket half, not the first parenthesis in the string.

    Splitting on the first "(" reaches into the verbatim upper half whenever
    the requirement text contains its own parentheses — SWE1_AMM_256's
    "(navigation prompts, warnings, chimes, etc.)" is one — so the
    sibling-distinction check was comparing fragments of the specification
    instead of the tails it exists to compare.
    """
    _, sep, tail = test_item.rpartition("\n\n(")
    return tail if sep else test_item


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch", default="B1")
    args = ap.parse_args()

    data = json.loads((ROOT / "generated" / f"{args.batch}.json")
                      .read_text(encoding="utf-8"))
    vocab = set(json.loads((ROOT / "data" / "recon.json")
                           .read_text(encoding="utf-8"))["design_method_vocab"])
    fails = []

    def bad(tc, msg):
        fails.append(f"{tc['req_id']}: {msg}")

    for tc in data["tcs"]:
        for key in DELIVERY:
            for line in str(tc[key]).split("\n"):
                if re.search(r"[一-鿿]", line):
                    bad(tc, f"{key} carries CJK text")
                if line.rstrip().endswith(".") and not re.search(
                        r"\b\d+\.$", line.rstrip()):
                    bad(tc, f"{key} line ends in a period")
        for line in tc["expected_result"].split("\n"):
            if MODALS.search(re.sub(r"\bCAN\b", "", line)):
                bad(tc, f"expected_result uses a modal verb: {line[:50]}")
        proc = tc["test_procedure"].split("\n")
        for step in proc:
            m = STEP_HEAD.match(step)
            if m:
                bad(tc, f"step opens with the 5.1 verb {m.group(1)!r}: "
                        f"{step[:60]}")
        if not FINAL_STEP.match(proc[-1]):
            bad(tc, f"final step observes nothing (canon 5.5): {proc[-1][:60]}")
        if len(proc) != len(tc["expected_result"].split("\n")):
            bad(tc, "step count does not match expected-result count")
        if tc["design_method"] not in vocab:
            bad(tc, f"design_method outside the dropdown vocabulary")
        for line in tc["spec_reference"].split("\n"):
            # R-AM23: a four-gate-empty anchor may ship as a bare NA so the
            # workbook carries no blocking value at 8.4.3; the DR stays open.
            if not (re.fullmatch(r"CFTS019-48\d{5}", line)
                    or re.match(r"^PENDING: DR-\w+\b", line)
                    or line == "NA"):
                bad(tc, f"spec_reference line malformed: {line!r}")
        if not re.fullmatch(r"SWE1_AMM_\d{3}", tc["req_id"]):
            bad(tc, "req_id is not the underscore form R-AM7 requires")
        if "\n\n(" not in tc["test_item"] or not tc["test_item"].endswith(")"):
            bad(tc, "test_item is not in the two-part shape")
        if tc["test_group"] != "Audio Management":
            bad(tc, f"test_group is {tc['test_group']!r}")
        if tc["priority"] not in ("P0", "P1", "P2"):
            bad(tc, f"priority is {tc['priority']!r}")

    # Advisory, not a gate. Calibrated against the time_management corpus:
    # a first draft flagged any step 1 that was not Confirm/Read/Record and
    # fired on 53 of 57 cases here and 27 of 35 there — it was flagging the
    # dominant legitimate shape ("1. Open the ... settings"), so it was noise.
    # What actually costs a tester is a case whose starting state is stated
    # nowhere: pre_conditions says NA and step 1 goes straight to a stimulus.
    # That reads 0/35 on time_management and isolates the real gaps here.
    hints = []
    for tc in data["tcs"]:
        first = tc["test_procedure"].split("\n")[0]
        if (str(tc["pre_conditions"]).strip().upper() == "NA"
                and re.match(r"^\s*\d+\.\s*(Trigger|Activate|Press|Receive"
                             r"|Switch|Set)\b", first)):
            hints.append(f"{tc['req_id']}: pre_conditions is NA and step 1 "
                         f"applies a stimulus, so the starting state is "
                         f"stated nowhere: {first[:50]}")

    brackets = defaultdict(list)
    for tc in data["tcs"]:
        brackets[tc["req_id"]].append(bracket_tail(tc["test_item"]))
    for req, xs in brackets.items():
        if len(xs) != len(set(xs)):
            fails.append(f"{req}: two rows share the same bracket text")

    print(f"{args.batch}: {len(data['tcs'])} TCs over "
          f"{data['leaves_authored']} leaves")
    if hints:
        print(f"\n{len(hints)} hint(s) — advisory, not a gate:")
        for h in hints:
            print(f"  {h}")

    if fails:
        print(f"\n{len(fails)} check(s) failed:")
        for f in fails:
            print(f"  {f}")
        sys.exit(1)
    print("\nall checks pass")


if __name__ == "__main__":
    main()
