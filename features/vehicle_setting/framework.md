# Vehicle Setting —— framework 草案（Layer 1–3）

**狀態：草案，未鎖定。** 依 28 包 §5 之 W-41 產出；
鎖定屬 Tier 2，待 Pei 簽核（P19）。canon §4.1.2 步驟 5 —— **僅列 Layer 1–3，不列個別 RD。**

母體：**237 個 Functional leaf**（R-VS15），取自 037 四本 SWRA。
Layer 3 之界定：037 之 SWE ID 中段 token（`SWE1-VC-<token>-NNN`），**共 18 個**。

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
