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
    """模擬 OpenAI Chat Completions 回應結構。"""
    message = SimpleNamespace(content=content)
    choice = SimpleNamespace(message=message)
    usage = SimpleNamespace(
        prompt_tokens=in_tokens,
        completion_tokens=out_tokens,
        prompt_tokens_details=SimpleNamespace(cached_tokens=0),
    )
    return SimpleNamespace(choices=[choice], usage=usage)


class TestSuggestReviewFix:
    def test_returns_suggestion_and_reason(self, client):
        body = (
            '{"suggestion": "tc_title 缺少觸發條件，請補上前置狀態。", '
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
        assert "tc_title" in payload["suggestion"]
        assert payload["suggestedReason"].startswith("Add precondition")
        assert "model" in payload
        assert payload["cost"] >= 0
        assert payload["usage"]["input"] == 100
        assert payload["usage"]["output"] == 60

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
