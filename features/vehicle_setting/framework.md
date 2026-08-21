# Vehicle Setting —— framework 草案（Layer 1–3）

**狀態：草案，未鎖定。** 依 28 包 §5 之 W-41 產出，14 輪 W-46 依 **R-VS37** 重判；
鎖定屬 Tier 2，待 Pei 簽核（P19）。canon §4.1.2 步驟 5 —— **僅列 Layer 1–3，不列個別 RD。**

母體：**237 個 Functional leaf**（R-VS15），取自 037 四本 SWRA。
Layer 3 之界定：**依 R-VS37 以 `reqid_list` 所跨之 CFTS044 章節判定**，
SWE ID 中段 token 僅為預設值。**共 19 個**（含新增之 `Common Features` 與 1 個無 reqid）。

## 依 R-VS37 之章節判定（14 輪 W-46，取代下方 token 判定表）

| Layer 3 | leaf | 相對 token 判定之變動 |
|---|---:|---|
| `ThreeStagesHeatedSeat` | 22 | — |
| `ThreeStagesVentedSeatsManagement` | 22 | — |
| `ThirdRowHeadrestDump` | 21 | — |
| `TwoStagesHeatedSeat` | 20 | — |
| `TwoStagesVentedSeatsManagement` | 20 | — |
| `HeatedSteeringWheel` | **19** | −1（`-009` 無 reqid） |
| `LeftFrontHeatedSeat` | **15** | **−2**（`-004`／`-011` 改判 Common） |
| `RightFrontHeatedSeat` | 15 | — |
| `LeftFrontVentedSeat` | 15 | — |
| `RightFrontVentedSeat` | 15 | — |
| `OneStageHeatedSeat` | 14 | — |
| `HeatedSteeringWheelManagement` | **8** | **−3**（`-025`／`-026`／`-027`，**該 3 筆 R-VS37 未涵蓋，見下**） |
| `Stop-StartSystem` | 6 | — |
| `SwitchLHD/RHDConfiguration` | 6 | — |
| `ScreenOFF` | 6 | — |
| **`Common Features`（新）** | **5** | **+5** |
| `FeaturesEnableCriteria` | 3 | — |
| `StopStartSystemBehavior` | 3 | — |
| `PHEVFeatures` | 1 | — |
| `(無 reqid)` | 1 | `HeatedSteeringWheel-009` |
| **合計** | **237** | |

**左右對稱已回復**：HeatedSeat 15 / 15、VentedSeat 15 / 15。

### 改判逐筆之依據（R-VS37 要求記明）

| leaf | 原 token | 改判為 | 依據（`section` 欄逐字） |
|---|---|---|---|
| `LeftFrontHeatedSeat-004` | `LeftFrontHeatedSeat` | `Common Features` | `1.3.2.1.3.1;1.3.2.1.3.2;1.3.2.1.3.3;1.3.2.1.3.4` |
| `LeftFrontHeatedSeat-011` | `LeftFrontHeatedSeat` | `Common Features` | 同上 |
| `HeatedSteeringWheelManagement-025` | `HeatedSteeringWheelManagement` | `Common Features` ⚠ | `1.3.2.1.3;1.3.3.3.6.1` |
| `HeatedSteeringWheelManagement-026` | 同上 | `Common Features` ⚠ | 同上 |
| `HeatedSteeringWheelManagement-027` | 同上 | `Common Features` ⚠ | 同上 |
| `HeatedSteeringWheel-009` | `HeatedSteeringWheel` | `(無 reqid)` ⚠ | 無 |

> ⚠ **四筆之改判逾出 R-VS37 之文義，未定案**：
> R-VS37 之第二分支為「跨越多個**同層**章節」，而 `1.3.2.1.3`（四段）
> 與 `1.3.3.3.6.1`（五段）**不同層**；R-VS37 亦未規定「無 reqid」之歸屬。
> 本表暫依「多章節即 Common」處理，**該處理無條文依據** ——
> 見上繳 12 §2.3，待分析層補條文。

---

## 原 token 判定表（12 輪 W-41，保留為對照）

