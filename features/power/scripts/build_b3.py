"""B3 — CFTS 本文嵌入物件清點（R-P39）。

背景：04 §九第 3 項實測 §1.6.2.1 之文字層僅有兩個 `WrapperResource`
inline RTF 參照，即規格內容可藏在 R-P17 文字層定義看不見之處。
故 G8 = 904 所代表之規格覆蓋率目前無上界保證（A-PW23）。

**本腳本不解 RTF、不改 R-P17 之文字層定義。** 只清點。

CFTS009（OOXML）：直接檢視 `word/document.xml` 之 `w:object` / `w:drawing` /
`w:pict` / `o:OLEObject`，並讀 `word/_rels/document.xml.rels` 之
embeddings / image 關聯，以及 `word/embeddings/` 目錄清單。

CFTS010（OLE2 `.doc`）：無 OOXML 部件可查。改以 `textutil -convert html`
之輸出計 `<img>` 與 `<object>`，並以文字層之 `WrapperResource` 字樣計數。
此為**下界**，於輸出中明示。

用法：
    python features/power/scripts/build_b3.py
"""

from __future__ import annotations

import re
import subprocess
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_textlayer import REQ_RE, SEC_RE, paragraphs  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
DATA = ROOT / "features/power/data"

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
O = "{urn:schemas-microsoft-com:office:office}"
WP = "{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}"
REL_NS = "{http://schemas.openxmlformats.org/package/2006/relationships}"


def find(pattern: str) -> Path:
    return next(f for f in IN.iterdir() if pattern in f.name)


def docx_objects(path: Path) -> dict:
    """OOXML：逐段統計嵌入物件，並歸屬於其前最近之章節錨點。"""
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
        names = z.namelist()
        rels = ET.fromstring(z.read("word/_rels/document.xml.rels"))

    per_chapter: dict[str, Counter] = defaultdict(Counter)
    totals = Counter()
    current = "（章節錨點之前）"
    wrapper_chapters: Counter = Counter()

    for p in root.iter(W + "p"):
        text = "".join(t.text or "" for t in p.iter(W + "t"))
        m = SEC_RE.match(text)
        if m:
            current = m.group(1)
            continue
        for tag, label in [
            (W + "object", "w:object"),
            (W + "drawing", "w:drawing"),
            (W + "pict", "w:pict"),
            (O + "OLEObject", "o:OLEObject"),
        ]:
            n = len(list(p.iter(tag)))
            if n:
                per_chapter[current][label] += n
                totals[label] += n
        if "WrapperResource" in text:
            per_chapter[current]["WrapperResource（文字層字樣）"] += text.count("WrapperResource")
            totals["WrapperResource（文字層字樣）"] += text.count("WrapperResource")
            wrapper_chapters[current] += text.count("WrapperResource")

    rel_types = Counter()
    for r in rels.iter(REL_NS + "Relationship"):
        t = r.get("Type", "").rsplit("/", 1)[-1]
        rel_types[t] += 1

    return {
        "per_chapter": per_chapter,
        "totals": totals,
        "wrapper_chapters": wrapper_chapters,
        "rel_types": rel_types,
        "embeddings": sorted(n for n in names if n.startswith("word/embeddings/")),
        "media": sorted(n for n in names if n.startswith("word/media/")),
    }


def doc_objects(path: Path) -> dict:
    """OLE2 .doc：無 OOXML 部件，以 textutil html 之 <img>/<object> 計數（下界）。"""
    html = subprocess.run(
        ["textutil", "-convert", "html", "-stdout", str(path)],
        capture_output=True, check=True,
    ).stdout.decode("utf-8")
    totals = Counter({
        "<img>": len(re.findall(r"<img\b", html)),
        "<object>": len(re.findall(r"<object\b", html)),
    })
    per_chapter: dict[str, Counter] = defaultdict(Counter)
    current = "（章節錨點之前）"
    for plain, _ in paragraphs(path):
        m = SEC_RE.match(plain)
        if m:
            current = m.group(1)
            continue
        if "WrapperResource" in plain:
            per_chapter[current]["WrapperResource（文字層字樣）"] += plain.count("WrapperResource")
            totals["WrapperResource（文字層字樣）"] += plain.count("WrapperResource")
    return {"totals": totals, "per_chapter": per_chapter}


def chapter_stats(path: Path) -> dict[str, dict]:
    """逐章：文字層字元數（扣除錨點 metadata 行後）與需求錨點數。"""
    out: dict[str, dict] = {}
    current = None
    for plain, bold in paragraphs(path):
        m = SEC_RE.match(plain)
        if m:
            current = m.group(1)
            out[current] = {"title": m.group(2), "chars": 0, "anchors": 0, "body": 0}
            continue
        if current is None:
            continue
        anchors = REQ_RE.findall(bold)
        out[current]["anchors"] += len(anchors)
        out[current]["chars"] += len(plain.strip())
        if not anchors:
            out[current]["body"] += len(plain.strip())
    return out


def main() -> None:
    f009, f010 = find("CFTS_009_Wake-up"), next(x for x in IN.iterdir() if x.suffix == ".doc")
    o9, o10 = docx_objects(f009), doc_objects(f010)
    s9, s10 = chapter_stats(f009), chapter_stats(f010)

    out = [
        "# B3 — CFTS 本文嵌入物件清點（R-P39）\n",
        "\n> 依 R-P39 與 05 §I：**不解 RTF、不改 R-P17 之文字層定義**。本檔只清點。\n",
        "> 產生指令：`python features/power/scripts/build_b3.py`\n",
        "\n## 1. 總計\n\n| 文件 | 型別 | 數量 |\n|---|---|---|\n",
    ]
    for label, totals in [("CFTS009 `.docx`（OOXML）", o9["totals"]),
                          ("CFTS010 `.doc`（OLE2）", o10["totals"])]:
        for k, v in sorted(totals.items()):
            out.append(f"| {label} | `{k}` | **{v}** |\n")

    out.append("\n### CFTS009 之部件與關聯\n\n")
    out.append(f"- `word/embeddings/` 檔案數：**{len(o9['embeddings'])}**\n")
    for n in o9["embeddings"][:30]:
        out.append(f"  - `{n}`\n")
    if len(o9["embeddings"]) > 30:
        out.append(f"  - …（其餘 {len(o9['embeddings']) - 30} 個）\n")
    out.append(f"- `word/media/` 檔案數：**{len(o9['media'])}**\n")
    out.append("- `document.xml.rels` 之關聯型別分布：\n\n")
    out.append("| 型別 | 數量 |\n|---|---|\n")
    for k, v in o9["rel_types"].most_common():
        out.append(f"| `{k}` | {v} |\n")

    out.append("\n> CFTS010 為 OLE2 `.doc`，無 OOXML 部件可查。"
               "上表之數量係以 `textutil -convert html` 輸出計得，為**下界**。\n")

    out.append("\n## 2. 含嵌入物件之章節\n\n")
    for tag, objs, stats in [("CFTS009", o9, s9), ("CFTS010", o10, s10)]:
        rows = sorted(
            objs["per_chapter"].items(),
            key=lambda kv: tuple(int(x) for x in kv[0].split(".")) if kv[0][0].isdigit() else (0,),
        )
        out.append(f"\n### {tag}（{len(rows)} 章含嵌入物件）\n\n")
        out.append("| 章節 | 標題 | 物件 | 需求錨點數 | 非錨點內文字元數 |\n|---|---|---|---|---|\n")
        for num, counter in rows:
            st = stats.get(num, {"title": "—", "anchors": 0, "body": 0})
            objs_txt = "、".join(f"`{k}` ×{v}" for k, v in sorted(counter.items()))
            out.append(f"| §{num} | {st['title'][:40]} | {objs_txt} | "
                       f"{st['anchors']} | {st['body']} |\n")

    out.append("\n## 3. 文字層內容為空或近乎為空、卻含嵌入物件之章節\n\n")
    out.append("判準：該章之**非錨點內文字元數 < 200**，且含至少一個嵌入物件。\n\n")
    out.append("| 文件 | 章節 | 標題 | 非錨點內文字元數 | 需求錨點數 | 物件 |\n|---|---|---|---|---|---|\n")
    thin = 0
    for tag, objs, stats in [("CFTS009", o9, s9), ("CFTS010", o10, s10)]:
        for num, counter in objs["per_chapter"].items():
            st = stats.get(num)
            if st and st["body"] < 200:
                thin += 1
                objs_txt = "、".join(f"`{k}` ×{v}" for k, v in sorted(counter.items()))
                out.append(f"| {tag} | §{num} | {st['title'][:36]} | {st['body']} | "
                           f"{st['anchors']} | {objs_txt} |\n")

    out.append("\n## 4. 與 G8 / G9 之交叉\n\n")
    out.append("| 指標 | CFTS009 | CFTS010 |\n|---|---|---|\n")
    for label, key in [("全部章節數", "chapters"), ("含嵌入物件之章節數", "objchapters"),
                       ("全部需求錨點數", "anchors"), ("落在含嵌入物件章節內之需求錨點數", "objanchors")]:
        vals = []
        for objs, stats in [(o9, s9), (o10, s10)]:
            if key == "chapters":
                vals.append(len(stats))
            elif key == "objchapters":
                vals.append(len(objs["per_chapter"]))
            elif key == "anchors":
                vals.append(sum(v["anchors"] for v in stats.values()))
            else:
                vals.append(sum(stats[n]["anchors"] for n in objs["per_chapter"] if n in stats))
        out.append(f"| {label} | {vals[0]} | {vals[1]} |\n")

    out.append("""

## 5. 結論 —— 不是「藏在嵌入物件裡」，是「根本不在檔案裡」

CFTS009 `.docx` 之部件清單實測（`zipfile.namelist()`）：

- **無 `word/embeddings/` 目錄**（0 個檔案）
- `word/media/` 僅 `image1.png`（3,253 B），由 `header2.xml.rels` 引用，屬頁首圖
- `word/document.xml` 內 `w:object` / `w:drawing` / `w:pict` / `o:OLEObject`
  各 **0 個**
- `document.xml.rels` 之關聯型別中無 `oleObject`、無 `package`

即 `CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource` 這類字串
**是純字面文字**，不是任何嵌入物件的錨。它是 Polarion 匯出時留下的
**懸空參照** —— 其所指之 RTF 資源並未隨文件一同匯出。

**故 04 §九第 3 項之推測（「規格內容藏於文字層看不見之處」）方向正確但形態不同**：
內容不是看不見，是**不存在於交付文件之中**。

實測範圍：CFTS009 **16 處**、CFTS010 **15 處**，合計 **31 處**，
分布於 **16 個章節**（各 8 章）。其中 8 章之非錨點內文 < 200 字元，
即該章之可讀內容幾乎只剩這些懸空參照。

受影響最嚴重者為 **CFTS009 §1.6.2.1 `TLM algorithm requirements`**
（非錨點內文 101 字元、2 個需求錨點、2 處懸空參照）——
該章正是 A-PW16 九章之一，且被九個 leaf 共同引用。
其兩個被引用錨點 `4941354` / `4941355` 之內文即為該二懸空參照，
故 B2 v2 判為「無法判定」。

**R-P39 之問題「G8 = 904 之規格覆蓋率有無上界保證」，答案為：**
904 個需求錨點本身完整存在於文字層；
但其中落在含懸空參照章節內者，其部分內容不可得。
本包依 R-P39 只清點，不解 RTF、不改 R-P17。
""")

    path = DATA / "b3_embedded_objects.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print("G24 嵌入物件清點：")
    for label, totals in [("CFTS009", o9["totals"]), ("CFTS010", o10["totals"])]:
        print(f"  {label}: {dict(totals)}")
    print(f"  CFTS009 embeddings 檔 {len(o9['embeddings'])}、media 檔 {len(o9['media'])}")
    print(f"  含嵌入物件之章節：CFTS009 {len(o9['per_chapter'])}、CFTS010 {len(o10['per_chapter'])}")
    print(f"  其中非錨點內文 < 200 字元者：{thin}")


if __name__ == "__main__":
    main()
