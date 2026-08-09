# RD-1 Questions — FW036 Home HMI TC Regeneration

| | |
|---|---|
| Prepared | 2026-08-09 |
| Prepared by | Pei (SWQT, FW036 Home HMI) |
| Sent to | _(fill in: RD author / requirements owner)_ |
| Sent on | _(fill in)_ |
| Response received | _(fill in)_ |

Open questions for the requirements author, raised during regeneration of
the FW036 SWQT Home test case specification (62 leaf FRs from
FMWIFSM037A03-N1L-SWE1 Home HMI, sourced from the Home Screen HMI Logic and
Flow spec and the Last Mode Table).

Full detail for every item is in `HomeHMI/ANOMALIES.md` under the same
anomaly id. Dispositions were designed so that a contrary answer changes
reference strings, not TC content — nothing on our side is waiting on this
document.

Status at time of writing: **72 TCs generated across 62 leaves, lint green,
4 placeholder rows (055-03, 066, 070, 071), release tag
`fw036-home-regen-v2` (supersedes v1; the only difference is the A-H26 Scope
correction — no TC content changed).**

---

## Summary — four groups

| Group | Items | Why it matters |
|---|---|---|
| **1. Systemic — chapter 9 export truncation** | **A-H12, A-H16, A-H18** | The SYS1 Polarion export silently drops sentences inside chapter 9 sections it otherwise carries — three instances found by accident, so undetected siblings are likely. **Request: re-export chapter 9 in full and diff it against the PDF**, rather than patching three sentences. |
| 2. Requirement-set corrections | A-H06, A-H01, A-H17, A-H21 | A missing requirement row, a parent needing reclassification, a wrong description, a wrong source id — each one sentence to fix, each currently absorbed by a local disposition. |
| 3. Confirmations & residual risk | A-H03(c), A-H15, A-H13, A-H19, A-H24, A-H02/A-H20, A-H07 | Label equivalences, which-string-ships questions, external-coverage confirmations. Each states what changes if the answer goes the other way. |
| 4. FYI — no action requested | A-H22, A-H25 | Recorded so reviewers do not rediscover them. |

---

## Group 1 — Systemic: SYS1 export drops chapter 9 sentences

**Request: full re-export of Home Screen HMI L&F chapter 9 (HSS/Shortcuts)
with a diff against the PDF.** Three sentences are known-missing; item-code
diffing cannot see this defect class, so per-sentence patches leave the next
omission undetected.

| Id | Missing from export | Effect on 037 |
|---|---|---|
| A-H12 | HSS4: `show "Edit <n>" within the routine button (see Edit Routine section …)` | 048-04 carries no button label and no routine behaviour; the referenced Edit Routine section exists in NO document we hold — please also name that spec |
| A-H16 | HSS6: `Exception: preset routines and custom routines can be duplicated …` | 054 states the no-duplicate rule without its exception |
| A-H18 | SW7.1: `The same behavior will be applied if the shortcut is part of a routine …` | 061 has no routine-borne coverage |

Evidence these are defects, not filtering: in chapter 11 the export
*correctly* dropped the struck-through Know & Go clauses (A-H04); the
chapter 9 sentences carry no strikethrough.

Local disposition until answered: TCs are scoped to the export text; the
missing behaviours generate nothing (§8.4 — we do not test unexported
requirements).

---

## Group 2 — Requirement-set corrections

| Id | Finding | Requested action | Local disposition |
|---|---|---|---|
| A-H06 | 037 numbers 001–090 with exactly one gap: **035**. The spec section exists (outline 4.9, Loading State) and the done region carries two TCs for it | Add the missing 035 row to 037 | Completeness invariant scoped to regen rows; 035 allow-listed |
| A-H01 | **066** and its sub-ids 066-01/-02 are all marked Functional Requirement; 066's content is fully decomposed into the sub-ids | Reclassify 066 as Heading | Placeholder row; TC content traces to -01/-02 |
| A-H17 | **056**'s description carries HSS6.1's text verbatim (including the `HSS6.1)` prefix) while its title and source id (9.7.2) are HSS6.2 | Correct the 056 description to HSS6.2's text | TC written against HSS6.2 (title + source id outvote the description) |
| A-H21 | **070**'s source id suffix is `_10.8`, but 10.8 is SNS8 (owned by 069); 070's title and description are SNS9, which sits at 10.9 | Correct 070's source id to 10.9 | spec_reference cites 10.9, divergence declared in the TC |

---

## Group 3 — Confirmations & residual risk

| Id | Question | If the answer differs |
|---|---|---|
| A-H03(c) | Confirm `Last Mode Table … R1L-R (August 2 2021)` ≡ `… R1 SR24 1A Post DCR19344` (same date; all 15 List Item references resolve; the table's 15 HOME rows match our B7 leaves 1:1) | Only the spec_reference string changes — TC content was derived from the table itself |
| A-H15 | Driver-lockout popup: four spec sections say `"Feature not available …"`, PU0091 says `"Function not available …"`. Which string ships? Is PU0243 (matching wording, but scoped to the main category bar, no exit conditions) a stale duplicate? | ER wording swaps one word; PU citation unchanged |
| A-H13 | 048-01 prompt: spec text says `"Press and hold to drag and reorder shortcuts."`; the SW06 figure renders `Hold & Drag To Reorder Shortcuts`. Which ships? | ER string swap only |
| A-H19 | PU1274's String/Popup Message merges the CarPlay and Android Auto variants into one cell (with an inline substitution instruction). Please split into per-variant rows or state base + substitution separately | Our ER cites PU1274 by ID without quoting the composite string; a clean row lets us quote verbatim |
| A-H24 | 075 is titled "Home Screen Locking" but BSP4 states only page ORDER. Is a reorder lock (user cannot move a branded page ahead of the Default Home Screen) intended? | If yes, it needs its own requirement text — a TC then becomes writable; today we test ordering only |
| A-H02 / A-H20 | 055-03, 070, 071 are pure references to the Phone HMI spec and the Navigation supplier spec. Confirm those projects carry parallel SWE coverage for the referenced behaviours | If not, they are genuine coverage gaps to assign, not TCs we can write |
| A-H07 | HSD5.6's grey-out sentence does not restate whether CarPlay must still be connected. Our 020 TC-03 assumes it does (marked `[ASSUMPTION A-H07]`) | Pre-Condition changes; the split does not |

---

## Group 4 — FYI, no action requested

| Id | Note |
|---|---|
| A-H22 | SNS numbering runs … SNS3, SNS3.1, SNS5 … in both SYS1 and the PDF — there is no SNS4. Recorded so the gap is not read as a dropped section |
| A-H25 | The done region's motion TCs write `above 0 (more than 8)`; no spec states a numeric threshold. Inherited as-is. A ruling is needed only if a tester requires the authoritative value |
| A-H26 | The workbook header's 範圍 Scope field named a different deliverable (`…AppDrawer-Projection-SWE1HMI-V0.1`) — a copy-paste residue predating this regeneration. **Already corrected on our side** to `FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告`; the delivered workbook is `fw036-home-regen-v2`. Listed only so the change of identity string between our v1 and v2 is on the record |
