"""FW036 project-profile wiring tests.

Covers: rules_loader profile overlay, remarks output key tolerance,
split_mode addendum, fixed Test Set vocabulary mode, and domain pack
injection — the five wiring points in docs/profiles/PROFILE_INTEGRATION.md.
"""
import json
import sys
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parent.parent / "backend"
REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND))

import generator  # noqa: E402
import prompt_builder  # noqa: E402
import rules_loader  # noqa: E402
from validator import normalize_design_method, validate_design_method  # noqa: E402


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

FW036_PROFILE = REPO / "docs" / "profiles" / "FW036_R1L_BT_Profile.md"
BT_PACK = REPO / "config" / "domain_packs" / "R1L_BT.json"

MINIMAL_TC = {
    "tc_title": "BT off, press Connect → error toast shown",
    "pre_conditions": "1. HU is powered on and in FULL OPERATION MODE",
    "input_test_data": "N/A",
    "test_procedure": "1. Press \"Connect\"",
    "expected_result": "1. Error toast is displayed",
    "design_method": "功能測試 (Functional based ; no specific technique)",
    "priority": "P1",
    "split_flag": False,
    "split_reason": "",
}


def _clear_env(monkeypatch):
    for var in ("TC_PROJECT_PROFILE", "TC_SPLIT_MODE",
                "TC_DOMAIN_PACK", "TC_FIXED_TEST_SETS"):
        monkeypatch.delenv(var, raising=False)


# ---------------------------------------------------------------------------
# 1. rules_loader — profile appended last
# ---------------------------------------------------------------------------

class TestProfileLoading:
    def test_profile_appended_after_generic_rules(self, tmp_path, monkeypatch):
        _clear_env(monkeypatch)
        generic = tmp_path / "generic.md"
        generic.write_text("GENERIC RULES", encoding="utf-8")
        profiles = tmp_path / "profiles"
        profiles.mkdir()
        (profiles / "MyProfile.md").write_text("PROFILE OVERRIDES", encoding="utf-8")
        monkeypatch.setattr(rules_loader, "PROFILES_DIR", profiles)

        text = rules_loader.load_rules(rule_files=[generic], profile="MyProfile")
        assert "GENERIC RULES" in text
        assert "PROFILE OVERRIDES" in text
        assert text.index("GENERIC RULES") < text.index("PROFILE OVERRIDES")

    def test_env_var_selects_profile(self, tmp_path, monkeypatch):
        _clear_env(monkeypatch)
        generic = tmp_path / "generic.md"
        generic.write_text("GENERIC RULES", encoding="utf-8")
        profiles = tmp_path / "profiles"
        profiles.mkdir()
        (profiles / "EnvProfile.md").write_text("ENV PROFILE BODY", encoding="utf-8")
        monkeypatch.setattr(rules_loader, "PROFILES_DIR", profiles)
        monkeypatch.setenv("TC_PROJECT_PROFILE", "EnvProfile")

        text = rules_loader.load_rules(rule_files=[generic])
        assert "ENV PROFILE BODY" in text

    def test_no_profile_keeps_legacy_behavior(self, tmp_path, monkeypatch):
        _clear_env(monkeypatch)
        generic = tmp_path / "generic.md"
        generic.write_text("GENERIC RULES", encoding="utf-8")
        text = rules_loader.load_rules(rule_files=[generic])
        assert text == "# generic\n\nGENERIC RULES"

    def test_fw036_profile_file_loads_with_key_overrides(self, monkeypatch):
        _clear_env(monkeypatch)
        monkeypatch.setattr(rules_loader, "PROFILES_DIR", FW036_PROFILE.parent)
        text = rules_loader.load_rules(
            rule_files=[], profile=FW036_PROFILE.stem,
            fallback="",
        )
        assert "HU is powered on and in FULL OPERATION MODE" in text
        assert "功能測試 (Functional based ; no specific technique)" in text
        assert "基礎故障注入 (Fault Injection Lite)" in text
        assert "CFTS085-XXXXXXX" in text
        assert "svc bluetooth disable" in text
        assert "IVI Integration" in text


# ---------------------------------------------------------------------------
# 2. remarks — listed in contract, tolerated when absent
# ---------------------------------------------------------------------------

class TestRemarksKey:
    def test_remarks_in_output_contract(self):
        assert "remarks" in prompt_builder.REQUIRED_OUTPUT_KEYS
        assert "remarks" in prompt_builder.OPTIONAL_OUTPUT_KEYS

    def test_parse_tc_response_without_remarks(self):
        parsed = generator.parse_tc_response(json.dumps(MINIMAL_TC))
        assert parsed["remarks"] == ""

    def test_parse_tc_response_preserves_remarks(self):
        tc = dict(MINIMAL_TC, remarks="Source: CFTS021 (OCR of scanned JPEG)")
        parsed = generator.parse_tc_response(json.dumps(tc))
        assert parsed["remarks"].startswith("Source: CFTS021")

    def test_parse_multi_tc_response_without_remarks(self):
        payload = {"reasoning": "單一原子行為", "keywords": [], "tcs": [MINIMAL_TC]}
        tcs, meta = generator.parse_multi_tc_response(json.dumps(payload))
        assert len(tcs) == 1
        assert tcs[0]["remarks"] == ""

    def test_missing_required_key_still_fails(self):
        broken = {k: v for k, v in MINIMAL_TC.items() if k != "tc_title"}
        with pytest.raises(generator.GenerationError):
            generator.parse_tc_response(json.dumps(broken))


