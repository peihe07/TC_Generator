# DECISIONS — Audio Management (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] D —— 讀自 feature.yaml；R-AM8 已定案
- spec text layer 之意涵: [AUTO] 檔 2 為真 PDF 且文字層完好，推翻 01 包 §一「實為純文字」之判定（A-AM02）；不影響 R-AM8，D 之判準為錨值 looked up 而非 constructed
- spec text layer: [AUTO] text-layer: 602279 chars (via pymupdf)
- source files: [AUTO] 5 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 0 checked, 0 PASS, 0 FAIL (measured values in RECON.md)

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage

> **警告 — 本節之 203 非本 feature 之葉數。** recon 之 `survey_a03` 只吃單一
> 分頁，本 feature 之 SWE.1 報告將 318 列分散於四個分頁（Part 01=76、
> 02=203、03=18、04=21），`paths_meta.a03_sheet` 取列數最多之 Part 02 為
> **代表**（比照 vehicle_setting R-VS4）。故以下 `203` 一律只反映代表分頁。
> **葉全集以 `data/leaves.tsv` 為準：318 列／317 唯一 SWE ID**
> （`SWE1_AMM_076` 碰撞兩列，R-AM6）。R-AM5 之驗證範圍為該 318 葉。
> 交付前之覆蓋率校驗須對 `data/leaves.tsv`，不得引用本節數字。

- 037 leaves: [AUTO] 203 —— 代表分頁；全集 318（見上方警告）
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 203 —— 代表分頁；全集之 regen target 為 318（BLANK 下全葉皆為目標）
- covered nowhere: [AUTO] 203 = 代表分頁全葉 — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap

## 4. Style bindings
- style authority: [PROPOSED: fallback chain — no done region]
- test item shape: [PROPOSED: standard §4.3 tc_title]
- test group/set columns: [PROPOSED: FILL per framework Part N]
- exemplar source: [PROPOSED: nearest sibling feature done region, cross-feature: style only]
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [PROPOSED: CFTS019-{object_id}]
- tc_id scheme: [RULED] NR1L-AMM-{n:03d} — frozen per this feature's RULINGS.md, not open at sign-off

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [RULED] framework.md 已 LOCKED（Pei 2026-08-26「1採 2採」），11 集／318 列
- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]

## 7. Execution
- batch plan: [RULED] B1 已由 03 包指定並經 Pei「B1准」——Source Transition 全 34 葉 ＋ Audio Arbitration 前 16 葉，共 50 葉。recon 之 by-chapter 提案不適用，B1 之葉清單、錨定與 sibling 軸見 03 包 §四／§五

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:
