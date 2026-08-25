#!/usr/bin/env python3
"""Sidecar writer for data/*.tsv (R-DM30).

A `.tsv` under features/display/data/ starts with its header row. Anything
else — provenance, measurement conditions, which rulings govern it, a
retraction note — goes into `<name>.tsv.meta.json` beside it.

Why not a `#` comment line in the file: `csv.DictReader` reads that comment
AS the header and yields zero usable rows, which looks like empty data
rather than an error (A-DM23). A missing sidecar is a missing file, which
is loud.

Producing scripts must call this immediately after writing the data file.
"""
import json
from pathlib import Path

STAMP = "2026-08-25"


def write_meta(path, columns, data_rows, *, generated_by, rulings=(),
               measurement_conditions="", notes="", inputs=(),
               generated_at=STAMP):
    path = Path(path)
    meta = {
        "data_file": path.name,
        "columns": list(columns),
        "data_rows": data_rows,
        "generated_by": generated_by,
        "generated_at": generated_at,
        "inputs": list(inputs),
        "measurement_conditions": measurement_conditions,
        "rulings": list(rulings),
        "notes": notes,
    }
    path.with_suffix(path.suffix + ".meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return meta
