"""Stage 7 — KPI Scorecard (PIPELINE_DESIGN § Stage 7).

Aggregates Stage 5 structural results + Stage 6 §9 findings into 7 KPIs and
writes `scorecard.json` (stable schema for trend comparison) + `scorecard.md`
(human-readable). Pure Python, no AI, zero cost.

Source availability (see M1/RECON_NOTES.md):
- first_pass_rate, design_method_accuracy  -> computable from findings alone.
- traceability_completeness                -> needs `traceability` input.
- field_completeness                       -> needs `validation` input.
- requirement_coverage                     -> needs `traceability.all_requirements`
                                              (the planned requirement universe).
- avg_decompose_depth                      -> needs `decompose_meta` (Stage 3).
- reality_gap_rate                         -> needs Stage 6 reality-gap markers.

When a KPI's source data is absent, its `value` is None (never fabricated, never
zero) and it does not participate in the gate.

Input shapes
------------
findings: dict          §9 findings.json (parsed). Uses batch_meta.total_tcs,
                        batch_meta.total_req_groups, per_tc_findings[].
validation: dict | None { tc_id: {"passed": bool} }  (Stage 5 per-TC).
traceability: dict | None
                        {
                          "per_tc": { tc_id: {"matched": bool, "req_id": str} },
                          "all_requirements": [req_id, ...]   # optional
                        }
decompose_meta: dict | None { req_id: int_step_count }  (Stage 3).
"""
from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass


# Fixed KPI order — keeps scorecard.json schema stable across runs for trend
# comparison. Do not reorder.
KPI_ORDER = [
    "first_pass_rate",
    "requirement_coverage",
    "traceability_completeness",
    "design_method_accuracy",
    "avg_decompose_depth",
    "field_completeness",
    "reality_gap_rate",
    # Appended (schema evolves by appending only, to keep older columns stable).
    "tier1_critical_req_rate",  # lower is better; measures decomposition depth
    "req_id_mismatch_rate",     # lower is better; TC's written req_id != content match
]

# Severities that disqualify a TC from "first pass".
_BLOCKING_SEVERITIES = {"Critical", "Major"}

# Rule refs whose presence on a TC means its design method is wrong/missing.
_DESIGN_METHOD_RULES = {"§8.5.2", "§8.5.3"}

# Default gate thresholds; overridable via config/kpi_thresholds.json or the
# `thresholds` argument. KPIs absent here are reported but not gated.
_DEFAULT_THRESHOLDS = {
    "first_pass_rate": 0.80,
    "requirement_coverage": 1.00,
    "traceability_completeness": 0.95,
    "field_completeness": 0.98,
}

_DEFAULT_THRESHOLDS_PATH = os.path.join("config", "kpi_thresholds.json")


@dataclass
class KPI:
    name: str
    numerator: int
    denominator: int
    value: float | None      # None when denominator == 0 or source missing
    threshold: float | None  # None when not gated
    passed: bool | None      # value >= threshold, else None when not gated / no value


@dataclass
class Scorecard:
    kpis: dict[str, KPI]
    total_tcs: int
    total_requirements: int
    gate_passed: bool        # True only if every computable gated KPI passed


def load_thresholds(path: str = _DEFAULT_THRESHOLDS_PATH) -> dict:
    """Read gate thresholds; fall back to built-in defaults when file absent."""
    if not os.path.isfile(path):
        return dict(_DEFAULT_THRESHOLDS)
    with open(path, encoding="utf-8") as fh:
        loaded = json.load(fh)
    merged = dict(_DEFAULT_THRESHOLDS)
    merged.update(loaded)
    return merged


def _make_kpi(name: str, numerator: int, denominator: int,
              threshold: float | None) -> KPI:
    """Build a ratio KPI with zero-division and gating guards."""
    value = numerator / denominator if denominator else None
    if threshold is None or value is None:
        passed = None
    else:
        passed = value >= threshold
    return KPI(name=name, numerator=numerator, denominator=denominator,
               value=value, threshold=threshold, passed=passed)


def _tc_findings(findings: dict) -> list[dict]:
    return findings.get("per_tc_findings") or []


def _first_pass_rate(findings: dict, total_tcs: int, threshold: float | None) -> KPI:
    blocked = {
        tc.get("tc_id")
        for tc in _tc_findings(findings)
        if any(f.get("severity") in _BLOCKING_SEVERITIES
               for f in tc.get("findings", []))
    }
    blocked.discard(None)
    return _make_kpi("first_pass_rate", total_tcs - len(blocked), total_tcs, threshold)


