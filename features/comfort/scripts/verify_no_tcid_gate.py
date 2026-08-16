#!/usr/bin/env python3
"""Reverse validation of `no-tcid-in-prose` (handoff 60 §1).

The gate is green on the corpus the moment it is written, because the
one-off rewrite happens in the same round. "Green" and "the predicate never
ran" print identically, so both directions are asserted here.

The regexes are IMPORTED from lint_tcs, never re-typed — a verifier that
carries its own copy tests the copy.

Directions:

  1. the spelled-out form (`NR1L-ComfortHMI-233`) fires
  2. the SHORT form (`` `-233` ``) fires  <- the form that actually broke in
     58 §2, and the one 60 §1's stated regex would have missed
  3. the req_id form (`` `119-07` ``) does NOT fire  <- otherwise the rule
     would forbid its own replacement
  4. a leaf-style citation (`` `015-04` ``) does NOT fire — that IS a req_id
  5. the corpus is currently clean, and the scan really visited prose (a
     scan of zero fields would also report clean)

Usage:
    python3 features/comfort/scripts/verify_no_tcid_gate.py
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint_tcs as L

FEATURE = Path(__file__).resolve().parents[1]


def fires(text: str) -> bool:
    """The gate's predicate, using lint_tcs' own compiled patterns."""
    return bool(L.TCID_LONG.findall(text) + L.TCID_SHORT.findall(text))


def main() -> int:
    fails = []

    def check(ok, label, detail=""):
        print(f"  {'PASS' if ok else '**FAIL**'} — {label}"
              + (f": {detail}" if detail else ""))
        if not ok:
            fails.append(label)

    check(fires("與 `NR1L-ComfortHMI-233` 同型"),
          "spelled-out tc_id FIRES", "NR1L-ComfortHMI-233")
    check(fires("`-231` 改風速 → MAX A/C 解除"),
          "short-form tc_id FIRES (the form that broke in 58 §2)", "`-231`")
    check(not fires("`119-07` 改風速 → MAX A/C 解除"),
          "req_id form stays silent — the rule permits its own remedy",
          "`119-07`")
    check(not fires("批次 9 停下 `015-04`／`015-05`"),
          "leaf-style req_id stays silent", "`015-04`")
    check(not fires("MAX DEF 之七項連動於 3.2 逐字相同"),
          "ordinary prose stays silent")

    # --- 5. the corpus is clean AND the scan visited something
    docs = [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted((FEATURE / "generated").glob("*.json"))]
    scanned, dirty = 0, []
    for d in docs:
        fields = {"reasoning": d.get("reasoning", ""),
                  "axis": d.get("distinguishing_axis", {}).get("axis", ""),
                  "delta": d.get("distinguishing_axis", {}).get("delta", ""),
                  "assumptions": " ".join(d.get("assumptions", []) or [])}
        for tc in d["tcs"]:
            fields[f"{tc['tc_id']}.split_reason"] = tc.get("split_reason") or ""
            fields[f"{tc['tc_id']}.remarks"] = tc.get("remarks") or ""
        for name, text in fields.items():
            if text:
                scanned += 1
            if fires(text):
                dirty.append(f"{d['outline']}:{name}")
    check(not dirty, "corpus carries no tc_id citation in prose",
          f"{dirty[:5]}" if dirty else f"{len(docs)} docs")
    check(scanned > 100,
          "the scan actually visited prose (a zero-field scan also reports "
          "clean)", f"{scanned} non-empty prose field(s)")

    # --- 6. the req_id citations that REPLACED the tc_ids are real req_ids.
    # Not the gate's job, but if the rewrite invented ids the gate would sit
    # green over a corpus that cites nothing.
    reqs = {tc["req_id"].replace("SWE1-HVAC-", "")
            for d in docs for tc in d["tcs"]}
    cited = set()
    for d in docs:
        for text in (d.get("reasoning", ""),
                     d.get("distinguishing_axis", {}).get("delta", "")):
            cited |= set(re.findall(r"`(\d{3}(?:-\d{2})?)`", text))
    # Withheld / withdrawn leaves are cited on purpose and have no TC. Read
    # them from the generators' own WITHHELD lists rather than a hand-kept
    # list here — a hand-kept list is the same shifting key the gate exists
    # to abolish. (Measured: the hand-kept version missed 125-08, 127-01,
    # 127-02, all legitimately cited stop-and-report leaves.)
    withheld = set()
    for gen in sorted((FEATURE / "scripts").glob("gen_*.py")):
        withheld |= {m.replace("SWE1-HVAC-", "") for m in re.findall(
            r'\("(SWE1-HVAC-\d+-\d+)"', gen.read_text(encoding="utf-8"))}
    unknown = sorted(c for c in cited if c not in reqs and c not in withheld)
    check(not unknown, "every req_id cited in prose is a real req_id "
          "(or a declared withheld leaf)", f"unknown: {unknown}")

    if fails:
        print(f"\n**{len(fails)} case(s) FAILED**")
        return 1
    print("\nall directional cases PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
