#!/usr/bin/env python3
"""M15（S4）：由各列實際差異推導 sibling 區分 token。

原則：token 必須自工作簿既有欄位之**實測差異**逐字取得，不得臆造。
比對順序 pre → input → proc → er，取第一個「組內全異」之欄位，
token = 該欄位中**內容不一致之行**（去行號後逐字保留，多行以 `; ` 併）。
逐字保留而不做摘要，是為了讓覆核者能直接對回該列欄位。
組內任兩列切出之 token 相同、或無欄位可切者 → UNRESOLVED，不填入。
"""

from __future__ import annotations

import re

FIELD_PRIORITY = ("pre", "input", "proc", "er")
NUMBER_PREFIX = re.compile(r"^\s*\d+[.)]\s*")


def lines_of(text: str) -> list[str]:
    """去行號、去空行後之行序列。"""
    out = [NUMBER_PREFIX.sub("", ln).strip() for ln in text.split("\n")]
    return [ln for ln in out if ln]


def differing_lines(group_texts: list[list[str]]) -> list[str] | None:
    """取各列中「組內不一致」之行。

    行數一致時逐位置比對；行數不齊時改取「非全組共有」之行，
    避免整欄傾倒。
    """
    counts = {len(t) for t in group_texts}
    if len(counts) == 1:
        width = counts.pop()
        idx = [i for i in range(width)
               if len({t[i] for t in group_texts}) > 1]
        if not idx:
            return None
        return ["; ".join(t[i] for i in idx) for t in group_texts]

    shared = set(group_texts[0]).intersection(*[set(t) for t in group_texts[1:]])
    out = ["; ".join(ln for ln in t if ln not in shared) for t in group_texts]
    return out if any(out) else None


def clean(token: str) -> str:
    """去尾標點；括號下半不使用尾句號。"""
    return token.strip().rstrip(".;,")


def _tokens_for(group_rows: list[dict], fields: tuple[str, ...]
                ) -> list[str] | None:
    """對指定欄位組合切出 token；不可用時回傳 None。"""
    parts: list[list[str]] = []
    for field in fields:
        got = differing_lines([lines_of(r[field]) for r in group_rows])
        if got is None:
            return None
        parts.append(got)
    tokens = [clean("; ".join(p[i] for p in parts if p[i]))
              for i in range(len(group_rows))]
    if all(tokens) and len(set(tokens)) == len(tokens):
        return tokens
    return None


def derive(group_rows: list[dict]) -> tuple[str | None, list[str] | None]:
    """對一組 sibling 推導 (來源欄位, 各列 token)。

    先試單欄；單欄無區分力者（多軸 sibling）再試雙欄組合。
    """
    for field in FIELD_PRIORITY:
        tokens = _tokens_for(group_rows, (field,))
        if tokens:
            return field, tokens
    for i, first in enumerate(FIELD_PRIORITY):
        for second in FIELD_PRIORITY[i + 1:]:
            tokens = _tokens_for(group_rows, (first, second))
            if tokens:
                return f"{first}+{second}", tokens
    return None, None
