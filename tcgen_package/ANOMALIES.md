# Anomaly Tracker — FW036 Remaining TC Generation

Per RUNBOOK.md Step 2: anomalies are recorded here, never silently worked
around. Append; do not rewrite history.

---

## A-001 — 037 does not allocate a leaf to every SYS1 sub-section

**Found:** 2026-08-06, while building the PLA-062 batch context.
**Scope:** 10 of the 158 remaining leaf sections, 20 orphan child sections.

`SWE1-MEDIA-PLA-062-01` maps to section 11.3.1, whose entire SYS1 text is the
abstract sentence *"USB1) For USB, label may change based on connected drive
type."* The concrete, testable behaviour lives in two child sections that 037
allocates to no leaf at all:

- `11.3.1.1` — iPod connected via USB → USB icon changes, label becomes "iPod"
- `11.3.1.1.1` — when the label becomes "iPod", the App Drawer name must not change

`make_batch_context.py` originally gathered only the leaf's own section plus its
immediate parent, so this parent would have been generated with no testable
content in context.

**Affected leaf sections:** 11.3.1, 14.2, 14.3, 14.3.2, 14.4.3, 16.1, 16.1.4,
16.1.5, 17.1, 23.3.

**Resolution:** `make_batch_context.py` now also pulls descendant sections that
are not themselves remaining leaves (a descendant that IS a leaf still belongs
to its own parent's batch). All pilot contexts were rebuilt afterwards.

**Open:** none. Reviewers should still check the 10 parents above extra
carefully — the TC content there derives from sections 037 never enumerated.

---

## A-002 — Duplicate item code `BTSA1.2)` in the spec

**Found:** 2026-08-06, generating PLA-065 / PLA-066.

Sections 11.4.1.2 and 11.4.1.3 both open with the literal code `BTSA1.2)`:

- `11.4.1.2` — BTSA1.2) If user presses no/close, system closes the popup and
  shows "Connect a Bluetooth Audio Device" in the metadata area.
- `11.4.1.3` — BTSA1.2) If the vehicle is in motion, do not provide this popup.

Confirmed against the source page image (`spec_pages/page_20.png`) — the
duplicate label is in the original deck, not an OCR or export artefact. The
third clause should presumably read `BTSA1.3)`.

**Impact:** none on generation — 037 allocates separate leaves (PLA-065,
PLA-066) and the outline numbers are distinct. Only matters if anything ever
keys on the item code instead of the outline number.

**Open:** candidate for RD-1 escalation to the requirements author. Low
priority; cosmetic.

---

## A-003 — `section_manifest` is 473 sections, RUNBOOK records 474

**Found:** 2026-08-06, rebuilding Step 1 artifacts.

The rebuild produced 473 outline entries against the 474 recorded in the
package. The single missing entry is `5.1.4`, in chapter 5 — outside the
remaining scope (chapters 11–23). All 158 remaining sections resolve and all
map to a page, matching the RUNBOOK's verified 158/158.

**Cause:** the SYS1 export used for the rebuild is the repo copy at
`spec-index/cache/SYS1_HMI_Media_HMI_Logic_and_Flow_R1L-L_(Febuary_9th,_2026).xlsx`,
which appears to be a marginally different revision from the one used when the
package was first built.

**CLOSED** 2026-08-06 by Pei's cross-check: 5 of 6 sampled done-region sections
(META2 / PC3 / ST2 / PSB3 / SMP1) hit 100% verbatim against the PDF OCR; the
one 25% hit (4.2) is a bullet list whose layout OCR scrambled, not a content
difference. Combined with 158/158 section-number resolution and the verbatim
11.3.1 match, the SYS1(R1L-L Feb 2026) ↔ PDF(July 2023) version risk is
resolved. No further action.

---

## A-004 — No spec-confirmed control label for opening the App Drawer

**Found:** 2026-08-06, generating PLA-062 TC-03.

`11.3.1.1.1` requires the App Drawer name to stay "USB" while the source label
reads "iPod", but neither the SYS1 text nor page 20 names the control that
opens the App Drawer. The step is therefore written as *"Open the App Drawer
and read the name of the USB media entry"* rather than inventing a quoted UI
label.

**Open:** a reviewer with HU access should replace this with the real labelled
step once the control name is confirmed.

---

## A-005 — Done region uses `as the baseline` in recording steps (§5.6 deviation)

**Found:** 2026-08-06, adding the §5.6 linter rule during pilot review.

docs/ASPICE_SWE6_AI_Instruction.md §5.6 reserves the word `baseline` for the
final comparison ER: *"Use the word `baseline` only in the comparison step in
the final ER, not in the recording step."* The human-authored done region
breaks this in 8 places, all in non-final recording ERs:

| TC | ER step |
|---|---|
| SWE1-MEDIA-PLA-044-01 | ER4 of 6 |
| SWE1-MEDIA-PLA-049-01 | ER4 of 7 |
| SWE1-MEDIA-COM-014-01 | ER3 of 6 |
| SWE1-MEDIA-COM-016-01 | ER3 of 5 |
| SWE1-MEDIA-COM-029-01 | ER2 of 6 |
| SWE1-MEDIA-COM-032-01 | ER3 of 7 |
| SWE1-MEDIA-COM-017-02 | ER2 of 3 |
| SWE1-MEDIA-COM-018-01 | ER2 of 5 |

**Impact:** the `er-baseline` gate rule is enforced on generated TCs (PLA-068
TC-01/TC-02 were corrected accordingly). The done region is exempted in
`tests/test_lint_tcs.py`, with the count pinned at 8 so it cannot grow
unnoticed.

**Open:** decide whether rows 10–332 get retro-fixed in a later pass, or
whether §5.6 should be relaxed to match established practice. Not a blocker —
rows 10–332 are explicitly out of scope for this regeneration.

---

## A-006 — No enumerated USB drive-type list to pair a negative against

**Found:** 2026-08-06, pilot review of PLA-062.

§7 requires enumerated supported items to carry a negative counterpart. Spec
11.3.1 / 11.3.1.1 name only iPod as a label-changing drive type; there is no
enumerated list of supported types and no statement of what an unsupported or
unlisted drive type does. Generated coverage is therefore the iPod case plus
the default USB mass-storage contrast (PLA-062 TC-01 / TC-02) — an
"unsupported drive type" TC would be inventing behaviour (§8.4) and was
deliberately not produced.

**Open:** RD-1 question to the requirements author — is there a defined set of
drive types that change the source label, and what is the label for a type
outside it?

---

## A-007 — PSB2.1 says max 5 pinned sources; table PSB2.4 tops out at 4

**Found:** 2026-08-06, generating COM ch12 (Pinned Sources Bank).

Section 12.2.1 text: *"The Pinned Sources Bank can have from 0 to a maximum of
5 pinned sources. (See Table PSB2.4)."* The referenced table on page 22 lists
every configured radio size, and the highest value is 4:

| Radio Size | Max |
|---|---|
| 7" Landscape | 3 |
| 8.4" Landscape | 4 |
| 10.1" Landscape | 4 |
| 10.1" Portrait | 4 |
| 10.25" Widescreen | 3 |
| 12" Landscape | 4 |
| 12" Portrait | 4 |

A bank of 5 is therefore unreachable on any listed configuration. The generated
TCs use the table (the more specific, per-configuration source) as ground
truth, not the "5" in the prose.

**Open:** RD-1 question — is 5 a stale value, or is there an unlisted radio
size that allows 5?

---

## A-008 — 037 allocates leaves to only part of the PSB tables

**Found:** 2026-08-06, generating COM ch12.

