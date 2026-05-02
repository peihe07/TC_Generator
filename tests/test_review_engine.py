"""Tests for the ASPICE SWE.6 Review engine.

Covers:
  - 4 deep-dive cases referenced by CLAUDE_CODE_BRIEF.md (synthesized
    fixtures rather than pulling rows out of a real workbook):
      A: fabricated value Critical (§7.4) — group has spec句
      B: multiple fabricated values across siblings
      C: multi-Req-ID + tool launch (§6.7 + §7.5 + §6.2-style boundary)
      D: tier1_skipped + §8.3.6 fallback (§6.6 + §8.3.6, NOT §7.4)
  - severity ceiling enforcement (Tier 3 cannot emit Critical)
  - §7.4 ⊕ §8.3.6 mutual exclusion
  - §6.4 → §8.1.4 suppression
  - dry_run does not invoke OpenAI
"""
from __future__ import annotations

from openpyxl import Workbook

import pytest

import review_engine
from review_engine import (
    ReqGroup,
    ReviewEngineError,
    TCRecord,
    _build_groups,
    _detect_7_4_or_8_3_6,
    _detect_7_5,
    _enforce_severity_ceiling,
    _normalize_row,
    _run_regex_pipeline,
    extract_spec_sentence,
    review_workbook,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _build_workbook(tmp_path, rows):
    fp = tmp_path / "Review_SWQT_Projection_20260502.xlsx"
    wb = Workbook()
    ws_pd = wb.active
    ws_pd.title = "Product Document"
    ws_pd.cell(row=3, column=2, value="Projection")

    ws_tc = wb.create_sheet("Test Case Specification&Result")
    headers = {
        2: "Test Level", 3: "Verification Criteria", 4: "Requirement or Design ID",
        5: "Functional Safety", 6: "Test Case ID", 7: "Test Group",
        8: "Test Set", 9: "Test Item", 10: "Pre-Conditions",
        11: "Input Test Data", 12: "Test Procedure", 13: "Expected Result",
        14: "Specification Reference", 15: "Remark", 16: "Test Case Priority",
        17: "Test Case Design Method",
    }
    for col, name in headers.items():
        ws_tc.cell(row=9, column=col, value=name)

    col_letter_to_idx = {chr(ord("A") + i): i + 1 for i in range(17)}
    for offset, row in enumerate(rows):
        r = 10 + offset
        for letter, value in row.items():
            ws_tc.cell(row=r, column=col_letter_to_idx[letter], value=value)
    wb.save(fp)
    return str(fp)


def _make_tc(**kw) -> TCRecord:
    """Cheap TCRecord factory with sensible defaults."""
    defaults = {
        "row_num": kw.pop("row_num", 10),
        "tc_id": kw.pop("tc_id", "TC-X-001"),
        "req_id_raw": kw.pop("req_id_raw", "REQ-A"),
        "req_ids": kw.pop("req_ids", ["REQ-A"]),
        "test_item": kw.pop("test_item", ""),
        "pre_conditions": kw.pop("pre_conditions", ""),
        "input_test_data": kw.pop("input_test_data", ""),
        "test_procedure": kw.pop("test_procedure", ""),
        "expected_result": kw.pop("expected_result", ""),
        "spec_reference": kw.pop("spec_reference", ""),
        "priority": kw.pop("priority", "P1"),
        "design_method": kw.pop("design_method", "Functional"),
    }
    return TCRecord(**defaults)


# ---------------------------------------------------------------------------
# Severity ceiling
# ---------------------------------------------------------------------------


def test_severity_ceiling_tier3_cannot_emit_critical():
    with pytest.raises(ReviewEngineError):
        _enforce_severity_ceiling(3, "§8.X", "Critical")


def test_severity_ceiling_passes_at_ceiling():
    assert _enforce_severity_ceiling(3, "§8.5.2", "Major") == "Major"
    assert _enforce_severity_ceiling(2, "§7.4", "Critical") == "Critical"
    assert _enforce_severity_ceiling(1, "§6.5", "Critical") == "Critical"


def test_unknown_severity_raises():
    with pytest.raises(ReviewEngineError):
        _enforce_severity_ceiling(2, "§7.5", "Severe")


# ---------------------------------------------------------------------------
# Spec句 extraction
# ---------------------------------------------------------------------------


def test_extract_english_spec_sentence():
    s = extract_spec_sentence("the HU shall connect to the device")
    assert s is not None and "shall" in s


def test_extract_returns_none_when_no_modal():
    assert extract_spec_sentence("車機應該完成連線（中文 only）") is None


def test_multi_req_id_segment_match():
    text = (
        "[SWE1-PROJ-212]\nAudio sensitivity MUST be 2500 RMS\n"
        "[SWE1-PROJ-213]\nAudio distortion MUST be < 1%"
    )
    s_a = extract_spec_sentence(text, "SWE1-PROJ-212")
    s_b = extract_spec_sentence(text, "SWE1-PROJ-213")
    assert s_a and "2500 RMS" in s_a
    assert s_b and "< 1%" in s_b


# ---------------------------------------------------------------------------
# Group A — fabricated value Critical (§7.4)
# ---------------------------------------------------------------------------


def test_group_a_fabricated_value_fires_7_4_when_spec_present():
    """Spec句 exists; spec_reference empty; "等待5秒" not in spec — §7.4 Critical fires.
    §8.3.6 must NOT fire (mutual exclusion)."""
    tc = _make_tc(
        test_item="the HU shall complete pairing",
        test_procedure="1. Bond the device.\n2. 等待5秒.\n3. Confirm pairing.",
        spec_reference="",
    )
    group = ReqGroup(req_id="REQ-A", tcs=[tc], spec_sentence="the HU shall complete pairing", tier1_skipped=False)
    findings = _detect_7_4_or_8_3_6(tc, group)
    refs = [f["rule_ref"] for f in findings]
    assert "§7.4" in refs
    assert "§8.3.6" not in refs
    f74 = next(f for f in findings if f["rule_ref"] == "§7.4")
    assert f74["severity"] == "Critical"
    assert f74["tier"] == 2
    assert f74["evidence_req_spec"] == "the HU shall complete pairing"


def test_value_in_spec_reference_does_not_fire_7_4():
    tc = _make_tc(
        test_item="the HU shall complete pairing",
        test_procedure="1. 等待 5 秒.",
        spec_reference="Spec §3.2: timeout 5 sec",
    )
    group = ReqGroup(req_id="REQ-A", tcs=[tc], spec_sentence="the HU shall complete pairing")
    assert _detect_7_4_or_8_3_6(tc, group) == []


def test_value_in_spec_sentence_does_not_fire_7_4():
    tc = _make_tc(
        test_item="the HU shall complete pairing in 5 seconds",
        test_procedure="1. 等待 5 秒.",
    )
    group = ReqGroup(req_id="REQ-A", tcs=[tc], spec_sentence="the HU shall complete pairing in 5 seconds")
    assert _detect_7_4_or_8_3_6(tc, group) == []


# ---------------------------------------------------------------------------
# Group B — multiple fabricated values (§7.4 fires per value)
# ---------------------------------------------------------------------------


def test_group_b_multiple_fabricated_values():
    tc = _make_tc(
        test_item="the system shall handle long sessions",
        test_procedure="1. 持續 30 分鐘.\n2. 重複 20 次.\n3. 維持 3 小時.",
        spec_reference="",
    )
    group = ReqGroup(req_id="REQ-B", tcs=[tc],
                     spec_sentence="the system shall handle long sessions")
    findings = _detect_7_4_or_8_3_6(tc, group)
    assert len(findings) == 3
    assert all(f["rule_ref"] == "§7.4" and f["severity"] == "Critical" for f in findings)


# ---------------------------------------------------------------------------
# Group C — multi-Req-ID + Tool launch (§6.7 + §7.5)
# ---------------------------------------------------------------------------


def test_group_c_multi_req_and_tool_launch(tmp_path):
    fp = _build_workbook(tmp_path, [{
        "D": "SWE1-PROJ-212\nSWE1-PROJ-213",
        "F": "TC-PROJ-212-001",
        "I": (
            "[SWE1-PROJ-212]\nAudio sensitivity MUST be 2500 RMS.\n"
            "[SWE1-PROJ-213]\nAudio distortion MUST be < 1%."
        ),
        "L": (
            "1. Setup phone.\n"
            "2. Connect HFP.\n"
            "3. Open PCTS-MT1 panel.\n"
            "4. Configure test profile.\n"
            "5. Run PCTS-MT1 to start measurement."
        ),
        "M": "1. ok\n2. ok\n3. ok\n4. ok\n5. measurement started.",
        "N": "",
        "P": "P1",
        "Q": "Functional",
    }])

    report = review_workbook(fp, dry_run=True)

    # §6.7 fires once with comma-joined req_id
    f67 = [f for f in report["per_req_findings"] if f["rule_ref"] == "§6.7"]
    assert len(f67) == 1
    assert f67[0]["req_id"] == "SWE1-PROJ-212, SWE1-PROJ-213"
    assert f67[0]["severity"] == "Major"

    # §7.5 fires on the multi-Req TC (last step launches PCTS-MT1, no follow-up)
    tc_entry = report["per_tc_findings"][0]
    refs = [f["rule_ref"] for f in tc_entry["findings"]]
    assert "§7.5" in refs


# ---------------------------------------------------------------------------
# Group D — tier1_skipped + §8.3.6 fallback (NOT §7.4)
# ---------------------------------------------------------------------------


def test_group_d_tier1_skipped_triggers_8_3_6_not_7_4(tmp_path):
    """When the Req group has no English spec句, §6.6 fires (Major),
    Tier 2 §7.4 is skipped, and §8.3.6 fallback (Major) takes the
    fabricated-value finding."""
    fp = _build_workbook(tmp_path, [{
        "D": "SWE1-PROJ-229",
        "F": "TC-PROJ-229-001",
        "I": "車機應在配對流程中完成裝置綁定。",
        "L": "1. 觸發配對\n2. 重複 5 次\n3. 確認結果",
        "M": "1. 開始\n2. 完成\n3. 通過",
        "N": "",
        "P": "P1",
        "Q": "Functional",
    }])
    report = review_workbook(fp, dry_run=True)

    refs_req = [f["rule_ref"] for f in report["per_req_findings"]]
    assert "§6.6" in refs_req

    tc_entry = report["per_tc_findings"][0]
    refs = [f["rule_ref"] for f in tc_entry["findings"]]
    assert "§8.3.6" in refs
    assert "§7.4" not in refs
    assert "§7.5" not in refs  # Tier 2 entirely skipped


# ---------------------------------------------------------------------------
# Mutual exclusion sanity (synthesized)
# ---------------------------------------------------------------------------


def test_mutual_exclusion_74_836_never_both_on_same_value():
    tc = _make_tc(
        test_procedure="1. 等待 5 秒",
        spec_reference="",
    )
    # Tier1 active group → §7.4 only
    g_active = ReqGroup(req_id="REQ", tcs=[tc],
                        spec_sentence="the HU shall connect", tier1_skipped=False)
    f1 = _detect_7_4_or_8_3_6(tc, g_active)
    refs1 = {f["rule_ref"] for f in f1}
    assert refs1 == {"§7.4"}

    # Tier1 skipped group → §8.3.6 only
    g_skipped = ReqGroup(req_id="REQ", tcs=[tc], spec_sentence=None, tier1_skipped=True)
    f2 = _detect_7_4_or_8_3_6(tc, g_skipped)
    refs2 = {f["rule_ref"] for f in f2}
    assert refs2 == {"§8.3.6"}


# ---------------------------------------------------------------------------
# §6.4 ↔ §8.1.4 suppression
# ---------------------------------------------------------------------------


def test_64_fires_when_siblings_have_identical_test_item(tmp_path):
    fp = _build_workbook(tmp_path, [
        {"D": "REQ-DUP", "F": "TC-A", "I": "the device shall connect via BT",
         "L": "1. Step.", "M": "1. Done.", "P": "P1", "Q": "Functional"},
        {"D": "REQ-DUP", "F": "TC-B", "I": "the device shall connect via BT",
         "L": "1. Step.", "M": "1. Done.", "P": "P1", "Q": "Functional"},
    ])
    report = review_workbook(fp, dry_run=True)
    refs = [f["rule_ref"] for f in report["per_req_findings"]]
    assert "§6.4" in refs


# ---------------------------------------------------------------------------
# Tier 3 detectors (sanity)
# ---------------------------------------------------------------------------


def test_8_5_2_design_method_missing(tmp_path):
    fp = _build_workbook(tmp_path, [{
        "D": "REQ-A",
        "F": "TC-A-1",
        "I": "the HU shall display the icon",
        "L": "1. Open menu.\n2. Confirm icon visible.",
        "M": "1. Menu opens.\n2. Icon shown.",
        "P": "P1",
        # Q (design_method) intentionally blank
    }])
    report = review_workbook(fp, dry_run=True)
    refs = [f["rule_ref"] for f in report["per_tc_findings"][0]["findings"]]
    assert "§8.5.2" in refs


def test_8_5_1_priority_outside_p0_p3(tmp_path):
    fp = _build_workbook(tmp_path, [{
        "D": "REQ-A", "F": "TC-A-1",
        "I": "the HU shall display the icon",
        "L": "1. Open menu.\n2. Confirm icon visible.",
        "M": "1. Menu opens.\n2. Icon shown.",
        "P": "High",
        "Q": "Functional",
    }])
    report = review_workbook(fp, dry_run=True)
    refs = [f["rule_ref"] for f in report["per_tc_findings"][0]["findings"]]
    assert "§8.5.1" in refs


def test_8_3_1_forbidden_verb(tmp_path):
    fp = _build_workbook(tmp_path, [{
        "D": "REQ-A", "F": "TC-A-1",
        "I": "the HU shall display the icon",
        "L": "1. Open menu.\n2. Observe whether icon appears.",
        "M": "1. Menu.\n2. Icon shown.",
        "P": "P1", "Q": "Functional",
    }])
    report = review_workbook(fp, dry_run=True)
    refs = [f["rule_ref"] for f in report["per_tc_findings"][0]["findings"]]
    assert "§8.3.1" in refs


# ---------------------------------------------------------------------------
# Dry run never calls the LLM
# ---------------------------------------------------------------------------


def test_dry_run_does_not_invoke_openai(tmp_path, monkeypatch):
    """If dry_run=True, _run_llm_pipeline must not be called and no OpenAI
    import should happen via review_engine."""
    called = {"flag": False}

    def _boom(*a, **kw):
        called["flag"] = True
        raise AssertionError("LLM pipeline must not run in dry-run")

    monkeypatch.setattr(review_engine, "_run_llm_pipeline", _boom)
    fp = _build_workbook(tmp_path, [{
        "D": "REQ-A", "F": "TC-A-1",
        "I": "the HU shall display the icon",
        "L": "1. Open menu.\n2. Confirm icon shown.",
        "M": "1. Menu.\n2. Icon shown.",
        "P": "P1", "Q": "Functional",
    }])
    review_workbook(fp, dry_run=True)
    assert called["flag"] is False


# ---------------------------------------------------------------------------
# Output schema invariants
# ---------------------------------------------------------------------------


def test_output_writes_json_and_markdown(tmp_path):
    fp = _build_workbook(tmp_path, [{
        "D": "REQ-A", "F": "TC-A-1",
        "I": "the HU shall display the icon",
        "L": "1. Open menu.\n2. Confirm icon shown.",
        "M": "1. Menu.\n2. Icon shown.",
        "P": "P1", "Q": "Functional",
    }])
    out = tmp_path / "out"
    review_workbook(fp, output_dir=str(out), dry_run=True)
    assert (out / "findings.json").is_file()
    assert (out / "findings_report.md").is_file()


def test_tier2_findings_have_evidence_req_spec(tmp_path):
    fp = _build_workbook(tmp_path, [{
        "D": "REQ-A", "F": "TC-A-1",
        "I": "the HU shall complete pairing",
        "L": "1. Trigger.\n2. 等待 5 秒.\n3. Confirm.",
        "M": "1. ok\n2. ok\n3. ok",
        "P": "P1", "Q": "Functional",
    }])
    report = review_workbook(fp, dry_run=True)
    for entry in report["per_tc_findings"]:
        for f in entry["findings"]:
            if f["tier"] == 2:
                assert "evidence_req_spec" in f and f["evidence_req_spec"]
            else:
                assert "evidence_req_spec" not in f
