# Reframe — Definition of Done

Maps each blueprint §16 DoD criterion to current evidence in code & tests so we
can declare the reframe shipped.

| # | DoD Criterion | Status | Evidence |
|---|---|---|---|
| 1 | Users can complete end-to-end run via new builder | ✅ | `/run-builder` 5-step flow (`src/components/builder/BuilderShell.tsx`) wired to `data → configure → validate → execute → review`. Each step lives in `src/components/builder/steps/*` and is no longer routed through `/legacy`. Component tests: `ConfigureStep.spec.tsx`, `ValidateStep.spec.tsx`, `ReviewStep.spec.tsx`. |
| 2 | Users can resume draft after refresh or relogin | ✅ | `useBuilderDraftStore` persists draft to localStorage (`tc-generator-builder-draft`). BuilderShell auto-loads on mount; Home shows `ContinueDraft` panel when a draft exists. Tests: `useBuilderDraftStore.spec.ts`, `HomeView.spec.tsx > 有 draft 時 Continue Draft 區出現`. |
| 3 | Failed run can be diagnosed and rerun in ≤ 3 actions | ✅ | From `/runs`: (1) click run row → (2) inspect Validation Log + Timeline + Resolved Config → (3) click `Rerun` (`from=`) or `Edit & Rerun` (`edit=`). Builder accepts both query params and shows a banner. See `RunDetailView.tsx` and `BuilderShell.tsx`. |
| 4 | Templates can be created and reused in subsequent runs | ⚠️ Partial | Reuse: `/templates/[id]` `Use in New Run` CTA → builder pre-fills `draft.configure.templateId`; backend persists via `GenerateRequest.templateId`. Usage analytics live (`GET /api/spec-library/{name}/usage`). Deprecate flag shipped (`PATCH /api/spec-library/{name}` + `template_save` event + `Show deprecated` toggle in `/templates`). **Authoring brand-new templates (create / clone) is deferred** — needs embedding ingestion pipeline. |
| 5 | Outputs can be searched, previewed, and compared | ✅ | `/outputs` with multi-select up to 2; `Compare` CTA navigates to `/outputs/compare?a=&b=`. Compare view fetches `POST /api/outputs/compare` and renders TC Content Diff (added / removed / changed / unchanged). Preview = inspect `Run Detail` per output. **Inline file preview** (rendering xlsx contents in-browser) is not implemented; users download for full preview. |
| 6 | KPI telemetry is available for all key workflow milestones | ✅ | `src/lib/telemetry.ts` emits 10 events including `experiment_exposure`, batched POST to `/api/events`. Backend appends to `output/events.jsonl` (allowlist-validated, capped 4 KB / 100 batch). Home KPI cards now report Success Rate, Avg Successful Duration, Needs Attention, 7d Success — see `src/components/home/KpiCards.tsx`. |

## Acceptance gates

| Gate | Run | Result |
|---|---|---|
| Frontend typecheck | `npm run typecheck` | ✅ |
| Frontend unit tests | `npm run test:unit` | ✅ 18 files / 92 tests |
| Frontend e2e smoke | `npm run test:e2e` | ✅ 5/5 |
| Backend tests | `pytest tests/test_api_server.py` | ✅ 78/78 |
| Frontend production build | `npm run build` | ✅ |

## Post-release work shipped

- **Inline xlsx preview** — `GET /api/jobs/{id}/output-preview` + `/outputs/[runId]` page; OutputsView grew a Preview link per row.
- **Server-side validation log capture** — `_record_stream_validation_failure` hooks the four streaming paths (budget skip, strict-fail, generation tool error, regenerate/rerun fail). ReviewStep still posts client-side validations on mount as a backstop.
- **Dataset re-hydrate** — `GET /api/jobs/{id}/dataset` returns parsed rows in TcRow shape; BuilderShell consumes `?dataset=:jobId` to populate `useJobStore`, mark Data step complete, and skip ahead to Configure.
- **Template changelog + version** — `_spec_manifest_path()` env override + `POST /api/spec-library/{name}/changelog` (loopback only); TemplateDetailView ships a Changelog timeline + add-entry form.
- **Bulk download** — `POST /api/outputs/bulk-download` streams a zip; OutputsView supports >2 selection with a `Download zip` toolbar button.
- **Experiment analytics dashboard** — `GET /api/events/aggregate` powers the Settings Experiments panel.
- **Workspaces (C-S1 + C-S2)** — local label-only workspaces with TopNav switcher, plus backend tagging via `X-Workspace-Id` for `/api/parse`, `/api/generate`, `/api/events`, `/api/events/aggregate`. Record / draft / event objects all carry `workspaceId`.
- **Runs bulk actions** — multi-select on `/runs` with archive / unarchive / CSV export; `archived` flag persisted in `useJobHistoryStore`; `Show archived` filter.
- **Data quality preview** — `/data/[jobId]` (`DatasetDetailView`) shows column coverage % and quality alerts (missing reqId, dup reqs, missing testItem, missing testSet).
- **DataTable primitive** — reusable `src/components/ui/DataTable.tsx` with column-def + sortBy + empty state, adopted by OutputPreviewView.
- **A/B experiments expansion** — added `runs_detail_mode` and `builder_split_layout` definitions with deterministic bucketing + exposure tracking; ConfigureStep + Grouping + SpecMatching react to the builder variant.
- **Template deprecate flow** — `PATCH /api/spec-library/{name}` deprecate flag, `template_save` telemetry event, TemplatesView `Show deprecated` toggle + badge, TemplateDetailView `DeprecateToggle`.
- **Deeper KPI dashboard** — `/api/events/aggregate` extended with templateUses / retryClicks / comparesOpened / builderStepNexts / validationFails buckets and 4 derived rates; `KpiDashboard` panel embedded in Settings.

## Open follow-ups

- Authoring brand-new templates (create / clone) — needs an embedding ingestion pipeline. Deprecate is shipped; changelog endpoint patches existing manifest entries.
- Hard isolation (S3): per-workspace SQLite DB / output dir, workspace-aware authentication.
- Promote A/B framework beyond `home_layout_emphasis` once the first experiment yields a decision.
- `/legacy` is fully removed; if a regression escapes, only e2e + unit tests catch it.
