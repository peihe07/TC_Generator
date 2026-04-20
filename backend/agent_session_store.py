"""SQLite-backed agent session store.

每個 session 保存：
- session_id：對應 trace_store 中的 session_id
- history：歷次 chat messages（OpenAI 格式）
- total_cost_usd：本 session 累計成本
- created_at / updated_at

與 trace_store 分離：session store 是「對話狀態」（可刪、可重設），
trace_store 是「稽核紀錄」（append-only）。兩者用同一 session_id 串起來。
"""

from __future__ import annotations

import json
import os
import sqlite3
import threading
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class AgentSession:
    session_id: str
    history: list[dict] = field(default_factory=list)
    total_cost_usd: float = 0.0
    created_at: float = 0.0
    updated_at: float = 0.0


class SqliteAgentSessionStore:
    """Thread-safe agent session store。"""

    def __init__(self, db_path: str | Path):
        self._path = Path(db_path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._conn = sqlite3.connect(self._path, check_same_thread=False)
        self._conn.execute(
            "CREATE TABLE IF NOT EXISTS agent_sessions ("
            "  session_id TEXT PRIMARY KEY,"
            "  history TEXT NOT NULL,"
            "  total_cost_usd REAL NOT NULL DEFAULT 0,"
            "  created_at REAL NOT NULL,"
            "  updated_at REAL NOT NULL"
            ")"
        )
        self._conn.commit()

    def create(self) -> AgentSession:
        """建立新 session，回傳含 UUID 的物件。"""
        now = time.time()
        session = AgentSession(
            session_id=str(uuid.uuid4()),
            history=[],
            created_at=now,
            updated_at=now,
        )
        self._save(session)
        return session

    def get(self, session_id: str) -> AgentSession | None:
        with self._lock:
            row = self._conn.execute(
                "SELECT session_id, history, total_cost_usd, created_at, updated_at "
                "FROM agent_sessions WHERE session_id = ?",
                (session_id,),
            ).fetchone()
        if row is None:
            return None
        return AgentSession(
            session_id=row[0],
            history=json.loads(row[1]),
            total_cost_usd=row[2],
            created_at=row[3],
            updated_at=row[4],
        )

    def get_or_create(self, session_id: str | None) -> AgentSession:
        """None 或找不到 → 建新 session；否則回傳既有。"""
        if session_id:
            existing = self.get(session_id)
            if existing is not None:
                return existing
        return self.create()

    def update(
        self,
        session_id: str,
        *,
        history: list[dict] | None = None,
        total_cost_usd: float | None = None,
    ) -> AgentSession:
        """更新 history / 成本。找不到 session 丟 KeyError。"""
        session = self.get(session_id)
        if session is None:
            raise KeyError(f"session not found: {session_id}")
        if history is not None:
            session.history = history
        if total_cost_usd is not None:
            session.total_cost_usd = total_cost_usd
        session.updated_at = time.time()
        self._save(session)
        return session

    def list_recent(self, limit: int = 20) -> list[AgentSession]:
        with self._lock:
            rows = self._conn.execute(
                "SELECT session_id, history, total_cost_usd, created_at, updated_at "
                "FROM agent_sessions ORDER BY updated_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [
            AgentSession(
                session_id=r[0],
                history=json.loads(r[1]),
                total_cost_usd=r[2],
                created_at=r[3],
                updated_at=r[4],
            )
            for r in rows
        ]

    def delete(self, session_id: str) -> bool:
        with self._lock:
            cur = self._conn.execute(
                "DELETE FROM agent_sessions WHERE session_id = ?", (session_id,)
            )
            self._conn.commit()
            return cur.rowcount > 0

    def clear_all(self) -> int:
        """Delete every session row. Returns count removed."""
        with self._lock:
            cur = self._conn.execute("DELETE FROM agent_sessions")
            self._conn.commit()
            return cur.rowcount or 0

    def purge_older_than(self, max_age_seconds: int) -> int:
        cutoff = time.time() - max_age_seconds
        with self._lock:
            cur = self._conn.execute(
                "DELETE FROM agent_sessions WHERE updated_at < ?", (cutoff,)
            )
            self._conn.commit()
            return cur.rowcount

    def close(self) -> None:
        with self._lock:
            self._conn.close()

    # ---- internal ----
    def _save(self, session: AgentSession) -> None:
        blob = json.dumps(session.history, ensure_ascii=False)
        with self._lock:
            self._conn.execute(
                "INSERT INTO agent_sessions "
                "(session_id, history, total_cost_usd, created_at, updated_at) "
                "VALUES (?, ?, ?, ?, ?) "
                "ON CONFLICT(session_id) DO UPDATE SET "
                "  history=excluded.history,"
                "  total_cost_usd=excluded.total_cost_usd,"
                "  updated_at=excluded.updated_at",
                (
                    session.session_id,
                    blob,
                    session.total_cost_usd,
                    session.created_at,
                    session.updated_at,
                ),
            )
            self._conn.commit()


def default_session_db_path() -> Path:
    """預設路徑 `output/agent_sessions.db`。`TC_AGENT_SESSION_DB` 可覆寫。"""
    base = os.environ.get("TC_AGENT_SESSION_DB")
    if base:
        return Path(base)
    return Path(__file__).resolve().parent.parent / "output" / "agent_sessions.db"
