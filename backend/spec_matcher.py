"""Spec reference matcher (RULES.md §2.4).

Layer 1: PDM code exact match (regex, deterministic).
Layer 1.5: Token Jaccard fuzzy match on spec description (deterministic, offline).
Layer 2: AI semantic match — future work; not implemented.
"""
import re

from openpyxl import load_workbook


# Regex for all PDM code patterns
PDM_PATTERN = re.compile(
    r"\b(PDM\d+\.?\d*|PDMS\d+\.?\d*|MPDM\d+\.?\d*|TD\d+\.?\d*"
    r"|DNDS\d+\.?\d*|PDEE\d+\.?\d*|APAC\d+\.?\d*|PSR\d+\.?\d*)\b"
)

# 通用英文 stop words 與無語意短詞
_STOP_WORDS = {
    "the", "and", "or", "but", "if", "then", "when", "where", "while",
    "is", "are", "was", "were", "be", "been", "being", "to", "of", "in",
    "on", "at", "for", "with", "by", "from", "this", "that", "these",
    "those", "it", "its", "as", "an", "a", "not", "no", "can", "will",
    "shall", "should", "must", "may", "do", "does", "did", "has", "have",
    "had", "one", "two", "any", "all", "some", "other", "user", "system",
    "via", "case", "which", "who", "what", "test", "item",
}


def _tokenize(text: str) -> set[str]:
    """切字：小寫、抽取 ≥3 字母的 alphabetic token，去 stop words。"""
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_]{2,}", (text or "").lower())
    return {t for t in tokens if t not in _STOP_WORDS}


def _jaccard(a: set[str], b: set[str]) -> float:
    """Jaccard similarity。空集合返回 0。"""
    if not a or not b:
        return 0.0
    inter = len(a & b)
    return inter / len(a | b)


def extract_pdm_codes(text: str) -> list[str]:
    """Extract all PDM-family codes from text."""
    return PDM_PATTERN.findall(text)


def build_spec_index(sys1_xlsx_path: str) -> dict:
    """
    Parse SYS1 spec xlsx (Basic Report sheet).

    Returns dict with:
        - "codes": {PDM code → entry}（Layer 1 用）
        - "entries": list[entry]（Layer 1.5 fuzzy 比對用，包含所有 SYS1 列）

    此結構向下相容：舊程式用 `entry_dict[code]` 取值時仍可用（"codes" 維度會自
    動 fallback）。對外保持 dict-like 方便既有呼叫端使用。
    """
    wb = load_workbook(sys1_xlsx_path, read_only=True, data_only=True)
    ws = wb["Basic Report"]

    index = SpecIndex()
    row_num = 2  # Skip header row
    while True:
        nrl_id = ws.cell(row=row_num, column=1).value
        if not nrl_id:
            break

        outline = ws.cell(row=row_num, column=3).value
        description = ws.cell(row=row_num, column=4).value or ""
        source_id = ws.cell(row=row_num, column=5).value or ""

        entry = {
            "nrl_id": nrl_id,
            "outline": outline,
            "source_id": source_id,
            "description": description,
            "tokens": _tokenize(description),
        }
        index.entries.append(entry)

        # Extract PDM codes from description
        for code in extract_pdm_codes(description):
            index[code] = entry

        row_num += 1

    wb.close()
    return index


class SpecIndex(dict):
    """Dict mapping PDM code → entry，並夾帶 `entries` list 供 fuzzy match。

    繼承 dict 讓舊呼叫 `index[code]` / `code in index` / `len(index)` 維持原語意
    （len 只計 PDM code 數），新功能透過 `.entries` 屬性取得全部 SYS1 列。
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.entries: list[dict] = []


# Fuzzy 比對閾值：低於此值視為 unmatched
FUZZY_THRESHOLD = 0.15


def match_spec_references(
    rows: list[dict],
    spec_index: dict,
    fuzzy_threshold: float = FUZZY_THRESHOLD,
) -> list[dict]:
    """
    Match Test Items to spec references.

    Layer 1：Test Item 文字中出現的 PDM code 直接對應 → `match_type="exact"`。
    Layer 1.5：若 Layer 1 無結果，對全部 SYS1 entries 跑 token Jaccard 相似度；
        相似度 ≥ threshold 採用最高分對應 → `match_type="fuzzy"` 並附 `match_score`。

    Returns 每列帶 spec_reference / match_type / 可選 match_score。
    """
    # SpecIndex 繼承 dict，所以 `code in spec_index` 直接可用
    entries = getattr(spec_index, "entries", None)
    codes_map = spec_index

    results = []
    for row in rows:
        test_item = row.get("test_item", "") or ""
        codes = extract_pdm_codes(test_item)
        matched_refs = []

        for code in codes:
            if code in codes_map:
                matched_refs.append(codes_map[code]["source_id"])

        if matched_refs:
            seen: set[str] = set()
            unique_refs: list[str] = []
            for ref in matched_refs:
                if ref not in seen:
                    seen.add(ref)
                    unique_refs.append(ref)
            results.append({
                **row,
                "spec_reference": "; ".join(unique_refs),
                "match_type": "exact",
            })
            continue

        # Layer 1.5 — fuzzy fallback
        if entries:
            item_tokens = _tokenize(test_item)
            best_entry = None
            best_score = 0.0
            for entry in entries:
                score = _jaccard(item_tokens, entry["tokens"])
                if score > best_score:
                    best_score = score
                    best_entry = entry
            if best_entry and best_score >= fuzzy_threshold:
                results.append({
                    **row,
                    "spec_reference": best_entry["source_id"],
                    "match_type": "fuzzy",
                    "match_score": round(best_score, 3),
                })
                continue

        results.append({
            **row,
            "spec_reference": None,
            "match_type": "unmatched",
        })

    return results
