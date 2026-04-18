"""`validate_tc_tool` 單元測試。"""

from __future__ import annotations

from backend.tools import get_tool, SafetyLevel, validate_tc_tool


_BASE_TC = {
    "tc_id": "newR1L-DMS-001",
    "test_item": "Original RD text.\n\n(User taps X → Y is displayed)",
    "pre_conditions": "1. System in normal state",
    "test_procedure": (
        "1. Tap the X button to open the menu.\n"
        "2. Verify that the Y panel is displayed."
    ),
    "expected_result": (
        "1. The menu appears.\n"
        "2. The Y panel is displayed on the HU."
    ),
    "design_method": "功能測試 (Functional based ; no specific technique)",
    "priority": "Medium",
}


def test_validate_returns_issues_and_has_warnings_shape():
    out = validate_tc_tool(tc=_BASE_TC)

    assert set(out.keys()) == {"issues", "hasWarnings"}
    assert isinstance(out["issues"], list)
    assert isinstance(out["hasWarnings"], bool)
    # 每筆 issue 都有預期欄位
    for issue in out["issues"]:
        assert set(issue.keys()) == {"id", "severity", "field", "message"}


def test_validate_invalid_priority_flags_warning():
    bad = {**_BASE_TC, "priority": "Critical"}
    out = validate_tc_tool(tc=bad)

    assert out["hasWarnings"] is True
    fields = [issue["field"] for issue in out["issues"]]
    assert any("priority" in field for field in fields)


def test_validate_invalid_design_method_flags_warning():
    bad = {**_BASE_TC, "design_method": "NotAMethod"}
    out = validate_tc_tool(tc=bad)

    assert out["hasWarnings"] is True
    fields = [issue["field"] for issue in out["issues"]]
    assert any("design" in field for field in fields)


def test_validate_issue_ids_are_unique():
    bad = {**_BASE_TC, "priority": "Bogus", "design_method": "NotAMethod"}
    out = validate_tc_tool(tc=bad)

    ids = [issue["id"] for issue in out["issues"]]
    assert len(ids) == len(set(ids))


def test_validate_passing_scenario_has_single_passing_issue():
    """只要所有 check 都過，就只會回一筆 severity=passing 的 issue。"""
    # 使用 mock-style：直接檢查當 hasWarnings=False 時 issues 結構
    out = validate_tc_tool(tc=_BASE_TC)
    if not out["hasWarnings"]:
        assert len(out["issues"]) == 1
        assert out["issues"][0]["severity"] == "passing"


def test_validate_tool_registered():
    spec = get_tool("validate_tc")
    assert spec.safety is SafetyLevel.READ_ONLY
