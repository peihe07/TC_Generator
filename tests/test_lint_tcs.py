"""Tests for the Step 3 TC linter (tcgen_package/scripts/lint_tcs.py)."""
import json
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPTS = REPO / "tcgen_package" / "scripts"
DATA = REPO / "tcgen_package" / "data"
sys.path.insert(0, str(SCRIPTS))

import lint_tcs  # noqa: E402


# exemplars.json is a rebuildable artifact derived from the customer workbook and
# is therefore gitignored — a fresh clone has scripts and tests but no derived
# data until Step 1 has been run. Skip rather than fail in that state.
EXEMPLARS = DATA / "exemplars.json"
needs_exemplars = pytest.mark.skipif(
    not EXEMPLARS.exists(),
    reason="data/exemplars.json not built yet — run scripts/extract_exemplars.py (RUNBOOK Step 1)",
)


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

VALID_TC = {
    "req_id": "SWE1-MEDIA-PLA-063-01",
    "test_group": "MediaHMI",
    "test_set": "Source Selection",
    "test_item": "No BT device connected -> pairing popup shown",
    "pre_conditions": "1. No Bluetooth audio device is connected to the HU",
    "input_test_data": "NA",
    "test_procedure": (
        '1. Press "Media" on Main Menu Bar to open the Media screen\n'
        '2. Press "Bluetooth" in the Source Drawer and read the content displayed on the HU'
    ),
    "expected_result": (
        "1. The Media screen is displayed\n"
        "2. The pairing popup is displayed as defined by PU0998 String/Popup Message"
    ),
    "specification_reference": "Media_HMI_Logic_and_Flow_R1_SR24_Post_2A_(July_25th,_2023)_11.4.1",
    "priority": "P1",
    "design_method": "功能測試 (Functional based ; no specific technique)",
}

TEST_SETS = {"Source Selection", "Source Tab", "Browse Tab", "Presets"}


def lint(**overrides):
    """Lint a copy of VALID_TC with the given field overrides."""
    tc = {**VALID_TC, **overrides}
    return lint_tcs.lint_tc(tc, TEST_SETS)


def rules(findings):
    return {f.rule for f in findings}


# ---------------------------------------------------------------------------
# baseline
# ---------------------------------------------------------------------------

def test_valid_tc_produces_no_findings():
    assert lint() == []


def test_report_passed_flag_and_exit_semantics():
    report = lint_tcs.LintReport(total=1)
    assert report.passed is True
    report.findings.append(lint_tcs.Finding("X-01", "keys", "missing"))
    assert report.passed is False
    assert report.failed_req_ids == ["X-01"]


# ---------------------------------------------------------------------------
# required keys
# ---------------------------------------------------------------------------

def test_missing_key_is_flagged():
    tc = {k: v for k, v in VALID_TC.items() if k != "priority"}
    assert "keys" in rules(lint_tcs.lint_tc(tc, TEST_SETS))


def test_empty_key_is_flagged():
    assert "keys" in rules(lint(expected_result="   "))


def test_na_allowed_only_for_input_test_data():
    assert lint(input_test_data="NA") == []
    assert "keys" in rules(lint(pre_conditions="NA"))


def test_non_string_key_is_flagged():
    assert "keys" in rules(lint(priority=1))


# ---------------------------------------------------------------------------
# trailing periods
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("tail", [".", "。"])
def test_trailing_period_is_flagged(tail):
    findings = lint(pre_conditions=f"1. No Bluetooth audio device is connected{tail}")
    assert "trailing-period" in rules(findings)


def test_trailing_period_reports_the_offending_line_number():
    findings = lint(
        expected_result="1. The Media screen is displayed\n2. The popup is displayed."
    )
    msg = next(f.message for f in findings if f.rule == "trailing-period")
    assert "line 2" in msg


# ---------------------------------------------------------------------------
# UI label formatting
# ---------------------------------------------------------------------------

def test_square_bracket_label_is_flagged():
    assert "label-format" in rules(
        lint(test_procedure='1. Press [Media] on Main Menu Bar\n2. Read the HU screen')
    )


def test_angle_bracket_placeholder_is_flagged():
    assert "label-format" in rules(
        lint(test_procedure='1. Press <Media> on Main Menu Bar\n2. Read the HU screen')
    )


def test_single_quoted_label_is_flagged():
    assert "label-format" in rules(
        lint(test_procedure="1. Press 'Media' on Main Menu Bar\n2. Read the HU screen")
    )


def test_english_possessive_is_not_mistaken_for_a_label():
    findings = lint(
        expected_result=(
            "1. The device's name is displayed on the HU\n"
            "2. The pairing popup is displayed"
        )
    )
    assert "label-format" not in rules(findings)


# ---------------------------------------------------------------------------
# dropdown / whitelist fields
# ---------------------------------------------------------------------------

def test_invalid_priority_is_flagged():
    assert "priority" in rules(lint(priority="High"))


def test_design_method_requires_exact_dropdown_string():
    assert "design-method" in rules(lint(design_method="Functional based"))
    assert lint(design_method="狀態轉換 (State Transition Testing)") == []


def test_wrong_test_group_is_flagged():
    assert "test-group" in rules(lint(test_group="Media"))


def test_test_set_outside_whitelist_is_flagged():
    assert "test-set" in rules(lint(test_set="Invented Set"))


def test_test_set_check_is_skipped_when_whitelist_is_unavailable():
    tc = {**VALID_TC, "test_set": "Invented Set"}
    assert "test-set" not in rules(lint_tcs.lint_tc(tc, set()))


# ---------------------------------------------------------------------------
# step structure
# ---------------------------------------------------------------------------

def test_single_step_procedure_is_flagged():
    findings = lint(
        test_procedure='1. Press "Media" on Main Menu Bar',
        expected_result="1. The Media screen is displayed",
    )
    assert "step-count" in rules(findings)


def test_procedure_er_count_mismatch_is_flagged():
    findings = lint(expected_result="1. The Media screen is displayed")
    assert "step-er-1to1" in rules(findings)


def test_blank_line_phase_breaks_do_not_change_the_count():
    steps = '1. Press "Media" on Main Menu Bar\n\n2. Press "Bluetooth" in the Source Drawer'
    ers = "1. The Media screen is displayed\n\n2. The pairing popup is displayed"
    assert lint(test_procedure=steps, expected_result=ers) == []


def test_wrapped_continuation_line_is_folded_into_the_previous_step():
    assert lint_tcs.split_steps("1. Press the button\n   on the HU screen\n2. Read the value") == [
        "Press the button on the HU screen",
        "Read the value",
    ]


# ---------------------------------------------------------------------------
# forbidden verbs / modals
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "verb", ["Observe", "Verify", "Check whether", "Confirm whether", "Watch", "Monitor", "Inspect", "See if"]
)
def test_forbidden_main_verb_is_flagged(verb):
    findings = lint(
        test_procedure=f'1. Press "Media" on Main Menu Bar\n2. {verb} the pairing popup is displayed'
    )
    assert "forbidden-verb" in rules(findings)


def test_verify_in_a_purpose_clause_is_allowed():
    findings = lint(
        test_procedure=(
            '1. Press "Media" on Main Menu Bar to verify that the screen opens\n'
            "2. Read the content displayed on the HU"
        )
    )
    assert "forbidden-verb" not in rules(findings)


def test_preferred_check_that_verb_is_allowed():
    findings = lint(
        test_procedure=(
            '1. Press "Media" on Main Menu Bar\n'
            "2. Check that the pairing popup is displayed on the HU"
        )
    )
    assert "forbidden-verb" not in rules(findings)


def test_literal_br_tag_is_flagged():
    assert "br-tag" in rules(
        lint(pre_conditions="1. No Bluetooth audio device is connected<br>2. FM is the active source")
    )


