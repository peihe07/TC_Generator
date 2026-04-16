# TC Auto-Generation Tool — Implementation Plan

## Overview

Automated test case generation tool for ASPICE SWE.6.
Input/output: `.xlsx` (Test Case Specification & Result sheet).
Architecture: Python backend + Next.js frontend (shadcn/ui).

---

## Risk Assessment

| Risk | Level | Mitigation |
|------|-------|------------|
| Claude API returns invalid JSON | HIGH | JSON parse retry + structured output schema |
| Excel formatting preservation (merged cells, formulas) | HIGH | openpyxl writes only specified columns |
| Spec matching accuracy | MEDIUM | Layer 1 PDM exact match first, Layer 2 AI for unmatched only |
| Token cost overrun | MEDIUM | Dry run estimation + budget cap + batch mode |
| Large file performance | LOW | Streaming read + batch API calls |

---

## Phases

### Phase 1: Project Skeleton & Infrastructure

> Setup project structure, dev environment, CI basics.

**Files to create:**

```
tc-generator/
├── src/                  # Python backend
├── app/                  # Next.js frontend
├── tests/                # pytest
├── output/
├── framework/
├── spec-index/
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── RULES.md
```

**Steps:**

- [ ] `git init` + `.gitignore` (.env, output/, __pycache__/, node_modules/)
- [ ] Python env: `pyproject.toml` (anthropic, openpyxl, pdfplumber, python-docx, python-dotenv, pytest)
- [ ] Next.js app: `create-next-app` with TypeScript + Tailwind + shadcn/ui
- [ ] `.env.example` with `ANTHROPIC_API_KEY=`
- [ ] Create `CLAUDE.md` for project-level instructions
- [ ] Create empty directory structure (output/, framework/, spec-index/)

**Done criteria:** `pytest` runs (0 tests), `npm run dev` starts without error.

---

### Phase 2: Excel Parser (RULES.md §10)

> Read TC xlsx, output structured JSON.

**Files:** `src/parser.py`, `tests/test_parser.py`

**Steps:**

- [ ] Write tests for parser (TDD RED)
- [ ] Read `Test Case Specification&Result` sheet, header Row 9, data Row 10+
- [ ] Read `Product Document` sheet Row 3 Col B → project name
- [ ] Parse Test Group from filename (`_SWQT_{TestGroup}_{date}.xlsx`)
- [ ] Output JSON structure (each row with col D, I, J, K, L, M, N, P, Q)
- [ ] Detect column fill status (which columns already have values)
- [ ] All tests pass (TDD GREEN)
- [ ] Refactor if needed

**Done criteria:** Correctly parses sample xlsx, extracts project name, test group, row count.

---

### Phase 3: TC ID Generator (RULES.md §2.1, §2.2)

> Generate `{project}-{group_abbr}-{sequence}` format IDs.

**Files:** `src/id_generator.py`, `tests/test_id_generator.py`

**Steps:**

- [ ] Write tests for ID generator (TDD RED)
- [ ] Generate abbreviation from Test Group name (`DeviceManager` → `DMS`)
- [ ] Generate 3-digit zero-padded sequence starting from 001
- [ ] Handle multiple TCs from same Req ID (distinct TC IDs)
- [ ] Incremental mode: continue from existing max sequence
- [ ] All tests pass (TDD GREEN)
- [ ] Refactor if needed

**Done criteria:** IDs follow `newR1L-DMS-001` format, no duplicates, monotonically increasing.

---

### Phase 4: Spec Matcher (RULES.md §2.4)

> Match Test Items to SYS1 spec requirements, fill Col N.

**Files:** `src/spec_matcher.py`, `tests/test_spec_matcher.py`

**Steps:**

- [ ] Write tests for spec matcher (TDD RED)
- [ ] **Layer 1 — PDM code exact match (programmatic, no AI):**
  - [ ] Parse SYS1 xlsx Basic Report sheet → build PDM code index
  - [ ] Regex extract PDM codes from Test Item (PDM, PDMS, MPDM, TD, DNDS, PDEE, APAC, PSR patterns)
  - [ ] Match → fill Col N with Source ID
- [ ] Handle multiple matches (semicolon-separated)
- [ ] Track unmatched rows for Layer 2 (AI, integrated in Phase 7)
- [ ] All tests pass (TDD GREEN)
- [ ] Refactor if needed

**Done criteria:** Layer 1 correctly matches PDM codes, outputs Source ID format.

> **Note:** Phase 2, 3, 4 can be developed in parallel — they have no dependencies on each other.

---

### Phase 5: Spec Document Parser (RULES.md §14.5, §14.6)

> Parse Slot C supplementary documents (PDF/DOCX/XLSX).

**Files:** `src/spec_parser.py`, `tests/test_spec_parser.py`

**Steps:**

- [ ] Write tests for spec parser (TDD RED)
- [ ] PDF parser (pdfplumber): extract text per page + PDM code index
- [ ] DOCX parser (python-docx): split by Heading styles + PDM code index
- [ ] XLSX parser (openpyxl): read rows + PDM code index
- [ ] Auto-detect format (extension + magic bytes)
- [ ] Merge SYS1 index (Slot B) + Slot C index → `spec_index.json`
- [ ] All tests pass (TDD GREEN)
- [ ] Refactor if needed

**Done criteria:** Each format correctly parsed, PDM codes extracted, merged index produced.

---

### Phase 6: Test Set Grouper (RULES.md §2.3)

> AI-cluster Test Items into sub-feature groups.

**Files:** `src/grouper.py`, `tests/test_grouper.py`

**Steps:**

- [ ] Write tests for grouper (TDD RED)
- [ ] First run: send all Test Items to Claude → return grouping suggestion
- [ ] Output `framework.json`: `{ "Test Set Name": [Req ID patterns] }`
- [ ] Subsequent runs: read confirmed `framework.json` (no AI needed)
- [ ] Generate Test Case Framework sheet data (Col A: Group, Col B: Set, Col C: count)
- [ ] All tests pass (TDD GREEN)
- [ ] Refactor if needed

**Done criteria:** Produces meaningful sub-feature groups, outputs framework.json.

---

### Phase 7: Prompt Builder & Generator (RULES.md §12)

> Assemble prompts, call Claude API, parse responses.

**Files:** `src/prompt_builder.py`, `src/generator.py`, `tests/test_prompt_builder.py`, `tests/test_generator.py`

**Steps:**

- [ ] Write tests for prompt builder (TDD RED)
- [ ] Assemble system prompt (ASPICE SWE.6 writer) + user prompt (rules §3-§5)
- [ ] Inject spec context per TC (matched PDM segment only, minimal tokens)
- [ ] Tests pass for prompt builder (TDD GREEN)
- [ ] Write tests for generator (TDD RED)
- [ ] Batch mode: N TCs per API call (configurable, default 5)
- [ ] API call with retry (max 2 retries per TC)
- [ ] JSON parse + error handling (invalid JSON → retry with stricter prompt)
- [ ] Token tracking (input/output tokens + cost calculation)
- [ ] Budget cap check (pause if approaching limit)
- [ ] Model selection: Sonnet 4.6 (default) / Haiku 4.5 (budget)
- [ ] Rate limiting: 0.5s delay between calls
- [ ] Integrate Layer 2 spec matching (AI semantic match for unmatched rows from Phase 4)
- [ ] Tests pass for generator (TDD GREEN)
- [ ] Refactor if needed

**Done criteria:** Generates valid TC JSON per requirement, tracks cost, respects budget.

---

### Phase 8: Validator (RULES.md §8)

> Programmatic validation of all generated fields. No AI.

**Files:** `src/validator.py`, `tests/test_validator.py`

**Steps:**

- [ ] Write tests for each validation rule (TDD RED)
- [ ] §8.1 Test Item format: `→` separator, parentheses wrap, blank line separation
- [ ] §8.2 Pre-Condition: no action verbs, numbered list or `NA`, no obvious states
- [ ] §8.3 Test Procedure: numbered list, purpose phrase per step, Final Step has verification verb, no vague verbs, step count ≥ 2
- [ ] §8.4 Expected Result: numbered list, count = procedure step count, no vague language, concrete final result
- [ ] §8.5 TC ID: format match, monotonic sequence, no duplicates
- [ ] §8.6 Design Method: exact match against 9 valid values
- [ ] §8.7 Priority: one of High/Medium/Low/NA
- [ ] Return structured result: pass/fail/warning per check with details
- [ ] All tests pass (TDD GREEN)
- [ ] Refactor if needed

**Done criteria:** All 7 validation categories implemented, returns actionable results.

---

### Phase 9: Excel Writer (RULES.md §10.3)

> Write generated results back to xlsx.

**Files:** `src/writer.py`, `tests/test_writer.py`

**Steps:**

- [ ] Write tests for writer (TDD RED)
- [ ] Write only specified columns: F, G, H, I (append), J, K, L, M, N, P, Q
- [ ] Preserve all original formatting, merged cells, formulas
- [ ] Set `alignment.wrap_text = True` for generated cells
- [ ] Use `\n` for in-cell line breaks
- [ ] Populate Test Case Framework sheet
- [ ] Output as `{input_filename}_generated.xlsx` in output/ directory
- [ ] All tests pass (TDD GREEN)
- [ ] Refactor if needed

**Done criteria:** Output xlsx preserves original formatting, generated content in correct columns.

---

### Phase 10: CLI Entry Point

> Command-line interface tying all modules together.

**Files:** `src/main.py`

**Steps:**

- [ ] Mode A: Full Generation (all rows, all columns)
- [ ] Mode B: Incremental (skip rows with existing TC ID)
- [ ] Mode C: Regenerate Specific (by row numbers or Req IDs)
- [ ] `--dry-run`: show estimated cost without calling API
- [ ] `--model`: select model (sonnet / haiku)
- [ ] `--batch-size`: set batch size (1 / 5 / 10)
- [ ] `--input`: TC xlsx path (required)
- [ ] `--sys1`: SYS1 spec xlsx path (optional)
- [ ] `--spec`: supplementary spec document path (optional)
- [ ] Progress output to terminal
- [ ] End-to-end test with sample file

**Done criteria:** `python src/main.py --input sample.xlsx --dry-run` runs successfully.

> **Milestone: Backend complete.** All Python modules functional via CLI.

---

### Phase 10.5: Job State Manager (Backend Enhancement)

> Manage per-row review state, support inline edit + re-validate + single TC regenerate.

**Files:** `src/job_manager.py`, `tests/test_job_manager.py`

**Problem:** Current backend is a one-shot pipeline (generate all -> write all). The Review page needs:
1. Track each row's status: `pending` / `accepted` / `edited` / `rejected` / `flagged`
2. Allow editing generated fields and re-validating without re-calling API
3. Regenerate only rejected rows (single TC or batch)
4. Export only accepted/edited rows
5. Persist job state to JSON for session recovery

**Job JSON structure (per row):**

```json
{
  "row_num": 10,
  "req_id": "SWE1-HMI-DM-001-01",
  "tc_id": "newR1L-DMR-001",
  "original": { "test_item": "...", "test_procedure": "...", "expected_result": "..." },
  "generated": { "test_item_rewrite": "...", "pre_conditions": "...", ... },
  "edited": null,
  "validation": { "status": "pass", "issues": [] },
  "review_status": "pending",
  "generation_history": [
    { "timestamp": "...", "model": "...", "cost": 0.003, "source": "ai" }
  ]
}
```

**Steps:**

- [ ] Write tests for job manager (TDD RED)
- [ ] `create_job()` — initialize job JSON from parsed xlsx data
- [ ] `save_job()` / `load_job()` — persist to / read from JSON file
- [ ] `update_row_status()` — change review_status (pending/accepted/edited/rejected/flagged)
- [ ] `edit_row()` — store user edits in `edited` field, re-run validator, update validation
- [ ] `get_rows_by_status()` — filter rows by review_status
- [ ] `get_exportable_rows()` — return accepted + edited rows with final content
- [ ] `get_job_stats()` — count per status
- [ ] All tests pass (TDD GREEN)
- [ ] Refactor if needed

**Review workflow supported:**

```
Generate -> all rows status = "pending"
  |
  User reviews each row:
  |  Accept  -> status = "accepted" (use generated content)
  |  Edit    -> store edits in "edited" field -> re-validate -> status = "edited"
  |  Reject  -> status = "rejected" -> regenerate -> status = "pending" (new cycle)
  |  Flag    -> status = "flagged" (skip for now)
  |
Export -> write accepted + edited rows to xlsx
```

**Done criteria:** Job state round-trips through JSON. Edit triggers re-validation. Export filters by status.

---

### Phase 11: Next.js Frontend (RULES.md §14)

> 5-page dashboard UI. Windows 95/98 style with 98.css + Remix Icon.
> Full spec: `docs/FRONTEND_PLAN.md`

**Files:** `frontend/` directory

#### Setup (partially done)

- [x] Next.js 16 + TypeScript created in `frontend/`
- [x] 98.css installed (`0.1.21`)
- [x] `@remixicon/react` installed (`4.9.0`)
- [x] Tailwind CSS v4 installed
- [x] Page route directories created: `upload/`, `configure/`, `generate/`, `review/`, `export/`
- [x] `styles/win95.css` created with desktop, taskbar, window, dialog styles
- [x] `public/icons/` directory created
- [ ] `app/layout.tsx` — still default Next.js template, needs 98.css + teal desktop bg
- [ ] `app/page.tsx` — still default Next.js template, needs Win95 desktop with TC Generator icon

#### Shared Components — Desktop

- [ ] `components/desktop/Desktop.tsx` — teal background + icon grid
- [ ] `components/desktop/DesktopIcon.tsx` — double-click to open app
- [ ] `components/desktop/Taskbar.tsx` — Start button + page tabs + clock
- [ ] `components/desktop/StartMenu.tsx` — navigation menu

#### Shared Components — Window

- [ ] `components/window/AppWindow.tsx` — 98.css window frame + title bar
- [ ] `components/window/TitleBar.tsx` — title text + min/max/close buttons
- [ ] `components/window/StatusBar.tsx` — window bottom status info

#### Shared Components — Retro UI

- [ ] `components/retro/RetroButton.tsx`
- [ ] `components/retro/RetroProgress.tsx`
- [ ] `components/retro/RetroTable.tsx`
- [ ] `components/retro/RetroTabs.tsx`
- [ ] `components/retro/RetroTreeView.tsx`
- [ ] `components/retro/RetroDialog.tsx`
- [ ] `components/retro/RetroSelect.tsx`
- [ ] `components/retro/RetroCheckbox.tsx`

#### Lib & Hooks

- [ ] `lib/types.ts` — Job, TcRow, Config TypeScript types
- [ ] `lib/constants.ts` — shared constants
- [ ] `hooks/useJob.ts` — job state context
- [ ] `hooks/usePython.ts` — call Python backend via API routes

#### Page 1 — Upload

- [ ] Three file upload slots (TC xlsx / SYS1 xlsx / Spec doc)
- [ ] Drag-and-drop file input with Remix Icon
- [ ] Auto-detect metadata after upload (project name, test group, row count, fill status)
- [ ] Summary card with detected metadata
- [ ] File type validation (.xlsx, .pdf, .docx)
- [ ] [Next] button (disabled until Slot A uploaded)

#### Page 2 — Configure

- [ ] Test Set grouping preview (RetroTreeView)
- [ ] Drag-and-drop to reassign TCs between groups
- [ ] Spec matching preview table (Layer 1 green / Layer 2 yellow)
- [ ] Manual override for spec matching
- [ ] Generation scope checkboxes per column
- [ ] Model selection (Sonnet / Haiku)
- [ ] Batch size selector (1 / 5 / 10)
- [ ] Save configuration as job JSON

#### Page 3 — Generate

- [ ] Progress bar (RetroProgress, X / N TCs)
- [ ] Live log textarea (monospace, auto-scroll)
- [ ] Pause / Resume / Cancel controls
- [ ] Running cost display (tokens + USD)
- [ ] Error collection for failed TCs
- [ ] Auto-transition dialog on completion

#### Page 4 — Review

- [ ] Table view with expandable rows (RetroTable)
- [ ] Side-by-side original vs generated diff
- [ ] Per-row actions: Accept / Edit / Reject / Flag (Remix Icons)
- [ ] Inline editing for generated fields
- [ ] Validation sidebar (red/yellow/green per check)
- [ ] Filters: validation status, Test Set, review status
- [ ] Bulk actions: accept all passing, regenerate rejected, export accepted

#### Page 5 — Export

- [ ] Export scope selector (all / accepted / by Test Set)
- [ ] Output format choice (new file vs overwrite)
- [ ] Column include/exclude checkboxes
- [ ] Framework sheet toggle
- [ ] Download link for generated xlsx

**Done criteria:** All 5 pages render with Win95 style, navigation flow works end-to-end.

---

### Phase 12: Frontend ↔ Backend Integration

> API routes connecting Next.js to Python backend.

**Files:** `app/src/app/api/` routes

**Steps:**

- [ ] `POST /api/parse` — upload xlsx → call parser.py → return JSON
- [ ] `POST /api/group` — call grouper.py → return framework
- [ ] `POST /api/match` — call spec_matcher.py → return matches
- [ ] `POST /api/generate` — call generator.py → stream progress via SSE
- [ ] `POST /api/validate` — call validator.py → return results
- [ ] `POST /api/export` — call writer.py → return download URL
- [ ] Error handling for all routes
- [ ] E2E test: upload → configure → generate → review → export

**Done criteria:** Full workflow works end-to-end through the browser.

---

## Execution Order

```
Phase 1  (Skeleton)
   │
   ├── Phase 2  (Parser)  ──┐
   ├── Phase 3  (ID Gen)  ──┼── can run in parallel
   └── Phase 4  (Matcher) ──┘
          │
      Phase 5  (Spec Doc Parser)
          │
      Phase 6  (Grouper)
          │
      Phase 7  (Prompt + Generator)
          │
      Phase 8  (Validator)
          │
      Phase 9  (Writer)
          │
      Phase 10 (CLI)  ← backend complete milestone
          │
      Phase 11 (Frontend)
          │
      Phase 12 (Integration)
```

---

## Complexity Estimate

| Phase | Complexity | Files |
|-------|-----------|-------|
| 1. Skeleton | Low | config only |
| 2. Parser | Medium | 1 src + 1 test |
| 3. ID Generator | Low | 1 src + 1 test |
| 4. Spec Matcher | Medium | 1 src + 1 test |
| 5. Spec Doc Parser | Medium | 1 src + 1 test |
| 6. Grouper | Medium | 1 src + 1 test |
| 7. Prompt + Generator | **High** | 2 src + 2 test |
| 8. Validator | Medium | 1 src + 1 test |
| 9. Writer | Medium | 1 src + 1 test |
| 10. CLI | Low | 1 src |
| 10.5. Job State Manager | Medium | 1 src + 1 test |
| 11. Frontend | **High** | ~15 files |
| 12. Integration | Medium | ~5 API routes |

---

## Progress Tracker

| Phase | Status | Date Started | Date Completed |
|-------|--------|-------------|----------------|
| 1. Skeleton | ✅ Done | 2026-04-16 | 2026-04-16 |
| 2. Parser | ✅ Done | 2026-04-16 | 2026-04-16 |
| 3. ID Generator | ✅ Done | 2026-04-16 | 2026-04-16 |
| 4. Spec Matcher | ✅ Done | 2026-04-16 | 2026-04-16 |
| 5. Spec Doc Parser | ✅ Done | 2026-04-16 | 2026-04-16 |
| 6. Grouper | ✅ Done | 2026-04-16 | 2026-04-16 |
| 7. Prompt + Generator | ✅ Done | 2026-04-16 | 2026-04-16 |
| 8. Validator | ✅ Done | 2026-04-16 | 2026-04-16 |
| 9. Writer | ✅ Done | 2026-04-16 | 2026-04-16 |
| 10. CLI | ✅ Done | 2026-04-16 | 2026-04-16 |
| 10.5. Job State Manager | ✅ Done | 2026-04-16 | 2026-04-16 |
| 11. Frontend | 🔄 In progress | 2026-04-16 | |
| 12. Integration | ⬜ Not started | | |
