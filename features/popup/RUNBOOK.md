# FW036 Popup HMI — TC Generation Runbook

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to Popup.

## Phase 0 — Intake（完，上繳包 01）
- [x] Source files —— **不落 `inputs/`**：R-G27 之 `sources/raw/<doc_id>/`
      為原檔落點，本 feature `inputs/` 恆空。doc_id 三個：
      `popup_037_v0_2`／`core_hmi_lf_sys1`／`core_hmi_lf_pdf`
- [x] spec_mode classified: **A+C** —— SYS1 export 為文字權威（A）；
      規格 PDF 21 頁**無文字層**（pdftotext／pdfplumber／pymupdf 三工具皆得 0
      非空白字元），圖面走 C
- [x] `feature.yaml` filled —— 欄位字母由母本 r9 表頭逐格實測，
      **母本為 Revision C**（Q = Estimated Test Time），非模板預填之 A/B
- [x] 工作簿自 R-G1 母本（sha `6372fb6b…`）起建，落 `sandbox/base/`

## Phase 1 — Recon (Tier 1, fully delegable)（完，上繳包 01）
Run recon; outputs `RECON.md` + pre-filled `DECISIONS.md`.
- [x] workbook_state: **BLANK**（done 0 / draft 0 / ambiguous 0）
- [x] Coverage: **5** leaves total / **0** done / **5** regen targets
- [x] assertions 4/4 PASS

## Phase 2 — Rulings (Tier 2)
- [ ] DECISIONS.md signed by Pei —— 現為 `recon.py` 預填，
      [PROPOSED]／[PEI] 未裁，Sign-off 為未填佔位
- [ ] 待裁四件：A-POP1（覆核）／A-POP2／A-POP3／A-POP4；
      R-POP5 [DEFAULT] 待追認。見 `docs/INDEX.md` §2

## Phase 3 — Framework & profile (Tier 2)
- [ ] `docs/fw036/framework.md` Part N appended
- [ ] `docs/runtime/profiles/FW036_R1L_Popup_Profile.md` written

## Phase 4 — Data build (Tier 1)
- [ ] Data artifacts built per feature.yaml; misses filed to ANOMALIES.md

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: ___  → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [ ] Batches generated → lint green → write-back invariants pass

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent

---

## Popup 專屬事實（上繳包 01 實測）

| 項 | 值 |
|---|---|
| 037 資料列 / leaf / Heading | 7 / 5 / 2 |
| leaf 之 spec 章節 | **全部 `_5.6`**（`_5.5` 僅 Heading `SWE1-POP-001` 引用，見 A-POP3）|
| SYS1 export | 167 列；第 5 章 7 項（NRL-168282 ～ NRL-168288）|
| Test Group / Test Set | `Popup` / `Pop-up Close`（R-POP4）|
| design-method 詞彙 | 母本 `下拉選單` A1:A9，**9 值** |
| 母本 data validation | `P10:Q1411`=`P0,P1,P2,P3`／`T10:Z1411`=`0,1`／`AF10:AF1411`=`Pass, Fail, Pending,Block,NA`。**design_method（R 欄）無 DV** |
| 規格 PDF | 真 PDF 1.5，21 頁，Power PDF Create，**無文字層** |
| `queue` 一詞 | SYS1 export `Description` 欄全文件 167 列命中 **0** 次 |
