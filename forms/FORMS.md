# FORMS — FW form-revision manifest

Purpose: canonical registry of the FM-WI form layouts (036 workbook and
related) used across features. The xlsx form files in this directory are
NOT committed (same policy as `<Feature>/inputs/`); this manifest IS
committed and records each form revision's structural facts so that:

1. recon can validate a feature workbook's column mapping against a known
   layout instead of re-deriving it from scratch
2. a missing per-feature workbook (cf. AMFM 2026-08) has a structural
   backup even when the pre-filled instance must be re-obtained
3. layout drift between form revisions is detected as a manifest diff

Rules:
- One entry per form revision / layout variant, keyed by filename stem
- SHA256 binds the manifest entry to the exact file placed here
- Column letters are recorded ONLY after verification (recon header match
  or manual probe) — no guessed values; unverified fields stay `TBD`
- Per-feature deviations from a form entry (e.g. remarks column extent)
  are recorded in the entry's Notes, and always re-verified per feature
  in that feature's `feature.yaml`
- The pre-filled workbook delivered per feature stays in
  `<Feature>/inputs/`; this directory holds blank/reference copies only

---

## Form: FM-WI-FSM-036-A01 (Test Case Specification & Result)

The form's own revision letter lives in the `ChangeHistory 修訂履歷` sheet
and the form id in the header row-5 cell at the far right of the data block.
**Two layouts are in circulation**, and the revision letter — not the file
date — tells them apart. Revision C inserted one column mid-table, which
moves five fields; that is why a column map is never reusable unverified.

### Revision C — with Estimated Test Time (the current blank form)

- File: `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
  Specification & Result_SWQT_20260121.xlsx`
- SHA256: `cd876c202c71e74b0eca92dd7b4454af1879ac9a700744d5fe448687f7a9287d`
- Captured: 2026-08-09 (blank form, 3 template rows at 10–12)
- Sheet: **`Test Case Specification 測試用例規範`** — note: NOT the
  `…&Result` name the instances use
- Header row: `9` · data from `10` · columns A–**AH** (34)
- Form-id cell: `AH5` = `FM-WI-FSM-036-A01`
- ChangeHistory: A (2025-10-20) · B (2025-12-08) · **C (2026-01-21)** —
  "新增欄位：預估測試時間(分鐘) / Add new column: Estimated Test Time (mins)"
- Column mapping (probed):

  | Field | Col | | Field | Col |
  |---|---|---|---|---|
  | No.# | B | | **Estimated Test Time** | **Q** |
  | req_id (Polarion) | C | | design_method | R |
  | req_id | D | | functional_safety | S |
  | tc_id (TestRail) | E | | vehicle models ×7 | T–Z |
  | tc_id | F | | author | AA |
  | test_group | G | | test_version | AB |
  | test_set | H | | test_vehicle | AC |
  | test_item | I | | test_period | AD |
  | pre_conditions | J | | tester | AE |
  | input_test_data | K | | test_result | AF |
  | test_procedure | L | | defect_id | AG |
  | expected_result | M | | remarks | AH |
  | spec_reference | N | | | |
  | tc_ref_id | O | | | |
  | priority | P | | | |

- Column B formula: `=IF(ISBLANK($D10),"",ROW()-9)`
- Design method vocabulary: `下拉選單`, 9 exact strings
- `Test Case Framework` sheet: **absent** (9 sheets total)
- Notes: no feature has been generated on this layout yet. A workbook dated
  after 2026-01-21 is NOT necessarily revision C — the AM/FM instance below
  is dated 2026-01-29 and is revision B.

### Revision A/B — no Estimated Test Time (every instance in the repo)

- Reference file: `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test
  Case Specification & Result_SWQT_Home_20260809.xlsx`
- SHA256: `1895fb2a2b44f06c46147e5c24731d2d1adf0f2eea80c7ec6f8900a679f24d72`
- Captured: 2026-08-09 (pre-filled Home instance, 225 rows — see the
  provenance warning below before treating it as a reference)
- Sheet: `Test Case Specification&Result` · header row `9` · A–**AG** (33)
- Form-id cell: `AG5` = `FM-WI-FSM-036-A01`
- Column mapping (verified independently by `recon.py` header-text resolution
  against Home and AM/FM — both resolve to identical letters):

  | Field | Col | | Field | Col |
  |---|---|---|---|---|
  | No.# | B | | design_method | Q |
  | req_id (Polarion) | C | | functional_safety | R |
  | req_id | D | | vehicle models ×7 | S–Y |
  | tc_id (TestRail) | E | | author | Z |
  | tc_id | F | | test_version | AA |
  | test_group | G | | test_vehicle | AB |
  | test_set | H | | test_period | AC |
  | test_item | I | | tester | AD |
  | pre_conditions | J | | test_result | AE |
  | input_test_data | K | | defect_id | AF |
  | test_procedure | L | | remarks | AG |
  | expected_result | M | | | |
  | spec_reference | N | | | |
  | tc_ref_id | O | | | |
  | priority | P | | | |

- Design method vocabulary: `下拉選單`, 9 exact strings (identical to rev C)
- `Test Case Framework` sheet: present, empty (10 sheets total)
- Column B formula: varies by instance — Home `=ROW()-9`,
  AM/FM `=IF(ISBLANK($D10),"",ROW()-9)`. Not a layout discriminator.
- Vehicle model block (both revisions, same 7 in the same order):
  HDCC27 Atl-Hi · DT27 Atl-Hi · VF(ProMaster)637 Atl-Mi · Commander (598)
  Atl-Mi · Regengade (5210) Atl-Mi · Toro(2261) Atl-Mi · Fastack (376) Atl-Mi
- Scope field: header cell found by the label text `範圍 Scope` (`C5`, value
  in the merged `D5:H5`). Hand-maintained upstream and **wrong in both
  instances captured so far** — Home A-H26, AMFM RULINGS C1.
- Notes: Media's remarks column is recorded elsewhere as `AH`. That is one
  column past this layout's last column and has not been re-probed here;
  treat it as unverified until a Media instance is captured.

#### Provenance warning on the Home reference file

This copy is **not** the Home v2 deliverable and must not be submitted as
one. Diffed cell-by-cell against `features/home/output/…_Home_20260720.xlsx`
(SHA256 `cfc007f3…`, tag `fw036-home-regen-v2`), it is the pre-A-H26 build
with four editorial passes applied on top:

| Cell / column | This copy | Home v2 |
|---|---|---|
| `D5` Scope | `…AppDrawer-Projection-SWE1HMI-V0.1` — **uncorrected** | `…Home-HMI-V0.1` |
| `F` Test Case ID | `NR1L-HomeHMI-001…` on all 216 rows | blank |
| `G` Test Group | `CoreHMI` on all 216 rows | blank |
| `K` Input Test Data | `NA` on all 216 rows | blank where generation left it so |
| `Z` Author (done region) | `ArifChen` ×144 | `Arif` ×144 |

Two consequences worth carrying forward:

1. **It carries the defect A-H26 fixed.** Whatever pipeline produced this
   file branched before the Scope correction.
2. **`Z` = `ArifChen` breaks the Home done-region selector.** `feature.yaml`
   sets `done_region.author_value: Arif`; against this file that matches 0
   rows, so `build_remaining.py` and `write_back.py`'s content-hash invariant
   would both mis-select. If this row-author spelling is what upstream
   expects, it is a `feature.yaml` change plus a fresh baseline hash, not a
   silent edit.

Neither is resolved here — the manifest records structure and states what it
found.

### Instance register (pre-filled workbooks, layout confirmed by recon)

| Feature | Instance | Revision | Layout | Author | Rows |
|---|---|---|---|---|---|
| Home | `…_SWQT_Home_20260720.xlsx` | ChangeHistory C (ours) | A/B | `Arif` (done) | 225 |
| AMFM | `…_SWQT_CFTS024_Radio_20260129.xlsx` | ChangeHistory **B** | A/B | `Wilson` | 167 |

AM/FM was expected to need "template adaptation" because its layout differed.
**It does not** — recon's header-text resolution returns the same letters as
Home, D through AG. What differs is content convention, not geometry:
`test_group`/`test_set` are populated (`Radio` / `FM & AM`), `tc_id` carries
`newR1L-Radio-nnn`, `tc_ref_id` reads `New` rather than `NEW`, and
`spec_reference` is `CFTS024-<ReqIF.ForeignID>` rather than a document/section
string. The adaptation that was actually required was in the **037 Analysis
Report**, not the workbook — see below.

---

## Form: FM-WI-FSM-037-A03 / FM-WI-SW-…-SWRA (Analysis Report)

No blank copy captured. Structure recorded from instances because the
positional read that worked for Home returns **zero leaves** on AM/FM, and an
empty leaf list is indistinguishable from a finished feature.

| | Home 037-A03 | AMFM 037-A03 | AMFM SWRA-A02 |
|---|---|---|---|
| Sheet | `Analysis Report` | `Analysis Report` | `Analysis Report` |
| Header row | 7 | 8 | 7 |
| ID column header | `SWE-Requirement ID ` | `SWE-Requirement ID ` | `ID` |
| req family | `SWE1-HMI-HOME-*` | `SWE-RA-RAD-*` | `SWE-RAD-*` |
| Categorization | col 7 | col **31** | absent |
| Categorization values | `Functional Requirement` / `Heading` | `Functional` only | — |
| Source column | `HMI Source ID` (document names) | `Source Requirement ID` (SYSAD components) | `Source Id` + `ReqIF.ForeignID` |
| ASIL / FTTI | absent | **absent** | present (`QM` ×57, FTTI `NA` ×57) |
| Leaves | 140 (+21 headings) | 102 (0 headings) | 57 |

Capture rules this produced, now implemented in `scripts/recon.py`:

- header row = the row containing a `Requirement Description` cell
- `Categorization` located by header text, excluding `Sub Categorization`
- a leaf is any row whose Categorization **starts with** `Functional` —
  `Functional` and `Functional Requirement` are the same classification
  written two ways
- ASIL / FTTI located by header text; their absence in the ruled requirement
  source is the finding that keeps the SYS2/SYSRA safety layer out of the
  trace chain

---

## Capture procedure (when adding a form)

1. Place the blank/reference xlsx in `forms/`
2. Compute SHA256 (`shasum -a 256 <file>`) and record it here
3. Probe sheet name, header row, column headers; fill the mapping table
4. Record design-method dropdown vocabulary source
5. Record the ChangeHistory revision letter — it, not the filename date,
   identifies the layout
6. If the file is a pre-filled instance rather than a blank form, diff it
   against the known-good deliverable and record the provenance
7. Commit the manifest change (xlsx stays untracked)
