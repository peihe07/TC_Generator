# DECISIONS — Privacy (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] D
- spec text layer: [AUTO] no-pdf
- source files: [AUTO] 3 present (SHA256 in RECON.md)

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- feature.yaml column letters: [PEI] 3 disagree with the header — update feature.yaml before Phase 4 (see RECON.md)
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- draft disposition: [PROPOSED: discard & regenerate — lint consistency cheaper than row salvage]
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 10
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 10 (list in recon.json)
- covered nowhere: [AUTO] 10 ['SWE1-HMI-PRIVACY_FEATURES-001', 'SWE1-HMI-PRIVACY_FEATURES-002', 'SWE1-HMI-PRIVACY_FEATURES-003', 'SWE1-HMI-PRIVACY_FEATURES-004', 'SWE1-HMI-PRIVACY_FEATURES-005', 'SWE1-HMI-PRIVACY_FEATURES-006', 'SWE1-HMI-PRIVACY_FEATURES-007', 'SWE1-HMI-PRIVACY_FEATURES-008'] … +2 more (full list in data/recon.json) — ANOMALIES entries required
- workbook req_ids absent from 037: [AUTO] done=0 (none) draft=1 ['xxx'] — ANOMALIES + RD-1 required; scope the write-back traceability invariant to regen rows only

## 4. Style bindings
- style authority: [PROPOSED: fallback chain — no done region]
- test item shape: [PROPOSED: standard §4.3 tc_title]
- test group/set columns: [PROPOSED: FILL per framework Part N]
- exemplar source: [PROPOSED: nearest sibling feature done region, cross-feature: style only]
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [PROPOSED: <Spec Filename>_{outline}]

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [PEI — draft with Claude, Tier 2]
- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]

## 7. Execution
- batch plan: [PROPOSED: group 10 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:
