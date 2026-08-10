# Project Profile — FW036 / R1L SWE1 AMFM (CFTS024 Radio, Stellantis newR1L)

> **PRECEDENCE: this profile OVERRIDES the generic ASPICE SWE.6 instruction
> wherever the two conflict.** Generic rules stay in force for everything this
> profile does not address. Rules tagged **[OVERRIDE]** replace a specific
> generic rule (the replaced rule is cited); rules tagged **[ADD]** are
> project-specific additions.

## 0. Project identity [ADD]

- Program: Stellantis newR1L; scope 037-A03 AMFM (RULINGS R1)
- Deliverable workbook: FM-WI-FSM-036-A01 (`SWQT_CFTS024_Radio_20260129`)
- Requirement IDs: `SWE-RA-RAD-NNN` from the 037-A03 — never invented,
  never renumbered. Numbering gaps 086/088 belong to the 037 (A-AM08).
- Author on new rows: `PeiPYHsu`. Authorship principle (R3): rows Pei
  generates carry `PeiPYHsu`; rows fully quoted from another author keep
  that author's name.
- **Legacy region (NOT a done region)**: 158 rows by `Wilson`, tracing the
  superseded `SWE-RAD-*` family (SWRA-A02). FROZEN per R4 (option i):
  byte-for-byte preserved, excluded from coverage and traceability
  invariants, style-borrowable, traceability-orphaned. The write-back
  traceability invariant (`assert_traceable_and_complete`) is scoped to
  regen rows only — the 102-leaf equality check ignores legacy rows.

## 1. Requirements authority chain [ADD]

- Chain: CFTS clause (STLA id) → SYS3 SYSAD components → 037-A03 leaf →
  FW036 TC. spec_mode D: no SYS1/Polarion export; the 037 Requirement Title
  quotes the CFTS clause text verbatim (with trailing `(stla_id)`), and the
  CFTS docx is the spec source for context, figures, and tables.
- Spec sources are MULTIPLE by design (R7-Q3):
  - CFTS024 (in `inputs/`) — 85 leaves (001–085)
  - CFTS011 (external, to be supplied by Pei when needed — A-AM06) —
    9 leaves (087, 089–096, Engineering Mode)
  - CFTS004 General Diagnostic Requirements (external, attribution
    ASSUMED until file confirms — A-AM07) — 8 leaves (097–104, DIDs)
- On 037-title ↔ CFTS-docx wording conflict: source spec wins (§8.6);
  flag the delta in ANOMALIES.md.
- SYS2/SYSRA safety layer does NOT enter the trace chain (DECISIONS §3,
  signed R6): the 037-A03 carries no ASIL/FTTI column.
- SWRA-A02 is NOT a requirement source (R1); its 57 rows have no coverage
  claim here (R5).

## 2. Test Set vocabulary [OVERRIDE — replaces done-region Test Set style]

- New rows write Test Group = `AMFM` (column G) and the capability Test Set
  (column H) from framework.md Part III (R7-Q1/Q2). This deliberately
  diverges from the legacy rows' `Radio` + band scheme (`FM`/`AM`/`USB`):
  the legacy scheme cannot carry the capability structure because most
  leaves apply to both bands. Legacy rows keep their own values, frozen.
- `fill_test_group_set: true` in feature.yaml — the workbook convention is
  filled columns (unlike Home).
- The workbook `Test Case Framework` sheet stays EMPTY (Wilson convention;
  framework Part III workbook-sync note).

## 3. FW036 AMFM house style (field rules)

### 3.1 Test Item [OVERRIDE — replaces §4.3 tc_title-only cell content]

- Legacy precedent (borrowable): Test Item cell carries the requirement's
  shall-sentence, or a scenario tag for siblings (e.g.
  `Browse Presets – Station name (Strength Signal)`).
- New rows: Test Item = condensed requirement statement in spec language
  (modals permitted HERE ONLY, quoting requirement text), same as the Home
  §3.1 override. The generic §4.3 tc_title (no modals) is still produced in
  output JSON for lint/sibling-distinction. Multiple TCs per leaf append
  the distinguishing scenario tag.
- §6 unchanged for ER: no modal verbs, ever.

### 3.2 Pre-Conditions [ADD — AMFM applicability triggers]

Valid spec-trigger Pre-Conditions (§8.5 exception) include:
- Configuration gates: `$AM_Presence$ = Present` / `Absent` (001/002
  family), `$ANT_TYP$` values (066), market/`$Country_Code$` configuration
  (081–085), dual-tuner vs single-tuner equipment (064/066)
- Source state: `HU Tuner source is selected on the Cabin Output Channel`
  (the CFTS's standing trigger phrase)
- Band state: `HU is in FM analog tuner mode` / `AM analog tuner mode`
  when the leaf scopes to a band
- Engineering Mode / Dealer Mode entry state for 087–096 ONLY if the spec
  defines it as the display's trigger (verify against CFTS011 when
  supplied; until then mark `[ASSUMPTION A-AM07]` where relied on)
- `HU is powered on` remains banned (generic rule)

### 3.3 Design Method [OVERRIDE — restricts §12 output strings]

Return exactly one of the 9 dropdown strings from the workbook 下拉選單
sheet, character-for-character. §12 mapping logic unchanged. Legacy region
is 89% Functional + BVA + Scenario — do not force-match; assign per §12
truthfully.
- **Config-gate rule (R10-1)**: leaves that pairwise/groupwise cover a
  configuration parameter's value classes (e.g. `$AM_Presence$`
  Present/Absent, `$ANT_TYP$`, dual/single tuner, market destination
  codes) are Equivalence Partitioning on every side of the partition, not
  Functional.

### 3.4 Signal / CAN citations [ADD]

- CFTS `$SIGNAL$ = [value]` notation is quoted verbatim in Pre-Condition /
  Input Test Data (e.g. `$ICS_KNOB2_DIR$ = [Increment]`) — the profile-
  scoped §11 exception for source-quoted tokens applies (square brackets
  retained inside quoted signal values only; author prose still uses
  `"..."` for UI labels).
- DID requirements (097–104) name the DID and the commanded/reported value
  from the 037 title text; do not invent DID numbers absent from the
  source (§8.4.1).

### 3.5 Spec Reference [OVERRIDE — replaces §10.7 filename format]

Format: `{doc}-{stla_id}` where `{doc}` ∈ `CFTS024` / `CFTS011` /
`CFTS004` for owning documents, plus `CFTS019` / `CFTS028` as cited-only
documents (see cross-document citations below), and `{stla_id}` is the 7-digit id taken from the
leaf's 037 Requirement Title tail — never constructed by guess (R7-Q3;
legacy precedent `CFTS024-4872420` confirms the shape).
- 001–085 → `CFTS024-{id}`; **exception: leaf 029 → `CFTS024-4872457`**
  (R9 — the 037's declared id tail is a copy error; override entry in
  `build_stla_map.py`)
- 087, 089–096 → `CFTS011-{id}` (attribution confirmed by supplied file —
  A-AM06 resolved: CFTS011 = Radio Engineering Mode, all declared ids
  verified present)
- 097–104 → `CFTS004-{id}` (attribution CONFIRMED 2026-08-10, all 8 ids
  verified in the supplied CFTS004 — the `[ASSUMPTION A-AM07]` marker is
  NO LONGER required)
- A leaf title lacking a parseable id → ANOMALIES entry + reference
  pending; never guess.

**Absorbed clauses** (R10-2) are same-document: the absorbed clause's own
7-digit anchor is appended as a second `CFTS024-{id}` token.

**Cross-document citations** are NOT the same case (A-AM15). Where a leaf's
clause delegates behaviour to another document, CFTS024 writes a
**short-id** token — `{See CFTS019-718}` in §1.3.3 (leaf 014),
`{See CFTS028-1}` in §1.3.4–1.3.6, and the same form when it cites itself
(`{See CFTS024-605}`). These short ids exist in **no supplied document**,
CFTS024's own anchors included, so they are a foreign numbering, not STLA
anchors.
**Handling is CITE-FORM, not absorption (R11)**:
- **Cite the token verbatim**, exactly as the source writes it — never
  renumbered, never converted to a 7-digit anchor, never dropped. It is a
  quotation of the spec, so it is not a guess. `specification_reference` =
  the leaf's own clause first, then the cross-doc token
  (`CFTS024-4872420; CFTS019-718`).
- **ER asserts the borrowed outcome, anchored to the citation**: `the key
  press rejection tone is played, as defined by CFTS019-718`. Unanchored
  assertion is forbidden — it reads as this leaf's own verified behaviour.
