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
    AGGREGATE_METRICS_SCHEMA,
    DIFF_JOBS_SCHEMA,
    ESTIMATE_COST_SCHEMA,
    GET_JOB_DETAIL_SCHEMA,
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
# get_job_detail
# ---------------------------------------------------------------------------

def _summarise_match(match_results: Any) -> dict | None:
    """從 matchResults 萃取 {total, matched, unmatched}；資料不全回 None。"""
    if not isinstance(match_results, dict):
        return None
    items = match_results.get("results")
    if not isinstance(items, list):
        return None
    matched = sum(1 for r in items if isinstance(r, dict) and r.get("matched"))
    return {"total": len(items), "matched": matched, "unmatched": len(items) - matched}


def _summarise_groups(group_results: Any) -> dict | None:
    """從 groupResults 萃取 {groupCount}；資料不全回 None。"""
    if not isinstance(group_results, dict):
        return None
    groups = group_results.get("groups")
    if not isinstance(groups, list):
        return None
    return {"groupCount": len(groups)}


def _count_generated(record: dict) -> int:
    """計算有 generated 內容的 row 數。兼容 generatedRows / parsedData.rows。"""
    sources = [record.get("generatedRows"), (record.get("parsedData") or {}).get("rows")]
    for rows in sources:
        if isinstance(rows, list):
            count = sum(
                1
                for r in rows
                if isinstance(r, dict) and r.get("generated")
            )
            if count:
                return count
    return 0


def get_job_detail_tool(*, job_id: str, job_store: Any) -> dict:
    """取得單一 job 的摘要（不含 rawBytes）。

    Returns:
        `{jobId, fileName, status, rowCount, project, testGroup, hasRawFile,
          createdAt, updatedAt, matchSummary, groupSummary, generatedRowCount,
          costUsd}`。matchSummary / groupSummary 在對應 phase 未跑時為 None。
    """
    if not job_id:
        raise ToolError("job_id is required", code="bad_request")

    record = job_store.get(job_id) if hasattr(job_store, "get") else job_store[job_id]
    if not record:
        raise ToolError(f"job not found: {job_id}", code="not_found")

    parsed = record.get("parsedData") or {}
    return {
        "jobId": record.get("jobId", job_id),
        "fileName": record.get("rawFileName") or "",
        "status": record.get("status", "unknown"),
        "rowCount": parsed.get("row_count") or record.get("totalRows") or 0,
        "project": parsed.get("project"),
        "testGroup": parsed.get("test_group"),
        "hasRawFile": bool(record.get("rawBytes")),
        "createdAt": record.get("createdAt"),
        "updatedAt": record.get("updatedAt"),
        "matchSummary": _summarise_match(record.get("matchResults")),
        "groupSummary": _summarise_groups(record.get("groupResults")),
        "generatedRowCount": _count_generated(record),
        "costUsd": record.get("costUsd"),
    }


register_tool(
    ToolSpec(
        name="get_job_detail",
        func=get_job_detail_tool,
        description=GET_JOB_DETAIL_SCHEMA["description"],
        safety=SafetyLevel.READ_ONLY,
        input_schema=GET_JOB_DETAIL_SCHEMA,
    )
)


# ---------------------------------------------------------------------------
# diff_jobs
# ---------------------------------------------------------------------------

def _delta_or_none(a: Any, b: Any) -> Any:
    """若任一端為 None/非數字，回 None；否則回 b - a。"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None
    return round(b - a, 4) if isinstance(b - a, float) else b - a


def diff_jobs_tool(*, job_a_id: str, job_b_id: str, job_store: Any) -> dict:
    """比較兩個 job 的摘要與 delta。

    Returns:
        `{"jobA": <get_job_detail shape>, "jobB": ..., "diff": {...}}`
        diff 欄位：rowCountDelta / costUsdDelta / statusChanged /
        matchedDelta / unmatchedDelta / generatedRowCountDelta。任一端缺資料
        的 delta 欄位為 None，讓 Agent 自己決定怎麼敘述。
    """
    if not job_a_id or not job_b_id:
        raise ToolError("job_a_id and job_b_id are required", code="bad_request")
    if job_a_id == job_b_id:
        raise ToolError("job_a_id and job_b_id must differ", code="bad_request")

    detail_a = get_job_detail_tool(job_id=job_a_id, job_store=job_store)
    detail_b = get_job_detail_tool(job_id=job_b_id, job_store=job_store)

    match_a = detail_a.get("matchSummary") or {}
    match_b = detail_b.get("matchSummary") or {}
    has_match_both = bool(detail_a.get("matchSummary") and detail_b.get("matchSummary"))

    diff = {
        "rowCountDelta": _delta_or_none(detail_a["rowCount"], detail_b["rowCount"]),
        "costUsdDelta": _delta_or_none(detail_a.get("costUsd"), detail_b.get("costUsd")),
        "statusChanged": detail_a["status"] != detail_b["status"],
        "matchedDelta": _delta_or_none(match_a.get("matched"), match_b.get("matched")) if has_match_both else None,
        "unmatchedDelta": _delta_or_none(match_a.get("unmatched"), match_b.get("unmatched")) if has_match_both else None,
        "generatedRowCountDelta": _delta_or_none(
            detail_a["generatedRowCount"], detail_b["generatedRowCount"]
        ),
    }

    return {"jobA": detail_a, "jobB": detail_b, "diff": diff}


register_tool(
    ToolSpec(
        name="diff_jobs",
        func=diff_jobs_tool,
        description=DIFF_JOBS_SCHEMA["description"],
        safety=SafetyLevel.READ_ONLY,
        input_schema=DIFF_JOBS_SCHEMA,
    )
)


# ---------------------------------------------------------------------------
# aggregate_metrics
# ---------------------------------------------------------------------------

def aggregate_metrics_tool(
    *,
    job_ids: list[str] | None = None,
    job_store: Any,
) -> dict:
    """跨 job 聚合指標：總 / 平均 row count、cost、match rate。

    Args:
        job_ids: 指定要納入統計的 job 列表；None 或空 → 以 job_store 全部為範圍。
        job_store: dict-like registry（dispatcher 注入）

    Returns:
        `{jobCount, totalRowCount, totalCostUsd, avgCostUsd, avgRowCount,
          matchRate, jobsWithMatch, jobsWithCost}`。無資料的欄位回 None，
        避免 0 與「未知」混淆。
    """
    if job_ids:
        targets = []
        for jid in job_ids:
            detail = get_job_detail_tool(job_id=jid, job_store=job_store)
            targets.append(detail)
    else:
        keys_fn = getattr(job_store, "keys", None)
        all_ids = list(keys_fn()) if callable(keys_fn) else list(job_store)
        targets = [
            get_job_detail_tool(job_id=jid, job_store=job_store) for jid in all_ids
        ]

    job_count = len(targets)
    total_row = sum(int(t.get("rowCount") or 0) for t in targets)

    costs = [t["costUsd"] for t in targets if isinstance(t.get("costUsd"), (int, float))]
    total_cost = round(sum(costs), 4) if costs else None
    avg_cost = round(total_cost / len(costs), 4) if costs else None

    avg_row = (total_row / job_count) if job_count else None

    # Match rate：只納入真的有跑過 match 的 job
    match_totals = [
        t["matchSummary"] for t in targets if isinstance(t.get("matchSummary"), dict)
    ]
    if match_totals:
        matched = sum(int(m.get("matched") or 0) for m in match_totals)
        total_match = sum(int(m.get("total") or 0) for m in match_totals)
        match_rate = (matched / total_match) if total_match else None
    else:
        match_rate = None

    return {
        "jobCount": job_count,
        "totalRowCount": total_row,
        "totalCostUsd": total_cost,
        "avgCostUsd": avg_cost,
        "avgRowCount": avg_row,
        "matchRate": match_rate,
        "jobsWithCost": len(costs),
        "jobsWithMatch": len(match_totals),
    }


register_tool(
    ToolSpec(
        name="aggregate_metrics",
        func=aggregate_metrics_tool,
        description=AGGREGATE_METRICS_SCHEMA["description"],
        safety=SafetyLevel.READ_ONLY,
        input_schema=AGGREGATE_METRICS_SCHEMA,
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
    rewrite = generated.get("tcTitle") or ""
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
