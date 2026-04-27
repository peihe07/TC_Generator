"""Tests for validator module (RULES.md §8)."""
import pytest

from validator import (
    validate_test_item,
    validate_pre_conditions,
    validate_test_procedure,
    validate_expected_result,
    validate_tc_id,
    validate_tc_ids_sequence,
    validate_design_method,
    validate_priority,
    validate_row,
    ValidationResult,
    normalize_design_method,
)


# --- §8.1 Test Item Format ---

class TestValidateTestItem:
    def test_valid(self):
        text = (
            "PDM01.1) The Device Manager can be added to the status bar.\n"
            "\n"
            "User adds DM to status bar → DM icon displayed"
        )
        r = validate_test_item(text)
        assert r.passed

    def test_missing_arrow(self):
        text = (
            "Original text.\n"
            "\n"
            "Some rewrite without arrow"
        )
        r = validate_test_item(text)
        assert not r.passed
        assert "→" in r.message

    def test_rewrite_without_parentheses_is_allowed(self):
        text = (
            "Original text.\n"
            "\n"
            "Condition → Outcome without parens"
        )
        r = validate_test_item(text)
        assert r.passed

    def test_missing_blank_line(self):
        text = (
            "Original text.\n"
            "Condition → Outcome"
        )
        r = validate_test_item(text)
        assert not r.passed
        assert "blank line" in r.message.lower()

    def test_original_only_no_rewrite(self):
        text = "PDM01 just original text, no rewrite."
        r = validate_test_item(text)
        assert not r.passed


# --- §8.2 Pre-Condition ---

class TestValidatePreConditions:
    def test_valid_numbered_list(self):
        r = validate_pre_conditions("1. Bluetooth enabled on HU\n2. Phone paired")
        assert r.passed

    def test_na(self):
        r = validate_pre_conditions("NA")
        assert r.passed

    def test_contains_action_verb(self):
        r = validate_pre_conditions("1. Insert USB cable into HU")
        assert not r.passed
        assert "action" in r.message.lower() or "insert" in r.message.lower()

    def test_tap_verb(self):
        r = validate_pre_conditions("1. Tap settings icon")
        assert not r.passed

    def test_obvious_state(self):
        r = validate_pre_conditions("1. HU is powered on")
        assert not r.passed
        assert "obvious" in r.message.lower() or "powered on" in r.message.lower()

    def test_not_numbered(self):
        r = validate_pre_conditions("Bluetooth enabled and phone ready")
        assert not r.passed


# --- §8.3 Test Procedure ---

class TestValidateTestProcedure:
    def test_valid(self):
        text = (
            "1. Open Settings to access Bluetooth menu.\n"
            "2. Tap Device Manager and check that the Device Manager screen is displayed."
        )
        r = validate_test_procedure(text)
        assert r.passed

    def test_single_step(self):
        text = "1. Check that the screen is displayed."
        r = validate_test_procedure(text)
        assert not r.passed
        assert "2" in r.message or "step" in r.message.lower()

    def test_final_step_no_verification(self):
        text = (
            "1. Open Settings to access menu.\n"
            "2. Select the Apple CarPlay icon."
        )
        r = validate_test_procedure(text)
        assert not r.passed
        assert "final" in r.message.lower() or "verif" in r.message.lower()

    def test_final_step_vague(self):
        text = (
            "1. Open Settings to access menu.\n"
            "2. Observe whether CarPlay launches."
        )
        r = validate_test_procedure(text)
        assert not r.passed

    def test_not_numbered(self):
        text = "Open settings and then verify."
        r = validate_test_procedure(text)
        assert not r.passed

    def test_verify_is_forbidden_in_final_step(self):
        text = (
            "1. Open Settings.\n"
            "2. Tap Device Manager and verify the Device Manager screen is displayed."
        )
        r = validate_test_procedure(text)
        assert not r.passed
        assert "forbidden" in r.message.lower()

    def test_final_step_must_check_test_item_outcome(self):
        text = (
            "1. Open Settings.\n"
            "2. Tap Device Manager and check that the toolbar is refreshed."
        )
        r = validate_test_procedure(text, "User opens Device Manager → Device Manager screen displayed")
        assert not r.passed
        assert "test item outcome" in r.message.lower()

    def test_non_final_step_cannot_own_main_outcome(self):
        text = (
            "1. Check that the Device Manager screen is displayed.\n"
            "2. Record the event log entry."
        )
        r = validate_test_procedure(text, "User opens Device Manager → Device Manager screen displayed")
        assert not r.passed
        assert "test item outcome" in r.message.lower() or "before the final step" in r.message.lower()


