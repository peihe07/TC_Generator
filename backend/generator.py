"""TC generator — AI call, response parsing, cost tracking.

後端 LLM：OpenAI（GPT-4.1 / GPT-5 系列）。OpenAI 對 ≥1024 tokens 的重複
prefix 會自動套用 prompt cache；cached input 依各 model 的 cached input 價格
計費，usage 透過 `prompt_tokens_details.cached_tokens` 回報。
"""
import json
import logging
import os
import random
import re
import time
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)

# 上游短暫錯誤的 retry 參數
_TRANSIENT_STATUS_CODES = {500, 502, 503, 504, 529}
_RETRY_MAX_ATTEMPTS = 3  # 首次呼叫 + 最多 2 次重試
_RETRY_BASE_DELAY = 1.0  # seconds

# 單次 OpenAI API 呼叫上限。可用 OPENAI_REQUEST_TIMEOUT_SECONDS 覆寫。
# multi-TC row 在規則/規格 context 很大時可能超過 90s；預設拉到 180s，
# 同時保留上限避免單一 request 無限卡住整個 SSE stream。
_DEFAULT_OPENAI_REQUEST_TIMEOUT_SECONDS = 180.0


def _openai_request_timeout_seconds() -> float:
    raw = os.environ.get("OPENAI_REQUEST_TIMEOUT_SECONDS")
    if not raw:
        return _DEFAULT_OPENAI_REQUEST_TIMEOUT_SECONDS
    try:
        value = float(raw)
    except ValueError:
        logger.warning(
            "Invalid OPENAI_REQUEST_TIMEOUT_SECONDS=%r; using default %.0fs.",
            raw,
            _DEFAULT_OPENAI_REQUEST_TIMEOUT_SECONDS,
        )
        return _DEFAULT_OPENAI_REQUEST_TIMEOUT_SECONDS
    if value <= 0:
        logger.warning(
            "OPENAI_REQUEST_TIMEOUT_SECONDS must be positive; using default %.0fs.",
            _DEFAULT_OPENAI_REQUEST_TIMEOUT_SECONDS,
        )
        return _DEFAULT_OPENAI_REQUEST_TIMEOUT_SECONDS
    return value


_OPENAI_REQUEST_TIMEOUT_SECONDS = _DEFAULT_OPENAI_REQUEST_TIMEOUT_SECONDS

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
    "gpt-5":           {"input": 5.00,  "cached_input": 0.50,  "output": 15.00},
    "gpt-5.4":         {"input": 2.50,  "cached_input": 0.25,  "output": 15.00},
    "gpt-5-mini":      {"input": 0.25,  "cached_input": 0.025, "output": 2.00},
    "gpt-4.1":         {"input": 2.00,  "cached_input": 0.20,  "output": 8.00},
    "gpt-4o":          {"input": 2.50,  "cached_input": 1.25,  "output": 10.00},
}

# Task-level model policy:
# - DEFAULT_MODEL: caller-selected default for decomposition / generation tasks
# - CLASSIFICATION_MODEL: fixed cheap model for Test Set grouping
DEFAULT_MODEL = "gpt-5"
CLASSIFICATION_MODEL = "gpt-5-mini"

