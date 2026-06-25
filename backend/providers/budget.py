"""Budget gate for the provider layer (PIPELINE_DESIGN § Phase 0).

`limit_usd=None` means unlimited — the subscription / interactive case where
usage carries no per-token cost. `charge()` is a no-op when `usage.cost_usd is
None`, so subscription runs never trip the gate.

This is distinct from `backend/tools/_budget.py` (`needs_confirmation`), which is
the legacy per-call confirmation helper and is left untouched.
"""
from __future__ import annotations

from .base import LLMUsage


class Budget:
    def __init__(self, limit_usd: float | None):
        self.limit_usd = limit_usd
        self.spent_usd = 0.0
        self.request_count = 0

    def charge(self, usage: LLMUsage) -> None:
        """Accumulate spend. No-op when the usage has no priced cost."""
        self.request_count += usage.request_count
        if usage.cost_usd is None:
            return
        self.spent_usd += usage.cost_usd

    def remaining(self) -> float | None:
        """Remaining USD, or None when unlimited (subscription)."""
        if self.limit_usd is None:
            return None
        return self.limit_usd - self.spent_usd

    def exceeded(self) -> bool:
        """True only when a finite limit has been overspent."""
        return self.limit_usd is not None and self.spent_usd > self.limit_usd
