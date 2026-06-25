"""Prompt builder for TC review (ASPICE_SWE6_AI_Review.md §9).

Mirrors `prompt_builder.py`'s shape but produces prompts that AUDIT existing
TCs instead of generating new ones. The Review spec is loaded once at import
time and embedded into the system prompt, exactly like the generate side
loads `ASPICE_SWE6_AI_Instruction.md`.

The engine (`review_engine.py`) calls `build_review_prompt(tcs_batch, rules)`
to assemble OpenAI chat messages. Only the rules with `requires_llm: true` go
through this builder; regex-only rules are evaluated directly in the engine
without an LLM round-trip.
"""
from __future__ import annotations

import json
from pathlib import Path


_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
_REVIEW_SPEC_PATH = _DOCS_DIR / "ASPICE_SWE6_AI_Review.md"


def _load_review_spec() -> str:
    """Read the auto-loaded Review spec; fall back to a minimal stub."""
    try:
        text = _REVIEW_SPEC_PATH.read_text(encoding="utf-8").strip()
        if text:
            return text
    except OSError:
        pass
    return (
        "ASPICE SWE.6 Review (fallback): produce findings per Tier 1 (§6.x) / "
        "Tier 2 (§7.x) / Tier 3 (§8.x). Output schema follows §9."
    )


REVIEW_SPEC_TEXT = _load_review_spec()


_SYSTEM_BASE = (
    "You are an ASPICE SWE.6 test case REVIEWER. You audit existing TCs against "
    "the Review spec loaded above. You do NOT rewrite TCs, you do NOT generate "
    "new TCs — you flag issues, cite the rule, and propose a minimal fix. "
    "Return ONLY valid JSON, no markdown fences."
)


_HARD_CONSTRAINTS = """
## REVIEW HARD CONSTRAINTS (non-negotiable)

1. **Findings text language** (`issue` / `reasoning` / `suggestion_note`)
   MUST be Traditional Chinese (繁體中文). This is so the Taiwanese reviewer
   can audit findings in their native language.
2. **Rewrites** (`original` / `revised`) MUST match the source field's
   language. Chinese TC → Chinese rewrite; English TC → English rewrite.
   Never translate; the reviewer pastes `revised` back into the workbook.
3. **Severity ceilings are FIXED**:
     - Tier 1 (§6.x): max Critical
     - Tier 2 (§7.x): max Critical
     - Tier 3 (§8.x): **max Major** (never Critical)
   Any Tier 3 finding emitted with severity `Critical` is a contract
   violation. Cap at Major.
4. **`tier` MUST match the rule's section**: §6.x → tier 1, §7.x → tier 2,
   §8.x → tier 3. No invented rule refs.
5. **Tier 2 findings MUST include `evidence_req_spec`** — the Req spec句
   used as the comparison anchor. Tier 3 findings MUST OMIT
   `evidence_req_spec`.
6. **`evidence` MUST be an exact substring quote from the source field** —
   no paraphrase, no translation.
7. **Mutual exclusion**: never emit BOTH §7.4 and §8.3.6 on the same
   numeric value. If the Req group is `tier1_skipped`, only §8.3.6 may
   fire; otherwise only §7.4 may fire.
8. **No fabricated rule refs**: every `rule_ref` must cite an actual
   section from the Review spec (§6.1–§6.7, §7.1–§7.5, §8.1.1–§8.5.3).
9. **Schema completeness**: emit only the fields the spec defines for
   each finding kind. Do not invent fields like `confidence` or `category`.
10. **No emoji** anywhere in the output.
"""


def build_review_system_prompt() -> str:
    """Build the system prompt: Review spec + hard constraints + role."""
    return (
        f"## ASPICE SWE.6 Review Spec (authoritative)\n\n"
        f"{REVIEW_SPEC_TEXT}\n\n"
        f"{_HARD_CONSTRAINTS}\n\n---\n\n"
        f"{_SYSTEM_BASE}"
    )


# Mapping each LLM-required rule to the JSON shape of its expected per-rule
# evaluation. The engine uses this list to tell the model which rules to
# evaluate against THIS batch (§7.1, §7.2, §7.3, etc.).
LLM_RULE_HINTS: dict[str, dict] = {
    "§6.1": {"tier": 1, "field": "req_group",
             "checks": "Missing supported/negative pair when Req spec句 has binary phrasing."},
    "§6.3": {"tier": 1, "field": "req_group",
             "checks": "Missing enumeration coverage — Req lists items A/B/C, TCs cover only subset."},
    "§7.1": {"tier": 2, "field": "test_item",
             "checks": "Test Item outcome not in Req spec句."},
    "§7.2": {"tier": 2, "field": "expected_result",
             "checks": "ER misses Req's stated outcome elements (Major; Critical if NONE covered)."},
    "§7.3": {"tier": 2, "field": "pre_conditions",
             "checks": "Pre-Cond duplicates the Req trigger (states it as already-true)."},
    "§8.2.4": {"tier": 3, "field": "pre_conditions",
               "checks": "Feature-under-test stated as ready in Pre-Cond (circular)."},
    "§8.4.2": {"tier": 3, "field": "expected_result",
               "checks": "Step↔ER count mismatch — alignment 1:1 fails."},
    "§8.5.3": {"tier": 3, "field": "design_method",
               "checks": "Design Method inconsistent with Procedure shape (e.g. BVA but no boundary)."},
    # Stage 6 enhancement — semantic reality-gap / executability (domain-grounded).
    "§7.6": {"tier": 2, "field": "test_procedure",
             "checks": "Reality gap vs spec/domain: (a) a step/ER assumes behaviour "
                       "the spec/domain does NOT define; (b) ER does not map to a "
                       "concrete spec-defined outcome; (c) the TC misses a spec-defined "
                       "branch/enumeration value; or (d) a step is not executable "
                       "(actor unclear, missing precondition, no observable result). "
                       "Use the Domain Pack as ground truth; cite the spec/domain line. "
                       "Mark these findings with \"reality_gap\": true."},
}


def build_review_user_prompt(
    tcs_batch: list[dict],
    rule_ids: list[str],
    req_spec_index: dict[str, str] | None = None,
    domain_block: str | None = None,
) -> str:
    """Build the user prompt for one LLM evaluation batch.

    Args:
        tcs_batch: TCs to evaluate, each dict carries the parsed fields
            (req_id, tc_id, row_num, test_item, pre_conditions,
            test_procedure, expected_result, spec_reference, priority,
            design_method) plus optional `req_spec_sentence` (resolved
            during Tier 1).
        rule_ids: subset of `LLM_RULE_HINTS` keys this batch should evaluate.
        req_spec_index: optional Req-ID → spec句 lookup (for multi-Req-ID
            scenarios where the engine pre-resolved the segment).

    Returns:
        User-message body string ready for `_chat(system, user, ...)`.
    """
    rules_listing_lines = []
    for rid in rule_ids:
        hint = LLM_RULE_HINTS.get(rid)
        if hint is None:
            continue
        rules_listing_lines.append(
            f"- **{rid}** (tier {hint['tier']}, field `{hint['field']}`): "
            f"{hint['checks']}"
        )
    rules_listing = "\n".join(rules_listing_lines) or "(no rules requested)"

    # 將每個 TC 序列化為 JSON，避免換行與 quote 混淆 prompt 結構
    tc_payloads = []
    for tc in tcs_batch:
        tc_payloads.append({
            "row_num": tc.get("row_num"),
            "tc_id": tc.get("tc_id"),
            "req_id": tc.get("req_id"),
            "test_item": tc.get("test_item", ""),
            "pre_conditions": tc.get("pre_conditions", ""),
            "input_test_data": tc.get("input_test_data", ""),
            "test_procedure": tc.get("test_procedure", ""),
            "expected_result": tc.get("expected_result", ""),
            "spec_reference": tc.get("spec_reference", ""),
            "priority": tc.get("priority", ""),
            "design_method": tc.get("design_method", ""),
            "req_spec_sentence": tc.get("req_spec_sentence"),
            "tier1_skipped": bool(tc.get("tier1_skipped", False)),
        })
    tc_json = json.dumps(tc_payloads, ensure_ascii=False, indent=2)

    spec_index_block = ""
    if req_spec_index:
        spec_index_block = (
            "\n## Req Spec Index (resolved during Tier 1)\n"
            f"{json.dumps(req_spec_index, ensure_ascii=False, indent=2)}\n"
        )

    domain_pack_block = ""
    if domain_block:
        domain_pack_block = (
            "\n## Domain Pack (GROUND TRUTH — audit TCs against this, "
            "cite it as evidence, do NOT invent behaviour beyond it)\n"
            f"{domain_block}\n"
        )

    return f"""## Task
Evaluate the following TCs against the listed rules ONLY. For every match,
emit a finding per the §9 schema. For any TC where the rule does NOT match,
emit nothing for that rule (do not emit "no issue" placeholders).
You are an INDEPENDENT auditor: judge only from the TC text + Req spec句 +
Domain Pack below; do not assume intent that is not written.
{domain_pack_block}

## Rules to evaluate in this batch
{rules_listing}
{spec_index_block}
## TCs (JSON)
{tc_json}

## Output (JSON only — no markdown fences)
Return a single object:

{{
  "per_req_findings": [
    {{
      "req_id": "<Req ID>",
      "tier": 1,
      "rule_ref": "§6.x",
      "severity": "Critical|Major",
      "scope_tcs": ["<TC ID>", ...],
      "issue": "<繁體中文一句話說明問題>",
      "evidence_req_spec": "<Req spec句 verbatim>",
      "suggestion_note": "<繁體中文修正建議>",
      "stub": {{ /* §6.1/§6.2/§6.3 only */ }}
    }}
  ],
  "per_tc_findings": [
    {{
      "tc_id": "<TC ID>",
      "row": <row_num>,
      "findings": [
        {{
          "tier": 2,
          "field": "<field key>",
          "step_index": <int or null>,
          "rule_ref": "§7.x",
          "severity": "Critical|Major",
          "issue": "<繁體中文>",
          "evidence": "<exact quote from source>",
          "evidence_req_spec": "<Req spec句; tier 2 only>",
          "original": "<source verbatim>",
          "revised": "<rewrite in source language>",
          "suggestion_note": "<繁體中文>",
          "reality_gap": true
        }}
      ]
    }}
  ]
}}

For §7.6 findings ONLY: set `"reality_gap": true` and make `evidence_req_spec`
quote the spec/Domain-Pack line the TC contradicts or omits. Other rules omit
the `reality_gap` key.

Self-check before emitting (per §10 of the spec):
1. `tier` matches the rule's section (§6→1, §7→2, §8→3).
2. `severity` ≤ tier ceiling (tier 3 ≤ Major).
3. Tier 2 findings have `evidence_req_spec`; tier 3 findings omit it.
4. `evidence` is an exact substring quote.
5. `revised` is in the same language as `original`.
6. No mutual-exclusion violations: §7.4 and §8.3.6 never both fire on the
   same numeric value. (If a TC is `tier1_skipped`, only §8.3.6 may fire.)
7. Rule refs cite real sections only.

If a rule does not apply to a given TC, emit nothing for that pairing —
do not pad the response."""
