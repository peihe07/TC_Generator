"""SQLite-backed job registry with dict-like interface.

提供與舊 in-memory `JOB_REGISTRY: dict[str, dict]` 相容的 API（__getitem__、
__setitem__、__contains__、get），讓 server 重啟後 job 不會遺失。

Job records 內含 bytes（rawBytes、specBytes 等）與巢狀結構，因此使用
JSON + base64 marker 存入 SQLite，避免 pickle 反序列化風險。
"""
from __future__ import annotations

import base64
import binascii
import json
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
        self._migrate_legacy_pickle_rows()

    # ---- dict-like API ----
    def __setitem__(self, key: str, value: dict) -> None:
        blob = self._serialize(value)
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
        return self._deserialize(row)

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
        return self._deserialize(row)

    def keys(self) -> list[str]:
        with self._lock:
            return [r[0] for r in self._conn.execute("SELECT id FROM jobs ORDER BY updated_at DESC")]

    def vacuum(self) -> None:
        """壓縮 DB 檔案大小。對小型工作集極快，頻繁的 job churn 後可用。"""
        with self._lock:
            self._conn.execute("VACUUM")
            self._conn.commit()

    def clear_all(self) -> int:
        """Delete every job row. Returns count removed."""
        with self._lock:
            cur = self._conn.execute("DELETE FROM jobs")
            self._conn.commit()
            return cur.rowcount or 0

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

    def _migrate_legacy_pickle_rows(self) -> None:
        """Upgrade legacy pickled rows in place once, then use JSON-only reads."""
        with self._lock:
            rows = list(self._conn.execute("SELECT id, data FROM jobs"))

        migrated: list[tuple[bytes, str]] = []
        for job_id, payload in rows:
            try:
                self._deserialize(payload)
            except ValueError:
                legacy = self._try_load_legacy_pickle(payload)
                if legacy is None:
                    continue
                migrated.append((self._serialize(legacy), job_id))

        if not migrated:
            return

        with self._lock:
            self._conn.executemany(
                "UPDATE jobs SET data = ?, updated_at = strftime('%s','now') WHERE id = ?",
                migrated,
            )
            self._conn.commit()

    @classmethod
    def _serialize(cls, value: dict) -> bytes:
        return json.dumps(
            cls._encode_json_safe(value),
            ensure_ascii=True,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")

    @classmethod
    def _deserialize(cls, payload: bytes) -> dict:
        try:
            decoded = json.loads(payload.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("invalid job payload: expected UTF-8 JSON") from exc

        if not isinstance(decoded, dict):
            raise ValueError("invalid job payload: top-level record must be an object")
        return cls._decode_json_safe(decoded)

    @classmethod
    def _encode_json_safe(cls, value):
        if isinstance(value, bytes):
            return {
                "__type__": "bytes",
                "base64": base64.b64encode(value).decode("ascii"),
            }
        if isinstance(value, dict):
            return {str(k): cls._encode_json_safe(v) for k, v in value.items()}
        if isinstance(value, list):
            return [cls._encode_json_safe(item) for item in value]
        if isinstance(value, tuple):
            return {
                "__type__": "tuple",
                "items": [cls._encode_json_safe(item) for item in value],
            }
        return value

    @classmethod
    def _decode_json_safe(cls, value):
        if isinstance(value, dict):
            value_type = value.get("__type__")
            if value_type == "bytes":
                encoded = value.get("base64")
                if not isinstance(encoded, str):
                    raise ValueError("invalid job payload: malformed bytes marker")
                try:
                    return base64.b64decode(encoded.encode("ascii"), validate=True)
                except (ValueError, binascii.Error) as exc:
                    raise ValueError("invalid job payload: malformed bytes marker") from exc
            if value_type == "tuple":
                items = value.get("items")
                if not isinstance(items, list):
                    raise ValueError("invalid job payload: malformed tuple marker")
                return tuple(cls._decode_json_safe(item) for item in items)
            return {k: cls._decode_json_safe(v) for k, v in value.items()}
        if isinstance(value, list):
            return [cls._decode_json_safe(item) for item in value]
        return value

    @staticmethod
    def _try_load_legacy_pickle(payload: bytes) -> dict | None:
        try:
            decoded = pickle.loads(payload)
        except Exception:
            return None
        return decoded if isinstance(decoded, dict) else None


def default_db_path() -> Path:
    """預設 DB 路徑：output/jobs.db；可用 TC_JOBS_DB 覆寫。"""
    env = os.environ.get("TC_JOBS_DB")
    if env:
        return Path(env)
    return Path(__file__).resolve().parent.parent / "output" / "jobs.db"
