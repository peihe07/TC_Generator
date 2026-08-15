#!/usr/bin/env python3
"""Comfort lint gate over generated/*.json — PASS/FAIL with measured values.

Written for Comfort, not copied from Privacy: Privacy's gate resolves
`specification_reference` against CFTS022 artifact ids, which Comfort does
not have. Comfort's authority is the SR24 outline set, so the reference gate
resolves against `data/layer3_map.tsv` — the 129 sections actually cited.

Authorities are READ, never hard-coded:
  design-method vocabulary  <- the workbook's own 下拉選單 sheet
  Test Group / tc_id format <- feature.yaml
  valid outlines            <- data/layer3_map.tsv
  clause text (token check) <- data/section_fulltext.tsv

Rulings encoded as gates rather than left to discipline:
  R-C1   spec_reference stem is the SR24 filename, never SR25
  R-C7   tc_id matches the frozen format and is unique and gap-free
  R-C22  ER carries no fabricated magnitude for a clause that gives none
  §3.4   `(-, +)` verbatim only in test_item / quoted fragments; procedure
         and non-quoting ER use "-" / "+"
  §3.2   every pre_condition line carries a source class
  §11    no trailing period on the four long fields; UI labels use "..."
  §4.6   axis="none" <=> duplicate_of is set

Exit 0 = clean, 1 = at least one finding.

Usage:
    python3 features/comfort/scripts/lint_tcs.py
"""

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

import openpyxl
import yaml

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
GEN = FEATURE / "generated"
LAYER3 = FEATURE / "data" / "layer3_map.tsv"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"

STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
LONG_FIELDS = ["pre_conditions", "input_test_data", "test_procedure",
               "expected_result"]
SOURCE_CLASSES = ("spec-verbatim", "spec-derived", "test-setup")
PRIORITIES = {"P0", "P1", "P2", "P3"}
MODALS = re.compile(r"\b(shall|must|should|will|would)\b", re.I)
# §10.1 — every TC object must carry all ten keys.
REQUIRED_KEYS = ("tc_title", "pre_conditions", "input_test_data",
                 "test_procedure", "expected_result", "specification_reference",
                 "design_method", "priority", "split_flag", "split_reason")
MIN_STEPS = 2                  # §10.5
BLOCKED_MARKERS = ("[BLOCKED-SPEC]",)   # profile §5.1 / R-C24
REASONING_SENTENCES = (2, 5)   # §10.4
# Chinese full stops are not followed by a space, so a lookahead for
# whitespace counts a whole paragraph as one sentence — which is how this
# gate first reported "1 sentence" for seven multi-sentence reasonings.
SENT_END = re.compile(r"[。！？]|[.!?](?=\s|$)")
# A magnitude that a clause without numbers cannot justify. Deliberately not
# a blanket digit ban: step numbering ("1.") and quoted spec values are legal.
FABRICATED_QTY = re.compile(r"\b\d+\s*(mm|cm|%|percent|seconds?|secs?|ms|"
                            r"levels?|steps?|degrees?)\b", re.I)


def load_authorities() -> dict:
    cfg = yaml.safe_load((FEATURE / "feature.yaml").read_text("utf-8"))
    wb_path = sorted(FEATURE.glob(cfg["paths"]["workbook"]))[0]
    wb = openpyxl.load_workbook(wb_path, read_only=True, data_only=True)
    vocab = [str(c).strip() for r in wb["下拉選單"].iter_rows(values_only=True)
             for c in r if c and str(c).strip()]
    wb.close()
    outlines = {r["outline"] for r in
                csv.DictReader(LAYER3.open(encoding="utf-8"), delimiter="\t")}
    clauses = {r["outline"]: r["full_text"].replace("\\n", "\n") for r in
               csv.DictReader(FULLTEXT.open(encoding="utf-8"), delimiter="\t")}
    return {"vocab": vocab, "outlines": outlines, "clauses": clauses,
            "test_group": cfg["test_group"],
            "tc_id_re": re.compile(r"^NR1L-ComfortHMI-\d{3}$")}


