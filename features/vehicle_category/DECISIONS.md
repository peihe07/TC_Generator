# DECISIONS — Vehicle Category (FW036)

> 本檔為簽出版。內容取自 `docs/DECISIONS_signoff_draft.md`
> （SHA256 `8c1abac4a46db819813396e293396bc08f6867f53c1e190c68273861483c45b2`），
> 經 Pei 2026-08-26 授權（下放包 07 §〇 / T41）寫入。
> 簽出時之逐字一致驗證見上繳包 07 §2.1（`diff -q` 無輸出）。
> 本檔已簽出，`recon.py` 不再覆寫（A-TM15）。

Markers per FEATURE_ONBOARDING §4；未簽之表阻斷 Phase 4+。
`[PROPOSED]` 於簽署時未經修改 = 依提案生效。

---

## 1. Intake

- spec_mode: `[AUTO]` **A**
  （FO §3 實測：SYS1 export 齊備、outline map 可建、037 之 66 個
  `HMI Source ID` 對 SYS1 命中 66/66；`intake.py` 獨立提案亦為 A）
- spec text layer: `[AUTO]` 18,750 chars (via pymupdf)
  （T17 逐頁量測：28 頁，其中 p9–p18、p24–p27 為影像頁，
  文字層僅存投影片標題與頁碼）
- source files: `[AUTO]` 6 present（SHA256 見 `RECON.md` 與 `feature.yaml`
  之 `reference:` 六項）
- ruled-constant assertions: `[AUTO]` 3 checked, 3 PASS, 0 FAIL
- spec outline map: `[AUTO]` 66 cited sections, all found in a 108-entry
  ruled export; map at `data/recon_leaf_to_section.tsv`

## 2. Workbook survey

- workbook_state: `[AUTO]` **BLANK**（R-VC2 所裁；done 0 / draft 0 / authors none）
- form layout revision: `[AUTO]` C (has Estimated Test Time)
- column mapping: `[AUTO]` 15 fields resolved from header text
  （`feature.yaml` 之字母僅為先驗，conflicts: none）
- done segments: `[AUTO]` none
- ambiguous rows: `[AUTO]` none
- design-method vocabulary: `[AUTO]` 9 exact strings from 下拉選單

## 3. Coverage

- 037 leaves: `[AUTO]` **145**
  > ⚠ **此為 `Categorization == Functional` 判準之 145，非 R-VC3 所裁之
  > 驗證母體 117**（子需求 ∪ 無子之父）。三判準並存：145 / 117 / 79。
  > **117 與覆蓋落差 17 無對應之 assertion 實作（A-VC8），
  > 其守護僅靠 T4／T12 之集合相等重測與上繳交叉檢查，非機器保證**
  > —— R-VC9 之揭露義務，簽署時請一併確認。
- safety attributes: `[PROPOSED: ruled source carries no ASIL/FTTI column,
  so the SYS2/SYSRA safety layer does NOT enter the trace chain]`
- regen targets: `[AUTO]` 145（清單於 `data/recon.json`）
- covered nowhere: `[AUTO]` 145 = all leaves —— BLANK 下之預期，非缺口；
  這是 Phase 4 之工作清單
- parent/child dupes: `[PROPOSED: proportion test per case]` —— 28 筆，
  即 R-VC3 之「有子之父」28，數字一致

## 4. Style bindings

- style authority: `[PROPOSED: fallback chain — no done region]`
- test item shape: `[PROPOSED: standard §4.3 tc_title]`
- test group/set columns: `[PROPOSED: FILL per framework Part N]`
  （R-VC2(a) 已裁 `fill_test_group_set: true`）
- exemplar source: `[PROPOSED: nearest sibling feature done region,
  cross-feature: style only]`
- author on new rows: `[PROPOSED: PeiPYHsu]`（R-VC2(b) 已裁，一致）
- **spec_reference**：**逐字取 037 `HMI Source ID` 欄原值（R-VC4）。**
  `feature.yaml` 之 `spec_reference_template: null` 係「查得而非構造」
  之宣告，**非空值**；資料件見 `data/recon_leaf_to_section.tsv`
  （145/145 逐字相符，R-VC8 修法後之產出）。

  > **本行係手動覆蓋。** `recon.py` 所產之 `DECISIONS.new.md` 於此印出
  > `[PROPOSED: None]` —— 那個 `None` 是 `null` 之內部表示洩漏到產出檔，
  > 非裁定值（A-VC11）。依下放包 05 §一裁定：**簽署時手動覆蓋，不修腳本**。
  >
  > 前例：`display` 遇同一症狀（其 `DECISIONS.new.md:33` 亦為
  > `[PROPOSED: None]`），處置為**拒絕降格、維持 `[PEI]`**，
  > 理由記於 `features/display/DECISIONS.md:211`：
  > 「`[PROPOSED]` 未經修改即生效，會使該項在簽核時無聲通過（R-DM32）」。
  > 本 feature 之情形不同 —— R-VC4 已裁明其值，故採實值覆蓋而非留 `[PEI]`。

## 5. Split & scope

- split_mode: `[PROPOSED: standard]`

## 6. Priority

> 本節為 `recon.py` 產出所無 —— priority 之判定不在 recon 之範圍
> （上繳包 04 §6.4）。依該節建議增列，否則 117 筆定案不在決策表之視野內。

- TC priority: `[AUTO — 已定案]` **`data/priority_final.tsv`**（117 leaf）
  - 分布：**P0 5 / P1 32 / P2 45 / P3 35**
  - 判準：R-VC11(a) 之 IN §10.2 rubric 逐 TC 判 ＋ R-VC13 之**章級**
    上游約束（High 之章至少一筆 ≥P1、Low 之章不得高於 P3、Medium 不設約束）
    ＋ R-VC14 之攔阻／執行失效區分
  - **不得建立 High/Medium/Low → P0–P3 之機械映射表**（A-VC9：037 該欄
    粒度為「章」）
  - 生成時之附帶義務（R-VC11(c)）：`VC-035-03`／`VC-036-02`（本地 P0
    而 037=Medium）與 `VC-036-01`（R-VC14(b)，隱私外洩風險）
    須於 `reasoning` 記明分歧與 §10.2 對應款

## 7. Framework & profile

- Test Set table (Part N): `[PEI — 提案已備，見下放包 05 §二；待簽]`
  - 提案為 **8 組**，leaf 數經獨立重測 117/117 相符，section 66/66，
    無 leaf 落於二組或零組（上繳包 05 §4）
- profile `[OVERRIDE]` clauses: `[PEI — draft with Claude, Tier 2]`

## 8. Execution

- batch plan: `[PROPOSED: group 145 targets by spec chapter,
  pilot = smallest coherent batch]`
  > 若 §7 之 8 組 Test Set 獲簽，建議改為依 Test Set 分批
  > （pilot 取 `Brake Service` 2 筆或 `Cabrio Widget` 1 筆過小，
  > 宜取 `Glove Box` 12 筆 —— 邊界清楚、含完整流程、無待補節）。
  > **此為建議，非提案** —— pilot 之選定屬 Tier 2。

---

## 未結事項（簽署時併看）

- **DR 七筆全未結**（DR-VC1 ~ DR-VC7）。同批 A ＝ DR-VC2 ＋ DR-VC7
  ＋ A-VC2 ＋ A-VC10。
- **A 七筆未結**：A-VC2、A-VC3、A-VC4、A-VC8、A-VC9、A-VC10、A-VC11。
- 表 B（覆蓋落差揭露，17 節）為草稿，最終措辭待 DR-VC3 回覆。
- 表 A（FROP 跨域揭露）之母體為 145 列中之 17 列（PM 16 ＋ Audio 1）。

  > **加註（下放包 25 §一，T129；簽署本文不改，R-TM13）** ——
  > 上行之母體標註（145 列）**正確**。加註之標的為其**編製方式**：
  > 表 A 之編製**依 leaf 母體之實測**，不得沿用任何由 R-VC16(e) 反推之敘述。
  > 章 13 之 leaf 母體為 **PM 12 ＋ VS 4**（REV-11／REV-14）。

---

## Sign-off

- Authorized by: PeiPYHsu — 2026-08-26（下放包 07 §〇，Tier 3 授權）
- Written by:    execution layer (Claude Code) — T41
- Verification:  diff -q vs docs/DECISIONS_signoff_draft.md → 一致（上繳包 07 §2.1）
