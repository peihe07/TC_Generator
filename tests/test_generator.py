"""Tests for generator module.

OpenAI calls are mocked to avoid actual API usage in tests.
"""
import json
from unittest.mock import MagicMock, patch

import pytest

from generator import (
    CLASSIFICATION_MODEL,
    DecomposeResult,
    GenerationError,
    GenerationResult,
    extract_decompose_rules,
    calculate_cost,
    decompose_requirement,
    generate_batch,
    generate_batch_multi,
    generate_quick_tc,
    generate_single_tc,
    generate_tcs_for_row,
    _openai_request_timeout_seconds,
    classify_test_sets,
    parse_batch_response,
    parse_multi_tc_batch_response,
    parse_multi_tc_response,
    parse_tc_response,
)
from providers import LLMResponse, LLMUsage


def _llm_response(text, *, prompt_tokens=0, completion_tokens=0, cached_tokens=0):
    """Build a normalized LLMResponse (what `_chat` now returns)."""
    return LLMResponse(
        text=text,
        usage=LLMUsage(
            input_tokens=prompt_tokens,
            output_tokens=completion_tokens,
            cached_input_tokens=cached_tokens,
        ),
        model="gpt-5",
    )


VALID_TC_JSON = {
    "tc_title": "(User adds DM to status bar → DM icon displayed)",
    "pre_conditions": "1. HU is in normal mode",
    "input_test_data": "Status bar customization menu",
    "test_procedure": "1. Open status bar settings to access customization.\n2. Add Device Manager and verify icon appears in status bar.",
    "expected_result": "1. Status bar customization screen is displayed.\n2. Device Manager icon is displayed in the status bar.",
    "design_method": "功能測試 (Functional based ; no specific technique)",
    "priority": "P1",
    "split_flag": False,
    "split_reason": "",
}


def make_chat_response(payload, *, prompt_tokens=0, completion_tokens=0, cached_tokens=0):
    return _llm_response(
        json.dumps(payload),
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        cached_tokens=cached_tokens,
    )


class TestParseTcResponse:
    def test_valid_json(self):
        result = parse_tc_response(json.dumps(VALID_TC_JSON))
        assert result["tc_title"] == VALID_TC_JSON["tc_title"]
        assert result["priority"] == "P1"

    def test_json_in_markdown_fence(self):
        raw = f"```json\n{json.dumps(VALID_TC_JSON)}\n```"
        result = parse_tc_response(raw)
        assert result["priority"] == "P1"

    def test_invalid_json(self):
        with pytest.raises(GenerationError, match="parse"):
            parse_tc_response("not json")

    def test_missing_required_key(self):
        incomplete = {"tc_title": "something"}
        with pytest.raises(GenerationError, match="missing"):
            parse_tc_response(json.dumps(incomplete))

    def test_short_design_method_is_normalized_to_canonical_value(self):
        payload = {**VALID_TC_JSON, "design_method": "Functional"}
        result = parse_tc_response(json.dumps(payload))
        assert result["design_method"] == "功能測試 (Functional based ; no specific technique)"


class TestClassifyTestSets:
    def test_accepts_camel_case_test_set_key(self):
        response = make_chat_response({
            "assignments": [
                {"id": "row-1", "testSet": "Connection"},
                {"id": "row-2", "testSet": "Media Metadata"},
            ],
        })

        with patch("generator._chat", return_value=response):
            result = classify_test_sets([
                {"id": "row-1", "req_id": "REQ-1", "test_item": "bluetooth connection"},
                {"id": "row-2", "req_id": "REQ-2", "test_item": "media artwork"},
            ])

        assert result.assignments == {
            "row-1": "Connection",
            "row-2": "Media Metadata",
        }

    def test_accepts_legacy_test_set_to_ids_mapping(self):
        response = make_chat_response({
            "Connection": ["row-1", "row-2"],
            "Device List": ["row-3"],
        })

        with patch("generator._chat", return_value=response):
            result = classify_test_sets([
                {"id": "row-1", "req_id": "REQ-1", "test_item": "pair device"},
                {"id": "row-2", "req_id": "REQ-2", "test_item": "disconnect device"},
                {"id": "row-3", "req_id": "REQ-3", "test_item": "show paired devices"},
            ])

        assert result.assignments == {
            "row-1": "Connection",
            "row-2": "Connection",
            "row-3": "Device List",
        }


class TestParseBatchResponse:
    def test_valid_array(self):
        batch = [VALID_TC_JSON, VALID_TC_JSON]
        results = parse_batch_response(json.dumps(batch))
        assert len(results) == 2

    def test_array_in_fence(self):
        batch = [VALID_TC_JSON]
        raw = f"```json\n{json.dumps(batch)}\n```"
        results = parse_batch_response(raw)
        assert len(results) == 1

    def test_not_array(self):
        with pytest.raises(GenerationError, match="array"):
            parse_batch_response(json.dumps(VALID_TC_JSON))

    def test_invalid_json(self):
        with pytest.raises(GenerationError):
            parse_batch_response("broken")

    def test_count_mismatch_raises(self):
        batch = [VALID_TC_JSON]
        with pytest.raises(GenerationError, match="count mismatch"):
            parse_batch_response(json.dumps(batch), expected_count=2)


class TestCalculateCost:
    def test_gpt41_cost(self):
        cost = calculate_cost(
            input_tokens=1000,
            output_tokens=500,
            model="gpt-4.1",
        )
        expected = (1000 / 1_000_000 * 2.0) + (500 / 1_000_000 * 8.0)
        assert abs(cost - expected) < 0.0001

    def test_gpt5mini_cost(self):
        cost = calculate_cost(
            input_tokens=1000,
            output_tokens=500,
            model="gpt-5-mini",
        )
        expected = (1000 / 1_000_000 * 0.25) + (500 / 1_000_000 * 2.00)
        assert abs(cost - expected) < 0.0001

    def test_zero_tokens(self):
        assert calculate_cost(0, 0, "gpt-4.1") == 0.0

    def test_cached_tokens_discount(self):
        cost = calculate_cost(
            input_tokens=1000,
            output_tokens=0,
            model="gpt-4.1",
            cache_read_tokens=400,
        )
        expected = ((600 / 1_000_000) * 2.0) + ((400 / 1_000_000) * 0.20)
        assert abs(cost - expected) < 0.0001


class TestGenerateSingleTc:
    # NB: OpenAI client creation / timeout / retry now live in OpenAIProvider;
    # those behaviours are covered in tests/test_providers.py.
    def test_openai_timeout_can_be_overridden_by_env(self):
        with patch.dict("os.environ", {"OPENAI_REQUEST_TIMEOUT_SECONDS": "240"}):
            assert _openai_request_timeout_seconds() == 240.0

    def test_openai_timeout_uses_default_for_invalid_env(self):
        from generator import _DEFAULT_OPENAI_REQUEST_TIMEOUT_SECONDS

        with patch.dict("os.environ", {"OPENAI_REQUEST_TIMEOUT_SECONDS": "nope"}):
            assert _openai_request_timeout_seconds() == _DEFAULT_OPENAI_REQUEST_TIMEOUT_SECONDS

    @patch("generator._chat")
    def test_success(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            VALID_TC_JSON,
            prompt_tokens=500,
            completion_tokens=300,
        )

        result = generate_single_tc(
            row={"req_id": "R001", "test_item": "PDM01 test"},
            context={"project": "p", "test_group": "G", "test_set": "S"},
            spec_index={},
            rules_text="rules",
            model="gpt-4.1",
        )
        assert isinstance(result, GenerationResult)
        assert result.tc_data["priority"] == "P1"
        assert result.input_tokens == 500
        assert result.output_tokens == 300

    @patch("generator._chat")
    def test_api_error_raises(self, mock_chat):
        mock_chat.side_effect = GenerationError("API call failed: API timeout")

        with pytest.raises(GenerationError, match="API"):
            generate_single_tc(
                row={"req_id": "R001", "test_item": "test"},
                context={"project": "p", "test_group": "G", "test_set": "S"},
                spec_index={},
                rules_text="rules",
            )


class TestGenerateBatch:
    @patch("generator._chat")
    def test_batch_success(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            {"tcs": [VALID_TC_JSON, VALID_TC_JSON]},
            prompt_tokens=1000,
            completion_tokens=800,
        )

        rows = [
            {"req_id": "R001", "test_item": "PDM01 test A"},
            {"req_id": "R002", "test_item": "PDM02 test B"},
        ]
        result = generate_batch(
            rows=rows,
            context={"project": "p", "test_group": "G", "test_set": "S"},
            spec_index={},
            rules_text="rules",
        )
        assert isinstance(result, GenerationResult)
        assert len(result.tc_data) == 2
        assert result.input_tokens == 1000


class TestGenerateQuickTc:
    @patch("generator._chat")
    def test_single_success(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            VALID_TC_JSON,
            prompt_tokens=400,
            completion_tokens=200,
        )

        result = generate_quick_tc(
            test_item="Button pressed → LED turns on",
            context=None,
            rules_text="rules",
        )
        assert isinstance(result, GenerationResult)
        assert result.tc_data["priority"] == "P1"
        assert result.input_tokens == 400
        assert result.output_tokens == 200

    @patch("generator._chat")
    def test_with_context_passes_context_to_prompt(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            VALID_TC_JSON,
            prompt_tokens=600,
            completion_tokens=300,
        )

        result = generate_quick_tc(
            test_item="Button pressed → LED turns on",
            context="System must be powered on",
            rules_text="rules",
        )
        assert "System must be powered on" in mock_chat.call_args.args[1]
        assert isinstance(result, GenerationResult)

    @patch("generator._chat")
    def test_api_error_raises(self, mock_chat):
        mock_chat.side_effect = GenerationError("API call failed: timeout")

        with pytest.raises(GenerationError, match="API"):
            generate_quick_tc(
                test_item="some test item",
                context=None,
                rules_text="rules",
            )


class TestExtractDecomposeRules:
    def test_keeps_only_split_relevant_sections(self):
        rules = """## 2. Core Principles
keep core
## 4. Workflow (Generate)
keep workflow
## 6. Field Rules
keep field rules
### 6.1 Test Item
keep split
### 6.2 Pre-Condition
keep precondition
## 7. Step Design
keep steps
## 8. Expected Results
keep expected
## 9. False Pass / False Fail
keep false
## 10. Requirement Alignment
keep alignment
### 10.2 Keyword Decomposition
keep keywords
## 11. Self-Check (before emitting each TC)
keep self check
## 12. Review Output
drop review
"""
        extracted = extract_decompose_rules(rules)
        assert "keep core" in extracted
        assert "keep workflow" in extracted
        assert "keep field rules" in extracted
        assert "keep split" in extracted
        assert "keep precondition" in extracted
        assert "keep steps" in extracted
        assert "keep expected" in extracted
        assert "keep false" in extracted
        assert "keep alignment" in extracted
        assert "keep keywords" in extracted
        assert "keep self check" in extracted
        assert "drop review" not in extracted

    @patch("generator._chat")
    def test_decompose_requirement_uses_focused_rules_subset(self, mock_chat):
        """Happy path：rules 含足夠多 expected headers 時用 focused subset。"""
        mock_chat.return_value = make_chat_response(
            {"reasoning": "ok", "scenarios": [{"id": 1, "name": "n", "description": "d", "test_item": "x"}]},
            prompt_tokens=100,
            completion_tokens=50,
        )
        rules = """## 2. Core Principles
keep core
## 4. Workflow (Generate)
keep workflow
## 6. Field Rules
keep field rules
### 6.1 Test Item
keep test item
### 6.2 Pre-Condition
keep precondition
## 7. Step Design
keep steps
## 8. Expected Results
keep expected
## 9. False Pass / False Fail
keep false
## 10. Requirement Alignment
keep alignment
### 10.2 Keyword Decomposition
keep keywords
## 11. Self-Check (before emitting each TC)
keep self check
## 12. Review Output
drop review
"""

        decompose_requirement(requirement="req", rules_text=rules)

        system_prompt = mock_chat.call_args.args[0]
        assert "keep core" in system_prompt
        assert "keep keywords" in system_prompt
        assert "keep precondition" in system_prompt
        assert "drop review" not in system_prompt

    @patch("generator._chat")
    def test_decompose_falls_back_to_full_rules_when_headers_dont_match(self, mock_chat):
        """若 rules doc 的 header 被 rename 到不認得（match ratio <50%），
        decompose 會 fallback 回完整 rules_text，避免偷偷丟掉 sections。"""
        mock_chat.return_value = make_chat_response(
            {"reasoning": "ok", "scenarios": [{"id": 1, "name": "n", "description": "d", "test_item": "x"}]},
            prompt_tokens=100,
            completion_tokens=50,
        )
        # 只有 1/7 header 認得 → trigger fallback
        rules = """## 2. Core Principles
keep core
## Renamed Section
should still pass through via fallback
## Another Unknown
also through via fallback
"""

        decompose_requirement(requirement="req", rules_text=rules)

        system_prompt = mock_chat.call_args.args[0]
        # Fallback：整份 rules 會被帶進來（包括原本該丟的 section）
        assert "keep core" in system_prompt
        assert "should still pass through via fallback" in system_prompt

    def test_real_aspice_doc_headers_still_match_whitelist(self):
        """Pin against the real ASPICE_SWE6_AI_Instruction.md so renaming a
        section shows up as a failing test instead of a silent token-waste
        fallback. Re-validates every entry in the hardcoded whitelist.
        """
        from pathlib import Path
        from generator import extract_decompose_rules

        doc_path = (
            Path(__file__).resolve().parent.parent
            / "docs" / "ASPICE_SWE6_AI_Instruction.md"
        )
        assert doc_path.is_file(), (
            f"Authoritative rules doc missing at {doc_path}; "
            "decompose prompt falls back to rules_loader.FALLBACK_RULES if this file is absent."
        )

        full_text = doc_path.read_text(encoding="utf-8")
        extracted = extract_decompose_rules(full_text)

        # Under-extraction guard would trigger → returns full text. Use that
        # as the failure signal: if the returned string equals the input, we
        # slipped into fallback, meaning a whitelisted header was renamed.
        assert extracted != full_text.strip(), (
            "extract_decompose_rules fell back to the full rules_text, which "
            "means <50% of the hardcoded headers matched. Either the ASPICE "
            "doc was restructured (update wanted_headers in generator.py) or "
            "the fallback threshold is wrong."
        )

        # Stronger pin: every whitelisted header must appear in the output.
        wanted_headers = {
            "## 2. Core Principles",
            "## 4. Workflow (Generate)",
            "## 6. Field Rules",
            "## 7. Step Design",
            "## 8. Expected Results",
            "## 9. False Pass / False Fail",
            "## 10. Requirement Alignment",
            "## 11. Self-Check (before emitting each TC)",
        }
        missing = [h for h in wanted_headers if h not in extracted]
        assert not missing, (
            f"Whitelisted headers missing from extracted rules: {missing}. "
            "Either the ASPICE doc renamed them or the whitelist drifted."
        )

    @patch("generator._chat")
    def test_invalid_json_response_raises(self, mock_chat):
        mock_chat.return_value = _llm_response(
            "not json at all", prompt_tokens=100, completion_tokens=50)

        with pytest.raises(GenerationError, match="parse"):
            generate_quick_tc(
                test_item="some test item",
                context=None,
                rules_text="rules",
            )


class TestDecomposeRequirement:
    VALID_DECOMPOSE_RESPONSE = {
        "reasoning": "The requirement has 3 distinct paths: normal, boundary, and error.",
        "keywords": [
            {"keyword": "button", "meaning": "The physical input trigger.", "scenarios": [1, 2]},
            {"keyword": "LED", "meaning": "The observable output indicator.", "scenarios": [1, 2]},
        ],
        "scenarios": [
            {"id": 1, "name": "Normal flow", "description": "Primary success path.", "test_item": "Button → LED on"},
            {"id": 2, "name": "Boundary", "description": "Edge case input.", "test_item": "Button held → LED blink"},
        ],
    }

    @patch("generator._chat")
    def test_success(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            self.VALID_DECOMPOSE_RESPONSE,
            prompt_tokens=700,
            completion_tokens=400,
        )

        result = decompose_requirement(
            requirement="When button is pressed, LED turns on. Boundary and error cases apply.",
            rules_text="rules",
        )
        assert isinstance(result, DecomposeResult)
        assert result.reasoning == self.VALID_DECOMPOSE_RESPONSE["reasoning"]
        assert len(result.scenarios) == 2
        assert result.scenarios[0]["name"] == "Normal flow"
        assert len(result.keywords) == 2
        assert result.keywords[0]["keyword"] == "button"
        assert result.input_tokens == 700
        assert result.output_tokens == 400

    @patch("generator._chat")
    def test_success_with_fenced_json(self, mock_chat):
        raw = f"```json\n{json.dumps(self.VALID_DECOMPOSE_RESPONSE)}\n```"
        mock_chat.return_value = _llm_response(
            raw, prompt_tokens=700, completion_tokens=400)

        result = decompose_requirement(requirement="req", rules_text="rules")
        assert len(result.scenarios) == 2

    @patch("generator._chat")
    def test_api_error_raises(self, mock_chat):
        mock_chat.side_effect = GenerationError("API call failed: network error")

        with pytest.raises(GenerationError, match="API"):
            decompose_requirement(requirement="req", rules_text="rules")

    @patch("generator._chat")
    def test_invalid_json_raises(self, mock_chat):
        mock_chat.return_value = _llm_response(
            "definitely not json", prompt_tokens=100, completion_tokens=50)

        with pytest.raises(GenerationError, match="parse"):
            decompose_requirement(requirement="req", rules_text="rules")

    @patch("generator._chat")
    def test_missing_scenarios_key_raises(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            {"reasoning": "ok"},
            prompt_tokens=100,
            completion_tokens=50,
        )

        with pytest.raises(GenerationError, match="scenarios"):
            decompose_requirement(requirement="req", rules_text="rules")

    @patch("generator._chat")
    def test_cost_calculation(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            self.VALID_DECOMPOSE_RESPONSE,
            prompt_tokens=1_000_000,
            completion_tokens=1_000_000,
        )

        result = decompose_requirement(requirement="req", rules_text="rules", model="gpt-4.1")
        assert abs(result.cost - 10.0) < 0.001


