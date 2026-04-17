# TC Generator — Implementation Plan

## Overview

Automated test case generation tool for ASPICE SWE.6.

Current architecture:

- Python backend and CLI for core processing
- Next.js desktop frontend with Win95-style window workflow
- Same-origin Next.js proxy routes between browser and Python backend

This file is now a **living status + next-step plan**, not the original greenfield scaffold checklist.

---

## Current State

### Backend

Implemented and tested:

- parser
- id generator
- spec matcher
- spec document parser
- grouper
- prompt builder
- generator
- validator
- writer
- job manager
- FastAPI integration layer
- CLI entry point

Current backend validation:

- `pytest -q` passing
- parse/export paths verified through frontend proxy flow

### Frontend

Implemented and active:

- Desktop shell: `Desktop`, `Taskbar`, `WindowManager`, `AppWindow`
- Zustand stores: `useJobStore`, `useWindowStore`
- Shared integration layer: `services/jobAdapter.ts`
- Next.js proxy routes:
  - `POST /api/parse`
  - `POST /api/group`
  - `POST /api/match`
  - `POST /api/generate`
  - `GET /api/generate/stream`
  - `POST /api/jobs/[jobId]/regenerate/stream`
  - `POST /api/export`
  - `GET /api/export/download/[jobId]`
- Workflow modules:
  - Upload
  - Configure
  - Generate
  - Review
  - Export

Removed:

- legacy `*Window.tsx` implementation path
- direct browser-side Python API hooks (`usePythonAPI.ts`, `useSSE.ts`)
- stale split-contract frontend API layer

Current frontend validation:

- `npx tsc --noEmit` passing
- parse/generate/regenerate/export proxy routes exercised end-to-end
- group/match backend routes covered by API tests
- export download verified through same-origin proxy

Known environment dependency:

- Real generation requires a valid `OPENAI_API_KEY` (GPT-4.1 / GPT-5 family).
- SQLite job registry at `output/jobs.db` (path overridable via `TC_JOBS_DB`).

---

## Completed Milestones

### Core Milestone

- Backend modules complete
- CLI complete
- Review-aware job management complete

### Frontend Milestone

- Single-page desktop shell complete
- Centralized store + adapter architecture established
- Same-origin proxy architecture established
- Configure grouping + exact matching previews wired to backend
- Parse → generate → regenerate → export verified on real user workbooks

### Provider & Prompt Milestone

- Anthropic → OpenAI migration complete (openai SDK, JSON mode, auto prompt caching)
- ASPICE SWE.6 rules auto-loaded from `docs/*.md` into system prompt
- Hard constraints footer appended so the 1:1 mapping and `test_item_rewrite`
  rules are enforced with recency bias
- Single-call retry in `generate_single_tc` when Proc ≠ ER counts

### Runtime Milestone

- SQLite-backed `JOB_REGISTRY` (`SqliteJobStore`) — jobs survive restart
- In-memory mutations explicitly written back via `JOB_REGISTRY[id] = job`
- SSE stats stream now emits cache-read / cache-creation tokens for UI
- Parser tolerates bilingual sheet titles and filename suffixes
  (`拷貝`, `-1`, etc.)

### Frontend UX Milestone

- CostMeter shows Model / Input / Output / Cache W / Cache R / Hit-rate
- Workspace Manager in taskbar (save / rename / load / delete /
  JSON import / JSON export; persisted in `localStorage`)
- Job History menu in taskbar (lifetime cumulative cost, per-job record,
  persisted in `localStorage`)
- Review: batch Accept / Reject / Delete / Regenerate; word-level diff
  on pending regeneration; selectable + copy-safe read fields
- Desktop icons draggable with position persistence; windows auto-clamp
  back into viewport on mount and resize

---

## Open Work

### Priority 1 — Configure Refinements

- [x] Allow manual override of grouped `testSet` per row — inline editable table in Configure/Grouping tab
- [x] Grouping fallback strategy for rows without explicit `testSet`: existing → PDM code → REQ prefix → `Unassigned` (already in `_derive_test_set_name`)
- [ ] Add richer match diagnostics when a reference workbook is incompatible
- [x] Surface Spec Reference in Review read-only fields (`TcRow.specReference` + `StackedReadField` row; auto-hidden when empty)

### Priority 2 — Generator Quality Hardening

- [x] Auto-escalate model on second count-mismatch (e.g. `gpt-4.1-mini` → `gpt-4.1` → `gpt-5`). `MODEL_ESCALATION` table in `backend/generator.py`.
- [x] Retry on hard validator violations (`design_method` / `priority` invalid, empty `test_item_rewrite`). Soft warnings still surface in UI but don't trigger retry (cost control).
- [ ] Consider JSON Schema response_format to guard structure more strongly

### Priority 3 — Session & Data Durability

- [x] `useJobStore` wrapped in zustand `persist` middleware (key `tc-job-session`; only `jobMetadata / tcRows / config / stats` persisted)
- [x] SQLite `purge_older_than` + `vacuum` on backend startup (default 30 days; `TC_JOBS_MAX_AGE_DAYS` env var)
- [x] Job History TTL (90 days) + `MAX_RECORDS` cap; enforced on load and on every append

### Priority 4 — Test Coverage

- [x] SqliteJobStore regression tests (`tests/test_job_store.py` — round-trip, bytes payload, cross-instance persistence, mutation writeback semantics)
- [x] Playwright Workspace JSON round-trip (`frontend/e2e/workspace.spec.ts` — save → export → new → import → load)
- [x] 44-row stress test on real workbook — baseline recorded: $0.125 / 251s / cache hit 90.9% / 1:1 violations 1/44 (2.3%) with GPT-4.1-mini + retry + escalation

---

## Recommended Execution Order

1. Configure manual `testSet` override (highest-value UX gap)
2. Auto-escalate model on persistent count mismatch
3. Coverage gaps in E2E (workspace / sqlite / stress)
4. Session persistence + data rotation

---

## Risks

| Risk | Level | Current mitigation |
|------|-------|--------------------|
| OpenAI credential or billing tier unavailable | High | Build Tier 1 ≥ $5 required; verified via direct SDK call |
| 1:1 count rule violated by weaker model (GPT-4.1-mini) | Medium | Hard-constraints footer + one retry; validator surfaces residual cases; user can regen with stronger model |
| Generated JSON / field quality drift | Medium | Validator + normalizer + retry; Review module shows word-level diff on regen |
| Export mismatch between frontend review state and backend writer | Low | Export proxy smoke-tested; SQLite now round-trips export path |
| Long review sessions losing in-memory state | Low | Workspace manager + Job history persist to localStorage |
| Desktop icon / window position lost on refresh | Low | `desktop-icon-positions` localStorage + controlled window clamp |

---

## Notes

- Rules documentation (`docs/RULES.md`, `docs/API_CONTRACT.md`) and architecture
  diagrams (`docs/TC_Generator_Architecture_Diagrams.html`,
  `frontend/public/diagrams.html`) are synchronized with the OpenAI + SQLite
  architecture as of this revision.
- `docs/temp/` holds real user workbooks used for validation; excluded via
  `.gitignore`.
- `_HARD_CONSTRAINTS` in `backend/prompt_builder.py` is the authoritative summary of
  invariants LLM output must satisfy; keep it in sync when Rules change.
