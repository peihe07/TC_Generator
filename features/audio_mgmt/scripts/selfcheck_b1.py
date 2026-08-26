#!/usr/bin/env python3
"""Package 03 section 3.8 self-check for a generated audio_mgmt batch.

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
DELIVERY = ("test_item", "pre_conditions", "input_test_data",
            "test_procedure", "expected_result", "remarks")


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
            if MODALS.search(line):
                bad(tc, f"expected_result uses a modal verb: {line[:50]}")
        proc = tc["test_procedure"].split("\n")
        if not re.match(r"^\d+\.\s+Verify\b", proc[-1]):
            bad(tc, "final step is not a Verify step")
        if len(proc) != len(tc["expected_result"].split("\n")):
            bad(tc, "step count does not match expected-result count")
        if tc["design_method"] not in vocab:
            bad(tc, f"design_method outside the dropdown vocabulary")
        for line in tc["spec_reference"].split("\n"):
            if not re.fullmatch(r"CFTS019-48\d{5}", line):
                bad(tc, f"spec_reference line malformed: {line!r}")
        if not re.fullmatch(r"SWE1_AMM_\d{3}", tc["req_id"]):
            bad(tc, "req_id is not the underscore form R-AM7 requires")
        if "\n\n(" not in tc["test_item"] or not tc["test_item"].endswith(")"):
            bad(tc, "test_item is not in the two-part shape")
        if tc["test_group"] != "Audio Management":
            bad(tc, f"test_group is {tc['test_group']!r}")
        if tc["priority"] not in ("P0", "P1", "P2"):
            bad(tc, f"priority is {tc['priority']!r}")

    brackets = defaultdict(list)
    for tc in data["tcs"]:
        brackets[tc["req_id"]].append(tc["test_item"].split("(", 1)[1])
    for req, xs in brackets.items():
        if len(xs) != len(set(xs)):
            fails.append(f"{req}: two rows share the same bracket text")

    print(f"{args.batch}: {len(data['tcs'])} TCs over "
          f"{data['leaves_authored']} leaves")
    if fails:
        print(f"\n{len(fails)} check(s) failed:")
        for f in fails:
            print(f"  {f}")
        sys.exit(1)
    print("all checks pass")


if __name__ == "__main__":
    main()
