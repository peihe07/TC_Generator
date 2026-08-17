"""自 CFTS 原始檔抽出文字層（R-P9 / R-P3′，spec_mode = D）。

文字層之統一定義（執行層 02 包提出，待分析層追認 —— 見 A-PW11）：

  每個段落同時產出兩種序列化：
    plain — 段落純文字，不含任何標記
    bold  — 對 run 層粗體加上 ** 標記

  §C rule 1（章節錨點）套用於 plain，rule 2（需求錨點）套用於 bold，
  兩者依段落索引對齊，故「需求錨點歸屬於其前最近之章節錨點」仍成立。

  理由：** 標記是為 rule 2 而存在的人工標記，rule 1 是純文字樣式匹配。
  兩份 CFTS 之標題粗體機制不同（CFTS009 用段落樣式 pStyle 1-8，
  CFTS010 用 run 層粗體），單一序列化無法同時滿足兩條正則。

讀取方式依 magic bytes 決定（R-P3′）：
  50 4B 03 04（OOXML .docx）→ zipfile + word/document.xml
  D0 CF 11 E0（OLE2  .doc ）→ textutil -convert html

用法：
    python features/power/scripts/extract_textlayer.py
"""

from __future__ import annotations

import hashlib
import html as html_mod
import json
import re
import subprocess
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
OUT = ROOT / "features/power/data/textlayer"

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# §C 之四條正則，逐字不改（禁區：不得自行調整）
SEC_RE = re.compile(r"^\s*(\d+(?:\.\d+)*)\s+(.{0,90}?)\s*\{(\d+)\}\s*$")
REQ_RE = re.compile(r"\*\*(\d{6,8}):\s*\[Artifact Type:")

MAGIC_OOXML = b"PK\x03\x04"
MAGIC_OLE2 = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"


def _serialize(runs: list[tuple[str, bool]]) -> tuple[str, str]:
    """把 [(文字, 是否粗體)] 轉為 (plain, bold) 兩種序列化。"""
    plain = "".join(t for t, _ in runs)
    bold = "".join(f"**{t}**" if b else t for t, b in runs).replace("****", "")
    return plain, bold


def paragraphs_ooxml(path: Path):
    """OOXML .docx：逐 w:p，run 層粗體取自 w:rPr/w:b。"""
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    for p in root.iter(W + "p"):
        runs = []
        for r in p.iter(W + "r"):
            text = "".join(n.text or "" for n in r.iter(W + "t"))
            if not text:
                continue
            rpr = r.find(W + "rPr")
            bold = False
            if rpr is not None:
                b = rpr.find(W + "b")
                bold = b is not None and b.get(W + "val") not in ("0", "false")
            runs.append((text, bold))
        yield _serialize(runs)


def paragraphs_ole2(path: Path):
    """OLE2 .doc：textutil 轉 html，以 <b>/<strong> 判定粗體，<p> 為段界。"""
    proc = subprocess.run(
        ["textutil", "-convert", "html", "-stdout", str(path)],
        capture_output=True,
        check=True,
    )
    body = proc.stdout.decode("utf-8")
    body = body[body.find("<body"):]

    def strip_tags(fragment: str) -> str:
        return html_mod.unescape(re.sub(r"<[^>]+>", "", fragment))

    for para in re.finditer(r"<p[^>]*>(.*?)</p>", body, re.S):
        inner = para.group(1)
        runs: list[tuple[str, bool]] = []
        pos = 0
        for m in re.finditer(r"<(b|strong)\b[^>]*>(.*?)</\1>", inner, re.S):
            before = strip_tags(inner[pos:m.start()])
            if before:
                runs.append((before, False))
            bold_text = strip_tags(m.group(2))
            if bold_text:
                runs.append((bold_text, True))
            pos = m.end()
        tail = strip_tags(inner[pos:])
        if tail:
            runs.append((tail, False))
        yield _serialize(runs)


def paragraphs(path: Path):
    """依 magic bytes 分派讀取器（R-P3′）。"""
    head = path.open("rb").read(8)
    if head.startswith(MAGIC_OOXML):
        return paragraphs_ooxml(path)
    if head.startswith(MAGIC_OLE2):
        return paragraphs_ole2(path)
    raise ValueError(f"未知 magic bytes {head.hex(' ')}：{path.name}")


def build_index(paras: list[tuple[str, str]]) -> dict:
    """建立 item_id → (章節號, 章節標題)，並回傳錨點統計。"""
    sections = []  # (段落索引, 章節號, 標題, 章節 id)
    requirements = []  # (段落索引, item id)
    for i, (plain, bold) in enumerate(paras):
        m = SEC_RE.match(plain)
        if m:
            sections.append((i, m.group(1), m.group(2), m.group(3)))
        for rm in REQ_RE.finditer(bold):
            requirements.append((i, rm.group(1)))

    # §C rule 1：同一章節 id 多次出現取最後一次（前面的是目錄頁）
    last = {sid: (i, num, title) for i, num, title, sid in sections}
    ordered = sorted((i, num, title, sid) for sid, (i, num, title) in last.items())

    mapping = {}
    for para_idx, item_id in requirements:
        prior = [s for s in ordered if s[0] <= para_idx]
        if prior:
            _, num, title, _ = prior[-1]
            mapping[item_id] = (num, title)

    return {
        "mapping": mapping,
        "sections_total": len(sections),
        "sections_unique": len(last),
        "requirements_total": len(requirements),
        "requirements_unique": len({r[1] for r in requirements}),
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    targets = {
        "cfts009": next(f for f in IN.iterdir() if "CFTS_009_Wake-up" in f.name),
        "cfts010": next(f for f in IN.iterdir() if f.suffix == ".doc"),
    }

    index = {}
    for tag, path in targets.items():
        paras = list(paragraphs(path))
        result = build_index(paras)
        index[tag] = result["mapping"]

        for variant in ("plain", "bold"):
            col = 0 if variant == "plain" else 1
            text = "\n".join(p[col] for p in paras)
            out_path = OUT / f"{tag}_{variant}.txt"
            out_path.write_text(text, encoding="utf-8")
            digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
            print(f"{out_path.name}\t{len(text.encode('utf-8'))} B\tsha256={digest}")

        print(
            f"  {tag}: 章節錨點 {result['sections_total']}"
            f"（unique {result['sections_unique']}）"
            f" | 需求錨點 {result['requirements_total']}"
            f"（unique {result['requirements_unique']}）"
            f" | 可歸屬 item {len(result['mapping'])}"
        )

    out = ROOT / "features/power/data/item_to_chapter.json"
    out.write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
