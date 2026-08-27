# DECISIONS — SW Update (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] ['A', 'B', 'D']
- spec text layer: [AUTO] text-layer: 83356 chars (via pymupdf)
- source files: [AUTO] 8 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 2 checked, 2 PASS, 0 FAIL (measured values in RECON.md)
- spec outline map: [AUTO] 0 cited sections, all found in a 120-entry ruled export; map at data/recon_leaf_to_section.tsv

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 307
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 307 (list in recon.json)
- covered nowhere: [AUTO] 307 = all leaves — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap

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
- batch plan: [PROPOSED: group 307 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:
