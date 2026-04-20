"""group_tests tool：把 requirements 分到 Test Set 的 AI 驅動工具。

完全沒有硬編碼 keyword / 分類表：所有沒帶 test_set 的 row 會一次送給 AI
分類（`generator.classify_test_sets`）。Route 層負責 jobId 驗證。
"""

from __future__ import annotations

from generator import DEFAULT_MODEL, GenerationError, classify_test_sets

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

    以前這裡會走 keyword/PDM 硬編碼 fallback，現在 fallback 由 AI 在
    `classify_test_sets` 一次處理整批 req，所以單列層級不再猜測。
    """
    return _get_any(row, "test_set", "testSet")


def group_tests_tool(
    *,
    rows: list[dict],
    model: str = DEFAULT_MODEL,
) -> dict:
    """把 rows 分成若干 Test Set 並回 grouping preview。

    Args:
        rows: list of dicts，可接受 camelCase 或 snake_case key
              必要欄位：`id`、`reqId`/`req_id`、`testItem`/`test_item`
              選填欄位：`testSet`/`test_set`（若已填，不會重新分類）
        model: OpenAI model id（僅當有 req 需要 AI 分類時才真的呼叫）

    Returns:
        `{"groups": [...], "framework": {...}, "assignments": [...]}`
        assignments 依 group 出現順序排列（對齊原 /api/group 行為）。

    Raises:
        ToolError: AI 分類失敗（network / parse error）。
    """
    # Phase 1: 先分出「已有 test_set」與「需要 AI 分類」兩批
    unresolved_reqs: dict[str, str] = {}  # req_id -> test_item
    for row in rows:
        if derive_test_set_name(row):
            continue
        req_id = _get_any(row, "req_id", "reqId")
        if not req_id:
            continue
        if req_id not in unresolved_reqs:
            unresolved_reqs[req_id] = _get_any(row, "test_item", "testItem")

    classified: dict[str, str] = {}
    if unresolved_reqs:
        try:
            result = classify_test_sets(
                [{"req_id": k, "test_item": v} for k, v in unresolved_reqs.items()],
                model=model,
            )
        except GenerationError as exc:
            raise ToolError(
                f"test-set classification failed: {exc}", code="internal",
            ) from exc
        classified = result.assignments

    # Phase 2: 組 group preview
    framework: dict[str, list[str]] = {}
    row_derived: list[tuple[dict, str, str, str]] = []  # row, test_set, req_id, source
    for row in rows:
        req_id = _get_any(row, "req_id", "reqId")
        existing = derive_test_set_name(row)
        if existing:
            test_set = existing
            source = "existing"
        else:
            test_set = classified.get(req_id, "")
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

    return {"groups": groups, "framework": framework, "assignments": assignments}


register_tool(
    ToolSpec(
        name="group_tests",
        func=group_tests_tool,
        description=GROUP_TESTS_SCHEMA["description"],
        safety=SafetyLevel.WRITE_COSTLY,  # 現在會觸發 AI 呼叫
        input_schema=GROUP_TESTS_SCHEMA,
    )
)
