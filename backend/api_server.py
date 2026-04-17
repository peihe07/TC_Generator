"""FastAPI server for frontend integration."""
from __future__ import annotations

import asyncio
import json
import os
import tempfile
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from generator import DEFAULT_MODEL, GenerationError, calculate_cost, generate_batch, generate_single_tc, generate_quick_tc, decompose_requirement
from id_generator import generate_group_abbreviation, generate_tc_ids
from job_store import SqliteJobStore, default_db_path
from parser import parse_tc_xlsx
from spec_matcher import build_spec_index, extract_pdm_codes, match_spec_references
from spec_parser import detect_format, parse_docx, parse_pdf, parse_xlsx
from validator import validate_row
from writer import build_output_path, write_framework_sheet, write_generated_results

load_dotenv()

app = FastAPI(title="tc-generator-api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_RAW_EXTENSIONS = {".xlsx", ".xlsm"}
# SQLite-backed job registry — server 重啟後 jobs 仍可被檢索
JOB_REGISTRY = SqliteJobStore(default_db_path())

# 內建精簡規則：當 docs/ 規則檔案不存在時的 fallback
_FALLBACK_RULES = """
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

# 規則文件路徑（專案根目錄下 docs/）
_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
_RULE_FILES = [
    _DOCS_DIR / "ASPICE_SWE6_Test_Case_Writing_Rules.md",
    _DOCS_DIR / "Test Case Design Method 判斷規則.md",
]


def _load_rules() -> str:
    """讀取 docs/ 下的規則 markdown 並串接；若全部缺失則退回精簡 fallback。"""
    sections: list[str] = []
    for path in _RULE_FILES:
        if path.is_file():
            try:
                text = path.read_text(encoding="utf-8").strip()
                if text:
                    sections.append(f"# {path.stem}\n\n{text}")
            except OSError:
                continue
    return "\n\n---\n\n".join(sections) if sections else _FALLBACK_RULES


RULES_SECTIONS = _load_rules()


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
    rows: list[dict] = Field(default_factory=list)


class RegenerateRequest(BaseModel):
    rowIds: list[str]
    config: GenerateConfig | None = None
    rows: list[dict]


class GroupPreviewRequest(BaseModel):
    jobId: str
    rows: list[GenerateRow]


class MatchPreviewRequest(BaseModel):
    jobId: str
    rows: list[GenerateRow]


class QuickGenerateRequest(BaseModel):
    testItem: str
    context: str | None = None
    mode: str = "single"  # "single" | "with_context" | "decompose"
    model: str = DEFAULT_MODEL


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


def _build_reference_match_index_for_job(job: dict) -> dict:
    reference_bytes = job.get("referenceWorkbookBytes")
    reference_filename = job.get("referenceWorkbookName")
    if not reference_bytes or not reference_filename:
        return {}

    with tempfile.TemporaryDirectory() as tmp_dir:
        reference_path = os.path.join(tmp_dir, reference_filename)
        with open(reference_path, "wb") as reference_file:
            reference_file.write(reference_bytes)
        try:
            return build_spec_index(reference_path)
        except Exception:
            return {}


def _derive_test_set_name(row: dict) -> str:
    existing = str(row.get("test_set") or row.get("testSet") or "").strip()
    if existing:
        return existing

    codes = extract_pdm_codes(str(row.get("test_item") or row.get("testItem") or ""))
    if codes:
        return codes[0]

    req_id = str(row.get("req_id") or row.get("reqId") or "").strip()
    req_parts = [part for part in req_id.split("-") if part]
    if len(req_parts) >= 2:
        return f"REQ-{req_parts[-2]}"

    return "Unassigned"


def _build_group_preview(rows: list[dict]) -> tuple[list[dict], dict[str, list[str]]]:
    assignments = []
    framework: dict[str, list[str]] = {}

    for row in rows:
        test_set = _derive_test_set_name(row)
        req_id = str(row.get("req_id") or row.get("reqId") or "")
        assignments.append(
            {
                "id": row.get("id"),
                "reqId": req_id,
                "testSet": test_set,
                "source": "existing" if str(row.get("test_set") or row.get("testSet") or "").strip() else "derived",
            }
        )
        framework.setdefault(test_set, []).append(req_id)

    groups = [
        {
            "testSet": test_set,
            "count": len(req_ids),
            "reqIds": req_ids,
        }
        for test_set, req_ids in framework.items()
    ]
    groups.sort(key=lambda group: (-group["count"], group["testSet"]))
    return groups, framework


def _prepare_match_preview_rows(rows: list[GenerateRow], job: dict) -> list[dict]:
    prepared_rows = []
    parsed_rows = job.get("parsedData", {}).get("rows", [])
    parsed_by_row_num = {row["row_num"]: row for row in parsed_rows}
    parsed_by_req_id = {row.get("req_id"): row for row in parsed_rows}

    for raw_row in rows:
        dump = raw_row.model_dump()
        base_row = None
        if dump.get("rowNum") is not None:
            base_row = parsed_by_row_num.get(dump["rowNum"])
        if base_row is None and dump.get("reqId"):
            base_row = parsed_by_req_id.get(dump["reqId"])
        base_row = base_row or {}
        prepared_rows.append(
            {
                "id": dump["id"],
                "req_id": dump.get("reqId") or base_row.get("req_id", ""),
                "test_item": dump.get("testItem") or base_row.get("test_item", ""),
            }
        )
    return prepared_rows


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

    reference_index = _build_reference_match_index_for_job(job)
    if reference_index:
        matched_rows = match_spec_references(prepared_rows, reference_index)
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


@app.post("/api/quick-generate/stream")
async def stream_quick_generate(payload: QuickGenerateRequest) -> StreamingResponse:
    """Ad-hoc TC generation from manual input. Supports single, with_context, and decompose modes."""

    async def event_generator():
        model = payload.model
        current_cost = 0.0

        yield _sse_event({"type": "job.started", "mode": payload.mode})

        if payload.mode == "decompose":
            # Step 1: decompose requirement into scenarios
            try:
                decompose_result = decompose_requirement(payload.testItem, RULES_SECTIONS, model)
            except GenerationError as exc:
                yield _sse_event({"type": "job.failed", "message": str(exc)})
                return

            current_cost += decompose_result.cost
            yield _sse_event(
                {
                    "type": "decompose.analysis",
                    "reasoning": decompose_result.reasoning,
                    "scenarios": decompose_result.scenarios,
                    "stats": {"total": len(decompose_result.scenarios), "currentCost": round(current_cost, 4)},
                }
            )

            # Step 2: generate TC for each scenario sequentially
            total = len(decompose_result.scenarios)
            for i, scenario in enumerate(decompose_result.scenarios):
                yield _sse_event(
                    {
                        "type": "tc.generating",
                        "scenarioId": scenario["id"],
                        "scenarioName": scenario.get("name", ""),
                        "stats": {"total": total, "processed": i, "currentCost": round(current_cost, 4)},
                    }
                )
                try:
                    result = generate_quick_tc(
                        test_item=scenario.get("test_item", scenario.get("description", "")),
                        context=f"Scenario: {scenario.get('name', '')}\n{payload.testItem}",
                        rules_text=RULES_SECTIONS,
                        model=model,
                    )
                    current_cost += result.cost
                    yield _sse_event(
                        {
                            "type": "tc.completed",
                            "scenarioId": scenario["id"],
                            "scenarioName": scenario.get("name", ""),
                            "tc": result.tc_data,
                            "stats": {"total": total, "processed": i + 1, "currentCost": round(current_cost, 4)},
                        }
                    )
                except GenerationError as exc:
                    yield _sse_event(
                        {
                            "type": "tc.failed",
                            "scenarioId": scenario["id"],
                            "message": str(exc),
                            "stats": {"total": total, "processed": i + 1, "currentCost": round(current_cost, 4)},
                        }
                    )
                await asyncio.sleep(0.05)

        else:
            # single or with_context: one TC directly
            context_text = payload.context if payload.mode == "with_context" else None
            try:
                result = generate_quick_tc(
                    test_item=payload.testItem,
                    context=context_text,
                    rules_text=RULES_SECTIONS,
                    model=model,
                )
                current_cost += result.cost
                yield _sse_event(
                    {
                        "type": "tc.completed",
                        "scenarioId": 1,
                        "tc": result.tc_data,
                        "stats": {"total": 1, "processed": 1, "currentCost": round(current_cost, 4)},
                    }
                )
            except GenerationError as exc:
                yield _sse_event({"type": "job.failed", "message": str(exc)})
                return

        yield _sse_event(
            {
                "type": "job.completed",
                "stats": {"currentCost": round(current_cost, 4)},
            }
        )

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.get("/api/health")
def healthcheck() -> dict:
    return {"status": "ok", "service": "tc-generator-api"}


@app.post("/api/parse")
async def parse_workbook(
    raw_file: UploadFile = File(...),
    reference_file: UploadFile | None = File(default=None),
    sys1_file: UploadFile | None = File(default=None),
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
    effective_reference_file = reference_file or sys1_file
    reference_ext = os.path.splitext(effective_reference_file.filename or "")[1].lower() if effective_reference_file and effective_reference_file.filename else ""
    if effective_reference_file and reference_ext not in ALLOWED_RAW_EXTENSIONS:
        raise HTTPException(status_code=400, detail="reference_file must be .xlsx or .xlsm")
    spec_format = detect_format(spec_file.filename) if spec_file and spec_file.filename else None
    reference_bytes = await effective_reference_file.read() if effective_reference_file else None
    spec_bytes = await spec_file.read() if spec_file else None
    job_id = _build_job_id()
    JOB_REGISTRY[job_id] = {
        "jobId": job_id,
        "rawFileName": raw_file.filename,
        "rawBytes": raw_bytes,
        "parsedData": parsed_data,
        "referenceWorkbookName": effective_reference_file.filename if effective_reference_file else None,
        "referenceWorkbookBytes": reference_bytes,
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
            "referenceWorkbookName": effective_reference_file.filename if effective_reference_file else None,
            "specFileName": spec_file.filename if spec_file else None,
            "specFormat": spec_format,
        },
    }


@app.post("/api/group")
async def preview_grouping(payload: GroupPreviewRequest) -> dict:
    job = JOB_REGISTRY.get(payload.jobId)
    if not job:
        raise HTTPException(status_code=404, detail="job not found")

    groups, framework = _build_group_preview([row.model_dump() for row in payload.rows])
    return {
        "jobId": payload.jobId,
        "groups": groups,
        "framework": framework,
        "assignments": [
            assignment
            for group in groups
            for assignment in [
                {
                    "id": row.id,
                    "reqId": row.reqId,
                    "testSet": group["testSet"],
                    "source": "existing" if (row.testSet or "").strip() else "derived",
                }
                for row in payload.rows
                if _derive_test_set_name(row.model_dump()) == group["testSet"]
            ]
        ],
    }


@app.post("/api/match")
async def preview_spec_matching(payload: MatchPreviewRequest) -> dict:
    job = JOB_REGISTRY.get(payload.jobId)
    if not job:
        raise HTTPException(status_code=404, detail="job not found")

    reference_index = _build_reference_match_index_for_job(job)
    prepared_rows = _prepare_match_preview_rows(payload.rows, job)
    matched_rows = match_spec_references(prepared_rows, reference_index) if reference_index else [
        {**row, "spec_reference": None, "match_type": "unmatched"} for row in prepared_rows
    ]

    exact_count = sum(1 for row in matched_rows if row.get("match_type") == "exact")
    unmatched_count = len(matched_rows) - exact_count
    return {
        "jobId": payload.jobId,
        "summary": {
            "total": len(matched_rows),
            "exact": exact_count,
            "unmatched": unmatched_count,
            "hasReferenceWorkbook": bool(reference_index),
        },
        "matches": [
            {
                "id": row.get("id"),
                "reqId": row.get("req_id"),
                "testItem": row.get("test_item"),
                "specReference": row.get("spec_reference"),
                "matchType": row.get("match_type"),
            }
            for row in matched_rows
        ],
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
        JOB_REGISTRY[jobId] = job  # 回寫 SQLite，避免修改只停留在反序列化副本
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
        total_input_tokens = 0
        total_output_tokens = 0
        total_cache_creation_tokens = 0
        total_cache_read_tokens = 0
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
                total_input_tokens += result.input_tokens
                total_output_tokens += result.output_tokens
                total_cache_creation_tokens += getattr(result, "cache_creation_tokens", 0)
                total_cache_read_tokens += getattr(result, "cache_read_tokens", 0)
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
                                "inputTokens": total_input_tokens,
                                "outputTokens": total_output_tokens,
                                "cacheCreationTokens": total_cache_creation_tokens,
                                "cacheReadTokens": total_cache_read_tokens,
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
        JOB_REGISTRY[jobId] = job  # 回寫 SQLite
        yield _sse_event(
            {
                "type": "job.completed",
                "jobId": jobId,
                "stats": {
                    "total": total,
                    "processed": total,
                    "currentCost": current_cost,
                    "inputTokens": total_input_tokens,
                    "outputTokens": total_output_tokens,
                    "cacheCreationTokens": total_cache_creation_tokens,
                    "cacheReadTokens": total_cache_read_tokens,
                },
                "message": "Backend generation complete. Review and export windows are ready.",
            }
        )

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.post("/api/jobs/{job_id}/regenerate/stream")
async def stream_regenerate(job_id: str, payload: RegenerateRequest) -> StreamingResponse:
    """Re-generate specific rows and stream results back as SSE."""
    job = JOB_REGISTRY.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="job not found")

    async def event_generator():
        all_rows = _prepare_generation_rows(job)
        id_set = set(payload.rowIds)
        id_order = {rid: i for i, rid in enumerate(payload.rowIds)}
        rows_to_regen = sorted(
            [r for r in all_rows if r["id"] in id_set],
            key=lambda r: id_order.get(r["id"], 999),
        )

        cfg = payload.config.model_dump() if payload.config else job.get("config", {})
        context = {
            "project": job.get("parsedData", {}).get("project"),
            "test_group": job.get("parsedData", {}).get("test_group"),
            "test_set": "N/A",
        }
        spec_index = _build_spec_index_for_job(job)
        total = len(rows_to_regen)
        model = cfg.get("model", DEFAULT_MODEL)
        batch_size = cfg.get("batchSize", 1)
        processed = 0
        current_cost = 0.0
        total_in = 0
        total_out = 0
        total_cache_create = 0
        total_cache_read = 0

        yield _sse_event({"type": "regen.started", "jobId": job_id, "total": total})

        def _stats() -> dict:
            return {
                "total": total,
                "processed": processed,
                "currentCost": round(current_cost, 4),
                "inputTokens": total_in,
                "outputTokens": total_out,
                "cacheCreationTokens": total_cache_create,
                "cacheReadTokens": total_cache_read,
            }

        for i in range(0, total, batch_size):
            batch = rows_to_regen[i : i + batch_size]
            try:
                if len(batch) == 1:
                    context["test_set"] = batch[0].get("test_set", "N/A")
                    result = generate_single_tc(batch[0], context, spec_index, RULES_SECTIONS, model)
                    tc_data_list = [result.tc_data]
                else:
                    result = generate_batch(batch, context, spec_index, RULES_SECTIONS, model)
                    tc_data_list = result.tc_data

                current_cost += result.cost
                total_in += result.input_tokens
                total_out += result.output_tokens
                total_cache_create += getattr(result, "cache_creation_tokens", 0)
                total_cache_read += getattr(result, "cache_read_tokens", 0)
                for row, tc in zip(batch, tc_data_list):
                    processed += 1
                    updated_row, _ = _build_stream_row(row, tc)
                    yield _sse_event(
                        {
                            "type": "row.regenerated",
                            "jobId": job_id,
                            "row": updated_row,
                            "stats": _stats(),
                        }
                    )
            except GenerationError as exc:
                for row in batch:
                    processed += 1
                    yield _sse_event(
                        {
                            "type": "row.regen_failed",
                            "jobId": job_id,
                            "row": _build_failed_stream_row(row, str(exc)),
                            "stats": _stats(),
                        }
                    )
            await asyncio.sleep(0.05)

        yield _sse_event(
            {
                "type": "regen.completed",
                "jobId": job_id,
                "stats": _stats(),
            }
        )

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


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
    JOB_REGISTRY[payload.jobId] = job  # 回寫 SQLite，否則下載時讀不到 exportPath
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
