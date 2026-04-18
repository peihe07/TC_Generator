"""Agent dispatcher — LLM loop + tool 分發。

這支模組是 Phase 1 的核心：
1. 把使用者訊息送給 OpenAI（附 `openai_tool_definitions()`）
2. LLM 回 tool_calls → 查 registry → 注入 caller-injected 依賴 → 執行
3. 把結果寫回 trace_store
4. 把結果塞回 messages，直到 LLM 不再要求呼叫工具

Route 層（`routes/agent.py`，下一步實作）負責把 dispatcher 產生的事件串流成 SSE；
測試則直接 mock `llm_fn` 來驗證 dispatch 行為。
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Iterator, Literal

from tools import ToolError, get_tool, openai_tool_definitions
from tools.registry import SafetyLevel
from tools._budget import needs_confirmation
from tools.generate import estimate_batch_cost
from trace_store import SqliteTraceStore, TraceEvent


AgentEventType = Literal[
    "message",
    "tool_call",
    "tool_result",
    "tool_error",
    "require_confirm",
    "done",
    "error",
]


@dataclass
class AgentEvent:
    """Dispatcher 產生的單一事件；route 把它包成 SSE。"""

    type: str
    data: dict


@dataclass
class DispatchContext:
    """跨 tool call 共用的依賴。Agent 看不到這些，由 dispatcher 注入。"""

    job_store: Any
    trace_store: SqliteTraceStore
    session_id: str
    rules_text: str = ""
    # 使用者已核准的 tool call id 集合（budget gate 用）
    approved_call_ids: set[str] = field(default_factory=set)
    # 預設自動核准（測試 / CLI 用）；正式環境由 UI 送回 confirm 才填入 approved_call_ids
    auto_approve: bool = False


# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT_TEMPLATE = """\
You are the TC Generator operations co-pilot. Users are ASPICE SWE.6 test engineers
working on automotive HMI test cases. They drive the GUI themselves — you only
assist with what the GUI cannot do well: cross-job queries, batch operations, and
natural-language diagnostics.

# Hard rules
1. You MUST complete every task by calling whitelisted tools. Never invent jobIds,
   row contents, spec references, or costs.
2. If the user's request is ambiguous or references prior work, call `list_jobs`
   or `get_job_detail` first (coming in Phase 4). Until those exist, ask the user
   to clarify rather than guessing.
3. For spec-match issues: check the match summary first and suggest attaching a
   SYS1 reference workbook before proposing fuzzy-threshold changes.
4. For validator warnings: classify as soft (language/format) vs hard (missing
   verification / 1:1 violation). Retry hard issues; surface soft issues to the
   user.
5. Any action where estimated cost > $0.50 requires explicit user confirmation.
   The harness will stop you and ask — do not try to bypass.
6. Reply in Traditional Chinese (繁體中文); keep technical keywords in English.

# Tool notes
- `parse_workbook` takes file system paths. The user attaches files via the chat
  UI; paths are already placed on disk for you.
- `generate_tc` consumes LLM tokens. Always estimate cost before looping.
- `write_excel` is DESTRUCTIVE and may overwrite files — always confirm first.

