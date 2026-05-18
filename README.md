# TC Generator

Automated test case generation tool for ASPICE SWE.6.

The project has two working surfaces:

- Python backend and CLI for parsing, generation, validation, and Excel writing
- Next.js desktop frontend for the upload -> configure -> generate -> review -> export workflow
- Optional modern Next.js UI variant under `frontend-modern/`, isolated from the legacy desktop app

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
docker compose up --build
```

Dev (hot reload for backend and frontend):

```bash
docker compose -f docker-compose.dev.yml up --build
```

Then open `http://localhost:3333`. Set `OPENAI_API_KEY` in `.env` at the repo root before starting.

Modern UI Docker runs use separate compose files and expose the frontend on
host port **3433** (backend on **8013**):

```bash
docker compose -f docker-compose.modern.dev.yml up --build
```

```bash
docker compose -f docker-compose.modern.yml up --build
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
- [docs/WORKFLOW_MECHANISM_TABLE.md](docs/WORKFLOW_MECHANISM_TABLE.md) — developer table for user actions, API routes, backend work, AI calls, and state writes
- [docs/API_CONTRACT.md](docs/API_CONTRACT.md) — browser ↔ backend API specs
- [docs/ASPICE_SWE6_AI_Instruction.md](docs/ASPICE_SWE6_AI_Instruction.md) — ASPICE SWE.6 AI Instruction (auto-loaded into LLM prompt)
- [docs/TEST_SET_POLICY.md](docs/TEST_SET_POLICY.md) — Test Set grouping, hint, override, and export policy
- [docs/ASPICE_SWE6_AI_Review.md](docs/ASPICE_SWE6_AI_Review.md) — ASPICE SWE.6 AI Review spec (auto-loaded into review prompt)
- [docs/Test Case Design Method 判斷規則.md](docs/Test%20Case%20Design%20Method%20判斷規則.md) — Design method selection rules (auto-loaded into LLM prompt)
- [docs/test_case_priority.md](docs/test_case_priority.md) — P0–P3 priority definitions
- [docs/TC_Generator_Architecture_Diagrams.html](docs/TC_Generator_Architecture_Diagrams.html) — visual architecture reference
- [docs/archive/README.md](docs/archive/README.md) — archived notes that must not be loaded into runtime prompts
