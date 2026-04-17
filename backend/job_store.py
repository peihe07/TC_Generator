"""SQLite-backed job registry with dict-like interface.

提供與舊 in-memory `JOB_REGISTRY: dict[str, dict]` 相容的 API（__getitem__、
__setitem__、__contains__、get），讓 server 重啟後 job 不會遺失。

Job records 內含 bytes（rawBytes、specBytes 等）與巢狀結構，因此使用 pickle
序列化到單一 BLOB 欄位，而非 JSON。
"""
from __future__ import annotations

import os
import pickle
import sqlite3
import threading
from pathlib import Path


class SqliteJobStore:
    """Dict-like SQLite job registry."""

    def __init__(self, db_path: str | Path):
        self._path = Path(db_path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        # 多執行緒安全：FastAPI worker 可能跨執行緒呼叫
        self._lock = threading.RLock()
        self._conn = sqlite3.connect(self._path, check_same_thread=False)
        self._conn.execute(
            "CREATE TABLE IF NOT EXISTS jobs ("
            "  id TEXT PRIMARY KEY,"
            "  data BLOB NOT NULL,"
            "  updated_at REAL NOT NULL DEFAULT (strftime('%s','now'))"
            ")"
        )
        self._conn.commit()

    # ---- dict-like API ----
    def __setitem__(self, key: str, value: dict) -> None:
        blob = pickle.dumps(value, protocol=pickle.HIGHEST_PROTOCOL)
        with self._lock:
            self._conn.execute(
                "INSERT INTO jobs (id, data) VALUES (?, ?) "
                "ON CONFLICT(id) DO UPDATE SET data=excluded.data, updated_at=strftime('%s','now')",
                (key, blob),
            )
            self._conn.commit()

    def __getitem__(self, key: str) -> dict:
        row = self._fetch(key)
        if row is None:
            raise KeyError(key)
        return pickle.loads(row)

    def __contains__(self, key: object) -> bool:
        if not isinstance(key, str):
            return False
        return self._fetch(key) is not None

    def __delitem__(self, key: str) -> None:
        with self._lock:
            self._conn.execute("DELETE FROM jobs WHERE id = ?", (key,))
            self._conn.commit()

    def get(self, key: str, default=None):
        row = self._fetch(key)
        if row is None:
            return default
        return pickle.loads(row)

    def keys(self) -> list[str]:
        with self._lock:
            return [r[0] for r in self._conn.execute("SELECT id FROM jobs ORDER BY updated_at DESC")]

    def vacuum(self) -> None:
        """壓縮 DB 檔案大小。對小型工作集極快，頻繁的 job churn 後可用。"""
        with self._lock:
            self._conn.execute("VACUUM")
            self._conn.commit()

    def purge_older_than(self, max_age_seconds: int) -> int:
        """刪除超過 max_age_seconds 的 job 紀錄；回傳刪除筆數。"""
        with self._lock:
            cur = self._conn.execute(
                "DELETE FROM jobs WHERE updated_at < strftime('%s','now') - ?",
                (max_age_seconds,),
            )
            self._conn.commit()
            return cur.rowcount or 0

    # ---- internals ----
    def _fetch(self, key: str) -> bytes | None:
        with self._lock:
            cur = self._conn.execute("SELECT data FROM jobs WHERE id = ?", (key,))
            row = cur.fetchone()
        return row[0] if row else None


def default_db_path() -> Path:
    """預設 DB 路徑：output/jobs.db；可用 TC_JOBS_DB 覆寫。"""
    env = os.environ.get("TC_JOBS_DB")
    if env:
        return Path(env)
    return Path(__file__).resolve().parent.parent / "output" / "jobs.db"
