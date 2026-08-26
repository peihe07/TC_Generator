#!/usr/bin/env python3
"""Emit the B3 test cases for audio_mgmt.

Same contract as gen_b1/gen_b2: the verbatim upper half of each `test_item`
is read from `batches/B3_context.json`, never retyped. Anchors come from
package 12's ruled table.

Two leaves ship with no anchor at all (026, 076a): package 12 section 3.5
rules them PENDING against DR-AM1, so their spec_reference carries the
PENDING and the case is written to the SWE.1 description alone.

Usage:
    python features/audio_mgmt/scripts/gen_b3.py
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

TDISP = "at most 100 ms"        # CFTS019, <Tdisp> Max = 100 ms

PEND_SIG = ("PENDING: DR-AM4 signal not found in the supplied DBC; name kept "
            "as written in CFTS019 per R-13 (g)")
# Package 12 section 4.6 lists $ShiftLeverPosition$ among the names to keep
# unqualified, but the DBC does carry it — TRANSM_FD_4.ShiftLeverPosition,
# with a VAL_ table whose 2 = "R" matches the spec's [R]. Check P caught the
# discrepancy, so the reverse-mute cases write the qualified v3 (a) form and
# take no DR-AM4 note.
PEND_CFTS028 = ("PENDING: DR-AM9 VR request handling defined in CFTS028 and "
                "the VR HMI documentation, neither available")
PEND_NOANCHOR = "PENDING: DR-AM1 no CFTS019 object found for this leaf"

AUTHORED: dict[str, list[dict]] = {}


def tc(swe_id, purpose, proc, er, *, prio="P1", method=FUNC, pre="NA",
       data="NA", remarks="", reasoning="", desc=None):
    AUTHORED.setdefault(swe_id, []).append(dict(
        purpose=purpose, proc=proc, er=er, prio=prio, method=method, pre=pre,
        data=data, remarks=remarks, reasoning=reasoning, desc=desc))


# --------------------------------------------------------- Mute Requests 13
for sid, anchor, what, sig, val in (
        ("SWE1_AMM_185", "4866696", "Information 1 audio", "$VolumeINFO1$",
         "the restored level"),
        ("SWE1_AMM_186", "4866697", "Information 2 audio", "$VolumeINFO2$",
         "the restored level")):
    tc(sid,
       f"Confirm releasing the fleet mute restores the {what} within the display response time",
       [f"Play the {what} source and send $VSIMMuteReq$ = \"Mute\"",
        "Send $VSIMMuteReq$ = \"Unmute\"",
        f"Read {sig} and record it",
        "Measure the time from the request to the response and record it"],
       [f"The {what} is muted",
        "$VSIMMuteReq$ reports \"Unmute\"",
        f"{sig} reports {val}",
        f"The measured response time is {TDISP}"],
       prio="P1", method=STATE, remarks=PEND_SIG,
       reasoning=f"{anchor} is this path's member of the unmute group "
                 f"4866695-4866698, the counterpart of the mute group B2 "
                 f"covered. <Tdisp> is defined at Max = 100 ms, so the timing "
                 f"step carries a real bound.")

tc("SWE1_AMM_187",
   "Confirm releasing the fleet mute unmutes the hands-free microphone",
   ["Establish a hands-free call on a vehicle equipped with a hands-free microphone",
    "Send $VSIMMuteReq$ = \"Mute\"",
    "Send $VSIMMuteReq$ = \"Unmute\"",
    "Record the state of the hands-free microphone",
    "Measure the time from the request to the response and record it"],
   ["The hands-free call is active",
    "The hands-free microphone is muted",
    "$VSIMMuteReq$ reports \"Unmute\"",
    "The hands-free microphone is not muted",
    f"The measured response time is {TDISP}"],
   prio="P1", method=STATE, remarks=PEND_SIG,
   reasoning="4866698 closes the unmute group. The clause qualifies the "
             "microphone with if equipped, so the equipped vehicle is stated "
             "in step 1 rather than assumed.")

tc("SWE1_AMM_183",
   "Confirm the fleet mute request drives the Entertainment mute indication on the HMI",
   ["Play an Entertainment source",
    "Send $VSIMMuteReq$ = \"Mute\"",
    "Record the Entertainment mute indication shown on the HMI"],
   ["Entertainment audio plays",
    "$VSIMMuteReq$ reports \"Mute\"",
    "The HMI indicates that Entertainment audio is muted"],
   prio="P1", method=FUNC, remarks=PEND_SIG,
   reasoning="4866693 is the display member of the mute group 4866689-4866694, "
             "alongside the four audio paths B2 covered. It is the only member "
             "whose outcome is on the screen rather than in the audio.")

tc("SWE1_AMM_191",
   "Confirm the mute indication is raised while the telematics mute holds",
   ["Play an Entertainment source",
    "Trigger the TBM mute",
    "Read $ENTMuted$ and record it"],
   ["Entertainment audio plays",
    "The TBM mute is active",
    "$ENTMuted$ reports the muted state"],
   prio="P1", method=STATE, remarks=PEND_SIG,
   reasoning="4866717 is one step of the TBM mute sequence, the indication; "
             "190 carries the volume step of the same sequence and 195 the "
             "release. Each is a separate object, so each takes its own row.")

tc("SWE1_AMM_190",
   "Confirm the Entertainment volume signal is driven to zero by the telematics mute",
   ["Play an Entertainment source at a known volume step",
    "Trigger the TBM mute",
    "Read $VolumeENT$ and record it"],
   ["Entertainment audio plays at the set volume step",
    "The TBM mute is active",
    "$VolumeENT$ reports 0"],
   prio="P1", method=STATE, remarks=PEND_SIG,
   reasoning="4866716 is the volume step of the TBM sequence. Distinct from "
             "191's indication step: a system could raise the flag and leave "
             "the level untouched.")

for sid, anchor, path, sig in (("SWE1_AMM_192", "4866718", "Information 1",
                                "$VolumeINFO1$"),
                               ("SWE1_AMM_193", "4866719", "Information 2",
                                "$VolumeINFO2$")):
    tc(sid,
       f"Confirm a lower priority {path} source is driven to zero by the telematics mute",
       [f"Activate an {path} source that ranks below the TBM mute in priority",
        "Trigger the TBM mute",
        f"Read {sig} and record it"],
       [f"The {path} source is active",
        "The TBM mute is active",
        f"{sig} reports 0"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       pre="No audio source is active",
       reasoning=f"{anchor} conditions the suppression on the source ranking "
                 f"below the TBM mute, so the precondition names that ranking "
                 f"rather than any {path} source.")

tc("SWE1_AMM_195",
   "Confirm the mute indication clears when the telematics mute is released",
   ["Play an Entertainment source and trigger the TBM mute",
    "Release the TBM mute",
    "Read $ENTMuted$ and record it"],
   ["The Entertainment audio is muted",
    "The TBM mute is released",
    "$ENTMuted$ reports the unmuted state"],
   prio="P1", method=STATE, remarks=PEND_SIG,
   reasoning="4866727 is the ELSE branch closing the TBM sequence that 190 and "
             "191 open.")

tc("SWE1_AMM_288",
   "Confirm selecting reverse stores the volume and mutes Entertainment audio",
   ["Enable the reverse mute function and play an Entertainment source at a known volume step",
    "Send the signal $TRANSM_FD_4.ShiftLeverPosition$ = 2 (R)",
    "Record the state of the Entertainment audio",
    "Read $VolumeENT$ and record it"],
   ["Reverse mute is enabled and Entertainment audio plays at the set volume step",
    "$TRANSM_FD_4.ShiftLeverPosition$ = 2 (R) is received",
    "The Entertainment audio is muted",
    "$VolumeENT$ reports 0"],
   prio="P0", method=STATE, remarks=PEND_SIG,
   reasoning="4866823 opens the reverse-mute chain. Out-of-pool anchor: the "
             "export omits all of 1.3.3.12, so under R-AM18 this is single-"
             "source corroboration, not two independent routes.")

tc("SWE1_AMM_289",
   "Confirm voice recognition requests are ignored while reverse is selected",
   ["Enable the reverse mute function and send $TRANSM_FD_4.ShiftLeverPosition$ = 2 (R)",
    "Press the Voice Recognition button",
    "Record the state of the Voice Recognition session"],
   ["Reverse mute is enabled and $TRANSM_FD_4.ShiftLeverPosition$ = 2 (R) is received",
    "The Voice Recognition request is raised",
    "No Voice Recognition session starts"],
   prio="P1", method=NEGATIVE, remarks=PEND_SIG,
   reasoning="4866824 suppresses VR while in reverse. Written as a negative "
             "case because the observable outcome is the absence of a session. "
             "Out-of-pool anchor, single-source under R-AM18.")

tc("SWE1_AMM_290",
   "Confirm leaving reverse restores Entertainment audio at the recalled volume",
   ["Enable the reverse mute function and play an Entertainment source at a known volume step",
    "Send the signal $TRANSM_FD_4.ShiftLeverPosition$ = 2 (R)",
    "Send the signal $TRANSM_FD_4.ShiftLeverPosition$ = 4 (D)",
    "Record the state of the Entertainment audio",
    "Read $VolumeENT$ and record it"],
   ["Reverse mute is enabled and Entertainment audio plays at the set volume step",
    "The Entertainment audio is muted",
    "$TRANSM_FD_4.ShiftLeverPosition$ = 4 (D) is received",
    "The Entertainment audio is not muted",
    "$VolumeENT$ reports the volume step stored before the mute"],
   prio="P0", method=STATE, remarks=PEND_SIG,
   reasoning="4866825 is the release half of 4866823. The recalled level is "
             "what proves the store happened, so the case reads the volume "
             "rather than only the mute state. Out-of-pool, single-source "
             "under R-AM18.")

tc("SWE1_AMM_291",
   "Confirm voice recognition requests are accepted again after leaving reverse",
   ["Enable the reverse mute function and send $TRANSM_FD_4.ShiftLeverPosition$ = 2 (R)",
    "Send the signal $TRANSM_FD_4.ShiftLeverPosition$ = 4 (D)",
    "Press the Voice Recognition button",
    "Record the state of the Voice Recognition session"],
   ["Reverse mute is enabled and $TRANSM_FD_4.ShiftLeverPosition$ = 2 (R) is received",
    "$TRANSM_FD_4.ShiftLeverPosition$ = 4 (D) is received",
    "The Voice Recognition request is raised",
    "A Voice Recognition session starts"],
   prio="P1", method=STATE, remarks=f"{PEND_CFTS028}; {PEND_SIG}",
   reasoning="Partial coverage, ruled at package 12 section 3.4. 4866826 says "
             "VR requests resume according to CFTS028 and the VR HMI "
             "documentation, neither of which is available, so the case "
             "observes only that the suppression 289 established has lifted. "
             "Nothing about CFTS028's content is written. Out-of-pool, "
             "single-source under R-AM18.")

for sid, anchor, cond in (
        ("SWE1_AMM_295", "4867710",
         "$Reverse_Mute_Enable$ is configured as \"Disable\""),
        ("SWE1_AMM_296", "4867712",
         "$Reverse_Mute_Enable$ is not programmed")):
    tc(sid,
       f"Confirm reverse mute stays inactive when {cond.split(' is ')[1]}",
       [f"Configure the vehicle so that {cond}",
        "Play an Entertainment source",
        "Send the signal $TRANSM_FD_4.ShiftLeverPosition$ = 2 (R)",
        "Record the state of the Entertainment audio"],
       [f"The configuration is such that {cond}",
        "Entertainment audio plays",
        "$TRANSM_FD_4.ShiftLeverPosition$ = 2 (R) is received",
        "The Entertainment audio is not muted"],
       prio="P1", method=NEGATIVE, remarks=PEND_SIG,
       reasoning=f"{anchor} disables the whole reverse-mute behaviour. The two "
                 f"leaves take the two ways that happens — configured off, and "
                 f"absent altogether — which are different configuration "
                 f"states, not the same one described twice. Out-of-pool, "
                 f"single-source under R-AM18.")

# -------------------------------------------------------- Volume Control 37
tc("SWE1_AMM_026",
   "Confirm a volume increase request results in the target volume being applied",
   ["Play an Entertainment source at a known volume step",
    "Send a volume increase request",
    "Read the resulting volume step and record it"],
   ["Entertainment audio plays at the set volume step",
    "The volume increase request is accepted",
    "The resulting volume step is one step above the starting step"],
   prio="P1", method=FUNC, remarks=PEND_NOANCHOR,
   desc=("Upon receiving a volume increase request, the Audio Management "
         "software shall determine the requested target volume and transmit "
         "it to the HW audio interface"),
   reasoning="Ruled at package 12 section 3.5 to ship without an anchor. Both "
             "routes searched their own corpus and found nothing: target "
             "volume matches only 4866011 and 4866015, which define the ramp "
             "functions' linear travel, and package 12 bars substituting them "
             "because their verification object is ramp continuity, not the "
             "decision of a target. The case is written to the SWE.1 "
             "description alone and the spec_reference carries the PENDING.")

tc("SWE1_AMM_076",
   "Confirm a steering wheel volume request adjusts the Information source volume",
   ["Activate an Information source at a known volume step",
    "Send a steering wheel volume increase request",
    "Read the resulting Information source volume step and record it"],
   ["The Information source is active at the set volume step",
    "The steering wheel volume increase request is accepted",
    "The resulting volume step is one step above the starting step"],
   prio="P1", method=FUNC, remarks=PEND_NOANCHOR,
   pre="No audio source is active",
   reasoning="This is 076a, source SYS-RA-AMM-242; 076b, SYS-RA-AMM-246, "
             "shipped in B2 against 4866155. Both rows read SWE1_AMM_076 in "
             "the delivery column under R-AM6, and they are told apart by "
             "content and by anchor. Ruled to ship without an anchor at "
             "package 12 section 3.5: StWhl_Volume and steering wheel volume "
             "return nothing in either corpus, so the behaviour is likely "
             "specified in a separate steering-wheel-controls CFTS.")

tc("SWE1_AMM_044",
   "Confirm a tone control adjustment refreshes the equalizer display in time",
   ["Open the equalizer settings",
    "Adjust a tone control",
    "Record the equalizer display state",
    "Measure the time from the adjustment to the display update and record it"],
   ["The equalizer settings open",
    "The tone control adjustment is accepted",
    "The equalizer display shows the selected tone control value",
    f"The measured update time is {TDISP}"],
   prio="P1", method=FUNC,
   reasoning="4866082 bounds the update by <Tdisp>, defined at Max = 100 ms, "
             "so the timing step carries the real value rather than a "
             "placeholder.")

tc("SWE1_AMM_050",
   "Confirm the three source categories hold volume levels independently",
   ["Play an Entertainment source and an Information 1 source",
    "Adjust the Entertainment volume",
    "Read the Entertainment volume step and the Information 1 volume step and record them"],
   ["Both sources play",
    "The Entertainment volume adjustment is accepted",
    "The Entertainment volume step changes and the Information 1 volume step is unchanged"],
   prio="P1", method=FUNC,
   reasoning="Partial coverage, ruled at package 12 section 3.2. 4866112 "
             "refers the detail out to the Radio Performance Standard, which "
             "R-AM5 places outside this feature's scope and package 12 bars "
             "from being an anchor, so the case checks only that the "
             "categories are independent and writes none of that document's "
             "detail.")

tc("SWE1_AMM_051",
   "Confirm each source category exposes its own volume control",
   ["Play an Entertainment source",
    "Read the available volume controls and record them",
    "Activate an Information 1 source",
    "Read the available volume controls again and record them"],
   ["Entertainment audio plays",
    "A volume control for the Entertainment category is available",
    "The Information 1 source is active",
    "A volume control for the Information 1 category is available"],
   prio="P1", method=FUNC,
   reasoning="4866099 is about the controls being provided, where 4866112 at "
             "leaf 050 is about the levels being independent. Availability and "
             "independence are separate properties, so the two leaves do not "
             "collapse into one case.")

tc("SWE1_AMM_053",
   "Confirm a volume adjustment lands on the highest priority active source",
   ["Play an Entertainment source and activate an Information source",
    "Adjust the volume",
    "Read the Entertainment volume step and the Information volume step and record them"],
   ["Both sources are active",
    "The volume adjustment is accepted",
    "The Information source volume step changes and the Entertainment volume step is unchanged"],
   prio="P0", method=DECISION,
   reasoning="4866107 routes the adjustment to the highest priority active "
             "source. The case reads both levels because the requirement is as "
             "much about which source is left alone as about which one moves.")
tc("SWE1_AMM_053",
   "Confirm the adjustment falls back to the only active source when it is alone",
   ["Play an Entertainment source",
    "Adjust the volume",
    "Read the Entertainment volume step and record it"],
   ["Entertainment audio plays",
    "The volume adjustment is accepted",
    "The Entertainment volume step changes"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="The single-source case of 4866107. Separated from the contested "
             "case so a failure in the arbitration cannot hide behind the "
             "simple path working.")

for sid, purpose_tail, reason_tail in (
        ("SWE1_AMM_054", "is published when the user changes it",
         "This row observes the publication that follows a user adjustment"),
        ("SWE1_AMM_065", "tracks every supported volume-control input",
         "This row observes that the same signal follows an input other than "
         "the front-panel control, which is what synchronisation adds over "
         "publication")):
    tc(sid,
       f"Confirm the Entertainment volume signal {purpose_tail}",
       ["Play an Entertainment source at a known volume step",
        "Adjust the Entertainment volume",
        "Read $VolumeENT$ and record it"],
       ["Entertainment audio plays at the set volume step",
        "The volume adjustment is accepted",
        "$VolumeENT$ reports the adjusted volume step"],
       prio="P1", method=FUNC, remarks=PEND_SIG,
       reasoning=f"054 and 065 share 4866113 under R-AM16, the upstream having "
                 f"split one requirement into two leaves. {reason_tail}, so "
                 f"the two brackets state different emphases as that ruling "
                 f"requires.")

for sid, anchor, path, sig in (("SWE1_AMM_055", "4866152", "Information 1",
                                "$VolumeINFO1$"),
                               ("SWE1_AMM_056", "4866153", "Information 2",
                                "$VolumeINFO2$")):
    tc(sid,
       f"Confirm the {path} volume is transmitted on every change",
       [f"Activate an {path} source at a known volume step",
        f"Adjust the {path} volume",
        f"Read {sig} and record it"],
       [f"The {path} source is active at the set volume step",
        "The volume adjustment is accepted",
        f"{sig} reports the adjusted volume step"],
       prio="P1", method=FUNC, remarks=PEND_SIG,
       pre="No audio source is active",
       reasoning=f"Re-anchored to {anchor} per package 12 section 3.3b. The "
                 f"earlier candidate was a table lookup defining the signal's "
                 f"value, not a behaviour; {anchor} is the transmission "
                 f"clause — send the volume every time it changes — which is "
                 f"what the leaf describes.")

tc("SWE1_AMM_063",
   "Confirm the volume knob adjusts an active Entertainment source in full operation",
   ["Set TLM_Status.Info to \"Full-Operation\" and play an Entertainment source",
    "Turn the volume knob",
    "Read the Entertainment volume step and record it"],
   ["TLM_Status.Info reports \"Full-Operation\" and Entertainment audio plays",
    "The knob adjustment is accepted",
    "The Entertainment volume step changes"],
   prio="P1", method=DECISION, pre="No audio source is active",
   reasoning="4866126 gates the knob on the telematics state and on an "
             "Entertainment source being active. This takes the Full-Operation "
             "state; the second case takes Timed, the other state the clause "
             "names.")
tc("SWE1_AMM_063",
   "Confirm the same knob handling applies in the timed state",
   ["Set TLM_Status.Info to \"Timed\" and play an Entertainment source",
    "Turn the volume knob",
    "Read the Entertainment volume step and record it"],
   ["TLM_Status.Info reports \"Timed\" and Entertainment audio plays",
    "The knob adjustment is accepted",
    "The Entertainment volume step changes"],
   prio="P1", method=DECISION, pre="No audio source is active",
   reasoning="Second state enumerated at 4866126.")

tc("SWE1_AMM_064",
   "Confirm the telematics volume up and down messages adjust Entertainment volume",
   ["Play an Entertainment source at a known volume step",
    "Send TLM_Vol_UP_Status.Info = \"Pressed\"",
    "Read the Entertainment volume step and record it",
    "Send TLM_Vol_DOWN_Status.Info = \"Pressed\"",
    "Read the Entertainment volume step again and record it"],
   ["Entertainment audio plays at the set volume step",
    "TLM_Vol_UP_Status.Info reports \"Pressed\"",
    "The Entertainment volume step is above the starting step",
    "TLM_Vol_DOWN_Status.Info reports \"Pressed\"",
    "The Entertainment volume step returns to the starting step"],
   prio="P1", method=FUNC,
   reasoning="4866127 names both messages, so both are exercised in one case: "
             "the down request returning the level to where the up request "
             "found it is a stronger observation than either alone.")

tc("SWE1_AMM_067",
   "Confirm reaching minimum volume attenuates without interrupting the source",
   ["Play an Entertainment source",
    "Adjust the Entertainment volume down to the minimum step",
    "Read the transport state of the Entertainment source and record it",
    "Read $VolumeENT$ and record it"],
   ["Entertainment audio plays",
    "The Entertainment volume is at the minimum step",
    "The Entertainment source reports the playing state",
    "$VolumeENT$ reports the minimum value"],
   prio="P1", method=BVA, remarks=PEND_SIG,
   reasoning="4866130 is the bottom boundary of the volume range, where the "
             "behaviour could plausibly change to a stop. The transport state "
             "is read for the same reason 315 reads it in B2: a system that "
             "paused the source would satisfy the level observation and still "
             "be wrong.")

for sid, emphasis, reason_tail in (
        ("SWE1_AMM_072", "each active Information source keeps its own level",
         "This row observes the independence between two concurrently active "
         "Information sources"),
        ("SWE1_AMM_075", "the knob reaches an active Information source",
         "This row observes the input path — the knob acting on an Information "
         "source at all — which independence alone does not establish")):
    tc(sid,
       f"Confirm {emphasis}",
       ["Set TLM_Status.Info to \"Full-Operation\" and activate an Information 1 source and an Information 2 source",
        "Adjust the Information 1 volume with the knob",
        "Read the Information 1 volume step and the Information 2 volume step and record them"],
       ["TLM_Status.Info reports \"Full-Operation\" and both Information sources are active",
        "The knob adjustment is accepted",
        "The Information 1 volume step changes and the Information 2 volume step is unchanged"],
       prio="P1", method=DECISION, pre="No audio source is active",
       desc=("The Audio Management software shall maintain independent volume "
             "control for concurrently active Information audio sources and "
             "apply a volume or mute adjustment to the identified source"),
       reasoning=f"072 and 075 share 4866150 under R-AM16 after the re-anchor "
                 f"at package 12 section 3.3b. {reason_tail}, so the brackets "
                 f"differ as that ruling requires.")

for sid, anchor, path, sig in (("SWE1_AMM_073", "4866148", "Information 1",
                                "$VolumeINFO1$"),
                               ("SWE1_AMM_074", "4866149", "Information 2",
                                "$VolumeINFO2$")):
    tc(sid,
       f"Confirm the {path} level is transmitted on the vehicle bus",
       [f"Activate an {path} source at a known volume step",
        f"Read {sig} from the vehicle bus and record it"],
       [f"The {path} source is active at the set volume step",
        f"{sig} reports the current {path} volume level"],
       prio="P1", method=FUNC, remarks=PEND_SIG,
       pre="No audio source is active",
       reasoning=f"{anchor} is about the level being present on the bus, where "
                 f"the 4866152 family at leaves 055 and 056 is about it being "
                 f"sent on change. Steady-state presence and change-driven "
                 f"transmission are different observations.")

tc("SWE1_AMM_077",
   "Confirm an Information source at minimum volume transmits the minimum value",
   ["Activate an Information 1 source",
    "Adjust the Information 1 volume down to the minimum step",
    "Read $VolumeINFO1$ and record it"],
   ["The Information 1 source is active",
    "The Information 1 volume is at the minimum step",
    "$VolumeINFO1$ reports the minimum value"],
   prio="P1", method=BVA, remarks=PEND_SIG, pre="No audio source is active",
   reasoning="4866156 is the Information-side counterpart of the Entertainment "
             "minimum at 4866130, and a boundary case for the same reason.")

tc("SWE1_AMM_081",
   "Confirm a NAFTA vehicle starts with speed controlled volume off",
   ["Configure the vehicle market as NAFTA",
    "Start the head unit",
    "Read the speed controlled volume setting and record it"],
   ["The vehicle market is NAFTA",
    "The head unit starts",
    "The speed controlled volume setting is \"Off\""],
   prio="P1", method=DECISION,
   reasoning="4866212 and 4866213 are a market enumeration pair that package "
             "12 section 4.4 requires to ship together — the default differs "
             "by market, so shipping one alone would leave the other default "
             "untested and the pairing invisible in the workbook.")

tc("SWE1_AMM_082",
   "Confirm a non-NAFTA vehicle starts with speed controlled volume at level 1",
   ["Configure the vehicle market as a non-NAFTA market",
    "Start the head unit",
    "Read the speed controlled volume setting and record it"],
   ["The vehicle market is a non-NAFTA market",
    "The head unit starts",
    "The speed controlled volume setting is \"Level 1\""],
   prio="P1", method=DECISION,
   reasoning="The other half of the 4866212/4866213 market pair.")

tc("SWE1_AMM_083",
   "Confirm speed controlled volume stays enabled through a phone call",
   ["Set the speed controlled volume to a level other than off",
    "Establish a hands-free call",
    "Read the speed controlled volume setting and record it"],
   ["The speed controlled volume setting is not off",
    "The hands-free call audio is active",
    "The speed controlled volume setting is unchanged"],
   prio="P1", method=NEGATIVE, pre="No call is in progress",
   reasoning="4866214 states what must not happen, so the case is negative: a "
             "system that suspended the function during calls would look "
             "correct in every positive SCV case and fail only here.")

for sid, emphasis, reason_tail in (
        ("SWE1_AMM_084", "the supported levels are offered for selection",
         "This row observes the range of choices the HMI presents"),
        ("SWE1_AMM_091", "a level change made in full operation is accepted",
         "This row observes the change being processed under the ignition "
         "states the leaf names, which the availability of the choices does "
         "not establish")):
    tc(sid,
       f"Confirm {emphasis}",
       ["Open the speed controlled volume settings",
        "Read the offered settings and record them",
        "Select \"Level 2\"",
        "Read the speed controlled volume setting and record it"],
       ["The speed controlled volume settings open",
        "The offered settings are \"Off\", \"Level 1\", \"Level 2\" and \"Level 3\"",
        "The selection is accepted",
        "The speed controlled volume setting is \"Level 2\""],
       prio="P1", method=DECISION,
       desc=("The Audio Management software shall provide an HMI interface "
             "that allows the user to select one of the supported Speed "
             "Controlled Volume (SCV) levels"),
       reasoning=f"084 and 091 share 4866215 under R-AM16. {reason_tail}, so "
                 f"the brackets carry different emphases as that ruling "
                 f"requires.")

tc("SWE1_AMM_085",
   "Confirm a new speed controlled volume level is published and shown",
   ["Open the speed controlled volume settings",
    "Select a level other than the current one",
    "Read $VolumeSCV$ and record it",
    "Read the speed controlled volume setting shown on the HMI and record it"],
   ["The speed controlled volume settings open",
    "The selection is accepted",
    "$VolumeSCV$ reports the selected level",
    "The HMI shows the selected level"],
   prio="P1", method=FUNC, remarks=PEND_SIG,
   reasoning="4866216 requires the signal and the display to move together, so "
             "both are read: a system that updated the screen without sending "
             "the signal would pass a display-only check.")

tc("SWE1_AMM_087",
   "Confirm volume and mute handling follows the configured HMI behaviour",
   ["Play an Entertainment source",
    "Adjust the volume and then apply a mute",
    "Record the volume and mute behaviour against the configured HMI specification"],
   ["Entertainment audio plays",
    "The adjustment and the mute are accepted",
    "The volume and mute behaviour matches the configured HMI specification"],
   prio="P1", method=FUNC,
   reasoning="Partial coverage, ruled at package 12 section 3.1. 4866221 is "
             "taken over the near-identical 4866223 because only 4866221 names "
             "the HU HMI Specification alongside the routing table, and the "
             "leaf requires both. The routing table is an external document, "
             "so no specific routing correspondence is written; that goes to "
             "DR-AM1.")

tc("SWE1_AMM_088",
   "Confirm the user can turn speed controlled volume on and off in full operation",
   ["Set TLM_Status.Info to \"Full-Operation\"",
    "Send SVC_Setup.Req = \"Disable\"",
    "Read the speed controlled volume state and record it",
    "Send SVC_Setup.Req to a value other than \"Disable\"",
    "Read the speed controlled volume state again and record it"],
   ["TLM_Status.Info reports \"Full-Operation\"",
    "SVC_Setup.Req reports \"Disable\"",
    "The speed controlled volume function is disabled",
    "SVC_Setup.Req reports a value other than \"Disable\"",
    "The speed controlled volume function is enabled"],
   prio="P1", method=DECISION, pre="No audio source is active",
   reasoning="Re-anchored to 4866230 per package 12 section 3.2 after route 2 "
             "found the original 4866309 to be about fader and balance. The "
             "two are structurally parallel sentences — same ignition scoping, "
             "same user-can-adjust shape, different function — which is how "
             "they came to be swapped. This leaf is the user's permission to "
             "switch the function; 089 and 090 are what the system does with "
             "each setting.")

tc("SWE1_AMM_089",
   "Confirm disabling speed controlled volume drives the signal to off",
   ["Send SVC_Setup.Req = \"Disable\"",
    "Read $VolumeSCV$ and record it",
    "Read the speed controlled volume state shown on the HMI and record it"],
   ["SVC_Setup.Req reports \"Disable\"",
    "$VolumeSCV$ reports \"Off\"",
    "The HMI shows the speed controlled volume function as disabled"],
   prio="P1", method=DECISION, remarks=PEND_SIG,
   reasoning="4866232 is the disable branch; 090 is the enable branch at "
             "4866233. The two are the IF and ELSE of one decision, so each "
             "takes a row and neither can stand for the other.")

tc("SWE1_AMM_090",
   "Confirm enabling speed controlled volume publishes the user's level",
   ["Select \"Level 2\" as the speed controlled volume level",
    "Send SVC_Setup.Req to a value other than \"Disable\"",
    "Read $VolumeSCV$ and record it"],
   ["The speed controlled volume level is \"Level 2\"",
    "SVC_Setup.Req reports a value other than \"Disable\"",
    "$VolumeSCV$ reports \"Level_2\""],
   prio="P1", method=DECISION, remarks=PEND_SIG,
   reasoning="The enable branch of 4866232/4866233. The published value has to "
             "follow the user's selection rather than a fixed default, so the "
             "case sets a level first.")

for sid, anchor, emphasis, reason_tail in (
        ("SWE1_AMM_114", "4866299", "a fade adjustment refreshes the display in time",
         "the fade control"),
        ("SWE1_AMM_119", "4866308", "a balance adjustment keeps the display in step",
         "the balance control")):
    tc(sid,
       f"Confirm {emphasis}",
       [f"Open the fade and balance settings",
        f"Adjust {reason_tail}",
        "Read the fade and balance display and record it",
        "Measure the time from the adjustment to the display update and record it"],
       ["The fade and balance settings open",
        "The adjustment is accepted",
        f"The display shows the adjusted value for {reason_tail}",
        f"The measured update time is {TDISP}"],
       prio="P1", method=FUNC,
       reasoning=f"{anchor} is one of a same-text pair — 4866299 and 4866308 "
                 f"are word for word identical and sit in different chapters. "
                 f"Package 12 section 4.3 requires the bracket to carry the "
                 f"difference, so each row takes one of the two controls the "
                 f"clause names. <Tdisp> is defined at Max = 100 ms.")

tc("SWE1_AMM_141",
   "Confirm display settings survive a restart",
   ["Change a display setting",
    "Restart the head unit",
    "Read the display setting and record it"],
   ["The display setting change is accepted",
    "The head unit restarts",
    "The display setting is the value set before the restart"],
   prio="P1", method=STATE,
   reasoning="4866490 says the settings are stored; the leaf adds restoring "
             "them at the next initialisation, and a restart is the only way "
             "to observe that the store was persistent rather than in memory. "
             "Package 12 section 4.2 notes 4866467 carries the same sentence "
             "in another sequence; this leaf takes 4866490 and the batch does "
             "not extend to the other.")

tc("SWE1_AMM_147",
   "Confirm an Information source returns at the volume it was last given",
   ["Activate an Information source and set its volume to a known step",
    "End the Information source",
    "Activate the same Information source again",
    "Read the Information source volume step and record it"],
   ["The Information source is active at the set volume step",
    "The Information source ends",
    "The Information source is active again",
    "The Information source volume step is the step set before it ended"],
   prio="P1", method=STATE, pre="No audio source is active",
   reasoning="Re-anchored per package 12 section 3.3 to cite both halves: "
             "4866527 stores the level and 4866878 recalls and sends the last "
             "used level when the source becomes active. Neither alone covers "
             "the leaf, and 4866526, the sequence header the earlier candidate "
             "used, is not an anchor for any leaf. 4866878 is out of pool, so "
             "that half is single-source under R-AM18.")

for sid, anchor, path, sig in (("SWE1_AMM_150", "4866114", "Information 1",
                                "$VolumeINFO1$"),
                               ("SWE1_AMM_153", "4866115", "Information 2",
                                "$VolumeINFO2$")):
    tc(sid,
       f"Confirm activating an {path} source publishes its current volume",
       [f"Activate an {path} source",
        f"Read {sig} and record it"],
       [f"The {path} source is active",
        f"{sig} reports the current {path} volume level"],
       prio="P1", method=FUNC, remarks=PEND_SIG,
       pre="No audio source is active",
       reasoning=f"{anchor} ties the signal to a user adjustment of that "
                 f"category's controls. The case observes it at activation "
                 f"because that is the point the leaf names alongside "
                 f"adjustment.")

tc("SWE1_AMM_158",
   "Confirm a volume change is written to persistent storage",
   ["Play an audio source and set the volume to a known step",
    "Restart the head unit",
    "Read the volume step and record it"],
   ["The audio source plays at the set volume step",
    "The head unit restarts",
    "The volume step is the step set before the restart"],
   prio="P1", method=STATE,
   reasoning="158 and 147 both draw on 4866527. This row observes persistence "
             "across a restart, where 147 observes recall when a source "
             "becomes active again — different lifetimes, so the brackets "
             "differ as R-AM16 requires.")


# ------------------------------------------------------- density pass
# Added only where the clause carries a branch, a list member or a direction
# the first pass covered once. Each names a behaviour that can fail while its
# siblings pass; bracket tails stay distinct per R-S4.

for sid, path, sig in (("SWE1_AMM_185", "Information 1", "$VolumeINFO1$"),
                       ("SWE1_AMM_186", "Information 2", "$VolumeINFO2$")):
    tc(sid,
       f"Confirm the {path} release is withheld while another mute reason is active",
       [f"Play the {path} source and send $VSIMMuteReq$ = \"Mute\"",
        "Raise a second mute condition",
        "Send $VSIMMuteReq$ = \"Unmute\"",
        f"Read {sig} and record it"],
       [f"The {path} audio is muted",
        "The second mute condition is active",
        "$VSIMMuteReq$ reports \"Unmute\"",
        f"{sig} reports 0"],
       prio="P1", method=NEGATIVE, remarks=PEND_SIG,
       reasoning="The guard on the unmute group is if no other reasons to mute "
                 "are active. A system that released on the transition alone "
                 "would pass the plain case and drop audio protection here.")

tc("SWE1_AMM_051",
   "Confirm the Information 2 category also carries its own volume control",
   ["Activate an Information 2 source",
    "Read the available volume controls and record them"],
   ["The Information 2 source is active",
    "A volume control for the Information 2 category is available"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="4866099 names three categories. The first case covers "
             "Entertainment and Information 1; this covers the third, since a "
             "system could expose two and omit the third.")

tc("SWE1_AMM_067",
   "Confirm a further decrease at minimum volume does not go below the floor",
   ["Play an Entertainment source at the minimum volume step",
    "Send a further volume decrease request",
    "Read $VolumeENT$ and record it"],
   ["Entertainment audio plays at the minimum volume step",
    "The volume decrease request is accepted",
    "$VolumeENT$ reports the minimum value"],
   prio="P1", method=BVA, remarks=PEND_SIG,
   reasoning="The lower bound at 4866130 read from below: the first case "
             "arrives at the minimum, this one pushes past it. An off-by-one "
             "in the clamp shows up here and nowhere else.")

tc("SWE1_AMM_077",
   "Confirm an Information 2 source at minimum volume transmits the minimum value",
   ["Activate an Information 2 source",
    "Adjust the Information 2 volume down to the minimum step",
    "Read $VolumeINFO2$ and record it"],
   ["The Information 2 source is active",
    "The Information 2 volume is at the minimum step",
    "$VolumeINFO2$ reports the minimum value"],
   prio="P1", method=BVA, remarks=PEND_SIG, pre="No audio source is active",
   reasoning="4866156 covers both Information paths; the first case takes "
             "Information 1 and this takes Information 2.")

tc("SWE1_AMM_147",
   "Confirm each Information source recalls its own stored level",
   ["Activate an Information 1 source and set its volume to a known step",
    "Activate an Information 2 source and set its volume to a different step",
    "End both sources",
    "Activate the Information 1 source again",
    "Read the Information 1 volume step and record it"],
   ["The Information 1 source is active at its set step",
    "The Information 2 source is active at its own set step",
    "Both sources end",
    "The Information 1 source is active again",
    "The Information 1 volume step is the step set for Information 1"],
   prio="P1", method=STATE, pre="No audio source is active",
   reasoning="The recall at 4866878 is per source. A single shared slot would "
             "satisfy the one-source case and return the wrong level here.")

tc("SWE1_AMM_064",
   "Confirm repeated telematics volume up requests stop at the maximum",
   ["Play an Entertainment source at the maximum volume step",
    "Send TLM_Vol_UP_Status.Info = \"Pressed\"",
    "Read the Entertainment volume step and record it"],
   ["Entertainment audio plays at the maximum volume step",
    "TLM_Vol_UP_Status.Info reports \"Pressed\"",
    "The Entertainment volume step is the maximum step"],
   prio="P1", method=BVA,
   reasoning="Upper bound of the range 4866127 drives. Paired with the "
             "minimum-side clamp at 067, the two ends of the range are covered "
             "rather than only the middle.")

for sid, path, sig in (("SWE1_AMM_192", "Information 1", "$VolumeINFO1$"),
                       ("SWE1_AMM_193", "Information 2", "$VolumeINFO2$")):
    tc(sid,
       f"Confirm a higher priority {path} source is left alone by the telematics mute",
       [f"Activate an {path} source that ranks above the TBM mute in priority",
        "Trigger the TBM mute",
        f"Read {sig} and record it"],
       [f"The {path} source is active",
        "The TBM mute is active",
        f"{sig} reports the current {path} volume level"],
       prio="P1", method=NEGATIVE, remarks=PEND_SIG,
       pre="No audio source is active",
       reasoning="The clause conditions the suppression on ranking below the "
                 "TBM mute. A blanket suppression would pass the positive case "
                 "and silence a source it must not touch.")

tc("SWE1_AMM_083",
   "Confirm speed controlled volume stays enabled through a voice recognition session",
   ["Set the speed controlled volume to a level other than off",
    "Start a Voice Recognition session",
    "Read the speed controlled volume setting and record it"],
   ["The speed controlled volume setting is not off",
    "The Voice Recognition session is active",
    "The speed controlled volume setting is unchanged"],
   prio="P1", method=NEGATIVE, pre="No call is in progress",
   reasoning="4866214 names phone calls, VR and other information sources. The "
             "first case takes the call; this takes the VR session, a separate "
             "path into the same suppression risk.")

tc("SWE1_AMM_295",
   "Confirm voice recognition is also unaffected when reverse mute is disabled",
   ["Configure the vehicle so that $Reverse_Mute_Enable$ is \"Disable\"",
    "Send the signal $TRANSM_FD_4.ShiftLeverPosition$ = 2 (R)",
    "Press the Voice Recognition button",
    "Record the state of the Voice Recognition session"],
   ["$Reverse_Mute_Enable$ reports \"Disable\"",
    "$TRANSM_FD_4.ShiftLeverPosition$ = 2 (R) is received",
    "The Voice Recognition request is raised",
    "A Voice Recognition session starts"],
   prio="P1", method=NEGATIVE, remarks=PEND_SIG,
   reasoning="4867710 disables all reverse-mute behaviour, which includes the "
             "VR suppression at 4866824 as well as the audio mute. The first "
             "case observes the audio; this observes the VR half, since a "
             "partial disable would pass one and fail the other. Out-of-pool, "
             "single-source under R-AM18.")


def main() -> None:
    ctx = {l["swe_id"]: l for l in json.loads(
        (ROOT / "batches" / "B3_context.json").read_text(encoding="utf-8"))}
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
    out = {"batch": "B3", "feature": "Audio Management",
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
    dest = ROOT / "generated" / "B3.json"
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
