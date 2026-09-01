# DECISIONS — Vehicle Setup Management R1 Low (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] D
- spec text layer: [AUTO] no-pdf
- source files: [AUTO] 11 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 0 checked, 0 PASS, 0 FAIL (measured values in RECON.md)

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 68
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 68 (list in recon.json)
- covered nowhere: [AUTO] 68 = all leaves — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap

## 4. Style bindings
- style authority: [PROPOSED: fallback chain — no done region]
- test item shape: [PROPOSED: standard §4.3 tc_title]
- test group/set columns: [PROPOSED: FILL per framework Part N]
- exemplar source: [PROPOSED: nearest sibling feature done region, cross-feature: style only]
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [PROPOSED: None]
- tc_id scheme: [RULED] NR1L-VSM42-{n:03d} — frozen per this feature's RULINGS.md, not open at sign-off

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [PEI — draft with Claude, Tier 2]
- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]

## 7. Execution
- batch plan: [PROPOSED: group 68 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:

---

## 執行層附註（下放包 02 W-3，2026-09-01）

- 本檔為 `recon.py` 之預填本，取代原 `new_feature.py` 空白模板（該模板無任何人為編輯，
  故取代不損失簽核痕跡）。**未簽**。
- `037 leaves: [AUTO] 68` 為 recon 代表檔（`a03_report` = Park Sense）之數，
  **非本線母體**。母體依 R-VL4 為兩份 037 之 Functional leaf 合計 **128**
  （68 ＋ 60，Source ID 去重 128，兩檔無交集），全集見 `data/leaves.tsv`（152 列 =
  128 leaf ＋ 23 Heading ＋ 1 UNCATEGORIZED）。簽核前請以 128 為準。
- `column mapping: [AUTO] 15 fields` 係 recon 依表頭文字解析所得；本包依 R-VL8(b)
  自 `sandbox/base` 副本 r9 **逐欄實測**後回填 `feature.yaml`，計 columns 21 鍵
  ＋ variant_columns 7 ＋ execution_columns 5。
