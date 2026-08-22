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

**型別（R-VS45）：**型 A**（規格缺陷）**

**狀態：已送出（Pei，2026-08-22，37 包送件文第 3 項）—— 待覆。**

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

**型別（R-VS45）：**型 A**（規格缺陷）**

**狀態：已送出（Pei，2026-08-22，37 包送件文第 1 項）—— 待覆。**

> **補充觀察（32 輪 D-3，依 52 包 §2；本段為我方之觀察，
> **不作為本 DR 之答覆**，本 DR 之待覆狀態不變 —— R-VS44）**
>
> 我方於 LID v1.76 列 769 觀察到：同一 LID `FL_VS_RQ_TGW` 於
> `Atlantis` 欄組對映至 `TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm`
> （2 bit、四階），於 `Atlantis High` 欄組對映至
> `TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm`（1 bit、Not_Pressed/Pressed）。
> 而 CFTS044 描述循環降階之條文（4858325／4858355／4858385／4858416）
> 標記為 `[EE Architecture:Atlantis High]`。
> 請確認該等條文之架構標記是否正確，或其所述行為是否屬 Atlantis Mid。
>
> **此觀察指出「1 bit」與「承載階數」兩者可能皆為真而分屬不同架構。
> 我方不以之作答**；`guard()` 之 DR-15 範圍不變（token 級，五個 token）。

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

**型別（R-VS45）：**型 A**（規格缺陷）**

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

**狀態：已送出（Pei，2026-08-22，37 包送件文第 2 項）—— 待覆。** 配對 anomaly：A-VS46。

## DR-18（新，**Urgency Medium** —— **確認型，不阻塞**；分析層擬，Pei 送出）

**型別（R-VS45）：**型 A**（規格缺陷）**

CFTS044 之座椅相關值域中，發現四類書寫問題，請確認其為筆誤或另有語意：

### 一、加熱／通風前綴交叉（4 筆 ＋ **LID 側 2 筆，32 輪 D-3 併入**）

> **併入 A-VS97（32 輪 D-3，依 52 包 §3）** —— 同型，**惟其在 LID 而非 CFTS044**：
>
> ```
> CAN Mapping 列 769  FL_VS_RQ_TGW  Atlantis 欄組
>     Format: Atlantis / 2 bit signal / 0 = Vented_Seat_Off / 1 = Vented_Seat_Low / …
> CAN Mapping 列 770  FL_VS_RQ_TGW2 Atlantis 欄組（同一 Signal Name FL_VS_Cmd_Tlm）
>     Format: 0 = Heated_seat_off / 1 = Heated_seat_low / 2 = Heated_seat_medium / 3 = Heated_seat_high
> CAN Mapping 列 790  FR_VS_RQ_TGW2 Atlantis 欄組（Signal Name FR_VS_Cmd_Tlm）
>     Format: 0 = Heated_seat_off / … / 3 = Heated_seat_high
> ```
>
> **同一訊號 `FL_VS_Cmd_Tlm` 在同一表內有兩個相衝之值域。**
> 52 包 §3 依 **R-VS38** 三項聯合判準裁：取 **`Vented_Seat_*`**，
> 列 770／790 之 `Heated_seat_*` 判為 LID 之轉錄錯誤；
> `spec_variables.tsv` 增 `suspect_prefix` 標記，**不改原值**。
> **請一併確認。**


```
4858393  §1.3.2.1.3.4  $VentedSeatFR$ = [Vented Seat High / HS_HI]
4858001  §1.3.1.1.3.4  $VentedSeatFR$ = [Vented Seat High/HS_HI]
4860021  §1.3.4.12.4   $VentedSeatFR$ = [Vented Seat Off / HS_OFF]
4860015  §1.3.4.12.3   $VentedSeatFL$ = [Vented Seat Off / HS_OFF]
```

對照：同章節內其餘同型條文一律 `VS_`；全文 `VS_OFF` 15 次對 `HS_OFF` 2 次。
我方判為筆誤，請確認。

### 二、值退化（1 筆）

```
4858413  §1.3.2.1.3.4  $CCDMF_FR_VS_RQ$ = [ Pressed]
```

