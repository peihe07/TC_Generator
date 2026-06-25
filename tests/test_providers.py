"""Phase 0 — provider abstraction tests. SDKs are mocked; no real API calls."""
from types import SimpleNamespace

import pytest

import generator
from providers import Budget, LLMResponse, LLMUsage, make_provider
from providers.anthropic_provider import AnthropicProvider
from providers.openai_provider import OpenAIProvider


def test_make_provider_known():
    assert isinstance(make_provider("openai", api_key="x"), OpenAIProvider)
    assert isinstance(make_provider("anthropic", api_key="x"), AnthropicProvider)
    # Case / whitespace tolerant.
    assert isinstance(make_provider("  OpenAI ", api_key="x"), OpenAIProvider)


def test_make_provider_unknown_raises():
    with pytest.raises(ValueError, match="Unknown LLM backend"):
        make_provider("gemini")


def _fake_openai_client(content, *, prompt=10, completion=4, cached=2):
    raw = SimpleNamespace(
        choices=[SimpleNamespace(
            message=SimpleNamespace(content=content), finish_reason="stop")],
        usage=SimpleNamespace(
            prompt_tokens=prompt, completion_tokens=completion,
            prompt_tokens_details=SimpleNamespace(cached_tokens=cached)),
    )
    create = lambda **kw: raw  # noqa: E731
    return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))


def test_openai_provider_normalizes_response():
    client = _fake_openai_client('{"ok": true}')
    provider = make_provider("openai", client=client)
    resp = provider.chat([{"role": "user", "content": "hi"}], "gpt-5")
    assert isinstance(resp, LLMResponse)
    assert resp.text == '{"ok": true}'
    assert resp.usage.input_tokens == 10
    assert resp.usage.output_tokens == 4
    assert resp.usage.cached_input_tokens == 2
    assert resp.usage.cost_usd is not None and resp.usage.cost_usd > 0
    assert resp.stop_reason == "stop"


def test_anthropic_provider_parses_text_blocks():
    raw = SimpleNamespace(
        content=[
            SimpleNamespace(type="text", text="Hello "),
            SimpleNamespace(type="tool_use", text="IGNORED"),
            SimpleNamespace(type="text", text="world"),
        ],
        usage=SimpleNamespace(
            input_tokens=100, output_tokens=20, cache_read_input_tokens=40),
        stop_reason="end_turn",
    )
    client = SimpleNamespace(messages=SimpleNamespace(create=lambda **kw: raw))
    provider = make_provider("anthropic", client=client)
    resp = provider.chat(
        [{"role": "system", "content": "S"}, {"role": "user", "content": "U"}],
        "claude-sonnet-4-6",
        cache_prefix="S",
    )
    assert resp.text == "Hello world"  # tool_use block excluded
    assert resp.usage.input_tokens == 100
    assert resp.usage.cached_input_tokens == 40
    assert resp.usage.cost_usd is not None and resp.usage.cost_usd > 0


def test_usage_cost_none_in_subscription():
    budget = Budget(limit_usd=None)
    budget.charge(LLMUsage(input_tokens=1000, output_tokens=500, cost_usd=None))
    assert budget.spent_usd == 0.0          # no-op on unpriced usage
    assert budget.remaining() is None        # unlimited
    assert budget.exceeded() is False
    # A finite budget does accumulate priced usage and can be exceeded.
    finite = Budget(limit_usd=1.0)
    finite.charge(LLMUsage(cost_usd=1.5))
    assert finite.exceeded() is True
    assert finite.remaining() == pytest.approx(-0.5)


def test_generator_delegates_to_provider():
    calls = {}

    class FakeProvider:
        def chat(self, messages, model, **kwargs):
            calls["messages"] = messages
            calls["model"] = model
            calls["cache_prefix"] = kwargs.get("cache_prefix")
            return LLMResponse(
                text='{"delegated": true}',
                usage=LLMUsage(input_tokens=5, output_tokens=3, cost_usd=0.0),
                model=model,
            )

    generator.set_provider(FakeProvider())
    try:
        resp = generator._chat("SYS", "USER", "gpt-5", max_tokens=100)
        # `_chat` now returns the provider's LLMResponse directly.
        assert resp.text == '{"delegated": true}'
        assert resp.usage.input_tokens == 5
        assert calls["model"] == "gpt-5"
        assert calls["cache_prefix"] == "SYS"
        assert calls["messages"][0]["role"] == "system"
    finally:
        generator.set_provider(None)  # restore default provider for other tests


# --- OpenAIProvider client config + retry (ported from test_generator) ----------

import openai as openai_module  # noqa: E402
from unittest.mock import MagicMock, patch  # noqa: E402


def _status_error(code):
    return openai_module.APIStatusError(
        "boom", response=MagicMock(status_code=code), body=None)


def _success_raw():
    return SimpleNamespace(
        choices=[SimpleNamespace(
            message=SimpleNamespace(content='{"ok": true}'), finish_reason="stop")],
        usage=SimpleNamespace(
            prompt_tokens=1, completion_tokens=1,
            prompt_tokens_details=SimpleNamespace(cached_tokens=0)),
    )


@patch("providers.openai_provider.import_module")
def test_openai_provider_client_config(mock_import_module):
    fake_module = MagicMock()
    mock_import_module.return_value = fake_module
    provider = OpenAIProvider(api_key="test-key", timeout=240.0)
    provider._get_client()
    fake_module.OpenAI.assert_called_once()
    kwargs = fake_module.OpenAI.call_args.kwargs
    assert kwargs.get("timeout") == 240.0
    assert kwargs.get("max_retries") == 0


@patch("providers.openai_provider.time.sleep", return_value=None)
def test_openai_provider_retries_on_transient(_sleep):
    create = MagicMock(side_effect=[_status_error(502), _success_raw()])
    client = SimpleNamespace(
        chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    provider = OpenAIProvider(client=client)
    resp = provider.chat([{"role": "user", "content": "x"}], "gpt-5-mini")
    assert resp.text == '{"ok": true}'
    assert create.call_count == 2


@patch("providers.openai_provider.time.sleep", return_value=None)
def test_openai_provider_does_not_retry_on_400(_sleep):
    create = MagicMock(side_effect=_status_error(400))
    client = SimpleNamespace(
        chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    provider = OpenAIProvider(client=client)
    with pytest.raises(RuntimeError, match="API call failed"):
        provider.chat([{"role": "user", "content": "x"}], "gpt-5-mini")
    assert create.call_count == 1


@patch("providers.openai_provider.time.sleep", return_value=None)
def test_openai_provider_gives_up_after_max_attempts(_sleep):
    from providers.openai_provider import _RETRY_MAX_ATTEMPTS
    create = MagicMock(side_effect=_status_error(502))
    client = SimpleNamespace(
        chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    provider = OpenAIProvider(client=client)
    with pytest.raises(RuntimeError, match="API call failed"):
        provider.chat([{"role": "user", "content": "x"}], "gpt-5-mini")
    assert create.call_count == _RETRY_MAX_ATTEMPTS
