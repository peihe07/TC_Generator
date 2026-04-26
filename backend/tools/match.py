"""match_spec tool：根據 SYS1 reference workbook 為 rows 匹配 Specification Reference。

純函式。Reference workbook 已由 route / agent 落地為磁碟路徑。
"""

from __future__ import annotations

from pathlib import Path

from spec_matcher import build_spec_index, load_spec_index, match_spec_references

from .errors import ToolError
from .registry import SafetyLevel, ToolSpec, register_tool
from .schemas import MATCH_SPEC_SCHEMA


def match_spec_tool(
    *,
    rows: list[dict],
    reference_workbook_path: str | None = None,
    selected_spec_name: str | None = None,
) -> dict:
    """回傳 spec match summary + per-row matches。

    Args:
        rows: snake_case dict，必要欄位 `id`、`req_id`、`test_item`
        reference_workbook_path: 可選 SYS1 .xlsx 絕對路徑；None 時走 unmatched fallback
        selected_spec_name: 從 ``spec-index/cache/`` 預建快取載入的 spec basename。
            若同時給定 ``reference_workbook_path``，``selected_spec_name`` 優先。

    Raises:
        ToolError: reference workbook 存在但無法解析
    """
    reference_index: dict = {}
    if selected_spec_name:
        try:
            reference_index = load_spec_index(names=[selected_spec_name])
        except Exception:
            reference_index = {}
    elif reference_workbook_path:
        ref_path = Path(reference_workbook_path)
        if not ref_path.is_file():
            raise ToolError(
                f"reference workbook not found: {reference_workbook_path}",
                code="not_found",
            )
        try:
            reference_index = build_spec_index(str(ref_path))
        except Exception:
            # 對齊原 route 行為：解析失敗當作無 reference，走 fallback
            reference_index = {}

    if reference_index:
        matched_rows = match_spec_references(rows, reference_index)
    else:
        matched_rows = [
            {**row, "spec_reference": None, "match_type": "unmatched"}
            for row in rows
        ]

    exact_count = sum(1 for row in matched_rows if row.get("match_type") == "exact")
    fuzzy_count = sum(1 for row in matched_rows if row.get("match_type") == "fuzzy")
    unmatched_count = len(matched_rows) - exact_count - fuzzy_count

    return {
        "summary": {
            "total": len(matched_rows),
            "exact": exact_count,
            "fuzzy": fuzzy_count,
            "unmatched": unmatched_count,
            "hasReferenceWorkbook": bool(reference_index),
        },
        "matches": [
            {
                "id": row.get("id"),
                "reqId": row.get("req_id"),
                "testItem": row.get("test_item"),
                "specReference": row.get("spec_reference"),
                "matchType": row.get("match_type"),
                "matchScore": row.get("match_score"),
            }
            for row in matched_rows
        ],
    }


register_tool(
    ToolSpec(
        name="match_spec",
        func=match_spec_tool,
        description=MATCH_SPEC_SCHEMA["description"],
        safety=SafetyLevel.READ_ONLY,
        input_schema=MATCH_SPEC_SCHEMA,
    )
)
