"""Tests for prompt builder module (RULES.md §12)."""
import pytest

from prompt_builder import (
    build_batch_prompt,
    build_multi_tc_user_prompt,
    build_system_blocks,
    build_system_prompt,
    build_user_prompt,
)


@pytest.fixture
def sample_row():
    return {
        "req_id": "SWE1-HMI-DM-001-01",
        "test_item": "PDM01.1) The Device Manager can be added to the status bar.",
    }


@pytest.fixture
def sample_context():
    return {
        "project": "newR1L",
        "test_group": "DeviceManager",
        "test_set": "Access & Entry",
    }


@pytest.fixture
def sample_spec():
    return {
        "PDM01.1": {
            "source_id": "Device_Manager_HMI Logic_2.3",
            "full_text": "PDM01.1 allows adding Device Manager shortcut to status bar.",
        }
    }


@pytest.fixture
def rules_text():
    return "## Rules\n- One behavior per TC\n- Final step must verify"


class TestBuildSystemPrompt:
    def test_contains_role(self):
        prompt = build_system_prompt()
        assert "ASPICE" in prompt
        assert "SWE.6" in prompt

    def test_contains_json_instruction(self):
        prompt = build_system_prompt()
        assert "JSON" in prompt

    def test_system_blocks_allow_traditional_chinese_only_for_analysis_fields(self):
        prompt = build_system_blocks("RULES", batch=False)
        assert "All TC output fields that will be written back to the workbook MUST be in" in prompt
        assert "Analytical explanation fields such as `reasoning`, `meaning`" in prompt
        assert "may be written in Traditional Chinese" in prompt

    def test_batch_system_blocks_request_json_object_contract(self):
        prompt = build_system_blocks("RULES", batch=True)
        assert "Return ONLY valid JSON object(s), no markdown fences." in prompt


class TestBuildUserPrompt:
    def test_contains_req_id(self, sample_row, sample_context, sample_spec, rules_text):
        prompt = build_user_prompt(sample_row, sample_context, sample_spec, rules_text)
        assert "SWE1-HMI-DM-001-01" in prompt

    def test_contains_test_item(self, sample_row, sample_context, sample_spec, rules_text):
        prompt = build_user_prompt(sample_row, sample_context, sample_spec, rules_text)
        assert "PDM01.1" in prompt

    def test_contains_context(self, sample_row, sample_context, sample_spec, rules_text):
        prompt = build_user_prompt(sample_row, sample_context, sample_spec, rules_text)
        assert "newR1L" in prompt
        assert "DeviceManager" in prompt
        assert "Access & Entry" in prompt

    def test_contains_spec_context(self, sample_row, sample_context, sample_spec, rules_text):
        prompt = build_user_prompt(sample_row, sample_context, sample_spec, rules_text)
        assert "adding Device Manager shortcut" in prompt

    def test_contains_rules(self, sample_row, sample_context, sample_spec, rules_text):
        prompt = build_user_prompt(sample_row, sample_context, sample_spec, rules_text)
        assert "One behavior per TC" in prompt

    def test_contains_output_keys(self, sample_row, sample_context, sample_spec, rules_text):
        prompt = build_user_prompt(sample_row, sample_context, sample_spec, rules_text)
        assert "test_item_rewrite" in prompt
        assert "pre_conditions" in prompt
        assert "test_procedure" in prompt
        assert "expected_result" in prompt

    def test_no_spec_available(self, sample_row, sample_context, rules_text):
        prompt = build_user_prompt(sample_row, sample_context, {}, rules_text)
        assert "SWE1-HMI-DM-001-01" in prompt

    def test_spec_none(self, sample_row, sample_context, rules_text):
        prompt = build_user_prompt(sample_row, sample_context, None, rules_text)
        assert "SWE1-HMI-DM-001-01" in prompt


class TestBuildBatchPrompt:
    def test_contains_all_rows(self, sample_context, rules_text):
        rows = [
            {"req_id": "R001", "test_item": "PDM01 feature A"},
            {"req_id": "R002", "test_item": "PDM02 feature B"},
            {"req_id": "R003", "test_item": "PDM03 feature C"},
        ]
        prompt = build_batch_prompt(rows, sample_context, {}, rules_text)
        assert "R001" in prompt
        assert "R002" in prompt
        assert "R003" in prompt

    def test_requests_json_array(self, sample_context, rules_text):
        rows = [{"req_id": "R001", "test_item": "test"}]
        prompt = build_batch_prompt(rows, sample_context, {}, rules_text)
        assert 'Return a JSON object with key `tcs`' in prompt
        assert "array of TC objects" in prompt

    def test_includes_per_row_test_set(self, sample_context, rules_text):
        rows = [
            {"req_id": "R001", "test_item": "test A", "test_set": "Access & Entry"},
            {"req_id": "R002", "test_item": "test B", "test_set": "Device List"},
        ]
        prompt = build_batch_prompt(rows, sample_context, {}, rules_text)
        assert "- Test Set: Access & Entry" in prompt
        assert "- Test Set: Device List" in prompt


class TestBuildMultiTcPrompt:
    def test_analysis_fields_are_traditional_chinese_but_tc_fields_remain_english(self, sample_row, sample_context):
        prompt = build_multi_tc_user_prompt(sample_row, sample_context, {}, "")
        assert "`reasoning` (string, 繁體中文)" in prompt
        assert '"meaning": "<繁中>"' in prompt
        assert "All output fields English" in prompt

    def test_design_method_mentions_system_normalization(self, sample_row, sample_context):
        prompt = build_multi_tc_user_prompt(sample_row, sample_context, {}, "")
        assert "short English" in prompt
        assert "normalized by the system" in prompt or "normalize it to the canonical dropdown value" in prompt