| Layer 2 | Layer 3 | leaf | 委派 yes | no | blocked | CFTS044 章節 |
|---|---|---:|---:|---:|---:|---|
| Common Features | `FeaturesEnableCriteria` | 3 | 0 | 3 | 0 | 1.3.4.2.2 |
| Common Features | `PHEVFeatures` | 1 | 0 | 1 | 0 | 1.3.4.2 |
| Common Features | `ScreenOFF` | 6 | 0 | 6 | 0 | 1.3.2.1.29 |
| Common Features | `Stop-StartSystem` | 6 | 0 | 6 | 0 | 1.3.2.1.3.12.1 |
| Common Features | `StopStartSystemBehavior` | 3 | 0 | 3 | 0 | 1.3.3.3.7 |
| Common Features | `SwitchLHD/RHDConfiguration` | 6 | 0 | 6 | 0 | 1.3.2.1.3.13, 1.3.3.3.8 |
| Common Features | `ThirdRowHeadrestDump` | 21 | 0 | 21 | 0 | 1.3.2.1.18, 1.3.2.1.22 |
| Heated Seat | `LeftFrontHeatedSeat` | 17 | 17 | 0 | 0 | 1.3.2.1.3.1（部分列並列 .2/.3/.4） |
| Heated Seat | `RightFrontHeatedSeat` | 15 | 15 | 0 | 0 | 1.3.2.1.3.2 |
| Heated Seat | `OneStageHeatedSeat` | 14 | 12 | 0 | **2** | 1.3.3.3.1.1 |
| Heated Seat | `TwoStagesHeatedSeat` | 20 | 16 | 0 | **4** | 1.3.3.3.2.1 |
| Heated Seat | `ThreeStagesHeatedSeat` | 22 | 20 | 0 | **2** | 1.3.3.3.3.1 |
| Vented Seat | `LeftFrontVentedSeat` | 15 | 15 | 0 | 0 | 1.3.2.1.3.3 |
| Vented Seat | `RightFrontVentedSeat` | 15 | 15 | 0 | 0 | 1.3.2.1.3.4 |
| Vented Seat | `TwoStagesVentedSeatsManagement` | 20 | 16 | 0 | **4** | 1.3.3.3.4.1 |
| Vented Seat | `ThreeStagesVentedSeatsManagement` | 22 | 20 | 0 | **2** | 1.3.3.3.5.1 |
| Heated Steering Wheel | `HeatedSteeringWheel` | 20 | 20 | 0 | 0 | 1.3.2.1.3.11 |
| Heated Steering Wheel | `HeatedSteeringWheelManagement` | 11 | 8 | 0 | **3** | 1.3.3.3.6.1（部分列並列 1.3.2.1.3） |
| **合計** | **18** | **237** | **174** | **46** | **17** | **21 章節** |

四數與 R-VS15（237）、08 包（174 / 46 / 17）、27 包（21 章節）逐項相符。

---

## 草案階段之三項未定，鎖定前須解

1. **`Common Features` 之七個 Layer 3 全數 `delegate = no`（46 / 46）**，
   其 TC 由本 feature 自寫；其餘四個 Layer 2 之 191 leaf 中 174 委派 Comfort、17 blocked。
   **本 feature 之實際自寫量集中於 Common Features。**

2. **階數已在 Layer 3 具名**（`OneStage` / `TwoStages` / `ThreeStages`），
   而 **DR-15 未答**。28 包 §5 判「DR-15 影響者為分支數，不影響 Layer 3 之界定」——
   **本表證實該判正確**：階數是 Layer 3 之切分依據，不是分支。
   惟 **12 輪 W-40(2) 新發現 Comfort 側亦明示 `Multi-Level` / `Single-Level`**
   （5 / 17，見上繳 10 §2.2）—— **該事實可能改變 DR-15 之問法**，鎖定前應併看。

3. **`SwitchLHD/RHDConfiguration` 之 token 含 `/`**，
   若 Layer 3 名稱進入 tc_id 或檔名須先定其轉寫規則。**未定。**

4. **（14 輪 W-46 已處理）`LeftFrontHeatedSeat` 之 `-004`／`-011` 為四側共通需求**
   （其 `section` 逐字含 `.1;.2;.3;.4`，見 A-VS47）。
   **依實質應屬 `Common Features`，本表以 SWE ID 中段 token 機械切分故放錯層。**
   Layer 3 之 17 vs 15 不對稱即源於此 —— **非 037 遺漏**（CFTS044 左右皆 29 條）。
   **未自行搬動**；同型問題是否存在於 Vented 側未掃。
   §1.3.2.1.3.4（RF Vented）之 30 條**已追因**：兩節正規化後之**相異**條文皆為 **28**，
   差 1 源自 RF Vented 多一組重複條文（`4858393`／`4858394`），
   二者僅差 `HS_HI` vs `VS_HI` —— **上游 typo**，見 A-VS49。

5. **`Common Features` 同時是 Layer 2 名稱與（新增之）Layer 3 名稱** ——
   名稱衝突，鎖定前須改名或改層。**未定。**
