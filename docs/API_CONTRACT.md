# API Contract

Current integration contract for the TC Generator desktop.

There are two layers:

- Browser-facing same-origin routes under `frontend/app/api/*`
- Python backend routes under `src/api_server.py`

The browser should call the Next.js routes. Those routes proxy to the Python backend using `PYTHON_API_BASE`.

## Environment

- Preferred frontend proxy env var: `PYTHON_API_BASE`
- Fallback env var: `NEXT_PUBLIC_PYTHON_API_BASE`
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
  ]
}
```

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
    "model": "claude-3-5-sonnet",
    "batchSize": 5,
    "budget": 2,
    "strictValidation": false
  }
}
```

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
    "currentCost": 0
  },
  "message": "Backend generation started for 12 row(s)."
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
      "testItemRewrite": "(PDM01 original text -> Observable outcome confirmed)",
      "preConditions": "1. Vehicle profile loaded\n2. Required subsystem available",
      "testProcedure": "1. ...",
      "expectedResult": "1. ...",
      "designMethod": "Functional",
      "priority": "High"
    }
  },
  "stats": {
    "total": 12,
    "processed": 1,
    "currentCost": 0.0085
  }
}
```

### `POST /api/jobs/[jobId]/regenerate/stream`

Proxy to Python `POST /api/jobs/{jobId}/regenerate/stream`.

Request:

```json
{
  "rowIds": ["row-10"],
  "rows": [],
  "config": {
    "model": "claude-3-5-sonnet",
    "batchSize": 5,
    "budget": 2,
    "strictValidation": false
  }
}
```

Response is SSE.

### `POST /api/export`

Proxy to Python `POST /api/export`.

Request:

```json
{
  "jobId": "parse-20260416-123456",
  "scope": "accepted",
  "outputMode": "new-file",
  "includeFrameworkSheet": true,
  "selectedColumns": ["TC ID", "Test Procedure", "Expected Result"],
  "rows": [
    {
      "id": "row-10",
      "rowNum": 10,
      "reqId": "SWE1-HMI-DM-001-01",
      "reviewStatus": "accepted",
      "generated": {
        "testItemRewrite": "(...)",
        "preConditions": "1. ...",
        "testProcedure": "1. ...",
        "expectedResult": "1. ...",
        "designMethod": "Functional",
        "priority": "High"
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
  "mode": "single",
  "model": "claude-sonnet-4-6"
}
```

- `mode`: one of `single`, `with_context`, `decompose`
- `context`: optional, only used when `mode` is `with_context`

SSE event sequence for `single` / `with_context`:

```
job.started → tc.completed → job.completed
```

SSE event sequence for `decompose`:

```
job.started → decompose.analysis → tc.generating → tc.completed (×N) → job.completed
```

Example events:

```json
{ "type": "job.started", "mode": "single" }
```

```json
{
  "type": "decompose.analysis",
  "reasoning": "Two distinct paths identified...",
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
    "test_item_rewrite": "(Button pressed → LED turns on)",
    "pre_conditions": "1. System is powered.",
    "input_test_data": "NA",
    "test_procedure": "1. Press button.\n2. Observe LED.",
    "expected_result": "1. LED turns on.",
    "design_method": "Functional",
    "priority": "Medium"
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

Implemented in `src/api_server.py`:

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
- Generate and regenerate route wiring works, but real success still depends on a valid `ANTHROPIC_API_KEY`.
