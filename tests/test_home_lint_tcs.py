"""Negative tests for features/home/scripts/lint_tcs.py.

A gate that never fires is indistinguishable from a gate that does not exist.
Each test mutates one field of a known-good TC and asserts the corresponding
rule appears — the pristine TC is asserted clean first, so a failure here is
always the mutation and never the fixture.

The rule fixtures are plain dicts, so these tests do not touch the customer
workbooks. One integration test runs the real loaders against `inputs/` and
skips when those files are absent (they are gitignored).
"""
import importlib.util
import json
import sys
from pathlib import Path

import pytest

HOME = Path(__file__).resolve().parent.parent / "features" / "home"

# features/media/scripts/lint_tcs.py exists too. Importing this one by bare name
# would put whichever module loads first into sys.modules under `lint_tcs`
# and hand it to the other project's tests, so load it under a unique name.
# `scripts/` still goes on sys.path because lint_tcs imports feature_config.
sys.path.append(str(HOME / "scripts"))
_spec = importlib.util.spec_from_file_location(
    "home_lint_tcs", HOME / "scripts" / "lint_tcs.py")
if _spec is None or _spec.loader is None:
    pytest.skip("features/home linter not present", allow_module_level=True)
lint_tcs = importlib.util.module_from_spec(_spec)
sys.modules["home_lint_tcs"] = lint_tcs
_spec.loader.exec_module(lint_tcs)

FUNCTIONAL = "功能測試 (Functional based ; no specific technique)"
TEMPLATE = ("Home Screen HMI Logic and Flow R1 SR24 Post 2A "
            "(March 17 2023)_{outline}")


@pytest.fixture
def ctx():
    return {
        "methods": {FUNCTIONAL, "負向測試 (Negative / Invalid)"},
        "popups": {"PU1291": {
            "message": "<X>\nWidget cannot be moved here. \n\n<OK>",
            "exit_conditions": "<OK>\n<X>\nTimeout",
        }},
        "popup_allow": {"PU1291"},
        "outlines": {"4.8.5"},
        "leaves": {"SWE1-HMI-HOME-033": {"req_id": "SWE1-HMI-HOME-033",
                                         "section": "4.8.5"}},
        "template": TEMPLATE,
    }


@pytest.fixture
def tc():
    """A minimal TC that passes every gate."""
    return {
        "req_id": "SWE1-HMI-HOME-033",
        "test_group": "",
        "test_set": "",
        "test_item": "Drag and drop shall not be allowed. This popup has "
                     "OK and [X] to dismiss.\n\n(blocked drag)",
        "pre_conditions": "1. The vehicle speed is 0\n2. Apple CarPlay is connected",
        "input_test_data": "",
        "test_procedure": "1. Press and hold the bottom 50% widget\n"
                          "2. Drag it into the CarPlay projection area",
        "expected_result": "1. The widget is not moved into the CarPlay "
                           "projection area\n"
                           "2. Popup PU1291 is displayed with the text "
                           "\"Widget cannot be moved here.\" and the <OK> and "
                           "<X> controls, as defined by PU1291 String/Popup "
                           "Message",
        "specification_reference": TEMPLATE.replace("{outline}", "4.8.5"),
        "priority": "P1",
        "design_method": "負向測試 (Negative / Invalid)",
        "remarks": "",
    }


def rules(tc, ctx):
    return {f.rule for f in lint_tcs.lint_tc(tc, ctx)}


def test_pristine_tc_is_clean(tc, ctx):
    assert rules(tc, ctx) == set()


def test_unknown_req_id(tc, ctx):
    tc["req_id"] = "SWE1-HMI-HOME-999"
    assert "unknown-req-id" in rules(tc, ctx)


def test_empty_required_field(tc, ctx):
    tc["test_item"] = ""
    assert "keys" in rules(tc, ctx)


def test_input_test_data_blank_is_allowed_but_na_is_not(tc, ctx):
    assert "blank-convention" not in rules(tc, ctx)
    tc["input_test_data"] = "NA"
    assert "blank-convention" in rules(tc, ctx)


@pytest.mark.parametrize("field", ["test_group", "test_set"])
def test_test_group_and_set_must_stay_blank(tc, ctx, field):
    tc[field] = "CarPlay Template"
    assert "blank-column" in rules(tc, ctx)


def test_priority_outside_p0_p3(tc, ctx):
    tc["priority"] = "P9"
    assert "priority" in rules(tc, ctx)


