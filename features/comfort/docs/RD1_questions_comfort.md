# Comfort HMI — Open Questions for the Requirements Owner

**Feature**: Comfort HMI (newR1L, SR24 CR24879)
**Source under test**: `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)`
**Date**: 2026-08-16
**Status of this document**: draft prepared by the test-design side; not yet issued.
**Please send replies to**: _______________________________________________
（回覆去向由 Pei 填寫：收件人／信箱／彙整方式）

---

## Summary

Test cases have been written for **383 of the 403 verification units** in the
Comfort HMI requirement analysis (95.0%). One further unit (item 8) has a test
case that cannot be completed, and one question (item 9) asks where a whole
class of behaviour is defined.

**22 units have an open question** on the requirements side. Each is listed
below with the sentence it comes from, what is missing, what we have done in
the meantime, and what we will do once the question is answered.

Of those 22, **20 have no test case at all**. The other two have a row in the
workbook that does not fully test them: item 7's unit is tested on one side
only, and item 8's unit is delivered as a row that names its owning document
and carries no procedure. The delivery note that accompanies the workbook
counts the other way — **20 units with no test case** — because that is what a
reviewer reading the workbook can see. Both numbers are stated with what they
count, so that neither is read as a correction of the other.

Six units that appeared in an earlier draft of this document have since been
written: four whose vehicle configuration is defined in the vehicle-controls
specification, and two whose content is defined in documents we have since
been able to read.

| # | Question | Units blocked |
|---|---|---|
| 1 | Which vehicle configuration produces which set of comfort tabs? | 2 |
| 2 | Why is the five-mode airflow requirement marked out of scope for this vehicle line, and what decides the airflow-mode set here? | **9** |
| 3 | Which PDO release carries the vehicle-specific recirculation and seat icons? | 3 |
| 4 | Which vehicles have the additional rear-climate controls? | 1 |
| 5 | Is the VF climate document we have the one the MAX A/C clause delegates to? | 2 |
| 6 | What distinguishes chapter 18 from chapter 17? | 3 |
| 7 | When is AUTO unavailable? | 1 |
| 8 | Does a document named "HMI Notes" exist for this programme? | 1 |
| 9 | Which document defines whether comfort **settings** survive an ignition cycle? | 0 |
| | **Total** | **22 of 403 verification units with an open question** (question 9 blocks none; 20 of the 22 have no test case, items 7 and 8 have a row that does not fully test them) |

Nothing in this document asks for a change to the requirements. Each item asks
for information that the requirement text refers to but does not contain.

---

## 1. Which vehicle configuration produces which set of comfort tabs?

**Units blocked**: 2 — `SWE1-HVAC-001-01`, `SWE1-HVAC-001-02` (section 2.1)

**The sentence**:

> R1C1.) The comfort category will have **up to 4 tabs depending on vehicle
> configuration**. Tabs are displayed in the following order: Front, Seats
> (WS or R1 Low) or Seat & Wheel (Maserati), Massage, Rear.

**What is missing**: the clause states that the tab set depends on the vehicle
configuration, and lists the possible tabs, but does not say which
configuration produces which set. A test for "the correct tabs are displayed"
needs to know, for the vehicle on the bench, what the correct set is.

**What we have done**: no test case is written for the number of tabs or their
order. The third unit of the same section (which tab is selected on entry) is
covered.

**Once answered**: two test cases are written, one per unit, with the
configuration stated as a pre-condition.

---

## 2. Why is the five-mode airflow requirement marked out of scope, and what decides the airflow-mode set here?

**Units blocked**: 9 — `SWE1-HVAC-016-01` … `-03` (section 2.12),
`SWE1-HVAC-018-01` … `-06` (section 2.12.2)

**The sentences**:

> C13.) **There are 4 Airflow Mode** displayed in this order (1) Face,
> (2) Face plus Feet, (3) Feet, (4) Feet plus Windshield.
>
> C13.0) **In some non-tri mode equipment types**, airflow modes has 5 states…

**What we found since the last version of this question**: the vehicle-controls
specification does state a condition for the five-mode set —

> The requirements in the section 'Defrost Softkey' shall be implemented if
> PROXI parameter `$VC_VEH_LINE$ = [637MCA]` OR `$Country_Code$ = [LATAM
> related countries]` then HU shall display the **5 airflow modes combination**
> according to the HMI specifications.

but in the export scoped to this vehicle line, all four rows carrying that
sentence have **Scope = None** and **Radio = R1M, R1H** — that is, they are
marked as not applying here. The four-mode set (C13) still carries no condition
of its own anywhere we have looked.

**What is missing**: two things, and the second matters more.

- Why those rows are marked out of scope for this vehicle line.
- **What does decide the airflow-mode set on the vehicles in this programme.**
  Marking the five-mode requirement out of scope does not by itself say the
  four-mode set applies — it says that one requirement is not ours. We would be
  inferring the rest.

**What we have done**: the 5-state set (2.12.1) and the tri-mode set (3.1) are
tested. The four-mode set and the hard-control cycle that depends on it are not.

**Once answered**: nine test cases are written, with the deciding configuration
stated as a pre-condition.

---

## 3. Which PDO release carries the vehicle-specific recirculation and seat icons?

**Units blocked**: 3 — `SWE1-HVAC-006-04` (2.5), `SWE1-HVAC-099` (14.15),
`SWE1-HVAC-122-02` (16.16)

**The sentences**:

> C4.) The recirc icon will display the vehicle model specific icon **as
> displayed in the table**.
>
> HVACSB1.) Available comfort controls (driver/passenger heated/vented seats,
> seat zones and heated wheel) **depend on vehicle configuration**.
>
> ICE15.) Off icon of seats will depend on system configuration
> **(see Climate section)**.

**What is missing**: the mapping from configuration to icon. The HMI Read Me
names the owner — "All graphics are place holders. **See PDO release** for
official graphics, animations, and layout" — so the question is now narrower:
**which PDO release carries these icons, and how do we obtain it?** The PDO
material available to us is a release cover sheet naming the receiving
organisation; it contains no icon table.

**What we have done**: no test case asserts which icon appears. Where a clause
has other content, that content is tested (the recirculation button's on/off
behaviour is covered; only the icon is not).

**Once answered**: three test cases are written, quoting the mapping for the
configuration under test.

---

## 4. Which vehicles have the additional rear-climate controls?

**Units blocked**: 1 — `SWE1-HVAC-039` (section 9.1)

**The sentence**:

> CR11.) **On some vehicles (See CFTS043 for details)**, there are additional
> Rear Climate controls and shortcuts.

**What is missing**: two things, of different weight.

- The clause itself has **no observable behaviour** — it introduces the
  variant rather than specifying anything. This unit may simply have no test
  case; please confirm.
- The seven units that follow it (the alternative fan pop-up, its labels, the
  status-bar shortcut) **have been written**, using this sentence as their
  pre-condition. To execute them, the tester must know **which vehicles are
  in that group**. CFTS043 is available to us, but the mapping from it to this
  clause's "some vehicles" is a decision we should not make on your behalf.

**What we have done**: seven test cases written and executable once the vehicle
group is known; this one unit not written.

**Once answered**: the vehicle group is added to the seven pre-conditions as a
sampling criterion; this unit is either written or recorded as having no
observable behaviour.

---

## 5. Is the VF climate document we have the one the MAX A/C clause delegates to?

**Units blocked**: 2 — `SWE1-HVAC-019-02`, `SWE1-HVAC-019-03` (section 2.13)

**The sentence**:

> C14.) MAX A/C modifies multiple climate parameters. On/Off logic should
> follow requirements from **VF HVAC document**.

**What is missing**: two things.

- **Whether `Climate_Controls_2_Zone_VF727` is that document.** It is the only
  VF climate document we have found, and the vehicle-controls specification
  does point at it ("follow the behavior described in {VF727}").
- **If it is, where the on/off logic lives.** What we can read there is the
  signal interface — a Max A/C request and a Max A/C status signal — and a
  signal is not something a tester can observe on the screen. The clause says
  the on/off *logic* follows that document; we could not find that logic in it.

**What we have done**: no test case for these two units. The MAX A/C behaviour
that chapter 16 states in its own words **is** tested; what is untested is the
on/off logic chapter 2 delegates away.

**Once answered**: two test cases are written from the named document, or the
two units are delivered as rows stating the owning document.

---

## 6. What distinguishes chapter 18 from chapter 17?

**Units blocked**: 3 — `SWE1-HVAC-129-01` … `-03` (section 18.1)

**The sentence**:

> W0.) The Comfort widget will have two screens: Comfort and Seats.

**What is missing**: this sentence is **word-for-word identical** to section
17.1. The only difference between the two chapters is the chapter heading
(17 is titled for one screen size, 18 for another) — and a heading is not a
requirement we can quote in a pre-condition.

**What we have done**: chapter 17's three units are tested. Chapter 18's three
are not, because the test cases would be identical to chapter 17's with
nothing to tell a tester which vehicle each applies to.

**Once answered**: if the two chapters differ by screen size, the screen size
is stated as a pre-condition and three test cases are written. If chapter 18
is a duplicate, the three units are recorded as covered by chapter 17.

---

## 7. When is AUTO unavailable?

**Units blocked**: 1 — `SWE1-HVAC-047` (section 10.4)

**The sentence**:

> EH4.) When the AUTO function is off **and available**, the user's first
> press of the AUTO button will activate the AUTO ECO functionality.

**What is missing**: the clause makes the behaviour conditional on AUTO being
"available", and **no section in the document says when AUTO is unavailable**.
We can test the available case, which we have; we cannot test the other side,
and we cannot tell a tester how to put the vehicle in it.

**What we have done**: the available case is covered. The unavailable case has
no test case.

**Once answered**: one test case is written for the unavailable case, with the
condition stated as a pre-condition.

---

## 8. Does a document named "HMI Notes" exist for this programme?

**Units blocked**: 1 — `SWE1-HVAC-072` (section 12.6)

**The sentences** — two chapters, one word apart:

> 11.5 HVS6. Refer to the **HMI Settings List** for the details on the Auto
> Comfort Settings options for heated/vented seats.
>
> 12.6 HVS6. Refer to the **HMI Notes** for the details on the Auto Comfort
> Settings options for heated/vented seats.

**What is missing**: the HMI Settings List exists and carries those options, so
section 11.5 is now tested. **No document named "HMI Notes" exists in the
material available to us.** The nearest candidate, the HMI Read Me, is a
conventions document — format key, acronyms, display anatomy — and contains
nothing about Auto Comfort Settings.

So the question is one of identity: **is "HMI Notes" another name for a
document that exists, is it a document we have not been given, or is the
reference an error for the HMI Settings List named one chapter earlier?**

**What we have done**: section 12.6 is delivered as a row that states the
owning document and records that no test case in this delivery covers it. We
have not assumed it means the same thing as 11.5 — the two chapters name two
different documents, and only one of them turned out to exist.

**Once answered**: if the document exists, one test case is written from it. If
the reference is an error, the row is replaced by one that mirrors 11.5.

---

## 9. Which document defines whether comfort **settings** survive an ignition cycle?

**Units blocked**: 0 — this question stops nothing; it may add work rather
than unblock it.

**Narrowed since the last version**: the Last Mode Table defines what happens to
the comfort **screen** across a power cycle — three rows name the COMFORT
category and give its behaviour ("Return to Comfort Main / Front Comfort
Screen", "Maintain Mode", "Return to Front Comfort Tab"), and their reference
column points back at the Comfort HMI Logic and Flow. **That half has an
owner, so we are not asking about it.**

**What is missing**: the other half. Of the verification units we examined,
**at most 222 describe a state the user sets** (an upper bound — the count was
taken by a keyword rule that errs towards including) — AUTO on or off, fan
speed, airflow mode, seat heating level — **and no document we have says
whether any of those values is retained after an ignition cycle or a cold
boot**. The Last Mode Table restores the screen, not the setting.

We checked the power-management specifications (CFTS009 Wake-up and Power-up,
CFTS010 Power Down) before asking. They state that climate pop-ups are shown
and HVAC controls stay active in certain power states, and they require the
restoring of *audio and telematics* settings by name — **but they say nothing
about retaining climate or seat settings**.

**What we have done**: nothing. Writing a test for "the fan speed is still 3
after a restart" would be inventing a requirement, so we have not written one.

**Once answered**: if the behaviour is owned by another document, we record the
owner and write nothing. If it belongs to Comfort, this becomes a batch of new
test cases rather than a correction to existing ones.

---


# Appendix — two questions that block nothing

**These are NOT part of the 22.** They are recorded so that nothing known is
left out of this document; neither of them stops a test case from being
written. They change the shape of what is delivered, not whether it can be
delivered.

- **Screen sizes in this delivery** — five test cases carry a screen or widget
  size taken word-for-word from the requirement (8.4"/10.1"/10.25"/12.3",
  12' Portrait 50%, 25% widget). If some of those configurations are not part
  of this delivery, the corresponding test cases apply to nothing and should be
  withdrawn rather than left in.
- **Chapters 11 and 12** — these two chapters describe the same heated and
  vented seat behaviour, with one difference: chapter 11 says a press "opens
  popup" and chapter 12 does not. Test cases exist for both. Whether that
  popup is a step in the interaction or a feedback display decides whether the
  two chapters are one requirement or two, and therefore whether 20 of the
  delivered test cases are duplicates.