其左側對稱條文 `4858382` 為 `[Vented Seat Pressed / VS_PSD]`。
請確認 `4858413` 應為 `[Vented Seat Pressed / VS_PSD]`。

### 三、同一值之多種大小寫寫法

```
[Vented Seat Low / VS_LO] 5 次 ／ [Vented Seat Low / VS_Lo] 4 次
[Vented Seat Medium / VS_MED] 2 ／ [Vented seat Medium / VS_MED] 2
  ／ [Vented seat medium / VS_MED] 4
```

請確認其為同一值。

### 四、參數名筆誤

`$Heated_Steats_Levels$`（`Steats`）與 `$Heated_Seats_Levels$` 並存，
前者於 `Logical Identifiers and CAN Mapping` 之 2,974 個 LID 中無對應。

### 影響

座椅加熱／通風之值域列舉分支數，涉及 Heated Seat 88 ＋ Vented Seat 72
共 **160 個 SWE leaf**。
我方已依內部判準處理（正規化計數、原值保留），**本請求為確認而非阻塞**。

**狀態：未送出** —— 37 包送件文第 6 項，**Pei 本次僅送 1–5**，本項維持待送。配對 anomaly：A-VS49／A-VS51／A-VS52／A-VS53。

## DR-19（**併入 DR-21**，R-VS42；原編號保留 —— R-TM13。已於 2026-08-22 送出，待覆）

**型別（R-VS45）：**型 A**（規格缺陷；併入 DR-21）**

**`EngRun_Stat` 之規格值於 LID 與 DBC 皆無對應。**

CFTS044 之 `4858551`／`4858553`／`4858555` 以
`$EngRun_Stat$ = [IDLE_STBL//UNLIMITED//LIMITED//RUN]`（或其否定）為觸發條件。

實測：

| 來源 | `EngRun_Stat` 之值域 |
|---|---|
| LID `Format` 欄 | `0 = Engine_Off`／`1 = Engine_Cranking`／`2 = Engine_On`／`3 = SNA` |
| 基線 DBC `EngineSts`（`STATUS_CCAN3`, id 994） | 同上，逐字相同 |
| CFTS044 所用 | `IDLE_STBL` / `UNLIMITED` / `LIMITED` / `RUN`（另有一處 `Engine_On`） |

`IDLE_STBL`／`UNLIMITED`／`LIMITED`／`RUN` **在 LID 與 DBC 中皆不存在**。
依 **R-VS9(2)**「兩者不一致時停下回報，不自行調和」，本層未作任何對映。

**影響**：`SWE1-VC-Stop-StartSystem-004`／`-005`／`-006` 三個 leaf 之 TC
無法決定應送出之匯流排值，已依 §8.4.3 於 `test_procedure`／`expected_result`
填 `PENDING: DR-19`。

### 提問（RD-1，35 包 §3 全文，分析層擬）

> CFTS044 條文 4858551／4858553／4858555（`[EE Architecture:Atlantis High]`）
> 以 `$EngRun_Stat$ = [IDLE_STBL]`／`[UNLIMITED]`／`[LIMITED]`／`[RUN]`
> 為 Stop/Start 開關可用性之判定條件。
>
> 惟 `Logical Identifiers and CAN Mapping v1.76` 將 `EngRun_Stat` 對映至
> `STATUS_CCAN3.EngineSts`（Atlantis High 欄組），
> 其 Format 與基線 DBC `PDT27_E2A_R4_BHCAN.dbc` 之 `VAL_` 皆為
> `0 = Engine_Off`／`1 = Engine_Cranking`／`2 = Engine_On`／`3 = SNA`。
> **四個規格值於 LID 與 DBC 中皆無對應。**
>
> 請提供 `IDLE_STBL`／`UNLIMITED`／`LIMITED`／`RUN` 之匯流排對應
> （訊號名、message、值），或確認其應改用他訊號。
> 影響：SWE1-VC-Stop-StartSystem-004／-005／-006 三個 leaf 之 procedure
> 與 expected_result 無法在不編造值之下寫出。

配對 anomaly：A-VS58。**狀態：已送出（Pei，2026-08-22，37 包送件文第 4 項）—— 待覆。**

## DR-20（**搜尋已停止，44 包 §2**；**併入 DR-23**，R-VS42；原編號保留 —— R-TM13。已於 2026-08-22 送出，待覆）

