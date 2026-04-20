"""Tests for FastAPI integration endpoints."""
from io import BytesIO
from types import SimpleNamespace
from unittest.mock import patch

import json
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


def _build_reference_workbook_bytes() -> bytes:
    wb = Workbook()
    ws = wb.active
    ws.title = "Basic Report"
    ws.cell(row=1, column=1, value="NRL ID")
    ws.cell(row=1, column=3, value="Outline")
    ws.cell(row=1, column=4, value="Description")
    ws.cell(row=1, column=5, value="Source ID")
    ws.cell(row=2, column=1, value="NRL-001")
    ws.cell(row=2, column=3, value="Device Manager")
    ws.cell(row=2, column=4, value="PDM01 behavior description")
    ws.cell(row=2, column=5, value="SPEC_REF_PDM01")
    ws.cell(row=3, column=1, value="NRL-002")
    ws.cell(row=3, column=3, value="Device Manager")
    ws.cell(row=3, column=4, value="PDM02 behavior description")
    ws.cell(row=3, column=5, value="SPEC_REF_PDM02")

    stream = BytesIO()
    wb.save(stream)
    return stream.getvalue()


client = TestClient(app)


def test_healthcheck():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_metrics_aggregate_returns_shape_with_empty_store():
    # 測試環境 JOB_REGISTRY 可能有也可能沒有資料；只驗回傳 shape 正確
    response = client.get("/api/metrics/aggregate")
    assert response.status_code == 200
    payload = response.json()
    for field in (
        "jobCount", "totalRowCount", "totalCostUsd", "avgCostUsd",
        "avgRowCount", "matchRate", "jobsWithCost", "jobsWithMatch",
    ):
        assert field in payload


def test_metrics_aggregate_rejects_unknown_job_id():
    response = client.get("/api/metrics/aggregate?job_ids=__does_not_exist__")
    assert response.status_code == 404


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


def test_parse_workbook_accepts_reference_workbook():
    files = {
        "raw_file": (
            "SomeProject_SWQT_DeviceManager_20260408.xlsx",
            _build_workbook_bytes(),
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ),
        "reference_file": (
            "ReferenceWorkbook.xlsx",
            _build_reference_workbook_bytes(),
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ),
    }
    response = client.post("/api/parse", files=files)
    assert response.status_code == 200
    payload = response.json()
    assert payload["files"]["referenceWorkbookName"] == "ReferenceWorkbook.xlsx"


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
                "model": "gpt-4.1",
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


@patch("tools.generate.generate_batch")
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
                "model": "gpt-4.1",
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
    assert '"tcId": "newR1L-DM-001"' in response.text


def _build_mixed_workbook_bytes() -> bytes:
    """Row 10 is a reference example (Pre-Cond/Procedure/Expected filled).
    Row 11 is a new row that needs generation.
    """
    wb = Workbook()
    ws_pd = wb.active
    ws_pd.title = "Product Document"
    ws_pd.cell(row=3, column=2, value="newR1L")

    ws_tc = wb.create_sheet("Test Case Specification&Result")
    ws_tc.cell(row=9, column=4, value="Requirement or Design ID")
    ws_tc.cell(row=9, column=9, value="Test Item")

    # Row 10: reference example — fully populated, must not be regenerated.
    ws_tc.cell(row=10, column=4, value="SWE1-REF-001")
    ws_tc.cell(row=10, column=9, value="Reference test item text")
    ws_tc.cell(row=10, column=10, value="1. Reference pre-condition")
    ws_tc.cell(row=10, column=12, value="1. Reference procedure step")
    ws_tc.cell(row=10, column=13, value="1. Reference expected outcome")

    # Row 11: needs generation.
    ws_tc.cell(row=11, column=4, value="SWE1-NEW-002")
    ws_tc.cell(row=11, column=9, value="New test item text")

    stream = BytesIO()
    wb.save(stream)
    return stream.getvalue()