def test_design_method_must_match_dropdown_exactly(tc, ctx):
    tc["design_method"] = "負向測試 (Negative/Invalid)"  # missing spaces
    assert "design-method" in rules(tc, ctx)


def test_spec_reference_wrong_format(tc, ctx):
    tc["specification_reference"] = "Home Screen HMI L&F_4.8.5"
    assert "spec-reference" in rules(tc, ctx)


def test_spec_reference_unresolvable_outline(tc, ctx):
    tc["specification_reference"] = TEMPLATE.replace("{outline}", "99.9")
    assert "spec-reference" in rules(tc, ctx)


def test_spec_reference_outline_disagrees_with_037(tc, ctx):
    ctx["outlines"].add("4.8.6")
    tc["specification_reference"] = TEMPLATE.replace("{outline}", "4.8.6")
    assert "spec-reference" in rules(tc, ctx)


def test_last_mode_reference_accepts_list_item(tc, ctx):
    ctx["leaves"]["SWE1-HMI-HOME-033"]["section"] = "181"
    tc["specification_reference"] = lint_tcs.LAST_MODE_REFERENCE_PREFIX + "181"
    assert "spec-reference" not in rules(tc, ctx)


def test_last_mode_reference_wrong_list_item(tc, ctx):
    ctx["leaves"]["SWE1-HMI-HOME-033"]["section"] = "181"
    tc["specification_reference"] = lint_tcs.LAST_MODE_REFERENCE_PREFIX + "182"
    assert "spec-reference" in rules(tc, ctx)


def test_step_and_er_counts_must_match(tc, ctx):
    tc["expected_result"] += "\n3. An extra unmatched line"
    assert "step-count" in rules(tc, ctx)


def test_single_step_procedure(tc, ctx):
    tc["test_procedure"] = "1. Press and hold the bottom 50% widget"
    tc["expected_result"] = "1. The widget is not moved"
    assert "step-count" in rules(tc, ctx)


def test_step_numbering_must_be_sequential(tc, ctx):
    tc["test_procedure"] = ("1. Press and hold the bottom 50% widget\n"
                            "3. Drag it into the CarPlay projection area")
    assert "step-numbering" in rules(tc, ctx)


def test_forbidden_main_verb_in_procedure(tc, ctx):
    tc["test_procedure"] = ("1. Verify the bottom 50% widget position\n"
                            "2. Drag it into the CarPlay projection area")
    assert "forbidden-verb" in rules(tc, ctx)


def test_modal_verb_in_expected_result(tc, ctx):
    tc["expected_result"] = ("1. The widget shall not be moved\n"
                             "2. Popup PU1291 is displayed, as defined by "
                             "PU1291 String/Popup Message")
    assert "er-modal" in rules(tc, ctx)


def test_a_h08_quoted_popup_text_is_exempt_from_the_modal_ban(tc, ctx):
    """`Widget cannot be moved here.` contains a modal but is source text."""
    assert "er-modal" not in rules(tc, ctx)


def test_unknown_popup_id(tc, ctx):
    tc["expected_result"] = tc["expected_result"].replace("PU1291", "PU9999")
    assert "popup-unknown" in rules(tc, ctx)


def test_popup_cited_without_the_profile_citation_form(tc, ctx):
    tc["expected_result"] = ("1. The widget is not moved\n"
                             "2. Popup PU1291 is displayed")
    assert "popup-citation" in rules(tc, ctx)


def test_paraphrased_popup_text_is_rejected(tc, ctx):
    tc["expected_result"] = tc["expected_result"].replace(
        "Widget cannot be moved here.", "The widget cannot be placed here.")
    assert "popup-verbatim" in rules(tc, ctx)


def test_bracket_token_not_a_control_of_the_cited_popup(tc, ctx):
    tc["expected_result"] = tc["expected_result"].replace("<OK>", "<Confirm>")
    assert "popup-token" in rules(tc, ctx)


def test_a_h10_test_item_may_use_the_rd_bracket_notation(tc, ctx):
    """Test Item quotes the requirement verbatim; `[X]` there is not a defect."""
    assert "popup-token" not in rules(tc, ctx)


def test_br_tag_is_rejected(tc, ctx):
    tc["pre_conditions"] = "1. The vehicle speed is 0<br>2. CarPlay connected"
    assert "br-tag" in rules(tc, ctx)


# ----------------------------------------------------- spec-reference override

