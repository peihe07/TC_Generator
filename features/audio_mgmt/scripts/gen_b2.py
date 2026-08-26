#!/usr/bin/env python3
"""Emit the B2 test cases for audio_mgmt.

Same contract as gen_b1.py: the verbatim upper half of every `test_item` is
read from `batches/B2_context.json`, never retyped, so it cannot drift from
SWE.1. Only the bracketed purpose line and the test body are authored here.

Anchors come from package 08's ruled table and are never recomputed. Where
package 08 marks a leaf **部分覆蓋**, the case is written to the anchor's
wording and stops there — no behaviour is invented to fill the gap
(IN 8.2.1, doubt resolves narrow).

Usage:
    python features/audio_mgmt/scripts/gen_b2.py
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

TDISP = "at most 100 ms"          # CFTS019, <Tdisp> Max = 100 ms
VENT_NAV_OFF = "9 steps"          # CFTS019-4867783, <Vent Nav Off> = 9 steps
# Spec-sourced: CFTS019-4867782 (1.5.4 Variables) gives <Vent off> = -16 dB,
# with R1L-R in its Radio list. An earlier revision here claimed the value was
# defined nowhere and came from the ruling instead — that was a case-sensitive
# search matching only the lowercase <vent off>, which occurs once, while the
# capitalised <Vent off> occurs eight times and carries the definition.
VENT_OFF = "-16 dB"

# Every signal B2 touches is absent from the supplied DBC — only SOSCallType
# is there, and B2 does not use it — so each keeps the specification's own
# name under 8.7.5 v3 (g) and carries the DR-AM4 note.
PEND_SIG = ("PENDING: DR-AM4 signal not found in the supplied DBC; name kept "
            "as written in CFTS019 per R-13 (g)")
PEND_CFTS020 = ("PENDING: DR-AM6 mute logic defined in CFTS020, document not "
                "available")

AUTHORED: dict[str, list[dict]] = {}


def tc(swe_id, purpose, proc, er, *, prio="P1", method=FUNC, pre="NA",
       data="NA", remarks="", reasoning="", desc=None):
    AUTHORED.setdefault(swe_id, []).append(dict(
        purpose=purpose, proc=proc, er=er, prio=prio, method=method, pre=pre,
        data=data, remarks=remarks, reasoning=reasoning, desc=desc))


# ---------------------------------------------- Audio Arbitration, 1.3.3.17
AMP17 = "non-amplifier and booster systems"
AMP18 = "CAN amplifier systems"

for sid, amp, anchor in (("SWE1_AMM_229", AMP17, "4866906"),
                         ("SWE1_AMM_236", AMP18, "4866929")):
    tc(sid,
       f"Confirm a traffic announcement is ignored during a VR session on {amp}",
       ["Start a Voice Recognition session",
        "Trigger a traffic announcement event",
        "Record the audio produced for the traffic announcement"],
       ["The Voice Recognition session is active",
        "The traffic announcement event is raised",
        "No traffic announcement audio is produced"],
       prio="P0", method=DECISION, pre="No audio source is active",
       reasoning=f"{anchor} is the {amp} half of the pair the same clause text "
                 f"carries at two anchors, so the amplifier type is the "
                 f"distinguishing token. This case takes the default branch, "
                 f"where the customer has not selected TA.")
    tc(sid,
       f"Confirm a customer-selected traffic announcement does play on {amp}",
       ["Start a Voice Recognition session",
        "Select the traffic announcement for activation",
        "Trigger a traffic announcement event",
        "Record the audio produced for the traffic announcement"],
       ["The Voice Recognition session is active",
        "The traffic announcement is selected for activation",
        "The traffic announcement event is raised",
        "The traffic announcement audio is produced"],
       prio="P1", method=DECISION, pre="No audio source is active",
       reasoning=f"The 'unless selected by the customer' exception at {anchor}. "
                 f"Without it a system that ignored TA unconditionally would "
                 f"pass the first case.")

for sid, amp, anchor in (("SWE1_AMM_232", AMP17, "4866913"),
                         ("SWE1_AMM_239", AMP18, "4866933")):
    tc(sid,
       f"Confirm a traffic announcement is ignored during Phone audio on {amp}",
       ["Establish a hands-free call",
        "Trigger a traffic announcement event",
        "Record the audio produced for the traffic announcement"],
       ["The hands-free call audio is active",
        "The traffic announcement event is raised",
        "No traffic announcement audio is produced"],
       prio="P0", method=DECISION, pre="No audio source is active",
       reasoning=f"{anchor} repeats the TA suppression rule with Phone audio in "
                 f"place of a VR session, on {amp}. Kept separate from the VR "
                 f"case because the two conditions are independent.")
    tc(sid,
       f"Confirm the customer selection exception also applies during Phone audio on {amp}",
       ["Select the traffic announcement for activation",
        "Establish a hands-free call",
        "Trigger a traffic announcement event",
        "Record the audio produced for the traffic announcement"],
       ["The traffic announcement is selected for activation",
        "The hands-free call audio is active",
        "The traffic announcement event is raised",
        "The traffic announcement audio is produced"],
       prio="P1", method=DECISION, pre="No audio source is active",
       reasoning=f"The exception clause at {anchor}, exercised under Phone audio.")

for sid, amp, anchor in (("SWE1_AMM_230", AMP17, "4866908"),
                         ("SWE1_AMM_237", AMP18, "4866930")):
    tc(sid,
       f"Confirm a customer-selected Navigation prompt cancels the VR session on {amp}",
       ["Start a Voice Recognition session",
        "Select the Navigation prompt for activation",
        "Trigger a Navigation audio event",
        "Record the state of the Voice Recognition session and the Navigation audio"],
       ["The Voice Recognition session is active",
        "The Navigation prompt is selected for activation",
        "The Navigation audio event is raised",
        "The Voice Recognition session is cancelled and the Navigation audio plays"],
       prio="P0", method=STATE, pre="No audio source is active",
       reasoning=f"{anchor} on {amp}. Pairs against the delay case at the "
                 f"neighbouring anchor: selected cancels, unselected defers, and "
                 f"the customer selection is what separates them.")

for sid, amp, anchor in (("SWE1_AMM_231", AMP17, "4866911"),
                         ("SWE1_AMM_238", AMP18, "4866931")):
    tc(sid,
       f"Confirm an unselected Navigation prompt is deferred and then replayed on {amp}",
       ["Start a Voice Recognition session",
        "Trigger a Navigation audio event that is not selected for activation",
        "Record the audio produced while the session runs",
        "End the Voice Recognition session",
        "Record the audio produced after the session ends"],
       ["The Voice Recognition session is active",
        "The Navigation audio event is raised",
        "No Navigation audio is produced while the session runs",
        "The Voice Recognition session ends",
        "The Navigation announcement is repeated"],
       prio="P0", method=STATE, pre="No audio source is active",
       reasoning=f"{anchor} on {amp} requires both halves — ignored during the "
                 f"session and repeated after it. A system that simply dropped "
                 f"the event would satisfy the first half alone.")

for sid, amp, anchor in (("SWE1_AMM_234", AMP17, "4866926"),):
    tc(sid,
       f"Confirm a Phone or VR button press cancels active Navigation audio on {amp}",
       ["Trigger a Navigation guidance prompt",
        "Press the Voice Recognition button",
        "Record the state of the Navigation audio"],
       ["The Navigation guidance prompt plays",
        "The Voice Recognition request is accepted",
        "The Navigation audio is cancelled"],
       prio="P0", method=SCENARIO, pre="No audio source is active",
       reasoning=f"{anchor} is the {amp} twin of 4866902, which B1 covers at "
                 f"SWE1_AMM_226. The amplifier type is written into the bracket "
                 f"so the two batches' rows stay distinguishable in one workbook.")

tc("SWE1_AMM_235",
   f"Confirm accepting an incoming call cancels a traffic announcement on {AMP17}",
   ["Trigger a traffic announcement",
    "Receive an incoming call and accept it",
    "Record the state of the traffic announcement audio"],
   ["The traffic announcement plays",
    "The incoming call is accepted",
    "The traffic announcement audio is cancelled"],
   prio="P0", method=SCENARIO, pre="No audio source is active",
   reasoning="4866927 is the non-amplifier twin of 4866903, which B1 covers at "
             "SWE1_AMM_227. Same treatment as the 226/234 pair.")

tc("SWE1_AMM_259",
   "Confirm the null Cabin EQ identifier falls back to the default profile",
   ["Configure the Cabin EQ curve identifier as \"S00\"",
    "Start the head unit",
    "Read the loaded Cabin EQ profile and record it",
    "Read the reported fault and record it"],
   ["The Cabin EQ curve identifier is \"S00\"",
    "The head unit starts",
    "The loaded Cabin EQ profile is the default \"SDF\"",
    "The Plausibility Cabin EQ Mismatch fault is set"],
   prio="P1", method=DECISION,
   reasoning="4867579 names two invalid identifiers in one OR. This takes the "
             "null value; the second case takes the all-ones value, since a "
             "range check can catch one and miss the other.")
tc("SWE1_AMM_259",
   "Confirm the all-ones Cabin EQ identifier falls back the same way",
   ["Configure the Cabin EQ curve identifier as \"SFF\"",
    "Start the head unit",
    "Read the loaded Cabin EQ profile and record it",
    "Read the reported fault and record it"],
   ["The Cabin EQ curve identifier is \"SFF\"",
    "The head unit starts",
    "The loaded Cabin EQ profile is the default \"SDF\"",
    "The Plausibility Cabin EQ Mismatch fault is set"],
   prio="P1", method=DECISION,
   reasoning="Second enumerated value of the same OR at 4867579.")

tc("SWE1_AMM_260",
   "Confirm an identifier outside the supported database falls back to the default",
   ["Configure a Cabin EQ curve identifier that the supported database does not list",
    "Start the head unit",
    "Read the loaded Cabin EQ profile and record it",
    "Read the reported fault and record it"],
   ["The configured Cabin EQ curve identifier is not listed in the supported database",
    "The head unit starts",
    "The loaded Cabin EQ profile is the default \"SDF\"",
    "The Plausibility Cabin EQ Mismatch fault is set"],
   prio="P1", method=DECISION,
   reasoning="4867580 covers an unlisted identifier, which is a different check "
             "from the two reserved values at 4867579 — a lookup miss rather "
             "than a value match.")

tc("SWE1_AMM_310",
   "Confirm a hands-free call cancels an active Navigation VR session",
   ["Start a Navigation Voice Recognition session",
    "Initiate a hands-free call",
    "Record the state of the Voice Recognition session"],
   ["The Navigation Voice Recognition session is active",
    "The hands-free call is initiated",
    "The Voice Recognition session is cancelled"],
   prio="P0", method=STATE, pre="No audio source is active",
   reasoning="4866909 lists three call types against three VR session types. "
             "This takes HFP against a NAV session; the second case takes an "
             "emergency call, which reaches the same rule by a different "
             "trigger path.")
tc("SWE1_AMM_310",
   "Confirm an emergency call cancels an active Phone VR session as well",
   ["Start a Phone Voice Recognition session",
    "Initiate an emergency call",
    "Record the state of the Voice Recognition session"],
   ["The Phone Voice Recognition session is active",
    "The emergency call is initiated",
    "The Voice Recognition session is cancelled"],
   prio="P1", method=STATE, pre="No audio source is active",
   reasoning="Second call type at 4866909. The anchor is the R1L-R variant, "
             "which carries E-Call and R-Call where the neighbouring 4866910 "
             "stops at HFP, so the emergency path belongs to this leaf.")

# ------------------------------------------------------ Focus and Ducking
tc("SWE1_AMM_004",
   "Confirm an Information source outranks Entertainment in focus arbitration",
   ["Play an Entertainment source",
    "Request audio focus for an Information source",
    "Record which source holds audio focus"],
   ["Entertainment audio plays",
    "The Information source requests audio focus",
    "The Information source holds audio focus"],
   prio="P0", method=DECISION,
   reasoning="4865916 ranks Entertainment below both information and signal "
             "sources. This case takes the information half; the second takes "
             "the signal half, which the clause names separately.")
tc("SWE1_AMM_004",
   "Confirm a signal source also outranks Entertainment in focus arbitration",
   ["Play an Entertainment source",
    "Trigger a signal source",
    "Record which source holds audio focus"],
   ["Entertainment audio plays",
    "The signal source is raised",
    "The signal source holds audio focus"],
   prio="P1", method=DECISION,
   reasoning="Signal half of the same ranking at 4865916.")

tc("SWE1_AMM_008",
   "Confirm focus passes to the Information source while Entertainment is playing",
   ["Play an Entertainment source",
    "Activate an Information source",
    "Record which source holds audio focus and the state of the Entertainment audio"],
   ["Entertainment audio plays",
    "The Information source becomes active",
    "The Information source holds audio focus and the Entertainment audio yields"],
   prio="P0", method=DECISION,
   reasoning="4865931 states the ranking from the Information side where 4865916 "
             "states it from the Entertainment side. The two anchors are "
             "separate objects, so each carries its own row; this one observes "
             "the grant, 004 observes the ranking.")

tc("SWE1_AMM_014",
   "Confirm a confirmation tone is overlaid on the Entertainment channel",
   ["Play an Entertainment source on an amplified system",
    "Trigger a confirmation tone",
    "Record the audio present on the amplifier Entertainment channel"],
   ["Entertainment audio plays",
    "The confirmation tone is triggered",
    "The amplifier Entertainment channel carries both the Entertainment audio and the tone"],
   prio="P1", method=FUNC,
   reasoning="4865968 names two channels, ENT and INFO1. This takes ENT; the "
             "second takes INFO1, since a mix applied to one path does not "
             "imply the other.")
tc("SWE1_AMM_014",
   "Confirm the same overlay applies on the Information 1 channel",
   ["Activate an Information 1 source on an amplified system",
    "Trigger a confirmation tone",
    "Record the audio present on the amplifier Information 1 channel"],
   ["The Information 1 source is active",
    "The confirmation tone is triggered",
    "The amplifier Information 1 channel carries both the Information 1 audio and the tone"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="Second channel named at 4865968.")

tc("SWE1_AMM_015",
   "Confirm a confirmation tone is kept off the Information 2 channel",
   ["Activate an Information 2 source on an amplified system",
    "Trigger a confirmation tone",
    "Record the audio present on the amplifier Information 2 channel"],
   ["The Information 2 source is active",
    "The confirmation tone is triggered",
    "The amplifier Information 2 channel carries the Information 2 audio without the tone"],
   prio="P1", method=NEGATIVE, pre="No audio source is active",
   reasoning="4865969 is the suppression counterpart of 4865968. Written as a "
             "negative case because the defect it guards against is a tone "
             "leaking into a path that must stay clean.")

tc("SWE1_AMM_030",
   "Confirm source selection follows the established priorities and the user request",
   ["Play an Entertainment source",
    "Request an Information 1 source",
    "Record which source is selected"],
   ["Entertainment audio plays",
    "The Information 1 source is requested",
    "The selected source follows the established source priorities"],
   desc=("The Audio Management software shall arbitrate concurrent audio requests according to the configured source priority, with INFO1 and INFO2 having higher priority than ENT"),
   prio="P1", method=DECISION,
   reasoning="Partial coverage, ruled at package 08 section 2.1. 4866054 covers "
             "source selection by established priority and user request, and "
             "this case goes no further than that wording. The leaf's duck, "
             "mute, reject and pause action set has no text anywhere in "
             "CFTS019 — zero hits — so it is not written; it is filed to "
             "DR-AM1 as material from the 1.3.4 condition tables or the "
             "{CFTS019-5129} cross-reference.")

tc("SWE1_AMM_031",
   "Confirm an activating Information 2 source takes priority over the conflicting streams",
   ["Play an Entertainment source",
    "Activate an Information 2 source",
    "Record which source holds priority and the state of the Entertainment stream"],
   ["Entertainment audio plays",
    "The Information 2 source becomes active",
    "The Information 2 source holds priority and the Entertainment stream is interrupted"],
   prio="P0", method=DECISION,
   reasoning="Shares 4866055 with SWE1_AMM_032 under R-AM16, the upstream having "
             "split one CFTS requirement into two SWE leaves. Per that ruling "
             "the two brackets must state different emphases: this row observes "
             "the priority grant and the transition to the interrupted state.")

tc("SWE1_AMM_032",
   "Confirm a pausable source stays paused until every Information 2 source ends",
   ["Play a USB media track",
    "Activate an Information 2 source",
    "Record the transport state of the USB media source",
    "End the Information 2 source",
    "Record the transport state of the USB media source again"],
   ["The USB media track plays",
    "The Information 2 source becomes active",
    "The USB media source reports the paused state",
    "The Information 2 source ends",
    "The USB media source resumes"],
   prio="P0", method=STATE,
   reasoning="The other half of the R-AM16 shared anchor: this row observes the "
             "pause of a source with pause capability and its release once no "
             "Information 2 source remains. spec_reference carries 4866054 as "
             "well, because the leaf's opening sentence on INFO2 outranking ENT "
             "and INFO1 belongs to that object rather than to 4866055.")

tc("SWE1_AMM_086",
   "Confirm the priority rules hold across Entertainment, Information and Signal sources",
   ["Play an Entertainment source under an Ignition Working Condition",
    "Activate an Information source",
    "Trigger a signal source",
    "Record which source is audible on each output channel"],
   ["Entertainment audio plays",
    "The Information source becomes active",
    "The signal source is raised",
    "The audible source on each output channel follows the configured priority"],
   prio="P1", method=DECISION,
   reasoning="Re-anchored to 4866442 per package 08 section 2.7 on coverage "
             "rather than similarity: the earlier candidate 4866220 scopes "
             "itself to at least two information sources, narrower than the "
             "leaf, while 4866442 spans Entertainment, Information and Signal "
             "under any Ignition Working Condition.")

tc("SWE1_AMM_233",
   "Confirm a signal source reaches every output channel while two Information sources run",
   ["Activate two Information sources",
    "Trigger a signal source",
    "Record the output channels carrying the signal source"],
   ["Both Information sources are active",
    "The signal source is raised",
    "Every output channel carries the signal source"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="Partial coverage, ruled at package 08 section 2.4. 4866916 states "
             "only the mixing onto all output channels; the leaf's ducking "
             "level for the Information sources has no counterpart in the "
             "anchor, so it is not written.")

tc("SWE1_AMM_286",
   "Confirm Alternate Audio is mixed with Main Audio before it reaches the outputs",
   ["Play a Main Audio source",
    "Activate an Alternate Audio source",
    "Record the audio present at the speaker and external amplifier feed"],
   ["The Main Audio source plays",
    "The Alternate Audio source becomes active",
    "The speaker and external amplifier feed carries both sources mixed"],
   prio="P0", method=FUNC,
   reasoning="4866817, in scope under R-AM14: the chapter heading names CarPlay "
             "but the requirement is a mixing behaviour, and the upstream "
             "produced SWE1_AMM leaves for it. Out-of-pool anchor, corroborated "
             "by the full text (R-AM2').")

tc("SWE1_AMM_287",
   "Confirm a ducking request attenuates Main Audio while Alternate Audio holds its level",
   ["Play a Main Audio source at a known level",
    "Activate an Alternate Audio source that carries a ducking request",
    "Measure the Main Audio level against its starting level and record it",
    "Record the Alternate Audio level"],
   ["The Main Audio source plays at the set level",
    "The Alternate Audio source becomes active with a ducking request",
    f"The Main Audio level is {VENT_OFF} below its starting level",
    "The Alternate Audio holds its level"],
   desc=("When an active Alternate Audio source requests ducking, the Audio Management software shall apply the configured ducking attenuation to the active Main Audio source within <vent off>"),
   prio="P0", method=FUNC,
   reasoning="4866818, in scope under R-AM14. The attenuation <Vent off> is "
             "defined at CFTS019-4867782 as -16 dB, so the value is "
             "spec-sourced. It stays distinct from <Vent Nav Off> at 9 steps, "
             "which belongs to the navigation chain. Out-of-pool anchor, "
             "corroborated by the full text (R-AM2\').")

tc("SWE1_AMM_309",
   "Confirm a pausable playback source is paused for the duration of a hands-free call",
   ["Play a CD",
    "Establish a hands-free call",
    "Record the transport state of the CD",
    "End the hands-free call",
    "Record the transport state of the CD again"],
   ["The CD plays",
    "The hands-free call audio is active",
    "The CD reports the paused state",
    "The hands-free call ends",
    "The CD resumes"],
   prio="P0", method=STATE,
   reasoning="4866484, ruled at package 08 section 2.5 after route 2 found it. "
             "Taken over the neighbouring 4866485 on two grounds: its Radio "
             "list carries R1L-R, and its text stops at HFP where 4866485 also "
             "covers E-Call and R-Call, wider than the leaf. Out-of-pool "
             "anchor, corroborated by the full text (R-AM2').")

tc("SWE1_AMM_312",
   "Confirm fixed fade-out keeps the Entertainment volume independent of Navigation",
   ["Set Navigation Entertainment Fade Out to \"Fixed\"",
    "Play an Entertainment source at a fixed volume step",
    "Trigger a Navigation guidance prompt",
    "Record the Entertainment volume step"],
   ["Navigation Entertainment Fade Out is \"Fixed\"",
    "Entertainment audio plays at the set volume step",
    "The Navigation guidance prompt starts",
    "The Entertainment volume step follows the customer selection and does not track the Navigation volume"],
   prio="P0", method=DECISION, pre="No audio source is active",
   reasoning="4867669 is the Fixed branch of the fade-out configuration; 313 is "
             "the Relative branch. The two are mutually exclusive settings, so "
             "each needs its own row. Out-of-pool anchor, corroborated by the "
             "full text (R-AM2').")

tc("SWE1_AMM_313",
   "Confirm relative fade-out puts Navigation in control of the Entertainment level",
   ["Set Navigation Entertainment Fade Out to \"Relative\"",
    "Play an Entertainment source",
    "Trigger a Navigation guidance prompt",
    "Record the Entertainment volume step against the Navigation level"],
   ["Navigation Entertainment Fade Out is \"Relative\"",
    "Entertainment audio plays",
    "The Navigation guidance prompt starts",
    "The Entertainment volume step follows the Navigation level"],
   prio="P0", method=DECISION, pre="No audio source is active",
   reasoning="4867670, the Relative branch against 312's Fixed branch. Out-of-"
             "pool anchor, corroborated by the full text (R-AM2').")

tc("SWE1_AMM_314",
   "Confirm the Entertainment level drops by the specified attenuation during Navigation",
   ["Play an Entertainment source",
    "Trigger a Navigation guidance prompt",
    "Read the Information source volume level and the Entertainment volume level and record them"],
   ["Entertainment audio plays",
    "The Navigation guidance prompt starts",
    f"The Entertainment volume level is {VENT_NAV_OFF} below the Information source volume level"],
   prio="P0", method=FUNC,
   reasoning="4867671 gives the attenuation as <Vent Nav Off>, defined at 9 "
             "steps near 4867783, so the expected result carries the real "
             "value rather than a placeholder. Out-of-pool anchor, "
             "corroborated by the full text (R-AM2').")

tc("SWE1_AMM_315",
   "Confirm the Entertainment output mutes when the attenuation reaches step 0",
   ["Play an Entertainment source at a volume step below the attenuation amount",
    "Trigger a Navigation guidance prompt",
    "Record the audio on every Entertainment output channel"],
   ["Entertainment audio plays at the set volume step",
    "The Navigation guidance prompt starts",
    "Every Entertainment output channel is muted"],
   prio="P0", method=BVA,
   reasoning="4867672 is the floor of the 4867671 attenuation, so it is a "
             "boundary case: the step reaches 0 and the behaviour changes from "
             "attenuate to mute. Out-of-pool anchor, corroborated by the full "
             "text (R-AM2').")
tc("SWE1_AMM_315",
   "Confirm that mute leaves the Entertainment source playing rather than paused",
   ["Play an Entertainment source at a volume step below the attenuation amount",
    "Trigger a Navigation guidance prompt",
    "Read the transport state of the Entertainment source and record it"],
   ["Entertainment audio plays at the set volume step",
    "The Navigation guidance prompt starts",
    "The Entertainment source reports the playing state"],
   prio="P0", method=NEGATIVE,
   reasoning="4867672 says without PAUSE, which package 08 section 3.1 flags as "
             "the key separation from the pause behaviour at 032 and 309. A "
             "system that paused the source would satisfy the mute observation "
             "and still be wrong, so the transport state is checked on its own.")

tc("SWE1_AMM_316",
   "Confirm the transmitted Entertainment volume carries the attenuation",
   ["Play an Entertainment source at a known customer-selected volume step",
    "Trigger a Navigation guidance prompt",
    "Read $VolumeENT$ and record it"],
   ["Entertainment audio plays at the customer-selected volume step",
    "The Navigation guidance prompt starts",
    f"$VolumeENT$ reports the customer-selected volume step minus {VENT_NAV_OFF}"],
   prio="P0", method=FUNC, remarks=PEND_SIG,
   reasoning="4867673 is the transmission counterpart of the attenuation at "
             "4867671 — the same subtraction, observed on the bus rather than "
             "in the output. $VolumeENT$ is absent from the supplied DBC, so "
             "the name stays as CFTS019 writes it under v3 (g). Out-of-pool "
             "anchor, corroborated by the full text (R-AM2').")

tc("SWE1_AMM_317",
   "Confirm a Navigation volume increase moves the Entertainment volume by the same amount",
   ["Trigger a Navigation guidance prompt while an Entertainment source plays",
    "Increase the Navigation volume by 2 steps",
    "Read the Entertainment volume step and record it"],
   ["The Navigation guidance prompt plays over the Entertainment source",
    "The Navigation volume increases by 2 steps",
    "The Entertainment volume step increases by 2 steps"],
   prio="P1", method=FUNC, pre="An Entertainment source is active",
   reasoning="4867674 uses an increase of 2 steps as its own example, so the "
             "case follows the clause rather than inventing a figure. Out-of-"
             "pool anchor, corroborated by the full text (R-AM2').")
tc("SWE1_AMM_317",
   "Confirm a Navigation volume decrease tracks in the same direction",
   ["Trigger a Navigation guidance prompt while an Entertainment source plays",
    "Decrease the Navigation volume by 2 steps",
    "Read the Entertainment volume step and record it"],
   ["The Navigation guidance prompt plays over the Entertainment source",
    "The Navigation volume decreases by 2 steps",
    "The Entertainment volume step decreases by 2 steps"],
   prio="P1", method=FUNC, pre="An Entertainment source is active",
   reasoning="The clause says the same adjustment, which covers both "
             "directions; an implementation that only tracked increases would "
             "pass the first case.")

# ------------------------------------------------------------ Mute Requests
tc("SWE1_AMM_027",
   "Confirm the idle telematics state holds the output channels muted",
   ["Set TLM_Status.Info to \"Idle\"",
    "Record the state of the output channels",
    "Read $ENTMuted$ and record it"],
   ["TLM_Status.Info reports \"Idle\"",
    "The output channels are muted",
    "$ENTMuted$ reports \"Muted\""],
   prio="P1", method=STATE, remarks=PEND_SIG, pre="No audio source is active",
   reasoning="4866032 is the mute half of the TLM state pair; 028 is the unmute "
             "half. TLM_Status.Info is an internal signal name kept without a "
             "dollar wrapper per 8.7.5 v3 (d).")

tc("SWE1_AMM_028",
   "Confirm the operational telematics states release the mute",
   ["Set TLM_Status.Info to \"Full-Operation\"",
    "Record the state of the output channels",
    "Read $ENTMuted$ and record it"],
   ["TLM_Status.Info reports \"Full-Operation\"",
    "The output channels are not muted",
    "$ENTMuted$ reports \"Not_Muted\""],
   prio="P1", method=STATE, remarks=PEND_SIG, pre="No audio source is active",
   reasoning="4866033 names Full-Operation and Timed in one OR; this takes the "
             "first. The clause also bounds the release by <Tdelay>, which is "
             "not observed here because the leaf states the state change "
             "rather than the timing.")

tc("SWE1_AMM_058",
   "Confirm the Entertainment mute state is published on every change",
   ["Play an Entertainment source",
    "Mute the Entertainment audio",
    "Read $ENTMuted$ and record it"],
   ["Entertainment audio plays",
    "The Entertainment audio is muted",
    "$ENTMuted$ reports \"Muted\""],
   prio="P1", method=FUNC, remarks=PEND_SIG,
   reasoning="4866120 and 4866129 carry the same indication rule in different "
             "chapters, so 058 and 066 are a same-text-different-anchor pair. "
             "This row observes publication on a change of state.")

tc("SWE1_AMM_066",
   "Confirm the published mute state stays synchronised with the source",
   ["Play an Entertainment source",
    "Mute the Entertainment audio",
    "Unmute the Entertainment audio",
    "Read $ENTMuted$ and record it"],
   ["Entertainment audio plays",
    "The Entertainment audio is muted",
    "The Entertainment audio is unmuted",
    "$ENTMuted$ reports \"Not_Muted\""],
   prio="P1", method=FUNC, remarks=PEND_SIG,
   reasoning="The 4866129 half of the pair with 058. Distinguished by observing "
             "the signal after a full mute and unmute cycle, where 058 observes "
             "a single transition — otherwise the two rows would read alike.")

tc("SWE1_AMM_059",
   "Confirm an Information source mute leaves the Entertainment mute signal alone",
   ["Play an Entertainment source and an Information source",
    "Mute the Information source",
    "Read $ENTMuted$ and record it"],
   ["Both sources play",
    "The Information source is muted",
    "$ENTMuted$ reports \"Not_Muted\""],
   prio="P1", method=NEGATIVE, remarks=PEND_SIG,
   reasoning="4866121 scopes the signal to Entertainment only. The defect it "
             "guards against is a shared mute flag, which only a negative case "
             "on a non-Entertainment source can expose.")

tc("SWE1_AMM_060",
   "Confirm the mute button mutes an unmuted Entertainment source",
   ["Play an Entertainment source",
    "Send $ICSMuteButton$ = \"pressed\"",
    "Record the mute state of the Entertainment audio"],
   ["Entertainment audio plays",
    "$ICSMuteButton$ reports \"pressed\"",
    "The Entertainment audio is muted"],
   prio="P1", method=STATE, remarks=PEND_SIG,
   reasoning="4866122 specifies a toggle, so both directions belong to the "
             "clause. This is the mute direction.")
tc("SWE1_AMM_060",
   "Confirm the same button unmutes a muted Entertainment source",
   ["Play an Entertainment source and mute it",
    "Send $ICSMuteButton$ = \"pressed\"",
    "Record the mute state of the Entertainment audio"],
   ["The Entertainment audio is muted",
    "$ICSMuteButton$ reports \"pressed\"",
    "The Entertainment audio is not muted"],
   prio="P1", method=STATE, remarks=PEND_SIG,
   reasoning="The unmute direction of the same toggle at 4866122. A latch that "
             "only muted would pass the first case.")

tc("SWE1_AMM_061",
   "Confirm the power button press is received and enters the mute path",
   ["Play an Entertainment source",
    "Send $ICSPowerButton$ = \"pressed\"",
    "Record the mute state of the Entertainment audio"],
   ["Entertainment audio plays",
    "$ICSPowerButton$ reports \"pressed\"",
    "The Entertainment audio mute state changes"],
   desc=("Upon receiving $ICSPowerButton$ = pressed, the Audio Management software shall evaluate the current audio and screen state and determine whether the POWER-button mute action is processed or ignored"),
   prio="P1", method=FUNC, remarks=f"{PEND_CFTS020}; {PEND_SIG}",
   reasoning="Partial coverage, ruled at package 08 section 2.3. 4866123 states "
             "the trigger and then hands the mute logic to {CFTS020}, which is "
             "not among the sources. The case therefore observes only what "
             "CFTS019 supports — the signal arriving and the mute path being "
             "entered — and the logic itself carries a PENDING. Nothing about "
             "CFTS020's content is guessed.")

tc("SWE1_AMM_068",
   "Confirm the telematics mute switch toggles an active Entertainment source",
   ["Play an Entertainment source with no ICS node present",
    "Press TLM_Mute.Switch",
    "Read $ENTMuted$ and record it"],
   ["Entertainment audio plays and no ICS node is present",
    "TLM_Mute_Setup.Req reports \"Pressed\"",
    "$ENTMuted$ reports the toggled state"],
   desc=("When $ICSPresent$ indicates Not Present and TLM_Mute_Setup.Req indicates Pressed, the Audio Management software shall toggle the mute state of an active Entertainment source"),
   prio="P1", method=DECISION, remarks=PEND_SIG,
   reasoning="4866131 branches on whether an Entertainment source is active. "
             "This takes the active branch; the second takes the inactive "
             "branch, where the event is ignored.")
tc("SWE1_AMM_068",
   "Confirm the same switch is ignored when no Entertainment source is active",
   ["Confirm no Entertainment source is active and no ICS node is present",
    "Press TLM_Mute.Switch",
    "Read $ENTMuted$ and record it"],
   ["No Entertainment source is active and no ICS node is present",
    "TLM_Mute_Setup.Req reports \"Pressed\"",
    "$ENTMuted$ is unchanged"],
   desc=("When $ICSPresent$ indicates Not Present and TLM_Mute_Setup.Req indicates Pressed, the Audio Management software shall toggle the mute state of an active Entertainment source"),
   prio="P1", method=NEGATIVE, remarks=PEND_SIG,
   reasoning="The ignore branch of 4866131. Without it a system that toggled "
             "unconditionally would pass the active case.")

tc("SWE1_AMM_069",
   "Confirm the telematics mute status toggles an active Entertainment source",
   ["Play an Entertainment source",
    "Send TLM_Mute_Status.Info = \"Pressed\"",
    "Read $ENTMuted$ and record it"],
   ["Entertainment audio plays",
    "TLM_Mute_Status.Info reports \"Pressed\"",
    "$ENTMuted$ reports the toggled state"],
   desc=("Upon receiving TLM_Mute_Status.Info = Pressed, the Audio Management software shall evaluate the Entertainment source activity state and toggle the mute state when a source is active"),
   prio="P1", method=DECISION, remarks=PEND_SIG,
   reasoning="4866132 carries the same two branches as 4866131 but keys on the "
             "status message rather than the switch press, so the two leaves "
             "exercise different inputs to the same decision.")
tc("SWE1_AMM_069",
   "Confirm the status message is ignored when no Entertainment source is active",
   ["Confirm no Entertainment source is active",
    "Send TLM_Mute_Status.Info = \"Pressed\"",
    "Read $ENTMuted$ and record it"],
   ["No Entertainment source is active",
    "TLM_Mute_Status.Info reports \"Pressed\"",
    "$ENTMuted$ is unchanged"],
   desc=("Upon receiving TLM_Mute_Status.Info = Pressed, the Audio Management software shall evaluate the Entertainment source activity state and toggle the mute state when a source is active"),
   prio="P1", method=NEGATIVE, remarks=PEND_SIG,
   reasoning="The ignore branch of 4866132.")

tc("SWE1_AMM_070",
   "Confirm an internal mute stores the Entertainment volume before muting",
   ["Play an Entertainment source at volume level 20",
    "Raise an internal mute condition",
    "Read $ENTMuted$ and record it"],
   ["Entertainment audio plays at volume level 20",
    "The internal mute condition is active",
    "$ENTMuted$ reports \"Muted\""],
   desc=("Upon activation of an internal mute condition, the Audio Management software shall preserve the current $VolumeENT$ value and Entertainment mute state and set $ENTMuted$ to Muted"),
   prio="P1", method=STATE, remarks=PEND_SIG,
   reasoning="4866133 pairs a store with a later restore. This row observes the "
             "store and the mute; the second observes the restore, which is "
             "what proves the stored value was kept rather than defaulted.")
tc("SWE1_AMM_070",
   "Confirm clearing the internal mute restores the stored volume",
   ["Play an Entertainment source at volume level 20",
    "Raise an internal mute condition",
    "Clear the internal mute condition",
    "Read the Entertainment volume level and record it"],
   ["Entertainment audio plays at volume level 20",
    "The internal mute condition is active",
    "The internal mute condition is cleared",
    "The Entertainment volume level is 20"],
   desc=("Upon activation of an internal mute condition, the Audio Management software shall preserve the current $VolumeENT$ value and Entertainment mute state and set $ENTMuted$ to Muted"),
   prio="P1", method=STATE,
   reasoning="The restore half of 4866133.")

tc("SWE1_AMM_071",
   "Confirm a volume change lifts an ordinary Entertainment mute",
   ["Play an Entertainment source at volume level 20 and mute it",
    "Change the Entertainment volume",
    "Read the Entertainment volume level and the mute state and record them"],
   ["The Entertainment audio is muted",
    "The volume change is accepted",
    "The Entertainment audio is not muted and plays at volume level 20"],
   desc=("While Entertainment audio is Muted, the Audio Management software shall process a valid user volume-change request as an unmute request when the mute state is not caused by an internal mute condition"),
   prio="P1", method=STATE,
   reasoning="4866134 makes a volume change an implicit unmute and recalls the "
             "stored level. This takes the ordinary mute; the second takes the "
             "internal-mute exception the clause carves out.")
tc("SWE1_AMM_071",
   "Confirm a volume change does not lift an internal mute",
   ["Play an Entertainment source and raise an internal mute condition",
    "Change the Entertainment volume",
    "Record the mute state of the Entertainment audio"],
   ["The internal mute condition is active",
    "The volume change is accepted",
    "The Entertainment audio stays muted"],
   desc=("While Entertainment audio is Muted, the Audio Management software shall process a valid user volume-change request as an unmute request when the mute state is not caused by an internal mute condition"),
   prio="P1", method=NEGATIVE,
   reasoning="The exception at 4866134. It is the only branch that separates an "
             "internal mute from a user mute, so a system that treated them "
             "alike would pass the first case and fail here.")

tc("SWE1_AMM_076",
   "Confirm the Information mute behaviour follows the configured mute enablement",
   ["Enable the Information source mute condition through the configured specification",
    "Activate an Information source",
    "Record the mute behaviour of the Information source"],
   ["The Information source mute condition is enabled",
    "The Information source becomes active",
    "The Information source mute behaviour follows the configured enablement"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="Partial coverage, ruled at package 08 section 2.6. 4866155 scopes "
             "the mute behaviour to what the HU HMI Specification and the "
             "routing table enable. The routing table is an external document, "
             "so no specific routing correspondence is written; that part goes "
             "to DR-AM1. This is the 076b row, SYS-RA-AMM-246; the delivery "
             "column still reads SWE1_AMM_076 under R-AM6.")

tc("SWE1_AMM_078",
   "Confirm the mute request is ignored when the ICS node is absent",
   ["Confirm no ICS node is present",
    "Press TLM_Mute.Switch",
    "Record the Information source mute state"],
   ["No ICS node is present",
    "TLM_Mute_Setup.Req reports \"Pressed\"",
    "The Information source mute state is unchanged"],
   prio="P1", method=NEGATIVE,
   reasoning="4866157 is the Information-side counterpart of the Entertainment "
             "handling at 4866131: same trigger, no node, but the event is "
             "ignored outright rather than branched on source activity.")

tc("SWE1_AMM_079",
   "Confirm the mute status event is ignored when the ICS node is absent",
   ["Confirm no ICS node is present",
    "Send TLM_Mute_Status.Info = \"Pressed\"",
    "Record the Information source mute state"],
   ["No ICS node is present",
    "TLM_Mute_Status.Info reports \"Pressed\"",
    "The Information source mute state is unchanged"],
   prio="P1", method=NEGATIVE,
   reasoning="4866158 is to 4866157 what 4866132 is to 4866131 — the status "
             "message path rather than the switch press.")

for sid, anchor, what, sig, val in (
        ("SWE1_AMM_179", "4866689", "Entertainment audio", "$ENTMuted$", "\"Muted\""),
        ("SWE1_AMM_180", "4866690", "Information 1 audio", "$VolumeINFO1$", "0"),
        ("SWE1_AMM_181", "4866691", "Information 2 audio", "$VolumeINFO2$", "0")):
    tc(sid,
       f"Confirm a fleet mute request mutes the {what} within the display response time",
       ["Play the affected audio source",
        "Send $VSIMMuteReq$ = \"Mute\"",
        f"Read {sig} and record it",
        "Measure the time from the request to the response and record it"],
       ["The affected audio source plays",
        "$VSIMMuteReq$ reports \"Mute\"",
        f"{sig} reports {val}",
        f"The measured response time is {TDISP}"],
       prio="P1", method=FUNC, remarks=PEND_SIG,
       reasoning=f"{anchor} is one of four parallel clauses in 1.3.3.5, each "
                 f"naming a different audio path. The response bound <Tdisp> is "
                 f"defined at Max = 100 ms in CFTS019, so the timing step "
                 f"carries a real value. Package 08 section 3.4 records that "
                 f"4866689 to 4866694 are the mute group and 4866695 to "
                 f"4866698 the unmute group, so there is no same-text ambiguity "
                 f"to resolve here.")

tc("SWE1_AMM_182",
   "Confirm a fleet mute request mutes the hands-free microphone and updates the display",
   ["Establish a hands-free call on a vehicle equipped with a hands-free microphone",
    "Send $VSIMMuteReq$ = \"Mute\"",
    "Record the state of the hands-free microphone",
    "Measure the time from the request to the display update and record it"],
   ["The hands-free call is active",
    "$VSIMMuteReq$ reports \"Mute\"",
    "The hands-free microphone is muted",
    f"The measured display update time is {TDISP}"],
   prio="P1", method=FUNC, remarks=PEND_SIG,
   reasoning="4866692 is the microphone member of the same 1.3.3.5 group. The "
             "clause qualifies it with if equipped, so the case states the "
             "equipped vehicle in its first step rather than assuming it.")

tc("SWE1_AMM_184",
   "Confirm releasing the fleet mute restores Entertainment audio",
   ["Play an Entertainment source and send $VSIMMuteReq$ = \"Mute\"",
    "Send $VSIMMuteReq$ = \"Unmute\"",
    "Read $ENTMuted$ and record it"],
   ["The Entertainment audio is muted",
    "$VSIMMuteReq$ reports \"Unmute\"",
    "$ENTMuted$ reports \"Unmuted\""],
   prio="P1", method=STATE, remarks=PEND_SIG,
   reasoning="4866695 is the unmute counterpart of 4866689. This takes the "
             "clean case where nothing else holds the mute.")
tc("SWE1_AMM_184",
   "Confirm the release is withheld while another mute reason is still active",
   ["Play an Entertainment source and send $VSIMMuteReq$ = \"Mute\"",
    "Raise a second mute condition",
    "Send $VSIMMuteReq$ = \"Unmute\"",
    "Read $ENTMuted$ and record it"],
   ["The Entertainment audio is muted",
    "The second mute condition is active",
    "$VSIMMuteReq$ reports \"Unmute\"",
    "$ENTMuted$ reports \"Muted\""],
   prio="P1", method=NEGATIVE, remarks=PEND_SIG,
   reasoning="The guard at 4866695 is if no other reasons to mute are active. "
             "A system that unmuted on the transition alone would pass the "
             "first case and drop audio protection here.")


def main() -> None:
    ctx = {l["swe_id"]: l for l in json.loads(
        (ROOT / "batches" / "B2_context.json").read_text(encoding="utf-8"))}
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
                # Ascending within the document, one id per line (IN 10.7).
                "spec_reference": "\n".join(
                    f"CFTS019-{a}" for a in sorted(leaf["anchors"])),
                "priority": e["prio"],
                "design_method": e["method"],
                "remarks": e["remarks"],
                "reasoning": e["reasoning"],
            })

    out_of_pool = sorted(k for k, v in ctx.items() if not v["anchor_in_pool"])
    out = {"batch": "B2", "feature": "Audio Management",
           "test_group": "Audio Management", "n_tcs": len(tcs),
           "leaves_authored": len(AUTHORED),
           "out_of_pool_anchors": [
               {"swe_id": k, "anchor": f"CFTS019-{ctx[k]['anchor']}",
                "title": ctx[k]["title"], "test_set": ctx[k]["test_set"],
                "basis": "State:Approved in the CFTS019 full text; absent from "
                         "both Basic Reports (A-AM03 / DR-AM3)"}
               for k in out_of_pool],
           "tcs": tcs}
    dest = ROOT / "generated" / "B2.json"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2),
                    encoding="utf-8")
    print(f"wrote {dest.relative_to(ROOT.parent.parent)}")
    print(f"  leaves authored {len(AUTHORED)}")
    print(f"  TCs             {len(tcs)}")
    print(f"  out-of-pool     {len(out_of_pool)}")


if __name__ == "__main__":
    main()
