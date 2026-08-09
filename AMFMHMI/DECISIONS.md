# DECISIONS — AMFM (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] D
- spec text layer: [AUTO] no-pdf
- source files: [AUTO] 5 present (SHA256 in RECON.md)

## 2. Workbook survey
- workbook_state: [AUTO] FULL
- form layout revision: [AUTO] A/B (no Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- feature.yaml column letters: [SIGNED R3] remarks AH → AG applied to feature.yaml 2026-08-09
- done_region.author_value: [SIGNED R3/R4: Wilson — selects the frozen legacy region, not a protected done region; rows fully quoted from others keep their author's name]
- done segments: [AUTO] 10-167
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單
- done-region compliance notes: [AUTO] 5 recorded (frozen, not fixed) — see RECON.md; register in ANOMALIES if new

## 3. Coverage
- 037 leaves: [AUTO] 102
- requirement-family mismatch: [SIGNED R4: 選項 (i) — 158 rows frozen as legacy region, excluded from coverage/traceability invariants; RD-1 attached (docs/fw036/RD1_questions_amfm.md); C3a per R5 — the 18 unrepresented SWRA-A02 rows are not covered by this workbook]
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
- Test Set table (Part N): [SIGNED R7 — framework.md Part III, 11 capability Test Sets, 102/102 allocated; Test Group = AMFM]
- profile [OVERRIDE] clauses: [SIGNED R7 — FW036_R1L_AMFM_Profile.md: §2 Test Set/Group divergence from legacy, §3.1 Test Item requirement-statement form, §3.3 dropdown strings, §3.5 spec_reference {doc}-{stla_id}]

## 7. Execution
- batch plan: [PROPOSED: group 102 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: PeiPYHsu  Date: 2026-08-09
- Overridden items: §2 feature.yaml letters (remarks→AG), §2 author_value
  (→Wilson), §3 requirement-family mismatch (→R4 選項 i)
- Ruling notes: rulings recorded verbatim in RULINGS.md R3–R6; all other
  [PROPOSED] items signed as proposed (R6). §6 framework/profile remain
  open — Phase 3 Tier 2 items, not part of this sign-off.
