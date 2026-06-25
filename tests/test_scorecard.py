"""Stage 7 — KPI Scorecard tests (synthetic data; no AI)."""
import json

import pytest

from scorecard import (
    KPI,
    Scorecard,
    compute_scorecard,
    to_dict,
    write_scorecard,
)


def _findings(total_tcs, total_reqs, per_tc):
    """Build a minimal §9-shaped findings dict."""
    return {
        "batch_meta": {
            "source_file": "synthetic.xlsx",
            "total_tcs": total_tcs,
            "total_req_groups": total_reqs,
        },
        "per_req_findings": [],
        "per_tc_findings": per_tc,
        "batch_summary": {},
    }


def _tc(tc_id, *severities, rule_refs=None):
    """One per-TC entry whose findings carry the given severities / rule_refs."""
    rule_refs = rule_refs or []
    findings = [{"severity": s, "rule_ref": None} for s in severities]
    findings += [{"severity": "Major", "rule_ref": r} for r in rule_refs]
    return {"tc_id": tc_id, "findings": findings}


def test_first_pass_rate():
    # 4 TCs: 1 Critical, 1 Major, 1 Minor, 1 Info -> 2 blocked (Critical/Major).
    findings = _findings(4, 1, [
        _tc("T1", "Critical"),
        _tc("T2", "Major"),
        _tc("T3", "Minor"),
        _tc("T4", "Info"),
    ])
    sc = compute_scorecard(findings)
    k = sc.kpis["first_pass_rate"]
    assert k.numerator == 2 and k.denominator == 4
    assert k.value == pytest.approx(0.5)
    # Minor / Info must NOT count as blocking.
    assert k.passed is False  # 0.5 < 0.80


def test_requirement_coverage():
    # 3 planned requirements; only R1, R2 have a TC -> 2/3.
    findings = _findings(2, 3, [_tc("T1"), _tc("T2")])
    traceability = {
        "per_tc": {
            "T1": {"matched": True, "req_id": "R1"},
            "T2": {"matched": True, "req_id": "R2"},
        },
        "all_requirements": ["R1", "R2", "R3"],
    }
    sc = compute_scorecard(findings, traceability=traceability)
    k = sc.kpis["requirement_coverage"]
    assert k.numerator == 2 and k.denominator == 3
    assert k.value == pytest.approx(2 / 3)


def test_traceability_ratio():
    findings = _findings(4, 2, [])
    traceability = {
        "per_tc": {
            "T1": {"matched": True, "req_id": "R1"},
            "T2": {"matched": True, "req_id": "R1"},
            "T3": {"matched": False, "req_id": "R2"},
            "T4": {"matched": True, "req_id": "R2"},
        }
    }
    sc = compute_scorecard(findings, traceability=traceability)
    k = sc.kpis["traceability_completeness"]
    assert k.numerator == 3 and k.denominator == 4
    assert k.value == pytest.approx(0.75)


def test_missing_decompose_meta_degrades():
    findings = _findings(2, 1, [_tc("T1"), _tc("T2")])
    sc = compute_scorecard(findings, decompose_meta=None)
    depth = sc.kpis["avg_decompose_depth"]
    assert depth.value is None
    assert depth.passed is None
    # Depth is not gated, so its absence must not crash the gate computation.
    assert isinstance(sc.gate_passed, bool)


def test_zero_division_guard():
    findings = _findings(0, 0, [])
    sc = compute_scorecard(findings)
    for name, k in sc.kpis.items():
        assert k.value is None, f"{name} should be None on empty input"
    # No computable gated KPI -> cannot certify -> gate fails (conservative).
    assert sc.gate_passed is False


def test_gate_passed_logic():
    # first_pass_rate 1.0 passes, but field_completeness 0.5 fails its 0.98 gate.
    findings = _findings(2, 1, [_tc("T1"), _tc("T2")])
    validation = {"T1": {"passed": True}, "T2": {"passed": False}}
    sc = compute_scorecard(findings, validation=validation)
    assert sc.kpis["first_pass_rate"].passed is True
    assert sc.kpis["field_completeness"].passed is False
    assert sc.gate_passed is False

    # All computable gated KPIs pass -> gate passes.
    validation_ok = {"T1": {"passed": True}, "T2": {"passed": True}}
    sc_ok = compute_scorecard(findings, validation=validation_ok)
    assert sc_ok.kpis["field_completeness"].passed is True
    assert sc_ok.gate_passed is True


def test_scorecard_json_schema_stable(tmp_path):
    findings = _findings(2, 1, [_tc("T1", "Major"), _tc("T2")])
    sc = compute_scorecard(findings)
    d = to_dict(sc)

    # Top-level keys and order are fixed.
    assert list(d.keys()) == ["total_tcs", "total_requirements", "gate_passed", "kpis"]
    expected_order = [
        "first_pass_rate",
        "requirement_coverage",
        "traceability_completeness",
        "design_method_accuracy",
        "avg_decompose_depth",
        "field_completeness",
        "reality_gap_rate",
        "tier1_critical_req_rate",
    ]
    assert list(d["kpis"].keys()) == expected_order

    # Every KPI entry has the fixed field set and types.
    for kpi in d["kpis"].values():
        assert set(kpi.keys()) == {
            "name", "numerator", "denominator", "value", "threshold", "passed",
        }
        assert isinstance(kpi["numerator"], int)
        assert isinstance(kpi["denominator"], int)
        assert kpi["value"] is None or isinstance(kpi["value"], float)

    # write_scorecard round-trips valid JSON + a markdown file.
    write_scorecard(sc, str(tmp_path))
    with open(tmp_path / "scorecard.json", encoding="utf-8") as fh:
        reloaded = json.load(fh)
    assert reloaded["total_tcs"] == 2
    assert (tmp_path / "scorecard.md").is_file()


def test_tier1_critical_req_rate():
    # 4 Req groups; 2 carry a Tier-1 Critical decomposition finding -> 0.5.
    findings = _findings(6, 4, [])
    findings["per_req_findings"] = [
        {"req_id": "R1", "tier": 1, "severity": "Critical", "rule_ref": "§6.3"},
        {"req_id": "R2", "tier": 1, "severity": "Critical", "rule_ref": "§6.1"},
        {"req_id": "R2", "tier": 1, "severity": "Critical", "rule_ref": "§6.1"},  # dup req
        {"req_id": "R3", "tier": 1, "severity": "Major", "rule_ref": "§6.6"},     # not Critical
    ]
    sc = compute_scorecard(findings)
    k = sc.kpis["tier1_critical_req_rate"]
    assert k.numerator == 2 and k.denominator == 4  # R1, R2 (dedup); R3 excluded
    assert k.value == pytest.approx(0.5)
    assert k.passed is None  # report-only


def test_design_method_accuracy_from_findings():
    # T1 flagged §8.5.2 (method missing) -> only T2 correct.
    findings = _findings(2, 1, [
        _tc("T1", rule_refs=["§8.5.2"]),
        _tc("T2"),
    ])
    sc = compute_scorecard(findings)
    k = sc.kpis["design_method_accuracy"]
    assert k.numerator == 1 and k.denominator == 2
    assert k.value == pytest.approx(0.5)
    assert k.passed is None  # not gated
