"""Trace replay CLI —— ASPICE SWE.6 稽核員的核心工具。

用法:
    python -m tools.replay <session_id>
    python -m tools.replay <session_id> --db /path/to/traces.db
    python -m tools.replay <session_id> --include-costly    # 重跑 WRITE_COSTLY
    python -m tools.replay <session_id> --include-destructive  # 重跑 DESTRUCTIVE

依照 trace_store 裡的 tool_call 順序重新執行每個 tool：
- 把新結果的 sha256 與原本記錄的 `result_hash` 比對
- 不一致 → 標 MISMATCH
- 預設跳過非決定性 tool（generate_tc）與破壞性 tool（write_excel）
- 只讀 / 寫入 job_store / validate 類 tool 結果應 byte-for-byte 一致
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from trace_store import SqliteTraceStore, default_trace_db_path, result_hash

from . import get_tool
from .registry import SafetyLevel


# WRITE_COSTLY / DESTRUCTIVE 預設不重跑（避免再花錢 / 覆寫檔案）
_DEFAULT_SKIP = {SafetyLevel.WRITE_COSTLY, SafetyLevel.DESTRUCTIVE}


@dataclass
class ReplayOutcome:
    index: int        # 第幾個 tool_call
    tool: str
    status: str       # "match" | "mismatch" | "skipped" | "error"
    message: str = ""
    original_hash: str | None = None
    new_hash: str | None = None


def replay_session(
    session_id: str,
    *,
    trace_db: Path | None = None,
    include_costly: bool = False,
    include_destructive: bool = False,
) -> list[ReplayOutcome]:
    """重放指定 session 的所有 tool_call，回傳結果列表。

    Args:
        session_id: 要重放的 session id
        trace_db: trace sqlite 路徑；None 用預設
        include_costly: 是否重跑 WRITE_COSTLY 的 tool（會吃 LLM token）
        include_destructive: 是否重跑 DESTRUCTIVE 的 tool（會寫檔）
    """
    store = SqliteTraceStore(trace_db or default_trace_db_path())
    try:
        events = store.replay(session_id)
    finally:
        store.close()

    if not events:
        raise SystemExit(f"No trace events found for session {session_id!r}")

    skip = set(_DEFAULT_SKIP)
    if include_costly:
        skip.discard(SafetyLevel.WRITE_COSTLY)
    if include_destructive:
        skip.discard(SafetyLevel.DESTRUCTIVE)

    # 為 tool 注入臨時依賴（replay 不共享主程式的 JOB_REGISTRY）
    job_store: dict = {}

    outcomes: list[ReplayOutcome] = []
    tool_index = 0
    for event in events:
        if event.type != "tool_call" or not event.tool:
            continue
        tool_index += 1

        try:
            spec = get_tool(event.tool)
        except KeyError:
            outcomes.append(
                ReplayOutcome(
                    index=tool_index,
                    tool=event.tool,
                    status="error",
                    message=f"tool {event.tool!r} is no longer registered",
                    original_hash=event.result_hash,
                )
            )
            continue

        if spec.safety in skip:
            outcomes.append(
                ReplayOutcome(
                    index=tool_index,
                    tool=event.tool,
                    status="skipped",
                    message=f"skipped ({spec.safety.value}); pass --include-* to run",
                    original_hash=event.result_hash,
                )
            )
            continue

        args = dict(event.args or {})
        # 注入需要的依賴（不會出現在 trace.args 裡）
        if event.tool == "parse_workbook":
            args["job_store"] = job_store

        try:
            new_result = spec.func(**args)
        except Exception as exc:  # 包含 ToolError
            outcomes.append(
                ReplayOutcome(
                    index=tool_index,
                    tool=event.tool,
                    status="error",
                    message=f"re-run raised: {exc}",
                    original_hash=event.result_hash,
                )
            )
            continue

        new_hash = result_hash(new_result)
        if event.result_hash and new_hash == event.result_hash:
            outcomes.append(
                ReplayOutcome(
                    index=tool_index,
                    tool=event.tool,
                    status="match",
                    original_hash=event.result_hash,
                    new_hash=new_hash,
                )
            )
        else:
            outcomes.append(
                ReplayOutcome(
                    index=tool_index,
                    tool=event.tool,
                    status="mismatch",
                    message="result_hash differs",
                    original_hash=event.result_hash,
                    new_hash=new_hash,
                )
            )

    return outcomes


def format_report(session_id: str, outcomes: list[ReplayOutcome]) -> str:
    """把結果格式化成 CLI 可讀的報告。"""
    lines: list[str] = []
    lines.append(f"Replay session: {session_id}")
    lines.append(f"Tool calls: {len(outcomes)}")

    counts: dict[str, int] = {}
    for o in outcomes:
        counts[o.status] = counts.get(o.status, 0) + 1
    summary = "  ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    lines.append(f"Summary: {summary or '(none)'}")
    lines.append("-" * 60)

    for o in outcomes:
        badge = {
            "match": "[OK]",
            "mismatch": "[DIFF]",
            "skipped": "[SKIP]",
            "error": "[ERR]",
        }.get(o.status, "[?]")
        line = f"{badge} #{o.index:02d} {o.tool}"
        if o.message:
            line += f" — {o.message}"
        lines.append(line)
        if o.status == "mismatch":
            lines.append(f"      original={o.original_hash}")
            lines.append(f"      current= {o.new_hash}")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="tools.replay",
        description="Replay an agent session's tool calls against current code.",
    )
    parser.add_argument("session_id")
    parser.add_argument("--db", type=Path, default=None, help="Path to traces.db")
    parser.add_argument("--include-costly", action="store_true")
    parser.add_argument("--include-destructive", action="store_true")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON instead of text report.",
    )
    args = parser.parse_args(argv)

    outcomes = replay_session(
        args.session_id,
        trace_db=args.db,
        include_costly=args.include_costly,
        include_destructive=args.include_destructive,
    )

    if args.json:
        print(json.dumps([o.__dict__ for o in outcomes], indent=2, ensure_ascii=False))
    else:
        print(format_report(args.session_id, outcomes))

    # 任何 mismatch / error 都回傳非 0 exit code，方便 CI
    bad = any(o.status in {"mismatch", "error"} for o in outcomes)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
