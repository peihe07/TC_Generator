"""generate_tc tool：執行單一批次 TC 生成（一次 LLM 呼叫）。

Tool 只處理「跑一批」：SSE 迴圈、budget gate、cost 累計都留給 route 層。
這樣 Agent 若想生成也只要呼叫這個 tool，不必碰 streaming。
"""

from __future__ import annotations

from generator import (
    DEFAULT_MODEL,
    GenerationError,
    GenerationResult,
    calculate_cost,
    generate_batch,
    generate_batch_multi,
    generate_single_tc,
    generate_tcs_for_row,
)

from .errors import ToolError
from .registry import SafetyLevel, ToolSpec, register_tool
from .schemas import GENERATE_TC_SCHEMA


def _result_to_dict(result: GenerationResult, tc_groups: list[list[dict]]) -> dict:
    return {
        # tcData: list[list[dict]] — 每個 input row 對應一個 TC list（長度 1..N）
        "tcData": tc_groups,
        # splitMeta: list[dict] — 與 tcData 對齊，每項 {"req_id","reasoning","keywords"}
        # Legacy (allow_split=False) 路徑為空 list。
        "splitMeta": getattr(result, "split_meta", []) or [],
        "cost": result.cost,
        "inputTokens": result.input_tokens,
        "outputTokens": result.output_tokens,
        "cacheCreationTokens": getattr(result, "cache_creation_tokens", 0),
        "cacheReadTokens": getattr(result, "cache_read_tokens", 0),
        "model": getattr(result, "model", "") or "",
    }


def generate_tc_tool(
    *,
    rows: list[dict],
    context: dict,
    spec_index: dict | None = None,
    rules_text: str,
    model: str = DEFAULT_MODEL,
    allow_split: bool = True,
) -> dict:
    """Run one LLM batch call to generate TC(s).

    Args:
        rows: snake_case dicts
        context: `{project, test_group, test_set}`；single-row 時 tool 會把
                 `test_set` 覆寫為 row 的 test_set（對齊原 route 行為）
        spec_index: 來自 Slot C / SYS1 的 spec 索引，None 視為空 dict
        rules_text: ASPICE SWE.6 規則 markdown
        model: OpenAI model id
        allow_split: True (default) 時讓 AI 自行決定每個 req 要回 1..5 筆 TC；
                     False 時維持舊行為，每個 req 強制 1 筆 TC（legacy 路徑）。

    Returns:
        `{"tcData": list[list[dict]], "cost", "inputTokens", "outputTokens",
          "cacheCreationTokens", "cacheReadTokens", "model"}`
        `tcData` 外層長度 == len(rows)，內層為該 req 對應的 1..N 筆 TC。

    Raises:
        ToolError: rows 為空 或 底層 GenerationError
    """
    if not rows:
        raise ToolError("rows must not be empty", code="bad_request")

    spec = spec_index or {}
    local_context = dict(context)

    try:
        if allow_split:
            if len(rows) == 1:
                row = rows[0]
                local_context["test_set"] = row.get("test_set", "N/A") or "N/A"
                result = generate_tcs_for_row(row, local_context, spec, rules_text, model)
                # result.tc_data 為 list[dict] → 包成 list[list[dict]]
                tc_groups = [result.tc_data if isinstance(result.tc_data, list) else [result.tc_data]]
            else:
                result = generate_batch_multi(rows, local_context, spec, rules_text, model)
                tc_groups = result.tc_data if isinstance(result.tc_data, list) else []
        else:
            # Legacy 1:1 path（維持給 regenerate 或其他舊用途使用）
            if len(rows) == 1:
                row = rows[0]
                local_context["test_set"] = row.get("test_set", "N/A") or "N/A"
                result = generate_single_tc(row, local_context, spec, rules_text, model)
                tc_groups = [[result.tc_data]] if isinstance(result.tc_data, dict) else [result.tc_data]
            else:
                result = generate_batch(rows, local_context, spec, rules_text, model)
                tc_list = result.tc_data if isinstance(result.tc_data, list) else [result.tc_data]
                # 每個 req 一筆 → wrap 成 [[tc]]
                tc_groups = [[tc] for tc in tc_list]
    except GenerationError as exc:
        raise ToolError(f"generation failed: {exc}", code="internal") from exc

    return _result_to_dict(result, tc_groups)


def estimate_batch_cost(
    *,
    row_count: int,
    model: str,
    avg_input_tokens: int = 1500,
    avg_output_tokens: int = 800,
) -> float:
    """Rough cost estimator for budget gating. Mirrors api_server._estimate_cost."""
    return calculate_cost(
        avg_input_tokens * row_count,
        avg_output_tokens * row_count,
        model,
    )


register_tool(
    ToolSpec(
        name="generate_tc",
        func=generate_tc_tool,
        description=GENERATE_TC_SCHEMA["description"],
        safety=SafetyLevel.WRITE_COSTLY,
        input_schema=GENERATE_TC_SCHEMA,
    )
)
