"""Tests for the narrow Review-fix-suggestion endpoint and module."""
from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    from api_server import app

    return TestClient(app)


def _fake_chat_response(content: str, in_tokens: int = 100, out_tokens: int = 60):
    """`_chat` 現在回傳正規化的 LLMResponse。"""
    from providers import LLMResponse, LLMUsage
    return LLMResponse(
        text=content,
        usage=LLMUsage(input_tokens=in_tokens, output_tokens=out_tokens),
        model="gpt-5",
    )


class TestSuggestReviewFix:
    def test_returns_structured_fix_proposal(self, client):
        body = (
            '{"problem_root_cause": "tc_title 為裸動作，違反 §6.1 sibling-distinction 規則。", '
            '"affected_fields": ["tc_title", "pre_conditions"], '
            '"proposed_change": "tc_title 補上 with iPhone via USB；pre_conditions 加 BT pairing 完成。", '
            '"suggested_reason": "Add precondition to tc_title trigger."}'
        )
        with patch("review_assistant._chat", return_value=_fake_chat_response(body)):
            response = client.post(
                "/api/review/suggest-fix",
                json={
                    "tc": {
                        "tc_id": "TC-001",
                        "tc_title": "Select X",
                        "test_procedure": "1. Select X.",
                        "expected_result": "1. X displayed.",
                    },
                    "errors": [
                        {
                            "severity": "error",
                            "field": "tc_title",
                            "message": "Trigger missing precondition.",
                        }
                    ],
                },
            )

        assert response.status_code == 200
        payload = response.json()
        assert "tc_title" in payload["problemRootCause"]
        assert payload["affectedFields"] == ["tc_title", "pre_conditions"]
        assert "tc_title 補上" in payload["proposedChange"]
        assert payload["suggestedReason"].startswith("Add precondition")
        assert "model" in payload
        assert payload["cost"] >= 0
        assert payload["usage"]["input"] == 100
        assert payload["usage"]["output"] == 60

    def test_unknown_field_keys_are_dropped_from_affected_fields(self, client):
        body = (
            '{"problem_root_cause": "x", '
            '"affected_fields": ["tc_title", "TC_TITLE", "bogus_key", ""], '
            '"proposed_change": "x", '
            '"suggested_reason": "x"}'
        )
        with patch("review_assistant._chat", return_value=_fake_chat_response(body)):
            response = client.post(
                "/api/review/suggest-fix",
                json={
                    "tc": {"tc_id": "TC-001"},
                    "errors": [
                        {"severity": "warning", "field": "tc_title", "message": "x"}
                    ],
                },
            )
        # tc_title kept (case-normalized); duplicates and unknown keys dropped.
        assert response.json()["affectedFields"] == ["tc_title"]

    def test_rejects_empty_errors(self, client):
        response = client.post(
            "/api/review/suggest-fix",
            json={"tc": {"tc_id": "TC-001"}, "errors": []},
        )
        assert response.status_code == 400
        assert "at least one" in response.json()["detail"]

    def test_handles_generation_error(self, client):
        from generator import GenerationError

        with patch(
            "review_assistant._chat",
            side_effect=GenerationError("OPENAI_API_KEY is not set."),
        ):
            response = client.post(
                "/api/review/suggest-fix",
                json={
                    "tc": {"tc_id": "TC-001"},
                    "errors": [
                        {"severity": "warning", "field": "tc_title", "message": "x"}
                    ],
                },
            )
        assert response.status_code == 502
        assert "OPENAI_API_KEY" in response.json()["detail"]

    def test_handles_non_json_response(self, client):
        with patch(
            "review_assistant._chat",
            return_value=_fake_chat_response("not actually JSON"),
        ):
            response = client.post(
                "/api/review/suggest-fix",
                json={
                    "tc": {"tc_id": "TC-001"},
                    "errors": [
                        {"severity": "warning", "field": "tc_title", "message": "x"}
                    ],
                },
            )
        assert response.status_code == 502
        assert "non-JSON" in response.json()["detail"]
