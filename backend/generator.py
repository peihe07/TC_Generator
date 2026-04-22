"""TC generator — AI call, response parsing, cost tracking.

後端 LLM：OpenAI（GPT-4.1 / GPT-5 系列）。OpenAI 自動對 ≥1024 tokens 的重複
prefix 提供 50% input cache discount，usage 透過 `prompt_tokens_details.cached_tokens`
回報，不需手動標記 cache_control。
"""
import json
import os
import re
from dataclasses import dataclass, field
from importlib import import_module
from importlib.metadata import PackageNotFoundError
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from openai import OpenAI

from prompt_builder import (
    build_system_blocks,
    build_user_prompt,
    build_batch_prompt,
    build_quick_generate_prompt,
    build_decompose_prompt,
    build_multi_tc_user_prompt,
    build_multi_tc_batch_prompt,
    build_test_set_classification_prompt,
    REQUIRED_OUTPUT_KEYS,
)

# OpenAI pricing per million tokens (USD). 來源：https://openai.com/api/pricing
# 僅列出本 app 會選用的幾個；若 model 不在表內會以 DEFAULT_MODEL 的價格推估。
MODEL_PRICING = {
    "gpt-5":           {"input": 5.00,  "output": 15.00},
    "gpt-5-mini":      {"input": 0.25,  "output": 2.00},
    "gpt-4.1":         {"input": 2.00,  "output": 8.00},
    "gpt-4.1-mini":    {"input": 0.40,  "output": 1.60},
    "gpt-4o":          {"input": 2.50,  "output": 10.00},
    "gpt-4o-mini":     {"input": 0.15,  "output": 0.60},
}

DEFAULT_MODEL = "gpt-4.1"

# 當同一 model 重試後仍違反 1:1 時，升級到下列 model 再試一次。
# 值為 None 代表已是最高層級、不再升級。
MODEL_ESCALATION = {
    "gpt-4o-mini":  "gpt-4o",
    "gpt-4.1-mini": "gpt-4.1",
    "gpt-5-mini":   "gpt-5",
    "gpt-4o":       "gpt-4.1",
    "gpt-4.1":      "gpt-5",
    "gpt-5":        None,
}


class GenerationError(Exception):
    """Raised when TC generation fails."""


@dataclass
class GenerationResult:
    """Result of a TC generation call."""
    tc_data: dict | list[dict]
    input_tokens: int = 0
    output_tokens: int = 0
    cache_creation_tokens: int = 0
    cache_read_tokens: int = 0
    cost: float = 0.0
    model: str = ""
    # Multi-TC 路徑會填入：split_meta[i] = {"req_id", "reasoning", "keywords"}
    # 與 tc_data（outer list for batch, 或 single list for per-row）對齊。
    # Legacy 路徑為空 list。
    split_meta: list[dict] = field(default_factory=list)


