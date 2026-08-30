#!/usr/bin/env python3
"""下放包 11 作業 D：CFTS022 之變體軸量測。

只讀不寫 repo 既有檔案；輸出到 stdout，由人工轉入報告。
抽取法：word/document.xml，</w:p> -> 換行、</w:tc> -> tab、去 XML 標籤、html.unescape。
NBSP（U+00A0）與其他空白正規化為一般空白後再掃描。
"""
import html
import re
import sys
import zipfile
from collections import Counter, OrderedDict

DOCX = ("/Users/peihe/Work_Projects/TC_Generator/features/ics_management/inputs/"
        "R1LR_Atl-H_26PI2.5 Jun Release-Privacy_CFTS_022 Functional Specification_"
        "20260608-1205.docx")

# 需檢測的變體相關詞
VARIANT_TERMS = ["Associated", "Disassociated", "Silver Box", "SilverBox", "DCSD",
                 "_ADspl", "_DDspl", "ADspl", "DDspl"]


def normalize(text: str) -> str:
    """把 NBSP / 各式空白正規化為一般空白（不合併，以保留欄位切分）。"""
    for ch in (" ", " ", " ", " ", " ", " ", "​"):
        text = text.replace(ch, " " if ch != "​" else "")
    return text


def extract_lines():
    with zipfile.ZipFile(DOCX) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    xml = xml.replace("</w:p>", "</w:p>\n")
    xml = xml.replace("</w:tc>", "</w:tc>\t")
    txt = re.sub(r"<[^>]+>", "", xml)
    txt = html.unescape(txt)
    txt = normalize(txt)
    return txt.split("\n")


OBJ_HEAD = re.compile(r"^(\d{7}): \[")
ATTR = re.compile(r"\[([^\[\]:]+):([^\[\]]*)\]")


def parse_objects(lines):
    """回傳 [(objid, attrs(OrderedDict), body, line_index)]。"""
    objs = []
    for i, ln in enumerate(lines):
        m = OBJ_HEAD.match(ln.strip())
        if not m:
            continue
        objid = m.group(1)
        attrs = OrderedDict()
        for k, v in ATTR.findall(ln):
            attrs.setdefault(k.strip(), v.strip())
        body = lines[i + 1].strip() if i + 1 < len(lines) else ""
        objs.append((objid, attrs, body, i))
    return objs


def main():
    lines = extract_lines()
    objs = parse_objects(lines)
    print(f"# lines={len(lines)} objects={len(objs)}")

    # --- §1 屬性軸值域全列 ---
    keys = Counter()
    domains = {}
    for _, attrs, _, _ in objs:
        for k, v in attrs.items():
            keys[k] += 1
            domains.setdefault(k, Counter())[v] += 1
    print("\n## ATTR KEYS")
    for k, c in keys.most_common():
        print(f"- {k}: present in {c}/{len(objs)} objects; distinct={len(domains[k])}")
        for v, n in domains[k].most_common():
            print(f"    * {v!r} x{n}")

    # --- §2 變體詞全文掃描 ---
    print("\n## VARIANT TERM HITS (case-insensitive, substring on NBSP-normalized text)")
    for term in VARIANT_TERMS:
        pat = re.compile(re.escape(term), re.I)
        hits = [(i, ln) for i, ln in enumerate(lines) if pat.search(ln)]
        print(f"\n### {term}: {len(hits)} line hit(s)")
        for i, ln in hits[:60]:
            print(f"  L{i}: {ln.strip()[:400]}")

    # 詞界版（僅英數詞可用 \b）
    print("\n## VARIANT TERM HITS (word-boundary \\b, case-insensitive)")
    for term in ["Associated", "Disassociated", "DCSD"]:
        pat = re.compile(r"\b" + re.escape(term) + r"\b", re.I)
        hits = [i for i, ln in enumerate(lines) if pat.search(ln)]
        print(f"- {term}: {len(hits)} line hit(s)")

    # --- §3 目標錨物件 ---
    targets = ["4914956", "4914957", "4914958", "4914974", "4914975", "4914976", "4914993"]
    print("\n## TARGET ANCHOR OBJECTS")
    by_id = {o[0]: o for o in objs}
    for t in targets:
        if t not in by_id:
            print(f"\n### {t}: NOT FOUND as object head")
            continue
        objid, attrs, body, idx = by_id[t]
        print(f"\n### {objid}  (line {idx})")
        print(f"  attrs: {dict(attrs)}")
        print(f"  body: {body[:1200]}")
        # 上下文：往上找最近的章節標題行
        for j in range(idx - 1, max(0, idx - 200), -1):
            if re.match(r"^\d+(\.\d+)*\s+\S", lines[j].strip()):
                print(f"  nearest-heading L{j}: {lines[j].strip()[:200]}")
                break

    # --- §4 章節樹（到二層） ---
    print("\n## HEADING TREE (depth<=2)")
    seen = set()
    for i, ln in enumerate(lines):
        s = ln.strip()
        m = re.match(r"^(\d+(?:\.\d+){0,1})\s+(\S.*)$", s)
        if m and len(m.group(2)) < 120 and not m.group(2).startswith("["):
            key = (m.group(1), m.group(2)[:100])
            if key in seen:
                continue
            seen.add(key)
            print(f"  L{i}: {m.group(1)}  {m.group(2)[:100]}")


if __name__ == "__main__":
    sys.exit(main())
