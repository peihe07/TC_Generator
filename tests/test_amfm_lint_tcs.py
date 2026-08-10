"""Tests for AMFMHMI/scripts/lint_tcs.py.

Every gate gets a test that mutates one field and asserts the rule fires. A
gate that never fires is indistinguishable from a gate that does not exist —
the Home lint learned this the hard way (A-H10 shipped inside a green corpus
because the rule itself encoded the wrong scope).

The two AMFM-specific gates carry the most weight:

- R10-2a: absorbing an unallocated CFTS clause is allowed only if the absorbed
  clause is cited. The check keys on the ids the `[A-AM10]` assumption itself
  names, because a plain count check misses a second absorbed clause and a
  blanket "marked parent ⇒ every TC multi-cites" over-fires when only one TC
  absorbs.
- R10-4: Remarks ships to the customer, so internal ruling ids must not appear
  there — while `R1L`, the program name, must not trip the same pattern.
"""
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location(
    "amfm_lint", ROOT / "AMFMHMI" / "scripts" / "lint_tcs.py")
if _spec is None or _spec.loader is None:
    pytest.skip("AMFM lint_tcs.py not present", allow_module_level=True)
lint = importlib.util.module_from_spec(_spec)
sys.modules["amfm_lint"] = lint
_spec.loader.exec_module(lint)


CFG = {
    "test_group": "AMFM",
    "spec_reference_template": "{doc}-{stla_id}",
}
METHODS = ["功能測試 (Functional based ; no specific technique)",
           "邊界值分析 (Boundary Value Analysis, BVA)"]
STLA = {"SWE-RA-RAD-025": {"doc": "CFTS024", "stla_id": 4872439}}


def tc(**over):
    base = {
        "req_id": "SWE-RA-RAD-025",
        "tc_title": "Tune Up increments to next higher station",
        "test_group": "AMFM", "test_set": "Tune",
        "test_item": "requirement text",
        "pre_conditions": "1. An FM/AM signal generator is ready",
        "input_test_data": "NA",
        "test_procedure": '1. Read the tuned frequency\n2. Press "Tune Up"',
        "expected_result": "1. The frequency is displayed\n2. The frequency "
                           "is incremented",
        "specification_reference": "CFTS024-4872439",
        "priority": "P1",
        "design_method": METHODS[0],
        "remarks": "",
    }
    base.update(over)
    return base


def gates(tc_dict, doc=None, citations=None):
    return {f["gate"] for f in
            lint.lint_tc("T-01", tc_dict, doc or {}, CFG, METHODS, STLA,
                         citations)}


def test_a_clean_tc_has_no_findings():
    assert gates(tc()) == set()


# ------------------------------------------------------------ generic gates

def test_single_step_procedure_fires():
    assert "step-count" in gates(tc(test_procedure="1. Do one thing",
                                    expected_result="1. It happened"))


def test_er_not_aligned_with_steps_fires():
    assert "er-alignment" in gates(tc(expected_result="1. Only one line"))


def test_trailing_period_fires():
    assert "trailing-period" in gates(
        tc(pre_conditions="1. An FM/AM signal generator is ready."))


def test_modal_in_er_fires():
    assert "er-modal" in gates(
        tc(expected_result="1. The frequency is displayed\n"
                           "2. The HU shall increment the frequency"))


def test_modal_in_title_fires():
    assert "title-modal" in gates(tc(tc_title="HU shall increment frequency"))


def test_overlong_title_fires():
    assert "title-length" in gates(tc(tc_title=" ".join(["word"] * 15)))


def test_bad_priority_fires():
    assert "priority" in gates(tc(priority="High"))


def test_design_method_outside_the_dropdown_fires():
    assert "design-method" in gates(tc(design_method="Functional"))


def test_legacy_test_group_fires():
    """The legacy region writes 'Radio'; R7-Q1 replaced it for new rows."""
    assert "test-group" in gates(tc(test_group="Radio"))


def test_empty_test_set_fires():
    assert "test-set" in gates(tc(test_set=""))


def test_square_bracket_outside_a_signal_token_fires():
    assert "square-bracket" in gates(
        tc(test_procedure='1. Read the frequency\n2. Press [Tune Up]'))


def test_a_source_quoted_signal_value_keeps_its_brackets():
    """Profile §3.4 — $SIGNAL$ = [value] is quoted verbatim from the CFTS."""
    assert "square-bracket" not in gates(
        tc(input_test_data="$ICS_KNOB2_DIR$ = [Increment]\n"
                           "$ICS_KNOB2_VAL$ = [63]"))


def test_spec_reference_not_matching_the_map_fires():
    assert "spec-reference" in gates(tc(specification_reference="CFTS024-9999999"))


def test_malformed_spec_reference_fires():
    assert "spec-reference" in gates(tc(specification_reference="CFTS024-4872439; 4872440"))


def test_unknown_req_id_fires():
    assert "unknown-req-id" in gates(tc(req_id="SWE-RA-RAD-999"))


# ------------------------------------------------- R10-2a absorption citing

ABSORB = {"assumptions": [
    "[A-AM10] CFTS024-4872440 and CFTS024-4872441 are unallocated clauses "
    "elaborating this leaf."]}


