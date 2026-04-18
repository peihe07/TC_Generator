"""group_tests tool：根據 Test Item / Req ID 推導 Test Set 並建立 grouping preview。

純函式，無 I/O、無 job_store 互動。Route 層負責 jobId 驗證。
"""

from __future__ import annotations

from spec_matcher import extract_pdm_codes

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
    """依序嘗試：既存 test_set → PDM code → REQ prefix → Unassigned。"""
    existing = _get_any(row, "test_set", "testSet")
    if existing:
        return existing

    codes = extract_pdm_codes(_get_any(row, "test_item", "testItem"))
    if codes:
        return codes[0]

    req_id = _get_any(row, "req_id", "reqId")
    req_parts = [part for part in req_id.split("-") if part]
    if len(req_parts) >= 2:
        return f"REQ-{req_parts[-2]}"

    return "Unassigned"


def group_tests_tool(*, rows: list[dict]) -> dict:
    """回傳 grouping preview：groups、framework、assignments。

    Args:
        rows: list of dicts，可接受 camelCase 或 snake_case key
              必要欄位：`id`、`reqId`/`req_id`、`testItem`/`test_item`
              選填欄位：`testSet`/`test_set`

    Returns:
        `{"groups": [...], "framework": {...}, "assignments": [...]}`
        assignments 依 group 出現順序排列（對齊原 /api/group 行為）。
    """
    framework: dict[str, list[str]] = {}
    # 預先計算每 row 的 test_set，避免二次呼叫
    row_derived: list[tuple[dict, str, str]] = []
    for row in rows:
        test_set = derive_test_set_name(row)
        req_id = _get_any(row, "req_id", "reqId")
        row_derived.append((row, test_set, req_id))
        framework.setdefault(test_set, []).append(req_id)

    groups = [
        {"testSet": test_set, "count": len(req_ids), "reqIds": req_ids}
        for test_set, req_ids in framework.items()
    ]
    groups.sort(key=lambda group: (-group["count"], group["testSet"]))

    # assignments：依 group 順序 flatten
    assignments = []
    for group in groups:
        for row, derived_set, req_id in row_derived:
            if derived_set != group["testSet"]:
                continue
            assignments.append(
                {
                    "id": row.get("id"),
                    "reqId": req_id,
                    "testSet": group["testSet"],
                    "source": "existing" if _get_any(row, "test_set", "testSet") else "derived",
                }
            )

    return {"groups": groups, "framework": framework, "assignments": assignments}


register_tool(
    ToolSpec(
        name="group_tests",
        func=group_tests_tool,
        description=GROUP_TESTS_SCHEMA["description"],
        safety=SafetyLevel.READ_ONLY,
        input_schema=GROUP_TESTS_SCHEMA,
    )
)
