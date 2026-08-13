#!/usr/bin/env python3
"""Zip-level surgical xlsx emit — R16-1/R16-2 remediation.

`openpyxl`'s `Workbook.save()` does not write the file it read; it writes a
file openpyxl can describe. Everything outside its object model is dropped or
regenerated. Measured on the AMFM delivery (R16 §2): 21 zip members lost,
10 added, all six `x14:dataValidation` elements gone — while the row contents
were correct and lint was green, which is exactly why the loss went unseen.

This module keeps openpyxl as the *calculation* layer and removes it from the
*emit* layer:

1. the caller mutates an openpyxl workbook as before
2. `surgical_save` diffs that workbook against a fresh read of the source,
   yielding a cell-level change set
3. the change set is applied to the SOURCE sheet XML as text, and every other
   zip member is copied byte-for-byte

What this preserves that `save()` does not: x14 (extension) data validations,
printer settings, SmartArt under `xl/diagrams/`, legacy VML comment drawings,
embedded media in its original encoding, `sharedStrings.xml`, and the shared
formula groups of untouched rows.

Deliberately NOT preserved, because the caller changed them: the target
sheets' XML. `verify_structure` enforces that the difference stops there —
zip member set equal, data-validation counts equal per sheet, only the
patched sheets' XML allowed to differ. A violation is canon §0 item 3
(invariant breach) and aborts; it is never downgraded to a warning.

Usage (see features/amfm/scripts/write_back.py):

    wb = openpyxl.load_workbook(src)
    ...mutate...
    report = surgical_save(wb, src, out)      # raises StructureError on drift
"""
from __future__ import annotations

import re
import shutil
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

# Cell reference: column letters + row digits.
CELL_RE = re.compile(r'<c r="([A-Z]+)(\d+)"([^>]*?)(?:/>|>(.*?)</c>)', re.S)
ROW_RE = re.compile(r'<row r="(\d+)"([^>]*?)(?:/>|>(.*?)</row>)', re.S)
DIMENSION_RE = re.compile(r'<dimension ref="[^"]*"/>')
CLASSIC_DV_RE = re.compile(r"<dataValidation[ >]")
X14_DV_RE = re.compile(r"<x14:dataValidation[ >]")


class StructureError(RuntimeError):
    """A structural invariant failed. Not recoverable by relaxing the check."""


# ------------------------------------------------------------ column helpers

def col_to_idx(letters: str) -> int:
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - 64)
    return n


def idx_to_col(idx: int) -> str:
    s, n = "", idx
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


# ------------------------------------------------------------ sheet ↔ member

def sheet_members(path: Path) -> dict[str, str]:
    """Worksheet name -> zip member path, resolved through workbook rels.

    Resolved rather than assumed: sheet order in `workbook.xml` is display
    order, which is not the `sheetN.xml` numbering. The AMFM workbook happens
    to agree; relying on that would be luck.
    """
    with zipfile.ZipFile(path) as z:
        book = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
    target = {}
    for rel in re.finditer(r"<Relationship\b([^>]*)/>", rels):
        attrs = rel.group(1)
        rid = re.search(r'Id="([^"]+)"', attrs)
        tgt = re.search(r'Target="([^"]+)"', attrs)
        if rid and tgt:
            target[rid.group(1)] = tgt.group(1)
    out = {}
    for m in re.finditer(r"<sheet\b([^>]*?)/?>", book):
        attrs = m.group(1)
        name = re.search(r'name="([^"]*)"', attrs)
        rid = re.search(r'r:id="([^"]*)"', attrs)
        if not (name and rid and rid.group(1) in target):
            continue
        tgt = target[rid.group(1)].lstrip("/")
        if not tgt.startswith("xl/"):
            tgt = "xl/" + tgt
        out[_unescape(name.group(1))] = tgt
    return out


def _unescape(s: str) -> str:
    return (s.replace("&amp;", "&").replace("&lt;", "<")
             .replace("&gt;", ">").replace("&quot;", '"'))


# ------------------------------------------------------------------- diffing

def diff_cells(original, mutated) -> dict[str, dict[tuple[int, int], object]]:
    """{sheet name: {(row, col): new value}} for every cell that changed.

    Compares openpyxl values, so a formula compares as its string. Shared
    formulas expand on read, which is what makes an untouched shared-formula
    row compare equal and therefore stay untouched in the XML.
    """
    changes: dict[str, dict[tuple[int, int], object]] = {}
    for name in mutated.sheetnames:
        if name not in original.sheetnames:
            raise StructureError(f"sheet {name!r} is new; surgical emit only "
                                 "patches sheets that exist in the source")
        old, new = original[name], mutated[name]
        max_row = max(old.max_row, new.max_row)
        max_col = max(old.max_column, new.max_column)
        sheet_changes: dict[tuple[int, int], object] = {}
        for r in range(1, max_row + 1):
            for c in range(1, max_col + 1):
                a = old.cell(r, c).value if r <= old.max_row and c <= old.max_column else None
                b = new.cell(r, c).value
                if a != b:
                    sheet_changes[(r, c)] = b
        if sheet_changes:
            changes[name] = sheet_changes
    return changes


# ------------------------------------------------------------- serialisation

def _cell_xml(coord: str, style_attr: str, value) -> str:
    """One `<c>` element. `style_attr` carries the source cell's `s="…"`.

    Strings go out as inline strings: the source `sharedStrings.xml` is copied
    verbatim, so appending to it would mean rewriting it — the one member the
    surgical path most wants to leave alone.
    """
    if value is None or value == "":
        return f'<c r="{coord}"{style_attr}/>'
    if isinstance(value, str) and value.startswith("="):
        return f'<c r="{coord}"{style_attr}><f>{escape(value[1:])}</f></c>'
    if isinstance(value, bool):
        return f'<c r="{coord}"{style_attr} t="b"><v>{int(value)}</v></c>'
    if isinstance(value, (int, float)):
        return f'<c r="{coord}"{style_attr}><v>{value}</v></c>'
    text = escape(str(value))
    return (f'<c r="{coord}"{style_attr} t="inlineStr">'
            f'<is><t xml:space="preserve">{text}</t></is></c>')


def _patch_row(row_xml: str, row_num: int,
               edits: dict[int, object]) -> str:
    """Rebuild one `<row>`'s cells, keeping every untouched cell verbatim."""
    cells: dict[int, str] = {}
    styles: dict[int, str] = {}
    for m in CELL_RE.finditer(row_xml):
        idx = col_to_idx(m.group(1))
        cells[idx] = m.group(0)
        s = re.search(r'\ss="\d+"', m.group(3) or "")
        styles[idx] = s.group(0) if s else ""
    for col, value in edits.items():
        cells[col] = _cell_xml(f"{idx_to_col(col)}{row_num}",
                               styles.get(col, ""), value)
    return "".join(cells[k] for k in sorted(cells))


def _new_row_xml(row_num: int, edits: dict[int, object]) -> str:
    body = "".join(_cell_xml(f"{idx_to_col(c)}{row_num}", "", v)
                   for c, v in sorted(edits.items()))
    return f'<row r="{row_num}">{body}</row>'


def patch_sheet_xml(xml: str, edits: dict[tuple[int, int], object]) -> str:
    """Apply a cell change set to one worksheet's XML."""
    by_row: dict[int, dict[int, object]] = {}
    for (r, c), v in edits.items():
        by_row.setdefault(r, {})[c] = v

    existing: dict[int, tuple[int, int, str, str]] = {}
    for m in ROW_RE.finditer(xml):
        existing[int(m.group(1))] = (m.start(), m.end(), m.group(2) or "",
                                     m.group(3) or "")

    # Rewrite existing rows from the end, so earlier offsets stay valid.
    out = xml
    for row_num in sorted(set(by_row) & set(existing), reverse=True):
        start, end, attrs, body = existing[row_num]
        out = (out[:start]
               + f'<row r="{row_num}"{attrs}>'
               + _patch_row(body, row_num, by_row[row_num])
               + "</row>"
               + out[end:])

    # Rows absent from the source are appended in order before </sheetData>.
    added = sorted(set(by_row) - set(existing))
    if added:
        highest = max(existing) if existing else 0
        if any(r < highest for r in added):
            raise StructureError(
                "surgical emit can only append rows past the last source row; "
                f"asked to insert {[r for r in added if r < highest][:5]} "
                f"before row {highest}. Inserting mid-sheet would shift every "
                "row below it, which this path deliberately cannot do")
        block = "".join(_new_row_xml(r, by_row[r]) for r in added)
        if "</sheetData>" in out:
            out = out.replace("</sheetData>", block + "</sheetData>", 1)
        else:
            out = out.replace("<sheetData/>", f"<sheetData>{block}</sheetData>", 1)

    return _fix_dimension(out)


