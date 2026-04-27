"""parse_workbook tool.

Pure function：讀檔 → 解析 → 寫入 job_store → 回傳 JSON-serializable dict。
同時被 FastAPI `/api/parse` 和 Agent dispatcher 呼叫。
"""

from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from typing import Any

from parser import parse_tc_xlsx
from spec_parser import detect_format

from .errors import ToolError
from .registry import SafetyLevel, ToolSpec, register_tool
from .schemas import PARSE_WORKBOOK_SCHEMA

ALLOWED_RAW_EXTENSIONS = {".xlsx", ".xlsm"}


def _build_preview(parsed_data: dict) -> tuple[list[str], list[dict]]:
    """回傳前 5 row 的欄位預覽。

    Import 後 Test Set 一律視為待分類；原始 workbook 的 Col H 保留在
    parsedData / columnFillStatus 裡，但不回填到前端 row preview。
    """
    preview_headers = ["req_id", "test_item", "test_set", "priority"]
    preview_rows = []
    for row in parsed_data["rows"][:5]:
        preview = {header: row.get(header, "") for header in preview_headers}
        preview["test_set"] = ""
        preview_rows.append(preview)
    return preview_headers, preview_rows


def _normalize_row(row: dict) -> dict:
    """把 parser 的 row dict 轉成前端用的 camelCase 格式。

    Test Set 不沿用原始 Excel：匯入後必須經 Configure grouping 或手動編輯
    才會成為本次 job 的正式 Test Set。
    """
    return {
        "id": f"row-{row['row_num']}",
        "rowNum": row["row_num"],
        "tcId": row.get("tc_id", ""),
        "reqId": row.get("req_id", ""),
        "testItem": row.get("test_item", ""),
        "originalRequirement": row.get("test_item", ""),
        "testSet": "",
        "specReference": row.get("spec_reference"),
        "priority": row.get("priority", ""),
        "status": "draft",
        "reviewStatus": "pending",
        "generated": None,
        "validation": [],
    }


def _build_job_id() -> str:
    return f"parse-{datetime.now().strftime('%Y%m%d-%H%M%S')}"


def _safe_upload_filename(filename: str | None, *, fallback: str, label: str) -> str:
    raw = (filename or "").strip()
    if not raw:
        return fallback
    if "/" in raw or "\\" in raw:
        raise ToolError(
            f"{label} filename must not contain path separators",
            code="bad_request",
            details={"filename": filename},
        )
    safe = os.path.basename(raw)
    if safe in {"", ".", ".."}:
        raise ToolError(
            f"{label} filename is invalid",
            code="bad_request",
            details={"filename": filename},
        )
    return safe


def _validate_extension(filename: str | None, *, label: str) -> str:
    """驗證副檔名，回傳小寫副檔名。"""
    ext = os.path.splitext(filename or "")[1].lower()
    if ext not in ALLOWED_RAW_EXTENSIONS:
        raise ToolError(
            f"{label} must be .xlsx or .xlsm",
            code="bad_request",
            details={"filename": filename, "ext": ext},
        )
    return ext


def parse_workbook_tool(
    *,
    raw_path: str,
    raw_filename: str,
    reference_path: str | None = None,
    reference_filename: str | None = None,
    spec_path: str | None = None,
    spec_filename: str | None = None,
    selected_spec_name: str | None = None,
    job_store: Any,
) -> dict:
    """Parse a TC workbook, register the job, and return the API-shaped result.

    Args:
        raw_path: 已落地到磁碟的 TC .xlsx 檔絕對路徑
        raw_filename: 原始上傳檔名（保留給 job_store 做 export 用）
        reference_path / reference_filename: 可選 SYS1 reference workbook
        spec_path / spec_filename: 可選補充文件（pdf/docx/xlsx）
        job_store: mapping-like，支援 `store[job_id] = record`

    Raises:
        ToolError: 副檔名錯誤或檔案讀取失敗
    """
    raw_filename = _safe_upload_filename(raw_filename, fallback="upload.xlsx", label="raw_file")
    _validate_extension(raw_filename, label="raw_file")

    raw_path_obj = Path(raw_path)
    if not raw_path_obj.is_file():
        raise ToolError(
            f"raw file not found: {raw_path}",
            code="not_found",
        )

    try:
        parsed_data = parse_tc_xlsx(str(raw_path_obj))
    except Exception as exc:  # parser 會丟各種錯誤，統一翻譯成 ToolError
        raise ToolError(f"failed to parse workbook: {exc}", code="unprocessable") from exc

    raw_bytes = raw_path_obj.read_bytes()

    reference_bytes: bytes | None = None
    if reference_path and reference_filename:
        reference_filename = _safe_upload_filename(
            reference_filename,
            fallback="reference.xlsx",
            label="reference_file",
        )
        _validate_extension(reference_filename, label="reference_file")
        ref_path = Path(reference_path)
        if not ref_path.is_file():
            raise ToolError(
                f"reference file not found: {reference_path}",
                code="not_found",
            )
        reference_bytes = ref_path.read_bytes()

    spec_format: str | None = None
    spec_bytes: bytes | None = None
    if spec_path and spec_filename:
        spec_filename = _safe_upload_filename(
            spec_filename,
            fallback="spec.bin",
            label="spec_file",
        )
        spec_format = detect_format(spec_filename)
        sp = Path(spec_path)
        if not sp.is_file():
            raise ToolError(
                f"spec file not found: {spec_path}",
                code="not_found",
            )
        spec_bytes = sp.read_bytes()

    preview_headers, preview_rows = _build_preview(parsed_data)

    selected_spec_name = (selected_spec_name or "").strip() or None

    job_id = _build_job_id()
    job_store[job_id] = {
        "jobId": job_id,
        "rawFileName": raw_filename,
        "rawBytes": raw_bytes,
        "parsedData": parsed_data,
        "referenceWorkbookName": reference_filename,
        "referenceWorkbookBytes": reference_bytes,
        "selectedSpecName": selected_spec_name,
        "specFileName": spec_filename,
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
            "rawFileName": raw_filename,
            "referenceWorkbookName": reference_filename,
            "selectedSpecName": selected_spec_name,
            "specFileName": spec_filename,
            "specFormat": spec_format,
        },
    }


# 註冊到 registry。JSON schema 留空，Phase 1 再補。
register_tool(
    ToolSpec(
        name="parse_workbook",
        func=parse_workbook_tool,
        description=PARSE_WORKBOOK_SCHEMA["description"],
        safety=SafetyLevel.WRITE_SAFE,
        input_schema=PARSE_WORKBOOK_SCHEMA,
    )
)
