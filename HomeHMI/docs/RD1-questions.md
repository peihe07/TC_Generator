# RD-1 questions — FW036 Home HMI (draft for upstream)

Prepared 2026-08-09 alongside the FMWIFSM036A01 Home regeneration (62 leaves,
72 test cases). Every item below is recorded in `HomeHMI/ANOMALIES.md` with the
evidence; this file is the outbound packaging.

**Nothing here blocks delivery.** Each question has a disposition already
applied, stated under "What we did". A different ruling changes the listed
cells only — no test content depends on the answers.

---

## 1. SYS1 export is dropping sentences from chapter 9 — SYSTEMIC

**Ask: re-export chapter 9 in full and diff it against the PDF, rather than
patching the three sentences below.**

Three separate sentences present in the Home Screen HMI Logic and Flow PDF are
absent from the SYS1 Polarion export, and therefore absent from the 037
analysis report:

| Ref | Section | Sentence missing from the export |
|---|---|---|
| A-H12 | HSS4 / outline 9.5 | `If there is a custom routine, or a preset routine that has customization, show "Edit <name>" within the routine button (see Edit Routine section for more information on custom routines).` |
| A-H16 | HSS6 / outline 9.7 | `Exception: preset routines and custom routines can be duplicated within the same shortcuts widget.` |
| A-H18 | SW7.1 / outline 9.12 | `SW7.1) The same behavior will be applied if the shortcut is part of a routine, if applicable (exceptions noted in table)` — the whole item, no 9.12.1 exists |

Why we believe these are export defects rather than intentional filtering: in
chapter 11 the export *correctly* dropped content that is struck through in the
source (the Know & Go clause in BSP2, and all of BSP5–BSP5.3). The chapter 9
sentences carry no strikethrough, so there was no reason to omit them.

Why a full re-export rather than three fixes: all three were found by manually
diffing the export against the PDF, batch by batch. Our automated check
(`data/spec_diff.json`) compares item **codes** only — it confirms every HSS/SW
code exists on both sides, and is structurally unable to see a sentence dropped
from inside a section that is otherwise present. We cannot say these three are
all of them.

**What we did:** wrote the affected leaves to the SYS1 scope. 048-04 covers the
routine-editing entry point only; the routines duplication exception and
SW7.1 generate nothing, because there is no SWE requirement to attach them to.

**Also needed:** the referenced *"Edit Routine section"* is in neither
document — the PDF only points at it. Please name the owning specification.

---

## 2. Requirement 035 is missing from 037

`SWE1-HMI-HOME-001` … `-090` has exactly one gap: **035**. The workbook's
frozen region nevertheless carries two test cases for `SWE1-HMI-HOME-035`
("Loading State and Minimum Dwell", outline 4.9), authored by the previous
author, and the spec text genuinely exists.

So the requirement is real and covered, but has no row in the analysis report.

**Ask:** add the missing 035 row to 037.
**What we did:** scoped our completeness check to regenerated rows only, with
035 as a recorded exception (A-H06). We did not touch the frozen rows.

---

## 3. Last Mode Table — confirm the release labels are equivalent

037 traces `SWE1-HMI-HOME-076` … `-090` to
`Last Mode Table HMI Logic and Flow R1L-R (August 2 2021)`.

The file supplied to us is titled `Last Mode Table HMI Logic and Flow R1 SR24
1A (August 2 2021).xlsx`, whose Title sheet reads `R1 Last Mode Table`, Spec
Release `SR24 1A Post DCR19344`, dated **2021-08-02** — the same date.

We verified them as the same document: all 15 `_{n}` suffixes resolve to List
Item numbers in its `Last Mode Table` sheet, each leaf's title matches its List
Item semantically, and the sheet contains exactly 15 rows with
`Screen Display Status = HOME` — a 1:1 match with the 15 leaves.

**Ask:** confirm `R1L-R` ≡ `R1 SR24 1A Post DCR19344`.
**What we did (A-H03):** generated all 15 normally, and cited the **actual file
name** in Specification Reference so a tester can locate the document. If the
labels are not equivalent, only that string changes — the test content came
from the table itself.

---

## 4. Two leaves whose behaviour lives in specifications we do not have

| Leaf | Text | Owner |
|---|---|---|
| 055-03 | "Refer to Setting Navigation Shortcuts and Phone HMI Logic and Flow for other specific behavior." | Nav side is this same spec's SNS section (leaves 062–071); Phone side is external |
| 070 / 071 | "See Navigation supplier specifications for naming of shortcuts / for errors notifications." | Navigation supplier specification, not supplied |

**Ask:** confirm the Phone project has parallel SWE coverage for the shortcut
exclusion exception, and identify the Navigation supplier specification that
owns shortcut naming and error notifications.

**What we did (A-H02, A-H20):** these three leaves carry placeholder rows with
the delegation recorded in Remarks. No test content is written, because a
reference-integrity test case cannot state a single verifiable objective.

---

## 5. Field-level corrections

| Ref | Where | Problem | What we did |
|---|---|---|---|
| A-H17 | 037, `SWE1-HMI-HOME-056` | Requirement Description holds HSS6.1's text verbatim — including the literal `HSS6.1)` prefix — duplicating 055-01/-02/-03. The title and the HMI Source ID (outline 9.7.2) both say HSS6.2, whose real content appears in no 037 description at all. | Wrote 056 against **HSS6.2**; recorded the divergence in the test case Remarks. |
| A-H21 | 037, `SWE1-HMI-HOME-070` | HMI Source ID suffix is `_10.8`, but 10.8 is SNS8 (iconography, already owned by 069). SNS9 is at **10.9**, which exists in the export. The title and description are both SNS9's. | Cited **10.9**, declared as an explicit override so our linter records rather than hides it. |
| A-H13 | Home PDF p.14, figure SW06 | The Edit Shortcuts screen header renders as `Hold & Drag To Reorder Shortcuts`, but HSS4 (both SYS1 and the PDF text) specifies `"Press and hold to drag and reorder shortcuts."` | Asserted the specified wording; flagged in Remarks. **Please confirm which string ships.** |
| A-H15 | Pop Up List | Four Home sections quote the driver lockout popup as `"Feature not available while vehicle is in motion." [OK, X]`. No Pop Up List row matches both wording and controls: **PU0091** has the right controls but says "Function"; **PU0243** has the right wording but is scoped to "Editing the main category bar" and lists no exit conditions. | Cited **PU0091** and used its wording, per the profile rule that popup text comes from the Pop Up List. **Please confirm which string ships, and whether PU0243 is a stale duplicate.** |
| A-H19 | Pop Up List, PU1274 | The String/Popup Message reads `No Apple CarPlay Android Auto device connected.` — both product names at once — while its last line is an authoring instruction: `For Apple CarPlay, replace "Android Auto" text with "Apple CarPlay"`. No vehicle can display the string as written. | Cited PU1274 by ID and described its content and controls, but did **not** quote the composite string: an expected result quoting it could never pass. **Please split into per-variant rows, or state the base string and the substitution separately.** |
| A-H24 | 037, `SWE1-HMI-HOME-075` | Titled "Home Screen Locking", but BSP4 states only an ordering rule (first page is the Default Home Screen, branded pages follow). Nothing forbids reordering — and HSD7 does let the user reorder pages. | Tested the stated ordering only. **If a reorder lock is intended it needs its own requirement text**; today there is nothing to write a test against. |

---

## 6. Reclassification request

`SWE1-HMI-HOME-066` and its sub-ids `066-01` / `066-02` are all marked
`Functional Requirement`, but 066 is a pure parent — its content is entirely
decomposed into the two children, with nothing left of its own.

**Ask:** reclassify 066 as a Heading.
**What we did (A-H01):** 066 carries a placeholder row so the completeness
invariant still holds; all test content traces to 066-01 / 066-02.

---

## Recorded, no action requested

- **A-H05** — 13 of the frozen rows have a blank Test Case Priority. Recorded
  so the deviation is visibly pre-existing, not introduced by this
  regeneration. The frozen region was not modified.
- **A-H22** — the SNS notes run SNS1, SNS2, SNS3, SNS3.1, SNS5 … SNS10. There
  is no SNS4 in either document. No requirement traces to it and no behaviour
  appears to be missing; noted only so a reviewer counting items does not read
  the gap as a fourth dropped section.
- **A-H04** — resolved locally: test cases are written against effective
  (non-struck) text only, so the Know & Go Hub population path is out of scope.
- **A-H07** — HSD5.6 does not restate whether CarPlay must still be connected
  for the grey-out clause. We assumed it must, marked inline in the affected
  test case. Low risk: a contrary ruling changes one pre-condition.
- **A-H08 / A-H10 / A-H11 / A-H23** — internal linting and scoping rulings, no
  upstream action.
