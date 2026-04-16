"""Tests for FastAPI integration endpoints."""
from io import BytesIO
from types import SimpleNamespace
from unittest.mock import patch

from fastapi.testclient import TestClient
from openpyxl import Workbook, load_workbook

from api_server import app


def _build_workbook_bytes() -> bytes:
    wb = Workbook()
    ws_pd = wb.active
    ws_pd.title = "Product Document"
    ws_pd.cell(row=3, column=2, value="newR1L")

    ws_tc = wb.create_sheet("Test Case Specification&Result")
    ws_tc.cell(row=9, column=4, value="Requirement or Design ID")
    ws_tc.cell(row=9, column=9, value="Test Item")
    ws_tc.cell(row=10, column=4, value="SWE1-HMI-DM-001-01")
    ws_tc.cell(row=10, column=9, value="PDM01 original text")
    ws_tc.cell(row=11, column=4, value="SWE1-HMI-DM-002-01")
    ws_tc.cell(row=11, column=9, value="PDM02 original text")

    stream = BytesIO()
    wb.save(stream)
    return stream.getvalue()


client = TestClient(app)


def test_healthcheck():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_parse_workbook():
    files = {
        "raw_file": (
            "SomeProject_SWQT_DeviceManager_20260408.xlsx",
            _build_workbook_bytes(),
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    }
    response = client.post("/api/parse", files=files)
    assert response.status_code == 200
    payload = response.json()
    assert payload["project"] == "newR1L"
    assert payload["testGroup"] == "DeviceManager"
    assert payload["rowCount"] == 2
    assert payload["previewHeaders"] == ["req_id", "test_item", "test_set", "priority"]
    assert payload["rows"][0]["reqId"] == "SWE1-HMI-DM-001-01"
    assert payload["rows"][0]["tcId"] == ""


def test_parse_rejects_invalid_extension():
    files = {
        "raw_file": ("bad.txt", b"not-an-excel", "text/plain"),
    }
    response = client.post("/api/parse", files=files)
    assert response.status_code == 400


def test_create_generate_job():
    response = client.post(
        "/api/generate",
        json={
            "jobId": "parse-20260416-123456",
            "rows": [
                {
                    "id": "row-10",
                    "reqId": "SWE1-HMI-DM-001-01",
                    "testItem": "PDM01 original text",
                    "originalRequirement": "PDM01 original text",
                    "testSet": "",
                    "priority": "",
                }
            ],
            "config": {
                "model": "claude-sonnet-4-6",
                "batchSize": 5,
                "budget": 2,
                "strictValidation": False,
            },
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["jobId"] == "parse-20260416-123456"
    assert payload["status"] == "queued"
    assert payload["totalRows"] == 1
    assert "/api/generate/stream?jobId=parse-20260416-123456" in payload["streamUrl"]


@patch("api_server.generate_batch")
def test_stream_generate_job(mock_generate_batch):
    parse_response = client.post(
        "/api/parse",
        files={
            "raw_file": (
                "SomeProject_SWQT_DeviceManager_20260408.xlsx",
                _build_workbook_bytes(),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        },
    )
    payload = parse_response.json()

    mock_generate_batch.return_value = SimpleNamespace(
        tc_data=[
            {
                "test_item_rewrite": "(Condition → Outcome A)",
                "pre_conditions": "NA",
                "input_test_data": "NA",
                "test_procedure": "1. Perform setup.\n2. Verify the result.",
                "expected_result": "1. Setup completes.\n2. Result is verified.",
                "design_method": "功能測試 (Functional based ; no specific technique)",
                "priority": "High",
                "split_flag": False,
                "split_reason": "",
            },
            {
                "test_item_rewrite": "(Condition → Outcome B)",
                "pre_conditions": "NA",
                "input_test_data": "NA",
                "test_procedure": "1. Perform setup.\n2. Verify the result.",
                "expected_result": "1. Setup completes.\n2. Result is verified.",
                "design_method": "功能測試 (Functional based ; no specific technique)",
                "priority": "Medium",
                "split_flag": False,
                "split_reason": "",
            },
        ],
        input_tokens=10,
        output_tokens=20,
        cost=0.001,
    )

    client.post(
        "/api/generate",
        json={
            "jobId": payload["jobId"],
            "rows": payload["rows"],
            "config": {
                "model": "claude-sonnet-4-6",
                "batchSize": 2,
                "budget": 2,
                "strictValidation": False,
            },
        },
    )

    response = client.get("/api/generate/stream", params={"jobId": payload["jobId"]})
    assert response.status_code == 200
    assert mock_generate_batch.called
    assert '"type": "job.started"' in response.text
    assert '"type": "row.completed"' in response.text
    assert '"type": "job.completed"' in response.text
    assert '"tcId": "newR1L-DMR-001"' in response.text


@patch("api_server.generate_single_tc")
def test_stream_generate_job_marks_strict_validation_failures(mock_generate_single_tc):
    parse_response = client.post(
        "/api/parse",
        files={
            "raw_file": (
                "SomeProject_SWQT_DeviceManager_20260408.xlsx",
                _build_workbook_bytes(),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        },
    )
    payload = parse_response.json()

    mock_generate_single_tc.return_value = SimpleNamespace(
        tc_data={
            "test_item_rewrite": "(Condition → Outcome)",
            "pre_conditions": "1. Open settings menu",
            "input_test_data": "NA",
            "test_procedure": "1. Perform setup.\n2. Execute action without verification.",
            "expected_result": "1. Setup completes.\n2. Works as expected.",
            "design_method": "invalid method",
            "priority": "Critical",
            "split_flag": False,
            "split_reason": "",
        },
        input_tokens=10,
        output_tokens=20,
        cost=0.001,
    )

    client.post(
        "/api/generate",
        json={
            "jobId": payload["jobId"],
            "rows": [payload["rows"][0]],
            "config": {
                "model": "claude-sonnet-4-6",
                "batchSize": 1,
                "budget": 2,
                "strictValidation": True,
            },
        },
    )

    response = client.get("/api/generate/stream", params={"jobId": payload["jobId"]})
    assert response.status_code == 200
    assert '"type": "row.failed"' in response.text
    assert '"generated": null' in response.text


def test_export_job_and_download():
    parse_response = client.post(
        "/api/parse",
        files={
            "raw_file": (
                "SomeProject_SWQT_DeviceManager_20260408.xlsx",
                _build_workbook_bytes(),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        },
    )
    job_id = parse_response.json()["jobId"]

    export_response = client.post(
        "/api/export",
        json={
            "jobId": job_id,
            "scope": "accepted",
            "outputMode": "new-file",
            "includeFrameworkSheet": True,
            "selectedColumns": ["Test Item Rewrite", "Expected Result"],
            "rows": [
                {
                    "id": "row-10",
                    "rowNum": 10,
                    "reqId": "SWE1-HMI-DM-001-01",
                    "testItem": "PDM01 original text",
                    "reviewStatus": "accepted",
                    "testSet": "Smoke",
                    "generated": {
                        "testItemRewrite": "(PDM01 original text → Observable outcome confirmed)",
                        "preConditions": "1. Vehicle profile loaded\n2. Required subsystem available",
                        "testProcedure": (
                            "1. Open the source screen and prepare the feature.\n"
                            "2. Trigger the target behavior and verify the visible outcome."
                        ),
                        "expectedResult": (
                            "1. The setup screen is ready for the operator.\n"
                            "2. The requested behavior is shown with the correct visible outcome."
                        ),
                        "designMethod": "功能測試 (Functional based ; no specific technique)",
                        "priority": "High",
                    },
                }
            ],
        },
    )
    assert export_response.status_code == 200
    payload = export_response.json()
    assert payload["status"] == "ready"
    assert payload["exportedRows"] == 1
    assert payload["fileName"].endswith("_generated.xlsx")

    download_response = client.get(f"/api/export/download/{job_id}")
    assert download_response.status_code == 200
    assert (
        download_response.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


def test_export_respects_selected_columns():
    parse_response = client.post(
        "/api/parse",
        files={
            "raw_file": (
                "SomeProject_SWQT_DeviceManager_20260408.xlsx",
                _build_workbook_bytes(),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        },
    )
    job_id = parse_response.json()["jobId"]

    export_response = client.post(
        "/api/export",
        json={
            "jobId": job_id,
            "scope": "accepted",
            "outputMode": "new-file",
            "includeFrameworkSheet": False,
            "selectedColumns": ["Expected Result", "Priority"],
            "rows": [
                {
                    "id": "row-10",
                    "rowNum": 10,
                    "reqId": "SWE1-HMI-DM-001-01",
                    "testItem": "PDM01 original text",
                    "reviewStatus": "accepted",
                    "testSet": "Smoke",
                    "generated": {
                        "testItemRewrite": "(PDM01 original text → Observable outcome confirmed)",
                        "preConditions": "1. Vehicle profile loaded\n2. Required subsystem available",
                        "inputTestData": "NA",
                        "testProcedure": (
                            "1. Open the source screen and prepare the feature.\n"
                            "2. Trigger the target behavior and verify the visible outcome."
                        ),
                        "expectedResult": (
                            "1. The setup screen is ready for the operator.\n"
                            "2. The requested behavior is shown with the correct visible outcome."
                        ),
                        "designMethod": "功能測試 (Functional based ; no specific technique)",
                        "priority": "High",
                    },
                }
            ],
        },
    )
    assert export_response.status_code == 200

    download_response = client.get(f"/api/export/download/{job_id}")
    workbook = load_workbook(BytesIO(download_response.content))
    ws = workbook["Test Case Specification&Result"]
    assert ws.cell(row=10, column=6).value is None
    assert ws.cell(row=10, column=9).value == "PDM01 original text"
    assert ws.cell(row=10, column=13).value == (
        "1. The setup screen is ready for the operator.\n"
        "2. The requested behavior is shown with the correct visible outcome."
    )
    assert ws.cell(row=10, column=16).value == "High"
