"""SqliteTraceStore 單元測試。"""

from __future__ import annotations

import json
import time

import pytest

from trace_store import (
    SqliteTraceStore,
    TraceEvent,
    default_trace_db_path,
    result_hash,
)


@pytest.fixture
def store(tmp_path):
    s = SqliteTraceStore(tmp_path / "trace.db")
    yield s
    s.close()


def test_record_and_replay_preserves_order(store):
    sid = "sess-1"
    store.record(TraceEvent(session_id=sid, type="tool_call", tool="parse_workbook"))
    store.record(TraceEvent(session_id=sid, type="tool_result", tool="parse_workbook"))
    store.record(TraceEvent(session_id=sid, type="llm_response"))

    events = store.replay(sid)
    assert [e.type for e in events] == ["tool_call", "tool_result", "llm_response"]


def test_record_tool_call_hashes_result(store):
    sid = "sess-2"
    store.record_tool_call(
        session_id=sid,
        tool="group_tests",
        args={"rows": [1, 2]},
        result={"groups": [{"testSet": "A", "count": 2}]},
        duration_ms=42,
    )
    events = store.replay(sid)
    assert len(events) == 1
    e = events[0]
    assert e.tool == "group_tests"
    assert e.result_hash and e.result_hash.startswith("sha256:")
    assert e.duration_ms == 42
    # same input → same hash
    same = result_hash({"groups": [{"testSet": "A", "count": 2}]})
    assert same == e.result_hash


def test_result_hash_is_order_independent():
    a = result_hash({"x": 1, "y": 2})
    b = result_hash({"y": 2, "x": 1})
    assert a == b


def test_result_hash_differs_when_content_changes():
    a = result_hash({"x": 1})
    b = result_hash({"x": 2})
    assert a != b


def test_sessions_are_isolated(store):
    store.record(TraceEvent(session_id="s1", type="tool_call", tool="a"))
    store.record(TraceEvent(session_id="s2", type="tool_call", tool="b"))

    assert [e.tool for e in store.replay("s1")] == ["a"]
    assert [e.tool for e in store.replay("s2")] == ["b"]
    assert store.replay("missing") == []


def test_list_sessions_sorted_by_last_activity(store):
    store.record(TraceEvent(session_id="old", type="tool_call", ts=100))
    store.record(TraceEvent(session_id="new", type="tool_call", ts=200))
    store.record(TraceEvent(session_id="old", type="tool_call", ts=150))

    sessions = store.list_sessions()
    assert sessions[0] == "new"
    assert "old" in sessions


def test_export_jsonl_roundtrips(store):
    sid = "export-sess"
    store.record(TraceEvent(session_id=sid, type="tool_call", tool="parse_workbook"))
    store.record(TraceEvent(session_id=sid, type="tool_result", tool="parse_workbook"))

    blob = store.export_jsonl(sid)
    lines = blob.decode("utf-8").strip().split("\n")
    assert len(lines) == 2
    payloads = [json.loads(line) for line in lines]
    assert [p["type"] for p in payloads] == ["tool_call", "tool_result"]
    assert all(p["session_id"] == sid for p in payloads)


def test_delete_session_removes_events(store):
    store.record(TraceEvent(session_id="del", type="tool_call", tool="x"))
    store.record(TraceEvent(session_id="del", type="llm_response"))
    store.record(TraceEvent(session_id="keep", type="tool_call", tool="y"))

    removed = store.delete_session("del")
    assert removed == 2
    assert store.replay("del") == []
    assert len(store.replay("keep")) == 1


def test_purge_older_than(store):
    now = time.time()
    store.record(TraceEvent(session_id="s", type="tool_call", ts=now - 10_000))
    store.record(TraceEvent(session_id="s", type="tool_call", ts=now))

    removed = store.purge_older_than(max_age_seconds=3600)
    assert removed == 1
    remaining = store.replay("s")
    assert len(remaining) == 1


def test_event_from_payload_ignores_unknown_fields(store):
    # 模擬未來 schema 多了欄位的情況
    store._conn.execute(
        "INSERT INTO trace_events (session_id, ts, type, tool, payload) VALUES (?, ?, ?, ?, ?)",
        (
            "future",
            time.time(),
            "tool_call",
            "mystery",
            json.dumps(
                {
                    "session_id": "future",
                    "type": "tool_call",
                    "tool": "mystery",
                    "ts": 1.0,
                    "future_field": "will not break load",
                }
            ),
        ),
    )
    store._conn.commit()

    events = store.replay("future")
    assert events[0].tool == "mystery"


def test_default_trace_db_path_env_override(monkeypatch, tmp_path):
    custom = tmp_path / "custom.db"
    monkeypatch.setenv("TC_TRACE_DB", str(custom))
    assert default_trace_db_path() == custom


def test_record_llm_response_usage_survives_roundtrip(store):
    store.record_llm_response(
        session_id="llm",
        reasoning="user asked to parse, I called parse_workbook",
        usage={"input_tokens": 100, "output_tokens": 30, "cached": 80},
    )
    events = store.replay("llm")
    assert events[0].llm_reasoning.startswith("user asked")
    assert events[0].usage["cached"] == 80
