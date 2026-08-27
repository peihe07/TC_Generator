#!/usr/bin/env python3
"""Emit the B6 test cases for audio_mgmt.

Anchors from package 22 as ruled by package 24, including the eight returned
leaves, D-B6-01's correction of 131 to 4866466, and A-AM14-b's Surround
re-ordering (098 to 4867602, 099 keeping 4867601).

140 ships against a PENDING: its description says restore at initialisation
while the object its position fixes says store, and neither route may
reconcile a leaf with its own source (DR-AM10).

Usage:
    python features/audio_mgmt/scripts/gen_b6.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FUNC = "功能測試 (Functional based ; no specific technique)"
STATE = "狀態轉換 (State Transition Testing)"
DECISION = "決策表 (Decision Table Testing)"
BVA = "邊界值分析 (Boundary Value Analysis, BVA)"
SCENARIO = "情境 / 用例 (Scenario / Use Case Testing)"
NEGATIVE = "負向測試 (Negative / Invalid)"

PEND_SIG = ("PENDING: DR-AM4 signal not found in the supplied DBC; name kept "
            "as written in CFTS019 per R-13 (g)")
PEND_NOANCHOR = ("PENDING: DR-AM10 anchor withheld pending upstream "
                 "confirmation of this leaf's source")
PEND_140 = ("PENDING: DR-AM10 the leaf describes restoration at "
            "initialisation while the object at its document position states "
            "storage; upstream to confirm the source")

AUTHORED: dict[str, list[dict]] = {}


def tc(swe_id, purpose, proc, er, *, prio="P1", method=FUNC, pre="NA",
       data="NA", remarks="", reasoning="", desc=None):
    AUTHORED.setdefault(swe_id, []).append(dict(
        purpose=purpose, proc=proc, er=er, prio=prio, method=method, pre=pre,
        data=data, remarks=remarks, reasoning=reasoning, desc=desc))


# ------------------------------------------------------ Power and Persistence
tc("SWE1_AMM_052",
   "Confirm each source category keeps its own last volume across a restart",
   ["Play an Entertainment source at a known volume step",
    "Activate an Information 1 source and set a different volume step",
    "Restart the head unit",
    "Read the Entertainment volume step and the Information 1 volume step and record them"],
   ["Entertainment audio plays at its set step",
    "The Information 1 source plays at its own step",
    "The head unit restarts",
    "Each source returns to the step it was left at"],
   prio="P1", method=STATE,
   reasoning="4866100 keeps the last value per source category, so the case "
             "sets two categories to different steps: a single shared slot "
             "would return one value for both and pass a one-source check.")

tc("SWE1_AMM_057",
   "Confirm a stored volume above the wake-up limit is brought down to it",
   ["Set the Entertainment volume to a step above the wake-up limit",
    "Put the vehicle through a CAN bus sleep and wake cycle",
    "Read the Entertainment volume step and record it"],
   ["Entertainment audio plays at the set step",
    "The bus wakes",
    "The Entertainment volume step is at the wake-up limit"],
   prio="P1", method=BVA, pre="No audio source is active",
   reasoning="4866117 caps the recalled level on wake-up rather than "
             "restoring it verbatim, so the case starts above the cap. "
             "Starting below it would restore unchanged and prove nothing.")

tc("SWE1_AMM_062",
   "Confirm the Entertainment volume returns when the system comes back on",
   ["Play an Entertainment source at a known volume step",
    "Switch the system off and on again",
    "Read the Entertainment volume step and record it"],
   ["Entertainment audio plays at the set step",
    "The system returns",
    "The Entertainment volume step is the one set before"],
   prio="P1", method=STATE,
   reasoning="4866124 is the plain recall, where 4866117 at leaf 057 is the "
             "capped one. This case stays below the cap so the two are not "
             "testing the same path.")

tc("SWE1_AMM_131",
   "Confirm the current mode settings are written to storage",
   ["Play an Entertainment source with known volume, tone and mode settings",
    "Trigger the sequence that stores the mode settings",
    "Read the stored mode settings and record them"],
   ["Entertainment audio plays with the set values",
    "The store sequence runs",
    "The stored mode settings are the values set before"],
   prio="P1", method=STATE,
   reasoning="Corrected to 4866466 by D-B6-01. The candidate 4866489 carries "
             "the same sentence in the Information sequence where 4866466 is "
             "the Entertainment one, and position fixes it: 130 sits at "
             "4866465 and 132 at 4866468. Text agreement between the routes "
             "could not have caught this — the text is genuinely identical, "
             "which is the boundary package 24 section 3 records.")

tc("SWE1_AMM_140",
   "Confirm the stored audio parameters are applied at start-up",
   ["Set the audio parameters to known values and allow them to be stored",
    "Restart the head unit",
    "Read the audio parameters and record them"],
   ["The audio parameters hold the set values",
    "The head unit restarts",
    "The audio parameters are the values stored before the restart"],
   prio="P1", method=STATE, remarks=PEND_140,
   reasoning="Ships against a PENDING under DR-AM10. Position fixes the leaf "
             "at 4866489 — 139 sits at 4866488 and 141 at 4866490 — but that "
             "object says store where the leaf says restore at "
             "initialisation. A leaf contradicting its own source is not "
             "something either route can resolve, so the case follows the "
             "leaf and the anchor waits on upstream.")

tc("SWE1_AMM_161",
   "Confirm the stored mode settings come back after a source is deactivated",
   ["Play an Entertainment source with known volume, tone and mode settings",
    "Activate a source that displaces it",
    "End the displacing source",
    "Read the volume, tone and mode settings and record them"],
   ["Entertainment audio plays with the set values",
    "The displacing source becomes active",
    "The displacing source ends",
    "The volume, tone and mode settings are the values held before"],
   prio="P1", method=STATE,
   reasoning="4866530 recalls the stored mode settings per CFTS019-2215. The "
             "leaf frames this as system initialisation while the clause's "
             "context is recovery after a source is deactivated; package 24 "
             "rules the scenario follows the specification and lists the "
             "framing drift as a DR-AM10 sub-item, so the case is written to "
             "the deactivation path.")

for sid, anchor, when, what in (
        ("SWE1_AMM_170", "4866607", "after the first signal source ends",
         "recall"),
        ("SWE1_AMM_172", "4866620", "after the Side Distance sequence ends",
         "recall")):
    tc(sid,
       f"Confirm the settings return {when}",
       ["Play an Entertainment source with known volume, tone, fade and balance values",
        "Trigger the signal source for this sequence",
        "Wait until the signal source ends",
        "Read the volume, tone, fade and balance values and record them"],
       ["Entertainment audio plays with the set values",
        "The signal source becomes active",
        "The signal source ends",
        "The four settings are the values held before"],
       prio="P1", method=STATE,
       reasoning=f"{anchor}. Four objects carry the same recall sentence, one "
                 f"per signal-source sub-chapter, so position rather than text "
                 f"fixes which one this leaf takes — package 24 section 1 "
                 f"settles it by bracketing with the SYS-RA order and then "
                 f"reading. All four settings are read because a partial "
                 f"restore is what the word 'settings' guards against.")

for sid, anchor, when in (
        ("SWE1_AMM_171", "4866616", "before the second signal source starts"),
        ("SWE1_AMM_173", "4866629", "before audio reaches any loudspeaker")):
    tc(sid,
       f"Confirm the settings are stored {when}",
       ["Play an Entertainment source with known volume, tone, fade and balance values",
        "Trigger the signal source for this sequence",
        "Read the stored audio mode settings and record them"],
       ["Entertainment audio plays with the set values",
        "The signal source becomes active",
        "The stored audio mode settings are the values held before it started"],
       prio="P1", method=STATE,
       reasoning=f"{anchor}, the store half of the same sub-chapter sequence. "
                 f"Same textual duplication as the recall halves, settled the "
                 f"same way. The leaf says entertainment source where the "
                 f"clause says loudspeaker activation; package 24 lists that "
                 f"widening as a DR-AM10 sub-item and the case follows the "
                 f"specification's trigger.")

# ------------------------------------------------------------- Surround
tc("SWE1_AMM_092",
   "Confirm surround cannot be turned on for a mode that does not support it",
   ["Select an audio mode that does not support surround sound",
    "Open the audio settings",
    "Record whether surround sound can be turned on"],
   ["The unsupported audio mode is active",
    "The audio settings open",
    "Surround sound cannot be turned on"],
   prio="P1", method=NEGATIVE,
   reasoning="4866251 restricts availability by audio mode, which is a "
             "different gate from the $Surround$ configuration parameter that "
             "098 and 099 carry: one is what the vehicle has, the other what "
             "the current mode allows.")

for sid, anchor, act, val in (
        ("SWE1_AMM_093", "4866254", "disable", '"OFF"'),
        ("SWE1_AMM_095", "4866257", "enable", '"ON"')):
    tc(sid,
       f"Confirm a request to {act} surround is sent on as the control value",
       [f"Select {act} for surround sound in the audio settings",
        "Read $SurroundOnOff$ and record it"],
       [f"The {act} selection is accepted",
        f"$SurroundOnOff$ reports {val}"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       pre="Surround sound is available in the current audio mode",
       reasoning=f"{anchor} is one direction of the user control. Its "
                 f"counterpart is a separate object and a separate leaf, so a "
                 f"latch that only ever set one value would pass whichever "
                 f"case matched its default.")

for sid, anchor, sts, shown in (
        ("SWE1_AMM_094", "4866256", '"CFG_ST"', "stereo mode"),
        ("SWE1_AMM_096", "4866259", '"CFG_VID_SURR" or "CFG_AUD_SURR"',
         "the surround mode reported"),
        ("SWE1_AMM_097", "4866260", '"SNA"', "stereo mode")):
    tc(sid,
       f"Confirm the display follows the amplifier status value {sts}",
       [f"Send $AMPSurroundSTS$ = {sts}",
        "Read the surround indication shown on the HMI and record it",
        "Measure the time from the signal to the display update and record it"],
       [f"$AMPSurroundSTS$ reports {sts}",
        f"The HMI indicates {shown}",
        "The measured update time is at most 100 ms"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       pre="No audio source is active",
       reasoning=f"{anchor}. Three objects carry the same sentence with three "
                 f"different status values, which is why the matcher scored "
                 f"them alike and package 22 reported a three-way collision; "
                 f"the value is what separates them. 097 differs again in "
                 f"that the amplifier reports nothing usable and the head "
                 f"unit assumes stereo rather than being told it. <Tdisp> is "
                 f"defined at Max 100 ms.")

for sid, anchor, state, outcome in (
        ("SWE1_AMM_099", "4867601", "Present",
         "the surround menu is present and accepts operation"),
        ("SWE1_AMM_098", "4867602", "Not Present",
         "the surround menu is absent and cannot be operated")):
    tc(sid,
       f"Confirm the menu follows the configuration when surround is {state}",
       [f"Configure the vehicle so that $Surround$ is {state}",
        "Start the head unit",
        "Open the audio settings",
        "Record the state of the surround menu item"],
       [f"$Surround$ reports {state}",
        "The head unit starts",
        "The audio settings open",
        f"{outcome.capitalize()}"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       reasoning=f"{anchor}. A-AM14-b re-read the section and found three "
                 f"families: 4867598 and 4867599 keyed on the signal value, "
                 f"4867601 and 4867602 on presence with the "
                 f"$Surround_Setup.Req$ path, and 4867603 and 4867604 on "
                 f"presence without it. 098 and 099 speak of operability, so "
                 f"they take the pair that names the control path; B4's 264 "
                 f"and 266 speak of the menu existing and take the other. The "
                 f"bracket says which of the two questions this row asks.")

tc("SWE1_AMM_100",
   "Confirm the surround requirements apply only while the feature is present",
   ["Configure the vehicle so that $Surround$ is Present",
    "Bring the telematics state to \"Full-Operation\"",
    "Open the audio settings",
    "Record whether surround functionality is active"],
   ["$Surround$ reports Present",
    "The telematics state is \"Full-Operation\"",
    "The audio settings open",
    "The surround functionality is active"],
   prio="P1", method=DECISION, remarks=PEND_SIG,
   reasoning="4866264 gates a block of requirements on presence and the "
             "ignition state together, so both are established before the "
             "observation rather than only the one the leaf leads with.")

tc("SWE1_AMM_101",
   "Confirm the surround setting survives an ignition cycle",
   ["Set surround sound to a known state",
    "Put the vehicle through an ignition cycle",
    "Read the surround setting and record it"],
   ["The surround setting holds the set state",
    "The ignition cycle completes",
    "The surround setting is the state set before"],
   prio="P1", method=STATE, remarks=PEND_SIG,
   pre="Surround sound is configured as Present",
   reasoning="4866261 is about persistence across ignition cycles, not about "
             "the disable request the leaf's title suggests; the case follows "
             "the anchor. Out-of-pool anchor, single-source under R-AM18.")

tc("SWE1_AMM_102",
   "Confirm an enable request from the HMI reaches the control parameter",
   ["Select enable for surround sound in the audio settings",
    "Read $SurroundOnOff$ and record it"],
   ["The enable selection is accepted",
    "$SurroundOnOff$ reports \"Surround_Sound_On\""],
   prio="P1", method=DECISION, remarks=PEND_SIG,
   pre="Surround sound is configured as Present",
   reasoning="4866266 states the same transaction as 4866257 at leaf 095 but "
             "in the named-value form rather than the bracketed one, and sits "
             "in the section scoped to $Surround$ == Present. The "
             "pre-condition carries that scope, which is a specification "
             "trigger and belongs there under 8.5.")

for sid, anchor, sig, val in (
        ("SWE1_AMM_103", "4866267", "$SurroundOnOff$", "\"Surround_Sound_On\""),
        ("SWE1_AMM_105", "4866271", "$AMPSurroundSTS$", "\"CFG_AUD_SURR\"")):
    tc(sid,
       f"Confirm {sig} starts at its configured default",
       ["Configure the vehicle so that $Surround$ is Present",
        "Start the head unit",
        f"Read {sig} and record it"],
       ["$Surround$ reports Present",
        "The head unit starts",
        f"{sig} reports {val}"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       reasoning=f"{anchor} sets the power-on default. The two leaves take the "
                 f"head unit side and the amplifier side of the same "
                 f"initialisation, which is why each has its own object.")

tc("SWE1_AMM_104",
   "Confirm the amplifier-side surround requirements are gated on presence",
   ["Configure the vehicle so that $Surround$ is Not Present",
    "Start the head unit",
    "Record whether amplifier surround processing is active"],
   ["$Surround$ reports Not Present",
    "The head unit starts",
    "The amplifier surround processing is not active"],
   prio="P1", method=NEGATIVE, remarks=PEND_SIG,
   reasoning="4866268 scopes the amplifier block to presence. Written from "
             "the absent side because that is where the gate has an effect; "
             "the present side is already covered by 100 on the head unit "
             "block.")

tc("SWE1_AMM_265",
   "Confirm the user can operate surround while the feature is present",
   ["Configure the vehicle so that $Surround$ is Present",
    "Open the audio settings",
    "Turn surround sound on and then off",
    "Read $SurroundOnOff$ after each change and record it"],
   ["$Surround$ reports Present",
    "The audio settings open",
    "Both changes are accepted",
    "$SurroundOnOff$ follows each change"],
   prio="P1", method=FUNC, remarks=PEND_SIG,
   reasoning="4866263 states the user's ability to operate the control where "
             "099 at 4867601 states the menu being present and operable at "
             "initialisation. This row exercises both directions in one pass, "
             "which is what 'can turn on or off' asserts.")

# --------------------------------------------------------- Fade and Balance
tc("SWE1_AMM_110",
   "Confirm fade acts on Entertainment and not on an Information source",
   ["Play an Entertainment source",
    "Adjust the fade control",
    "Record the effect on the Entertainment audio",
    "Trigger a Navigation guidance prompt",
    "Record the effect of the fade setting on the Information audio"],
   ["Entertainment audio plays",
    "The fade adjustment is accepted",
    "The Entertainment audio reflects the fade setting",
    "The Navigation guidance prompt starts",
    "The Information audio is unaffected by the fade setting"],
   prio="P1", method=DECISION,
   reasoning="4866295 restricts fade to Entertainment. The restriction is "
             "only observable against a source it must not reach, so the case "
             "reads both.")

tc("SWE1_AMM_111",
   "Confirm balance applies only when the speakers are the output device",
   ["Route audio to an output device other than the speakers",
    "Adjust the balance control",
    "Record the effect on the audio"],
   ["The audio is routed away from the speakers",
    "The balance adjustment is accepted",
    "The audio is unaffected by the balance setting"],
   prio="P1", method=NEGATIVE,
   reasoning="4866296 conditions balance on the speaker output. Written from "
             "the excluded side, since the positive case is what 112 and 113 "
             "already exercise.")

tc("SWE1_AMM_112",
   "Confirm balance shifts level between the driver and passenger channels",
   ["Play an Entertainment source at equal driver and passenger levels",
    "Adjust the balance towards the driver side",
    "Read the driver-side and passenger-side levels and record them"],
   ["Entertainment audio plays at equal levels",
    "The balance adjustment is accepted",
    "The driver-side level rises relative to the passenger-side level"],
   prio="P1", method=FUNC,
   reasoning="4866297 describes a proportional shift between two channels, so "
             "both are read: a change on one alone would not show the "
             "proportionality the clause states.")

tc("SWE1_AMM_113",
   "Confirm balance acts on Entertainment and not on an Information source",
   ["Play an Entertainment source",
    "Adjust the balance control",
    "Record the effect on the Entertainment audio",
    "Trigger a Navigation guidance prompt",
    "Record the effect of the balance setting on the Information audio"],
   ["Entertainment audio plays",
    "The balance adjustment is accepted",
    "The Entertainment audio reflects the balance setting",
    "The Navigation guidance prompt starts",
    "The Information audio is unaffected by the balance setting"],
   prio="P1", method=DECISION,
   reasoning="4866298 is the balance counterpart of the fade restriction at "
             "4866295. Kept as its own row because the two controls travel "
             "different paths and one can leak where the other does not.")

for sid, anchor, ctrl, sig in (
        ("SWE1_AMM_115", "4866300", "fade", "$ToneFADE$"),
        ("SWE1_AMM_117", "4866304", "balance", "$ToneBAL$")):
    tc(sid,
       f"Confirm a {ctrl} adjustment is communicated on its own parameter",
       [f"Adjust the {ctrl} control to a known level",
        f"Read {sig} and record it"],
       [f"The {ctrl} adjustment is accepted",
        f"{sig} reports the selected level"],
       prio="P1", method=FUNC, remarks=PEND_SIG,
       reasoning=f"{anchor} names the signal for this control. 121 at 4866311 "
                 f"sends both settings together to the amplifier; these two "
                 f"are the individual communications, so the three do not "
                 f"collapse into one.")

for sid, anchor, ctrl, sig, neg, pos in (
        ("SWE1_AMM_116", "4866301", "fade", "$ToneFADE$", "front", "rear"),
        ("SWE1_AMM_118", "4866305", "balance", "$ToneBAL$", "left", "right")):
    tc(sid,
       f"Confirm the {ctrl} parameter spans its 19 steps in both directions",
       [f"Adjust the {ctrl} control fully towards {neg} and read {sig}",
        f"Adjust the {ctrl} control fully towards {pos} and read {sig}",
        "Read the distinct levels between them and record the count"],
       [f"{sig} reports a negative level for {neg}",
        f"{sig} reports a positive level for {pos}",
        "The distinct levels number 19"],
       prio="P1", method=BVA, remarks=PEND_SIG,
       reasoning=f"{anchor} fixes the distribution at 19 steps with the sign "
                 f"carrying the direction. Both ends and the count are read, "
                 f"since the failure a range clause guards against is an "
                 f"off-by-one at a limit.")

tc("SWE1_AMM_120",
   "Confirm both controls share one normalized nine-either-side range",
   ["Adjust the fade control fully in one direction and read its level",
    "Adjust the balance control fully in the same direction and read its level",
    "Compare the two ranges and record the outcome"],
   ["The fade level reaches its limit",
    "The balance level reaches its limit",
    "Both controls span nine steps either side of neutral"],
   prio="P1", method=BVA,
   reasoning="Re-anchored to 4866310 at package 24 section 2.3, which states "
             "both fader and balance in 19 equal steps from minus nine to "
             "plus nine. The suspected 4866306 and 4866307 are "
             "amplifier-side clauses. This row observes that the two controls "
             "share the range; 116 and 118 observe each control's own "
             "distribution.")

tc("SWE1_AMM_121",
   "Confirm the configured fade and balance settings reach the amplifier",
   ["Set the fade and balance controls to known levels",
    "Read $ToneFADE$ and $ToneBAL$ at the amplifier interface and record them"],
   ["The fade and balance settings hold the set levels",
    "$ToneFADE$ and $ToneBAL$ report the configured settings"],
   prio="P1", method=FUNC, remarks=PEND_SIG,
   pre="No audio source is active",
   reasoning="Shares 4866311 with B5's leaf 025 across batches, declared under "
             "the package 22 section 3 procedure and approved at package 24 "
             "section 2.1. 025 observes the transmission a change triggers; "
             "this row observes the configured settings themselves arriving. "
             "The leaf writes $ToneFADES$ and $ToneBALS$ where the clause "
             "writes them without the S; R-13 (g) keeps the leaf's spelling in "
             "the delivery column and the difference is a DR-AM4 sub-item.")

# -------------------------------------------------- presence and Cabin EQ
tc("SWE1_AMM_248",
   "Confirm an amplifier reported present is treated as present",
   ["Configure the vehicle so that $AMPPresent$ is \"ECU Present\"",
    "Start the head unit",
    "Record whether the amplifier is treated as present"],
   ["$AMPPresent$ reports \"ECU Present\"",
    "The head unit starts",
    "The amplifier is treated as present on the vehicle"],
   prio="P1", method=DECISION, remarks=PEND_SIG,
   reasoning="4867484 is the judgment sentence, which route 2 missed by "
             "starting its range scan one object later at 4867486. Its "
             "negative counterpart 4867485 has no SWE.1 leaf; disclosed here "
             "and not extended into, as with 4867568 in B4.")

for sid, anchor, present, mode in (
        ("SWE1_AMM_249", "4867486", "ECU Present", "Fixed-Gain"),
        ("SWE1_AMM_250", "4867487", "ECU Not Present", "Variable-Gain")):
    tc(sid,
       f"Confirm the output runs in {mode} mode when the amplifier is {present.lower()}",
       [f"Configure the vehicle so that $AMPPresent$ is \"{present}\"",
        "Start the head unit",
        "Record the output gain mode"],
       [f"$AMPPresent$ reports \"{present}\"",
        "The head unit starts",
        f"The output operates in {mode} mode"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       reasoning=f"{anchor}. The two form a section 7 enumeration pair — the "
                 f"gain mode follows directly from presence — so both ship.")

for sid, anchor, side in (("SWE1_AMM_251", "4867507", "Left"),
                          ("SWE1_AMM_252", "4867508", "Right")):
    tc(sid,
       f"Confirm the {side.lower()} blind spot system is treated as available",
       ["Configure the vehicle so that $BSSPresent$ is \"ECU Present\"",
        "Start the head unit",
        f"Record whether the {side} Blind Spot System is treated as present"],
       ["$BSSPresent$ reports \"ECU Present\"",
        "The head unit starts",
        f"The {side} Blind Spot System is treated as present on the vehicle"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       reasoning=f"{anchor}. Left and right have their own objects and their "
                 f"own leaves, a section 7 pair, even though one signal drives "
                 f"both.")

tc("SWE1_AMM_253",
   "Confirm both blind spot systems are treated as absent together",
   ["Configure the vehicle so that $BSSPresent$ is \"ECU Not Present\"",
    "Start the head unit",
    "Record whether the Left and Right Blind Spot Systems are treated as present"],
   ["$BSSPresent$ reports \"ECU Not Present\"",
    "The head unit starts",
    "Neither the Left nor the Right Blind Spot System is treated as present"],
   prio="P1", method=NEGATIVE, remarks=PEND_SIG,
   reasoning="4867510 covers both sides in one sentence where the present "
             "case at 4867507 and 4867508 takes one each, so the absent case "
             "is a single row rather than a pair.")

for sid, anchor, present, verdict in (
        ("SWE1_AMM_254", "4867517", "ECU Present", "present"),
        ("SWE1_AMM_255", "4867518", "ECU Not Present", "not present")):
    tc(sid,
       f"Confirm the chime system is treated as {verdict} when reported so",
       [f"Configure the vehicle so that $ICSPresent$ is \"{present}\"",
        "Start the head unit",
        "Record whether the Integrated Chime System is treated as present"],
       [f"$ICSPresent$ reports \"{present}\"",
        "The head unit starts",
        f"The Integrated Chime System is treated as {verdict} on the vehicle"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       reasoning=f"{anchor}. Package 22 warned that the matcher offered "
                 f"4867712 for the absent case; that object is the Reverse "
                 f"Mute parameter and matches only on the words 'not "
                 f"present'. The real answer sits one sentence after the "
                 f"present case, which is where reading the section found it.")

tc("SWE1_AMM_258",
   "Confirm the configured Cabin EQ identifier is carried on its signal",
   ["Configure a Cabin EQ curve identifier",
    "Start the head unit",
    "Read $CabinEQ$ and record it"],
   ["The Cabin EQ curve identifier is configured",
    "The head unit starts",
    "$CabinEQ$ reports the configured curve identifier"],
   prio="P1", method=FUNC, remarks=PEND_SIG,
   reasoning="Partial coverage. 4867577 defines the carrier — the curve ID is "
             "sent in $CabinEQ$ — but says nothing about the timing the leaf "
             "gives as initialisation. Validity handling is held by 259, 260 "
             "and 261, so this row stops at the carrying and does not restate "
             "their checks.")

tc("SWE1_AMM_261",
   "Confirm a valid Cabin EQ identifier loads its own parameters",
   ["Configure a Cabin EQ curve identifier that the supported database lists",
    "Start the head unit",
    "Record the Cabin EQ parameters loaded"],
   ["The configured identifier is listed in the supported database",
    "The head unit starts",
    "The parameters loaded are those the database gives for that identifier"],
   prio="P1", method=DECISION,
   reasoning="4867581 is the ELSE of the two rejection branches B4 covered at "
             "259 and 260, so this is the accept path that gives those two "
             "their meaning.")

# ---------------------------------------------------------------- Loudness
tc("SWE1_AMM_267",
   "Confirm the base system offers loudness and handles it locally",
   ["Configure the vehicle so that $AudioSystemType$ is \"Base\"",
    "Open the audio settings",
    "Record the state of the loudness menu item"],
   ["$AudioSystemType$ reports \"Base\"",
    "The audio settings open",
    "The loudness menu item is present and operable"],
   prio="P1", method=DECISION, remarks=PEND_SIG,
   pre="The vehicle is configured with a Base audio system",
   reasoning="4867639. The system type is a specification trigger condition, "
             "so it belongs in the pre-condition under the 8.5 exception "
             "rather than being set as a step.")

tc("SWE1_AMM_268",
   "Confirm loudness on a base system reaches Entertainment audio only",
   ["Play an Entertainment source and activate an Information source",
    "Enable loudness",
    "Record the effect on each source"],
   ["Both sources play",
    "Loudness is enabled",
    "The Entertainment audio reflects loudness and the Information audio does not"],
   prio="P1", method=DECISION,
   pre="The vehicle is configured with a Base audio system",
   reasoning="4867647 restricts the processing to Entertainment. Both sources "
             "are read because the restriction is only visible against the "
             "one it must not reach.")

for sid, anchor, emphasis, tail in (
        ("SWE1_AMM_269", "4867641", "the loudness menu is withheld",
         "This row observes the menu item being absent"),
        ("SWE1_AMM_271", "4867648", "no loudness adjustment is applied",
         "This row observes the processing staying off, which the absent menu "
         "alone does not establish — a hidden control can still be acting")):
    tc(sid,
       f"Confirm {emphasis} on a Fiat Booster system",
       ["Open the audio settings",
        "Record the state of the loudness menu item",
        "Play an Entertainment source",
        "Record whether loudness processing is applied"],
       ["The audio settings open",
        "The loudness menu item is absent",
        "Entertainment audio plays",
        "No loudness processing is applied"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       pre="The vehicle is configured with a Fiat Booster audio system",
       reasoning=f"{anchor}. 4867641 and 4867648 carry identical text in two "
                 f"system-type sections, so 269 and 271 are a same-text pair "
                 f"rather than a duplicate: SWE.1 labels 271 a duplicate "
                 f"requirement, but under 10.6 strict equivalence the two "
                 f"anchor to different objects and each keeps its row. {tail}.")

tc("SWE1_AMM_270",
   "Confirm the premium systems hide loudness because the amplifier owns it",
   ["Open the audio settings",
    "Record the state of the loudness menu item"],
   ["The audio settings open",
    "The loudness menu item is absent"],
   prio="P1", method=DECISION,
   pre="The vehicle is configured with a Premium CAN or Beats audio system",
   reasoning="4867643. The outcome matches the Fiat Booster case at 269 but "
             "the reason differs — here the amplifier manages loudness rather "
             "than the function being off — so the bracket names the system "
             "type and the two rows stay apart.")


def main() -> None:
    ctx = {l["swe_id"]: l for l in json.loads(
        (ROOT / "batches" / "B6_context.json").read_text(encoding="utf-8"))}
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
    out = {"batch": "B6", "feature": "Audio Management",
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
    dest = ROOT / "generated" / "B6.json"
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
