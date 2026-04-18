"""Job 查詢類 tools：list_jobs / estimate_cost / get_job_validation。

以 `job_store`（dict-like）為資料源；dispatcher 注入。
`get_job_validation` 接 rows 直接做聚合，便於 Agent 傳入任何 row 集合。
"""

from __future__ import annotations

from typing import Any

from generator import DEFAULT_MODEL

from .errors import ToolError
from .generate import estimate_batch_cost
from .registry import SafetyLevel, ToolSpec, register_tool
from .schemas import (
    ESTIMATE_COST_SCHEMA,
    GET_JOB_VALIDATION_SCHEMA,
    LIST_JOBS_SCHEMA,
)
from .validate import validate_tc_tool


# ---------------------------------------------------------------------------
# list_jobs
# ---------------------------------------------------------------------------

def list_jobs_tool(
    *,
    status_filter: str | None = None,
    limit: int = 20,
    job_store: Any,
) -> dict:
    """列出 job_store 中最近的 job。

    Args:
        status_filter: 可選狀態過濾（如 "parsed" / "queued" / "completed"）
        limit: 最多回幾筆（按 job_store.keys() 順序，通常是新→舊）
        job_store: dict-like registry（dispatcher 注入）

    Returns:
        `{"jobs": [{jobId, fileName, status, rowCount, testGroup}], "total": N}`
    """
    if limit <= 0:
        raise ToolError("limit must be positive", code="bad_request")

    keys_fn = getattr(job_store, "keys", None)
    all_ids = list(keys_fn()) if callable(keys_fn) else list(job_store)

    jobs: list[dict] = []
    for job_id in all_ids:
        record = job_store.get(job_id) if hasattr(job_store, "get") else job_store[job_id]
        if record is None:
            continue
        status = record.get("status", "unknown")
        if status_filter and status != status_filter:
            continue

        parsed = record.get("parsedData") or {}
        jobs.append(
            {
                "jobId": record.get("jobId", job_id),
                "fileName": record.get("rawFileName") or "",
                "status": status,
                "rowCount": parsed.get("row_count") or record.get("totalRows") or 0,
                "testGroup": parsed.get("test_group"),
                "project": parsed.get("project"),
            }
        )
        if len(jobs) >= limit:
            break

    return {"jobs": jobs, "total": len(jobs)}


register_tool(
    ToolSpec(
        name="list_jobs",
        func=list_jobs_tool,
        description=LIST_JOBS_SCHEMA["description"],
        safety=SafetyLevel.READ_ONLY,
        input_schema=LIST_JOBS_SCHEMA,
    )
)


# ---------------------------------------------------------------------------
# estimate_cost
# ---------------------------------------------------------------------------

def estimate_cost_tool(
    *,
    job_id: str,
    model: str = DEFAULT_MODEL,
    batch_size: int = 5,
    job_store: Any,
) -> dict:
    """估算在指定 model / batch_size 下生成該 job 的成本。"""
    if batch_size <= 0:
        raise ToolError("batch_size must be positive", code="bad_request")

    record = job_store.get(job_id) if hasattr(job_store, "get") else job_store[job_id]
    if not record:
        raise ToolError(f"job not found: {job_id}", code="not_found")

    parsed = record.get("parsedData") or {}
    row_count = parsed.get("row_count") or record.get("totalRows") or 0
    est = estimate_batch_cost(row_count=row_count, model=model)

    return {
        "jobId": job_id,
        "rowCount": row_count,
        "model": model,
        "batchSize": batch_size,
        "estCostUsd": round(est, 4),
    }


register_tool(
    ToolSpec(
        name="estimate_cost",
        func=estimate_cost_tool,
        description=ESTIMATE_COST_SCHEMA["description"],
        safety=SafetyLevel.READ_ONLY,
        input_schema=ESTIMATE_COST_SCHEMA,
    )
)


# ---------------------------------------------------------------------------
# get_job_validation
# ---------------------------------------------------------------------------

def _coerce_row_to_tc(row: dict) -> dict | None:
    """從 frontend/API row dict 抽出 validator 要的 TC 欄位。回 None 表示無 generated 內容。"""
    generated = row.get("generated") or {}
    if not generated:
        return None

    original = row.get("originalRequirement") or row.get("original_requirement") or ""
    rewrite = generated.get("testItemRewrite") or ""
    test_item = f"{original}\n\n{rewrite}" if original else rewrite

    return {
        "tc_id": row.get("tcId") or row.get("tc_id") or "",
        "test_item": test_item,
        "pre_conditions": generated.get("preConditions") or "",
        "test_procedure": generated.get("testProcedure") or "",
        "expected_result": generated.get("expectedResult") or "",
        "design_method": generated.get("designMethod") or "",
        "priority": generated.get("priority") or "",
    }


def get_job_validation_tool(*, rows: list[dict]) -> dict:
    """對一組 row（含 generated 欄位）逐一跑 validate_tc，聚合結果。

    Returns:
        `{"total", "pass", "warnings", "errors", "perRow": [{id, tcId, hasWarnings, issues}]}`
        `errors` 目前等於 `warnings`（validator 只有 warning / passing 兩級），保留欄位給日後擴充。
    """
    per_row: list[dict] = []
    warnings = 0
    passed = 0

    for row in rows:
        tc = _coerce_row_to_tc(row)
        if tc is None:
            per_row.append(
                {
                    "id": row.get("id"),
                    "tcId": row.get("tcId") or row.get("tc_id") or "",
                    "hasWarnings": False,
                    "issues": [],
                    "skipped": True,
                    "reason": "no generated content",
                }
            )
            continue

        result = validate_tc_tool(tc=tc)
        per_row.append(
            {
                "id": row.get("id"),
                "tcId": tc["tc_id"],
                "hasWarnings": result["hasWarnings"],
                "issues": result["issues"],
            }
        )
        if result["hasWarnings"]:
            warnings += 1
        else:
            passed += 1

    return {
        "total": len(rows),
        "pass": passed,
        "warnings": warnings,
        "errors": 0,
        "perRow": per_row,
    }


register_tool(
    ToolSpec(
        name="get_job_validation",
        func=get_job_validation_tool,
        description=GET_JOB_VALIDATION_SCHEMA["description"],
        safety=SafetyLevel.READ_ONLY,
        input_schema=GET_JOB_VALIDATION_SCHEMA,
    )
)
