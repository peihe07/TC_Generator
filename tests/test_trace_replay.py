"""Trace replay CLI 測試。

用真實 tools（READ_ONLY / WRITE_SAFE）跑一次 → 記錄 trace → replay → 驗證 hash 一致。
"""

from __future__ import annotations

import json

import pytest

from agent_dispatcher import DispatchContext, dispatch_tool
from tools.replay import format_report, main, replay_session
from trace_store import SqliteTraceStore


def _group_rows() -> list[dict]:
    # 預填 test_set 讓 group_tests_tool 直接走 existing 路徑，
    # 不會觸發 AI 分類（trace replay 需要確定性結果）。
    return [
        {"id": "r1", "reqId": "SWE1-DM-001", "testItem": "PDM01 text", "testSet": "Access"},
        {"id": "r2", "reqId": "SWE1-DM-002", "testItem": "PDM02 text", "testSet": "Access"},
    ]


@pytest.fixture
def traced_session(tmp_path):
    """跑兩次 READ_ONLY 工具寫進 trace，回傳 (db_path, session_id)。

    group_tests 現在會觸發 AI 分類（WRITE_COSTLY / 非確定性），改用 validate_tc
    連跑兩次當確定性的回放 fixture。
    """
    db_path = tmp_path / "trace.db"
    trace = SqliteTraceStore(db_path)
    ctx = DispatchContext(
        job_store={},
        trace_store=trace,
        session_id="sess-A",
        rules_text="",
        auto_approve=True,
    )

    dispatch_tool(
        "validate_tc",
        {
            "tc": {
                "tc_id": "x",
                "test_item": "orig\n\n(a → b)",
                "pre_conditions": "NA",
                "test_procedure": "1. do. 2. verify.",
                "expected_result": "1. ok.\n2. ok.",
                "design_method": "功能測試 (Functional based ; no specific technique)",
                "priority": "P1",
            }
        },
        ctx,
    )
    dispatch_tool(
        "validate_tc",
        {
            "tc": {
                "tc_id": "x",
                "test_item": "orig\n\n(a → b)",
                "pre_conditions": "NA",
                "test_procedure": "1. do. 2. verify.",
                "expected_result": "1. ok.\n2. ok.",
                "design_method": "功能測試 (Functional based ; no specific technique)",
                "priority": "P1",
            }
        },
        ctx,
    )
    trace.close()
    yield db_path, "sess-A"


def test_replay_matches_identical_results(traced_session):
    db_path, sid = traced_session
    outcomes = replay_session(sid, trace_db=db_path)

    assert len(outcomes) == 2
    assert all(o.status == "match" for o in outcomes), [o.__dict__ for o in outcomes]


def test_replay_report_has_expected_lines(traced_session):
    db_path, sid = traced_session
    outcomes = replay_session(sid, trace_db=db_path)
    report = format_report(sid, outcomes)

    assert f"Replay session: {sid}" in report
    assert "Tool calls: 2" in report
    assert "[OK]" in report
    assert "validate_tc" in report


def test_replay_skips_destructive_by_default(tmp_path):
    db_path = tmp_path / "trace.db"
    trace = SqliteTraceStore(db_path)
    ctx = DispatchContext(
        job_store={},
        trace_store=trace,
        session_id="sess-B",
        rules_text="",
        auto_approve=True,
    )
    # 故意跑一個 WRITE_COSTLY —— 但不想花錢，所以直接寫 trace event，不真的呼叫 tool
    from trace_store import TraceEvent

    trace.record(
        TraceEvent(
            session_id="sess-B",
            type="tool_call",
            tool="generate_tc",
            args={"rows": [], "context": {"project": "p", "test_group": "g"}, "rules_text": ""},
            result_hash="sha256:fake",
            duration_ms=0,
        )
    )
    trace.close()

    outcomes = replay_session("sess-B", trace_db=db_path)
    assert outcomes[0].status == "skipped"
    assert "write_costly" in outcomes[0].message


def test_replay_detects_mismatch_when_args_changed(tmp_path):
    db_path = tmp_path / "trace.db"
    trace = SqliteTraceStore(db_path)
    from trace_store import TraceEvent

    trace.record(
        TraceEvent(
            session_id="sess-C",
            type="tool_call",
            tool="validate_tc",
            args={
                "tc": {
                    "tc_id": "x",
                    "test_item": "orig\n\n(a → b)",
                    "pre_conditions": "NA",
                    "test_procedure": "1. do. 2. verify.",
                    "expected_result": "1. ok.\n2. ok.",
                    "design_method": "功能測試 (Functional based ; no specific technique)",
                    "priority": "P1",
                }
            },
            result_hash="sha256:definitely_wrong_hash",
            duration_ms=0,
        )
    )
    trace.close()

    outcomes = replay_session("sess-C", trace_db=db_path)
    assert outcomes[0].status == "mismatch"
    assert outcomes[0].new_hash != outcomes[0].original_hash


def test_replay_error_when_tool_missing(tmp_path):
    db_path = tmp_path / "trace.db"
    trace = SqliteTraceStore(db_path)
    from trace_store import TraceEvent

    trace.record(
        TraceEvent(
            session_id="sess-D",
            type="tool_call",
            tool="nope_tool",
            args={},
            result_hash="sha256:whatever",
        )
    )
    trace.close()

    outcomes = replay_session("sess-D", trace_db=db_path)
    assert outcomes[0].status == "error"
    assert "no longer registered" in outcomes[0].message


def test_replay_raises_when_session_has_no_events(tmp_path):
    db_path = tmp_path / "trace.db"
    SqliteTraceStore(db_path).close()  # empty db

    with pytest.raises(SystemExit):
        replay_session("missing-sess", trace_db=db_path)


def test_main_returns_zero_on_all_match(traced_session, capsys):
    db_path, sid = traced_session
    rc = main([sid, "--db", str(db_path)])
    assert rc == 0
    assert "Replay session" in capsys.readouterr().out


def test_main_returns_nonzero_on_mismatch(tmp_path, capsys):
    db_path = tmp_path / "trace.db"
    trace = SqliteTraceStore(db_path)
    from trace_store import TraceEvent

    trace.record(
        TraceEvent(
            session_id="bad",
            type="tool_call",
            tool="validate_tc",
            args={
                "tc": {
                    "tc_id": "x",
                    "test_item": "orig\n\n(a → b)",
                    "pre_conditions": "NA",
                    "test_procedure": "1. do. 2. verify.",
                    "expected_result": "1. ok.\n2. ok.",
                    "design_method": "功能測試 (Functional based ; no specific technique)",
                    "priority": "P1",
                }
            },
            result_hash="sha256:wrong",
        )
    )
    trace.close()

    rc = main(["bad", "--db", str(db_path)])
    assert rc == 1
    out = capsys.readouterr().out
    assert "[DIFF]" in out


def test_main_json_output(traced_session, capsys):
    db_path, sid = traced_session
    rc = main([sid, "--db", str(db_path), "--json"])
    assert rc == 0
    payload = json.loads(capsys.readouterr().out)
    assert len(payload) == 2
    assert all(p["status"] == "match" for p in payload)
