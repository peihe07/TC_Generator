#!/usr/bin/env python3
"""Build spec_id -> SYS1 outline mapping for Home HMI spec references.

Reads the SYS1 Polarion export (Basic Report sheet) and extracts the mapping
from spec item codes (HSD1, HSS4.1, SNS3, ...) to Polarion Outline Numbers.
The outline number is the section suffix used in the workbook's
Specification Reference column, following the done-region format:

    Home Screen HMI Logic and Flow R1 SR24 Post 2A (March 17 2023)_{outline}

Derived artifact — regenerate whenever SYS1 is re-exported. Do NOT hand-edit
the output tsv; stale mappings silently corrupt traceability.

The SYS1 path defaults to `feature.yaml` `paths.sys1_export`; --sys1
overrides it.

Known limitation: only rows whose Description starts with an item code
pattern `XXn[.n].)` resolve to a spec_id (76 of 104 in the 2023-03-17
export). Rows without a code (Assumptions, chapter headings, image-only
rows) are emitted with spec_id `-`. Downstream lookups that miss MUST fail
loud and land in ANOMALIES.md — never leave spec_reference blank silently.
"""

import argparse
import csv
import re
import sys
from pathlib import Path

import openpyxl

from feature_config import load_feature_config, resolve_path

# Matches leading item codes like `HSD1.)`, `HSS4.1)`, `SNS3.1)`, `HS9.2.1)`
ITEM_CODE_RE = re.compile(r"\s*([A-Z]{2,4}\d+(?:\.\d+)*)\.?\)")


def build_map(sys1_path: Path) -> list[tuple[str, str, str]]:
    """Return rows of (spec_id_or_dash, outline, desc_head)."""
    wb = openpyxl.load_workbook(sys1_path, read_only=True)
    ws = wb["Basic Report"]
    rows = []
    for r in list(ws.iter_rows(values_only=True))[1:]:
        item_id, outline, desc = r[0], r[2], r[3]
        if not item_id or not outline:
            continue
        desc = str(desc or "")
        m = ITEM_CODE_RE.match(desc)
        spec_id = m.group(1) if m else "-"
        head = desc[:70].replace("\n", " ").replace("\r", " ")
        rows.append((spec_id, str(outline), head))
    wb.close()
    if not rows:
        raise SystemExit(f"no outline rows extracted from {sys1_path}")
    return rows


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sys1", help="override feature.yaml paths.sys1_export")
    ap.add_argument("--feature-dir", default=".")
    ap.add_argument("--out", default="data", help="output directory")
    args = ap.parse_args()

    cfg = load_feature_config(args.feature_dir)
    rows = build_map(resolve_path(cfg, "sys1_export", args.sys1))
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "spec_id_to_outline.tsv"

    with out_path.open("w", newline="", encoding="utf-8") as f:
        f.write("# spec_id_to_outline.tsv — derived from SYS1 Basic Report; "
                "regenerate via build_outline_map.py, do not hand-edit\n")
        f.write("# spec_reference format: Home Screen HMI Logic and Flow "
                "R1 SR24 Post 2A (March 17 2023)_{outline}\n")
        w = csv.writer(f, delimiter="\t")
        w.writerow(["spec_id", "outline", "desc"])
        for row in rows:
            w.writerow(row)

    mapped = sum(1 for r in rows if r[0] != "-")
    print(f"wrote {out_path}: {len(rows)} outline rows, "
          f"{mapped} with spec_id", file=sys.stderr)


if __name__ == "__main__":
    main()
