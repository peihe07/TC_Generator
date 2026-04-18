"""Tool 註冊表。

Phase 0 的目標是建立骨架；後續 Phase 1 會把每個 tool 的 JSON schema
補進來，讓 Agent dispatcher 能用 `list_tools()` 產生 OpenAI function
calling 的 tools 參數。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable


class SafetyLevel(str, Enum):
    """Tool 的安全分級，決定 Agent 是否需要使用者確認。"""

    READ_ONLY = "read_only"          # 只讀，Agent 可自由使用
    WRITE_SAFE = "write_safe"        # 有寫入但無成本（e.g. parse / validate）
    WRITE_COSTLY = "write_costly"    # 會花 LLM token（e.g. generate）
    DESTRUCTIVE = "destructive"      # 覆寫檔案 / 無法還原


@dataclass(frozen=True)
class ToolSpec:
    """單一 tool 的註冊資訊。"""

    name: str
    func: Callable
    description: str
    safety: SafetyLevel
    # JSON schema（OpenAI function calling 格式），Phase 1 實作時逐一補上
    input_schema: dict = field(default_factory=dict)


_REGISTRY: dict[str, ToolSpec] = {}


def register_tool(spec: ToolSpec) -> ToolSpec:
    """註冊一個 tool。重複註冊同名 tool 會覆寫（方便測試 reload）。"""
    _REGISTRY[spec.name] = spec
    return spec


def get_tool(name: str) -> ToolSpec:
    """取得已註冊的 tool，找不到就丟 KeyError。"""
    if name not in _REGISTRY:
        raise KeyError(f"tool not registered: {name}")
    return _REGISTRY[name]


def list_tools() -> list[ToolSpec]:
    """列出所有已註冊 tool，依名稱排序。"""
    return sorted(_REGISTRY.values(), key=lambda s: s.name)


def clear_registry() -> None:
    """僅供測試使用。"""
    _REGISTRY.clear()
