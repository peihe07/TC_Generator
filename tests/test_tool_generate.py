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
    "priority": "Medium",
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
        "priority": "Medium",
        "split_flag": False,
        "split_reason": "",
    }


def test_generate_single_row_uses_single_tc_path():
    fake_result = SimpleNamespace(
        tc_data=_fake_tc("A"),
        input_tokens=100,
        output_tokens=50,
        cache_creation_tokens=0,
        cache_read_tokens=20,
        cost=0.001,
        model="gpt-4.1-mini",
    )
    with patch("backend.tools.generate.generate_single_tc", return_value=fake_result) as single, \
         patch("backend.tools.generate.generate_batch") as batch_mock:
        out = generate_tc_tool(
            rows=[_BASE_ROW],
            context=_CONTEXT,
            spec_index={},
            rules_text="RULES",
            model="gpt-4.1-mini",
        )

    assert single.called
    assert not batch_mock.called
    assert out["tcData"] == [fake_result.tc_data]
    assert out["cost"] == 0.001
    assert out["inputTokens"] == 100
    assert out["outputTokens"] == 50
    assert out["cacheReadTokens"] == 20


def test_generate_multi_row_uses_batch_path():
    tcs = [_fake_tc("A"), _fake_tc("B")]
    fake_result = SimpleNamespace(
        tc_data=tcs,
        input_tokens=200,
        output_tokens=90,
        cache_creation_tokens=0,
        cache_read_tokens=0,
        cost=0.002,
        model="gpt-4.1",
    )
    with patch("backend.tools.generate.generate_batch", return_value=fake_result) as batch_mock, \
         patch("backend.tools.generate.generate_single_tc") as single_mock:
        out = generate_tc_tool(
            rows=[_BASE_ROW, {**_BASE_ROW, "id": "r2", "row_num": 11}],
            context=_CONTEXT,
            spec_index={},
            rules_text="RULES",
        )

    assert batch_mock.called
    assert not single_mock.called
    assert out["tcData"] == tcs
    assert out["cost"] == 0.002


def test_generate_empty_rows_raises():
    with pytest.raises(ToolError) as info:
        generate_tc_tool(rows=[], context=_CONTEXT, rules_text="RULES")
    assert info.value.code == "bad_request"


def test_generate_wraps_generation_error():
    from generator import GenerationError

    with patch("backend.tools.generate.generate_single_tc", side_effect=GenerationError("API down")):
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
        tc_data=_fake_tc(),
        input_tokens=1, output_tokens=1, cache_creation_tokens=0,
        cache_read_tokens=0, cost=0.0, model="",
    )
    ctx = {"project": "p", "test_group": "g", "test_set": "OriginalSet"}
    with patch("backend.tools.generate.generate_single_tc", return_value=fake_result):
        generate_tc_tool(rows=[_BASE_ROW], context=ctx, rules_text="RULES")

    # caller's context 應未被改動
    assert ctx["test_set"] == "OriginalSet"


def test_estimate_batch_cost_positive():
    cost = estimate_batch_cost(row_count=10, model="gpt-4.1-mini")
    assert cost > 0


def test_generate_tool_registered():
    spec = get_tool("generate_tc")
    assert spec.safety is SafetyLevel.WRITE_COSTLY
