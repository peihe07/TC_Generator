#!/usr/bin/env python3
"""Build the spec knowledge base for Home HMI TC generation.

Unlike the Media deck (scanned, OCR-only), the Home PDF carries a real text
layer, so page text is extracted directly and OCR is a per-page fallback for
pages that come back empty. Page PNGs are still rendered: the anatomy and
layout pages (VMB/HMB/LSW/SW/SNS figures) carry information that exists only
as graphics, and the generator needs to look at them.

  1. Spec TEXT authority is the SYS1 Polarion export (Outline Number == the
     section numbering used by 037's HMI Source ID suffix).
  2. Spec IMAGES come from rendering each PDF page to PNG.
  3. section -> page mapping matches the item codes (HSD1, HSS4.1, SNS3,
     BSP5.1, ...) that lead every SYS1 description against the page text.
  4. A diff check reports SYS1 sections whose code never appears in the PDF
     and vice versa; both directions are traceability smells worth seeing.

Outputs (under --out):
  spec_sections.json    {outline: {text, code}}
  spec_pages/page_NN.png
  page_text/page_NN.txt
  page_index.json       [{page, source, header, codes:[...], chars}]
  section_manifest.json {outline: {text, code, pages:[...]}}
  spec_diff.json        {sys1_codes_missing_from_pdf, pdf_codes_missing_from_sys1}

Usage:
    python split_spec.py --sys1 <SYS1.xlsx> --pdf <HomeScreen.pdf> --out data/
    # --skip-render reuses previous PNGs; --force-ocr ignores the text layer
"""
import argparse
import json
import re
from pathlib import Path

import fitz  # pymupdf
import openpyxl

# Item codes leading spec sentences: HSD1) HSS4.1) SNS3) BSP5.1) SW7) HS9.0.1)
CODE_RE = re.compile(r"\b([A-Z]{1,4}\d+(?:\.\d+)*)\s*[).]")
# Tokens that match CODE_RE but are release/version noise, not item codes.
CODE_DENYLIST = {"R1", "R2", "SR24", "SR23", "P1", "P2", "A01", "A03"}
# Below this many extracted characters a page is treated as image-only and
# handed to OCR. Cover/section-divider pages legitimately fall here; the
# fallback is cheap and keeps figure-page codes discoverable.
MIN_TEXT_CHARS = 40
DPI = 150


def clean_codes(text: str) -> list[str]:
    return sorted({c for c in CODE_RE.findall(text) if c not in CODE_DENYLIST})


def build_spec_sections(sys1_path: str) -> dict:
    """{outline: {text, code}} from the SYS1 Basic Report sheet."""
    wb = openpyxl.load_workbook(sys1_path, read_only=True)
    ws = wb["Basic Report"]
    sections = {}
    for r in ws.iter_rows(min_row=2, values_only=True):
        outline = str(r[2] or "").strip()
        if not outline:
            continue
        text = str(r[3] or "").strip()
        m = CODE_RE.match(text)
        code = m.group(1) if m and m.group(1) not in CODE_DENYLIST else ""
        sections[outline] = {"text": text, "code": code}
    wb.close()
    if not sections:
        raise SystemExit(f"no outline rows extracted from {sys1_path}")
    return sections


def render_pages(pdf_path: str, out_dir: Path, skip: bool) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    pngs = []
    for pno in range(doc.page_count):
        p = out_dir / f"page_{pno + 1:02d}.png"
        if not (skip or p.exists()):
            doc[pno].get_pixmap(dpi=DPI).save(str(p))
        pngs.append(p)
    doc.close()
    return pngs


def extract_text(pdf_path: str, txt_dir: Path, pngs: list[Path],
                 force_ocr: bool) -> list[dict]:
    """Text layer first, OCR only for pages that come back (near) empty."""
    txt_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    index = []
    for pno in range(doc.page_count):
        page_no = pno + 1
        txt_path = txt_dir / f"page_{page_no:02d}.txt"
        text = "" if force_ocr else doc[pno].get_text().strip()
        source = "text-layer"
        if len(text) < MIN_TEXT_CHARS:
            ocr = ocr_page(pngs[pno]) if pno < len(pngs) else ""
            if len(ocr) > len(text):
                text, source = ocr, "ocr"
            elif not force_ocr:
                source = "text-layer(sparse)"
        txt_path.write_text(text, encoding="utf-8")
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        index.append({
            "page": page_no,
            "png": pngs[pno].name if pno < len(pngs) else "",
            "source": source,
            "chars": len(text),
            "header": lines[0] if lines else "",
            "codes": clean_codes(text),
        })
    doc.close()
    return index


def ocr_page(png: Path) -> str:
    """OCR one rendered page; returns '' when OCR is unavailable."""
    try:
        import pytesseract
        from PIL import Image
    except ImportError:
        return ""
    if not png.exists():
        return ""
    return pytesseract.image_to_string(Image.open(png)).strip()


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", s.lower())


