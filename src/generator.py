"""TC generator — AI call, response parsing, cost tracking (RULES.md §12)."""
import json
import re
from dataclasses import dataclass, field

import anthropic

from prompt_builder import (
    build_system_prompt,
    build_batch_system_prompt,
    build_user_prompt,
    build_batch_prompt,
    build_quick_generate_prompt,
    build_decompose_prompt,
    REQUIRED_OUTPUT_KEYS,
)

# Pricing per million tokens (verify at docs.anthropic.com)
MODEL_PRICING = {
    "claude-sonnet-4-6": {"input": 3.0, "output": 15.0},
    "claude-haiku-4-5-20251001": {"input": 0.80, "output": 4.0},
}

DEFAULT_MODEL = "claude-sonnet-4-6"
MAX_RETRIES = 2


class GenerationError(Exception):
    """Raised when TC generation fails."""


@dataclass
class GenerationResult:
    """Result of a TC generation call."""
    tc_data: dict | list[dict]
    input_tokens: int = 0
    output_tokens: int = 0
    cost: float = 0.0
    model: str = ""


def _strip_fences(text: str) -> str:
    """Strip markdown code fences from text."""
    match = re.search(r"```(?:json)?\s*\n?(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else text.strip()


def parse_tc_response(raw: str) -> dict:
    """Parse single TC JSON response. Raises GenerationError on failure."""
    text = _strip_fences(raw)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise GenerationError(f"Failed to parse TC response: {e}") from e

    # Validate required keys
    missing = [k for k in REQUIRED_OUTPUT_KEYS if k not in data]
    if missing:
        raise GenerationError(f"TC response missing required keys: {missing}")

    return data


def parse_batch_response(raw: str, expected_count: int | None = None) -> list[dict]:
    """Parse batch TC JSON array response. Raises GenerationError on failure."""
    text = _strip_fences(raw)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise GenerationError(f"Failed to parse batch response: {e}") from e

    if not isinstance(data, list):
        raise GenerationError(f"Expected JSON array, got {type(data).__name__}")

    # Validate each item
    for i, item in enumerate(data):
        missing = [k for k in REQUIRED_OUTPUT_KEYS if k not in item]
        if missing:
            raise GenerationError(f"TC[{i}] missing required keys: {missing}")

    if expected_count is not None and len(data) != expected_count:
        raise GenerationError(
            f"Batch response count mismatch: expected {expected_count}, got {len(data)}"
        )

    return data


def calculate_cost(
    input_tokens: int,
    output_tokens: int,
    model: str,
) -> float:
    """Calculate API cost in USD."""
    pricing = MODEL_PRICING.get(model, MODEL_PRICING[DEFAULT_MODEL])
    return (
        (input_tokens / 1_000_000 * pricing["input"])
        + (output_tokens / 1_000_000 * pricing["output"])
    )


def generate_single_tc(
    row: dict,
    context: dict,
    spec_index: dict | None,
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> GenerationResult:
    """
    Generate a single TC by calling Claude API.

    Raises GenerationError on API or parse failure.
    """
    client = anthropic.Anthropic()
    system_prompt = build_system_prompt()
    user_prompt = build_user_prompt(row, context, spec_index, rules_text)

    try:
        response = client.messages.create(
            model=model,
            max_tokens=2000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
    except Exception as e:
        raise GenerationError(f"API call failed: {e}") from e

    raw_text = response.content[0].text
    tc_data = parse_tc_response(raw_text)
    cost = calculate_cost(
        response.usage.input_tokens,
        response.usage.output_tokens,
        model,
    )

    return GenerationResult(
        tc_data=tc_data,
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
        cost=cost,
        model=model,
    )


@dataclass
class DecomposeResult:
    """Result of a requirement decomposition call."""
    reasoning: str
    scenarios: list[dict]
    input_tokens: int = 0
    output_tokens: int = 0
    cost: float = 0.0


def generate_quick_tc(
    test_item: str,
    context: str | None,
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> GenerationResult:
    """
    Generate a single TC from ad-hoc input (no job context required).

    Raises GenerationError on API or parse failure.
    """
    client = anthropic.Anthropic()
    system_prompt = build_system_prompt()
    user_prompt = build_quick_generate_prompt(test_item, context, rules_text)

    try:
        response = client.messages.create(
            model=model,
            max_tokens=2000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
    except Exception as e:
        raise GenerationError(f"API call failed: {e}") from e

    raw_text = response.content[0].text
    tc_data = parse_tc_response(raw_text)
    cost = calculate_cost(response.usage.input_tokens, response.usage.output_tokens, model)

    return GenerationResult(
        tc_data=tc_data,
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
        cost=cost,
        model=model,
    )


def decompose_requirement(
    requirement: str,
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> DecomposeResult:
    """
    Decompose a requirement into distinct test scenarios.

    Returns structured analysis + scenario list.
    Raises GenerationError on API or parse failure.
    """
    client = anthropic.Anthropic()
    user_prompt = build_decompose_prompt(requirement, rules_text)

    try:
        response = client.messages.create(
            model=model,
            max_tokens=2000,
            system="You are an ASPICE SWE.6 test analyst. Return ONLY valid JSON, no markdown fences.",
            messages=[{"role": "user", "content": user_prompt}],
        )
    except Exception as e:
        raise GenerationError(f"API call failed: {e}") from e

    raw_text = response.content[0].text
    text = _strip_fences(raw_text)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise GenerationError(f"Failed to parse decompose response: {e}") from e

    if not isinstance(data, dict) or "scenarios" not in data:
        raise GenerationError("Decompose response missing 'scenarios' field")

    cost = calculate_cost(response.usage.input_tokens, response.usage.output_tokens, model)

    return DecomposeResult(
        reasoning=data.get("reasoning", ""),
        scenarios=data["scenarios"],
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
        cost=cost,
    )


def generate_batch(
    rows: list[dict],
    context: dict,
    spec_index: dict | None,
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> GenerationResult:
    """
    Generate multiple TCs in a single API call.

    Raises GenerationError on API or parse failure.
    """
    client = anthropic.Anthropic()
    system_prompt = build_batch_system_prompt()
    user_prompt = build_batch_prompt(rows, context, spec_index, rules_text)

    try:
        response = client.messages.create(
            model=model,
            max_tokens=2000 * len(rows),
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
    except Exception as e:
        raise GenerationError(f"API call failed: {e}") from e

    raw_text = response.content[0].text
    tc_data = parse_batch_response(raw_text, expected_count=len(rows))
    cost = calculate_cost(
        response.usage.input_tokens,
        response.usage.output_tokens,
        model,
    )

    return GenerationResult(
        tc_data=tc_data,
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
        cost=cost,
        model=model,
    )