# --- §8.4 Expected Result ---

class TestValidateExpectedResult:
    def test_valid(self):
        r = validate_expected_result(
            "1. Settings screen displayed.\n2. DM icon shown in status bar.",
            step_count=2,
        )
        assert r.passed

    def test_count_mismatch(self):
        r = validate_expected_result(
            "1. Result A.\n2. Result B.\n3. Result C.",
            step_count=2,
        )
        assert not r.passed
        assert "mismatch" in r.message.lower() or "count" in r.message.lower()

    def test_vague_language_normal(self):
        r = validate_expected_result(
            "1. Setup done.\n2. Feature works normal.",
            step_count=2,
        )
        assert not r.passed

    def test_vague_language_as_expected(self):
        r = validate_expected_result(
            "1. OK.\n2. Display as expected.",
            step_count=2,
        )
        assert not r.passed

    def test_not_numbered(self):
        r = validate_expected_result("Everything is fine.", step_count=1)
        assert not r.passed


# --- §8.5 TC ID ---

class TestValidateTcId:
    def test_valid(self):
        r = validate_tc_id("newR1L-DMS-001")
        assert r.passed

    def test_invalid_format(self):
        r = validate_tc_id("bad-id")
        assert not r.passed

    def test_no_zero_pad(self):
        r = validate_tc_id("p-A-1")
        assert not r.passed


class TestValidateTcIdsSequence:
    def test_valid_sequence(self):
        ids = ["p-A-001", "p-A-002", "p-A-003"]
        r = validate_tc_ids_sequence(ids)
        assert r.passed

    def test_duplicate(self):
        ids = ["p-A-001", "p-A-001"]
        r = validate_tc_ids_sequence(ids)
        assert not r.passed
        assert "duplicate" in r.message.lower()

    def test_not_increasing(self):
        ids = ["p-A-003", "p-A-001"]
        r = validate_tc_ids_sequence(ids)
        assert not r.passed
        assert "monoton" in r.message.lower() or "increas" in r.message.lower()


# --- §8.6 Design Method ---

class TestValidateDesignMethod:
    def test_valid(self):
        r = validate_design_method("功能測試 (Functional based ; no specific technique)")
        assert r.passed

    def test_state_transition(self):
        r = validate_design_method("狀態轉換 (State Transition Testing)")
        assert r.passed

    def test_invalid(self):
        r = validate_design_method("random method")
        assert not r.passed

    def test_short_english_label_normalizes_to_canonical_string(self):
        assert normalize_design_method("Functional") == "功能測試 (Functional based ; no specific technique)"
        r = validate_design_method("Functional")
        assert r.passed
        assert "normalized to" in r.message


# --- §8.7 Priority ---

class TestValidatePriority:
    def test_p0(self):
        assert validate_priority("P0").passed

    def test_p1(self):
        assert validate_priority("P1").passed

    def test_p2(self):
        assert validate_priority("P2").passed

    def test_p3(self):
        assert validate_priority("P3").passed

    def test_na_rejected(self):
        assert not validate_priority("NA").passed

    def test_old_high_rejected(self):
        assert not validate_priority("High").passed

    def test_invalid(self):
        assert not validate_priority("Critical").passed

    def test_case_sensitive(self):
        assert not validate_priority("p0").passed


# --- Full row validation ---

class TestValidateRow:
    def test_all_pass(self):
        row = {
            "tc_id": "p-A-001",
            "test_item": "Original.\n\nOpen DM → DM visible",
            "pre_conditions": "1. BT enabled",
            "test_procedure": "1. Open settings to access BT.\n2. Check that the DM is visible in the list.",
            "expected_result": "1. BT settings shown.\n2. DM is visible in list.",
            "design_method": "功能測試 (Functional based ; no specific technique)",
            "priority": "P1",
        }
        results = validate_row(row)
        assert all(r.passed for r in results.values())

    def test_mixed_results(self):
        row = {
            "tc_id": "bad",
            "test_item": "Original.\n\nOpen DM → DM visible",
            "pre_conditions": "NA",
            "test_procedure": "1. Setup.\n2. Verify result is correct.",
            "expected_result": "1. OK.\n2. Works as expected.",
            "design_method": "功能測試 (Functional based ; no specific technique)",
            "priority": "P1",
        }
        results = validate_row(row)
        assert not results["tc_id"].passed
        assert not results["expected_result"].passed
        assert results["test_item"].passed
