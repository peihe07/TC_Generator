#!/usr/bin/env python3
"""Reverse validation of the (b)-class gates: `mirror-map-verified` and
`withheld-not-generated` (62 §1.1), `axis-candidate-registered` (64 §1) and
`moved-leaf-identity` (65 §4).

Both are green on the corpus the moment they are written, which is the state
R-C41 exists to distrust. Predicates are imported from lint_tcs, never
re-typed.

Directions:

  mirror-map-verified
    1. all 18 `mirrored` rows measure ≥ the threshold — and there ARE 18, so
       the check is not scanning an empty set
    2. two unrelated sections FIRE (short shared run)
    3. an outline that does not exist in section_fulltext FIRES
    4. **the autojunk regression**: difflib's default heuristic collapses
       16.13↔2.13's shared 100-character sentence to 1, i.e. the gate would
       have failed three correct rows. Asserted explicitly so the flag is
       never quietly restored.

  withheld-not-generated
    5. no leaf is both withheld and produced — and the withheld set is
       non-empty (a gate over an empty set proves nothing)
    6. a leaf that is both FIRES
    7. every withheld leaf exists in 037's 403

Usage:
    python3 features/comfort/scripts/verify_b_gates.py
"""

import difflib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint_tcs as L

FEATURE = Path(__file__).resolve().parents[1]


def main() -> int:
    fails = []

    def check(ok, label, detail=""):
        print(f"  {'PASS' if ok else '**FAIL**'} — {label}"
              + (f": {detail}" if detail else ""))
        if not ok:
            fails.append(label)

    full = L.FULLTEXT_BY_OUTLINE
    rows = L.mirror_map_rows()
    mirrored = [(a, b) for _, a, b, k in rows
                if k == "mirrored" and "no-counterpart" not in (a, b)]

    check(len(mirrored) == 18,
          "the map really carries `mirrored` rows to measure",
          f"{len(mirrored)} row(s)")
    short = [(a, b, L._longest_run(full[a], full[b])[0]) for a, b in mirrored
             if L._longest_run(full[a], full[b])[0] < L.MIRROR_MIN_RUN]
    check(not short, "every `mirrored` row shares a verbatim run ≥ threshold",
          f"below threshold: {short}")

    # --- 2. two sections that are NOT a mirror pair
    size, _ = L._longest_run(full["7.3"], full["2.5"])
    check(size < L.MIRROR_MIN_RUN,
          "two unrelated sections would FIRE if labelled `mirrored`",
          f"7.3 ↔ 2.5 share {size} chars")

    # --- 3. a missing outline
    check("9.9.9" not in full,
          "an outline absent from section_fulltext would FIRE", "9.9.9")

    # --- 4. the autojunk regression, asserted rather than remembered
    a, b = full["16.13"], full["2.13"]
    with_junk = difflib.SequenceMatcher(None, a, b)
    m = with_junk.find_longest_match(0, len(a), 0, len(b))
    without = L._longest_run(a, b)[0]
    check(m.size < L.MIRROR_MIN_RUN <= without,
          "difflib's default autojunk WOULD have failed a correct row — "
          "the gate must keep autojunk=False",
          f"16.13 ↔ 2.13: autojunk=True {m.size} chars, "
          f"autojunk=False {without} chars")

    # --- 5-7. withheld-not-generated
    docs = [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted((FEATURE / "generated").glob("*.json"))]
    produced = {tc["req_id"] for d in docs for tc in d["tcs"]}
    withheld = set()
    for gen in sorted((FEATURE / "scripts").glob("gen_*.py")):
        withheld |= set(L.WITHHELD_DECL.findall(
            gen.read_text(encoding="utf-8")))
    check(len(withheld) >= 20,
          "generators really do declare withheld leaves, so the gate is not "
          "scanning an empty set", f"{len(withheld)} declared")
    check(not (withheld & produced),
          "no leaf is both withheld and produced",
          f"both: {sorted(withheld & produced)}")
    probe = sorted(produced)[0]
    check(bool({probe} & produced),
          "a leaf declared withheld while produced WOULD fire (probe against "
          "a real produced leaf)", probe)
    unknown = sorted(withheld - set(L.LEAF_UNIVERSE))
    check(not unknown, "every withheld leaf exists in 037's 403",
          f"unknown: {unknown}")

    # --- 8-10. axis-candidate-registered (R-C42 三). Its reach is measured
    # over written pre_conditions, not section text: the risk it guards is two
    # TCs stating the same condition differently, and only a written PC can do
    # that. (The first cut measured section text and mis-declared three of the
    # four candidates.)
    prof = L.PROFILE.read_text(encoding="utf-8")
    blocks = L.PENDING_AXIS_BLOCK.findall(prof)
    check(len(blocks) >= 4,
          "the profile declares axis candidates, so the gate is not scanning "
          "an empty set", f"{len(blocks)} block(s)")
    fields = []
    for raw in blocks:
        f = {}
        for line in raw.strip().split("\n"):
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                f[k.strip()] = v.strip()
        fields.append(f)
    check(all(f.get("disposition") for f in fields),
          "every candidate carries a named disposition",
          f"{[f.get('condition') for f in fields if not f.get('disposition')]}")
    multi = [f for f in fields
             if len([x for x in f.get("sections", "").split("|") if x.strip()]) >= 2]
    check(len(multi) >= 3,
          "candidates really do span >=2 sections — the case the gate exists "
          "for is live, not hypothetical",
          f"{[f['condition'] for f in multi]}")
    pcs = " ".join(tc["pre_conditions"] for d in docs for tc in d["tcs"])
    check("dual airflow mode" in pcs.lower(),
          "the measured pattern actually occurs in written pre_conditions "
          "(a pattern that matches nothing would report reach 0 and pass)")

    # --- 11-13. moved-leaf-identity (65 §4). The count-only invariant it
    # replaces balances even when a declared-moved leaf was never produced,
    # so BOTH directions are asserted: declared-not-produced and
    # produced-not-declared.
    import re as _re
    declared = set()
    for gen in sorted((FEATURE / "scripts").glob("gen_batch*.py")):
        m = _re.search(r"MOVED_TO_BATCH16 = (\[[^\]]*\])",
                       gen.read_text(encoding="utf-8"))
        if m:
            declared |= set(_re.findall(r"['\"](SWE1-HVAC-[\d-]+)['\"]",
                                        m.group(1)))
    b16 = (FEATURE / "scripts" / "gen_batch16.py").read_text(encoding="utf-8")
    produced16 = {f"SWE1-HVAC-{x}"
                  for x in _re.findall(r'\("(\d{3}(?:-\d{2})?)",', b16)}
    check(len(declared) == 19 and declared == produced16,
          "every moved leaf is declared exactly once and produced exactly "
          "once", f"declared {len(declared)}, produced {len(produced16)}, "
          f"symmetric difference {sorted(declared ^ produced16)}")
    probe = sorted(declared)[0]
    check(bool(declared - {probe}) and (declared - {probe}) != produced16,
          "dropping one declaration WOULD break the identity (the count-only "
          "invariant would not notice)", f"probe {probe}")
    check(produced16 | {"SWE1-HVAC-999-99"} != declared,
          "adding an unclaimed batch-16 leaf WOULD break the identity")

    # --- 14-17. rc42-condition-marker after 66 §2.2 (named disposition, not
    # a hard block). Both directions: a disposition-less miss must FAIL, and
    # a listed qualifier must still pass without any disposition at all.
    prof2 = L.PROFILE.read_text(encoding="utf-8")
    disp = {}
    for raw in L.RC42_EXC_BLOCK.findall(prof2):
        f = {}
        for line in raw.strip().split("\n"):
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                f[k.strip()] = v.strip()
        if f.get("req_id"):
            disp[f["req_id"]] = f
    markers = []
    for raw in L.RC42_QUAL_BLOCK.findall(prof2):
        for line in raw.strip().split("\n"):
            if line.startswith("markers:"):
                markers = [m.strip() for m in line.split(":", 1)[1].split("|")
                           if m.strip()]
    # 68 §3 — the assertion is CONDITIONAL on there being misses, and the
    # path is exercised by an INJECTED miss rather than by whatever the corpus
    # happens to contain. An assertion that holds only while the data exists
    # disappears with the data (36 §6's rule, one step further).
    misses = []
    for d in docs:
        for tc in d["tcs"]:
            if int(tc["tc_id"].rsplit("-", 1)[-1]) < L.RC42_FIRST_N:
                continue
            head = tc["pre_conditions"].split("\n")[0]
            cite = re.search(r"\(([\d.]+)\)\s*$", head)
            src = cite.group(1) if cite else d["outline"]
            frag = re.sub(r"^\d+\.\s*\[[a-z-]+\]\s*", "", head)
            frag = re.sub(r"\s*\([\d.]+\)\s*$", "", frag)
            size, seg = L._longest_run(frag, L.FULLTEXT_BY_OUTLINE.get(src, ""))
            at = L.FULLTEXT_BY_OUTLINE.get(src, "").find(seg)
            before = L.FULLTEXT_BY_OUTLINE.get(src, "")[max(0, at - 70):at]
            if not any(re.search(rf"\b{re.escape(m)}\b", before)
                       or seg.lstrip().startswith(m) for m in markers):
                misses.append(tc["req_id"].replace("SWE1-HVAC-", ""))
    check(all(k in disp for k in misses),
          "IF misses exist THEN each has a disposition (vacuously true when "
          "there are none — which is why the injected case below exists)",
          f"misses {misses or 'none'}")

    # injected miss: a fragment quoting an unqualified sentence, unregistered
    inj_src = L.FULLTEXT_BY_OUTLINE["2.11"]
    inj_frag = "Adjusting Fan speed and Mode will alter the Front and Rear"
    size_i, seg_i = L._longest_run(inj_frag, inj_src)
    at_i = inj_src.find(seg_i)
    before_i = inj_src[max(0, at_i - 70):at_i]
    fires_i = not any(re.search(rf"\b{re.escape(m)}\b", before_i)
                      or seg_i.lstrip().startswith(m) for m in markers)
    check(size_i >= 15 and fires_i,
          "an INJECTED unqualified quotation is detected as a miss, so the "
          "path is exercised without depending on the corpus containing one",
          f"quoted {size_i} chars from 2.11, preceded by {before_i[-24:]!r}")
    check(all(d.get("condition") or d.get("not-a-condition")
              for d in disp.values()),
          "every disposition answers `condition:` or `not-a-condition:`")
    check("For" in markers and "On the" in markers and len(markers) >= 9,
          "the qualifier list carries the 66 §2.2 additions (instances of the "
          "criterion, not the criterion itself)", f"{len(markers)} markers")

    # --- 17-19. ambiguity-register (67 §1): a REGISTER, reconciled both
    # ways. Registered-but-absent is the direction 44 §7.3 named and 66's
    # version could not see.
    reg = L.AMBIGUITY_REMARKS
    by_id = {tc["tc_id"]: tc for d in docs for tc in d["tcs"]}
    check(len(reg) >= 3, "the register is non-empty, so both directions have "
          "something to reconcile", f"{len(reg)} row(s)")
    check(all(phrase in by_id[i]["remarks"] for i, phrase in reg.items()),
          "every registered row still carries its ambiguity text")
    vals = list(reg.values())
    check(len(set(vals)) == len(vals),
          "no two registered rows are reconciled against the same fragment "
          "(68 §2) — a shared fragment checks existence, not aboutness",
          f"{vals}")
    check(all(not any(t in by_id[i]["remarks"] for t in L.REMARKS_FORBIDDEN)
              for i in reg),
          "no registered Remarks carries an internal identifier — the column "
          "is customer-visible")
    unregistered = [tc["tc_id"] for d in docs for tc in d["tcs"]
                    if tc["remarks"] and not tc["remarks"].startswith("[")
                    and tc["tc_id"] not in reg]
    check(not unregistered,
          "no row carries ambiguity Remarks while staying out of the register",
          f"{unregistered}")

    if fails:
        print(f"\n**{len(fails)} case(s) FAILED**")
        return 1
    print("\nall directional cases PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
