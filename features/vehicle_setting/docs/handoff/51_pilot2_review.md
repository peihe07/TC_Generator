# 51 下放包 — pilot #2 逐條分類（15 條）＋ 30 輪未執行

分析層寫入，2026-08-22。**15 條全數逐條讀過。**

---

## 0. 30 輪僅產出空骨架

`docs/upstream/28_cmd_tlm.md` 之 D-1 已建（R-VS18 之機制正確運作），
**D-2～D-5 與 W-86／W-87／W-88 全部 ⬜ 未執行。**

**30 輪指令（50 包 §4）需重貼。** W-86（`*_Cmd_Tlm` 61 leaf）仍是最大解鎖。

---

## 1. pilot #2 之建議分類（**Pei 覆核此表即可，不需重讀 15 條**）

| # | leaf | 建議 | 摘要 |
|---:|---|---|---|
| 1 | `StopStartSystemBehavior-054` | **pass** | baseline 比較正確；`ESS_ENG_ST != ENS_DSBL` 以 `= 3 (ENS Running)` 滿足 |
| 2 | `SwitchLHD/RHD-012` | **defect D-1** | 見 §2.1 |
| 3 | `HeatedSteeringWheelManagement-027` | **pass**（附 note） | baseline 比較正確。note：`4858299` 之逐字節錄把下一節標題 `1.3.2.1.3.1 Left Front Heated Seat {4858300}` 吞入，抽取邊界問題，不影響 TC |
| 4 | `LeftFrontHeatedSeat-008` | **defect D-2** | 見 §2.2 |
| 5 | `LeftFrontHeatedSeat-003` | **pass** | 「不送任何 frame」之負向設定明確 |
| 6 | `TwoStagesHeatedSeat-057` | **pass**（附 note） | 循環驗證正確，`dr15_exposed = no` 依 44 包 §3 成立。note：來源列四種 Ignition Working Condition 而 TC 取 `Ignition On` 一種，未說明取捨理由 |
| 7 | `HeatedSteeringWheelManagement-025` | **pass** | spec_ref 併列適用性前言 `4859492` **正確** —— §10.7 明文含 `relies on as setup` |
| 8 | `HeatedSteeringWheel-006` | **pass** | 注入未定義編碼 `4` 且不加 label，依 44 包 §4 之優先序 (1) |
| 9 | `HeatedSteeringWheel-003` | **pass** | |
| 10 | `LeftFrontVentedSeat-004` | **pass** | 三個有效值逐一驗，與 #11 之負向配對（§7） |
| 11 | `LeftFrontVentedSeat-006` | **defect D-2** | 同 #4 |
| 12 | `LeftFrontVentedSeat-003` | **pass** | |
| 13 | `LeftFrontHeatedSeat-014` | **defect D-3** | 見 §2.3 |
| 14 | `RightFrontHeatedSeat-031` | **defect D-4** | 見 §2.4 |
| 15 | `HeatedSteeringWheel-021` | **note** | `duplicate_of` 標記正確；兩條並存為 A-VS85 之後果，見 §3 |

**合計：pass 10／defect 4（涉 5 條）／note 1。**
**另有一項 style-divergence 橫跨 8 條，見 §2.5。**

---

## 2. 四項 defect

### 2.1 D-1 `SwitchLHD/RHD-012` —— 步驟不可執行（§5.1）

```
2. Drive DrvSeatHeating.Req to Requested by pressing the left front heated seat switch
```

`DrvSeatHeating.Req` 為**內部訊號**（§8.7.5(d) 保留來源名，正確），
**但測試者無法「drive」一個內部訊號** —— 該訊號是按壓之**結果**，不是手段。
措辭把因果倒置，且其主動詞 `Drive` 之受詞不可操作。

**修法**：`2. Press the left front heated seat switch and record the resulting heated seat icon status`
（步驟 4 同）。內部訊號名移至 `reasoning`。

### 2.2 D-2 `LeftFrontHeatedSeat-008`／`LeftFrontVentedSeat-006` —— 前置條件自相矛盾

```
1. The vehicle is configured for two heated seat states, Off and Low and High
```

**「two states」卻列三個值。** 來源 `4858367`／`4858307` 寫
`For vehicles with two states (i.e. LO and HI)` 而其有效值列舉為三個（含 Off）——
**來源之矛盾被逐字照抄進前置條件**，成為一句自相矛盾之測試條件。

**修法**：`1. The vehicle is configured for the two-stage seat setting (LO and HI), whose valid states are Off, Low and High`

**此為 §4.4 之 Pre-Condition 須為明確狀態**；自相矛盾者不可據以布置環境。

### 2.3 D-3 `LeftFrontHeatedSeat-014` —— **ER 以 `<Tsend>` 為通過條件**

```
3. The signal $…FL_HS_Tlm$ = 0 (Not_Pressed) is registered within <Tsend>
```

**直接違反 42 包 §3.2 之裁定**（「ER 不得以 `within <Tsend>` 為通過條件」）
與 canon §8.7.1（門檻須為具體值）。procedure 步驟 3 亦同。

**修法**：ER 改為可觀察終態
`3. The signal $…FL_HS_Tlm$ reads 0 (Not_Pressed) after the press`，
時限以 Remarks 標 `BLOCKED: DR-24′`，並標 `dr_dependent = DR-24′`。