**型別（R-VS45）：**型 B**（素材缺件：未具名之 HMI 需求文件；併入 DR-23）**

**`4858560` 交叉參照未具名之 HMI 需求。**

條文逐字：`When $DriverSide$ = [Right hand drive] the HMI shall be modified as
defined by HMI requirements.`

「HMI requirements」未具名任何文件、章節或需求 ID，故無可判定之修改項。
依 §8.4.2，其修改內容若定義於外部規格，屬該規格所有者，
本 TC 不得吸收；依 §8.4.3 以 `PENDING: DR-20` 佔位。

**影響**：`SWE1-VC-SwitchLHD/RHDConfiguration-010`。
其 canon §9 檢查 5（§5.5 末步驟須擁有驗證）**因此不通過**，
在本 DR 答覆前無法修正。

### 提問（RD-1，35 包 §3 全文，分析層擬）

> CFTS044 條文 4858560（`[EE Architecture:Atlantis High]`）逐字為
> `… the HMI shall be modified as defined by HMI requirements.`
> —— **未具名任何文件、章節或需求 ID**。
>
> 我方已查 26PI2.5/HMI 之全部 107 檔（含對無文字層 PDF 施以旋轉 OCR），
> 未能定位其所指之 HMI 需求。
>
> 請指明該 HMI 需求之文件與章節。
> 影響：SWE1-VC-SwitchLHD/RHDConfiguration-010 之末步驟無可寫之驗證目標；
> 寫具體修改項即為造值（§8.4.1），寫「HMI is modified」則不可觀察（§6）。
> 現以 `PENDING: DR-20` 佔位。

配對 anomaly：A-VS59。**狀態：已送出（Pei，2026-08-22，37 包送件文第 5 項）—— 待覆。**

## DR-21（**類別式，B2**，依 **R-VS42** 改制於 20 輪；Urgency High）

**型別（R-VS45）：**型 A**（規格缺陷，B2 類）**

**類別：規格值於 LID 與 DBC 皆無對應。**

**併入本類者**：**DR-19**（`EngRun_Stat` 四值，**已於 2026-08-22 單獨送出**）、
**DR-12**（`IGN_OFF_ACC`，29 包 §1.2 開立）。
> 本類別包含已於 2026-08-22 送出之 **DR-19**，其為本類之實例。

**影響範圍（31 輪依 R-VS50 回查重估；取代 20 輪之「82 個 leaf」）**：
**137 個 leaf**、215 次命中、**27 個相異 token**。

逐 token 之 leaf 數（全表，非「主要」）：

| token | leaf | token | leaf |
|---|---:|---|---:|
| `HeatedSeatFL` | 22 | `Heated_Steats_Levels` | 4 |
| `HeatedSeatFR` | 22 | `HSW_Cmd_Tlm` | 4 |
| `VentedSeatFL` | 20 | `ESS_ENG_ST` | 2 |
| `VentedSeatFR` | 20 | `VC_VEH_LINE` | 2 |
| `FL_HS_Cmd_Tlm` | 16 | `PowerMode` | 2 |
| `FR_HS_Cmd_Tlm` | 16 | `FL_HS_RQ` | 2 |
| `Hybrid_Type` | 14 | `FR_HS_RQ` | 2 |
| `FL_VS_Cmd_Tlm` | 14 | `FL_VS_RQ_TGW` | 2 |
| `FR_VS_Cmd_Tlm` | 14 | `FR_VS_RQ_TGW` | 2 |
| `EngRun_Stat` | 12 | `DSP_SK_PRSNT` | 1 |
| `Heated_Seat_Levels` | 5 | `Heated_Steering_Levels` | 1 |
| `PrplsnSysAtv` | 5 | `HSW_RQ_TGW` | 1 |
| `HSW_Stat_2` | 5 | `Heated_Steering_Wheel` | 1 |
| `HdRstRelRq` | 4 | | |

**依 R-VS50 之群組回查（相異 leaf，非累加）**：

| 群 | 相異 leaf |
|---|---:|
| `HeatedSeatFL`／`FR`／`VentedSeatFL`／`FR` | **84** |
| `*_Cmd_Tlm` 四者 | **60** |
| HSW 系（5 token） | 12 |

