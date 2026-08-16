#!/usr/bin/env python3
"""Reverse validation of `axis-type-reverse-test` (handoff 52 §3).

This gate is the one most likely to be green for the wrong reason. Its live
case is currently ONE axis (16) and ZERO offending TCs, so "PASS" and "the
predicate never ran" print identically. Both directions are asserted here,
and the profile is read for the criteria exactly as the gate reads it — no
re-typed copy (the lesson from verify_provisional_gate.py).

Six directions:

  1. every 功能型 axis in the profile table has a block  <- omission is the
     silence the gate exists to break
  2. the live axis (removed-interface != none) really has TCs on that
     interface — otherwise the test is vacuous while claiming to be live
  3. a TC on the removed interface, with the axis's function, and WITHOUT
     the axis pre_condition, FIRES
  4. the same TC WITH the axis pre_condition stays silent  <- this is the
     interpretation added in 上繳 36 §3.2; if it were wrong, -125/-126
     would have to fail, and they must not
  5. a TC on some other interface stays silent
  6. an axis declaring `none` cannot fire, whatever the corpus says
  7. the wording version (52 §3) is a subset of the purpose version (54 §1),
     which is why the latter is the FAIL criterion

Usage:
    python3 features/comfort/scripts/verify_axis_type_gate.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint_tcs as L

FEATURE = Path(__file__).resolve().parents[1]


def blocks() -> dict:
    out = {}
    for raw in L.FN_AXIS_BLOCK.findall(L.PROFILE.read_text(encoding="utf-8")):
        f = dict(l.split(":", 1) for l in raw.strip().split("\n")
                 if ":" in l and not l.lstrip().startswith("#"))
        out[f.get("axis", "?").strip().split()[0]] = {
            k: v.strip() for k, v in f.items()}
    return out


def terms(block: dict, key: str) -> list:
    v = block.get(key, "").strip()
    return [] if v in ("", "none") else [t.strip() for t in v.split("|")
                                         if t.strip()]


def fires(block: dict, tc: dict, worded: bool = False) -> bool:
    """The gate's predicate, verbatim from lint_tcs.py's gate body.

    `worded=False` is the 54 §1 PURPOSE version and is the FAIL criterion.
    `worded=True` adds 52 §3's original function filter, kept so the two can
    be compared — if they ever diverge again, the difference is the finding.
    """
    iface, fn = (terms(block, "removed-interface-keywords"),
                 terms(block, "function-keywords"))
    pcs = terms(block, "axis-pc-keywords")
    if not iface:
        return False
    observable = f"{tc['test_procedure']}\n{tc['expected_result']}"
    if not any(t in observable for t in iface):
        return False
    if any(t in tc["pre_conditions"] for t in pcs):
        return False
    if worded:
        subject = f"{tc['test_item']}\n{observable}"
        return bool(fn) and any(t in subject for t in fn)
    return True


def main() -> int:
    fails = []

    def check(ok, label, detail=""):
        print(f"  {'PASS' if ok else '**FAIL**'} — {label}"
              + (f": {detail}" if detail else ""))
        if not ok:
            fails.append(label)

    b = blocks()
    tcs = [t for p in sorted((FEATURE / "generated").glob("*.json"))
           for t in json.loads(p.read_text(encoding="utf-8"))["tcs"]]
    print(f"blocks: {len(b)}   TCs: {len(tcs)}")

    # --- 1. no 功能型 axis without a block
    table = L.AXIS_TABLE_ROW.findall(L.PROFILE.read_text(encoding="utf-8"))
    missing = [n for n, _, k in table if k == "功能型" and n not in b]
    check(not missing, "every 功能型 axis in the table has a block",
          f"missing {missing}" if missing else
          f"{sum(1 for _, _, k in table if k == '功能型')} axes, all declared")

    live = {a: v for a, v in b.items()
            if terms(v, "removed-interface-keywords")}
    check(bool(live), "at least one axis declares a removed interface",
          f"live: {sorted(live)}")

    for axis, blk in sorted(live.items()):
        iface = terms(blk, "removed-interface-keywords")
        on_iface = [t for t in tcs
                    if any(x in f"{t['test_procedure']}\n{t['expected_result']}"
                           for x in iface)]
        # --- 2. the live test is not secretly vacuous
        check(bool(on_iface),
              f"axis {axis}: TCs exist on the removed interface, so the live "
              f"test actually runs", f"{len(on_iface)} TC(s): "
              f"{[t['tc_id'] for t in on_iface]}")
        # --- 4. those TCs carry the axis PC, hence silent
        firing = [t["tc_id"] for t in on_iface if fires(blk, t)]
        check(not firing,
              f"axis {axis}: TCs on that interface carry the axis "
              f"pre_condition, so they stay silent", f"firing: {firing}")
        # --- 3. strip the pre_condition and it must fire. The probe must be
        # a TC that satisfies the FUNCTION filter too, or the case proves
        # nothing — the first attempt picked -117, whose function is not
        # axis-governed, and read the (correct) silence as a failure.
        fn = terms(blk, "function-keywords")
        probe_src = next(
            (t for t in on_iface
             if not fn or any(x in f"{t['test_item']}\n{t['test_procedure']}\n"
                              f"{t['expected_result']}" for x in fn)), None)
        check(probe_src is not None,
              f"axis {axis}: a TC exists that matches BOTH the interface and "
              f"the function filter", probe_src["tc_id"] if probe_src else "none")
        if probe_src:
            probe = dict(probe_src)
            probe["pre_conditions"] = "1. [test-setup] nothing"
            check(fires(blk, probe),
                  f"axis {axis}: the SAME TC without the axis pre_condition "
                  f"DOES fire", probe["tc_id"])

        # --- 3c. 54 §1 — the two versions must be reported separately, and
        # the purpose version must be at least as wide as the wording one.
        p_hits = [t["tc_id"] for t in tcs if fires(blk, t)]
        w_hits = [t["tc_id"] for t in tcs if fires(blk, t, worded=True)]
        check(set(w_hits) <= set(p_hits),
              f"axis {axis}: the wording version is a SUBSET of the purpose "
              f"version (54 §1 — purpose is the wider, hence the criterion)",
              f"purpose {p_hits or 'none'} / wording {w_hits or 'none'}")

        # --- 3b. 上繳 36 §3.3 — the WORDED test asks for an axis-governed
        # function; the PURPOSE it was given (35 §1 / 50 §1) is the opposite
        # case: another TC losing its observable while ITS function survives.
        # Run the purpose-version too and report it, because a gate that
        # matches its wording and misses its reason is the worst kind of green.
        purpose = [t["tc_id"] for t in on_iface
                   if not any(x in t["pre_conditions"]
                              for x in terms(blk, "axis-pc-keywords"))]
        check(not purpose,
              f"axis {axis}: no TC depends on that interface WITHOUT stating "
              f"the axis value (purpose-version of the test)",
              f"unprotected: {purpose}")
        # --- 5. an unrelated TC stays silent
        other = next((t for t in tcs if t not in on_iface), None)
        if other:
            check(not fires(blk, other),
                  f"axis {axis}: a TC on another interface stays silent",
                  other["tc_id"])

    # --- 6. a `none` axis cannot fire on anything
    vac = next((a for a, v in b.items()
                if not terms(v, "removed-interface-keywords")), None)
    if vac:
        check(not any(fires(b[vac], t) for t in tcs),
              f"axis {vac}: declares `none` and fires on nothing",
              f"checked against all {len(tcs)} TCs")

    if fails:
        print(f"\n**{len(fails)} case(s) FAILED**")
        return 1
    print("\nall directional cases PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
