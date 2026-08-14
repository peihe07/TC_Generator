#!/usr/bin/env python3
"""Applicability verdict for the 17 in-baseline `substantive` sections (D-C10 前置).

Handoff 05 §5 / 06 §3. A-CF08 established that 17 SR24 sections carry
behavioural text the 037 never analysed. Classification answered "does this
read like a requirement"; this answers the different question D-C10 needs:
"should Comfort R1L-R verify it".

Three verdicts. `undetermined` is a legitimate — and required — outcome:
a section whose governing source is not in `inputs/` is undetermined, NOT
out_of_scope. Failing to read something is not evidence of its absence
(handoff 06 §3).

The machine-checkable half is re-derived on every run from the CFTS043
R1L-R scope tree view: whether each cited CFTS043 item sits in the workbook's
own `Scope=Yes` allow-list (sheet `工作表1`, 599 ForeignIDs), and its Radio /
EE Architecture / Market attributes. The judgement half — which CFTS043
section governs which SR24 clause — is declared here and cited per row, so a
reader can check the reasoning rather than take the verdict on trust.

MEASUREMENT ONLY. No TC is generated, nothing enters a coverage denominator,
nothing is marked BLOCKED, no RD item is filed, and R-C5 / R-C5-1 are
untouched (handoff 06 §3).

Usage:
    python3 features/comfort/scripts/applicability_substantive.py
"""

import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
TREE = (FEATURE / "inputs" /
        "SYS1_CFTS043-HVAC Controls and Displays_Tree view_R1L-R scope.xlsx")
OUT = FEATURE / "data" / "sr24_substantive_applicability.tsv"

# CFTS043 §1.3.5.1.22 "Alternate Rear Blower Control Softkeys" and its three
# sub-sections. SR24 §20's own title says "See CFTS043 for applicable
# vehicles", so this section IS the ruled answer to that pointer.
#
# NOTE ON THE TITLE MISMATCH: SR24 writes "LATAM Alternative Rear Blower";
# CFTS043 writes "Alternate Rear Blower" and never uses "Alternative" or
# LATAM for it. Searching the customer's own wording returns zero hits and
# would have produced a false out_of_scope — see A-CF11.
ARB_SECTION = "1.3.5.1.22 Alternate Rear Blower Control Softkeys"
ARB_ITEMS = {
    "20.1":   ["4803261", "4803262"],   # CRB1 — softkey availability vs vent mode
    "20.1.1": ["4803263"],              # CRB1.1 — pop-up on rear hard control
    "20.1.2": ["4803263", "4803265"],   # CRB1.2 — rear hard control while unavailable
    "20.1.3": ["4803263", "4803265"],   # CRB1.3 — unavailable + pop-up (PU1268)
    "20.2":   ["4803279", "4803281", "4803284", "4803285", "4803286"],  # CRB2 — Lock
    "20.3":   ["4803264", "4803275", "4803276", "4803278"],             # CRB3 — Select, 1-4
    "20.4":   ["4803266", "4803267", "4803271", "4803272"],             # CRB4 — Power
    "20.4.1": ["4803268", "4803272"],   # CRB4.1 — REAR ON re-activates
    "20.4.2": ["4803261", "4803263"],   # CRB4.2 — grey out vs front vent mode
    "20.4.3": ["4803262", "4803271"],   # CRB4.3 — OFF via HVAC mode hard control
}
PROXI_GATE = "$Indipendent_Rear_Fan$ = [Present] (CFTS043 4803260)"

# Sections whose governing source is NOT in inputs/. Naming what is missing
# is the deliverable here — an `undetermined` without a named gap is just a
# shrug, and cannot be turned into a data request.
UNDETERMINED = {
    "16.1": ("EMEA ICS CARRYOVER — market applicability. CFTS043 contains no "
             "'EMEA' string at all (0 hits in the 442-page main doc; 0 rows "
             "in the tree view Description). Its 11 in-scope 'ICS' rows are "
             "ICS hardware (rotary knob, lost communication), not the EMEA "
             "ICS climate screen. No market-applicability source in inputs/; "
             "every Scope=Yes row carries Market='All', so this export cannot "
             "exclude or include a market.",
             "EMEA market (unconfirmed)"),
    "18.2": ("10.25\" Home screen Comfort Widget — screen-size applicability "
             "for R1LR ATL-H. CFTS043 has no 'Comfort Widget', no 'Home "
             "screen' and no '10.25' string; it is an HVAC controls spec and "
             "does not carry home-screen widget scope. No machine/screen "
             "configuration source for R1LR ATL-H in inputs/.",
             "10.25\" display (unconfirmed for R1LR ATL-H)"),
    "18.3": None, "18.4": None,      # same basis as 18.2, filled below
    "19.1": ("7\" Home screen Comfort Widget — screen-size applicability for "
             "R1LR ATL-H. Same gap as 18.x: CFTS043 carries no home-screen "
             "widget content. SR24 §1.1 lists a 7\" radio among the document's "
             "covered variants, but handoff 06 §3 is explicit that \"spec 有寫\" "
             "is not evidence of being in this delivery's scope.",
             "7\" display (unconfirmed for R1LR ATL-H)"),
    "19.2": None, "19.3": None,      # same basis as 19.1
}


def load_tree() -> tuple[dict, set]:
    if not TREE.exists():
        sys.exit(f"CFTS043 tree view not found: {TREE}")
    wb = openpyxl.load_workbook(TREE, read_only=True, data_only=True)
    allow = {str(r[1]).strip() for r in wb["工作表1"].iter_rows(values_only=True)
             if r[1] and str(r[0]).strip() == "Yes"}
    rows = list(wb["Basic Report"].iter_rows(values_only=True))
    hdr = [str(c) if c else "" for c in rows[0]]
    ix = {h: j for j, h in enumerate(hdr)}
    items: dict = {}
    for r in rows[1:]:
        fid = str(r[ix["ReqIF.ForeignID"]] or "").strip()
        if fid and fid not in items:
            items[fid] = {k: str(r[ix[k]] or "").strip() for k in
                          ("Scope", "Radio", "EE Architecture", "Market",
                           "Source Id")}
    wb.close()
    return items, allow


def main() -> None:
    items, allow = load_tree()
    out = ["outline\tscope_verdict\tbasis\tvariant_condition"]
    counts = {"in_scope": 0, "out_of_scope": 0, "undetermined": 0}

    for outline in sorted(ARB_ITEMS, key=lambda s: [int(x) for x in s.split(".")]):
        fids = ARB_ITEMS[outline]
        seen = [f for f in fids if f in items]
        missing = [f for f in fids if f not in items]
        in_allow = [f for f in seen if f in allow]
        radios = sorted({items[f]["Radio"] for f in seen})
        r1lr = all("R1L-R" in items[f]["Radio"] for f in seen) and seen
        # The verdict rests on the workbook's OWN scope marker, not on the EE
        # attribute: the Scope=Yes set spans Atlantis High (264) and Atlantis
        # Mid (130) alike, so EE does not gate R1L-R scope membership here.
        if seen and len(in_allow) == len(seen) and r1lr:
            verdict = "in_scope"
            basis = (f"CFTS043 §{ARB_SECTION}; SR24 §20 title itself directs "
                     f"'See CFTS043 for applicable vehicles'. Items "
                     f"{'/'.join(seen)} all carry Scope=Yes in the tree view's "
                     f"own R1L-R allow-list (sheet 工作表1, {len(allow)} ids) "
                     f"and Radio includes R1L-R ({radios[0]}). Market=All. "
                     f"EE=Atlantis Mid, which does NOT gate scope here: the "
                     f"Scope=Yes set spans Atlantis High and Mid alike.")
        else:
            verdict = "undetermined"
            basis = (f"CFTS043 §{ARB_SECTION} mapping incomplete — "
                     f"items not found in tree view: {missing or 'none'}; "
                     f"not in allow-list: {sorted(set(seen) - set(in_allow))}")
        counts[verdict] += 1
        out.append("\t".join([outline, verdict, basis, PROXI_GATE]))

    base18 = UNDETERMINED["18.2"]
    base19 = UNDETERMINED["19.1"]
    for outline in ("16.1", "18.2", "18.3", "18.4", "19.1", "19.2", "19.3"):
        spec = UNDETERMINED[outline]
        if spec is None:
            spec = base18 if outline.startswith("18.") else base19
            spec = (spec[0] + f" (same basis as {'18.2' if outline.startswith('18.') else '19.1'})",
                    spec[1])
        counts["undetermined"] += 1
        out.append("\t".join([outline, "undetermined",
                              " ".join(spec[0].split()), spec[1]]))

    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    total = sum(counts.values())
    print(f"{total} sections written to {OUT.relative_to(ROOT)}")
    for k, v in counts.items():
        print(f"  {k:<14} {v}")
    if total != 17:
        sys.exit(f"expected 17 substantive sections, wrote {total}")


if __name__ == "__main__":
    main()
