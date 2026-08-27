#!/usr/bin/env python3
"""Emit the delivery workbook: copy → normalise → digest → sidecar.

FO §6: the digest goes into the TAG ANNOTATION, never a tracked file, and
`--write` must touch no tracked file — so the output and its `.sha256`
sidecar land in the gitignored `output/`.

Normalisation (zip timestamps + dcterms dates) makes the SHA256 reproducible:
without it the digest changes on every emit and cannot bind a tag to a state.
Ported from `features/amfm/scripts/write_back.py` §reproducible.

**The normaliser rebuilds the zip** (members re-sorted by name, timestamps
zeroed), so the structural counts are re-verified afterwards — a rebuild that
silently dropped the x14 dropdown would otherwise reach the customer.
"""
import hashlib
import re
import shutil
import sys
import zipfile
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
_EPOCH = (1980, 1, 1, 0, 0, 0)
_DCTERMS = re.compile(rb"(<dcterms:(created|modified)[^>]*>)[^<]*(</dcterms:\2>)")
_STAMP = b"2000-01-01T00:00:00Z"


def normalise(path: Path) -> None:
    src = zipfile.ZipFile(path)
    items = sorted(src.infolist(), key=lambda i: i.filename)
    tmp = path.with_suffix(".normalising")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as dst:
        for info in items:
            data = src.read(info.filename)
            if info.filename == "docProps/core.xml":
                data = _DCTERMS.sub(rb"\g<1>" + _STAMP + rb"\g<3>", data)
            new = zipfile.ZipInfo(info.filename, date_time=_EPOCH)
            new.compress_type = zipfile.ZIP_DEFLATED
            new.external_attr = info.external_attr
            dst.writestr(new, data)
    src.close()
    tmp.replace(path)


def counts(p: Path) -> dict:
    pats = {"legacy_dv": rb"<dataValidation[ >]", "x14_dv": rb"<x14:dataValidation[ >]",
            "extLst": rb"<extLst[ >]"}
    with zipfile.ZipFile(p) as z:
        names = z.namelist()
        out = {"members": len(names),
               "sheets": len([n for n in names
                              if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", n)])}
        for k in pats:
            out[k] = 0
        for n in names:
            if n.endswith(".xml"):
                b = z.read(n)
                for k, rx in pats.items():
                    out[k] += len(re.findall(rx, b))
    return out


def main() -> int:
    src = FEAT / "workbook" / "bed_lowering_11.xlsx"
    name = ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
            "Specification & Result_SWQT_BedLowering_20260827.xlsx")
    out = FEAT / "output" / name
    out.parent.mkdir(exist_ok=True)
    shutil.copy(src, out)
    before = counts(out)
    normalise(out)
    after = counts(out)
    print(f"source : {src.name}")
    print(f"output : output/{name}")
    print("\n正規化前後結構計數：")
    bad = 0
    for k in before:
        ok = before[k] == after[k]
        bad += not ok
        print(f"  {k:<10} {before[k]:>4} -> {after[k]:>4}  {'OK' if ok else '**差異**'}")
    if bad:
        print("\n正規化改變了結構計數 —— 停，不產 digest")
        return 1
    # 冪等性：再正規化一次，digest 須不變（否則 tag 綁不住狀態）
    d1 = hashlib.sha256(out.read_bytes()).hexdigest()
    normalise(out)
    d2 = hashlib.sha256(out.read_bytes()).hexdigest()
    print(f"\nsha256          {d1}")
    print(f"重跑正規化後      {d2}")
    print(f"冪等             {'OK — digest 可重現' if d1 == d2 else '**不冪等，digest 綁不住狀態**'}")
    if d1 != d2:
        return 1
    side = out.with_name(out.name + ".sha256")
    side.write_text(f"{d1}  {name}\n", encoding="utf-8")
    print(f"sidecar          output/{side.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
