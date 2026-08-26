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
  A  forbidden step verbs (5.1)          G  test_set closed vocabulary (4.2)
  B  modal verbs in ER (6)               M  required-field three-state (8.4.3)
  E  step to ER alignment (6)            N  trailing period (11)
  I  test_item bracket tail (S4)         O  spec_reference format (R-2)
  K  CJK in delivery columns (1)         P  signal notation (8.7.5 v3)

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
            outside = re.sub(r'"[^"]*"', "", line)
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
            if not SPEC_REF.match(line):
                fails.append(f"{tag}: spec_reference line {line!r} (R-2)")

        check_p(tc, dbc, fails, notes)                               # P

    brackets = defaultdict(list)
    for tc in data["tcs"]:
        brackets[tc["req_id"]].append(tc["test_item"].split("(", 1)[1])
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
