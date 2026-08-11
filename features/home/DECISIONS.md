# DECISIONS — Home (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] A
- spec text layer: [AUTO] text-layer: 30719 chars
- source files: [AUTO] 5 present (SHA256 in RECON.md)

## 2. Workbook survey
- workbook_state: [AUTO] PARTIAL_INTERLEAVED
- form layout revision: [AUTO] A/B (no Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] 10-86, 91-124, 129-161
- ambiguous rows: [AUTO] none
- draft disposition: [PROPOSED: discard & regenerate — lint consistency cheaper than row salvage]
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單
- done-region compliance notes: [AUTO] 27 recorded (frozen, not fixed) — see RECON.md; register in ANOMALIES if new

## 3. Coverage
- 037 leaves: [AUTO] 140
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 62 (list in recon.json)
- covered nowhere: [AUTO] 2 ['SWE1-HMI-HOME-055-03', 'SWE1-HMI-HOME-066'] — ANOMALIES entries required
- parent/child dupes: [PROPOSED: proportion test per case — ['SWE1-HMI-HOME-066']]
- workbook req_ids absent from 037: [AUTO] done=1 ['SWE1-HMI-HOME-035'] draft=0 (none) — ANOMALIES + RD-1 required; scope the write-back traceability invariant to regen rows only

## 4. Style bindings
- style authority: [AUTO] done region
- test item shape: [PROPOSED: follow done-region first-row shape — verify against profile]
- test group/set columns: [PROPOSED: match done-region (blank if blank)]
- exemplar source: [AUTO] own done region
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [PROPOSED: Home Screen HMI Logic and Flow R1 SR24 Post 2A (March 17 2023)_{outline}]

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [PEI — draft with Claude, Tier 2]
- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]

## 7. Execution
- batch plan: [PROPOSED: group 62 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:
