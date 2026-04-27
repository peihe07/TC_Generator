"""`group_tests_tool` 單元測試。"""

from __future__ import annotations

from unittest.mock import patch

from backend.tools import group_tests_tool, get_tool, SafetyLevel
from generator import CLASSIFICATION_MODEL


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
    """Per-row classification: assignments now keyed by row uuid (id)."""
    rows = [
        {"id": "a", "reqId": "R-01", "testItem": "BT switch checkbox"},
        {"id": "b", "reqId": "R-02", "testItem": "read paired device list"},
        {"id": "c", "reqId": "R-03"},
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        return_value=_fake_classify_result({
            "a": "BT Switch",
            "b": "Device List",
            "c": "Misc",
        }),
    ) as mock_classify:
        out = group_tests_tool(rows=rows)

    assert mock_classify.called
    sent_reqs = mock_classify.call_args.args[0]
    assert [r["id"] for r in sent_reqs] == ["a", "b", "c"]
    derived_sets = {a["id"]: a["testSet"] for a in out["assignments"]}
    assert derived_sets["a"] == "BT Switch"
    assert derived_sets["b"] == "Device List"
    assert derived_sets["c"] == "Misc"
    for assignment in out["assignments"]:
        assert assignment["source"] == "derived"


def test_group_sends_original_test_set_hint_for_unresolved_rows():
    """原 workbook 的 Test Set 只能當 AI hint，不能讓 row 被視為已分類。"""
    rows = [
        {
            "id": "a",
            "reqId": "R-01",
            "testItem": "BT switch checkbox",
            "testSet": "",
            "testSetHint": "Legacy BT Switch",
        },
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        return_value=_fake_classify_result({"a": "Power Control"}),
    ) as mock_classify:
        out = group_tests_tool(rows=rows)

    sent_reqs = mock_classify.call_args.args[0]
    assert sent_reqs == [
        {
            "id": "a",
            "req_id": "R-01",
            "test_item": "BT switch checkbox",
            "current_test_set": "Legacy BT Switch",
        }
    ]
    assert out["assignments"][0]["testSet"] == "Power Control"
    assert out["assignments"][0]["source"] == "derived"


def test_group_classifies_duplicate_req_id_per_row():
    """Same Requirement ID across multiple rows with different test_items
    must each get their own Test Set, not collapse to the first one."""
    rows = [
        {"id": "r1", "reqId": "R-DUP", "testItem": "bluetooth pairing flow"},
        {"id": "r2", "reqId": "R-DUP", "testItem": "media metadata display"},
        {"id": "r3", "reqId": "R-DUP", "testItem": "phonebook synchronization"},
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        return_value=_fake_classify_result({
            "r1": "Connection",
            "r2": "Media",
            "r3": "Phonebook",
        }),
    ) as mock_classify:
        out = group_tests_tool(rows=rows)

    sent_reqs = mock_classify.call_args.args[0]
    # Each row sent independently — duplicate req_id no longer dedups.
    assert [r["id"] for r in sent_reqs] == ["r1", "r2", "r3"]
    assert [r["test_item"] for r in sent_reqs] == [
        "bluetooth pairing flow",
        "media metadata display",
        "phonebook synchronization",
    ]
    derived = {a["id"]: a["testSet"] for a in out["assignments"]}
    assert derived == {"r1": "Connection", "r2": "Media", "r3": "Phonebook"}


def test_group_uses_fixed_classification_model_by_default():
    rows = [{"id": "a", "reqId": "R-01", "testItem": "BT switch checkbox"}]
    with patch(
        "backend.tools.group.classify_test_sets",
        return_value=_fake_classify_result({"a": "Connection"}),
    ) as mock_classify:
        group_tests_tool(rows=rows)

    assert mock_classify.call_args.kwargs["model"] == CLASSIFICATION_MODEL


def test_group_mixes_existing_and_ai_classified():
    """已填 test_set 的 row 直接沿用，不帶入 AI 分類批次。"""
    rows = [
        {"id": "r1", "reqId": "R-A", "testItem": "...", "testSet": "Preset"},
        {"id": "r2", "reqId": "R-B", "testItem": "bluetooth unpair"},
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        return_value=_fake_classify_result({"r2": "BT Pairing"}),
    ) as mock_classify:
        out = group_tests_tool(rows=rows)

    # AI 只收到 r2（其 reqId = R-B）
    sent_reqs = mock_classify.call_args.args[0]
    assert [r["id"] for r in sent_reqs] == ["r2"]
    assert [r["req_id"] for r in sent_reqs] == ["R-B"]

    groups = {g["testSet"]: g for g in out["groups"]}
    assert "Preset" in groups
    assert "BT Pairing" in groups


def test_group_force_regroup_sends_existing_test_set_as_ai_hint():
    rows = [
        {"id": "r1", "reqId": "R-A", "testItem": "bluetooth connection", "testSet": "Old Connectivity"},
        {"id": "r2", "reqId": "R-B", "testItem": "media artwork", "testSet": "Old Media"},
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        return_value=_fake_classify_result({
            "r1": "BT Connection",
            "r2": "Media Metadata",
        }),
    ) as mock_classify:
        out = group_tests_tool(rows=rows, force_regroup=True)

    sent_reqs = mock_classify.call_args.args[0]
    assert sent_reqs == [
        {
            "id": "r1",
            "req_id": "R-A",
            "test_item": "bluetooth connection",
            "current_test_set": "Old Connectivity",
        },
        {
            "id": "r2",
            "req_id": "R-B",
            "test_item": "media artwork",
            "current_test_set": "Old Media",
        },
    ]
    assignments = {a["id"]: a for a in out["assignments"]}
    assert assignments["r1"]["testSet"] == "BT Connection"
    assert assignments["r1"]["source"] == "derived"
    assert assignments["r2"]["testSet"] == "Media Metadata"


def test_group_sorts_by_count_desc_then_name_asc():
    rows = [
        {"id": "r1", "reqId": "R-A-01", "testItem": "..."},
        {"id": "r2", "reqId": "R-A-02", "testItem": "..."},
        {"id": "r3", "reqId": "R-B-01", "testItem": "..."},
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        return_value=_fake_classify_result({
            "r1": "BT Switch", "r2": "BT Switch", "r3": "Device List",
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


def test_group_falls_back_when_ai_classification_fails():
    from generator import GenerationError

    rows = [
        {"id": "r1", "reqId": "SWE1-HMI-DM-001-01", "testItem": "PDM01 toggle bluetooth"},
        {"id": "r2", "reqId": "SWE1-HMI-DM-002-01", "testItem": "no keyword here"},
        {"id": "r3", "testItem": ""},
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        side_effect=GenerationError("network down"),
    ) as mock_classify:
        out = group_tests_tool(rows=rows)

    assert mock_classify.called
    derived_sets = {a["id"]: a["testSet"] for a in out["assignments"]}
    # PDM detection still wins when test_item carries a PDM code.
    assert derived_sets["r1"] == "PDM01"
    # No PDM code and AI failed → unified `Unclassified` so reviewers can
    # see at a glance that the row was not classified (replaces the old
    # `REQ <prefix>` label which looked like a real Test Set).
    assert derived_sets["r2"] == "Unclassified"
    assert derived_sets["r3"] == "Unclassified"


def test_group_fallback_uses_comfort_hmi_requirement_code_when_ai_fails():
    from generator import GenerationError

    rows = [
        {
            "id": "hmi-1",
            "reqId": "SWE1-HVAC-002-01",
            "testItem": "C1.) The system shall changes reflected in both touchscreen and hard controls",
        },
        {
            "id": "hmi-2",
            "reqId": "SWE1-HVAC-002-02",
            "testItem": "CR7.) SYNC has on/off state on climate screen",
        },
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        side_effect=GenerationError("network down"),
    ):
        out = group_tests_tool(rows=rows)

    derived_sets = {a["id"]: a["testSet"] for a in out["assignments"]}
    assert derived_sets == {"hmi-1": "C1", "hmi-2": "CR7"}


def test_group_fallback_prefers_original_test_set_hint_before_code():
    from generator import GenerationError

    rows = [
        {
            "id": "hmi-1",
            "reqId": "SWE1-HVAC-002-01",
            "testItem": "C1.) The system shall changes reflected in both touchscreen and hard controls",
            "testSetHint": "System Reflected Touchscreen Hard Controls",
        },
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        side_effect=GenerationError("network down"),
    ):
        out = group_tests_tool(rows=rows)

    assert out["assignments"][0]["testSet"] == "Touchscreen & Hard Controls"


def test_group_fallback_shortens_long_original_hmi_test_set_hints():
    from generator import GenerationError

    rows = [
        {
            "id": "hmi-1",
            "reqId": "SWE1-HVAC-002-07",
            "testItem": "The system shall on climate screen: status changes indicated directly",
            "testSetHint": "HVAC Popup Behavior",
        },
        {
            "id": "hmi-2",
            "reqId": "SWE1-HVAC-002-08",
            "testItem": "The system shall LEDs on hard controls reflect new status",
            "testSetHint": "System Leds Hard Controls Reflect New Made",
        },
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        side_effect=GenerationError("network down"),
    ):
        out = group_tests_tool(rows=rows)

    derived = {a["id"]: a["testSet"] for a in out["assignments"]}
    assert derived == {
        "hmi-1": "HVAC Popup",
        "hmi-2": "Hard Control LEDs",
    }


def test_group_lookup_falls_back_to_req_id_when_ai_returns_legacy_key():
    """If the AI ignores the new prompt and returns req_id-keyed assignments,
    group still uses them rather than dropping every row to fallback."""
    rows = [
        {"id": "r1", "reqId": "R-A", "testItem": "alpha"},
        {"id": "r2", "reqId": "R-B", "testItem": "beta"},
    ]
    with patch(
        "backend.tools.group.classify_test_sets",
        # Simulates AI returning req_id-keyed assignments (legacy behaviour).
        return_value=_fake_classify_result({
            "R-A": "Connection",
            "R-B": "Power",
        }),
    ):
        out = group_tests_tool(rows=rows)

    derived = {a["id"]: a["testSet"] for a in out["assignments"]}
    assert derived == {"r1": "Connection", "r2": "Power"}


def test_group_tool_registered():
    spec = get_tool("group_tests")
    # 會觸發 AI 呼叫 → 提升到 WRITE_COSTLY
    assert spec.safety is SafetyLevel.WRITE_COSTLY
