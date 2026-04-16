"""FastAPI server for frontend integration."""
from __future__ import annotations

import asyncio
import json
import os
import tempfile
from datetime import datetime

from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field

from generator import DEFAULT_MODEL, GenerationError, calculate_cost, generate_batch, generate_single_tc
from id_generator import generate_group_abbreviation, generate_tc_ids
from parser import parse_tc_xlsx
from spec_matcher import match_spec_references
from spec_parser import detect_format, parse_docx, parse_pdf, parse_xlsx
from validator import validate_row
from writer import build_output_path, write_framework_sheet, write_generated_results

app = FastAPI(title="tc-generator-api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_RAW_EXTENSIONS = {".xlsx", ".xlsm"}
JOB_REGISTRY: dict[str, dict] = {}
RULES_SECTIONS = """
## Test Item Rewrite
- One behavior per TC, must match requirement intent
- Format: (Condition/Trigger → Observable Outcome)

## Pre-Conditions
- State or environment ONLY, never actions
- Minimum necessary state, numbered list or NA

## Input Test Data
- Explicit deterministic values, or NA

## Test Procedure
- Setup steps → Transition steps → Final Step (verification)
- Each step: executable action + purpose
- Final step must include action + verification target

## Expected Result
- 1:1 mapping with procedure steps
- Observable, judgeable, no vague language

## Design Method
- Use decision waterfall: Negative → Fault Injection → State Transition → Decision Table → EP → BVA → Combinatorial → Scenario → Functional

## Priority
- High: safety, core functionality, data loss risk
- Medium: standard feature, user-facing behavior
- Low: UI cosmetic, edge cases
""".strip()


class GenerateConfig(BaseModel):
    model: str
    batchSize: int = Field(ge=1)
    budget: float = Field(ge=0)
    strictValidation: bool = False


class GenerateRow(BaseModel):
    id: str
    rowNum: int | None = None
    tcId: str | None = None
    reqId: str
    testItem: str
    originalRequirement: str | None = None
    testSet: str | None = None
    specReference: str | None = None
    priority: str | None = None


class GenerateRequest(BaseModel):
    jobId: str | None = None
    rows: list[GenerateRow]
    config: GenerateConfig


class ExportRequest(BaseModel):
    jobId: str
    scope: str
    outputMode: str
    includeFrameworkSheet: bool = True
    selectedColumns: list[str] = Field(default_factory=list)
    rows: list[dict]


EXPORT_COLUMN_TO_FIELD = {
    "TC ID": "tc_id",
    "Test Set": "test_set",
    "Test Item Rewrite": "test_item_rewrite",
    "Pre-Conditions": "pre_conditions",
    "Test Procedure": "test_procedure",
    "Expected Result": "expected_result",
    "Priority": "priority",
    "Spec Reference": "spec_reference",
    "Design Method": "design_method",
}


def _build_job_id() -> str:
    return f"parse-{datetime.now().strftime('%Y%m%d-%H%M%S')}"


def _build_generate_job_id() -> str:
    return f"generate-{datetime.now().strftime('%Y%m%d-%H%M%S')}"


def _build_export_path(filename: str, output_mode: str) -> str:
    export_dir = os.path.join(tempfile.gettempdir(), "tc_generator_exports")
    os.makedirs(export_dir, exist_ok=True)
    if output_mode == "overwrite":
        return os.path.join(export_dir, filename)
    return build_output_path(os.path.join(export_dir, filename))


def _normalize_row(row: dict) -> dict:
    return {
        "id": f"row-{row['row_num']}",
        "rowNum": row["row_num"],
        "tcId": row.get("tc_id", ""),
        "reqId": row.get("req_id", ""),
        "testItem": row.get("test_item", ""),
        "originalRequirement": row.get("test_item", ""),
        "testSet": row.get("test_set", ""),
        "specReference": row.get("spec_reference"),
        "priority": row.get("priority", ""),
        "status": "draft",
        "reviewStatus": "pending",
        "generated": None,
        "validation": [],
    }


def _build_preview(parsed_data: dict) -> tuple[list[str], list[dict]]:
    preview_headers = ["req_id", "test_item", "test_set", "priority"]
    preview_rows = []
    for row in parsed_data["rows"][:5]:
        preview_rows.append({header: row.get(header, "") for header in preview_headers})
    return preview_headers, preview_rows


def _map_export_rows(rows: list[dict], scope: str, test_group: str | None) -> list[dict]:
    exportable = []
    for row in rows:
        review_status = row.get("reviewStatus")
        generated = row.get("generated") or {}
        if not generated:
            continue
        if scope == "accepted" and review_status != "accepted":
            continue
        if scope == "flagged" and review_status != "flagged":
            continue

        exportable.append(
            {
                "row_num": row.get("rowNum"),
                "tc_id": row.get("tcId", ""),
                "test_group": test_group or row.get("testGroup"),
                "test_set": row.get("testSet"),
                "test_item_rewrite": generated.get("testItemRewrite", ""),
                "pre_conditions": generated.get("preConditions", ""),
                "input_test_data": generated.get("inputTestData", ""),
                "test_procedure": generated.get("testProcedure", ""),
                "expected_result": generated.get("expectedResult", ""),
                "priority": generated.get("priority", ""),
                "design_method": generated.get("designMethod", ""),
                "spec_reference": row.get("specReference") or generated.get("specReference"),
            }
        )

    return exportable


def _build_framework_rows(rows: list[dict], test_group: str | None) -> list[dict]:
    counts: dict[tuple[str | None, str | None], int] = {}
    for row in rows:
        key = (test_group or row.get("testGroup"), row.get("test_set"))
        counts[key] = counts.get(key, 0) + 1

    framework_rows = []
    for (group_name, test_set), req_count in counts.items():
        framework_rows.append(
            {
                "test_group": group_name or "",
                "test_set": test_set or "",
                "req_count": req_count,
            }
        )
    return framework_rows


def _selected_export_fields(selected_columns: list[str]) -> set[str] | None:
    mapped = {
        EXPORT_COLUMN_TO_FIELD[column]
        for column in selected_columns
        if column in EXPORT_COLUMN_TO_FIELD
    }
    return mapped or None


def _extract_existing_sequence_numbers(rows: list[dict]) -> list[int]:
    sequences = []
    for row in rows:
        tc_id = row.get("tc_id") or row.get("tcId")
        if not tc_id:
            continue
        parts = tc_id.rsplit("-", 1)
        if len(parts) == 2 and parts[1].isdigit():
            sequences.append(int(parts[1]))
    return sequences


def _estimate_cost(row_count: int, model: str, batch_size: int) -> float:
    avg_input = 1500
    avg_output = 800
    calls = (row_count + batch_size - 1) // batch_size
    del calls
    return calculate_cost(avg_input * row_count, avg_output * row_count, model)


def _would_exceed_budget(current_cost: float, batch_size: int, model: str, budget: float) -> bool:
    estimated_batch_cost = _estimate_cost(batch_size, model, batch_size)
    return current_cost + estimated_batch_cost > budget


def _build_spec_index_for_job(job: dict) -> dict:
    spec_bytes = job.get("specBytes")
    spec_filename = job.get("specFileName")
    spec_format = job.get("specFormat")
    if not spec_bytes or not spec_filename or not spec_format:
        return {}

    parsers = {"pdf": parse_pdf, "docx": parse_docx, "xlsx": parse_xlsx}
    parser = parsers.get(spec_format)
    if parser is None:
        return {}

    with tempfile.TemporaryDirectory() as tmp_dir:
        spec_path = os.path.join(tmp_dir, spec_filename)
        with open(spec_path, "wb") as spec_file:
            spec_file.write(spec_bytes)
        return parser(spec_path)


def _prepare_generation_rows(job: dict) -> list[dict]:
    parsed_rows = job.get("parsedData", {}).get("rows", [])
    parsed_by_row_num = {row["row_num"]: row for row in parsed_rows}
    parsed_by_req_id = {row.get("req_id"): row for row in parsed_rows}

    prepared_rows = []
    for raw_row in job["rows"]:
        base_row = None
        if raw_row.get("rowNum") is not None:
            base_row = parsed_by_row_num.get(raw_row["rowNum"])
        if base_row is None and raw_row.get("reqId"):
            base_row = parsed_by_req_id.get(raw_row["reqId"])
        base_row = base_row or {}

        prepared_rows.append(
            {
                "id": raw_row["id"],
                "row_num": raw_row.get("rowNum") or base_row.get("row_num") or 0,
                "tc_id": raw_row.get("tcId") or base_row.get("tc_id", ""),
                "req_id": raw_row.get("reqId") or base_row.get("req_id", ""),
                "test_item": raw_row.get("testItem") or base_row.get("test_item", ""),
                "original_requirement": raw_row.get("originalRequirement")
                or base_row.get("test_item", ""),
                "test_set": raw_row.get("testSet")
                if raw_row.get("testSet") is not None
                else base_row.get("test_set", ""),
                "spec_reference": raw_row.get("specReference")
                if raw_row.get("specReference") is not None
                else base_row.get("spec_reference"),
                "priority": raw_row.get("priority")
                if raw_row.get("priority") is not None
                else base_row.get("priority", ""),
            }
        )

    spec_index = _build_spec_index_for_job(job)
    if spec_index:
        matched_rows = match_spec_references(prepared_rows, spec_index)
        for prepared_row, matched_row in zip(prepared_rows, matched_rows):
            prepared_row["spec_reference"] = matched_row.get("spec_reference")

    existing_sequences = _extract_existing_sequence_numbers(parsed_rows) + _extract_existing_sequence_numbers(prepared_rows)
    missing_rows = [row for row in prepared_rows if not row.get("tc_id")]
    if missing_rows:
        project = job.get("parsedData", {}).get("project") or "project"
        test_group = job.get("parsedData", {}).get("test_group") or "TC"
        start = max(existing_sequences) + 1 if existing_sequences else 1
        tc_ids = generate_tc_ids(
            project,
            generate_group_abbreviation(test_group),
            len(missing_rows),
            start=start,
        )
        for row, tc_id in zip(missing_rows, tc_ids):
            row["tc_id"] = tc_id

    return prepared_rows


def _normalize_validation_issues(results: dict) -> list[dict]:
    issues = []
    for check, result in results.items():
        if result.passed:
            continue
        issues.append(
            {
                "id": f"{check}-{len(issues) + 1}",
                "severity": "warning",
                "field": check,
                "message": result.message or f"{check} failed validation.",
            }
        )

    if not issues:
        issues.append(
            {
                "id": "validation-pass",
                "severity": "passing",
                "field": "expected_result",
                "message": "Generated row passed the current programmatic validation checks.",
            }
        )

    return issues


def _build_stream_row(row: dict, tc: dict) -> tuple[dict, bool]:
    validation = _normalize_validation_issues(
        validate_row(
            {
                "tc_id": row["tc_id"],
                "test_item": f"{row['original_requirement']}\n\n{tc['test_item_rewrite']}",
                "pre_conditions": tc["pre_conditions"],
                "test_procedure": tc["test_procedure"],
                "expected_result": tc["expected_result"],
                "design_method": tc["design_method"],
                "priority": tc["priority"],
            }
        )
    )
    has_warnings = any(issue["severity"] == "warning" for issue in validation)
    return (
        {
            "id": row["id"],
            "rowNum": row["row_num"],
            "tcId": row["tc_id"],
            "reqId": row["req_id"],
            "testItem": row["test_item"],
            "originalRequirement": row["original_requirement"],
            "testSet": row.get("test_set", ""),
            "specReference": row.get("spec_reference"),
            "priority": tc["priority"],
            "status": "error" if has_warnings else "ready",
            "reviewStatus": "pending",
            "generated": {
                "testItemRewrite": tc["test_item_rewrite"],
                "preConditions": tc["pre_conditions"],
                "inputTestData": tc["input_test_data"],
                "testProcedure": tc["test_procedure"],
                "expectedResult": tc["expected_result"],
                "designMethod": tc["design_method"],
                "priority": tc["priority"],
                "specReference": row.get("spec_reference"),
            },
            "validation": validation,
        },
        has_warnings,
    )


def _build_failed_stream_row(row: dict, message: str) -> dict:
    return {
        "id": row["id"],
        "rowNum": row["row_num"],
        "tcId": row.get("tc_id", ""),
        "reqId": row.get("req_id", ""),
        "testItem": row.get("test_item", ""),
        "originalRequirement": row.get("original_requirement", ""),
        "testSet": row.get("test_set", ""),
        "specReference": row.get("spec_reference"),
        "priority": row.get("priority", ""),
        "status": "error",
        "reviewStatus": "pending",
        "generated": None,
        "validation": [
            {
                "id": f"runtime-{row.get('id', 'row')}",
                "severity": "warning",
                "field": "runtime",
                "message": message,
            }
        ],
    }


def _sse_event(payload: dict) -> str:
    return f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"


@app.get("/api/health")
def healthcheck() -> dict:
    return {"status": "ok", "service": "tc-generator-api"}


@app.post("/api/parse")
async def parse_workbook(
    raw_file: UploadFile = File(...),
    spec_file: UploadFile | None = File(default=None),
) -> dict:
    _, raw_ext = os.path.splitext(raw_file.filename or "")
    raw_ext = raw_ext.lower()
    if raw_ext not in ALLOWED_RAW_EXTENSIONS:
        raise HTTPException(status_code=400, detail="raw_file must be .xlsx or .xlsm")

    raw_bytes = await raw_file.read()
    with tempfile.TemporaryDirectory() as tmp_dir:
        temp_path = os.path.join(tmp_dir, raw_file.filename or f"upload{raw_ext}")
        with open(temp_path, "wb") as tmp:
            tmp.write(raw_bytes)
        parsed_data = parse_tc_xlsx(temp_path)

    preview_headers, preview_rows = _build_preview(parsed_data)
    spec_format = detect_format(spec_file.filename) if spec_file and spec_file.filename else None
    spec_bytes = await spec_file.read() if spec_file else None
    job_id = _build_job_id()
    JOB_REGISTRY[job_id] = {
        "jobId": job_id,
        "rawFileName": raw_file.filename,
        "rawBytes": raw_bytes,
        "parsedData": parsed_data,
        "specFileName": spec_file.filename if spec_file else None,
        "specFormat": spec_format,
        "specBytes": spec_bytes,
        "status": "parsed",
    }

    return {
        "jobId": job_id,
        "project": parsed_data["project"],
        "testGroup": parsed_data["test_group"],
        "rowCount": parsed_data["row_count"],
        "previewHeaders": preview_headers,
        "previewRows": preview_rows,
        "rows": [_normalize_row(row) for row in parsed_data["rows"]],
        "columnFillStatus": parsed_data["column_fill_status"],
        "files": {
            "rawFileName": raw_file.filename,
            "specFileName": spec_file.filename if spec_file else None,
            "specFormat": spec_format,
        },
    }


@app.post("/api/generate")
async def create_generate_job(payload: GenerateRequest, request: Request) -> dict:
    if not payload.rows:
        raise HTTPException(status_code=400, detail="rows must not be empty")

    job_id = payload.jobId or _build_generate_job_id()
    total_rows = len(payload.rows)
    stream_url = str(request.url_for("stream_generate_job")) + f"?jobId={job_id}"

    job_record = JOB_REGISTRY.get(job_id, {"jobId": job_id})
    job_record.update(
        {
            "status": "queued",
            "rows": [row.model_dump() for row in payload.rows],
            "config": payload.config.model_dump(),
            "totalRows": total_rows,
        }
    )
    JOB_REGISTRY[job_id] = job_record

    return {
        "jobId": job_id,
        "status": "queued",
        "totalRows": total_rows,
        "streamUrl": stream_url,
    }


@app.get("/api/generate/stream", name="stream_generate_job")
async def stream_generate_job(jobId: str) -> StreamingResponse:
    job = JOB_REGISTRY.get(jobId)
    if not job:
        raise HTTPException(status_code=404, detail="job not found")

    async def event_generator():
        rows = _prepare_generation_rows(job)
        total = len(rows)
        config = job.get("config", {})
        context = {
            "project": job.get("parsedData", {}).get("project"),
            "test_group": job.get("parsedData", {}).get("test_group"),
            "test_set": "N/A",
        }
        spec_index = _build_spec_index_for_job(job)
        job["status"] = "running"
        yield _sse_event(
            {
                "type": "job.started",
                "jobId": jobId,
                "stats": {"total": total, "processed": 0, "currentCost": 0},
                "message": f"Backend generation started for {total} row(s).",
            }
        )

        processed = 0
        current_cost = 0.0
        batch_size = config.get("batchSize", 1)
        model = config.get("model", DEFAULT_MODEL)
        strict_validation = config.get("strictValidation", False)
        budget = config.get("budget", 0)

        for i in range(0, total, batch_size):
            batch = rows[i:i + batch_size]

            if budget and _would_exceed_budget(current_cost, len(batch), model, budget):
                for row in batch:
                    processed += 1
                    yield _sse_event(
                        {
                            "type": "row.failed",
                            "jobId": jobId,
                            "row": _build_failed_stream_row(
                                row,
                                f"Skipped because the next batch would exceed the configured budget of ${budget:.2f}.",
                            ),
                            "stats": {
                                "total": total,
                                "processed": processed,
                                "currentCost": round(current_cost, 4),
                            },
                            "message": f"Skipped {row.get('req_id')} due to budget limit.",
                        }
                    )
                continue

            try:
                if len(batch) == 1:
                    context["test_set"] = batch[0].get("test_set", "N/A")
                    result = generate_single_tc(batch[0], context, spec_index, RULES_SECTIONS, model)
                    tc_data_list = [result.tc_data]
                else:
                    result = generate_batch(batch, context, spec_index, RULES_SECTIONS, model)
                    tc_data_list = result.tc_data

                current_cost += result.cost
                for row, tc in zip(batch, tc_data_list):
                    processed += 1
                    updated_row, has_warnings = _build_stream_row(row, tc)
                    event_type = "row.failed" if strict_validation and has_warnings else "row.completed"
                    if event_type == "row.failed":
                        updated_row["generated"] = None
                    yield _sse_event(
                        {
                            "type": event_type,
                            "jobId": jobId,
                            "row": updated_row,
                            "stats": {
                                "total": total,
                                "processed": processed,
                                "currentCost": round(current_cost, 4),
                            },
                            "message": (
                                f"Processed {processed}/{total} rows for {row.get('req_id') or row.get('id')}."
                            ),
                        }
                    )
            except GenerationError as exc:
                for row in batch:
                    processed += 1
                    yield _sse_event(
                        {
                            "type": "row.failed",
                            "jobId": jobId,
                            "row": _build_failed_stream_row(
                                row,
                                f"Generation failed: {exc}",
                            ),
                            "stats": {
                                "total": total,
                                "processed": processed,
                                "currentCost": round(current_cost, 4),
                            },
                            "message": f"Generation failed for {row.get('req_id') or row.get('id')}.",
                        }
                    )

            await asyncio.sleep(0.15)

        job["status"] = "completed"
        yield _sse_event(
            {
                "type": "job.completed",
                "jobId": jobId,
                "stats": {
                    "total": total,
                    "processed": total,
                    "currentCost": current_cost,
                },
                "message": "Backend generation complete. Review and export windows are ready.",
            }
        )

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.post("/api/export")
async def export_job(payload: ExportRequest, request: Request) -> dict:
    job = JOB_REGISTRY.get(payload.jobId)
    if not job or "rawBytes" not in job or "rawFileName" not in job:
        raise HTTPException(status_code=404, detail="export source workbook not found")

    export_rows = _map_export_rows(
        payload.rows,
        payload.scope,
        job.get("parsedData", {}).get("test_group") if job.get("parsedData") else None,
    )
    if not export_rows:
        raise HTTPException(status_code=400, detail="no exportable rows for the selected scope")

    export_path = _build_export_path(job["rawFileName"], payload.outputMode)
    selected_fields = _selected_export_fields(payload.selectedColumns)

    with tempfile.TemporaryDirectory() as tmp_dir:
        source_path = os.path.join(tmp_dir, job["rawFileName"])
        with open(source_path, "wb") as source_file:
            source_file.write(job["rawBytes"])

        write_generated_results(
            source_path,
            export_rows,
            export_path,
            selected_fields=selected_fields,
        )

    if payload.includeFrameworkSheet:
        write_framework_sheet(
            export_path,
            _build_framework_rows(export_rows, job.get("parsedData", {}).get("test_group")),
            export_path,
        )

    job["exportPath"] = export_path
    download_url = str(request.url_for("download_export", jobId=payload.jobId))
    return {
        "jobId": payload.jobId,
        "status": "ready",
        "exportedRows": len(export_rows),
        "fileName": os.path.basename(export_path),
        "downloadUrl": download_url,
        "selectedColumns": payload.selectedColumns,
    }


@app.get("/api/export/download/{jobId}", name="download_export")
async def download_export(jobId: str) -> FileResponse:
    job = JOB_REGISTRY.get(jobId)
    if not job or not job.get("exportPath") or not os.path.exists(job["exportPath"]):
        raise HTTPException(status_code=404, detail="export file not found")

    return FileResponse(
        job["exportPath"],
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=os.path.basename(job["exportPath"]),
    )
