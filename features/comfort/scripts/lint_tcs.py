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
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

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
# profile §5.1 / §5.2 — R-C24's [BLOCKED-SPEC] and R-C38's [BLOCKED-NON-HMI].
# Both produce an empty row; they differ in WHY, and the Remarks gate below
# is what keeps them from collapsing into one another.
BLOCKED_MARKERS = ("[BLOCKED-SPEC]", "[BLOCKED-NON-HMI]")
# R-C26 — a marker that grants a lint exemption must not be self-issuable.
# The whitelist is the named list in profile §5.1/§5.2; adding to it is a
# ruling, not an edit. Without this, a BLOCKED marker is an exemption anyone
# can take by typing it, which is the same as having no exemption condition
# at all.
MARKER_WHITELIST = {"[BLOCKED-SPEC]": {"NR1L-ComfortHMI-010",
                                       "NR1L-ComfortHMI-012"},
                    # 41 §1.2 — ruled together with R-C38 itself.
                    "[BLOCKED-NON-HMI]": {"NR1L-ComfortHMI-081"}}
OWNER_WINDOW = 60          # R-C27 — chars visible on the clipped first line
# R-C38 — [BLOCKED-NON-HMI]'s first visible line must say what is missing,
# and must NOT name an owner: having no owner IS the classification. An
# "Owner:" here would be a [BLOCKED-SPEC] wearing the wrong marker.
NON_HMI_PHRASE = "Not an HMI-observable property"
# handoff 26 §4.1 — keys a TC object may carry WITHOUT landing in a column.
# `COLS` in write_back.py is a hand-kept list; if it loses an entry, nothing
# shouts. This gate makes the silence audible: every TC key must either map to
# a column or be named here. Adding to this list is a ruling, not an edit
# (same reason as MARKER_WHITELIST — a self-issuable whitelist is no whitelist).
# Extended to the doc level per 29 §5.1: four of the original eight entries
# (reasoning, keywords, duplicate_of, distinguishing_axis) live on the doc
# object, not the TC object, so naming them while scanning only TCs named
# nothing — they were never in the scanned layer.
NOT_IN_WORKBOOK = {
    "tc_title",             # canon §4.3 — derivation input, never a column
    "estimated_test_time",  # no column in revision C
    "split_flag", "split_reason",
    "reasoning", "keywords", "duplicate_of", "distinguishing_axis",
    # doc-level structural keys (29 §5.1)
    "assumptions", "batch", "outline", "parent", "source_clause", "tcs",
    "interface_axis_review",          # 36 §6 — R-C34's duty, recorded
    "emea_ics_review",                # 38 §1 — R-C36-1's per-TC answer
}
# 36 §6 — the four interface-type axes must each carry a non-empty answer.
# Correctness cannot be machine-checked; having been asked can.
IFACE_KEYS = ("observable_interface", "axis_9", "axis_12", "axis_13",
              "emea_ics")
# 36 §4 — a sibling whose counterpart section is not generated yet leaves
# duplicate_of empty. Legal while the counterpart is missing, a defect the
# day it lands. The table turns "remember to backfill" into a condition.
# Read from data/pending_sibling.tsv so the gate and the candidate generator
# share one table (37 §6). Only `sibling` verdicts are watched.
def _load_sibling_table() -> list:
    path = FEATURE / "data" / "pending_sibling.tsv"
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


SIBLING_TABLE = _load_sibling_table()
PENDING_SIBLING = [(r["outline"], r["sibling_outline"])
                   for r in SIBLING_TABLE if r["verdict"] == "sibling"]
# 42 §1 — a `provisional` verdict was reached against a section that had no
# TCs. The day that section's Test Set is complete, the verdict must be
# looked at again and the flag cleared by hand. Re-confirmation MAY keep the
# verdict; what it may not do is stay silent.
TEST_SET_MAP = FEATURE / "data" / "test_set_map.tsv"


def _load_test_sets() -> dict:
    with TEST_SET_MAP.open(encoding="utf-8") as fh:
        return {r["outline"]: r["test_set"]
                for r in csv.DictReader(fh, delimiter="\t")}


SECTION_TEST_SET = _load_test_sets()
ANOMALY_ID = re.compile(r"\bA-CF\d+\b")
PROFILE = ROOT / "docs" / "runtime" / "profiles" / "FW036_R1L_Comfort_Profile.md"
# 35 §4 — a negated pre_condition ("the vehicle does NOT have X") covers
# whatever values the axis happens to have today, and axes gain values. The
# profile records the limit; this gate is the mechanism, because a record is
# not a mechanism. Adding a value without re-reviewing the negation users
# fails, and the failure names them.
AXIS_BLOCK = re.compile(r"```axis-values\n(.*?)```", re.S)
# 52 §3, criterion corrected by 54 §1 — `axis-type-reverse-test`.
#
# 52 §3 worded the question as "is there a TC whose FUNCTION is governed by
# this axis, and whose observable sits on the interface the axis removes?"
# The purpose it was given (35 §1.1) is the opposite case: "an interface-type
# axis matters because the function survives while ANOTHER TC's observable
# disappears". The wording is the narrower of the two, and 54 §1 rules the
# PURPOSE version to be the FAIL criterion:
#
#   FAIL  — any TC whose observable sits on an interface some axis value
#           removes, and which does not state that axis's value.
#   report— of those, how many also have an axis-governed function (the
#           wording version). Kept as a named line, not deleted: if the two
#           ever diverge again, the difference is the finding.
#
# Criteria are READ FROM THE PROFILE, never hard-coded (52 §3).
FN_AXIS_BLOCK = re.compile(r"```function-axis-reverse-test\n(.*?)```", re.S)
# 56 §4 — the fields that MAKE UP the declaration. `declared-at-tc-count`
# and `judged-at` are excluded on purpose: they record when, not what.
HASHED_FIELDS = ("axis", "function-keywords", "removed-interface-keywords",
                 "axis-pc-keywords", "judged-at-tc-count",
                 "judged-at-provenance")
# The profile's axis table, used only to catch a 功能型 axis with NO block —
# an omission is otherwise silent, which is the failure this gate exists for.
AXIS_TABLE_ROW = re.compile(
    r"^\|\s*([0-9]+|—)\s*\|\s*(.+?)\s*\|\s*\*{0,2}(功能型|介面型)\*{0,2}\s*\|",
    re.M)
# 43 §4 — one block per axis that uses a negated pre_condition, each carrying
# its own `negation:` string. Until 43 §4 this gate watched ONE hard-coded
# phrase (axis 13's), so the other four negations had no protection: 34 §4's
# reason is about what a negation covers, and that does not depend on which
# axis is negated.
# 60 §1 — module level so verify_no_tcid_gate.py reads THESE objects
# rather than a re-typed copy (the lesson from verify_provisional_gate).
TCID_LONG = re.compile(r"NR1L-ComfortHMI-\d+")
TCID_SHORT = re.compile(r"`-\d{3}`")

NEGATED_PC = re.compile(r"\bdoes not\b|\bis not\b|\bnot configured\b"
                        r"|\bnot present\b|\bnot currently\b")
# Negated pre_conditions that are NOT configuration axes: runtime state and
# test setup. Naming them is what lets the coverage check below FAIL on a NEW
# axis negation instead of quietly ignoring it (same shape as NOT_IN_WORKBOOK
# — a list nobody has to maintain is a list that protects nothing).
NON_AXIS_NEGATIONS = {
    "The lower screen is not in the stowed position":
        "13.2 之執行期狀態（同一台車兩種狀態），非配置軸",
    "The user is not in the climate section on the main head unit":
        "13.2 之執行期畫面位置，非配置軸",
    "The Seats tab is not currently shown":
        "test-setup 之起始狀態，非配置軸",
}
# §5.1's nine forbidden MAIN verbs, verbatim and nothing else.
# Authority: canon §5.1, via handoff 31 §1.
#
# `locate` was in this list for one batch and is now OUT (32 §2): canon §5.6
# uses it in a POSITIVE example — "Locate the phone and record its A2DP and
# HFP status shown in the list". It is a positioning action and defers no
# judgement to the tester, so the gate had mechanically forbidden a wording
# the canon recommends.
#
# Rule this cost us: an entry with no cited authority does not go in the
# list. A habit from hand-checking swayed one judgement; inside a gate it
# would have swayed every batch after it.
# Listed one-for-one against §5.1 so the two can be diffed by eye — nine
# entries, nine in the canon. `observe whether` is subsumed by `observe` as
# a matcher, but a list that silently carries eight where the canon says
# nine cannot be checked against its own authority.
FORBIDDEN_VERBS = ("observe whether", "observe", "see if", "check whether",
                   "confirm whether", "verify", "watch", "monitor", "inspect")
# Anchored at the step's own start — "1." then optional whitespace then the
# verb. §5.1 explicitly ALLOWS `verify` inside a purpose clause
# ("... to verify that ..."), so a substring test would fail legal usage, and
# a gate that fails legal usage teaches authors to route around it rather
# than to fix anything (31 §1).
# Longest-first, so the reported verb is the fullest phrase that matched
# ("check whether", not "check") rather than whichever came first in the list.
STEP_HEAD = re.compile(
    r"^\s*\d+\.\s*("
    + "|".join(sorted(FORBIDDEN_VERBS, key=len, reverse=True))
    + r")\b", re.I | re.M)
# A SAFETY NET, NOT THE CRITERION (31 §2). The criterion is §6 — the ER's
# subject must be something the system does — and it stays human-reviewed.
# rev1 shipped `is readable` and rev2 shipped `is recorded`: the same error
# changed words and survived, which is exactly why a word list cannot be
# promoted to a criterion. §9 item 10 may not cite this gate as its basis.
ER_SUBJECT_NET = ("is recorded", "is readable", "is noted", "can be read")
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


def identical_tc_groups(docs: list) -> list:
    """61 §2 — corpus-wide scan for TCs identical in the three content fields.

    A MEASUREMENT, not a gate. Found by accident in round 61: four pairs had
    been recorded as equivalent while NINE more existed, because equivalence
    had only ever been looked for where a handoff pointed. It does not FAIL —
    037's decomposition granularity is upstream's fact and §8.2.2 forbids
    merging leaves — but it prints, so it cannot be unseen again.
    """
    ident = {}
    for d in docs:
        for tc in d["tcs"]:
            ident.setdefault(
                (tc["test_item"], tc["test_procedure"], tc["expected_result"]),
                []).append((d["outline"], tc["tc_id"], tc["req_id"]))
    return [g for g in ident.values() if len(g) > 1]


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
    # §8.2.2 lets one leaf produce several TCs, so a repeated req_id is legal
    # — but ONLY when every row carrying it declares the split. An accidental
    # duplicate and a declared split look identical in the id column; the
    # split_flag is what tells them apart, so the gate reads it rather than
    # dropping the uniqueness check altogether.
    rids = [tc["req_id"] for _, tc in all_tcs]
    for rid, n in sorted(Counter(rids).items()):
        if n == 1:
            continue
        rows = [tc for _, tc in all_tcs if tc["req_id"] == rid]
        undeclared = [tc["tc_id"] for tc in rows if not tc.get("split_flag")]
        if undeclared:
            bad("req-id-unique",
                f"req_id {rid!r} appears on {n} TCs but {undeclared} do not "
                "set split_flag — a split must be declared on every row it "
                "produces (§8.2.2), otherwise this is a duplicate")
        elif not all(tc.get("split_reason") for tc in rows):
            bad("req-id-unique",
                f"req_id {rid!r} is split {n} ways but a row has an empty "
                "split_reason (§10.1)")

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
                    f"{w}: carries a BLOCKED marker but "
                    "test_procedure/expected_result are not empty (R-C24)")
        elif steps < MIN_STEPS:
            bad("proc-min-steps",
                f"{w}: {steps} numbered step(s), §10.5 requires >= {MIN_STEPS} "
                "(Setup -> Verification)")

        # ---- spec reference (R-C1) --------------------------------------
        # R-C29 lets one TC cite several sections — its own, plus any section
        # a cross-section pre_condition draws its fact from (§10.7 "relied on
        # as setup"). Items are "; "-separated and each carries the full stem,
        # so the stem rule stays per-item rather than being checked once and
        # assumed for the rest.
        ref = tc["specification_reference"]
        refs = [r.strip() for r in ref.split(";") if r.strip()]
        if len(refs) != len(set(refs)):
            bad("spec-ref-outline",
                f"{w}: specification_reference repeats a section: {refs}")
        for item in refs:
            if not item.startswith(STEM + "_"):
                bad("spec-ref-stem",
                    f"{w}: stem is not the ruled SR24 filename (R-C1) — {item!r}")
                continue
            outline = item[len(STEM) + 1:]
            if outline not in auth["outlines"]:
                bad("spec-ref-outline",
                    f"{w}: {outline!r} is not one of the 129 cited sections")
        if refs and not refs[0].endswith("_" + d["outline"]):
            # The TC's own section leads; cited-for-setup sections follow.
            bad("spec-ref-outline",
                f"{w}: first specification_reference is not the TC's own "
                f"section {d['outline']!r} (R-C29: own section leads)")
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
        # ---- R-C26 marker whitelist -------------------------------------
        for mk, allowed in MARKER_WHITELIST.items():
            if mk in tc.get("remarks", "") and w not in allowed:
                bad("marker-whitelist",
                    f"{w}: carries {mk} but is not in profile §5.1's named "
                    "whitelist; an exemption-granting marker cannot be "
                    "self-issued (R-C26)")

        if w in blocked:
            mark = next((m for m in BLOCKED_MARKERS
                         if tc["remarks"].startswith(m)), None)
            if mark is None:
                bad("blocked-remarks",
                    f"{w}: one of {list(BLOCKED_MARKERS)} must be the leading "
                    "token of Remarks (R-C24 / R-C38)")
            if re.search(r"\bA-CF\d+\b|\bR-C\d+\b|§\d", tc["remarks"]):
                bad("blocked-remarks", f"{w}: Remarks is externally visible and "
                                       "must not carry an internal ruling id "
                                       "(AMFM R10-4)")
            # R-C27 — the Remarks column clips to one visible line, so what
            # the marker exists to point at must sit inside that line. For
            # [BLOCKED-SPEC] that is the owner; for [BLOCKED-NON-HMI] it is
            # the absence of one, which is why the two checks are opposites
            # rather than one shared check (R-C38: the missing owner is the
            # classification, so a lenient "either is fine" gate would let a
            # delegated leaf hide under the wrong marker).
            head = tc["remarks"][:OWNER_WINDOW]
            if mark == "[BLOCKED-NON-HMI]":
                if NON_HMI_PHRASE not in head:
                    bad("blocked-remarks",
                        f"{w}: {NON_HMI_PHRASE!r} must appear within the first "
                        f"{OWNER_WINDOW} characters of Remarks (R-C38); "
                        f"measured head = {head[:48]!r}")
                if "Owner:" in tc["remarks"]:
                    bad("blocked-remarks",
                        f"{w}: [BLOCKED-NON-HMI] must not name an owner "
                        "(R-C38) — a leaf with an owner is [BLOCKED-SPEC]")
            elif "Owner:" not in head:
                bad("blocked-remarks",
                    f"{w}: 'Owner:' must appear within the first "
                    f"{OWNER_WINDOW} characters of Remarks (R-C27); "
                    f"measured head = {head[:48]!r}")
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

    # ---- §5.1 forbidden main verbs (31 §1) ------------------------------
    for _, tc in all_tcs:
        for m in STEP_HEAD.finditer(tc["test_procedure"]):
            step = tc["test_procedure"][m.start():].split("\n", 1)[0]
            bad("forbidden-verb",
                f"{tc['tc_id']}: step leads with the forbidden main verb "
                f"{m.group(1)!r} (§5.1) — {step[:64]!r}")

    # ---- ER subject safety net (31 §2) ----------------------------------
    for _, tc in all_tcs:
        for phrase in ER_SUBJECT_NET:
            if phrase in tc["expected_result"].lower():
                bad("er-subject-net",
                    f"{tc['tc_id']}: expected_result contains {phrase!r}, "
                    "which puts the observer in the subject position (§6). "
                    "This gate is a net, not the criterion — passing it does "
                    "not mean the ER subjects were checked")

    # ---- 36 §6 — R-C34's generation-time duty was discharged ------------
    for d in docs:
        rev = d.get("interface_axis_review")
        if not isinstance(rev, dict):
            bad("interface-axis-answered",
                f"{d['parent']} ({d['outline']}): no interface_axis_review; "
                "R-C34 requires naming the observable's interface and "
                "answering each interface-type axis")
            continue
        blank = [k for k in IFACE_KEYS if not str(rev.get(k, "")).strip()]
        if blank:
            bad("interface-axis-answered",
                f"{d['parent']} ({d['outline']}): interface_axis_review is "
                f"missing or empty for {blank}")

    # ---- 38 §1 / R-C36-1 — every EMEA exclusion carries a per-TC answer ---
    # The gate fails only on a MISSING answer. A "no" verdict is reported on
    # its own named line instead: removal is a ruling, not something lint may
    # force, and a red build would push the executor into removing it unilaterally.
    emea_no = []
    for _, tc in all_tcs:
        if "not an EMEA ICS" not in tc["pre_conditions"]:
            continue
        rev = tc.get("emea_ics_review")
        if not isinstance(rev, dict) or not str(rev.get("ch16_sentence", "")).strip():
            bad("emea-per-tc-answered",
                f"{tc['tc_id']}: carries the EMEA exclusion but has no "
                "per-TC judgement pointing at a ch16 sentence (R-C36-1); "
                "section-level `mirrored` is not an answer")
        elif rev.get("verdict") != "yes":
            emea_no.append((tc["tc_id"], rev.get("verdict"),
                            rev.get("ch16_outline")))

    # ---- 60 §1 — tc_id may not be used to NAME another row in prose ------
    # This is a PROHIBITION, not a correctness check. A "the cited tc_id
    # exists and matches its description" gate is mechanically possible for
    # the first half and useless (after a shift `-227` still exists, it just
    # points elsewhere) and unmechanisable for the second. R-C7 makes tc_id a
    # generator-assigned, shifting key; req_id is stable. So prose cites
    # req_id, full stop, and this gate needs no semantics to be reliable.
    #
    # TWO patterns, not one. 60 §1 specifies `NR1L-ComfortHMI-\d+` — measured
    # across the corpus that form appears TWICE, while the SHORT form
    # (`-233` in backticks, the house style) appears 132 times and is the
    # form that actually broke in 58 §2. A gate matching only the spelled-out
    # form would have passed on the very corpus that motivated it.
    for d in docs:
        prose = {"reasoning": d.get("reasoning", ""),
                 "distinguishing_axis.axis": d.get(
                     "distinguishing_axis", {}).get("axis", ""),
                 "distinguishing_axis.delta": d.get(
                     "distinguishing_axis", {}).get("delta", ""),
                 "assumptions": " ".join(d.get("assumptions", []) or [])}
        for tc in d["tcs"]:
            prose[f"{tc['tc_id']}.split_reason"] = tc.get("split_reason") or ""
            prose[f"{tc['tc_id']}.remarks"] = tc.get("remarks") or ""
        for field, text in prose.items():
            hits = TCID_LONG.findall(text) + TCID_SHORT.findall(text)
            if hits:
                bad("no-tcid-in-prose",
                    f"{d['outline']} ({field}): cites tc_id {sorted(set(hits))} "
                    f"in prose — profile §3.6 requires req_id, because tc_id "
                    f"moves (R-C7) and a moved citation still parses")

    # ---- 36 §4 — a pending sibling must be resolved once its section lands -
    generated = {d["outline"] for d in docs}
    for outline, sibling in sorted(PENDING_SIBLING):
        doc = next((d for d in docs if d["outline"] == outline), None)
        if doc is None or sibling not in generated:
            continue
        unresolved = [tc["tc_id"] for tc in doc["tcs"]
                      if not doc.get("duplicate_of")
                      and doc["distinguishing_axis"]["axis"] in
                      ("", "see per-TC titles")]
        if unresolved:
            bad("pending-sibling",
                f"{outline}'s sibling {sibling} is now generated, but "
                f"duplicate_of/distinguishing_axis is still unset for "
                f"{unresolved} — §4.6 判定須於對造節生成後回填")

    # ---- 42 §1 / 43 §1 — provisional verdicts owed a second look --------
    # TRIGGER CORRECTED (43 §1). 42 §1 fired when EITHER side's Test Set
    # completed — but `provisional` is caused by ONE side having no TCs, and
    # the side that completes is the side that already had them. The missing
    # evidence stayed missing, so the re-confirmation had nothing new to look
    # at: measured 632 rows due, 0 of them with both sides generated.
    #
    # 43 §1 names the discriminant outright: `provisional == true` AND both
    # sides generated <=> the side that was missing has landed. That is the
    # condition below. It is section-granular rather than Test-Set-granular,
    # so it fires the moment the evidence exists rather than at the coarser
    # set boundary — earlier, never later (上繳 32 §1.2).
    due = [r for r in SIBLING_TABLE
           if r.get("provisional") == "true"
           and r["outline"] in generated
           and r["sibling_outline"] in generated]
    if due:
        shown = ", ".join(f"{r['outline']}<->{r['sibling_outline']}"
                          f"[{r['verdict']}]" for r in due[:8])
        bad("provisional-sibling",
            f"{len(due)} provisional row(s) now have BOTH sides generated — "
            f"the side that was missing when the verdict was reached has "
            f"landed, so the verdict is owed a re-confirmation against TCs "
            f"rather than clauses (43 §1). Re-confirm — the verdict MAY "
            f"stand — then set provisional=false. First 8: {shown}"
            + (f" … and {len(due) - 8} more" if len(due) > 8 else ""))

    # ---- 35 §4 / 43 §4 — every negated axis, not just axis 13 ------------
    blocks = AXIS_BLOCK.findall(PROFILE.read_text(encoding="utf-8"))
    if not blocks:
        bad("axis-value-count",
            "profile carries no ```axis-values``` block; a negated "
            "pre_condition cannot be checked against the axis it negates")
    negations = []
    for raw in blocks:
        f = dict(l.split(":", 1) for l in raw.strip().split("\n")
                 if ":" in l and not l.lstrip().startswith("#"))
        axis = f.get("axis", "?").strip().split()[0]
        values = [v.strip() for v in f.get("values", "").split("|") if v.strip()]
        declared = f.get("value-count", "").strip()
        reviewed = f.get("negation-reviewed-at-value-count", "").strip()
        negation = f.get("negation", "").strip()
        listed = [v.strip() for v in f.get("negation-users", "").split(",")
                  if v.strip()]
        if not negation:
            bad("axis-value-count",
                f"axis {axis}: block carries no `negation:` field, so the "
                "gate cannot find the pre_conditions it protects (43 §4)")
            continue
        negations.append(negation)
        actual = [tc["tc_id"] for _, tc in all_tcs
                  if negation in tc["pre_conditions"]]
        if declared != str(len(values)):
            bad("axis-value-count",
                f"axis {axis}: profile declares value-count {declared!r} but "
                f"lists {len(values)} values {values}")
        elif reviewed != declared:
            bad("axis-value-count",
                f"axis {axis}: gained a value (now {declared}) but the negated "
                f"pre_condition was last reviewed at {reviewed!r}. "
                f"Re-review these {len(actual)} TCs and then bump "
                f"negation-reviewed-at-value-count: {sorted(actual)}")
        if sorted(listed) != sorted(actual):
            bad("axis-value-count",
                f"axis {axis}: negation-users list is stale — "
                f"missing {sorted(set(actual) - set(listed))}, "
                f"extra {sorted(set(listed) - set(actual))}")

    # ---- 52 §3 — axis-type-reverse-test ---------------------------------
    profile_text = PROFILE.read_text(encoding="utf-8")
    declared, live, vacuous, worded_hits = {}, 0, 0, []
    for raw in FN_AXIS_BLOCK.findall(profile_text):
        f = dict(l.split(":", 1) for l in raw.strip().split("\n")
                 if ":" in l and not l.lstrip().startswith("#"))
        axis = f.get("axis", "?").strip().split()[0]
        declared[axis] = f
        # 56 §4 — `declared-at-tc-count` records WHEN this declaration was
        # written, so it may only move when the declaration changes. The
        # content hash is the gate: recompute it, and a mismatch means the
        # block was edited without the timestamp following.
        payload = "\n".join(f"{k}={f.get(k, '').strip()}" for k in HASHED_FIELDS)
        want = hashlib.sha256(payload.encode()).hexdigest()[:12]
        got = f.get("content-sha", "").strip()
        if got != want:
            bad("axis-type-reverse-test",
                f"axis {axis}: content-sha is {got or 'missing'} but the "
                f"block hashes to {want}. The declaration changed without "
                f"`declared-at-tc-count` (currently "
                f"{f.get('declared-at-tc-count', '?').strip()}) following it "
                f"— update both together (56 §4)")

        def terms(key):
            v = f.get(key, "").strip()
            return [] if v in ("", "none") else [t.strip() for t in v.split("|")
                                                 if t.strip()]

        iface, fn = terms("removed-interface-keywords"), terms("function-keywords")
        pcs = terms("axis-pc-keywords")
        if not iface:
            vacuous += 1
            continue
        live += 1
        for _, tc in all_tcs:
            observable = f"{tc['test_procedure']}\n{tc['expected_result']}"
            if not any(t in observable for t in iface):
                continue
            # A TC that already states this axis's value is confined to one of
            # them; its observable cannot vanish unexpectedly.
            if any(t in tc["pre_conditions"] for t in pcs):
                continue
            # PURPOSE version (54 §1) — the function filter is NOT applied
            # here. A TC whose function belongs to some other section is
            # exactly the case this test exists for.
            subject = f"{tc['test_item']}\n{observable}"
            also_worded = bool(fn) and any(t in subject for t in fn)
            worded_hits.append((axis, tc["tc_id"])) if also_worded else None
            bad("axis-type-reverse-test",
                f"axis {axis}: {tc['tc_id']} observes "
                f"{[t for t in iface if t in observable]!r} — the interface "
                f"this axis's value removes — and states no value for that "
                f"axis, so it is false on the value that removes it. Either "
                f"add the axis pre_condition or re-decide the axis's type "
                f"(judged at {f.get('judged-at-tc-count', '?').strip()} TCs; "
                f"54 §1 purpose version)"
                + ("  [also matches the 52 §3 wording version]"
                   if also_worded else ""))
    for num, name, kind in AXIS_TABLE_ROW.findall(profile_text):
        if kind == "功能型" and num not in declared:
            bad("axis-type-reverse-test",
                f"axis {num} ({re.sub(chr(96) + '|[*]', '', name)[:40]}) is "
                "marked 功能型 but has no ```function-axis-reverse-test``` "
                "block, so its classification is never re-checked (52 §3). "
                "Declare it, using `removed-interface-keywords: none` if the "
                "axis removes no interface — an explicit `none` is a claim; "
                "a missing block is silence")
    fn_axis_report = (len(declared), live, vacuous, len(all_tcs),
                      worded_hits)

    # 43 §4 — the part that makes a NEW unprotected negation audible. Without
    # it, adding a negated pre_condition for an axis that has no block is
    # exactly as silent as axis 13's situation was before 34 §4.
    for _, tc in all_tcs:
        for line in tc["pre_conditions"].split("\n"):
            if not line.strip() or not NEGATED_PC.search(line):
                continue
            if any(n in line for n in negations):
                continue
            if any(k in line for k in NON_AXIS_NEGATIONS):
                continue
            bad("axis-value-count",
                f"{tc['tc_id']}: negated pre_condition matches no axis block "
                f"and is not named in NON_AXIS_NEGATIONS — its coverage "
                f"changes silently when that axis gains a value (43 §4): "
                f"{line.strip()[:96]!r}")

    # ---- handoff 26 §4.1 — every TC key lands in a column or is named ----
    from write_back import COLS
    columned = set(COLS.values())
    scanned = [(tc["tc_id"], tc) for _, tc in all_tcs]
    scanned += [(f"{d['parent']} (doc)", d) for d in docs]      # 29 §5.1
    for label, obj in scanned:
        stray = sorted(set(obj) - columned - NOT_IN_WORKBOOK)
        if stray:
            bad("json-key-coverage",
                f"{label}: key(s) {stray} neither map to a workbook "
                "column nor appear in NOT_IN_WORKBOOK. Either write_back.py's "
                "COLS lost an entry, or the key is deliberately not delivered "
                "and must be named (adding to the list is a ruling)")

    # ---- handoff 26 §4.2 — an anomaly id cited must actually be registered --
    # A-CF16 was used across two upstream packages while ANOMALIES.md never
    # carried it. Citing an id and the id existing are two different things,
    # and the failure is silent: nothing rejects a number that means nothing.
    registered = ANOMALY_ID.findall((FEATURE / "ANOMALIES.md").read_text("utf-8"))
    cited = {}
    for doc in sorted((FEATURE / "docs").rglob("*.md")):
        for aid in ANOMALY_ID.findall(doc.read_text(encoding="utf-8")):
            cited.setdefault(aid, doc.relative_to(FEATURE).as_posix())
    orphans = {a: p for a, p in sorted(cited.items()) if a not in registered}
    if orphans:
        bad("anomaly-id-registered",
            "anomaly id(s) cited in docs/ but absent from ANOMALIES.md: "
            + ", ".join(f"{a} (first seen {p})" for a, p in orphans.items()))

    # ---- handoff 26 §4.3 — the residue scan must reach max_row -------------
    # Verified by reading write_back.py's source, not by running it: a fixed
    # window (24-35) silently stops short of the sheet's real extent (59), so
    # residue past the window would never be looked at.
    wb_src = (FEATURE / "scripts" / "write_back.py").read_text("utf-8")
    if "ws.max_row" not in wb_src or re.search(r"range\(last, last \+ \d+\)", wb_src):
        bad("residue-scan-window",
            "write_back.py's post-write residue scan does not run to "
            "ws.max_row (a fixed-width window leaves the tail unchecked)")
    return out, blocked, emea_no, fn_axis_report


def main() -> int:
    auth = load_authorities()
    docs = [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(GEN.glob("*.json"))]
    n_tc = sum(len(d["tcs"]) for d in docs)
    findings, blocked_ids, emea_no, fn_axis = lint(docs, auth)

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
             "blocked-row-empty", "blocked-remarks",
             # added 2026-08-15 with R-C26
             "marker-whitelist",
             # added 2026-08-15 per handoff 26 §4
             "json-key-coverage", "anomaly-id-registered",
             "residue-scan-window",
             # added 2026-08-15 per handoff 31 §1 / §2
             "forbidden-verb", "er-subject-net",
             # added 2026-08-15 per handoff 35 §4
             "axis-value-count",
             # added 2026-08-15 per handoff 36 §4 / §6
             "pending-sibling", "interface-axis-answered",
             # added 2026-08-15 per handoff 38 §1
             "emea-per-tc-answered",
             # added 2026-08-15 per handoff 42 §1
             "provisional-sibling",
             # added 2026-08-15 per handoff 52 §3
             "axis-type-reverse-test",
             # added 2026-08-16 per handoff 60 §1
             "no-tcid-in-prose"]
    failed = {g for _, g, _ in findings}

    print(f"files: {len(docs)}   TCs: {n_tc}   "
          f"vocabulary: {len(auth['vocab'])} strings   "
          f"valid outlines: {len(auth['outlines'])}\n")
    print("gates:")
    for g in gates:
        # er-subject-net prints its own self-qualifying line below; a plain
        # "PASS — er-subject-net" alongside it would read as a second, equal
        # claim, which is the exact impression 31 §2 forbids.
        if g == "er-subject-net" and g not in failed:
            continue
        print(f"- {'**FAIL**' if g in failed else 'PASS'} — {g}")
    # R-C24 — the exemption is visible on every run, whether or not it fired.
    print(f"- PASS — rows exempted as BLOCKED, all markers "
          f"(proc-min-steps, proc-er-1to1): {sorted(blocked_ids) or 'none'}")
    for mk in BLOCKED_MARKERS:
        print(f"- PASS — marker whitelist (profile §5.1/§5.2) {mk}: "
              f"{sorted(MARKER_WHITELIST[mk])}")
    equivalent_groups = identical_tc_groups(docs)
    print(f"- PASS — identical-TC scan (61 §2, measurement): "
          f"{len(equivalent_groups)} group(s) of TCs whose test_item, "
          f"test_procedure and expected_result are character-identical — "
          f"037 decomposition artefacts, kept as separate rows (§8.2.2), "
          f"recorded in pending_sibling's equivalent_tc_pairs")
    for g in equivalent_groups:
        print(f"    · {' ≡ '.join(f'{o}:{r}' for o, _, r in g)}")
    if emea_no:
        print(f"- PASS — EMEA exclusions whose per-TC answer is NOT `yes` "
              f"(R-C36-1; over-strict, removal awaits a ruling): "
              f"{[(i, v, o) for i, v, o in emea_no]}")
    n_decl, n_live, n_vac, n_tc_seen, worded = fn_axis
    print(f"- PASS — axis-type-reverse-test re-ran on {n_tc_seen} TCs "
          f"(52 §3, criterion = 54 §1 purpose version): {n_decl} 功能型 axes "
          f"declared, {n_live} with a removed interface (live test), "
          f"{n_vac} declaring `none` (vacuous by claim, not by omission)")
    print(f"- PASS — of the purpose-version hits, those ALSO matching the "
          f"52 §3 wording version (function governed by the axis): "
          f"{worded or 'none'} — the two versions are reported separately so "
          f"a future divergence is visible rather than absorbed")
    print(f"- PASS — pending siblings awaiting their counterpart section "
          f"(36 §4 / 37 §6): {sorted(PENDING_SIBLING)}")
    print("- PASS — the pending-sibling table is produced by lexical overlap "
          "and is NOT a completeness proof (R-C37); run "
          "scripts/sibling_candidates.py when a Test Set completes")
    if "er-subject-net" not in failed:
        print("- PASS — er-subject-net (a safety net, not the criterion; "
              "the criterion is §6 and is human-reviewed)")
    print(f"- PASS — keys deliberately not in the workbook, TC + doc layer "
          f"(26 §4.1 / 29 §5.1): {sorted(NOT_IN_WORKBOOK)}")
    if findings:
        print(f"\n{len(findings)} finding(s):")
        for sev, g, msg in findings:
            print(f"  [{sev}] {g}: {msg}")
    print(f"\n{len(gates) - len(failed)} / {len(gates)} gates PASS; "
          f"{len(findings)} finding(s) across {n_tc} TCs")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
