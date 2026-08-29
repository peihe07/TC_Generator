#!/usr/bin/env python3
"""下放包 04 作業 D 偵察腳本（唯讀，不改任何素材）。

依 R-ICS21(c)：只列材料不判採用，不充 verbatim 來源、不充錨。

目標二本（spec-index/sources/）：
  1. Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf
  2. HeadUnitCameraSystems HMI Logic and Flow R1 SR24 Post 2A v7 (February 10th, 2023).pdf

抽取法：pdftotext 與 pdfplumber 雙工具逐頁。二者逐頁非空白字元皆 0 者記
NO_TEXT_LAYER，不做 OCR、不強解。

另做去連字號重掃：PDF 常見 "pop-\nup" 這類斷行，逐行掃描會漏命中。
每頁另備三種正規化文本：
  raw      原文
  dehyph   移除 "-\n"（含後續縮排）後之文本
  flat     dehyph 再把所有空白（含換行）壓成單一空格

關鍵詞比對一律大小寫不敏感。
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/Users/peihe/Work_Projects/TC_Generator")
SRC = ROOT / "spec-index" / "sources"

DOCS = {
    "popup_matrix": "Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf",
    "hu_camera": (
        "HeadUnitCameraSystems HMI Logic and Flow R1 SR24 Post 2A v7 "
        "(February 10th, 2023).pdf"
    ),
}

KEYWORDS = {
    "popup_matrix": [
        "VOLUME POP_UP", "VOLUME POP-UP", "VOLUME POPUP", "VOLUME POP UP",
        "volume", "priority", "popup", "pop up", "pop-up",
        "mute", "timeout", "dismiss", "duration",
    ],
    "hu_camera": [
        "rear view", "rearview", "rear camera", "backup cam", "reverse",
        "RVC", "camera transition", "PAM", "gear", "park",
    ],
}

# VOLUME POP_UP 之寬鬆樣式：VOLUME 後接任意分隔符再接 POP 再接分隔符再接 UP
VOL_POPUP_RE = re.compile(r"volume[\s_\-]*pop[\s_\-]*up", re.IGNORECASE)


def sha256(path: Path) -> str:
    """實算 sha256（與 shasum -a 256 一致）。"""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def pages_pdftotext(path: Path) -> list[str]:
    """pdftotext -layout 逐頁文本（以 form feed 切頁）。"""
    res = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"],
        capture_output=True, check=True,
    )
    text = res.stdout.decode("utf-8", "replace")
    pages = text.split("\f")
    # 末尾常多出一個空段
    if pages and pages[-1].strip() == "":
        pages = pages[:-1]
    return pages


def pages_pdfplumber(path: Path) -> list[str]:
    """pdfplumber extract_text 逐頁文本。"""
    import pdfplumber
    out = []
    with pdfplumber.open(str(path)) as doc:
        for page in doc.pages:
            out.append(page.extract_text() or "")
    return out


def normalize(text: str) -> dict[str, str]:
    """回傳三種正規化文本。"""
    dehyph = re.sub(r"-[ \t]*\n[ \t]*", "", text)
    flat = re.sub(r"\s+", " ", dehyph)
    return {"raw": text, "dehyph": dehyph, "flat": flat}


def nonspace(text: str) -> int:
    """非空白字元數。"""
    return len(re.sub(r"\s", "", text))


def scan(doc_key: str, path: Path) -> dict:
    """單本偵察，回傳結構化結果。"""
    pt = pages_pdftotext(path)
    pp = pages_pdfplumber(path)
    n = max(len(pt), len(pp))
    pt += [""] * (n - len(pt))
    pp += [""] * (n - len(pp))

    kws = KEYWORDS[doc_key]
    pages = []
    for i in range(n):
        # 兩工具文本合併掃描（各自獨立記非空白字元數）
        merged = pt[i] + "\n" + pp[i]
        norms = normalize(merged)
        hits = {}
        for kw in kws:
            forms = []
            for form, txt in norms.items():
                if kw.lower() in txt.lower():
                    forms.append(form)
            if forms:
                hits[kw] = forms
        vol = [m.group(0) for m in VOL_POPUP_RE.finditer(norms["flat"])]
        pages.append({
            "page": i + 1,
            "ns_pdftotext": nonspace(pt[i]),
            "ns_pdfplumber": nonspace(pp[i]),
            "no_text_layer": nonspace(pt[i]) == 0 and nonspace(pp[i]) == 0,
            "hits": hits,
            "vol_popup_loose": vol,
            "first_lines": [
                ln.strip() for ln in pt[i].splitlines() if ln.strip()
            ][:4],
            "flat": norms["flat"],
        })

    return {
        "key": doc_key,
        "filename": path.name,
        "sha256": sha256(path),
        "size": path.stat().st_size,
        "pages_pdftotext": len(pt),
        "pages_pdfplumber": len(pp),
        "pages": pages,
    }


def main() -> int:
    out = {}
    for key, name in DOCS.items():
        path = SRC / name
        if not path.exists():
            print(f"MISSING: {path}", file=sys.stderr)
            return 1
        out[key] = scan(key, path)
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