def _strip_fences(text: str) -> str:
    """Strip markdown code fences from text."""
    match = re.search(r"```(?:json)?\s*\n?(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else text.strip()


_LIST_FIELDS = {"pre_conditions", "test_procedure", "expected_result", "input_test_data"}


_PREFIX_NUM = re.compile(r"^\s*\d+[\.\)、]\s*")


def _normalize_tc_dict(data: dict) -> dict:
    """把 LLM 有時回傳的陣列欄位轉為編號字串，避免下游驗證器 crash。

    若 item 已帶有開頭號碼（如 "1.", "1)", "1、"），保留原號碼，避免雙重編號。
    """
    from validator import normalize_design_method

    for key in _LIST_FIELDS:
        val = data.get(key)
        if isinstance(val, list):
            lines = []
            for i, item in enumerate(val, 1):
                if isinstance(item, dict):
                    text = "; ".join(f"{k}: {v}" for k, v in item.items())
                else:
                    text = str(item)
                # 已經有 "N." 前綴就直接用；否則自行編號
                if _PREFIX_NUM.match(text):
                    lines.append(text.strip())
                else:
                    lines.append(f"{i}. {text.strip()}")
            data[key] = "\n".join(lines)
        elif val is None:
            data[key] = ""
    normalized_method = normalize_design_method(data.get("design_method"))
    if normalized_method:
        data["design_method"] = normalized_method
    return data


def _count_steps(text: str) -> int:
    """計算編號項目數量（同 validator 的邏輯）。"""
    if not text:
        return 0
    return len(re.findall(r"^\s*\d+[.)、]\s", text, re.MULTILINE))


def _violates_count_rule(tc: dict) -> bool:
    """檢查單一 TC 是否違反 1:1 規則（procedure 與 expected_result 項數需一致）。"""
    proc = _count_steps(tc.get("test_procedure", ""))
    er = _count_steps(tc.get("expected_result", ""))
    return proc > 0 and er > 0 and proc != er


def _hard_issues(tc: dict) -> list[str]:
    """
    只回傳「硬性、確定可修正」的違規（觸發 retry/escalation）。
    其他軟性違規（措辭模糊、動詞分類等）讓 validator warnings 在 UI 顯示即可，
    避免每筆 TC 都 retry 造成成本暴增。

    硬性檢查：
    - design_method 不在允許清單也不含關鍵字
    - priority 不是 High/Medium/Low/NA
    - test_item_rewrite 空白
    """
    from validator import validate_design_method, validate_priority

    issues: list[str] = []

    dm = validate_design_method(tc.get("design_method", ""))
    if not dm.passed:
        issues.append(f"- design_method: {dm.message}")

    pri = validate_priority(tc.get("priority", ""))
    if not pri.passed:
        issues.append(f"- priority: {pri.message}")

    if not (tc.get("test_item_rewrite") or "").strip():
        issues.append("- test_item_rewrite: must not be empty; rewrite the requirement as (Condition → Outcome)")

    return issues


def parse_tc_response(raw: str) -> dict:
    """Parse single TC JSON response. Raises GenerationError on failure."""
    text = _strip_fences(raw)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise GenerationError(f"Failed to parse TC response: {e}") from e

    # Validate required keys
    missing = [k for k in REQUIRED_OUTPUT_KEYS if k not in data]
    if missing:
        raise GenerationError(f"TC response missing required keys: {missing}")

    return _normalize_tc_dict(data)


def parse_batch_response(raw: str, expected_count: int | None = None) -> list[dict]:
    """Parse batch TC JSON array response. Raises GenerationError on failure."""
    text = _strip_fences(raw)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise GenerationError(f"Failed to parse batch response: {e}") from e

    if not isinstance(data, list):
        raise GenerationError(f"Expected JSON array, got {type(data).__name__}")

    # Validate each item
    for i, item in enumerate(data):
        missing = [k for k in REQUIRED_OUTPUT_KEYS if k not in item]
        if missing:
            raise GenerationError(f"TC[{i}] missing required keys: {missing}")

    if expected_count is not None and len(data) != expected_count:
        raise GenerationError(
            f"Batch response count mismatch: expected {expected_count}, got {len(data)}"
        )

    return [_normalize_tc_dict(item) for item in data]


def calculate_cost(
    input_tokens: int,
    output_tokens: int,
    model: str,
    cache_creation_tokens: int = 0,
    cache_read_tokens: int = 0,
) -> float:
    """
    Calculate API cost in USD.

    OpenAI 計費：
    - 一般 input：1.0x
    - cached input：0.5x（自動折扣，對應舊 cache_read）
    - output：依模型 output 價

    cache_creation_tokens 在 OpenAI 沒有對應概念（快取自動建立、不另外計費），
    保留此參數僅為維持舊介面相容；這裡以一般 input 計算。
    """
    pricing = MODEL_PRICING.get(model, MODEL_PRICING[DEFAULT_MODEL])
    in_rate = pricing["input"] / 1_000_000
    out_rate = pricing["output"] / 1_000_000
    # OpenAI: input_tokens 已包含 cached_tokens 嗎？實際上 input_tokens 是總數、
    # 其中 cache_read_tokens 這部分可打 5 折。我們拆開算。
    uncached_input = max(input_tokens - cache_read_tokens, 0)
    return (
        uncached_input * in_rate
        + cache_read_tokens * in_rate * 0.5
        + cache_creation_tokens * in_rate  # 視同一般 input
        + output_tokens * out_rate
    )


def _usage_tokens(usage) -> dict:
    """標準化 OpenAI usage 物件為 dict；cache_read 來自 prompt_tokens_details.cached_tokens。"""
    if usage is None:
        return {"input": 0, "output": 0, "cache_creation": 0, "cache_read": 0}
    prompt_tokens = getattr(usage, "prompt_tokens", 0) or 0
    completion_tokens = getattr(usage, "completion_tokens", 0) or 0
    details = getattr(usage, "prompt_tokens_details", None)
    cached = 0
    if details is not None:
        cached = getattr(details, "cached_tokens", 0) or 0
    return {
        "input": prompt_tokens,
        "output": completion_tokens,
        "cache_creation": 0,  # OpenAI 不回報 cache write 事件
        "cache_read": cached,
    }


def _client() -> Any:
    """建立 OpenAI client。讀 OPENAI_API_KEY env var。

    `openai` 套件改為延遲載入，讓沒裝 AI 依賴的環境（例如純工具 CLI 測試）
    也能 import `generator` 而不會炸，只有真的要呼叫 API 才會要求套件存在。
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise GenerationError("OPENAI_API_KEY is not set. Add it to .env.")
    try:
        openai_module = import_module("openai")
    except (PackageNotFoundError, ImportError, ModuleNotFoundError) as exc:
        raise GenerationError(
            "openai package is not installed. Run `pip install -e \".[dev]\"` first."
        ) from exc
    return openai_module.OpenAI(api_key=api_key)


def _chat(
    system: str,
    user: str,
    model: str,
    max_tokens: int | None = None,
    json_mode: bool = True,
):
    """呼叫 OpenAI chat completions；統一錯誤處理與 JSON mode。

    `max_tokens=None` 時不傳 `max_completion_tokens`，讓 OpenAI 用 model 的預設
    上限。對於拆分 TC 不固定數量的場景特別重要，避免被截斷導致 JSON parse 失敗。
    """
    client = _client()
    kwargs: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    if max_tokens is not None:
        kwargs["max_completion_tokens"] = max_tokens
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
    try:
        return client.chat.completions.create(**kwargs)
    except Exception as e:
        raise GenerationError(f"API call failed: {e}") from e


def generate_single_tc(
    row: dict,
    context: dict,
    spec_index: dict | None,
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> GenerationResult:
    """
    Generate a single TC by calling the chat completion API.

    Raises GenerationError on API or parse failure.
    """
    system = build_system_blocks(rules_text)
    user_prompt = build_user_prompt(row, context, spec_index, rules_text="")
    response = _chat(system, user_prompt, model, max_tokens=2000)

    raw_text = response.choices[0].message.content or ""
    tc_data = parse_tc_response(raw_text)
    t = _usage_tokens(response.usage)
    used_model = model

    def _has_issues(tc: dict) -> list[str]:
        """彙整觸發 retry 的硬性違規：1:1 計數 + hard validator 檢查。"""
        issues = []
        if _violates_count_rule(tc):
            p, e = _count_steps(tc.get("test_procedure", "")), _count_steps(tc.get("expected_result", ""))
            issues.append(f"- 1:1 rule: test_procedure has {p} items but expected_result has {e} items")
        issues.extend(_hard_issues(tc))
        return issues

    issues = _has_issues(tc_data)
    if issues:
        retry_prompt = (
            user_prompt
            + "\n\nPREVIOUS ATTEMPT FAILED these checks. Regenerate to fix them:\n"
            + "\n".join(issues)
        )
        retry = _chat(system, retry_prompt, model, max_tokens=2000)
        retry_text = retry.choices[0].message.content or ""
        retry_data = parse_tc_response(retry_text)
        rt = _usage_tokens(retry.usage)
        t = {
            "input": t["input"] + rt["input"],
            "output": t["output"] + rt["output"],
            "cache_creation": t["cache_creation"] + rt["cache_creation"],
            "cache_read": t["cache_read"] + rt["cache_read"],
        }
        tc_data = retry_data

        # 同 model retry 仍違規 → 升級 model 再試一次
        remaining = _has_issues(tc_data)
        if remaining:
            escalated = MODEL_ESCALATION.get(model)
            if escalated:
                esc_prompt = (
                    user_prompt
                    + "\n\nPreviously tried twice with the same model and still failed:\n"
                    + "\n".join(remaining)
                    + "\n\nBe extra careful; correct every item above."
                )
                esc = _chat(system, esc_prompt, escalated, max_tokens=2000)
                esc_text = esc.choices[0].message.content or ""
                esc_data = parse_tc_response(esc_text)
                et = _usage_tokens(esc.usage)
                base_cost = calculate_cost(t["input"], t["output"], model, t["cache_creation"], t["cache_read"])
                esc_cost = calculate_cost(et["input"], et["output"], escalated, et["cache_creation"], et["cache_read"])
                return GenerationResult(
                    tc_data=esc_data,
                    input_tokens=t["input"] + et["input"],
                    output_tokens=t["output"] + et["output"],
                    cache_creation_tokens=t["cache_creation"] + et["cache_creation"],
                    cache_read_tokens=t["cache_read"] + et["cache_read"],
                    cost=base_cost + esc_cost,
                    model=escalated,
                )

    cost = calculate_cost(t["input"], t["output"], used_model, t["cache_creation"], t["cache_read"])

    return GenerationResult(
        tc_data=tc_data,
        input_tokens=t["input"],
        output_tokens=t["output"],
        cache_creation_tokens=t["cache_creation"],
        cache_read_tokens=t["cache_read"],
        cost=cost,
        model=used_model,
    )


@dataclass
class DecomposeResult:
    """Result of a requirement decomposition call."""
    reasoning: str
    scenarios: list[dict]
    keywords: list[dict] = field(default_factory=list)
    input_tokens: int = 0
    output_tokens: int = 0
    cost: float = 0.0


def generate_quick_tc(
    test_item: str,
    context: str | None,
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> GenerationResult:
    """
    Generate a single TC from ad-hoc input (no job context required).

    Raises GenerationError on API or parse failure.
    """
    system = build_system_blocks(rules_text)
    user_prompt = build_quick_generate_prompt(test_item, context, rules_text="")
    response = _chat(system, user_prompt, model, max_tokens=2000)

    raw_text = response.choices[0].message.content or ""
    tc_data = parse_tc_response(raw_text)
    t = _usage_tokens(response.usage)
    cost = calculate_cost(t["input"], t["output"], model, t["cache_creation"], t["cache_read"])

    return GenerationResult(
        tc_data=tc_data,
        input_tokens=t["input"],
        output_tokens=t["output"],
        cache_creation_tokens=t["cache_creation"],
        cache_read_tokens=t["cache_read"],
        cost=cost,
        model=model,
    )


def decompose_requirement(
    requirement: str,
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> DecomposeResult:
    """
    Decompose a requirement into distinct test scenarios.

    Returns structured analysis + scenario list.
    Raises GenerationError on API or parse failure.
    """
    analyst_base = "You are an ASPICE SWE.6 test analyst. Return ONLY valid JSON, no markdown fences."
    system = (
        f"## ASPICE SWE.6 Rules (authoritative — follow strictly)\n\n{rules_text}\n\n---\n\n{analyst_base}"
        if rules_text else analyst_base
    )
    user_prompt = build_decompose_prompt(requirement, rules_text="")
    response = _chat(system, user_prompt, model, max_tokens=2000)

    raw_text = response.choices[0].message.content or ""
    text = _strip_fences(raw_text)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise GenerationError(f"Failed to parse decompose response: {e}") from e

    if not isinstance(data, dict) or "scenarios" not in data:
        raise GenerationError("Decompose response missing 'scenarios' field")

    t = _usage_tokens(response.usage)
    cost = calculate_cost(t["input"], t["output"], model, t["cache_creation"], t["cache_read"])

    return DecomposeResult(
        reasoning=data.get("reasoning", ""),
        scenarios=data["scenarios"],
        keywords=data.get("keywords", []) or [],
        input_tokens=t["input"],
        output_tokens=t["output"],
        cost=cost,
    )


def generate_batch(
    rows: list[dict],
    context: dict,
    spec_index: dict | None,
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> GenerationResult:
    """
    Generate multiple TCs in a single API call.

    Raises GenerationError on API or parse failure.
    """
    system = build_system_blocks(rules_text, batch=True)
    # OpenAI json_object 模式只能回傳物件，所以我們要求 {"tcs":[...]} 的包裝
    user_prompt = (
        build_batch_prompt(rows, context, spec_index, rules_text="")
        + '\n\nReturn a JSON object with key "tcs" whose value is the array.'
    )
    response = _chat(system, user_prompt, model, max_tokens=2000 * len(rows))

    raw_text = response.choices[0].message.content or ""
    # 解包 {"tcs": [...]} → list
    try:
        wrapped = json.loads(_strip_fences(raw_text))
    except json.JSONDecodeError as e:
        raise GenerationError(f"Failed to parse batch response: {e}") from e
    if isinstance(wrapped, dict) and "tcs" in wrapped:
        array_text = json.dumps(wrapped["tcs"])
    elif isinstance(wrapped, list):
        array_text = json.dumps(wrapped)
    else:
        raise GenerationError("Batch response did not contain an array")
    tc_data = parse_batch_response(array_text, expected_count=len(rows))

    t = _usage_tokens(response.usage)
    cost = calculate_cost(t["input"], t["output"], model, t["cache_creation"], t["cache_read"])

    return GenerationResult(
        tc_data=tc_data,
        input_tokens=t["input"],
        output_tokens=t["output"],
        cache_creation_tokens=t["cache_creation"],
        cache_read_tokens=t["cache_read"],
        cost=cost,
        model=model,
    )


# ---------------------------------------------------------------------------
# Multi-TC generation (one requirement → 1..N TCs as decided by the model).
# 沒有上限：AI 依 ASPICE_SWE6 規則決定每個 req 要拆幾筆（§1.2, §1.4, §1.5 等）。
# ---------------------------------------------------------------------------


# 注意：multi-TC 路徑**不傳** `max_tokens`。拆幾筆由 AI 依 ASPICE 規則判斷，
# 任何上限都可能在「AI 想拆 20 筆」時截斷 JSON 中段造成 parse 失敗。讓 OpenAI
# 用 model 預設上限（gpt-5 64k / gpt-4.1 32768 / gpt-4o 16384）就行。


def _validate_tcs_array(tcs, *, context: str) -> list[dict]:
    """檢查陣列型 TC 回傳是否合法，回傳 normalize 後的 list。"""
    if not isinstance(tcs, list) or not tcs:
        raise GenerationError(f"{context}: expected non-empty 'tcs' array")
    for i, tc in enumerate(tcs):
        if not isinstance(tc, dict):
            raise GenerationError(f"{context}: tcs[{i}] is not an object")
        missing = [k for k in REQUIRED_OUTPUT_KEYS if k not in tc]
        if missing:
            raise GenerationError(f"{context}: tcs[{i}] missing keys: {missing}")
    return [_normalize_tc_dict(tc) for tc in tcs]


def parse_multi_tc_response(raw: str) -> tuple[list[dict], dict]:
    """Parse a `{reasoning, keywords, tcs}` JSON response.

    Returns (tcs, meta) where meta = {"reasoning": str, "keywords": list}.
    Old callers can just take [0] to keep the TC list.
    """
    text = _strip_fences(raw)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise GenerationError(f"Failed to parse multi-TC response: {e}") from e

    reasoning = ""
    keywords: list = []

    if isinstance(data, list):
        tcs = data
    elif isinstance(data, dict) and "tcs" in data:
        tcs = data["tcs"]
        reasoning = str(data.get("reasoning") or "")
        kws = data.get("keywords")
        if isinstance(kws, list):
            keywords = kws
    # 容忍 AI 只回單一 TC（退化成 1 筆）
    elif isinstance(data, dict) and all(k in data for k in REQUIRED_OUTPUT_KEYS):
        tcs = [data]
    else:
        raise GenerationError("Multi-TC response missing 'tcs' field")

    return _validate_tcs_array(tcs, context="multi_tc"), {
        "reasoning": reasoning,
        "keywords": keywords,
    }


def parse_multi_tc_batch_response(
    raw: str, expected_count: int,
) -> tuple[list[list[dict]], list[dict]]:
    """Parse `{requirements: [{req_id, reasoning, keywords, tcs}, ...]}`.

    Returns (tc_groups, meta_list). `meta_list[i]` = {"reasoning": str,
    "keywords": list, "req_id": str} aligned with input rows.
    """
    text = _strip_fences(raw)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise GenerationError(f"Failed to parse multi-TC batch response: {e}") from e

    if isinstance(data, dict) and "requirements" in data:
        reqs = data["requirements"]
    elif isinstance(data, list):
        reqs = data
    else:
        raise GenerationError("Multi-TC batch response missing 'requirements' field")

    if not isinstance(reqs, list) or len(reqs) != expected_count:
        raise GenerationError(
            f"Multi-TC batch: expected {expected_count} requirement groups, got "
            f"{len(reqs) if isinstance(reqs, list) else 'non-list'}"
        )

    tc_groups: list[list[dict]] = []
    meta_list: list[dict] = []
    for i, entry in enumerate(reqs):
        if not isinstance(entry, dict):
            raise GenerationError(f"requirements[{i}] is not an object")
        tcs = entry.get("tcs")
        tc_groups.append(_validate_tcs_array(tcs, context=f"requirements[{i}]"))
        kws = entry.get("keywords")
        meta_list.append({
            "req_id": str(entry.get("req_id") or ""),
            "reasoning": str(entry.get("reasoning") or ""),
            "keywords": kws if isinstance(kws, list) else [],
        })
    return tc_groups, meta_list


def generate_tcs_for_row(
    row: dict,
    context: dict,
    spec_index: dict | None,
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> GenerationResult:
    """Generate 1..N TCs for a single requirement. AI decides how many to split."""
    system = build_system_blocks(rules_text)
    user_prompt = build_multi_tc_user_prompt(row, context, spec_index, rules_text="")
    # 不設 max_tokens：AI 拆幾筆 TC 不固定，讓 OpenAI 用 model 預設完整上限。
    response = _chat(system, user_prompt, model)

    raw_text = response.choices[0].message.content or ""
    tcs, meta = parse_multi_tc_response(raw_text)
    meta["req_id"] = str(row.get("req_id") or row.get("reqId") or "")

    t = _usage_tokens(response.usage)
    cost = calculate_cost(t["input"], t["output"], model, t["cache_creation"], t["cache_read"])

    return GenerationResult(
        tc_data=tcs,
        input_tokens=t["input"],
        output_tokens=t["output"],
        cache_creation_tokens=t["cache_creation"],
        cache_read_tokens=t["cache_read"],
        cost=cost,
        model=model,
        split_meta=[meta],
    )


def generate_batch_multi(
    rows: list[dict],
    context: dict,
    spec_index: dict | None,
    rules_text: str,
    model: str = DEFAULT_MODEL,
) -> GenerationResult:
    """Batch variant: N requirements → list[list[TC]]（每個 req 1..N 筆）。"""
    system = build_system_blocks(rules_text, batch=True)
    user_prompt = build_multi_tc_batch_prompt(rows, context, spec_index, rules_text="")
    # 不設 max_tokens：batch 中每個 req 可能拆不同數量，讓 OpenAI 用 model 預設上限。
    response = _chat(system, user_prompt, model)

    raw_text = response.choices[0].message.content or ""
    tc_groups, meta_list = parse_multi_tc_batch_response(raw_text, expected_count=len(rows))

    t = _usage_tokens(response.usage)
    cost = calculate_cost(t["input"], t["output"], model, t["cache_creation"], t["cache_read"])

    return GenerationResult(
        tc_data=tc_groups,  # type: ignore[arg-type]
        input_tokens=t["input"],
        output_tokens=t["output"],
        cache_creation_tokens=t["cache_creation"],
        cache_read_tokens=t["cache_read"],
        cost=cost,
        model=model,
        split_meta=meta_list,
    )


# ---------------------------------------------------------------------------
# Test Set classification — 一次 AI 呼叫把整份 requirements 分到若干 Test Set。
# 不再靠硬編碼 keyword table，純 prompt 驅動。
# ---------------------------------------------------------------------------


@dataclass
class ClassificationResult:
    """Result of a test-set classification call."""
    # {req_id: test_set_label}
    assignments: dict[str, str]
    input_tokens: int = 0
    output_tokens: int = 0
    cache_creation_tokens: int = 0
    cache_read_tokens: int = 0
    cost: float = 0.0
    model: str = ""


def classify_test_sets(
    reqs: list[dict],
    model: str = DEFAULT_MODEL,
) -> ClassificationResult:
    """Classify a batch of requirements into coherent Test Sets (single AI call).

    Args:
        reqs: list of dicts, each with at least `req_id` and `test_item`.
              Deduplicate to req-level before calling (not TC-level).
        model: OpenAI model id.

    Returns:
        ClassificationResult whose `assignments[req_id]` is the AI-chosen label.

    Raises:
        GenerationError on API or parse failure.
    """
    if not reqs:
        return ClassificationResult(assignments={})

    system = (
        "You are a test architect. Your job is to group software requirements "
        "into coherent Test Sets based on what they verify. "
        "Return ONLY valid JSON, no markdown fences."
    )
    user = build_test_set_classification_prompt(reqs)
    response = _chat(system, user, model)

    raw_text = response.choices[0].message.content or ""
    text = _strip_fences(raw_text)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise GenerationError(f"Failed to parse classification response: {exc}") from exc

    items = data.get("assignments") if isinstance(data, dict) else None
    if not isinstance(items, list):
        raise GenerationError("Classification response missing 'assignments' array")

    assignments: dict[str, str] = {}
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            raise GenerationError(f"assignments[{i}] is not an object")
        rid = str(item.get("req_id") or "").strip()
        label = str(item.get("test_set") or "").strip()
        if rid and label:
            assignments[rid] = label

    t = _usage_tokens(response.usage)
    cost = calculate_cost(t["input"], t["output"], model, t["cache_creation"], t["cache_read"])
    return ClassificationResult(
        assignments=assignments,
        input_tokens=t["input"],
        output_tokens=t["output"],
        cache_creation_tokens=t["cache_creation"],
        cache_read_tokens=t["cache_read"],
        cost=cost,
        model=model,
    )
