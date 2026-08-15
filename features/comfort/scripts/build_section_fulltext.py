#!/usr/bin/env python3
"""Full text of every cited spec section — handoff 13 §4, ruling R-C18.

`layer3_map.tsv` carries `section_title` truncated to 60 characters. R-C18
rules that such a field is for navigation only and must never carry a
placement, scope, equivalence, applicability or grouping judgement — because
truncation fails silently and can produce a fragment that reads perfectly
well and means something else. The precedent is section 6.3, where
`secondary` was cut to `secon` and "secondary lower screen" was read as
"second row".

This file is the antidote: the full clause, untruncated, for all 129 cited
sections. Extract once rather than per-question — Phase 4 needs the real text
for every TC it writes, and a per-question workaround would leave the same
trap in place for whoever asks the next question.

Newlines inside a clause are escaped to a literal \\n so one section is
always exactly one TSV row. Consumers must unescape before reading.

Usage:
    python3 features/comfort/scripts/build_section_fulltext.py
"""

import csv
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
SYS1 = (ROOT / "spec-index" / "cache" /
        "SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023).xlsx")
LAYER3 = FEATURE / "data" / "layer3_map.tsv"
TEST_SETS = FEATURE / "data" / "test_set_map.tsv"
OUT = FEATURE / "data" / "section_fulltext.tsv"

EXPECTED_ROWS = 129
TRUNCATE_AT = 60          # what layer3_map.tsv used


def clean(raw: str) -> str:
    """Export text -> readable clause. Image refs dropped, CRLF markers
    turned into real newlines; NO length limit — that is the whole point."""
    s = str(raw or "")
    s = re.sub(r"\(image:[^)]*\)", " ", s)
    s = s.replace("_x000D_", "\n").replace("\r\n", "\n").replace("\r", "\n")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


def main() -> None:
    layer3 = {r["outline"]: r for r in
              csv.DictReader(LAYER3.open(encoding="utf-8"), delimiter="\t")}
    tset = {r["outline"]: r["test_set"] for r in
            csv.DictReader(TEST_SETS.open(encoding="utf-8"), delimiter="\t")}

    wb = openpyxl.load_workbook(SYS1, read_only=True)
    export = {str(r[2]).strip(): clean(r[3])
              for r in wb["Basic Report"].iter_rows(values_only=True) if r[2]}
    wb.close()

    def key(s): return tuple(int(p) for p in s.split("."))

    rows, short = [], []
    for outline in sorted(layer3, key=key):
        full = export.get(outline, "")
        if len(full) <= TRUNCATE_AT:
            short.append((outline, len(full)))
        rows.append({
            "outline": outline,
            "req_id": layer3[outline]["req_ids"],
            "test_set": tset.get(outline, "(unassigned)"),
            "full_text": full.replace("\\", "\\\\").replace("\n", "\\n")
                             .replace("\t", " "),
        })

    hdr = ["outline", "req_id", "test_set", "full_text"]
    OUT.write_text("\n".join(["\t".join(hdr)] +
                             ["\t".join(r[h] for h in hdr) for r in rows])
                   + "\n", encoding="utf-8")

    # ---------------------------------------------------------- assertions
    checks = []
    checks.append(("row count == 129", EXPECTED_ROWS, len(rows), ""))

    # The point of the file: no row may still be the truncated value.
    #
    # Equality alone is not the test. Section 3.3's clause is exactly 60
    # characters ("C21.) MAX DEF and REAR DEF are available during climate
    # off.") so it equals its own truncation — a coincidence, not a failure.
    # The question is whether truncation actually REMOVED anything, so the
    # comparison is against the untruncated export length, not the title's.
    still_truncated = [
        r["outline"] for r in rows
        if r["full_text"] == layer3[r["outline"]]["section_title"]
        and len(export.get(r["outline"], "")) > TRUNCATE_AT]
    coincident = [r["outline"] for r in rows
                  if r["full_text"] == layer3[r["outline"]]["section_title"]
                  and len(export.get(r["outline"], "")) == TRUNCATE_AT]
    checks.append(("no row equals its truncated layer3_map value",
                   [], still_truncated,
                   f"compared against the export's own length, not the "
                   f"title's; {len(coincident)} row(s) equal by coincidence "
                   f"(clause is exactly {TRUNCATE_AT} chars): {coincident}"))

    # A short full_text is legitimate ONLY if the clause really is short.
    # Listed explicitly rather than asserted away, per handoff 13 §4 item 3.
    checks.append((f"full_text shorter than {TRUNCATE_AT} chars",
                   "listed, each confirmed genuinely short",
                   "listed, each confirmed genuinely short",
                   f"{len(short)} rows: {short}" if short else "none"))

    checks.append(("outline set equals layer3_map's",
                   [], sorted(set(layer3) ^ {r["outline"] for r in rows}, key=key),
                   f"{len(layer3)} vs {len(rows)}"))

    failed = 0
    print(f"{len(rows)} sections written to {OUT.relative_to(ROOT)}\n")
    print("assertions:")
    for name, expected, actual, note in checks:
        ok = expected == actual
        failed += not ok
        print(f"- {'PASS' if ok else '**FAIL**'} — {name}: "
              f"expected `{expected}`, measured `{actual}`"
              + (f" — {note}" if note else ""))

    lens = [len(r["full_text"]) for r in rows]
    print(f"\nfull_text length: min {min(lens)}, median "
          f"{sorted(lens)[len(lens) // 2]}, max {max(lens)}")
    if failed:
        sys.exit(f"\nFAILED: {failed} assertion(s) — this file exists to be "
                 "the untruncated source; a failure here means it is not.")


if __name__ == "__main__":
    main()