@pytest.mark.parametrize("variant", ["<br>", "<br/>", "<br />", "<BR>"])
def test_all_br_tag_spellings_are_flagged(variant):
    assert "br-tag" in rules(lint(test_item=f"Some requirement{variant}(tag)"))


def test_baseline_in_a_recording_step_is_flagged():
    findings = lint(
        test_procedure=(
            '1. Press "Media" on Main Menu Bar\n'
            "2. Read the track name shown on the Media screen\n"
            "3. Read the track name again after 5 seconds"
        ),
        expected_result=(
            "1. The Media screen is displayed\n"
            "2. The track name is recorded as the baseline\n"
            "3. The track name differs from the value read in step 2"
        ),
    )
    assert "er-baseline" in rules(findings)


def test_baseline_in_the_final_comparison_step_is_allowed():
    findings = lint(
        expected_result=(
            "1. The Media screen is displayed\n"
            "2. The track name matches the value recorded as the baseline"
        )
    )
    assert "er-baseline" not in rules(findings)


def test_rd_single_quotes_in_test_item_are_allowed():
    """test_item quotes the RD sentence verbatim; RD source text uses '...' for strings."""
    findings = lint(
        test_item="The system shall display 'Connect a Bluetooth Audio Device' in the metadata area.\n\n(tag)"
    )
    assert "label-format" not in rules(findings)


@pytest.mark.parametrize("modal", ["shall", "will", "should", "would"])
def test_modal_verb_in_er_is_flagged(modal):
    findings = lint(
        expected_result=f"1. The Media screen is displayed\n2. The popup {modal} be displayed"
    )
    assert "er-modal" in rules(findings)


def test_modal_substring_is_not_flagged():
    findings = lint(
        expected_result=(
            "1. The Media screen is displayed\n"
            "2. The shallow copy indicator is displayed"
        )
    )
    assert "er-modal" not in rules(findings)


# ---------------------------------------------------------------------------
# payload shapes / whitelist loading
# ---------------------------------------------------------------------------

def test_extract_tcs_handles_all_three_payload_shapes():
    assert lint_tcs.extract_tcs([VALID_TC]) == [VALID_TC]
    assert lint_tcs.extract_tcs({"tcs": [VALID_TC]}) == [VALID_TC]
    assert lint_tcs.extract_tcs({"requirements": [{"tcs": [VALID_TC]}]}) == [VALID_TC]
    assert lint_tcs.extract_tcs({"unexpected": 1}) == []


@needs_exemplars
def test_whitelist_loads_chapters_overrides_and_done_region_from_real_data():
    whitelist = lint_tcs.load_test_set_whitelist(DATA)
    # the two new Sets ruled by Pei
    assert "Preset Management" in whitelist
    assert "Media Widget" in whitelist
    # PLA-062 override target must be present even though no chapter defaults to it
    assert "Source Tab" in whitelist
    # done-region Sets no remaining chapter maps to must stay valid
    assert {"General Anatomy", "Playing Tab", "Metadata", "Tuning Controls"} <= whitelist


def test_dynamic_label_inside_double_quotes_is_allowed():
    findings = lint(
        test_procedure=(
            '1. Press "Media" on Main Menu Bar\n'
            '2. Press "Playing: <source>" on the Tab Buttons'
        )
    )
    assert "label-format" not in rules(findings)


def test_whitelist_is_empty_when_mapping_file_is_absent(tmp_path):
    assert lint_tcs.load_test_set_whitelist(tmp_path) == set()


def test_blocked_parent_is_reported_not_failed(tmp_path):
    f = tmp_path / "blocked.json"
    f.write_text(json.dumps({
        "parent": "SWE1-MEDIA-COM-051",
        "blocked": {"reason": "PU0996 absent from the Pop Up List", "anomaly": "A-009"},
        "tcs": [],
    }), encoding="utf-8")
    report = lint_tcs.lint_paths([f], TEST_SETS)
    assert report.passed is True
    assert report.blocked == [("blocked.json", "A-009: PU0996 absent from the Pop Up List")]


