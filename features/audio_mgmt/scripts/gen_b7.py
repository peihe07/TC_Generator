#!/usr/bin/env python3
"""Emit the B7 test cases for audio_mgmt — the final batch.

Anchors from package 26, verified by route 2. With B7 the 318-leaf scope is
covered: the difference set against framework.md is zero.

Usage:
    python features/audio_mgmt/scripts/gen_b7.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FUNC = "功能測試 (Functional based ; no specific technique)"
STATE = "狀態轉換 (State Transition Testing)"
DECISION = "決策表 (Decision Table Testing)"
BVA = "邊界值分析 (Boundary Value Analysis, BVA)"
NEGATIVE = "負向測試 (Negative / Invalid)"

PEND_SIG = ("PENDING: DR-AM4 signal not found in the supplied DBC; name kept "
            "as written in CFTS019 per R-13 (g)")

# Spec-sourced thresholds (package 26 section 2), all from 1.5.4 Variables.
HFP_MIN = "15 steps"          # 4867753
HFP_MIN_LATAM = "19 steps"    # 4867754
HFP_MAX = "38 steps"          # 4867752
NAV_MIN = "15 steps"          # 4867755

AUTHORED: dict[str, list[dict]] = {}


def tc(swe_id, purpose, proc, er, *, prio="P1", method=FUNC, pre="NA",
       data="NA", remarks="", reasoning="", desc=None):
    AUTHORED.setdefault(swe_id, []).append(dict(
        purpose=purpose, proc=proc, er=er, prio=prio, method=method, pre=pre,
        data=data, remarks=remarks, reasoning=reasoning, desc=desc))


# ------------------------------------------------ store and recall sequences
tc("SWE1_AMM_174",
   "Confirm the settings return once the speaker activation sequence ends",
   ["Play an Entertainment source with known volume, tone, fade and balance values",
    "Trigger a signal source that activates a loudspeaker",
    "Wait until the signal source ends",
    "Read the volume, tone, fade and balance values and record them"],
   ["Entertainment audio plays with the set values",
    "The signal source activates a loudspeaker",
    "The signal source ends",
    "The four settings are the values held before"],
   prio="P1", method=STATE,
   reasoning="Shares 4866662 with B4's leaf 176 across batches, declared under "
             "the package 22 section 3 procedure and approved at package 26 "
             "section 3. 176 observes the recall after a routing change; this "
             "row observes it after the speaker activation sequence, the two "
             "upstream decompositions of one recall sentence. All four "
             "settings are read because a partial restore is what the word "
             "settings guards against.")

tc("SWE1_AMM_177",
   "Confirm the settings are stored before audio reaches the loudspeaker",
   ["Play an Entertainment source with known volume, tone, fade and balance values",
    "Trigger a signal source that requires a loudspeaker",
    "Read the stored audio mode settings and record them"],
   ["Entertainment audio plays with the set values",
    "The signal source requires a loudspeaker",
    "The stored audio mode settings are the values held before it started"],
   prio="P1", method=STATE,
   reasoning="4866674 is the HALF-system store, written for HU and AMP "
             "together where the earlier sequences name the HU alone — which "
             "is what separates it from 171 and 173 in B6.")

tc("SWE1_AMM_178",
   "Confirm the stored settings return at the end of that same sequence",
   ["Play an Entertainment source with known volume, tone, fade and balance values",
    "Trigger a signal source that requires a loudspeaker",
    "Wait until the signal source is deactivated",
    "Read the volume, tone, fade and balance values and record them"],
   ["Entertainment audio plays with the set values",
    "The signal source requires a loudspeaker",
    "The signal source is deactivated",
    "The four settings are the values held before"],
   prio="P1", method=STATE,
   reasoning="4866677 is the recall that closes 177's sequence, confirmed by "
             "reading 4866675 to 4866680 as package 26 asked: the ramp-up, "
             "the ramp-down on deactivation, then this recall, all carrying "
             "the HU/AMP form.")

tc("SWE1_AMM_188",
   "Confirm every active source has its level stored when the mute request arrives",
   ["Play an Entertainment source and an Information source at known volume steps",
    "Send $TBMMuteReq$ = \"Mute\"",
    "Read the stored volume levels and record them"],
   ["Both sources play at their set steps",
    "$TBMMuteReq$ reports \"Mute\"",
    "The stored levels are those of both active sources"],
   prio="P1", method=STATE, remarks=PEND_SIG,
   reasoning="4866714 says all currently active sources, so the case runs two "
             "of them: storing one and dropping the other would pass a "
             "single-source check and lose a level on restore.")

# ------------------------------------------------ diagnostics and status
tc("SWE1_AMM_245",
   "Confirm an electrical fault on a loudspeaker line is detected and reported",
   ["Introduce an open circuit on a loudspeaker line",
    "Read the reported loudspeaker diagnostic and record it"],
   ["The loudspeaker line is open",
    "The loudspeaker diagnostic reports the fault"],
   prio="P1", method=FUNC,
   pre="The vehicle is configured with a Base audio system",
   reasoning="Partial coverage. 4867162 lists the electrical faults the head "
             "unit detects — open circuit, short to battery, short to ground, "
             "short between terminals — but says nothing about the "
             "initialisation timing the leaf gives for enabling the "
             "diagnostics, so the case observes detection and stops there. "
             "The open circuit is taken as the representative fault; the "
             "clause's list is not enumerated into four rows because the "
             "requirement is the detection, not the taxonomy.")

tc("SWE1_AMM_246",
   "Confirm the head unit follows the amplifier into the unavailable state and back",
   ["Send $AMPAudioStatus$ = \"Not_Available\"",
    "Read $HUAudioStatus$ and record it",
    "Send $AMPAudioStatus$ = \"Available\"",
    "Read $HUAudioStatus$ again and record it"],
   ["$AMPAudioStatus$ reports \"Not_Available\"",
    "$HUAudioStatus$ reports \"Not_Available\"",
    "$AMPAudioStatus$ reports \"Available\"",
    "$HUAudioStatus$ reports \"Available\""],
   prio="P1", method=STATE, remarks=PEND_SIG,
   pre="No audio source is active",
   reasoning="4867426 holds the head unit in the unavailable state until the "
             "amplifier recovers, so the case drives the signal back as well: "
             "a latch that never released would satisfy the first half. The "
             "anchor is the head-unit-side object; 4867177 states the "
             "amplifier side and is out of pool, so it is not the one.")

tc("SWE1_AMM_247",
   "Confirm the stored configuration comes back on each bus wake-up",
   ["Set the configuration settings to known values",
    "Put the vehicle through a bus sleep and wake cycle",
    "Read the configuration settings and record them"],
   ["The configuration settings hold the set values",
    "The bus wakes",
    "The configuration settings are the values stored before"],
   prio="P1", method=STATE, pre="No audio source is active",
   reasoning="4867457 is the head-unit clause; 4867458 and 4867459 say the "
             "same for the amplifier and the ANC, and this leaf is the head "
             "unit's, so those two are not it.")

# ------------------------------------------- sleep-resume volume thresholds
for sid, anchor, source, sig, rel, limit, value in (
        ("SWE1_AMM_297", "4866141", "Navigation", "NAV Volume", "below",
         "<NAV vol min>", NAV_MIN),
        ("SWE1_AMM_298", "4866142", "Phone", "Phone Volume", "below",
         "<HFP Vol Th min>", HFP_MIN),
        ("SWE1_AMM_300", "4866144", "Phone", "Phone Volume", "above",
         "<HFP Vol Th max>", HFP_MAX),
        ("SWE1_AMM_301", "4866145", "Ringer", "Ringer Volume", "below",
         "<HFP Vol Th min>", HFP_MIN),
        ("SWE1_AMM_302", "4866146", "Ringer", "Ringer Volume", "above",
         "<HFP Vol Th max>", HFP_MAX),
        ("SWE1_AMM_303", "4866147", "Voice Recognition", "VR Volume", "below",
         "<HFP Vol Th min>", HFP_MIN)):
    edge = "below" if rel == "below" else "above"
    tc(sid,
       f"Confirm a stored {source} level {edge} the limit is brought back to it",
       [f"Set the {source} volume to a step {edge} {value}",
        "Put the head unit through a sleep and resume cycle",
        f"Read the {source} volume step and record it"],
       [f"The {source} volume holds the set step",
        "The head unit resumes",
        f"The {source} volume step is {value}"],
       prio="P1", method=BVA, pre="No audio source is active",
       desc=(f"Upon exiting Sleep Mode, the Audio Management software shall "
             f"reset the stored {source} volume to {limit} when the stored "
             f"level is {edge} that limit"),
       reasoning=f"{anchor}, one of the seven consecutive sleep-resume clauses "
                 f"at 4866141 to 4866147. Each names a different source and a "
                 f"different limit, which is what separates them — the "
                 f"sentences are otherwise the same shape, and that is why "
                 f"the matcher collided on three of them. {limit} resolves at "
                 f"1.5.4 Variables to {value}, so the case carries the real "
                 f"figure. Written as a boundary case because the clause is a "
                 f"clamp. Out-of-pool anchor: the whole sleep-resume block is "
                 f"absent from the export, and none of it is a figure — a "
                 f"further instance for DR-AM3 in its corrected form "
                 f"(A-AM13).")

tc("SWE1_AMM_299",
   "Confirm a LATAM vehicle uses its own phone volume floor on resume",
   [f"Configure the vehicle market as LATAM",
    f"Set the Phone volume to a step below {HFP_MIN_LATAM}",
    "Put the head unit through a sleep and resume cycle",
    "Read the Phone volume step and record it"],
   ["The vehicle market is LATAM",
    "The Phone volume holds the set step",
    "The head unit resumes",
    f"The Phone volume step is {HFP_MIN_LATAM}"],
   prio="P1", method=BVA, pre="No audio source is active",
   desc=("Upon exiting Sleep Mode in a LATAM market vehicle, the Audio "
         "Management software shall reset the stored Phone volume to "
         "<HFP Vol Th min LATAM> when the stored level is below that limit"),
   reasoning="4866143 is the LATAM variant of 4866142, re-anchored at package "
             "26 after the matcher gave both leaves the same object. The two "
             "differ only in the market and the threshold — 19 steps at "
             "4867754 against 15 at 4867753 — so the market is established in "
             "step 1 rather than left to the reader. Out-of-pool anchor.")

# ------------------------------------------------------------ Logistic Mode
tc("SWE1_AMM_242",
   "Confirm entering logistic mode silences every output channel",
   ["Play an Entertainment source",
    "Enter Logistic Mode",
    "Record the audio on every output channel"],
   ["Entertainment audio plays",
    "Logistic Mode is active",
    "Every output channel is muted"],
   prio="P1", method=STATE,
   reasoning="4867027 mutes all output channels, so the case reads every one: "
             "a partial mute in a transport mode would leave audio in a "
             "vehicle that must be silent.")

tc("SWE1_AMM_243",
   "Confirm the audio status reports unavailable while logistic mode holds",
   ["Enter Logistic Mode",
    "Read $HUAudioStatus$ and record it"],
   ["Logistic Mode is active",
    "$HUAudioStatus$ reports \"Not_Available\""],
   prio="P1", method=STATE, remarks=PEND_SIG,
   pre="No audio source is active",
   reasoning="4867028 is the status half of the entry that 4867027 mutes. The "
             "exit is 244's own object, so the three form the mode's full "
             "cycle across three leaves.")

tc("SWE1_AMM_244",
   "Confirm leaving logistic mode restores audio output",
   ["Enter Logistic Mode",
    "Change the power mode from \"Logistic_Mode_ON\" to \"Standard_Power\"",
    "Play an Entertainment source",
    "Record the audio on the output channels"],
   ["Logistic Mode is active",
    "The power mode reports \"Standard_Power\"",
    "The Entertainment source starts",
    "The output channels carry the Entertainment audio"],
   prio="P1", method=STATE, remarks=PEND_SIG,
   pre="No audio source is active",
   reasoning="4867029 keys the exit on the power-mode transition rather than "
             "on any audio request, so the case drives the signal and then "
             "checks that audio is possible again — which is what closes the "
             "cycle 242 and 243 open.")


def main() -> None:
    ctx = {l["swe_id"]: l for l in json.loads(
        (ROOT / "batches" / "B7_context.json").read_text(encoding="utf-8"))}
    missing = sorted(k for k in ctx if k not in AUTHORED)
    extra = sorted(k for k in AUTHORED if k not in ctx)
    if missing or extra:
        sys.exit(f"leaves with no authored TC: {missing}; unknown: {extra}")

    tcs = []
    for swe_id, entries in AUTHORED.items():
        leaf = ctx[swe_id]
        for e in entries:
            if len(e["proc"]) != len(e["er"]):
                sys.exit(f"{swe_id}: {len(e['proc'])} steps vs {len(e['er'])}")
            desc = (e["desc"] or leaf["swe"]["description"]).rstrip().rstrip(".")
            refs = ("\n".join(f"CFTS019-{a}" for a in sorted(leaf["anchors"]))
                    if leaf["anchors"] else PEND_NOANCHOR)
            tcs.append({
                "req_id": swe_id,
                "test_group": "Audio Management",
                "test_set": leaf["test_set"],
                "test_item": f"{desc}\n\n({e['purpose']})",
                "pre_conditions": e["pre"],
                "input_test_data": e["data"],
                "test_procedure": "\n".join(
                    f"{i}. {s}" for i, s in enumerate(e["proc"], 1)),
                "expected_result": "\n".join(
                    f"{i}. {s}" for i, s in enumerate(e["er"], 1)),
                "spec_reference": refs,
                "priority": e["prio"],
                "design_method": e["method"],
                "remarks": e["remarks"],
                "reasoning": e["reasoning"],
            })

    # R-AM18: an out-of-pool anchor has no independent second corpus, so the
    # register marks it single-source rather than implying two routes agreed.
    out_of_pool = sorted(k for k, v in ctx.items()
                         if v["anchors"] and not v["anchor_in_pool"])
    unanchored = sorted(k for k, v in ctx.items() if not v["anchors"])
    out = {"batch": "B7", "feature": "Audio Management",
           "test_group": "Audio Management", "n_tcs": len(tcs),
           "leaves_authored": len(AUTHORED),
           "out_of_pool_anchors": [
               {"swe_id": k,
                # List the ids that are actually out of pool, not the first
                # anchor: a dual-anchor leaf can have one of each, and naming
                # the in-pool one reads as if the whole leaf were outside.
                "anchor": ", ".join(
                    f"CFTS019-{a}" for a in ctx[k]["anchors"]),
                "title": ctx[k]["swe"]["title"], "test_set": ctx[k]["test_set"],
                "corroboration": "single-source (R-AM18): the export omits "
                                 "this object, so route 2 had no independent "
                                 "corpus and could only re-read the full text"}
               for k in out_of_pool],
           "unanchored_leaves": unanchored,
           "tcs": tcs}
    dest = ROOT / "generated" / "B7.json"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2),
                    encoding="utf-8")
    print(f"wrote {dest.relative_to(ROOT.parent.parent)}")
    print(f"  leaves authored {len(AUTHORED)}")
    print(f"  TCs             {len(tcs)}")
    print(f"  out-of-pool     {len(out_of_pool)} (single-source, R-AM18)")
    print(f"  unanchored      {len(unanchored)} {unanchored}")


if __name__ == "__main__":
    main()
