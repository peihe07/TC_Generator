# DATA_REQUESTS — FW036 Vehicle Setting

每項含**路徑與 SHA**（G-L：沒有路徑的「到齊」不算到齊）。
`inputs/` 之權威雜湊見 `inputs/INPUTS.sha256`（14 檔，`shasum -a 256 -c` 全數 OK）。

## 已關閉

| # | 項目 | 路徑 | SHA256 | 關閉依據 |
|---|---|---|---|---|
| 1 | CFTS044 原始 docx | `inputs/R1LR_Atl-H_25PI3.5_…CFTS_044_Vehicle Controls_SR26_20250909-1816.docx` | `87fe31774eeab35cf3d209d50f187ace8a756298b7027d139f70e30943ce7060` | 實測 `PK\x03\x04`、28 個 zip member；heading 樣式與 outline map 已建（W-4b） |
| 2 | SYS3 SYSAD 原始 docx | `inputs/SYS3_Vehicle_Settings_FM-WI-FSM-011-A01_…_v1.0.docx` | `469162b81bf3101855089feb87b4a155d4ce867860c194d65d2a901bad08b200` | 已入。**⚠ 內文本輪未複驗**（00C §5-1 之待辦仍未做） |
| 3 | 素材落地並取 SHA | `inputs/`（14 檔） | 見 `INPUTS.sha256` | W-1 完成；三個分析層沙箱 SHA 與 repo 實體檔相符 |
| 4 | `$HSW_StatFailSts$` 值域 | — | — | **除名**（00B §0：規格以訊號路徑記法給出） |
| 4b | `$TGW_DISP_STAT$` 讀取途徑 | `inputs/PDT27_E2A_R4_BHCAN.dbc` / `…R5_FDCAN8.dbc` | `9ef1ec98…`／`51c8fd60…` | 實測 `TGW_DISP_STATSts` 於 `TELEMATIC_DISPLAY2(1500)` 與 `TELEMATIC_FD_4(1427)` |
| 5c | Pop Up List／HMI Settings List／Market Configuration | — | — | **不請求**（CFTS044 對 `Pop Up`／`Settings List` 命中 0） |

## 仍開啟

| # | 項目 | 為何需要 | 阻塞 | Urgency |
|---|---|---|---|---|
| **5-A** | `Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf` 自 `…/26PI2.5/HMI/` 入 `inputs/` | 16 leaf 之按鍵循環、LED 數、highlight 狀態 | 該 16 leaf 之可觀察 ER | **待 Pei 授權**（Tier 3；本輪未複製，禁區所限） |
| **5-B** | 失效彈窗內容 ＋ 加熱方向盤圖示之左右駕鏡像 | CFTS044 之 `Refer to TLM HMI Document`／`Refer to PDO graphics` 所指 | 畫面層 ER | **RD-1 提問**（上游從未具名） |
| **7** | PROXI 表 —— `Heated_Seats`／`Heated_Seat_Levels`／`Heated_Steering_Wheel`／`DSP_SK_PRSNT` 之值域 | LID 表之 `Format` 欄逐字為 `See Proxi Table`，值域被轉指出去 | 該四 LID 之值域佐證（CFTS044 有內嵌值可用） | Medium |
| **8** | `$VC_VEH_LINE$` 之完整車型碼對照 | LID 表之列舉截斷於 `101 = WL (65 Hex) # = Not Used`；CFTS044 所用之 `DT`／`WS`／`HDCC`／`M240` 全不在內 | 8 個引用 | Medium |
| **9（新）** | `SWE1-VC-HeatedSteeringWheel-009` 之正確 `Source Requirement ID` | 其值逐字為 `SYS-RA-CFTS100` —— 指向 CFTS100 且無 `-N` 序號，錨鏈斷 | 該 1 leaf 之 `specification_reference` | **High**（成對 A-VS12） |
| **10（新）** | 5 個跨章節 leaf 之 `specification_reference` 該取哪一章節 | `LeftFrontHeatedSeat-004`／`-011` 各落 4 章節；`HeatedSteeringWheelManagement-025`／`-026`／`-027` 各落 2 章節 | 該 5 leaf 之 N 欄 | **High**（成對 A-VS14；屬裁決非索檔） |

## 已查而不取用（G-D 留痕）

**已查 `features/comfort/inputs/` 三份**（`HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx`、
`Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx`、`SR24 R1 Market Configuration Table v1.6.xlsx`）
**與 26PI2.5/HMI 四份**（Comfort HMI L&F、Hard Controls HMI L&F、Pop Up List HMI R1 (26PI)、
HMI Settings List R1 SR25 Post R1L-R），**本 feature 條文不引用者不取用**。

