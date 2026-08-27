#!/usr/bin/env python3
"""Emit the B5 test cases for audio_mgmt.

Anchors from package 18 as ruled by package 20. 293 is absent: package 20
section 2.3 authorised writing it only on an in-pool anchor, and gate 4
found 4866193, which is out of pool, so it returns as a single item.

Four shared-anchor groups this batch (R-AM16), each with distinct bracket
halves: 021/023 on 4865986, 022/281 on 4865984, 043/048 on 4866090, and
292/294 on 4866173. 283/285 share 4867695 and 107 shares 4866286 with B4's
020 across batches, which R-AM21 now checks.

Usage:
    python features/audio_mgmt/scripts/gen_b5.py
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

# Every signal B5 touches is absent from the supplied DBC, rechecked without
# case sensitivity per package 12 section 4.8.
PEND_SIG = ("PENDING: DR-AM4 signal not found in the supplied DBC; name kept "
            "as written in CFTS019 per R-13 (g)")
TABLE_NOTE = ("table object; the case verifies the mapping is applied, not "
              "the table's contents (IN 4.3.1 R-3)")

AUTHORED: dict[str, list[dict]] = {}


def tc(swe_id, purpose, proc, er, *, prio="P1", method=FUNC, pre="NA",
       data="NA", remarks="", reasoning="", desc=None):
    AUTHORED.setdefault(swe_id, []).append(dict(
        purpose=purpose, proc=proc, er=er, prio=prio, method=method, pre=pre,
        data=data, remarks=remarks, reasoning=reasoning, desc=desc))


# --------------------------------------------------------- VR and conf tones
tc("SWE1_AMM_011",
   "Confirm the navigation voice session plays its start and end tones",
   ["Start a Navigation voice recognition session",
    "Record the tone played at the start of the session",
    "End the session",
    "Record the tone played at the end"],
   ["The Navigation voice session starts",
    "The configured start tone plays",
    "The session ends",
    "The configured end tone plays"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="4865939 covers the tones NAV and HFP use to bracket a voice "
             "session. Both ends are read because a start tone alone leaves "
             "the user without the cue that the session closed.")

tc("SWE1_AMM_012",
   "Confirm the hands-free voice session reuses the same tone resources",
   ["Start a Navigation voice recognition session and record the start tone",
    "Start a hands-free voice recognition session",
    "Record the start tone and compare it against the one recorded"],
   ["The Navigation voice session start tone plays",
    "The hands-free voice session starts",
    "The same start tone plays for both sessions"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="4865940 requires NAV and HFP to draw on one set of files. The "
             "only way to observe sameness is to hear both and compare, so "
             "the case runs the two sessions rather than one.")

tc("SWE1_AMM_016",
   "Confirm confirmation tones are suppressed while the setting is off",
   ["Set the confirmation tone setting to off",
    "Press a touchscreen control",
    "Record the audio produced"],
   ["The confirmation tone setting is off",
    "The touchscreen press is accepted",
    "No confirmation tone is produced"],
   prio="P1", method=NEGATIVE, pre="No audio source is active",
   reasoning="4865970 makes generation conditional on the customer setting. "
             "Written as a negative because the failure that matters is a tone "
             "sounding when the user turned it off.")
tc("SWE1_AMM_016",
   "Confirm the tones return when the setting is switched back on",
   ["Set the confirmation tone setting to on",
    "Press a touchscreen control",
    "Record the audio produced"],
   ["The confirmation tone setting is on",
    "The touchscreen press is accepted",
    "The confirmation tone is produced"],
   prio="P1", method=DECISION, pre="No audio source is active",
   reasoning="The positive branch of the same condition at 4865970: a system "
             "that never generated tones would pass the negative case alone.")

tc("SWE1_AMM_017",
   "Confirm the three key press tones are distinguished by event",
   ["Press a control whose function is permitted",
    "Record the tone produced",
    "Press a control whose function is not permitted",
    "Record the tone produced"],
   ["The permitted press is accepted",
    "The acceptance tone plays",
    "The rejected press is registered",
    "The rejection tone plays and differs from the acceptance tone"],
   prio="P1", method=DECISION, pre="No audio source is active",
   reasoning="4865971 names Conf1, Conf2 and Conf3. The classification only "
             "means something if the tones differ, so the case hears two of "
             "them against each other rather than checking one exists.")

tc("SWE1_AMM_018",
   "Confirm the requested chime type drives the tone parameters used",
   ["Request a confirmation tone of a given chime type",
    "Record the tone parameters applied"],
   ["The chime request is accepted",
    "The tone parameters applied are those the table associates with the requested chime type"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning=f"4866568 defers the parameters to the Chime Type table, a "
             f"{TABLE_NOTE}.")

tc("SWE1_AMM_019",
   "Confirm the set tone plays as pulse A then pulse B in order",
   ["Request a Conf3 set tone",
    "Record the sequence of pulses produced"],
   ["The Conf3 request is accepted",
    "Pulse A plays and pulse B follows it"],
   prio="P1", method=STATE, pre="No audio source is active",
   reasoning="4865974 gives Conf3 an internal structure the other two tones "
             "lack, so the ordering of the two pulses is what the case "
             "observes rather than the tone's presence.")

for sid, emphasis, tail in (
        ("SWE1_AMM_021", "the parameters follow the received event type",
         "This row observes the lookup keyed on the incoming alert event"),
        ("SWE1_AMM_023", "the parameters follow the selected alert type",
         "This row observes the lookup keyed on the alert type already "
         "selected, one step further along the same path")):
    tc(sid,
       f"Confirm {emphasis}",
       ["Enable the entertainment and information alert feature",
        "Raise an alert event",
        "Record the tone parameters applied"],
       ["The alert feature is enabled",
        "The alert event is raised",
        "The tone parameters applied are those the alert-tone configuration associates with that alert"],
       prio="P1", method=FUNC, pre="No audio source is active",
       reasoning=f"021 and 023 share 4865986 under R-AM16 — package 20 section "
                 f"1 re-anchored 021 there after route 2 found the ObjectID "
                 f"written in the leaf's own description, which the first "
                 f"route had not scanned for. {tail}, so the brackets differ "
                 f"as that ruling requires. 4865986 is the waveform parameter "
                 f"table, a {TABLE_NOTE}. Out-of-pool anchor, single-source "
                 f"under R-AM18.")

for sid, emphasis, tail in (
        ("SWE1_AMM_022", "each alert event resolves to its own alert identifier",
         "This row observes the event-to-identifier mapping across the "
         "Information alert types"),
        ("SWE1_AMM_281", "the reserved identifiers are held back from assignment",
         "This row observes the reservation of Alert6 to Alert8 for MIM, "
         "which the mapping alone does not establish")):
    tc(sid,
       f"Confirm {emphasis}",
       ["Raise a sports alert event",
        "Record the alert identifier used",
        "Raise a traffic alert event",
        "Record the alert identifier used"],
       ["The sports alert event is raised",
        "The identifier used is the one configured for the sports alert",
        "The traffic alert event is raised",
        "The identifier used is the one configured for the traffic alert and differs from the first"],
       prio="P1", method=DECISION, pre="No audio source is active",
       desc=("The Audio Management software shall map supported Information "
             "alert events to their configured alert types"
             if sid == "SWE1_AMM_022" else
             "The Audio Management software shall map each supported alert "
             "event to its corresponding system-generated alert definition "
             "and generate the alert using the configured parameters"),
       reasoning=f"022 and 281 share 4865984 under R-AM16. {tail}. 023 takes "
                 f"the other half of the chain at 4865986: identifier to "
                 f"parameters, where these two are event to identifier.")

tc("SWE1_AMM_025",
   "Confirm a fade or balance change is transmitted to the amplifier",
   ["Adjust the fade control",
    "Read $ToneFADE$ and record it",
    "Adjust the balance control",
    "Read $ToneBAL$ and record it"],
   ["The fade adjustment is accepted",
    "$ToneFADE$ reports the fade setting",
    "The balance adjustment is accepted",
    "$ToneBAL$ reports the balance setting"],
   prio="P1", method=FUNC, remarks=PEND_SIG,
   reasoning="Partial coverage, ruled at package 20 section 2.4. 4866311 "
             "carries fade and balance only; the EQ and tone side of the leaf "
             "is at 4866090, which 043 and 048 hold, and the ruling assigns it "
             "to them rather than making a third leaf share it. This case "
             "therefore writes fade and balance and nothing about tone "
             "controls.")

tc("SWE1_AMM_029",
   "Confirm the base configuration behaviour is enabled for a base system type",
   ["Configure the vehicle so that $AudioSystemType$ is \"Base\"",
    "Start the head unit",
    "Record which audio-system behaviour is enabled"],
   ["$AudioSystemType$ reports \"Base\"",
    "The head unit starts",
    "The behaviour allocated to Base and Fiat Booster configurations is enabled"],
   prio="P1", method=DECISION, remarks=PEND_SIG,
   reasoning="4866042 scopes a block of requirements to the Base and Fiat "
             "Booster types. The leaf is the SWE.1 rendering of that scoping "
             "decision, so the case observes which behaviour set the type "
             "selects rather than any one requirement inside the block.")

tc("SWE1_AMM_033",
   "Confirm a touchscreen press raises a confirmation tone request",
   ["Press an active area of the touchscreen",
    "Record the audio produced"],
   ["The touchscreen press is accepted",
    "A confirmation tone is produced"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="4866057 ties the tone to touchscreen feedback and excludes dead "
             "areas, so the case presses an active area; the dead-area "
             "exclusion is a display concern the clause states but does not "
             "make observable in audio.")

tc("SWE1_AMM_034",
   "Confirm each of the three tone types is available and distinct",
   ["Trigger an acceptance tone and record it",
    "Trigger a rejection tone and record it",
    "Trigger a set tone",
    "Compare the three recorded tones and record the outcome"],
   ["The acceptance tone plays",
    "The rejection tone plays and differs from the acceptance tone",
    "The set tone plays",
    "The three tones differ from one another"],
   prio="P1", method=DECISION, pre="No audio source is active",
   reasoning="4866058 enumerates the three types. All three are exercised in "
             "one case because what the clause asserts is the set, and a "
             "missing third member is only visible against the other two.")

tc("SWE1_AMM_035",
   "Confirm tone processing is available whenever the touchscreen is active",
   ["Enable the confirmation tone feature",
    "Bring the touchscreen to the active state",
    "Press a control",
    "Record the audio produced"],
   ["The confirmation tone feature is enabled",
    "The touchscreen is active",
    "The press is accepted",
    "A confirmation tone is produced"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="4866059 conditions availability on the touchscreen being active, "
             "which is a different gate from the customer setting at 4865970 "
             "that leaf 016 covers.")

tc("SWE1_AMM_036",
   "Confirm a second tone is not raised for the same press",
   ["Press a control once",
    "Record the number of confirmation tones produced"],
   ["The press is accepted",
    "Exactly one confirmation tone is produced"],
   prio="P1", method=NEGATIVE, pre="No audio source is active",
   reasoning="4866060 bars a repeat tone for the current press. Counting is "
             "the observation, since the defect is an extra tone rather than a "
             "missing one.")

for sid, anchor, kind, cond in (
        ("SWE1_AMM_037", "4866061", "acceptance",
         "a short press whose function is permitted"),
        ("SWE1_AMM_038", "4866062", "rejection",
         "a short press whose function is not permitted"),
        ("SWE1_AMM_039", "4866063", "set",
         "a press whose function completes a setting")):
    tc(sid,
       f"Confirm the {kind} tone is chosen for {cond}",
       [f"Perform {cond}",
        "Record the confirmation tone produced"],
       ["The press is registered",
        f"The {kind} tone plays"],
       prio="P1", method=DECISION, pre="No audio source is active",
       reasoning=f"{anchor} is one row of the three-way selection package 18 "
                 f"marks as a section 7 enumeration: the three ship together "
                 f"because each names a different press outcome, and testing "
                 f"one says nothing about the routing of the others.")

tc("SWE1_AMM_040",
   "Confirm an enabled alert event produces its configured alert",
   ["Enable the entertainment and information alert feature",
    "Raise an enabled alert event",
    "Record the alert produced"],
   ["The alert feature is enabled",
    "The alert event is raised",
    "The alert configured for that event type is produced"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="Re-anchored to 4865982 at package 20 section 1: the clause reads "
             "for each enabled event type, matching this leaf, where package "
             "18 had it against 021. This row is the generation step; 021 and "
             "023 at 4865986 are the parameters that generation uses.")

# ------------------------------------------------------------ tone controls
tc("SWE1_AMM_041",
   "Confirm tone controls act on Entertainment audio",
   ["Play an Entertainment source",
    "Adjust the bass control",
    "Record the effect on the Entertainment audio"],
   ["Entertainment audio plays",
    "The bass adjustment is accepted",
    "The Entertainment audio reflects the bass adjustment"],
   prio="P1", method=FUNC,
   reasoning="4866079 restricts tone controls to Entertainment. The positive "
             "half is here; 042 at 4866080 carries the other half, which is "
             "what the restriction actually protects.")

tc("SWE1_AMM_042",
   "Confirm Information and Signal sources stay at the neutral tone setting",
   ["Adjust the bass control while an Entertainment source plays",
    "Trigger a Navigation guidance prompt",
    "Record the tone setting applied to the Information audio"],
   ["The bass adjustment is accepted",
    "The Navigation guidance prompt starts",
    "The Information audio carries the neutral tone setting"],
   prio="P1", method=NEGATIVE,
   reasoning="4866080 is the complement of 4866079: the user's tone settings "
             "must not follow onto information or signal audio. A system that "
             "applied them globally would pass 041 and fail here, which is why "
             "the case adjusts first and then triggers the Information source.")

for sid, emphasis, tail in (
        ("SWE1_AMM_043", "a tone adjustment is converted and sent",
         "This row observes the conversion — the user's level arriving as the "
         "signal value"),
        ("SWE1_AMM_048", "the amplifier receives the tone setup signals",
         "This row observes the transmission reaching the amplifier, which the "
         "conversion alone does not establish")):
    tc(sid,
       f"Confirm {emphasis}",
       ["Adjust the bass control to a known level",
        "Read $ToneBASS$ and record it",
        "Adjust the treble control to a known level",
        "Read $ToneTREB$ and record it"],
       ["The bass adjustment is accepted",
        "$ToneBASS$ reports the selected bass level",
        "The treble adjustment is accepted",
        "$ToneTREB$ reports the selected treble level"],
       prio="P1", method=FUNC, remarks=PEND_SIG,
       reasoning=f"043 and 048 share 4866090 under R-AM16. {tail}, so the "
                 f"brackets differ as that ruling requires. Package 20 section "
                 f"2.4 keeps 025 out of this sharing: its EQ side is ceded to "
                 f"these two rather than making a third leaf cite the same "
                 f"object.")

tc("SWE1_AMM_045",
   "Confirm the tone range spans nine steps either side of neutral",
   ["Adjust the bass control to its lowest level and read $ToneBASS$",
    "Adjust the bass control to its highest level and read $ToneBASS$",
    "Read the distinct levels between them and record the count"],
   ["$ToneBASS$ reports the lowest level",
    "$ToneBASS$ reports the highest level",
    "The distinct levels number 19, being nine below neutral, neutral, and nine above"],
   desc=("The Audio Management software shall support 19 valid adjustment levels for $SUB_LVLSts$, $ToneBASS$, $ToneMID$, and $ToneTREB$"),
   prio="P1", method=BVA, remarks=PEND_SIG,
   reasoning="4866083 fixes the range at 19 levels. Both ends and the count "
             "are read because an off-by-one at either limit is exactly what a "
             "range requirement guards against.")

tc("SWE1_AMM_046",
   "Confirm tone adjustment is offered in the full operation state",
   ["Set TLM_Status.Info to \"Full-Operation\"",
    "Open the audio settings",
    "Record whether the tone controls accept adjustment"],
   ["TLM_Status.Info reports \"Full-Operation\"",
    "The audio settings open",
    "The tone controls accept adjustment"],
   prio="P1", method=DECISION, pre="No audio source is active",
   reasoning="4866087 gates adjustment on the telematics state, the same shape "
             "as the volume gate B3 covered at 4866126. TLM_Status.Info is an "
             "internal signal name kept without a dollar wrapper per v3 (d).")

tc("SWE1_AMM_047",
   "Confirm a bass, mid or treble request is processed to the audio path",
   ["Play an Entertainment source",
    "Adjust the mid control to a known level",
    "Record the effect on the Entertainment audio"],
   ["Entertainment audio plays",
    "The mid adjustment is accepted",
    "The Entertainment audio reflects the mid adjustment"],
   prio="P1", method=FUNC,
   reasoning="4866088 is the processing of the request where 4866090 at 043 "
             "and 048 is its transmission. The mid control is taken here "
             "because bass and treble are already exercised on the "
             "transmission side, so the three controls are covered between "
             "the leaves rather than repeated in each.")

tc("SWE1_AMM_049",
   "Confirm each selected level maps to its defined signal value",
   ["Adjust the bass control to the neutral level",
    "Read $ToneBASS$ and record it",
    "Adjust the bass control one step above neutral",
    "Read $ToneBASS$ and record it"],
   ["The neutral selection is accepted",
    "$ToneBASS$ reports the value the mapping table gives for neutral",
    "The one-step selection is accepted",
    "$ToneBASS$ reports the value the mapping table gives for that level"],
   desc=("The Audio Management software shall map each user-selected Bass, Mid, and Treble adjustment level to the corresponding HW signal value"),
   prio="P1", method=FUNC, remarks=PEND_SIG,
   reasoning=f"4866092 is the level-to-value encoding, a {TABLE_NOTE}. Two "
             f"adjacent levels are read rather than one, since an encoding "
             f"offset shows up as a shift and not as a single wrong value.")

# ------------------------------------------------------- routing and mixing
tc("SWE1_AMM_080",
   "Confirm the alert level tracks the cabin level on a CAN amplified system",
   ["Configure a CAN amplified audio system and play a cabin audio source at a known level",
    "Raise an alert",
    "Read the cabin audio level and the alert level and record them"],
   ["The CAN amplified system plays cabin audio at the set level",
    "The alert plays",
    "The alert level follows the cabin audio level as the specification defines"],
   desc=("For CAN-amplified audio systems, while cabin audio is active, the Audio Management software shall determine the alert playback level based on the active cabin audio level"),
   prio="P1", method=DECISION,
   reasoning="4866209 is the CAN-amplified counterpart of the default alert "
             "levels B4 covered at 306 and 307, so the system configuration is "
             "named in step 1 and the bracket says which system it is.")

tc("SWE1_AMM_106",
   "Confirm confirmation tones reach the front speakers only",
   ["Enable the confirmation tone feature",
    "Press a control",
    "Record the output channels carrying the tone"],
   ["The confirmation tone feature is enabled",
    "The press is accepted",
    "The front speakers carry the tone and no other channel does"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="4866283 says exclusively front, so the case reads the other "
             "channels too: exclusivity is only observable as an absence "
             "elsewhere.")

tc("SWE1_AMM_107",
   "Confirm alert tones reach the front speakers when the feature is enabled",
   ["Enable the entertainment and information alert feature",
    "Raise an alert",
    "Record the output channels carrying the alert"],
   ["The alert feature is enabled",
    "The alert plays",
    "The front speakers carry the alert"],
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning="4866286 is shared with B4's leaf 020 across batches, which is "
             "the sharing R-AM21 was ruled to catch. 020 pairs it with "
             "4865981 and observes the minimum-front rule; this row observes "
             "the routing that follows from the feature being enabled, so the "
             "bracket halves differ as R-AM16 requires.")

tc("SWE1_AMM_109",
   "Confirm loudness compensation is set from the detected amplifier configuration",
   ["Configure the vehicle with an external booster amplifier",
    "Start the head unit",
    "Record the loudness compensation state"],
   ["The external booster amplifier is configured",
    "The head unit starts",
    "The loudness compensation state follows the detected configuration"],
   prio="P1", method=DECISION,
   reasoning="4866291 keys the setting on detection at initialisation, so the "
             "case restarts rather than reconfiguring live — detection is the "
             "trigger the clause names.")

for sid, anchor, kind, verb in (
        ("SWE1_AMM_125", "4866453", "tone", "interrupts"),
        ("SWE1_AMM_127", "4866455", "alert", "interrupts")):
    tc(sid,
       f"Confirm a higher priority {kind} {verb} one already playing",
       [f"Trigger a lower priority {kind}",
        f"Trigger a higher priority {kind} while the first is still playing",
        f"Record which {kind} is audible"],
       [f"The lower priority {kind} plays",
        f"The higher priority {kind} is requested",
        f"The higher priority {kind} is audible and the lower one is not"],
       prio="P1", method=DECISION, pre="No audio source is active",
       reasoning=f"{anchor} states the pre-emption direction. Its converse is "
                 f"a separate object and a separate leaf, so the two are not "
                 f"merged: an implementation can pre-empt correctly and still "
                 f"fail to reject.")

for sid, anchor, kind in (("SWE1_AMM_126", "4866454", "tone"),
                          ("SWE1_AMM_128", "4866456", "alert")):
    tc(sid,
       f"Confirm a lower priority {kind} is rejected rather than queued",
       [f"Trigger a higher priority {kind}",
        f"Trigger a lower priority {kind} while the first is still playing",
        f"Record the audio produced after the higher priority {kind} ends"],
       [f"The higher priority {kind} plays",
        f"The lower priority {kind} is requested and produces no audio",
        f"No {kind} plays after the higher priority one ends"],
       prio="P1", method=NEGATIVE, pre="No audio source is active",
       reasoning=f"{anchor} says the lower request is ignored, not deferred. "
                 f"The case therefore waits past the end of the first tone: a "
                 f"queue would satisfy the silence during playback and then "
                 f"play the rejected request.")

tc("SWE1_AMM_160",
   "Confirm every speaker returns from the mute sequence",
   ["Trigger a sequence that mutes the speakers",
    "Wait until the sequence completes",
    "Record the audio on every speaker output"],
   ["The speakers are muted",
    "The sequence completes",
    "Every speaker output carries audio"],
   prio="P1", method=STATE, pre="No audio source is active",
   reasoning="4866529 says all speakers, so the case reads every output "
             "rather than sampling one: a partial unmute is the failure the "
             "word all guards against.")

tc("SWE1_AMM_168",
   "Confirm surround is suspended for an exclusive event and restored after",
   ["Enable surround sound and play an Entertainment source",
    "Trigger a system event that requires exclusive head unit audio",
    "Record the surround state",
    "End the event",
    "Record the surround state again"],
   ["Surround sound is enabled and Entertainment audio plays",
    "The event becomes active",
    "Surround sound is off",
    "The event ends",
    "Surround sound is on again"],
   prio="P1", method=STATE,
   reasoning="4866594, found by the range scan package 20 section 4 ruled in "
             "as gate 4. The keyword search behind package 18's zero-hit "
             "report was true but not evidence: the spec says requires HU "
             "audio and turn off surround sound, sharing no term with "
             "exclusive, override or emergency. Both halves are read because "
             "the requirement is that the state returns, not merely that it "
             "changes.")

tc("SWE1_AMM_222",
   "Confirm surround is unavailable without an external amplifier",
   ["Configure the vehicle without an external amplifier",
    "Open the audio settings",
    "Record the state of the surround sound function"],
   ["The vehicle has no external amplifier",
    "The audio settings open",
    "The surround sound function is unavailable"],
   prio="P1", method=NEGATIVE,
   reasoning="4866894 removes the function for a hardware configuration, so "
             "the case is negative and the configuration is named in step 1 "
             "rather than assumed.")

# --------------------------------------------------------- sound file sets
tc("SWE1_AMM_279",
   "Confirm each confirmation event draws its configured pre-recorded sound",
   ["Trigger a Conf1 confirmation event",
    "Record the sound file used",
    "Trigger a Conf2 confirmation event",
    "Record the sound file used"],
   ["The Conf1 event is raised",
    "The sound file used is the one configured for Conf1",
    "The Conf2 event is raised",
    "The sound file used is the one configured for Conf2 and differs from the first"],
   desc=("The Audio Management software shall select the applicable confirmation sound for Conf1, Conf2, and Conf3 based on the configured sound resource"),
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning=f"4865976 is the pre-recorded sound table for the confirmation "
             f"identifiers, a {TABLE_NOTE}. Two identifiers are exercised so "
             f"the selection is observable as a difference. Out-of-pool "
             f"anchor, single-source under R-AM18.")

tc("SWE1_AMM_280",
   "Confirm each confirmation event resolves to its system-generated definition",
   ["Trigger a Conf1 confirmation event",
    "Record the tone definition applied",
    "Trigger a Conf3 confirmation event",
    "Record the tone definition applied"],
   ["The Conf1 event is raised",
    "The tone definition applied is the one configured for Conf1",
    "The Conf3 event is raised",
    "The tone definition applied is the one configured for Conf3 and differs from the first"],
   desc=("The Audio Management software shall associate each supported confirmation event with its configured system-generated sound definition"),
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning=f"4865972 is the system-generated definition table, the "
             f"counterpart of the pre-recorded table at 279. A {TABLE_NOTE}.")

tc("SWE1_AMM_282",
   "Confirm each alert event draws its configured sound resource",
   ["Trigger a sports alert event",
    "Record the sound resource used",
    "Trigger a weather alert event",
    "Record the sound resource used"],
   ["The sports alert event is raised",
    "The sound resource used is the one configured for that alert",
    "The weather alert event is raised",
    "The sound resource used is the one configured for that alert"],
   desc=("The Audio Management software shall select the applicable sound resource for each supported alert event"),
   prio="P1", method=FUNC, pre="No audio source is active",
   reasoning=f"4865990 is the alert sound file table, a {TABLE_NOTE}. "
             f"Out-of-pool anchor, single-source under R-AM18.")

for sid, emphasis, tail in (
        ("SWE1_AMM_283", "the default fileset loads when the theme is absent",
         "This row takes the parameter missing from the configuration"),
        ("SWE1_AMM_285", "the default fileset loads for an unsupported value",
         "This row takes the parameter present but carrying a value the "
         "system does not support, which is a different configuration state "
         "reaching the same fallback")):
    tc(sid,
       f"Confirm {emphasis}",
       ["Configure the vehicle for the case under test",
        "Start the head unit",
        "Record the loaded sound fileset"],
       ["The configuration is as set",
        "The head unit starts",
        "The default sound fileset is loaded"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       reasoning=f"283 and 285 share 4867695 under R-AM16. {tail}, so the "
                 f"brackets differ. Out-of-pool anchor, single-source under "
                 f"R-AM18.")

tc("SWE1_AMM_284",
   "Confirm the branded fileset loads for its configured theme value",
   ["Configure the vehicle so that $Themed_Sounds$ is \"Fiat Latam\"",
    "Start the head unit",
    "Record the loaded sound fileset"],
   ["$Themed_Sounds$ reports \"Fiat Latam\"",
    "The head unit starts",
    "The Fiat Latam sound fileset is loaded"],
   prio="P1", method=DECISION, remarks=PEND_SIG,
   reasoning="4867696 is the positive branch against the two fallbacks at "
             "4867695. Without it, a system that always loaded the default "
             "would pass both 283 and 285. Out-of-pool anchor, single-source "
             "under R-AM18.")

for sid, emphasis, tail in (
        ("SWE1_AMM_292", "the strategy configured as customer selectable is honoured",
         "This row takes the strategy named in the configuration"),
        ("SWE1_AMM_294", "the same behaviour is the fallback when no strategy is set",
         "This row takes the strategy absent from the configuration, which "
         "the clause's closing sentence makes the default")):
    tc(sid,
       f"Confirm {emphasis}",
       ["Configure the vehicle for the case under test",
        "Adjust the park assist chime volume through the user setting",
        "Trigger a park assist chime",
        "Record the chime volume"],
       ["The configuration is as set",
        "The volume adjustment is accepted",
        "The park assist chime plays",
        "The chime volume is the user-selected setting"],
       prio="P1", method=DECISION, remarks=PEND_SIG,
       reasoning=f"292 and 294 share 4866173 under R-AM16, the sharing added "
                 f"at package 20 section 2.2 from the clause's closing "
                 f"sentence that this is the default behaviour. {tail}. "
                 f"Package 18's candidate 4866171 has no text in either "
                 f"corpus. Out-of-pool anchor, single-source under R-AM18.")

tc("SWE1_AMM_304",
   "Confirm the tone level is referenced to the active source and capped",
   ["Play an Entertainment source at a high volume step",
    "Press a control to raise a confirmation tone",
    "Read the source volume step and the tone volume step and record them"],
   ["Entertainment audio plays at the set volume step",
    "The confirmation tone plays",
    "The tone volume step is referenced to the source volume step and does not exceed volume step 22"],
   desc=("While cabin audio is active, the Audio Management software shall calculate the confirmation-tone playback volume using the currently active Entertainment or Information source volume as the reference"),
   prio="P1", method=BVA,
   reasoning="4866200 is the R1L variant: 4 volume steps below the active "
             "source or step 8, whichever is greater, capped at step 22. The "
             "neighbouring 4866198 gives 15 dB and step 6 and carries the VP4 "
             "and CTS1_2 radio list, not ours — the same variant "
             "discrimination that settled 310 in B2. The cap is read because "
             "it is the boundary the clause adds. Out-of-pool anchor, "
             "single-source under R-AM18.")

tc("SWE1_AMM_305",
   "Confirm the tone falls back to the fixed step when no cabin audio plays",
   ["Play no audio source",
    "Press a control to raise a confirmation tone",
    "Read the tone volume step and record it"],
   ["No audio source is active",
    "The confirmation tone plays",
    "The tone volume step is 8"],
   prio="P1", method=DECISION,
   reasoning="4866201 is the inactive-cabin branch of the pair with 4866200, "
             "and its figure is step 8 where the VP-family object at 4866199 "
             "says step 6 — the leaf says 8, which is the second confirmation "
             "that the R1L pair is ours. Out-of-pool anchor, single-source "
             "under R-AM18.")

tc("SWE1_AMM_293",
   "Confirm the gear-based strategy takes the volume from the chime request",
   ["Configure the vehicle so that $Park_Assist_Volume_Strategy$ is Gear Position Based",
    "Trigger a park assist chime carrying a requested volume",
    "Read the chime volume and record it"],
   ["The gear position based strategy is configured",
    "The park assist chime plays",
    "The chime volume is the level the chime request carried"],
   prio="P1", method=DECISION, remarks=PEND_SIG,
   pre="No audio source is active",
   reasoning="4866193, found by the gate-4 range scan package 20 section 2.3 "
             "authorised and ruled at the B5 delivery review. Partial "
             "coverage: the leaf also says user adjustment is disabled, which "
             "the anchor never states — that is an inference on the SWE.1 "
             "side, so it is disclosed here and kept out of the expected "
             "result under 8.4. Out-of-pool anchor, single-source under "
             "R-AM18.")


def main() -> None:
    ctx = {l["swe_id"]: l for l in json.loads(
        (ROOT / "batches" / "B5_context.json").read_text(encoding="utf-8"))}
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
    out = {"batch": "B5", "feature": "Audio Management",
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
    dest = ROOT / "generated" / "B5.json"
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
