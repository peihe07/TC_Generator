"""Provider factory + public surface for the LLM backend abstraction."""
from __future__ import annotations

from typing import Any

from .base import LLMProvider, LLMResponse, LLMUsage
from .budget import Budget

__all__ = [
    "LLMProvider",
    "LLMResponse",
    "LLMUsage",
    "Budget",
    "make_provider",
]


def make_provider(backend: str, **cfg: Any) -> LLMProvider:
    """Build a provider by name.

    backend: 'openai' | 'anthropic'. Raises ValueError on unknown backend.
    Extra kwargs (api_key, client, timeout) are passed to the provider.
    """
    key = (backend or "").strip().lower()
    if key == "openai":
        from .openai_provider import OpenAIProvider
        return OpenAIProvider(**cfg)
    if key == "anthropic":
        from .anthropic_provider import AnthropicProvider
        return AnthropicProvider(**cfg)
    raise ValueError(f"Unknown LLM backend: {backend!r}. Use 'openai' or 'anthropic'.")
