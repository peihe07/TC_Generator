"""Tests for job state manager (Phase 10.5)."""
import json
import pytest

from job_manager import (
    create_job,
    save_job,
    load_job,
    update_row_status,
    edit_row,
    get_rows_by_status,
    get_exportable_rows,
    get_job_stats,
    VALID_STATUSES,
)


@pytest.fixture
def parsed_data():
    return {
        "project": "newR1L",
        "test_group": "DeviceManager",
        "row_count": 3,
        "rows": [
            {
                "row_num": 10,
                "req_id": "SWE1-HMI-DM-001-01",
                "test_item": "PDM01 original text",
                "test_procedure": "1. Old proc",
                "expected_result": "1. Old result",
                "tc_id": "",
                "test_group": "",
                "test_set": "",
                "pre_conditions": "",
                "input_test_data": "",
                "spec_reference": "",
                "priority": "",
                "design_method": "",
            },
            {
                "row_num": 11,
                "req_id": "SWE1-HMI-DM-002-01",
                "test_item": "PDM02 another text",
                "test_procedure": "",
                "expected_result": "",
                "tc_id": "",
                "test_group": "",
                "test_set": "",
                "pre_conditions": "",
                "input_test_data": "",
                "spec_reference": "",
                "priority": "",
                "design_method": "",
            },
            {
                "row_num": 12,
                "req_id": "SWE1-HMI-DM-003-01",
                "test_item": "PDM03 third text",
                "test_procedure": "",
                "expected_result": "",
                "tc_id": "",
                "test_group": "",
                "test_set": "",
                "pre_conditions": "",
                "input_test_data": "",
                "spec_reference": "",
                "priority": "",
                "design_method": "",
            },
        ],
    }


@pytest.fixture
def sample_generated():
    return {
        "test_item_rewrite": "(Condition → Outcome)",
        "pre_conditions": "1. BT enabled",
        "input_test_data": "Settings menu",
        "test_procedure": "1. Open settings to access BT.\n2. Check DM and verify it appears.",
        "expected_result": "1. BT settings shown.\n2. DM is visible.",
        "design_method": "功能測試 (Functional based ; no specific technique)",
        "priority": "Medium",
        "split_flag": False,
        "split_reason": "",
    }


@pytest.fixture
def job_with_generated(parsed_data, sample_generated):
    job = create_job(parsed_data, "dm_20260416")
    for row in job["rows"]:
        row["generated"] = {**sample_generated}
        row["tc_id"] = f"newR1L-DMR-{str(row['row_num'] - 9).zfill(3)}"
    return job


class TestCreateJob:
    def test_structure(self, parsed_data):
        job = create_job(parsed_data, "dm_20260416")
        assert job["job_id"] == "dm_20260416"
        assert job["project"] == "newR1L"
        assert job["test_group"] == "DeviceManager"
        assert len(job["rows"]) == 3

    def test_row_structure(self, parsed_data):
        job = create_job(parsed_data, "dm_20260416")
        row = job["rows"][0]
        assert row["row_num"] == 10
        assert row["req_id"] == "SWE1-HMI-DM-001-01"
        assert row["original"]["test_item"] == "PDM01 original text"
        assert row["generated"] is None
        assert row["edited"] is None
        assert row["review_status"] == "pending"
        assert row["validation"] == {"status": None, "issues": []}
        assert row["generation_history"] == []

    def test_initial_stats(self, parsed_data):
        job = create_job(parsed_data, "dm_20260416")
        stats = get_job_stats(job)
        assert stats["total"] == 3
        assert stats["pending"] == 3
        assert stats["accepted"] == 0


class TestSaveLoadJob:
    def test_round_trip(self, parsed_data, tmp_path):
        job = create_job(parsed_data, "test_job")
        filepath = str(tmp_path / "job.json")
        save_job(job, filepath)
        loaded = load_job(filepath)
        assert loaded["job_id"] == "test_job"
        assert len(loaded["rows"]) == 3

    def test_load_not_found(self):
        assert load_job("/nonexistent/job.json") is None


class TestUpdateRowStatus:
    def test_accept(self, job_with_generated):
        update_row_status(job_with_generated, row_num=10, status="accepted")
        row = job_with_generated["rows"][0]
        assert row["review_status"] == "accepted"

    def test_reject(self, job_with_generated):
        update_row_status(job_with_generated, row_num=11, status="rejected")
        row = job_with_generated["rows"][1]
        assert row["review_status"] == "rejected"

    def test_flag(self, job_with_generated):
        update_row_status(job_with_generated, row_num=12, status="flagged")
        assert job_with_generated["rows"][2]["review_status"] == "flagged"

    def test_invalid_status(self, job_with_generated):
        with pytest.raises(ValueError, match="Invalid status"):
            update_row_status(job_with_generated, row_num=10, status="unknown")

    def test_row_not_found(self, job_with_generated):
        with pytest.raises(ValueError, match="not found"):
            update_row_status(job_with_generated, row_num=999, status="accepted")


class TestEditRow:
    def test_stores_edits(self, job_with_generated):
        edits = {"test_procedure": "1. New step.\n2. Verify new thing."}
        edit_row(job_with_generated, row_num=10, edits=edits)
        row = job_with_generated["rows"][0]
        assert row["edited"]["test_procedure"] == "1. New step.\n2. Verify new thing."
        assert row["review_status"] == "edited"

    def test_merges_with_generated(self, job_with_generated):
        edits = {"pre_conditions": "1. WiFi connected"}
        edit_row(job_with_generated, row_num=10, edits=edits)
        row = job_with_generated["rows"][0]
        # Edited field is overridden
        assert row["edited"]["pre_conditions"] == "1. WiFi connected"
        # Non-edited fields come from generated
        assert row["edited"]["test_item_rewrite"] == "(Condition → Outcome)"

    def test_triggers_revalidation(self, job_with_generated):
        edits = {"expected_result": "1. Works as expected."}
        edit_row(job_with_generated, row_num=10, edits=edits)
        row = job_with_generated["rows"][0]
        # Should have validation issues (vague language)
        assert row["validation"]["status"] == "fail"
        assert len(row["validation"]["issues"]) > 0

    def test_valid_edit_passes_validation(self, job_with_generated):
        edits = {
            "test_procedure": "1. Open settings to access BT.\n2. Check DM and verify it is visible.",
            "expected_result": "1. BT settings screen displayed.\n2. DM icon shown in list.",
        }
        edit_row(job_with_generated, row_num=10, edits=edits)
        row = job_with_generated["rows"][0]
        assert row["validation"]["status"] == "pass"

    def test_multiple_edits_override(self, job_with_generated):
        edit_row(job_with_generated, row_num=10, edits={"priority": "High"})
        edit_row(job_with_generated, row_num=10, edits={"priority": "Low"})
        row = job_with_generated["rows"][0]
        assert row["edited"]["priority"] == "Low"


class TestGetRowsByStatus:
    def test_filter_pending(self, job_with_generated):
        rows = get_rows_by_status(job_with_generated, "pending")
        assert len(rows) == 3

    def test_filter_accepted(self, job_with_generated):
        update_row_status(job_with_generated, row_num=10, status="accepted")
        rows = get_rows_by_status(job_with_generated, "accepted")
        assert len(rows) == 1
        assert rows[0]["row_num"] == 10

    def test_filter_rejected(self, job_with_generated):
        update_row_status(job_with_generated, row_num=11, status="rejected")
        rows = get_rows_by_status(job_with_generated, "rejected")
        assert len(rows) == 1


class TestGetExportableRows:
    def test_only_accepted_and_edited(self, job_with_generated):
        update_row_status(job_with_generated, row_num=10, status="accepted")
        edit_row(job_with_generated, row_num=11, edits={"priority": "High"})
        update_row_status(job_with_generated, row_num=12, status="rejected")

        exportable = get_exportable_rows(job_with_generated)
        assert len(exportable) == 2
        row_nums = [r["row_num"] for r in exportable]
        assert 10 in row_nums
        assert 11 in row_nums
        assert 12 not in row_nums

    def test_accepted_uses_generated(self, job_with_generated):
        update_row_status(job_with_generated, row_num=10, status="accepted")
        exportable = get_exportable_rows(job_with_generated)
        assert exportable[0]["test_item_rewrite"] == "(Condition → Outcome)"

    def test_edited_uses_edited_content(self, job_with_generated):
        edit_row(job_with_generated, row_num=10, edits={"priority": "High"})
        exportable = get_exportable_rows(job_with_generated)
        assert exportable[0]["priority"] == "High"
        # Non-edited field still from generated
        assert exportable[0]["test_item_rewrite"] == "(Condition → Outcome)"

    def test_empty_when_none_accepted(self, job_with_generated):
        exportable = get_exportable_rows(job_with_generated)
        assert len(exportable) == 0


class TestGetJobStats:
    def test_mixed_statuses(self, job_with_generated):
        update_row_status(job_with_generated, row_num=10, status="accepted")
        update_row_status(job_with_generated, row_num=11, status="rejected")
        update_row_status(job_with_generated, row_num=12, status="flagged")

        stats = get_job_stats(job_with_generated)
        assert stats["total"] == 3
        assert stats["accepted"] == 1
        assert stats["rejected"] == 1
        assert stats["flagged"] == 1
        assert stats["pending"] == 0
        assert stats["edited"] == 0
