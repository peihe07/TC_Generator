#!/usr/bin/env python3
"""Emit the B1 test cases for audio_mgmt.

The upper half of every `test_item` is taken verbatim from the SWE.1
Requirement Description in `batches/B1_context.json` — it is never retyped
here, so it cannot drift from the source (package 03 section 3.2 / IN R-S4).
Only the bracketed purpose line and the test body are authored below.

Seven anchors sit outside the R-AM2 pool. Pei ruled them written as given
(R-AM2', 2026-08-26); each says so in its reasoning and they are listed in the
`out_of_pool_anchors` register the submission package needs.

Usage:
    python features/audio_mgmt/scripts/gen_b1.py
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

# Spec-sourced timing, CFTS019-4867766..4867769 and 4867773.
RAMP = "25 ms to 50 ms"
TMUTE_AMP = "at most 100 ms"

# <Temp Ramp Down> / <Temt Ramp Down> are used by the spec but never defined
# in it; the only defined entertainment ramp-down is <Tent Ramp Down>. The
# execution layer does not infer (package 03 preamble), so these carry a
# PENDING and the reading is proposed to the analysis layer as A-AM04.
PEND_TEMP = ("PENDING: DR-AM5 <Temp Ramp Down> value not defined in "
             "available sources")
PEND_SIG = ("PENDING: DR-AM4 $HUModeStatus$ not found in the supplied DBC; "
            "signal name kept as written in CFTS019 per R-13 (g)")
PEND_VOL = ("PENDING: DR-AM4 $VolumeENT$ not found in the supplied DBC; "
            "signal name kept as written in CFTS019 per R-13 (g)")

AUTHORED: dict[str, list[dict]] = {}


def tc(swe_id, purpose, proc, er, *, prio="P1", method=FUNC, pre="NA",
       data="NA", remarks="", reasoning="", desc=None, extra_refs=()):
    AUTHORED.setdefault(swe_id, []).append(dict(
        purpose=purpose, proc=proc, er=er, prio=prio, method=method,
        pre=pre, data=data, remarks=remarks, reasoning=reasoning,
        desc=desc, extra_refs=list(extra_refs)))


# ---------------------------------------------------------------- 132..144
tc("SWE1_AMM_132",
   "Confirm every active media function is cancelled before the source transition starts",
   ["Play an FM station and start a \"SEEK\" operation",
    "Select a different audio source while the seek is still running",
    "Read the state of the seek operation and record it",
    "Record the order of the seek operation end and the source transition start"],
   ["FM audio plays and the seek operation runs",
    "The source selection is accepted",
    "The seek operation is cancelled",
    "The source transition starts with no media function still active"],
   prio="P0", method=SCENARIO,
   reasoning="4866468 lists the media functions to interrupt; SEEK is chosen as the "
             "representative because the SWE.1 Verification Method names seek and scan.")
tc("SWE1_AMM_132",
   "Confirm a running scan is cancelled by the same transition path as a seek",
   ["Play an FM station and start a \"SCAN\" operation",
    "Select a different audio source while the scan is still running",
    "Record the order of the scan cancellation and the source transition"],
   ["FM audio plays and the scan operation runs",
    "The source selection is accepted",
    "The scan operation is cancelled and no media function remains active"],
   prio="P1", method=SCENARIO,
   reasoning="Second function from the 4866468 list, kept separate so a pass on seek "
             "cannot mask a failure on scan.")

tc("SWE1_AMM_133",
   "Confirm Entertainment audio is ramped down to mute over the specified ramp duration",
   ["Play an Entertainment source at a fixed volume",
    "Select another Entertainment source",
    "Measure the time between the start of the level decrease and silence",
    "Compare the measured ramp-down time against the specification and record the outcome"],
   ["Entertainment audio plays at the set volume",
    "The new source selection is accepted",
    f"The Entertainment level decreases gradually to mute within {RAMP}",
    f"The measured ramp-down time is within {RAMP}"],
   prio="P0", method=STATE,
   reasoning="4866469 states the ramp-down uses <Tent Ramp Down>; the value is taken "
             "from CFTS019-4867767, so the step carries a real bound and not a placeholder.",
   extra_refs=["4867767"])

tc("SWE1_AMM_134",
   "Confirm the newly selected Entertainment source becomes active once the transition completes",
   ["Play Entertainment source A",
    "Select Entertainment source B",
    "Wait until the ramp-down of source A has completed",
    "Record which Entertainment source is active"],
   ["Entertainment source A plays",
    "The selection of source B is accepted",
    "Source A is muted",
    "Source B is the active Entertainment source"],
   prio="P0", method=STATE,
   reasoning="4866470 is the activation step of the sequence; the check is placed after "
             "ramp-down completion because that is the ordering the clause states.")

tc("SWE1_AMM_135",
   "Confirm the mute is held for ramp-down plus amplifier mute plus ramp-up before audio returns",
   ["Play Entertainment source A",
    "Select Entertainment source B",
    "Measure the interval during which the output stays muted",
    "Compare the measured mute interval against the sum of the three specified intervals and record the outcome"],
   ["Entertainment source A plays",
    "The selection of source B is accepted",
    f"The output stays muted for the ramp-down ({RAMP}), the amplifier mute "
    f"({TMUTE_AMP}) and the ramp-up ({RAMP})",
    "The measured mute interval matches the sum of the three specified intervals"],
   prio="P0", method=STATE,
   reasoning="4866471 composes the hold from <Tent Ramp Down> + <Tmute amp> + "
             "<Tent Ramp Up>; all three have spec values (4867767, 4867773, 4867766), "
             "so the whole sum is spec-sourced.",
   extra_refs=["4867766", "4867767", "4867773"])

tc("SWE1_AMM_136",
   "Confirm the mode status signal reports the new Entertainment source once ramp-down completes",
   ["Play Entertainment source A",
    "Select Entertainment source B",
    "Record $HUModeStatus$ from the vehicle bus",
    "Read $HUModeStatus$ at the moment the ramp-down completes and record it"],
   ["Entertainment source A plays",
    "The selection of source B is accepted",
    "$HUModeStatus$ is transmitted",
    "$HUModeStatus$ reports source B immediately after the ramp-down completes"],
   prio="P0", method=STATE, remarks=PEND_SIG,
   reasoning="4866472 names $HUModeStatus$ but the supplied DBC carries no such signal "
             "and no variant of it, so the name is kept verbatim per R-13 (g) and the "
             "gap is raised as DR-AM4 rather than resolved by substituting a lookalike.")

tc("SWE1_AMM_137",
   "Confirm Entertainment audio ramps back up to the recalled volume within the specified time",
   ["Play Entertainment source A at volume level 20",
    "Select Entertainment source B",
    "Wait until the mute hold has completed",
    "Measure the ramp-up time and the final volume",
    "Compare the measured ramp-up time against the specification and read the restored volume level"],
   ["Entertainment source A plays at volume level 20",
    "The selection of source B is accepted",
    "The output is muted for the hold interval",
    f"The Entertainment level increases to volume level 20 within {RAMP}",
    f"The measured ramp-up time is within {RAMP} and the volume is level 20"],
   prio="P0", method=STATE,
   reasoning="4866477 ties the ramp-up to <Tent Ramp Up> and to the recalled volume; "
             "volume level 20 is an arbitrary but fixed level so the recall is observable.",
   extra_refs=["4867766"])

tc("SWE1_AMM_142",
   "Confirm a pause is issued to a media source that supports pause before it is deactivated",
   ["Play a USB media track",
    "Select a different Entertainment source",
    "Read the transport state of the USB media source and record it",
    "Record the order of the USB media pause and its deactivation"],
   ["The USB media track plays",
    "The new source selection is accepted",
    "The USB media source reports the paused state",
    "The pause precedes the deactivation of the USB media source"],
   prio="P1", method=SCENARIO,
   reasoning="4866492 qualifies the pause with \"if possible\", so a pause-capable "
             "source (USB media) is used to make the positive case observable.")

tc("SWE1_AMM_143",
   "Confirm media control operations are cancelled before the Entertainment source is deactivated",
   ["Play an FM station and start a \"PTY SEEK\" operation",
    "Select a different Entertainment source",
    "Record the order of the PTY seek cancellation and the Entertainment source deactivation"],
   ["FM audio plays and the PTY seek runs",
    "The new source selection is accepted",
    "The PTY seek is cancelled and the cancellation precedes the deactivation"],
   prio="P1", method=SCENARIO,
   reasoning="4866493 repeats the 4866468 function list at the deactivation point; "
             "PTY SEEK is used here so this case does not duplicate the SWE1_AMM_132 pair.")

tc("SWE1_AMM_144",
   "Confirm Entertainment audio ramps down when an Information source becomes active",
   ["Play an Entertainment source at a fixed volume",
    "Trigger a Navigation guidance prompt",
    "Measure the Entertainment ramp-down time",
    "Measure the Entertainment ramp-down time and record it"],
   ["Entertainment audio plays at the set volume",
    "The Navigation guidance prompt starts",
    f"The Entertainment level decreases within {RAMP}",
    f"The measured ramp-down time is within {RAMP}"],
   prio="P0", method=STATE,
   reasoning="4866494 covers the entertainment ramp-down triggered by an information "
             "source, distinct from the entertainment-to-entertainment case in 133.",
   extra_refs=["4867767"])

# ---------------------------------------------------------------- 154..169
tc("SWE1_AMM_154",
   "Confirm the Information source ramps up to its table volume on the configured channels",
   ["Play no audio source",
    "Trigger a Navigation guidance prompt",
    "Measure the ramp-up time of the Information audio",
    "Read the Information volume level and record it",
    "Record the channels the ramp is applied to"],
   ["No audio source is active",
    "The Navigation guidance prompt starts",
    f"The Information level increases within {RAMP}",
    "The Information audio reaches the volume level defined in the Information Source Handling Table",
    "The ramp is applied only to the channels listed in the \"Applied Channels\" column"],
   prio="P0", method=STATE,
   reasoning="4866512 defers both the level and the channel set to the Information Source "
             "Handling Table, so the expected result cites the table rather than a number "
             "the clause does not give.",
   extra_refs=["4867768"])

tc("SWE1_AMM_159",
   "Confirm the Information source ramps down to volume level 0 when it becomes inactive",
   ["Trigger a Navigation guidance prompt",
    "Wait until the guidance prompt ends",
    "Measure the ramp-down time and the final Information volume",
    "Measure the Information ramp-down time and read the final volume level"],
   ["The Navigation guidance prompt plays",
    "The guidance prompt ends",
    f"The Information level decreases within {RAMP}",
    "The Information audio is at volume level 0"],
   pre="No audio source is active",
   prio="P0", method=STATE,
   reasoning="4866528 states volume level 0 as the ramp-down target, which is stronger "
             "than mute and is therefore checked as a level rather than as silence.",
   extra_refs=["4867769"])

tc("SWE1_AMM_169",
   "Confirm the signal source ramps up on the channels the spec indicates",
   ["Play no audio source",
    "Trigger a signal source",
    "Record the channels the signal source ramps up on"],
   ["No audio source is active",
    "The signal source starts",
    "The signal source ramps up on the indicated channels and on no other channel"],
   prio="P1", method=STATE,
   reasoning="4866603 states the ramp-up and the channel restriction; the channel set is "
             "left as \"indicated\" because the clause points at a table rather than "
             "naming channels.")

# ---------------------------------------------------------------- 200..225
tc("SWE1_AMM_201",
   "Confirm a source starting from the idle state ramps up over the specified duration",
   ["Confirm no audio source is active",
    "Activate an Entertainment source",
    "Measure the ramp-up time",
    "Compare the measured ramp-up time against the specification and record the outcome"],
   ["No audio source is active",
    "The Entertainment source starts",
    f"The Entertainment level increases from mute within {RAMP}",
    f"The measured ramp-up time is within {RAMP}"],
   prio="P0", method=STATE,
   reasoning="4866842 covers the no-source-active entry path and points at <Tent Ramp Up> "
             "or <Tinfo Ramp Up>; the Entertainment leg is taken here and the Information "
             "leg in the second case.",
   extra_refs=["4867766"])
tc("SWE1_AMM_201",
   "Confirm the Information leg of the same idle-state entry path ramps up over its own duration",
   ["Confirm no audio source is active",
    "Trigger a Navigation guidance prompt",
    "Measure the ramp-up time",
    "Compare the measured ramp-up time against the specification and record the outcome"],
   ["No audio source is active",
    "The Navigation guidance prompt starts",
    f"The Information level increases from mute within {RAMP}",
    f"The measured ramp-up time is within {RAMP}"],
   prio="P1", method=STATE,
   reasoning="Second leg of 4866842. Split from the first because the clause binds the two "
             "legs to different parameters, 4867766 and 4867768.",
   extra_refs=["4867768"])

tc("SWE1_AMM_203",
   "Confirm a deactivating source is ramped down over the duration its own type specifies",
   ["Play an Entertainment source",
    "Deactivate the Entertainment source",
    "Measure the ramp-down time",
    "Measure the ramp-down time and record it"],
   ["Entertainment audio plays",
    "The deactivation is accepted",
    "The Entertainment level decreases gradually",
    "The measured ramp-down time is within the value the specification defines for this source type"],
   prio="P1", method=STATE, remarks=PEND_TEMP,
   reasoning="4866844 writes <Temt Ramp Down>, which the specification never defines; the "
             "only defined entertainment ramp-down is <Tent Ramp Down> at 4867767. The "
             "execution layer does not infer, so the bound is left to the PENDING and the "
             "reading is proposed as A-AM04.")

tc("SWE1_AMM_206",
   "Confirm the active Entertainment source ramps down before the incoming one is activated",
   ["Play Entertainment source A",
    "Select Entertainment source B",
    "Record the order of the source A ramp-down and the first audio of source B"],
   ["Entertainment source A plays",
    "The selection of source B is accepted",
    "Source A ramps down to mute and source B is not audible until that ramp-down has completed"],
   prio="P0", method=STATE, remarks=PEND_TEMP,
   reasoning="4866853 is the ramp-down half of the Ent to Ent axis and again writes "
             "<Temp Ramp Down>; the ordering is verifiable without the value, so the case "
             "checks ordering and leaves the duration to the PENDING.")

tc("SWE1_AMM_208",
   "Confirm the output stays muted for the whole transition delay and the new source waits for it",
   ["Play Entertainment source A",
    "Select Entertainment source B",
    "Record the state of the output channel for the Entertainment source",
    "Measure the interval between the end of source A and the first audio of source B",
    "Record the output state throughout the delay and the moment source B first produces audio"],
   ["Entertainment source A plays",
    "The selection of source B is accepted",
    "The output channel for the Entertainment source is muted",
    f"The interval covers the entertainment ramp-down, the amplifier mute "
    f"({TMUTE_AMP}) and the entertainment ramp-up ({RAMP})",
    "Source B produces no audio before the delay expires"],
   prio="P0", method=STATE, remarks=PEND_TEMP,
   reasoning="4866855 sums <Temp Ramp Down> + <Tmute AMP> + <Tent Ramp Up>. Two of the "
             "three resolve (4867773, 4867766); the first does not, so the sum carries the "
             "PENDING while the mute-throughout behaviour is still checked.",
   extra_refs=["4867766", "4867773"])

tc("SWE1_AMM_209",
   "Confirm the incoming source ramps up and starts playing once the transition delay expires",
   ["Play Entertainment source A",
    "Select Entertainment source B",
    "Wait until the transition delay expires",
    "Measure the ramp-up time of source B",
    "Measure the source B ramp-up and record when playback starts"],
   ["Entertainment source A plays",
    "The selection of source B is accepted",
    "The transition delay expires",
    f"The level of source B increases within {RAMP}",
    "Source B plays after its ramp-up has completed"],
   prio="P0", method=STATE,
   reasoning="4866856 is the ramp-up half of the Ent to Ent axis and binds to <Tent Ramp Up>, "
             "which resolves at 4867766, so this case needs no PENDING.",
   extra_refs=["4867766"])

tc("SWE1_AMM_212",
   "Confirm activation updates the mode status, sends the volume and routes audio to the amplifier",
   ["Play no audio source",
    "Activate an Entertainment source",
    "Record $HUModeStatus$ and $VolumeENT$ from the vehicle bus",
    "Read $HUModeStatus$ and record it",
    "Read $VolumeENT$ and record it",
    "Record the audio stream present at the amplifier input"],
   ["No audio source is active",
    "The Entertainment source starts",
    "$HUModeStatus$ and $VolumeENT$ are transmitted",
    "$HUModeStatus$ reports the active Entertainment source",
    "$VolumeENT$ carries the current Entertainment volume",
    "The amplifier receives the Entertainment audio stream"],
   prio="P0", method=DECISION, remarks=f"{PEND_SIG}; {PEND_VOL}",
   reasoning="4866874 requires three outcomes at once, so they are checked in one case "
             "rather than split. Neither $HUModeStatus$ nor $VolumeENT$ is in the supplied "
             "DBC, and the DBC carries no volume signal at all, so both names stay verbatim "
             "per R-13 (g) under DR-AM4.")

tc("SWE1_AMM_213",
   "Confirm a DAB traffic announcement sets the mode status to the DAB value",
   ["Tune a DAB station with traffic announcements enabled",
    "Trigger a traffic announcement",
    "Record $HUModeStatus$ from the vehicle bus",
    "Read $HUModeStatus$ and record it",
    "Record the audio stream present at the amplifier input"],
   ["The DAB station is tuned and traffic announcements are enabled",
    "The traffic announcement starts",
    "$HUModeStatus$ is transmitted",
    "$HUModeStatus$ reports \"DAB_Selected\"",
    "The amplifier receives the announcement audio"],
   prio="P1", method=DECISION, remarks=PEND_SIG,
   reasoning="4866875 maps the TA source onto three status values; the DAB row is taken "
             "here and the FM row in the second case, so each mapping is exercised without "
             "one masking the other. The label is quoted verbatim from the clause because "
             "the DBC has no entry to check it against.")
tc("SWE1_AMM_213",
   "Confirm an FM traffic announcement sets the mode status to the FM value instead",
   ["Tune an FM station with traffic announcements enabled",
    "Trigger a traffic announcement",
    "Record $HUModeStatus$ from the vehicle bus",
    "Read $HUModeStatus$ and record it"],
   ["The FM station is tuned and traffic announcements are enabled",
    "The traffic announcement starts",
    "$HUModeStatus$ is transmitted",
    "$HUModeStatus$ reports \"FM_Selected\""],
   prio="P1", method=DECISION, remarks=PEND_SIG,
   reasoning="Second row of the 4866875 mapping table.")

tc("SWE1_AMM_216",
   "Confirm the mode status returns to the off value when the Entertainment source ends",
   ["Play an Entertainment source",
    "Deactivate the Entertainment source",
    "Record $HUModeStatus$ from the vehicle bus",
    "Read $HUModeStatus$ and record it"],
   ["Entertainment audio plays",
    "The deactivation is accepted",
    "$HUModeStatus$ is transmitted",
    "$HUModeStatus$ reports \"HU_Off\""],
   prio="P1", method=STATE, remarks=PEND_SIG,
   reasoning="4866880 gives the label as \"HU_Off\"; the SWE.1 description writes HU_OFF. "
             "The clause spelling is used because R-AM2 makes CFTS019 the anchor and the "
             "DBC offers no third reading.")

tc("SWE1_AMM_223",
   "Confirm the passenger-side Entertainment restart stores the Information volume first",
   ["Play an Entertainment source",
    "Trigger a Navigation guidance prompt and allow Entertainment on the passenger-side channel",
    "End the guidance prompt",
    "Read the stored Information volume level and record it",
    "Record the Information ramp-down and the Entertainment ramp-up on the passenger and driver channels"],
   ["Entertainment audio plays",
    "The guidance prompt plays on the configured channels",
    "The guidance prompt ends",
    "The last Information source volume level is stored",
    "The Information audio ramps down and Entertainment ramps up on the passenger and driver channels"],
   prio="P1", method=SCENARIO,
   desc="When an Information or Signal source becomes inactive and Entertainment playback "
        "is permitted on the passenger-side channel, the Audio Management software shall "
        "store the last Information source volume and restore Entertainment audio",
   reasoning="The SWE.1 description runs to 53 tokens, over the R-S4 cap, so the upper half "
             "is shortened and specification_reference carries the reader back to 4866895 "
             "for the full sequence.")

tc("SWE1_AMM_224",
   "Confirm cabin settings are stored and the active Information source ramps down on all channels",
   ["Trigger a Navigation guidance prompt",
    "Trigger a Voice Recognition session while the guidance prompt is still active",
    "Read the stored cabin mode settings and record them",
    "Record the order of the Navigation ramp-down on all channels and the Voice Recognition audio start"],
   ["The Navigation guidance prompt plays",
    "The Voice Recognition session starts",
    "The cabin mode settings are stored",
    "The Navigation audio ramps down on all channels and the Voice Recognition audio starts afterwards"],
   pre="No audio source is active",
   prio="P0", method=STATE,
   desc="When an Information source is in use as the cabin audio source and another "
        "Information source becomes active, the Audio Management software shall store the "
        "current cabin settings and ramp down the active Information source",
   reasoning="The SWE.1 description runs to 56 tokens, over the R-S4 cap, so the upper half "
             "is shortened and specification_reference points at 4866898. Navigation to VR "
             "is the Info1 to Info2 pairing named on the package 03 sibling axis.")

tc("SWE1_AMM_225",
   "Confirm Entertainment is restored and the deactivated Information volume is retained",
   ["Play an Entertainment source",
    "Trigger a Navigation guidance prompt",
    "End the guidance prompt",
    "Read the stored Information volume level and record it",
    "Record the final Information volume level and the Entertainment ramp-up"],
   ["Entertainment audio plays",
    "The guidance prompt plays and the Entertainment audio is attenuated",
    "The guidance prompt ends",
    "The volume level last used by the deactivated Information source is stored",
    "The Information audio is at volume level 0 and the Entertainment audio is restored"],
   prio="P1", method=SCENARIO,
   desc="When an Information source becomes inactive and Entertainment playback is "
        "permitted on the passenger-side channel, the Audio Management software shall store "
        "the last Information source volume and restore Entertainment audio",
   reasoning="The SWE.1 description runs to 52 tokens, over the R-S4 cap. 223 and 225 are "
             "near-duplicates across two clauses; the bracket line and the expected results "
             "differ on what each clause makes observable, 223 on the channel pair and 225 "
             "on the volume level 0 target.")

# ---------------------------------------------------------------- 275..278 (BVA)
for sid, label, direction, anchor_extra in [
        ("SWE1_AMM_275", "Entertainment", "up", "4867766"),
        ("SWE1_AMM_276", "Entertainment", "down", "4867767"),
        ("SWE1_AMM_277", "Information", "up", "4867768"),
        ("SWE1_AMM_278", "Information", "down", "4867769")]:
    pre = ("No audio source is active" if sid in ("SWE1_AMM_275", "SWE1_AMM_277")
           else "An Entertainment source is active" if sid == "SWE1_AMM_276"
           else "An Information source is active")
    trigger = ("Activate an Entertainment source" if sid == "SWE1_AMM_275" else
               "Switch from one Entertainment source to another" if sid == "SWE1_AMM_276" else
               "Trigger a Navigation guidance prompt" if sid == "SWE1_AMM_277" else
               "Trigger a second Information source while the first is active")
    tc(sid,
       f"Confirm the {label.lower()} ramp-{direction} does not complete before the lower bound",
       [trigger,
        f"Measure the {label.lower()} ramp-{direction} duration",
        "Compare the measured duration against the lower bound and record the outcome"],
       [f"The {label} source ramp-{direction} starts",
        f"The ramp-{direction} duration is measured",
        "The measured duration is 25 ms or longer"],
       prio="P1", method=BVA, pre=pre,
       reasoning=f"Lower bound of the {RAMP} window at CFTS019-{anchor_extra}. Package 03 "
                 f"marks 275 to 278 as the boundary value candidates, so each leaf is split "
                 f"into a minimum case and a maximum case.")
    tc(sid,
       f"Confirm the {label.lower()} ramp-{direction} completes within the upper bound",
       [trigger,
        f"Measure the {label.lower()} ramp-{direction} duration",
        "Compare the measured duration against the upper bound and record the outcome"],
       [f"The {label} source ramp-{direction} starts",
        f"The ramp-{direction} duration is measured",
        "The measured duration is 50 ms or shorter"],
       prio="P1", method=BVA, pre=pre,
       reasoning=f"Upper bound of the same window at CFTS019-{anchor_extra}.")

# ---------------------------------------------------------------- Audio Arbitration
tc("SWE1_AMM_123",
   "Confirm only the highest priority signal source stays active when several are requested",
   ["Trigger a signal source with priority S2",
    "Trigger a signal source with priority S1 while S2 is still active",
    "Record which signal source is active"],
   ["The S2 signal source is active",
    "The S1 signal source is requested",
    "The S1 signal source is active and the S2 signal source is not active"],
   pre="No signal source is active",
   prio="P0", method=DECISION,
   reasoning="4866451 defines priority by lower numeric value, so S1 over S2 is the "
             "smallest pair that exercises the rule.")

tc("SWE1_AMM_124",
   "Confirm a higher priority source interrupts and overrides an active lower priority source",
   ["Play an Entertainment source",
    "Trigger a higher priority audio source",
    "Record which source is active after the request"],
   ["Entertainment audio plays",
    "The higher priority source is requested",
    "The higher priority source is active and the Entertainment source is overridden"],
   prio="P0", method=DECISION,
   reasoning="4866452 is the general pre-emption rule that the rest of the arbitration set "
             "specialises.")

tc("SWE1_AMM_129",
   "Confirm an Entertainment request waits until the active confirmation tone has finished",
   ["Trigger a confirmation tone",
    "Request an Entertainment source while the tone is still playing",
    "Record the order of the confirmation tone end and the Entertainment source start"],
   ["The confirmation tone plays",
    "The Entertainment request is accepted and held",
    "The Entertainment source starts after the confirmation tone has completed"],
   pre="No audio source is active",
   prio="P1", method=STATE,
   reasoning="4866457 delays entertainment and information alerts behind a signal source or "
             "a confirmation tone; the tone is the shorter of the two and makes the delay "
             "observable without a second arbitration.")

tc("SWE1_AMM_130",
   "Confirm an insufficient priority request is queued until the active source releases",
   ["Trigger a high priority audio source",
    "Request a lower priority audio source",
    "Record the audio produced for the lower priority request",
    "End the high priority source",
    "Record when the queued request plays"],
   ["The high priority source is active",
    "The lower priority request is accepted",
    "The lower priority request produces no audio",
    "The high priority source ends",
    "The queued request plays"],
   pre="No audio source is active",
   prio="P0", method=STATE,
   reasoning="4866465 and 4866488 carry the same clause text at two anchors. This case "
             "takes the queue-until-eligible reading; SWE1_AMM_139 takes the re-evaluation "
             "reading, so the pair is distinguishable in the workbook as package 03 requires.")

tc("SWE1_AMM_139",
   "Confirm queued requests are re-evaluated in priority order as sources become inactive",
   ["Trigger a high priority audio source",
    "Request two lower priority sources with different priorities",
    "End the high priority source",
    "Record the order in which the queued requests play",
    "Record when the remaining queued request plays"],
   ["The high priority source is active",
    "Both lower priority requests are accepted and produce no audio",
    "The high priority source ends",
    "The higher priority queued request plays",
    "The remaining queued request plays after the previous one ends"],
   pre="No audio source is active",
   prio="P0", method=STATE,
   reasoning="Same clause text as 4866465 at a second anchor. Two queued requests are used "
             "so the ordering, and not merely the release, is what the case observes.")

tc("SWE1_AMM_166",
   "Confirm the next highest priority source is activated when the current one ends",
   ["Trigger a high priority audio source and a lower priority audio source",
    "End the high priority source",
    "Record which source is active after the high priority source ends"],
   ["Both sources are requested and the high priority source is active",
    "The high priority source ends",
    "The next highest priority source is active"],
   pre="No audio source is active",
   prio="P1", method=STATE,
   reasoning="4866538 states the activation half of the activate/re-mix clause; the re-mix "
             "half is covered by SWE1_AMM_167 at its own anchor.")

tc("SWE1_AMM_167",
   "Confirm the remaining sources are re-mixed after the highest priority source is removed",
   ["Trigger two audio sources that are allowed to play together",
    "End the higher priority source",
    "Record the channels the remaining sources are mixed onto"],
   ["Both sources play together",
    "The higher priority source ends",
    "The remaining sources are re-mixed on the configured channels"],
   pre="No audio source is active",
   prio="P1", method=STATE,
   reasoning="4866590 repeats the activate/re-mix clause at the mixing anchor, so this case "
             "keeps two sources concurrent to make the re-mix, rather than an activation, "
             "the observable outcome.")

tc("SWE1_AMM_189",
   "Confirm sources below the mute request in priority are muted and higher ones are not",
   ["Play an Entertainment source and a higher priority audio source",
    "Trigger the TBM mute",
    "Record the playback state of the sources below the TBM mute in priority",
    "Record the playback state of the sources above the TBM mute in priority"],
   ["Both sources play",
    "The TBM mute is active",
    "The sources below the TBM mute in priority are muted or paused",
    "The sources above the TBM mute in priority keep playing"],
   prio="P0", method=DECISION,
   reasoning="4866715 only states the muting of lower priority sources; the case adds the "
             "higher priority observation so that a blanket mute would fail rather than pass.")

tc("SWE1_AMM_198",
   "Confirm a manual emergency call mutes the sources below the mute request in priority",
   ["Play an Entertainment source",
    "Set $TBM_FD_1.SOSCallType$ = 2 (Manual_SOS_call)",
    "Record the mute state of the audio sources below \"TBM Mute Request\" in priority"],
   ["Entertainment audio plays",
    "$TBM_FD_1.SOSCallType$ reports 2 (Manual_SOS_call)",
    "The audio sources below \"TBM Mute Request\" in priority are muted"],
   prio="P0", method=DECISION,
   reasoning="4866726 names $SOSCallType$, which the supplied DBC does carry, in TBM_FD_1 "
             "with a VAL_ table whose labels match the clause verbatim, so the signal is "
             "written in full with its raw value and label per IN 8.7.5 v3. 198 and 218 are "
             "the near-duplicate pair package 03 flags; this one takes the manual call.")

tc("SWE1_AMM_199",
   "Confirm the muted sources are unmuted once no emergency call is active",
   ["Set $TBM_FD_1.SOSCallType$ = 2 (Manual_SOS_call) while an Entertainment source plays",
    "Set $TBM_FD_1.SOSCallType$ = 1 (No_active_SOS_call)",
    "Record the mute state of the audio sources below \"TBM Mute Request\" in priority"],
   ["The audio sources below \"TBM Mute Request\" in priority are muted",
    "$TBM_FD_1.SOSCallType$ reports 1 (No_active_SOS_call)",
    "The audio sources below \"TBM Mute Request\" in priority are unmuted"],
   pre="An Entertainment source is active and $TBM_FD_1.SOSCallType$ = 1 (No_active_SOS_call)",
   prio="P0", method=DECISION,
   reasoning="4866727 is the ELSE branch of 4866726. The restore is written against the "
             "No_active_SOS_call value rather than against call termination, because the "
             "clause keys on the signal.")

tc("SWE1_AMM_211",
   "Confirm activation from the idle state follows the routing tables",
   ["Confirm no audio source is active",
    "Activate an audio source",
    "Record the routing the activation produces"],
   ["No audio source is active",
    "The audio source becomes active",
    "The routing matches the configured routing table"],
   prio="P1", method=DECISION,
   reasoning="4866873 states two activation scenarios. This case takes the no-source-active "
             "scenario; SWE1_AMM_215 at its own anchor takes the coexistence scenario.")

tc("SWE1_AMM_215",
   "Confirm activation alongside an existing source follows the routing tables",
   ["Play an audio source",
    "Activate a second audio source that is allowed to play together with the first",
    "Record which sources are audible"],
   ["The first audio source plays",
    "The second audio source becomes active",
    "Both sources play together as the routing table configures"],
   prio="P1", method=DECISION,
   reasoning="4866879 restates the scenarios as A and B. The coexistence scenario is taken "
             "here so this case is not a duplicate of SWE1_AMM_211.")

tc("SWE1_AMM_218",
   "Confirm an automatic emergency call mutes the sources below the mute request in priority",
   ["Play an Entertainment source",
    "Set $TBM_FD_1.SOSCallType$ = 3 (Automatic_SOS_call)",
    "Record the mute state of the audio sources below \"TBM Mute Request\" in priority"],
   ["Entertainment audio plays",
    "$TBM_FD_1.SOSCallType$ reports 3 (Automatic_SOS_call)",
    "The audio sources below \"TBM Mute Request\" in priority are muted"],
   prio="P0", method=DECISION,
   reasoning="4866885 carries the same clause text as 4866726 at a second anchor. The "
             "automatic call value is used here so the pair covers two of the three call "
             "types instead of repeating one.")

tc("SWE1_AMM_219",
   "Confirm the unmute also follows a callback emergency call ending",
   ["Set $TBM_FD_1.SOSCallType$ = 4 (Callback_SOS_call) while an Entertainment source plays",
    "Set $TBM_FD_1.SOSCallType$ = 1 (No_active_SOS_call)",
    "Record the mute state of the audio sources below \"TBM Mute Request\" in priority"],
   ["The audio sources below \"TBM Mute Request\" in priority are muted",
    "$TBM_FD_1.SOSCallType$ reports 1 (No_active_SOS_call)",
    "The audio sources below \"TBM Mute Request\" in priority are unmuted"],
   pre="An Entertainment source is active and $TBM_FD_1.SOSCallType$ = 1 (No_active_SOS_call)",
   prio="P0", method=DECISION,
   reasoning="4866886 is the ELSE branch at the second anchor. The callback call type is "
             "used so the pair 199 and 219 covers the third call type as well.")

tc("SWE1_AMM_226",
   "Confirm a voice recognition request cancels active navigation audio",
   ["Trigger a Navigation guidance prompt",
    "Press the Voice Recognition button while the guidance prompt is playing",
    "Record the state of the Navigation audio",
    "Record the state of the Voice Recognition audio"],
   ["The Navigation guidance prompt plays",
    "The Voice Recognition request is accepted",
    "The Navigation audio is cancelled",
    "The Voice Recognition audio is active"],
   pre="No audio source is active",
   prio="P0", method=SCENARIO,
   reasoning="4866902 covers TA or NAV against Phone or VR. The NAV against VR pairing is "
             "taken here; the TA against call pairing is SWE1_AMM_227 at its own anchor, so "
             "the two cases do not overlap.")

tc("SWE1_AMM_227",
   "Confirm accepting an incoming call cancels an active traffic announcement",
   ["Trigger a traffic announcement",
    "Receive an incoming call and accept it",
    "Record the state of the traffic announcement audio",
    "Record the state of the hands-free call audio"],
   ["The traffic announcement plays",
    "The incoming call is accepted",
    "The traffic announcement audio is cancelled",
    "The hands-free call audio is active"],
   pre="No audio source is active and no call is in progress",
   prio="P0", method=SCENARIO,
   reasoning="4866903 is the accepted-call case, distinct from 4866902 which keys on the "
             "Phone or VR button press.")


# ------------------------------------------------- R-AM2' out-of-pool anchors
# Pei ruled 2026-08-26 ("2採 R-AM2'准 DR-AM3發"): these seven anchors sit
# outside the two Basic Reports but are State:Approved objects in the CFTS019
# full text, verified on both routes. They are written as given; every
# reasoning field says so, and the submission package carries the register
# gen_b1.py emits alongside the batch.
#
# All seven are "Refer to figure" objects. The behavioural sequence therefore
# comes from the figure caption text plus the SWE.1 Description; timing values
# are still never invented (IN 8.4.1) — they are cited only where a named
# parameter resolves in 1.5.4 Variables.

tc("SWE1_AMM_138",
   "Confirm the Entertainment source change follows the ramp-down, mute hold and ramp-up order",
   ["Play Entertainment source A",
    "Select Entertainment source B",
    "Record the order of the ramp-down, the mute hold and the ramp-up",
    "Compare the observed phase order against the transition figure and record the outcome"],
   ["Entertainment source A plays",
    "The selection of source B is accepted",
    "The ramp-down, the mute hold and the ramp-up are observed",
    "The three phases occur in the order the transition figure gives"],
   prio="P0", method=STATE,
   reasoning="Out-of-pool anchor, corroborated by the full text (R-AM2'): 4866479 is "
             "State:Approved in CFTS019 but absent from both Basic Reports under A-AM03. "
             "The object is the \"Entertainment Active -> Entertainment Active\" figure, so "
             "the case checks phase ordering, which the caption states, rather than the "
             "durations, which only the figure body carries.",
   extra_refs=["4867766", "4867767", "4867773"])

tc("SWE1_AMM_156",
   "Confirm an Information source activating over Entertainment follows the figure sequence",
   ["Play an Entertainment source",
    "Trigger a Navigation guidance prompt",
    "Record the order of the Entertainment ramp-down and the Information ramp-up",
    "Compare the observed sequence against the Entertainment to Information transition figure and record the outcome"],
   ["Entertainment audio plays",
    "The Navigation guidance prompt starts",
    "The Entertainment ramp-down and the Information ramp-up are observed",
    "The sequence matches the Entertainment to Information transition figure"],
   prio="P0", method=STATE,
   reasoning="Out-of-pool anchor, corroborated by the full text (R-AM2'): 4866520 is the "
             "\"Entertainment Active -> Information Active\" figure. This is the Ent to Info "
             "sibling axis; SWE1_AMM_224 covers the same axis from the cabin-settings angle, "
             "so the bracket lines differ on what each observes.",
   extra_refs=["4867767", "4867768"])

tc("SWE1_AMM_157",
   "Confirm a second Information source activating over the first follows the figure sequence",
   ["Trigger a Navigation guidance prompt",
    "Trigger a Voice Recognition session while the guidance prompt is active",
    "Record the order of the Information 1 ramp-down and the Information 2 ramp-up",
    "Compare the observed sequence against the Information 1 to Information 2 transition figure and record the outcome"],
   ["The Navigation guidance prompt plays",
    "The Voice Recognition session starts",
    "The Information 1 ramp-down and the Information 2 ramp-up are observed",
    "The sequence matches the Information 1 to Information 2 transition figure"],
   pre="No audio source is active",
   prio="P0", method=STATE,
   reasoning="Out-of-pool anchor, corroborated by the full text (R-AM2'): 4866522 is the "
             "\"Information 1 Active -> Information 2 Active\" figure. Paired with "
             "SWE1_AMM_241 on the Info1 to Info2 axis; 157 takes the non-arbitrated "
             "ordering and 241 the arbitrated one.",
   extra_refs=["4867768", "4867769"])

tc("SWE1_AMM_200",
   "Confirm a source starting with nothing active follows the non-arbitrated sequence",
   ["Confirm no audio source is active",
    "Activate an Entertainment source",
    "Record the transition sequence",
    "Compare the observed sequence against the non-arbitrated source transition diagram and record the outcome"],
   ["No audio source is active",
    "The Entertainment source starts",
    "The transition sequence is observed",
    "The sequence matches the non-arbitrated source transition diagram with no arbitration step"],
   prio="P1", method=STATE,
   reasoning="Out-of-pool anchor, corroborated by the full text (R-AM2'): 4866839 is the "
             "no-source-active diagram. The absence of an arbitration step is the "
             "distinguishing observation against the arbitrated diagrams at 4866956 and "
             "4866967, so the expected result states it explicitly.")

tc("SWE1_AMM_205",
   "Confirm an Entertainment source replacing another follows the non-arbitrated sequence",
   ["Play Entertainment source A",
    "Activate Entertainment source B",
    "Record the transition sequence",
    "Compare the observed sequence against the non-arbitrated Entertainment to Entertainment diagram and record the outcome"],
   ["Entertainment source A plays",
    "Entertainment source B is activated",
    "The transition sequence is observed",
    "The sequence matches the non-arbitrated Entertainment to Entertainment diagram"],
   prio="P0", method=STATE,
   reasoning="Out-of-pool anchor, corroborated by the full text (R-AM2'): 4866850 heads the "
             "Ent to Ent axis whose steps 206, 208, 209 and 212 carry in-pool anchors. This "
             "case checks the sequence as a whole, which is what the diagram adds over the "
             "individual step clauses.")

tc("SWE1_AMM_240",
   "Confirm a chime request over an active source follows the arbitrated sequence",
   ["Play an Entertainment source",
    "Trigger a signal chime request",
    "Record the arbitration and routing behaviour",
    "Compare the observed sequence against the arbitrated source transition diagram and record the outcome"],
   ["Entertainment audio plays",
    "The signal chime request is raised",
    "The arbitration and the routing are observed",
    "The sequence matches the arbitrated source transition diagram"],
   prio="P0", method=STATE,
   reasoning="Out-of-pool anchor, corroborated by the full text (R-AM2'): 4866956 is the "
             "arbitrated diagram for a chime over entertainment or information. Distinct "
             "from 4866839 in that arbitration runs, which is the observation the case "
             "turns on.")

tc("SWE1_AMM_241",
   "Confirm a higher priority Information source arbitrates against the active one",
   ["Trigger a Navigation guidance prompt",
    "Trigger a higher priority Information source",
    "Record the arbitration and routing behaviour",
    "Compare the observed sequence against the arbitrated Information source transition diagram and record the outcome"],
   ["The Navigation guidance prompt plays",
    "The higher priority Information source is raised",
    "The arbitration and the routing are observed",
    "The sequence matches the arbitrated Information source transition diagram"],
   pre="No audio source is active",
   prio="P0", method=STATE,
   reasoning="Out-of-pool anchor, corroborated by the full text (R-AM2'): 4866967 is the "
             "arbitrated Info to Info diagram. Pairs with SWE1_AMM_157 on the same sibling "
             "axis, 157 non-arbitrated and 241 arbitrated, so the two bracket lines stay "
             "distinguishable.")


def main() -> None:
    ctx = {l["swe_id"]: l for l in json.loads(
        (ROOT / "batches" / "B1_context.json").read_text(encoding="utf-8"))}
    out_of_pool = sorted(k for k, v in ctx.items() if not v["anchor_in_pool"])
    missing = sorted(k for k in ctx if k not in AUTHORED)
    if missing:
        sys.exit(f"leaves with no authored TC: {missing}")

    tcs = []
    for swe_id, entries in AUTHORED.items():
        leaf = ctx[swe_id]
        for e in entries:
            if len(e["proc"]) != len(e["er"]):
                sys.exit(f"{swe_id}: {len(e['proc'])} steps vs {len(e['er'])} results")
            # R-S4 wants the upper half verbatim, while the workbook bans a
            # trailing period. Only that final period is removed — nothing else
            # in the sentence is touched — matching the time_management corpus,
            # where none of the 19 B1 upper halves ends in a period.
            desc = (e["desc"] or leaf["swe"]["description"]).rstrip().rstrip(".")
            refs = [leaf["anchor"], *e["extra_refs"]]
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
                "spec_reference": "\n".join(f"CFTS019-{r}" for r in refs),
                "priority": e["prio"],
                "design_method": e["method"],
                "remarks": e["remarks"],
                "reasoning": e["reasoning"],
            })

    out = {"batch": "B1", "feature": "Audio Management",
           "test_group": "Audio Management", "n_tcs": len(tcs),
           "leaves_authored": len(AUTHORED),
           # R-AM2' requires the submission package to carry this register.
           "out_of_pool_anchors": [
               {"swe_id": k, "anchor": f"CFTS019-{ctx[k]['anchor']}",
                "title": ctx[k]["title"], "test_set": ctx[k]["test_set"],
                "basis": "State:Approved in the CFTS019 full text; absent from "
                         "both Basic Reports (A-AM03 / DR-AM3)"}
               for k in out_of_pool],
           "tcs": tcs}
    dest = ROOT / "generated" / "B1.json"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2),
                    encoding="utf-8")
    print(f"wrote {dest.relative_to(ROOT.parent.parent)}")
    print(f"  leaves authored  {len(AUTHORED)}")
    print(f"  TCs              {len(tcs)}")
    print(f"  out-of-pool anchors carried per R-AM2'  {len(out_of_pool)}")


if __name__ == "__main__":
    main()
