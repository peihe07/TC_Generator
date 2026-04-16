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
    GenerationError,
    generate_single_tc,
    generate_batch,
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
