#!/usr/bin/env python3
"""Build remaining_leaves.json + sibling_map.json + row_segments.json.

Diff the 037 A03 Analysis Report (leaf Functional Requirements) against the
DONE region of FW036. Everything not covered there is the remaining work.

Home differs from Media in one structural way: the done region is not a
positional prefix. Arif's rows are INTERLEAVED with the blank-author regen
rows in three segments each, so the done region is detected by the Test Case
Author column (Z) being non-empty, never by a row threshold. The detected
segment boundaries are emitted to `row_segments.json` for the write-back step,
which rewrites regen segments in place and content-hashes the Arif segments.

Usage:
    python build_remaining.py --a03 <037.xlsx> --fw036 <036.xlsx> --out data/
"""
import argparse
import hashlib
import json
import re
from collections import OrderedDict
from pathlib import Path

import openpyxl

TC_SHEET = "Test Case Specification&Result"
A03_SHEET = "Analysis Report"
TC_FIRST_DATA_ROW = 10
AUTHOR_COL = 25  # 0-based index of column Z (Test Case Author)
REQ_ID_COL = 3   # 0-based index of column D (Requirement or Design ID)
# Content columns hashed for the done-region invariant: D..AG (1-based 4..33)
CONTENT_COLS = range(3, 33)

# Expected shape, verified against the 2026-07-20 workbook. A mismatch means
# the inputs changed underneath the plan — fail loud rather than regenerate
# against a moved target.
EXPECT_LEAVES = 140
EXPECT_REMAINING = 62
EXPECT_ARIF_ROWS = 144


def load_a03(path: str) -> "OrderedDict[str, dict]":
    """Return all leaf FRs from the 037 analysis report, in document order."""
    wb = openpyxl.load_workbook(path, read_only=True)
    ws = wb[A03_SHEET]
    leaves = OrderedDict()
    for r in ws.iter_rows(min_row=8, values_only=True):
        rid, cat = r[0], str(r[6] or "")
        if not rid or not str(rid).startswith("SWE1"):
            continue
        if cat != "Functional Requirement":
            continue
        src = str(r[2] or "")
        m = re.search(r"_(\d{1,2}(?:\.\d+)*)$", src)
        leaves[str(rid)] = {
            "req_id": str(rid),
            "parent": str(rid).rsplit("-", 1)[0] if re.search(r"-\d+-\d+$", str(rid))
                      else str(rid),
            "title": str(r[3] or "").strip(),
            "description": str(r[4] or "").strip(),
            "hmi_source_id": src,
            "section": m.group(1) if m else "",
            "source_req_id": str(r[1] or ""),
            "frop": str(r[7] or "") if len(r) > 7 else "",
        }
    wb.close()
    return leaves


