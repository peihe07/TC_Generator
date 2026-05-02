# Claude Code Brief — Add Review Feature to TC Generator

## Mission

Add an **ASPICE SWE.6 Review** feature to the existing `tc-generator` repo. The current tool generates TCs; this feature audits existing TCs against the same SWE.6 standard and produces a Three-Tier Findings Report. Review is a **parallel feature**, not a replacement — generate prompt, rules, parser, UI all stay untouched.

The two source-of-truth files for this feature are already in the repo (drop them in first if not):

- `docs/ASPICE_SWE6_AI_Review.md` — full v2.2 spec, auto-loaded into review LLM prompt at runtime
- `backend/rules/review_rules.yaml` — structured rule table for the rule engine

**Read both before starting. The spec defines the Three-Tier model (§3), severity rubric (§4), output schema (§9), and 31 detection rules. The yaml table is the machine-readable companion that the rule engine iterates.**

---

## Background You Need

### Existing project shape

```
backend/
├── api_server.py              # FastAPI; existing /generate endpoints
├── main.py                    # CLI; existing --mode flag
├── prompt_builder.py          # auto-loads docs/ASPICE_SWE6_AI_Instruction.md
├── parser.py (or similar)     # parses Test Case Specification 測試用例規範 sheet
└── ...

frontend/
├── app/api/                   # Next.js proxy routes
│   └── generate/route.ts      # mirrors backend
├── src/
│   ├── modules/               # active UI; *Module.tsx convention
│   │   └── GenerateModule.tsx
│   └── services/jobAdapter.ts # single backend adapter
└── ...

docs/
├── ASPICE_SWE6_AI_Instruction.md  # generate spec (auto-loaded; DO NOT MODIFY)
├── ASPICE_SWE6_AI_Review.md       # review spec (auto-loaded; THIS FEATURE)
└── RULES.md                       # tool-side rules (column mapping etc; DO NOT MODIFY)
```

### Hard constraints

1. **DO NOT modify the generate path.** No edits to `prompt_builder.py`, `ASPICE_SWE6_AI_Instruction.md`, generate API routes, or `GenerateModule.tsx`.
2. **DO mirror generate patterns.** Read existing modules first; new review modules should look like siblings of existing generate ones in style, naming, error handling, logging.
3. **DO NOT merge specs.** `Instruction.md` (generate) and `Review.md` (review) stay as two separate files. They are intentionally not cross-referenced.
4. **Language policy** (from spec §1):
   - Findings text (`issue` / `reasoning` / `suggestion_note`) → Traditional Chinese
   - Rewrites (`original` / `revised`) → match source field language; never translate
   - Code comments → English (per project preference)
   - User-facing UI strings → Traditional Chinese (per existing convention)

---

## Phase Breakdown

Six phases, each independently shippable. Run them in order; later phases assume earlier ones merged.

### Phase 1 — Drop-in spec files (5 min)

**Goal:** Get the two source-of-truth files into the repo.

**Tasks:**
1. Verify `docs/ASPICE_SWE6_AI_Review.md` exists. If not, copy from the integration drop-in folder.
2. Verify `backend/rules/review_rules.yaml` exists. If not, copy from drop-in. Create `backend/rules/` dir if missing.
3. Update repo root `README.md` "Reference docs" section to add:
   ```
   - [docs/ASPICE_SWE6_AI_Review.md](docs/ASPICE_SWE6_AI_Review.md) — ASPICE SWE.6 AI Review spec (auto-loaded into review prompt)
   ```

**Done when:** Both files committed; README links resolve.

---

### Phase 2 — Backend parser audit (30 min)

**Goal:** Make sure the existing TC parser surfaces the fields the review engine needs. Most likely it already does for generate; review needs two extra fields.

**Tasks:**

1. Locate the existing parser (likely `backend/parser.py` or similar). Find where it reads each TC row from `Test Case Specification 測試用例規範` sheet and constructs the per-TC dict.

2. Verify the parsed dict carries these fields needed by review (and how they're keyed):

   | Spec field (yaml/spec ref) | Excel column header | Why review needs it |
   |---|---|---|
   | `req_id` | `Requirement or Design ID / 需求/設計 ID` (col D) | Tier 1 grouping |
   | `tc_id` | `Test Case ID / 測試用例ID` (col F) | identification |
   | `test_item` | `Test Item / 測試項目` (col I) | spec句 extraction (Tier 1), §7.1, §8.1.x |
   | `pre_cond` | `Pre-Conditions / 先前條件` (col J) | §7.3, §8.2.x |
   | `procedure` | `Test procedure / 測試程序` (col L) | §7.4, §7.5, §8.3.x |
   | `expected` | `Expected Result / 預期結果` (col M) | §7.2, §7.4, §8.4.x |
   | `spec_ref` | `Specification Reference / 規格參考` (col N) | **§7.4 critical** — checks if numeric values are documented |
   | `priority` | `Test Case Priority / 測試用例優先級別` (col P) | §8.5.1 |
   | `design_method` | `Test Case Design / Methods / 測試用例設計方法` (col Q) | §8.5.2, §8.5.3 |

3. **Critical check — multi-Req-ID:** the `req_id` cell may contain multiple newline-separated Req IDs (e.g. `SWE1-PROJ-212\nSWE1-PROJ-213`). Generate path may have stripped or normalised this. Review needs the **raw value preserved** to detect §6.7. Verify the parser does not strip newlines from this cell. If it does, add a `req_id_raw` field that preserves the original string while leaving the normalised `req_id` for generate.

4. **Critical check — Specification Reference:** verify the parser reads col N. If generate doesn't surface this field, add it to the parsed dict (don't break generate consumers — add as optional new field).

5. Add unit test `backend/tests/test_parser_for_review.py` covering:
   - A TC with single Req ID parses correctly
   - A TC with multi-Req-ID newline-separated cell preserves both IDs
   - A TC with empty `Specification Reference` parses to empty string (not `None` typed differently from other empty fields)
   - Use real fixture rows from `Test Case Specification 測試用例規範` sheet — pick rows 10, 480, 526 from any sample workbook

**Done when:**
- Parser dict carries `req_id` (raw, with newlines if present) and `spec_ref` for every TC row
- Tests pass
- Generate path tests still pass (verify no regression)

---

### Phase 3 — Backend rule engine + prompt builder (3-4 hours)

**Goal:** Implement the core review engine that takes parsed TCs and produces findings.

#### 3a — `backend/review_prompt_builder.py`

Mirror `backend/prompt_builder.py`'s structure exactly. Read it first.

**Interface:**
```python
def build_review_prompt(
    tcs_batch: list[dict],
    rules_context: dict,  # rules that need LLM judgment, scoped to this batch
) -> list[dict]:  # OpenAI chat messages format
    """Build prompt for LLM to make Tier 2 §7.1/§7.2/§7.3 + Tier 3 §8.2.4/§8.4.2/§8.5.3
    judgments that pure regex cannot. Returns chat messages array."""
```

**Construction:**
- System message body = contents of `docs/ASPICE_SWE6_AI_Review.md` loaded once at module import (mirror how `prompt_builder.py` loads `ASPICE_SWE6_AI_Instruction.md`)
- User message includes: TC batch as JSON, list of rules to evaluate, schema reminder
- Output schema: per spec §9 contract — `per_req_findings` + `per_tc_findings` (no `batch_summary`; that's done by `review_engine.py` aggregating from raw findings)

#### 3b — `backend/review_engine.py`

**Interface:**
```python
def review_workbook(
    workbook_path: str,
    output_dir: str,
    model: str = "gpt-5",
    dry_run: bool = False,
) -> dict:  # full findings report per spec §9.1
    """End-to-end review pipeline. Returns the findings JSON; also writes
    findings.json + findings_report.md to output_dir."""
```

**Algorithm (follow spec §5 Workflow exactly):**

```
1. Parse workbook (reuse existing parser from Phase 2)
2. Group TCs by Req ID (multi-Req-ID TCs registered under each constituent ID per §6.7)
3. For each Req group:
   a. Extract Req spec句 (first English sentence with shall/must/should from any TC's Test Item;
      for multi-Req-ID TCs, match by [REQ-ID] bracket tag if present)
   b. If no spec句 found → emit §6.6 finding (Major), mark group `tier1_skipped`
   c. If 2+ TCs carry materially different spec句 → emit §6.5 finding (Critical)
   d. Apply §6.1, §6.2, §6.3, §6.4 (load logic from review_rules.yaml)
4. For each TC:
   - Tier 2 (skip if Req group is tier1_skipped): §7.1, §7.2, §7.3, §7.4, §7.5
   - Tier 3 (always run): §8.1.x, §8.2.x, §8.3.x, §8.4.x, §8.5.x
   - §8.3.6 fallback ONLY runs when TC's Req group is tier1_skipped
5. Apply interactions from review_rules.yaml:
   - mutual_exclusions: §7.4 ⊕ §8.3.6 (never both fire on same value)
   - suppressions: §6.4 suppresses §8.1.4 on same TCs
6. Aggregate batch_summary
7. Generate findings_report.md (human-readable from JSON)
8. Return findings JSON; write findings.json + findings_report.md to output_dir
```

**Rule execution:**
- Load `backend/rules/review_rules.yaml` at import
- Each rule has `requires_llm: true | false`
- `requires_llm: false` → execute via Python regex/keyword detection (write a `_detect_<rule_id>` function for each, e.g. `_detect_8_3_1` for forbidden verbs)
- `requires_llm: true` → batch up TC + rule context, call OpenAI via `review_prompt_builder.py`, parse response, merge into findings list

**Spec句 extraction helper:**
```python
def extract_spec_sentence(test_item: str, req_id: str = None) -> str | None:
    """Extract first English sentence containing shall/must/should from Test Item.
    For multi-Req-ID TC: if [REQ-ID] bracket tag matches `req_id`, use only that segment.
    Returns None if no spec句 found."""
```

Implementation hints:
- Multi-line Test Item: split on double newline first, then look for `shall|must|should` (case-insensitive)
- `[REQ-ID]` tag: regex `\[(SWE1-PROJ-\d+(?:-\d+)?)\]\s*\n?(.+?)(?=\n\[|$)` to extract tagged segments

**Mutual exclusion handling:**
After all detections run, when both §7.4 and §8.3.6 fire on the same `step_index` of the same TC, drop the §8.3.6 finding (§7.4 takes precedence per spec §10 self-check item 10).

**Suppression handling:**
After Tier 1, collect Req IDs where §6.4 fired. For TCs in those groups, skip §8.1.4 detection.

**Severity ceiling enforcement:**
Each tier has a max severity (Tier 3 ≤ Major). Add an assertion: if any finding violates ceiling, raise `ReviewEngineError`. Don't silently clamp — surface the bug.

#### 3c — Tests `backend/tests/test_review_engine.py`

Use the four validated deep-dive cases as canonical fixtures:

```python
# Use a small fixture workbook with these rows (or load from an actual sample workbook).

def test_group_a_fabricated_value_critical():
    """Rows 52-55 (PROJ-081-001): step '等待5秒' must trigger §7.4 Critical
    on each of 4 TCs. §8.3.6 must NOT fire (mutual exclusion)."""

def test_group_b_multiple_fabricated_values():
    """Rows 109-113 (PROJ-092-001): expect 8 §7.4 Critical findings across
    5 TCs covering 30分鐘, 3小時, 20次, <3s values."""

def test_group_c_multi_req_id_and_tool_launch():
    """Row 480 (PROJ-212+213): exactly one §6.7 Major in per_req_findings
    with comma-joined req_id 'SWE1-PROJ-212, SWE1-PROJ-213'.
    §7.5 Critical fires on step 5 (PCTS-MT1 launch with no result read).
    §6.2 Critical fires for both PROJ-212 and PROJ-213 (boundary missing)."""

def test_group_d_tier1_not_executable_with_fallback():
    """Rows 526-532 (PROJ-229/230/231): three §6.6 Major in per_req_findings.
    Tier 2 entirely skipped for these TCs.
    Row 532 step 6 '重複5次' triggers §8.3.6 (Tier 3 fallback), NOT §7.4."""

def test_severity_ceiling_enforced():
    """Tier 3 finding with severity 'Critical' raises ReviewEngineError."""

def test_mutual_exclusion_74_836():
    """Synthesize a TC where both §7.4 and §8.3.6 would match;
    only §7.4 should be in output."""

def test_suppression_64_814():
    """Synthesize a Req group where §6.4 fires; verify §8.1.4 not in
    per_tc_findings for TCs in that group."""

def test_dry_run_no_api_call():
    """dry_run=True must not invoke OpenAI; should still run rule-engine
    pre-pass and return findings for requires_llm=false rules only."""
```

**Done when:**
- All tests pass
- Manual run: `python backend/main.py --review --input <sample workbook> --output-dir output --dry-run` produces a `findings.json` with regex-detected findings (no LLM call)
- Manual run with API key: full review of sample workbook completes without errors and emits both `findings.json` and `findings_report.md`

---

### Phase 4 — CLI integration (1 hour)

**Goal:** Add `--review` flag to existing CLI without disturbing generate flow.

**Tasks:**

1. In `backend/main.py`, add new mode value `review` to existing `--mode` flag (or add separate `--review` boolean flag — pick whichever is more consistent with existing CLI patterns).

2. When review mode is selected:
   - Required arg: `--input` (the workbook to audit)
   - Optional: `--output-dir` (default `output/`)
   - Optional: `--model` (default `gpt-5`)
   - Optional: `--dry-run` (skip LLM call, regex-only pass)
   - Optional: `--budget` (reuse existing budget enforcement if present)
   - **NOT applicable** in review mode: `--sys1`, `--spec`, `--framework`, `--batch-size`, `--rows`, `--strict-validation`. If user passes them with `--review`, error out clearly.

3. Output files:
   - `<output-dir>/findings.json` — full report per spec §9.1
   - `<output-dir>/findings_report.md` — human-readable rendering
   - Console: print `batch_summary` reasoning + verdict counts

4. Update `README.md` CLI Usage section. Add a new subsection:

   ```markdown
   ### Review Mode

   Audit existing TCs against ASPICE SWE.6:

   ​```bash
   python backend/main.py --review --input path/to/existing_tcs.xlsx --output-dir output
   ​```

   Outputs `output/findings.json` and `output/findings_report.md`.
   ```

**Done when:**
- `python backend/main.py --review --help` shows review-specific options cleanly
- Sample workbook produces both output files
- Generate flow CLI tests still pass

---

### Phase 5 — Backend API + frontend integration (4-5 hours)

**Goal:** Wire review into the desktop app as a new module.

#### 5a — Backend API

Add to `backend/api_server.py`:

- `POST /review` — start review job, returns `job_id` (mirror existing generate job pattern)
- `GET /review/{job_id}/status` — job status (or whatever the existing generate API uses)
- `GET /review/{job_id}/findings` — completed findings JSON
- `GET /review/{job_id}/report` — markdown report
- Reuse existing job queue / async pattern from generate side. Don't introduce new infrastructure.

#### 5b — Frontend proxy

Create `frontend/app/api/review/route.ts` mirroring `frontend/app/api/generate/route.ts` exactly. POST handler proxies to backend `/review`; status & findings are GET handlers.

#### 5c — Frontend module

Create `frontend/src/modules/ReviewModule.tsx` mirroring `GenerateModule.tsx`'s style:

**UI states:**
1. **Idle** — file upload zone, "Start Review" button (disabled until file uploaded)
2. **Reviewing** — progress indicator, current TC counter, ability to cancel
3. **Done** — summary panel + findings table

**Summary panel** shows (from `batch_summary`):
- Total TCs reviewed, total Req groups
- Tier 1 / Tier 2 / Tier 3 counts (Critical / Major / Minor / Info bar chart)
- Top 5 violated rules
- Reasoning text (from `batch_summary.reasoning`)

**Findings table** shows (filterable by Tier and Severity):
- Two tabs: `Per Requirement` (Tier 1 findings) and `Per TC` (Tier 2 + Tier 3)
- Per-Req tab columns: Req ID, Rule, Severity, Issue, Affected TCs, expandable for stub
- Per-TC tab columns: Row, TC ID, Verdict, Tier, Rule, Severity, Field, Issue, expandable for evidence/original/revised

**Export action:**
- Download `findings.json` (raw)
- Download `findings_report.md` (human-readable)
- (Future: write findings back to Excel as new sheet — out of scope for Phase 5)

#### 5d — JobAdapter extension

Add to `frontend/src/services/jobAdapter.ts`:
- `startReviewJob(workbookFile: File): Promise<{ jobId: string }>`
- `getReviewStatus(jobId): Promise<JobStatus>`
- `getReviewFindings(jobId): Promise<FindingsReport>`
- `getReviewReport(jobId): Promise<string>` (markdown)

Mirror existing `startGenerateJob` etc. Use same error handling, cancellation, polling patterns.

#### 5e — Module registration

Wire `ReviewModule` into the desktop's module registry / navigation (wherever `GenerateModule` is registered). The Win95 desktop should show it as a new "icon" alongside Generate.

**Done when:**
- Run `npm run dev` per README, open `http://127.0.0.1:3333`
- Upload sample workbook through Review module, see findings table populated
- Download findings.json and findings_report.md from UI; contents match CLI output for same file
- `npm run typecheck` clean
- Generate flow still works end-to-end (no regression)

---

### Phase 6 — Documentation + final polish (1 hour)

**Goal:** Update docs so future devs find their way.

**Tasks:**

1. Update `docs/STATUS.md` — add review feature to "what's been built" section.

2. Update `docs/WORKFLOW_MECHANISM_TABLE.md` — add review user actions, API routes, backend work, AI calls, state writes (same shape as existing generate entries).

3. Update `docs/API_CONTRACT.md` — add review endpoints with request/response schemas.

4. Add `docs/REVIEW_RULES.md` (optional, for human readers) — markdown table summarising all 31 rules from `review_rules.yaml`. Useful when reviewer wants to understand why a finding fired.

5. Update root `README.md`:
   - "Run The Desktop App" — add note that Review module is now available alongside Generate
   - "CLI Usage" — already done in Phase 4
   - "Reference docs" — add `docs/ASPICE_SWE6_AI_Review.md` link (already done in Phase 1)

**Done when:** All docs updated; cross-links between docs resolve.

---

## Acceptance Criteria (Whole Feature)

The feature is done when ALL of the following are true:

1. ✅ A user can run `python backend/main.py --review --input some.xlsx --output-dir output` and get `findings.json` + `findings_report.md`
2. ✅ A user can open the desktop app, upload an Excel through the Review module, see findings, and download both files
3. ✅ All 4 deep-dive test cases pass (Group A/B/C/D from Phase 3)
4. ✅ Severity ceiling enforced (Tier 3 cannot emit Critical)
5. ✅ §7.4 / §8.3.6 mutual exclusion verified
6. ✅ §6.4 suppresses §8.1.4 verified
7. ✅ Multi-Req-ID parsing preserves original cell value
8. ✅ Generate path: existing tests still pass (no regression)
9. ✅ Frontend typecheck clean
10. ✅ Sample run on the Projection workbook (~602 TCs) completes without errors and `batch_summary.reasoning` is coherent (Tier 1 first, Tier 2/3 after)

---

## Implementation Tips for Claude Code

### Order of operations within Phase 3

The 31 rules are not equal in implementation cost. Implement in this order:

**Easy regex-only rules first** (build confidence + most coverage with least LLM cost):
- §8.3.1 forbidden verb — keyword list, very high frequency
- §8.5.1 priority outside P0–P3 — value membership check
- §8.5.2 design_method missing — empty check
- §8.4.1 vague outcome — keyword list
- §8.2.1 / §8.2.2 / §8.2.3 / §8.2.5 — keyword lists
- §8.3.3 single-step — line count
- §8.3.4 step numbering anomaly — regex
- §8.4.3 ER numbering anomaly — regex
- §8.1.1 length out of range — word count
- §8.1.2 modal/hedge — keyword list
- §8.1.3 multi-language collision — character class detection

**Medium rules** (regex with cross-field lookup):
- §6.6 Tier 1 not executable — group-level scan for shall/must/should
- §6.7 Multi-Req-ID — cell-level newline split
- §7.4 Fabricated value — regex + spec_ref absence check + spec句 absence check
- §7.5 Final Step launches tool — verb + tool name regex on last step + verification follow-up scan
- §8.3.5 Final Step no check target — last-step keyword scan
- §8.3.6 Fabricated value fallback — same as §7.4 but only fires when group is tier1_skipped
- §8.1.5 No spec句 nor traceable Req — combine spec句 absence with Req ID presence
- §6.5 Spec句 inconsistent — set diff across group's TCs
- §6.4 Sibling axis ambiguous — string similarity within group

**Hard rules requiring LLM**:
- §6.1 Missing supported/negative pair
- §6.2 Missing boundary axis
- §6.3 Missing enumeration coverage
- §7.1 Test Item outcome not in Req spec
- §7.2 ER misses Req outcome elements
- §7.3 Pre-Cond duplicates Req trigger
- §8.2.4 Feature-under-test stated as ready
- §8.4.2 Step↔ER count mismatch
- §8.5.3 Design Method inconsistent with Procedure

For LLM rules, batch detection by sending up to ~5 TCs per call with all applicable LLM rules in one prompt. The spec at §9 defines the exact response format.

### Spec句 extraction edge cases (you'll hit these)

- Test Item with no English at all (rows 526+): `extract_spec_sentence` returns `None`, group goes `tier1_skipped`
- Test Item with `[REQ-ID]` tags (row 480): need to match the right segment for each Req ID in multi-Req-ID case
- Spec句 spanning multiple lines: most are single sentence on one line, but be defensive — join all whitespace before regex
- Mixed case `Shall` / `MUST` / `should`: case-insensitive
- "should" in non-spec context (e.g. "the test should run for 30 minutes"): rare in practice; accept some false positives — reviewer adjusts. If it becomes a problem, require sentence to also contain a subject like "HU" / "system" / "device" before `shall`

### Findings schema gotchas

- `evidence_req_spec`: REQUIRED for Tier 2 findings, FORBIDDEN for Tier 3 findings (per spec §9 + §10 self-check)
- `step_index`: 1-indexed (matches numbered steps as written in workbook)
- `original` and `revised`: same language as the source field, never translated
- §6.7 finding: comma-joined `req_id` (e.g. `"SWE1-PROJ-212, SWE1-PROJ-213"`), recorded ONCE in per_req_findings, NOT duplicated under each constituent group
- `overall_verdict`: `fail` if ANY Critical anywhere on the TC (Tier 2 or Tier 3); `pass_with_issues` if any Major/Minor; `pass` only if findings list is empty or only Info

### Performance / cost

- A 600-TC workbook with all rules running LLM would cost ~$5 at gpt-5 prices. The regex-only pre-pass should handle ~65% of findings before LLM is called.
- Batch size 5 TCs per LLM call is a reasonable starting point (matches generate-side `--batch-size` default).
- Cache spec句 extraction per Req group (multi-Req-ID makes naive re-extraction inefficient).

### What to ask the user before starting

If anything in this brief is ambiguous after reading repo:
- Is `--mode review` or separate `--review` flag preferred? (Look at how existing generate options are structured.)
- Does `api_server.py` use FastAPI background tasks, Celery, or something else for jobs? Mirror it.
- Does `jobAdapter.ts` use React Query, SWR, or plain fetch? Mirror it.
- Where exactly does Win95 desktop register modules? (The new ReviewModule needs to register the same way.)

---

## Out of Scope (Explicit)

These are NOT part of this feature. If user requests them, push back:

- Writing findings back into the Excel workbook as a new sheet (planned for v3 or later)
- Auto-fixing findings (review proposes; doesn't apply)
- Reviewing more than the `Test Case Specification 測試用例規範` sheet
- Reviewing TCs across multiple workbooks in one job
- Generating new TCs from review findings (would re-enter generate path)
- Real-time review while user types in a TC editor
- LLM rule v2.2 §6.8 (Reference-pointer Req) — deferred to future spec version
- Review history / diffing between review runs

---

## Final Sanity Check

Before declaring the feature done, run this end-to-end smoke test:

```bash
# 1. Backend tests
pytest backend/tests/ -q

# 2. Frontend typecheck
cd frontend && npm run typecheck

# 3. CLI dry run on Projection workbook (~602 TCs)
python backend/main.py --review \
  --input "FM-WI-FSM-036-A01_STLA_測試用例規範與結果_SWQT_STLA_Test_Case_Specification___Result_SWQT_Projection_20260502.xlsx" \
  --output-dir output \
  --dry-run

# 4. Inspect output/findings.json:
#    - per_req_findings should include §6.6 entries for PROJ-229/230/231
#    - per_tc_findings for row 480 should include §6.7 + §7.5 + §6.2 entries
#    - per_tc_findings for rows 52-55 should each include §7.4 (etc) since their groups have spec sentences
#    - severity_counts should show Tier 3 § ≤ Major (zero Critical at Tier 3)

# 5. Frontend smoke test
cd frontend && npm run dev
# Upload the same workbook through the Review module
# Verify summary matches CLI output
```

If all 5 steps pass, ship it.