def _fix_dimension(xml: str) -> str:
    """Restate `<dimension>` over the patched sheet's actual extent."""
    max_row, max_col = 0, 0
    for m in ROW_RE.finditer(xml):
        max_row = max(max_row, int(m.group(1)))
        for cm in CELL_RE.finditer(m.group(3) or ""):
            max_col = max(max_col, col_to_idx(cm.group(1)))
    if not max_row:
        return xml
    ref = f"A1:{idx_to_col(max_col or 1)}{max_row}"
    return DIMENSION_RE.sub(f'<dimension ref="{ref}"/>', xml, count=1)


# -------------------------------------------------------------- verification

def _dv_counts(path: Path) -> dict[str, tuple[int, int]]:
    counts = {}
    with zipfile.ZipFile(path) as z:
        for member in z.namelist():
            if member.startswith("xl/worksheets/sheet"):
                xml = z.read(member).decode("utf-8")
                counts[member] = (len(CLASSIC_DV_RE.findall(xml)),
                                  len(X14_DV_RE.findall(xml)))
    return counts


def verify_structure(src: Path, out: Path, patched: set[str]) -> dict:
    """R16 §3.2 invariant. Raises `StructureError`; never warns."""
    with zipfile.ZipFile(src) as a, zipfile.ZipFile(out) as b:
        src_members, out_members = set(a.namelist()), set(b.namelist())
    lost, added = sorted(src_members - out_members), sorted(out_members - src_members)
    if lost or added:
        raise StructureError(
            f"zip member set changed — lost {lost}, added {added}. "
            "The delivered file must carry every part the customer's file "
            "carried (R16-1)")

    before, after = _dv_counts(src), _dv_counts(out)
    bad = {m: (before[m], after[m]) for m in before if before[m] != after[m]}
    if bad:
        raise StructureError(
            f"data-validation counts changed (classic, x14): {bad}. "
            "The dropdowns are part of the controlled form (R16-2)")

    with zipfile.ZipFile(src) as a, zipfile.ZipFile(out) as b:
        differing = sorted(m for m in src_members
                           if a.read(m) != b.read(m))
    unexpected = [m for m in differing if m not in patched]
    if unexpected:
        raise StructureError(
            f"members differ that were not written: {unexpected}. "
            "Only the target sheets' XML may change")

    return {"members": len(src_members), "differing": differing,
            "dv_counts": {m: after[m] for m in sorted(after) if any(after[m])}}


# --------------------------------------------------------------------- emit

def surgical_save(mutated, src: Path, out: Path, *, verify: bool = True) -> dict:
    """Write `mutated`'s cell changes into a byte-for-byte copy of `src`."""
    import openpyxl

    src, out = Path(src), Path(out)
    original = openpyxl.load_workbook(src)
    changes = diff_cells(original, mutated)
    members = sheet_members(src)

    patched: dict[str, str] = {}
    for name, edits in changes.items():
        member = members.get(name)
        if member is None:
            raise StructureError(f"no zip member resolved for sheet {name!r}")
        with zipfile.ZipFile(src) as z:
            xml = z.read(member).decode("utf-8")
        patched[member] = patch_sheet_xml(xml, edits)

    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(
            out, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            data = (patched[info.filename].encode("utf-8")
                    if info.filename in patched else zin.read(info.filename))
            zout.writestr(info, data)

    report = {"sheets_patched": {n: len(e) for n, e in changes.items()},
              "members_patched": sorted(patched)}
    if verify:
        report.update(verify_structure(src, out, set(patched)))
    return report


def copy_unchanged(src: Path, out: Path) -> None:
    """Byte-for-byte copy, for the no-edits case."""
    shutil.copy(src, out)
