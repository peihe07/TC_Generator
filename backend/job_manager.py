"""Job state manager for TC review workflow (Phase 10.5).

Manages per-row review status, inline edits, re-validation, and export filtering.
Job state persisted as JSON for session recovery.
"""
import json
import os
from datetime import datetime

from validator import validate_row

VALID_STATUSES = {"pending", "accepted", "edited", "rejected", "flagged"}

# Fields stored in original/generated/edited
CONTENT_FIELDS = [
    "tc_title", "pre_conditions", "input_test_data",
    "test_procedure", "expected_result", "design_method", "priority",
    "split_flag", "split_reason",
]

ORIGINAL_FIELDS = ["test_item", "test_procedure", "expected_result"]


def create_job(parsed_data: dict, job_id: str) -> dict:
    """Create a new job from parsed xlsx data."""
    rows = []
    for row in parsed_data["rows"]:
        rows.append({
            "row_num": row["row_num"],
            "req_id": row.get("req_id", ""),
            "tc_id": row.get("tc_id", ""),
            "original": {field: row.get(field, "") for field in ORIGINAL_FIELDS},
            "generated": None,
            "edited": None,
            "validation": {"status": None, "issues": []},
            "review_status": "pending",
            "generation_history": [],
        })

    return {
        "job_id": job_id,
        "project": parsed_data["project"],
        "test_group": parsed_data["test_group"],
        "rows": rows,
        "config": {},
        "created_at": datetime.now().isoformat(),
    }


def save_job(job: dict, filepath: str) -> None:
    """Save job state to JSON file."""
    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(job, f, indent=2, ensure_ascii=False)


def load_job(filepath: str) -> dict | None:
    """Load job state from JSON file. Returns None if not found."""
    if not os.path.exists(filepath):
        return None
    with open(filepath) as f:
        return json.load(f)


def _find_row(job: dict, row_num: int) -> dict:
    """Find row by row_num. Raises ValueError if not found."""
    for row in job["rows"]:
        if row["row_num"] == row_num:
            return row
    raise ValueError(f"Row {row_num} not found in job")


def update_row_status(job: dict, row_num: int, status: str) -> None:
    """Update review status for a specific row."""
    if status not in VALID_STATUSES:
        raise ValueError(f"Invalid status '{status}'. Must be one of: {VALID_STATUSES}")
    row = _find_row(job, row_num)
    row["review_status"] = status


def _get_final_content(row: dict) -> dict:
    """Get the final content for a row (edited takes priority over generated)."""
    if row["edited"]:
        return {**row["edited"]}
    if row["generated"]:
        return {**row["generated"]}
    return {}


def _validate_content(row: dict, content: dict) -> dict:
    """Run validator on content and return validation result."""
    # Build a row dict that validator expects
    validate_input = {
        "tc_id": row.get("tc_id", ""),
        "test_item": f"{row['original'].get('test_item', '')}\n\n{content.get('tc_title', '')}",
        "pre_conditions": content.get("pre_conditions", ""),
        "test_procedure": content.get("test_procedure", ""),
        "expected_result": content.get("expected_result", ""),
        "design_method": content.get("design_method", ""),
        "priority": content.get("priority", ""),
    }
    results = validate_row(validate_input)
    issues = [
        {"check": v.check, "message": v.message}
        for v in results.values() if not v.passed
    ]
    status = "fail" if issues else "pass"
    return {"status": status, "issues": issues}


def edit_row(job: dict, row_num: int, edits: dict) -> None:
    """
    Apply user edits to a row. Merges with generated content, re-validates.

    The edited field stores the full merged content (generated + user overrides).
    """
    row = _find_row(job, row_num)

    # Merge: start from generated, apply edits on top
    base = {**row["generated"]} if row["generated"] else {}
    if row["edited"]:
        base.update(row["edited"])
    base.update(edits)
    row["edited"] = base
    row["review_status"] = "edited"

    # Re-validate the merged content
    row["validation"] = _validate_content(row, base)


def get_rows_by_status(job: dict, status: str) -> list[dict]:
    """Filter rows by review status."""
    return [r for r in job["rows"] if r["review_status"] == status]


def get_exportable_rows(job: dict) -> list[dict]:
    """
    Get rows ready for export (accepted + edited).

    Returns flat dicts with row_num, tc_id, and all content fields
    ready for the writer module.
    """
    exportable = []
    for row in job["rows"]:
        if row["review_status"] not in ("accepted", "edited"):
            continue

        content = _get_final_content(row)
        exportable.append({
            "row_num": row["row_num"],
            "tc_id": row.get("tc_id", ""),
            "test_group": job["test_group"],
            "test_set": content.get("test_set"),
            **{field: content.get(field, "") for field in CONTENT_FIELDS},
        })

    return exportable


def get_job_stats(job: dict) -> dict:
    """Count rows per review status."""
    stats = {"total": len(job["rows"])}
    for status in VALID_STATUSES:
        stats[status] = sum(1 for r in job["rows"] if r["review_status"] == status)
    return stats