### 2.4 D-4 `RightFrontHeatedSeat-031` —— 同源條文，處置與 -014 相反

`-031` **完全丟掉時限**（procedure 與 ER 皆無 `<Tsend>`），
且其 **ER 3 與 ER 1 逐字相同**（`reads 0 (Not_Pressed)`）。

| | -014 | -031 |
|---|---|---|
| 時限 | 寫入 ER（違規） | **靜默丟棄**（未標 BLOCKED） |
| ER 3 | `registered within <Tsend>` | 與 ER 1 逐字相同 |

**兩條源自同型條文（`4858320`／`4858350`），處置相反。**
`-031` 之靜默丟棄更嚴重 —— **需求之核心（`within <Tsend>`）消失而無任何痕跡**。

**修法**：兩條一律依 §2.3 之修法，**並標 `dr_dependent = DR-24′`**。

### 2.5 style-divergence（橫跨 8 條）—— `is registered without a bus error`

出現於 #1／#4／#8／#11／#13／#14／#15 等。**A-VS62 自 25 輪懸置至今。**

分析層仍**無法自既有交付本枚舉其 house style**（`comfort/inputs` 之 036 為空白樣板，
SWC 0708 不在本 feature `inputs/`）。

**請 Pei 於 pilot #2 一併裁**：
(a) 認可現行措辭為本 feature 之既定寫法 → A-VS62 關閉；或
(b) 提供任一已交付本之「送 CAN 訊號」步驟樣本 → 據以對齊

**不阻擋放行**；若日後對齊為單欄字串替換。

---

## 3. #15 之並存 —— Pei 須知其後果

`HeatedSteeringWheel-021` 與 `-015` **嚴格等價**（觸發／結果／輸入／驗證對象全同），
其差別僅在來源條文之記法（`[1h: On]` vs `[On]`）。

**兩條皆交付**，因 037 有兩個 leaf（`4858544`／`4858538`），
而 §8.2.1 反向禁令**禁止 TC 作者合併 leaf**。

→ **工作簿內將有兩條內容相同之 TC，各自追溯不同 reqid。**
**這是正確處置，但交付前須向客戶說明**，否則會被讀為重複。
A-VS85 已登記，**最終覆蓋報告須揭露 `duplicate_of` 之條數**。

---

## 4. 31 輪指令（**含 30 輪未執行之三項**）

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/50_review_round29.md   ← 30 輪之作業（未執行）
  features/vehicle_setting/docs/handoff/51_pilot2_review.md    ← 本輪依據

## 文書

D-1  沿用既有之 docs/upstream/28_cmd_tlm.md（骨架已建），逐節填入。
D-2  逐字轉錄 50 包 §1 之 **R-VS50** 入 RULINGS.md。
D-3  DR-21 之影響範圍以 W-86 之結果重估並改寫。
D-4  依 R-VS35 列兩數。

## 作業（三項，R-VS25）

W-86  **`*_Cmd_Tlm` 四者之 LID 回查**（最高優先，61 leaf）
      —— 全文同 50 包 §4 之 W-86，不變。

W-89  **pilot #2 之 defect 修正**（51 包 §2）
      (1) `SwitchLHD/RHD-012`：步驟 2／4 之 `Drive … Req to Requested by
          pressing …` 改為 `Press …`；內部訊號名移至 reasoning
      (2) `LeftFrontHeatedSeat-008`／`LeftFrontVentedSeat-006`：
          前置條件 1 改為
          `The vehicle is configured for the two-stage seat setting (LO and HI),
           whose valid states are Off, Low and High`
      (3) `LeftFrontHeatedSeat-014`／`RightFrontHeatedSeat-031`：
          ER 改為可觀察終態，時限以 Remarks 標 `BLOCKED: DR-24′`，
          並標 `dr_dependent = DR-24′`；**兩條處置須一致**
      產出各批次之 `_v{n+1}`，**原版保留不刪**。
      重跑 §9 十七項自檢 ＋ DBC 值表核對。

W-87  適用性前言之全量掃描 —— 全文同 50 包 §4 之 W-87，不變。

**batch13 順延**，俟 W-86 之結果定其池。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
不得撰寫適用性前言型條文之 TC。R-VS49 限於該四 PROXI 參數。

## 升級條件

W-86(3) 判四者為實值域（**正向**，61 leaf 可解，立即回報）；
W-86(3) 判為轉指且所指之表不在 `inputs/`；
W-87(1) 之同型總數 > 20；
W-89 修正後 §9 出現新違規。
```

---

## 5. 待 Pei

| 項 | 內容 |
|---|---|
| **pilot #2 之裁決** | 覆核 §1 之分類表：**pass 10／defect 4／note 1**。defect 之修法已具名，31 輪執行 |
| **A-VS62** | §2.5 之二選一 —— 認可現行措辭，或給一份交付本樣本 |
| DR-17／DR-20／DR-23／DR-8′／DR-24′／DR-18／DR-11 | 待送；**DR-21 俟 W-86 定案** |

---

## 6. 本包產生之新條文清單（自檢）

無新條文。本包為 pilot #2 之分類與 31 輪指令。