def lint(docs: list, auth: dict) -> list[tuple[str, str, str]]:
    """-> [(severity, gate, message)]"""
    out = []

    def bad(gate, msg):
        out.append(("FAIL", gate, msg))

    all_tcs = [(d, tc) for d in docs for tc in d["tcs"]]

    # R-C24: a BLOCKED row is exempt from the two gates that assume a
    # procedure exists. The exemption is REPORTED as its own line, never a
    # silent skip inside a condition — the precedent being the
    # `and n != "Comfort Widget"` that once hid a real naming defect behind a
    # green check (upstream 06 §2.1).
    blocked = [tc["tc_id"] for _, tc in all_tcs
               if any(m in tc.get("remarks", "") for m in BLOCKED_MARKERS)]

    # ---- id gates -------------------------------------------------------
    ids = [tc["tc_id"] for _, tc in all_tcs]
    for tid in ids:
        if not auth["tc_id_re"].match(tid):
            bad("tc-id-format", f"{tid!r} does not match NR1L-ComfortHMI-NNN (R-C7)")
    dup = [i for i, n in Counter(ids).items() if n > 1]
    if dup:
        bad("tc-id-unique", f"duplicate tc_ids {dup}")
    nums = sorted(int(i.rsplit("-", 1)[1]) for i in ids)
    if nums != list(range(1, len(nums) + 1)):
        bad("tc-id-sequence", f"tc_id numbers are not 1..{len(nums)} gap-free: {nums}")
    rids = [tc["req_id"] for _, tc in all_tcs]
    rdup = [i for i, n in Counter(rids).items() if n > 1]
    if rdup:
        bad("req-id-unique", f"duplicate req_ids {rdup}")

    for d, tc in all_tcs:
        w = tc["tc_id"]
        clause = auth["clauses"].get(d["outline"], "")

        # ---- §10.1 required keys ----------------------------------------
        missing = [k for k in REQUIRED_KEYS if k not in tc]
        if missing:
            bad("required-keys", f"{w}: missing §10.1 key(s) {missing}")

        # ---- §10.5 minimum two numbered procedure steps ------------------
        # proc-er-1to1 does NOT cover this: a single step against a single ER
        # line is 1:1 and passes. That is how TC-004 reached "25/25 PASS"
        # with a one-step procedure (handoff 20 §1.1).
        steps = len(re.findall(r"^\s*\d+\.", tc["test_procedure"], re.M))
        if w in blocked:
            # A BLOCKED row must be EMPTY, not merely short — a stray step
            # would mean the row is half-written rather than blocked.
            if tc["test_procedure"] or tc["expected_result"]:
                bad("blocked-row-empty",
                    f"{w}: carries a {BLOCKED_MARKERS[0]} marker but "
                    "test_procedure/expected_result are not empty (R-C24)")
        elif steps < MIN_STEPS:
            bad("proc-min-steps",
                f"{w}: {steps} numbered step(s), §10.5 requires >= {MIN_STEPS} "
                "(Setup -> Verification)")

        # ---- spec reference (R-C1) --------------------------------------
        ref = tc["specification_reference"]
        if not ref.startswith(STEM + "_"):
            bad("spec-ref-stem", f"{w}: stem is not the ruled SR24 filename (R-C1)")
        outline = ref[len(STEM) + 1:]
        if outline not in auth["outlines"]:
            bad("spec-ref-outline", f"{w}: {outline!r} is not one of the 129 cited sections")
        if "SR25" in ref:
            bad("spec-ref-sr25", f"{w}: reference names SR25 (R-C1 forbids)")

        # ---- fixed columns ----------------------------------------------
        if tc["test_group"] != auth["test_group"]:
            bad("test-group", f"{w}: test_group {tc['test_group']!r} != feature.yaml")
        if tc["design_method"] not in auth["vocab"]:
            bad("design-method", f"{w}: {tc['design_method']!r} not in 下拉選單 vocabulary")
        if tc["priority"] not in PRIORITIES:
            bad("priority", f"{w}: {tc['priority']!r} not in {sorted(PRIORITIES)}")
        if tc["functional_safety"] != "NA":
            bad("functional-safety", f"{w}: S column must be 'NA' (profile §3.8)")
        if tc["estimated_test_time"] != "":
            bad("estimated-time", f"{w}: Q column must be blank (profile §3.7)")
        if w in blocked:
            if not tc["remarks"].startswith(BLOCKED_MARKERS[0]):
                bad("blocked-remarks", f"{w}: {BLOCKED_MARKERS[0]} must be the "
                                       "leading token of Remarks (R-C24)")
            if re.search(r"\bA-CF\d+\b|\bR-C\d+\b|§\d", tc["remarks"]):
                bad("blocked-remarks", f"{w}: Remarks is externally visible and "
                                       "must not carry an internal ruling id "
                                       "(AMFM R10-4)")
        elif tc["remarks"] != "":
            bad("remarks", f"{w}: remarks must be empty for a non-BLOCKED row")

        # ---- §11 formatting ---------------------------------------------
        for f in LONG_FIELDS:
            for ln in tc[f].split("\n"):
                if ln.rstrip().endswith("."):
                    bad("trailing-period", f"{w}.{f}: line ends with a period — {ln[:48]!r}")
            if re.search(r"\[[A-Za-z][^\]]*\]", tc[f]) and f != "pre_conditions":
                bad("ui-bracket", f"{w}.{f}: square-bracket label; use \"...\" (§11)")

        # ---- tc_title (§4.3) --------------------------------------------
        words = tc["tc_title"].split()
        if not 2 <= len(words) <= 14:
            bad("title-length", f"{w}: tc_title is {len(words)} words, need 2–14")
        if MODALS.search(tc["tc_title"]):
            bad("title-modal", f"{w}: tc_title contains a modal (§4.3)")

        # ---- test_item is the ONLY field allowed a modal (profile §3.1) --
        if not MODALS.search(tc["test_item"]):
            bad("item-modal", f"{w}: test_item carries no modal (profile §3.1)")
        if MODALS.search(tc["expected_result"]):
            bad("er-modal", f"{w}: expected_result contains a modal (§6)")

        # ---- pre_conditions source class (profile §3.2) ------------------
        for ln in [l for l in tc["pre_conditions"].split("\n") if l.strip()]:
            if not any(f"[{c}]" in ln for c in SOURCE_CLASSES):
                bad("source-class", f"{w}: pre_condition without source class — {ln[:52]!r}")

        # ---- procedure <-> ER 1:1 (§6) ----------------------------------
        np_ = len(re.findall(r"^\s*\d+\.", tc["test_procedure"], re.M))
        ne = len(re.findall(r"^\s*\d+\.", tc["expected_result"], re.M))
        if w in blocked:
            pass                      # exempt; reported on its own line
        elif np_ != ne or np_ == 0:
            bad("proc-er-1to1", f"{w}: {np_} procedure steps vs {ne} ER lines")

        # ---- §3.4 (-, +) placement (19 §3) -------------------------------
        if "(-, +)" in tc["test_procedure"]:
            bad("token-placement", f"{w}: '(-, +)' in test_procedure; use \"-\" / \"+\" (§3.4)")
        if "(-, +)" in tc["test_item"] and "(-, +)" not in clause:
            bad("token-source", f"{w}: '(-, +)' in test_item but absent from clause {d['outline']}")

        # ---- R-C22: no fabricated magnitude where the clause gives none --
        clause_has_num = bool(re.search(r"\d", clause))
        m = FABRICATED_QTY.search(tc["expected_result"])
        if m and not clause_has_num:
            bad("fabricated-qty", f"{w}: ER states {m.group(0)!r} but clause has no number (R-C22/§8.4.1)")

    # ---- §10.4 reasoning length / §10.6 duplicate_of encoding ------------
    for d in docs:
        n = len(SENT_END.findall(d.get("reasoning", "")))
        lo, hi = REASONING_SENTENCES
        if not lo <= n <= hi:
            bad("reasoning-sentences",
                f"{d['parent']}: reasoning has {n} sentence(s), §10.4 requires {lo}-{hi}")
        dup = d.get("duplicate_of", "")
        if dup and not re.fullmatch(r"\d+", dup):
            bad("duplicate-of-format",
                f"{d['parent']}: duplicate_of {dup!r} is not a digits-only row "
                "number (§10.6)")

    # ---- §4.6 sibling bookkeeping ---------------------------------------
    for d in docs:
        axis = d["distinguishing_axis"]["axis"]
        dup_of = d["duplicate_of"]
        if (axis == "none") != bool(dup_of):
            bad("sibling-axis", f"{d['parent']}: axis={axis!r} but duplicate_of={dup_of!r} "
                                "(§4.6 requires axis='none' <=> duplicate_of set)")
    return out, blocked


