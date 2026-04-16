"""Tests for prompt builder module (RULES.md §12)."""
import pytest

from prompt_builder import build_system_prompt, build_user_prompt, build_batch_prompt


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
        assert "array" in prompt.lower() or "Array" in prompt
