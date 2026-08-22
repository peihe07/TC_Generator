# FW036 R1L — Vehicle Setting Profile

依 `features/vehicle_setting/docs/handoff/35_pilot_review1.md` §2 之 W-54 建檔，18 輪。

**本檔為既有裁決之 profile 化，不新增任何規則。** 每條 cite 其來源條文。
與 `docs/runtime/ASPICE_SWE6_AI_Instruction.md` 之關係依 **R-VS41(4)**：
feature 級條文與 canon 衝突時 canon 勝，**除非該例外寫入本檔並於條文中 cite**。

| 項 | 值 |
|---|---|
| Feature | Vehicle Setting |
| 母 spec | `R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_044_Vehicle Controls_SR26_20250909-1816.docx` |
| Layer 1（Test Group） | `Vehicle Setting`（R-VS3） |
| Layer 2（Test Set） | `Common Features`／`Heated Seat`／`Vented Seat`／`Heated Steering Wheel`（R-VS4） |
| 母體 | 237 個 Functional leaf（R-VS15） |
| 基線 DBC | `PDT27_E2A_R4_BHCAN.dbc`（CAN-B／BH-CAN）／`PDT27_E2A_R5_FDCAN8.dbc`（CAN-FD）（R-VS9(4)） |

---

## [OVERRIDE §11] `test_item` 上半段之方括號 token 予以保留

`test_item` 上半段為 037 Requirement Description **逐字**（R-VS6／R-S4）。
CFTS044 原文含方括號 token，例如
`[IDLE_STBL//UNLIMITED//LIMITED//RUN]`、`[ENS_DSBL]`、`[SNA]`、
`[Right Drive]`、`[Pressed]`。**該等 token 予以保留。**

四個交付欄（`pre_conditions`／`input_test_data`／`test_procedure`／
`expected_result`）**仍禁方括號**，一律以 `"..."` 書寫 UI 標籤。

lint 對 `test_item` 之保留 token 以「**與所引來源列逐字相符**」驗證，非禁用。

**先例**：Home A-H10（pilot review 時修訂）。
**來源**：35 包 §2；關閉 A-VS60。

## [OVERRIDE §4.1.3／§4.2] Layer 2 = `Common Features` 之粗粒度

Layer 2 之 `Common Features`（R-VS4，**Pei 裁定**）為 **037 之檔界**，
其 46 個 Functional leaf 涵蓋 Stop-Start System、Switch LHD/RHD、
Screen OFF、Third Row Headrest Dump、PHEV Features、Features Enable Criteria
等異質能力，**不滿足 §4.2 之「共用 setup 與 UI 進入路徑」期待**。

**理由**：037 檔界即上游作者選定之能力叢集邊界（00 包 §3 之 R-VS4）。

**來源**：35 包 §2；關閉 A-VS61。

## [ADD] 訊號書寫依 canon §8.7.5 v3

`$<MESSAGE>.<Signal>$`，值採 `= <raw> (<label>)`；
`<raw>` 取 DBC 數值、`<label>` 取 DBC `VAL_` 逐字。

signal 之**拼寫**取 DBC（R-VS9(1)′）；
**所屬 message、網段、LID ↔ signal 之對映**取 LID 表（R-VS9(1)′）。
`$var$` 之規格 token **不入** `test_procedure`／`expected_result`（R-VS9(5)）。

**網段以 Pre-Condition 承載**（R-VS41(2)，依 R-12a：工具型前置採 SWC 措辭、置末位）。

**來源**：R-VS41(1)(2)。**R-VS9(3) 之三件組已撤回**，lint L-VS1 一併撤回；L-VS2 不變。

## [ADD] `specification_reference` 依 canon §10.7(a)

`CFTS044-{7位數}`（Polarion ObjectID），**一個 ObjectID 一行**，
每行完整重述前綴，**禁用 `,`／`、`／`;` 串接**，升冪。

**來源**：R-VS41(3)（更正 R-VS33′ 與 R-VS14 之排列段）。

## [ADD] `PENDING` 行不計入 §10.5 之最低步數

`PENDING: DR-{n}` 佔位行**不計入 canon §10.5 之最低步數**。
一條 TC 若扣除 PENDING 行後不足 2 個可執行步驟，
該 TC 標 `split_flag = false` 但於 `split_reason` 記
`BLOCKED-BY-DR-{n}: executable steps < 2`，
**並自該批移出，待該 DR 覆後再入批**。

**來源**：38 包 §1 之 D-3 裁定（分析層，記入 profile，不另編號）。
實例：`SWE1-VC-Stop-StartSystem-006` 於 19 輪自 batch01 移出。

## [ADD] 無效值注入之優先序

  (1) DBC 中**未定義之編碼** → 寫作 `= <raw>`，**不加 `(<label>)`**
  (2) 無未定義編碼時，取**配置相依之無效值**（他條文之有效值列舉所排除者），
      寫作 `= <raw> (<label>)` 並於 `reasoning` 記其依據條文
  (3) 二者皆無 → `PENDING: DR-{n}`

**來源**：44 包 §4（分析層裁定，記入 profile）。
實例：`HeatedSteeringWheel-006` 取 (1)（`Tri_Level_HSW_StatSts` 之 4 未定義）；
`LeftFrontHeatedSeat-008`／`RightFrontHeatedSeat-026`／`LeftFrontVentedSeat-006`
取 (2)（`4858307`／`4858363` 之二階有效值列舉排除 `medium`）。

**`SNA` 不得作為 invalid state 之注入值** —— 其為 DBC 已定義之編碼，
語意為「訊號不可用」，非「無效狀態」。

## [ADD] `input_test_data` 一律 `NA`

資料內聯至 `pre_conditions` 或 `test_procedure`，使步驟自足。

**來源**：R-VS5（承 canon §4.5 之 SWC 基準）。

## [OVERRIDE §8.7.5] 訊號書寫依 SWC 0708 交付本（R-VS52）

> **cite**：R-VS52（Pei 2026-08-22，54 包 §1）。
> 依 canon §0「a feature profile's cited override wins over the generic rule here」，
> 本段取得 R-VS41(4)（canon 優先）之例外資格。
> **取代 canon §8.7.5 v3 之 `$<MESSAGE>.<Signal>$ = <raw> (<label>)` 形式。**

```
(1) 送出型步驟
    procedure：Send CAN: <MESSAGE>.<Signal> = <raw> (<label>)
    ER       ：<MESSAGE>.<Signal> = <raw> (<label>) is sent
               必要時附時機（交付本用 during press window／after release）
    訊號名不加 `$` 包夾（交付本 `$MSG.Sig$` 形態命中 0）

(2) 讀取型步驟
    procedure：Read <對象> and record as <變數名>
    ER       ：<變數名> is recorded
               比較步驟之 ER 用 <變數名> = <期望> 或 <變數名A> = <變數名B>

(3) 保持型步驟
    `Hold for <t>` 自成一步，ER 為 `The signal is held for <t>`

(4) baseline 比較採具名變數（交付本：Vol_initial／Vol_after），
    不用「the same as recorded in step N」
```

**撤回者**：R-VS41(1)（canon §8.7.5 v3 形式）；
A-VS62 之 (a) 認可（`is registered without a bus error`）——
**送出型 ER 改為 `is sent`**。

**理由**：本 feature 之交付物須與 SWC 0708 交付本外觀一致。
canon §8.7.5 v3 之修訂（2026-08-21）晚於 SWC 0708 交付（2026-07-08），
而該一致性屬交付形式，Pei 裁定。

---

---

## 未寫入本檔者（即依 canon 通則）

- §4.3 tc_title 三形、2–14 字、無模態
- §4.4／§8.5 Pre-Condition 僅狀態／環境
- §5 步驟設計、§6 ER、§9 十七項自檢、§10 輸出契約、§12 Design Method
- §8.4.1／§8.4.2 不造值、不造範圍；§8.4.3 `PENDING: DR-{n}` 佔位
