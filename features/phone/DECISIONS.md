# DECISIONS — Phone (FW036)

> **本檔為人工補寫，非 `recon.py` 產出。**
> `recon.py`（2026-09-07 執行）之 ruled-constant 斷言
> 「SYS1 export available for outline lookup」為 **FAIL**（`paths.sys1_export is null`，
> 見 `ANOMALIES.md` A-PH01／`DATA_REQUESTS.md` DRAFT-PH-a），
> 依其設計**拒絕產出 DECISIONS.md**：
> 「An assertion failure blocks DECISIONS.md; RECON.md is still written because it is the evidence.」
> 該拒絕**如實留著、不繞過**；本檔補寫是為了讓下放包 §6-6 之
> [PROPOSED] 清單有落點，其中凡繫於 SYS1 者一律標 `[BLOCKED]`，**不預填值**。
> 斷言轉綠後應重跑 `recon.py` 並以其產出為準。

Marker semantics per FO §4：

- `[AUTO]` — machine-determined, recorded for audit, no action needed
- `[PROPOSED: value — rationale]` — Pei edits if disagreeing; untouched at
  sign-off = binding as proposed
- `[PEI]` — cannot be proposed; must be filled before sign-off
- `[BLOCKED: DRAFT-PH-a]` — 本包新增之標記：**繫於未結之升級項，不得提案**

An unsigned sheet blocks Phase 4+.

---

## 1. Intake

- spec_mode: `[BLOCKED: DRAFT-PH-a]` — `intake.py` 提案 **A**（SYS1 匯出存在＋圖面 PDF）；
  惟「哪一份 SYS1」未定。二份 PDF 皆有文字層（B 亦可用，見 A-PH02），故裁定後之值
  預期為 `A` 或 `A+B`。
- Source files present: `[AUTO]` — 5 件，sha256 全表見 `up/20260907_PH-01.md` §1。
- Missing referenced specs: `[AUTO]` — 需求報告之引用 stem 僅一個
  （`Phone HMI Logic and Flow R1 SR24 Post 2A (June 21 2022)`，754 leaf 全指向它），
  且該文件在件（`phone_hmi_lf_pdf_2022`）。**無缺件。**
- Spec release/version pinned: `[AUTO]` — `R1 SR24 Post 2A (June 21 2022)`；
  037 為 `V0.1`（封面版本 D，2026-04-27 核准）。
- 26PI 增補（MPA11／MPA12）: `[AUTO]` — 不併入本輪（R-PH2）；原文落 `docs/26pi_delta.md`。

## 2. Workbook survey

- workbook_state: `[AUTO]` **BLANK** —— 母本副本 `sandbox/base/…_20260817_ext.xlsx`
  （sha256 `6372fb6be02f48dc…`，與 `forms/` 母本**全等**），authored rows 0、draft rows 0。
- Header row index: `[AUTO]` **9**
- Column mapping: `[AUTO]` 15/15 欄由表頭文字解出，與 `feature.yaml` 之字母**無衝突**；
  form layout revision **C**（有 `Estimated Test Time` 於 Q）。
- Done-region segments: `[AUTO]` （none）
- Regen-region segments: `[AUTO]` 全簿
- Ambiguous rows: `[AUTO]` （none）
- Draft-region disposition: `[AUTO]` 不適用（無 draft）
- Design-method vocabulary: `[AUTO]` 9 strings（自 `下拉選單` 分頁）
- BLANK fallback chain（FO §2.1）: `[PROPOSED: 以 HFP 交付本
  `…_CFTS026_HandsFreePhone_20260316(Refine).xlsx` 為**風格**樣板 —— 同為電話語意場，
  步驟句式與通話情境 setup 可直接參照（R-PH3(a)）；**只取寫法，不取
  spec_reference 與 Test Set 切法**（R-PH3(d)）]`

## 3. Coverage

- 037 資料列: `[AUTO]` **911**（parent 213／child 698）
- 037 leaf count: `[AUTO]` **754**（判準 `Categorization == Functional Requirement`；
  另 157 列為 `Heading`）
- Covered by done region: `[AUTO]` **0**
- Regen targets: `[AUTO]` **754**
- Leaves covered nowhere: `[AUTO]` 754（即全部；BLANK 之必然）
- Parent/child both-leaf duplications: `[AUTO]` （none）
- **Heading 157 列之台帳處置**: `[PROPOSED: 不出 TC 列，於覆蓋台帳具名為
  `Heading`（沿 `R-POP5` 之形態）—— 理由：R-PH2 之母體為 911 資料列，而
  FO §5「Every leaf gets a row」之 leaf 為 Functional；二者以本項橋接，
  使「911」與「754」在紙上可對得起來]`
- **56 個 parent-shaped 卻為 Functional 之列**: `[AUTO]` `recon.py` 已具名
  （全表在 `data/recon.json`）；判準採 Categorization 而非 id-suffix，故此 56 列**入** leaf 集。

## 4. Style bindings

- Style authority: `[PROPOSED: BLANK fallback chain（見 §2 末）]`
- Test Item shape: `[PROPOSED — 待 §2 樣板裁定後於 Phase 3 落定]`
- Test Group / Test Set 欄: `[AUTO]` Test Group = `Phone`（**R-PH1，已裁**）；
  `fill_test_group_set: true`（BLANK 之故）。Test Set 見 §6。
- spec_reference format: `[BLOCKED: DRAFT-PH-a]`
  —— 形制已定為 `{檔名}_{章節號}`（IN §10.7(b)），且 037 `HMI Source ID` 欄
  **本身即載該形制**（213 個相異值，A-PH05）；`{檔名}` 逐字為
  `Phone HMI Logic and Flow R1 SR24 Post 2A (June 21 2022)`。
  **缺的只有「章節號取自哪一份 SYS1」**，故標 BLOCKED 而非 PROPOSED。
- Author value on new rows: `[AUTO]` `PeiPYHsu`（R-G42 四）
- Priority rubric deviations: `[AUTO]` 無 done region 可比

## 5. Split & scope

- split_mode: `[PROPOSED: standard]`
- 範圍: `[AUTO]` **整份 037，911 列**（R-PH2，已裁）；不做 Multiphone 子集篩選。
  關鍵字子集之登記數見 A-PH06（實測 35 parent／108 child，與下放包預期 42／120 不符，不調和）。
- Known scope carve-outs: `[PROPOSED: 無]` —— 037 內無刪節線標記可辨識者；
  26PI 之 MPA11／MPA12 依 R-PH2 不併入，另案（DRAFT-PH-b）。

## 6. Framework & profile

- **TC ID `{ABBR}`**: `[PEI]` —— **R-G42 二在本 feature 取不到值**：
  037 之 req_id 為 `SWE1-HMI-{nnn}`，其 token `HMI` 為文件類別而非 feature 縮寫
  （同一 token 為全部 HMI L&F 系 feature 共用，不具鑑別力）。
  依 R-G42 二「req_id 無縮寫或有歧義者，由 Pei 裁一次後登 feature.yaml，不得自定」，
  本項為 `[PEI]`。候選（附依據，不代裁）：

  | 候選 | 依據 | 反面 |
  |---|---|---|
  | **`Phone`** | `R-POP13`（2026-08-27）之實測：五本交付／產出簿 4/5 為 `NR1L-{FeatureName}-{NNN}`（power／SXM／UserProfiles／TimeManagement）。本 repo 現況亦以全名居多（`Popup`／`Privacy`／`ComfortHMI`／`PROJ`…）。與 R-PH1 之 Test Group `Phone` 同字。 | 較長 |
  | `PH` | `new_feature.py` 之 scaffold 預設（前二字）。全 repo 除本檔外無 `NR1L-PH-` 出現。 | **非裁定**，只是預設值 |
  | `HMI` | R-G42 二之字面（037 req_id 之 token） | 不具鑑別力，跨 feature 必撞 |

  **執行層不代裁；`feature.yaml` `tc_id.abbr` 現為 `null`。**
- Test Set table (Part N draft): `[PROPOSED — 以 037 之 27 個頂層章為第一版切分]`
  037 之章分佈（leaf 數）：1(10)、2(23)、3(4)、4(5)、5(128)、6(18)、7(16)、8(9)、
  9(62)、10(85)、11(7)、12(54)、13(32)、14(65)、15(13)、16(16)、17(35)、18(17)、
  19(33)、20(26)、21(3)、22(6)、23(1)、24(29)、25(37)、26(16)、27(4)。
  **章名逐字須自 SYS1 取**（頂層章 27 個，Outline 不含 `.`）→ `[BLOCKED: DRAFT-PH-a]`。
  參考：HFP 交付本用 13 個 Test Set（Call Log 47／Bluetooth 22／Device Manager 13／
  AddressBook 11／Contact 8／Voice recognition 7／Message 7／Service Control 6／
  Status Information 4／System State 3／Phone Call 1／該欄空白 6／一列為中文備註誤入）
  —— **只作對照，不採用**（母體不同，R-PH3(d)）。
- Profile [OVERRIDE] clauses needed: `[PROPOSED — 待 Phase 3]`
- lint `P`(v4) 與 `X`: `[AUTO]` 兩者皆於
  `docs/runtime/profiles/FW036_R1L_Phone_Profile.md` 啟用（FO §4 [ADD] 第一項）。

## 7. Execution

- Batch plan: `[PROPOSED — 754 leaf 依章切批，5／10／14／9 四個大章各自成批，
  其餘併批；批數與序待 §6 Test Set 定案後落定]`
- Model assignment per batch: `[PROPOSED — Opus for 第 5／10／14 章（列多且情境交錯），
  Sonnet for 其餘（有 HFP 樣板）]`
- BLOCKED batches at start: `[AUTO]` **全部** —— `DRAFT-PH-a` 未結前無 `spec_reference` 來源。

---

## Sign-off

- Reviewed by: ____________  Date: ____________
- Overridden items (list numbers): ____________
- Ruling notes:
