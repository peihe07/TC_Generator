"""Anthropic (Claude) backend for the LLMProvider interface.

Parses Messages-API responses: concatenate only `type == "text"` content blocks,
map usage (input/output/cache_read) to LLMUsage, price from ANTHROPIC_PRICING.

Env gotcha: when ANTHROPIC_API_KEY is set, Claude Code itself bills via the API.
This provider is for the *headless* path only and expects that key to exist.
"""
from __future__ import annotations

import logging
import os
from importlib import import_module
from typing import Any

from .base import LLMProvider, LLMResponse, LLMUsage

logger = logging.getLogger(__name__)

# USD per million tokens (2026-06). cached_input = 10% of input (cache read).
ANTHROPIC_PRICING = {
    "claude-opus-4-8":   {"input": 5.00, "cached_input": 0.50, "output": 25.00},
    "claude-sonnet-4-6": {"input": 3.00, "cached_input": 0.30, "output": 15.00},
    "claude-haiku-4-5":  {"input": 1.00, "cached_input": 0.10, "output": 5.00},
}


def _price(input_tokens: int, output_tokens: int, cached: int,
           model: str) -> float | None:
    pricing = ANTHROPIC_PRICING.get(model)
    if pricing is None:
        return None
    uncached = max(input_tokens - cached, 0)
    return (
        uncached * pricing["input"] / 1_000_000
        + cached * pricing["cached_input"] / 1_000_000
        + output_tokens * pricing["output"] / 1_000_000
    )


class AnthropicProvider(LLMProvider):
    name = "anthropic"

    def __init__(self, api_key: str | None = None, client: Any = None,
                 timeout: float = 180.0):
        self._api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self._client = client
        self._timeout = timeout

    def _get_client(self) -> Any:
        if self._client is not None:
            return self._client
        if not self._api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set. Add it to .env.")
        anthropic_module = import_module("anthropic")
        self._client = anthropic_module.Anthropic(
            api_key=self._api_key, timeout=self._timeout,
        )
        return self._client

    @staticmethod
    def _split_system(messages: list[dict]) -> tuple[str, list[dict]]:
        """Anthropic takes `system` separately from the message list."""
        system_parts = [m["content"] for m in messages if m.get("role") == "system"]
        convo = [m for m in messages if m.get("role") != "system"]
        return "\n\n".join(system_parts), convo

    def chat(
        self,
        messages: list[dict],
        model: str,
        *,
        max_tokens: int = 4096,
        temperature: float = 0.0,
        cache_prefix: str | None = None,
        timeout: float = 180.0,
        **kwargs: Any,
    ) -> LLMResponse:
        client = self._get_client()
        system_text, convo = self._split_system(messages)

        call_kwargs: dict = {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": convo,
        }
        if system_text:
            if cache_prefix:
                # Mark the stable system prefix for prompt caching.
                call_kwargs["system"] = [{
                    "type": "text",
                    "text": system_text,
                    "cache_control": {"type": "ephemeral"},
                }]
            else:
                call_kwargs["system"] = system_text

        raw = client.messages.create(**call_kwargs)
        return self._normalize(raw, model)

    @staticmethod
    def _normalize(raw: Any, model: str) -> LLMResponse:
        text = "".join(
            getattr(block, "text", "")
            for block in getattr(raw, "content", [])
            if getattr(block, "type", None) == "text"
        )
        usage_obj = getattr(raw, "usage", None)
        input_tokens = getattr(usage_obj, "input_tokens", 0) or 0
        output_tokens = getattr(usage_obj, "output_tokens", 0) or 0
        cached = getattr(usage_obj, "cache_read_input_tokens", 0) or 0

        return LLMResponse(
            text=text,
            usage=LLMUsage(
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                cached_input_tokens=cached,
                request_count=1,
                cost_usd=_price(input_tokens, output_tokens, cached, model),
            ),
            model=model,
            stop_reason=getattr(raw, "stop_reason", None),
            raw=raw,
        )
