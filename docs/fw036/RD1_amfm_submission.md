# RD-1 — AMFM (FW036 CFTS024_Radio) — Submission Draft v1

- Workbook: `FM-WI-FSM-036-A01 …_SWQT_CFTS024_Radio` (regen v1)
- Requirement basis: `SWE1_AMFM_FM-WI-FSM-037-A03 … SWRA_20260323` (102 leaves)
- Prepared: 2026-08-10 (analysis layer). Sending is Tier 3 (Pei).
- Ordering per FEATURE_ONBOARDING §7: systemic classes first; every item
  carries anomaly id, one-line evidence, the disposition already taken
  locally, and the requested upstream action. No item blocks delivery —
  dispositions are designed so a contrary answer changes strings, not
  content.

---

## 1. Systemic defects (class-level remedies requested)

### S1 — Cross-reference short-id scheme resolves nowhere [A-AM15 / R11]
- Evidence: CFTS024 carries 37 `{See CFTS0xx-nnn}` tokens — including
  citations of itself (`CFTS024-605`, `-707`, `-789`) — in a short-id scheme
  that no released file uses; CFTS019's clauses are 7-digit and `718` appears
  neither in its text nor in any of its 37 tables. The SXM corpus hits the
  same class (`CFTS024-193/195/197`, `CFTS019-494/496`, `CFTS020-138`;
  A-SX02), so this is a document-family property, not a one-off.
- Disposition taken: cite-form (ruling R11) — the borrowed outcome is
  asserted in the ER anchored to the verbatim token; the cited document's own
  rule surface is not tested; the token is carried as an additional
  specification reference.
- Requested action (class remedy): publish the short-id ↔ current-anchor
  mapping, or re-issue cross-references in the 7-digit anchor scheme. Either
  answer upgrades our citations mechanically.

### S2 — Version labels do not identify content [A-SX06; merged AMFM + SXM]
- Evidence: `SR24 R1 Market Configuration Table v1.6.xlsx` is byte-different
  in all four releases (4 distinct SHA256) under one unchanged label;
  `CIP_Radio_Tables_v6.7.xlsx` likewise differs across releases (Default ROW
  Market Presets, Weather Icons); `SYS3_SXM_…SYSAD` has three files on one
  document line with three hashes. Three instances make it a class.
- Disposition taken: every reference workbook is release-pinned and
  hash-recorded at intake; cross-feature copies are hash-verified on both
  sides.
- Requested action: version by content — change the label whenever the
  content changes, or publish per-release digests.

### S3 — 037 Requirement Titles drop clause text, one-directionally [A-AM09]
- Evidence: 20 of the 85 in-corpus leaf titles diverge from the CFTS024
  clause they cite, and in every case the clause says more: VR-trigger
  wording (4 leaves), pointers to companion documents (~9), substantive
  caveats (~6). Measured per leaf at context build (`wording_agreement`).
- Disposition taken: TCs are generated from the clause text (source spec
  wins); the VR trigger path is ruled out of this workbook's scope (R8) and
  delegated to the CFTS028 delivery, matching the 037's own systematic
  omission of VR wording.
- Requested action (class remedy): regenerate titles from clause text at the
  next 037 revision, or state that titles are non-normative summaries.
  Per-title patches would leave the next omission undetected.

---

## 2. Requirement-set questions and corrections

### Q-AM1 — SWRA-A02 ↔ 037-A03 lineage [A-AM03 / A-AM04; rulings R4/R5]
- Evidence: the workbook's 158 pre-existing rows trace the `SWE-RAD-*` family
  (SWRA-A02, 57 leaves, all ASIL QM / FTTI NA). Against the 037-A03: 35
  leaves carry near-verbatim SWRA-A02 descriptions (1:1), 61 have no
  ancestor, 18 SWRA-A02 rows are represented nowhere — and the drop is a
  contiguous tail (`SWE-RAD-040`…`-045` + the `SWE-RAD-001` sub-items), which
  reads like an earlier-revision basis or a deferred block, not 18 deletions.
- Disposition taken: 158 rows frozen as a legacy region (R4), excluded from
  the 037 coverage claim; the 18 rows' coverage is not carried by this
  workbook (R5); no ASIL-rated requirement is dropped (all QM).
- Questions:
  1. Was the 037-A03 authored against an earlier SWRA-A02 revision?
  2. Is the tail `SWE-RAD-040`…`-045` (and the `SWE-RAD-001` sub-items)
     deferred or deleted?
  3. Is FM-WI-SW-RAD-SWRA-A02 formally superseded as this workbook's
     requirement basis? (The delivered form's Scope field named it; corrected
     to the 037-A03 at write-back.)

### Q-AM2 — 037-A03 internal defects [A-AM08 / R9 / R12]
- Evidence: mechanical id-vs-clause verification over all leaves
  (`verify_ids`).
