# API Contract

Current integration contract for the TC Generator desktop.

There are two layers:

- Browser-facing same-origin routes under `frontend/app/api/*`
- Python backend routes under `backend/api_server.py`

The browser should call the Next.js routes. Those routes proxy to the Python backend using `PYTHON_API_BASE`.

## Environment

- Frontend proxy env var: `PYTHON_API_BASE`
- Example backend target: `http://127.0.0.1:8000`

## Browser-Facing Routes

### `POST /api/parse`

Proxy to Python `POST /api/parse`.

Request:

- `multipart/form-data`
- `raw_file`: required `.xlsx` / `.xlsm`
- `reference_file`: optional reference workbook `.xlsx` / `.xlsm`
- `spec_file`: optional supplementary file

Response:

```json
{
  "jobId": "parse-20260416-123456",
  "project": "newR1L",
  "testGroup": "DeviceManager",
  "rowCount": 12,
  "previewHeaders": ["req_id", "test_item", "test_set", "priority"],
  "previewRows": [
    {
      "req_id": "SWE1-HMI-DM-001-01",
      "test_item": "PDM01 original text",
      "test_set": "",
      "priority": ""
    }
  ],
  "rows": [
    {
      "id": "row-10",
      "rowNum": 10,
      "reqId": "SWE1-HMI-DM-001-01",
      "testItem": "PDM01 original text",
      "originalRequirement": "PDM01 original text",
      "testSet": "",
      "priority": "",
      "status": "draft",
      "reviewStatus": "pending",
      "generated": null,
      "validation": []
    }
  ]
}
```

### `POST /api/group`

Proxy to Python `POST /api/group`.

Purpose:

- Build Configure page grouping preview from current rows
- Reuse existing `testSet` values when present
- Otherwise derive fallback grouping labels for preview and apply-back

Request:

```json
{
  "jobId": "parse-20260416-123456",
  "rows": [
    {
      "id": "row-10",
      "reqId": "SWE1-HMI-DM-001-01",
      "testItem": "PDM01 original text",
      "testSet": ""
    }
  ]
}
```

Response:

```json
{
  "jobId": "parse-20260416-123456",
  "groups": [
    {
      "testSet": "PDM01",
      "count": 1,
      "reqIds": ["SWE1-HMI-DM-001-01"]
    }
  ],
  "assignments": [
    {
      "id": "row-10",
      "reqId": "SWE1-HMI-DM-001-01",
      "testSet": "PDM01",
      "source": "derived"
    }
  ],
  "cost": 0.0012,
  "inputTokens": 420,
  "outputTokens": 120,
  "cacheCreationTokens": 0,
  "cacheReadTokens": 80,
  "model": "gpt-5"
}
```

Notes:

- If every row already has `testSet`, grouping is deterministic and the usage fields will be zero.
- If AI-based Test Set classification runs, that cost is now counted into the job's cumulative usage.

### `POST /api/match`

Proxy to Python `POST /api/match`.

Purpose:

- Build Configure page exact-match preview
- Uses the optional reference workbook only when it is compatible with the expected `Basic Report` structure

Response:

```json
{
  "jobId": "parse-20260416-123456",
  "summary": {
    "total": 1,
    "exact": 1,
    "unmatched": 0,
    "hasReferenceWorkbook": true
  },
  "matches": [
    {
      "id": "row-10",
      "reqId": "SWE1-HMI-DM-001-01",
      "testItem": "PDM01 original text",
      "specReference": "SPEC_REF_PDM01",
      "matchType": "exact"
    }
  ]
}
```

### `POST /api/generate`

Proxy to Python `POST /api/generate`.

Request:

```json
{
  "jobId": "parse-20260416-123456",
  "rows": [
    {
      "id": "row-10",
      "reqId": "SWE1-HMI-DM-001-01",
      "testItem": "PDM01 original text",
      "testSet": ""
    }
  ],
  "config": {
    "model": "gpt-5",
    "batchSize": 5,
    "budget": 2,
    "strictValidation": false,
    "regenerateAll": false
  }
}
```

`regenerateAll` is still accepted for backward compatibility, but the current
pipeline always runs AI generation for the submitted rows. Reviewer pre-filled
content is passed as prompt hints rather than causing rows to be preserved.

Response:

```json
{
  "jobId": "parse-20260416-123456",
  "status": "queued",
  "totalRows": 12,
  "streamUrl": "/api/generate/stream?jobId=parse-20260416-123456"
}
```

### `GET /api/generate/stream?jobId=...`

Proxy to Python `GET /api/generate/stream?jobId=...`.

SSE event examples:

```json
{
  "type": "job.started",
  "jobId": "parse-20260416-123456",
  "stats": {
    "total": 12,
    "processed": 0,
    "currentCost": 0.0012
  },
  "message": "Backend generation started for 12 row(s) (12 to generate, 0 preserved)."
}
```

```json
{
  "type": "row.completed",
  "jobId": "parse-20260416-123456",
  "row": {
    "id": "row-10",
    "status": "ready",
    "reviewStatus": "pending",
    "generated": {
      "testItemRewrite": "PDM01 original text -> Observable outcome confirmed",
      "preConditions": "1. Vehicle profile loaded\n2. Required subsystem available",
      "inputTestData": "NA",
      "testProcedure": "1. ...",
      "expectedResult": "1. ...",
      "designMethod": "Functional",
      "priority": "P1"
    }
  },
  "stats": {
    "total": 12,
    "processed": 1,
    "currentCost": 0.0085
  }
}
```

Notes:

- `stats.currentCost` is cumulative for the job, not just the current stream step.
- If Configure → Grouping already triggered AI Test Set classification, generation starts from that existing cost baseline.
- Re-run and regenerate continue accumulating on the same job usage counters.
- `priority` is a tool/workbook output field and uses `P0` / `P1` / `P2`, not
  `High` / `Medium` / `Low`.
- `testItemRewrite` is generated without outer parentheses; the backend writer
  adds `(...)` only when appending it into the workbook Test Item cell.
- When a requirement is split into multiple TCs, the branch tag belongs in
  `tc_title` / UI `scenarioName`, not inside `testItemRewrite`.

### `POST /api/jobs/[jobId]/regenerate/stream`

Proxy to Python `POST /api/jobs/{jobId}/regenerate/stream`.

Request:

```json
{
  "rowIds": ["row-10"],
  "rows": [],
  "config": {
    "model": "gpt-5",
    "batchSize": 5,
    "budget": 2,
    "strictValidation": false
  }
}
```

Response is SSE.

Notes:

- `regenerate` keeps the legacy 1:1 contract: one selected row regenerates into one replacement TC.
- `stats.currentCost` is cumulative job cost, including earlier grouping / generation usage on the same job.

### `POST /api/jobs/[jobId]/rerun/stream`

Proxy to Python `POST /api/jobs/{jobId}/rerun/stream`.

Request:

```json
{
  "rowIds": ["row-10"],
  "rows": [],
  "project": "newR1L",
  "testGroup": "DeviceManager",
  "config": {
    "model": "gpt-5",
    "batchSize": 5,
    "budget": 2,
    "strictValidation": false
  }
}
```

Response is SSE.

Notes:

- `rerun` re-enters the full generation pipeline with splitting enabled.
- One selected row may emit one `row.regenerated` plus additional `row.added` events.
- `stats.currentCost` is cumulative job cost, not delta-only cost for this rerun call.

### `POST /api/export`

Proxy to Python `POST /api/export`.

Request:

```json
{
  "jobId": "parse-20260416-123456",
  "scope": "accepted",
  "outputMode": "new-file",
  "includeFrameworkSheet": true,
  "selectedColumns": ["TC ID", "Pre-Conditions", "Input Test Data", "Test Procedure", "Expected Result"],
  "rows": [
    {
      "id": "row-10",
      "rowNum": 10,
      "reqId": "SWE1-HMI-DM-001-01",
      "reviewStatus": "accepted",
      "generated": {
        "testItemRewrite": "...",
        "preConditions": "1. ...",
        "inputTestData": "NA",
        "testProcedure": "1. ...",
        "expectedResult": "1. ...",
        "designMethod": "Functional",
        "priority": "P1"
      }
    }
  ]
}
```

