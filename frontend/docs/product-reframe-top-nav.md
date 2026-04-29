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

- run completion rate
- first successful run time
- template reuse rate
- rerun conversion rate
- weekly active workspaces

## 12.2 UX KPIs

- validation error rate
- abandonment rate by builder step
- run diagnosis time
- success after retry

---

## 13. Experiment Plan

## 13.1 A/B Test Themes

- Home layout emphasis (KPI-first vs action-first)
- Builder split layout (fixed preview vs collapsible preview)
- Run list detail mode (inline panel vs dedicated page)

## 13.2 Event Tracking

Core events:

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

---

## 17. Next Technical Deliverables

1. Route scaffold and AppShell implementation.
2. Common data table and filter primitives.
3. Builder state orchestration and step guards.
4. Observability and event instrumentation layer.
5. Migration guide from legacy navigation model.
