#!/usr/bin/env python3
"""spec_mode extraction-capability probe (handoff 01 step 11, canon §3).

Measures what each of the three source forms can actually yield, so the
spec_mode choice rests on measurement rather than on the scaffold's proposal:

  CFTS_020 docx  — paragraph/table yield, clause-id inventory, and whether an
                   id found in the body is also reachable from a heading
                   (index) — the 全文 id 數 vs 索引數 comparison
  SYS3 SYSAD docx — same, plus image count (a SYSAD is often mostly figures)
  SYS2 xlsx      — Basic Report field structure already measured in
                   recount_sys2.py; here only the outline/section-anchor
                   question is asked
"""
import re
import zipfile
from collections import Counter
from pathlib import Path

import docx
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
CFTS = ROOT / "inputs" / ("R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 "
                          "ICS and DCSD _20260310-1533.docx")
SYS3 = ROOT / "inputs" / ("SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System "
                          "Architectural Design_SYSAD_v1.0.docx")
SYS2 = ROOT / "inputs" / ("SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System"
                          "_Accepted & Released.xlsx")

# Clause-id shapes observed in this corpus. PSCFTS020-1-45-1 is the Melco ID
# form that 037's Excluded sheet carries (R-DM4); the outline form is the
# numbered-heading form a spec_reference would be built from under mode B/D.
ID_PATTERNS = {
    "melco (PSCFTS020-n-n-n)": r"PSCFTS\d{3}-\d+-\d+(?:-\d+)?",
    "outline heading (n.n / n.n.n)": r"(?m)^\s*(\d+(?:\.\d+){1,3})\s+\S",
}


def probe_docx(path, label):
    print(f"\n## {label} — {path.name}")
    d = docx.Document(path)
    paras = [p.text for p in d.paragraphs]
    nonempty = [p for p in paras if p.strip()]
    print(f"paragraphs: {len(paras)} (non-empty {len(nonempty)})")
    print(f"tables: {len(d.tables)}")
    cells = []
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                if c.text.strip():
                    cells.append(c.text)
    print(f"non-empty table cells: {len(cells)}")
    with zipfile.ZipFile(path) as z:
        media = [n for n in z.namelist() if n.startswith("word/media/")]
    print(f"embedded media files: {len(media)}")

    body = "\n".join(nonempty + cells)
    print(f"extracted characters: {len(body)}")

    heads = [p for p in d.paragraphs
             if p.style is not None and str(p.style.name).lower()
             .startswith("heading")]
    print(f"paragraphs with a Heading style: {len(heads)}")
    head_text = "\n".join(h.text for h in heads)

    for name, pat in ID_PATTERNS.items():
        full = re.findall(pat, body)
        idx = re.findall(pat, head_text)
        print(f"  id form {name}: 全文 {len(full)} 次 / "
              f"{len(set(full))} 相異 | 標題(索引) {len(set(idx))} 相異")
        if set(full):
            sample = sorted(set(full))[:5]
            print(f"     sample: {sample}")
    return body


def main():
    print("# spec_mode extraction probe")
    print("engine: python-docx (paragraphs + table cells), zipfile for media")

    cfts = probe_docx(CFTS, "CFTS_020 本文 (candidate spec source, mode D)")
    sys3 = probe_docx(SYS3, "SYS3 SYSAD (candidate, traceability/architecture)")

    print("\n## SYS2 Polarion export — outline anchor availability")
    wb = openpyxl.load_workbook(SYS2, read_only=True, data_only=True)
    grid = [list(r) for r in wb["Basic Report"].iter_rows(values_only=True)]
    wb.close()
    head = [" ".join(str(h or "").split()) for h in grid[0]]
    doc_col = [i for i, h in enumerate(head) if "Document ID" in h]
    src_col = [i for i, h in enumerate(head) if "Source Requirement items" in h]
    print(f"columns present: Document ID={bool(doc_col)} "
          f"Source Requirement items={bool(src_col)}")
    for label, cols in (("Document ID", doc_col),
                        ("Source Requirement items", src_col)):
        if not cols:
            continue
        vals = [" ".join(str(r[cols[0]] or "").split()) for r in grid[1:]
                if str(r[0] or "").strip()]
        nonblank = [v for v in vals if v]
        print(f"  {label}: {len(nonblank)}/{len(vals)} non-blank, "
              f"{len(set(nonblank))} distinct")
        for v, n in Counter(nonblank).most_common(5):
            print(f"     {v!r} x{n}")

    print("\n## 交叉：SYS2 Melco ID 是否可在 CFTS 本文中定位")
    wb = openpyxl.load_workbook(SYS2, read_only=True, data_only=True)
    grid = [list(r) for r in wb["Basic Report"].iter_rows(values_only=True)]
    wb.close()
    mcol = [i for i, h in enumerate(head) if h == "SYS2 Melco ID"][0]
    toks = set()
    for r in grid[1:]:
        if str(r[0] or "").strip():
            for t in re.split(r"[,\s;]+", str(r[mcol] or "")):
                if t.strip():
                    toks.add(t.strip())
    hit = sum(1 for t in toks if t in cfts)
    print(f"  SYS2 Melco tokens: {len(toks)}; found verbatim in CFTS body: {hit}")
    hit3 = sum(1 for t in toks if t in sys3)
    print(f"  found verbatim in SYS3 body: {hit3}")


if __name__ == "__main__":
    main()
