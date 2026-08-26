#!/usr/bin/env python3
"""Lint a generated audio_mgmt batch against the canon and this feature's profile.

Check P (CAN assertion notation) is the reason `--profile` exists. The shared
lint still implements P against 8.7.5 **v2**, whose `Send CAN:` prefix was
revoked in 2026-08-21; audio_mgmt is on the global **v3** default and declares
no `[OVERRIDE 8.7.5]`. Running P with the v2 criteria against v3 text reports
every correct line as a violation, so the profile is selected explicitly and
this script refuses to guess:

    python features/audio_mgmt/scripts/lint_tcs.py --profile audio_mgmt

Checks implemented here, lettered as in PREVENTION_ARCHITECTURE:
  A  forbidden step verbs (5.1)          H  vague ER wording (6)
  B  modal verbs in ER (6)               I  test_item bracket tail (S4)
  C  test_item hedges and modals (4.3)   J  line-opening capital (R-4)
  D  pre-condition shape (4.4)           K  CJK in delivery columns (1)
  E  step to ER alignment (6)            L  verbatim half token cap (R-3)
  F  square brackets (11)                M  required-field three-state (8.4.3)
  G  test_set closed vocabulary (4.2)    N  trailing period (11)
                                         O  spec_reference format (R-2)
                                         P  signal notation (8.7.5 v3)

Usage:
    python features/audio_mgmt/scripts/lint_tcs.py --profile audio_mgmt
    python features/audio_mgmt/scripts/lint_tcs.py --profile audio_mgmt --batch B1
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

FEATURE = Path(__file__).resolve().parents[1]

FORBIDDEN_VERBS = ("observe whether", "observe", "see if", "check whether",
                   "confirm whether", "verify", "watch", "monitor", "inspect")
STEP_HEAD = re.compile(
    r"^\s*\d+\.\s*(" + "|".join(sorted(FORBIDDEN_VERBS, key=len, reverse=True))
    + r")\b", re.I)
MODALS = re.compile(r"\b(shall|should|must|will|would|may|might)\b", re.I)
CJK = re.compile(r"[一-鿿]")
SPEC_REF = re.compile(r"^CFTS019-48\d{5}$")
# A leaf ruled to ship with no anchor at all (package 12 section 3.5) carries
# a PENDING here instead of an id. 8.4.3 makes that legal now and illegal at
# delivery, which is check M's job, not this one's.
SPEC_REF_PENDING = re.compile(r"^PENDING: DR-\w+\b.*$")

# ---- check P, 8.7.5 v3 -----------------------------------------------------
# v1's triple and v2's prefix are both revoked; text carrying either is stale.
V1_TRIPLE = re.compile(r"\bin\s+[A-Z][A-Za-z0-9_]*\s+on\s+\w*CAN\w*\b")
V2_PREFIX = re.compile(r"\bSend\s+CAN\s*:", re.I)
# v3(a): a signal is $MESSAGE.Signal$ — the $ wraps the whole qualified name.
SIGNAL_TOKEN = re.compile(r"\$([^$]+)\$")
QUALIFIED = re.compile(r"^[A-Za-z][A-Za-z0-9_]*\.[A-Za-z][A-Za-z0-9_]*$")
# v3(a): the value form is `= <raw> (<label>)`.
VALUE_FORM = re.compile(r"=\s*-?\d+\s*\([A-Za-z0-9_]+\)")
# v3(c): PROXI parameters never take $.
PROXI_DOLLAR = re.compile(r"\bPROXI\s+\$")

# ---- check C, canon 4.3 -----------------------------------------------------
# The canon names three: properly, successfully, within reasonable time.
# Listed one-for-one so the list can be diffed against its authority.
HEDGES = ("properly", "successfully", "within reasonable time")
HEDGE_RE = re.compile(r"\b(" + "|".join(HEDGES) + r")\b", re.I)
# 4.3 also bars modals from the title half; MODALS above is reused.

# ---- check D, canon 4.4 -----------------------------------------------------
# A pre-condition is starting state or environment. The canon's forbidden set
# is system defaults, the feature under test as premise, actions, and
# step-controlled state, with the self-test: if it needs doing, checking or
# confirming, it is not a pre-condition.
PC_DEFAULT = re.compile(r"\b(powered on|power(ed)? up|switched on|booted|"
                        r"ignition is on|system is (on|ready))\b", re.I)
PC_ACTION = re.compile(r"^\s*(insert|connect|open|press|select|start|play|"
                       r"launch|enable|disable|set|trigger|activate|do|check|"
                       r"confirm|read|verify)\w*\b", re.I)

# ---- check H, canon 6 -------------------------------------------------------
VAGUE = re.compile(r"\b(as expected|normally|normal behaviou?r|correctly|"
                   r"appropriately|properly)\b", re.I)

# ---- check F, canon 11 ------------------------------------------------------
# UI labels take double quotes, never square brackets. audio_mgmt writes
# signal values as `= <raw> (<label>)` under 8.7.5 v3, so unlike the v2-era
# features there is no source-quoted `$SIG$ = [value]` form to exempt here.
BRACKET = re.compile(r"[\[\]]")

# ---- check J, R-4 -----------------------------------------------------------
# A content line opens with a capital. Exempt: a technical token, camelCase,
# an opening quote, and a $signal$ — all of which carry their own casing.
LINE_LOWER_OK = re.compile(r'^\s*(\d+\.\s*)?(["\$<\[(]|[a-z]+[A-Z]|'
                           r'[a-z]+[_.][a-z]|PROXI\b)')

# ---- check L, R-3 -----------------------------------------------------------
VERBATIM_TOKEN_CAP = 50

DELIVERY = ("test_item", "pre_conditions", "input_test_data",
            "test_procedure", "expected_result", "remarks")
REQUIRED = ("req_id", "test_group", "test_set", "test_item", "pre_conditions",
            "input_test_data", "test_procedure", "expected_result",
            "spec_reference", "priority", "design_method")


def test_set_vocabulary() -> set[str]:
    """Layer 2 values, read from framework.md rather than restated here."""
    text = (FEATURE / "framework.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\|\s*([A-Z][^|]*?)\s*\|\s*1\.3[^|]*\|", text, re.M)
    return {r.strip() for r in rows}


def dbc_signal_names() -> set[str]:
    """Bare signal names the supplied DBCs carry, for check P's (g) branch."""
    names = set()
    for dbc in (FEATURE.parent.parent / "forms").glob("*.dbc"):
        text = dbc.read_text(encoding="latin-1")
        names |= set(re.findall(r"^\s*SG_ (\w+)", text, re.M))
    return names


def check_p(tc, dbc: set[str], fails: list, notes: list) -> None:
    """8.7.5 v3 signal notation."""
    tag = tc["req_id"]
    for key in ("test_procedure", "expected_result", "pre_conditions",
                "input_test_data"):
        text = str(tc[key])
        if V2_PREFIX.search(text):
            fails.append(f"{tag}/{key}: uses the revoked v2 `Send CAN:` prefix")
        if V1_TRIPLE.search(text):
            fails.append(f"{tag}/{key}: uses the revoked v1 signal triple")
        if PROXI_DOLLAR.search(text):
            fails.append(f"{tag}/{key}: PROXI parameter carries $ (v3 c)")
        for token in SIGNAL_TOKEN.findall(text):
            if QUALIFIED.match(token):
                continue
            # Unqualified. Legal only where the DBC has no such signal, in
            # which case v3 (g) keeps the specification's own name; if the DBC
            # does carry it, the qualified form was available and required.
            if token in dbc:
                fails.append(
                    f"{tag}/{key}: ${token}$ is unqualified but the DBC "
                    f"carries it — v3 (a) requires $MESSAGE.{token}$")
            else:
                notes.append(
                    f"{tag}/{key}: ${token}$ kept unqualified under v3 (g); "
                    f"absent from the supplied DBC")
    # Where a qualified signal is given a value, the value must be raw (label).
    for key in ("test_procedure", "expected_result"):
        for line in str(tc[key]).split("\n"):
            if "$" in line and "=" in line and not VALUE_FORM.search(line):
                m = SIGNAL_TOKEN.search(line)
                if m and QUALIFIED.match(m.group(1)):
                    fails.append(
                        f"{tag}/{key}: signal value is not `= <raw> (<label>)`"
                        f": {line[:60]}")



