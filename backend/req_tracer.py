"""Content-based traceability: map a TC to its source requirement by TEXT, not ID.

Req IDs in the TC workbook can be renumbered / out of sync with the SWE1
analysis (a confirmed defect on the Player project), so ID-based tracing is
unreliable. This matches each TC's wording against the SWE1 requirement
descriptions via token Jaccard (deterministic, no AI), and flags TCs whose
content does not map to any requirement.
"""
from __future__ import annotations

import json
from dataclasses import dataclass

from spec_matcher import _tokenize, _jaccard

# Below this Jaccard score a TC is considered NOT traceable to any requirement.
DEFAULT_THRESHOLD = 0.08


@dataclass
class TraceResult:
    tc_id: str
    tc_req_id: str            # the (unreliable) req_id written on the TC
    matched_req_id: str | None  # best content match in the SWE1 universe
    matched_title: str
    score: float
    traceable: bool
    id_agrees: bool           # does the TC's own req_id match the content match?


def load_swe1_reqs(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _req_tokens(req: dict) -> set[str]:
    return _tokenize(f"{req.get('title', '')} {req.get('desc', '')}")


def match_tc(tc_text: str, reqs: list[dict],
             req_tokens: list[set[str]] | None = None) -> tuple[dict | None, float]:
    """Return (best requirement, score) by token Jaccard over title+desc."""
    tokens = _tokenize(tc_text)
    if not tokens:
        return None, 0.0
    if req_tokens is None:
        req_tokens = [_req_tokens(r) for r in reqs]
    best, best_score = None, 0.0
    for req, rt in zip(reqs, req_tokens):
        score = _jaccard(tokens, rt)
        if score > best_score:
            best, best_score = req, score
    return best, best_score


def trace_tcs(tcs: list[dict], reqs: list[dict],
              threshold: float = DEFAULT_THRESHOLD) -> list[TraceResult]:
    """Match each TC (dict with tc_id / req_id / test_item[/expected_result])
    to its best content requirement."""
    req_tokens = [_req_tokens(r) for r in reqs]
    out: list[TraceResult] = []
    for tc in tcs:
        text = f"{tc.get('test_item', '')} {tc.get('expected_result', '')}"
        best, score = match_tc(text, reqs, req_tokens)
        matched_id = best.get("id") if best else None
        tc_req = str(tc.get("req_id", "") or "")
        out.append(TraceResult(
            tc_id=str(tc.get("tc_id", "") or ""),
            tc_req_id=tc_req,
            matched_req_id=matched_id,
            matched_title=best.get("title", "") if best else "",
            score=round(score, 3),
            traceable=score >= threshold,
            # IDs "agree" only if the TC's own req_id is a prefix-or-equal of the
            # content match (tolerant of -NN suffixes).
            id_agrees=bool(matched_id and tc_req and (
                matched_id == tc_req or matched_id.startswith(tc_req)
                or tc_req.startswith(matched_id))),
        ))
    return out


def to_scorecard_traceability(results: list[TraceResult],
                              all_req_ids: list[str]) -> dict:
    """Shape req_tracer output for `scorecard.compute_scorecard(traceability=...)`.

    per_tc carries content-match status + whether the written id agrees, so the
    scorecard can compute traceability_completeness, requirement_coverage and
    req_id_mismatch_rate.
    """
    return {
        "per_tc": {
            r.tc_id: {
                "matched": r.traceable,
                "req_id": r.matched_req_id,   # content-matched req (the reliable one)
                "id_agrees": r.id_agrees,
            }
            for r in results
        },
        "all_requirements": list(all_req_ids),
    }


def summarize(results: list[TraceResult]) -> dict:
    total = len(results)
    traceable = sum(1 for r in results if r.traceable)
    id_mismatch = sum(1 for r in results if r.traceable and not r.id_agrees)
    return {
        "total_tcs": total,
        "traceable": traceable,
        "untraceable": total - traceable,
        "content_traceability_rate": (traceable / total) if total else None,
        "id_mismatch_count": id_mismatch,  # content matches but written req_id differs
    }
