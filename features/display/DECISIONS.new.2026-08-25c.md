<!-- R-DM35(b)：本檔為 2026-08-25（12 包）之 recon 產出。19 包步驟 11(b)
     之複驗重跑 recon 時，我**未先依 R-DM35(b) 改名**即讓其覆寫
     `DECISIONS.new.md`；察覺後自 `git show HEAD:` 取回本版保留。
     與新版之唯一差異：`source files` 由 5 present 變為 7 present
     （Pop Up List 兩檔於本輪納入 paths:）。
     此為 R-DM35(b) 之一次違反，已補救；記於上繳包 19 §5.2。 -->

# DECISIONS — Display (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] D
- spec text layer: [AUTO] text-layer: 854333 chars (via pymupdf)
- source files: [AUTO] 5 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 1 checked, 1 PASS, 0 FAIL (measured values in RECON.md)

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 8
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 8 (list in recon.json)
- covered nowhere: [AUTO] 8 = all leaves — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap

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
- batch plan: [PROPOSED: group 8 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:
