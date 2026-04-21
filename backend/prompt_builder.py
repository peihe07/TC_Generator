"""Prompt builder for TC generation (RULES.md §12)."""
from spec_matcher import extract_pdm_codes


REQUIRED_OUTPUT_KEYS = [
    "test_item_rewrite",
    "pre_conditions",
    "input_test_data",
    "test_procedure",
    "expected_result",
    "design_method",
    "priority",
    "split_flag",
    "split_reason",
]


_SYSTEM_BASE = (
    "You are an ASPICE SWE.6 test case writer. "
    "Return ONLY valid JSON, no markdown fences."
)
_SYSTEM_BASE_BATCH = (
    "You are an ASPICE SWE.6 test case writer. "
    "Return a JSON array, one object per TC. No markdown fences."
)


def build_system_prompt() -> str:
    """純文字 system prompt（保留以利舊測試/相容）。"""
    return _SYSTEM_BASE


def build_batch_system_prompt() -> str:
    return _SYSTEM_BASE_BATCH


_HARD_CONSTRAINTS = """
## HARD CONSTRAINTS (non-negotiable; violation = failure)

1. **Every single output field MUST be written in English.** This includes
   `test_item_rewrite`, `pre_conditions`, `input_test_data`, `test_procedure`,
   `expected_result`, `design_method`, `reasoning`, and every entry inside
   `keywords` (keyword, meaning, covered_by labels). Requirements may be
   bilingual (Chinese + English); read both but produce ONLY English output.
   Proper nouns / API names / protocol names (HFP, A2DP, BLE, etc.) stay
   as-is. Do NOT emit Chinese anywhere in the response.
2. **test_item_rewrite MUST be filled** — rewrite the requirement as
   `(Condition/Trigger → Observable Outcome)`; must not be blank, must not
   copy the source verbatim.
3. **test_procedure and expected_result must have the SAME number of
   numbered items (1:1 mapping).** If procedure has N steps, expected_result
   must also have exactly N items, aligned in order.
4. **pre_conditions only describes states / environment.** Never include
   actions (no "click", "enter", "send" — those belong in test_procedure).
5. **design_method MUST be one of these 9 values (English label only):**
   Negative / Fault Injection / State Transition / Decision Table / EP / BVA
   / Combinatorial / Scenario / Functional.
6. **priority MUST be one of P0 / P1 / P2.** Mapping: P0 = highest (safety,
   core functionality, data loss risk), P1 = standard feature (user-facing
   behaviour), P2 = cosmetic / edge case. Do NOT return "High", "Medium",
   "Low", "NA", or any other value — always use exactly P0, P1, or P2.
7. All field keys are snake_case (test_item_rewrite, pre_conditions,
   input_test_data, test_procedure, expected_result, design_method,
   priority, split_flag, split_reason).
8. **Every test_procedure step MUST be a single, concrete, executable action
   with explicit target + value.** FORBIDDEN: vague verbs ("check", "verify
   the feature", "operate normally"), multiple actions glued by "and/then"
   in one step, placeholder tokens ("<some value>", "xxx", "TBD"), steps
   that only restate the expected result. REQUIRED: one action per step,
   name the exact UI element / API / signal, include the exact value / data
   used (e.g. "Send AT+BLDN with number 0912345678", not "Send a call").
9. **Every expected_result item MUST be observable and measurable** — state
   what appears on screen, what log/signal is emitted, what state changes,
   or what value is returned. No "works correctly", no "no error".
10. **input_test_data lists concrete values only** (numbers, strings, file
    names, enum values). If no data is needed, write "N/A" — never leave
    it empty and never describe actions here.
11. **Follow the ASPICE SWE.6 AI Instruction loaded above verbatim.** The
    instruction doc is authoritative. Apply the relevant sections — §2 Core
    Principles, §6 Field Rules, §7 Step Design (incl. §7.5 Final Step /
    §7.6 Baseline), §8 Expected Results, §9 False Pass/Fail, §10 Requirement
    Alignment, §11 Review Checklist — do not paraphrase, skip, or relax.
"""


_WRITING_DISCIPLINE = """
## WRITING DISCIPLINE (run this self-check BEFORE emitting each TC)

For every TC you are about to output, silently verify:
  [ ] test_item_rewrite follows `(Trigger → Observable Outcome)` and carries
      a scenario tag when the req was split (§6.1 Test Item).
  [ ] pre_conditions only describes state/environment, no actions.
  [ ] Every test_procedure step has: explicit actor, explicit action verb,
      explicit target, and (when applicable) explicit value/data.
  [ ] procedure step count == expected_result item count, aligned 1:1.
  [ ] expected_result items are observable (UI / log / API response / state).
  [ ] design_method is chosen by the 9-method decision flow, not guessed.
  [ ] priority is exactly P0 / P1 / P2.
  [ ] No Chinese leaks into any output field (繁中只允許在 reasoning / meaning).
  [ ] No cross-reference like "same as TC1"; every TC is self-contained.

If any check fails, FIX the TC before outputting. Do not emit a TC that
would fail the §11 12-item self-check in the instruction doc.
"""


def build_system_blocks(rules_text: str, batch: bool = False) -> str:
    """
    建構 system prompt（OpenAI chat completions 格式為單一字串）。
    規則放在 prefix，OpenAI 會自動對 ≥1024 tokens 重複前綴提供 50% cache 折扣。
    Hard constraints 放在最後（recency bias），強化關鍵不變量。
    """
    base = _SYSTEM_BASE_BATCH if batch else _SYSTEM_BASE
    if not rules_text:
        return f"{_HARD_CONSTRAINTS}\n{_WRITING_DISCIPLINE}\n\n---\n\n{base}"
    return (
        f"## ASPICE SWE.6 Rules (authoritative — follow strictly)\n\n{rules_text}\n\n"
        f"{_HARD_CONSTRAINTS}\n{_WRITING_DISCIPLINE}\n\n---\n\n{base}"
    )


def _get_spec_context(row: dict, spec_index: dict | None) -> str:
    """Extract relevant spec context for a single row."""
    if not spec_index:
        return "N/A"

    codes = extract_pdm_codes(row["test_item"])
    segments = []
    for code in codes:
        if code in spec_index:
            entry = spec_index[code]
            text = entry.get("full_text") or entry.get("description", "")
            if text:
                segments.append(f"[{code}] {text}")

    return "\n".join(segments) if segments else "N/A"


def build_user_prompt(
    row: dict,
    context: dict,
    spec_index: dict | None,
    rules_text: str,
) -> str:
    """Build user prompt for single TC generation."""
    spec_context = _get_spec_context(row, spec_index)
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)

    rules_section = f"\n\n## Rules\n{rules_text}" if rules_text else ""
    return f"""## Context
- Project: {context['project']}
- Test Group: {context['test_group']}
- Test Set: {context.get('test_set', 'N/A')}

## Requirement
- Requirement ID: {row.get('req_id') or row.get('reqId') or ''}
- Original Test Item: {row['test_item']}

## Spec Context
{spec_context}{rules_section}

## Output
Return JSON with keys: {output_keys}

REMINDER — run the WRITING DISCIPLINE self-check before emitting:
- test_item_rewrite rewritten (not blank, not a copy), `(Trigger → Outcome)` form.
- Each test_procedure step = one concrete action with explicit target + value;
  no vague verbs ("check", "verify"), no "and/then"-chained actions, no placeholders.
- test_procedure and expected_result have the SAME number of numbered items (1:1).
- Each expected_result item is observable (UI / log / signal / API response).
- pre_conditions = state only (no actions); input_test_data = concrete values or "N/A".
- design_method chosen by the 9-method decision flow; priority is P0 / P1 / P2.
- All output fields in English."""


def build_quick_generate_prompt(
    test_item: str,
    context: str | None,
    rules_text: str,
) -> str:
    """Build prompt for quick (ad-hoc) single TC generation."""
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)
    context_section = f"\n## Additional Context\n{context}" if context else ""
    rules_section = f"\n\n## Rules\n{rules_text}" if rules_text else ""
    return f"""## Task
Generate a single test case for the following test item. Follow all rules strictly.

## Test Item
{test_item}{context_section}{rules_section}

## Output
Return JSON with keys: {output_keys}

REMINDER — run the WRITING DISCIPLINE self-check before emitting:
- test_item_rewrite rewritten (not blank, not a copy), `(Trigger → Outcome)` form.
- Each test_procedure step = one concrete action with explicit target + value;
  no vague verbs ("check", "verify"), no "and/then"-chained actions, no placeholders.
- test_procedure and expected_result have the SAME number of numbered items (1:1).
- Each expected_result item is observable (UI / log / signal / API response).
- pre_conditions = state only (no actions); input_test_data = concrete values or "N/A".
- design_method chosen by the 9-method decision flow; priority is P0 / P1 / P2.
- All output fields in English."""


def build_decompose_prompt(requirement: str, rules_text: str) -> str:
    """Build prompt to decompose a requirement into distinct test scenarios."""
    rules_section = (
        f"\n\n## Rules (for context, these will guide TC generation after decomposition)\n{rules_text}"
        if rules_text else ""
    )
    return f"""## Task
Analyze the following software requirement following the ASPICE SWE.6 reviewer workflow:

1. Extract the key concepts ("keywords") from the requirement. For each keyword, state its meaning in this context and which scenario ids will verify it.
2. Decompose the requirement into distinct, independent test scenarios. Each scenario should cover a different aspect, condition, or behaviour path.

Every keyword must map to at least one scenario id — if a concept has no coverage, add a scenario for it.

## Language
The `meaning`, `reasoning`, `name`, and `description` fields MUST be written
in Traditional Chinese (繁體中文) so the Taiwanese reviewer can audit the
decomposition logic in their native language. Keep the `keyword` and
`test_item` fields in the source language of the requirement (do not
translate) so downstream TC generation stays consistent with the spec.

## Requirement
{requirement}{rules_section}

## Output
Return ONLY valid JSON (no markdown fences) with this exact structure:
{{
  "keywords": [
    {{
      "keyword": "<short keyword from the requirement — source language>",
      "meaning": "<此關鍵字在本需求中的意義（繁體中文）>",
      "scenarios": [1, 2]
    }}
  ],
  "reasoning": "<說明你如何識別出這些 scenario、為什麼這樣拆（繁體中文）>",
  "scenarios": [
    {{
      "id": 1,
      "name": "<簡短的 scenario 名稱（繁體中文）>",
      "description": "<這個 scenario 驗證什麼的一句話說明（繁體中文）>",
      "test_item": "<rewritten test item statement — source language>"
    }}
  ]
}}"""


def build_batch_prompt(
    rows: list[dict],
    context: dict,
    spec_index: dict | None,
    rules_text: str,
) -> str:
    """Build user prompt for batch TC generation."""
    items = []
    for i, row in enumerate(rows):
        spec_context = _get_spec_context(row, spec_index)
        items.append(
            f"### TC {i + 1}\n"
            f"- Req ID: {row.get('req_id') or row.get('reqId') or ''}\n"
            f"- Test Set: {row.get('test_set', context.get('test_set', 'N/A'))}\n"
            f"- Test Item: {row['test_item']}\n"
            f"- Spec: {spec_context}"
        )
    batch_text = "\n\n".join(items)
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)

    rules_section = f"\n\n## Rules\n{rules_text}" if rules_text else ""
    return f"""## Context
- Project: {context['project']}
- Test Group: {context['test_group']}
- Test Set: {context.get('test_set', 'N/A')}

## Requirements
{batch_text}{rules_section}

## Output
Return a JSON Array with one object per TC. Each object has keys: {output_keys}

REMINDER for every TC — run the WRITING DISCIPLINE self-check:
- test_item_rewrite rewritten (not blank, `(Trigger → Outcome)` form).
- Each test_procedure step = one concrete action with explicit target + value;
  no vague verbs, no "and/then"-chained actions, no placeholders.
- test_procedure and expected_result have the SAME count (1:1 mapping).
- Each expected_result item is observable; input_test_data = concrete values or "N/A".
- design_method from the 9-method flow; priority is P0 / P1 / P2; output is English."""


# ---------------------------------------------------------------------------
# Multi-TC prompts: AI 自行判斷一個 requirement 要拆成幾筆 TC，回傳陣列。
# 不再硬性 1 req = 1 TC，由 AI 針對不同 condition / branch / boundary 自行切分。
# ---------------------------------------------------------------------------


def _format_reviewer_hints(row: dict) -> str:
    """把 template 原本填在 J/K/L/M 欄的內容收集起來，當作 reviewer 已列出的
    拆解提示（acceptance criteria / 情境 split / 預期行為片段）丟給 AI 參考。

    使用者刻意把 criteria / RD 預期拆解放在 test_procedure 或 expected_result，
    這些是拆分 TC 時必須一起看的輸入，不是「已完成的 TC 內容」。
    """
    fields = [
        ("Pre-Conditions", row.get("pre_conditions") or row.get("preConditions")),
        ("Input Test Data", row.get("input_test_data") or row.get("inputTestData")),
        ("Test Procedure (reviewer pre-fill)", row.get("test_procedure") or row.get("testProcedure")),
        ("Expected Result (reviewer pre-fill)", row.get("expected_result") or row.get("expectedResult")),
    ]
    parts = [(label, str(val).strip()) for label, val in fields if val and str(val).strip()]
    if not parts:
        return ""
    body = "\n".join(f"### {label}\n{text}" for label, text in parts)
    return (
        "\n## Reviewer Pre-Fills (use as splitting hints, NOT as finished TCs)\n"
        "These sections were filled by the reviewer before AI generation, containing "
        "acceptance criteria / split scenarios / expected behaviour fragments. They "
        "serve as authoritative hints for how the requirement should be decomposed "
        "and what each TC must verify. Re-use the exact conditions / scenarios they "
        "describe; never ignore a scenario they listed.\n\n"
        f"{body}\n"
    )



_MULTI_TC_GUIDANCE = """
## Splitting Policy (strictly follow ASPICE SWE.6 rules loaded above)

Return as many TCs as the rules require — **no upper cap**. The number of TCs
is driven entirely by what the requirement mandates, not by an arbitrary limit.

Apply these authoritative rules from `ASPICE_SWE6_AI_Instruction.md`:

- **§6.1 Test Item** — If the requirement can be validated by more than
  one scenario, EACH distinct scenario is its own TC, and each `test_item_rewrite`
  MUST carry a parenthesised scenario tag so reviewers can tell the TCs apart
  (e.g. `(Initial Sync = 5,000)` vs `(Initial Sync > 5,000)`).
- **§10.2 Keyword-Driven Scenario Decomposition** — Identify the key concepts
  in the requirement (limits, per-device rules, order-preservation, stop
  conditions, etc.) and ensure **every keyword maps to at least one TC**.
  A concept with no TC coverage is a gap that must be closed by adding a TC.
- **§9 False Pass prevention** — When the requirement explicitly lists
  multiple supported items (file formats, device types, markets, input
  classes, etc.), produce ONE TC per item. Never combine them. e.g. supported
  video formats `.mp4 / .avi / .mpg / .wmv / .3gp / .mkv` → 6 separate TCs.
- **§10.2.1 Extended Branch Checklist** — Scan for implicit branches the
  requirement rarely states explicitly (unknown / private / withheld values,
  before-vs-after states, boundary =/>/<, negative paths, concurrency,
  persistence after reboot) and add TCs for each that the requirement covers.
- **§7.6 Baseline Comparison** — When a TC involves before/after comparison,
  that TC's procedure must establish a baseline before the change action.

Splitting decision tree:
1. Does the requirement enumerate supported items (§9)? → one TC per item.
2. Does it describe multiple distinct scenarios / conditions / boundaries?
   → one TC per scenario (§6.1).
3. Does it imply extended branches (unknown / error / negative)?
   → add TCs for each covered branch (§10.2.1, plus Design Method guide).
4. Only a single atomic behaviour with no branches? → return exactly one TC.

Additional hard constraints:
- Each TC is self-contained: its own pre-conditions, procedure, expected result.
  NEVER write "same as TC1 but…" cross-references.
- `design_method` for each TC must come from the 9 methods defined in
  `Test Case Design Method 判斷規則.md`; choose via the "快速判斷流程"
  (negative → fault → state → decision → EP → BVA → combinatorial →
  scenario → functional).
- Every TC must pass the §11 12-item self-check in the instruction doc.
"""


def build_multi_tc_user_prompt(
    row: dict,
    context: dict,
    spec_index: dict | None,
    rules_text: str,
) -> str:
    """Build user prompt for multi-TC-per-req generation (single row input)."""
    spec_context = _get_spec_context(row, spec_index)
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)

    rules_section = f"\n\n## Rules\n{rules_text}" if rules_text else ""
    hints_section = _format_reviewer_hints(row)
    return f"""## Context
- Project: {context['project']}
- Test Group: {context['test_group']}
- Test Set: {context.get('test_set', 'N/A')}

## Requirement
- Requirement ID: {row.get('req_id') or row.get('reqId') or ''}
- Original Test Item: {row['test_item']}

## Spec Context
{spec_context}{hints_section}{rules_section}
{_MULTI_TC_GUIDANCE}
## Output
Return a JSON object with these top-level keys:
- `reasoning` (string, 繁體中文): ≤3 sentences explaining WHY this requirement
  was split into N TCs, citing the rule section(s) you applied (e.g.
  「§9 列舉了 6 種支援格式，因此拆成 6 筆；每筆 test_item_rewrite 帶不同情境 tag」).
  For atomic requirements returning 1 TC, briefly state it is atomic.
- `keywords` (array, optional): keyword analysis per §10.2, each entry
  `{{"keyword": "...", "meaning": "<繁中>", "covered_by": [1, 2]}}` where the
  numbers are 1-based indices into `tcs`.
- `tcs` (array): produce as many TCs as the rules require — do not collapse
  distinct scenarios to save output. Each TC object has keys: {output_keys}

Example (requirement that enumerates 3 supported formats would return 3 TCs):
{{"reasoning": "§9 列舉 3 種格式，各一筆 TC 避免 False Pass 風險。",
  "keywords": [
    {{"keyword": "supported formats", "meaning": "系統允許的影片格式",
      "covered_by": [1, 2, 3]}}
  ],
  "tcs": [
    {{... TC for format 1 ...}},
    {{... TC for format 2 ...}},
    {{... TC for format 3 ...}}
  ]}}

REMINDER for every TC — run the WRITING DISCIPLINE self-check before emitting:
- test_item_rewrite rewritten with scenario tag (§6.1), not blank, not a copy.
- Each test_procedure step = one concrete, executable action with explicit
  target + value; no "check/verify" handwaving, no chained actions, no placeholders.
- test_procedure and expected_result have the SAME count (1:1, §8).
- Each expected_result item is observable (UI / log / signal / API response).
- pre_conditions = state only; input_test_data = concrete values or "N/A".
- design_method via the 9-method decision flow; priority is P0 / P1 / P2.
- All output fields English; must pass the §11 12-item self-check."""


def build_test_set_classification_prompt(reqs: list[dict]) -> str:
    """整份 requirements 分成若干 Test Set 的 prompt。

    Args:
        reqs: list of {"req_id", "test_item"}。去重到 req 層級，不傳 TC。

    Returns:
        User prompt 字串，AI 需回 JSON
        `{"assignments": [{"req_id": "...", "test_set": "..."}, ...]}`。
    """
    items = []
    for i, r in enumerate(reqs, 1):
        test_item = str(r.get("test_item") or "").strip().replace("\n", " ")
        if len(test_item) > 400:
            test_item = test_item[:397] + "..."
        items.append(f"{i}. [{r.get('req_id', '')}] {test_item}")
    body = "\n".join(items)

    return f"""## Task
Group the following requirements into coherent **Test Sets**. A Test Set is a
short thematic label (typically 1–3 words, English) that captures the feature
area the requirement belongs to. Examples: "BT Switch", "Device List",
"Phonebook Sync", "Permissions", "Caller ID".

Rules for choosing labels:
- Derive labels from what the requirements actually describe; do NOT invent a
  fixed taxonomy up front.
- Requirements that verify the same behavioural area MUST share the same
  Test Set label. Aim for coherent groupings of 2–10 requirements per label,
  but create a single-req Test Set if a requirement is genuinely unique.
- Prefer short noun phrases (no trailing "Testing", no "Req-xxx" placeholders,
  no generic words like "Feature" or "Function" alone).
- Every requirement must be assigned exactly one Test Set — no empty, no
  "None", no duplicates on the same req_id.

## Requirements
{body}

## Output
Return ONLY valid JSON (no markdown fences):
{{"assignments": [
  {{"req_id": "<exact id from the list>", "test_set": "<short label>"}},
  ...
]}}

The array length must equal the input count ({len(reqs)})."""


def build_multi_tc_batch_prompt(
    rows: list[dict],
    context: dict,
    spec_index: dict | None,
    rules_text: str,
) -> str:
    """Build user prompt for multi-TC batch generation (N rows → N TC arrays)."""
    items = []
    for i, row in enumerate(rows):
        spec_context = _get_spec_context(row, spec_index)
        hints = _format_reviewer_hints(row)
        item = (
            f"### Requirement {i + 1}\n"
            f"- Req ID: {row.get('req_id') or row.get('reqId') or ''}\n"
            f"- Test Set: {row.get('test_set', context.get('test_set', 'N/A'))}\n"
            f"- Test Item: {row['test_item']}\n"
            f"- Spec: {spec_context}"
        )
        if hints:
            # 縮排到同一個 Requirement 區塊裡，AI 才知道屬於哪個 req。
            item += "\n" + hints.strip()
        items.append(item)
    batch_text = "\n\n".join(items)
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)

    rules_section = f"\n\n## Rules\n{rules_text}" if rules_text else ""
    return f"""## Context
- Project: {context['project']}
- Test Group: {context['test_group']}
- Test Set: {context.get('test_set', 'N/A')}

## Requirements
{batch_text}{rules_section}
{_MULTI_TC_GUIDANCE}
## Output
Return a JSON object `{{"requirements": [...]}}`; the outer array has exactly
one entry per input requirement, in the same order. Each entry has the shape:
`{{"req_id": "...", "reasoning": "<繁中>", "keywords": [...], "tcs": [...]}}`
- `reasoning`: ≤3 sentences explaining WHY that req was split into N TCs,
  citing rule sections. For atomic reqs returning 1 TC, say so.
- `keywords` (optional): per-req keyword analysis (§10.2),
  `{{"keyword": "...", "meaning": "<繁中>", "covered_by": [1, 2]}}`.
- `tcs`: as many TC objects as the rules demand (no cap).
Each TC object has keys: {output_keys}

Example (requirement 1 enumerates 6 formats → 6 TCs; requirement 2 is atomic → 1 TC):
{{"requirements": [
  {{"req_id": "REQ-001",
    "reasoning": "§9 列出 6 種支援格式，各一筆 TC。",
    "keywords": [], "tcs": [{{...}}, {{...}}, {{...}}, {{...}}, {{...}}, {{...}}]}},
  {{"req_id": "REQ-002",
    "reasoning": "單一原子行為，不需拆分。",
    "keywords": [], "tcs": [{{...}}]}}
]}}

REMINDER for every TC — run the WRITING DISCIPLINE self-check before emitting:
- test_item_rewrite rewritten with scenario tag (§6.1), not blank, not a copy.
- Each test_procedure step = one concrete, executable action with explicit
  target + value; no "check/verify" handwaving, no chained actions, no placeholders.
- test_procedure and expected_result have the SAME count (1:1, §8).
- Each expected_result item is observable (UI / log / signal / API response).
- pre_conditions = state only; input_test_data = concrete values or "N/A".
- design_method via the 9-method decision flow; priority is P0 / P1 / P2.
- All output fields English; must pass the §11 12-item self-check."""
