"""`inspect_workbook` / `list_jobs` / `estimate_cost` / `get_job_validation` 單元測試。"""

from __future__ import annotations

from pathlib import Path

import pytest
from openpyxl import Workbook

from backend.tools import (
    SafetyLevel,
    ToolError,
    estimate_cost_tool,
    get_job_validation_tool,
    get_tool,
    inspect_workbook_tool,
    list_jobs_tool,
)


def _build_tc_workbook(path: Path) -> Path:
    wb = Workbook()
    pd = wb.active
    pd.title = "Product Document"
    pd.cell(row=3, column=2, value="newR1L")

    tc = wb.create_sheet("Test Case Specification&Result")
    tc.cell(row=9, column=4, value="Requirement or Design ID")
    tc.cell(row=9, column=9, value="Test Item")
    for i in range(3):
        tc.cell(row=10 + i, column=4, value=f"SWE1-DM-00{i + 1}-01")
        tc.cell(row=10 + i, column=9, value=f"PDM0{i + 1} text")
    wb.save(path)
    return path


# ---------------------------------------------------------------------------
# inspect_workbook
# ---------------------------------------------------------------------------

def test_inspect_workbook_reports_sheets_and_rows(tmp_path):
    path = _build_tc_workbook(tmp_path / "Proj_SWQT_DeviceManager_20260408.xlsx")
    out = inspect_workbook_tool(path=str(path))

    assert out["fileName"].startswith("Proj_SWQT_DeviceManager")
    assert out["fileSizeBytes"] > 0
    assert "Test Case Specification&Result" in out["sheets"]
    assert out["testGroup"] == "DeviceManager"
    assert out["rowsEstimate"] == 3
    assert out["hasTcSheet"] is True


def test_inspect_workbook_rejects_missing_file(tmp_path):
    with pytest.raises(ToolError) as info:
        inspect_workbook_tool(path=str(tmp_path / "nope.xlsx"))
    assert info.value.code == "not_found"


def test_inspect_workbook_rejects_bad_extension(tmp_path):
    bad = tmp_path / "thing.txt"
    bad.write_text("nope")
    with pytest.raises(ToolError) as info:
        inspect_workbook_tool(path=str(bad))
    assert info.value.code == "bad_request"


def test_inspect_workbook_handles_no_tc_sheet(tmp_path):
    wb = Workbook()
    wb.active.title = "Some Random Sheet"
    path = tmp_path / "nope_SWQT_X_20260101.xlsx"
    wb.save(path)

    out = inspect_workbook_tool(path=str(path))
    assert out["hasTcSheet"] is False
    assert out["rowsEstimate"] == 0


def test_inspect_tool_registered():
    spec = get_tool("inspect_workbook")
    assert spec.safety is SafetyLevel.READ_ONLY


# ---------------------------------------------------------------------------
# list_jobs
# ---------------------------------------------------------------------------

def test_list_jobs_empty_store():
    out = list_jobs_tool(job_store={})
    assert out["jobs"] == []
    assert out["total"] == 0


def test_list_jobs_returns_shape_and_limit():
    store = {
        "j1": {
            "jobId": "j1",
            "rawFileName": "a.xlsx",
            "status": "parsed",
            "parsedData": {"row_count": 10, "test_group": "DM", "project": "P"},
        },
        "j2": {
            "jobId": "j2",
            "rawFileName": "b.xlsx",
            "status": "completed",
            "parsedData": {"row_count": 5, "test_group": "CM", "project": "P"},
        },
    }
    out = list_jobs_tool(limit=1, job_store=store)
    assert out["total"] == 1
    assert len(out["jobs"]) == 1
    job = out["jobs"][0]
    assert {"jobId", "fileName", "status", "rowCount", "testGroup", "project"} <= set(job)


def test_list_jobs_status_filter():
    store = {
        "j1": {"jobId": "j1", "status": "parsed", "parsedData": {"row_count": 1}},
        "j2": {"jobId": "j2", "status": "completed", "parsedData": {"row_count": 2}},
    }
    out = list_jobs_tool(status_filter="completed", job_store=store)
    assert len(out["jobs"]) == 1
    assert out["jobs"][0]["jobId"] == "j2"


def test_list_jobs_invalid_limit_raises():
    with pytest.raises(ToolError):
        list_jobs_tool(limit=0, job_store={})


def test_list_jobs_registered():
    spec = get_tool("list_jobs")
    assert spec.safety is SafetyLevel.READ_ONLY


# ---------------------------------------------------------------------------
# estimate_cost
# ---------------------------------------------------------------------------

def test_estimate_cost_positive():
    store = {
        "jX": {
            "jobId": "jX",
            "parsedData": {"row_count": 20},
        }
    }
    out = estimate_cost_tool(job_id="jX", model="gpt-4.1-mini", job_store=store)
    assert out["rowCount"] == 20
    assert out["estCostUsd"] > 0
    assert out["jobId"] == "jX"


def test_estimate_cost_missing_job():
    with pytest.raises(ToolError) as info:
        estimate_cost_tool(job_id="ghost", job_store={})
    assert info.value.code == "not_found"


def test_estimate_cost_invalid_batch_size():
    with pytest.raises(ToolError):
        estimate_cost_tool(job_id="x", batch_size=0, job_store={"x": {"parsedData": {"row_count": 1}}})


def test_estimate_cost_registered():
    spec = get_tool("estimate_cost")
    assert spec.safety is SafetyLevel.READ_ONLY


# ---------------------------------------------------------------------------
# get_job_validation
# ---------------------------------------------------------------------------

def _row_with_generated(tc_id: str, *, priority: str = "Medium") -> dict:
    return {
        "id": f"row-{tc_id}",
        "tcId": tc_id,
        "originalRequirement": "Original",
        "generated": {
            "testItemRewrite": "(A → B)",
            "preConditions": "NA",
            "testProcedure": "1. Do A to start.\n2. Verify B.",
            "expectedResult": "1. A happens.\n2. B is visible.",
            "designMethod": "功能測試 (Functional based ; no specific technique)",
            "priority": priority,
        },
    }


def test_get_job_validation_aggregates_counts():
    rows = [
        _row_with_generated("tc-1"),
        _row_with_generated("tc-2", priority="Bogus"),  # 一定有 warning
    ]
    out = get_job_validation_tool(rows=rows)

    assert out["total"] == 2
    assert out["pass"] + out["warnings"] == 2
    assert out["warnings"] >= 1
    assert len(out["perRow"]) == 2


def test_get_job_validation_skips_rows_without_generated():
    rows = [
        {"id": "r1", "tcId": "t1"},              # 無 generated
        _row_with_generated("tc-2"),
    ]
    out = get_job_validation_tool(rows=rows)

    assert out["total"] == 2
    skipped = [r for r in out["perRow"] if r.get("skipped")]
    assert len(skipped) == 1


def test_get_job_validation_registered():
    spec = get_tool("get_job_validation")
    assert spec.safety is SafetyLevel.READ_ONLY
