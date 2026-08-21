"""W-39 —— in-scope 判準之反向驗證（28 包 §3）。

11 輪 W-37 於已覆蓋側之 130 條上驗得新判準（＋ECU＋Radio）成立 130/130，
惟該驗證只是**方向性**（該排除者被排除）。本腳本補其**範圍向**（R-G9）：
確認新判準未把任何已知 in-scope 者排除掉。

判準兩版：
  LEGACY  Artifact Type 含 Subsystem Functional Requirement
          且 EE Architecture 含 Atlantis High 或 All
  NEW     LEGACY ＋ ECU 含 LTM/ETM/RRM 之一
                 ＋ Radio 含 R1L 或 R1L-R（Radio 欄為空者視為不限）

輸出：新舊兩組之 in-scope 數、251 個已覆蓋 reqid 之落點、21 章節內重算。
"""
from __future__ import annotations

import re
import zipfile
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
DOCX = next(FEAT.glob("inputs/R1LR_Atl-H_*CFTS_044*.docx"))

BLOCK_RE = re.compile(r"(\d{7})\s*:\s*\[Artifact Type")
ATTR_RE = re.compile(r"\[([^:\]]+):([^\]]*)\]")
ECU_HEAD = {"LTM", "ETM", "RRM"}
RADIO_OK = {"R1L", "R1L-R"}


def paragraphs() -> list[str]:
    """docx body 段落之純文字，順序即文件順序。"""
    xml = zipfile.ZipFile(DOCX).read("word/document.xml").decode("utf-8")
    out = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S):
        out.append("".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)))
    return out


def blocks() -> list[dict]:
    """以 `\\d{7}: [Artifact Type` 為界切出條文區塊。"""
    paras = paragraphs()
    starts = [i for i, t in enumerate(paras) if BLOCK_RE.search(t)]
    out = []
    for k, i in enumerate(starts):
        j = starts[k + 1] if k + 1 < len(starts) else len(paras)
        text = "\n".join(paras[i:j])
        attrs = {}
        for name, val in ATTR_RE.findall(text):
            attrs.setdefault(name.strip(), val.strip())   # R-VS?: 取首次命中
        out.append({"id": BLOCK_RE.search(paras[i]).group(1),
                    "attrs": attrs, "text": text})
    return out


def _vals(attrs: dict, key: str) -> list[str]:
    return [v.strip() for v in attrs.get(key, "").split(",") if v.strip()]


def legacy(b: dict) -> bool:
    a = b["attrs"]
    if "Subsystem Functional Requirement" not in a.get("Artifact Type", ""):
        return False
    ee = _vals(a, "EE Architecture")
    return any(v in ("Atlantis High", "All") for v in ee)


def new(b: dict) -> bool:
    if not legacy(b):
        return False
    a = b["attrs"]
    if not (set(_vals(a, "ECU")) & ECU_HEAD):
        return False
    radio = _vals(a, "Radio")
    return (not radio) or bool(set(radio) & RADIO_OK)   # 空欄視為不限


HEAD_RE = re.compile(r'<w:pStyle w:val="([1-7])"')
SEC_RE = re.compile(r"^\s*((?:\d+\.)+\d+|\d+)\s+\S")


def blocks_with_sec() -> list[dict]:
    """同 blocks()，另附 `sec` —— 其為該區塊之上一個標題段落所帶之節號。

    節號在本 docx 中為標題**文字之一部分**（非自動編號欄位），
    故直接由文字前綴取得，不需重建編號狀態。
    """
    xml = zipfile.ZipFile(DOCX).read("word/document.xml").decode("utf-8")
    paras, is_head = [], []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S):
        paras.append("".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)))
        is_head.append(bool(HEAD_RE.search(p)))
    sec_of, cur = [], ""
    for t, h in zip(paras, is_head):
        if h:
            m = SEC_RE.match(t)
            if m:
                cur = m.group(1)
        sec_of.append(cur)
    starts = [i for i, t in enumerate(paras) if BLOCK_RE.search(t)]
    out = []
    for k, i in enumerate(starts):
        j = starts[k + 1] if k + 1 < len(starts) else len(paras)
        text = "\n".join(paras[i:j])
        attrs = {}
        for name, val in ATTR_RE.findall(text):
            attrs.setdefault(name.strip(), val.strip())
        out.append({"id": BLOCK_RE.search(paras[i]).group(1), "sec": sec_of[i],
                    "attrs": attrs, "text": text})
    return out