- **The cited document's rule surface is out of scope**: which conditions
  qualify, the specification of the behaviour itself. That belongs to that
  document's delivery. Verify only that the outcome occurs in the citing
  clause's scenario.
- Cite-form claims **no coverage** of the cited requirement, so it takes no
  `[A-AM10]` marker and does not enter the R10-2a absorption gate — that
  gate is for same-document absorbed clauses only.
- `data/cross_doc_citations.json` (from `build_stla_map.py`) carries every
  token, the leaves it reaches, and ranked candidate clauses where the
  cited document is in `inputs/`; `make_batch_context.py` attaches it to
  the leaf as `cross_references`.
- `CFTS019` / `CFTS028` therefore appear only as cited documents, never as
  a leaf's primary owner.

### 3.6 Remarks [ADD]

Empty string unless: BLOCKED row (none expected — no leaf is blocked),
anomaly flag (A-AM08 duplicate-pair marks), or documented workaround.
- **External language only (R10-4)**: a signed upstream-correction note
  may enter Remarks, phrased for external readers with source anchors
  (document + clause id), never internal ruling/anomaly ids. Template:
  `Requirement source id corrected: 037-A03 declares (…); the requirement
  text is CFTS024 clause …. Reported upstream.` Internal ids stay in
  ANOMALIES/RULINGS.

## 4. Split policy [ADD]

- `standard` split mode. Primary split axes for this feature (§8.3):
  band (AM vs FM where behavior is per-band), input path (HU HMI vs
  Steering Wheel vs ICS knob — the CFTS names them explicitly), boundary
  (station list max 50 / 120 s update / frequency wrap-around), negative
  (recall failure 073, absent presence 002).
- **VR Command trigger path is OUT OF SCOPE (R8)**: leaves 003/009/025/027
  test the HU HMI main path only; the CFTS "or a VR Command" alternative
  belongs to the CFTS028 delivery. Note the delegation in reasoning; do
  not add a VR procedure path or a VR split axis.
- **Unallocated-clause absorption (R10-2, A-AM10)**: a CFTS clause the 037
  allocated to no leaf is absorbed into a leaf's TC set iff it is (a) in
  the same spec section and (b) elaborates the leaf's cited clause. On
  absorption: `[A-AM10]` marker in assumptions AND the absorbed clause id
  added to `specification_reference` (multi-cite, §10.7). Anything failing
  the test → coverage hole in reasoning + RD-1; never silently absorbed.
- **Suppression TC rule (R10-3)**: an "only if X" execution condition with
  reachable ¬X yields an independent suppression TC (own trigger state,
  own setup; Decision Table method typical). Never folded into the main
  TC as an extra ER.
- Wrap-around behaviors (seek/tune at band edge) are boundary TCs, not
  separate features.
- 037 duplicates (A-AM08 pairs) are NOT consolidated (§8.2, R7-Q4): each
  leaf gets its own TC; `duplicate_of` / `distinguishing_axis` must state
  the relation; Pei rules per pair at review.

## 5. AMFM step-writing conventions [ADD]

- Band/source entry: `Select "FM" source on the HU` / `Select "AM" source
  on the HU` (or the CFTS Source Select phrasing once verified in figures).
- Hard controls named as the CFTS names them: `Steering Wheel Buttons`,
  `ICS tune rotary knob`; signal-level alternatives use the two-line `$`
  command format (§5.4) on bench profiles.
- Timing verifications (120 s station list, 1 s sampling) state the
  spec-sourced concrete value (§8.7.1) and the measurement method in the
  step, never `quickly` / `in time`.

## 6. Known anomalies register [ADD]

A-AM01 stale Scope field (resolved — write-back config); A-AM02 legacy
region covers 0/102 (resolved — R4 freeze); A-AM03 family-overlap evidence
(resolved — consumed by R4); A-AM04 18 SWRA-A02 rows unrepresented
(resolved-conditional — R5 + RD-1); A-AM05 feature.yaml priors (resolved —
R3); A-AM06 CFTS011 not in inputs; A-AM07 CFTS004 attribution assumed;
A-AM08 037-internal duplicate STLA ids + numbering gaps.
Details and dispositions live in `AMFMHMI/ANOMALIES.md`.
