"""Phase 0 骨架測試：確認 tools package 可正確 import 並註冊 / 查詢 tool。"""

from __future__ import annotations

import pytest

from backend.tools import (
    SafetyLevel,
    ToolError,
    ToolSpec,
    get_tool,
    list_tools,
    register_tool,
)
from backend.tools._budget import needs_confirmation
from backend.tools.registry import _REGISTRY, clear_registry


@pytest.fixture(autouse=True)
def _reset_registry():
    """快照 → 清空 → 執行 → 還原，避免汙染其他測試檔的註冊狀態。"""
    snapshot = dict(_REGISTRY)
    clear_registry()
    yield
    clear_registry()
    _REGISTRY.update(snapshot)


def _dummy(**kwargs):
    return {"ok": True, "echo": kwargs}


def test_register_and_get_tool():
    spec = ToolSpec(
        name="dummy",
        func=_dummy,
        description="test only",
        safety=SafetyLevel.READ_ONLY,
    )
    register_tool(spec)

    got = get_tool("dummy")
    assert got is spec
    assert got.safety is SafetyLevel.READ_ONLY
    assert got.func(x=1) == {"ok": True, "echo": {"x": 1}}


def test_list_tools_sorted():
    register_tool(ToolSpec("b_tool", _dummy, "", SafetyLevel.READ_ONLY))
    register_tool(ToolSpec("a_tool", _dummy, "", SafetyLevel.WRITE_SAFE))

    names = [s.name for s in list_tools()]
    assert names == ["a_tool", "b_tool"]


def test_get_tool_missing_raises():
    with pytest.raises(KeyError):
        get_tool("does_not_exist")


def test_tool_error_http_status_mapping():
    err = ToolError("bad file", code="bad_request")
    assert err.http_status == 400

    err2 = ToolError("nope", code="not_found")
    assert err2.http_status == 404

    err3 = ToolError("over budget", code="budget_exceeded", details={"limit": 0.5})
    payload = err3.to_dict()
    assert payload == {
        "error": "budget_exceeded",
        "message": "over budget",
        "details": {"limit": 0.5},
    }
    assert err3.http_status == 402


def test_tool_error_default_code():
    err = ToolError("boom")
    assert err.code == "bad_request"
    assert err.details == {}


def test_budget_threshold_default():
    assert needs_confirmation(0.1) is False
    assert needs_confirmation(0.6) is True


def test_budget_threshold_override():
    assert needs_confirmation(0.1, threshold=0.05) is True
    assert needs_confirmation(1.0, threshold=2.0) is False


def test_safety_level_values():
    assert SafetyLevel.READ_ONLY.value == "read_only"
    assert SafetyLevel.DESTRUCTIVE.value == "destructive"
