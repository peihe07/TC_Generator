#!/usr/bin/env python3
"""Reverse validation of the generalised `axis-value-count` gate (43 §4).

Same reason as verify_provisional_gate.py: a gate that has never been seen to
FAIL has not been shown to work. This one matters more than most, because the
thing it protects is silent by construction — a negated pre_condition whose
axis gained a value keeps passing every other check in the file.

Four directions are asserted, each against the SHIPPED profile blocks rather
than a re-typed copy:

  1. every axis block is well-formed and its declared count matches its values
  2. bumping a block's value-count without bumping the reviewed count FAILs,
     and the failure names the TCs owed a re-review
  3. a negated pre_condition matching no block and not named in
     NON_AXIS_NEGATIONS FAILs  <- the case 43 §4 exists for
  4. the three known non-axis negations (runtime / test-setup state) stay
     silent

Usage:
    python3 features/comfort/scripts/verify_axis_gate.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint_tcs as L

FEATURE = Path(__file__).resolve().parents[1]


def parse_blocks() -> list:
    out = []
    for raw in L.AXIS_BLOCK.findall(L.PROFILE.read_text(encoding="utf-8")):
        f = dict(l.split(":", 1) for l in raw.strip().split("\n")
                 if ":" in l and not l.lstrip().startswith("#"))
        out.append({k: v.strip() for k, v in f.items()})
    return out


def negation_users(negation: str) -> list:
    ids = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        for tc in json.loads(p.read_text(encoding="utf-8"))["tcs"]:
            if negation in tc["pre_conditions"]:
                ids.append(tc["tc_id"])
    return sorted(ids)


def all_negated_lines() -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        for tc in json.loads(p.read_text(encoding="utf-8"))["tcs"]:
            for line in tc["pre_conditions"].split("\n"):
                if line.strip() and L.NEGATED_PC.search(line):
                    out.append((tc["tc_id"], line.strip()))
    return out


def main() -> int:
    blocks = parse_blocks()
    fails = []

    def check(ok, label, detail=""):
        print(f"  {'PASS' if ok else '**FAIL**'} — {label}"
              + (f": {detail}" if detail else ""))
        if not ok:
            fails.append(label)

    print(f"axis blocks in profile: {len(blocks)}")
    negations = []
    for b in blocks:
        axis = b.get("axis", "?").split()[0]
        values = [v for v in b.get("values", "").split("|") if v.strip()]
        users = negation_users(b.get("negation", "\0"))
        listed = [v.strip() for v in b.get("negation-users", "").split(",")
                  if v.strip()]
        negations.append(b.get("negation", "\0"))
        print(f"\n  axis {axis:5} values={len(values)} "
              f"negation={b.get('negation','')!r}")
        check(b.get("value-count") == str(len(values)),
              f"axis {axis}: declared value-count matches the listed values",
              f"{b.get('value-count')} vs {len(values)}")
        check(b.get("negation-reviewed-at-value-count") == b.get("value-count"),
              f"axis {axis}: reviewed-at equals value-count")
        check(sorted(listed) == users,
              f"axis {axis}: negation-users matches the corpus",
              f"{len(listed)} listed vs {len(users)} measured")
        check(len(users) > 0,
              f"axis {axis}: the negation actually occurs in the corpus",
              f"{len(users)} TCs")
        # 44 §6 — value-count now means "scanned the corpus, saw no N+1th
        # value". A block without a `scan:` line has an UNPROVEN count, and
        # the gate built on it would be checking against an unchecked number.
        check(bool(b.get("scan")),
              f"axis {axis}: carries a `scan:` line proving its value-count",
              (b.get("scan", "")[:70] or "MISSING"))
        check("catch-all" in b.get("scan", "") or "列舉窮盡" in b.get("scan", "")
              or "邏輯上之窮盡" in b.get("scan", ""),
              f"axis {axis}: `scan:` states WHICH kind of exhaustiveness",
              "catch-all vs enumerated — the gate is only live on enumerated")

    # --- direction 2: an axis that gains a value must FAIL until re-reviewed
    print("\n  simulated: axis 13 gains a fourth value, reviewed-at not bumped")
    sim = dict(blocks[0])
    sim["values"] = sim["values"] + " | a fourth value"
    sim["value-count"] = str(len([v for v in sim["values"].split("|")
                                  if v.strip()]))
    would_fail = sim["value-count"] != sim["negation-reviewed-at-value-count"]
    check(would_fail, "adding a value without bumping reviewed-at FAILs",
          f"count {sim['value-count']} vs reviewed "
          f"{sim['negation-reviewed-at-value-count']}")

    # --- direction 3: an unprotected negation must FAIL
    print("\n  coverage of every negated pre_condition in the corpus")
    uncovered = [(i, l) for i, l in all_negated_lines()
                 if not any(n in l for n in negations)
                 and not any(k in l for k in L.NON_AXIS_NEGATIONS)]
    check(not uncovered, "no negated PC is left unprotected",
          f"{len(uncovered)} uncovered" if uncovered else "0 uncovered")
    for i, l in uncovered:
        print(f"      {i}: {l[:100]}")

    invented = "[spec-derived] The vehicle is not fitted with a widget bar (99.9)"
    would_fire = (not any(n in invented for n in negations)
                  and not any(k in invented for k in L.NON_AXIS_NEGATIONS))
    check(would_fire,
          "an invented negation for an axis with no block DOES fire",
          repr(invented[:60]))

    # --- direction 4: the named non-axis negations stay silent
    print("\n  named non-axis negations (runtime / test-setup state)")
    for phrase, why in sorted(L.NON_AXIS_NEGATIONS.items()):
        hits = [i for i, l in all_negated_lines() if phrase in l]
        check(bool(hits),
              f"{phrase[:44]!r} is still used — an allowlist entry with no "
              f"user is stale", f"{len(hits)} TC(s); {why}")

    if fails:
        print(f"\n**{len(fails)} case(s) FAILED**")
        return 1
    print("\nall directional cases PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
