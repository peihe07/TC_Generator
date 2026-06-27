"""Content-based traceability tests (deterministic; no AI)."""
from req_tracer import match_tc, summarize, trace_tcs

_REQS = [
    {"id": "SWE1-PLA-006-02", "title": "Repeat All Behavior",
     "desc": "When in Repeat All mode the system plays each item sequentially "
             "and continues from the first item after the last."},
    {"id": "SWE1-PLA-010-02", "title": "Shuffle On Behavior",
     "desc": "When Shuffle mode is On the system plays the playlist in a "
             "randomized sequence."},
    {"id": "SWE1-PLA-001", "title": "Popup For No Supported Files Found Error",
     "desc": "When No Supported Files Found Error occurs the HU displays PU0003."},
]


def test_match_tc_picks_best_by_content():
    best, score = match_tc(
        "Verify Repeat All mode plays each item sequentially and loops to first",
        _REQS)
    assert best["id"] == "SWE1-PLA-006-02"
    assert score > 0


def test_match_unrelated_text_scores_low():
    best, score = match_tc("Adjust the cabin temperature climate fan speed", _REQS)
    assert score < 0.08  # below default threshold -> not traceable


def test_trace_tcs_flags_untraceable_and_id_mismatch():
    tcs = [
        # content matches Repeat req, but the TC carries a renumbered req_id.
        {"tc_id": "T1", "req_id": "SWE1-PLA-030-02",
         "test_item": "Repeat All mode plays each item sequentially loops to first"},
        # content has no matching requirement.
        {"tc_id": "T2", "req_id": "SWE1-PLA-999",
         "test_item": "calibrate steering wheel torque sensor"},
    ]
    results = trace_tcs(tcs, _REQS)
    by_id = {r.tc_id: r for r in results}
    assert by_id["T1"].matched_req_id == "SWE1-PLA-006-02"
    assert by_id["T1"].traceable is True
    assert by_id["T1"].id_agrees is False        # renumbered ID caught
    assert by_id["T2"].traceable is False         # content untraceable

    s = summarize(results)
    assert s["total_tcs"] == 2 and s["traceable"] == 1
    assert s["id_mismatch_count"] == 1


def test_id_agrees_across_namespaces():
    """Different projects use different id namespaces but share the FEATURE-NNN
    core (TC 'SWE1-DEAL-001-01' vs SWE1 analysis 'NEWR1L-SWRA-DEAL-001')."""
    from req_tracer import _ids_agree
    assert _ids_agree("NEWR1L-SWRA-DEAL-001", "SWE1-DEAL-001-01") is True
    assert _ids_agree("SWE1-PLA-006-02", "SWE1-PLA-006-02") is True
    # Genuinely different feature numbers do NOT agree.
    assert _ids_agree("SWE1-PLA-006-02", "SWE1-PLA-030-02") is False


def test_sibling_twin_suppressed_real_suspect_kept():
    """Templated twins (MSC vs DAP Alphajump, identical wording) -> ambiguous, not
    a mismatch. A TC whose content clearly leans to a different feature -> suspect."""
    reqs = [
        {"id": "SWE1-PLA-014", "title": "USB MSC Alphajump",
         "desc": "enable the alphajump softkey and display the alphajump screen"},
        {"id": "SWE1-PLA-016", "title": "USB DAP Alphajump",
         "desc": "enable the alphajump softkey and display the alphajump screen"},
        {"id": "SWE1-PLA-039", "title": "Metadata Display",
         "desc": "show and hide the track metadata title artist album on screen"},
    ]
    tcs = [
        # Written 016 (DAP); content has no MSC/DAP keyword -> identical to both -> twin.
        {"tc_id": "T-twin", "req_id": "SWE1-PLA-016",
         "test_item": "enable the alphajump softkey and display the alphajump screen"},
        # Written 040 (not in universe); content clearly = metadata -> suspect.
        {"tc_id": "T-suspect", "req_id": "SWE1-PLA-040",
         "test_item": "show and hide the track metadata title artist album on screen"},
    ]
    res = {r.tc_id: r for r in trace_tcs(tcs, reqs)}
    assert res["T-twin"].ambiguous is True
    assert res["T-twin"].confident_mismatch is False
    assert res["T-suspect"].confident_mismatch is True

    s = summarize(list(res.values()))
    assert s["id_mismatch_count"] == 1
    assert s["ambiguous_twin_count"] == 1


def test_coverage_counts_written_id_and_rollup():
    """A requirement is covered when a TC's written id points to it even if
    content-tracing attributed the TC to a templated twin; a parent is covered
    when a child is covered."""
    from req_tracer import to_scorecard_traceability
    reqs = [
        {"id": "SWE1-PLA-014", "title": "USB MSC Alphajump",
         "desc": "enable the alphajump softkey and display the alphajump screen"},
        {"id": "SWE1-PLA-016", "title": "USB DAP Alphajump",
         "desc": "enable the alphajump softkey and display the alphajump screen"},
        {"id": "SWE1-PLA-016-02", "title": "Display Alphajump Screen",
         "desc": "display the alpha-numeric selection screen"},
        {"id": "SWE1-PLA-099", "title": "Lonely", "desc": "totally unrelated climate"},
    ]
    tcs = [
        # written for 014, but identical wording content-matches 016 (twin).
        {"tc_id": "T1", "req_id": "SWE1-PLA-014",
         "test_item": "enable the alphajump softkey and display the alphajump screen"},
        # written for the child 016-02 -> parent 016 should roll up as covered.
        {"tc_id": "T2", "req_id": "SWE1-PLA-016-02",
         "test_item": "display the alpha-numeric selection screen"},
    ]
    all_ids = [r["id"] for r in reqs]
    trace = to_scorecard_traceability(trace_tcs(tcs, reqs), all_ids)
    cov = set(trace["covered_requirements"])
    # 014 (written), 016 (twin/parent rollup), 016-02 (written) all covered.
    assert {"SWE1-PLA-014", "SWE1-PLA-016", "SWE1-PLA-016-02"} <= cov
    # the unrelated requirement stays uncovered.
    assert "SWE1-PLA-099" not in cov