> ⚠ **此句在本輪為「照錄分析層之結論」，非執行層複驗**。
> 前三份之「不引用」依據為 00A §2 之 DR-5c（CFTS044 對 `Pop Up`／`Settings List` 命中 0），
> 該掃描本輪**未重跑**；後四份之逐份實測為 00D，本輪**未重跑**（W-13 未執行）。

**已入 `inputs/` 而不取用**：
`PDO Graphics Release - SR24_SR25_Post2A_CR27516_CR27517.pdf`（`7c26bb93…`）、
`PDO Theme Config V3.4.xlsx`（`0079740c…`）——依 00C §3 判為內容不符；**本輪未複驗**。
`PDT25_E3A_R4_FDCAN8_vs_PDT25_E3A_R5_FDCAN8.xlsx`（`74d11e1b…`）——證據性素材，
依 R-VS12 入庫目的為存證非取值。

## DR-14′（取代 DR-14，14 包 §2）

LID 表載 `HdRstRelRq` 之 Atlantis High 對映為 `RADIO_B3.HDRstRelRq_3rdRow`，
但基線 DBC 之 `RADIO_B3` 不含該 signal（其 4 支為 `ManDispCtrl` /
`PowerSideStep_Req` / `RQ_DISP_INTS` / `VR_Blower_Req`）；
兩份 DBC 全域僅有 `Driver_Headrest_Req` 與 `Passenger_Headrest_Req`，無第三排。

請確認第三排頭枕釋放請求之實際 signal 名與所屬 message，
或該功能於本專案是否不落在此二網段。

**影響**：037 引用 `$HdRstRelRq$` 之 16 處，其 procedure 之操作步驟需要此訊號。
**Urgency**：Medium（由 DR-14 之 High 降級 —— 範圍自 8 支縮為 1 支）。

> **DR-13 撤銷**（14 包 §1）：`$ESS_ENG_ST$` 之 message 歸屬非矛盾，係執行層未展開 LID 單格多值。

## DR-15（新，**Urgency High** —— 排在 framework 之前）

**兩造皆 in-scope，非架構差異可吸收者。**

**CFTS044 側**：條文 **`4858325`（`$FL_HS_RQ$`）／`4858355`（`$FR_HS_RQ$`）／
`4858385`（`$FL_VS_RQ_TGW$`）／`4858416`（`$FR_VS_RQ_TGW$`）**，
標籤逐字 `[EE Architecture:Atlantis High]`，載請求訊號**承載階數且為循環降階**：

> **引用更正（29 包 §2.2，13 輪 D-3 執行）**：本條原引 `4858356` 與 `4858386`，
> 該二條實為**接收側**（`When the HU receives a $HeatedSeatFR$ = [HS_OFF] signal,
> the HU shall change the stored status…`），非請求側。
> 成因為以命中位置取「前一個 7 位數」而未以區塊邊界驗證歸屬（A-VS45）。
> **本 DR 尚未送出，更正無外部代價。**
High → `[Medium]`、Medium → `[Low]`、Low → `[Off]`、Off → `[High]`。

**LID ＋ DBC 側**：LID 之 Atlantis High 欄組將其對映至
`TELEMATIC_VEHICLE_SETUP3.<X>_Tlm`；基線 DBC 實測
`FL_HS_Tlm`／`FR_HS_Tlm`／`FL_VS_Tlm`／`HSW_Tlm` **皆為 1 bit**，
`VAL_` 為 `0 "Not_Pressed"` / `1 "Pressed"`。

> `Pressed / Not Pressed` 之四階對照另見於 `4857991` 等條文，
> 其標籤為 `[EE Architecture:CUSW]`，依 R-VS19 不取用 ——
> **故此衝突無法以架構差異解釋。**

### 提問（RD-1，可直接送出）

> CFTS044 條文 4858325 / 4858355 / 4858385 / 4858416
> （皆 `[EE Architecture:Atlantis High]`）定義
> `$FL_HS_RQ$` / `$FR_HS_RQ$` / `$FL_VS_RQ_TGW$` / `$FR_VS_RQ_TGW$`
> 依目前座椅狀態送出 `Medium` / `Low` / `Off` / `High` 之循環降階值。
>
> 惟基線 CAN 資料庫 `PDT27_E2A_R4_BHCAN.dbc` 中，
> `TELEMATIC_VEHICLE_SETUP3` 之 `FL_HS_Tlm` / `FR_HS_Tlm` /
> `FL_VS_Tlm` / `HSW_Tlm` 皆為 **1 bit**，值表為
> `0 = Not_Pressed`、`1 = Pressed`；
> `Logical Identifiers and CAN Mapping v1.76` 之 Atlantis High 欄組
> 亦將該等請求對映至上述 1 bit 訊號。
>
> 請確認 Atlantis High 之實作為何者：
> (a) 請求訊號為 1 bit，階數之循環由 HU 內部狀態機決定；或
> (b) 請求訊號承載階數，則其實際 signal 名／bit 寬／值表為何。
>
> 影響：Heated Seat 與 Vented Seat 兩個 Test Set 之 procedure、
> expected_result 與設計方法（Functional Based vs Decision Table），
> 涉及 160 個 Functional leaf。

**阻塞**：`Heated Seat`（88 leaf）與 `Vented Seat`（72 leaf）之**分支結構**
—— 即 framework Part Vehicle Setting 之 Layer 3 與設計方法。
**配對 A-VS30。**

> **DR-16 撤銷**（24 包 §0）：分析層以自身假設之 `CFTS044-NNNN` 形態掃描，
> 掃出 4/237 後把「我方假設之形態找不到」記成「素材缺對照」。
> 實測 reqid 即 SYS2 `Source Requirement items` 之 7 位數，覆蓋 **236 / 237**
> （唯一無值者為 `SWE1-VC-HeatedSteeringWheel-009`，即 DR-11）。**不向上游提出。**


### DR-14′ 之追問文字（定稿，W-35）

> `Logical Identifiers and CAN Mapping v1.76` 之 Atlantis High 欄組將
> `HdRstRelRq` 對映至 `RADIO_B3.HDRstRelRq_3rdRow`。
>
> 惟基線 CAN 資料庫 `PDT27_E2A_R4_BHCAN.dbc` 之 `RADIO_B3` 不含該 signal
> —— 其四支 signal 為 `ManDispCtrl` / `PowerSideStep_Req` /
> `RQ_DISP_INTS` / `VR_Blower_Req`。
> 兩份 DBC（`R4_BHCAN`、`R5_FDCAN8`）全域僅有 `Driver_Headrest_Req`
> 與 `Passenger_Headrest_Req`，**無第三排**。
>
> 請確認第三排頭枕釋放請求之實際 signal 名與所屬 message，
> 或該功能於本專案是否不落在此二網段。
>
> **影響**：037 引用 `$HdRstRelRq$` 之條文，其 procedure 之操作步驟需要此訊號；
> 涉及 `SWE1-VC-ThirdRowHeadrestDump-033` / `-034` / `-035` / `-036` 四 leaf
> 之按鍵請求步驟。
> **Urgency**：Medium。

> **（追問，29 包 §2.3 加入）** 階數本身為配置維度 ——
> CFTS044 以 `$Heated_Seat_Levels$ = [1] / [2] / [3]` 表達，
> 而 Comfort（CFTS043）側寫作 `Single-Level` / `Multi-Level`。
> **請求訊號之行為是否隨 `$Heated_Seat_Levels$` 之配置而不同？**
> 例如 `Levels = 1` 時請求訊號為 1 bit，`Levels = 3` 時承載階數。
> CFTS044 未明言此點。

## DR-17（新，**Urgency High** —— 分析層擬，Pei 送出）

**Comfort 側沒有任何「單階座椅」之條文。**

CFTS044 定義單階加熱座椅之配置（`$Heated_Seat_Levels$ = [1]`），
本 feature 有 **14 個** 對應之 SWE leaf（`SWE1-VC-OneStageHeatedSeat-*`），
其中 **12 個已委派**。

而 Comfort HMI Logic and Flow（`SWE1-HVAC-*`，全母體 **129** 個相異 leaf）中，
所有座椅加熱／通風之畫面行為條文，其開頭皆逐字為
`For Multi-Level Heated/Vented seats`；
明示 `Single-Level` 者僅 `SWE1-HVAC-063`，**且其主詞為加熱方向盤**。
以 `single[\s-]?level` ∧ `seats?` 交叉查詢 **命中 0**。

### 提問（RD-1）

> 請確認單階加熱座椅之畫面行為：
>
> (a) 由 Comfort 之某條文涵蓋而未明示階數？若是，請指明其 leaf id
> (b) 單階座椅無彈窗、直接切換，故 Comfort 無對應條文？
> (c) 該行為由第三份文件承載（如 TLM HMI Document）？

**影響**：14 個 `OneStageHeatedSeat` leaf 之委派界線（R-VS7）。
在答覆前，該 12 個已委派之 leaf 其委派標的與其配置條件矛盾。

**狀態：未送出**（送出屬 Pei）。配對 anomaly：A-VS46。
