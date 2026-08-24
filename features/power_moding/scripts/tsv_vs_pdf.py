#!/usr/bin/env python3
"""18 包步驟 6 —— `layer3_sections.tsv` 之 `section_title` vs PDF（只量測，不改）。

17 §5.4 第 1 項：**R-PMH50（`source_clause` 不取 SYS1）未回頭套用於
`layer3_sections.tsv`** —— 其 `section_title`／`chapter_title` 全部取自
SYS1 匯出（`build_layer3_sections.py` 之 `outline_title`），
**而 lint 之 profile §3.4 正是拿該 TSV 之 outline 對照**。

本檔對 48 leaf 逐一比對其 `section_title`（SYS1 側，已截 120 字元）
是否**逐字出現於 PDF 全文**（R-PMH66：判定為二值）。
不符者列為殘餘，逐則人讀 —— **不由任何門檻自動判為「相符」**。

用法:
    python scripts/tsv_vs_pdf.py
"""
import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "layer3_sections.tsv"
PDF_TXT = ROOT / "sandbox" / "spec.txt"

LIMITS = [
    "只比對 `section_title`（SYS1 側**已截 120 字元**之前綴）—— **截斷之後的內容一律不看**",
    "**`chapter_title` 不在本檔之比對範圍** —— 章標題不對應任何 leaf",
    "PDF 側為 `pdftotext -layout` 之交錯文字；**章 9 之矩陣區已知不可用**（A-PMH16(d)）",
    "**只驗字之有無，不驗語意** —— SYS1 之同義改寫會被判為不符，改寫錯誤會被判為相符",
    "**本檔不改任何檔** —— 其輸出為量測，處置屬待裁（17 §5.4 第 1 項）",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


def norm(t: str) -> str:
    t = str(t).replace("_x000D_", " ")
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'),
                 ("”", '"'), ("…", "..."), ("–", "-"), ("—", "-")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()


def pdf_blocks() -> str:
    """PyMuPDF block 層之萃取 —— p9 之 `PM1)` 為單一區塊，不與矩陣交錯。

    **不作預設** —— 改預設來源屬判準變更，須另立條文（A-PMH16(d)）。
    """
    import fitz
    import yaml
    cfg = yaml.safe_load((ROOT / "feature.yaml").read_text(encoding="utf-8"))
    d = fitz.open(ROOT / cfg["paths"]["spec_pdf"])
    return norm(" ".join(b[4] for pg in d for b in pg.get_text("blocks")))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--block", action="store_true",
                    help="PDF 側改用 PyMuPDF block 層萃取（不與矩陣交錯）")
    a = ap.parse_args()
    if a.block:
        pdf = pdf_blocks()
        src = "PyMuPDF block 層"
    else:
        pdf = norm(PDF_TXT.read_text(errors="replace"))
        src = "`pdftotext -layout`（現行預設）"
    rows = list(csv.DictReader(TSV.open(encoding="utf-8"), delimiter="\t"))
    print("=== `layer3_sections.tsv` 之 `section_title` vs PDF（18 包步驟 6）===")
    print(f"leaf = **{len(rows)}**；PDF 側 = {src}，{len(pdf)} 字元\n")
    bad = []
    for r in rows:
        t = norm(r["section_title"])
        if t and t not in pdf:
            bad.append(r)
    by_ch: dict[str, list] = {}
    for r in rows:
        by_ch.setdefault(r["chapter"], []).append(r)
    print(f"{'章':>3} {'leaf':>5} {'不符':>5}")
    for ch in sorted(by_ch, key=int):
        n = sum(1 for r in by_ch[ch] if r in bad)
        print(f"{ch:>3} {len(by_ch[ch]):>5} {n:>5}"
              + ("" if n == 0 else "   ← 見下"))
    print(f"\n**逐字不符者 = {len(bad)} / {len(rows)}**")
    for r in bad:
        t = norm(r["section_title"])
        print(f"\n  {r['swe_requirement_id']}  outline {r['outline_number']}"
              f"（p{r['pdf_page']}）")
        print(f"    SYS1：{t}")
    print_limits()
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
