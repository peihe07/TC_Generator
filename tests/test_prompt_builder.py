"""Tests for prompt builder module (RULES.md §12)."""
import pytest

from prompt_builder import (
    build_batch_prompt,
    build_decompose_prompt,
    build_multi_tc_user_prompt,
    build_system_blocks,
    build_system_prompt,
    build_test_set_classification_prompt,
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

    def test_system_blocks_forbid_fabricated_numeric_values(self):
        """需求沒給的具體數值（20 筆、5 秒、1024 bytes）AI 不可自己編出來。"""
        prompt = build_system_blocks("RULES", batch=False)
        assert "NEVER fabricate specific numeric values" in prompt
        # 範例必須提到合法的 abstract 寫法，讓 AI 知道替代寫法
        assert "configured maximum" in prompt or "configured limit" in prompt
        # Self-check 也要有對應條目
        assert "No FABRICATED numeric values" in prompt

    def test_system_blocks_forbid_other_unstated_data_points(self):
        prompt = build_system_blocks("RULES", batch=False)
        assert "NEVER fabricate any other unstated data point either" in prompt
        assert "error code" in prompt
        assert "default states" in prompt
        assert "No FABRICATED unstated data" in prompt


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

    def test_reminds_model_not_to_invent_unstated_data(self, sample_row, sample_context, sample_spec, rules_text):
        prompt = build_user_prompt(sample_row, sample_context, sample_spec, rules_text)
        assert "Do NOT invent unstated values or data points" in prompt
        assert "<configured limit>" in prompt


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

    def test_multi_tc_prompt_forbids_inventing_unstated_data(self, sample_row, sample_context):
        prompt = build_multi_tc_user_prompt(sample_row, sample_context, {}, "")
        assert "Do NOT invent unstated values or data points" in prompt
        assert "configured/per spec" in prompt


class TestBuildDecomposePrompt:
    def test_decompose_prompt_preserves_unknowns_instead_of_guessing(self):
        prompt = build_decompose_prompt("REQ text", "")
        assert "Do NOT invent missing data while analyzing" in prompt
        assert "preserve that ambiguity explicitly instead of guessing" in prompt


class TestBuildTestSetClassificationPrompt:
    """Test Set labels 要用 functional capability 而非 sub-action。
    參考例子：Pairing / Reconnect / Disconnect 都應該 merge 成 Connection。"""

    def _reqs(self):
        return [
            {"req_id": "R1", "test_item": "Pair a new device via BT settings."},
            {"req_id": "R2", "test_item": "Auto-reconnect to last paired device on power-on."},
            {"req_id": "R3", "test_item": "Disconnect current BT device from menu."},
        ]

    def test_prompt_includes_capability_grouping_rule(self):
        prompt = build_test_set_classification_prompt(self._reqs())
        # 核心指令：by capability, not by sub-action
        assert "Group by capability, not by sub-action" in prompt
        # 明確舉例把 pairing / reconnect / disconnect 合成 Connection
        assert "Connection" in prompt
        assert "Pairing" in prompt or "pairing" in prompt

    def test_prompt_discourages_splitting_sub_actions(self):
        prompt = build_test_set_classification_prompt(self._reqs())
        assert "zoom out one level" in prompt
        # 跨行 wrap 時 "user-facing\ncapability" — 正規化空白再比對
        assert "user-facing capability" in " ".join(prompt.split())

    def test_prompt_defaults_to_broad_capability_when_unsure(self):
        prompt = build_test_set_classification_prompt(self._reqs())
        assert "default to the broader capability" in " ".join(prompt.split())

    def test_prompt_still_requires_full_assignment(self):
        reqs = self._reqs()
        prompt = build_test_set_classification_prompt(reqs)
        assert f"array length must equal the input count ({len(reqs)})" in prompt

    def test_test_group_context_tells_ai_not_to_repeat_feature_prefix(self):
        prompt = build_test_set_classification_prompt(self._reqs(), test_group="Bluetooth")
        assert 'Test Group **"Bluetooth"**' in prompt
        # 明確要求不要在 label 裡重複 feature 名
        assert "do NOT repeat it in the Test Set label" in prompt

    def test_no_test_group_leaves_context_block_empty(self):
        prompt = build_test_set_classification_prompt(self._reqs(), test_group=None)
        assert "Feature group context" not in prompt
        prompt_empty = build_test_set_classification_prompt(self._reqs(), test_group="")
        assert "Feature group context" not in prompt_empty
