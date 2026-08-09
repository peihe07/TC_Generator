# DECISIONS — AMFM (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] D
- spec text layer: [AUTO] no-pdf
- source files: [AUTO] 4 present (SHA256 in RECON.md)

## 2. Workbook survey
- workbook_state: [AUTO] FULL
- form layout revision: [AUTO] A/B (no Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- feature.yaml column letters: [PEI] 1 disagree with the header — update feature.yaml before Phase 4 (see RECON.md)
- done_region.author_value: [PROPOSED: Wilson — feature.yaml value matches 0 rows]
- done segments: [AUTO] 10-167
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單
- done-region compliance notes: [AUTO] 5 recorded (frozen, not fixed) — see RECON.md; register in ANOMALIES if new

## 3. Coverage
- 037 leaves: [AUTO] 102
- requirement-family mismatch: [PEI] the 158 authored rows cover 0 of 102 ruled leaves and trace 57 req_ids absent from the ruled source. Rule their disposition (freeze as legacy / replace / re-map) BEFORE the write-back strategy — it defines what 'done region' and 'completeness' mean here
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 102 (list in recon.json)
- covered nowhere: [AUTO] 102 ['SWE-RA-RAD-001', 'SWE-RA-RAD-002', 'SWE-RA-RAD-003', 'SWE-RA-RAD-004', 'SWE-RA-RAD-005', 'SWE-RA-RAD-006', 'SWE-RA-RAD-007', 'SWE-RA-RAD-008'] … +94 more (full list in data/recon.json) — ANOMALIES entries required
- workbook req_ids absent from 037: [AUTO] done=57 ['SWE-RAD-001', 'SWE-RAD-001-01', 'SWE-RAD-001-02', 'SWE-RAD-001-03'] … +53 more (full list in data/recon.json) draft=0 (none) — ANOMALIES + RD-1 required; scope the write-back traceability invariant to regen rows only

## 4. Style bindings
- style authority: [PROPOSED: the existing rows — they are the workbook's only precedent — but they are NOT the traceability authority; style may be borrowed from rows whose req_ids the ruled source does not contain]
- test item shape: [PROPOSED: follow done-region first-row shape — verify against profile]
- test group/set columns: [PROPOSED: match done-region (blank if blank)]
- exemplar source: [AUTO] own done region
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [PROPOSED: <Spec Filename>_{outline}]

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [PEI — draft with Claude, Tier 2]
- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]

## 7. Execution
- batch plan: [PROPOSED: group 102 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:
