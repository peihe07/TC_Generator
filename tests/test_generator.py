"""Tests for generator module.

OpenAI calls are mocked to avoid actual API usage in tests.
"""
import json
from unittest.mock import MagicMock, patch

import pytest

from generator import (
    DecomposeResult,
    GenerationError,
    GenerationResult,
    calculate_cost,
    decompose_requirement,
    generate_batch,
    generate_quick_tc,
    generate_single_tc,
    parse_batch_response,
    parse_tc_response,
)


VALID_TC_JSON = {
    "test_item_rewrite": "(User adds DM to status bar → DM icon displayed)",
    "pre_conditions": "1. HU is in normal mode",
    "input_test_data": "Status bar customization menu",
    "test_procedure": "1. Open status bar settings to access customization.\n2. Add Device Manager and verify icon appears in status bar.",
    "expected_result": "1. Status bar customization screen is displayed.\n2. Device Manager icon is displayed in the status bar.",
    "design_method": "功能測試 (Functional based ; no specific technique)",
    "priority": "Medium",
    "split_flag": False,
    "split_reason": "",
}


def make_chat_response(payload, *, prompt_tokens=0, completion_tokens=0, cached_tokens=0):
    response = MagicMock()
    response.choices = [MagicMock(message=MagicMock(content=json.dumps(payload)))]
    response.usage = MagicMock(
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        prompt_tokens_details=MagicMock(cached_tokens=cached_tokens),
    )
    return response


class TestParseTcResponse:
    def test_valid_json(self):
        result = parse_tc_response(json.dumps(VALID_TC_JSON))
        assert result["test_item_rewrite"] == VALID_TC_JSON["test_item_rewrite"]
        assert result["priority"] == "Medium"

    def test_json_in_markdown_fence(self):
        raw = f"```json\n{json.dumps(VALID_TC_JSON)}\n```"
        result = parse_tc_response(raw)
        assert result["priority"] == "Medium"

    def test_invalid_json(self):
        with pytest.raises(GenerationError, match="parse"):
            parse_tc_response("not json")

    def test_missing_required_key(self):
        incomplete = {"test_item_rewrite": "something"}
        with pytest.raises(GenerationError, match="missing"):
            parse_tc_response(json.dumps(incomplete))


class TestParseBatchResponse:
    def test_valid_array(self):
        batch = [VALID_TC_JSON, VALID_TC_JSON]
        results = parse_batch_response(json.dumps(batch))
        assert len(results) == 2

    def test_array_in_fence(self):
        batch = [VALID_TC_JSON]
        raw = f"```json\n{json.dumps(batch)}\n```"
        results = parse_batch_response(raw)
        assert len(results) == 1

    def test_not_array(self):
        with pytest.raises(GenerationError, match="array"):
            parse_batch_response(json.dumps(VALID_TC_JSON))

    def test_invalid_json(self):
        with pytest.raises(GenerationError):
            parse_batch_response("broken")

    def test_count_mismatch_raises(self):
        batch = [VALID_TC_JSON]
        with pytest.raises(GenerationError, match="count mismatch"):
            parse_batch_response(json.dumps(batch), expected_count=2)


class TestCalculateCost:
    def test_gpt41_cost(self):
        cost = calculate_cost(
            input_tokens=1000,
            output_tokens=500,
            model="gpt-4.1",
        )
        expected = (1000 / 1_000_000 * 2.0) + (500 / 1_000_000 * 8.0)
        assert abs(cost - expected) < 0.0001

    def test_gpt41mini_cost(self):
        cost = calculate_cost(
            input_tokens=1000,
            output_tokens=500,
            model="gpt-4.1-mini",
        )
        expected = (1000 / 1_000_000 * 0.40) + (500 / 1_000_000 * 1.60)
        assert abs(cost - expected) < 0.0001

    def test_zero_tokens(self):
        assert calculate_cost(0, 0, "gpt-4.1") == 0.0

    def test_cached_tokens_discount(self):
        cost = calculate_cost(
            input_tokens=1000,
            output_tokens=0,
            model="gpt-4.1",
            cache_read_tokens=400,
        )
        expected = ((600 / 1_000_000) * 2.0) + ((400 / 1_000_000) * 2.0 * 0.5)
        assert abs(cost - expected) < 0.0001


class TestGenerateSingleTc:
    @patch("generator._chat")
    def test_success(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            VALID_TC_JSON,
            prompt_tokens=500,
            completion_tokens=300,
        )

        result = generate_single_tc(
            row={"req_id": "R001", "test_item": "PDM01 test"},
            context={"project": "p", "test_group": "G", "test_set": "S"},
            spec_index={},
            rules_text="rules",
            model="gpt-4.1",
        )
        assert isinstance(result, GenerationResult)
        assert result.tc_data["priority"] == "Medium"
        assert result.input_tokens == 500
        assert result.output_tokens == 300

    @patch("generator._chat")
    def test_api_error_raises(self, mock_chat):
        mock_chat.side_effect = GenerationError("API call failed: API timeout")

        with pytest.raises(GenerationError, match="API"):
            generate_single_tc(
                row={"req_id": "R001", "test_item": "test"},
                context={"project": "p", "test_group": "G", "test_set": "S"},
                spec_index={},
                rules_text="rules",
            )


class TestGenerateBatch:
    @patch("generator._chat")
    def test_batch_success(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            {"tcs": [VALID_TC_JSON, VALID_TC_JSON]},
            prompt_tokens=1000,
            completion_tokens=800,
        )

        rows = [
            {"req_id": "R001", "test_item": "PDM01 test A"},
            {"req_id": "R002", "test_item": "PDM02 test B"},
        ]
        result = generate_batch(
            rows=rows,
            context={"project": "p", "test_group": "G", "test_set": "S"},
            spec_index={},
            rules_text="rules",
        )
        assert isinstance(result, GenerationResult)
        assert len(result.tc_data) == 2
        assert result.input_tokens == 1000


class TestGenerateQuickTc:
    @patch("generator._chat")
    def test_single_success(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            VALID_TC_JSON,
            prompt_tokens=400,
            completion_tokens=200,
        )

        result = generate_quick_tc(
            test_item="Button pressed → LED turns on",
            context=None,
            rules_text="rules",
        )
        assert isinstance(result, GenerationResult)
        assert result.tc_data["priority"] == "Medium"
        assert result.input_tokens == 400
        assert result.output_tokens == 200

    @patch("generator._chat")
    def test_with_context_passes_context_to_prompt(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            VALID_TC_JSON,
            prompt_tokens=600,
            completion_tokens=300,
        )

        result = generate_quick_tc(
            test_item="Button pressed → LED turns on",
            context="System must be powered on",
            rules_text="rules",
        )
        assert "System must be powered on" in mock_chat.call_args.args[1]
        assert isinstance(result, GenerationResult)

    @patch("generator._chat")
    def test_api_error_raises(self, mock_chat):
        mock_chat.side_effect = GenerationError("API call failed: timeout")

        with pytest.raises(GenerationError, match="API"):
            generate_quick_tc(
                test_item="some test item",
                context=None,
                rules_text="rules",
            )

    @patch("generator._chat")
    def test_invalid_json_response_raises(self, mock_chat):
        response = MagicMock()
        response.choices = [MagicMock(message=MagicMock(content="not json at all"))]
        response.usage = MagicMock(
            prompt_tokens=100,
            completion_tokens=50,
            prompt_tokens_details=MagicMock(cached_tokens=0),
        )
        mock_chat.return_value = response

        with pytest.raises(GenerationError, match="parse"):
            generate_quick_tc(
                test_item="some test item",
                context=None,
                rules_text="rules",
            )


class TestDecomposeRequirement:
    VALID_DECOMPOSE_RESPONSE = {
        "reasoning": "The requirement has 3 distinct paths: normal, boundary, and error.",
        "keywords": [
            {"keyword": "button", "meaning": "The physical input trigger.", "scenarios": [1, 2]},
            {"keyword": "LED", "meaning": "The observable output indicator.", "scenarios": [1, 2]},
        ],
        "scenarios": [
            {"id": 1, "name": "Normal flow", "description": "Primary success path.", "test_item": "Button → LED on"},
            {"id": 2, "name": "Boundary", "description": "Edge case input.", "test_item": "Button held → LED blink"},
        ],
    }

    @patch("generator._chat")
    def test_success(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            self.VALID_DECOMPOSE_RESPONSE,
            prompt_tokens=700,
            completion_tokens=400,
        )

        result = decompose_requirement(
            requirement="When button is pressed, LED turns on. Boundary and error cases apply.",
            rules_text="rules",
        )
        assert isinstance(result, DecomposeResult)
        assert result.reasoning == self.VALID_DECOMPOSE_RESPONSE["reasoning"]
        assert len(result.scenarios) == 2
        assert result.scenarios[0]["name"] == "Normal flow"
        assert len(result.keywords) == 2
        assert result.keywords[0]["keyword"] == "button"
        assert result.input_tokens == 700
        assert result.output_tokens == 400

    @patch("generator._chat")
    def test_success_with_fenced_json(self, mock_chat):
        raw = f"```json\n{json.dumps(self.VALID_DECOMPOSE_RESPONSE)}\n```"
        response = MagicMock()
        response.choices = [MagicMock(message=MagicMock(content=raw))]
        response.usage = MagicMock(
            prompt_tokens=700,
            completion_tokens=400,
            prompt_tokens_details=MagicMock(cached_tokens=0),
        )
        mock_chat.return_value = response

        result = decompose_requirement(requirement="req", rules_text="rules")
        assert len(result.scenarios) == 2

    @patch("generator._chat")
    def test_api_error_raises(self, mock_chat):
        mock_chat.side_effect = GenerationError("API call failed: network error")

        with pytest.raises(GenerationError, match="API"):
            decompose_requirement(requirement="req", rules_text="rules")

    @patch("generator._chat")
    def test_invalid_json_raises(self, mock_chat):
        response = MagicMock()
        response.choices = [MagicMock(message=MagicMock(content="definitely not json"))]
        response.usage = MagicMock(
            prompt_tokens=100,
            completion_tokens=50,
            prompt_tokens_details=MagicMock(cached_tokens=0),
        )
        mock_chat.return_value = response

        with pytest.raises(GenerationError, match="parse"):
            decompose_requirement(requirement="req", rules_text="rules")

    @patch("generator._chat")
    def test_missing_scenarios_key_raises(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            {"reasoning": "ok"},
            prompt_tokens=100,
            completion_tokens=50,
        )

        with pytest.raises(GenerationError, match="scenarios"):
            decompose_requirement(requirement="req", rules_text="rules")

    @patch("generator._chat")
    def test_cost_calculation(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            self.VALID_DECOMPOSE_RESPONSE,
            prompt_tokens=1_000_000,
            completion_tokens=1_000_000,
        )

        result = decompose_requirement(requirement="req", rules_text="rules", model="gpt-4.1")
        assert abs(result.cost - 10.0) < 0.001
