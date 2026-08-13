#!/usr/bin/env python3
"""P7 write-back safety probe for the FM-WI-FSM-036-A01 rev C template.

Answers one question with evidence, not opinion: what does a write path cost
the workbook? Compares two strategies against the untouched original —

1. `openpyxl` load → mutate → save (the obvious path)
2. zip-level surgical splice: rewrite ONLY the target sheet's XML, copy every
   other zip member byte-for-byte (the path this feature adopts)

Measured on the Privacy template 2026-08-13 (A-PV09). openpyxl drops the x14
extension data validation that drives the R-column "測試用例設計方法" dropdown,
and the loss is not limited to that: printer settings, the legacy VML comment
drawing and the embedded JPEG are all rewritten or dropped. The surgical path
leaves all 48 zip members identical.

Usage:
    python features/privacy/scripts/xlsx_roundtrip_probe.py \
        --workbook features/privacy/inputs/<template>.xlsx \
        --sheet-xml xl/worksheets/sheet6.xml
"""

import argparse
import re
import shutil
import zipfile
from pathlib import Path

import openpyxl

X14_SQREF = re.compile(r"<xm:sqref>([^<]+)</xm:sqref>")
CLASSIC_DV = re.compile(r'<dataValidation [^>]*sqref="([^"]+)"')


def probe(path: Path, sheet_xml: str) -> dict:
    """Structural fingerprint of a workbook: DV coverage + zip inventory."""
    with zipfile.ZipFile(path) as z:
        xml = z.read(sheet_xml).decode("utf-8")
        return {
            "x14_dv": X14_SQREF.findall(xml),
            "classic_dv": CLASSIC_DV.findall(xml),
            "members": set(z.namelist()),
        }


def openpyxl_roundtrip(src: Path, dst: Path, sheet_name: str) -> None:
    """Strategy 1 — the obvious path. Writes a probe value into I10."""
    wb = openpyxl.load_workbook(src)
    wb[sheet_name]["I10"] = "round-trip probe"
    wb.save(dst)


def surgical_roundtrip(src: Path, dst: Path, sheet_xml: str) -> None:
    """Strategy 2 — splice the sheet XML, copy everything else verbatim.

    Writes the same probe value into I10 as an inline string. The template
    ships I10 as a styled-but-empty cell (`<c r="I10" s="81"/>`), so the
    style attribute survives by being carried through the replacement rather
    than regenerated — which is also why this path can clear the residual
    sample values in row 10/11 without disturbing their formatting.
    """
    with zipfile.ZipFile(src) as zin:
        xml = zin.read(sheet_xml).decode("utf-8")
        patched = xml.replace(
            '<c r="I10" s="81"/>',
            '<c r="I10" s="81" t="inlineStr"><is><t>round-trip probe</t></is></c>',
            1)
        with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = (patched.encode("utf-8") if item.filename == sheet_xml
                        else zin.read(item.filename))
                zout.writestr(item, data)


def report(tag: str, base: dict, after: dict) -> bool:
    """Print the delta; return True when the strategy is lossless."""
    lost_x14 = set(base["x14_dv"]) - set(after["x14_dv"])
    lost_dv = set(base["classic_dv"]) - set(after["classic_dv"])
    dropped = sorted(base["members"] - after["members"])
    added = sorted(after["members"] - base["members"])
    ok = not (lost_x14 or lost_dv or dropped or added)
    print(f"\n--- {tag}: {'LOSSLESS' if ok else 'LOSSY'}")
    print(f"  x14 DV lost      : {sorted(lost_x14) or 'none'}")
    print(f"  classic DV lost  : {sorted(lost_dv) or 'none'}")
    print(f"  zip members lost : {dropped or 'none'}")
    print(f"  zip members added: {added or 'none'}")
    return ok


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--workbook", required=True, type=Path)
    ap.add_argument("--sheet-xml", default="xl/worksheets/sheet6.xml")
    ap.add_argument("--sheet-name", default="Test Case Specification 測試用例規範")
    ap.add_argument("--tmp", type=Path,
                    default=Path("features/privacy/data/roundtrip"))
    args = ap.parse_args()

    args.tmp.mkdir(parents=True, exist_ok=True)
    original = args.tmp / "original.xlsx"
    shutil.copy(args.workbook, original)
    base = probe(original, args.sheet_xml)
    print(f"baseline: {len(base['members'])} zip members, "
          f"x14 DV {base['x14_dv']}, classic DV {base['classic_dv']}")

    via_openpyxl = args.tmp / "via_openpyxl.xlsx"
    openpyxl_roundtrip(original, via_openpyxl, args.sheet_name)
    ok_openpyxl = report("openpyxl load/save", base,
                         probe(via_openpyxl, args.sheet_xml))

    via_surgical = args.tmp / "via_surgical.xlsx"
    surgical_roundtrip(original, via_surgical, args.sheet_xml)
    ok_surgical = report("zip-level surgical splice", base,
                         probe(via_surgical, args.sheet_xml))

    wb = openpyxl.load_workbook(via_surgical)
    written = wb[args.sheet_name]["I10"].value
    print(f"\nsurgical write read back: I10 = {written!r}")

    print("\nverdict: P7 must use the surgical path"
          if ok_surgical and not ok_openpyxl else "\nverdict: re-examine")


if __name__ == "__main__":
    main()
