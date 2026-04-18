"""Budget gate helper。

Phase 1 會被 Agent dispatcher 呼叫，決定某個 tool call 是否需要先向使用者
取得確認。Phase 0 先留空殼，避免後續再改 API。
"""

from __future__ import annotations

import os

# 預設門檻 $0.50，可用環境變數覆寫
DEFAULT_BUDGET_THRESHOLD_USD = float(
    os.environ.get("TC_AGENT_BUDGET_THRESHOLD_USD", "0.5")
)


def needs_confirmation(estimated_cost_usd: float, *, threshold: float | None = None) -> bool:
    """判斷某個估算成本是否超過門檻、需要使用者確認。"""
    limit = threshold if threshold is not None else DEFAULT_BUDGET_THRESHOLD_USD
    return estimated_cost_usd > limit
