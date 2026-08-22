# Vehicle Setting —— framework（Layer 1–3）

**狀態：已簽核並鎖定。** Pei 於 2026-08-20 簽核（P19，Tier 2），19 輪 D-5 落鎖。

```
P19（Pei 2026-08-20：簽核）
`features/vehicle_setting/framework.md` 之三層結構定案並鎖定：

  Layer 1  `Vehicle Setting`（R-VS3′）
  Layer 2  `Common Features` 46／`Heated Seat` 88／`Vented Seat` 72／
           `Heated Steering Wheel` 31 ＝ 237（R-VS4、R-VS15）
  Layer 3  19 個，依 R-VS37′ 四分支以 CFTS044 章節判定

簽核之依據（皆已實測）：
  Layer 2 歸屬以 037 檔界逐 leaf 驗證，**0 / 237 不一致**（16 輪 W-52）
  Layer 2 四數與 R-VS15 逐項相符
  左右對稱 HeatedSeat 15/15、VentedSeat 15/15
  分支使用 (1)231／(2)2／(3)3／(4)1 ＝ 237
  token 判定與章節判定不一致者 2，皆逐筆記明依據

**簽核不涵蓋**（各自另有其關卡）：
  TC 內容（pilot review）
  委派狀態之逐 leaf 正確性（R-VS7(a)′ 為群層級）
  未結 DR 之答覆
```

```
Layer 3 名稱之轉寫（36 包 §2.1，隨本次簽核生效）
`framework.md` 內之顯示名維持 `SwitchLHD/RHDConfiguration`（037 之逐字）。
凡用於檔名、批次名、或任何不接受 `/` 之識別碼者，
取其**正規化形式** `SwitchLHDRHDConfiguration`（去 `/`，不補底線）。
兩者於 Layer 3 表並列，逐字對照。
```

**重開條件**：新 RD 無法對映入現行三層；或 Layer 2 四數因上游改版而變動；
或 pilot review 發現之缺陷可追溯至分層本身。**重開屬 Tier 2（Pei）。**

---

**原草案標題保留加註**（R-TM13）：本檔原題為
「Vehicle Setting —— framework 草案（Layer 1–3）」，狀態「草案，未鎖定」。

依 28 包 §5 之 W-41 產出，14 輪 W-46 依 R-VS37 重判；
canon §4.1.2 步驟 5 —— **僅列 Layer 1–3，不列個別 RD。**

母體：**237 個 Functional leaf**（R-VS15），取自 037 四本 SWRA。
Layer 3 之界定：**依 R-VS37′ 四分支以 `reqid_list` 所跨之 CFTS044 章節判定**，
SWE ID 中段 token 僅為預設值。**共 19 個**（含新增之 `Common Features` 與 1 個無 reqid）。

## 依 R-VS37′ 之章節判定（15 輪 W-49，取代下方 token 判定表）

| Layer 2 | Layer 3 | **正規化名**（檔名／批次名用） | leaf | yes | no | blocked | pending |
|---|---|---|---:|---:|---:|---:|---:|
| Heated Seat | `ThreeStagesHeatedSeat` | `ThreeStagesHeatedSeat` | 22 | 20 | 0 | 2 | 0 |
| Vented Seat | `ThreeStagesVentedSeatsManagement` | `ThreeStagesVentedSeatsManagement` | 22 | 20 | 0 | 2 | 0 |
| Common Features | `ThirdRowHeadrestDump` | `ThirdRowHeadrestDump` | 21 | 0 | 21 | 0 | 0 |
| Heated Seat | `TwoStagesHeatedSeat` | `TwoStagesHeatedSeat` | 20 | 16 | 0 | 4 | 0 |
| Heated Steering Wheel | `HeatedSteeringWheel` | `HeatedSteeringWheel` | 20 | 20 | 0 | 0 | 0 |
| Vented Seat | `TwoStagesVentedSeatsManagement` | `TwoStagesVentedSeatsManagement` | 20 | 16 | 0 | 4 | 0 |
| Heated Seat | `LeftFrontHeatedSeat` | `LeftFrontHeatedSeat` | 15 | 15 | 0 | 0 | 0 |
| Heated Seat | `RightFrontHeatedSeat` | `RightFrontHeatedSeat` | 15 | 15 | 0 | 0 | 0 |
| Vented Seat | `LeftFrontVentedSeat` | `LeftFrontVentedSeat` | 15 | 15 | 0 | 0 | 0 |
| Vented Seat | `RightFrontVentedSeat` | `RightFrontVentedSeat` | 15 | 15 | 0 | 0 | 0 |
| Heated Seat | `OneStageHeatedSeat` | `OneStageHeatedSeat` | 14 | 0 | 0 | 2 | **12** |
| Heated Steering Wheel | `HeatedSteeringWheelManagement` | `HeatedSteeringWheelManagement` | 11 | 8 | 0 | 3 | 0 |
| Common Features | `Stop-StartSystem` | `Stop-StartSystem` | 6 | 0 | 6 | 0 | 0 |
| Common Features | `SwitchLHD/RHDConfiguration` | `SwitchLHDRHDConfiguration` | 6 | 0 | 6 | 0 | 0 |
| Common Features | `ScreenOFF` | `ScreenOFF` | 6 | 0 | 6 | 0 | 0 |
| Common Features | `FeaturesEnableCriteria` | `FeaturesEnableCriteria` | 3 | 0 | 3 | 0 | 0 |
| Common Features | `StopStartSystemBehavior` | `StopStartSystemBehavior` | 3 | 0 | 3 | 0 | 0 |
| Heated Seat | **`CrossZone Common`** | **`CrossZoneCommon`** | 2 | 2 | 0 | 0 | 0 |
| Common Features | `PHEVFeatures` | `PHEVFeatures` | 1 | 0 | 1 | 0 | 0 |
| **合計** | **19** | — | **237** | **162** | **46** | **17** | **12** |