Response:

```json
{
  "jobId": "parse-20260416-123456",
  "status": "ready",
  "exportedRows": 1,
  "fileName": "SomeProject_SWQT_DeviceManager_20260408_generated.xlsx",
  "downloadUrl": "/api/export/download/parse-20260416-123456",
  "selectedColumns": ["TC ID", "Test Procedure", "Expected Result"]
}
```

### `GET /api/export/download/[jobId]`

Proxy to Python `GET /api/export/download/{jobId}`.

Returns workbook bytes with:

- `content-disposition: attachment`
- `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`

### `POST /api/quick-generate/stream`

Proxy to Python `POST /api/quick-generate/stream`.

Ad-hoc TC generation from manual input. No job context or uploaded workbook required.

Request:

```json
{
  "testItem": "Button pressed → LED turns on",
  "context": "System must be powered on",
  "model": "gpt-5"
}
```

- `context`: optional additional background for the requirement
- Quick Generate always uses the current auto-split flow; there is no separate mode switch

SSE event sequence:

```
job.started → decompose.analysis → tc.generating → tc.completed (×N) → job.completed
```

Example events:

```json
{ "type": "job.started" }
```

```json
{
  "type": "decompose.analysis",
  "reasoning": "Two distinct paths identified...",
  "keywords": [
    { "keyword": "Caller ID", "meaning": "Incoming caller number shown on UI.", "scenarios": [1, 2] }
  ],
  "scenarios": [
    { "id": 1, "name": "Normal flow", "description": "...", "test_item": "..." }
  ],
  "stats": { "total": 1, "currentCost": 0.0012 }
}
```

```json
{
  "type": "tc.completed",
  "scenarioId": 1,
  "scenarioName": "Normal flow",
  "tc": {
    "test_item_rewrite": "Button pressed → LED turns on",
    "pre_conditions": "1. System is powered.",
    "input_test_data": "NA",
    "test_procedure": "1. Press button.\n2. Check that the LED is turned on.",
    "expected_result": "1. LED turns on.",
    "design_method": "Functional",
    "priority": "P1"
  },
  "stats": { "total": 1, "processed": 1, "currentCost": 0.003 }
}
```

```json
{ "type": "job.completed", "stats": { "currentCost": 0.003 } }
```

On error:

```json
{ "type": "job.failed", "message": "API call failed: ..." }
```

## Python Backend Routes

Implemented in `backend/api_server.py`:

- `GET /api/health`
- `POST /api/parse`
- `POST /api/group`
- `POST /api/match`
- `POST /api/generate`
- `GET /api/generate/stream`
- `POST /api/jobs/{jobId}/regenerate/stream`
- `POST /api/export`
- `GET /api/export/download/{jobId}`
- `POST /api/quick-generate/stream`

## Notes

- The active frontend no longer calls the Python backend directly from browser modules.
- `jobAdapter.ts` should be treated as the frontend integration boundary.
- Parse, group, match, and export have automated coverage.
- Generate and regenerate route wiring works, but real success still depends on a valid `OPENAI_API_KEY`.
- Generated TC content must not fabricate unstated details. If the
  requirement/spec/reviewer input does not explicitly provide a number,
  threshold, timeout, dataset, state, identifier, error code, retry count, or
  similar concrete data point, the output should keep it abstract (for example
  `<configured limit>` or `defined in spec`) instead of guessing.

## Model Policy

- `classify_test_sets` uses fixed `gpt-5-mini`
- quick generate / generate / regenerate / rerun use the caller-selected model
- the primary UI exposes only `gpt-5` / `gpt-5.4` as user-selectable models
- prompts are task-bound, not model-bound: the same task keeps the same prompt
  shape across `gpt-5` and `gpt-5.4`
