# Comfort HMI — Test Case Delivery Note

**Feature**: Comfort HMI (newR1L)
**Requirement under test**: `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)`
**Analysis document**: `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1`
**Workbook**: `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Comfort_20260817_itemfmt.xlsx`
**Date**: 2026-08-17
**Baseline**: the requirement baseline for this delivery is **SR24 CR24879
(September 25 2023)**. The folder also contains an SR25 revision of the same
document for reference; **it is not the baseline for these test cases**.
**Version**: this is **one version of an ongoing delivery**, not a final one. See
"What is still open" below; a later version will add rows rather than correct
these.

---

## What is covered

**434 test cases covering 383 of the 403 verification units** in the analysis
document.

A verification unit is one testable statement identified in the requirement
analysis. Several units are verified by more than one test case where the
requirement lists more than one way to trigger the same behaviour — for
example, a clause that names three separate actions that each break AUTO mode
is verified by three test cases, one per action.

---

## What is not covered — 20 units with no test case

These 20 units have **no row in the workbook**. Each depends on information the
requirement text refers to but does not contain, and a question document has
been prepared for the requirements owner (see the last section).

Two further units have a row that does not fully test them: one is tested on
one side only (described after the table), and one is a row that names its
owning document and carries no procedure (listed further down). The question
document counts **22 units with an open question**; this note counts **20 units
with no test case**. Both numbers are stated with what they count, and those
two units are the difference between them.

| Unit | Section | What is missing |
|---|---|---|
| `SWE1-HVAC-001-01` | 2.1 | The clause says the comfort tab set depends on vehicle configuration, but not which configuration produces which set. |
| `SWE1-HVAC-001-02` | 2.1 | As above, for the display order of the tabs. |
| `SWE1-HVAC-016-01` | 2.12 | The four-mode airflow set does not state which vehicles it applies to; the other two airflow sets do. |
| `SWE1-HVAC-016-02` | 2.12 | As above. |
| `SWE1-HVAC-016-03` | 2.12 | As above. |
| `SWE1-HVAC-018-01` | 2.12.2 | The hard-control cycle depends on the four-mode set above, so it inherits the same gap. |
| `SWE1-HVAC-018-02` | 2.12.2 | As above. |
| `SWE1-HVAC-018-03` | 2.12.2 | As above. |
| `SWE1-HVAC-018-04` | 2.12.2 | As above. |
| `SWE1-HVAC-018-05` | 2.12.2 | As above. |
| `SWE1-HVAC-018-06` | 2.12.2 | As above. |
| `SWE1-HVAC-006-04` | 2.5 | The recirculation icon is specified "as displayed in the table"; that table is not in the document. |
| `SWE1-HVAC-099` | 14.15 | The available comfort controls are said to depend on vehicle configuration; the mapping is not in the document. |
| `SWE1-HVAC-122-02` | 16.16 | The seat off-icon is specified by reference to the "Climate section"; no section carries that mapping. |
| `SWE1-HVAC-039` | 9.1 | The clause introduces a vehicle variant by reference to another document and specifies no observable behaviour of its own. |
| `SWE1-HVAC-019-02` | 2.13 | The clause hands its on/off logic to a VF HVAC document that is not available here. |
| `SWE1-HVAC-019-03` | 2.13 | As above. |
| `SWE1-HVAC-129-01` | 18.1 | The sentence is word-for-word identical to section 17.1; nothing in either chapter tells a tester which vehicle each applies to. |
| `SWE1-HVAC-129-02` | 18.1 | As above. |
| `SWE1-HVAC-129-03` | 18.1 | As above. |

### One unit is covered only in part

`SWE1-HVAC-047` (section 10.4) **has a row**. The requirement makes the
behaviour conditional on AUTO being "available", and no section states when
AUTO is unavailable. The available case is tested; the unavailable case has no
test case, because there is no stated way to put the vehicle in it.

---

## Four rows that carry no test procedure

Four rows in the workbook state a requirement and deliberately carry no
procedure or expected result. They are in the workbook so that the gap is
visible in the same place as the coverage, rather than only in this note.

| Row | Section | Why there is no procedure |
|---|---|---|
| `NR1L-ComfortHMI-010` | 13.4 | The long-press logic is defined in the HMI Core Logic and Flow requirement; with that delegation removed, nothing in the clause is verifiable against this specification alone. |
| `NR1L-ComfortHMI-012` | 13.5 | The equivalence to the previous 4-way rocker hard control is defined in CFTS044; same shape as above. |
| `NR1L-ComfortHMI-383` | 12.6 | The clause refers to a document named "HMI Notes"; no document of that name is available to us. The equivalent clause one chapter earlier (11.5) refers to the HMI Settings List, which we do have, and that unit **is** tested. |
| `NR1L-ComfortHMI-081` | 2.14 | The requirement states a reduction in climate-control power consumption, which no Comfort HMI screen, pop-up or indicator displays. |

Each of these rows names the owning document and states that no test case in
this delivery covers it.

They are identified in the workbook by the marker at the start of the Remarks
column; searching that column for `[BLOCKED` finds all four.

---

## Screen and widget sizes

Five test cases carry a screen or widget size taken word-for-word from the
requirement. If any of those configurations is not part of this programme, the
corresponding test cases apply to nothing and should be withdrawn rather than
executed.

---

## What is still open

A question document covering the 20 units above, and the two units with a
partial row, has been prepared for the requirements owner — **22 units with an
open question** in total. **It has not yet been issued.** When answers arrive:

- units that can then be written will be added to a later version of this
  workbook, identified by its own delivery record;
- units that turn out not to apply to this programme will be recorded as such
  rather than left as untested.

Two further questions have been recorded that block nothing: whether the two
heated-and-vented-seat chapters (11 and 12) describe one requirement or two,
and whether comfort settings are expected to survive an ignition cycle — the
requirement document does not say, and no test asserts either way.
