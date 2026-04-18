"""`/api/agent/*` SSE / session endpoint 測試。

用獨立 `FastAPI` + factory-built router，避免影響 `api_server.app` 的
process-wide store。LLM 呼叫一律 mock。
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from agent_dispatcher import LLMStep
from agent_session_store import SqliteAgentSessionStore
from routes.agent import build_agent_router
from trace_store import SqliteTraceStore


def _mock_llm(script: list[LLMStep]):
    it = iter(script)

    def fn(messages, tool_defs):
        return next(it)

    return fn


@pytest.fixture
def client(tmp_path):
    app = FastAPI()
    trace = SqliteTraceStore(tmp_path / "trace.db")
    sessions = SqliteAgentSessionStore(tmp_path / "sessions.db")
    job_store: dict = {}

    # Injected LLM：先回一個純文字（完結），之後每次呼叫也都回文字
    def llm_fn(messages, tool_defs):
        user = messages[-1]["content"]
        return LLMStep(text=f"Echo: {user}", tool_calls=[])

    app.include_router(
        build_agent_router(
            job_store=job_store,
            trace_store=trace,
            session_store=sessions,
            rules_text_getter=lambda: "",
            llm_fn=llm_fn,
        )
    )
    with TestClient(app) as c:
        yield c, sessions, trace
    trace.close()
    sessions.close()


def test_chat_creates_session_and_streams_message(client):
    c, sessions, _ = client
    resp = c.post("/api/agent/chat", json={"message": "hi there"})
    assert resp.status_code == 200
    text = resp.text

    assert "event: message" in text
    assert '"text": "Echo: hi there"' in text
    assert "event: done" in text

    # session 已被持久化
    recent = sessions.list_recent()
    assert len(recent) == 1
    # 使用者 + 助理兩條都被存起來
    roles = [m["role"] for m in recent[0].history]
    assert "user" in roles and "assistant" in roles


def test_chat_reuses_session_id(client):
    c, sessions, _ = client
    first = c.post("/api/agent/chat", json={"message": "first"}).text
    # 從 SSE 抽出 session_id
    sid = sessions.list_recent()[0].session_id

    c.post("/api/agent/chat", json={"session_id": sid, "message": "second"})

    session = sessions.get(sid)
    # 第一次兩條（user+assistant），第二次再加兩條 → 4
    assert len(session.history) == 4


def test_chat_rejects_empty_message(client):
    c, _, _ = client
    resp = c.post("/api/agent/chat", json={"message": ""})
    assert resp.status_code == 422


def test_list_sessions(client):
    c, _, _ = client
    c.post("/api/agent/chat", json={"message": "first"})
    c.post("/api/agent/chat", json={"message": "second"})

    resp = c.get("/api/agent/sessions")
    assert resp.status_code == 200
    payload = resp.json()
    assert len(payload["sessions"]) == 2
    assert "sessionId" in payload["sessions"][0]
    assert "messageCount" in payload["sessions"][0]


def test_get_session_returns_history(client):
    c, sessions, _ = client
    c.post("/api/agent/chat", json={"message": "hello world"})
    sid = sessions.list_recent()[0].session_id

    resp = c.get(f"/api/agent/sessions/{sid}")
    assert resp.status_code == 200
    body = resp.json()
    assert body["sessionId"] == sid
    assert len(body["history"]) >= 1


def test_get_session_404(client):
    c, _, _ = client
    resp = c.get("/api/agent/sessions/does-not-exist")
    assert resp.status_code == 404


def test_delete_session(client):
    c, sessions, _ = client
    c.post("/api/agent/chat", json={"message": "x"})
    sid = sessions.list_recent()[0].session_id

    resp = c.delete(f"/api/agent/sessions/{sid}")
    assert resp.status_code == 200
    assert resp.json()["deleted"] is True

    # 再刪一次 → 404
    assert c.delete(f"/api/agent/sessions/{sid}").status_code == 404


def test_trace_export_returns_jsonl(client):
    c, sessions, _ = client
    c.post("/api/agent/chat", json={"message": "trace me"})
    sid = sessions.list_recent()[0].session_id

    resp = c.get(f"/api/agent/sessions/{sid}/trace")
    assert resp.status_code == 200
    assert "application/x-ndjson" in resp.headers["content-type"]
    # 該 SSE 回合沒有 tool_call，但仍可能是空（LLM_response 也沒 usage）
    # 至少能回 200 且合法字串
    assert resp.text == "" or resp.text.endswith("\n")


def test_chat_emits_tool_call_events(tmp_path):
    """當 LLM 回 tool_call 時，SSE 應看到 tool_call / tool_result 事件。"""
    app = FastAPI()
    trace = SqliteTraceStore(tmp_path / "trace.db")
    sessions = SqliteAgentSessionStore(tmp_path / "sessions.db")
    job_store: dict = {}

    script = iter(
        [
            LLMStep(
                tool_calls=[
                    {
                        "id": "call-1",
                        "name": "group_tests",
                        "args": {
                            "rows": [{"id": "r1", "reqId": "R-001", "testItem": "PDM01"}]
                        },
                    }
                ]
            ),
            LLMStep(text="grouped", tool_calls=[]),
        ]
    )

    app.include_router(
        build_agent_router(
            job_store=job_store,
            trace_store=trace,
            session_store=sessions,
            rules_text_getter=lambda: "",
            llm_fn=lambda *_: next(script),
        )
    )
    c = TestClient(app)
    resp = c.post("/api/agent/chat", json={"message": "group please"})
    text = resp.text

    assert "event: tool_call" in text
    assert "event: tool_result" in text
    assert '"tool": "group_tests"' in text
    assert "event: done" in text

    trace.close()
    sessions.close()
