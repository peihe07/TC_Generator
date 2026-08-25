# DECISIONS — Vehicle Category (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] A
- spec text layer: [AUTO] text-layer: 18750 chars (via pymupdf)
- source files: [AUTO] 6 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 3 checked, 3 PASS, 0 FAIL (measured values in RECON.md)
- spec outline map: [AUTO] 66 cited sections, all found in a 108-entry ruled export; map at data/recon_leaf_to_section.tsv

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 145
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 145 (list in recon.json)
- covered nowhere: [AUTO] 145 = all leaves — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap
- parent/child dupes: [PROPOSED: proportion test per case — ['SWE1-HMI-VC-001', 'SWE1-HMI-VC-007', 'SWE1-HMI-VC-012', 'SWE1-HMI-VC-013', 'SWE1-HMI-VC-019', 'SWE1-HMI-VC-025', 'SWE1-HMI-VC-026', 'SWE1-HMI-VC-028', 'SWE1-HMI-VC-033', 'SWE1-HMI-VC-034', 'SWE1-HMI-VC-035', 'SWE1-HMI-VC-036', 'SWE1-HMI-VC-037', 'SWE1-HMI-VC-038', 'SWE1-HMI-VC-042', 'SWE1-HMI-VC-046', 'SWE1-HMI-VC-047', 'SWE1-HMI-VC-048', 'SWE1-HMI-VC-051', 'SWE1-HMI-VC-052', 'SWE1-HMI-VC-056', 'SWE1-HMI-VC-058', 'SWE1-HMI-VC-059', 'SWE1-HMI-VC-060', 'SWE1-HMI-VC-062', 'SWE1-HMI-VC-063', 'SWE1-HMI-VC-064', 'SWE1-HMI-VC-065']]

## 4. Style bindings
- style authority: [PROPOSED: fallback chain — no done region]
- test item shape: [PROPOSED: standard §4.3 tc_title]
- test group/set columns: [PROPOSED: FILL per framework Part N]
- exemplar source: [PROPOSED: nearest sibling feature done region, cross-feature: style only]
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [PROPOSED: None]

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [PEI — draft with Claude, Tier 2]
- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]

## 7. Execution
- batch plan: [PROPOSED: group 145 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:
