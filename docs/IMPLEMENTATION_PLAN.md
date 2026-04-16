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

- Real generation still requires a valid `ANTHROPIC_API_KEY`

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
- Configure grouping preview wired to backend
- Configure exact matching preview wired to backend
- Parse and export smoke-tested end-to-end

---

## Open Work

### Priority 1 — Real API Validation

These are the highest-value remaining tasks because they validate the full system, not just local fallback behavior.

- [ ] Set a valid `ANTHROPIC_API_KEY` in the runtime environment
- [ ] Run full desktop flow with real generation:
  - Upload
  - Configure
  - Generate
  - Review
  - Export
- [ ] Re-run selective regenerate with real API output
- [ ] Capture any generator/prompt/validation mismatches found in real runs

### Priority 2 — Session Stability And Real-Run UX

- [ ] Optional `persist` middleware for long-running sessions
- [ ] Validate Configure previews against real user workbooks, not only fixtures
- [ ] Decide whether spec references should also be stored in frontend row state

### Priority 3 — Configure Page Refinements

- [ ] Allow manual override of grouped `testSet` assignments
- [ ] Decide final grouping strategy for rows without explicit `testSet`
- [ ] Add richer match diagnostics when the reference workbook is incompatible

### Priority 4 — Quick Generate Documentation And Validation

Quick Generate appears in the desktop and should be documented and validated consistently.

- [ ] Confirm current backend/frontend implementation status for Quick Generate
- [ ] Add or refresh docs for its request/response flow
- [ ] Add smoke validation if it remains an active feature

---

## Recommended Execution Order

1. Real API validation with a working Anthropic credential
2. Validate group / match preview behavior on real files
3. Session persistence and Configure refinements
4. Optional persistence and larger UX refinements

---

## Risks

| Risk | Level | Current mitigation |
|------|-------|--------------------|
| Anthropic credential missing or invalid | High | Proxy and stream paths tested separately; real generation blocked until valid key is available |
| Generated JSON or field quality drift | High | Validator already in place; real-run verification still required |
| Export mismatch between frontend review state and backend writer | Medium | Export proxy path already smoke-tested with accepted rows |
| Frontend state drift across modules | Medium | Shared Zustand stores + adapter now act as the single integration boundary |
| Long review sessions losing state | Medium | `persist` middleware deferred but identified |

---

## Notes

- Earlier sections from the original implementation checklist were removed because they described greenfield scaffolding work that is already complete.
- Outdated references to `shadcn/ui`, `*Window.tsx`, `usePythonAPI.ts`, and direct browser-to-Python calls have been removed from the current plan.
- This file should only describe active architecture and real remaining work.
