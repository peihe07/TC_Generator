# TC Generator — Frontend

Top-nav workspace for AI-driven test case generation. Built on Next.js 16 (App Router) + React 19 + TanStack Query + Zustand + Tailwind v4.

The legacy 98.css desktop has been removed; the current shell is the only entry point.

## Quick start

```sh
npm install
npm run dev          # starts at http://localhost:3000
```

Other scripts:

| Command | Purpose |
|---|---|
| `npm run dev` | Local dev server with hot reload |
| `npm run build` | Production build |
| `npm run typecheck` | `tsc --noEmit` |
| `npm run test:unit` | Vitest unit + adapter tests |
| `npm run test:e2e` | Playwright workspace smoke spec |
| `npm run test:e2e:ui` | Playwright UI mode |

## Routes

```
/                          Home (KPIs, Continue Draft, Recent Runs, Quick Actions)
/runs                      Runs list with filter + sortable table
/runs/[runId]              Run Detail (KPIs, token breakdown, rerun)
/run-builder               Run Builder (5-step flow + draft auto-save)
/templates                 Templates list (spec library)
/templates/[templateId]    Template detail + Use in New Run
/outputs                   Outputs library (multi-select compare)
/outputs/compare           Side-by-side metadata diff
/data                      Dataset registry derived from history + draft
/settings                  Workspace defaults + stats
```

Run Builder accepts these query params:

- `?step=<step>` — jump straight to data / configure / validate / execute / review
- `?from=<runId>` — start a draft as a Rerun of the given run
- `?edit=<runId>` — start a draft as Edit & Rerun of the given run
- `?templateId=<name>` — pre-fill `draft.configure.templateId`
- `?dataset=<jobId>` — placeholder reserved for dataset reuse (not wired yet)

## Architecture

```
app/
  layout.tsx                 root html (Space Mono via next/font)
  globals.css                tokens (colors / shadows / utility classes / skeleton shimmer)
  (workspace)/
    layout.tsx               wraps with AppShell
    page.tsx                 Home
    runs/, templates/, outputs/, data/, settings/, run-builder/
  api/                       proxy routes to backend (/api/jobs, /api/parse, /api/spec-library, etc.)

src/
  components/
    shell/                   AppShell, TopNav, CommandPalette, Skeleton, EmptyState, DevStoreExposer
    builder/                 BuilderShell + 5 step components (data / configure / validate / execute / review)
    home/, runs/, outputs/, templates/, data/, settings/   page-specific views
  store/                     5 zustand stores (jobStore, jobHistoryStore, builderDraftStore, commandPaletteStore, workspaceSettingsStore)
  services/                  jobAdapter (legacy backend wrapper) + runAdapter (UI view-model layer)
  lib/                       specLibrary, configureConstants, configurePreviewTypes, telemetry, costEstimate, logging
  __tests__/                 Vitest specs

e2e/
  workspace-smoke.spec.ts    Playwright smoke
```

### State layering

- `useJobStore` — current run state (rows, config, logs, stats). Mutated by Builder + ReviewStep.
- `useJobHistoryStore` — completed runs persisted to localStorage. Source of truth for Home / Runs / Outputs / Data.
- `useBuilderDraftStore` — current builder draft (id, step, data, configure, completed flags). Persisted.
- `useWorkspaceSettingsStore` — user defaults applied when starting a new draft.
- `useCommandPaletteStore` — open/closed flag for `Cmd/Ctrl+K`.

The `Run` view-model in `src/services/runAdapter.ts` wraps each `JobRecord` with derived status, formatted duration, formatted cost, etc. UI code should read `Run`, never `JobRecord` directly.

### Design tokens

See [`docs/design-tokens.md`](docs/design-tokens.md). Short version:

- Palette: Ink Black `#001524`, Stormy Teal `#15616D`, Papaya Whip `#FFECD1`, Vivid Tangerine `#FF7D00`, Brandy `#78290F`
- Font: Space Mono (`--font-space-mono`)
- Surfaces use translucent papaya + `backdrop-blur` and `box-shadow`; **no borders**
- Hover lifts via `translateY(-1px)` + deeper shadow; `prefers-reduced-motion` respected

### Telemetry

`src/lib/telemetry.ts` exposes `track(name, props)`. In dev/test, events also push to `window.__tcEvents` (capped 200) for Playwright assertions.

Currently wired:

| Event | Where |
|---|---|
| `home_new_run_click` | TopNav New Run, Home Quick Actions |
| `builder_step_next` | BuilderShell onNext |
| `builder_validation_fail` | ValidateStep critical-fail change |
| `run_execute_start` / `run_execute_success` / `run_execute_fail` | ExecuteStep |
| `run_retry_click` | RunDetailView Rerun + Edit & Rerun |
| `template_use_click` | TemplateDetailView |
| `output_compare_open` | OutputsView Compare CTA |

There is no backend collector yet; add a transport in `telemetry.ts` when ready.

## Backend dependencies

Frontend talks to the backend via Next API routes that proxy under `/api/`. Required endpoints:

- `POST /api/parse` — workbook upload + parse
- `POST /api/generate/stream`, `POST /api/quick-generate/stream` — streaming generation (SSE)
- `POST /api/jobs/:id/regenerate/stream`, `POST /api/jobs/:id/rerun/stream` — streaming reprocess
- `GET  /api/jobs/:id/usage` — Run Detail live usage
- `POST /api/group`, `POST /api/match` — Configure step previews
- `GET  /api/spec-library` — Templates list source
- `POST /api/export` + `GET /api/export/download/:id` — Review export
- `POST /api/review/suggest-fix` — Ask AI in Review step

See `app/api/_lib/backend.ts` for proxy setup and base-URL resolution.

## Notes for contributors

- Next.js 16 made `params` and `searchParams` Promises (since v15). Always `await` in page components. See [`docs/nextjs16-notes.md`](docs/nextjs16-notes.md).
- Don't reintroduce `border` on UI elements — use shadow + spacing instead (`docs/design-tokens.md`).
- The legacy 98.css world has been removed; if you spot stray `win95-*` tokens in CSS, they're safe to delete.
- Telemetry props are typed via `KnownEvents` in `src/lib/telemetry.ts`. Add new events there to keep callers strongly typed.
