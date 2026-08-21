# W-9 — Comfort 逐條對照（R-VS7 委派句之來源表）

來源：`features/comfort/inputs/FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx`
（`Analysis Report`、表頭列 7、資料自列 8、**498 leaf**）。

本 feature 側母體：**237 個 Functional leaf**（R-VS15），非 271。

---

## 1. Comfort 側之命中 —— 兩種計數，**43 = 43**

| 掃描條件 | 命中 |
|---|---|
| 子字串、**無詞界**（00D 之條件） | **43** |
| 詞界 v1（`\bseat\b`，本輪首版） | 30 |
| **詞界 v2（名詞允許複數 `s`）** | **43** |

**詞界 v2 與子字串版之集合完全相同**（兩側差集皆 0）。
→ **00D 所記之「上界 43」實為精確值**，無詞界不足所致之偽陽性。

### 1.1 首版之 13 筆差額全為我方假陰性（先報自己的錯）

詞界 v1 得 30，較子字串少 13。逐筆檢視後**全部為複數形 `seats`**：
`heated/vented seats`／`heated and vented seats` 一類。
`\bseat\b` 於 `seats` 之 `seat` 與 `s` 之間無詞界，故不匹配。

**此為 canon §5a 條 7 之「假陰性源自詞彙不全」**，非「詞界濾掉偽陽性」。
v2 將名詞改為 `seats?`、`ventilat` 改為只要求左詞界（涵蓋 `ventilated`／`ventilation`）後即復原。

掃描欄位：**A–E 欄**合併，**不分大小寫**。

---

## 2. 決定性發現 —— Comfort 037 **不含任何訊號層**

配對依據原擬三者之一：共同訊號名／共同 CFTS044 章節／共同 UI 元件。
**前二者於原理上不可能成立**，實測（Comfort 037 全文 151,266 字元）：

| 探針 | 命中 |
|---|---|
| `$var$` 形態 | **0** |
| `STATUS_` 前綴 | **0** |
| `_Sts` ／ `_Req` 後綴 | **0** |
| 字面 `CAN` | **0** |
| `MESSAGE.Signal` 形態 | 11（皆非本 feature 之訊號） |

且其 `Source Requirement ID` 為 **`SYS-HMI-RA-HVAC-*`**，
與本 feature 之 `SYS-RA-CFTS044-*` **命名空間完全不相交** ——
故「共同 CFTS044 章節」亦不可能成立。

> **這不是配對失敗，是 R-VS7 分層委派之量化證據。**
> Comfort 擁有畫面行為，其 037 因而不含訊號；本 feature 擁有訊號與配置層。
> 二者之交集**只存在於實體功能**，不存在於訊號或章節。

---

## 3. 配對依據：**同一實體功能**（可具名、可驗證）

依 R-VS4，本 feature 之 Layer 3 為 SWE ID 之中段 token。實測 Layer 3 全集 **18** 個：

`FeaturesEnableCriteria`／`HeatedSteeringWheel`／`HeatedSteeringWheelManagement`／
`LeftFrontHeatedSeat`／`LeftFrontVentedSeat`／`OneStageHeatedSeat`／`PHEVFeatures`／
`RightFrontHeatedSeat`／`RightFrontVentedSeat`／`ScreenOFF`／`Stop-StartSystem`／
`StopStartSystemBehavior`／`SwitchLHD/RHDConfiguration`／`ThirdRowHeadrestDump`／
`ThreeStagesHeatedSeat`／`ThreeStagesVentedSeatsManagement`／`TwoStagesHeatedSeat`／
`TwoStagesVentedSeatsManagement`

配對式為**具名之正則 → Layer 3 清單**，非泛關鍵詞：

| Comfort 措辭之判準 | 對應 Layer 3 | 標籤 |
|---|---|---|
| `heated steering` ／ `steering wheel heat` | `HeatedSteeringWheel*` 三者 | 加熱方向盤 |
| `(driver\|left)` 與 `heated seat` 相距 ≤24 字元 | `LeftFrontHeatedSeat` | 左前座椅加熱 |
| `(passenger\|right)` 與 `heated seat` 相距 ≤24 | `RightFrontHeatedSeat` | 右前座椅加熱 |
| `(driver\|left)` 與 `vented seat` 相距 ≤24 | `LeftFrontVentedSeat` | 左前座椅通風 |
| `(passenger\|right)` 與 `vented seat` 相距 ≤24 | `RightFrontVentedSeat` | 右前座椅通風 |
| `heated seat` ／ `seat heat`（未分左右） | 左右前座椅加熱**兩者** | 座椅加熱（未分左右） |
| `vented seat` ／ `ventilat`（未分左右） | 左右前座椅通風**兩者** | 座椅通風（未分左右） |

