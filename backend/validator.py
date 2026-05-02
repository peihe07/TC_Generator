"""Programmatic validator for generated TC fields (ASPICE_SWE6_AI_Instruction.md §7/§11). No AI."""
import re
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of a single validation check."""
    passed: bool
    check: str
    message: str = ""


# Valid values for dropdown fields
VALID_DESIGN_METHODS = [
    "功能測試 (Functional based ; no specific technique)",
    "狀態轉換 (State Transition Testing)",
    "決策表 (Decision Table Testing)",
    "等價劃分 (Equivalence Partitioning, EP)",
    "邊界值分析 (Boundary Value Analysis, BVA)",
    "組合測試 (Combinatorial Testing ; Pairwise / t-wise)",
    "情境 / 用例 (Scenario / Use Case Testing)",
    "負向測試 (Negative / Invalid)",
    "基礎故障注入 (Fault Injection Lite)",
]

_DESIGN_METHOD_ALIASES = {
    "functional": VALID_DESIGN_METHODS[0],
    "functional based": VALID_DESIGN_METHODS[0],
    "state transition": VALID_DESIGN_METHODS[1],
    "state transition testing": VALID_DESIGN_METHODS[1],
    "decision table": VALID_DESIGN_METHODS[2],
    "decision table testing": VALID_DESIGN_METHODS[2],
    "ep": VALID_DESIGN_METHODS[3],
    "equivalence": VALID_DESIGN_METHODS[3],
    "equivalence partitioning": VALID_DESIGN_METHODS[3],
    "equivalence partitioning, ep": VALID_DESIGN_METHODS[3],
    "bva": VALID_DESIGN_METHODS[4],
    "boundary": VALID_DESIGN_METHODS[4],
    "boundary value analysis": VALID_DESIGN_METHODS[4],
    "boundary value analysis, bva": VALID_DESIGN_METHODS[4],
    "combinatorial": VALID_DESIGN_METHODS[5],
    "pairwise": VALID_DESIGN_METHODS[5],
    "combinatorial testing": VALID_DESIGN_METHODS[5],
    "scenario": VALID_DESIGN_METHODS[6],
    "use case": VALID_DESIGN_METHODS[6],
    "scenario / use case": VALID_DESIGN_METHODS[6],
    "negative": VALID_DESIGN_METHODS[7],
    "invalid": VALID_DESIGN_METHODS[7],
    "negative / invalid": VALID_DESIGN_METHODS[7],
    "fault injection": VALID_DESIGN_METHODS[8],
    "fault injection lite": VALID_DESIGN_METHODS[8],
}

VALID_PRIORITIES = ["P0", "P1", "P2", "P3"]

# 舊字串 → P-code 的 fuzzy 映射（AI / template 可能還回舊值）。
_PRIORITY_ALIAS = {
    "high": "P0",
    "p0": "P0",
    "medium": "P1",
    "med": "P1",
    "p1": "P1",
    "low": "P2",
    "p2": "P2",
    "minor": "P3",
    "p3": "P3",
    # 若 AI 回 NA 或空值，不做 fuzzy 映射，交給 validator 回 fail。
}


def normalize_priority(value: str | None) -> str:
    """Fuzzy-normalize 使用者 / AI 輸入到 P0/P1/P2/P3；對不上就回空字串。"""
    if not value:
        return ""
    key = str(value).strip().lower()
    if not key:
        return ""
    return _PRIORITY_ALIAS.get(key, "")

# Action verbs not allowed in pre-conditions
ACTION_VERBS = [
    "insert", "connect", "press", "tap", "click",
    "open", "navigate", "pair", "plug",
]

# System-obvious states not allowed in pre-conditions
OBVIOUS_STATES = [
    "hu is powered on", "system is running", "system is booted",
    "hu is on", "head unit is powered on",
]

# Vague terms not allowed in expected results
VAGUE_TERMS = ["normal", "as expected", "works correctly", "no issue"]

# Vague verbs not allowed in final procedure step (§7.1.1)
VAGUE_FINAL_VERBS = [
    "observe whether", "observe ", "see if", "look at",
    "check whether", "confirm whether",
    "watch ", "monitor ", "inspect ",
]

# Forbidden verification phrases anywhere in a step's imperative text (§7.1.1)
FORBIDDEN_STEP_PHRASES = [
    "observe whether", "observe ", "see if", "look at",
    "check whether", "confirm whether", "verify", "watch ", "monitor ", "inspect ",
]

# Preferred verification patterns for the final step (§7.1.1 / §7.5)
FINAL_STEP_PATTERNS = [
    "check that",
    "confirm that",
    "read ",
    "record ",
    "compare ",
]

_OUTCOME_STOPWORDS = {
    "the", "a", "an", "is", "are", "be", "to", "on", "in", "of", "and", "or",
    "for", "with", "by", "from", "into", "at", "as", "that", "this", "these",
    "those", "it", "its", "shown", "displayed", "visible",
}

# TC ID pattern: {project}-{abbr}-{3-digit}
TC_ID_PATTERN = re.compile(r"^[A-Za-z0-9]+-[A-Za-z0-9]+-\d{3}$")


def _count_numbered_items(text: str) -> int:
    """Count numbered list items (e.g. '1. xxx')."""
    return len(re.findall(r"^\d+\.", text, re.MULTILINE))


def _is_numbered_list(text: str) -> bool:
    """Check if text is a numbered list."""
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if not lines:
        return False
    return all(re.match(r"^\d+\.", line) for line in lines)


# --- §8.1 Test Item Format ---

def validate_test_item(text: str) -> ValidationResult:
    """Validate appended rewrite format."""
    check = "test_item"

    # Must have blank line separating original and rewrite
    if "\n\n" not in text:
        return ValidationResult(False, check, "Missing blank line between original and rewrite.")

    parts = text.split("\n\n", 1)
    if len(parts) < 2 or not parts[1].strip():
        return ValidationResult(False, check, "No rewrite found after blank line.")

    rewrite = parts[1].strip()

    # 接受 §6.1 三種形狀：Arrow / Sentence / Scenario tag
    # 不再強制 → 分隔符；僅檢查長度 2–14 詞
    word_count = len(rewrite.split())
    if word_count < 2 or word_count > 14:
        return ValidationResult(
            False, check,
            f"Rewrite must be 2–14 words (got {word_count}).",
        )

    return ValidationResult(True, check)


# --- §8.2 Pre-Condition ---

def validate_pre_conditions(text: str) -> ValidationResult:
    """Validate pre-conditions field."""
    check = "pre_conditions"

    if text.strip() == "NA":
        return ValidationResult(True, check)

    # Must be numbered list
    if not _is_numbered_list(text):
        return ValidationResult(False, check, "Must be a numbered list or 'NA'.")

    text_lower = text.lower()

    # No action verbs
    for verb in ACTION_VERBS:
        if re.search(rf"\b{verb}\b", text_lower):
            return ValidationResult(
                False, check,
                f"Contains action verb '{verb}'. Pre-conditions must be states only.",
            )

    # No obvious states
    for state in OBVIOUS_STATES:
        if state in text_lower:
            return ValidationResult(
                False, check,
                f"Contains system-obvious state '{state}'.",
            )

    return ValidationResult(True, check)


# --- §8.3 Test Procedure ---

def _numbered_lines(text: str) -> list[str]:
    return [line.strip() for line in text.strip().split("\n") if re.match(r"^\d+\.", line.strip())]


def _extract_outcome_keywords(tc_title: str | None) -> set[str]:
    if not tc_title or "→" not in tc_title:
        return set()
    outcome = tc_title.split("→", 1)[1].lower()
    words = re.findall(r"[a-z0-9]+", outcome)
    return {w for w in words if len(w) >= 3 and w not in _OUTCOME_STOPWORDS}


def _contains_forbidden_phrase(step: str) -> str | None:
    step_lower = step.lower()
    for phrase in FORBIDDEN_STEP_PHRASES:
        if phrase in step_lower:
            return phrase.strip()
    return None


def _verification_clause(step_lower: str) -> str:
    for pattern in FINAL_STEP_PATTERNS:
        idx = step_lower.find(pattern)
        if idx >= 0:
            return step_lower[idx:]
    return step_lower


def validate_test_procedure(text: str, tc_title: str | None = None) -> ValidationResult:
    """Validate test procedure field."""
    check = "test_procedure"

    if not _is_numbered_list(text):
        return ValidationResult(False, check, "Must be a numbered list.")

    step_count = _count_numbered_items(text)
    if step_count < 2:
        return ValidationResult(False, check, "Must have at least 2 steps (setup + verification).")

    steps = _numbered_lines(text)
    final_step = steps[-1].lower()

    for i, step in enumerate(steps, 1):
        forbidden = _contains_forbidden_phrase(step)
        if forbidden:
            return ValidationResult(
                False, check,
                f"Step {i} contains forbidden verification phrase '{forbidden}' (§7.1.1).",
            )

    # Final step must use preferred verification patterns from §7.1.1 / §7.5
    has_final_check = any(pattern in final_step for pattern in FINAL_STEP_PATTERNS)
    if not has_final_check:
        return ValidationResult(
            False, check,
            "Final step must use Check that / Confirm that / Read / Record / Compare (§7.5).",
        )

    # Final step must not contain vague verbs / forbidden phrases
    for vague in VAGUE_FINAL_VERBS:
        if vague in final_step:
            return ValidationResult(
                False, check,
                f"Final step contains vague verb '{vague}'.",
            )

    # Heuristic for §7.5 / §7.7: the final step should own the Test Item outcome.
    outcome_keywords = _extract_outcome_keywords(tc_title)
    if outcome_keywords:
        final_clause = _verification_clause(final_step)
        final_hits = {w for w in outcome_keywords if w in final_clause}
        if not final_hits:
            return ValidationResult(
                False, check,
                "Final step does not appear to check the Test Item outcome (§7.5).",
            )

        for i, step in enumerate(steps[:-1], 1):
            step_lower = step.lower()
            verify_clause = _verification_clause(step_lower)
            early_hits = {w for w in outcome_keywords if w in verify_clause}
            if len(early_hits) >= 2 and any(pattern in step_lower for pattern in FINAL_STEP_PATTERNS):
                return ValidationResult(
                    False, check,
                    f"Step {i} appears to validate the main outcome before the final step (§7.7).",
                )

    return ValidationResult(True, check)


# --- §8.4 Expected Result ---

def validate_expected_result(text: str, step_count: int) -> ValidationResult:
    """Validate expected result field."""
    check = "expected_result"

    if not _is_numbered_list(text):
        return ValidationResult(False, check, "Must be a numbered list.")

    result_count = _count_numbered_items(text)
    if result_count != step_count:
        return ValidationResult(
            False, check,
            f"Count mismatch: {result_count} results vs {step_count} procedure steps.",
        )

    # No vague language
    text_lower = text.lower()
    for term in VAGUE_TERMS:
        if term in text_lower:
            return ValidationResult(
                False, check,
                f"Contains vague language: '{term}'.",
            )

    return ValidationResult(True, check)


# --- §8.5 TC ID ---

def validate_tc_id(tc_id: str) -> ValidationResult:
    """Validate single TC ID format."""
    check = "tc_id"
    if not TC_ID_PATTERN.match(tc_id):
        return ValidationResult(
            False, check,
            f"Invalid TC ID format: '{tc_id}'. Expected {{project}}-{{abbr}}-{{3-digit}}.",
        )
    return ValidationResult(True, check)


def validate_tc_ids_sequence(ids: list[str]) -> ValidationResult:
    """Validate TC ID sequence: no duplicates, monotonically increasing."""
    check = "tc_id_sequence"

    if len(ids) != len(set(ids)):
        return ValidationResult(False, check, "Duplicate TC IDs found.")

    # Extract sequence numbers and check monotonic increase
    sequences = []
    for tc_id in ids:
        parts = tc_id.rsplit("-", 1)
        if len(parts) == 2 and parts[1].isdigit():
            sequences.append(int(parts[1]))

    for i in range(1, len(sequences)):
        if sequences[i] <= sequences[i - 1]:
            return ValidationResult(
                False, check,
                f"TC IDs not monotonically increasing at index {i}.",
            )

    return ValidationResult(True, check)


# --- §8.6 Design Method ---

# LLM 常回傳短版英文（如 "State Transition"），這些關鍵字皆視為合法
DESIGN_METHOD_KEYWORDS = list(_DESIGN_METHOD_ALIASES.keys())


def normalize_design_method(method: str | None) -> str:
    """Normalize short English / mixed labels to the canonical dropdown string."""
    if not method:
        return ""
    text = str(method).strip()
    if not text:
        return ""
    if text in VALID_DESIGN_METHODS:
        return text
    low = text.lower()
    for alias, canonical in _DESIGN_METHOD_ALIASES.items():
        if alias in low:
            return canonical
    return ""


def validate_design_method(method: str) -> ValidationResult:
    """Validate design method against the 9 methods in
    `Test Case Design Method 判斷規則.md`.

    - 完全匹配 VALID_DESIGN_METHODS：pass
    - 僅關鍵字匹配（例：AI 回 "State Transition"）：pass，但回傳訊息提示
      建議改用完整繁中 + 英文的標準字串
    - 兩者皆非：fail，強制 user 看到 warning
    """
    check = "design_method"
    if not method:
        return ValidationResult(False, check, "Design method is empty.")
    if method in VALID_DESIGN_METHODS:
        return ValidationResult(True, check)
    normalized = normalize_design_method(method)
    if normalized:
        matched = [kw for kw in DESIGN_METHOD_KEYWORDS if kw in method.lower()]
        return ValidationResult(
            True, check,
            f"Design method '{method}' normalized to '{normalized}'"
            + (f" via keyword {matched[0]!r}." if matched else "."),
        )
    return ValidationResult(
        False, check,
        f"Invalid design method: '{method}'. 必須是 9 種之一："
        + "／".join(VALID_DESIGN_METHODS[:3]) + " ... 等",
    )


# --- §8.7 Priority ---

def validate_priority(priority: str) -> ValidationResult:
    """Validate priority value."""
    check = "priority"
    if priority not in VALID_PRIORITIES:
        return ValidationResult(False, check, f"Invalid priority: '{priority}'.")
    return ValidationResult(True, check)


# --- Full row validation ---

def validate_row(row: dict) -> dict[str, ValidationResult]:
    """
    Run all validations on a generated TC row.

    Returns dict mapping check name -> ValidationResult.
    """
    procedure_step_count = _count_numbered_items(row.get("test_procedure", ""))

    return {
        "tc_id": validate_tc_id(row.get("tc_id", "")),
        "test_item": validate_test_item(row.get("test_item", "")),
        "pre_conditions": validate_pre_conditions(row.get("pre_conditions", "")),
        "test_procedure": validate_test_procedure(
            row.get("test_procedure", ""),
            tc_title=(row.get("test_item", "").split("\n\n", 1)[1] if "\n\n" in row.get("test_item", "") else ""),
        ),
        "expected_result": validate_expected_result(
            row.get("expected_result", ""),
            step_count=procedure_step_count,
        ),
        "design_method": validate_design_method(row.get("design_method", "")),
        "priority": validate_priority(row.get("priority", "")),
    }
