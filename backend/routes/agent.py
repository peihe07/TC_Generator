"""`/api/agent/chat` — Agent 副駕模式的 SSE endpoint。

輸入:
    POST /api/agent/chat  (application/json)
    {
      "session_id": "uuid" | null,
      "message": "string",
      "approved_call_ids": ["call-xxx", ...]  // 可選，使用者剛剛點了確認
    }

輸出（SSE）:
    event: message        → {text}
    event: tool_call      → {call_id, tool, args}
    event: tool_result    → {call_id, tool, duration_ms, result}
    event: tool_error     → {call_id, tool, error}
    event: require_confirm → {call_id, tool, args, est_cost_usd}
    event: done           → {step_count, session_id}
    event: error          → {code, message}
"""

from __future__ import annotations

import json
from typing import Any, Callable

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from agent_dispatcher import DispatchContext, LLMFn, run_agent_turn
from agent_session_store import SqliteAgentSessionStore
from trace_store import SqliteTraceStore


class AgentChatRequest(BaseModel):
    session_id: str | None = None
    message: str = Field(min_length=1)
    approved_call_ids: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Factory：把依賴（stores / llm_fn / rules）綁進一個 router
# ---------------------------------------------------------------------------

def build_agent_router(
    *,
    job_store: Any,
    trace_store: SqliteTraceStore,
    session_store: SqliteAgentSessionStore,
    rules_text_getter: Callable[[], str],
    llm_fn: LLMFn | None = None,
) -> APIRouter:
    """回傳一個已綁定依賴的 router。main app 呼叫此工廠。

    使用 factory 而非 FastAPI Depends，是因為依賴都是 process-wide singleton
    且必須跨請求共享同一個 sqlite connection。
    """

    router = APIRouter(prefix="/api/agent", tags=["agent"])

    @router.post("/chat")
    async def agent_chat(payload: AgentChatRequest) -> StreamingResponse:
        session = session_store.get_or_create(payload.session_id)

        ctx = DispatchContext(
            job_store=job_store,
            trace_store=trace_store,
            session_id=session.session_id,
            rules_text=rules_text_getter(),
            approved_call_ids=set(payload.approved_call_ids),
            auto_approve=False,
        )

        def _sse(event_type: str, data: dict) -> str:
            return f"event: {event_type}\ndata: {json.dumps(data, ensure_ascii=False, default=str)}\n\n"

        def event_generator():
            try:
                events, new_history = run_agent_turn(
                    user_message=payload.message,
                    history=session.history,
                    ctx=ctx,
                    llm_fn=llm_fn,
                )
            except Exception as exc:  # 防守性：任何未預期錯誤都通知前端
                yield _sse("error", {"code": "internal", "message": str(exc)})
                return

            # 持久化最新 history
            try:
                session_store.update(session.session_id, history=new_history)
            except KeyError:
                pass  # 理論上不該發生；忽略避免 event stream 中斷

            for event in events:
                payload_data = dict(event.data)
                # 在每個事件中附帶 session_id，讓前端方便關聯
                payload_data.setdefault("session_id", session.session_id)
                yield _sse(event.type, payload_data)

        return StreamingResponse(
            event_generator(),
            media_type="text/event-stream",
            headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
        )

    @router.get("/sessions")
    def list_agent_sessions(limit: int = 20) -> dict:
        sessions = session_store.list_recent(limit=limit)
        return {
            "sessions": [
                {
                    "sessionId": s.session_id,
                    "totalCostUsd": s.total_cost_usd,
                    "createdAt": s.created_at,
                    "updatedAt": s.updated_at,
                    "messageCount": len(s.history),
                }
                for s in sessions
            ]
        }

    @router.get("/sessions/{session_id}")
    def get_agent_session(session_id: str) -> dict:
        session = session_store.get(session_id)
        if session is None:
            raise HTTPException(status_code=404, detail="session not found")
        return {
            "sessionId": session.session_id,
            "history": session.history,
            "totalCostUsd": session.total_cost_usd,
            "createdAt": session.created_at,
            "updatedAt": session.updated_at,
        }

    @router.delete("/sessions/{session_id}")
    def delete_agent_session(session_id: str) -> dict:
        ok = session_store.delete(session_id)
        if not ok:
            raise HTTPException(status_code=404, detail="session not found")
        return {"deleted": True}

    @router.get("/sessions/{session_id}/trace")
    def export_agent_trace(session_id: str) -> StreamingResponse:
        """下載 JSONL 稽核檔。"""
        blob = trace_store.export_jsonl(session_id)
        return StreamingResponse(
            iter([blob]),
            media_type="application/x-ndjson",
            headers={"Content-Disposition": f'attachment; filename="trace-{session_id}.jsonl"'},
        )

    return router