def _design_method_accuracy(findings: dict, total_tcs: int,
                            threshold: float | None) -> KPI:
    flagged = {
        tc.get("tc_id")
        for tc in _tc_findings(findings)
        if any(f.get("rule_ref") in _DESIGN_METHOD_RULES
               for f in tc.get("findings", []))
    }
    flagged.discard(None)
    return _make_kpi("design_method_accuracy", total_tcs - len(flagged),
                     total_tcs, threshold)


def _traceability_completeness(traceability: dict | None, total_tcs: int,
                               threshold: float | None) -> KPI:
    per_tc = (traceability or {}).get("per_tc")
    if not per_tc:
        return _make_kpi("traceability_completeness", 0, 0, threshold)
    matched = sum(1 for v in per_tc.values() if v.get("matched"))
    return _make_kpi("traceability_completeness", matched, total_tcs, threshold)


def _requirement_coverage(findings: dict, traceability: dict | None,
                          threshold: float | None) -> KPI:
    all_reqs = (traceability or {}).get("all_requirements")
    if not all_reqs:
        # findings alone cannot see requirements that produced zero TCs.
        return _make_kpi("requirement_coverage", 0, 0, threshold)
    per_tc = (traceability or {}).get("per_tc") or {}
    reqs_with_tc = {v.get("req_id") for v in per_tc.values() if v.get("req_id")}
    covered = sum(1 for r in all_reqs if r in reqs_with_tc)
    return _make_kpi("requirement_coverage", covered, len(all_reqs), threshold)


def _field_completeness(validation: dict | None, total_tcs: int,
                        threshold: float | None) -> KPI:
    if not validation:
        return _make_kpi("field_completeness", 0, 0, threshold)
    passed = sum(1 for v in validation.values() if v.get("passed"))
    return _make_kpi("field_completeness", passed, total_tcs, threshold)


def _avg_decompose_depth(decompose_meta: dict | None, total_requirements: int,
                         threshold: float | None) -> KPI:
    if not decompose_meta:
        return _make_kpi("avg_decompose_depth", 0, 0, threshold)
    total_steps = sum(int(v) for v in decompose_meta.values())
    return _make_kpi("avg_decompose_depth", total_steps, total_requirements, threshold)


def _reality_gap_rate(findings: dict, total_tcs: int, threshold: float | None) -> KPI:
    # Only computable once Stage 6 emits reality-gap markers; detect capability
    # by the presence of a `reality_gap` key on any finding.
    has_capability = any(
        "reality_gap" in f
        for tc in _tc_findings(findings)
        for f in tc.get("findings", [])
    )
    if not has_capability:
        return _make_kpi("reality_gap_rate", 0, 0, threshold)
    flagged = {
        tc.get("tc_id")
        for tc in _tc_findings(findings)
        if any(f.get("reality_gap") for f in tc.get("findings", []))
    }
    flagged.discard(None)
    return _make_kpi("reality_gap_rate", len(flagged), total_tcs, threshold)


def _tier1_critical_req_rate(findings: dict, total_requirements: int,
                            threshold: float | None) -> KPI:
    """Fraction of Req groups carrying a Tier-1 Critical decomposition finding.

    Lower is better — directly measures under-decomposition (missing enumeration
    values / negative branches) that only the semantic review catches.
    """
    crit = {
        f.get("req_id")
        for f in findings.get("per_req_findings", [])
        if f.get("tier") == 1 and f.get("severity") == "Critical"
    }
    crit.discard(None)
    return _make_kpi("tier1_critical_req_rate", len(crit), total_requirements, threshold)


def _req_id_mismatch_rate(traceability: dict | None, total_tcs: int,
                          threshold: float | None) -> KPI:
    """Fraction of TCs whose written req_id disagrees with their content match.

    Lower is better — surfaces renumbered / mis-tagged req IDs (the confirmed
    Player defect). Only content-traceable TCs are considered for the numerator.
    """
    per_tc = (traceability or {}).get("per_tc")
    if not per_tc:
        return _make_kpi("req_id_mismatch_rate", 0, 0, threshold)
    mismatch = sum(1 for v in per_tc.values()
                   if v.get("matched") and v.get("id_agrees") is False)
    return _make_kpi("req_id_mismatch_rate", mismatch, total_tcs, threshold)


def compute_scorecard(
    findings: dict,
    validation: dict | None = None,
    traceability: dict | None = None,
    decompose_meta: dict | None = None,
    thresholds: dict | None = None,
) -> Scorecard:
    """Aggregate findings + structural + traceability data into 7 KPIs."""
    th = thresholds if thresholds is not None else load_thresholds()
    meta = findings.get("batch_meta", {})
    total_tcs = int(meta.get("total_tcs", 0) or 0)
    total_requirements = int(meta.get("total_req_groups", 0) or 0)

    kpis = {
        "first_pass_rate": _first_pass_rate(
            findings, total_tcs, th.get("first_pass_rate")),
        "requirement_coverage": _requirement_coverage(
            findings, traceability, th.get("requirement_coverage")),
        "traceability_completeness": _traceability_completeness(
            traceability, total_tcs, th.get("traceability_completeness")),
        "design_method_accuracy": _design_method_accuracy(
            findings, total_tcs, th.get("design_method_accuracy")),
        "avg_decompose_depth": _avg_decompose_depth(
            decompose_meta, total_requirements, th.get("avg_decompose_depth")),
        "field_completeness": _field_completeness(
            validation, total_tcs, th.get("field_completeness")),
        "reality_gap_rate": _reality_gap_rate(
            findings, total_tcs, th.get("reality_gap_rate")),
        "tier1_critical_req_rate": _tier1_critical_req_rate(
            findings, total_requirements, th.get("tier1_critical_req_rate")),
        "req_id_mismatch_rate": _req_id_mismatch_rate(
            traceability, total_tcs, th.get("req_id_mismatch_rate")),
    }

    gated = [k for k in kpis.values() if k.threshold is not None and k.value is not None]
    gate_passed = bool(gated) and all(k.passed for k in gated)

    return Scorecard(
        kpis={name: kpis[name] for name in KPI_ORDER},
        total_tcs=total_tcs,
        total_requirements=total_requirements,
        gate_passed=gate_passed,
    )


def to_dict(sc: Scorecard) -> dict:
    """Stable, ordered dict for scorecard.json."""
    return {
        "total_tcs": sc.total_tcs,
        "total_requirements": sc.total_requirements,
        "gate_passed": sc.gate_passed,
        "kpis": {name: asdict(sc.kpis[name]) for name in KPI_ORDER},
    }


def _fmt_value(kpi: KPI) -> str:
    if kpi.value is None:
        return "N/A (來源缺)"
    # avg_decompose_depth is an average, not a ratio; show raw.
    if kpi.name == "avg_decompose_depth":
        return f"{kpi.value:.2f}"
    return f"{kpi.value:.1%}"


def _fmt_gate(kpi: KPI) -> str:
    if kpi.threshold is None:
        return "—（僅報）"
    if kpi.passed is None:
        return f"門檻 {kpi.threshold:.0%} · 無法評估"
    return f"門檻 {kpi.threshold:.0%} · {'PASS' if kpi.passed else 'FAIL'}"


def render_markdown(sc: Scorecard) -> str:
    """Human-readable scorecard.md."""
    lines = [
        "# TC Generator — KPI Scorecard",
        "",
        f"- 總 TC 數:{sc.total_tcs}",
        f"- 總需求數:{sc.total_requirements}",
        f"- **Gate:{'PASS ✅' if sc.gate_passed else 'FAIL ❌'}**",
        "",
        "| KPI | 數值 | 分子/分母 | 門檻 / 結果 |",
        "|---|---|---|---|",
    ]
    for name in KPI_ORDER:
        k = sc.kpis[name]
        lines.append(
            f"| {k.name} | {_fmt_value(k)} | {k.numerator}/{k.denominator} | {_fmt_gate(k)} |"
        )
    missing = [sc.kpis[n].name for n in KPI_ORDER if sc.kpis[n].value is None]
    if missing:
        lines += ["", "## 無法計算（缺來源資料）", ""]
        lines += [f"- `{m}`" for m in missing]
    lines.append("")
    return "\n".join(lines)


def write_scorecard(sc: Scorecard, out_dir: str) -> None:
    """Write scorecard.json + scorecard.md into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "scorecard.json"), "w", encoding="utf-8") as fh:
        json.dump(to_dict(sc), fh, ensure_ascii=False, indent=2)
    with open(os.path.join(out_dir, "scorecard.md"), "w", encoding="utf-8") as fh:
        fh.write(render_markdown(sc))
