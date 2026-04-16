"""Prompt builder for TC generation (RULES.md §12)."""
from spec_matcher import extract_pdm_codes


REQUIRED_OUTPUT_KEYS = [
    "test_item_rewrite",
    "pre_conditions",
    "input_test_data",
    "test_procedure",
    "expected_result",
    "design_method",
    "priority",
    "split_flag",
    "split_reason",
]


def build_system_prompt() -> str:
    """Build system prompt for ASPICE SWE.6 test case writer."""
    return (
        "You are an ASPICE SWE.6 test case writer. "
        "Return ONLY valid JSON, no markdown fences."
    )


def build_batch_system_prompt() -> str:
    """Build system prompt for batch TC generation."""
    return (
        "You are an ASPICE SWE.6 test case writer. "
        "Return a JSON array, one object per TC. No markdown fences."
    )


def _get_spec_context(row: dict, spec_index: dict | None) -> str:
    """Extract relevant spec context for a single row."""
    if not spec_index:
        return "N/A"

    codes = extract_pdm_codes(row["test_item"])
    segments = []
    for code in codes:
        if code in spec_index:
            entry = spec_index[code]
            text = entry.get("full_text") or entry.get("description", "")
            if text:
                segments.append(f"[{code}] {text}")

    return "\n".join(segments) if segments else "N/A"


def build_user_prompt(
    row: dict,
    context: dict,
    spec_index: dict | None,
    rules_text: str,
) -> str:
    """Build user prompt for single TC generation."""
    spec_context = _get_spec_context(row, spec_index)
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)

    return f"""## Context
- Project: {context['project']}
- Test Group: {context['test_group']}
- Test Set: {context.get('test_set', 'N/A')}

## Requirement
- Requirement ID: {row['req_id']}
- Original Test Item: {row['test_item']}

## Spec Context
{spec_context}

## Rules
{rules_text}

## Output
Return JSON with keys: {output_keys}"""


def build_quick_generate_prompt(
    test_item: str,
    context: str | None,
    rules_text: str,
) -> str:
    """Build prompt for quick (ad-hoc) single TC generation."""
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)
    context_section = f"\n## Additional Context\n{context}" if context else ""
    return f"""## Task
Generate a single test case for the following test item. Follow all rules strictly.

## Test Item
{test_item}{context_section}

## Rules
{rules_text}

## Output
Return JSON with keys: {output_keys}"""


def build_decompose_prompt(requirement: str, rules_text: str) -> str:
    """Build prompt to decompose a requirement into distinct test scenarios."""
    return f"""## Task
Analyze the following software requirement and decompose it into distinct, independent test scenarios.
Each scenario should cover a different aspect, condition, or behaviour path.

## Requirement
{requirement}

## Rules (for context, these will guide TC generation after decomposition)
{rules_text}

## Output
Return ONLY valid JSON (no markdown fences) with this exact structure:
{{
  "reasoning": "<explain how you identified the scenarios and why>",
  "scenarios": [
    {{
      "id": 1,
      "name": "<short scenario name>",
      "description": "<one-sentence description of what this scenario tests>",
      "test_item": "<rewritten test item statement for this specific scenario>"
    }}
  ]
}}"""


def build_batch_prompt(
    rows: list[dict],
    context: dict,
    spec_index: dict | None,
    rules_text: str,
) -> str:
    """Build user prompt for batch TC generation."""
    items = []
    for i, row in enumerate(rows):
        spec_context = _get_spec_context(row, spec_index)
        items.append(
            f"### TC {i + 1}\n"
            f"- Req ID: {row['req_id']}\n"
            f"- Test Set: {row.get('test_set', context.get('test_set', 'N/A'))}\n"
            f"- Test Item: {row['test_item']}\n"
            f"- Spec: {spec_context}"
        )
    batch_text = "\n\n".join(items)
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)

    return f"""## Context
- Project: {context['project']}
- Test Group: {context['test_group']}
- Test Set: {context.get('test_set', 'N/A')}

## Requirements
{batch_text}

## Rules
{rules_text}

## Output
Return a JSON Array with one object per TC. Each object has keys: {output_keys}"""