def main() -> int:
    auth = load_authorities()
    docs = [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(GEN.glob("*.json"))]
    n_tc = sum(len(d["tcs"]) for d in docs)
    findings, blocked_ids = lint(docs, auth)

    gates = ["tc-id-format", "tc-id-unique", "tc-id-sequence", "req-id-unique",
             "spec-ref-stem", "spec-ref-outline", "spec-ref-sr25", "test-group",
             "design-method", "priority", "functional-safety", "estimated-time",
             "remarks", "trailing-period", "ui-bracket", "title-length",
             "title-modal", "item-modal", "er-modal", "source-class",
             "proc-er-1to1", "token-placement", "token-source",
             "fabricated-qty", "sibling-axis",
             # added 2026-08-15 after handoff 20 §1.1's coverage audit
             "required-keys", "proc-min-steps", "reasoning-sentences",
             "duplicate-of-format",
             # added 2026-08-15 with R-C24's BLOCKED-SPEC marker
             "blocked-row-empty", "blocked-remarks"]
    failed = {g for _, g, _ in findings}

    print(f"files: {len(docs)}   TCs: {n_tc}   "
          f"vocabulary: {len(auth['vocab'])} strings   "
          f"valid outlines: {len(auth['outlines'])}\n")
    print("gates:")
    for g in gates:
        print(f"- {'**FAIL**' if g in failed else 'PASS'} — {g}")
    # R-C24 — the exemption is visible on every run, whether or not it fired.
    print(f"- PASS — rows exempted as BLOCKED-SPEC "
          f"(proc-min-steps, proc-er-1to1): {blocked_ids or 'none'}")
    if findings:
        print(f"\n{len(findings)} finding(s):")
        for sev, g, msg in findings:
            print(f"  [{sev}] {g}: {msg}")
    print(f"\n{len(gates) - len(failed)} / {len(gates)} gates PASS; "
          f"{len(findings)} finding(s) across {n_tc} TCs")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
