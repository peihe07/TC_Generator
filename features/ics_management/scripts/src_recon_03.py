#!/usr/bin/env python3
"""下放包 03 作業 F 偵察腳本（只讀，不改任何素材）。

F-1: spec-index/sources/ 四本 HMI L&F 之目次／章節標題關鍵詞命中。
F-2: features/audio_mgmt/inputs/ CFTS019 七件之音量階數域與 VOLUME POP_UP 命中。

抽取法：PDF 用 pdfplumber extract_text（逐頁），xlsx 用 openpyxl read_only，
docx 用 zipfile 讀 word/document.xml 後剝 XML tag。
關鍵詞比對一律大小寫不敏感（re.IGNORECASE）。
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path("/Users/peihe/Work_Projects/TC_Generator")

F1_KEYWORDS = [
    "knob", "volume", "browse", "tune", "screen off", "power",
    "enter", "back", "menu bar", "app drawer", "camera",
    "rear view", "reverse",
]

F2_KEYWORDS = [
    "VOLUME POP_UP", "volume level", "volume step", "detent",
    "pop-up", "popup", "pop up", "timeout",
    "volume range", "max volume", "0-63", "0~63",
]


def pdf_pages(path):
    """回傳 [(頁次, 該頁文字)]。"""
    import pdfplumber
    out = []
    with pdfplumber.open(path) as doc:
        for i, page in enumerate(doc.pages, 1):
            out.append((i, page.extract_text() or ""))
    return out


def xlsx_cells(path):
    """回傳 [(sheet名, 儲存格座標, 文字)]。"""
    import openpyxl
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if isinstance(cell.value, str) and cell.value.strip():
                    yield ws.title, cell.coordinate, cell.value
    wb.close()


def docx_paragraphs(path):
    """回傳 [(段落序號, 文字)]，直接剝 word/document.xml。"""
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8", "replace")
    # 以段落切分後移除所有 XML tag
    paras = re.split(r"</w:p>", xml)
    out = []
    for i, p in enumerate(paras, 1):
        text = re.sub(r"<[^>]+>", "", p)
        text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        if text.strip():
            out.append((i, text.strip()))
    return out


def hits(text, keywords):
    """回傳該段文字命中的關鍵詞集合。"""
    found = []
    for kw in keywords:
        if re.search(re.escape(kw), text, re.IGNORECASE):
            found.append(kw)
    return found


def mode_f1(paths):
    for path in paths:
        p = Path(path)
        print(f"\n########## {p.name}")
        try:
            pages = pdf_pages(p)
        except Exception as exc:  # noqa: BLE001
            print(f"  EXTRACT_ERROR: {exc}")
            continue
        total = sum(len("".join(t.split())) for _, t in pages)
        print(f"  pages={len(pages)} nonws_chars={total}")
        if total == 0:
            print("  NO_TEXT_LAYER")
            continue
        for pno, text in pages:
            if not text.strip():
                continue
            lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
            found = hits(text, F1_KEYWORDS)
            title = lines[0] if lines else ""
            print(f"  --- p.{pno} | TITLE: {title[:110]}")
            if found:
                print(f"      HITS: {', '.join(found)}")
            for ln in lines[1:]:
                if hits(ln, F1_KEYWORDS):
                    print(f"      L: {ln[:160]}")


def mode_f2(paths):
    for path in paths:
        p = Path(path)
        print(f"\n########## {p.name}")
        suf = p.suffix.lower()
        try:
            if suf == ".pdf":
                for pno, text in pdf_pages(p):
                    for ln in [x.strip() for x in text.splitlines() if x.strip()]:
                        f = hits(ln, F2_KEYWORDS)
                        if f:
                            print(f"  p.{pno} [{','.join(f)}] {ln[:300]}")
            elif suf == ".xlsx":
                for sheet, coord, val in xlsx_cells(p):
                    f = hits(val, F2_KEYWORDS)
                    if f:
                        flat = " ".join(val.split())
                        print(f"  [{sheet}]{coord} [{','.join(f)}] {flat[:400]}")
            elif suf == ".docx":
                for idx, text in docx_paragraphs(p):
                    f = hits(text, F2_KEYWORDS)
                    if f:
                        print(f"  para{idx} [{','.join(f)}] {text[:400]}")
            else:
                print(f"  UNSUPPORTED: {suf}")
        except Exception as exc:  # noqa: BLE001
            print(f"  EXTRACT_ERROR: {exc}")


if __name__ == "__main__":
    mode = sys.argv[1]
    targets = sys.argv[2:]
    if mode == "f1":
        mode_f1(targets)
    elif mode == "f2":
        mode_f2(targets)
    else:
        raise SystemExit("usage: src_recon_03.py {f1|f2} <files...>")
