#!/usr/bin/env python3
"""Build the spec knowledge base for TC generation.

The Media HMI PDF is a scanned slide deck (no extractable text), so:
  1. Spec TEXT  comes from the SYS1 Polarion export xlsx (Outline Number ==
     the section numbering used by 037's HMI Source ID).
  2. Spec IMAGES come from rendering each PDF page to PNG.
  3. section -> page mapping is built by OCR-ing each page and matching the
     item codes (e.g. "USB1)", "BT1.2.1)", "MW9)") that lead every SYS1
     description.

Outputs (under --out):
  spec_sections.json    {outline: {text, code}}
  spec_pages/page_NN.png
  page_ocr/page_NN.txt
  page_index.json       [{page, png, header, codes:[...]}]
  section_manifest.json {outline: {text, code, pages:[...]}}

Usage:
    python split_spec.py --sys1 <SYS1.xlsx> --pdf <MediaHMI.pdf> --out data/
    # add --skip-render / --skip-ocr to reuse previous artifacts
"""
import argparse
import json
import re
from pathlib import Path

import fitz  # pymupdf
import openpyxl
import pytesseract
from PIL import Image

# Item codes leading spec sentences: MN1) USB1) BT1.2.1) SA3.) MW9) PT2.1) ...
CODE_RE = re.compile(r"\b([A-Z]{1,4}\d+(?:\.\d+)*)\s*[).]")
DPI = 150


def build_spec_sections(sys1_path: str) -> dict:
    wb = openpyxl.load_workbook(sys1_path, read_only=True)
    ws = wb["Basic Report"]
    sections = {}
    for r in ws.iter_rows(min_row=2, values_only=True):
        outline = str(r[2] or "").strip()
        if not outline:
            continue
        text = str(r[3] or "").strip()
        m = CODE_RE.match(text)
        sections[outline] = {"text": text, "code": m.group(1) if m else ""}
    return sections


def render_pages(pdf_path: str, out_dir: Path) -> list:
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    pngs = []
    for pno in range(doc.page_count):
        p = out_dir / f"page_{pno + 1:02d}.png"
        if not p.exists():
            doc[pno].get_pixmap(dpi=DPI).save(str(p))
        pngs.append(p)
    return pngs


def ocr_pages(pngs: list, ocr_dir: Path) -> list:
    ocr_dir.mkdir(parents=True, exist_ok=True)
    index = []
    for png in pngs:
        txt_path = ocr_dir / (png.stem + ".txt")
        if txt_path.exists():
            text = txt_path.read_text()
        else:
            text = pytesseract.image_to_string(Image.open(png))
            txt_path.write_text(text)
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        header = lines[0] if lines else ""
        codes = sorted(set(CODE_RE.findall(text)))
        index.append({
            "page": int(png.stem.split("_")[1]),
            "png": png.name,
            "header": header,
            "codes": codes,
        })
    return index


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", s.lower())


def build_manifest(sections: dict, page_index: list, ocr_dir: Path) -> dict:
    code_to_pages = {}
    for entry in page_index:
        for c in entry["codes"]:
            code_to_pages.setdefault(c, []).append(entry["page"])

    # normalized full OCR text per page, for phrase fallback
    page_text = {
        e["page"]: _norm((ocr_dir / f"page_{e['page']:02d}.txt").read_text())
        for e in page_index
    }

    def by_adjacent_code(code: str) -> list:
        """OCR sometimes drops a code; sequential sibling codes share pages."""
        m = re.match(r"([A-Z]+)(\d+)$", code)
        if not m:
            return []
        prefix, n = m.group(1), int(m.group(2))
        pages = []
        for d in (1, -1, 2, -2):
            pages += code_to_pages.get(f"{prefix}{n + d}", [])
        return sorted(set(pages))

    def by_phrase(text: str) -> list:
        words = _norm(text).split()
        if len(words) < 8:
            return []
        # use a distinctive 6-word window from mid-sentence (skip the code)
        for start in (2, 5, 8):
            phrase = " ".join(words[start:start + 6])
            if len(phrase) < 20:
                continue
            hits = [p for p, t in page_text.items() if phrase in t]
            if 0 < len(hits) <= 3:
                return hits
        return []

    manifest = {}
    for outline, info in sections.items():
        code = info["code"]
        pages = code_to_pages.get(code, []) if code else []
        if not pages and code and "." in code:
            # parent code, e.g. BT1.2.1 -> BT1.2 -> BT1
            parts = code.split(".")
            for cut in range(len(parts) - 1, 0, -1):
                pages = code_to_pages.get(".".join(parts[:cut]), [])
                if pages:
                    break
        if not pages and code:
            pages = by_adjacent_code(code)
        if not pages:
            pages = by_phrase(info["text"])
        manifest[outline] = {"text": info["text"], "code": code, "pages": pages}
    return manifest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sys1", required=True)
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", default="data")
    ap.add_argument("--skip-render", action="store_true")
    ap.add_argument("--skip-ocr", action="store_true")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    sections = build_spec_sections(args.sys1)
    (out / "spec_sections.json").write_text(
        json.dumps(sections, ensure_ascii=False, indent=2))
    print(f"spec_sections: {len(sections)} outline entries")

    pngs = (sorted((out / "spec_pages").glob("page_*.png"))
            if args.skip_render else render_pages(args.pdf, out / "spec_pages"))
    print(f"pages rendered: {len(pngs)}")

    page_index = ocr_pages(pngs, out / "page_ocr")
    (out / "page_index.json").write_text(
        json.dumps(page_index, ensure_ascii=False, indent=2))

    manifest = build_manifest(sections, page_index, out / "page_ocr")
    (out / "section_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2))
    mapped = sum(1 for v in manifest.values() if v["pages"])
    print(f"section_manifest: {len(manifest)} sections, {mapped} mapped to pages")


if __name__ == "__main__":
    main()
