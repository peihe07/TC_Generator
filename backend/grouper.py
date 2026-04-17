"""Test Set grouper (RULES.md §2.3).

Clusters Test Items into sub-feature groups.
First run: AI clustering. Subsequent runs: use confirmed framework.json.
"""
import json
import os
import re
from fnmatch import fnmatch


def load_framework(filepath: str) -> dict | None:
    """Load confirmed framework mapping from JSON file."""
    if not os.path.exists(filepath):
        return None
    with open(filepath) as f:
        return json.load(f)


def save_framework(framework: dict, filepath: str) -> None:
    """Save framework mapping to JSON file."""
    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(framework, f, indent=2, ensure_ascii=False)


def assign_test_sets(rows: list[dict], framework: dict) -> list[dict]:
    """
    Assign Test Set to each row based on framework mapping.

    Framework maps Test Set name -> list of Req ID patterns (supports * wildcard).
    Returns new list with 'test_set' field added.
    """
    results = []
    for row in rows:
        req_id = row["req_id"]
        matched_set = None

        for set_name, patterns in framework.items():
            for pattern in patterns:
                if fnmatch(req_id, pattern):
                    matched_set = set_name
                    break
            if matched_set:
                break

        results.append({**row, "test_set": matched_set})

    return results


def build_framework_sheet_data(test_group: str, framework: dict) -> list[dict]:
    """
    Build data for Test Case Framework sheet.

    Returns list of {test_group, test_set, req_count}.
    """
    return [
        {
            "test_group": test_group,
            "test_set": set_name,
            "req_count": len(patterns),
        }
        for set_name, patterns in framework.items()
    ]


def build_grouping_prompt(rows: list[dict]) -> str:
    """
    Build prompt for AI-based Test Set clustering.

    Sends all Test Items and asks AI to return sub-feature grouping as JSON.
    """
    items_text = "\n".join(
        f"- {row['req_id']}: {row['test_item']}" for row in rows
    )

    return f"""Analyze the following test requirements and cluster them into sub-feature groups (Test Sets).

## Requirements
{items_text}

## Instructions
- Group related requirements into meaningful sub-feature categories
- Each group should have a short English label (e.g. "Access & Entry", "Device List & Recognition")
- Each requirement should belong to exactly one group
- Use wildcard patterns for Req IDs (e.g. "SWE1-HMI-DM-001-*" matches all TCs under that requirement)

## Output
Return ONLY a JSON object mapping Test Set names to arrays of Req ID patterns:
{{"Test Set Name": ["pattern1", "pattern2"], "Another Set": ["pattern3"]}}"""


def parse_grouping_response(raw: str) -> dict:
    """
    Parse AI response into framework dict.

    Handles raw JSON or JSON wrapped in markdown code fences.
    Raises ValueError if response is not valid JSON.
    """
    text = raw.strip()

    # Strip markdown code fences
    fence_match = re.search(r"```(?:json)?\s*\n?(.*?)```", text, re.DOTALL)
    if fence_match:
        text = fence_match.group(1).strip()

    try:
        result = json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse grouping response as JSON: {e}") from e

    if not isinstance(result, dict):
        raise ValueError(f"Expected JSON object, got {type(result).__name__}")

    return result