**43 / 43 皆有具名依據；無具名依據者 0（0%）** —— 升級條件之三成門檻未觸及。

| 依據 | Comfort leaf 數 |
|---|---|
| 座椅通風（未分左右） | 25 |
| 座椅加熱（未分左右） | 11 |
| 加熱方向盤 | 6 |
| 左前座椅通風 | 1 |

> ⚠ **「未分左右」佔 36 / 43**。其對應到左右**兩個** leaf。
> **此為 Comfort 措辭所致，非配對之含糊** —— 其原文即寫 `heated/vented seats` 而未指明側別。

---

## 4. 逐條對照表

| # | Comfort leaf | 標題（節錄） | 配對依據 | 對應 leaf 數 |
|---|---|---|---|---|
| 1 | `SWE1-HVAC-014` | MAX DEF Behavior | 座椅通風（未分左右） | 30 |
| 2 | `SWE1-HVAC-054` | HVAC Popup Behavior | 座椅加熱（未分左右） | 32 |
| 3 | `SWE1-HVAC-054-01` | HVAC Popup Behavior | 座椅加熱（未分左右） | 32 |
| 4 | `SWE1-HVAC-055` | HVAC Popup Behavior | 座椅通風（未分左右） | 30 |
| 5 | `SWE1-HVAC-056` | Status Bar Behavior | 座椅通風（未分左右） | 30 |
| 6 | `SWE1-HVAC-057` | Heated Seat Control | 座椅加熱（未分左右） | 32 |
| 7 | `SWE1-HVAC-057-01` | Heated Seat Control | 座椅加熱（未分左右） | 32 |
| 8 | `SWE1-HVAC-057-02` | Vented Seat Control | 座椅通風（未分左右） | 30 |
| 9 | `SWE1-HVAC-058` | AUTO Mode Behavior | 座椅通風（未分左右） | 30 |
| 10 | `SWE1-HVAC-059` | HVAC Popup Behavior | 座椅通風（未分左右） | 30 |
| 11 | `SWE1-HVAC-059-02` | HVAC Popup Behavior | 座椅通風（未分左右） | 30 |
| 12 | `SWE1-HVAC-059-06` | Seat Zone Control | 座椅通風（未分左右） | 30 |
| 13 | `SWE1-HVAC-060` | Seat Zone Control | 座椅通風（未分左右） | 30 |
| 14 | `SWE1-HVAC-060-02` | Vented Seat Control | 座椅通風（未分左右） | 30 |
| 15 | `SWE1-HVAC-061` | Seat Zone Control | 座椅通風（未分左右） | 30 |
| 16 | `SWE1-HVAC-062` | HVAC Popup Behavior | 加熱方向盤 | 31 |
| 17 | `SWE1-HVAC-063` | HVAC Popup Behavior | 加熱方向盤 | 31 |
| 18 | `SWE1-HVAC-064` | HVAC Popup Behavior | 座椅通風（未分左右） | 30 |
| 19 | `SWE1-HVAC-064-03` | Seat Zone Control | 座椅通風（未分左右） | 30 |
| 20 | `SWE1-HVAC-065` | Temperature Control | 加熱方向盤 | 31 |
| 21 | `SWE1-HVAC-065-01` | Vented Seat Control | 座椅通風（未分左右） | 30 |
| 22 | `SWE1-HVAC-067` | Heated Seat Control | 座椅加熱（未分左右） | 32 |
| 23 | `SWE1-HVAC-068` | Vented Seat Control | 座椅通風（未分左右） | 30 |
| 24 | `SWE1-HVAC-070` | Status Bar Behavior | 座椅通風（未分左右） | 30 |
| 25 | `SWE1-HVAC-071` | Heated Seat Control | 座椅加熱（未分左右） | 32 |
| 26 | `SWE1-HVAC-071-01` | Heated Seat Control | 座椅加熱（未分左右） | 32 |
| 27 | `SWE1-HVAC-071-02` | Vented Seat Control | 座椅通風（未分左右） | 30 |
| 28 | `SWE1-HVAC-072` | AUTO Mode Behavior | 座椅通風（未分左右） | 30 |
| 29 | `SWE1-HVAC-074` | Heated Seat Control | 座椅加熱（未分左右） | 32 |
| 30 | `SWE1-HVAC-075` | Fan Speed Control | 座椅通風（未分左右） | 30 |
| 31 | `SWE1-HVAC-099` | Seat Zone Control | 左前座椅通風 | 15 |
| 32 | `SWE1-HVAC-100` | HVAC Popup Behavior | 座椅加熱（未分左右） | 32 |
| 33 | `SWE1-HVAC-100-03` | Heated Seat Control | 座椅加熱（未分左右） | 32 |
| 34 | `SWE1-HVAC-101` | Seat Zone Control | 座椅通風（未分左右） | 30 |
| 35 | `SWE1-HVAC-101-03` | Vented Seat Control | 座椅通風（未分左右） | 30 |
| 36 | `SWE1-HVAC-104` | Temperature Control | 加熱方向盤 | 31 |
| 37 | `SWE1-HVAC-104-06` | HVAC Popup Behavior | 座椅加熱（未分左右） | 32 |
| 38 | `SWE1-HVAC-104-07` | HVAC Popup Behavior | 座椅通風（未分左右） | 30 |
| 39 | `SWE1-HVAC-104-08` | HVAC Popup Behavior | 加熱方向盤 | 31 |
| 40 | `SWE1-HVAC-115` | MAX DEF Behavior | 座椅通風（未分左右） | 30 |
| 41 | `SWE1-HVAC-115-05` | Rear Defrost Control | 座椅通風（未分左右） | 30 |
| 42 | `SWE1-HVAC-124` | Climate Widget Behavior | 座椅通風（未分左右） | 30 |
| 43 | `SWE1-HVAC-126` | Climate Widget Behavior | 加熱方向盤 | 31 |

