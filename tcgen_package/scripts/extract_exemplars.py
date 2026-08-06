#!/usr/bin/env python3
"""Extract few-shot exemplar TCs from the compliant region of FW036.

Samples up to N complete TCs per Test Set from rows 10-332 (the human-authored
region). These anchor the generator's output style far more effectively than
prose rules alone.

Selection heuristic per Test Set: prefer diversity of Design Method, then
longest procedures (richer patterns: baseline, multi-phase ER, CLI format).

Usage:
    python extract_exemplars.py --fw036 <036.xlsx> --out data/ [--per-set 3]
"""
import argparse
import json
from collections import OrderedDict
from pathlib import Path

import openpyxl

DONE_REGION_LAST_ROW = 332
TC_SHEET = "Test Case Specification 測試用例規範"

FIELDS = {
    "req_id": 3, "test_group": 6, "test_set": 7, "test_item": 8,
    "pre_conditions": 9, "input_test_data": 10, "test_procedure": 11,
    "expected_result": 12, "specification_reference": 13, "priority": 15,
    "design_method": 17,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fw036", required=True)
    ap.add_argument("--out", default="data")
    ap.add_argument("--per-set", type=int, default=3)
    args = ap.parse_args()

    wb = openpyxl.load_workbook(args.fw036, read_only=True)
    ws = wb[TC_SHEET]

    by_set = OrderedDict()
    rownum = 9
    for r in ws.iter_rows(min_row=10, values_only=True):
        rownum += 1
        if rownum > DONE_REGION_LAST_ROW:
            break
        if not r[3]:
            continue
        tc = {k: (str(r[i]).strip() if r[i] is not None else "")
              for k, i in FIELDS.items()}
        tc["_row"] = rownum
        by_set.setdefault(tc["test_set"], []).append(tc)

    exemplars = OrderedDict()
    for ts, tcs in by_set.items():
        # one TC per distinct design method first (diversity), then longest
        picked, seen_methods = [], set()
        for tc in sorted(tcs, key=lambda t: -len(t["test_procedure"])):
            if tc["design_method"] not in seen_methods:
                picked.append(tc)
                seen_methods.add(tc["design_method"])
            if len(picked) >= args.per_set:
                break
        for tc in sorted(tcs, key=lambda t: -len(t["test_procedure"])):
            if len(picked) >= args.per_set:
                break
            if tc not in picked:
                picked.append(tc)
        exemplars[ts] = sorted(picked, key=lambda t: t["_row"])

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "exemplars.json").write_text(
        json.dumps(exemplars, ensure_ascii=False, indent=2))

    total = sum(len(v) for v in exemplars.values())
    print(f"exemplars: {total} TCs across {len(exemplars)} Test Sets")
    for ts, tcs in exemplars.items():
        print(f"  {ts}: {len(tcs)} (rows {[t['_row'] for t in tcs]})")


if __name__ == "__main__":
    main()