def bracket_tail(test_item: str) -> str:
    """The authored bracket half, not the first parenthesis in the string.

    Splitting on the first "(" reaches into the verbatim upper half whenever
    the requirement text contains its own parentheses — SWE1_AMM_256's
    "(navigation prompts, warnings, chimes, etc.)" is one — so the
    sibling-distinction check was comparing fragments of the specification
    instead of the tails it exists to compare.
    """
    _, sep, tail = test_item.rpartition("\n\n(")
    return tail if sep else test_item


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch", default="B1")
    ap.add_argument("--profile", required=True,
                    help="feature profile selecting the 8.7.5 revision for "
                         "check P; audio_mgmt is on the v3 global default")
    args = ap.parse_args()

    if args.profile != "audio_mgmt":
        sys.exit(f"profile {args.profile!r} is not this feature's. Check P "
                 f"would run on the wrong 8.7.5 revision")

    data = json.loads((FEATURE / "generated" / f"{args.batch}.json")
                      .read_text(encoding="utf-8"))
    vocab = test_set_vocabulary()
    dbc = dbc_signal_names()
    fails: list[str] = []
    notes: list[str] = []

    for tc in data["tcs"]:
        tag = tc["req_id"]
        proc = tc["test_procedure"].split("\n")
        er = tc["expected_result"].split("\n")

        for step in proc:                                            # A
            m = STEP_HEAD.match(step)
            if m:
                fails.append(f"{tag}: step opens with {m.group(1)!r} (5.1)")
        for line in er:                                              # B
            # "CAN amplified" is the bus, not the modal. Drop all-caps
            # technical tokens before the modal test rather than letting a
            # case-insensitive \bcan\b flag every CAN system reference.
            outside = re.sub(r"\bCAN\b", "", re.sub(r'"[^"]*"', "", line))
            if MODALS.search(outside):
                fails.append(f"{tag}: ER carries a modal verb (6): {line[:50]}")
        if len(proc) != len(er):                                     # E
            fails.append(f"{tag}: {len(proc)} steps against {len(er)} results")
        if not re.search(r"\n\n\(.+\)$", tc["test_item"], re.S):     # I
            fails.append(f"{tag}: test_item has no bracket tail (S4)")
        for key in DELIVERY:                                         # K
            if CJK.search(str(tc[key])):
                fails.append(f"{tag}/{key}: CJK in a delivery column (1)")
        if tc["test_set"] not in vocab:                              # G
            fails.append(f"{tag}: test_set {tc['test_set']!r} is outside the "
                         f"framework.md Layer 2 vocabulary")
        for key in REQUIRED:                                         # M
            val = str(tc.get(key, "")).strip()
            if not val:
                fails.append(f"{tag}/{key}: empty (8.4.3 — NA or PENDING, "
                             f"never blank)")
            elif val.startswith("PENDING:"):
                notes.append(f"{tag}/{key}: PENDING — legal now, blocks "
                             f"delivery (8.4.3)")
        for key in DELIVERY:                                         # N
            for line in str(tc[key]).split("\n"):
                if line.rstrip().endswith(".") and not re.search(
                        r"\b\d+\.$", line.rstrip()):
                    fails.append(f"{tag}/{key}: line ends in a period (11)")
        for line in tc["spec_reference"].split("\n"):                # O
            if not (SPEC_REF.match(line) or SPEC_REF_PENDING.match(line)):
                fails.append(f"{tag}: spec_reference line {line!r} (R-2)")

        upper, _, bracket = tc["test_item"].partition("\n\n")
        m = HEDGE_RE.search(bracket)                                 # C
        if m:
            fails.append(f"{tag}: test_item bracket hedges on "
                         f"{m.group(1)!r} (4.3)")
        m = MODALS.search(bracket)
        if m:
            fails.append(f"{tag}: test_item bracket uses the modal "
                         f"{m.group(1)!r} (4.3)")
        n_tok = len(upper.split())                                   # L
        if n_tok > VERBATIM_TOKEN_CAP:
            fails.append(f"{tag}: verbatim half is {n_tok} tokens, over the "
                         f"{VERBATIM_TOKEN_CAP} R-3 allows")
        pc = str(tc["pre_conditions"]).strip()                       # D
        if pc.upper() != "NA":
            for line in pc.split("\n"):
                if PC_DEFAULT.search(line):
                    fails.append(f"{tag}: pre_condition states a system "
                                 f"default (4.4): {line[:46]}")
                if PC_ACTION.match(line):
                    fails.append(f"{tag}: pre_condition is an action or a "
                                 f"check (4.4): {line[:46]}")
        for line in tc["expected_result"].split("\n"):               # H
            m = VAGUE.search(line)
            if m:
                fails.append(f"{tag}: ER is vague on {m.group(1)!r} (6): "
                             f"{line[:46]}")
        for key in DELIVERY:                                         # F
            if BRACKET.search(str(tc[key])):
                fails.append(f"{tag}/{key}: square bracket — UI labels take "
                             f'double quotes (11)')
        for key in ("test_procedure", "expected_result"):            # J
            for line in str(tc[key]).split("\n"):
                body = re.sub(r"^\s*\d+\.\s*", "", line)
                if body and body[0].islower() and not LINE_LOWER_OK.match(line):
                    fails.append(f"{tag}/{key}: line opens lower case (R-4): "
                                 f"{line[:46]}")

        check_p(tc, dbc, fails, notes)                               # P

    brackets = defaultdict(list)
    for tc in data["tcs"]:
        brackets[tc["req_id"]].append(bracket_tail(tc["test_item"]))
    for req, xs in brackets.items():
        if len(xs) != len(set(xs)):
            fails.append(f"{req}: sibling rows share a bracket tail (S4)")

    print(f"lint {args.batch} — profile {args.profile}, check P on 8.7.5 v3")
    print(f"  {len(data['tcs'])} TCs, {data['leaves_authored']} leaves")
    print(f"  test_set vocabulary: {len(vocab)} values from framework.md")
    print(f"  DBC signals available: {len(dbc)}")
    if notes:
        print(f"\n{len(notes)} note(s):")
        for n in sorted(set(notes)):
            print(f"  {n}")
    if fails:
        print(f"\n{len(fails)} violation(s):")
        for f in fails:
            print(f"  {f}")
        return 1
    print("\nlint green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