**與此前之優先序不符**：24～51 包以 `*_Cmd_Tlm`「61 leaf」為單一最大解鎖，
實際最大群為 `HeatedSeat*`／`VentedSeat*` 四者之 **84 leaf**。
20 輪所載之「82 個 leaf」與其逐 token 次數（`PowerMode` 10、`DriverSide` 6 等）
亦與現行掃描不符 —— 其為 W-59／W-77／W-80 三次改判前之計數，
本次不追改該歷史記載，僅以本節取代其作為決策依據之地位。
逐列見 `docs/reports/writability.tsv`。

**我方之掃描條件與其盲區**見上繳 18 §4。

---

### （原逐實例條文，保留 —— R-TM13）

## ~~DR-21（新，Urgency High —— 阻塞 2 個 leaf；17 輪 W-53 開立）~~

**`$PowerMode$` 之 `IGN_START` 與 `IGN_OFF_ACC` 於基線 DBC 無對應值。**

LID 表將 `PowerMode` 對映至 `STATUS_BH_BCM2.CmdIgnSts`（Atlantis High 欄組），
其 Format 與兩份基線 DBC 之 `VAL_` 皆為：

```
0 = Initialization   1 = IGN_LK   3 = ACC   4 = RUN   5 = START   7 = SNA
```

CFTS044 所用之值與其對應狀況（全文實測次數）：

| CFTS044 值 | 次數 | DBC 對應 | 判 |
|---|---:|---|---|
| `[Ignition lock / IGN_LK]` | 11 | `1 (IGN_LK)` | **逐字相符，可用** |
| `[4h:Ignition run]` | 5 | `4 (RUN)` | **CFTS044 自載原始碼值 `4h`，可用** |
| `[IGN_RUN]`／`[Ignition run / IGN_RUN]`／`[Ignition run]` | 20／5／9 | 同上 | 依 `4h` 之並列可用 |
| **`[Ignition start / IGN_START]`** | **3** | 無（DBC 為 `START`） | **無對應，且無原始碼值** |
| **`[Ign. off & acc. (4 position switch) / IGN_OFF_ACC]`** | **4** | 無 | **無對應** |
| `[Ignition off (5 position switch) / IGN_OFF]`／`[IGN_OFF]` | 1／1 | 無 | 本批未涉 |

依 **R-VS9(2)**「兩者不一致時停下回報，不自行調和」，本層未把 `IGN_START` 讀為 `START`。

**影響**：`SWE1-VC-ThirdRowHeadrestDump-029`（IGN_START）與 `-031`（IGN_OFF_ACC）。

> **與 37 包送件文第 8 項之關係**：該項已就 `4858978`（Second Row Headrest Dump）
> 提出 `IGN_OFF_ACC` 之同一問題，**惟其未送出且無 DR 編號**。
> 本 DR 併同 `IGN_START` 一併提出，範圍及於 Third Row。

**提問文待分析層擬**（本層不代擬）。配對 anomaly：A-VS63。**狀態：未送出。**

## DR-22′（**已撤回，R-VS49**，29 輪 D-4；原文保留 —— R-TM13）

**狀態：撤回，不送出。** 49 包 §1 之 R-VS49 採用 `PROXI_HDCC27_R3_20250424.xlsx` 之四參數值域，本 DR 之訴求消滅。
**惟其所稱之「影響 79 leaf」為錯** —— 實測僅 8 條 leaf 引用該四參數（29 輪 W-83，見 A-VS95）。

---

### （原文保留）

## ~~DR-22′（型 B — 素材缺件；44 包 §1 改為是非題，25 輪 D-2；Urgency High）~~

**型別（R-VS45）：型 B。搜尋已停止（44 包 §2）—— 客戶目錄已窮盡，R1LR 之 PROXI 表不存在。**