@pytest.mark.parametrize("blocked", [
    {"reason": "no anomaly id given"},
    {"anomaly": "A-009"},
    {},
    "not a dict",
])
def test_blocked_without_both_reason_and_anomaly_still_fails(tmp_path, blocked):
    """A blocked parent needs a paper trail; a bare marker must not silence the gate."""
    f = tmp_path / "bad.json"
    f.write_text(json.dumps({"blocked": blocked, "tcs": []}), encoding="utf-8")
    report = lint_tcs.lint_paths([f], TEST_SETS)
    assert "empty" in rules(report.findings)
    assert report.blocked == []


def test_assumption_marker_is_reported_not_failed(tmp_path):
    f = tmp_path / "assumed.json"
    f.write_text(json.dumps({
        "parent": "SWE1-MEDIA-COM-059",
        "assumption": {"note": "BT1.1.2 wins over BT1.1.1 by specific-over-general",
                       "anomaly": "A-011"},
        "tcs": [VALID_TC],
    }), encoding="utf-8")
    report = lint_tcs.lint_paths([f], TEST_SETS)
    assert report.passed is True
    assert report.assumptions == [
        ("assumed.json", "A-011: BT1.1.2 wins over BT1.1.1 by specific-over-general")]


@pytest.mark.parametrize("assumption", [
    {"note": "no anomaly id given"},
    {"anomaly": "A-011"},
    {},
    "not a dict",
])
def test_assumption_without_both_note_and_anomaly_fails(tmp_path, assumption):
    """A bet on a pending ruling must stay machine-retrievable, so the marker is strict."""
    f = tmp_path / "bad.json"
    f.write_text(json.dumps({"assumption": assumption, "tcs": [VALID_TC]}), encoding="utf-8")
    report = lint_tcs.lint_paths([f], TEST_SETS)
    assert "assumption-marker" in rules(report.findings)
    assert report.assumptions == []


def test_lint_paths_reports_files_with_no_tcs(tmp_path):
    bad = tmp_path / "empty.json"
    bad.write_text(json.dumps({"unexpected": 1}), encoding="utf-8")
    report = lint_tcs.lint_paths([bad], TEST_SETS)
    assert "empty" in rules(report.findings)


# ---------------------------------------------------------------------------
# regression: the human-authored done region must survive its own gate
# ---------------------------------------------------------------------------

def _done_region_findings():
    exemplars = json.loads(EXEMPLARS.read_text(encoding="utf-8"))
    whitelist = lint_tcs.load_test_set_whitelist(DATA)
    findings = []
    for test_set, tcs in exemplars.items():
        for tc in tcs:
            findings.extend(lint_tcs.lint_tc(tc, whitelist, source=test_set))
    return findings


@needs_exemplars
def test_done_region_exemplars_pass_every_rule_except_the_known_deviation():
    """Rows 10-332 are the compliant reference region — the gate must not reject them.

    Sole exception: the done region writes `recorded as the baseline` in
    recording steps, which docs/ASPICE_SWE6_AI_Instruction.md §5.6 reserves for
    the final comparison ER. That is a pre-existing deviation in the
    human-authored rows, not a linter defect — see ANOMALIES.md A-005.
    """
    offenders = [f.format() for f in _done_region_findings() if f.rule != "er-baseline"]
    assert not offenders, "\n".join(offenders)


@needs_exemplars
def test_done_region_baseline_deviation_count_is_pinned():
    """Pin the known §5.6 deviations so the count cannot grow unnoticed."""
    baseline_findings = [f for f in _done_region_findings() if f.rule == "er-baseline"]
    assert len(baseline_findings) == 8, "\n".join(f.format() for f in baseline_findings)
