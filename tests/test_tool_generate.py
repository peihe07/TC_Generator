"""`generate_tc_tool` 單元測試。"""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import patch

import pytest

from backend.tools import ToolError, estimate_batch_cost, generate_tc_tool, get_tool, SafetyLevel


_BASE_ROW = {
    "id": "r1",
    "row_num": 10,
    "tc_id": "newR1L-DMS-001",
    "req_id": "SWE1-HMI-DM-001-01",
    "test_item": "PDM01 original",
    "original_requirement": "PDM01 original",
    "test_set": "Access",
    "spec_reference": None,
    "priority": "P1",
}

_CONTEXT = {"project": "newR1L", "test_group": "DeviceManager", "test_set": "N/A"}


def _fake_tc(suffix: str = "A") -> dict:
    return {
        "test_item_rewrite": f"(Condition -> Outcome {suffix})",
        "pre_conditions": "NA",
        "input_test_data": "NA",
        "test_procedure": "1. Setup.\n2. Verify.",
        "expected_result": "1. Done.\n2. Verified.",
        "design_method": "功能測試 (Functional based ; no specific technique)",
        "priority": "P1",
        "split_flag": False,
        "split_reason": "",
    }


def test_generate_single_row_uses_multi_tc_path():
    """Default (allow_split=True) 走 generate_tcs_for_row，回傳 list[list[dict]]。"""
    fake_tc = _fake_tc("A")
    fake_result = SimpleNamespace(
        tc_data=[fake_tc],
        input_tokens=100,
        output_tokens=50,
        cache_creation_tokens=0,
        cache_read_tokens=20,
        cost=0.001,
        model="gpt-5.4-mini",
    )
    with patch("backend.tools.generate.generate_tcs_for_row", return_value=fake_result) as multi, \
         patch("backend.tools.generate.generate_batch_multi") as batch_mock:
        out = generate_tc_tool(
            rows=[_BASE_ROW],
            context=_CONTEXT,
            spec_index={},
            rules_text="RULES",
            model="gpt-5.4-mini",
        )

    assert multi.called
    assert not batch_mock.called
    # tcData 是 list[list[dict]]
    assert out["tcData"] == [[fake_tc]]
    assert out["cost"] == 0.001
    assert out["inputTokens"] == 100


def test_generate_single_row_splits_into_multiple_tcs():
    """AI 判斷一個 req 需 3 筆 TC，tool 回傳 [[tc1, tc2, tc3]]。"""
    tcs = [_fake_tc("A"), _fake_tc("B"), _fake_tc("C")]
    fake_result = SimpleNamespace(
        tc_data=tcs,
        input_tokens=100, output_tokens=50, cache_creation_tokens=0,
        cache_read_tokens=0, cost=0.001, model="gpt-5.4-mini",
    )
    with patch("backend.tools.generate.generate_tcs_for_row", return_value=fake_result):
        out = generate_tc_tool(
            rows=[_BASE_ROW], context=_CONTEXT, rules_text="RULES",
        )
    assert out["tcData"] == [tcs]


def test_generate_multi_row_uses_batch_multi_path():
    tc_groups = [[_fake_tc("A1"), _fake_tc("A2")], [_fake_tc("B1")]]
    fake_result = SimpleNamespace(
        tc_data=tc_groups,
        input_tokens=200,
        output_tokens=90,
        cache_creation_tokens=0,
        cache_read_tokens=0,
        cost=0.002,
        model="gpt-5.4-mini",
    )
    with patch("backend.tools.generate.generate_batch_multi", return_value=fake_result) as batch_mock, \
         patch("backend.tools.generate.generate_tcs_for_row") as single_mock:
        out = generate_tc_tool(
            rows=[_BASE_ROW, {**_BASE_ROW, "id": "r2", "row_num": 11}],
            context=_CONTEXT,
            spec_index={},
            rules_text="RULES",
        )

    assert batch_mock.called
    assert not single_mock.called
    assert out["tcData"] == tc_groups
    assert out["cost"] == 0.002


def test_generate_legacy_single_path_with_allow_split_false():
    """allow_split=False 走舊的 generate_single_tc，回傳仍包成 [[tc]] 以統一介面。"""
    fake_tc = _fake_tc("A")
    fake_result = SimpleNamespace(
        tc_data=fake_tc,
        input_tokens=100, output_tokens=50, cache_creation_tokens=0,
        cache_read_tokens=0, cost=0.001, model="gpt-5.4-mini",
    )
    with patch("backend.tools.generate.generate_single_tc", return_value=fake_result) as single:
        out = generate_tc_tool(
            rows=[_BASE_ROW], context=_CONTEXT, rules_text="RULES",
            allow_split=False,
        )
    assert single.called
    assert out["tcData"] == [[fake_tc]]


def test_generate_empty_rows_raises():
    with pytest.raises(ToolError) as info:
        generate_tc_tool(rows=[], context=_CONTEXT, rules_text="RULES")
    assert info.value.code == "bad_request"


def test_generate_wraps_generation_error():
    from generator import GenerationError

    with patch("backend.tools.generate.generate_tcs_for_row", side_effect=GenerationError("API down")):
        with pytest.raises(ToolError) as info:
            generate_tc_tool(
                rows=[_BASE_ROW],
                context=_CONTEXT,
                rules_text="RULES",
            )
    assert info.value.code == "internal"
    assert "API down" in info.value.message


def test_generate_does_not_mutate_caller_context():
    fake_result = SimpleNamespace(
        tc_data=[_fake_tc()],
        input_tokens=1, output_tokens=1, cache_creation_tokens=0,
        cache_read_tokens=0, cost=0.0, model="",
    )
    ctx = {"project": "p", "test_group": "g", "test_set": "OriginalSet"}
    with patch("backend.tools.generate.generate_tcs_for_row", return_value=fake_result):
        generate_tc_tool(rows=[_BASE_ROW], context=ctx, rules_text="RULES")

    # caller's context 應未被改動
    assert ctx["test_set"] == "OriginalSet"


def test_estimate_batch_cost_positive():
    cost = estimate_batch_cost(row_count=10, model="gpt-5.4-mini")
    assert cost > 0


def test_generate_tool_registered():
    spec = get_tool("generate_tc")
    assert spec.safety is SafetyLevel.WRITE_COSTLY