### 4.1 對應 leaf 之逐條展開（供 reasoning 指名用）

**座椅通風（未分左右）** —— Comfort 25 條，對應本 feature leaf：

```
SWE1-VC-LeftFrontVentedSeat-003, SWE1-VC-LeftFrontVentedSeat-004, SWE1-VC-LeftFrontVentedSeat-005, SWE1-VC-LeftFrontVentedSeat-006, SWE1-VC-LeftFrontVentedSeat-007, SWE1-VC-LeftFrontVentedSeat-008, SWE1-VC-LeftFrontVentedSeat-009, SWE1-VC-LeftFrontVentedSeat-010, SWE1-VC-LeftFrontVentedSeat-011, SWE1-VC-LeftFrontVentedSeat-012, SWE1-VC-LeftFrontVentedSeat-013, SWE1-VC-LeftFrontVentedSeat-014, SWE1-VC-LeftFrontVentedSeat-015, SWE1-VC-LeftFrontVentedSeat-016, SWE1-VC-LeftFrontVentedSeat-017, SWE1-VC-RightFrontVentedSeat-020, SWE1-VC-RightFrontVentedSeat-021, SWE1-VC-RightFrontVentedSeat-022, SWE1-VC-RightFrontVentedSeat-023, SWE1-VC-RightFrontVentedSeat-024, SWE1-VC-RightFrontVentedSeat-025, SWE1-VC-RightFrontVentedSeat-026, SWE1-VC-RightFrontVentedSeat-027, SWE1-VC-RightFrontVentedSeat-028, SWE1-VC-RightFrontVentedSeat-029, SWE1-VC-RightFrontVentedSeat-030, SWE1-VC-RightFrontVentedSeat-031, SWE1-VC-RightFrontVentedSeat-032, SWE1-VC-RightFrontVentedSeat-033, SWE1-VC-RightFrontVentedSeat-034
```

