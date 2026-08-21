#!/usr/bin/env python3
"""M10-PM（R-3）：test_item 上半摘句至 50 token 以內。

規則（canon §4.3.1）：「摘句以與括號下半之測試目的直接相關之句為限」。
本模組據此實作：
1. 將上半切為段（先按行；過長之行再按句；仍過長者按子句標記切）。
2. 以與括號下半之實詞重疊度為相關度評分。
3. 依分數高低取段，但**輸出維持原文順序**，累加至逼近 50 token 為止；
   至少保留分數最高之一段。
段落一律逐字保留，不改寫、不縮寫 —— verbatim 之片段仍是 verbatim。
"""

from __future__ import annotations

import re

LIMIT = 50
TOKEN_RE = re.compile(r"[A-Za-z0-9$_.'\"-]+")
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
CLAUSE_SPLIT = re.compile(r"(?<=[;:])\s+|\s+(?=THEN\b)|\s+(?=OR\b)|\s+(?=AND\b)")
# 末段手段：子句切完仍超限者，再按逗號與「無空白之 THEN」切。
# 來源多處缺空白（`valueTHENTLM`），上面的 `\s+(?=THEN)` 切不到；
# 前後皆切可讓 `THEN` 自成一段，摘句不致以 `THENTLM` 這種黏詞開頭。
LAST_RESORT_SPLIT = re.compile(r"(?<=,)\s+|(?=THEN)|(?<=THEN)")

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "is", "are", "be",
    "shall", "has", "have", "it", "its", "for", "with", "as", "at", "by",
    "that", "this", "if", "then", "not", "from", "read", "reads", "when",
    "which", "was", "were", "been", "will", "can", "case", "also", "any",
}


def n_tokens(text: str) -> int:
    return len(TOKEN_RE.findall(text))


def content_words(text: str) -> set[str]:
    """取實詞集合，供相關度評分。"""
    words = {w.strip("\"'.,;:()[]").lower() for w in TOKEN_RE.findall(text)}
    return {w for w in words if w and w not in STOPWORDS and len(w) > 2}


def segment(upper: str) -> list[str]:
    """切段：行 → 句 → 子句 → 逗號，僅在該層仍超限時往下切。"""
    out: list[str] = []
    for line in (ln.strip() for ln in upper.split("\n")):
        if not line:
            continue
        if n_tokens(line) <= LIMIT:
            out.append(line)
            continue
        for sentence in (x.strip() for x in SENTENCE_SPLIT.split(line)):
            if not sentence:
                continue
            if n_tokens(sentence) <= LIMIT:
                out.append(sentence)
                continue
            for clause in (x.strip() for x in CLAUSE_SPLIT.split(sentence)):
                if not clause:
                    continue
                if n_tokens(clause) <= LIMIT:
                    out.append(clause)
                    continue
                out.extend(x.strip() for x in LAST_RESORT_SPLIT.split(clause)
                           if x and x.strip())
    return out


def score(seg: str, purpose: set[str]) -> float:
    """相關度 = 與測試目的之實詞交集大小，長度作次要正規化。"""
    words = content_words(seg)
    if not words:
        return 0.0
    return len(words & purpose) + len(words & purpose) / (len(words) + 1)


ANCHOR_MAX_TOKENS = 5


def anchor_index(upper: str, segments: list[str]) -> int | None:
    """表格型 verbatim 之首行為狀態鍵（如 `Full-Operation`），必須保留。

    去掉它，rows 12/23 這類「同一張表不同狀態列」之摘句會逐字相同，
    反而製造 sibling 不可分。散文型（單行）無此結構，不設錨。
    """
    lines = [ln for ln in upper.split("\n") if ln.strip()]
    if len(lines) > 1 and segments and segments[0] == lines[0].strip() \
            and n_tokens(segments[0]) <= ANCHOR_MAX_TOKENS:
        return 0
    return None


def excerpt(upper: str, paren: str) -> tuple[str, list[int]]:
    """回傳 (摘句後之上半, 所取之段索引)。

    只取與測試目的有實詞交集之段（相關度 > 0）；全數為 0 時退而取
    分數最高之一段，避免空輸出。零相關之段不得因「還有額度」而混入。
    """
    segments = segment(upper)
    if not segments or n_tokens(upper) <= LIMIT:
        return upper, list(range(len(segments)))

    purpose = content_words(paren)
    scores = {i: score(segments[i], purpose) for i in range(len(segments))}
    anchor = anchor_index(upper, segments)

    chosen: list[int] = []
    used = 0
    if anchor is not None:
        chosen.append(anchor)
        used += n_tokens(segments[anchor])

    ranked = [i for i in sorted(scores, key=lambda i: (-scores[i], i))
              if i not in chosen and scores[i] > 0]
    if not ranked and not chosen:
        ranked = [max(scores, key=lambda i: (scores[i], -i))]

    for i in ranked:
        cost = n_tokens(segments[i])
        if chosen and used + cost > LIMIT:
            continue
        chosen.append(i)
        used += cost
    chosen.sort()
    return "\n".join(segments[i] for i in chosen), chosen