# ---------------------------------------------------------------------------
# 3. split_mode — max granularity addendum
# ---------------------------------------------------------------------------

ROW = {"req_id": "SWE1_BT_151", "test_item": "When A2DP connected ..."}
CTX = {"project": "R1L", "test_group": "Bluetooth", "test_set": "Media (A2DP)"}


class TestSplitMode:
    def test_standard_mode_has_no_addendum(self, monkeypatch):
        _clear_env(monkeypatch)
        prompt = prompt_builder.build_multi_tc_user_prompt(ROW, CTX, None, "")
        assert "MAX GRANULARITY" not in prompt

    def test_max_granularity_param(self, monkeypatch):
        _clear_env(monkeypatch)
        prompt = prompt_builder.build_multi_tc_user_prompt(
            ROW, CTX, None, "", split_mode="max_granularity")
        assert "MAX GRANULARITY" in prompt
        assert "极致拆" in prompt
        assert "AVRCP control→command→display" in prompt  # triad exception kept

    def test_max_granularity_env(self, monkeypatch):
        _clear_env(monkeypatch)
        monkeypatch.setenv("TC_SPLIT_MODE", "max_granularity")
        prompt = prompt_builder.build_multi_tc_batch_prompt([ROW], CTX, None, "")
        assert "MAX GRANULARITY" in prompt

    def test_unknown_mode_falls_back_to_standard(self, monkeypatch):
        _clear_env(monkeypatch)
        monkeypatch.setenv("TC_SPLIT_MODE", "whatever")
        prompt = prompt_builder.build_multi_tc_user_prompt(ROW, CTX, None, "")
        assert "MAX GRANULARITY" not in prompt


# ---------------------------------------------------------------------------
# 4. fixed Test Set vocabulary
# ---------------------------------------------------------------------------

FW036_TEST_SETS = [
    "Adapter & Device", "Connection", "Pairing", "Phonebook (PBAP)",
    "Phone (HFP)", "Media (A2DP)", "Data Control", "IVI Integration",
]
REQS = [{"id": "u1", "req_id": "SWE1_BT_151", "test_item": "HFP call ..."}]


class TestFixedTestSets:
    def test_closed_list_mode_via_param(self, monkeypatch):
        _clear_env(monkeypatch)
        prompt = prompt_builder.build_test_set_classification_prompt(
            REQS, test_group="Bluetooth", fixed_test_sets=FW036_TEST_SETS)
        for label in FW036_TEST_SETS:
            assert f"- {label}" in prompt
        assert "character-for-character" in prompt
        # free-form derivation wording must be gone
        assert "Derive labels" not in prompt
        assert "do NOT invent a\n  fixed taxonomy" not in prompt

    def test_closed_list_mode_via_env(self, monkeypatch):
        _clear_env(monkeypatch)
        monkeypatch.setenv("TC_FIXED_TEST_SETS", "|".join(FW036_TEST_SETS))
        prompt = prompt_builder.build_test_set_classification_prompt(REQS)
        assert "- Phonebook (PBAP)" in prompt
        assert "closed list" in prompt

    def test_default_stays_free_form(self, monkeypatch):
        _clear_env(monkeypatch)
        prompt = prompt_builder.build_test_set_classification_prompt(
            REQS, test_group="Bluetooth")
        assert "Group the following requirements" in prompt
        assert "closed list" not in prompt


# ---------------------------------------------------------------------------
# 5. domain pack injection
# ---------------------------------------------------------------------------

class TestDomainPack:
    def test_bt_pack_loads_and_renders(self):
        from domain_pack import load_domain_pack, to_prompt_block, validate
        pack = load_domain_pack(str(BT_PACK))
        warnings = validate(pack)
        # only Gate-1 human-signoff warnings are acceptable
        assert all("open_question" in w or "reviewed_at" in w for w in warnings)
        block = to_prompt_block(pack)
        assert "STATUS_TELEMATIC.CurrentSource = 23" in block
        assert "getHfpDevice()" in block

    def test_env_pack_injected_into_multi_tc_prompt(self, monkeypatch):
        _clear_env(monkeypatch)
        monkeypatch.setenv("TC_DOMAIN_PACK", str(BT_PACK))
        prompt_builder._DOMAIN_BLOCK_CACHE.clear()
        prompt = prompt_builder.build_multi_tc_user_prompt(ROW, CTX, None, "")
        assert "Domain Pack (GROUND TRUTH" in prompt
        assert "HFM_BlueTooth_1_Selected" in prompt

    def test_param_beats_env(self, monkeypatch):
        _clear_env(monkeypatch)
        prompt = prompt_builder.build_multi_tc_user_prompt(
            ROW, CTX, None, "", domain_block="PARAM BLOCK CONTENT")
        assert "PARAM BLOCK CONTENT" in prompt

    def test_no_pack_no_section(self, monkeypatch):
        _clear_env(monkeypatch)
        prompt = prompt_builder.build_multi_tc_user_prompt(ROW, CTX, None, "")
        assert "Domain Pack (GROUND TRUTH" not in prompt


# ---------------------------------------------------------------------------
# 6. regression — FW036 design_method strings already on the dropdown
# ---------------------------------------------------------------------------

class TestDesignMethodVocab:
    @pytest.mark.parametrize("value", [
        "功能測試 (Functional based ; no specific technique)",
        "基礎故障注入 (Fault Injection Lite)",
    ])
    def test_fw036_strings_pass_verbatim(self, value):
        assert normalize_design_method(value) == value
        assert validate_design_method(value).passed