> 我方 LID v1.76 之 `Proxi & Configuration` 分頁，下列四參數之
> `Format` 欄為 `See Proxi Table`，`VFs` 欄為 `664`：
>
>     Cooled_Seats／Heated_Seats／Heated_Seat_Levels／Heated_Steering_Wheel
>
> 請確認 R1LR 之該四參數值域，是否即 VF664_V2／V3 所對應之 PROXI 表定義
> （我方於他車型之 PROXI 表見：
>  `Cooled_Seats`／`Heated_Seats` = `0 Absent／1 Front Seats／2 Front And Rear Seats`；
>  `Heated_Steering_Wheel` = `0 Absent／1 Present`；
>  `Heated_Seat_Levels` = `0 = 1 Level／1 = 2 Levels／2 = 3 Levels`）？
>
> 若否，請提供 R1LR 所適用之 PROXI 表。

**影響：79 個 SWE leaf。** 我方**不採用**他車型之值（44 包 §1 裁定），
四參數維持未解；`writability.tsv` 之 `evidence_note = VF664-inferred` 保留供比對。

**理由（44 包 §1）**：`VF664_V42_R3`（Toro226）完全未提及該四參數，
而 `V2_R1`／`V2_R2` 提及 —— **VF664 之內容隨版本而異，而 R1LR 目錄下無 VF664**。
兩份轉錄一致只證明 DT27 與 HDCC28 用同一版。

**狀態：未送出**（送出屬 Pei）。

---

### （原 DR-22 逐實例／類別式條文，保留 —— R-TM13）

## ~~DR-22（類別式，B3，依 R-VS42 改制於 20 輪；Urgency High）~~

**類別：PROXI／參數於 LID、DBC、值域資料三處皆無命中。**

**影響範圍（20 輪 W-58）**：**2 個 leaf**、2 次命中 ——
`ThirdRowHeadrestDump-028`（`VC_HdRstPrsnt`）、
`HeatedSteeringWheel-004`（`HSW_StatS`，**實為來源 `$` 不對稱之 typo**，見 A-VS68）。

---

### （原逐實例條文，保留 —— R-TM13）

## ~~DR-22（新，Urgency High —— 阻塞 1 個 leaf；19 輪 W-57 開立）~~

**`VC_HdRstPrsnt` 於 LID、DBC、值域資料三處皆無記載。**

CFTS044 `4858989` 逐字：
`When the HU receives the vehicle configuration signal VC_HdRstPrsnt = [Present],
the HU shall dispaly the Third Row Headrest Dump softkey button.`

實測命中數：

| 來源 | 命中 |
|---|---:|
| `Logical Identifiers and CAN Mapping v1.76`（`lid_pairs.tsv` 2,710 列） | **0** |
| `PDT27_E2A_R4_BHCAN.dbc`／`PDT27_E2A_R5_FDCAN8.dbc` | **0** |
| `data/spec_variables.tsv`（30 個 token） | **0** |

> **附記（R-VS34 形態）**：該 token 於 CFTS044 中寫作**裸名 `VC_HdRstPrsnt`，無 `$...$` 包夾**，
> 故早輪以 `$var$` 形態建立 `spec_variables.tsv` 時未收入。
> 本輪依 **R-VS36** 之三形態試法方發現。

**影響**：`SWE1-VC-ThirdRowHeadrestDump-028`。

**提問文待分析層擬**（本層不代擬）。配對 anomaly：A-VS64。**狀態：未送出。**

## DR-23（**搜尋已停止，44 包 §2**；**類別式，B1**，依 **R-VS42** 改制於 20 輪；Urgency Medium）

**型別（R-VS45）：**型 B**（素材缺件，B1 類）**

**類別：未具名之外部交叉參照 —— 其整個結果被外推至未具名之文件。**

**併入本類者**：**DR-20**（`4858560`，**已於 2026-08-22 單獨送出**）。
> 本類別包含已於 2026-08-22 送出之 **DR-20**，其為本類之實例。

**影響範圍（20 輪 W-58）**：**8 個 leaf**、8 個相異條文：

```
4858560  4859509   the HMI shall be modified as defined by HMI requirements
4859032            the HU shall follow the HMI Logic & Flow to update the state …
4859386  4859387   TLM has to show an informative popup …
4859448  4859449
4859498
```

> **判準之精化須記明**：初測以「`as defined by`／`refer to`／`follow the`／
> `per the`／`as specified by`／`according to` ＋ 未帶文件名或章節號」為準，
> 得 **65 條**。逐條讀後，其中 **57 條為尾綴修飾**
> （如 `shall be shown as greyed-out, **per the HMI**` —— 結果動詞已具體），
> **僅 8 條為整個結果被外推**。**尾綴修飾不阻塞。**

