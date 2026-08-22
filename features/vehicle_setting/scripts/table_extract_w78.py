"""W-78 —— docx 表格抽取（46 包 §3）。

現行之 `blocks_with_sec()` 抽 `word/document.xml` 之**段落文字流**，
`<w:tbl>` 之儲存格被攤平為段落，**列／欄關係遺失**（A-VS88）。

本模組改以文件順序走訪 `<w:p>` 與 `<w:tbl>` 兩種區塊，
表格保留為 `list[list[str]]`（列 × 欄），並歸屬至其前一個 7 位數條文區塊。
"""
from __future__ import annotations

import re
import zipfile
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
DOCX = next(FEAT.glob("inputs/R1LR_Atl-H_*CFTS_044*.docx"))
BLOCK_RE = re.compile(r"(\d{7})\s*:\s*\[Artifact Type")
# 以文件順序取出頂層之 <w:p> 與 <w:tbl>。**非貪婪且不跨越同名開標籤**，
# 故巢狀表格之內層會被外層吞入 —— 已知界線，見上繳 25 §4。
NODE = re.compile(r"<w:(p|tbl)[ >].*?</w:\1>", re.S)
TEXT = re.compile(r"<w:t[^>]*>([^<]*)</w:t>")


def _cells(row_xml: str) -> list[str]:
    return [" ".join(TEXT.findall(tc)).strip()
            for tc in re.findall(r"<w:tc[ >].*?</w:tc>", row_xml, re.S)]


def nodes() -> list[tuple[str, object]]:
    """回傳 [(kind, payload)]；kind 為 `p`（str）或 `tbl`（list[list[str]]）。"""
    xml = zipfile.ZipFile(DOCX).read("word/document.xml").decode("utf-8")
    out: list[tuple[str, object]] = []
    for m in NODE.finditer(xml):
        if m.group(1) == "p":
            out.append(("p", "".join(TEXT.findall(m.group(0)))))
        else:
            rows = [_cells(r) for r in
                    re.findall(r"<w:tr[ >].*?</w:tr>", m.group(0), re.S)]
            out.append(("tbl", rows))
    return out


def blocks_with_tables() -> dict[str, dict]:
    """條文 id → {"text": 段落文字, "tables": [表格…]}。"""
    out: dict[str, dict] = {}
    cur = None
    for kind, payload in nodes():
        if kind == "p":
            m = BLOCK_RE.search(payload)
            if m:
                cur = m.group(1)
                out[cur] = {"text": payload, "tables": []}
            elif cur:
                out[cur]["text"] += "\n" + payload
        elif cur:
            out[cur]["tables"].append(payload)
    return out
