"""Tests for generator module (RULES.md §12).

AI calls are mocked to avoid actual API usage in tests.
"""
import json
import pytest
from unittest.mock import MagicMock, patch

from generator import (
    parse_tc_response,
    parse_batch_response,
    calculate_cost,
    GenerationResult,
    DecomposeResult,
    GenerationError,
    generate_single_tc,
    generate_batch,
    generate_quick_tc,
    decompose_requirement,
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
    def test_sonnet_cost(self):
        cost = calculate_cost(
            input_tokens=1000,
            output_tokens=500,
            model="claude-sonnet-4-6",
        )
        # Sonnet: $3/MTok input, $15/MTok output
        expected = (1000 / 1_000_000 * 3.0) + (500 / 1_000_000 * 15.0)
        assert abs(cost - expected) < 0.0001

    def test_haiku_cost(self):
        cost = calculate_cost(
            input_tokens=1000,
            output_tokens=500,
            model="claude-haiku-4-5-20251001",
        )
        # Haiku: $0.80/MTok input, $4/MTok output
        expected = (1000 / 1_000_000 * 0.80) + (500 / 1_000_000 * 4.0)
        assert abs(cost - expected) < 0.0001

    def test_zero_tokens(self):
        assert calculate_cost(0, 0, "claude-sonnet-4-6") == 0.0


class TestGenerateSingleTc:
    @patch("generator.anthropic")
    def test_success(self, mock_anthropic):
        # Mock API response
        mock_msg = MagicMock()
        mock_msg.content = [MagicMock(text=json.dumps(VALID_TC_JSON))]
        mock_msg.usage.input_tokens = 500
        mock_msg.usage.output_tokens = 300
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        result = generate_single_tc(
            row={"req_id": "R001", "test_item": "PDM01 test"},
            context={"project": "p", "test_group": "G", "test_set": "S"},
            spec_index={},
            rules_text="rules",
            model="claude-sonnet-4-6",
        )
        assert isinstance(result, GenerationResult)
        assert result.tc_data["priority"] == "Medium"
        assert result.input_tokens == 500
        assert result.output_tokens == 300

    @patch("generator.anthropic")
    def test_api_error_raises(self, mock_anthropic):
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = Exception("API timeout")
        mock_anthropic.Anthropic.return_value = mock_client

        with pytest.raises(GenerationError, match="API"):
            generate_single_tc(
                row={"req_id": "R001", "test_item": "test"},
                context={"project": "p", "test_group": "G", "test_set": "S"},
                spec_index={},
                rules_text="rules",
            )


class TestGenerateBatch:
    @patch("generator.anthropic")
    def test_batch_success(self, mock_anthropic):
        batch_response = [VALID_TC_JSON, VALID_TC_JSON]
        mock_msg = MagicMock()
        mock_msg.content = [MagicMock(text=json.dumps(batch_response))]
        mock_msg.usage.input_tokens = 1000
        mock_msg.usage.output_tokens = 800
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

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
    @patch("generator.anthropic")
    def test_single_success(self, mock_anthropic):
        mock_msg = MagicMock()
        mock_msg.content = [MagicMock(text=json.dumps(VALID_TC_JSON))]
        mock_msg.usage.input_tokens = 400
        mock_msg.usage.output_tokens = 200
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        result = generate_quick_tc(
            test_item="Button pressed → LED turns on",
            context=None,
            rules_text="rules",
        )
        assert isinstance(result, GenerationResult)
        assert result.tc_data["priority"] == "Medium"
        assert result.input_tokens == 400
        assert result.output_tokens == 200

    @patch("generator.anthropic")
    def test_with_context_passes_context_to_prompt(self, mock_anthropic):
        mock_msg = MagicMock()
        mock_msg.content = [MagicMock(text=json.dumps(VALID_TC_JSON))]
        mock_msg.usage.input_tokens = 600
        mock_msg.usage.output_tokens = 300
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        result = generate_quick_tc(
            test_item="Button pressed → LED turns on",
            context="System must be powered on",
            rules_text="rules",
        )
        # Verify the prompt that was built contains the context
        call_kwargs = mock_client.messages.create.call_args[1]
        assert "System must be powered on" in call_kwargs["messages"][0]["content"]
        assert isinstance(result, GenerationResult)

    @patch("generator.anthropic")
    def test_api_error_raises(self, mock_anthropic):
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = Exception("timeout")
        mock_anthropic.Anthropic.return_value = mock_client

        with pytest.raises(GenerationError, match="API"):
            generate_quick_tc(
                test_item="some test item",
                context=None,
                rules_text="rules",
            )

    @patch("generator.anthropic")
    def test_invalid_json_response_raises(self, mock_anthropic):
        mock_msg = MagicMock()
        mock_msg.content = [MagicMock(text="not json at all")]
        mock_msg.usage.input_tokens = 100
        mock_msg.usage.output_tokens = 50
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        with pytest.raises(GenerationError, match="parse"):
            generate_quick_tc(
                test_item="some test item",
                context=None,
                rules_text="rules",
            )


class TestDecomposeRequirement:
    VALID_DECOMPOSE_RESPONSE = {
        "reasoning": "The requirement has 3 distinct paths: normal, boundary, and error.",
        "scenarios": [
            {"id": 1, "name": "Normal flow", "description": "Primary success path.", "test_item": "Button → LED on"},
            {"id": 2, "name": "Boundary", "description": "Edge case input.", "test_item": "Button held → LED blink"},
        ],
    }

    @patch("generator.anthropic")
    def test_success(self, mock_anthropic):
        mock_msg = MagicMock()
        mock_msg.content = [MagicMock(text=json.dumps(self.VALID_DECOMPOSE_RESPONSE))]
        mock_msg.usage.input_tokens = 700
        mock_msg.usage.output_tokens = 400
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        result = decompose_requirement(
            requirement="When button is pressed, LED turns on. Boundary and error cases apply.",
            rules_text="rules",
        )
        assert isinstance(result, DecomposeResult)
        assert result.reasoning == self.VALID_DECOMPOSE_RESPONSE["reasoning"]
        assert len(result.scenarios) == 2
        assert result.scenarios[0]["name"] == "Normal flow"
        assert result.input_tokens == 700
        assert result.output_tokens == 400

    @patch("generator.anthropic")
    def test_success_with_fenced_json(self, mock_anthropic):
        raw = f"```json\n{json.dumps(self.VALID_DECOMPOSE_RESPONSE)}\n```"
        mock_msg = MagicMock()
        mock_msg.content = [MagicMock(text=raw)]
        mock_msg.usage.input_tokens = 700
        mock_msg.usage.output_tokens = 400
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        result = decompose_requirement(requirement="req", rules_text="rules")
        assert len(result.scenarios) == 2

    @patch("generator.anthropic")
    def test_api_error_raises(self, mock_anthropic):
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = Exception("network error")
        mock_anthropic.Anthropic.return_value = mock_client

        with pytest.raises(GenerationError, match="API"):
            decompose_requirement(requirement="req", rules_text="rules")

    @patch("generator.anthropic")
    def test_invalid_json_raises(self, mock_anthropic):
        mock_msg = MagicMock()
        mock_msg.content = [MagicMock(text="definitely not json")]
        mock_msg.usage.input_tokens = 100
        mock_msg.usage.output_tokens = 50
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        with pytest.raises(GenerationError, match="parse"):
            decompose_requirement(requirement="req", rules_text="rules")

    @patch("generator.anthropic")
    def test_missing_scenarios_key_raises(self, mock_anthropic):
        mock_msg = MagicMock()
        mock_msg.content = [MagicMock(text=json.dumps({"reasoning": "ok"}))]
        mock_msg.usage.input_tokens = 100
        mock_msg.usage.output_tokens = 50
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        with pytest.raises(GenerationError, match="scenarios"):
            decompose_requirement(requirement="req", rules_text="rules")

    @patch("generator.anthropic")
    def test_cost_calculation(self, mock_anthropic):
        mock_msg = MagicMock()
        mock_msg.content = [MagicMock(text=json.dumps(self.VALID_DECOMPOSE_RESPONSE))]
        mock_msg.usage.input_tokens = 1_000_000
        mock_msg.usage.output_tokens = 1_000_000
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        result = decompose_requirement(requirement="req", rules_text="rules", model="claude-sonnet-4-6")
        # Sonnet: $3 input + $15 output = $18 total for 1M each
        assert abs(result.cost - 18.0) < 0.001
