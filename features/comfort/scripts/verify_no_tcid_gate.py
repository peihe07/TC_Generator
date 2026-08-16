#!/usr/bin/env python3
"""Reverse validation of `no-tcid-in-prose` (60 §1) and
`prose-reqid-exists` (62 §5) — the two halves of profile §3.6.1.

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
  6. `prose-reqid-exists`: an invented req_id FIRES, a withheld leaf does
     NOT, and the leaf universe really is 037's 403 (a universe read from
     the corpus itself could never fail)

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

    # --- 6. `prose-reqid-exists` (62 §5). The one-shot check this file ran
    # in round 60 is now a standing gate; both directions are asserted here
    # against lint's OWN universe and pattern, not a copy.
    universe = {r.replace("SWE1-HVAC-", "") for r in L.LEAF_UNIVERSE}
    check(len(L.LEAF_UNIVERSE) == 403,
          "the leaf universe is 037's 403 leaves, not something derived from "
          "the corpus (a self-derived universe can never fail)",
          f"{len(L.LEAF_UNIVERSE)} leaves")

    cited = set()
    for d in docs:
        for text in (d.get("reasoning", ""),
                     d.get("distinguishing_axis", {}).get("delta", "")):
            cited |= set(L.REQ_CITE.findall(text))
    unknown = sorted(c for c in cited if c not in universe)
    check(not unknown, "every req_id cited in prose exists in 037",
          f"unknown: {unknown}" if unknown else f"{len(cited)} distinct cited")
    check(len(cited) > 50, "prose really does cite req_ids, so the gate is "
          "not passing over an empty set", f"{len(cited)} distinct req_id(s)")

    invented = sorted(L.REQ_CITE.findall("與 `999-99` 同型"))
    check(invented and invented[0] not in universe,
          "an invented req_id would FIRE", f"{invented}")
    withheld_cited = [c for c in ("128-01", "122-02", "125-08", "016-01")
                      if c in universe]
    check(len(withheld_cited) == 4,
          "STOPPED leaves are inside the universe, so citing them stays "
          "silent (they are cited on purpose)", f"{withheld_cited}")

    if fails:
        print(f"\n**{len(fails)} case(s) FAILED**")
        return 1
    print("\nall directional cases PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