def load_fw036(path: str) -> tuple[list[dict], list[dict]]:
    """Return (rows, segments) for the TC sheet.

    Each row is {row, req_id, author, content_hash}. Segments are contiguous
    runs of the same kind: {"kind": "ARIF"|"REGEN", "start": r, "end": r}.
    """
    wb = openpyxl.load_workbook(path, read_only=True)
    ws = wb[TC_SHEET]
    rows = []
    for i, r in enumerate(ws.iter_rows(min_row=TC_FIRST_DATA_ROW,
                                       values_only=True),
                          start=TC_FIRST_DATA_ROW):
        if not any(c is not None for c in r):
            continue
        cells = [str(r[c]) if c < len(r) and r[c] is not None else ""
                 for c in CONTENT_COLS]
        rows.append({
            "row": i,
            "req_id": str(r[REQ_ID_COL] or ""),
            "author": str(r[AUTHOR_COL] or "").strip()
                      if len(r) > AUTHOR_COL else "",
            "content_hash": hashlib.sha256(
                "\x1f".join(cells).encode("utf-8")).hexdigest()[:16],
        })
    wb.close()

    segments = []
    for row in rows:
        kind = "ARIF" if row["author"] else "REGEN"
        if segments and segments[-1]["kind"] == kind \
                and segments[-1]["end"] == row["row"] - 1:
            segments[-1]["end"] = row["row"]
            segments[-1]["rows"] += 1
        else:
            segments.append({"kind": kind, "start": row["row"],
                             "end": row["row"], "rows": 1})
    return rows, segments


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--a03", required=True)
    ap.add_argument("--fw036", required=True)
    ap.add_argument("--out", default="data")
    ap.add_argument("--no-assert", action="store_true",
                    help="skip the expected-shape assertions (inputs changed)")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    leaves = load_a03(args.a03)
    rows, segments = load_fw036(args.fw036)

    done = {r["req_id"] for r in rows if r["author"] and r["req_id"]}
    draft = {r["req_id"] for r in rows if not r["author"] and r["req_id"]}

    remaining = OrderedDict(
        (rid, info) for rid, info in leaves.items() if rid not in done
    )
    # Req IDs the workbook traces to but 037 does not define at all. This is an
    # upstream traceability break, not a generation input — record, never fix.
    orphans = sorted((done | draft) - set(leaves))
    uncovered = [rid for rid in remaining if rid not in draft]

    # sibling_map: parent -> ordered list of ALL its leaf sub-ids (done ones
    # included, so the generator sees full sibling context per docs.md §4.6)
    sibling_map = OrderedDict()
    for rid, info in leaves.items():
        sibling_map.setdefault(info["parent"], []).append(
            {"req_id": rid, "title": info["title"], "remaining": rid in remaining}
        )
    sibling_map = OrderedDict(
        (p, subs) for p, subs in sibling_map.items()
        if any(s["remaining"] for s in subs)
    )

    arif_rows = [r for r in rows if r["author"]]
    done_region = {
        "arif_row_count": len(arif_rows),
        "segments": segments,
        # Content-based invariant (RUNBOOK Step 4.2): the ordered sequence of
        # Arif row contents must survive write-back regardless of row shifts.
        "ordered_content_hash": hashlib.sha256(
            "\n".join(r["content_hash"] for r in arif_rows).encode()
        ).hexdigest(),
    }

    (out / "remaining_leaves.json").write_text(
        json.dumps(list(remaining.values()), ensure_ascii=False, indent=2))
    (out / "sibling_map.json").write_text(
        json.dumps(sibling_map, ensure_ascii=False, indent=2))
    (out / "row_segments.json").write_text(
        json.dumps(done_region, ensure_ascii=False, indent=2))

    print(f"037 leaves: {len(leaves)}  done: {len(done & set(leaves))}  "
          f"remaining: {len(remaining)} across {len(sibling_map)} parents")
    print("segments: " + "  ".join(
        f"{s['kind']} {s['start']}-{s['end']} ({s['rows']})" for s in segments))
    print(f"arif rows: {len(arif_rows)}  "
          f"ordered_content_hash: {done_region['ordered_content_hash'][:16]}…")
    if uncovered:
        print(f"not covered anywhere (no draft row either): {uncovered}")
    if orphans:
        print(f"ORPHAN req_ids in workbook but absent from 037: {orphans} "
              f"-> must be recorded in ANOMALIES.md")

    if not args.no_assert:
        problems = []
        if len(leaves) != EXPECT_LEAVES:
            problems.append(f"leaves {len(leaves)} != {EXPECT_LEAVES}")
        if len(remaining) != EXPECT_REMAINING:
            problems.append(f"remaining {len(remaining)} != {EXPECT_REMAINING}")
        if len(arif_rows) != EXPECT_ARIF_ROWS:
            problems.append(f"arif rows {len(arif_rows)} != {EXPECT_ARIF_ROWS}")
        if problems:
            raise SystemExit("input shape changed: " + "; ".join(problems)
                             + "\nre-verify the plan, then rerun --no-assert")


if __name__ == "__main__":
    main()
