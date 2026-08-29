#!/usr/bin/env python3
"""下放包 07 作業 H 偵察腳本（唯讀，不改任何素材）。

依 R-ICS21(c)：只列材料不判採用，不充 verbatim 來源、不充錨。

目標一本（spec-index/sources/）：
  Notifications HMI Logic and Flow R1L-R (Feb 13 2026).pdf

抽取法：pdftotext 與 pdfplumber 雙工具逐頁。二者逐頁非空白字元皆 0 者記
NO_TEXT_LAYER，不做 OCR、不強解。

A-ICS32：前輪實測發現漏命中的真因是「純換行斷詞」（如 Rear / View 各據一
行），不只是連字號。故每頁備四種正規化文本，逐式各掃一次並記錄命中形態：
  raw      原文
  dehyph   去連字號：移除 "-\\n"（含前後縮排）
  flatnl   壓平換行：僅把換行（及其兩側縮排）換成單一空格，不動連字號
  flat     dehyph + 全空白壓平（最寬鬆）

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

DOC = "Notifications HMI Logic and Flow R1L-R (Feb 13 2026).pdf"

# 下放包指定關鍵詞（大小寫不敏感）
KEYWORDS = [
    "VOLUME POP_UP", "VOLUME POP-UP", "VOLUME POPUP", "VOLUME POP UP",
    "volume", "mute", "timeout", "duration", "dismiss", "priority",
]

# 「是否即 Pop-up List Notification」之自稱／結構對應線索詞
SELF_REF = [
    "Pop-up List Notification", "Pop up List Notification",
    "Popup List Notification", "Pop-up List", "Pop Up List",
    "Priority Matrix", "Notifications HMI", "Cat.", "Category",
    "X button", "5 sec", "5 second",
]

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
    """回傳四種正規化文本（見模組 docstring）。"""
    dehyph = re.sub(r"-[ \t]*\n[ \t]*", "", text)
    flatnl = re.sub(r"[ \t]*\n[ \t]*", " ", text)
    flat = re.sub(r"\s+", " ", dehyph)
    return {"raw": text, "dehyph": dehyph, "flatnl": flatnl, "flat": flat}


def nonspace(text: str) -> int:
    """非空白字元數。"""
    return len(re.sub(r"\s", "", text))


def excerpt(text: str, needle: str, span: int = 160) -> list[str]:
    """逐字照錄命中片段（前後各 span 字元）。"""
    out = []
    low = text.lower()
    nl = needle.lower()
    start = 0
    while len(out) < 6:
        i = low.find(nl, start)
        if i < 0:
            break
        a = max(0, i - span)
        b = min(len(text), i + len(needle) + span)
        out.append(text[a:b])
        start = i + len(needle)
    return out


def scan(path: Path) -> dict:
    """單本偵察，回傳結構化結果。"""
    pt = pages_pdftotext(path)
    pp = pages_pdfplumber(path)
    n = max(len(pt), len(pp))
    pt += [""] * (n - len(pt))
    pp += [""] * (n - len(pp))

    pages = []
    for i in range(n):
        merged = pt[i] + "\n" + pp[i]
        norms = normalize(merged)
        hits = {}
        for kw in KEYWORDS:
            forms = [f for f, t in norms.items() if kw.lower() in t.lower()]
            if forms:
                hits[kw] = {
                    "forms": forms,
                    "excerpts": excerpt(norms["flat"], kw),
                }
        srefs = {}
        for kw in SELF_REF:
            forms = [f for f, t in norms.items() if kw.lower() in t.lower()]
            if forms:
                srefs[kw] = {
                    "forms": forms,
                    "excerpts": excerpt(norms["flat"], kw),
                }
        vol = []
        for m in VOL_POPUP_RE.finditer(norms["flat"]):
            a = max(0, m.start() - 200)
            b = min(len(norms["flat"]), m.end() + 200)
            vol.append({"match": m.group(0), "context": norms["flat"][a:b]})

        pages.append({
            "page": i + 1,
            "ns_pdftotext": nonspace(pt[i]),
            "ns_pdfplumber": nonspace(pp[i]),
            "no_text_layer": nonspace(pt[i]) == 0 and nonspace(pp[i]) == 0,
            "hits": hits,
            "self_ref": srefs,
            "vol_popup_loose": vol,
            "first_lines": [
                ln.strip() for ln in pt[i].splitlines() if ln.strip()
            ][:6],
            "flat": norms["flat"],
        })

    return {
        "filename": path.name,
        "sha256": sha256(path),
        "size": path.stat().st_size,
        "pages_pdftotext": len(pt),
        "pages_pdfplumber": len(pp),
        "pages": pages,
    }


def main() -> int:
    path = SRC / DOC
    if not path.exists():
        print(f"MISSING: {path}", file=sys.stderr)
        return 1
    json.dump(scan(path), sys.stdout, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
