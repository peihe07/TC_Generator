"""Tests for SqliteJobStore — persistence across instances."""
from __future__ import annotations

import json
import pickle
import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))

from job_store import SqliteJobStore  # noqa: E402


@pytest.fixture()
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "jobs.db"


def test_set_and_get_roundtrip(db_path: Path) -> None:
    store = SqliteJobStore(db_path)
    store["job-1"] = {"jobId": "job-1", "status": "parsed", "rowCount": 3}
    assert store.get("job-1") == {"jobId": "job-1", "status": "parsed", "rowCount": 3}


def test_bytes_payload_roundtrip(db_path: Path) -> None:
    """Raw file bytes (xlsx uploads) must survive JSON-safe serialization."""
    store = SqliteJobStore(db_path)
    raw = b"\x00\x01\x02PK\x03\x04" + b"\xff" * 100
    store["j"] = {"rawBytes": raw, "name": "sample.xlsx"}
    assert store["j"]["rawBytes"] == raw


def test_sql_payload_is_json_not_pickle(db_path: Path) -> None:
    """DB payload should be inspectable JSON instead of executable pickle bytes."""
    store = SqliteJobStore(db_path)
    store["job-json"] = {
        "jobId": "job-json",
        "rawBytes": b"\x00\x01binary",
        "nested": {"specBytes": b"\xff\x10"},
    }

    conn = sqlite3.connect(db_path)
    row = conn.execute("SELECT data FROM jobs WHERE id = ?", ("job-json",)).fetchone()
    assert row is not None

    payload = json.loads(row[0])
    assert payload["jobId"] == "job-json"
    assert payload["rawBytes"]["__type__"] == "bytes"
    assert payload["nested"]["specBytes"]["__type__"] == "bytes"


def test_legacy_pickle_payload_is_rejected(db_path: Path) -> None:
    """Unexpected legacy pickle blobs should not be deserialized."""
    conn = sqlite3.connect(db_path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS jobs ("
        "  id TEXT PRIMARY KEY,"
        "  data BLOB NOT NULL,"
        "  updated_at REAL NOT NULL DEFAULT (strftime('%s','now'))"
        ")"
    )
    conn.execute(
        "INSERT INTO jobs (id, data) VALUES (?, ?)",
        ("legacy", b"\x80\x05bad-pickle-payload"),
    )
    conn.commit()
    conn.close()

    store = SqliteJobStore(db_path)
    with pytest.raises(ValueError, match="invalid job payload"):
        store.get("legacy")


def test_valid_legacy_pickle_payload_is_rejected_by_default(db_path: Path) -> None:
    """Startup should not deserialize legacy pickle unless explicitly opted in."""
    record = {"jobId": "legacy-ok", "rawBytes": b"\x00\x01"}
    conn = sqlite3.connect(db_path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS jobs ("
        "  id TEXT PRIMARY KEY,"
        "  data BLOB NOT NULL,"
        "  updated_at REAL NOT NULL DEFAULT (strftime('%s','now'))"
        ")"
    )
    conn.execute(
        "INSERT INTO jobs (id, data) VALUES (?, ?)",
        ("legacy-ok", pickle.dumps(record, protocol=pickle.HIGHEST_PROTOCOL)),
    )
    conn.commit()
    conn.close()

    store = SqliteJobStore(db_path)
    with pytest.raises(ValueError, match="invalid job payload"):
        store.get("legacy-ok")


def test_valid_legacy_pickle_payload_can_be_migrated_with_explicit_opt_in(db_path: Path) -> None:
    """Trusted legacy app data can still be upgraded by an explicit migration run."""
    record = {"jobId": "legacy-ok", "rawBytes": b"\x00\x01"}
    conn = sqlite3.connect(db_path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS jobs ("
        "  id TEXT PRIMARY KEY,"
        "  data BLOB NOT NULL,"
        "  updated_at REAL NOT NULL DEFAULT (strftime('%s','now'))"
        ")"
    )
    conn.execute(
        "INSERT INTO jobs (id, data) VALUES (?, ?)",
        ("legacy-ok", pickle.dumps(record, protocol=pickle.HIGHEST_PROTOCOL)),
    )
    conn.commit()
    conn.close()

    store = SqliteJobStore(db_path, allow_legacy_pickle_migration=True)
    assert store.get("legacy-ok") == record

    conn = sqlite3.connect(db_path)
    row = conn.execute("SELECT data FROM jobs WHERE id = ?", ("legacy-ok",)).fetchone()
    assert row is not None
    payload = json.loads(row[0])
    assert payload["rawBytes"]["__type__"] == "bytes"


def test_persistence_across_instances(db_path: Path) -> None:
    """Store a record, discard the instance, reopen — record should still be there.

    This is the regression for the bug where SSE mutations were lost because the
    returned dict was a deserialized copy.
    """
    store1 = SqliteJobStore(db_path)
    store1["job-9"] = {"jobId": "job-9", "exportPath": "/tmp/out.xlsx"}

    # New instance on the same file — simulates server restart
    store2 = SqliteJobStore(db_path)
    record = store2.get("job-9")
    assert record is not None
    assert record["exportPath"] == "/tmp/out.xlsx"


def test_writeback_after_mutation(db_path: Path) -> None:
    """Mutating a fetched copy does NOT persist; explicit writeback is required.

    This locks in the behavior so future refactors don't accidentally start
    returning mutable references that pretend to write through.
    """
    store = SqliteJobStore(db_path)
    store["k"] = {"status": "running"}

    record = store.get("k")
    record["status"] = "completed"  # mutate the returned copy
    # Without writeback, the stored value is unchanged
    assert store.get("k")["status"] == "running"

    # Explicit writeback persists the change
    store["k"] = record
    assert store.get("k")["status"] == "completed"


def test_delete(db_path: Path) -> None:
    store = SqliteJobStore(db_path)
    store["x"] = {"a": 1}
    assert "x" in store
    del store["x"]
    assert "x" not in store
    assert store.get("x") is None


def test_contains_rejects_non_string(db_path: Path) -> None:
    store = SqliteJobStore(db_path)
    store["s"] = {"v": 1}
    assert ("s" in store) is True
    assert (123 in store) is False  # non-string key
    assert (None in store) is False


def test_keys_order_by_updated(db_path: Path) -> None:
    store = SqliteJobStore(db_path)
    store["a"] = {"v": 1}
    store["b"] = {"v": 2}
    # "a" is now older in updated_at
    store["a"] = {"v": 3}  # bump updated_at for a
    keys = store.keys()
    assert set(keys) == {"a", "b"}
    assert keys[0] == "a"  # most-recently-updated first
