"""Content-based traceability: map a TC to its source requirement by TEXT, not ID.

Req IDs in the TC workbook can be renumbered / out of sync with the SWE1
analysis (a confirmed defect on the Player project), so ID-based tracing is
unreliable. This matches each TC's wording against the SWE1 requirement
descriptions via token Jaccard (deterministic, no AI), and flags TCs whose
content does not map to any requirement.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass

from spec_matcher import _tokenize, _jaccard

# Trailing "FEATURE-NNN(-NN)*" core of a req id, namespace-independent.
# e.g. SWE1-DEAL-001-01 -> DEAL-001-01 ; NEWR1L-SWRA-DEAL-001 -> DEAL-001.
_CORE_RE = re.compile(r"[A-Za-z]+-\d+(?:-\d+)*$")


def _core(req_id: str) -> str:
    m = _CORE_RE.search(req_id or "")
    return m.group(0).upper() if m else (req_id or "").upper()


def _ids_agree(a: str, b: str) -> bool:
    """Compare two req ids by normalized core, tolerant of different namespaces
    (project A uses SWE1-DEAL-..., the SWE1 analysis uses NEWR1L-SWRA-DEAL-...)
    and of -NN sub-suffixes (parent vs child req)."""
    if not a or not b:
        return False
    ca, cb = _core(a), _core(b)
    return ca == cb or ca.startswith(cb) or cb.startswith(ca)

# Below this Jaccard score a TC is considered NOT traceable to any requirement.
DEFAULT_THRESHOLD = 0.08
# The content match must beat the TC's own written-id requirement by at least
# this margin to be a SUSPECT mismatch worth a human/semantic check. Sibling-
# templated requirements (MSC vs DAP Alphajump, Skip Forward vs Back, the "BT
# Device Function - X" family) score almost identically — a tiny margin means
# "ambiguous twin", where the written id is probably fine and token-Jaccard
# simply cannot tell them apart (only a semantic review can). Calibrated on the
# Player set, where genuine suspects sit at margin >= ~0.03 and exact twins at 0.
MISMATCH_MARGIN = 0.03


@dataclass
class TraceResult:
    tc_id: str
    tc_req_id: str            # the (unreliable) req_id written on the TC
    matched_req_id: str | None  # best content match in the SWE1 universe
    matched_title: str
    score: float
    traceable: bool
    id_agrees: bool           # does the TC's own req_id match the content match?
    written_score: float = 0.0   # content score of TC vs its own written-id req
    ambiguous: bool = False      # best match barely beats written id -> sibling twin

    @property
    def confident_mismatch(self) -> bool:
        """A mismatch we trust: content-traceable, the written id does not match
        the content, AND it is not a sibling-twin ambiguity."""
        return self.traceable and not self.id_agrees and not self.ambiguous


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
        tc_tokens = _tokenize(text)
        best, score = match_tc(text, reqs, req_tokens)
        matched_id = best.get("id") if best else None
        tc_req = str(tc.get("req_id", "") or "")

        # Score the TC against its OWN written-id requirement (if it exists).
        written_score = 0.0
        written_found = False
        for req, rt in zip(reqs, req_tokens):
            if _ids_agree(req.get("id", ""), tc_req):
                written_found = True
                written_score = max(written_score, _jaccard(tc_tokens, rt))

        id_agrees = _ids_agree(matched_id, tc_req)
        # Ambiguous = the written id req exists and scores almost as well as the
        # best match -> sibling-templated twin, the content can't separate them.
        ambiguous = (not id_agrees and written_found
                     and (score - written_score) < MISMATCH_MARGIN)

        out.append(TraceResult(
            tc_id=str(tc.get("tc_id", "") or ""),
            tc_req_id=tc_req,
            matched_req_id=matched_id,
            matched_title=best.get("title", "") if best else "",
            score=round(score, 3),
            traceable=score >= threshold,
            id_agrees=id_agrees,
            written_score=round(written_score, 3),
            ambiguous=ambiguous,
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
                # Treat sibling-twin ambiguity as "agrees" so it isn't counted as
                # a req_id mismatch in the scorecard.
                "id_agrees": r.id_agrees or r.ambiguous,
            }
            for r in results
        },
        "all_requirements": list(all_req_ids),
    }


def summarize(results: list[TraceResult]) -> dict:
    total = len(results)
    traceable = sum(1 for r in results if r.traceable)
    confident = sum(1 for r in results if r.confident_mismatch)
    ambiguous = sum(1 for r in results if r.ambiguous)
    return {
        "total_tcs": total,
        "traceable": traceable,
        "untraceable": total - traceable,
        "content_traceability_rate": (traceable / total) if total else None,
        "id_mismatch_count": confident,    # confident mismatches only (twins excluded)
        "ambiguous_twin_count": ambiguous,  # sibling-templated; written id likely fine
    }
