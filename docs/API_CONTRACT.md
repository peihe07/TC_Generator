# API Contract

Current frontend/backend integration contract for the TC Generator desktop.

Base URL:

- Development: `NEXT_PUBLIC_PYTHON_API_BASE`
- Example: `http://127.0.0.1:8000`

## `GET /api/health`

Purpose:

- Lightweight reachability probe for the desktop shell.

Response:

```json
{
  "status": "ok",
  "service": "tc-generator-api"
}
```

## `POST /api/parse`

Purpose:

- Parse the uploaded TC workbook.
- Return structured metadata and normalized rows for frontend state hydration.
- Create a job payload shape compatible with the review/generation workflow.

Request:

- Content type: `multipart/form-data`
- Fields:
  - `raw_file`: required `.xlsx` / `.xlsm`
  - `spec_file`: optional supplementary file, currently metadata only

Response:

```json
{
  "jobId": "parse-20260416-123456",
  "project": "newR1L",
  "testGroup": "DeviceManager",
  "rowCount": 12,
  "previewHeaders": ["req_id", "test_item", "priority"],
  "previewRows": [
    {
      "req_id": "SWE1-HMI-DM-001-01",
      "test_item": "PDM01 original text",
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
  ],
  "columnFillStatus": {
    "D": 12,
    "F": 0,
    "G": 0
  },
  "files": {
    "rawFileName": "SomeProject_SWQT_DeviceManager_20260408.xlsx",
    "specFileName": "spec.docx",
    "specFormat": "docx"
  }
}
```

Notes:

- `previewRows` is capped to the first 5 rows.
- `rows` contains normalized frontend-ready row objects.
- `specFormat` may be `pdf`, `docx`, `xlsx`, or `null`.
- If `raw_file` is missing or has an unsupported extension, the endpoint returns `400`.

## `POST /api/generate`

Purpose:

- Create a generation job from the normalized frontend rows.
- Return a stable `jobId` and stream URL for the desktop control room.

Request:

- Content type: `application/json`

```json
{
  "jobId": "parse-20260416-123456",
  "rows": [
    {
      "id": "row-10",
      "reqId": "SWE1-HMI-DM-001-01",
      "testItem": "PDM01 original text",
      "originalRequirement": "PDM01 original text",
      "testSet": "",
      "priority": ""
    }
  ],
  "config": {
    "model": "claude-sonnet-4-6",
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
  "streamUrl": "http://127.0.0.1:8000/api/generate/stream?jobId=parse-20260416-123456"
}
```

Notes:

- `rows` must not be empty.
- This endpoint only creates the job; progress is delivered via SSE.

## `GET /api/generate/stream?jobId=...`

Purpose:

- Stream generation progress back to the desktop using Server-Sent Events.

Event payloads:

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
    "reqId": "SWE1-HMI-DM-001-01",
    "status": "ready",
    "reviewStatus": "pending",
    "generated": {
      "testItemRewrite": "(PDM01 original text → Observable outcome confirmed)",
      "preConditions": "1. Vehicle profile loaded\n2. Required subsystem available",
      "testProcedure": "1. ...",
      "expectedResult": "1. ...",
      "designMethod": "功能測試 (Functional based ; no specific technique)",
      "priority": "High"
    },
    "validation": [
      {
        "id": "validation-pass",
        "severity": "passing",
        "field": "expected_result",
        "message": "Generated row passed the current programmatic validation checks."
      }
    ]
  },
  "stats": {
    "total": 12,
    "processed": 1,
    "currentCost": 0.0085
  },
  "message": "Processed 1/12 rows for SWE1-HMI-DM-001-01."
}
```

```json
{
  "type": "job.completed",
  "jobId": "parse-20260416-123456",
  "stats": {
    "total": 12,
    "processed": 12,
    "currentCost": 0.102
  },
  "message": "Backend generation complete. Review and export windows are ready."
}
```

## `POST /api/export`

Purpose:

- Convert reviewed frontend rows back into an `.xlsx` artifact.
- Reuse the original uploaded workbook as the export base.

Request:

```json
{
  "jobId": "parse-20260416-123456",
  "scope": "accepted",
  "outputMode": "new-file",
  "includeFrameworkSheet": true,
  "selectedColumns": [
    "TC ID",
    "Requirement ID",
    "Test Item Rewrite",
    "Expected Result"
  ],
  "rows": [
    {
      "id": "row-10",
      "rowNum": 10,
      "reqId": "SWE1-HMI-DM-001-01",
      "testItem": "PDM01 original text",
      "reviewStatus": "accepted",
      "generated": {
        "testItemRewrite": "(PDM01 original text → Observable outcome confirmed)",
        "preConditions": "1. Vehicle profile loaded\n2. Required subsystem available",
        "testProcedure": "1. ...",
        "expectedResult": "1. ...",
        "designMethod": "功能測試 (Functional based ; no specific technique)",
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
  "downloadUrl": "http://127.0.0.1:8000/api/export/download/parse-20260416-123456",
  "selectedColumns": [
    "TC ID",
    "Requirement ID",
    "Test Item Rewrite",
    "Expected Result"
  ]
}
```

Notes:

- `jobId` must refer to a previously parsed workbook so the backend can reuse the original file.
- `scope` is applied on the backend using each row's `reviewStatus`.
- `selectedColumns` is currently preserved in metadata for the UI; workbook writing still follows the writer module's supported generated columns.

## `GET /api/export/download/{jobId}`

Purpose:

- Download the generated workbook after a successful export request.