def build_manifest(sections: dict, page_index: list, txt_dir: Path) -> dict:
    code_to_pages: dict[str, list[int]] = {}
    for entry in page_index:
        for c in entry["codes"]:
            code_to_pages.setdefault(c, []).append(entry["page"])

    page_text = {
        e["page"]: _norm((txt_dir / f"page_{e['page']:02d}.txt")
                         .read_text(encoding="utf-8"))
        for e in page_index
    }

    def by_parent_code(code: str) -> list[int]:
        """HSS4.1.2 -> HSS4.1 -> HSS4; sub-items live on the parent's page."""
        parts = code.split(".")
        for cut in range(len(parts) - 1, 0, -1):
            pages = code_to_pages.get(".".join(parts[:cut]))
            if pages:
                return pages
        return []

    def by_adjacent_code(code: str) -> list[int]:
        """Sequential sibling codes share pages; covers extraction dropouts."""
        m = re.match(r"([A-Z]+)(\d+)$", code)
        if not m:
            return []
        prefix, n = m.group(1), int(m.group(2))
        pages: list[int] = []
        for d in (1, -1, 2, -2):
            pages += code_to_pages.get(f"{prefix}{n + d}", [])
        return sorted(set(pages))

    def by_phrase(text: str) -> list[int]:
        words = _norm(text).split()
        if len(words) < 8:
            return []
        for start in (2, 5, 8):
            phrase = " ".join(words[start:start + 6])
            if len(phrase) < 20:
                continue
            hits = [p for p, t in page_text.items() if phrase in t]
            if 0 < len(hits) <= 3:
                return hits
        return []

    def by_heading(text: str) -> list[int]:
        """Chapter rows carry no item code; match their title to a page header.

        Slide headers repeat the chapter title with a brand prefix ("R1 Home
        Screen with Vertical Menu Bar" for chapter "Home Screen with Vertical
        Menu Bar"), so containment either way is a reliable signal.
        """
        title = _norm(text.splitlines()[0] if text else "").strip()
        if len(title) < 8:
            return []
        hits = []
        for e in page_index:
            header = _norm(e["header"]).strip()
            if header and (title in header or header in title):
                hits.append(e["page"])
        return hits

    manifest = {}
    # Shallow outlines first so `4.1` can inherit from `4` in the same pass.
    ordered = sorted(sections.items(),
                     key=lambda kv: (kv[0].count("."), kv[0]))
    for outline, info in ordered:
        code = info["code"]
        pages = code_to_pages.get(code, []) if code else []
        if not pages and code and "." in code:
            pages = by_parent_code(code)
        if not pages and code:
            pages = by_adjacent_code(code)
        if not pages:
            pages = by_phrase(info["text"])
        if not pages and not code:
            pages = by_heading(info["text"])
        if not pages and "." in outline:
            # Image-only sub-rows ("Please refer to the diagram") sit on their
            # chapter's page; inherit rather than leave the generator blind.
            parent = manifest.get(outline.rsplit(".", 1)[0])
            pages = list(parent["pages"]) if parent else []
        manifest[outline] = {"text": info["text"], "code": code,
                             "pages": sorted(set(pages))}
    # Restore SYS1 document order for a stable, diffable artifact.
    return {k: manifest[k] for k in sections}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sys1", required=True)
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", default="data")
    ap.add_argument("--skip-render", action="store_true")
    ap.add_argument("--force-ocr", action="store_true",
                    help="ignore the text layer (Media-style OCR pipeline)")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    sections = build_spec_sections(args.sys1)
    (out / "spec_sections.json").write_text(
        json.dumps(sections, ensure_ascii=False, indent=2))
    print(f"spec_sections: {len(sections)} outline entries")

    pngs = render_pages(args.pdf, out / "spec_pages", args.skip_render)
    print(f"pages: {len(pngs)} ({'reused' if args.skip_render else 'rendered'})")

    page_index = extract_text(args.pdf, out / "page_text", pngs, args.force_ocr)
    (out / "page_index.json").write_text(
        json.dumps(page_index, ensure_ascii=False, indent=2))
    by_source: dict[str, int] = {}
    for e in page_index:
        by_source[e["source"]] = by_source.get(e["source"], 0) + 1
    print("text extraction: " + ", ".join(f"{k}={v}" for k, v in by_source.items()))

    manifest = build_manifest(sections, page_index, out / "page_text")
    (out / "section_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2))
    mapped = sum(1 for v in manifest.values() if v["pages"])
    print(f"section_manifest: {len(manifest)} sections, {mapped} mapped to pages")

    sys1_codes = {v["code"] for v in sections.values() if v["code"]}
    pdf_codes = {c for e in page_index for c in e["codes"]}
    diff = {
        "sys1_codes_missing_from_pdf": sorted(sys1_codes - pdf_codes),
        "pdf_codes_missing_from_sys1": sorted(pdf_codes - sys1_codes),
    }
    (out / "spec_diff.json").write_text(
        json.dumps(diff, ensure_ascii=False, indent=2))
    print(f"diff: {len(diff['sys1_codes_missing_from_pdf'])} SYS1 codes absent "
          f"from PDF, {len(diff['pdf_codes_missing_from_sys1'])} PDF codes "
          f"absent from SYS1")
    if diff["sys1_codes_missing_from_pdf"]:
        print("  SYS1-only: " + ", ".join(diff["sys1_codes_missing_from_pdf"]))


if __name__ == "__main__":
    main()