---

### （原逐實例條文，保留 —— R-TM13）

## ~~DR-23（新，Urgency Medium —— 阻塞 1 個 leaf；19 輪 W-57 開立）~~

**`4859032` 交叉參照未具名之 HMI Logic and Flow。**

條文逐字：
`When the signal $PowerMode$ <> [IGN_RUN], the HU shall follow the HMI Logic &
Flow to update the state of the Rear View Camera soft button.`

「HMI Logic & Flow」未具名任何文件、章節或需求 ID。
其「更新後之狀態」為何無從判定：寫具體狀態即造值（§8.4.1），
寫「state is updated」則不可觀察（§6）。

**與 A-VS59／DR-20（`4858560`）為同型**，惟所指之文件不同
（該條為「HMI requirements」，本條為「HMI Logic & Flow」）。

**影響**：`SWE1-VC-ThirdRowHeadrestDump-039`。

**提問文待分析層擬**（本層不代擬）。配對 anomaly：A-VS65。**狀態：未送出。**


## DR-8′（**改寫**，44 包 §5；25 輪 D-2。型 B — 素材缺件）

**型別（R-VS45）：型 B。搜尋已停止（44 包 §2）。**

`Logical Identifiers and CAN Mapping v1.76` 之 `VC_VEH_LINE` 值域列舉
為數字車型碼且截斷於 `101 = WL (65 Hex)`。

而 R1LR 之 CFTS 文件**實際使用之值**為 `332`／`M182`／`M189`
（`VEH_M182 OR VEH_M189` 等形態，24 輪 W-68(3) 實測 **103 處引用**），
**與該列舉無交集**。

**請提供 R1LR 所適用之完整車型碼對照**（含 `332`／`M182`／`M189` 之編碼）。

> **原 DR-8 之前提已失效**：其列舉 `DT`／`WS`／`HDCC`／`M240`，
> 而該四碼於 R1LR 之 CFTS 中交叉命中 **0**。

**狀態：未送出。**

---

### （原 DR-8 條文，保留 —— R-TM13）

## ~~DR-8（補登記，20 輪 D-3 —— 00G §5 開立而未入簿）~~

**型別（R-VS45）：**型 B**（素材缺件：完整車型碼對照表）**

**`$VC_VEH_LINE$` 之車型碼對照。**

CFTS044 使用 `[DT]`／`[WS]`／`[HDCC]`／`[M240]`／`DS or DJ or D2…` 等代號；
LID 表之 `VC_VEH_LINE` 值域列舉為數字車型碼且截斷於 `101 = WL (65 Hex)`，
**二者完全無交集**。請提供完整之車型碼對照。

37 包送件文第 **7** 項即本條。**狀態：未送出**（Pei 本次僅送 1–5）。
配對 anomaly：A-VS66（本條未入簿之事實）。

## DR-12（補登記，20 輪 D-3 —— 29 包 §1.2 開立而未入簿；**併入 DR-21**）

**型別（R-VS45）：**型 A**（規格缺陷；併入 DR-21）**

**`$PowerMode$` 之 `IGN_OFF_ACC`。**

CFTS044 `4858978`（Second Row Headrest Dump）以
`$PowerMode$ = [Ign. off & acc. (4 position switch) / IGN_OFF_ACC]` 為軟鍵可選之條件；
LID 將 `PowerMode` 對映至 `STATUS_BH_BCM2.CmdIgnSts`，其值域為
`Initialization / IGN_LK / ACC / RUN / START / SNA`，**無 `IGN_OFF_ACC`**。

37 包送件文第 **8** 項即本條。**狀態：未送出。**
依 **R-VS42 併入 DR-21**（B2 類），原編號保留。


## DR-24′（改寫，併入 `<Tdisplay>`；43 包 §3.1，24 輪 D-3）

**型別（R-VS45）：型 A（規格缺陷）。**

CFTS044 使用**兩個**時間符號而未給其具體值：

```
`<Tsend>`     15 次引用
`<Tdisplay>`  28 次引用
去重後涉及 **43 個 SWE leaf**
```