Table PSB2.4 has 7 radio sizes; `SWE1-MEDIA-COM-047` covers only 3 of them
(8.4" Landscape, 10.1" Landscape, 10.1" Portrait — all max 4). Unallocated:
7" Landscape (3), 10.25" Widescreen (3), 12" Landscape (4), 12" Portrait (4).
Both **max-3** configurations — the more interesting boundary — have no leaf.

Table PSB2.3 has 5 market variants (NAFTA / EMEA / LATAM / APAC / APAC-China);
`SWE1-MEDIA-COM-046` quotes only the NAFTA row. Generated TCs follow the leaf
and cover NAFTA.

Unlike A-001 this cannot be fixed in the context builder: the missing cases
have no req_id, and a TC without a workbook row has nowhere to be written.

**Open:** RD-1 question — should 037 gain leaves for the remaining radio sizes
and market variants, or are those configurations out of scope for FW036?

---

## A-009 — PU0996 does not exist in the Pop Up List (BLOCKED)

**Found:** 2026-08-06, generating COM ch13.

`SWE1-MEDIA-COM-051-01` (section 13.2) has exactly one requirement sentence:
*"SMP1) See Pop Up List: PU0996"*. The whole content of the requirement is
delegated to that popup definition — and PU0996 is not in the Pop Up List.

Verified against `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx`: all
three sheets (Main / Templates / Drop Down Fields) searched, 1340 PU ids
present, and the only id in the PU099x range is PU0998.

**Status: BLOCKED.** No TC generated. Writing one would require inventing the
popup's layout, strings and exit conditions (§8.4). `generated/
SWE1-MEDIA-COM-051.json` carries a `blocked` marker naming this anomaly, and
the linter reports it as a blocked parent rather than an empty file.

**RD-1 question (two directions, ask both at once — the follow-up differs):**

1. Is `PU0996` a typo in SMP1, i.e. should it point at a different PU id? →
   follow-up is a spec correction, and the TC can then be written from the
   existing Pop Up List.
2. Or is PU0996 defined in a Pop Up List revision newer than Dec 15 2023? →
   follow-up is obtaining that revision, and `data/` must be rebuilt against it.

**Write-back handling — the hole must be visible in the deliverable.** Without
a row, A03's 450 leaves would produce only 449 rows and an ASPICE traceability
audit would see an unexplained gap. COM-051-01 therefore still gets a row:

| Column | Value |
|---|---|
| D | `SWE1-MEDIA-COM-051-01` |
| G / H | `MediaHMI` / `Source Selection` |
| I | the RD sentence verbatim |
| J / K | `NA` |
| L / M | `BLOCKED - see Remarks` |
| N | `Media_HMI_Logic_and_Flow_R1_SR24_Post_2A_(July_25th,_2023)_13.2` |
| O | `NEW` |
| P / R | left blank - both are dropdown-constrained and no value is truthful |
| **AH (Remarks)** | `BLOCKED: PU0996 not found in Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023). Requirement content is fully delegated to that missing definition. See ANOMALIES A-009. Awaiting RD-1.` |

Note: the workbook has no authoring-status dropdown (the `下拉選單` sheet holds
only the 9 design methods) and column AF `Test Result` is for execution
results, so column AH `Remarks` is the correct home for the declaration.

**RUNBOOK Step 4 gap:** the column mapping in Step 4 does not list AH. It must
be added before write-back, or the blocked declaration is silently dropped.

---

## A-010 — Table SMP2.2 marks two radio sizes N/A with no stated meaning

**Found:** 2026-08-06, generating COM ch13.

Table SMP2.2 (Max Number of Recent Sources by Radio Size, page 23):

| Radio Size | Max Recent Sources |
|---|---|
| 7" Landscape | **N/A** |
| 8.4" Landscape | 5 |
| 10.1" Landscape | 6 |
| 10.1" Portrait | 5 |
| 10.25" Widescreen | **N/A** |
| 12" Landscape | 6 |
| 12" Portrait | 6 |

`N/A` is undefined here: it could mean the Source Secondary Menu Pop up is not
available on those sizes, that the count is unlimited, or that the value was
never specified. No TC covers those two configurations — all three readings
would produce a different expected result.

037 again allocates leaves to only 3 of the 7 sizes (`SWE1-MEDIA-COM-055`:
8.4" = 5, 10.1" Landscape = 6, 10.1" Portrait = 5), the same pattern as A-008.

**Open:** RD-1 — what does N/A mean for 7" Landscape and 10.25" Widescreen?

---

## A-011 — BT1.1.1 and BT1.1.2 contradict each other on the empty-media case

**Found:** 2026-08-06, reading page 24 for the ch14 first parent.

Two adjacent sub-clauses give opposite answers for the same situation:

- `14.1.1.1` — *"BT1.1.1) When a source is connected ~~USB or Disc is
  inserted~~ with no files with valid audio format, Browse Tab is **not
  available**."*
- `14.1.1.2` — *"BT1.1.2) When a USB or Disc is inserted with no files with
  valid audio format, Browse Tab **is available** and if the user presses
  browse each category will display 'No items'."*

BT1.1.1 carries a visible strikethrough edit on the page image: "USB or Disc
is inserted" was struck out and replaced with the broader "a source is
connected". That edit is what created the overlap — after it, the USB/Disc
case falls under both clauses, with opposite outcomes.

**Impact:** `SWE1-MEDIA-COM-058` (14.1.1.1) and `SWE1-MEDIA-COM-059`
(14.1.1.2) are the next two parents in ch14 and sit directly on the
contradiction. Neither can be written unambiguously for USB/Disc without a
ruling.

**Ruling (Pei, 2026-08-06) — the two parents are handled differently:**

- `SWE1-MEDIA-COM-058` (BT1.1.1) → **BLOCKED.** Resolving the overlap in favour
  of the more specific BT1.1.2 leaves BT1.1.1 with a residual scope of
  "a connected non-USB/Disc source that supports browse and has a file
  concept" — which has no instantiable subject in the spec (BTSA streaming has
  no file concept; AUX does not support browse at all and is already covered by
  BT1.1 / COM-057-02). Writing this TC would mean inventing the test scope, not
  merely picking a reading.
- `SWE1-MEDIA-COM-059` (BT1.1.2) → **generated on a declared assumption.** Its
  own clause is complete, self-consistent and testable; the contradiction is
  spilled onto it by the BT1.1.1 edit. Blocking a well-formed requirement to
  atone for a neighbour's editing error is the wrong trade. specific-over-
  general is a defensible interpretation canon, and the strikethrough on the
  page image supports "the broadening forgot to carve out USB/Disc".

`generated/SWE1-MEDIA-COM-059.json` carries an `assumption` marker naming this
anomaly, so every TC betting on this reading is machine-retrievable when the
ruling arrives. The linter enforces the same contract as `blocked`: both a
`note` and an `anomaly` id, or it is a finding.

**Open:** RD-1 — ask for a ruling on **both** clauses at once:

1. Was BT1.1.1 meant to be narrowed to non-USB/Disc sources when it was
   broadened, leaving BT1.1.2 as the USB/Disc rule? (If yes, COM-059 stands as
   generated and COM-058 needs a stated scope or removal.)
2. If BT1.1.1 is instead authoritative for USB/Disc, BT1.1.2 is dead text and
   every TC in COM-059 must be reworked.

---

## A-012 — BT1.6 "cursor always begins from the top" contradicts BT1.2.1

**Found:** 2026-08-06, generating ch14 page-24 parents.

- `14.1.6` — *"BT1.6) Currently playing song or station shall be highlighted in
  activated color, however the cursor **will always begin from the top of the
  list**."*
- `14.1.2.1` — *"BT1.2.1) For the presets or the All Stations list, the cursor
  should **initially be either at a) currently tuned station** or b) top of the
  list for presets, when current channel is not a preset or c) the previous
  browse category."*

For the Presets / All Stations lists the two clauses give different initial
cursor positions. Same shape as A-011: a general clause ("always") against a
list-specific clause.

**Handling — resolved by scope, then declared:** `SWE1-MEDIA-COM-065-02`
(the general "cursor at top on entering Browse") is generated against a list
that is *not* Presets or All Stations, so the TC itself is unambiguous;
`SWE1-MEDIA-COM-061-01..04` cover the Presets / All Stations behaviour under
BT1.2.1. The carve-out is an application of specific-over-general — the same
canon ruled on in A-011 — so `generated/SWE1-MEDIA-COM-065.json` carries an
`assumption` marker naming this anomaly.

**Open:** RD-1 — is BT1.6's "always" meant to exclude the Presets / All
Stations lists governed by BT1.2.1? If instead BT1.6 is authoritative
everywhere, COM-061-01 and COM-061-04 must be reworked.

**Marker location (corrected 2026-08-06):** the `assumption` marker sits on
`generated/SWE1-MEDIA-COM-061.json`, not on COM-065. Markers follow the rework
target: COM-065-02 is unambiguous by scope and needs no rework whatever the
ruling, so a marker there would be a false positive. COM-065's reasoning
cross-references A-012 instead.

---

## A-013 — BT4.1.1's field list skips number 2

**Found:** 2026-08-07, reading page 26 for RAD ch14.

*"BT4.1.1) Display station information as follows: **1)** Frequency, **3)**
Station ID (call sign), if available, **4)** short form of genre name (station
program type), if available."*

The enumeration runs 1, 3, 4 — item **2** is absent, in both the page image and
the SYS1 export, so this is not an OCR artefact. Either a field was deleted
without renumbering, or one is missing from the list.

037 allocates exactly three leaves (`SWE1-MEDIA-RAD-040-01..03`), one per
surviving item, so the generated TCs cover what is written. If item 2 was a
real field, no TC covers it and no leaf exists for it.

**Open:** RD-1 — was a second field (e.g. HD indicator, station name) removed
from BT4.1.1, or is the numbering simply wrong?

---

## A-014 — Item code `BT4.2.1` is used for two different clauses (informational)

**Found:** 2026-08-07, cross-reading pages 25/26 against the SYS1 outline.

On the page images, `BT4.2.1)` labels both:

- page 25 — *"When entering that category the first line item will state 'No items'."*
- page 26 — the *"List Display Reference"* table

The SYS1 R1L-L export renumbers the first one to `BT3.3.1`, which is the
consistent reading (it belongs under BT3.3, empty categories). Generation
follows the SYS1 outline number (14.3.3.1), so nothing is ambiguous in
practice.

**Impact:** none on generation — outline numbers, not item codes, drive every
mapping. Recorded only so a reviewer comparing TCs against the 2023 PDF does
not read the mismatch as an error. Same class as A-002.

**Open:** none. Informational.

---

## A-015 — PU0997 is also absent; two consecutive missing PU ids

**Found:** 2026-08-07, reading page 30 while surveying RAD ch16.

`APP1` (ch18, All Presets Pop up) cites *"(See Pop up List: PU0997)"*. PU0997
is not in `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` either — same
search as A-009 (all 3 sheets, 1340 PU ids; the PU099x range holds only
PU0998).

**This materially changes the reading of A-009.** Two *consecutive* ids —
PU0996 (SMP1, ch13) and PU0997 (APP1, ch18) — are both missing from the same
revision, while PU0998 in the same range is present. Two independent typos
landing on adjacent ids is far less likely than one revision gap: the evidence
now favours A-009's RD-1 direction 2 (the Pop Up List revision post-dates
Dec 15 2023 and PU0996/PU0997 were added in it).

**Action:** ask the RD-1 question once for both ids. If a newer Pop Up List is
obtained, `SWE1-MEDIA-COM-051` unblocks and the ch18 APP1 leaf can be written
without a blocked marker.

---

## A-016 — `Table PRE1.2` does not exist

**Found:** 2026-08-07, generating RAD ch16.

`16.2.3.1 (PRE2.3.1)` — *"The default will be 3 banks of presets from a maximum
of 6 preset banks. **(See Table PRE1.2)**"*.

There is no Table PRE1.2. `PRE1.2` is a clause ("If a preset has not been set
it will display a plus sign"), and the only table in the Mixed Presets section
is `PRE1.1) Presets per Bank by Radio Size`. Neither PRE1.1 nor any table on
pages 28 or 30 states a bank count of 3 or a maximum of 6.

The values 3 and 6 appear only in the PRE2.3.1 sentence itself, so the
generated TC takes them from the prose and cites 16.2.3.1 alone.

**Open:** RD-1 — is the reference meant to be Table PRE1.1, or is a bank-count
table missing from the deck?

---

## A-017 — APP clause numbering jumps from APP4 to APP10

**Found:** 2026-08-07, reading page 30 (ch18 All Presets Pop up).

The clause list runs APP1, APP2, APP2.1, APP3, APP3.1, APP4, APP4.1, then
**APP10** through APP18. APP5–APP9 are absent from both the page image and the
SYS1 export.

Same class as A-013 (BT4.1.1 skipping item 2). 037 allocates leaves only to the
clauses that exist, so nothing is silently dropped from generation — but if
APP5–APP9 were real clauses, the ch18 Preset Management set has a coverage hole
that no leaf reveals.

**Open:** RD-1 — were APP5–APP9 removed, or are they missing from this deck
revision? Ask together with A-015, since both point at the same revision
question.

---

## A-018 — MPB1.1 allows 8 presets per bank; Table PRE1.1 tops out at 6

**Found:** 2026-08-07, generating RAD ch17.

- `17.1.1 (MPB1.1)` — *"The preset bank can have a maximum of **8** presets."*
- `16.1.1 (PRE1.1)` Presets per Bank by Radio Size — 7" = 5 (LATAM 4),
  8.4" = 5, 10.1" L = 6, 10.1" P = 5, 10.25" = 6, 12" L = 6, 12" P = 6.

No listed radio size allows more than 6, so a bank of 8 is unreachable on any
configuration. Structurally identical to A-007 (PSB2.1's "maximum of 5" against
Table PSB2.4's max of 4).

**Handling — generated on a declared assumption.** A-007 was ruled
table-over-prose (the per-configuration table is the more specific source).
Applying the same canon here, `SWE1-MEDIA-RAD-062-01` verifies the bank against
the value defined for the vehicle radio size in Table PRE1.1, expressed
symbolically, rather than against the unreachable literal 8.

Unlike A-007 this *is* a bet: there the leaf was the table itself, here the leaf
sentence is the one asserting 8. `generated/SWE1-MEDIA-RAD-062.json` therefore
carries an `assumption` marker naming this anomaly.

**Open:** RD-1 — ask together with A-007, they are the same question twice: is
the prose figure stale, or does a radio size exist that is missing from both
tables?

---

## A-019 — MPB clause numbering skips 1.4

**Found:** 2026-08-07, reading page 29.

The clause list runs MPB1.1, 1.2, 1.3, 1.3.1, **1.5**, 1.5.1, 1.6, 1.7, 1.8,
1.8.1–1.8.3, 1.9. `MPB1.4` is absent from the page image and from the SYS1
export, and the SYS1 outline numbering absorbs the gap (17.1.4 → MPB1.5), so
outline-driven generation is unaffected.

Third instance of the same defect class: A-013 (BT4.1.1 skips 2), A-017
(APP5–APP9 absent), and now this. **Recommend raising the pattern itself with
RD-1**, not just the individual gaps — three independent numbering holes in one
deck suggests clauses were deleted without renumbering, and each hole is a place
where a requirement may have been silently dropped.

**Open:** RD-1 — was an MPB1.4 clause removed?

---

## A-020 — MPB1.7 / MPB1.8.x have no leaf, and are not elaborations of their ancestor

**Found:** 2026-08-07, generating RAD ch17.

Five sub-sections under 17.1 have no leaf of their own: `17.1.6 (MPB1.7)` HD
sub-channel preset labels, `17.1.7 (MPB1.8)` FM-EU PSN labels, and
`17.1.7.1–.3 (MPB1.8.1–.3)` PSN fallback, truncation, and save-as-displayed.

The A-001 coverage rule routes orphan sub-sections to the batch of their nearest
leaf ancestor, so these land in `SWE1-MEDIA-RAD-061`'s context. **That is the
right routing but the wrong content relationship**, and it marks a limit of the
rule worth stating explicitly:

> A-001 decides which batch *sees* an orphan's text. It does not decide that
> the orphan elaborates the ancestor leaf. Here the ancestor leaf is MPB1
> ("Playing Tab shows one full bank at a time"); the orphans are preset-button
> *label* rules, i.e. siblings of MPB1.5 / MPB1.6 — which do have leaves
> (RAD-066, RAD-067, RAD-068). Writing them under RAD-061-01 would attribute
> label requirements to a layout requirement.

Generation therefore covers only MPB1 under RAD-061, and these five clauses get
no TC — no req_id, nothing to write a row against (A-008 logic).

Scope note: MPB1.8.x is FM-EU, likely out of scope for this NAFTA programme;
MPB1.7 (HD Radio) is not — HD Radio is an NA feature and its preset label rule
is genuinely uncovered.

**Open:** RD-1 — should 037 gain a leaf for MPB1.7 (HD preset labels)? Confirm
MPB1.8.x is out of scope for FW036.

---

## A-021 — "All Presets Pop up" and "Presets Pop Up": one container or two?

**Found:** 2026-08-07, generating RAD ch18 (the Preset Management stop point).

ch18 names its popup two different ways and never states whether they are the
same thing:

- `APP1` — *"Pressing the 'All Presets' button opens the **All Presets Pop up**
  displaying up to 3 banks of presets per page, a 'Presets Shown' indicator,
  currently playing metadata, an X."*
- `APP2`, `APP10`–`APP13`, `APP17`, `APP18` — all say **"Presets Pop Up"**.
- The page-30 screenshot is captioned **"Presets Pop Up"**, and shows metadata,
  an X, preset rows and an "Edit Presets" button.

Evidence they are the same: the screenshot's contents match APP1's list, and
nothing in the deck describes opening a second, different popup.
Evidence they might not be: APP1 lists a "Presets Shown" indicator, but in the
screenshots that indicator appears on the **Edit Presets Pop Up**, not on the
"Presets Pop Up"; and APP1 never mentions the Edit Presets button that APP12
places on the "Presets Pop Up".

**Handling — generated on a declared assumption.** They are treated as one
container. Each TC uses the container name from the clause it is written
against (APP1 leaves say "All Presets Pop-up", APP10+ leaves say "Presets
Pop-up"), matching 037's own wording, and never invents a third name.

This matters more than a naming nit: the whole ch18 review discipline is
"anchor every ER to its container and quote that container's own strings". A
container that has two names in the source is exactly where that discipline
produces false confidence.

**Open:** RD-1 — are "All Presets Pop up" and "Presets Pop Up" the same
screen? If yes, which name is canonical? If no, what opens the second one?

---

## A-022 — APP10/APP17 and APP11/APP18 are duplicate requirements

**Found:** 2026-08-07, generating RAD ch18.

Two pairs of clauses state the same requirement twice:

| | |
|---|---|
| `APP10` (18.5) | *"The user can long press an existing preset (500 ms) to save a new preset over that existing preset on the Presets Pop up."* |
| `APP17` (18.12) | *"The user is able to long press and save a new preset over an existing preset from the Presets Pop Up."* |
| `APP11` (18.6) | *"The user can short press a plus ['+'] sign to add a new preset to an empty slot on the Presets Pop Up."* |
| `APP18` (18.13) | *"short press a plus ['+'] sign to add a new preset from the Presets Pop Up."* |

037 allocated a separate leaf to each, so the pairs produce identical TC
content under different req_ids: RAD-075-01 ≡ RAD-082-01, RAD-076-01 ≡
RAD-083-01. APP10 adds the 500 ms figure that APP17 omits; otherwise the
clauses are equivalent in trigger, input and verification target.

**Handling:** the later parents (RAD-082, RAD-083) will set `duplicate_of`
pointing at the earlier TC rather than silently emitting a second copy — this is
what the field exists for. Both still get a workbook row, because both leaves
exist in 037 and traceability needs them.

**Open:** RD-1 — are APP17/APP18 redundant restatements to be removed, or was a
distinction intended that the wording lost?

---

## A-023 — APP13 names the wrong container

**Found:** 2026-08-07, generating RAD ch18.

*"APP13) The **Presets Pop Up** will have a 'Done' button and an [X} which both
close the popup and return to the **Presets Pop Up** screen."*

As written the clause is circular — a popup whose Done button closes it and
returns to itself. The page-30 screenshots resolve it: "Done" appears on the
**Edit Presets Pop Up**, and closing it returns to the Presets Pop Up. 037 reads
it that way too — all four `SWE1-MEDIA-RAD-078` leaves say "Edit Presets
Pop-up".

Generation follows 037 and the screenshots (Done/X live on the Edit Presets Pop
Up). Because that is a reading of a self-contradictory clause, RAD-078 will
carry an `assumption` marker naming this anomaly.

**Open:** RD-1 — confirm APP13's first "Presets Pop Up" should read "Edit
Presets Pop Up". Ask together with A-021; both are container-naming defects in
the same section.

---

## A-024 — INT-017-01 is mapped to the wrong section

**Found:** 2026-08-07, generating INT ch21.

`SWE1-MEDIA-INT-017-01` — *"The system shall increase or decrease volume levels
using plus and minus buttons for each volume category."* — carries HMI Source
ID `21.12`. But 21.12 is `SA15`, which says only:

> *"The order of the categories in Volume Adjustments is: Media, Phone Call,
> Phone Ring, Navigation, VR."*

The behaviour the leaf describes is `SA14` at **21.11**:

> *"For Volume Adjustment, press plus / minus buttons to increase / decrease the
> volume level for each category."*

21.11 has no leaf of its own, and 21.12 has two leaves (INT-017, INT-018) of
which only INT-018 ("display the categories in this order") matches SA15.

**Handling:** the TC is written against the behaviour the leaf actually states
(SA14), and `specification_reference` cites **21.11 first, then 21.12**, so the
row traces to the clause that governs it without dropping 037's own mapping.
`generated/SWE1-MEDIA-INT-017.json` carries an `assumption` marker, because
overriding 037's stated HMI Source ID is a judgement, not a transcription.

**Open:** RD-1 / 037 owner — should INT-017-01's HMI Source ID be corrected to
21.11 (SA14)?

---

## A-025 — Nine ch21 sections have no leaf at all, including R1H Virtual Venue

**Found:** 2026-08-07, generating INT ch21.

Unlike A-008 (unallocated *rows* of an allocated table) and A-020 (orphan
sub-sections under an allocated leaf), these are whole clauses that 037 skipped
outright:

| Section | Clause | Content |
|---|---|---|
| 21.8 | `SA9` | Beats Audio — Balance/Fade and Equalizer graphics updated when the vehicle supports it |
| 21.11 | `SA14` | Volume Adjustment plus/minus per category (see A-024 — its content did get a leaf, mis-mapped to 21.12) |
| 21.13 | — | Radio Off with Door |
| 21.14 | `SA19` | **(R1H Only)** Virtual Venue setting: On / Off |
| 21.14.1 | `SA19.1` | Cycling venues with the arrow buttons or tune knob |
| 21.14.1.1 | `SA19.1.1` | Wrapping from the last venue back to Default |
| 21.14.1.2 | `SA19.1.2` | Virtual Venue does not latch over ignition cycles |
| 21.15 | `SA19.2` | Venue name as defined in `Virtual_Venues_Profiles_V1.0` |
| 21.16 | `SA19.3` | Venue info popup as defined in `Virtual_Venues_Profiles_V1.0` |

**The Virtual Venue block is marked *(R1H Only)*, and whether it applies is
NOT yet established.** An earlier draft of this entry asserted the programme is
Atlantis High and cited MN2 plus done-region usage as proof. That reasoning was
wrong and is retracted — see A-026. What the inputs actually show:

- The workbook's vehicle columns (T–Z) cover **both** tiers: `HDCC27` and
  `DT27` marked **Atl-Hi**, and five models (`VF(ProMaster)637`,
  `Commander 598`, `Regengade 5210`, `Toro 2261`, `Fastack 376`) marked
  **Atl-Mi**. All 322 done-region rows set every one of the seven flags to `1`.
- The SYS1 export is `R1L-L` and the CFTS input is `R1LR_Atl-H`, i.e. R1 **Low**
  variants, while `(R1H Only)` names R1 **High**.
- Spec 1.2 says the deck "covers requirements for R1 High and Low radios".

So `(R1H Only)` may apply to a subset of the programme's vehicles, all of them,
or none — this cannot be decided from the inputs. If it applies to only the two
Atl-Hi models, its TCs would also be the first rows in the workbook not to set
all seven vehicle flags to `1`, which no done-region row does.

The other six clauses in the table above carry their own gating, assessed
separately below.

Two of them (`SA19.2`, `SA19.3`) also delegate to an external document,
`Virtual_Venues_Profiles_V1.0`, which is not among the inputs — so even with a
leaf they would need that file.

### Per-clause gating assessment

Reporting all nine as gaps would be wrong — some may be correct
non-configuration rather than omissions. Classified:

| Section | Gating in the spec text | Classification |
|---|---|---|
| 21.11 `SA14` | none | **Not a gap** — its content did get a leaf, mis-mapped to 21.12. See A-024. |
| 21.13 Radio Off with Door | none stated; page 34 shows a full settings screen with On/Off | **Real gap** — no gating, no leaf. |
| 21.8 `SA9` Beats Audio | *"If the vehicle supports Beats Audio"* — an audio-hardware option | **Cannot determine** — nothing in the inputs says whether these seven models carry Beats. Ask. |
| 21.14–21.16 `SA19.x` Virtual Venue | *(R1H Only)* | **Cannot determine** — see the tier question above. Ask. |

Only 21.13 is reported as an unambiguous gap. The rest are questions, so that a
single "that one doesn't apply" answer cannot be used to dismiss the others.

**Open:** RD-1 / 037 owner —
(a) **Radio tier:** which of the seven vehicle models are R1 High and which are
    R1 Low? This decides SA19.x and, more urgently, A-026.
(b) **Virtual Venue:** if any model is R1H, 037 needs leaves for SA19.x, and we
    need `Virtual_Venues_Profiles_V1.0` (not among our inputs).
(c) **Beats Audio:** do any of the seven models support it?
(d) **21.13 Radio Off with Door:** confirmed missing a leaf — should 037 gain one?

---

## A-026 — Tab Button label is tier-dependent, and 76 of 171 generated TCs assume one tier

**Found:** 2026-08-07, while building the evidence chain for A-025 — and it
invalidates the claim that entry originally made.

`4.2 (MN2)` defines the Media Tab Button labels:

> *"Playing" (R1High Only) or "Playing: Source" (R1Low Only)*

The label a tester must press therefore depends on the radio tier. **The
done region uses both forms**, which is how this surfaced:

| Form | Done-region TCs |
|---|---|
| `"Playing"` (R1High) | SWE1-MEDIA-COM-001-05, COM-002-02 |
| `"Playing: <source>"` (R1Low) | SWE1-MEDIA-COM-014-01, COM-032-01 (×3) |

The human-authored reference region is itself inconsistent, so anchoring on it —
which is what generation did — cannot resolve the question, and the sample that
informed the choice happened to contain only the `"Playing"` form.

**Scale: 76 of 171 generated TCs contain the literal `"Playing"` label** in a
step or an expected result. If the programme is R1 Low, every one of those steps
names a button that does not exist on the unit, and the TCs fail on a wording
defect rather than a real one.

Evidence pointing at **R1 Low**: the SYS1 export is `R1L-L`; the CFTS input is
`R1LR_Atl-H`; spec 1.9 lists exclusions specific to `R1L-R`.
Evidence pointing at **mixed**: spec 1.2 covers "R1 High and Low radios"; the
workbook covers Atl-Hi and Atl-Mi models with all vehicle flags set to `1`.

**Status: not yet fixed — awaiting the tier ruling in A-025(a).** Three
outcomes, deliberately not pre-empted:

1. **R1 High** → the generated TCs are correct as written; the two done-region
   `"Playing: <source>"` TCs are the ones that are wrong.
2. **R1 Low** → all 76 TCs need the label changed to `"Playing: <source>"`.
3. **Mixed fleet** → the label cannot be written literally at all. Every
   affected TC needs a tier-neutral formulation, and the workbook's uniform
   all-`1` vehicle flags need revisiting for tier-specific rows.

A mechanical fix is available for outcomes 2 and 3 once the ruling lands (the
label appears in a fixed step-prefix form), so the cost of waiting is low and
the cost of guessing wrong is 76 TCs rewritten twice.

### Tracking — counted by the linter, deliberately not marked

No `assumption` markers are used here. Markers are for precise retrieval of a
handful of TCs; a population this size would drown that signal. Instead the
gate **counts** the two label forms and prints them on every run, following the
A-005 pinning pattern:

```
A-026 tier-dependent tab labels (open ruling, tracked not flagged): playing-r1high=76
```

Retrieval patterns (regex over `test_procedure`, `expected_result`,
`test_item`):

| Form | Pattern |
|---|---|
| R1 High | `"Playing"` |
| R1 Low | `"Playing:[^"]*"` |

Counts are TCs, not occurrences. Baseline as of INT ch21 start: **76 R1High, 0
R1Low** across 171 TCs; update this line at each chapter close.

**Acceptance after the ruling:** one replacement pass, then the counters must be
all-or-nothing — either `playing-r1low=0` (outcome 1, nothing changes) or
`playing-r1high=0` (outcome 2, all switched). A split result means the pass
missed rows. Under outcome 3 both counters go to zero and a tier-neutral
formulation replaces them.

Note that the eight done-region rows carrying a hard-coded label are in the same
position and are not ours to change (rows 10–332 are out of scope, cf. A-005) —
but they should be included in whatever the ruling decides.

**Open:** RD-1 — see A-025(a). This is the highest-impact open question in the
tracker.


---

## A-027 — 22.2.2 has no leaf while its own child does

**Found:** 2026-08-07, generating INT ch22.

- `22.2.2 (AP2.2)` — *"If user listens to iPod and then plugs it in the HU, the
  system will continue playing the item selected **if AutoPlay is ON**."* — no
  leaf.
- `22.2.2.1 (AP2.2.1)` — *"If AutoPlay is OFF when the user selects to start
  playing that device start playing the item the user had playing previous."* —
  **has** a leaf (under a PLA parent).

So the AutoPlay **OFF** branch is covered and the **ON** branch is not, even
though the ON branch is the primary case and its child exists only as its
counterpart. §7's positive/negative pairing has one half missing at the source.

Also without a leaf: `22.2` (a pure reference — *"See Last Mode Table … as well
as AutoPlay Setting - Use Cases"*) and `22.6` (a Use Cases table, image only).
`22.2` carries no testable content of its own; `22.6` may.

Not the A-020 shape: there the orphan asserted something parallel to a sibling
leaf. Here the orphan is the **parent** of a leaf and states the primary branch
of the same rule.

**Open:** RD-1 / 037 owner — should AP2.2 (AutoPlay ON, resume the item that
was playing) gain a leaf? It reads as the main case of the pair whose exception
already has one.