其 Comfort leaf：`SWE1-HVAC-014`, `SWE1-HVAC-055`, `SWE1-HVAC-056`, `SWE1-HVAC-057-02`, `SWE1-HVAC-058`, `SWE1-HVAC-059`, `SWE1-HVAC-059-02`, `SWE1-HVAC-059-06`, `SWE1-HVAC-060`, `SWE1-HVAC-060-02`, `SWE1-HVAC-061`, `SWE1-HVAC-064`, `SWE1-HVAC-064-03`, `SWE1-HVAC-065-01`, `SWE1-HVAC-068`, `SWE1-HVAC-070`, `SWE1-HVAC-071-02`, `SWE1-HVAC-072`, `SWE1-HVAC-075`, `SWE1-HVAC-101`, `SWE1-HVAC-101-03`, `SWE1-HVAC-104-07`, `SWE1-HVAC-115`, `SWE1-HVAC-115-05`, `SWE1-HVAC-124`

**座椅加熱（未分左右）** —— Comfort 11 條，對應本 feature leaf：

```
SWE1-VC-LeftFrontHeatedSeat-003, SWE1-VC-LeftFrontHeatedSeat-004, SWE1-VC-LeftFrontHeatedSeat-005, SWE1-VC-LeftFrontHeatedSeat-006, SWE1-VC-LeftFrontHeatedSeat-007, SWE1-VC-LeftFrontHeatedSeat-008, SWE1-VC-LeftFrontHeatedSeat-009, SWE1-VC-LeftFrontHeatedSeat-010, SWE1-VC-LeftFrontHeatedSeat-011, SWE1-VC-LeftFrontHeatedSeat-012, SWE1-VC-LeftFrontHeatedSeat-013, SWE1-VC-LeftFrontHeatedSeat-014, SWE1-VC-LeftFrontHeatedSeat-015, SWE1-VC-LeftFrontHeatedSeat-016, SWE1-VC-LeftFrontHeatedSeat-017, SWE1-VC-LeftFrontHeatedSeat-018, SWE1-VC-LeftFrontHeatedSeat-019, SWE1-VC-RightFrontHeatedSeat-022, SWE1-VC-RightFrontHeatedSeat-023, SWE1-VC-RightFrontHeatedSeat-024, SWE1-VC-RightFrontHeatedSeat-025, SWE1-VC-RightFrontHeatedSeat-026, SWE1-VC-RightFrontHeatedSeat-027, SWE1-VC-RightFrontHeatedSeat-028, SWE1-VC-RightFrontHeatedSeat-029, SWE1-VC-RightFrontHeatedSeat-030, SWE1-VC-RightFrontHeatedSeat-031, SWE1-VC-RightFrontHeatedSeat-032, SWE1-VC-RightFrontHeatedSeat-033, SWE1-VC-RightFrontHeatedSeat-034, SWE1-VC-RightFrontHeatedSeat-035, SWE1-VC-RightFrontHeatedSeat-036
```

其 Comfort leaf：`SWE1-HVAC-054`, `SWE1-HVAC-054-01`, `SWE1-HVAC-057`, `SWE1-HVAC-057-01`, `SWE1-HVAC-067`, `SWE1-HVAC-071`, `SWE1-HVAC-071-01`, `SWE1-HVAC-074`, `SWE1-HVAC-100`, `SWE1-HVAC-100-03`, `SWE1-HVAC-104-06`

**加熱方向盤** —— Comfort 6 條，對應本 feature leaf：

```
SWE1-VC-HeatedSteeringWheel-003, SWE1-VC-HeatedSteeringWheel-004, SWE1-VC-HeatedSteeringWheel-005, SWE1-VC-HeatedSteeringWheel-006, SWE1-VC-HeatedSteeringWheel-007, SWE1-VC-HeatedSteeringWheel-008, SWE1-VC-HeatedSteeringWheel-009, SWE1-VC-HeatedSteeringWheel-010, SWE1-VC-HeatedSteeringWheel-011, SWE1-VC-HeatedSteeringWheel-012, SWE1-VC-HeatedSteeringWheel-013, SWE1-VC-HeatedSteeringWheel-014, SWE1-VC-HeatedSteeringWheel-015, SWE1-VC-HeatedSteeringWheel-016, SWE1-VC-HeatedSteeringWheel-017, SWE1-VC-HeatedSteeringWheel-018, SWE1-VC-HeatedSteeringWheel-019, SWE1-VC-HeatedSteeringWheel-020, SWE1-VC-HeatedSteeringWheel-021, SWE1-VC-HeatedSteeringWheel-022, SWE1-VC-HeatedSteeringWheelManagement-025, SWE1-VC-HeatedSteeringWheelManagement-026, SWE1-VC-HeatedSteeringWheelManagement-027, SWE1-VC-HeatedSteeringWheelManagement-028, SWE1-VC-HeatedSteeringWheelManagement-029, SWE1-VC-HeatedSteeringWheelManagement-030, SWE1-VC-HeatedSteeringWheelManagement-031, SWE1-VC-HeatedSteeringWheelManagement-032, SWE1-VC-HeatedSteeringWheelManagement-033, SWE1-VC-HeatedSteeringWheelManagement-034, SWE1-VC-HeatedSteeringWheelManagement-035
```

其 Comfort leaf：`SWE1-HVAC-062`, `SWE1-HVAC-063`, `SWE1-HVAC-065`, `SWE1-HVAC-104`, `SWE1-HVAC-104-08`, `SWE1-HVAC-126`

**左前座椅通風** —— Comfort 1 條，對應本 feature leaf：

```
SWE1-VC-LeftFrontVentedSeat-003, SWE1-VC-LeftFrontVentedSeat-004, SWE1-VC-LeftFrontVentedSeat-005, SWE1-VC-LeftFrontVentedSeat-006, SWE1-VC-LeftFrontVentedSeat-007, SWE1-VC-LeftFrontVentedSeat-008, SWE1-VC-LeftFrontVentedSeat-009, SWE1-VC-LeftFrontVentedSeat-010, SWE1-VC-LeftFrontVentedSeat-011, SWE1-VC-LeftFrontVentedSeat-012, SWE1-VC-LeftFrontVentedSeat-013, SWE1-VC-LeftFrontVentedSeat-014, SWE1-VC-LeftFrontVentedSeat-015, SWE1-VC-LeftFrontVentedSeat-016, SWE1-VC-LeftFrontVentedSeat-017
```

其 Comfort leaf：`SWE1-HVAC-099`

---

## 5. CFTS044 以 `{CFTS043}` 引用 Comfort 之三處（各前後 200 字元）

**三處全數命中**，作為 R-VS7 分層委派之文件層佐證。

### 第 1 處 —— Climate 捷徑類別

```
…[EE Architecture:Atlantis Mid, PowerNet, Atlantis High] The "Climate" shortcut Category
shall be available as per the "Climate Controls Management" section in {CFTS043} and
according to specified by HMI.  4859991: [Artifact Type:Subsystem Functional Requirement]…
```

### 第 2 處 —— 「I am cold」例程

```
…[EE Architecture:PowerNet, Atlantis High, Atlantis Mid] IF the routine "I am cold" is
activated by the user, the HU shall follow the requirements into {CFTS043} to set the
signal $HVACJumpVAL$ to the "full hot" value.  4859995:…
```

### 第 3 處 —— 「I am hot」例程

```
…[EE Architecture:PowerNet, Atlantis Mid, Atlantis High] IF the routine "I am hot" is
activated by the user, the HU shall follow the requirements into {CFTS043} to set the
signal $HVACJumpVAL$ to the "full cold" value. 1.3.4.12.1 Driver Heated Seats {4859998}…
```

> **三處皆為「照 CFTS043 之要求辦」之外推**，與 R-VS7 之分層一致：
> CFTS044 在需要畫面行為時把它推給 CFTS043，自己只保留訊號側（`$HVACJumpVAL$`）。
> **⚠ 三處皆不在本輪之 43 條重疊範圍內** —— 其主題為 Climate 捷徑與 I am cold/hot 例程，
> 非座椅加熱／通風／方向盤加熱。故其為**分層原則之佐證**，非本表之配對來源。

---

## 6. 本表之用法（R-VS7(a)）

TC 撰寫時若需提及畫面行為，於 `reasoning` 以 §8.2.1 之委派句指名 Comfort 之對應 leaf id，
**不寫入 procedure／expected_result 之斷言**。查本表第 4 節即得該 id。

**例外**（R-VS7(b)）：CFTS044 條文自身以 `Refer to TLM HMI Document` 指出畫面行為者
（16 leaf），其畫面層斷言仍屬本 feature，惟在 DR-5-B 到位前依 R-VS17 標 BLOCKED。
**該 16 leaf 不走本表之委派。**
