# TC Generator

Automated test case generation tool for ASPICE SWE.6.

The project has two working surfaces:

- Python backend and CLI for parsing, generation, validation, and Excel writing
- Next.js desktop frontend for the upload -> configure -> generate -> review -> export workflow

## Requirements

- Python `>=3.10`
- Node.js `>=20`
- A valid `ANTHROPIC_API_KEY` for real AI generation

Example:

```bash
export ANTHROPIC_API_KEY=your_key_here
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

## Run Tests

Backend:

```bash
pytest -q
```

Frontend typecheck:

```bash
cd frontend
npx tsc --noEmit
```

## Run The Desktop App

1. Start the Python API:

```bash
uvicorn api_server:app --app-dir src --host 127.0.0.1 --port 8000
```

2. Start the Next.js frontend:

```bash
cd frontend
PYTHON_API_BASE=http://127.0.0.1:8000 npm run dev -- --hostname 127.0.0.1 --port 3000
```

3. Open `http://127.0.0.1:3000`

Notes:

- The frontend talks to the backend through same-origin Next.js proxy routes under `/api/*`.
- `PYTHON_API_BASE` is the preferred server-side env var for the frontend proxy.
- If the backend is unavailable, parts of the desktop fall back to local mock behavior.

## CLI Usage

Dry run:

```bash
python src/main.py --input path/to/SomeProject_SWQT_DeviceManager_20260408.xlsx --dry-run
```

Generate output:

```bash
python src/main.py \
  --input path/to/SomeProject_SWQT_DeviceManager_20260408.xlsx \
  --sys1 path/to/SYS1.xlsx \
  --spec path/to/spec.docx \
  --framework path/to/framework.json \
  --output-dir output \
  --model claude-haiku-4-5-20251001 \
  --batch-size 5
```

## CLI Options

- `--input`: required TC specification `.xlsx`
- `--sys1`: optional SYS1 spec `.xlsx` used for traceability matching
- `--spec`: optional supplementary spec document; supported formats are `.pdf`, `.docx`, `.xlsx`
- `--framework`: optional confirmed `framework.json` for assigning `Test Set`
- `--output-dir`: output directory; default is `output`
- `--model`: Anthropic model name; default is `claude-haiku-4-5-20251001`
- `--batch-size`: number of TCs per API call; default is `5`
- `--mode`: one of `full`, `incremental`, `regenerate`
- `--rows`: comma-separated row numbers or requirement IDs for `regenerate` mode
- `--dry-run`: skip API calls and only print estimated cost
- `--budget`: maximum allowed spend in USD; default is `5.0`
- `--strict-validation`: treat validation warnings as failures

## Current Frontend Architecture

- The frontend is a single-page Win95-style desktop, not a multi-route form flow.
- Active UI modules are `*Module.tsx`; legacy `*Window.tsx` files were removed.
- Shared workflow state lives in Zustand stores.
- All frontend backend access goes through `frontend/app/api/*` proxy routes.
- `frontend/src/services/jobAdapter.ts` is the single adapter layer used by active modules.

## Notes

- The parser expects the workbook sheets `Product Document` and `Test Case Specification&Result`.
- The test group is derived from the input filename pattern `*_SWQT_{TestGroup}_YYYYMMDD.xlsx`.
- If the workbook contains blank rows between valid data rows, parsing continues and later rows are still processed.
- Parse and export are verified end-to-end through the desktop and proxy routes.
- Real generation still depends on a valid Anthropic credential at runtime.

## Related Docs

- [docs/RULES.md](/Users/peihe/Work_Projects/TC_Generator/docs/RULES.md)
- [docs/IMPLEMENTATION_PLAN.md](/Users/peihe/Work_Projects/TC_Generator/docs/IMPLEMENTATION_PLAN.md)
- [docs/API_CONTRACT.md](/Users/peihe/Work_Projects/TC_Generator/docs/API_CONTRACT.md)
- [docs/project_overview.md](/Users/peihe/Work_Projects/TC_Generator/docs/project_overview.md)