- Items:
  1. **Correction requested** — `SWE-RA-RAD-029`'s title is the verbatim body
     of clause **4872457** (Tune by Direct Number Input, §1.3.6; agreement
     0.909) but its declared id tail reads `(4872451)` (ICS tune-down, owned
     by 028; agreement 0.036). Please correct the id tail. TC side already
     cites 4872457 (R9).
  2. Numbering gaps `SWE-RA-RAD-086`, `-088` — deleted or misnumbered?
  3. For awareness (no correction requested; handled per-pair at review):
     087/094 share id 4942534, 089/095 share 4942540 (untagged vs
     `(Engineering Mode)` variants); 090/096 near-identical text, distinct
     ids; 015's clause is a near-subset of 014's first sentence (distinct
     verification targets carved on the TC side, R12-1).
  4. `SWE-RA-RAD-019`'s source clause `4872426` is an
     `[Artifact Type: Description]` item used as a requirement carrier.
     Generated against it per the leaf's own citation (R12-2); please confirm
     Description-type carriers are intended, or reissue as SFRs.

### Q-AM3 — CFTS clauses allocated to no leaf: allocation policy [A-AM10 / A-AM13 / A-AM14; ruling R10-2]
- Evidence: **95 unallocated clauses (91 SFR, 4 Description) across the 20
  CFTS024 sections the 037 uses** — full list with scope tags and text in the
  attachment (`unallocated_clauses.json` rendering). The distribution is not
  uniform (§1.3.1/§1.3.2 Seek carry 23 against 11 claimed; §1.3.12 carries
  0), so this is asked as an allocation-policy question, not asserted as a
  systematic omission.
- Disposition taken: where an unallocated clause elaborates an allocated
  leaf's cited clause in the same section, its behaviour is absorbed into
  that leaf's TCs, marked and multi-cited (R10-2), so specified behaviour is
  not left untested. Clauses failing that test are recorded as coverage
  holes, two of which are itemized below.
- Questions:
  1. Please confirm the absorption reading, or allocate these clauses to
     leaves explicitly in the next 037 revision.
  2. If any unallocated clause is intentionally out of scope, please state so
     — the TC side will retract the corresponding coverage.
  3. **Fast seek** [A-AM13]: `4872398` (Seek Up) and `4872416` (Seek Down)
     define a long-press continuous-advance feature reaching no leaf and
     failing the absorption test (different trigger, different behaviour).
     The companion `SEEK Cancel_Stop Transitions` worksheet carries matching
     `Fast SEEK` state rows, so the feature is real. Should fast seek have
     leaves — and is the 500 ms `<Tpress>` threshold, stated only in
     `4872416`, meant to apply in both directions?
  4. **Direction asymmetry** [A-AM14]: Seek Up has a dedicated initiation
     leaf (004, `4872384`); Seek Down's equivalents `4872402`/`4872403` are
     unallocated (absorbed into 009). Same policy question as above.

---

## 3. Wording / definition confirmations (answer changes strings, not content)

- **W1** [A-AM11]: `4872442`/`4872451` require tune stepping "based on the
  rate received in the $ICS_KNOB2_VAL$ signal value" [1..63] but define no
  rate→frequency-step mapping. Disposition: ERs assert the monotonic relation
  (63 moves further than 1); no step count fabricated. Requested: a testable
  mapping if one exists, else confirmation that the monotonic check is the
  intended verification depth.
- **W2** [A-AM12]: `4872459` requires "intelligent" direct-entry behaviour
  based on market configuration and tuner mode, defining neither the band
  plans' constraint semantics nor "intelligent". Disposition: TCs are
  parameterized on the held market configuration; nothing invented.
  Requested: definition or confirmation.
- **W3** [A-AM07 residual]: SYS3 cites CFTS004 at `26PI1.5 Mar Release
  20260310`; the supplied file is `25PI3.5 SR26 20250909`. All 8 declared ids
  are present in the supplied file (4939808/09/22/46/49, 4940333/34/37).
  Requested: confirm no clause-level delta for these ids between the two
  releases, else supply the Mar release.

---

## 4. FYI — no action requested

- **F1**: the 158 `SWE-RAD-*` legacy rows remain in the workbook, frozen and
  attributed to their author; they are excluded from the 037-A03 coverage
  claim pending the Q-AM1 answer.
- **F2**: TCs carrying absorbed (R10-2) or cited (R11) clauses list every
  supporting id in their Specification Reference column (multi-cite) — for
  reviewer orientation, not a defect report.
- **F3**: CFTS024 states requirements in both the analog (§1.3.x) and
  satellite (§1.5.x) chapters under distinct ids. A full-corpus sweep finds
  **11 twin pairs at ≥0.95 similarity — 9 word-for-word identical, 2
  differing only in band vocabulary** (e.g. "Tuner" → "Satellite Audio").
  Each deliverable covers its own chapter's clause. Noted because an
  amendment to one chapter silently leaves its twin stale; the per-pair list
  accompanies the SXM delivery (twin-list attachment).

---

Attachments: `unallocated_clauses.json` rendering (Q-AM3);
`stla_id_suspects.json` extract (Q-AM2 item 1); family-overlap table
(Q-AM1); version/hash table (S2).
