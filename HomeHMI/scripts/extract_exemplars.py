#!/usr/bin/env python3
"""Extract few-shot exemplar TCs from the done region of FW036 (Home).

These anchor the generator's output style far more effectively than prose
rules alone. Media keyed exemplars by Test Set; Home cannot, because the Test
Group / Test Set columns are BLANK throughout the done region (RUNBOOK §5) —
so exemplars are keyed by SPEC CHAPTER instead, derived from the outline
suffix of the Specification Reference column via `spec_id_to_outline.tsv`
(HSD / HSS / SNS / BSP / HS / SW / LSW ...).

The done region is detected by a non-empty Test Case Author column, never by a
row threshold: Home's Arif rows are interleaved with the regen rows.

Selection heuristic per chapter: prefer diversity of Design Method, then the
longest procedures (richer patterns: baseline setup, multi-phase ER, popup
citation format).

Usage:
    python extract_exemplars.py --fw036 <036.xlsx> --out data/ [--per-chapter 3]
"""
import argparse
import csv
import json
import re
from collections import OrderedDict
from pathlib import Path

import openpyxl

TC_SHEET = "Test Case Specification&Result"
TC_FIRST_DATA_ROW = 10
AUTHOR_COL = 25  # column Z

# 0-based column indices, verified against the 2026-07-20 workbook header row 9
FIELDS = {
    "req_id": 3, "test_group": 6, "test_set": 7, "test_item": 8,
    "pre_conditions": 9, "input_test_data": 10, "test_procedure": 11,
    "expected_result": 12, "specification_reference": 13, "priority": 15,
    "design_method": 16, "remarks": 32,
}

OUTLINE_RE = re.compile(r"_(\d{1,2}(?:\.\d+)*)\s*$")
CHAPTER_RE = re.compile(r"^([A-Z]{2,4})")


def load_outline_to_chapter(tsv_path: Path) -> dict[str, str]:
    """{outline: chapter} from the derived outline map, e.g. '4.1' -> 'HSD'."""
    if not tsv_path.exists():
        raise SystemExit(f"missing {tsv_path}; run build_outline_map.py first")
    mapping = {}
    with tsv_path.open(encoding="utf-8") as f:
        rows = csv.reader((ln for ln in f if not ln.startswith("#")),
                          delimiter="\t")
        next(rows, None)  # header
        for spec_id, outline, *_ in rows:
            m = CHAPTER_RE.match(spec_id)
            if m:
                mapping[outline] = m.group(1)
    return mapping


def chapter_of(spec_ref: str, outline_to_chapter: dict[str, str]) -> str:
    """Chapter for a Specification Reference cell; '?' when unresolvable.

    Unresolved refs are kept under '?' rather than dropped — a chapter that
    never resolves is a mapping bug worth seeing, not something to hide.
    """
    m = OUTLINE_RE.search(spec_ref)
    if not m:
        return "?"
    outline = m.group(1)
    if outline in outline_to_chapter:
        return outline_to_chapter[outline]
    # Sub-outlines inherit their parent's chapter (4.8.4 -> 4.8 -> 4).
    parts = outline.split(".")
    for cut in range(len(parts) - 1, 0, -1):
        parent = ".".join(parts[:cut])
        if parent in outline_to_chapter:
            return outline_to_chapter[parent]
    return "?"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fw036", required=True)
    ap.add_argument("--out", default="data")
    ap.add_argument("--per-chapter", type=int, default=3)
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    outline_to_chapter = load_outline_to_chapter(out / "spec_id_to_outline.tsv")

    wb = openpyxl.load_workbook(args.fw036, read_only=True)
    ws = wb[TC_SHEET]

    by_chapter: "OrderedDict[str, list]" = OrderedDict()
    for rownum, r in enumerate(ws.iter_rows(min_row=TC_FIRST_DATA_ROW,
                                            values_only=True),
                               start=TC_FIRST_DATA_ROW):
        if not r[FIELDS["req_id"]]:
            continue
        if not (len(r) > AUTHOR_COL and str(r[AUTHOR_COL] or "").strip()):
            continue  # regen region — not an exemplar
        tc = {k: (str(r[i]).strip() if len(r) > i and r[i] is not None else "")
              for k, i in FIELDS.items()}
        tc["_row"] = rownum
        tc["_chapter"] = chapter_of(tc["specification_reference"],
                                    outline_to_chapter)
        by_chapter.setdefault(tc["_chapter"], []).append(tc)
    wb.close()

    exemplars = OrderedDict()
    for chapter, tcs in by_chapter.items():
        picked, seen_methods = [], set()
        # Complete rows first: 13 done-region rows have a blank Priority
        # (A-H05) and would teach the generator to leave it blank too.
        longest = sorted(tcs, key=lambda t: (not t["priority"],
                                             -len(t["test_procedure"])))
        for tc in longest:  # one per distinct design method first (diversity)
            if tc["design_method"] not in seen_methods:
                picked.append(tc)
                seen_methods.add(tc["design_method"])
            if len(picked) >= args.per_chapter:
                break
        for tc in longest:  # top up with the richest remaining procedures
            if len(picked) >= args.per_chapter:
                break
            if tc not in picked:
                picked.append(tc)
        exemplars[chapter] = sorted(picked, key=lambda t: t["_row"])

    (out / "exemplars.json").write_text(
        json.dumps(exemplars, ensure_ascii=False, indent=2))

    total = sum(len(v) for v in exemplars.values())
    print(f"exemplars: {total} TCs across {len(exemplars)} spec chapters")
    for chapter, tcs in exemplars.items():
        pool = len(by_chapter[chapter])
        print(f"  {chapter}: {len(tcs)} of {pool} "
              f"(rows {[t['_row'] for t in tcs]})")
    if "?" in exemplars:
        print("  '?' = Specification Reference did not resolve through "
              "spec_id_to_outline.tsv — investigate before relying on it")


if __name__ == "__main__":
    main()