@patch("tools.generate.generate_single_tc")
def test_stream_generate_preserves_existing_content(mock_generate_single):
    """RULES.md §499 — rows with existing Pre-Cond/Procedure/Expected are
    passed through without an AI call; only empty rows trigger generation.
    """
    parse_response = client.post(
        "/api/parse",
        files={
            "raw_file": (
                "SomeProject_SWQT_DeviceManager_20260408.xlsx",
                _build_mixed_workbook_bytes(),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        },
    )
    parsed = parse_response.json()

    mock_generate_single.return_value = SimpleNamespace(
        tc_data={
            "test_item_rewrite": "(Condition → Outcome)",
            "pre_conditions": "NA",
            "input_test_data": "NA",
            "test_procedure": "1. Setup.\n2. Verify.",
            "expected_result": "1. Setup ok.\n2. Verified.",
            "design_method": "功能測試 (Functional based ; no specific technique)",
            "priority": "Medium",
            "split_flag": False,
            "split_reason": "",
        },
        input_tokens=10,
        output_tokens=20,
        cache_creation_tokens=0,
        cache_read_tokens=0,
        cost=0.001,
        model="gpt-4.1",
    )

    client.post(
        "/api/generate",
        json={
            "jobId": parsed["jobId"],
            "rows": parsed["rows"],
            "config": {
                "model": "gpt-4.1",
                "batchSize": 1,
                "budget": 2,
                "strictValidation": False,
            },
        },
    )

    response = client.get("/api/generate/stream", params={"jobId": parsed["jobId"]})
    assert response.status_code == 200
    # AI called exactly once — for the empty row only.
    assert mock_generate_single.call_count == 1
    sent_row = mock_generate_single.call_args.args[0]
    assert sent_row["req_id"] == "SWE1-NEW-002"

    # Preserved row's original content survives in the SSE payload.
    assert "Reference pre-condition" in response.text
    assert "Reference procedure step" in response.text
    assert "Reference expected outcome" in response.text
    assert '"preserved": true' in response.text
    assert "1 to generate, 1 preserved" in response.text


@patch("tools.generate.generate_batch")
def test_stream_generate_regenerate_all_skips_preservation(mock_generate_batch):
    """regenerateAll=True forces AI regeneration for every row."""
    parse_response = client.post(
        "/api/parse",
        files={
            "raw_file": (
                "SomeProject_SWQT_DeviceManager_20260408.xlsx",
                _build_mixed_workbook_bytes(),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        },
    )
    parsed = parse_response.json()

    mock_generate_batch.return_value = SimpleNamespace(
        tc_data=[
            {
                "test_item_rewrite": "(Condition → Outcome)",
                "pre_conditions": "NA",
                "input_test_data": "NA",
                "test_procedure": "1. Setup.\n2. Verify.",
                "expected_result": "1. Setup ok.\n2. Verified.",
                "design_method": "功能測試 (Functional based ; no specific technique)",
                "priority": "Medium",
                "split_flag": False,
                "split_reason": "",
            }
        ] * 2,
        input_tokens=10,
        output_tokens=20,
        cost=0.001,
    )

    client.post(
        "/api/generate",
        json={
            "jobId": parsed["jobId"],
            "rows": parsed["rows"],
            "config": {
                "model": "gpt-4.1",
                "batchSize": 2,
                "budget": 2,
                "strictValidation": False,
                "regenerateAll": True,
            },
        },
    )

    response = client.get("/api/generate/stream", params={"jobId": parsed["jobId"]})
    assert response.status_code == 200
    # Both rows in one batch — AI called once with 2 rows.
    assert mock_generate_batch.call_count == 1
    sent_rows = mock_generate_batch.call_args.args[0]
    assert len(sent_rows) == 2


@patch("tools.generate.generate_single_tc")
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
                "model": "gpt-4.1",
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


@patch("tools.generate.generate_single_tc")
def test_stream_generate_job_keeps_warning_rows_completed_in_non_strict_mode(mock_generate_single_tc):
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
                "model": "gpt-4.1",
                "batchSize": 1,
                "budget": 2,
                "strictValidation": False,
            },
        },
    )

    response = client.get("/api/generate/stream", params={"jobId": payload["jobId"]})
    assert response.status_code == 200
    assert '"type": "row.completed"' in response.text
    assert '"status": "ready"' in response.text
    assert '"generated": {' in response.text


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


