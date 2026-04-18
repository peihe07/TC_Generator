"""validate_tc tool：對單一 TC dict 執行程式化驗證。

Pure function。Route / SSE stream / Agent 都可直接呼叫。
"""

from __future__ import annotations

from validator import validate_row

from .registry import SafetyLevel, ToolSpec, register_tool
from .schemas import VALIDATE_TC_SCHEMA


def _normalize_issues(results: dict) -> list[dict]:
    """把 validator 原始結果轉成 API issue payload。"""
    issues: list[dict] = []
    for check, result in results.items():
        if result.passed:
            continue
        issues.append(
            {
                "id": f"{check}-{len(issues) + 1}",
                "severity": "warning",
                "field": check,
                "message": result.message or f"{check} failed validation.",
            }
        )

    if not issues:
        issues.append(
            {
                "id": "validation-pass",
                "severity": "passing",
                "field": "expected_result",
                "message": "Generated row passed the current programmatic validation checks.",
            }
        )

    return issues


def validate_tc_tool(*, tc: dict) -> dict:
    """驗證單一 TC dict。

    Args:
        tc: snake_case 欄位 — `tc_id`、`test_item`、`pre_conditions`、
            `test_procedure`、`expected_result`、`design_method`、`priority`

    Returns:
        `{"issues": [...], "hasWarnings": bool}`
        `hasWarnings` 為 True 表示至少有一筆 `severity == warning`。
    """
    issues = _normalize_issues(validate_row(tc))
    has_warnings = any(issue["severity"] == "warning" for issue in issues)
    return {"issues": issues, "hasWarnings": has_warnings}


register_tool(
    ToolSpec(
        name="validate_tc",
        func=validate_tc_tool,
        description=VALIDATE_TC_SCHEMA["description"],
        safety=SafetyLevel.READ_ONLY,
        input_schema=VALIDATE_TC_SCHEMA,
    )
)
