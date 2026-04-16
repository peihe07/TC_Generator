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

from parser import parse_tc_xlsx
from spec_parser import detect_format
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


class GenerateConfig(BaseModel):
    model: str
    batchSize: int = Field(ge=1)
    budget: float = Field(ge=0)
    strictValidation: bool = False


class GenerateRow(BaseModel):
    id: str
    reqId: str
    testItem: str
    originalRequirement: str | None = None
    testSet: str | None = None
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
        "reqId": row.get("req_id", ""),
        "testItem": row.get("test_item", ""),
        "originalRequirement": row.get("test_item", ""),
        "testSet": row.get("test_set", ""),
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
                "test_procedure": generated.get("testProcedure", ""),
                "expected_result": generated.get("expectedResult", ""),
                "priority": generated.get("priority", ""),
                "design_method": generated.get("designMethod", ""),
                "spec_reference": generated.get("specReference"),
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


def _mock_generated_fields(row: dict) -> dict:
    req_id = row.get("reqId", "")
    label = row.get("testItem") or req_id or "Requirement"
    warning_mode = req_id.endswith("2") or req_id.endswith("4")

    generated = {
        "test_item": f"{row.get('originalRequirement') or row.get('testItem', '')}\n\n({label} → Observable outcome confirmed)",
        "pre_conditions": (
            "1. Vehicle profile loaded\n2. Open setup screen"
            if warning_mode
            else "1. Vehicle profile loaded\n2. Required subsystem available"
        ),
        "test_procedure": (
            "1. Open the source screen and prepare the feature.\n"
            "2. Trigger the target behavior and verify the visible outcome."
        ),
        "expected_result": (
            "1. The setup screen is ready for the operator.\n"
            "2. The requested behavior is shown with the correct visible outcome."
        ),
        "design_method": (
            "Functional smoke review"
            if warning_mode
            else "功能測試 (Functional based ; no specific technique)"
        ),
        "priority": "Medium" if warning_mode else (row.get("priority") or "High"),
    }
    return generated


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


def _build_stream_row(row: dict) -> dict:
    generated = _mock_generated_fields(row)
    validation = _normalize_validation_issues(
        validate_row(
            {
                "tc_id": "mock-TCG-001",
                **generated,
            }
        )
    )
    status = "error" if any(issue["severity"] == "warning" for issue in validation) else "ready"
    return {
        **row,
        "status": status,
        "reviewStatus": "pending",
        "generated": {
            "testItemRewrite": generated["test_item"].split("\n\n", 1)[1] if "\n\n" in generated["test_item"] else generated["test_item"],
            "preConditions": generated["pre_conditions"],
            "testProcedure": generated["test_procedure"],
            "expectedResult": generated["expected_result"],
            "designMethod": generated["design_method"],
            "priority": generated["priority"],
        },
        "validation": validation,
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
    job_id = _build_job_id()
    JOB_REGISTRY[job_id] = {
        "jobId": job_id,
        "rawFileName": raw_file.filename,
        "rawBytes": raw_bytes,
        "parsedData": parsed_data,
        "specFileName": spec_file.filename if spec_file else None,
        "specFormat": spec_format,
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
        rows = job["rows"]
        total = len(rows)
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
        for row in rows:
            processed += 1
            current_cost = round(processed * 0.0085, 4)
            updated_row = _build_stream_row(row)
            yield _sse_event(
                {
                    "type": "row.completed",
                    "jobId": jobId,
                    "row": updated_row,
                    "stats": {
                        "total": total,
                        "processed": processed,
                        "currentCost": current_cost,
                    },
                    "message": (
                        f"Processed {processed}/{total} rows for {row.get('reqId') or row.get('id')}."
                    ),
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

    with tempfile.TemporaryDirectory() as tmp_dir:
        source_path = os.path.join(tmp_dir, job["rawFileName"])
        with open(source_path, "wb") as source_file:
            source_file.write(job["rawBytes"])

        write_generated_results(source_path, export_rows, export_path)

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
