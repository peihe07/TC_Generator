"""group_tests tool：把 requirements 分到 Test Set.

Policy: docs/runtime/TEST_SET_POLICY.md

優先使用既有 `test_set`；沒有時先嘗試 AI 分類（per-row by `id`，failover
to `req_id`）。若 AI 不可用或結果漏配，退回 deterministic fallback；
fallback label 不應看起來像已正式分類的 requirement-code placeholder。
Route 層負責 jobId 驗證。
"""

from __future__ import annotations

import re

from generator import CLASSIFICATION_MODEL, GenerationError, classify_test_sets
from spec_matcher import extract_pdm_codes

from .errors import ToolError
from .registry import SafetyLevel, ToolSpec, register_tool
from .schemas import GROUP_TESTS_SCHEMA

_AI_CLASSIFICATION_BATCH_SIZE = 50
NEEDS_CLASSIFICATION_LABEL = "Needs Classification"
_FALLBACK_LABELS = {"unclassified", "misc", "none", NEEDS_CLASSIFICATION_LABEL.lower()}


def _norm(value) -> str:
    return str(value or "").strip()


def _is_fallback_label(value: str) -> bool:
    return _norm(value).lower() in _FALLBACK_LABELS


def _is_projection_group(test_group: str | None) -> bool:
    return _norm(test_group).lower() == "projection"


def _get_any(row: dict, *keys) -> str:
    """對 snake_case / camelCase 雙格式取值，回傳 stripped string。"""
    for key in keys:
        value = row.get(key)
        text = _norm(value)
        if text and not _is_fallback_label(text):
            return text
    return ""


def derive_test_set_name(row: dict) -> str:
    """回傳既存 test_set；沒有就回空字串。

    只讀取資料裡既有的 test_set，不自行推論。
    """
    return _get_any(row, "test_set", "testSet")


def derive_test_set_hint(row: dict) -> str:
    """回傳供 AI 參考的既有 Test Set hint，不代表已分類完成。"""
    return _get_any(
        row,
        "current_test_set",
        "currentTestSet",
        "test_set_hint",
        "testSetHint",
        "original_test_set",
        "originalTestSet",
    )


_HMI_HINT_LABELS = {
    "system reflected touchscreen hard controls": "Touchscreen & Hard Controls",
    "system leds hard controls reflect new made": "Hard Control LEDs",
}


def _shorten_test_set_label(label: str) -> str:
    text = _norm(label)
    if not text:
        return ""

    key = re.sub(r"\s+", " ", text.lower())
    if key in _HMI_HINT_LABELS:
        return _HMI_HINT_LABELS[key]

    text = re.sub(r"\bSystem\s+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+Behavior$", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text).strip()
    return text or _norm(label)


def _fallback_test_set_name(row: dict) -> str:
    """AI 失敗或漏配時的 deterministic fallback。

    保留 PDMxx 偵測（test_item 帶 PDM01 之類的就用該 code，這是可讀的真標籤）；
    其他情況回 `Needs Classification` preview placeholder，並由 assignment
    metadata 標記 needsReview，避免 placeholder 被當成正式 Test Set。
    """
    hint = derive_test_set_hint(row)
    if hint:
        return _shorten_test_set_label(hint)

    test_item = _get_any(row, "test_item", "testItem")
    lowered = test_item.lower()
    if any(term in lowered for term in ("bluetooth audio", "bt audio", "audio source")):
        return "Bluetooth Audio Management"
    if any(term in lowered for term in ("pair", "pairing", "paired")) and any(
        term in lowered for term in ("bluetooth", "bt")
    ):
        return "Bluetooth Pairing"
    if any(term in lowered for term in ("carplay", "android auto", "wireless projection", "projection")):
        if any(term in lowered for term in ("determine", "detect", "capability", "supports", "supported", "prompt")):
            return "Projection Detection"
        if any(term in lowered for term in ("launch", "start", "connect", "connected", "enable")):
            return "Projection Launch"
        return "Projection"

    codes = extract_pdm_codes(test_item)
    if codes:
        return codes[0].upper()

    return NEEDS_CLASSIFICATION_LABEL


