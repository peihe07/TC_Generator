"""TC generator — AI call, response parsing, cost tracking.

後端 LLM：OpenAI（GPT-4.1 / GPT-5 系列）。OpenAI 自動對 ≥1024 tokens 的重複
prefix 提供 50% input cache discount，usage 透過 `prompt_tokens_details.cached_tokens`
回報，不需手動標記 cache_control。
"""
import json
import os
import re
from dataclasses import dataclass, field

from openai import OpenAI

from prompt_builder import (
    build_system_blocks,
    build_user_prompt,
    build_batch_prompt,
    build_quick_generate_prompt,
    build_decompose_prompt,
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
MAX_RETRIES = 2

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


def _client() -> OpenAI:
    """建立 OpenAI client。讀 OPENAI_API_KEY env var。"""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise GenerationError("OPENAI_API_KEY is not set. Add it to .env.")
    return OpenAI(api_key=api_key)


def _chat(system: str, user: str, model: str, max_tokens: int, json_mode: bool = True):
    """呼叫 OpenAI chat completions；統一錯誤處理與 JSON mode。"""
    client = _client()
    kwargs: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "max_completion_tokens": max_tokens,
    }
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

    # 1:1 count 違規 → 重試一次（同 model），附上具體提示
    if _violates_count_rule(tc_data):
        proc_n = _count_steps(tc_data.get("test_procedure", ""))
        er_n = _count_steps(tc_data.get("expected_result", ""))
        retry_prompt = (
            user_prompt
            + f"\n\nPREVIOUS ATTEMPT FAILED the 1:1 rule: test_procedure had {proc_n} items but "
              f"expected_result had {er_n} items. Regenerate with EXACTLY the same number of "
              "numbered items in test_procedure and expected_result."
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
        if _violates_count_rule(tc_data):
            escalated = MODEL_ESCALATION.get(model)
            if escalated:
                esc_prompt = (
                    user_prompt
                    + "\n\nPreviously tried twice with the same model and still produced "
                      "mismatched counts. Pay extra attention to the 1:1 rule. "
                      "Generate test_procedure and expected_result with EQUAL numbered items."
                )
                esc = _chat(system, esc_prompt, escalated, max_tokens=2000)
                esc_text = esc.choices[0].message.content or ""
                esc_data = parse_tc_response(esc_text)
                et = _usage_tokens(esc.usage)
                # 分兩段計費：舊 model + escalated model
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
