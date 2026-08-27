# DECISIONS — Popup (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] A+C
- spec text layer: [AUTO] scanned (OCR path) — 0 chars via pymupdf
- source files: [AUTO] 4 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 4 checked, 4 PASS, 0 FAIL (measured values in RECON.md)
- spec outline map: [AUTO] 1 cited sections, all found in a 167-entry ruled export; map at data/recon_leaf_to_section.tsv

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 5
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 5 (list in recon.json)
- covered nowhere: [AUTO] 5 = all leaves — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap

## 4. Style bindings
- style authority: [PROPOSED: fallback chain — no done region]
- test item shape: [PROPOSED: standard §4.3 tc_title]
- test group/set columns: [PROPOSED: FILL per framework Part N]
- exemplar source: [PROPOSED: nearest sibling feature done region, cross-feature: style only]
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [PROPOSED: SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_{outline}] (refined by R-POP8: -002-02-derived TCs list both _5.5 and _5.6, ascending; others single _5.6)

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [PEI 2026-08-27] Test Group `Popup`; single Test Set `Pop-up Close` (R-POP4). Framework at features/popup/framework.md, LOCKED, R-G10 remainder check green (5/5 leaf, 2/2 Heading). Layer 3 = PC1, not exported.
- profile [OVERRIDE] clauses: [PEI 2026-08-27] profile created at docs/runtime/profiles/FW036_R1L_Popup_Profile.md. One [OVERRIDE §12 — output strings] (9 dropdown strings, Home §3.3 precedent); rest [ADD]: Pop Up List citation rules incl. IN §11 notation exception (R-POP6, Home A-H10 precedent), authority chain, spec_reference clarification (no §10.7 override; R-POP8 two-line for -002-02).

## 7. Execution
- batch plan: [PROPOSED: group 5 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: PeiPYHsu  Date: 2026-08-27
- Overridden items: none — 8 `[PROPOSED]` left untouched, binding as proposed
  (§4 spec_reference reads with the R-POP8 refinement annotated in place).
- Ruling notes:
  - §6 兩筆 `[PEI 2026-08-27]` 由 Pei 回填：Test Set table 引 R-POP4 ＋
    `features/popup/framework.md` LOCKED；profile 新建於
    `docs/runtime/profiles/FW036_R1L_Popup_Profile.md`（執行層實測 3,813 B）。
  - **本簽署由執行層轉錄，`Reviewed by` 與 `Date` 之值由 Pei 指定**
    （2026-08-27 指示逐字：「你只需填 Sign-off 之 Reviewed by 與 Date」）。
    形制沿 comfort `DECISIONS.md` §12 §5.4 之轉錄前例。
  - P2 於此成立；下放包 02 §六-0 之前置達成。
