"""`group_tests_tool` 單元測試。"""

from __future__ import annotations

from unittest.mock import patch

from backend.tools import group_tests_tool, get_tool, SafetyLevel


def _fake_classify_result(mapping: dict[str, str]):
    from generator import ClassificationResult
    return ClassificationResult(
        assignments=mapping, input_tokens=0, output_tokens=0, cost=0.0,
    )


def test_group_respects_existing_test_set_no_ai_call():
    """All rows already have test_set → AI must not be invoked."""
    rows = [
        {"id": "r1", "reqId": "R-01", "testItem": "PDM01 text", "testSet": "Access & Entry"},
        {"id": "r2", "reqId": "R-02", "testItem": "PDM02 text", "testSet": "Access & Entry"},
    ]
    with patch("backend.tools.group.classify_test_sets") as mock_classify:
        out = group_tests_tool(rows=rows)

    assert not mock_classify.called
    assert len(out["groups"]) == 1
    assert out["groups"][0]["testSet"] == "Access & Entry"
    assert out["groups"][0]["count"] == 2
    assert out["assignments"][0]["source"] == "existing"


def test_group_calls_ai_for_unresolved_rows():
    rows = [
        {"id": "a", "reqId": "R-01", "testItem": "BT switch checkbox"},
        {"id": "b", "reqId": "R-02", "testItem": "read paired device list"},
        {"id": "c", "reqId": "R-03"},
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        return_value=_fake_classify_result({
            "R-01": "BT Switch",
            "R-02": "Device List",
            "R-03": "Misc",
        }),
    ) as mock_classify:
        out = group_tests_tool(rows=rows)

    assert mock_classify.called
    derived_sets = {a["id"]: a["testSet"] for a in out["assignments"]}
    assert derived_sets["a"] == "BT Switch"
    assert derived_sets["b"] == "Device List"
    assert derived_sets["c"] == "Misc"
    for assignment in out["assignments"]:
        assert assignment["source"] == "derived"


def test_group_mixes_existing_and_ai_classified():
    """已填 test_set 的 row 直接沿用，不帶入 AI 分類批次。"""
    rows = [
        {"id": "r1", "reqId": "R-A", "testItem": "...", "testSet": "Preset"},
        {"id": "r2", "reqId": "R-B", "testItem": "bluetooth unpair"},
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        return_value=_fake_classify_result({"R-B": "BT Pairing"}),
    ) as mock_classify:
        out = group_tests_tool(rows=rows)

    # AI 只收到 R-B
    sent_reqs = mock_classify.call_args.args[0]
    assert [r["req_id"] for r in sent_reqs] == ["R-B"]

    groups = {g["testSet"]: g for g in out["groups"]}
    assert "Preset" in groups
    assert "BT Pairing" in groups


def test_group_sorts_by_count_desc_then_name_asc():
    rows = [
        {"id": "r1", "reqId": "R-A-01", "testItem": "..."},
        {"id": "r2", "reqId": "R-A-02", "testItem": "..."},
        {"id": "r3", "reqId": "R-B-01", "testItem": "..."},
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        return_value=_fake_classify_result({
            "R-A-01": "BT Switch", "R-A-02": "BT Switch", "R-B-01": "Device List",
        }),
    ):
        out = group_tests_tool(rows=rows)

    assert [g["testSet"] for g in out["groups"]] == ["BT Switch", "Device List"]
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
    # 會觸發 AI 呼叫 → 提升到 WRITE_COSTLY
    assert spec.safety is SafetyLevel.WRITE_COSTLY
