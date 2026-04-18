"""write_excel tool：把生成結果寫回 .xlsx（含可選的 Test Case Framework sheet）。"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

from writer import write_framework_sheet, write_generated_results

from .errors import ToolError
from .registry import SafetyLevel, ToolSpec, register_tool
from .schemas import WRITE_EXCEL_SCHEMA


def write_excel_tool(
    *,
    source_path: str,
    output_path: str,
    rows: list[dict],
    selected_fields: Iterable[str] | None = None,
    framework_rows: list[dict] | None = None,
) -> dict:
    """把 rows 寫回 Excel，可選擇性追加 framework sheet。

    Args:
        source_path: 原始 .xlsx（當作寫入模板）
        output_path: 輸出檔路徑（可與 source_path 相同 = overwrite 模式）
        rows: list of dict，至少需含 `row_num`, `tc_id`, 以及 writer 認得的欄位
        selected_fields: 可選的欄位白名單；None 表示全部欄位都寫
        framework_rows: 可選 framework sheet 資料

    Returns:
        `{"outputPath", "rowsWritten", "frameworkSheetWritten"}`

    Raises:
        ToolError: source 不存在、或 rows 為空
    """
    if not rows:
        raise ToolError("no exportable rows", code="bad_request")

    source = Path(source_path)
    if not source.is_file():
        raise ToolError(f"source workbook not found: {source_path}", code="not_found")

    # 確保輸出目錄存在
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    selected = set(selected_fields) if selected_fields else None
    write_generated_results(str(source), rows, str(out), selected_fields=selected)

    framework_written = False
    if framework_rows:
        write_framework_sheet(str(out), framework_rows, str(out))
        framework_written = True

    return {
        "outputPath": str(out),
        "rowsWritten": len(rows),
        "frameworkSheetWritten": framework_written,
    }


register_tool(
    ToolSpec(
        name="write_excel",
        func=write_excel_tool,
        description=WRITE_EXCEL_SCHEMA["description"],
        safety=SafetyLevel.DESTRUCTIVE,
        input_schema=WRITE_EXCEL_SCHEMA,
    )
)
