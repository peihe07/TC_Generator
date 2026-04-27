# TC Auto-Generation Tool — RULES.md

> **⚠️ DEPRECATED (2026-04-22).** This document is no longer the authoritative
> rule source. The live rules (禁用動詞清單、Design Method 於 TC 定稿後指派、
> §11 self-check…) are maintained in
> [`ASPICE_SWE6_AI_Instruction.md`](./ASPICE_SWE6_AI_Instruction.md).
> Content below is retained for historical reference only and may be out of sync
> with `backend/prompt_builder.py` / `backend/validator.py`.

## 0. Overview

This document defines all rules for the automated test case generation tool.
Input/output: `.xlsx` (Test Case Specification & Result sheet).

---

## 1. Column Mapping

### 1.1 Input (read-only)

| Column | Field | Purpose |
|--------|-------|---------|
| D | Requirement or Design ID | Traceability anchor (e.g. `SWE1-HMI-DM-003-01`) |
| I | Test Item (original) | RD's raw requirement description — source of truth for generation |

### 1.2 Generated — preserve + append

| Column | Field | Rule |
|--------|-------|------|
| I | Test Item | Keep original text intact. Append rewritten version below with a blank line, wrapped in parentheses when writing back to the workbook. The generated field itself is plain `Condition/Trigger → Observable Outcome`; the `(...)` wrapper is presentation-layer only. |

### 1.3 Generated — overwrite

| Column | Field | Rule Source |
|--------|-------|-------------|
| J | Pre-Conditions | §3.2 |
| K | Input Test Data | §3.3 |
| L | Test Procedure | §4 |
| M | Expected Result | §5 |

### 1.4 Generated — new fill

| Column | Field | Rule Source |
|--------|-------|-------------|
| F | Test Case ID | §2.1 |
| G | Test Group | §2.2 |
| H | Test Set | §2.3 |
| N | Specification Reference | §2.4 |
| P | Test Case Priority | §6 |
| Q | Test Case Design Method | §7 |

### 1.5 Generated — sheet

| Sheet | Purpose |
|-------|---------|
| Test Case Framework | Populated from Test Set grouping result (§2.3) |

### 1.6 Untouched

Columns B, C, E, O, R–AG: preserve original values. Do not modify.

---

## 2. ID & Grouping Rules

### 2.1 Test Case ID (Col F)

Format: `{project}-{group_abbr}-{sequence}`

- `{project}`: extracted from "Product Document" sheet Row 3 Col B (e.g. `newR1L`).
  Non-alphanumeric characters (spaces, `/`, …) are stripped so a source value
  like `new R/L` becomes `newRL`.
- `{group_abbr}`: first letter of each CamelCase word, uppercased, no padding.
  e.g. `DeviceManager` → `DM`, `MediaPlayer` → `MP`, `AppleCarPlay` → `ACP`,
  `Bluetooth` → `BLU` (single word → first 3 chars), `BT` → `BT` (pure acronym
  stays as-is — the previous logic padded to `BTT`, which is no longer the case).
- `{sequence}`: 3-digit zero-padded, starting from `001`, incrementing per row

Example: `newR1L-DM-001`, `newR1L-DM-002`, ...

TC IDs already present in Col F are normalized on read — a cell like
`new R1L-DMR-014` becomes `newR1L-DMR-014` before validation. Structurally
broken values (missing segments, non-numeric sequence) are cleared and
regenerated from scratch.

Multiple TCs from the same requirement share the same Col D (Req ID) but have distinct Col F (TC ID).

### 2.2 Test Group (Col G)

Derived from the filename of the input `.xlsx`.

Pattern: `..._SWQT_{TestGroup}_{date}.xlsx`
Example: `..._SWQT_DeviceManager_20260408.xlsx` → `DeviceManager`

All rows in the same file share the same Test Group value.

### 2.3 Test Set (Col H)

Sub-feature grouping based on semantic analysis of Test Item content.

**Process:**
1. First run on a new CFTS: use AI to cluster all Test Items into sub-feature groups
2. Generate a `framework.json` mapping: `{ "Test Set Name": [list of Req ID patterns] }`
3. Human reviews and confirms the mapping
4. Subsequent runs use the confirmed mapping (no AI needed)

**Naming convention:** Short English labels describing the sub-feature (e.g. `Access & Entry`, `Device List & Recognition`, `Function Connection`)

**Also populate the "Test Case Framework" sheet** with the resulting structure:
- Column A: Test Group
- Column B: Test Set name
- Column C: Req ID range or count

### 2.4 Specification Reference (Col N)

Automatically match each Test Item to its source requirement in the SYS1 spec Excel.

**Input file:** SYS1 HMI spec Excel (Basic Report sheet)

**SYS1 structure:**
| Column | Field | Example |
|--------|-------|---------|
| A | NRL ID | `NRL-144757` |
| C | Outline Number | `2.2` |
| D | Description | `PDM01.) The user can access...` |
| E | Source ID | `Device_Manager_HMI Logic_and_Flow_R1_SR24_Post_2A_(March_13_2023)_2.2` |

**Matching strategy — three layers (all three implemented):**

**Layer 1: PDM code exact match (programmatic, no AI)**

1. Parse SYS1 descriptions to extract PDM codes: `PDM01`, `PDM05.2`, `PDMS01`, `MPDM1`, `TD1.7`, `DNDS2`, `PDEE01`, `APAC0.1`, etc.
2. Build `SpecIndex` (dict subclass): `{ "PDM01": entry }`, plus `.entries: list[entry]` for Layer 1.5.
3. Parse each Test Item (Col I) to extract PDM codes using regex: `/\b(PDM\d+\.?\d*|PDMS\d+\.?\d*|MPDM\d+\.?\d*|TD\d+\.?\d*|DNDS\d+\.?\d*|PDEE\d+\.?\d*|APAC\d+\.?\d*|PSR\d+\.?\d*)\b/`
4. Match → fill Col N with Source ID value; `match_type = "exact"`.

**Layer 1.5: Token Jaccard fallback (programmatic, no AI — implemented)**

For Test Items without a PDM code or where Layer 1 returns no match:

1. Tokenize the Test Item: lower-case, keep 3+ char alphanumeric tokens, drop stop-words.
2. Compute Jaccard similarity against every SYS1 description.
3. If the best score ≥ `FUZZY_THRESHOLD` (default `0.15`), take that entry; set `match_type = "fuzzy"` and attach `match_score` (rounded to 3 decimals).
4. Otherwise mark `match_type = "unmatched"`.

On the DeviceManager real workbook this lifted match rate from **54.5% → 100%** (24 exact + 20 fuzzy).

**Layer 2: Semantic match (precomputed embeddings — implemented)**

Runs when the active `SpecIndex` already carries entry-level embeddings (i.e. cached in `spec-index/cache/<name>.json` with `embedding_model` set; built by `scripts/build_spec_index.py`).

1. Embed the Test Item via the same model as the index (default `text-embedding-3-large`, see `spec_matcher.DEFAULT_EMBEDDING_MODEL`).
2. Compute cosine similarity against every spec entry's embedding.
3. If the best score ≥ semantic threshold, set `match_type = "fuzzy"` with `match_score` = cosine score; otherwise mark `unmatched`.
4. Top-N near-miss entries (when no exact match) are surfaced as `reference_candidate_context` for the AI prompt; the matched entry is exposed as `matched_spec_context`. `prompt_builder._get_spec_context` consumes both fields so generation can cite the referenced spec verbatim.

When the index has no embeddings (e.g. uploaded reference workbook freshly built via `build_spec_index`), Layer 2 is skipped and Layer 1.5 (Jaccard) handles fuzzy fallback automatically.

**Selecting an index at runtime:**

- The Upload page dropdown calls `GET /api/spec-library`, lists every entry from `spec-index/manifest.json`, and posts the chosen `selected_spec_name` to `POST /api/parse`. The job persists `selectedSpecName`, and `/api/match` plus generation load it via `spec_matcher.load_spec_index([name])`.
- If `selected_spec_name` is unset, the legacy uploaded reference workbook path remains.

**Output format for Col N:**
`Device_Manager_HMI Logic_and_Flow_R1_SR24_Post_2A_(March_13_2023)_{outline_number}`

**Multiple matches:** If a Test Item maps to multiple spec requirements, list them separated by `; ` (semicolon + space).

---

## 3. Field Generation Rules

### 3.1 Test Item — Rewrite (Col I append)

**Source:** AI Instruction §6.1

**Format:**
```
{original RD text}

([Condition/Trigger] → [Observable Outcome])
```

**Rules:**
- One behavior only per Test Item
- Must match the requirement intent
- Must include the specific scenario (not generic)
- The `[Condition/Trigger]` MUST carry the condition / state / context — a
  bare action (`Select X`, `Press Y`) is ambiguous because the same action
  under different states yields different outcomes. Use
  `[action] while/with/after [state]` or front-load the state
  (`With BT off, press Connect → ...`). Bare-action triggers are acceptable
  only when there is genuinely no relevant state (e.g. cold-boot smoke test).
- The `[Observable Outcome]` is what the tester verifies
- For `tc_title` specifically, a natural scenario sentence
  (`[Outcome] when [trigger]`, `[Object] [state] under [condition]`) is
  preferred when the arrow form would force telegraphic compression that
  hides the condition (see AI Instruction §6.1 examples).

**Example:**
```
PDM01.1) The Device Manager can be added to the reconfigurable status bar.

(User adds Device Manager to the status bar via customization interface → Device Manager shortcut icon is displayed in the status bar and opens Device Manager when tapped)
```

### 3.2 Pre-Conditions (Col J)

**Source:** AI Instruction §6.2

**Rules:**
- State or environment ONLY — never actions
- Minimum necessary state
- One item per numbered line

**Belongs:**
- External environment DUT cannot control (e.g. GPS signal available)
- Hardware/peripheral required (e.g. CarPlay-capable phone available)
- Functional initial state for dependency (e.g. Bluetooth enabled on HU)
- System version/mode constraint (e.g. R1 High variant only)

**Does NOT belong:**
- System-obvious baseline (`HU is powered on`) — assumed given
- Feature under test as premise (`Device Manager is accessible`) — this is the verification target
- Action-controlled state (`USB is inserted`) — move to Test Procedure steps

**Output:** Numbered list, or `NA` if no pre-conditions needed.

### 3.3 Input Test Data (Col K)

**Source:** AI Instruction §6.3

- Explicit, deterministic values: button name, option path, file type, trigger event
- Or `NA` if not applicable
- Never invent unstated data. If the requirement/spec does not explicitly give
  a number, threshold, timeout, dataset, state, identifier, error code, retry
  count, or comparison target, keep it abstract instead of guessing, e.g.
  `<configured limit>`, `<device under test>`, `the value defined in spec`.

### 3.4 No Fabricated Details

This rule applies to **all generated TC fields**: `test_item_rewrite`,
`pre_conditions`, `input_test_data`, `test_procedure`, and `expected_result`.

- Do not fabricate any concrete value or data point that is not explicitly
  stated in the requirement, matched spec text, or reviewer pre-fill.
- This includes not only numeric values, but also file names, dataset names,
  default states, IDs, error codes, retry limits, capacities, and comparison
  targets.
- If the source is ambiguous or incomplete, preserve the ambiguity explicitly
  rather than filling the gap with a plausible guess.
- Domain-standard constants are allowed only when they are truly standard and
  unambiguous in context.

---

## 4. Test Procedure Rules (Col L)

**Source:** AI Instruction §7.1–7.7

### 4.1 Structure

Every procedure follows this flow:
```
Setup steps → Transition steps → Final Step (verification)
```

### 4.2 Step Requirements (MANDATORY)

Each step MUST be:
1. **Executable** — a concrete action the tester performs
2. **Purposeful** — state why this step is executed

Allowed purposes: establish condition / transition system state / trigger behavior / observe & verify

**✗ Bad:** `Press H/K [Screen off] button.`
**✓ Good:** `Press H/K [Screen Off] button to turn off the screen.`

**✗ Bad:** `Tap "X"`
**✓ Good:** `Tap "X" to exit Dealer Mode.`

### 4.3 No Skipping

Do not omit steps when:
- State isn't guaranteed
- Navigation path isn't obvious
- Connection/pairing is required but not yet established

### 4.4 Step Classification

| Type | Purpose | Failure means |
|------|---------|---------------|
| Setup | Establish condition, prevent False Fail | Setup not reached |
| Transition | Move system to required state | Cannot proceed |
| Final Step | **Verification owner** — maps to Test Item | Test objective not met |

### 4.5 Final Step (CRITICAL)

**Rule: The tester must understand what is being verified by reading the Final Step alone.**

Must include:
- Explicit ACTION
- Verification target
- Direct mapping to Test Item's `→ [Observable Outcome]`

**✗ Bad:** `Select the Apple CarPlay icon.` — missing verification target
**✗ Bad:** `Observe whether CarPlay launches.` — vague
**✓ Good:** `Select the Apple CarPlay icon in the Menu Bar and check that the Apple CarPlay interface is displayed on the HU.`

### 4.6 Baseline Comparison

When Test Item involves state change or limit boundary:
1. Establish **baseline (before)** — verify starting state
2. Perform the action
3. Verify **outcome (after)** — compare against baseline

Missing baseline → final result is unjudgeable.

### 4.7 Output Format

Numbered list in a single cell. Each step on its own line:
```
1. [Setup step with purpose]
2. [Transition step with purpose]
3. [Final Step with action + verification target]
```

Use `\n` for line breaks within the Excel cell.

---

## 5. Expected Result Rules (Col M)

**Source:** AI Instruction §8

### 5.1 1:1 Mapping

Each procedure step has exactly one expected result. Numbering must align:
- Step 1 → Result 1
- Step 2 → Result 2
- Step N → Result N

### 5.2 Quality Requirements

- Observable and judgeable — tester can determine pass/fail
- No vague language: NEVER use `normal`, `as expected`, `works correctly`
- Setup results are allowed (e.g. `Bluetooth pairing completed successfully`)
- Final result must cover the **complete** verification objective

**✗ Bad:** `The feature works as expected.`
**✓ Good:** `The Device Manager shortcut icon is displayed in the status bar area.`

### 5.3 Completeness

If Test Item requires verifying multiple aspects (e.g. upload + playback), the final expected result must cover ALL aspects, not just one.

### 5.4 Output Format

Same as Test Procedure: numbered list, `\n` line breaks, 1:1 aligned.

---

## 6. Test Case Priority Rules (Col P)

**Current app contract values:** `P0`, `P1`, `P2`

**Historical note:** this section previously used `High`, `Medium`, `Low`, `NA`.
That is obsolete. The live backend now requires `P0` / `P1` / `P2` for the
workbook/export pipeline. This is an application contract, not a rule defined
by `ASPICE_SWE6_AI_Instruction.md`.

**Alignment with SWRA priority:**
- If SWRA provides priority for the requirement → use SWRA priority
- If no SWRA priority available → apply the following heuristic:

| Priority | Criteria |
|----------|----------|
| P0 | Safety-related (Functional Safety = Yes), core functionality that blocks usage, data loss/corruption risk |
| P1 | Standard feature verification, user-facing behavior, connection/disconnection flows |
| P2 | UI cosmetic details, edge cases, display formatting, non-critical convenience features |

**Note:** Priority rule may need refinement based on project-specific SWRA mapping. This section should be updated when SWRA data is available.

---

## 7. Test Case Design Method Rules (Col Q)

**Source:** Test Case Design Method 判斷規則 §12

**Values (dropdown):**
1. `功能測試 (Functional based ; no specific technique)`
2. `狀態轉換 (State Transition Testing)`
3. `決策表 (Decision Table Testing)`
4. `等價劃分 (Equivalence Partitioning, EP)`
5. `邊界值分析 (Boundary Value Analysis, BVA)`
6. `組合測試 (Combinatorial Testing ; Pairwise / t-wise)`
7. `情境 / 用例 (Scenario / Use Case Testing)`
8. `負向測試 (Negative / Invalid)`
9. `基礎故障注入 (Fault Injection Lite)`

### 7.1 Decision Waterfall

Evaluate in this order. First match wins:

```
1. Is it testing invalid input or illegal operation?
   → Negative / Invalid Testing

2. Is it simulating system/environment fault?
   → Fault Injection Lite

3. Does it involve system state change?
   → State Transition Testing

4. Does it depend on multiple condition combinations?
   → Decision Table Testing

5. Is it testing input ranges/partitions?
   → Equivalence Partitioning

6. Is it testing boundary values?
   → Boundary Value Analysis

7. Does it involve multiple parameter combinations?
   → Combinatorial Testing

8. Is it verifying a complete user workflow?
   → Scenario / Use Case Testing

9. None of the above?
   → Functional based
```

### 7.2 Keyword Hints for Programmatic Detection

| Method | Keywords / Patterns |
|--------|-------------------|
| Negative / Invalid | reject, prevent, not allowed, error, invalid, unauthorized, fail |
| Fault Injection | disconnect during, remove during, lost, timeout, unavailable, crash |
| State Transition | state, mode, switch to, change to, transition, idle → active, connect → disconnect |
| Decision Table | if...then, when...and, enable/disable + behavior, toggle ON/OFF |
| Equivalence Partitioning | types, categories, supported/unsupported formats, valid/invalid |
| Boundary Value Analysis | maximum, minimum, limit, up to, exceed, boundary, ≤, ≥, count |
| Combinatorial | combination, with different, across variants, multiple settings |
| Scenario / Use Case | user flow, end-to-end, workflow, sequence of actions |
| Functional based | display, show, exist, open, access, verify presence |

---

## 8. Validator Rules (Programmatic — No AI)

### 8.1 Test Item Format Check

- Appended rewrite must contain `→` separator
- Must be wrapped in parentheses `(...)`
- Must be separated from original by one blank line

### 8.2 Pre-Condition Check

- Must NOT contain action verbs: `insert`, `connect`, `press`, `tap`, `click`, `open`, `navigate`, `pair`, `plug`
- Must be numbered list or `NA`
- Must NOT contain system-obvious states: `HU is powered on`, `system is running`

### 8.3 Test Procedure Check

- Must be numbered list
- Each step should contain a purpose phrase (look for `to [verb]` pattern)
- Final step must contain verification verb: `verify`, `check`, `confirm`, `ensure`
- Final step must NOT contain vague verbs: `observe whether`, `see if`, `look at`
- Step count must be ≥ 2 (at minimum: one setup + one verification)

### 8.4 Expected Result Check

- Must be numbered list
- Count must equal Test Procedure step count (1:1)
- Must NOT contain: `normal`, `as expected`, `works correctly`, `no issue`
- Final result must be a concrete observable statement

### 8.5 Test Case ID Check

- Format must match: `{project}-{abbr}-{3-digit number}`
- Sequence must be monotonically increasing
- No duplicates

### 8.6 Design Method Check

- Value must be one of the 9 valid dropdown values (exact string match)

### 8.7 Priority Check

- Value must be one of: `P0`, `P1`, `P2`

---

## 9. False Pass / False Fail Prevention

**Source:** AI Instruction §9

### 9.1 False Pass Prevention (Split Rule)

When a requirement contains independent items that could pass/fail independently, they MUST be split into separate TCs:

- Multiple supported formats (e.g. `.mp4`, `.avi`, `.mpg`) → one TC per format
- Multiple device types → one TC per type
- Multiple protocols → one TC per protocol
- Multiple UI paths → one TC per path
- Multiple config values → one TC per value

**The tool should flag requirements that may need splitting** but not auto-split (splitting changes row count and Req ID mapping — requires human decision).

### 9.2 False Fail Prevention

- Include all necessary setup/transition steps
- Do not assume hidden state
- If a connection is needed, include the connection steps explicitly

---

## 10. Excel I/O Specification

### 10.1 Input File

- Format: `.xlsx`
- Main sheet: `Test Case Specification&Result`
- Header row: Row 9
- Data starts: Row 10
- Data ends: last row where Col D is not empty

### 10.2 Column Index Mapping (0-based)

```
B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8,
J=9, K=10, L=11, M=12, N=13, O=14, P=15, Q=16
```

### 10.3 Output File

- Same format as input
- Preserve all formatting, merged cells, formulas in untouched columns
- Write generated content to specified columns only
- Use `\n` for in-cell line breaks (openpyxl: set `alignment.wrap_text = True`)
- Output filename: `{input_filename}_generated.xlsx`

### 10.4 Test Case Framework Sheet

Populate with the Test Set grouping structure:
- If sheet is empty, create the header row and fill data
- If sheet has existing content, append or update as needed

---

## 11. Tool Execution Modes

### Mode A: Full Generation (default)

Process all rows from Row 10 to last data row. Generate all specified columns.

### Mode B: Incremental (legacy description)

The current API pipeline no longer preserves rows based on filled
Pre-Conditions / Procedure / Expected Result cells. Submitted rows always go
through AI generation; reviewer pre-filled content is passed into prompts as
hints instead of causing zero-cost `preserved` events.

`config.regenerateAll` is still accepted by the API for backward
compatibility, but it no longer changes generation behaviour.

### Mode C: Regenerate Specific

Accept selected row IDs and an optional `regenerateReason`. The reason is
passed into the AI prompt as the primary correction target. Regenerate uses the
split-aware generation path: AI first returns `req.split` analysis and an
`insertPlan` (`needsInsert`, `insertAfterId`, `newCount`,
`renumberRequired`). If no split is needed, the primary row is regenerated and
shown in diff preview. If split is needed, the primary row is regenerated and
extra TCs stream as `row.added` for insertion after the parent row.

### Mode D: Re-run Selected

Accept selected row IDs and re-enter the full generation pipeline without a
reviewer reason. This is used when the user wants AI to reassess decomposition
or add missing scenarios. The stream contract is the same split-aware shape:
`req.split.insertPlan`, primary `row.regenerated`, and optional `row.added`.

---

## 12. Prompt Template (for AI generation steps)

When calling the LLM API for test case generation, the prompt should include:

```
You are an ASPICE SWE.6 test case writer.

## Context
- Project: {project_name}
- Test Group: {test_group}
- Test Set: {test_set}

## Requirement
- Requirement ID: {req_id}
- Original Test Item: {original_test_item}

## Rules
{embed RULES.md §3–§5 here}

## Output Format
Return JSON:
{
  "test_item_rewrite": "Condition/Trigger → Observable Outcome",
  "pre_conditions": "1. ...\n2. ...",
  "input_test_data": "...",
  "test_procedure": "1. ...\n2. ...\n3. ...",
  "expected_result": "1. ...\n2. ...\n3. ...",
  "design_method": "one of 9 values",
  "priority": "P0|P1|P2",
  "split_flag": true/false,
  "split_reason": "reason if flagged"
}
```

Notes:

- `test_item_rewrite` is generated as plain `Trigger → Outcome` text. Outer
  parentheses are added only by the workbook writer when appending the rewrite
  below the original Test Item cell.
- When a requirement splits into multiple TCs, the scenario tag belongs in the
  TC title / `tc_title`, not inside `test_item_rewrite`.
- `priority` is an application workbook/export contract, not an ASPICE SWE.6
  rule from `ASPICE_SWE6_AI_Instruction.md`.

### 12.2 API Integration

**API:** OpenAI Chat Completions API (`https://api.openai.com/v1/chat/completions`). The openai Python SDK reads `OPENAI_API_KEY` automatically.

**Recommended models:**

| Use Case | Model | Model String | Why |
|----------|-------|-------------|-----|
| TC generation (default) | GPT-5 | `gpt-5` | Highest-quality decomposition for ambiguous specs |
| Alternative top quality | GPT-5.4 | `gpt-5.4` | Strong reasoning at roughly half the input price |
| Cheaper | GPT-5 mini | `gpt-5-mini` | Lower-cost option when prompts are simple |
| Legacy stable | GPT-4.1 | `gpt-4.1` | Keep available for comparison or fallback |
| Legacy | GPT-4o | `gpt-4o` | Retained for compatibility; not recommended for new runs |

Prompt caching is **automatic** on OpenAI for any prompt prefix ≥1024 tokens — no manual `cache_control` markers. Cached input tokens are billed at each model's `cached input` rate and reported via `response.usage.prompt_tokens_details.cached_tokens`.

**API call structure:**

```python
from openai import OpenAI
import json

client = OpenAI()  # reads OPENAI_API_KEY from env

def generate_test_case(req_id, test_item, spec_context, rules_text, model="gpt-5"):
    system_prompt = (
        f"## ASPICE SWE.6 Rules (authoritative)\n\n{rules_text}\n\n---\n\n"
        "You are an ASPICE SWE.6 test case writer. Return ONLY valid JSON, no markdown fences."
    )
    response = client.chat.completions.create(
        model=model,
        max_completion_tokens=2000,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"""## Context
- Requirement ID: {req_id}
- Original Test Item: {test_item}

## Spec Context
{spec_context}

## Output
Return JSON with keys: test_item_rewrite, pre_conditions, input_test_data,
test_procedure, expected_result, design_method, priority, split_flag, split_reason"""},
        ],
    )
    return json.loads(response.choices[0].message.content)
```

**Batch processing** — `response_format=json_object` forces an object, so we wrap the array in `{"tcs": [...]}` and unwrap on parse. Rules are kept identical across calls so the system prefix is served from cache on every batch after the first.

### 12.3 API Key Management

**Step 1 — Get API key:** https://platform.openai.com/api-keys → Create new key → copy `sk-proj-...`.

**Step 2 — `.env` in project root:**

```bash
# tc-generator/.env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxx
```

**Step 3 — ensure `.env` is ignored:**

```bash
# tc-generator/.gitignore
.env
.env.local
*.env
output/*.xlsx
output/*.db
node_modules/
__pycache__/
```

**Step 4 — load in Python backend:**

```python
# backend/generator.py
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()  # auto-reads OPENAI_API_KEY from env
```

**Step 5 — frontend proxy routes** (Next.js app router, server-side only):

```typescript
// frontend/app/api/generate/route.ts
const backend = process.env.PYTHON_API_BASE;  // http://localhost:8000
// proxies to the Python backend; browser never sees OPENAI_API_KEY
```

**Dependencies:**

```bash
# Python backend
pip install 'openai>=1.50' python-dotenv openpyxl pdfplumber python-docx fastapi uvicorn
```

### 12.4 Architecture — Frontend ↔ Backend ↔ API

```
Browser (Next.js client)
    ↓ fetch /api/generate
Next.js API route (server, thin proxy)
    ↓ HTTP
FastAPI backend (reads .env, holds OPENAI_API_KEY)
    ↓ openai SDK
OpenAI API
    ↓ response → SSE events → Next.js → browser
```

Key stays in the Python backend's `.env`; the frontend only sees the relative URL. Jobs are persisted to SQLite (`output/jobs.db`) via `SqliteJobStore` so they survive a backend restart.

### 12.5 Cost Control & Safeguards

1. **Budget cap per job:** configurable max-spend. Backend halts the batch loop before a call that would exceed the budget.

2. **Dry run / Configure estimate:** estimate uses the same backend-style token heuristic
   (`avg input per req` + `avg output per TC × expected split factor`) instead of a flat
   per-row coefficient.

3. **Token tracking:** input, output, cache-creation (0 on OpenAI), and cache-read tokens are
   summed per job and streamed to the frontend's CostMeter. This cumulative total includes:
   Test Set grouping AI calls, initial generation, regenerate, and rerun on the same job.

```python
usage = response.usage
prompt = usage.prompt_tokens
output = usage.completion_tokens
cached = (usage.prompt_tokens_details.cached_tokens or 0)
uncached = prompt - cached
cost = uncached * in_rate + cached * cached_in_rate + output * out_rate
```

4. **Pricing reference** (USD per million tokens; verify at https://openai.com/api/pricing):

| Model | Input | Output | Cached input |
|-------|-------|--------|--------------|
| gpt-5-mini | $0.25 | $2.00  | $0.025 |
| gpt-4.1    | $2.00 | $8.00  | $0.20  |
| gpt-4o     | $2.50 | $10.00 | $1.25  |
| gpt-5.4    | $2.50 | $15.00 | $0.25  |
| gpt-5      | $5.00 | $15.00 | $0.50  |

5. **Retry budget:** max 2 retries per TC; after 2 failures flag for manual handling.

6. **Rate limiting:** OpenAI limits TPM / RPM per tier. Batch mode (≥1 TC per call) is the primary mitigation; add `asyncio.sleep(0.15)` between batches.

---

## 13. File Structure (for implementation)

```
tc-generator/
├── RULES.md                        # This file
├── rules.json                      # Machine-readable version of rules
├── framework/
│   └── {test_group}_framework.json # Test Set mapping per CFTS
├── spec-index/
│   ├── manifest.json               # Library index consumed by GET /api/spec-library
│   ├── sources/                    # Original spec PDFs/PPTX (reference material)
│   └── cache/
│       ├── {name}.xlsx             # Source SYS1 workbook (Basic Report sheet)
│       └── {name}.json             # Built by scripts/build_spec_index.py:
│                                   # SpecIndex + per-entry embeddings (§2.4 Layer 2)
├── backend/
│   ├── parser.py                   # Excel reader (§10)
│   ├── spec_matcher.py             # Spec reference matching (§2.4)
│   ├── grouper.py                  # Test Set clustering (§2.3)
│   ├── id_generator.py             # TC ID generation (§2.1)
│   ├── prompt_builder.py           # Prompt assembly (§12)
│   ├── generator.py                # AI call + response parsing
│   ├── validator.py                # Rule checks (§8)
│   ├── writer.py                   # Excel writer (§10.3)
│   └── main.py                     # CLI entry point
├── app/                            # Next.js UI (§14)
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx            # Dashboard home
│   │   │   ├── upload/page.tsx     # File upload
│   │   │   ├── review/page.tsx     # TC review & edit
│   │   │   ├── validate/page.tsx   # Validation results
│   │   │   └── api/                # API routes (call Python backend)
│   │   ├── components/
│   │   └── lib/
│   ├── package.json
│   └── tailwind.config.ts
├── tests/
│   ├── test_validator.py
│   ├── test_id_generator.py
│   ├── test_spec_matcher.py
│   └── test_parser.py
└── output/
    └── (generated .xlsx files)
```

---

## 14. UI Specification

### 14.1 Overview

Local Next.js desktop app (localhost) for managing the TC generation workflow.
Tech stack: Next.js + Tailwind + 98.css + Zustand. Backend: Python FastAPI exposed through Next.js API proxy routes.

### 14.2 Pages & Flow

```
[Upload] → [Configure] → [Generate] → [Review] → [Export]
```

**Page 1: Upload (入口)**

Purpose: Upload input files and configure the generation job.

File slots:
- Slot A — TC Specification xlsx (required): the Test Case Specification & Result file
- Slot B — SYS1 Spec xlsx (optional): for Specification Reference matching (§2.4)
- Slot C — Spec document (optional): for additional context during AI generation
  - Accepted formats: `.pdf`, `.docx`, `.xlsx`
  - System auto-detects format and applies the appropriate parser (see §14.6)

After upload, system auto-detects:
- Project name (from Product Document sheet)
- Test Group (from filename)
- Row count (number of TCs to process)
- Column fill status (which columns are already filled vs empty)
- Slot C file type and extraction preview (first N paragraphs / rows)

Display a summary card with detected metadata before proceeding.

**Page 2: Configure (設定)**

Purpose: Review and adjust generation parameters before running.

Sections:
- Test Set grouping preview: show AI-suggested groups, allow drag-and-drop to reassign TCs between groups, allow rename/merge/split groups
- Spec matching preview: show Layer 1 (PDM code) matches and Layer 2 (AI) candidates, allow manual override
- Generation scope: select which columns to generate (checkboxes for each: Test Item rewrite, Pre-Conditions, Procedure, Expected Result, Priority, Design Method, Spec Reference)
- Model selection: GPT-5.4 mini (default) vs GPT-5.4 (quality) vs GPT-5.4 nano (budget/re-run)
- Batch size: 1 / 5 / 10 TCs per API call

Save configuration as a job file for reproducibility.

**Page 3: Generate (生成)**

Purpose: Execute generation and show progress.

Features:
- Progress bar: X / N TCs completed
- Live log: show each TC being processed (Req ID, Test Item snippet, status)
- Pause / Resume / Cancel controls
- Running cumulative spend for the job (includes prior grouping AI calls and later regenerate / rerun on the same job)
- Error handling: failed TCs collected for retry

**Page 4: Review (審閱)**

Purpose: Human review of generated results before export.

Layout: Table view with expandable rows. Each row shows:
- Left column: Original content (Col I original, Col L original, Col M original)
- Right column: Generated content (Test Item rewrite, new Procedure, new Expected Result)
- Diff highlighting between original and generated

Per-row actions:
- Accept (✓): mark as approved
- Edit (✏️): inline edit any generated field
- Reject (✗): mark for regeneration
- Flag (⚑): mark for human attention (e.g. split needed per §9.1)

Filters:
- By validation status: pass / fail / warning
- By Test Set group
- By review status: pending / accepted / rejected / flagged

Bulk actions:
- Accept all passing
- Regenerate all rejected
- Export only accepted

Validation panel (sidebar):
- Show validator results per TC (§8)
- Red: critical violations (missing Final Step verification, 1:1 mismatch)
- Yellow: warnings (vague language detected, possible False Pass)
- Green: all checks passed

**Page 5: Export (匯出)**

Purpose: Write approved results back to xlsx and download.

Options:
- Export scope: all / accepted only / by Test Set
- Output format: overwrite original file vs create new file
- Include/exclude: choose which generated columns to write
- Framework sheet: option to populate Test Case Framework sheet

Output: download link for the generated `.xlsx` file.

### 14.3 Data Flow

```
Upload page
    ├── TC xlsx → Python parser → structured JSON (all rows + columns)
    ├── SYS1 xlsx → Python spec_matcher → spec_index.json
    └── HMI PDF → Python pdf_parser → chunked text (optional)
         ↓
Configure page
    ├── grouper.py → framework.json (Test Set groups)
    ├── spec_matcher.py → matched references
    └── User confirms / adjusts
         ↓
Generate page
    ├── prompt_builder.py → assembled prompts
    ├── generator.py → OpenAI API calls → raw responses
    └── validator.py → validation results
         ↓
Review page
    ├── Display original vs generated (diff view)
    ├── User accepts / edits / rejects per row
    └── Re-run generator for rejected rows
         ↓
Export page
    └── writer.py → output .xlsx with approved content
```

### 14.4 State Management

Use a single JSON file per job as the source of truth:

```json
{
  "job_id": "dm_20260416",
  "project": "newR1L",
  "test_group": "DeviceManager",
  "files": {
    "tc_xlsx": "path/to/input.xlsx",
    "sys1_xlsx": "path/to/sys1.xlsx",
    "hmi_pdf": "path/to/spec.pdf"
  },
  "config": {
    "model": "haiku",
    "batch_size": 5,
    "columns_to_generate": ["I_rewrite", "J", "K", "L", "M", "N", "P", "Q"]
  },
  "framework": { ... },
  "spec_index": { ... },
  "rows": [
    {
      "row_num": 10,
      "req_id": "SWE1-HMI-DM-001-01",
      "original": { "I": "...", "L": "...", "M": "..." },
      "generated": { "I_rewrite": "...", "J": "...", ... },
      "validation": { "status": "pass", "issues": [] },
      "review": "pending"
    }
  ],
  "stats": {
    "total": 81,
    "generated": 81,
    "accepted": 0,
    "rejected": 0,
    "flagged": 0
  }
}
```

No database needed. Each job is a self-contained JSON file.

### 14.5 Spec Document Input (Slot B + C)

**Slot B — SYS1 Spec xlsx (structured requirement source)**

Used for Specification Reference matching (§2.4). Expected format: Basic Report sheet with columns ID, Outline Number, Description, Source ID. This is the primary traceability source.

**Slot C — Spec document (supplementary context)**

Provides additional requirement detail for AI generation. Accepted formats and parsing strategy:

| Format | Parser | Output |
|--------|--------|--------|
| `.pdf` | `pdfplumber` for text + tables; fall back to `pymupdf` for image-heavy pages | Chunked text segments keyed by page number and detected PDM codes |
| `.docx` | `python-docx`; split by Heading styles (Heading 1/2/3) | Chunked text segments keyed by heading hierarchy |
| `.xlsx` | `openpyxl`; treat each row as a requirement entry | Structured records keyed by row ID or first-column value |

### 14.6 Spec Document Pre-processing Pipeline

```
Slot C file uploaded
    ↓
Detect format (extension + magic bytes)
    ↓
├── .pdf  → pdfplumber extract text per page
│           → regex scan for PDM/PDMS/TD codes per page
│           → build index: { "PDM05.2": { page: 5, text: "..." } }
│
├── .docx → python-docx iterate paragraphs
│           → split at Heading styles into sections
│           → regex scan for PDM codes per section
│           → build index: { "PDM05.2": { heading: "Main", text: "..." } }
│
└── .xlsx → openpyxl read rows
            → use first column or detected ID column as key
            → regex scan for PDM codes per row
            → build index: { "PDM05.2": { row: 12, text: "..." } }
    ↓
Merge with SYS1 index (Slot B) if both provided:
    → SYS1 provides: NRL ID, Source ID, outline number (for Col N)
    → Slot C provides: full requirement text (for AI prompt context)
    → Combined index: { "PDM05.2": { source_id, nrl_id, full_text } }
    ↓
Store as spec_index.json for this job
```

**Key design decisions:**

1. Slot B and Slot C serve different purposes: B is for traceability (Col N), C is for AI context. Both are optional, and they complement each other.
2. If only Slot C is provided without Slot B, the tool can still extract PDM codes for matching but cannot fill Col N with formal Source IDs.
3. If only Slot B is provided without Slot C, Col N can be filled but AI generation relies only on the Test Item text (less context, potentially lower quality).
4. If both are provided, the tool merges them into a rich index that supports both traceability and high-quality generation.
5. The chunking strategy ensures that only the relevant spec segment (matched by PDM code) is injected into each TC's generation prompt, keeping token usage minimal regardless of total spec size.
