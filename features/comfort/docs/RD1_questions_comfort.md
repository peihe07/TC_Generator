# Comfort HMI — Open Questions for the Requirements Owner

**Feature**: Comfort HMI (newR1L, SR24 CR24879)
**Source under test**: `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)`
**Date**: 2026-08-16
**Status of this document**: draft prepared by the test-design side; not yet issued.
**Please send replies to**: _______________________________________________
（回覆去向由 Pei 填寫：收件人／信箱／彙整方式）

---

## Summary

Test cases have been written for **378 of the 403 verification units** in the
Comfort HMI requirement analysis (93.8%). One further unit (item 8) has a test
case that cannot be completed, and one question (item 9) asks where a whole
class of behaviour is defined.

The remaining **26 units** cannot be written without an answer from the
requirements side. Each is listed below with the sentence it comes from, what
is missing, what we have done in the meantime, and what we will do once the
question is answered.

| # | Question | Units blocked |
|---|---|---|
| 1 | Which vehicle configuration produces which set of comfort tabs? | 2 |
| 2 | Which airflow-mode set applies to which vehicle? | **9** |
| 3 | Where is the icon table for the recirculation and seat icons? | 3 |
| 4 | Is rear climate present on the vehicles these front-climate clauses describe? | 4 |
| 5 | Which vehicles have the additional rear-climate controls? | 1 |
| 6 | Where are the documents these clauses delegate to? | 3 |
| 7 | What distinguishes chapter 18 from chapter 17? | 3 |
| 8 | When is AUTO unavailable? | 1 |
| 9 | Which document defines whether comfort settings survive an ignition cycle? | 0 |
| | **Total** | **26 of 403 verification units** (question 9 blocks none) |

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

## 2. Which airflow-mode set applies to which vehicle?

**Units blocked**: 9 — `SWE1-HVAC-016-01` … `-03` (section 2.12),
`SWE1-HVAC-018-01` … `-06` (section 2.12.2)

**The sentences**:

> C13.) **There are 4 Airflow Mode** displayed in this order (1) Face,
> (2) Face plus Feet, (3) Feet, (4) Feet plus Windshield.
>
> C13.0) **In some non-tri mode equipment types**, airflow modes has 5 states…
>
> C19.) (tri-mode vehicles: three buttons, seven combinations)

**What is missing**: the specification describes three different front
airflow-mode sets. Two of them say which vehicles they apply to — "in some
non-tri mode equipment types" and the tri-mode chapter. **The four-mode set
(C13) carries no such statement**, so the only way to know a vehicle has four
modes is to rule out the other two, which is an inference rather than a
requirement.

**What we have done**: the 5-state set (2.12.1) and the tri-mode set (3.1)
are tested. The four-mode set and the hard-control cycle that depends on it
are not.

**Once answered**: nine test cases are written. If the answer is that the
four-mode set applies to vehicles outside this delivery, the nine units are
recorded as not applicable to this delivery rather than as untested.

---

## 3. Where is the icon table for the recirculation and seat icons?

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

**What is missing**: each clause points at a mapping — configuration to icon,
configuration to available controls — that is not in this document. "See
Climate section" does not name a section; we searched all 129 sections and
found no such table.

**What we have done**: no test case asserts which icon appears. Where a clause
has other content, that content is tested (for example, the recirculation
button's on/off behaviour is covered; only the icon is not).

**Once answered**: three test cases are written, quoting the mapping for the
configuration under test. If the mapping lives in another document, please
name it and we will treat it the same way as item 6.

---

## 4. Is rear climate present on the vehicles these front-climate clauses describe?

**Units blocked**: 4 — `SWE1-HVAC-015-04`, `SWE1-HVAC-015-05` (2.11),
`SWE1-HVAC-116-03`, `SWE1-HVAC-116-04` (16.11)

**The sentences** (identical in both chapters):

> Adjusting Fan speed and Mode will alter the **Front and Rear** passengers.
>
> If the **rear** fan speed, mode, or temp are adjust from either the
> touchscreen or rear climate controls will break SYNC and turn it off.

**What is missing**: these are front-climate clauses whose observable effect is
in the rear. Whether the vehicle under test has rear climate at all is not
stated anywhere in the document — the rear-climate chapters describe rear
behaviour, but no clause says which vehicles have it.

**What we have done**: the rear-climate chapter itself is fully tested (its
clauses are about rear climate, so the equipment is their subject). These four
units, whose clauses are about front climate, are not written.

**Once answered**: four test cases are written with the rear-climate
configuration stated as a pre-condition.

---

## 5. Which vehicles have the additional rear-climate controls?

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

## 6. Where are the documents these clauses delegate to?

**Units blocked**: 3 — `SWE1-HVAC-019-02`, `SWE1-HVAC-019-03` (2.13),
`SWE1-HVAC-083` (14.1)

**The sentences**:

> C14.) MAX A/C modifies multiple climate parameters. On/Off logic should
> follow requirements from **VF HVAC document**.
>
> HVACP1.) HVAC pop-ups should **follow the pop-up list**.

**What is missing**: both clauses hand their content to a document we do not
have. With the delegation removed, nothing testable remains in them.

**What we have done**: no test case for these three units. Two further units
of the same shape (sections 11.5 and 12.6, which delegate to an "HMI Settings
List" and to "HMI Notes") are delivered as rows that state the owning document
and record that no test case in this delivery covers them; the three units
here can be delivered the same way if you prefer.

**Once answered**: if the documents are supplied, test cases are written from
them. If they are out of scope for this delivery, the three units are
delivered as owner-stating rows like the two above.

---

## 7. What distinguishes chapter 18 from chapter 17?

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

## 8. When is AUTO unavailable?

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

## 9. Which document defines whether comfort settings survive an ignition cycle?

**Units blocked**: 0 — this question stops nothing; it may add work rather
than unblock it.

**What is missing**: of the 373 verification units we examined, **at most 222
describe a state the user sets** (the count is an upper bound — it was taken
by a keyword rule that errs towards including) — AUTO on or off, fan speed, airflow mode, seat
heating level — **and the document never says whether any of them is retained
after an ignition cycle or a cold boot**. Only two sections mention power or
key cycles at all (the pop-up suppression during ignition cycles, and the
latching of the last lumbar/bolster selection).

We checked the power-management specifications (CFTS009 Wake-up and Power-up,
CFTS010 Power Down) before asking. They state that climate pop-ups are shown
and HVAC controls stay active in certain power states, and they require the
restoring of *audio and telematics* settings by name — **but they say nothing
about retaining climate or seat settings**.

**What we have done**: nothing. Writing a test for "the fan speed is still 3
after a restart" would be inventing a requirement, so we have not written one.

**Once answered**: if the behaviour is owned by another document, we record
the owner and write nothing. If it belongs to Comfort, this becomes a batch of
new test cases rather than a correction to existing ones.

---


# Appendix — two questions that block nothing

**These are NOT part of the 25.** They are recorded so that nothing known is
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
