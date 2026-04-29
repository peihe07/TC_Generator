# Product Reframe Blueprint (No-Sidebar, Top Navigation)

## 1. Objective

Transform the current frontend from a "single-run utility" into a "workflow workspace" where users can:

1. Prepare and validate data.
2. Configure reusable generation rules.
3. Run jobs with observable progress.
4. Review, compare, and export outputs.
5. Re-run and iterate with historical context.

---

## 2. Product Positioning

**Positioning statement**

> A workflow-centric test-case generation workspace that unifies data ingestion, configuration, execution, review, and output versioning.

**Target users**

- New users: need guided flows and guardrails.
- Power users: need speed, repeatability, and batch operations.
- Team users: need traceability and shareable templates.

---

## 3. Information Architecture (No Sidebar)

## 3.1 Global Navigation Model

Use a fixed top navigation instead of left sidebar.

- Left: Brand + workspace switcher
- Center: primary destinations
  - Home
  - Runs
  - Templates
  - Outputs
  - Data
- Right:
  - Global search
  - Primary CTA (`New Run`)
  - User menu

## 3.2 Command Palette

Trigger by `Cmd/Ctrl + K`.

Functions:

- Navigate: go to pages and entities.
- Action: new run, upload file, duplicate template.
- Search: run ID, output file, tag, template.

This preserves power-user efficiency without persistent sidebar complexity.

---

## 4. Sitemap

1. `/` Home
2. `/runs` Runs list
3. `/runs/:runId` Run detail
4. `/run-builder` Run builder shell
5. `/run-builder/:draftId/:step` Builder step route
6. `/templates` Templates list
7. `/templates/:templateId` Template detail
8. `/outputs` Output library
9. `/outputs/compare` Output comparison
10. `/data` Data sources
11. `/settings` Workspace settings

---

## 5. Page-Level Specifications

## 5.1 Home

Purpose: provide status overview and immediate action path.

Sections:

- KPI cards (success rate, avg duration, fail count)
- Continue draft panel
- Recent runs table (compact)
- Quick actions (`New Run`, `Use Template`, `Upload Data`)
- Issue feed (validation hot spots and recent failures)

Primary metric:

- Click-through rate from Home to successful run.

## 5.2 Runs List

Purpose: operational visibility and job management.

Capabilities:

- Filters: status, date range, template, owner, tags
- Sort: start time, duration, output count
- Bulk actions: retry, archive, export metadata
- Row quick actions: view, duplicate, rerun with edits

Primary metric:

- Retry success rate and mean time to recovery.

## 5.3 Run Detail

Purpose: traceability and troubleshooting.

Sections:

- Header summary (run ID, status, trigger source)
- Timeline (queued -> running -> completed/failed)
- Config snapshot (resolved template + overrides)
- Validation logs and error context
- Output artifacts and download links
- One-click `Rerun` and `Edit & Rerun`

Primary metric:

- Time to diagnose failed runs.

## 5.4 Run Builder

Purpose: complete one run with high confidence and low friction.

Flow:

1. Select Data
2. Configure Rules
3. Validate
4. Execute
5. Review

UX rules:

- Auto-save drafts.
- Step guardrails (block execution on critical validation errors).
- Keep preview visible when feasible.
- Persist user context after refresh.

Primary metric:

- First-attempt run completion rate.

## 5.5 Templates

Purpose: reuse and standardize configuration.

Capabilities:

- Create, clone, version, deprecate
- Changelog per template version
- Usage analytics (runs created by template)

Primary metric:

- Template reuse rate.

## 5.6 Outputs

Purpose: output management and iterative quality checks.

Capabilities:

- Search/filter by run, tag, date, owner
- Output preview
- Compare two outputs (diff view)
- Export bundle and metadata

Primary metric:

- Output comparison usage rate and re-run conversion.

## 5.7 Data

Purpose: ingestion reliability and schema visibility.

Capabilities:

- Dataset upload registry
- Schema preview and compatibility hints
- Data quality alerts

Primary metric:

- Validation error reduction over time.

---

## 6. Text Wireframe (Key Screens)

## 6.1 Home Wireframe

- Top bar
- KPI row (4 cards)
- Left column
  - Continue Draft
  - Recent Runs
- Right column
  - Quick Actions
  - Issue Feed

## 6.2 Runs Wireframe

- Filter bar
- Data table
- Optional right-side quick detail panel on row click
- Sticky bulk-action footer when rows selected

## 6.3 Builder Wireframe

- Stepper header
- Main split layout
  - Left: form sections
  - Right: data/config preview and validation results
- Sticky action footer
  - Back
  - Save Draft
  - Next/Execute

## 6.4 Run Detail Wireframe

- Header summary
- Timeline panel
- Config snapshot accordion
- Validation logs
- Output cards

---

## 7. Route Map and Access Rules

## 7.1 Route Groups

- Public shell routes
  - `/`
  - `/runs`
  - `/templates`
  - `/outputs`
  - `/data`
- Entity routes
  - `/runs/:runId`
  - `/templates/:templateId`
- Workflow routes
  - `/run-builder/:draftId/:step`

## 7.2 Navigation Policies

- Keep top nav stable across all routes.
- Use breadcrumb for deep pages.
- Preserve filter/query in URL for shareability.

---

## 8. Frontend Component Tree (Reference)

```text
AppShell
├── TopNav
│   ├── WorkspaceSwitcher
│   ├── PrimaryNav
│   ├── GlobalSearch
│   ├── NewRunButton
│   └── UserMenu
├── CommandPalette
├── PageContainer
│   ├── HomePage
│   ├── RunsPage
│   ├── RunDetailPage
│   ├── RunBuilderPage
│   ├── TemplatesPage
│   ├── TemplateDetailPage
│   ├── OutputsPage
│   └── DataPage
└── GlobalToasts
```

Run Builder sub-tree:

```text
RunBuilderPage
├── BuilderStepper
├── BuilderContent
│   ├── DataStepPanel
│   ├── ConfigureStepPanel
│   ├── ValidateStepPanel
│   ├── ExecuteStepPanel
│   └── ReviewStepPanel
└── BuilderActionBar
```

---

## 9. State Model

## 9.1 Client State

- UI state
  - active step
  - panel collapse/expand
  - table selection
- Draft state
  - selected dataset
  - configuration payload
  - validation result snapshot

## 9.2 Server State

- runs list and detail
- templates list and detail
- outputs list and compare result
- dataset metadata

## 9.3 Persistence

- URL query for shareable filters
- local storage for non-sensitive UI preferences
- server draft checkpoint for resumable builder flow

---

## 10. API Contract Suggestions

1. `GET /runs`
2. `GET /runs/:runId`
3. `POST /runs`
4. `POST /runs/:runId/rerun`
5. `GET /templates`
6. `POST /templates`
7. `GET /outputs`
8. `POST /outputs/compare`
9. `GET /datasets`
10. `POST /datasets/upload`

Response principles:

- Stable IDs for all entities
- Explicit status enums
- Pagination and cursor support
- Include timestamps and actor metadata

---

## 11. Interaction and UX Rules

1. Never lose user work (auto-save + restore).
2. Show system status at every critical operation.
3. Block destructive actions behind confirmation.
4. Make failed states actionable (`retry`, `edit`, `duplicate`).
5. Keep critical actions reachable within 1-2 interactions.

---

## 12. KPI Framework

## 12.1 Product KPIs

| KPI | UI / Event Source | Current Definition |
|---|---|---|
| Run success rate | Home KPI, `run_execute_success`, `run_execute_fail` | `completed / finished`, excluding actively running runs |
| Avg successful duration | Home KPI, `run_execute_success.durationMs` | Average duration for completed runs only |
| Needs attention | Home KPI, run history status | `failed + partial` runs |
| 7d success | Home KPI, run history timestamps | Success rate for runs active in the last 7 days |
| First successful run time | Event stream | Time from first `home_new_run_click` or builder start to first `run_execute_success` |
| Template reuse rate | `template_use_click` | Template-backed runs / all started runs |
| Rerun conversion rate | `run_retry_click`, run terminal events | Successful reruns / rerun clicks |

## 12.2 UX KPIs

| KPI | Event Source | Current Definition |
|---|---|---|
| Validation error rate | `builder_validation_fail`, `builder_step_next` | Validation failures / validation step visits |
| Abandonment by builder step | `builder_step_next`, draft resume state | Last recorded step before session exit |
| Run diagnosis time | Run Detail open to `run_retry_click` | Median time between failed-run inspection and next action |
| Success after retry | `run_retry_click`, terminal run events | Successful retry runs / retry attempts |
| Output comparison engagement | `output_compare_open` | Compare opens / completed runs |

## 12.3 KPI Display Rules

1. Home KPI cards use local run history only, so the dashboard remains useful without a backend analytics collector.
2. Duration cards use completed runs only; partial and failed runs feed `Needs Attention` instead of skewing performance.
3. Recent health uses a 7-day rolling window anchored to run `finishedAt` when present, otherwise `startedAt`.
4. Telemetry events carry the active experiment assignment under `experiments`, allowing KPI slices by variant.

---

## 13. Experiment Plan

## 13.1 A/B Test Themes

| Experiment | Status | Variants | Decision Metric |
|---|---|---|---|
| `home_layout_emphasis` | Implemented | `kpi_first`, `action_first` | New-run click rate, successful run completion, 7d success |
| Builder split layout | Planned | Fixed preview, collapsible preview | Validation failure rate, step abandonment |
| Run list detail mode | Planned | Inline panel, dedicated page | Diagnosis time, retry conversion |

Implementation notes:

1. Client assignments are persisted in `localStorage` under `tc:experiments:v1`.
2. Deterministic bucketing uses the experiment key plus subject id; explicit overrides are supported with `?exp_home_layout_emphasis=action_first`.
3. `experiment_exposure` fires on Home mount and every tracked event includes the active assignment map.
4. Experiments must define one default/control variant and keep the control behavior shippable.

## 13.2 Event Tracking

Core events:

- `experiment_exposure`
- `home_new_run_click`
- `builder_step_next`
- `builder_validation_fail`
- `run_execute_start`
- `run_execute_success`
- `run_execute_fail`
- `run_retry_click`
- `template_save`
- `output_compare_open`

---

## 14. Rollout Plan

## Phase 1 (Foundation)

- Introduce AppShell with top nav.
- Deliver Home and Runs list.
- Keep legacy flow available as fallback.

## Phase 2 (Workflow)

- Launch Run Builder v1 with draft auto-save.
- Add Run Detail timeline and rerun actions.

## Phase 3 (Reuse + Output)

- Launch Templates center with versioning.
- Launch Outputs compare and library operations.

## Phase 4 (Optimization)

- Add command palette actions expansion.
- Complete KPI dashboard and UX tuning.

---

## 15. Risks and Mitigations

1. Navigation discoverability risk
   - Mitigation: onboarding hints + command palette education.
2. Top-nav overcrowding risk
   - Mitigation: keep 5 primary destinations max.
3. Data-heavy performance risk
   - Mitigation: virtualization, pagination, and lazy loading.
4. Builder complexity risk
   - Mitigation: progressive disclosure and template-first defaults.

---

## 16. Definition of Done (Reframe Release)

1. Users can complete end-to-end run via new builder.
2. Users can resume draft after refresh or relogin.
3. Failed run can be diagnosed and rerun in <= 3 actions.
4. Templates can be created and reused in subsequent runs.
5. Outputs can be searched, previewed, and compared.
6. KPI telemetry is available for all key workflow milestones.
7. Home A/B assignment persists across reloads and can be overridden for QA.
8. KPI cards match the definitions in section 12 and have unit coverage for edge cases.

## 16.1 DoD Acceptance Matrix

| Area | Acceptance Check | Verification |
|---|---|---|
| Navigation | Top nav reaches Home, Runs, Templates, Outputs, Settings without dead ends | Playwright smoke + manual pass |
| Run builder | User can complete a new run and refresh without losing draft state | Component tests + smoke scenario |
| Failure recovery | Failed or partial run exposes retry/edit path in <= 3 actions | Run Detail test + manual pass |
| Reuse | Template can be opened and used as the basis for a new run | Template detail test |
| Output review | Completed outputs can be opened and compared | Outputs test |
| Telemetry | Core workflow events include typed props and experiment assignment | `telemetry.spec.ts`, dev buffer |
| A/B framework | `home_layout_emphasis` persists assignment and supports URL override | `experiments.spec.ts`, HomeView test |
| KPI | Success, duration, attention, and 7d window use documented formulas | `runAdapter.test.ts` |
| Release evidence | Unit test suite, typecheck, and E2E/manual notes are attached to release notes | Release checklist |

---

## 17. Next Technical Deliverables

1. Route scaffold and AppShell implementation.
2. Common data table and filter primitives.
3. Builder state orchestration and step guards.
4. Observability and event instrumentation layer.
5. Migration guide from legacy navigation model.
