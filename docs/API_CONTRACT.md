# API Contract

Current integration contract for the TC Generator desktop.

There are two layers:

- Browser-facing same-origin routes under `frontend/app/api/*`
- Python backend routes under `backend/api_server.py`

The browser should call the Next.js routes. Those routes proxy to the Python backend using `PYTHON_API_BASE`.

## Route Index

Developer-facing table. The desktop UI should call the same-origin Next.js
routes; the Next.js route then proxies to the Python backend route.
For the full user action → API → backend → AI → state mapping, see
[WORKFLOW_MECHANISM_TABLE.md](WORKFLOW_MECHANISM_TABLE.md).

| Area | Method | Browser / Next.js route | Python backend route | Body / stream | Main caller | Notes |
|---|---:|---|---|---|---|---|
| Health | GET | N/A | `/api/health` | JSON | Dev / smoke checks | Backend-only endpoint; reports backend status and whether `OPENAI_API_KEY` is configured. |
| Spec library | GET | `/api/spec-library` | `/api/spec-library` | JSON | Upload | Lists cached spec indices from `spec-index/manifest.json`. |
| Parse | POST | `/api/parse` | `/api/parse` | `multipart/form-data` | Upload | Creates parsed job, stores raw workbook bytes, returns `jobId` and normalized rows. |
| Group preview | POST | `/api/group` | `/api/group` | JSON | Configure | Fill Blank / Regroup All preview. Returns assignments only; Apply or Start Generate writes them into frontend rows. |
| Spec match preview | POST | `/api/match` | `/api/match` | JSON | Configure | Builds traceability preview from cached spec index, reference workbook, or no-reference fallback. |
| Create generate job | POST | `/api/generate` | `/api/generate` | JSON | Generate | Queues rows/config in backend job store. Next.js rewrites returned `streamUrl` to same-origin `/api/generate/stream?jobId=...`. |
| Generate stream | GET | `/api/generate/stream?jobId=...` | `/api/generate/stream?jobId=...` | SSE | Generate | Emits `job.started`, split/row events, `job.completed`; batch usage is persisted as generation progresses. |
| Review fix suggestion | POST | `/api/review/suggest-fix` | `/api/review/suggest-fix` | JSON | Review / ValidationPanel | Single-shot AI suggestion for one row with validation errors; no chat session. |
| Regenerate stream | POST | `/api/jobs/[jobId]/regenerate/stream` | `/api/jobs/{job_id}/regenerate/stream` | SSE | Review | Uses reviewer reason when provided. `regen.started` carries base usage; history records delta. |
| Re-run stream | POST | `/api/jobs/[jobId]/rerun/stream` | `/api/jobs/{job_id}/rerun/stream` | SSE | Review | Re-runs selected rows through full decompose + generate pipeline. `rerun.started` carries base usage. |
| Job usage | GET | `/api/jobs/[jobId]/usage` | `/api/jobs/{job_id}/usage` | JSON | CostMeter / dashboard | Per-job cost and token breakdown, including model-level attribution. |
| Metrics aggregate | GET | `/api/metrics/aggregate?job_ids=...` | `/api/metrics/aggregate?job_ids=...` | JSON | Cost dashboard | Aggregates job metrics; `job_ids` query is optional and comma-separated. |
| Telemetry events | POST | `/api/events` | `/api/events` | JSON | Client telemetry | Appends typed client analytics events to JSONL. |
| Telemetry aggregate | GET | `/api/events/aggregate?experiment=...` | `/api/events/aggregate?experiment=...` | JSON | Experiment analysis | Aggregates event counts by experiment variant; query is optional. |
| Source status | GET | `/api/jobs/[jobId]/source-status` | `/api/jobs/{job_id}/source-status` | JSON | Export | Checks whether backend still has original workbook bytes before export. |
| Attach raw workbook | POST | `/api/jobs/[jobId]/attach-raw` | `/api/jobs/{job_id}/attach-raw` | `multipart/form-data` | Export fallback | Restores original workbook bytes when a workspace was reloaded without backend raw bytes. |
| Export | POST | `/api/export` | `/api/export` | JSON | Export | Requires active parsed job. Writes workbook, may classify missing Test Sets, resequences TC IDs. |
| Download export | GET | `/api/export/download/[jobId]` | `/api/export/download/{jobId}` | file stream | Export | Downloads the generated workbook. Next.js proxies backend file response. |
| Quick Generate | POST | `/api/quick-generate/stream` | `/api/quick-generate/stream` | SSE | QuickGenerate | Ad-hoc generation without parsed job. Stop uses browser abort → proxy signal → backend disconnect checks. |
| Admin reset | DELETE | `/api/admin/reset` | `/api/admin/reset` | JSON | Workspace menu / dev | Localhost only. Clears SQLite job registry and vacuums DB. Destructive. |

Current active API does not include Agent routes. Historical Agent references live
only in deprecated roadmap/design-system notes.

## Environment

- Frontend proxy env var: `PYTHON_API_BASE`
- Example backend target: `http://127.0.0.1:8000`

## Browser-Facing Routes

### `POST /api/parse`

Proxy to Python `POST /api/parse`.

Request:

- `multipart/form-data`
- `raw_file`: required `.xlsx` / `.xlsm`
- `reference_file`: optional reference workbook `.xlsx` / `.xlsm`. Ignored when `selected_spec_name` is supplied.
- `selected_spec_name`: optional. Basename (no extension) of a pre-built spec index entry returned by `GET /api/spec-library`. When set, the backend skips the uploaded reference workbook and loads the cached `SpecIndex` from `spec-index/cache/<name>.json`.
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
- Default mode (`forceRegroup: false`, UI: **Fill Blank**) reuses existing
  `testSet` values and asks AI only for rows where `testSet` is blank.
- Force regroup mode (`forceRegroup: true`, UI: **Regroup All**) sends existing
  `testSet` values as hints, but asks AI to produce a fresh assignment for
  every row.
- The endpoint returns preview assignments only. Frontend rows are changed when
  the user clicks **Apply** or when **Start Generate** is clicked with a preview
  still loaded; Start Generate auto-applies that preview before opening Generate.
- If AI classification fails or omits a row, deterministic fallback labels are
  used for preview and apply-back.

Request:

```json
{
  "jobId": "parse-20260416-123456",
  "forceRegroup": false,
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

- If every row already has `testSet` and `forceRegroup` is false, grouping is deterministic and the usage fields will be zero.
- If `forceRegroup` is true, existing `testSet` values remain in the request as AI hints but may be replaced in the returned preview assignments.
- If AI-based Test Set classification runs, that cost is now counted into the job's cumulative usage.

### `POST /api/match`

Proxy to Python `POST /api/match`.

Purpose:

- Build Configure page traceability preview (PDM exact + Jaccard fuzzy + cosine semantic).
- Source order of precedence: `selectedSpecName` (cached spec index, includes precomputed embeddings) → uploaded reference workbook (`Basic Report` structure) → no-reference fallback (all rows `unmatched`).

Response:

```json
{
  "jobId": "parse-20260416-123456",
  "summary": {
    "total": 1,
    "exact": 1,
    "fuzzy": 0,
    "unmatched": 0,
    "hasReferenceWorkbook": true
  },
  "matches": [
    {
      "id": "row-10",
      "reqId": "SWE1-HMI-DM-001-01",
      "testItem": "PDM01 original text",
      "specReference": "SPEC_REF_PDM01",
      "matchType": "exact",
      "matchScore": null
    }
  ]
}
```

`matchType` is one of `exact` / `fuzzy` / `unmatched`. `matchScore` is non-null for fuzzy / semantic matches (cosine or Jaccard, rounded to 3 decimals).

### `GET /api/spec-library`

Proxy to Python `GET /api/spec-library`.

Purpose:

- List pre-built reference spec indices stored in `spec-index/manifest.json`. Used by the Upload page dropdown so users can reuse a cached SYS1 spec without uploading a workbook.

Response:

```json
{
  "specs": [
    {
      "name": "SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR25_Post_3A_CR29359_(Feb_24_2025)",
      "sourceFile": "SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR25_Post_3A_CR29359_(Feb_24_2025).xlsx",
      "entriesCount": 187,
      "embeddingModel": "text-embedding-3-large",
      "updatedAt": "2026-04-24T14:56:18.772253+00:00"
    }
  ]
}
```

### `POST /api/events`

Proxy to Python `POST /api/events`.

Purpose:

- Append client telemetry to the backend JSONL event log.
- Events are best-effort analytics only; callers should not block core UX on the response.
- Each event may include an `experiments` map so aggregates can be sliced by active A/B variant.

Request:

```json
{
  "events": [
    {
      "name": "experiment_exposure",
      "props": {
        "experiment": "home_layout_emphasis",
        "variant": "action_first"
      },
      "experiments": {
        "home_layout_emphasis": "action_first"
      },
      "ts": 1714000000000
    }
  ]
}
```

Allowed `name` values:

- `experiment_exposure`
- `home_new_run_click`
- `builder_step_next`
- `builder_validation_fail`
- `run_execute_start`
- `run_execute_success`
- `run_execute_fail`
- `run_retry_click`
- `template_use_click`
- `output_compare_open`

Response:

```json
{
  "ok": true,
  "count": 1
}
```

### `GET /api/events/aggregate`

Proxy to Python `GET /api/events/aggregate`.

Purpose:

- Read the append-only telemetry JSONL and produce lightweight experiment analysis.
- Supports `?experiment=home_layout_emphasis` to group metrics by assigned variant.
- Malformed historical JSONL rows are skipped and counted under `malformedLines`.

Response:

```json
{
  "experiment": "home_layout_emphasis",
  "totalEvents": 5,
  "malformedLines": 0,
  "variants": {
    "action_first": {
      "eventCount": 4,
      "exposures": 1,
      "newRunClicks": 1,
      "runStarts": 1,
      "runSuccesses": 1,
      "runFailures": 0,
      "completionRate": 1.0,
      "failureRate": 0.0
    }
  },
  "unknownVariant": {
    "eventCount": 0,
    "exposures": 0,
    "newRunClicks": 0,
    "runStarts": 0,
    "runSuccesses": 0,
    "runFailures": 0,
    "completionRate": 0.0,
    "failureRate": 0.0
  }
}
```

Returns `{ "specs": [] }` when the manifest is missing or unreadable. Entries are sorted alphabetically by `name`. Pass the chosen `name` back as `selected_spec_name` on `POST /api/parse`.

### `POST /api/review/suggest-fix`

Proxy to Python `POST /api/review/suggest-fix`.

Single-shot AI assist for the Review module. Given **one** TC and its
validation errors, returns a structured fix proposal the reviewer can
inspect before sending a Regenerate Reason back to the AI. Replaces the
removed generic chat co-pilot — no session, no streaming.

Request:

```json
{
  "tc": {
    "tc_id": "newR1L-DM-005",
    "req_id": "PDM01",
    "tc_title": "Select X",
    "pre_conditions": "1. ...",
    "input_test_data": "NA",
    "test_procedure": "1. ...",
    "expected_result": "1. ...",
    "design_method": "Functional",
    "priority": "P1"
  },
  "errors": [
    {
      "severity": "error",
      "field": "tc_title",
      "message": "Trigger missing precondition (§6.1)."
    }
  ],
  "model": null
}
```

Response:

```json
{
  "problemRootCause": "tc_title 為裸動作，違反 §6.1 sibling-distinction 規則。",
  "affectedFields": ["tc_title", "pre_conditions"],
  "proposedChange": "tc_title 補上 with iPhone connected via USB；pre_conditions 補 BT pairing 完成。",
  "suggestedReason": "Add precondition (iPhone connected via USB) to tc_title trigger so it distinguishes from the no-phone-paired sibling.",
  "model": "gpt-5",
  "cost": 0.00041,
  "usage": { "input": 870, "output": 162, "cache_creation": 0, "cache_read": 0 }
}
```

Notes:

- `errors[]` MUST contain at least one entry (`400 Bad Request` otherwise).
- `affectedFields` is whitelisted to the canonical TC field keys
  (`tc_title`, `pre_conditions`, `input_test_data`, `test_procedure`,
  `expected_result`, `design_method`, `priority`); unknown / case-variant
  values from the model are dropped silently.
- `problemRootCause` and `proposedChange` are mandatory on the AI side;
  empty values cause the backend to raise `502 Bad Gateway` with a
  `GenerationError` detail rather than emitting a useless suggestion.
- `suggestedReason` is the string the frontend ValidationPanel offers as
  the editable Regenerate Reason — clicking "套用為 Regenerate Reason"
  pre-fills the dialog opened by the toolbox Regenerate button.

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
    "currentCost": 0.0012,
    "inputTokens": 420,
    "outputTokens": 120,
    "cacheCreationTokens": 0,
    "cacheReadTokens": 80
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
- The `job.started` event carries the stream's base usage. The frontend records
  history as `final cumulative - started cumulative`.
- Backend generation / regenerate / rerun persist usage after each successful
  batch, so disconnects do not drop already-incurred usage.
- `stats.total` is the count of **original Requirement IDs** in the job
  (deduped at the input rows). It is locked once at start; AI splits that
  add sub-TCs do not inflate the denominator. `stats.processed` advances
  once per unique reqId seen on a row event, so the progress bar reaches
  100% when all requirements have been processed regardless of how many
  TCs they expand into.
- If Configure → Grouping already triggered AI Test Set classification, generation starts from that existing cost baseline.
- Re-run and regenerate continue accumulating on the same job usage counters.
- Generate / Regenerate do not fall back to local mock generation. Missing or
  inactive backend job state is reported as an error.
- `priority` is a tool/workbook output field and uses `P0` / `P1` / `P2` / `P3`, not
  `High` / `Medium` / `Low`.
- `testItemRewrite` is generated without outer parentheses; the backend writer
  adds `(...)` only when appending it into the workbook Test Item cell.
- When a requirement is split into multiple TCs, the branch tag belongs in
  `tc_title` / UI `scenarioName`, not inside `testItemRewrite`.
- Each row event carries a `splitDecision` object summarizing AI's
  decision for the row's parent requirement:
  - `reqId`, `tcCount`, `subIndex`, `parentId` — split structure.
  - `reasoning`, `keywords` — AI's analysis (only on the primary row).
  - `duplicateOf` (string, optional) — the **row number** of a sibling
    row this row is **strictly equivalent** to (same trigger, outcome,
    input bucket, verification target). Backend resolves whatever AI
    returns ("11" / "row #11" / legacy uuid) against the row's siblings;
    hallucinated values are dropped to "" so the frontend hides the
    badge instead of showing a misleading placeholder.
  - `distinguishingAxis` (object, optional) — `{axis, delta}` declaring
    how this row differs from its siblings. `axis ∈ {trigger_state,
    input_data, timing, boundary, mode, none}`; `delta` is a single
    Traditional Chinese sentence with concrete tokens. Backend
    enforces the cross-rule `axis="none" ⇔ duplicateOf is set`:
    inconsistent AI output is reconciled (conflict drops `duplicateOf`,
    lone `duplicateOf` fills `axis="none"`, lone `axis="none"` without
    a target is cleared).

### `POST /api/jobs/[jobId]/regenerate/stream`

Proxy to Python `POST /api/jobs/{jobId}/regenerate/stream`.

Request:

```json
{
  "rowIds": ["row-10"],
  "rows": [],
  "regenerateReason": "Missing negative validation path",
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

- `regenerateReason` is optional reviewer guidance. The backend passes it into
  AI context as the primary correction target.
- `regenerate` now uses the full split-aware generation path. It always emits a
  `req.split` analysis event before row events. If no split is needed,
  `insertPlan.newCount` is `0`; if split is needed, the primary TC emits
  `row.regenerated` and additional TCs emit `row.added`.
- `req.split.insertPlan` tells the UI where to create space:
  `needsInsert`, `insertAfterId`, `newCount`, and `renumberRequired`.
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
- `req.split.insertPlan` reports the proposed insertion count and anchor row before
  added rows stream back.
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
  "selectedColumns": ["TC ID", "Test Procedure", "Expected Result"],
  "fallbackTemplate": false,
  "tcIdsRenumbered": 0
}
```

Notes:

- Export requires an active parsed backend job. Browser-only simulated export is
  not part of the active workflow.
- `fallbackTemplate: true` means the backend no longer had the original uploaded
  workbook bytes and rebuilt a minimal blank template from the current rows
  before export.
- `tcIdsRenumbered` is the count of TC IDs the backend resequenced
  before write-back to close gaps left by reviewer-side deletes
  (`-001, -002, -005…` → `-001, -002, -003`). Renumbering happens per
  `(project, group_abbr)` bucket sorted by `row_num`. `0` means every
  bucket was already contiguous.
- The browser-facing Next.js route preserves the upstream HTTP status/body. If
  the Python backend returns a non-JSON 500 body, the proxy no longer rewrites
  it into a synthetic `503`.
- Unexpected backend export failures are normalized to:

```json
{ "detail": "export failed: ValueError: ..." }
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
- Stop/cancel is disconnect-aware: browser aborts the request, the Next proxy
  forwards the abort signal, and the Python stream stops sending success events
  if the client disconnects.

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
- `GET /api/spec-library`
- `POST /api/parse`
- `POST /api/group`
- `POST /api/match`
- `POST /api/generate`
- `GET /api/generate/stream`
- `POST /api/jobs/{jobId}/regenerate/stream`
- `POST /api/jobs/{jobId}/rerun/stream`
- `GET /api/jobs/{jobId}/usage`
- `GET /api/metrics/aggregate`
- `POST /api/review/suggest-fix`
- `POST /api/export`
- `POST /api/jobs/{jobId}/attach-raw`
- `GET /api/jobs/{jobId}/source-status`
- `GET /api/export/download/{jobId}`
- `POST /api/quick-generate/stream`
- `DELETE /api/admin/reset`

## Notes

- The active frontend no longer calls the Python backend directly from browser modules.
- `jobAdapter.ts` should be treated as the frontend integration boundary.
- Parse, group, match, and export have automated coverage.
- Browser-facing JSON proxy routes preserve upstream statuses. Generic `503`
  proxy errors now mean the proxy itself failed to reach/process the backend,
  not that the backend returned an application error body.
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