# Style
- Be terse. Prefer numbered steps over prose when reporting outcomes.
- When you finish, summarise what changed and which jobId is now current.
"""


def build_system_prompt(rules_text: str | None = None) -> str:
    """返回完整 system prompt；rules_text 不為空時附在後面。"""
    if rules_text:
        return (
            f"{SYSTEM_PROMPT_TEMPLATE}\n\n"
            "# ASPICE SWE.6 rules (authoritative, auto-loaded)\n\n"
            f"{rules_text}"
        )
    return SYSTEM_PROMPT_TEMPLATE


# ---------------------------------------------------------------------------
# Tool dispatch
# ---------------------------------------------------------------------------

# 哪些 tool 需要注入哪些 caller-provided 參數。
_INJECT_JOB_STORE = {"parse_workbook", "list_jobs", "estimate_cost"}
_INJECT_RULES_TEXT = {"generate_tc"}


def _inject_dependencies(name: str, args: dict, ctx: DispatchContext) -> dict:
    """把 agent 不該自己傳的依賴塞回 args。"""
    merged = dict(args)
    if name in _INJECT_JOB_STORE:
        merged["job_store"] = ctx.job_store
    if name in _INJECT_RULES_TEXT and "rules_text" not in merged:
        merged["rules_text"] = ctx.rules_text
    return merged


def _requires_confirmation(name: str, args: dict) -> tuple[bool, float]:
    """根據 safety level + budget 估算，回傳 (需不需要確認, 預估美金成本)。"""
    spec = get_tool(name)

    if spec.safety is SafetyLevel.READ_ONLY:
        return (False, 0.0)
    if spec.safety is SafetyLevel.WRITE_SAFE:
        return (False, 0.0)
    if spec.safety is SafetyLevel.DESTRUCTIVE:
        return (True, 0.0)
    if spec.safety is SafetyLevel.WRITE_COSTLY:
        rows = args.get("rows") or []
        model = args.get("model", "gpt-4.1-mini")
        est = estimate_batch_cost(row_count=len(rows), model=model)
        return (needs_confirmation(est), est)

    return (False, 0.0)


def dispatch_tool(name: str, args: dict, ctx: DispatchContext) -> dict:
    """執行單一 tool call，含 trace 記錄。

    Returns:
        `{"ok": bool, "result"?: Any, "error"?: {code, message}, "duration_ms": int}`
    """
    spec = get_tool(name)
    injected = _inject_dependencies(name, args, ctx)

    started = time.time()
    try:
        result = spec.func(**injected)
    except ToolError as exc:
        duration_ms = int((time.time() - started) * 1000)
        ctx.trace_store.record(
            TraceEvent(
                session_id=ctx.session_id,
                type="tool_error",
                tool=name,
                args=args,  # 不記 injected 的 secret 欄位
                duration_ms=duration_ms,
                message=exc.message,
            )
        )
        return {
            "ok": False,
            "error": {"code": exc.code, "message": exc.message, "details": exc.details},
            "duration_ms": duration_ms,
        }

    duration_ms = int((time.time() - started) * 1000)
    ctx.trace_store.record_tool_call(
        session_id=ctx.session_id,
        tool=name,
        args=args,
        result=result,
        duration_ms=duration_ms,
    )
    return {"ok": True, "result": result, "duration_ms": duration_ms}


# ---------------------------------------------------------------------------
# LLM loop
# ---------------------------------------------------------------------------

@dataclass
class LLMStep:
    """LLM 一回合的結果，抽象化掉 OpenAI / Anthropic 差異。"""

    text: str | None = None
    tool_calls: list[dict] = field(default_factory=list)
    # 每個 tool_call = {"id": str, "name": str, "args": dict}
    usage: dict | None = None


LLMFn = Callable[[list[dict], list[dict]], LLMStep]
# signature: fn(messages, tool_definitions) -> LLMStep


def _default_llm_fn(messages: list[dict], tool_definitions: list[dict]) -> LLMStep:
    """真正呼叫 OpenAI Chat Completions 的實作。測試時會被替換。"""
    from openai import OpenAI  # 延後 import，避免測試不必要

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        tools=tool_definitions,
        tool_choice="auto",
    )
    choice = response.choices[0].message
    tool_calls = []
    for call in choice.tool_calls or []:
        try:
            args = json.loads(call.function.arguments or "{}")
        except json.JSONDecodeError:
            args = {}
        tool_calls.append(
            {"id": call.id, "name": call.function.name, "args": args}
        )
    usage = None
    if response.usage:
        usage = {
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
        }
    return LLMStep(text=choice.content, tool_calls=tool_calls, usage=usage)


def run_agent_turn(
    *,
    user_message: str,
    history: list[dict],
    ctx: DispatchContext,
    llm_fn: LLMFn | None = None,
    max_steps: int = 8,
) -> tuple[list[AgentEvent], list[dict]]:
    """跑完使用者一次發言所觸發的所有 LLM ↔ tool 迴圈。

    Args:
        user_message: 使用者本次訊息
        history: 先前的 messages（不含 system prompt，由本函式在 call 時加上）
        ctx: 依賴注入容器
        llm_fn: 可注入的 LLM 呼叫（預設 OpenAI）
        max_steps: 最多幾輪 tool-call 來回，防失控

    Returns:
        `(events, new_history)`；new_history 不含 system prompt。
    """
    llm = llm_fn or _default_llm_fn
    tool_defs = openai_tool_definitions()

    # Build messages with system prompt prepended
    system_msg = {"role": "system", "content": build_system_prompt(ctx.rules_text)}
    messages = [system_msg, *history, {"role": "user", "content": user_message}]

    events: list[AgentEvent] = []
    new_history = [*history, {"role": "user", "content": user_message}]

    for step in range(max_steps):
        llm_step = llm(messages, tool_defs)

        if llm_step.usage:
            ctx.trace_store.record_llm_response(
                session_id=ctx.session_id,
                reasoning=llm_step.text,
                usage=llm_step.usage,
            )

        if llm_step.text:
            events.append(AgentEvent("message", {"text": llm_step.text}))

        if not llm_step.tool_calls:
            # 收尾：把 assistant 最終回覆存進 history
            new_history.append({"role": "assistant", "content": llm_step.text or ""})
            events.append(AgentEvent("done", {"step_count": step + 1}))
            return events, new_history

        # assistant 訊息含 tool_calls，也要回寫進 messages
        messages.append(
            {
                "role": "assistant",
                "content": llm_step.text or "",
                "tool_calls": [
                    {
                        "id": call["id"],
                        "type": "function",
                        "function": {
                            "name": call["name"],
                            "arguments": json.dumps(call["args"], ensure_ascii=False),
                        },
                    }
                    for call in llm_step.tool_calls
                ],
            }
        )
        new_history.append(messages[-1])

        for call in llm_step.tool_calls:
            name = call["name"]
            args = call["args"]
            call_id = call["id"]

            need_confirm, est_cost = _requires_confirmation(name, args)
            if need_confirm and not (ctx.auto_approve or call_id in ctx.approved_call_ids):
                events.append(
                    AgentEvent(
                        "require_confirm",
                        {
                            "call_id": call_id,
                            "tool": name,
                            "args": args,
                            "est_cost_usd": round(est_cost, 4),
                        },
                    )
                )
                # 把 "user_declined" 回寫，讓 LLM 下一輪看到
                tool_msg = {
                    "role": "tool",
                    "tool_call_id": call_id,
                    "content": json.dumps(
                        {"ok": False, "error": {"code": "requires_confirmation"}},
                        ensure_ascii=False,
                    ),
                }
                messages.append(tool_msg)
                new_history.append(tool_msg)
                # 本 turn 提早結束：等待下一輪帶 approved_call_ids 再 run
                return events, new_history

            events.append(AgentEvent("tool_call", {"call_id": call_id, "tool": name, "args": args}))
            outcome = dispatch_tool(name, args, ctx)

            if outcome["ok"]:
                events.append(
                    AgentEvent(
                        "tool_result",
                        {
                            "call_id": call_id,
                            "tool": name,
                            "duration_ms": outcome["duration_ms"],
                            "result": outcome["result"],
                        },
                    )
                )
                tool_content = json.dumps(
                    {"ok": True, "result": outcome["result"]},
                    default=str, ensure_ascii=False,
                )
            else:
                events.append(
                    AgentEvent(
                        "tool_error",
                        {"call_id": call_id, "tool": name, "error": outcome["error"]},
                    )
                )
                tool_content = json.dumps({"ok": False, "error": outcome["error"]}, ensure_ascii=False)

            tool_msg = {"role": "tool", "tool_call_id": call_id, "content": tool_content}
            messages.append(tool_msg)
            new_history.append(tool_msg)

    # 超過 max_steps 仍要回傳 error 事件，避免使用者以為還在跑
    events.append(
        AgentEvent(
            "error",
            {"code": "max_steps_exceeded", "message": f"Agent exceeded {max_steps} tool-call rounds."},
        )
    )
    return events, new_history