def test_recorded_override_allows_a_deliberate_section_divergence(tc, ctx):
    """037 sometimes records the wrong outline; diverging must be declared."""
    ctx["outlines"].add("4.8.6")
    tc["specification_reference"] = TEMPLATE.replace("{outline}", "4.8.6")
    assert "spec-reference" in rules(tc, ctx)
    tc["spec_reference_override"] = "A-H21"
    assert "spec-reference" not in rules(tc, ctx)


def test_override_must_be_an_anomaly_id(tc, ctx):
    ctx["outlines"].add("4.8.6")
    tc["specification_reference"] = TEMPLATE.replace("{outline}", "4.8.6")
    tc["spec_reference_override"] = "because 037 is wrong"
    found = rules(tc, ctx)
    assert "spec-reference-override" in found
    assert "spec-reference" in found, "a malformed override must not excuse it"


def test_override_does_not_excuse_an_unresolvable_outline(tc, ctx):
    """An outline absent from the map is still a hard failure."""
    tc["specification_reference"] = TEMPLATE.replace("{outline}", "99.9")
    tc["spec_reference_override"] = "A-H21"
    assert "spec-reference" in rules(tc, ctx)


# --------------------------------------------------------------- placeholders

@pytest.fixture
def placeholder(tc):
    """Profile §6 shape: a leaf that legitimately produces no test content."""
    return dict(tc, placeholder=True,
                pre_conditions="",
                test_procedure=lint_tcs.PLACEHOLDER_BODY,
                expected_result=lint_tcs.PLACEHOLDER_BODY,
                priority="",
                design_method="",
                remarks="Covered by 062-071; external Phone HMI spec (A-H02)")


def test_pristine_placeholder_is_clean(placeholder, ctx):
    assert rules(placeholder, ctx) == set()


@pytest.mark.parametrize("field,value", [
    ("test_procedure", "1. Do something\n2. Do more"),
    ("expected_result", "1. Something happens\n2. More happens"),
    ("priority", "P1"),
    ("design_method", FUNCTIONAL),
    ("test_item", ""),
])
def test_placeholder_body_must_stay_empty_or_fixed(placeholder, ctx, field, value):
    placeholder[field] = value
    assert "placeholder-body" in rules(placeholder, ctx)


@pytest.mark.parametrize("remarks", ["", "covered elsewhere"])
def test_placeholder_remarks_must_cite_an_anomaly(placeholder, ctx, remarks):
    placeholder["remarks"] = remarks
    assert "placeholder-remarks" in rules(placeholder, ctx)


def test_placeholder_still_checks_traceability(placeholder, ctx):
    placeholder["specification_reference"] = TEMPLATE.replace("{outline}", "99.9")
    assert "spec-reference" in rules(placeholder, ctx)


def test_placeholder_still_checks_blank_columns(placeholder, ctx):
    placeholder["test_set"] = "Shortcut Exclusion"
    assert "blank-column" in rules(placeholder, ctx)


def test_placeholder_is_exempt_from_content_gates(placeholder, ctx):
    """The gates that assume real content must not fire on a placeholder."""
    assert not ({"step-count", "step-numbering", "priority", "design-method",
                 "keys"} & rules(placeholder, ctx))


def test_generated_b1_output_passes_the_real_gate():
    """Integration: real loaders, real inputs. Skips when inputs are absent."""
    data = HOME / "data"
    generated = sorted((HOME / "generated").glob("*.json"))
    if not generated or not (data / "remaining_leaves.json").exists():
        pytest.skip("features/home data/ or generated/ not built")
    cfg = lint_tcs.load_feature_config(HOME)
    try:
        workbook = lint_tcs.resolve_path(cfg, "workbook")
        popup = lint_tcs.resolve_path(cfg, "popup_list")
    except SystemExit:
        pytest.skip("features/home inputs/ not present (gitignored)")
    real = {
        "methods": lint_tcs.load_design_methods(workbook),
        "popups": lint_tcs.load_popup_index(popup),
        "popup_allow": set(cfg.get("lint", {}).get("popup_ids") or []),
        "outlines": lint_tcs.load_outlines(data),
        "leaves": lint_tcs.load_leaves(data),
        "template": cfg["spec_reference_template"],
    }
    findings = []
    for path in generated:
        for entry in json.loads(path.read_text()).get("tcs", []):
            findings += lint_tcs.lint_tc(entry, real, source=path.name)
    assert not findings, "\n".join(f.format() for f in findings)