canon §8.7.1 要求門檻須為具體值，故二者皆無法作為 ER 之通過條件。

**請提供 `<Tsend>` 與 `<Tdisplay>` 之具體時值（含單位與量測起訖點）。**

我方之暫行處置：procedure 保留符號原樣（來源逐字），
ER 改寫為可觀察之終態，不以時限為通過條件。

**狀態：未送出。**

---

### （原 DR-24 條文，保留 —— R-TM13）

## ~~DR-24（新，型 A — 規格缺陷；23 輪 D-3 開立，分析層擬）~~

**`<Tsend>` 無具體值。**

CFTS044 `4858320` 等條文以 `within a time period of <Tsend>` 為請求訊號之
時間條件，**來源未給該符號之具體值**。

canon §8.7.1 逐字：`Every trigger / release threshold MUST come from the spec
and appear as a concrete value in the Pre-Condition, never vague language.`
故 `<Tsend>` **不得作為 ER 之通過條件**。

**請提供 `<Tsend>` 之具體值**（毫秒），及其是否隨訊號或配置而異。

影響：引用 `<Tsend>` 之 leaf（數量見上繳 21 §1.4）。
現行處置：procedure 保留 `<Tsend>` 原樣，**ER 改寫為可觀察之終態**（42 包 §3.2）。

**狀態：未送出。**

---

## DR-25（新，**Urgency High** —— 阻塞剩餘全池 33 leaf；35 輪 W-91 開立，分析層擬）

**型別（R-VS45）：型 B — 素材缺件。**

**成對之 anomaly：A-VS110。**

本 feature 之基線 CAN 為 `PDT27_E2A_R4_BHCAN.dbc` ＋ `PDT27_E2A_R5_FDCAN8.dbc`
（R-VS8；兩檔 `VersionYear` = 25、`VersionWeek` = 50）。

CFTS044 之 `1.3.3.3.2.1`／`1.3.3.3.3.1`／`1.3.3.3.4.1`／`1.3.3.3.5.1` 四節
共 33 個 in-scope leaf，其 `THEN` 之賦值目標為：

    TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm     11 leaf
    TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm     11 leaf
    TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm    11 leaf

該三個 signal 於基線兩檔之 `SG_` 命中**各為 0**。
該 33 條之 `EE Architecture` 皆為 **`Atlantis Mid`**。

LID `CAN Mapping` 列 763（`FL_HS_RQ2`）之 **`Atlantis` 欄組**確有其對映與值域
（`0 = Heated_seat_off`／`1 = Heated_seat_low`／`2 = Heated_seat_medium`／
`3 = Heated_seat_high`），且該列之 `Atlantis High` 欄組標 `ATL_HIGH_EMPTY`。

**即：對映與值域皆有來源，唯獨匯流排定義本身（DBC）沒有。**

依 R-VS9(1)′（拼寫以 DBC 為第一權威）與 L-VS2（不存在於基線 DBC 者 FAIL），
該 33 leaf **不可寫出通過自檢之 TC**。

**請提供下列之一：**

  (1) `Atlantis Mid` 網段之 DBC（含 `TELEMATIC_VEHICLE_SETUP`／
      `TELEMATIC_VEHICLE_SETUP2` 之 `FL_HS_Cmd_Tlm`／`FR_HS_Cmd_Tlm`／
      `FL_VS_Cmd_Tlm` 定義），或
  (2) 裁定該 33 leaf 之處置 —— 標 BLOCKED 並自 `generatable` 池移出，
      或裁定以 LID `Atlantis` 欄組之值域為權威而豁免 L-VS2

**不採第三路**：以 `Atlantis High` 之對稱訊號（列 762 之
`TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm`）代之 —— 其為跨列引入，
與 A-VS103 之處置一致，屬裁定事項而非執行層自裁。

**影響**：`generatable = 108` 中已交付 76、DR 阻斷 3（A-VS110 以外之
`HeatedSteeringWheel-012`／`PHEVFeatures-017`／`FeaturesEnableCriteria-023`，
見 A-VS109／A-VS111／A-VS112），**其餘 33 全數落於本 DR**。
即 **本 feature 之可生成池於本 DR 覆前為 0**。

**狀態：未送出。**
