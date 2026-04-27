"""Narrow AI assist for Review module: given a TC and its validation errors,
return a human-readable fix suggestion plus a short reason string the
reviewer can paste into the Regenerate Reason field.

Replaces the removed generic agent co-pilot — single-purpose, single-call,
no session, no streaming, no chat panel.
"""
from __future__ import annotations

import json
from typing import Any

from generator import DEFAULT_MODEL, GenerationError, _chat, _usage_tokens, calculate_cost


_SYSTEM_PROMPT = (
    "You are an ASPICE SWE.6 test case reviewer assistant. The user shows you "
    "ONE test case that failed validation, plus the validator's complaints. "
    "Your job: explain what is wrong and how to fix it, then propose a SHORT "
    "regenerate reason the human can hand to the regenerator.\n\n"
    "Return ONLY a JSON object with these keys:\n"
    "  - suggestion (string): 2–6 sentences in Traditional Chinese explaining "
    "the root cause and the concrete fix. Reference specific TC fields "
    "(tc_title, pre_conditions, test_procedure step N, expected_result, "
    "design_method, priority) when relevant.\n"
    "  - suggested_reason (string): a single short imperative sentence "
    "(<= 30 words) in English, suitable to paste verbatim into the "
    "regenerate-reason input. Must reference the concrete change needed, not "
    "the validation message itself."
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


def suggest_review_fix(
    *,
    tc: dict[str, Any],
    errors: list[dict[str, Any]],
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> dict[str, Any]:
    """LLM 一次性呼叫 → 回 {suggestion, suggested_reason, usage, cost, model}.

    呼叫方（API endpoint）負責 HTTP 包裝；本函式只負責拼 prompt + 解 JSON。
    """
    user_prompt = (
        f"# Validation errors\n{_format_errors(errors)}\n\n"
        f"# Test Case under review\n{_format_tc(tc)}\n\n"
        f"# Project rules excerpt\n{(rules_text or '').strip() or '(none provided)'}\n"
    )
    response = _chat(_SYSTEM_PROMPT, user_prompt, model, max_tokens=800)
    raw = response.choices[0].message.content or ""
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise GenerationError(f"suggest_review_fix returned non-JSON: {raw[:200]}") from exc

    suggestion = str(parsed.get("suggestion") or "").strip()
    suggested_reason = str(parsed.get("suggested_reason") or "").strip()
    if not suggestion:
        raise GenerationError("suggest_review_fix: empty suggestion")

    tokens = _usage_tokens(response.usage)
    return {
        "suggestion": suggestion,
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