class TestParseMultiTcResponse:
    def test_wrapped_tcs_array_with_reasoning(self):
        payload = {
            "reasoning": "測試拆 2 筆的理由",
            "keywords": [{"keyword": "k1", "meaning": "m1", "covered_by": [1]}],
            "tcs": [VALID_TC_JSON, {**VALID_TC_JSON, "priority": "P0"}],
        }
        tcs, meta = parse_multi_tc_response(json.dumps(payload))
        assert len(tcs) == 2
        assert tcs[0]["priority"] == "P1"
        assert meta["reasoning"] == "測試拆 2 筆的理由"
        assert len(meta["keywords"]) == 1

    def test_plain_array_also_accepted(self):
        tcs, meta = parse_multi_tc_response(json.dumps([VALID_TC_JSON]))
        assert len(tcs) == 1
        assert meta["reasoning"] == ""

    def test_single_object_falls_back_to_list(self):
        tcs, _ = parse_multi_tc_response(json.dumps(VALID_TC_JSON))
        assert len(tcs) == 1

    def test_empty_array_raises(self):
        with pytest.raises(GenerationError, match="non-empty"):
            parse_multi_tc_response(json.dumps({"tcs": []}))

    def test_no_upper_cap_on_tc_count(self):
        many = {"tcs": [VALID_TC_JSON] * 10}
        tcs, _ = parse_multi_tc_response(json.dumps(many))
        assert len(tcs) == 10

    def test_missing_keys_raises(self):
        broken = {"tcs": [{"test_procedure": "only one field"}]}
        with pytest.raises(GenerationError, match="missing keys"):
            parse_multi_tc_response(json.dumps(broken))

    def test_distinguishing_axis_captured_when_present(self):
        # B 方案：sibling 存在時 AI 必須宣告差異軸；parser 要原封透傳。
        payload = {
            "reasoning": "拆 1 筆",
            "tcs": [VALID_TC_JSON],
            "duplicate_of": "",
            "distinguishing_axis": {
                "axis": "trigger_state",
                "delta": "本列觸發於 disable 狀態，sibling 為 enable 狀態",
            },
        }
        _, meta = parse_multi_tc_response(json.dumps(payload))
        assert meta["distinguishing_axis"]["axis"] == "trigger_state"
        assert "disable" in meta["distinguishing_axis"]["delta"]

    def test_distinguishing_axis_absent_returns_empty_dict(self):
        # 沒有 sibling 時 AI 應 omit；parser 要回 {} 而非 None。
        payload = {"reasoning": "原子", "tcs": [VALID_TC_JSON]}
        _, meta = parse_multi_tc_response(json.dumps(payload))
        assert meta["distinguishing_axis"] == {}

    def test_distinguishing_axis_malformed_normalized_to_empty(self):
        # AI 回了非 dict（例如直接寫字串），parser 不該爆，只回 {}。
        payload = {
            "reasoning": "x",
            "tcs": [VALID_TC_JSON],
            "distinguishing_axis": "trigger_state",
        }
        _, meta = parse_multi_tc_response(json.dumps(payload))
        assert meta["distinguishing_axis"] == {}

    def test_reconcile_drops_duplicate_when_axis_says_distinct(self):
        # AI 衝突：既說與 row 11 重複，又說 axis = trigger_state（其實不重複）。
        # Reconcile 信任 axis（描述更具體），清掉 duplicate_of。
        payload = {
            "reasoning": "x",
            "tcs": [VALID_TC_JSON],
            "duplicate_of": "11",
            "distinguishing_axis": {"axis": "trigger_state", "delta": "BT off vs on"},
        }
        _, meta = parse_multi_tc_response(json.dumps(payload))
        assert meta["duplicate_of"] == ""
        assert meta["distinguishing_axis"]["axis"] == "trigger_state"

    def test_reconcile_fills_axis_none_when_only_duplicate_set(self):
        # AI 只回 duplicate_of 沒回 axis → 補 axis = "none" 維持對等。
        payload = {
            "reasoning": "x",
            "tcs": [VALID_TC_JSON],
            "duplicate_of": "11",
        }
        _, meta = parse_multi_tc_response(json.dumps(payload))
        assert meta["duplicate_of"] == "11"
        assert meta["distinguishing_axis"] == {"axis": "none", "delta": ""}

    def test_reconcile_drops_axis_none_without_duplicate_target(self):
        # axis = "none" 但沒指出哪一個 sibling → 不可 actionable，整個清掉。
        payload = {
            "reasoning": "x",
            "tcs": [VALID_TC_JSON],
            "distinguishing_axis": {"axis": "none", "delta": ""},
        }
        _, meta = parse_multi_tc_response(json.dumps(payload))
        assert meta["duplicate_of"] == ""
        assert meta["distinguishing_axis"] == {}


