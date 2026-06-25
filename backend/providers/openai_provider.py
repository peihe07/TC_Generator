"""OpenAI backend for the LLMProvider interface.

Moves the OpenAI client creation / call / retry / response normalization out of
`generator.py` so the LLM backend is pluggable. Behaviour mirrors the legacy
`generator._chat`: explicit timeout, SDK retries disabled (we own backoff),
JSON mode by default, `cached_tokens` read from `prompt_tokens_details`.
"""
from __future__ import annotations

import logging
import os
import random
import time
from importlib import import_module
from typing import Any

from .base import LLMProvider, LLMResponse, LLMUsage

logger = logging.getLogger(__name__)

_TRANSIENT_STATUS_CODES = {500, 502, 503, 504, 529}
_RETRY_MAX_ATTEMPTS = 3
_RETRY_BASE_DELAY = 1.0


class OpenAIProvider(LLMProvider):
    name = "openai"

    def __init__(self, api_key: str | None = None, client: Any = None,
                 timeout: float = 180.0):
        self._api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self._client = client          # allow injection (tests / reuse)
        self._timeout = timeout

    def _get_client(self) -> Any:
        if self._client is not None:
            return self._client
        if not self._api_key:
            raise RuntimeError("OPENAI_API_KEY is not set. Add it to .env.")
        openai_module = import_module("openai")
        self._client = openai_module.OpenAI(
            api_key=self._api_key, timeout=self._timeout, max_retries=0,
        )
        return self._client

    def chat(
        self,
        messages: list[dict],
        model: str,
        *,
        max_tokens: int = 4096,
        temperature: float = 0.0,
        cache_prefix: str | None = None,
        timeout: float = 180.0,
        json_mode: bool = True,
        **kwargs: Any,
    ) -> LLMResponse:
        client = self._get_client()
        call_kwargs: dict = {"model": model, "messages": messages}
        if max_tokens is not None:
            call_kwargs["max_completion_tokens"] = max_tokens
        if json_mode:
            call_kwargs["response_format"] = {"type": "json_object"}
        # NB: temperature intentionally not forwarded — gpt-5 family only accepts
        # the default; matches legacy `_chat` behaviour. `cache_prefix` relies on
        # OpenAI's automatic >=1024-token prefix cache, so nothing to send.

        raw = self._call_with_retry(client, call_kwargs)
        return self._normalize(raw, model)

    def _call_with_retry(self, client: Any, call_kwargs: dict) -> Any:
        openai_module = import_module("openai")
        transient = tuple(
            cls for name in ("APIConnectionError", "APITimeoutError", "RateLimitError")
            if (cls := getattr(openai_module, name, None)) is not None
        )
        status_error_cls = getattr(openai_module, "APIStatusError", None)
        last_exc: BaseException | None = None
        for attempt in range(_RETRY_MAX_ATTEMPTS):
            try:
                return client.chat.completions.create(**call_kwargs)
            except Exception as e:  # noqa: BLE001 — re-raised below
                is_transient = isinstance(e, transient) or (
                    status_error_cls is not None
                    and isinstance(e, status_error_cls)
                    and getattr(e, "status_code", None) in _TRANSIENT_STATUS_CODES
                )
                last_exc = e
                if not is_transient or attempt == _RETRY_MAX_ATTEMPTS - 1:
                    break
                delay = _RETRY_BASE_DELAY * (2 ** attempt) + random.uniform(0, 0.5)
                logger.warning(
                    "OpenAI transient error (attempt %d/%d): %s — retry in %.1fs",
                    attempt + 1, _RETRY_MAX_ATTEMPTS, e, delay,
                )
                time.sleep(delay)
        raise RuntimeError(f"API call failed: {last_exc}") from last_exc

    @staticmethod
    def _normalize(raw: Any, model: str) -> LLMResponse:
        choice = raw.choices[0]
        text = choice.message.content or ""
        stop_reason = getattr(choice, "finish_reason", None)
        usage_obj = getattr(raw, "usage", None)
        input_tokens = getattr(usage_obj, "prompt_tokens", 0) or 0
        output_tokens = getattr(usage_obj, "completion_tokens", 0) or 0
        details = getattr(usage_obj, "prompt_tokens_details", None)
        cached = getattr(details, "cached_tokens", 0) or 0 if details else 0

        # Cost: single source of truth in generator.calculate_cost.
        from generator import calculate_cost
        cost = calculate_cost(input_tokens, output_tokens, model, cache_read_tokens=cached)

        return LLMResponse(
            text=text,
            usage=LLMUsage(
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                cached_input_tokens=cached,
                request_count=1,
                cost_usd=cost,
            ),
            model=model,
            stop_reason=stop_reason,
            raw=raw,
        )
