"""SQLite-backed trace store — 記錄 Agent 每個決策步驟。

為 ASPICE SWE.6 稽核可重現性提供資料源：
- 每個 tool call 記錄完整 args / result_hash / duration
- 每個 LLM response 記錄 reasoning / usage（不存 raw chunk，太雜）
- 支援 replay：依 session 順序取回事件，驗證 tool 結果 hash 一致

Schema 直接用 JSON 欄位，因為 agent trace 裡沒有像 job_store 那種大 bytes blob。
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
import threading
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable, Literal

TraceEventType = Literal["tool_call", "tool_result", "llm_response", "user_confirm", "error"]


@dataclass
class TraceEvent:
    """單一 trace 事件。"""

    session_id: str
    type: str
    ts: float = field(default_factory=time.time)
    tool: str | None = None
    args: dict | None = None
    result_hash: str | None = None
    result_preview: str | None = None
    duration_ms: int | None = None
    llm_reasoning: str | None = None
    usage: dict | None = None
    message: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


def result_hash(value: Any) -> str:
    """對 tool 結果算穩定 hash，用來 replay 比對。"""
    canonical = json.dumps(value, sort_keys=True, default=str, ensure_ascii=False)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


class SqliteTraceStore:
    """Agent trace 存取層。thread-safe、append-only。"""

    def __init__(self, db_path: str | Path):
        self._path = Path(db_path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._conn = sqlite3.connect(self._path, check_same_thread=False)
        self._conn.execute(
            "CREATE TABLE IF NOT EXISTS trace_events ("
            "  id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "  session_id TEXT NOT NULL,"
            "  ts REAL NOT NULL,"
            "  type TEXT NOT NULL,"
            "  tool TEXT,"
            "  payload TEXT NOT NULL"  # 完整 event dict as JSON
            ")"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_trace_session "
            "ON trace_events (session_id, id)"
        )
        self._conn.commit()

    # ---- write ----
    def record(self, event: TraceEvent) -> int:
        """寫入一個事件，回傳 auto-increment id。"""
        payload = json.dumps(event.to_dict(), default=str, ensure_ascii=False)
        with self._lock:
            cur = self._conn.execute(
                "INSERT INTO trace_events (session_id, ts, type, tool, payload) "
                "VALUES (?, ?, ?, ?, ?)",
                (event.session_id, event.ts, event.type, event.tool, payload),
            )
            self._conn.commit()
            return cur.lastrowid or 0

    def record_tool_call(
        self,
        session_id: str,
        tool: str,
        args: dict,
        result: Any,
        duration_ms: int,
    ) -> int:
        """便利方法：一次寫入 tool_call（含 result_hash）。"""
        event = TraceEvent(
            session_id=session_id,
            type="tool_call",
            tool=tool,
            args=args,
            result_hash=result_hash(result),
            result_preview=_preview(result),
            duration_ms=duration_ms,
        )
        return self.record(event)

    def record_llm_response(
        self,
        session_id: str,
        *,
        reasoning: str | None,
        usage: dict | None,
    ) -> int:
        event = TraceEvent(
            session_id=session_id,
            type="llm_response",
            llm_reasoning=reasoning,
            usage=usage,
        )
        return self.record(event)

    # ---- read ----
    def replay(self, session_id: str) -> list[TraceEvent]:
        """依順序取回 session 的所有事件。"""
        with self._lock:
            rows = self._conn.execute(
                "SELECT payload FROM trace_events WHERE session_id = ? ORDER BY id ASC",
                (session_id,),
            ).fetchall()
        return [_event_from_payload(r[0]) for r in rows]

    def list_sessions(self, limit: int = 50) -> list[str]:
        """最近 N 個 session id，依最後活動時間降冪。"""
        with self._lock:
            rows = self._conn.execute(
                "SELECT session_id, MAX(ts) AS last_ts "
                "FROM trace_events GROUP BY session_id "
                "ORDER BY last_ts DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [r[0] for r in rows]

    def export_jsonl(self, session_id: str) -> bytes:
        """匯出 session 的 trace 為 JSONL（稽核友善）。"""
        events = self.replay(session_id)
        lines = [
            json.dumps(e.to_dict(), default=str, ensure_ascii=False)
            for e in events
        ]
        return ("\n".join(lines) + ("\n" if lines else "")).encode("utf-8")

    def delete_session(self, session_id: str) -> int:
        """刪除單一 session 的所有事件，回傳筆數。"""
        with self._lock:
            cur = self._conn.execute(
                "DELETE FROM trace_events WHERE session_id = ?", (session_id,)
            )
            self._conn.commit()
            return cur.rowcount

    def clear_all(self) -> int:
        """Delete every trace event. Returns count removed."""
        with self._lock:
            cur = self._conn.execute("DELETE FROM trace_events")
            self._conn.commit()
            return cur.rowcount or 0

    def purge_older_than(self, max_age_seconds: int) -> int:
        """刪除超過 max_age 秒的事件。"""
        cutoff = time.time() - max_age_seconds
        with self._lock:
            cur = self._conn.execute(
                "DELETE FROM trace_events WHERE ts < ?", (cutoff,)
            )
            self._conn.commit()
            return cur.rowcount

    def close(self) -> None:
        with self._lock:
            self._conn.close()


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _preview(value: Any, limit: int = 500) -> str:
    """把 result 壓縮成一段短預覽，方便 UI/CLI 瀏覽。"""
    try:
        text = json.dumps(value, default=str, ensure_ascii=False)
    except Exception:
        text = repr(value)
    return text if len(text) <= limit else text[:limit] + "…"


def _event_from_payload(payload: str) -> TraceEvent:
    data = json.loads(payload)
    # 濾掉未知欄位，避免未來 schema 變動造成反序列化失敗
    known = {f for f in TraceEvent.__dataclass_fields__.keys()}
    return TraceEvent(**{k: v for k, v in data.items() if k in known})


def default_trace_db_path() -> Path:
    """預設 trace DB 路徑，與 jobs.db 放同一個 output 目錄。"""
    import os
    base = os.environ.get("TC_TRACE_DB")
    if base:
        return Path(base)
    return Path(__file__).resolve().parent.parent / "output" / "traces.db"
