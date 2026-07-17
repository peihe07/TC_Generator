# TC Generator

Automated test case generation tool for ASPICE SWE.6.

The project has two working surfaces:

- Python backend and CLI for parsing, generation, validation, and Excel writing
- Next.js desktop frontend for the upload -> configure -> generate -> review -> export workflow
- Optional modern Next.js UI variant under `frontend-modern/`, isolated from the legacy desktop app

## Project Status

The backend is being reworked into a grounded, KPI-measured pipeline. All work
below currently lives on `feat/m1-stage7-scorecard` and has **not** been merged
into `main` yet. Backend test baseline: **618 tests collected**. The full
per-session log lives in [`M1/PROGRESS.md`](M1/PROGRESS.md); this table is the
canonical summary.

### Milestones

| Milestone | Scope | Status |
|---|---|---|
| **M0** — Provider abstraction | `backend/providers/` (OpenAI + Anthropic + budget + factory), `set_provider` seam | Done |
| **M0b** — De-couple generator | `generator._chat` routes through the provider layer; `TC_LLM_BACKEND` env switch | Done |
| **M1** — Stage 7 KPI scorecard | `backend/scorecard.py`, `config/kpi_thresholds.json`, `--scorecard` CLI | Done |
| **M2** — Budget planner | `backend/budget_planner.py`, `--preflight` / `--calibrate` | Done |

### Pipeline stages

| Stage | Capability | Status |
|---|---|---|
| **Stage 1** — Domain grounding | `backend/domain_pack.py`; Player pack rebuilt from SWE1 analysis (`M1/domain_pack_player.json`) | Done |
| **Stage 3** — Deep decompose | Single-requirement decomposition grounded in the domain pack | Done |
| **Stage 6** — Grounded review | Domain-injected review + §7.6 reality-gap rule (`--domain-pack`) | Done |
| **Stage 7** — KPI scorecard | 7+1 KPIs incl. `tier1_critical_req_rate` and L2 `spec_coverage` | Done |

### Cross-cutting

- **Content traceability** — `backend/req_tracer.py` + `--trace` CLI, id-mismatch KPI (validated on Dealer & Player data).
- **Closed-loop generation** — SPEC-grounded generation bridge writes TCs into the team template with house rules, then re-exports a re-reviewable `.xlsx` so output can be audited again.
- **Interactive review SOP** — semantic review layer runnable on subscription (`review_workbook(..., domain_pack_path=...)`).

### Backlog (not blocking, confirm before starting)

- Stage 3/4 single-requirement agent fan-out orchestration (decompose is still batched).
- Full 157-TC A/B run for complete KPI numbers.
- Wire the Stage 4 generation-fill layer to the domain pack (currently only decompose + review consume it).

### Branches

| Branch | State | Notes |
|---|---|---|
| `main` | Stable baseline (2026-05-05) | Behind the feature branch by 43 commits; none of the pipeline rework is here yet. |
| `feat/m1-stage7-scorecard` | **Active** — pushed to `origin`, tracked | Current development line; contains all M0/M1/M2 + Stage work above. |
| `codex/modern-ui-shell` | Local only (2026-06-18), not pushed | Modern UI shell experiment; its commits are already included in the feature branch. |

## Requirements

- Python `>=3.10`
- Node.js `>=20`
- A valid `OPENAI_API_KEY` for real AI generation

Example:

```bash
export OPENAI_API_KEY=sk-proj-xxxxxxxxxxxx
```

You can also place the key in a local `.env` file because the Python entry points load dotenv.

## Install

Backend:

```bash
pip install -e ".[dev]"
```

Frontend:

```bash
cd frontend
npm install
```

Modern frontend variant:

```bash
cd frontend-modern
npm install
```

## Run Tests

Backend:

```bash
pytest -q
```

Frontend typecheck:

```bash
cd frontend
npm run typecheck
```

Modern frontend checks:

```bash
cd frontend-modern
npm run typecheck
npm run test:unit
```

## Run The Desktop App

1. Start the Python API:

```bash
uvicorn api_server:app --app-dir backend --host 127.0.0.1 --port 8003
```

2. Start the Next.js frontend:

```bash
cd frontend
PYTHON_API_BASE=http://127.0.0.1:8003 npm run dev -- --hostname 127.0.0.1 --port 3333
```

3. Open `http://127.0.0.1:3333`

Notes:

- The frontend talks to the backend through same-origin Next.js proxy routes under `/api/*`.
- `PYTHON_API_BASE` is the preferred server-side env var for the frontend proxy.
- Local non-Docker frontend defaults to `http://127.0.0.1:8003`; Docker overrides this to the internal service URL `http://backend:8000`.
- Generate / Regenerate / Export require an active backend job; the desktop no longer creates local mock generated rows when the backend is unavailable.

## Run The Modern UI Variant

The modern UI is a separate frontend package. It does not replace the existing
`frontend/` desktop app and uses separate ports by default.

From the repository root:

```bash
./start-modern.sh
```

Modern UI ports:

- Frontend: `http://127.0.0.1:3433`
- Backend: `http://127.0.0.1:8013`

The launcher reads `.env`, writes `frontend-modern/.env.local`, starts the
backend with reload, and starts the modern Next.js dev server.

## Run With Docker

Both dev and prod expose the frontend on host port **3333** (backend on **8003**).

Prod (production build, no hot reload):

```bash
docker compose -f docker/docker-compose.yml up --build
```

Dev (hot reload for backend and frontend):

```bash
docker compose -f docker/docker-compose.dev.yml up --build
```

Then open `http://localhost:3333`. Set `OPENAI_API_KEY` in `.env` at the repo root before starting.

Modern UI Docker runs use separate compose files and expose the frontend on
host port **3433** (backend on **8013**):

```bash
docker compose -f docker/docker-compose.modern.dev.yml up --build
```

```bash
docker compose -f docker/docker-compose.modern.yml up --build
```

The modern backend writes runtime output to `output-modern/`, which is ignored
by git and kept separate from the legacy `output/` directory.

## CLI Usage

Dry run:

```bash
python backend/main.py --input path/to/SomeProject_SWQT_DeviceManager_20260408.xlsx --dry-run
```

Generate output:

```bash
python backend/main.py \
  --input path/to/SomeProject_SWQT_DeviceManager_20260408.xlsx \
  --sys1 path/to/SYS1.xlsx \
  --spec path/to/spec.docx \
  --framework path/to/framework.json \
  --output-dir output \
  --model gpt-5 \
  --batch-size 5
```

Review existing TCs against ASPICE SWE.6 (no generation):

```bash
python backend/main.py --review \
  --input path/to/existing_tcs.xlsx \
  --output-dir output
```

Outputs `output/findings.json` (full §9 schema) and `output/findings_report.md`
(human-readable). Add `--dry-run` to run only the regex pre-pass without
calling the LLM.

## CLI Options

- `--input`: required TC specification `.xlsx`
- `--sys1`: optional SYS1 spec `.xlsx` used for traceability matching
- `--spec`: optional supplementary spec document; supported formats are `.pdf`, `.docx`, `.xlsx`
- `--framework`: optional confirmed `framework.json` for assigning `Test Set`
- `--output-dir`: output directory; default is `output`
- `--model`: OpenAI model for generation/decomposition tasks; default is `gpt-5` (desktop UI also exposes `gpt-5.4`). Test Set classification always runs on the cheaper `gpt-5-mini` internally and is not affected by this flag. Other `gpt-*` ids in `MODEL_PRICING` are accepted for CLI experimentation but not surfaced in the desktop UI.
- `--batch-size`: number of TCs per API call; default is `5`
- `--mode`: one of `full`, `incremental`, `regenerate`
- `--rows`: comma-separated row numbers or requirement IDs for `regenerate` mode
- `--dry-run`: skip API calls and only print estimated cost
- `--budget`: maximum allowed spend in USD; default is `5.0`
- `--strict-validation`: treat validation warnings as failures
- `--review`: switch to review mode; audits existing TCs and writes `findings.json` + `findings_report.md` to `--output-dir`. Incompatible with generate-only flags (`--sys1`, `--spec`, `--framework`, `--mode`, `--rows`, `--batch-size`, `--strict-validation`)

### KPI scorecard (M1, no LLM, $0)

- `--scorecard`: compute a KPI scorecard from an existing `findings.json`; no LLM calls
- `--findings`: path to the `findings.json` consumed by `--scorecard`
- `--spec-coverage`: path to a `spec_coverage_*.json` (from `M1/spec_coverage_analysis.py`) to feed the L2 `spec_coverage` KPI

### Domain grounding & traceability

- `--domain-pack`: path to a domain pack `.json` injected into review and decompose (Stage 1/3/6 grounding)
- `--trace`: content-based traceability pass against `--sys1`; emits `traceability.json` + `traceability.md`

### Budget planner (M2)

- `--preflight`: estimate spend/time before a run
- `--calibrate`: derive throughput from a probe run
- `--regime`: calibration regime, one of `light`, `deep`
- `--n-light` / `--n-deep`: requirement counts per regime
- `--n-probe`: requirements processed in the probe run
- `--start-pct` / `--end-pct`: usage-window percentage before/after the probe
- `--remaining-pct`: fraction `0..1` of the 5h usage window remaining (from `/usage`)

### Interactive review (subscription, $0)

- `--export-bundle`: export a review context bundle for answering on a subscription instead of API
- `--assemble`: assemble a filled `review_bundle.json` back into findings

### Closed-loop generation (interactive, $0)

- `--gen-export-bundle`: export a SPEC-grounded per-requirement generation bundle (single-req decompose + TC fan-out)
- `--req-ids`: comma-separated requirement ids to limit `--gen-export-bundle`
- `--gen-assemble`: flatten a filled `gen_bundle.json` into generated TCs
- `--gen-template`: blank team TC template `.xlsx`; `--gen-assemble` writes the generated TCs into it with the house rules applied

## Current Frontend Architecture

- The frontend is a single-page Win95-style desktop, not a multi-route form flow.
- Active UI modules are `*Module.tsx`; legacy `*Window.tsx` files were removed.
- Shared workflow state lives in Zustand stores.
- All frontend backend access goes through `frontend/app/api/*` proxy routes.
- `frontend/src/services/jobAdapter.ts` is the single adapter layer used by active modules.
- `frontend-modern/` mirrors the backend proxy pattern in a separate Next.js package and has its own README, tests, E2E specs, Dockerfile, and runtime ports.

## Notes

- The parser expects the workbook sheets `Product Document` and `Test Case Specification&Result`.
- The test group is derived from the input filename pattern `*_SWQT_{TestGroup}_YYYYMMDD.xlsx`.
- If the workbook contains blank rows between valid data rows, parsing continues and later rows are still processed.
- Parse and export are verified end-to-end through the desktop and proxy routes.
- Real generation still depends on a valid OpenAI credential at runtime.

## Documentation

Entry point:

- **[docs/CHANGELOG.md](docs/CHANGELOG.md)** — what's been built, current architecture, test baselines, recent changes
- **[frontend-modern/README.md](frontend-modern/README.md)** — modern UI variant setup, ports, and Docker commands

Reference docs:

- [docs/README.md](docs/README.md) — docs index: runtime / developer / archive split
- [docs/WORKFLOW_MECHANISM_TABLE.md](docs/dev/WORKFLOW_MECHANISM_TABLE.md) — developer table for user actions, API routes, backend work, AI calls, and state writes
- [docs/API_CONTRACT.md](docs/dev/API_CONTRACT.md) — browser ↔ backend API specs
- [docs/ASPICE_SWE6_AI_Instruction.md](docs/ASPICE_SWE6_AI_Instruction.md) — ASPICE SWE.6 AI Instruction (auto-loaded into LLM prompt)
- [docs/TEST_SET_POLICY.md](docs/TEST_SET_POLICY.md) — Test Set grouping, hint, override, and export policy
- [docs/ASPICE_SWE6_AI_Review.md](docs/ASPICE_SWE6_AI_Review.md) — ASPICE SWE.6 AI Review spec (auto-loaded into review prompt)
- [docs/TEST_CASE_DESIGN_METHOD.md](docs/TEST_CASE_DESIGN_METHOD.md) — Design method selection rules (auto-loaded into LLM prompt)
- [docs/TEST_CASE_PRIORITY.md](docs/TEST_CASE_PRIORITY.md) — P0–P3 priority definitions
- [docs/TC_Generator_Architecture_Diagrams.html](docs/dev/TC_Generator_Architecture_Diagrams.html) — visual architecture reference
- [docs/archive/README.md](docs/archive/README.md) — archived notes that must not be loaded into runtime prompts
