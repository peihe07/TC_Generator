"""Generation bridge tests (deterministic; the LLM step is simulated)."""
import json

import pytest

from gen_bridge import (
    GEN_BUNDLE_SCHEMA,
    export_generation_bundle,
    assemble_generation,
    _spec_pc_for_req,
)


def _write_reqs(tmp_path):
    reqs = [
        {"id": "SWE1-PLA-006", "title": "USB Repeat",
         "desc": "Default Repeat All; toggle Repeat Song."},
        {"id": "SWE1-PLA-010", "title": "Shuffle",
         "desc": "Toggle Shuffle On/Off."},
    ]
    p = tmp_path / "reqs.json"
    p.write_text(json.dumps(reqs), encoding="utf-8")
    return str(p)


def _write_spec_cov(tmp_path):
    rows = [
        {"pc": "PC4", "text": "Repeat has 3 states: Off / Song / All.",
         "cited_by": ["SWE1-PLA-006"], "best_req": "SWE1-PLA-006", "req_covered": True},
        {"pc": "PC4.7", "text": "Repeat Off not presented if unsupported.",
         "cited_by": [], "best_req": "SWE1-PLA-006", "req_covered": False},  # SPEC-only
    ]
    p = tmp_path / "spec.json"
    p.write_text(json.dumps(rows), encoding="utf-8")
    return str(p)


def test_spec_pc_links_cited_and_content():
    rows = [
        {"pc": "PC4", "text": "x", "cited_by": ["R1"], "best_req": "R9", "req_covered": True},
        {"pc": "PC4.7", "text": "y", "cited_by": [], "best_req": "R1", "req_covered": False},
        {"pc": "PC9", "text": "z", "cited_by": [], "best_req": "R2", "req_covered": True},
    ]
    linked = _spec_pc_for_req("R1", rows)
    assert {p["pc"] for p in linked} == {"PC4", "PC4.7"}  # cited OR best match


def test_export_includes_spec_only_and_req_filter(tmp_path):
    bundle = export_generation_bundle(
        _write_reqs(tmp_path), spec_coverage_path=_write_spec_cov(tmp_path),
        req_ids=["SWE1-PLA-006"])
    assert bundle["schema"] == GEN_BUNDLE_SCHEMA
    assert len(bundle["requirements"]) == 1           # filtered
    req = bundle["requirements"][0]
    assert req["req_id"] == "SWE1-PLA-006"
    assert req["spec_only_count"] == 1                 # PC4.7 is SPEC-only
    assert "PC4.7" in req["context_prompt"]            # SPEC original fed into decompose
    assert "★SPEC-only" in req["context_prompt"]
    assert req["answer"] is None


def test_assemble_flattens_and_tags_spec_only(tmp_path):
    bundle = export_generation_bundle(
        _write_reqs(tmp_path), spec_coverage_path=_write_spec_cov(tmp_path),
        req_ids=["SWE1-PLA-006"])
    # Claude fills the answer in-session (simulated)
    bundle["requirements"][0]["answer"] = {
        "decomposition": {"reasoning": "...", "scenarios": [
            {"id": 1, "source": "requirement"},
            {"id": 2, "source": "spec-only"},  # the Repeat Off behaviour
        ]},
        "test_cases": [
            {"scenario_id": 1, "tc_title": "Repeat All loops", "priority": "P1"},
            {"scenario_id": 2, "tc_title": "Repeat Off hidden when unsupported", "priority": "P2"},
        ],
    }
    result = assemble_generation(bundle)
    assert result["stats"]["tcs_generated"] == 2
    assert result["stats"]["tcs_from_spec_only"] == 1
    ids = [tc["tc_id"] for tc in result["test_cases"]]
    assert ids == ["GEN-0001", "GEN-0002"]
    assert result["test_cases"][1]["source"] == "spec-only"


def test_system_prompt_carries_authoritative_rules(tmp_path):
    # gen_bridge must inject the team's existing rules (load_rules), not a
    # hand-rolled partial prompt — so writing rules / Design Method / Priority
    # all come from the single source of truth.
    bundle = export_generation_bundle(_write_reqs(tmp_path), req_ids=["SWE1-PLA-006"])
    sp = bundle["system_prompt"]
    assert "State Transition Testing" in sp   # from Design Method 判斷規則
    assert "Design Method" in sp
    # the per-req context defers field/method/priority rules to the system prompt
    assert "權威規則" in bundle["requirements"][0]["context_prompt"]


def _full_tc(sid, **over):
    base = {"scenario_id": sid, "tc_title": "T", "test_item": "the HU shall X",
            "test_procedure": "1. Do.\n2. Check that X.", "expected_result": "1. X.",
            "design_method": "狀態轉換 (State Transition Testing)", "priority": "P1"}
    base.update(over)
    return base


def test_assemble_flags_off_vocabulary_design_method(tmp_path):
    from gen_bridge import DESIGN_METHODS
    bundle = export_generation_bundle(_write_reqs(tmp_path), req_ids=["SWE1-PLA-006"])
    bundle["requirements"][0]["answer"] = {
        "decomposition": {"scenarios": [{"id": 1, "source": "requirement"},
                                        {"id": 2, "source": "requirement"}]},
        "test_cases": [
            _full_tc(1),
            _full_tc(2, design_method="場景測試 (Scenario)"),  # off-vocabulary
        ],
    }
    result = assemble_generation(bundle)
    by_id = {tc["tc_id"]: tc for tc in result["test_cases"]}
    assert by_id["GEN-0001"]["design_method_valid"] is True
    assert by_id["GEN-0002"]["design_method_valid"] is False
    assert "design_method:off-vocabulary" in by_id["GEN-0002"]["compliance_issues"]
    assert "狀態轉換 (State Transition Testing)" in DESIGN_METHODS


def test_assemble_flags_bad_priority_and_empty_fields(tmp_path):
    bundle = export_generation_bundle(_write_reqs(tmp_path), req_ids=["SWE1-PLA-006"])
    bundle["requirements"][0]["answer"] = {
        "decomposition": {"scenarios": [{"id": 1, "source": "requirement"},
                                        {"id": 2, "source": "requirement"}]},
        "test_cases": [
            _full_tc(1, priority="P5"),                 # bad priority
            _full_tc(2, expected_result=""),            # empty required field
        ],
    }
    result = assemble_generation(bundle)
    assert result["stats"]["tcs_noncompliant"] == 2
    by_id = {tc["tc_id"]: tc for tc in result["test_cases"]}
    assert "priority:not P0-P3" in by_id["GEN-0001"]["compliance_issues"]
    assert "expected_result:empty" in by_id["GEN-0002"]["compliance_issues"]


def test_assemble_rejects_bad_schema():
    with pytest.raises(ValueError):
        assemble_generation({"schema": "nope", "requirements": []})
