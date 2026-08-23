# DECISIONS — Power Moding (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] A+B
- spec 基線分工: [RULED §9.1 通則 3] 判讀基準 = `spec_pdf`（內文面）；追溯用 = `sys1_export`（結構面，`{outline}` 之唯一來源）。已知例外四項見 `feature.yaml` `spec_baseline.known_exceptions`
- 指名複核項: [RULED A-PMH03] outline `7.1` 之 5 個 leaf（`pdf_page` 皆 p8）於 Phase 4 逐一以 PDF 原文複核語句順序 —— export 該節相對 PDF 為重排，被移位改寫者為動畫／splash 之時序
- spec text layer: [AUTO] text-layer: 15618 chars (via pymupdf)
- source files: [AUTO] 5 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 1 checked, 1 PASS, 0 FAIL (measured values in RECON.md)
- spec outline map: [AUTO] 29 cited sections, all found in a 52-entry ruled export; map at data/recon_leaf_to_section.tsv

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields + estimated_test_time = 16，與 `feature.yaml` 零衝突（R-PMH9 之四方交叉佐證另證 34/34 逐欄相等）
- 前言三欄: [RULED R-PMH10] `D3`／`D4`／`D5` 一律留空（語料 5/5 皆空）；`write_back.keep_blank` 已設
- DV 全量: [AUTO 03 包步驟 2] legacy 3 組（`P10:Q1411` = `"P0,P1,P2,P3"`／`T10:Z1411` = `"0,1"`／`AF10:AF1411` = `"Pass, Fail, Pending,Block,NA"`）＋ x14 1 組（`R10:R1411` → `下拉選單!$A$1:$A$9`）。四份已交付件之逸出 **0**
- 寫回機制: [RULED R-G3／R-G1 註] x14 DV 存在 —— **不得 `openpyxl` + `save()`**，一律走 `xlsx_surgical` splice
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 48
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 48 (list in recon.json)
- covered nowhere: [AUTO] 48 = all leaves — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap

## 4. Style bindings
- style authority: [PROPOSED: fallback chain — no done region]
- test item shape: [PROPOSED: standard §4.3 tc_title]
- Test Group（G）欄: [RULED R-PMH13，Pei 2026-08-23 核可] 一律填 `Disclaimer screen`（交付夾名，**小寫 s**，R-PMH18）。依據為四份已交付件 4/4 皆填交付夾名；R-PMH2 之後半已撤回
- Test Set（H）欄: [PEI — Phase 3] R-PMH6 之延後**不受 R-PMH13 核可影響**，仍待 framework Layer 2 定版
- tc_id_format: [RULED R-PMH16，Pei 2026-08-23 裁（乙）] `NR1L-DisclaimerScreen-{NNN}`（**大寫 S**，R-PMH18）。已知反例 Comfort `ComfortHMI` 隨條保留；本條為本 feature 之裁定，**不主張為全案慣例**
- exemplar source: [PROPOSED: nearest sibling feature done region, cross-feature: style only]
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [AUTO 已驗] `Power Moding HMI Logic and Flow R1 SR24 2A_{outline}` —— 與 037 `HMI Source ID`、SYS1 `SYSRE_HMI_Source ID` 三方同構，非構造而是複現
- 字面常數保真: [RULED R-PMH18] `Disclaimer screen`（G 欄）與 `DisclaimerScreen`（tc_id abbr）**刻意不同，不得統一**；一切比對與 lint 須大小寫敏感

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [PEI — draft with Claude, Tier 2]
- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]

## 7. Execution
- batch plan: [PROPOSED: 依 spec 章節分組，pilot 取最小之完整章節] leaf 之章分布 7(19)／8(6)／9(5)／10(10)／11(5)／12(3)；PDF 頁分布 p8(25)／p9(5)／p10(15)／p11(3)
- BLOCKED batches at start: [AUTO] **0** —— 29/29 章節於 SYS1 命中、48/48 leaf 之 `pdf_page` 已解、無 DR-PMH 待答

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:

---

## 附註 —— 本檔之產生方式

recon.py 於 2026-08-23 產出 `DECISIONS.new.md`（A-TM15 之防護：不覆寫既有檔）。
原 `DECISIONS.md` 為 scaffold 模板，**全部欄位皆為未填之 placeholder，
無任何人工內容**，故本次合併為「以 recon 產出為底，逐項補上 recon 不讀之
`RULINGS.md` 既裁條文」，未丟棄任何既有內容。`DECISIONS.new.md` 已刪除。

標為 `[RULED …]` 者為已裁條文之落地，**不是 recon 之提案**，簽核時不得
視為可逕改之 `[PROPOSED]`。
