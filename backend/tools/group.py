"""group_tests tool：把 requirements 分到 Test Set。

優先使用既有 `test_set`；沒有時先嘗試 AI 分類。若 AI 不可用或結果不完整，
退回 deterministic fallback：`PDMxx` → `REQ <prefix>` → `Unassigned`。
Route 層負責 jobId 驗證。
"""

from __future__ import annotations

import re

from generator import CLASSIFICATION_MODEL, GenerationError, classify_test_sets

from .errors import ToolError
from .registry import SafetyLevel, ToolSpec, register_tool
from .schemas import GROUP_TESTS_SCHEMA


def _norm(value) -> str:
    return str(value or "").strip()


def _get_any(row: dict, *keys) -> str:
    """對 snake_case / camelCase 雙格式取值，回傳 stripped string。"""
    for key in keys:
        value = row.get(key)
        if value:
            return str(value).strip()
    return ""


def derive_test_set_name(row: dict) -> str:
    """回傳既存 test_set；沒有就回空字串。

    只讀取資料裡既有的 test_set，不自行推論。
    """
    return _get_any(row, "test_set", "testSet")


_PDM_PATTERN = re.compile(r"\b(PDM\d{2,})\b", re.IGNORECASE)


def _fallback_test_set_name(row: dict) -> str:
    """AI 失敗或漏配時的 deterministic fallback。"""
    test_item = _get_any(row, "test_item", "testItem")
    match = _PDM_PATTERN.search(test_item)
    if match:
        return match.group(1).upper()

    req_id = _get_any(row, "req_id", "reqId")
    if req_id:
        parts = [part for part in req_id.split("-") if part]
        if len(parts) >= 2:
            return f"REQ {'-'.join(parts[:-1])}"
        return f"REQ {req_id}"

    return "Unassigned"


def group_tests_tool(
    *,
    rows: list[dict],
    model: str = CLASSIFICATION_MODEL,
    force_regroup: bool = False,
) -> dict:
    """把 rows 分成若干 Test Set 並回 grouping preview。

    Args:
        rows: list of dicts，可接受 camelCase 或 snake_case key
              必要欄位：`id`、`reqId`/`req_id`、`testItem`/`test_item`
              選填欄位：`testSet`/`test_set`（若已填，預設不會重新分類）
        model: OpenAI model id（僅當有 req 需要 AI 分類時才真的呼叫）
        force_regroup: True 時，既有 testSet 會當作 AI hint，但 preview
              assignment 會使用 AI 重新分類結果；Apply 前不會改動前端 rows。

    Returns:
        `{"groups": [...], "framework": {...}, "assignments": [...]}`
        assignments 依 group 出現順序排列（對齊原 /api/group 行為）。

    AI 分類失敗時不拋錯，改走 deterministic fallback，避免 agent / API 預覽
    因外部網路不可用而整體失敗。
    """
    # Phase 1: 先分出「已有 test_set」與「需要 AI 分類」兩批。
    # force_regroup=True 時，既有 test_set 不直接沿用，而是送給 AI 當 hint。
    unresolved_reqs: dict[str, str] = {}  # req_id -> test_item
    for row in rows:
        existing = derive_test_set_name(row)
        if existing and not force_regroup:
            continue
        req_id = _get_any(row, "req_id", "reqId")
        if not req_id:
            continue
        if req_id not in unresolved_reqs:
            unresolved_reqs[req_id] = _get_any(row, "test_item", "testItem")

    classified: dict[str, str] = {}
    usage = {
        "cost": 0.0,
        "inputTokens": 0,
        "outputTokens": 0,
        "cacheCreationTokens": 0,
        "cacheReadTokens": 0,
        "model": model,
    }
    if unresolved_reqs:
        try:
            reqs = []
            for k, v in unresolved_reqs.items():
                item = {"req_id": k, "test_item": v}
                row = next((_row for _row in rows if _get_any(_row, "req_id", "reqId") == k), None)
                existing = derive_test_set_name(row or {})
                if existing and force_regroup:
                    item["current_test_set"] = existing
                reqs.append(item)
            result = classify_test_sets(reqs, model=model)
            classified = result.assignments
            usage = {
                "cost": result.cost,
                "inputTokens": result.input_tokens,
                "outputTokens": result.output_tokens,
                "cacheCreationTokens": result.cache_creation_tokens,
                "cacheReadTokens": result.cache_read_tokens,
                "model": result.model,
            }
        except GenerationError:
            classified = {}

    # Phase 2: 組 group preview
    framework: dict[str, list[str]] = {}
    row_derived: list[tuple[dict, str, str, str]] = []  # row, test_set, req_id, source
    for row in rows:
        req_id = _get_any(row, "req_id", "reqId")
        existing = derive_test_set_name(row)
        if existing and not force_regroup:
            test_set = existing
            source = "existing"
        else:
            test_set = classified.get(req_id, "") or _fallback_test_set_name(row)
            source = "derived"
        row_derived.append((row, test_set, req_id, source))
        framework.setdefault(test_set, []).append(req_id)

    groups = [
        {"testSet": test_set, "count": len(req_ids), "reqIds": req_ids}
        for test_set, req_ids in framework.items()
    ]
    groups.sort(key=lambda group: (-group["count"], group["testSet"]))

    # assignments：依 group 順序 flatten
    assignments = []
    for group in groups:
        for row, derived_set, req_id, source in row_derived:
            if derived_set != group["testSet"]:
                continue
            assignments.append(
                {
                    "id": row.get("id"),
                    "reqId": req_id,
                    "testSet": group["testSet"],
                    "source": source,
                }
            )

    return {
        "groups": groups,
        "framework": framework,
        "assignments": assignments,
        **usage,
    }


register_tool(
    ToolSpec(
        name="group_tests",
        func=group_tests_tool,
        description=GROUP_TESTS_SCHEMA["description"],
        safety=SafetyLevel.WRITE_COSTLY,  # 現在會觸發 AI 呼叫
        input_schema=GROUP_TESTS_SCHEMA,
    )
)
