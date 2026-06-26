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