# 當同一 model 重試後仍違反 1:1 時，升級到下列 model 再試一次。
# 值為 None 代表已是最高層級、不再升級。
MODEL_ESCALATION = {
    "gpt-5-mini":   "gpt-5",
    "gpt-4o":       "gpt-4.1",
    "gpt-4.1":      "gpt-5.4",
    "gpt-5.4":      "gpt-5",
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


def _strip_line_trailing_period(line: str) -> str:
    """移除單行末尾的句點（"." / "。"），保留行內標點。"""
    s = line.rstrip()
    while s and s[-1] in (".", "。"):
        s = s[:-1].rstrip()
    return s


def _strip_trailing_periods(text: str) -> str:
    """把多行字串裡每一行末尾的句點移除（§格式：四大欄位末段不留句點）。"""
    if not text:
        return text
    return "\n".join(_strip_line_trailing_period(line) for line in text.split("\n"))


def _normalize_tc_dict(data: dict) -> dict:
    """把 LLM 有時回傳的陣列欄位轉為編號字串，避免下游驗證器 crash。

    若 item 已帶有開頭號碼（如 "1.", "1)", "1、"），保留原號碼，避免雙重編號。
    Pre-Conditions / Input Test Data / Test Procedure / Expected Result 四欄
    末尾不留句點 — 由 `_strip_trailing_periods` 統一逐行清掉。
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
            data[key] = _strip_trailing_periods("\n".join(lines))
        elif val is None:
            data[key] = ""
        elif isinstance(val, str):
            data[key] = _strip_trailing_periods(val)
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
    - tc_title 空白
    """
    from validator import validate_design_method, validate_priority

    issues: list[str] = []

    dm = validate_design_method(tc.get("design_method", ""))
    if not dm.passed:
        issues.append(f"- design_method: {dm.message}")

    pri = validate_priority(tc.get("priority", ""))
    if not pri.passed:
        issues.append(f"- priority: {pri.message}")

    if not (tc.get("tc_title") or "").strip():
        issues.append("- tc_title: must not be empty; rewrite the requirement as Condition → Outcome")

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
    - 一般 input：依 model input 價
    - cached input：依 model cached_input 價
    - output：依 model output 價

    cache_creation_tokens 在 OpenAI 沒有對應概念（快取自動建立、不另外計費），
    保留此參數僅為維持舊介面相容；這裡以一般 input 計算。
    """
    pricing = MODEL_PRICING.get(model, MODEL_PRICING[DEFAULT_MODEL])
    in_rate = pricing["input"] / 1_000_000
    cached_in_rate = pricing["cached_input"] / 1_000_000
    out_rate = pricing["output"] / 1_000_000
    # input_tokens 為總 prompt tokens，其中 cache_read_tokens 子集以 cached rate 計價。
    uncached_input = max(input_tokens - cache_read_tokens, 0)
    return (
        uncached_input * in_rate
        + cache_read_tokens * cached_in_rate
        + cache_creation_tokens * in_rate  # 視同一般 input
        + output_tokens * out_rate
    )


def _usage_tokens(usage) -> dict:
    """標準化 `LLMUsage` 為舊版 token dict(下游成本累加沿用此形狀)。"""
    if usage is None:
        return {"input": 0, "output": 0, "cache_creation": 0, "cache_read": 0}
    return {
        "input": getattr(usage, "input_tokens", 0) or 0,
        "output": getattr(usage, "output_tokens", 0) or 0,
        "cache_creation": 0,  # provider 不回報 cache write 事件
        "cache_read": getattr(usage, "cached_input_tokens", 0) or 0,
    }


# Minimum fraction of expected headers that must match before we trust the
# extraction. Below this threshold we assume the rules doc was restructured
# (headers renamed / numbering shifted) and fall back to the full text so
# decompose quality doesn't silently degrade.
_DECOMPOSE_EXTRACT_MIN_MATCH_RATIO = 0.5


def extract_decompose_rules(rules_text: str) -> str:
    """Keep only the splitting-relevant sections for decompose.

    Goal: preserve task semantics while reducing prompt bulk for weaker/cheaper
    models. This helper is task-bound, not model-bound: every model doing the
    decompose task receives the same focused rule subset.

    Under-extraction guard: if fewer than half the expected headers match
    (doc was likely restructured), we log a warning and return the full
    rules_text instead of a mutilated subset.
    """
    if not rules_text:
        return ""

    wanted_headers = {
        "## 2. Core Principles",
        "## 4. Workflow (Generate)",
        "## 6. Field Rules",
        "## 7. Step Design",
        "## 8. Expected Results",
        "## 9. False Pass / False Fail",
        "## 10. Requirement Alignment",
        "## 11. Self-Check (before emitting each TC)",
    }
    lines = rules_text.splitlines()
    kept: list[str] = []
    matched_headers: set[str] = set()
    keep = False
    keep_parent_h2 = False
    for line in lines:
        if line.startswith("## "):
            header = line.strip()
            keep = header in wanted_headers
            keep_parent_h2 = keep
            if keep:
                matched_headers.add(header)
        elif line.startswith("### "):
            header = line.strip()
            if header in wanted_headers:
                keep = True
                matched_headers.add(header)
            else:
                keep = keep_parent_h2
        if keep:
            kept.append(line)

    match_ratio = len(matched_headers) / len(wanted_headers)
    if match_ratio < _DECOMPOSE_EXTRACT_MIN_MATCH_RATIO:
        logger.warning(
            "extract_decompose_rules matched only %d/%d expected headers "
            "(%.0f%%); falling back to full rules_text. Rules doc sections "
            "may have been renamed — update wanted_headers to restore the "
            "token-saving fast path.",
            len(matched_headers), len(wanted_headers), match_ratio * 100,
        )
        return rules_text.strip()

    return "\n".join(kept).strip()


# OpenAI client creation / retry / timeout now live in
# `providers/openai_provider.py`. generator no longer imports openai directly.

# --- LLM provider delegation (Phase 0) -----------------------------------------
# All LLM calls go through an LLMProvider. `_ACTIVE_PROVIDER` overrides the
# default (set via `set_provider`, e.g. for headless / A-B / Claude); otherwise a
# lazily-built OpenAI provider is used so behaviour matches the legacy path.
_ACTIVE_PROVIDER: Any = None
_DEFAULT_PROVIDER: Any = None


def set_provider(provider: Any) -> None:
    """Register an LLMProvider for `_chat` to use (None = default OpenAI)."""
    global _ACTIVE_PROVIDER
    _ACTIVE_PROVIDER = provider


def get_provider() -> Any:
    return _ACTIVE_PROVIDER


def _default_provider() -> Any:
    """Lazily build (and cache) the default provider.

    Backend is chosen by the single `TC_LLM_BACKEND` env var (default 'openai'),
    so swapping OpenAI->Anthropic needs no code change.
    """
    global _DEFAULT_PROVIDER
    if _DEFAULT_PROVIDER is None:
        from providers import make_provider
        backend = os.environ.get("TC_LLM_BACKEND", "openai")
        _DEFAULT_PROVIDER = make_provider(
            backend, timeout=_openai_request_timeout_seconds())
    return _DEFAULT_PROVIDER


def _chat(
    system: str,
    user: str,
    model: str,
    max_tokens: int | None = None,
    json_mode: bool = True,
):
    """呼叫 LLM chat completions(經 provider);統一錯誤處理與 JSON mode。

    預設走 OpenAI provider;`set_provider` 後改用指定 provider(headless / A-B / Claude)。
    回傳 `LLMResponse`(`.text` / `.usage` 為 `LLMUsage`)。
    `max_tokens=None` 時用 model 預設上限。
    """
    provider = _ACTIVE_PROVIDER or _default_provider()
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]
    try:
        return provider.chat(
            messages,
            model,
            max_tokens=max_tokens if max_tokens is not None else 4096,
            json_mode=json_mode,
            cache_prefix=system,
        )
    except GenerationError:
        raise
    except Exception as e:  # normalize provider/SDK errors to GenerationError
        message = str(e)
        if not message.startswith("API call failed"):
            message = f"API call failed: {message}"
        raise GenerationError(message) from e


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

    raw_text = response.text
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
        retry_text = retry.text
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
                esc_text = esc.text
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


def build_decompose_meta(results: "dict[str, DecomposeResult]") -> dict[str, int]:
    """Map req_id -> decomposition depth (scenario count) for Stage 7's
    `avg_decompose_depth` KPI. Feed the output of per-requirement decompose."""
    return {req_id: len(res.scenarios or []) for req_id, res in results.items()}


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

    raw_text = response.text
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
    domain_block: str | None = None,
) -> DecomposeResult:
    """
    Decompose a requirement into distinct test scenarios.

    `domain_block` (Stage 1 Domain Pack) grounds the decomposition so it covers
    every spec-defined branch/enumeration without inventing undefined states.
    Returns structured analysis + scenario list.
    Raises GenerationError on API or parse failure.
    """
    analyst_base = "You are an ASPICE SWE.6 test analyst. Return ONLY valid JSON, no markdown fences."
    focused_rules = extract_decompose_rules(rules_text)
    system = (
        f"## ASPICE SWE.6 Rules (authoritative — follow strictly)\n\n{focused_rules}\n\n---\n\n{analyst_base}"
        if focused_rules else analyst_base
    )
    user_prompt = build_decompose_prompt(requirement, rules_text="", domain_block=domain_block)
    response = _chat(system, user_prompt, model, max_tokens=2000)

    raw_text = response.text
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

    raw_text = response.text
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
# 用 model 預設上限即可。


_AXIS_VALUES = {"trigger_state", "input_data", "timing", "boundary", "mode", "none"}


def _normalize_distinguishing_axis(value: object) -> dict:
    """規格化 AI 回的 distinguishing_axis 物件。

    回傳 ``{"axis": str, "delta": str}``；不合法 / 缺欄一律回 ``{}``，由
    review 階段自行 fallback 顯示空值。axis 不在 enum 內時保留 raw 字串
    讓 reviewer 看見模型偷懶的字眼，但不阻擋 generation。
    """
    if not isinstance(value, dict):
        return {}
    axis = str(value.get("axis") or "").strip()
    delta = str(value.get("delta") or "").strip()
    if not axis and not delta:
        return {}
    return {"axis": axis, "delta": delta}


def _reconcile_duplicate_axis(duplicate_of: str, axis: dict) -> tuple[str, dict]:
    """確保 duplicate_of 與 distinguishing_axis 一致：兩者必須同步表態。

    Prompt 規定 ``axis="none"`` ⇔ ``duplicate_of`` 必填。AI 不一致時的 reconcile
    策略：

    - 兩者都填且 axis ≠ "none"：兩者衝突（既說重複又說有差異）→ 移除
      duplicate_of，相信 axis 給的差異描述。
    - 只填 duplicate_of：補上 ``axis="none"`` 維持對等。
    - 只填 axis="none"：清掉 axis（沒指出對哪個 sibling 不算 actionable）。

    回傳 reconcile 後的 ``(duplicate_of, axis)``。
    """
    has_dup = bool(duplicate_of)
    axis_label = (axis.get("axis") or "").strip().lower()
    is_none_axis = axis_label == "none"

    if has_dup and axis and not is_none_axis:
        # 衝突：先信 axis（差異更具描述性），把 duplicate_of 清掉。
        return "", axis
    if has_dup and not axis:
        return duplicate_of, {"axis": "none", "delta": ""}
    if is_none_axis and not has_dup:
        # axis="none" 但沒指出哪一個 sibling → 清掉 axis 視同未判定。
        return "", {}
    return duplicate_of, axis


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
    duplicate_of = ""
    distinguishing_axis: dict = {}

    if isinstance(data, list):
        tcs = data
    elif isinstance(data, dict) and "tcs" in data:
        tcs = data["tcs"]
        reasoning = str(data.get("reasoning") or "")
        kws = data.get("keywords")
        if isinstance(kws, list):
            keywords = kws
        duplicate_of = str(data.get("duplicate_of") or "").strip()
        distinguishing_axis = _normalize_distinguishing_axis(data.get("distinguishing_axis"))
    # 容忍 AI 只回單一 TC（退化成 1 筆）
    elif isinstance(data, dict) and all(k in data for k in REQUIRED_OUTPUT_KEYS):
        tcs = [data]
    else:
        raise GenerationError("Multi-TC response missing 'tcs' field")

    duplicate_of, distinguishing_axis = _reconcile_duplicate_axis(
        duplicate_of, distinguishing_axis,
    )
    return _validate_tcs_array(tcs, context="multi_tc"), {
        "reasoning": reasoning,
        "keywords": keywords,
        "duplicate_of": duplicate_of,
        "distinguishing_axis": distinguishing_axis,
    }


def parse_multi_tc_batch_response(
    raw: str, expected_count: int,
) -> tuple[list[list[dict]], list[dict]]:
    """Parse `{requirements: [{req_id, reasoning, keywords, tcs}, ...]}`.

    Returns (tc_groups, meta_list). `meta_list[i]` = {"reasoning": str,
    "keywords": list, "req_id": str} aligned with input rows.
    """
    tc_groups, meta_list, invalid_indices = _parse_multi_tc_batch_response_lenient(
        raw,
        expected_count=expected_count,
    )
    if invalid_indices:
        i = invalid_indices[0]
        error = meta_list[i].get("error") or "invalid 'tcs' array"
        raise GenerationError(f"requirements[{i}]: {error}")
    return tc_groups, meta_list


def _parse_multi_tc_batch_response_lenient(
    raw: str, expected_count: int,
) -> tuple[list[list[dict]], list[dict], list[int]]:
    """Parse a batch response and mark per-requirement TC validation failures.

    Count/shape errors are still fatal because they break alignment. Per-row
    `tcs` errors can be recovered by regenerating only the affected row.
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
    invalid_indices: list[int] = []
    for i, entry in enumerate(reqs):
        if not isinstance(entry, dict):
            raise GenerationError(f"requirements[{i}] is not an object")
        tcs = entry.get("tcs")
        error = ""
        try:
            tc_groups.append(_validate_tcs_array(tcs, context=f"requirements[{i}]"))
        except GenerationError as exc:
            tc_groups.append([])
            invalid_indices.append(i)
            prefix = f"requirements[{i}]: "
            error = str(exc)
            if error.startswith(prefix):
                error = error[len(prefix):]
        kws = entry.get("keywords")
        dup_of, axis = _reconcile_duplicate_axis(
            str(entry.get("duplicate_of") or "").strip(),
            _normalize_distinguishing_axis(entry.get("distinguishing_axis")),
        )
        meta_list.append({
            "req_id": str(entry.get("req_id") or ""),
            "reasoning": str(entry.get("reasoning") or ""),
            "keywords": kws if isinstance(kws, list) else [],
            "duplicate_of": dup_of,
            "distinguishing_axis": axis,
            "error": error,
        })
    return tc_groups, meta_list, invalid_indices


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

    raw_text = response.text
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


def _generate_rows_individually(
    rows: list[dict],
    context: dict,
    spec_index: dict | None,
    rules_text: str,
    model: str,
    base_tokens: tuple[int, int, int, int] = (0, 0, 0, 0),
    base_cost: float = 0.0,
) -> GenerationResult:
    """對每個 row 逐筆呼叫 `generate_tcs_for_row` 並彙總成一個 batch 結果。

    當批次回應無法和輸入對齊（數量/結構不符）時的 fallback：逐筆生成保證
    每個 req 都能獨立產出。`base_tokens` / `base_cost` 用來把先前失敗批次
    已耗用的用量算進來，避免漏計成本。
    """
    tc_groups: list[list[dict]] = []
    meta_list: list[dict] = []
    input_tokens, output_tokens, cache_creation_tokens, cache_read_tokens = base_tokens
    cost = base_cost

    for row in rows:
        result = generate_tcs_for_row(
            row=row,
            context=context,
            spec_index=spec_index,
            rules_text=rules_text,
            model=model,
        )
        tcs = result.tc_data if isinstance(result.tc_data, list) else [result.tc_data]
        tc_groups.append(tcs)
        if result.split_meta:
            meta_list.append(result.split_meta[0])
        else:
            meta_list.append({
                "req_id": str(row.get("req_id") or row.get("reqId") or ""),
                "reasoning": "Batch response could not be aligned; regenerated this requirement individually.",
                "keywords": [],
            })
        input_tokens += result.input_tokens
        output_tokens += result.output_tokens
        cache_creation_tokens += result.cache_creation_tokens
        cache_read_tokens += result.cache_read_tokens
        cost += result.cost

    return GenerationResult(
        tc_data=tc_groups,  # type: ignore[arg-type]
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        cache_creation_tokens=cache_creation_tokens,
        cache_read_tokens=cache_read_tokens,
        cost=cost,
        model=model,
        split_meta=meta_list,
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

    raw_text = response.text
    t = _usage_tokens(response.usage)
    cost = calculate_cost(t["input"], t["output"], model, t["cache_creation"], t["cache_read"])
    input_tokens = t["input"]
    output_tokens = t["output"]
    cache_creation_tokens = t["cache_creation"]
    cache_read_tokens = t["cache_read"]

    try:
        tc_groups, meta_list, invalid_indices = _parse_multi_tc_batch_response_lenient(
            raw_text,
            expected_count=len(rows),
        )
    except GenerationError as exc:
        # 群組數量/結構無法和輸入對齊（模型把多個 req 合併或漏掉）時無法逐欄救援，
        # 改成整批逐筆生成，並把這次失敗批次已耗用的 token/cost 一併帶入。
        logger.warning(
            "Batch response unalignable (%s); falling back to per-row generation for %d rows.",
            exc, len(rows),
        )
        return _generate_rows_individually(
            rows,
            context,
            spec_index,
            rules_text,
            model,
            base_tokens=(input_tokens, output_tokens, cache_creation_tokens, cache_read_tokens),
            base_cost=cost,
        )

    for i in invalid_indices:
        fallback = generate_tcs_for_row(
            row=rows[i],
            context=context,
            spec_index=spec_index,
            rules_text=rules_text,
            model=model,
        )
        fallback_tcs = fallback.tc_data if isinstance(fallback.tc_data, list) else [fallback.tc_data]
        tc_groups[i] = fallback_tcs
        if fallback.split_meta:
            meta_list[i] = fallback.split_meta[0]
        else:
            meta_list[i] = {
                "req_id": str(rows[i].get("req_id") or rows[i].get("reqId") or ""),
                "reasoning": "Batch response invalid; regenerated this requirement individually.",
                "keywords": [],
            }
        input_tokens += fallback.input_tokens
        output_tokens += fallback.output_tokens
        cache_creation_tokens += fallback.cache_creation_tokens
        cache_read_tokens += fallback.cache_read_tokens
        cost += fallback.cost

    return GenerationResult(
        tc_data=tc_groups,  # type: ignore[arg-type]
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        cache_creation_tokens=cache_creation_tokens,
        cache_read_tokens=cache_read_tokens,
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
    model: str = CLASSIFICATION_MODEL,
    test_group: str | None = None,
) -> ClassificationResult:
    """Classify a batch of requirements/rows into coherent Test Sets (single AI call).

    Args:
        reqs: list of dicts; each item must carry **either** an `id`
              (row-level UUID, preferred — pass this when the same req_id
              may map to multiple rows whose contents differ) or a `req_id`
              (used as fallback identifier when `id` is absent). Plus
              `test_item` for the actual classification text.
        model: OpenAI model id.

    Returns:
        ClassificationResult whose `assignments[<id-or-req_id>]` is the
        AI-chosen label. The key matches whichever identifier the caller
        supplied — use `id` when you need per-row classification, `req_id`
        when intentionally deduplicating at requirement level.

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
    user = build_test_set_classification_prompt(reqs, test_group=test_group)
    response = _chat(system, user, model)

    raw_text = response.text
    text = _strip_fences(raw_text)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise GenerationError(f"Failed to parse classification response: {exc}") from exc

    assignments: dict[str, str] = {}
    items = data.get("assignments") if isinstance(data, dict) else None
    if isinstance(items, list):
        for i, item in enumerate(items):
            if not isinstance(item, dict):
                raise GenerationError(f"assignments[{i}] is not an object")
            # Accept either "id" (new per-row key) or legacy "req_id" — whichever
            # the AI returns, mirroring whatever was supplied in the prompt.
            key = str(item.get("id") or item.get("req_id") or item.get("row_id") or "").strip()
            label = str(item.get("test_set") or item.get("testSet") or "").strip()
            if key and label:
                assignments[key] = label
    elif isinstance(data, dict):
        # Backward-compatible parser for the older prompt shape:
        # {"Test Set Name": ["row-1", "row-2"]}. Some models still return this
        # after seeing the words "mapping" or older cached context.
        metadata_keys = {"inputTokens", "outputTokens", "cost", "model"}
        for label, ids in data.items():
            if label in metadata_keys or label == "assignments" or not isinstance(ids, list):
                continue
            label = str(label or "").strip()
            if not label:
                continue
            for key in ids:
                key = str(key or "").strip()
                if key:
                    assignments[key] = label
    else:
        raise GenerationError("Classification response must be a JSON object")

    if not assignments:
        raise GenerationError("Classification response contained no usable assignments")

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