def test_group_preview_returns_assignments():
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

    response = client.post(
        "/api/group",
        json={
            "jobId": payload["jobId"],
            "rows": payload["rows"],
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["groups"]
    assert body["assignments"]
    assert body["assignments"][0]["testSet"]


def test_match_preview_uses_reference_workbook():
    parse_response = client.post(
        "/api/parse",
        files={
            "raw_file": (
                "SomeProject_SWQT_DeviceManager_20260408.xlsx",
                _build_workbook_bytes(),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ),
            "reference_file": (
                "ReferenceWorkbook.xlsx",
                _build_reference_workbook_bytes(),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ),
        },
    )
    payload = parse_response.json()

    response = client.post(
        "/api/match",
        json={
            "jobId": payload["jobId"],
            "rows": payload["rows"],
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["summary"]["hasReferenceWorkbook"] is True
    assert body["summary"]["exact"] == 2
    assert body["matches"][0]["specReference"] == "SPEC_REF_PDM01"


# ── Quick Generate Stream ─────────────────────────────────────────────────────

VALID_TC_JSON = {
    "test_item_rewrite": "(Button pressed → LED turns on)",
    "pre_conditions": "1. System is powered.",
    "input_test_data": "NA",
    "test_procedure": "1. Press button.\n2. Observe LED.",
    "expected_result": "1. LED turns on.",
    "design_method": "Functional",
    "priority": "Medium",
    "split_flag": False,
    "split_reason": "",
}

VALID_DECOMPOSE_RESPONSE = {
    "reasoning": "Two distinct scenarios: normal and boundary.",
    "scenarios": [
        {"id": 1, "name": "Normal", "description": "Primary path.", "test_item": "Button pressed → LED on"},
        {"id": 2, "name": "Boundary", "description": "Edge case.", "test_item": "Button held → LED blink"},
    ],
}


def _parse_sse(content: bytes) -> list[dict]:
    """Parse SSE response body into a list of event dicts."""
    events = []
    for line in content.decode().split("\n"):
        line = line.strip()
        if line.startswith("data: "):
            try:
                events.append(json.loads(line[len("data: "):]))
            except json.JSONDecodeError:
                pass
    return events


@patch("api_server.generate_quick_tc")
def test_quick_generate_single_mode(mock_gen):
    from generator import GenerationResult
    mock_gen.return_value = GenerationResult(
        tc_data=VALID_TC_JSON,
        input_tokens=300,
        output_tokens=150,
        cost=0.003,
        model="gpt-4.1",
    )

    response = client.post(
        "/api/quick-generate/stream",
        json={"testItem": "Button pressed → LED on", "context": None, "mode": "single", "model": "gpt-4.1"},
    )
    assert response.status_code == 200
    events = _parse_sse(response.content)
    types = [e["type"] for e in events]
    assert "job.started" in types
    assert "tc.completed" in types
    assert "job.completed" in types

    tc_event = next(e for e in events if e["type"] == "tc.completed")
    assert tc_event["tc"]["priority"] == "Medium"
    assert tc_event["scenarioId"] == 1


@patch("api_server.generate_quick_tc")
def test_quick_generate_with_context_mode(mock_gen):
    from generator import GenerationResult
    mock_gen.return_value = GenerationResult(
        tc_data=VALID_TC_JSON,
        input_tokens=400,
        output_tokens=200,
        cost=0.004,
        model="gpt-4.1",
    )

    response = client.post(
        "/api/quick-generate/stream",
        json={
            "testItem": "Button pressed → LED on",
            "context": "System must be powered",
            "mode": "with_context",
            "model": "gpt-4.1",
        },
    )
    assert response.status_code == 200
    events = _parse_sse(response.content)
    # generate_quick_tc should receive context
    call_kwargs = mock_gen.call_args[1]
    assert call_kwargs["context"] == "System must be powered"
    types = [e["type"] for e in events]
    assert "tc.completed" in types
    assert "job.completed" in types


@patch("api_server.generate_quick_tc")
def test_quick_generate_single_mode_api_error(mock_gen):
    from generator import GenerationError
    mock_gen.side_effect = GenerationError("API timeout")

    response = client.post(
        "/api/quick-generate/stream",
        json={"testItem": "some item", "context": None, "mode": "single", "model": "gpt-4.1"},
    )
    assert response.status_code == 200
    events = _parse_sse(response.content)
    types = [e["type"] for e in events]
    assert "job.failed" in types
    failed = next(e for e in events if e["type"] == "job.failed")
    assert "API timeout" in failed["message"]


@patch("api_server.generate_quick_tc")
@patch("api_server.decompose_requirement")
def test_quick_generate_decompose_mode(mock_decompose, mock_gen):
    from generator import DecomposeResult, GenerationResult
    mock_decompose.return_value = DecomposeResult(
        reasoning=VALID_DECOMPOSE_RESPONSE["reasoning"],
        scenarios=VALID_DECOMPOSE_RESPONSE["scenarios"],
        input_tokens=500,
        output_tokens=250,
        cost=0.005,
    )
    mock_gen.return_value = GenerationResult(
        tc_data=VALID_TC_JSON,
        input_tokens=300,
        output_tokens=150,
        cost=0.003,
        model="gpt-4.1",
    )

    response = client.post(
        "/api/quick-generate/stream",
        json={"testItem": "Full requirement text", "context": None, "mode": "decompose", "model": "gpt-4.1"},
    )
    assert response.status_code == 200
    events = _parse_sse(response.content)
    types = [e["type"] for e in events]

    assert "job.started" in types
    assert "decompose.analysis" in types
    assert "tc.generating" in types
    assert "tc.completed" in types
    assert "job.completed" in types

    # Two scenarios → two tc.completed events
    tc_done = [e for e in events if e["type"] == "tc.completed"]
    assert len(tc_done) == 2

    analysis = next(e for e in events if e["type"] == "decompose.analysis")
    assert len(analysis["scenarios"]) == 2


@patch("api_server.decompose_requirement")
def test_quick_generate_decompose_mode_decompose_error(mock_decompose):
    from generator import GenerationError
    mock_decompose.side_effect = GenerationError("Decompose failed")

    response = client.post(
        "/api/quick-generate/stream",
        json={"testItem": "Full requirement text", "context": None, "mode": "decompose", "model": "gpt-4.1"},
    )
    assert response.status_code == 200
    events = _parse_sse(response.content)
    types = [e["type"] for e in events]
    assert "job.failed" in types
    failed = next(e for e in events if e["type"] == "job.failed")
    assert "Decompose failed" in failed["message"]