def test_multi_cite_without_an_absorption_marker_fires():
    assert "absorption-cite" in gates(
        tc(specification_reference="CFTS024-4872439; CFTS024-4872440"), doc={})


def test_multi_cite_with_an_absorption_marker_passes():
    assert "absorption-cite" not in gates(
        tc(specification_reference="CFTS024-4872439; CFTS024-4872440"),
        doc=ABSORB)


def test_absorbed_ids_are_read_from_the_marker():
    assert lint.absorbed_ids(ABSORB) == {"4872440", "4872441"}
    assert lint.absorbed_ids({"assumptions": ["[R8] no absorption here"]}) == set()


def test_a_single_cite_under_a_marked_parent_is_not_itself_an_error():
    """Only one TC of a pair may absorb; the leaf-level check catches a clause
    nobody cites, so the per-TC check must not over-fire here."""
    assert "absorption-cite" not in gates(tc(), doc=ABSORB)


# ------------------------------------------------------- R10-4 Remarks scope

def test_internal_ruling_id_in_remarks_fires():
    assert "remarks-internal" in gates(tc(remarks="Corrected per R9"))


def test_internal_anomaly_id_in_remarks_fires():
    assert "remarks-internal" in gates(
        tc(remarks="Wrap-around behaviour sourced from CFTS024-4872441 (A-AM10)"))


def test_external_language_remarks_passes():
    assert "remarks-internal" not in gates(tc(
        remarks="Source reference corrected: the requirement report's clause "
                "id tail names the ICS tune-down clause, while the requirement "
                "text is the Direct Number Input clause."))


def test_the_program_name_r1l_does_not_trip_the_internal_id_pattern():
    assert "remarks-internal" not in gates(
        tc(remarks="Applies to the R1L program only"))


# --------------------------------------------------------------- integration

def test_the_real_generated_corpus_is_clean(tmp_path):
    """Everything generated so far must stay green as gates and batches grow.

    The count is asserted as a floor, not an equality: pinning the exact total
    makes every new batch fail a test that is not about the new batch.
    """
    home = ROOT / "AMFMHMI"
    if not (home / "data" / "stla_to_cfts.json").exists():
        pytest.skip("AMFM data/ not built")
    if not list((home / "generated").glob("*.json")):
        pytest.skip("AMFM generated/ empty")
    import argparse
    report = tmp_path / "r.json"
    rc = lint.run(argparse.Namespace(feature_dir=str(home), generated="generated",
                                     json_report=str(report)))
    payload = json.loads(report.read_text(encoding="utf-8"))
    assert rc == 0, payload["findings"]
    assert payload["tcs"] >= 13, "the pilot's 13 TCs must still be there"


# ------------------------------------------------- R11 cross-doc cite-form

# The spec writes `{See CFTS019-718}` in leaf 025's clause only. Everything
# below turns on that: the same token is a legitimate citation here and a
# fabricated one under any other leaf.
CITATIONS = {"CFTS019-718": {"doc": "CFTS019", "status": "unresolved-scheme-mismatch",
                             "req_ids": ["SWE-RA-RAD-025"],
                             "citing_clauses": [{"clause_id": 4872439,
                                                 "context": "rejection tone"}]}}
CITE_FORM = dict(
    specification_reference="CFTS024-4872439; CFTS019-718",
    expected_result="1. The frequency is displayed\n2. The key press rejection "
                    "tone is played, as defined by CFTS019-718")


def test_a_short_form_cross_doc_token_is_accepted_for_the_leaf_that_cites_it():
    """`CFTS019-718` is 3-digit — the 7-digit anchor shape must not reject it."""
    assert gates(tc(**CITE_FORM), citations=CITATIONS) == set()


def test_a_cross_doc_token_no_clause_of_this_leaf_writes_is_caught():
    other = {"CFTS019-718": dict(CITATIONS["CFTS019-718"],
                                 req_ids=["SWE-RA-RAD-014"])}
    assert "cross-reference" in gates(tc(**CITE_FORM), citations=other)


def test_a_cited_token_with_no_anchoring_er_line_fires():
    """R11 allows the borrowed outcome only anchored to the citation."""
    unanchored = dict(CITE_FORM,
                      expected_result="1. The frequency is displayed\n2. The "
                                      "key press rejection tone is played")
    assert "cross-reference-anchor" in gates(tc(**unanchored),
                                             citations=CITATIONS)


def test_cite_form_does_not_demand_an_absorption_marker():
    """R11 claims no coverage of the cited clause, so R10-2a does not apply."""
    assert "absorption-cite" not in gates(tc(**CITE_FORM), doc={},
                                          citations=CITATIONS)


def test_absorption_still_needs_its_marker_alongside_a_cross_reference():
    """The cite-form exemption must not launder a same-document multi-cite."""
    both = dict(CITE_FORM,
                specification_reference="CFTS024-4872439; CFTS024-4872440; "
                                        "CFTS019-718")
    assert "absorption-cite" in gates(tc(**both), doc={}, citations=CITATIONS)


def test_cited_tokens_are_scoped_per_leaf():
    assert lint.cited_tokens(CITATIONS, "SWE-RA-RAD-025") == {"CFTS019-718"}
    assert lint.cited_tokens(CITATIONS, "SWE-RA-RAD-014") == set()
    assert lint.cited_tokens({}, "SWE-RA-RAD-025") == set()
