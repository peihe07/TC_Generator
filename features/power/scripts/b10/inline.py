#!/usr/bin/env python3
"""A2／A3：Input Test Data 內聯至 Procedure，步驟自足。

原則：**動詞取自原句、資料取自 input 欄**，不自行發明動作。
把回指語 `the <名詞> listed in Input Test Data` 換為具體資料之呈現；
呈現式依資料類別而定（CAN／內部訊號／PROXI／自由文字）。

無法安全呈現者回傳 None，由呼叫端標記待覆核，不硬寫（§8.4.1）。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import signals as S                                   # noqa: E402

REF = re.compile(r"\bthe\s+([A-Za-z0-9_ ]*?)\s*listed in Input Test Data\b")
REF_BARE = re.compile(r"\blisted in Input Test Data\b")

TRIPLET = re.compile(r"\b[A-Za-z0-9_]+\s+in\s+[A-Z][A-Z0-9_]{2,}\s+on\s+[A-Za-z0-9-]+\b")
DOTTED = re.compile(r"\b[A-Z][A-Z0-9_]{2,}\.[A-Za-z][A-Za-z0-9_]*\b")
INTERNAL = re.compile(r"^([A-Za-z][A-Za-z0-9_]*\.(?:Info|Req|GUI))\s*[:=]\s*(.+)$")
PROXI = re.compile(r"^(\$[^$]+\$)\s*[:=]\s*(.+)$")
TRANSITION = re.compile(r'^"?([^"]+?)"?\s+to\s+"?([^"]+?)"?$')


def classify(line: str) -> str:
    line = line.strip()
    if TRIPLET.search(line) or DOTTED.search(line):
        return "can"
    if INTERNAL.match(line):
        return "internal"
    if PROXI.match(line):
        return "proxi"
    return "free"


def can_parts(line: str) -> tuple[str, list[int]] | None:
    """解析 CAN 輸入行 → (訊號, [raw 值…])；transition 型回兩個 raw。"""
    dotted = S.to_dotted(line)
    m = DOTTED.search(dotted)
    if not m:
        return None
    signal = m.group(0)
    if signal not in S.VAL_LABELS:
        return None
    tail = dotted[m.end():].lstrip(" :=").strip()
    trans = TRANSITION.match(tail)
    values = [trans.group(1), trans.group(2)] if trans else [tail]
    raws = [S.resolve_raw(signal, v) for v in values]
    if any(r is None for r in raws):
        return None
    return signal, raws


def render(line: str) -> tuple[str, list[str]] | None:
    """回傳 (類別, [具體呈現…])；transition 之 CAN 回兩則。"""
    kind = classify(line)
    line = line.strip()
    if kind == "can":
        parsed = can_parts(line)
        if not parsed:
            return None
        signal, raws = parsed
        return "can", [S.assignment(signal, r) for r in raws]
    if kind == "internal":
        m = INTERNAL.match(line)
        name, value = m.group(1), m.group(2).strip()
        trans = TRANSITION.match(value)
        if trans:
            return "internal", [f"{name} from \"{trans.group(1)}\" "
                                f"to \"{trans.group(2)}\""]
        return "internal", [f"{name} = {value}"]
    if kind == "proxi":
        m = PROXI.match(line)
        name, value = m.group(1), m.group(2).strip()
        trans = TRANSITION.match(value)
        if trans:
            return "proxi", [f"PROXI {name} from {trans.group(1)} "
                             f"to {trans.group(2)}"]
        return "proxi", [f"PROXI {name} = {value}"]
    return "free", [line.rstrip(".")]


def substitute(sentence: str, concrete: str) -> str | None:
    """把回指語換成具體資料；換不掉回 None。"""
    if REF.search(sentence):
        return REF.sub(concrete, sentence, count=1)
    if REF_BARE.search(sentence):
        return REF_BARE.sub(concrete, sentence, count=1)
    return None
