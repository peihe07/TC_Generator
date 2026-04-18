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

ALLOWED_RAW_EXTENSIONS = {".xlsx", ".xlsm"}


def _build_preview(parsed_data: dict) -> tuple[list[str], list[dict]]:
    """回傳前 5 row 的欄位預覽。"""
    preview_headers = ["req_id", "test_item", "test_set", "priority"]
    preview_rows = [
        {header: row.get(header, "") for header in preview_headers}
        for row in parsed_data["rows"][:5]
    ]
    return preview_headers, preview_rows


def _normalize_row(row: dict) -> dict:
    """把 parser 的 row dict 轉成前端用的 camelCase 格式。"""
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


def _build_job_id() -> str:
    return f"parse-{datetime.now().strftime('%Y%m%d-%H%M%S')}"


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
        spec_format = detect_format(spec_filename)
        sp = Path(spec_path)
        if not sp.is_file():
            raise ToolError(
                f"spec file not found: {spec_path}",
                code="not_found",
            )
        spec_bytes = sp.read_bytes()

    preview_headers, preview_rows = _build_preview(parsed_data)

    job_id = _build_job_id()
    job_store[job_id] = {
        "jobId": job_id,
        "rawFileName": raw_filename,
        "rawBytes": raw_bytes,
        "parsedData": parsed_data,
        "referenceWorkbookName": reference_filename,
        "referenceWorkbookBytes": reference_bytes,
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
            "specFileName": spec_filename,
            "specFormat": spec_format,
        },
    }


# 註冊到 registry。JSON schema 留空，Phase 1 再補。
register_tool(
    ToolSpec(
        name="parse_workbook",
        func=parse_workbook_tool,
        description=(
            "Parse an ASPICE SWE.6 TC workbook (.xlsx/.xlsm) into structured rows. "
            "Registers a job and returns jobId for downstream tools."
        ),
        safety=SafetyLevel.WRITE_SAFE,
    )
)
