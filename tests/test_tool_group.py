"""`group_tests_tool` 單元測試。"""

from __future__ import annotations

import pytest

from backend.tools import group_tests_tool, get_tool, SafetyLevel


def test_group_respects_existing_test_set():
    rows = [
        {"id": "r1", "reqId": "SWE1-HMI-DM-001-01", "testItem": "PDM01 text", "testSet": "Access & Entry"},
        {"id": "r2", "reqId": "SWE1-HMI-DM-002-01", "testItem": "PDM02 text", "testSet": "Access & Entry"},
    ]
    out = group_tests_tool(rows=rows)

    assert len(out["groups"]) == 1
    assert out["groups"][0]["testSet"] == "Access & Entry"
    assert out["groups"][0]["count"] == 2
    assert out["assignments"][0]["source"] == "existing"


def test_group_derives_from_pdm_code_and_req_id_fallback():
    rows = [
        {"id": "a", "reqId": "SWE1-HMI-DM-001-01", "testItem": "PDM05 behaviour"},
        {"id": "b", "reqId": "SWE1-HMI-DM-002-01", "testItem": "no code here"},
        {"id": "c", "reqId": "solo"},
    ]
    out = group_tests_tool(rows=rows)

    derived_sets = {a["id"]: a["testSet"] for a in out["assignments"]}
    assert derived_sets["a"] == "PDM05"
    assert derived_sets["b"] == "REQ-002"  # req_parts[-2]
    assert derived_sets["c"] == "Unassigned"
    for assignment in out["assignments"]:
        assert assignment["source"] == "derived"


def test_group_sorts_by_count_desc_then_name_asc():
    rows = [
        {"id": "r1", "reqId": "R-A-01", "testItem": "PDM01"},
        {"id": "r2", "reqId": "R-A-02", "testItem": "PDM01"},
        {"id": "r3", "reqId": "R-B-01", "testItem": "PDM02"},
    ]
    out = group_tests_tool(rows=rows)

    assert [g["testSet"] for g in out["groups"]] == ["PDM01", "PDM02"]
    # assignments flatten by group order
    assert [a["id"] for a in out["assignments"]] == ["r1", "r2", "r3"]


def test_group_framework_keyed_by_test_set():
    rows = [
        {"id": "r1", "reqId": "X-01", "testSet": "Alpha"},
        {"id": "r2", "reqId": "X-02", "testSet": "Alpha"},
        {"id": "r3", "reqId": "Y-01", "testSet": "Beta"},
    ]
    out = group_tests_tool(rows=rows)

    assert set(out["framework"].keys()) == {"Alpha", "Beta"}
    assert out["framework"]["Alpha"] == ["X-01", "X-02"]


def test_group_tool_registered():
    spec = get_tool("group_tests")
    assert spec.safety is SafetyLevel.READ_ONLY