**Layer 2 合計 46／88／72／31 —— 與 R-VS15 逐項相符。**
**左右對稱：HeatedSeat 15/15、VentedSeat 15/15。**

### 分支使用（R-VS37′）

| 分支 | 筆數 |
|---|---:|
| (1) 單一章節 | 231 |
| (2) 跨同層 → `CrossZone Common` | 2 |
| (3) 跨異層 → 取最深 | 3 |
| (4) 無 reqid → token 預設值 | 1 |

### 改判與標記逐筆（R-VS37′ 要求記明）

| leaf | 原 token | 判定 | 分支 | 依據（`section` 逐字） |
|---|---|---|---|---|
| `LeftFrontHeatedSeat-004` | `LeftFrontHeatedSeat` | **`CrossZone Common`** | (2) | `1.3.2.1.3.1;1.3.2.1.3.2;1.3.2.1.3.3;1.3.2.1.3.4` |
| `LeftFrontHeatedSeat-011` | `LeftFrontHeatedSeat` | **`CrossZone Common`** | (2) | 同上 |
| `HeatedSteeringWheelManagement-025` | HSWManagement | `HeatedSteeringWheelManagement`（不變） | (3) | 取最深 `1.3.3.3.6.1` |
| `HeatedSteeringWheelManagement-026` | 同上 | 同上 | (3) | 同上 |
| `HeatedSteeringWheelManagement-027` | 同上 | 同上 | (3) | 同上 |
| `HeatedSteeringWheel-009` | HeatedSteeringWheel | `HeatedSteeringWheel`（不變），標 **`UNRESOLVED-SOURCE / DR-11`** | (4) | 無 reqid；Source 為 `SYS-RA-CFTS100` |

**token 判定與章節判定不一致者：2**（14 輪為 6；R-VS37′(3) 使 3 筆回歸一致，(4) 使 1 筆回歸一致）。

---

## 鎖定前尚未解之項目（W-52(2)，16 輪更新）

| # | 項目 | 阻塞？ | 所待 |
|---|---|---|---|
| 1 | ~~R-VS19′ 主文與 (a) 段互斥~~ **已解**（**R-VS19″**，34 包 §1）：採讀法一，`EE Architecture` 僅排除 `CUSW`／`PowerNet` 專屬者。定案數字 in-scope **425**／21 節內 **259**／未覆蓋 **8**／覆蓋率 **96.9%**／落外 **0**／**(a) = 0**。43 條為 out-of-scope，不歸因。A-VS55 關閉 | **不再阻塞** | — |
| 2 | **DR-15** — 請求訊號 1 bit vs 承載階數 | **阻塞** | **已送出（2026-08-22，送件文第 1 項）—— 待覆** |
| 3 | **DR-17** — Comfort 側無單階座椅條文（14 leaf／12 `pending`） | **阻塞** | **已送出（2026-08-22，送件文第 2 項）—— 待覆** |
| 4 | **DR-11** — `HeatedSteeringWheel-009` 之來源（`SYS-RA-CFTS100`） | 不阻塞 | 該 leaf 已標 `UNRESOLVED-SOURCE` |
| 5 | **DR-18** — 座椅值域之四類書寫問題 | **不阻塞（確認型）** | **未送出**（送件文第 6 項，本次僅送 1–5） |
| 6 | A-VS51 — `4858413` 值退化為 `[ Pressed]` | 不阻塞 | 併 DR-18 |
| 7 | A-VS52／A-VS56 — 大小寫重複影響 **12 個 token** | 不阻塞 | 已依 **R-VS39** 以 `normalized_key` 處理 |
| 8 | ~~`SwitchLHD/RHDConfiguration` 之 `/` 轉寫~~ **已解**（36 包 §2.1）：Layer 3 不入工作簿（§4.1.5）亦不入 `tc_id`（§10.3），唯一受影響者為 `generated/` 之檔名／批次名，取正規化名 `SwitchLHDRHDConfiguration` | **不再阻塞** | — |
| 9 | `$HSW_StatFailSts$` 之 R-VS20 階梯歸屬（R-VS19″ 承 R-VS19′(d) 令其重查） | 不阻塞 | **凍結**：`BACKLOG.md` B-02（R-VS40） |
| 10 | ~~訊號書寫形式衝突~~ **已解**（**R-VS41**，35 包 §1）：三件組撤回，改依 canon §8.7.5 v3；網段入 Pre-Condition。profile 已建。A-VS57／60／61 關閉 | **不再阻塞** | — |
| 11 | **DR-19** — `EngRun_Stat` 之規格值於 LID／DBC 無對應 | **阻塞 1 leaf**（`-006` 已移出批次；`-004`／`-005` 保留 PENDING） | **已送出（送件文第 4 項）—— 待覆**；A-VS58 |
| 12 | **DR-20** — `4858560` 交叉參照未具名之 HMI 需求 | **阻塞 1 leaf**（已移出批次） | **已送出（送件文第 5 項）—— 待覆**；A-VS59 |

**已解者**：`Common Features` 名稱衝突（→ `CrossZone Common`）；
**Layer 2 歸屬已以 037 檔界逐 leaf 驗證，0 / 237 不一致**（W-52(1)）——
`CrossZone Common` 之 2 leaf 確實出自 `HeatedSeat.xlsx`（15 輪 §6-4 之待驗項已閉）。

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

5. ~~`Common Features` 同時是 Layer 2 與 Layer 3 名稱~~ **已解**（15 輪）：
   Layer 3 之跨區共通桶改名 `CrossZone Common`（31 包 §2）。**本項為過期記載。**