def group_tests_tool(
    *,
    rows: list[dict],
    model: str = CLASSIFICATION_MODEL,
    force_regroup: bool = False,
    test_group: str | None = None,
) -> dict:
    """把 rows 分成若干 Test Set 並回 grouping preview。

    Args:
        rows: list of dicts，可接受 camelCase 或 snake_case key
              必要欄位：`id`、`reqId`/`req_id`、`testItem`/`test_item`
              選填欄位：`testSet`/`test_set`（若已填，預設不會重新分類）
        model: OpenAI model id（僅當有 req 需要 AI 分類時才真的呼叫）
        force_regroup: True 時，既有 testSet 會當作 AI hint，但 preview
              assignment 會使用 AI 重新分類結果；Apply 前不會改動前端 rows。
        test_group: workbook Test Group context passed to the AI prompt.

    Returns:
        `{"groups": [...], "framework": {...}, "assignments": [...]}`
        assignments 依 group 出現順序排列（對齊原 /api/group 行為）。

    AI 分類失敗時不拋錯，改走 deterministic fallback，避免 agent / API 預覽
    因外部網路不可用而整體失敗。
    """
    # Phase 1: 收集要送給 AI 分類的 row（per-row，不再以 req_id 去重）。
    # 這讓「同一 Requirement ID 對應多列且內容不同」的 case 能拿到各自的
    # Test Set，而不是被迫共用第一筆的分類結果。
    # force_regroup=True 時，既有 test_set 不直接沿用，而是送給 AI 當 hint。
    unresolved_rows: list[dict] = []
    for row in rows:
        existing = derive_test_set_name(row)
        if existing and not force_regroup:
            continue
        row_id = _get_any(row, "id")
        req_id = _get_any(row, "req_id", "reqId")
        # 必須有 id 或 req_id 之一才能送 AI；都沒有就跳過（之後走 fallback）。
        if not row_id and not req_id:
            continue
        hint = existing if force_regroup else derive_test_set_hint(row)
        item = {
            "id": row_id or req_id,  # row uuid 優先；缺則用 req_id 當 fallback key
            "req_id": req_id,
            "test_item": _get_any(row, "test_item", "testItem"),
        }
        if hint:
            item["current_test_set"] = hint
        unresolved_rows.append(item)

    classified: dict[str, str] = {}  # key = row id (or req_id when row id 缺)
    usage = {
        "cost": 0.0,
        "inputTokens": 0,
        "outputTokens": 0,
        "cacheCreationTokens": 0,
        "cacheReadTokens": 0,
        "model": model,
    }
    if unresolved_rows:
        if not _is_projection_group(test_group):
            for start in range(0, len(unresolved_rows), _AI_CLASSIFICATION_BATCH_SIZE):
                chunk = unresolved_rows[start:start + _AI_CLASSIFICATION_BATCH_SIZE]
                try:
                    result = classify_test_sets(chunk, model=model, test_group=test_group)
                except GenerationError:
                    continue
                classified.update(result.assignments)
                usage["cost"] += result.cost
                usage["inputTokens"] += result.input_tokens
                usage["outputTokens"] += result.output_tokens
                usage["cacheCreationTokens"] += result.cache_creation_tokens
                usage["cacheReadTokens"] += result.cache_read_tokens
                usage["model"] = result.model

    # Phase 2: 組 group preview
    framework: dict[str, list[str]] = {}
    row_derived: list[tuple[dict, str, str, str, bool]] = []
    for row in rows:
        row_id = _get_any(row, "id")
        req_id = _get_any(row, "req_id", "reqId")
        existing = derive_test_set_name(row)
        if existing and not force_regroup:
            test_set = existing
            source = "existing"
            needs_review = False
        else:
            # 雙重查找：先試 row_id（新 prompt 要 AI 回 id-keyed），命中失敗
            # 再退回 req_id（AI 偶爾忽略指示沿用舊 req_id-keyed 格式時的 backup）。
            # 兩者皆 miss 才走 deterministic fallback。
            ai_test_set = (
                classified.get(row_id or "", "")
                or classified.get(req_id or "", "")
            )
            if ai_test_set and not _is_fallback_label(ai_test_set):
                test_set = ai_test_set
                source = "derived"
                needs_review = False
            else:
                test_set = _fallback_test_set_name(row)
                source = "fallback"
                needs_review = _is_fallback_label(test_set)
        row_derived.append((row, test_set, req_id, source, needs_review))
        framework.setdefault(test_set, []).append(req_id)

    groups = [
        {"testSet": test_set, "count": len(req_ids), "reqIds": req_ids}
        for test_set, req_ids in framework.items()
    ]
    groups.sort(key=lambda group: (-group["count"], group["testSet"]))

    # assignments：依 group 順序 flatten
    assignments = []
    for group in groups:
        for row, derived_set, req_id, source, needs_review in row_derived:
            if derived_set != group["testSet"]:
                continue
            assignments.append(
                {
                    "id": row.get("id"),
                    "reqId": req_id,
                    "testSet": group["testSet"],
                    "source": source,
                    "needsReview": needs_review,
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
