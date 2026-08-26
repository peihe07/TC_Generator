#!/usr/bin/env python3
"""Emit the B4 test cases for audio_mgmt (R-AM20 green channel, first batch).

Same contract as the earlier generators: the verbatim upper half of each
`test_item` is read from `batches/B4_context.json`, never retyped.

002 and 122 are absent: route 2 disagreed with the candidate anchor on both,
and R-AM15 bars one route from settling an anchor. The green channel lifts
the per-batch ruling for leaves where the routes agree, not that bar.

Usage:
    python features/audio_mgmt/scripts/gen_b4.py
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
PEND_TEMP = ("PENDING: DR-AM5 <Temp Ramp Down> value not defined in "
             "available sources")
PEND_NOANCHOR = "PENDING: DR-AM1 no CFTS019 object found for this leaf"

AUTHORED: dict[str, list[dict]] = {}


def tc(swe_id, purpose, proc, er, *, prio="P1", method=FUNC, pre="NA",
       data="NA", remarks="", reasoning="", desc=None):
    AUTHORED.setdefault(swe_id, []).append(dict(
        purpose=purpose, proc=proc, er=er, prio=prio, method=method, pre=pre,
        data=data, remarks=remarks, reasoning=reasoning, desc=desc))


# ------------------------------------------------------------ Audio Sources
tc("SWE1_AMM_001",
   "Confirm an Entertainment source is reproduced on both stereo channels",
   ["Play an Entertainment source",
    "Read the audio present on the left and right output channels and record it"],
   ["Entertainment audio plays",
    "Both the left and the right output channel carry the Entertainment audio"],
   prio="P1", method=FUNC,
   reasoning="4865912 processes Entertainment sources as stereo, so the "
             "observation is that both channels carry audio rather than that "
             "any audio exists.")

tc("SWE1_AMM_003",
   "Confirm Entertainment playback continues until the user stops it",
   ["Play an Entertainment source",
    "Wait without issuing any request",
    "Record the playback state of the Entertainment source",
    "Send a pause request",
    "Record the playback state again"],
   ["Entertainment audio plays",
    "No request is issued",
    "The Entertainment source is still playing",
    "The pause request is accepted",
    "The Entertainment source is paused"],
   prio="P1", method=STATE,
   desc=("The Audio Management software shall maintain the Entertainment "
         "source in the active playback state until a user pause or stop "
         "request or a higher-priority audio event occurs"),
   reasoning="4865915 makes continuity the requirement, so the case observes "
             "the source surviving a period of inactivity before the user "
             "stops it. The higher-priority interruption the clause also names "
             "is covered by the arbitration leaves in B1.")

tc("SWE1_AMM_005",
   "Confirm a tuner source and a USB source are both handled as Entertainment",
   ["Play an FM station",
    "Record the source category applied to the FM source",
    "Play a USB media track",
    "Record the source category applied to the USB source"],
   ["FM audio plays",
    "The FM source is handled as an Entertainment source",
    "The USB media track plays",
    "The USB source is handled as an Entertainment source"],
   prio="P1", method=FUNC,
   reasoning="4865917 gives an open list. Two members from different families "
             "are exercised — a tuner source and a stored-media source — "
             "because a classification that keyed on one family would pass a "
             "single-member case.")

tc("SWE1_AMM_006",
   "Confirm a traffic announcement is handled with Entertainment audio settings",
   ["Tune an FM station with traffic announcements enabled",
    "Trigger a traffic announcement",
    "Record the source category and the audio settings applied to the announcement"],
   ["The FM station is tuned and traffic announcements are enabled",
    "The traffic announcement starts",
    "The announcement is handled as an Entertainment source with the Entertainment audio settings"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="4865918 classifies TA/PTY31 as Entertainment, which is what "
             "makes the B1 transition leaves treat it with the entertainment "
             "ramp parameters rather than the information ones.")

tc("SWE1_AMM_007",
   "Confirm an Information source is reproduced as mono on its assigned path",
   ["Trigger a Navigation guidance prompt",
    "Record the channel content of the Information audio",
    "Record the Information path the source is assigned to"],
   ["The Navigation guidance prompt starts",
    "The Information audio is mono",
    "The source is assigned to the Information 1 path"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="4865928 states both properties in one clause — mono processing "
             "and path assignment — so both are read in one case rather than "
             "split, since the clause does not separate them.")

tc("SWE1_AMM_009",
   "Confirm a navigation prompt is routed through the Information 1 path",
   ["Trigger a Navigation guidance prompt",
    "Record the Information path carrying the audio"],
   ["The Navigation guidance prompt starts",
    "The Information 1 path carries the audio"],
   prio="P1", method=DECISION, pre="No audio source is active",
   reasoning="4865932 lists the Information 1 members. Navigation is taken "
             "here; 010 covers the Information 2 list, and the two lists are "
             "what separate the paths.")

tc("SWE1_AMM_010",
   "Confirm a hands-free call is routed through the Information 2 path",
   ["Establish a hands-free call",
    "Record the Information path carrying the audio"],
   ["The hands-free call audio is active",
    "The Information 2 path carries the audio"],
   prio="P1", method=DECISION, pre="No audio source is active",
   reasoning="4865936 lists the Information 2 members. This assignment is what "
             "the B2 leaf 032 relies on when it pauses user sources while "
             "Information 2 is active.")

tc("SWE1_AMM_013",
   "Confirm confirmation tones reach the front channels on a non-amplified system",
   ["Play an Entertainment source on a non-amplified system",
    "Trigger a confirmation tone",
    "Record the output channels carrying the tone"],
   ["Entertainment audio plays",
    "The confirmation tone is triggered",
    "The front output channels carry the tone"],
   prio="P1", method=FUNC,
   reasoning="4865967 is the non-amplified counterpart of the amplified "
             "overlay B2 covered at 4865968, so the system configuration is "
             "named in step 1 rather than left open.")

tc("SWE1_AMM_020",
   "Confirm alert audio reaches the front channels at minimum",
   ["Play no audio source",
    "Trigger an Entertainment alert",
    "Record the output channels carrying the alert"],
   ["No audio source is active",
    "The alert plays",
    "The front output channels carry the alert"],
   prio="P1", method=FUNC,
   reasoning="Anchored at package 16 section 3 to 4865981 and 4866286 as a "
             "pair: 4865981 sets the minimum — alerts may play on all "
             "channels but at a minimum on the front — and 4866286 states the "
             "front-speaker routing for the feature. Route 2 had rejected "
             "4865981 for saying all channels where the leaf says front; that "
             "reading came from a truncated view of the row, whose next clause "
             "is exactly the minimum the leaf states. The enablement 4866286 "
             "defers to {CFTS024} is a settings concern, so this case checks "
             "routing and not the setting, and takes no DR.")

tc("SWE1_AMM_024",
   "Confirm the three source streams reach an external amplifier on their own paths",
   ["Configure the vehicle with an external amplifier",
    "Play an Entertainment source and activate an Information 1 source",
    "Record the streams present on the external amplifier inputs"],
   ["The external amplifier configuration is active",
    "Both sources are active",
    "The Entertainment stream and the Information 1 stream reach the amplifier on their own paths"],
   prio="P1", method=FUNC,
   reasoning="Anchored at package 16 section 3 to 4866001, which the leaf's "
             "own SWE.1 description names outright — the strongest trace "
             "available, the upstream stating the ObjectID itself. Route 2 "
             "returned nothing because 4866001 is an embedded table: its "
             "exported Description is an image reference, so no text search "
             "of either corpus could reach it, the same mechanism as A-AM03 "
             "except that this object is in the pool. The output mapping "
             "lives in that table, so the case observes that each stream "
             "arrives on its own path and does not restate the table.")

tc("SWE1_AMM_108",
   "Confirm channel assignment runs after the per-source gain stage",
   ["Play an Entertainment source and activate an Information source",
    "Record the order of the per-source gain adjustment and the channel assignment"],
   ["Both sources are active",
    "The channel assignment follows the per-source gain adjustment"],
   prio="P1", method=STATE, pre="No audio source is active",
   reasoning="4866289 fixes the ordering of two processing stages, so ordering "
             "is what the case observes. It is general channel assignment and "
             "says nothing about an external amplifier, which is why leaf 024 "
             "does not share it.")

tc("SWE1_AMM_145",
   "Confirm the ramp-down touches only the channels the table applies",
   ["Play an Entertainment source",
    "Trigger an Information source that applies to a subset of channels",
    "Record the channels on which the Entertainment audio ramps down"],
   ["Entertainment audio plays",
    "The Information source becomes active",
    "The Entertainment audio ramps down only on the applied channels named in the Information Source Handling Table"],
   prio="P0", method=FUNC, pre="No audio source is active",
   reasoning="4866497, resolved by route 2 and reported in package 15 section "
             "3.1. It is its own object, distinct from 4866494 that B1 used "
             "for 144: that one is the general deactivation ramp, this one is "
             "the applied-channels restriction, so no shared-anchor argument "
             "is needed. The restriction is the point, so the case observes "
             "which channels are left alone as much as which ramp.")

tc("SWE1_AMM_146",
   "Confirm the channels outside the applied set ramp down on their own parameter",
   ["Play an Entertainment source",
    "Trigger an Information source that applies to a subset of channels",
    "Measure the ramp-down on the channels outside the applied set and record it"],
   ["Entertainment audio plays",
    "The Information source becomes active",
    "The Entertainment audio on the remaining channels ramps down within 25 ms to 50 ms"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="Anchored at package 16 section 3 to 4866498, which runs "
             "consecutively with 145's 4866497 as the two halves of the "
             "attenuate branch: applied channels first, remaining channels "
             "after. Route 2 missed it by searching the singular remaining "
             "channel where the spec writes remaining audio channels. The "
             "parameter here is <Tent Ramp Down>, which is defined at "
             "4867767, so the bound is real — it is not the undefined "
             "<Temp Ramp Down> that 204 and 207 carry a PENDING for. The "
             "channel set itself is defined in {CIP Radio DSPPP}, outside "
             "this feature's scope under R-AM5, so it is not restated.")

for sid, anchor, sig, val, path, emphasis in (
        ("SWE1_AMM_148", "4866501", "$INFO1Active$", "the active state",
         "Information 1", "the activity flag"),
        ("SWE1_AMM_149", "4866502", "$INFO1Type$",
         "the type from the Information Source Handling Table",
         "Information 1", "the type value"),
        ("SWE1_AMM_151", "4866506", "$INFO2Active$", "the active state",
         "Information 2", "the activity flag"),
        ("SWE1_AMM_152", "4866507", "$INFO2Type$",
         "the type from the Information Source Handling Table",
         "Information 2", "the type value")):
    tc(sid,
       f"Confirm activation drives {emphasis} for the {path} path",
       [f"Activate an {path} source",
        f"Read {sig} and record it"],
       [f"The {path} source is active",
        f"{sig} reports {val}"],
       prio="P1", method=FUNC, remarks=PEND_SIG, pre="No audio source is active",
       reasoning=f"{anchor} is one sub-clause of the activation sequence. "
                 f"Package 13 section 4.2 leaves the split to 8.2.2: the four "
                 f"are kept apart because each is its own object with its own "
                 f"signal, and a system can set the flag while leaving the "
                 f"type stale. The bracket names which of the two this row "
                 f"observes.")

for sid, anchor, sig, val, path in (
        ("SWE1_AMM_162", "4866532", "$INFO1Active$", "the inactive state",
         "Information 1"),
        ("SWE1_AMM_163", "4866533", "$INFO1Type$", "\"NONE\"", "Information 1"),
        ("SWE1_AMM_164", "4866535", "$INFO2Active$", "the inactive state",
         "Information 2"),
        ("SWE1_AMM_165", "4866536", "$INFO2Type$", "\"NONE\"", "Information 2")):
    tc(sid,
       f"Confirm deactivation resets {sig} for the {path} path",
       [f"Activate an {path} source",
        f"End the {path} source",
        f"Read {sig} and record it"],
       [f"The {path} source is active",
        f"The {path} source ends",
        f"{sig} reports {val}"],
       prio="P1", method=FUNC, remarks=PEND_SIG, pre="No audio source is active",
       reasoning=f"{anchor} is the deactivation counterpart of the activation "
                 f"sub-clause. A stale type after deactivation is exactly the "
                 f"defect the pairing guards against, so the reset is observed "
                 f"separately from the flag.")

tc("SWE1_AMM_155",
   "Confirm the ramp-up touches only the channels the table indicates",
   ["Play no audio source",
    "Trigger an Information source that applies to a subset of channels",
    "Record the channels on which the Information audio ramps up"],
   ["No audio source is active",
    "The Information source becomes active",
    "The Information audio ramps up only on the channels indicated in the Information Source Handling Table"],
   prio="P0", method=FUNC,
   reasoning="4866513, resolved by route 2 and reported in package 15 section "
             "3.2. B1's leaf 154 uses 4866512, which is the volume-level "
             "clause; this is the channel clause, a separate object, so the "
             "two need no shared-anchor argument.")

tc("SWE1_AMM_175",
   "Confirm the audio settings are stored before the speaker routing changes",
   ["Play an Entertainment source with a known volume, tone and fade setting",
    "Trigger a change of speaker routing",
    "Read the stored audio mode settings and record them"],
   ["Entertainment audio plays with the set volume, tone and fade values",
    "The speaker routing change starts",
    "The stored audio mode settings are the values set before the change"],
   prio="P1", method=STATE,
   reasoning="4866659 stores, 4866662 at leaf 176 recalls. The store is only "
             "observable through what comes back, so the two leaves make a "
             "pair; this row reads the stored values at the moment of the "
             "change.")

tc("SWE1_AMM_176",
   "Confirm the stored audio settings come back after the routing change",
   ["Play an Entertainment source with a known volume, tone and fade setting",
    "Trigger a change of speaker routing",
    "Wait until the routing change completes",
    "Read the volume, tone and fade settings and record them"],
   ["Entertainment audio plays with the set volume, tone and fade values",
    "The speaker routing change starts",
    "The routing change completes",
    "The volume, tone and fade settings are the values set before the change"],
   prio="P1", method=STATE,
   reasoning="4866662 is the recall half of the pair with 175. Reading all "
             "three settings rather than one catches a partial restore.")

tc("SWE1_AMM_202",
   "Confirm the source status signals follow a completed ramp-up",
   ["Play no audio source",
    "Activate an Information 1 source",
    "Wait until the ramp-up completes",
    "Read $HUModeStatus$, $INFO1Active$ and $INFO1Type$ and record them"],
   ["No audio source is active",
    "The Information 1 source becomes active",
    "The ramp-up completes",
    "$INFO1Active$ reports the active state and $INFO1Type$ reports the source type"],
   prio="P0", method=STATE, remarks=PEND_SIG,
   reasoning="4866843 ties the status update to the ramp-up expiring, so the "
             "case waits for that rather than reading immediately. The signals "
             "are read together because the clause updates them together.")

tc("SWE1_AMM_204",
   "Confirm the source status signals reset after a completed ramp-down",
   ["Activate an Information 1 source",
    "End the Information 1 source",
    "Wait until the ramp-down completes",
    "Read $HUModeStatus$, $INFO1Active$ and $INFO1Type$ and record them"],
   ["The Information 1 source is active",
    "The Information 1 source ends",
    "The ramp-down completes",
    "$INFO1Active$ reports \"Not_Active\" and $INFO1Type$ reports \"None\""],
   prio="P0", method=STATE, remarks=f"{PEND_TEMP}; {PEND_SIG}",
   pre="No audio source is active",
   reasoning="4866845 keys on <Temp Ramp Down> expiring. That parameter is "
             "undefined in CFTS019 — A-AM04 and DR-AM5, confirmed by a "
             "case-insensitive search this time — so the duration carries a "
             "PENDING while the ordering is still observed.")

tc("SWE1_AMM_207",
   "Confirm the mode status names the incoming source once the ramp-down expires",
   ["Play Entertainment source A",
    "Select Entertainment source B",
    "Wait until the ramp-down completes",
    "Read $HUModeStatus$ and record it"],
   ["Entertainment source A plays",
    "The selection of source B is accepted",
    "The ramp-down completes",
    "$HUModeStatus$ reports source B"],
   prio="P0", method=STATE, remarks=f"{PEND_TEMP}; {PEND_SIG}",
   reasoning="4866854 is the Entertainment-transition counterpart of 4866845. "
             "It carries the same undefined <Temp Ramp Down>, so the same "
             "PENDING applies to the duration and not to the ordering.")

tc("SWE1_AMM_210",
   "Confirm all source status signals reset together when nothing is playing",
   ["Play an Entertainment source and an Information source",
    "End both sources",
    "Read $HUModeStatus$, $INFO1Active$, $INFO1Type$, $INFO2Active$ and $INFO2Type$ and record them"],
   ["Both sources are active",
    "Both sources end",
    "$HUModeStatus$ reports \"HU_Off\", $INFO1Active$ and $INFO2Active$ report \"Inactive\", and $INFO1Type$ and $INFO2Type$ report \"None\""],
   prio="P0", method=STATE, remarks=PEND_SIG, pre="No audio source is active",
   reasoning="Package 13 section 4.5 rules this one case with a composite "
             "expected result rather than five rows: 4866872 fires one trigger "
             "and updates five signals, and splitting it would test five "
             "triggers the clause does not have.")

tc("SWE1_AMM_214",
   "Confirm an incoming hands-free call sets the Information 2 status and recalls its volume",
   ["Establish a hands-free call",
    "Read $INFO2Active$, $INFO2Type$ and $VolumeINFO2$ and record them"],
   ["The hands-free call audio is active",
    "$INFO2Active$ reports \"Active\", $INFO2Type$ reports \"Phone_Aud\", and $VolumeINFO2$ reports the recalled call volume"],
   prio="P0", method=STATE, remarks=PEND_SIG, pre="No audio source is active",
   reasoning="4866876 is the HFP activation sequence. It sits alongside three "
             "other HFP rows in the workbook — B3's 309 on pausing user "
             "sources and 273/274 on the volume thresholds — so the bracket "
             "names the status and the recall to keep them apart.")

tc("SWE1_AMM_217",
   "Confirm ending a hands-free call stores its volume and clears the status",
   ["Establish a hands-free call and set its volume to a known step",
    "End the hands-free call",
    "Read $VolumeINFO2$ and $INFO2Active$ and record them"],
   ["The hands-free call is active at the set volume step",
    "The hands-free call ends",
    "The stored call volume is the step set before the call ended and $INFO2Active$ reports \"Not_Active\""],
   prio="P0", method=STATE, remarks=PEND_SIG, pre="No audio source is active",
   reasoning="4866881 is the deactivation counterpart of 4866876. The store is "
             "what makes 214's recall meaningful, so the pair is written to "
             "read the same value from both ends.")

tc("SWE1_AMM_228",
   "Confirm call audio moves to the passenger side while a navigation prompt runs",
   ["Trigger a Navigation guidance prompt",
    "Receive an incoming call and accept it",
    "Record the channels carrying the call audio",
    "Wait until the guidance prompt ends",
    "Record the channels carrying the call audio again"],
   ["The Navigation guidance prompt plays",
    "The incoming call is accepted",
    "The passenger-side channel carries the call audio",
    "The guidance prompt ends",
    "Both front channels carry the call audio"],
   prio="P0", method=STATE, pre="No audio source is active",
   reasoning="4866904 has two phases, during the prompt and after it, and the "
             "second is what makes the first temporary. Reading only the first "
             "would pass a system that left the call on one channel for good.")

for sid, anchor, side, val, chan in (
        ("SWE1_AMM_256", "4867564", "left-hand drive", "LHD", "left"),
        ("SWE1_AMM_257", "4867566", "right-hand drive", "RHD", "right")):
    tc(sid,
       f"Confirm driver audio follows the {chan} side on a {side} vehicle",
       [f"Configure the vehicle as {side}",
        "Trigger a Navigation guidance prompt",
        "Record the channel carrying the driver-related audio"],
       [f"$DriverSide$ reports \"{val}\"",
        "The Navigation guidance prompt starts",
        f"The {chan}-side channel carries the driver-related audio"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       pre="No audio source is active",
       reasoning=f"{anchor} is one half of the section 7 enumeration pair with "
                 f"the other drive side; package 13 section 4.4 requires both "
                 f"to ship. The anchor is the HU-side object, not the "
                 f"amplifier-side 4867567. Disclosed and not extended: "
                 f"4867568 handles an invalid $DriverSide$ value by falling "
                 f"back to the CIP default and has no SWE.1 leaf, so it is a "
                 f"negative-path gap in the upstream decomposition rather than "
                 f"something to write here.")

tc("SWE1_AMM_263",
   "Confirm the rear channels are muted on a two-speaker cabin configuration",
   ["Configure a Cabin EQ profile that corresponds to a two-speaker system",
    "Play an Entertainment source",
    "Record the audio on the rear speaker channels"],
   ["The Cabin EQ profile corresponds to a two-speaker system",
    "Entertainment audio plays",
    "The rear speaker channels are muted"],
   prio="P1", method=DECISION,
   reasoning="4867584 and 4867582 at leaf 262 are two consequences of the same "
             "two-speaker configuration — muting the rear and disabling fade. "
             "Each is its own object and could be implemented without the "
             "other.")

tc("SWE1_AMM_311",
   "Confirm a navigation prompt during a call is placed on the driver side",
   ["Establish a hands-free call",
    "Trigger a Navigation guidance prompt",
    "Record the channel carrying the Navigation audio"],
   ["The hands-free call audio is active",
    "The Navigation guidance prompt starts",
    "The driver-side channel carries the Navigation audio"],
   prio="P1", method=DECISION, pre="No audio source is active",
   reasoning="4866914 places NAV on the driver side while Phone holds the "
             "other, the mirror of 228 where the call moves to the passenger "
             "side. Out-of-pool anchor, single-source corroboration under "
             "R-AM18.")

tc("SWE1_AMM_002",
   "Confirm an Entertainment stream is assigned to both the left and right paths",
   ["Play an Entertainment source",
    "Record the audio paths the Entertainment stream is assigned to"],
   ["Entertainment audio plays",
    "The Entertainment stream is assigned to the Entertainment Left and Right audio paths"],
   prio="P1", method=FUNC,
   reasoning="Re-anchored at package 16 section 2 to 4865913, adopting route "
             "2's proposal. The earlier candidate 4867570 reads the left or "
             "right drive, which 4867569's $DriverSide$ LHD and RHD test "
             "shows to be the steering position rather than the audio "
             "channels — the two collide on the words left, right and audio "
             "output channels while meaning different things. Distinct from "
             "001, which observes stereo reproduction: this observes the path "
             "assignment that makes it possible.")

tc("SWE1_AMM_122",
   "Confirm arbitration and routing follow the approved routing table",
   ["Play an Entertainment source and activate an Information source",
    "Record the arbitration outcome and the channels each source is routed to"],
   ["Both sources are active",
    "The arbitration outcome and the routing match the approved Audio Routing Table"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="Re-anchored at package 16 section 2 to 4866444 with partial "
             "coverage. The earlier candidate 4865895 is a table's title, not "
             "a requirement. 4866444 refers the routing table out to the "
             "component technical specification, the same shape as 076b and "
             "087, so the case observes that arbitration follows the table "
             "and writes none of the table's own content; that goes to "
             "DR-AM1.")

# ----------------------------------------------------------- Volume Control
for sid, anchor, sig, path in (
        ("SWE1_AMM_194", "4866722", "$VolumeENT$", "Entertainment"),
        ("SWE1_AMM_196", "4866724", "$VolumeINFO1$", "Information 1"),
        ("SWE1_AMM_197", "4866725", "$VolumeINFO2$", "Information 2")):
    tc(sid,
       f"Confirm the {path} level returns after the telematics mute is released",
       [f"Play the {path} source at a known volume step",
        "Trigger the TBM mute",
        "Release the TBM mute",
        f"Read {sig} and record it"],
       [f"The {path} source plays at the set volume step",
        "The TBM mute is active",
        "The TBM mute is released",
        f"{sig} reports the volume step set before the mute"],
       prio="P1", method=STATE, remarks=PEND_SIG,
       reasoning=f"{anchor} is this path's member of the TBM unmute sequence, "
                 f"the counterpart of the mute steps B3 covered at 4866716 to "
                 f"4866719. The recalled level is what proves the store, so "
                 f"the case sets a known step first. This leaf is the one "
                 f"deferred from B3 when 076a took a Volume Control slot."
                 if sid == "SWE1_AMM_194" else
                 f"{anchor} is this path's member of the TBM unmute sequence, "
                 f"the counterpart of the mute steps B3 covered. The recalled "
                 f"level is what proves the store, so the case sets a known "
                 f"step first.")

tc("SWE1_AMM_220",
   "Confirm a volume change during navigation moves only the navigation level",
   ["Play an Entertainment source",
    "Trigger a Navigation guidance prompt",
    "Adjust the volume while the prompt is playing",
    "Record the displayed screen",
    "Read the Navigation volume step and the Entertainment volume step and record them"],
   ["Entertainment audio plays",
    "The Navigation guidance prompt starts",
    "The volume adjustment is accepted",
    "The Volume Level Adjustment screen shows the Navigation volume",
    "The Navigation volume step changes and the Entertainment volume step is unchanged"],
   prio="P1", method=DECISION,
   reasoning="4866891 makes the adjustment land on the Navigation level and "
             "the screen show it. Both are read because a system that "
             "displayed the right screen while moving the wrong level would "
             "pass a display-only check.")

tc("SWE1_AMM_262",
   "Confirm fade control is unavailable on a two-speaker cabin configuration",
   ["Configure a Cabin EQ profile that corresponds to a two-speaker system",
    "Open the audio settings",
    "Record the state of the fade control"],
   ["The Cabin EQ profile corresponds to a two-speaker system",
    "The audio settings open",
    "The fade control is disabled"],
   prio="P1", method=NEGATIVE,
   reasoning="4867582 removes a control, so the case is negative: what must "
             "not be offered is the requirement. Paired with 263, which mutes "
             "the rear channels under the same configuration.")

for sid, anchor, present, state, what in (
        ("SWE1_AMM_264", "4867598", "1", "enabled", "offered in the audio settings"),
        ("SWE1_AMM_266", "4867604", "0", "disabled", "not offered and cannot be changed")):
    tc(sid,
       f"Confirm the surround setting is {what} when the feature reports {state}",
       [f"Configure the vehicle so that $Surround$ = {present}",
        "Open the audio settings",
        "Record the state of the surround sound setting"],
       [f"$Surround$ reports {present}",
        "The audio settings open",
        f"The surround sound setting is {state}"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       reasoning=f"{anchor} is one half of the section 7 enumeration pair: "
                 f"present enables the menu, absent removes it and bars any "
                 f"change. Both must ship, since a system that ignored the "
                 f"configuration would pass whichever half matched its "
                 f"default. Reported out of pool in package 15; that was wrong — 4867598 and 4867604 are in the expanded pool (A-AM12), so package 16 section 1 was right and A-AM10 is withdrawn.")

for sid, anchor, param, value, subject in (
        ("SWE1_AMM_272", "4867751", "<ENT Key Vol>", "15 steps",
         "the Entertainment key volume ceiling"),
        ("SWE1_AMM_273", "4867752", "<HFP Vol Th max>", "38 steps",
         "the restored call volume ceiling"),
        ("SWE1_AMM_274", "4867753", "<HFP Vol Th min>", "15 steps",
         "the restored call volume floor")):
    tc(sid,
       f"Confirm {subject} holds at the specified value",
       ["Drive the volume towards the limit the specification sets",
        "Read the resulting volume step and record it"],
       ["The volume request is accepted",
        f"The resulting volume step is {value}"],
       prio="P1", method=BVA,
       reasoning=f"{anchor} is a variable-definition object giving {param} = "
                 f"{value}, the same shape as the ramp parameters B1 covered "
                 f"at 275 to 278. Package 13 section 4.1 asked route 2 to look "
                 f"for a separate behavioural object; the sleep-resume range "
                 f"4867742 to 4867749 turned out to be VirtualConcertHall and "
                 f"ANC, so none was found and the variable anchor stands "
                 f"alone. Written as a boundary case because a limit is what "
                 f"the object defines.")

tc("SWE1_AMM_306",
   "Confirm the alert sits the specified interval below a louder cabin level",
   ["Play a cabin audio source at a level well above the minimum",
    "Trigger an alert",
    "Read the cabin audio level and the alert level and record them"],
   ["The cabin audio plays at the set level",
    "The alert plays",
    "The alert level is 15 dB below the cabin audio level"],
   prio="P1", method=DECISION,
   reasoning="4866207 sets the default as the greater of two candidates, so "
             "the two branches need a case each. This is the branch where the "
             "cabin level is high enough that 15 dB below it wins. Out-of-pool "
             "anchor, single-source under R-AM18.")
tc("SWE1_AMM_306",
   "Confirm the alert falls back to the floor when the cabin level is low",
   ["Play a cabin audio source at a level near the minimum",
    "Trigger an alert",
    "Read the cabin audio level and the alert level and record them"],
   ["The cabin audio plays at the set level",
    "The alert plays",
    "The alert level is the equivalent of volume step 6"],
   prio="P1", method=DECISION,
   reasoning="The other branch of the whichever is greater rule at 4866207: "
             "with the cabin level low, 15 dB below it falls under step 6 and "
             "the floor takes over. Testing only the first branch would leave "
             "the floor unexercised, which is the branch that protects "
             "audibility. Out-of-pool, single-source under R-AM18.")

tc("SWE1_AMM_307",
   "Confirm the alert uses the floor level when no cabin audio is playing",
   ["Play no audio source",
    "Trigger an alert",
    "Read the alert level and record it"],
   ["No audio source is active",
    "The alert plays",
    "The alert level is the equivalent of volume step 6"],
   prio="P1", method=DECISION,
   reasoning="4866208 is the inactive-cabin counterpart of 4866207. It reaches "
             "the same level as 306's floor branch by a different route — no "
             "reference level rather than a low one — so the two are separate "
             "objects and separate rows. Out-of-pool, single-source under "
             "R-AM18.")

tc("SWE1_AMM_308",
   "Confirm speed volume control stops when the level setting is turned off",
   ["Send SVC_Level_Setting.Req = \"Off\"",
    "Drive the vehicle above the speed at which the function would act",
    "Read the applied speed volume compensation and record it"],
   ["SVC_Level_Setting.Req reports \"Off\"",
    "The vehicle speed is above the threshold",
    "No speed volume compensation is applied"],
   prio="P1", method=NEGATIVE, pre="No call is in progress",
   reasoning="4866242 disables the function unless the vehicle EQ "
             "configuration defines a minimum level. The case takes the plain "
             "disable; the EQ-defined minimum is a configuration this leaf "
             "does not describe, so it is not written. Out-of-pool anchor, "
             "single-source under R-AM18.")


def main() -> None:
    ctx = {l["swe_id"]: l for l in json.loads(
        (ROOT / "batches" / "B4_context.json").read_text(encoding="utf-8"))}
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
    out = {"batch": "B4", "feature": "Audio Management",
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
    dest = ROOT / "generated" / "B4.json"
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
