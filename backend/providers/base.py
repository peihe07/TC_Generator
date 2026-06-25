"""LLM provider abstraction (PIPELINE_DESIGN § Phase 0).

Serves the *programmatic* backends only (OpenAI API, Anthropic API) — i.e. the
headless path and the OpenAI->Claude migration. "Interactive" is NOT a provider:
interactive runs happen inside Claude Code driven by you and never go through
this layer (routing them through an API would re-introduce metered billing).
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class LLMUsage:
    input_tokens: int = 0
    output_tokens: int = 0
    cached_input_tokens: int = 0
    request_count: int = 1
    cost_usd: float | None = None   # None when not API-priced (subscription / interactive)


@dataclass
class LLMResponse:
    text: str
    usage: LLMUsage
    model: str
    stop_reason: str | None = None
    raw: Any = None                 # provider-native payload, for debugging only


class LLMProvider(ABC):
    name: str = "base"

    @abstractmethod
    def chat(
        self,
        messages: list[dict],
        model: str,
        *,
        max_tokens: int = 4096,
        temperature: float = 0.0,
        cache_prefix: str | None = None,   # stable prefix to mark for prompt caching
        timeout: float = 180.0,
        **kwargs: Any,
    ) -> LLMResponse:
        ...
