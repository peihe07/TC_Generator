"""SqliteAgentSessionStore 單元測試。"""

from __future__ import annotations

import pytest

from agent_session_store import (
    AgentSession,
    SqliteAgentSessionStore,
    default_session_db_path,
)


@pytest.fixture
def store(tmp_path):
    s = SqliteAgentSessionStore(tmp_path / "sessions.db")
    yield s
    s.close()


def test_create_assigns_uuid_and_persists(store):
    session = store.create()
    assert session.session_id
    assert session.history == []
    assert store.get(session.session_id) is not None


def test_get_or_create_returns_existing(store):
    first = store.create()
    second = store.get_or_create(first.session_id)
    assert second.session_id == first.session_id


def test_get_or_create_handles_none_and_missing(store):
    fresh_none = store.get_or_create(None)
    fresh_missing = store.get_or_create("does-not-exist")
    assert fresh_none.session_id != fresh_missing.session_id


def test_update_persists_history_and_cost(store):
    s = store.create()
    new_history = [{"role": "user", "content": "hi"}]
    updated = store.update(s.session_id, history=new_history, total_cost_usd=0.123)
    assert updated.history == new_history
    assert updated.total_cost_usd == 0.123

    reloaded = store.get(s.session_id)
    assert reloaded.history == new_history
    assert reloaded.total_cost_usd == 0.123


def test_update_missing_session_raises(store):
    with pytest.raises(KeyError):
        store.update("missing", history=[])


def test_list_recent_sorted_by_updated_at(store):
    a = store.create()
    b = store.create()
    # touch a last
    store.update(b.session_id, history=[{"role": "user", "content": "first"}])
    store.update(a.session_id, history=[{"role": "user", "content": "second"}])

    recent = store.list_recent(limit=10)
    assert recent[0].session_id == a.session_id


def test_delete_removes_session(store):
    s = store.create()
    assert store.delete(s.session_id) is True
    assert store.get(s.session_id) is None
    assert store.delete(s.session_id) is False


def test_purge_older_than(store):
    import time as time_mod

    old = store.create()
    store.update(old.session_id, history=[])
    # 手動把 updated_at 往過去挪
    store._conn.execute(
        "UPDATE agent_sessions SET updated_at = ? WHERE session_id = ?",
        (time_mod.time() - 10_000, old.session_id),
    )
    store._conn.commit()

    new = store.create()
    removed = store.purge_older_than(max_age_seconds=3600)
    assert removed == 1
    assert store.get(old.session_id) is None
    assert store.get(new.session_id) is not None


def test_default_session_db_path_env_override(monkeypatch, tmp_path):
    custom = tmp_path / "custom-sessions.db"
    monkeypatch.setenv("TC_AGENT_SESSION_DB", str(custom))
    assert default_session_db_path() == custom