class TestParseMultiTcBatchResponse:
    def test_per_req_arrays_with_reasoning(self):
        payload = {
            "requirements": [
                {
                    "req_id": "R1",
                    "reasoning": "R1 拆兩筆",
                    "tcs": [VALID_TC_JSON, VALID_TC_JSON],
                },
                {
                    "req_id": "R2",
                    "reasoning": "原子需求",
                    "tcs": [VALID_TC_JSON],
                },
            ]
        }
        tc_groups, meta_list = parse_multi_tc_batch_response(
            json.dumps(payload), expected_count=2,
        )
        assert len(tc_groups) == 2
        assert len(tc_groups[0]) == 2
        assert len(tc_groups[1]) == 1
        assert meta_list[0]["reasoning"] == "R1 拆兩筆"
        assert meta_list[1]["reasoning"] == "原子需求"

    def test_count_mismatch_raises(self):
        payload = {"requirements": [{"req_id": "R1", "tcs": [VALID_TC_JSON]}]}
        with pytest.raises(GenerationError, match="expected 2 requirement"):
            parse_multi_tc_batch_response(json.dumps(payload), expected_count=2)

    def test_batch_distinguishing_axis_per_entry(self):
        # B：batch 路徑也要 per-req 透傳 distinguishing_axis。
        payload = {
            "requirements": [
                {
                    "req_id": "R1",
                    "tcs": [VALID_TC_JSON],
                    "distinguishing_axis": {"axis": "input_data", "delta": "格式 A vs sibling 格式 B"},
                },
                {"req_id": "R2", "tcs": [VALID_TC_JSON]},
            ]
        }
        _, meta_list = parse_multi_tc_batch_response(json.dumps(payload), expected_count=2)
        assert meta_list[0]["distinguishing_axis"]["axis"] == "input_data"
        assert meta_list[1]["distinguishing_axis"] == {}


class TestGenerateTcsForRow:
    @patch("generator._chat")
    def test_returns_list_of_tcs_with_meta(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            {
                "reasoning": "§1.4 拆 2 筆",
                "tcs": [VALID_TC_JSON, {**VALID_TC_JSON, "priority": "P0"}],
            },
            prompt_tokens=100, completion_tokens=50,
        )
        result = generate_tcs_for_row(
            row={"req_id": "R1", "test_item": "trigger X"},
            context={"project": "p", "test_group": "g"},
            spec_index=None,
            rules_text="rules",
        )
        assert len(result.tc_data) == 2
        assert result.split_meta[0]["reasoning"] == "§1.4 拆 2 筆"
        assert result.split_meta[0]["req_id"] == "R1"


class TestGenerateBatchMulti:
    @patch("generator._chat")
    def test_returns_groups_with_meta_aligned(self, mock_chat):
        mock_chat.return_value = make_chat_response(
            {
                "requirements": [
                    {"req_id": "R1", "reasoning": "A", "tcs": [VALID_TC_JSON]},
                    {"req_id": "R2", "reasoning": "B", "tcs": [VALID_TC_JSON, VALID_TC_JSON]},
                ]
            },
            prompt_tokens=200, completion_tokens=100,
        )
        result = generate_batch_multi(
            rows=[
                {"req_id": "R1", "test_item": "x"},
                {"req_id": "R2", "test_item": "y"},
            ],
            context={"project": "p", "test_group": "g"},
            spec_index=None,
            rules_text="rules",
        )
        assert len(result.tc_data) == 2
        assert len(result.tc_data[0]) == 1
        assert len(result.tc_data[1]) == 2
        assert [m["reasoning"] for m in result.split_meta] == ["A", "B"]

    @patch("generator._chat")
    def test_empty_batch_group_falls_back_to_single_row_generation(self, mock_chat):
        mock_chat.side_effect = [
            make_chat_response(
                {
                    "requirements": [
                        {"req_id": "R1", "reasoning": "A", "tcs": [VALID_TC_JSON]},
                        {"req_id": "R2", "reasoning": "B", "tcs": []},
                    ]
                },
                prompt_tokens=200,
                completion_tokens=100,
            ),
            make_chat_response(
                {
                    "reasoning": "Fallback regenerated R2",
                    "tcs": [{**VALID_TC_JSON, "priority": "P0"}],
                },
                prompt_tokens=20,
                completion_tokens=10,
            ),
        ]

        result = generate_batch_multi(
            rows=[
                {"req_id": "R1", "test_item": "x"},
                {"req_id": "R2", "test_item": "y"},
            ],
            context={"project": "p", "test_group": "g"},
            spec_index=None,
            rules_text="rules",
        )

        assert mock_chat.call_count == 2
        assert len(result.tc_data) == 2
        assert len(result.tc_data[0]) == 1
        assert len(result.tc_data[1]) == 1
        assert result.tc_data[1][0]["priority"] == "P0"
        assert result.split_meta[1]["reasoning"] == "Fallback regenerated R2"
        assert result.split_meta[1]["req_id"] == "R2"

    @patch("generator._chat")
    def test_group_count_mismatch_falls_back_to_per_row_generation(self, mock_chat):
        """模型把多個 req 合併/漏掉導致群組數量不符時，整批改逐筆生成而非整批失敗。"""
        # 第 1 次批次：3 個 req 只回 2 個 group → 無法對齊。
        # 之後 3 次：逐筆 fallback 各回 1 筆 TC。
        mock_chat.side_effect = [
            make_chat_response(
                {
                    "requirements": [
                        {"req_id": "R1", "reasoning": "merged", "tcs": [VALID_TC_JSON]},
                        {"req_id": "R3", "reasoning": "merged", "tcs": [VALID_TC_JSON]},
                    ]
                },
                prompt_tokens=300,
                completion_tokens=150,
            ),
            make_chat_response(
                {"reasoning": "per-row R1", "tcs": [{**VALID_TC_JSON, "priority": "P0"}]},
                prompt_tokens=10, completion_tokens=5,
            ),
            make_chat_response(
                {"reasoning": "per-row R2", "tcs": [{**VALID_TC_JSON, "priority": "P1"}]},
                prompt_tokens=10, completion_tokens=5,
            ),
            make_chat_response(
                {"reasoning": "per-row R3", "tcs": [{**VALID_TC_JSON, "priority": "P2"}]},
                prompt_tokens=10, completion_tokens=5,
            ),
        ]

        result = generate_batch_multi(
            rows=[
                {"req_id": "R1", "test_item": "x"},
                {"req_id": "R2", "test_item": "y"},
                {"req_id": "R3", "test_item": "z"},
            ],
            context={"project": "p", "test_group": "g"},
            spec_index=None,
            rules_text="rules",
        )

        # 1 次失敗批次 + 3 次逐筆
        assert mock_chat.call_count == 4
        # 每個 row 都有獨立產出（不再整批失敗）
        assert len(result.tc_data) == 3
        assert [g[0]["priority"] for g in result.tc_data] == ["P0", "P1", "P2"]
        assert [m["req_id"] for m in result.split_meta] == ["R1", "R2", "R3"]
        # 失敗批次已耗用的 token 仍被計入（300+150 + 3*(10+5)）
        assert result.input_tokens == 330
        assert result.output_tokens == 165


class TestStage3DecomposeDomain:
    def test_build_decompose_prompt_injects_domain_block(self):
        from prompt_builder import build_decompose_prompt
        p = build_decompose_prompt("the HU shall toggle Repeat", rules_text="",
                                   domain_block="# Domain Pack\nRepeat: All/One Track only")
        assert "Domain Pack" in p and "All/One Track only" in p
        # Without a domain block the section is absent.
        assert "Domain Pack" not in build_decompose_prompt("x", rules_text="")

    @patch("generator._chat")
    def test_decompose_requirement_passes_domain_block(self, mock_chat):
        captured = {}

        def _cap(system, user, model, max_tokens=None, json_mode=True):
            captured["user"] = user
            return make_chat_response({
                "keywords": [], "reasoning": "r",
                "scenarios": [{"name": "s1"}, {"name": "s2"}],
            })

        mock_chat.side_effect = _cap
        decompose_requirement("the HU shall toggle Repeat", rules_text="",
                              domain_block="# Domain Pack\nRepeat: All/One Track only")
        assert "Domain Pack" in captured["user"]

    def test_build_decompose_meta_counts_scenarios(self):
        from generator import build_decompose_meta, DecomposeResult
        results = {
            "REQ-A": DecomposeResult(reasoning="", scenarios=[{}, {}, {}]),
            "REQ-B": DecomposeResult(reasoning="", scenarios=[{}]),
        }
        assert build_decompose_meta(results) == {"REQ-A": 3, "REQ-B": 1}
