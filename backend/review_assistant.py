"""Narrow AI assist for Review module: given a TC and its validation errors,
return a structured fix proposal plus a short reason string the reviewer
can paste into the Regenerate Reason field.

Replaces the removed generic agent co-pilot — single-purpose, single-call,
no session, no streaming, no chat panel.
"""
from __future__ import annotations

import json
from typing import Any

from generator import DEFAULT_MODEL, GenerationError, _chat, _usage_tokens, calculate_cost


_VALID_FIELDS = {
    "tc_title",
    "pre_conditions",
    "input_test_data",
    "test_procedure",
    "expected_result",
    "design_method",
    "priority",
}


_SYSTEM_PROMPT = (
    "You are an ASPICE SWE.6 test case reviewer assistant. The user shows you "
    "ONE test case that failed validation, plus the validator's complaints. "
    "Your job is to explain WHAT is wrong, WHICH fields are affected, WHAT "
    "the concrete change should be, and provide a short regenerate-reason "
    "string ready to paste into the AI.\n\n"
    "Return ONLY a JSON object with these keys (every key is mandatory):\n\n"
    "  - problem_root_cause (string, Traditional Chinese, 2–4 sentences): "
    "點出最根本的問題：哪個欄位 / 違反哪一條 ASPICE SWE.6 規則 / 為什麼此寫法"
    "在規則下不成立。引用節號（§6.1 / §7.5 / §8 / §9 / §10.x）以利 reviewer 對照。\n\n"
    "  - affected_fields (array of string): list of TC field keys this fix "
    "would touch. Use ONLY these snake_case identifiers: tc_title, "
    "pre_conditions, input_test_data, test_procedure, expected_result, "
    "design_method, priority. Empty array if the issue is structural / "
    "cross-field.\n\n"
    "  - proposed_change (string, Traditional Chinese, 2–5 sentences): "
    "具體該怎麼改。明確指出每個 affected_field 的目前內容缺口、應補入什麼、"
    "範例（簡短，不必寫完整新值）。例：「tc_title 目前是 `Select X` 為裸"
    "動作，建議補上前置條件，例如 `Select X with iPhone connected via "
    "USB → CarPlay 顯示`。」\n\n"
    "  - suggested_reason (string, English, single imperative sentence, "
    "<= 35 words): the regenerate-reason text the reviewer will hand to the "
    "AI. Must reference the concrete change, NOT the validator message. "
    "Example: `Add precondition (iPhone connected via USB) to tc_title "
    "trigger so it distinguishes from the no-phone-paired sibling.`"
)


def _format_tc(tc: dict[str, Any]) -> str:
    """以 reviewer 視角呈現 TC 欄位（保留缺值，方便 LLM 看出哪欄空）。"""
    lines: list[str] = []
    for key in (
        "tc_id",
        "req_id",
        "tc_title",
        "pre_conditions",
        "input_test_data",
        "test_procedure",
        "expected_result",
        "design_method",
        "priority",
    ):
        value = tc.get(key, "")
        rendered = str(value).strip() if value not in (None, "") else "(empty)"
        lines.append(f"## {key}\n{rendered}")
    return "\n\n".join(lines)


def _format_errors(errors: list[dict[str, Any]]) -> str:
    if not errors:
        return "(none)"
    out = []
    for i, err in enumerate(errors, 1):
        sev = str(err.get("severity") or "warning")
        field = str(err.get("field") or "?")
        msg = str(err.get("message") or "")
        out.append(f"{i}. [{sev.upper()} • {field}] {msg}")
    return "\n".join(out)


def _normalize_affected_fields(raw: Any) -> list[str]:
    """Accept whatever AI returned; keep only known snake_case field keys."""
    if not isinstance(raw, list):
        return []
    out: list[str] = []
    for item in raw:
        key = str(item or "").strip().lower()
        if key in _VALID_FIELDS and key not in out:
            out.append(key)
    return out


def suggest_review_fix(
    *,
    tc: dict[str, Any],
    errors: list[dict[str, Any]],
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> dict[str, Any]:
    """LLM 一次性呼叫 → 結構化 fix proposal。

    Returns dict with keys:
      problem_root_cause, affected_fields, proposed_change,
      suggested_reason, usage, cost, model.

    呼叫方（API endpoint）負責 HTTP 包裝；本函式只負責拼 prompt + 解 JSON。
    """
    user_prompt = (
        f"# Validation errors\n{_format_errors(errors)}\n\n"
        f"# Test Case under review\n{_format_tc(tc)}\n\n"
        f"# Project rules excerpt\n{(rules_text or '').strip() or '(none provided)'}\n"
    )
    response = _chat(_SYSTEM_PROMPT, user_prompt, model, max_tokens=1200)
    raw = response.choices[0].message.content or ""
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise GenerationError(f"suggest_review_fix returned non-JSON: {raw[:200]}") from exc

    problem_root_cause = str(parsed.get("problem_root_cause") or "").strip()
    proposed_change = str(parsed.get("proposed_change") or "").strip()
    suggested_reason = str(parsed.get("suggested_reason") or "").strip()
    affected_fields = _normalize_affected_fields(parsed.get("affected_fields"))

    if not problem_root_cause:
        raise GenerationError("suggest_review_fix: empty problem_root_cause")
    if not proposed_change:
        raise GenerationError("suggest_review_fix: empty proposed_change")

    tokens = _usage_tokens(response.usage)
    return {
        "problem_root_cause": problem_root_cause,
        "affected_fields": affected_fields,
        "proposed_change": proposed_change,
        "suggested_reason": suggested_reason,
        "usage": tokens,
        "cost": calculate_cost(
            input_tokens=tokens.get("input", 0),
            output_tokens=tokens.get("output", 0),
            model=model,
            cache_read_tokens=tokens.get("cache_read", 0),
            cache_creation_tokens=tokens.get("cache_creation", 0),
        ),
        "model": model,
    }
