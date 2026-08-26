#!/usr/bin/env python3
"""Count the structural features an openpyxl round-trip silently destroys.

R-G1's note (and user_profiles A-UP09) records the failure this guards: the
036 master's R-column design_method dropdown is an x14 extension, openpyxl
drops it on load, and a check that compares only row counts, formulas and
sheet counts stays green while the dropdown is gone. So every count here is
read from the raw XML through `zipfile` — openpyxl is never opened.
"""
import hashlib
import re
import sys
import zipfile
from pathlib import Path

PATTERNS = {
    # 前綴不可用 `\w+:` 通配 —— 那會把 <x14:dataValidation> 一併算進 legacy，
    # 使 legacy 虛報為 4+1=5，而 R-G1 註之實測值為「3 條 legacy 存活」。
    # 兩者須分開計，否則 x14 損壞時 legacy 之數字會替它補位。
    "dataValidation (legacy)":   re.compile(rb"<dataValidation[ >]"),
    "x14:dataValidation":        re.compile(rb"<x14:dataValidation[ >]"),
    "conditionalFormatting":     re.compile(rb"<(?:\w+:)?conditionalFormatting[ >]"),
    "extLst":                    re.compile(rb"<extLst[ >]"),
}


def probe(path: Path) -> dict:
    out = {"file": str(path), "size": path.stat().st_size,
           "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        out["zip_members"] = len(names)
        out["sheet_xml"] = len([n for n in names
                                if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", n)])
        out["drawing_rels"] = len([n for n in names if "drawing" in n.lower()])
        out["chart_rels"] = len([n for n in names if "/charts/" in n.lower()])
        counts = dict.fromkeys(PATTERNS, 0)
        for n in names:
            if not n.endswith(".xml"):
                continue
            blob = z.read(n)
            for k, rx in PATTERNS.items():
                counts[k] += len(rx.findall(blob))
        out.update(counts)
        wb = z.read("xl/workbook.xml")
        out["sheets_declared"] = len(re.findall(rb"<sheet[ >]", wb))
    return out


def main(argv) -> int:
    if len(argv) < 2:
        sys.exit("usage: xlsx_structure_probe.py <a.xlsx> [b.xlsx]")
    reports = [probe(Path(p)) for p in argv[1:]]
    keys = [k for k in reports[0] if k != "file"]
    width = max(len(k) for k in keys)
    for r in reports:
        print(f"# {r['file']}")
    print()
    print(f"{'':<{width}}  " + "  ".join(f"{i:>66}" for i in range(len(reports))))
    diffs = []
    for k in keys:
        vals = [str(r[k]) for r in reports]
        same = len(set(vals)) == 1
        if not same:
            diffs.append(k)
        print(f"{k:<{width}}  " + "  ".join(f"{v:>66}" for v in vals)
              + ("" if same or len(reports) == 1 else "   <-- DIFFERS"))
    if len(reports) > 1:
        print()
        print("差異欄位:", diffs or "無 —— 逐位元以外之結構計數全等")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
