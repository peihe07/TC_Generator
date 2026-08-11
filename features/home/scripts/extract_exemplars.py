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

Workbook path, sheet and column letters come from `feature.yaml`; --fw036
overrides the path.

Usage:
    python extract_exemplars.py --out data/ [--per-chapter 3]
"""
import argparse
import csv
import json
import re
from collections import OrderedDict
from pathlib import Path

import openpyxl

from feature_config import load_feature_config, resolve_path

# Exemplar field -> feature.yaml column key. The output key stays
# `specification_reference` because downstream consumers read that name.
FIELD_COLUMNS = {
    "req_id": "req_id", "test_group": "test_group", "test_set": "test_set",
    "test_item": "test_item", "pre_conditions": "pre_conditions",
    "input_test_data": "input_test_data", "test_procedure": "test_procedure",
    "expected_result": "expected_result",
    "specification_reference": "spec_reference", "priority": "priority",
    "design_method": "design_method", "remarks": "remarks",
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
    ap.add_argument("--fw036", help="override feature.yaml paths.workbook")
    ap.add_argument("--feature-dir", default=".")
    ap.add_argument("--out", default="data")
    ap.add_argument("--per-chapter", type=int, default=3)
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    outline_to_chapter = load_outline_to_chapter(out / "spec_id_to_outline.tsv")

    cfg = load_feature_config(args.feature_dir)
    fields = {k: cfg["col"][v] for k, v in FIELD_COLUMNS.items()}
    author_col = cfg["col"]["author"]
    first_data_row = cfg["workbook"]["header_row"] + 1

    wb = openpyxl.load_workbook(
        resolve_path(cfg, "workbook", args.fw036), read_only=True)
    ws = wb[cfg["workbook"]["sheet"]]

    by_chapter: "OrderedDict[str, list]" = OrderedDict()
    for rownum, r in enumerate(ws.iter_rows(min_row=first_data_row,
                                            values_only=True),
                               start=first_data_row):
        if not r[fields["req_id"]]:
            continue
        if not (len(r) > author_col and str(r[author_col] or "").strip()):
            continue  # regen region — not an exemplar
        tc = {k: (str(r[i]).strip() if len(r) > i and r[i] is not None else "")
              for k, i in fields.items()}
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
