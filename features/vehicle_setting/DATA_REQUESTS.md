# DATA_REQUESTS — FW036 Vehicle Setting

每項含**路徑與 SHA**（G-L：沒有路徑的「到齊」不算到齊）。
`inputs/` 之權威雜湊見 `inputs/INPUTS.sha256`（**32 檔**：CFTS044 16 ＋ VF230 13 ＋ VF230 補入 2 ＋ Part 1 遺漏補列 1，
`shasum -a 256 -c` 全數 OK；61 包 W-102）。

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

## DR-15′（**改寫**，63 包 §5；40 輪 D-3。取代 DR-15 —— Pei 指示「說明更詳細一點」。Urgency High；**已送出者補送本文**）

**條文逐字轉錄自 `docs/handoff/63_rulings_round39.md` §5：**

```
DR-15′（取代 17 包 §2.3；已送出者以本文補送）

**問題**：加熱／通風座椅之請求訊號，其承載階數或為單一位元？

**背景**：本專案（R1LR，Atlantis High）之 TC 撰寫中，
同一個邏輯識別碼在三份文件上得到互相矛盾之描述。

**證據一 —— CFTS044 之條文（標記 `[EE Architecture:Atlantis High]`）**
條文 `4858325`（`$FL_HS_RQ$`）／`4858355`（`$FR_HS_RQ$`）／
`4858385`（`$FL_VS_RQ_TGW$`）／`4858416`（`$FR_VS_RQ_TGW$`）
令 HU 依座椅**目前狀態**送出循環降階之值：

    目前 High   → 送出 Medium
    目前 Medium → 送出 Low
    目前 Low    → 送出 Off
    目前 Off    → 送出 High

即該請求訊號**承載四個階數值**。

**證據二 —— 基線 CAN 資料庫**
`PDT27_E2A_R4_BHCAN.dbc`（VersionYear 25／VersionWeek 50）之
`TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm`／`FR_HS_Tlm`／`FL_VS_Tlm`／`HSW_Tlm`
皆為 **1 bit**，值表為 `0 = Not_Pressed`／`1 = Pressed`。
即該請求訊號**只有二值**。

**證據三 —— LID v1.76 之同一列（列 769）**
同一個 LID `FL_VS_RQ_TGW` 於兩個欄組對映至不同訊號：

    `Atlantis` 欄組      → `TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm`
                           2 bit，四階（Off／Low／Medium／High）
    `Atlantis High` 欄組 → `TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm`
                           1 bit（Not_Pressed／Pressed）

且該表對請求類 LID 之 `Format` 欄**無位元寬宣告**，
而對狀態類 LID（如 `HeatedSeatFL`）明載 `2 bit signal`。

**我方之觀察**：三份證據可以一致地解釋為 ——
**四階者屬 Atlantis Mid 架構，二值者屬 Atlantis High**；
而 CFTS044 描述循環降階之四條條文標記為 `Atlantis High`，
**其架構標記疑為自 Atlantis Mid 遷入時未更新**。

**請確認（擇一）**：
(a) 請求訊號為 1 bit，階數之循環由 HU 內部狀態機決定
    → 則 `4858325` 等四條之描述應改；
(b) 請求訊號承載階數
    → 請提供其實際 signal 名、bit 寬、值表；
(c) 兩者皆是，依 EE Architecture 分流
    → 則 `4858325` 等四條之 `[EE Architecture]` 標記應為 `Atlantis Mid`。

**另請確認**：該行為是否隨 `$Heated_Seat_Levels$`（1／2／3）之配置而不同？

**影響**：Heated Seat 88 ＋ Vented Seat 72 共 160 個 SWE leaf 之
測試步驟、預期結果與測試設計方法（Functional Based vs Decision Table）。
其中已交付 **6 條** TC 之斷言落在該五個 token 上，覆後須逐條複檢。
```

**狀態：已送出（原 DR-15，2026-08-22）—— 待覆；本文為補送之詳本。**
**覆後回溯之已交付 TC 為 6 條**（A-VS86 3 ＋ A-VS108 2 ＋ A-VS114 1）。

---

### （原 DR-15 條文，保留 —— R-TM13）

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

> **40 輪 D-3（依 R-VS61，63 包 §3）**：**性質由阻塞轉確認，不阻塞。**
> `$EngRun_Stat$` 之 `IDLE_STBL`／`UNLIMITED`／`LIMITED`／`RUN` 四值於 LID 與 DBC 皆無對應，
> 依 R-VS61 **仍產 TC**，其值取來源逐字（`STATUS_CCAN3.EngineSts = IDLE_STBL`，**不附 label**），
> 標 `dr_dependent = DR-19`。覆後補 raw 碼。**解 7 條。**

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

> **36 輪 D-3 註記**：本 DR 之 `*_Cmd_Tlm` 部分（`FL_HS_Cmd_Tlm`／
> `FR_HS_Cmd_Tlm`／`FL_VS_Cmd_Tlm`／`FR_VS_Cmd_Tlm` 四者）**由 DR-25 承載**
> （57 包 §2）；本 DR 保留其餘 token。

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


## DR-8′（**撤回，不送出** —— R-VS62′，65 包 §1；42 輪 D-3。原文保留 —— R-TM13）

> **撤回理由（R-VS62′）**：本 DR 縮限後之三碼（`M182`／`M189`／`M240`）
> **於 237 leaf 母體命中 0**，覆之不解本 feature 任何一條。
> 母體實際引用者為 `WL`（→ 101）與 `M4 OR MP`（→ 98 OR 93），
> 二者於 `PROXI_HDCC27_R3` 之 `Format` 列 466 皆已解。
> **成對之 A-VS140 依本條關閉。**

### （原 DR-8′ 條文，保留）

## DR-8′（**改寫**，44 包 §5；25 輪 D-2。型 B — 素材缺件）

**型別（R-VS45）：型 B。搜尋已停止（44 包 §2）。**

`Logical Identifiers and CAN Mapping v1.76` 之 `VC_VEH_LINE` 值域列舉
為數字車型碼且截斷於 `101 = WL (65 Hex)`。

而 R1LR 之 CFTS 文件**實際使用之值**為 `332`／`M182`／`M189`
（`VEH_M182 OR VEH_M189` 等形態，24 輪 W-68(3) 實測 **103 處引用**），
**與該列舉無交集**。

**請提供 R1LR 所適用之完整車型碼對照**（含 `332`／`M182`／`M189` 之編碼）。

> **40 輪 D-3 之縮限（依 R-VS62，63 包 §4，Pei 2026-08-23）**：
> `332`／`WS`／`DT`／`HDCC` 四碼已自 `PROXI_HDCC27_R3_20250424.xlsx` 之 `Format` 分頁
> 列 466 解得（`332 → 105 (69 Hex)`／`WS → 104 (68 Hex)`／`DT → 124 (7C hex)`／
> `HDCC → 130 (82 Hex)`）。**本 DR 縮限為 `M182`／`M189`／`M240` 三碼**，
> 三者於該表命中 0。適用範圍限 `VC_VEH_LINE` 一參數。

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

## DR-25′（**改寫**，60 包 §3；37 輪 D-3。取代 57 包 §2 之 DR-25 —— 由 3 訊號／33 leaf 擴為 **5 訊號／65 leaf**。型 A/B 兼具，Urgency Medium）

**成對之 anomaly：A-VS110（阻塞）＋ A-VS115（範圍不足，依本條關閉）。**

**條文逐字轉錄自 `docs/handoff/60_review_round36.md` §3：**

```
DR-25′（取代 57 包 §2 之 DR-25；型 A/B 兼具，Urgency Medium）
CFTS044 之 SWE leaf 其行為賦值於下列五個訊號，
而該五者於本專案之基線 CAN 資料庫
（`PDT27_E2A_R4_BHCAN.dbc`／`PDT27_E2A_R5_FDCAN8.dbc`，
 VersionYear 25／VersionWeek 50）中**皆不存在**（`SG_` 命中各 0）：

    TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm      17 leaf
    TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm      16 leaf
    TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm     14 leaf
    TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm     14 leaf
    HSW_Cmd_Tlm                                 4 leaf
    ——— 相異 leaf 合計 65

基線僅有 `TELEMATIC_VEHICLE_SETUP3`。
而 `Logical Identifiers and CAN Mapping v1.76` 之 `Atlantis` 欄組
確載其值域。該等條文之 `EE Architecture` 皆為 `Atlantis Mid`。

請確認：
(a) 承載該五訊號之 CAN 資料庫為何？（請提供）；或
(b) 該等訊號不適用於 R1LR，其對應之 CFTS044 條文於本專案不需驗證？

我方之暫行處置（Pei 2026-08-22，R-VS57）：**以 spec 與 037 所載為主**，
訊號名取來源逐字撰寫 TC，並標 `dr_dependent = DR-25`。
**該等 TC 在現行 CAN 環境上無法執行**，其依賴已逐條標記。
若答覆為 (b)，該 65 leaf 之 TC 逐條撤回。
```

**擴充之依據**：36 輪 W-98(1) 實測之 L-VS2 WARN 類為 **5 個相異 signal**，受影響 leaf **65**（`FR_VS_Cmd_Tlm` 14／`HSW_Cmd_Tlm` 4 為 DR-25 原文所漏）。

> **38 輪 D-3 之更正（依 R-VS57(4)，61 包 §4）**：
> `HSW_Cmd_Tlm` 之**值域於 LID 兩欄組皆為 `None`**，
> 依 R-VS57(4)「名有來源 ∧ 值域無來源 → **W2／`B6-value-absent`**」，
> 其 **4 leaf 自本 DR 之範圍移出**，改列於 **A-VS118 之 B6 類**。
>
> **本 DR 之影響段因而為四訊號／61 leaf**：
> `FL_HS_Cmd_Tlm` 17／`FR_HS_Cmd_Tlm` 16／`FL_VS_Cmd_Tlm` 14／`FR_VS_Cmd_Tlm` 14
> —— 相異 leaf 合計 **61**（38 輪 W-108 實測，與 61 包 §4 之預期相符）。
>
> 上文條文區塊之五訊號列表為 60 包 §3 之逐字轉錄，**不追改**（R-TM13）；
> 其 `HSW_Cmd_Tlm` 一列於送出時應連同本註記。

**`FR_VS_Cmd_Tlm` 另受牽制**：其 LID `Atlantis` 欄組之值域為 `Heated_seat_*`，52 包 §3 已判該前綴為 typo，惟其正確值域須自 `FL_VS_Cmd_Tlm` 之列跨列引入 —— **A-VS103 判其為裁定事項，本層不跨列引入**，該 14 leaf 之值域仍未解（併 DR-18）。

> **40 輪 D-3（依 R-VS59，63 包 §6）**：**性質由阻塞轉確認，不阻塞。**
> 其 61 leaf 依 R-VS57／R-VS59 照寫，訊號名與值域取來源逐字並標 `dr_dependent`；
> 覆後為 (b) 者逐條撤回。

**狀態：未送出。**

---

### （原 DR-25 條文，保留 —— R-TM13）

## DR-25（**Urgency Medium** —— 依 R-VS57 由 High 降級，性質由阻塞轉確認；35 輪 W-91 開立、36 輪 D-3 依 57 包 §2 全文改寫）

**型別（R-VS45）：型 A/B 兼具**（分析層 57 包 §2）。

**成對之 anomaly：A-VS110。**

**條文逐字轉錄自 `docs/handoff/57_review_round35.md` §2：**

```
DR-25（分析層擬，Urgency High，型 A/B 兼具）
CFTS044 之 33 個 SWE leaf（`EE Architecture: Atlantis Mid`）其行為賦值於
    TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm ／ .FR_HS_Cmd_Tlm
    TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm
三者於本專案之基線 CAN 資料庫
（`PDT27_E2A_R4_BHCAN.dbc`／`PDT27_E2A_R5_FDCAN8.dbc`，
 VersionYear 25／VersionWeek 50）中**皆不存在**（`SG_` 命中各 0）；
基線僅有 `TELEMATIC_VEHICLE_SETUP3`。

而 `Logical Identifiers and CAN Mapping v1.76` 之 `Atlantis` 欄組
確載其值域（列 763：`0 = Heated_seat_off` … `3 = Heated_seat_high`）。

請確認：
(a) 承載該三訊號之 CAN 資料庫為何？（請提供）；或
(b) 該等訊號不適用於 R1LR，其對應之 CFTS044 條文於本專案不需驗證？

影響：33 個 SWE leaf 之 TC 無法寫出可執行之訊號斷言。
若為 (b)，我方之適用性判準（`Radio` ＋ `ECU`）須修訂。
```

---

### 兩種讀法（57 包 §2，逐字）

| 讀法 | 意涵 |
|---|---|
| (a) **素材缺件** | 承載 Mid 網段之 DBC 我方未持有 |
| (b) **R-VS19″ 判錯** | 該等條文屬 Atlantis Mid 專屬，其訊號不在本專案之匯流排上 —— 即不適用 R1LR |

**(b) 若成立，R-VS19″ 之 `Radio`／`ECU` 判準即不足** ——
`Radio` 含 R1L 只表示該條文之文字涵蓋該車型，不表示其訊號在本專案佈線上存在。

### 依 R-VS57 之降級（59 包 §1，Pei 2026-08-22）

L-VS2 改三分後，該 33 條判 **WARN** 而非 FAIL：
訊號名取 CFTS044 條文／LID `Atlantis` 欄組之逐字來源，**照常撰寫 TC**，
並標 `dr_dependent = DR-25`。

故本 DR 之性質由「阻塞」轉為「確認」，**Urgency High → Medium**：

  覆後為 **(a)** —— 以該 DBC 複驗訊號名與值域
  覆後為 **(b)** —— `dr_dependent = DR-25` 之 TC **逐條撤回**

**須向客戶揭露之風險（59 包 §2）**：該 33 條 TC 之訊號斷言指向基線 DBC
中不存在之訊號，**執行時無法在現行 CAN 環境上跑**。
其為已知且已標記之狀態，非缺陷；交付前須揭露該依賴。

### 與 DR-21 之關係（57 包 §2）

**DR-21 之 `*_Cmd_Tlm` 大宗即此。DR-25 取代其中該部分之提問**，
DR-21 保留其餘 token。

**狀態：未送出。**

---

## DR-26（新，**Urgency Low** —— 阻塞 1 個比較步驟；36 輪 W-101(3) 開立）

**型別（R-VS45）：型 A — 規格缺陷（未載之狀態）。**

**成對之 anomaly：A-VS113。**

`CFTS044-4859031`（1.3.2.1.22）逐字為：

```
The Rear View Camera soft button shall be selectable only when the signal
$PowerMode$ = [IGN_RUN].
```

該條文載明 `IGN_RUN` 時**可選**，**未載** `IGN_RUN` 以外時該按鍵之狀態 ——
其可能為「不可選（灰階）」、「不顯示」、或「顯示而不回應」，三者皆與
`selectable only when` 相容。

**請確認**：`$PowerMode$ ≠ [IGN_RUN]` 時，Rear View Camera soft button 之
狀態為下列何者？

  (a) 顯示但不可選（灰階）
  (b) 不顯示
  (c) 顯示且可選但不回應

**影響**：`SWE1-VC-ThirdRowHeadrestDump-038` 之步驟 2 記錄 `RVC_button_ign_lk`
而其比較之期望值無來源。依 canon §8.4.3 標 `PENDING: DR-26`。

**背景**：35 輪本層曾自 tc_title 與條文推得 `not selectable` 並列供覆核；
57 包 §3.3 判其為**造值**（§8.4.1：推論即造值），令退回記錄形態。
本 DR 即該退回所留下之缺口。

**狀態：未送出。**

---

## DR-27（新，**Urgency Medium** —— 4 個 leaf；37 輪 W-105 之唯一性掃描開立）

**型別（R-VS45）：型 A — 規格缺陷（條文冗餘）。**

**成對之 anomaly：A-VS119。**

CFTS044 之 `1.3.2.1.3.11` 內，四個 leaf 之條文兩兩僅差值之書寫形式：

```
4858538（-015）  When the HU receives a $HSW_Stat$ = [On] signal, …
4858544（-021）  When the HU receives a $HSW_Stat$ = [1h: On] signal, …

4858539（-016）  When the HU receives a $HSW_Stat$ = [Off] signal, …
4858545（-022）  When the HU receives a $HSW_Stat$ = [0h: Off] signal, …
```

四者之後半段（`shall change the stored status … within <Tdisplay>`）**逐字相同**，
`EE Architecture` 亦相同（`PowerNet, Atlantis High`）。

**其可測內容因而完全一致** —— 已交付之四條 TC，其
`pre_conditions`／`test_procedure`／`expected_result` **三欄全同**，
僅 `specification_reference` 相異。

依 §8.2.2「一 leaf 得對多 TC，反向不可」，四個 leaf 不得共用一份 TC；
而其可測內容無法分辨，**故無從產生四份相異之 TC**。

**請確認：**

  (a) `[1h: On]` 與 `[On]` 為同一需求之兩次書寫（條文冗餘）？
      若是，`-021`／`-022` 是否可標為 `-015`／`-016` 之重複而不獨立產 TC？
  (b) 二者有語意差別（如前者指原始碼值、後者指邏輯狀態），
      其差別應如何在 TC 中呈現？

**影響**：4 個已交付 leaf 之 TC 唯一性。**本層未合併、未刪除**（§8.2.2 之限制
與「各版保留不刪」之禁區皆及於此）。

**狀態：未送出。**

---

## DR-28（新，**Urgency Low** —— VF230 缺 SYS2 ICS export；61 包 §6／§7 開立）

> **⚠ 本件之「影響」段已作廢（38 輪，A-VS134）。** 開立時之前提為「無第二來源
> 可核」，該前提不成立：`inputs/` 內之 `FM-WI-FSM-035-A02_…_SYSRA_VF230_V4_Released.xlsx`
> 與 SYS2 同型且涵蓋 037 之全部 745 列，跨源驗核已完成（`docs/reports/vf230_crosscheck.md`），
> 錯配亦已偵得 8 個（A-VS132）。Urgency 由「待定」降 **Low**。

> **⚠ 改號**：61 包 §7 之草稿編為 DR-27，而 **DR-27 已為 37 輪 W-105 之
> 唯一性提問所用**（成對 A-VS119，本檔 §DR-27）。本件改編為 **DR-28**。
> 撞號之登記見 A-VS124。61 包 §7、§8 之「DR-27」一律指本件。

**型別（R-VS45）：型 C — 素材缺件。**

**成對之 anomaly：無**（缺件非量測異常）。

CFTS044 之素材含 SYS2 ICS export
（`SYS2  R1LR_Atl-H_25PI1.1_Activation and Configuration_CFTS_044_
Vehicle Controls_SR26_20250815-1022_20260324_Version3_Released.xlsx`），
VF230 之交付資料夾 `VF230_V1_R5/` 內無對應檔案（61 包 §2.1 之清冊實測，
本輪複驗：該目錄一層 17 項，無任何 `SYS2` 檔名）。

**請提供**：VF230（`C-VF230_V1_R5_PDT27`）對應之 SYS2 ICS and DCSD export
（Released 版）。

**影響**：SYS2 為 Part 1 之 Category 交叉驗核來源（01 輪唯一之跨源檢驗，
537 列對帳、零錯配）。VF230 缺此來源者，其 **619 個 leaf** 之
Functional/Heading 判定將無第二來源可核，A-VS01 型之錯配無從偵測。

**不得代用 CFTS044 之 SYS2** —— 其為該 CFTS 專屬（R-VS63 之末段明排除）。
`feature.yaml` 之 `paths.sys1_export_vf230` 現為 `null`，覆後方填。

**~~本輪之處置~~**：~~VF230 之 leaf 母體（619）單源自 037，未經跨源驗核。~~
**已於同輪稍後完成跨源驗核**（`scripts/vf230_crosscheck.py`）：037 之 745 列
**全數命中** 035，leaf 側 619/619 皆為 `Functional Requirement`（零錯配、
反向錯配 0），heading 側 126 列中 **8 列錯配**（A-VS132）。

**本件仍請求之理由（縮小後）**：

1. `SYS2_VF230.xlsx` 已於 `9_ASPICE/SYS.2 System Requirements Analysis/
   Z.QS YuShen 260423/08.[SYS2]Vehicle Settings/` 尋得（2626 列，schema 同型），
   **但未取用、未複製入 `inputs/`** —— 其為 repo 既定根目錄之外之素材，
   補入須依 **R-VS61**（由 Pei 執行；2026-08-23 之免除為單次個案）。
2. 該檔**缺 037 之 6 個 `E-Save` leaf**（`SYS-RA-VF230_V1-2660`～`-2665`），
   而 035 有、spec 目次無（A-VS127 §2.1）。**三源不一致，需原生 SYS2 方能定讞。**

**請確認**：(a) 是否將 `SYS2_VF230.xlsx` 補入 `inputs/`；
(b) `E-Save` 之 7 列於三源之不一致該以何者為準。

**狀態：未送出。**

---

## DR-29（新，**Urgency Low** —— 19 個 `SWE-Requirement ID` 缺連字號；62 包 §5.3／W-118 開立）

> **開號依據**：本檔與 `RULINGS.md`／`ANOMALIES.md`／`docs/` 之最大已用
> DR 號為 **DR-28**（62 包 §5.3 令「開號前先查最大已用號」）。

**型別（R-VS45）：型 A — 規格缺陷（書寫瑕疵）。**

**成對之 anomaly：A-VS130。**

VF230 之 037 分報告 `FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA_STLA_
Trailer_Name - Max_Power_Level_Report.xlsx` 內，**19 列之 `SWE-Requirement ID`
於序號前缺連字號**：

```
SWE1-VC-TrailerBrakeType024 … 037      14 列（024 為 Heading，025–037 為 leaf）
SWE1-VC-MaxPowerLevel139 … 143          5 列（139 為 Heading，140–143 為 leaf）
```

同檔內其餘 ID 皆為 `SWE1-VC-<Family>-NNN` 之形態（例：同檔之
`SWE1-VC-TrailerName-001`）。**本層已回原始儲存格逐字實測，確認為上游所書**，
非本層抽取或序列化所致。

**請確認：**

  (a) 該 19 列之正確 ID 是否為 `SWE1-VC-TrailerBrakeType-024` …
      與 `SWE1-VC-MaxPowerLevel-139` …（即補上連字號）？
  (b) 若是，上游是否會出修訂版？在其到位前，本層應以原值或補號後之值
      作為 `specification_reference` 之錨？

**影響**：`swe_id` 之 family／序號分離。實測受影響之處 **1**：
`scripts/layer3_w46.py:41` 之 `re.match(r"SWE1-VC-(.+)-\d+$", swe_id)`
對該 17 個 leaf 回 `None`。Part 1 之 271 leaf 受影響 **0**。
`scripts/recon.py` 之 `-\d\d$` 於兩 feature 皆命中 0（其為 R-C3 之證據測量，
非選取路徑），與本件無關。

**本層未補連字號**（改值即造值，同 A-VS103／A-VS104 之處置）。
容錯改為 `-?(\d+)$` 之修法**已列出而未施行**（62 包 §5.2 令「先列清單，不逕改」）。

**狀態：未送出。**

---

## DR-30（新，**Urgency Low** —— 037 與 035 於 8 列之 Categorization 相左；V06 §5.4 開立）

> **開號依據**：全庫（`DATA_REQUESTS.md`／`RULINGS.md`／`ANOMALIES.md`／
> `docs/handoff/`／`docs/upstream/`）之最大已用 DR 號為 **DR-29**。

**型別（R-VS45）：型 A —— 規格／分析文件間之不一致。**

**成對之 anomaly：A-VS132。**

VF230 之 037 分報告判為 `Heading` 而 035（SYSRA）判為
`Functional Requirement` 者 8 列，集中於 SWITCH 族
（Power Mode／Type／Hold Last State）。其 037 條文逐字為需求形態：

```
The HMI layer shall capture the customer selection for …          （5 列）
HW supplier shall notify the IPC_VEHICLE_SETUP2.* signal
via VHAL interface …                                              （3 列）
```

逐一為 `SWE1-VC-SWITCH3PowerMode-014`／`SWITCH6PowerMode-026`／
`SWITCH3Type-039`／`SWITCH5Type-045`／`SWITCH6Type-051`／
`SWITCH2HoldLastState-058`／`SWITCH3HoldLastState-063`／
`SWITCH6HoldLastState-076`。

**請確認**：該 8 列之正確 Categorization 為 `Functional Requirement`
或 `Heading`？

**本層之處置（已定，不待覆文）**：依 Pei 裁定（**R-VF16**）計入可測 leaf，
母體為 **627**。該 8 列於 `data/vf230_leaves.tsv` 已加 `disagree=1` 註記，
以資分辨。若上游覆為 `Heading`，本層將於當時另裁是否回退。

**已實測之影響（W-VF17）**：Layer 2 之簇數（106）與 spec 目次交集（104／2）
**皆不因 627 而變**，僅 8 個既有簇各 +1 leaf，且全落於同一份 037 分報告。

**狀態：未送出。**

---

## DR-31（新，**Urgency Low** —— 2 簇於 spec 目次無對應章；R-VF34 開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-30**（R-VF10；R-VF34 第 4 項令
> 「若 30 已被占用則順延並具名」—— 已占用，故本件為 31）。

**型別（R-VS45）：型 A — 規格缺陷（章節缺漏）。**

**成對之 anomaly：A-VS127**（交集法之粒度失效）。

VF230 之 037 分報告有 **2 個 Requirement Title 簇**，於 spec
`C-VF230_V1_R5_PDT27.doc` 之 192 個 Heading 中**查無對應章**
（正規化後全等比對，含 NFKC ＋ 換行摺疊 —— W-VF7 複驗後之
exact 104 ／ 無對應 2）：

```
E-Save                              6 leaf
CHMSL CAMERA DYNAMIC CENTERLINE     5 leaf
```

**`E-Save` 另於 `SYS2_VF230.xlsx` 亦無對應**（其 6 個
`SYS-RA-VF230_V1-2660`～`-2665` 於該檔命中 0），惟於 035 SYSRA 有。
**三源不一致。**

**請確認**：該 2 簇之 spec 章節歸屬為何？其是否為 spec 之遺漏，
抑或另有本層未查之章名？

**本層之處置（已定，不待覆文）**：依 **R-VF34** 採 (a)＋(c) 併行 ——
Layer 3 **留空且可見**，不自創章名（R-VF25 配套 3）；
其 11 leaf **仍計入母體 627 與其所屬 Test Set**（Layer 3 為導航工具，
非可測性之判準）。

**狀態：未送出**（送出屬 Pei，R-VF27）。

---

## DR-32（新，**Urgency Low** —— 037 分報告之切分依據；R-VF47 一開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-31**（R-VF10）。

**型別（R-VS45）：型 A — 上游作業準則之確認。**

**成對之 anomaly：無**（其為準則之提問，非量測異常）。

VF230 之 11 份 037 分報告中，**同一功能之需求被分置兩份**：

```
SWITCH 1 Power Mode        6 條  →  分報告 A 3 條 ／ 分報告 B 3 條
SWITCH 1 Type              6 條  →  同型
SWITCH 1 Hold Last State   6 條  →  同型
                                    （SWITCH 1–4 × 三屬性 = 12 個功能如此）
```

**請確認**：037 分報告之切分係依何準則？（依撰寫者、依交付時程、
依 EE 分支、抑或其他？）

**背景與影響**：本層之 Layer 2（Test Set）分組以 037 分報告族群為基底，
再依條文主旨逐筆調整（提案 C，R-VF41／R-VF44，已鎖定於 `framework.md`）。
**若上游之切分另有準則，本層之分組可能與其相左。** 現行分組立於本層對
條文主旨之判斷，**非上游之準則** —— 該狀態已記於 `framework.md` 之鎖定註記。

**狀態：未送出**（送出屬 Pei，R-VF27）。

---

## DR-33（新，**Urgency Low** —— SWITCH 5／6 是否本不需要「HMI 送出」類需求；R-VF47 一開立）

> **開號依據**：同上，接續 DR-32。

**型別（R-VS45）：型 A — 規格缺漏之確認。**

**成對之 anomaly：無**（其為缺漏之提問；實測見下）。

**實測（W-VF36 第 3 項，以條文形態為可測代理）**：

```
                          顯示   HW通知   HMI送出   合計
SWITCH 1–4 Power Mode       3      1        2        6
SWITCH 5－6 Power Mode      2      1        0        3
SWITCH 1–4 Type             4      2        0        6
SWITCH 5－6 Type            2      1        0        3
SWITCH 1–4 Hold Last State  4      2        0        6
SWITCH 5－6 Hold Last State 2      1        0        3
```

**SWITCH 5／6 完全無「HMI 送出」類需求**，且其總條數為 1–4 之半。

**請確認**：係 SWITCH 5／6 本不需要該類需求，抑或上游未寫？

**影響**：若為後者，SWITCH 5／6 之 TC 將**缺少一類驗證對象**
（HMI 送出之訊號行為），而其缺少不會於本層之任何檢查中顯現 ——
因本層無「每個功能應有幾類需求」之基準。

**本層之處置**：SWITCH 5／6 於 `framework.md` **不加 R-VF43 之
「含兩種條文形態」標註**（其確無兩種形態），並於鎖定註記中具名其成因未查。

**狀態：未送出**（送出屬 Pei，R-VF27）。

---

## DR-34（新，**Urgency Medium** —— 11 個 PROXI 參數之值域無來源；W-VF44 開立）

> ⚠ **本 DR 之範圍於 38 輪 W-VF70 大幅更正 —— 其 11 個標的中 10 個為偽陽。**
> `proxi_known()` 讀 PROXI 表時寫死 `max_row=800`，而該分頁**實有 1060 列** ——
> 11 個「無來源」參數中 **9 個在第 800 列之後**（`AUX_Switch_Types` 列 911、
> `Blindspot_Trailer_Detection` 列 810、`Turn_Signal_Camera_View` 列 924 等），
> 另 1 個（`FOA_Presence`）表內逐字名為 `FOA _Presence`（多一空格）而未被比對到。
> **真正表內所無者僅 `Greeting_Light` 一個，影響 leaf 由 28 條降為 2 條。**
> 詳見 **A-VF27**。本 DR 之所詢**僅就 `Greeting_Light` 仍然成立**。

> **開號依據**：全庫最大已用 DR 號為 **DR-33**（R-VF10）。

**型別（R-VS45）：型 C — 素材缺件（值域來源）。**

**成對之 anomaly：A-VF11。**

VF230 之 627 leaf 中，**252 leaf 之可測內容立於 PROXI 配置之取得**
（條文形態為 `The HMI layer shall send a request to VehicleConfigManager to
retrieve the <X> PROXI configuration …`），共引用 **46 個相異 PROXI 參數**。

以 `inputs/PROXI_HDCC27_R3_20250424.xlsx` 之 `Format` 分頁比對：

```
表內可查得      35
表內無          11   →  影響 28 leaf，分級判 W1，標 PENDING: DR-34
```

**表內無者逐一**：

```
AUX_Switch_Types            Blindspot_Trailer_Detection   Digital_CHMSL_Camera_Prsnt
FOA_Presence                Greeting_Light                INVM_LIN_Module
Paddle_Shifter_Menu         Parksense_Camera_View         Trailer_Light_Check
Turn_Signal_Camera_View     Utility_Lighting
```

**請提供**：上列 11 個 PROXI 參數之值域（其 allowed values 與其語意），
或指明其所在之 PROXI 表版本。

**影響**：該 28 leaf 之 TC 之前提條件無法寫出具體值，
依 **R-VS47／R-VS71** 判 **W1**（部分可寫）—— 照常生成，
未解處標 `PENDING: DR-34`，並於該 TC 標 `dr_dependent = DR-34`。
**其驗證目標為顯示／啟用行為，非該 PROXI 值本身**，故不判 W2。

**與 Part 1 之 DR-7 之關係**：DR-7 求四個指定參數
（`Heated_Seats`／`Heated_Seat_Levels`／`Heated_Steering_Wheel`／`DSP_SK_PRSNT`）
之值域，其中 `Heated_Seats` 於本表可查得。
**本件之 11 個與 DR-7 之四個無交集**，故另立而非併入。

> **標的自 11 縮為 2，並具名一個近名參數（W-VF71 第 5 項實測，2026-08-24）**：
> 依 `A-VF27`，11 個中之 10 個為本層 `max_row=800` 讀表截斷所致之偽陽
> （9 個實在第 800 列之後，1 個表內逐字名為 `FOA _Presence`）。
> **真正表內所無者僅 `Greeting_Light`（其二 leaf）。**
>
> **本輪之獨立確認（R-VF92 一）**：以 zipfile 直讀 xlsx 之 shared strings
> （**不經 `proxi_known()`** —— 其為被驗程式，A-VF27 之缺陷正出於它），
> 不設列上限、不限欄，實測 `Greeting_Light` **確不在表內**；
> 對照組 `Heated_Seats`／`AUX_Switch_Types`（列 911）／
> `Blindspot_Trailer_Detection`（列 810）／`FOA _Presence` **皆在表內**。
> 即該必不命中錨點之不命中係「因資料如此」，非「因讀不到」。
>
> **⚠ 同一路徑另測到**：表內有 **`Greeting_Lights_Menu`** 一參數，與本件所求之
> `Greeting_Light` **名近而不同**。**本層不以名近推定其對應**（`R-VF92` 二：
> 比對不符時不得改取他標的，`A-VF28` 之教訓）—— **登記於此並回報，未改取、未據以生成**。
> **請上游一併裁示** `Greeting_Light` 與 `Greeting_Lights_Menu` 是否為同一參數；
> 若是，本件即可結案。

**狀態：未送出**（送出屬 Pei，R-VF27）。

---

## DR-35（新，**Urgency Low** —— `LaneSenseWarning-014` 條文內部不一致；A-VF18／V23 §4.1 開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-34**（R-VF10）。

**型別（R-VS45）：型 A — 規格缺陷（條文內部矛盾）。**

**成對之 anomaly：A-VF18。**

`SWE1-VC-LaneSenseWarning-014`（`SYS-RA-VF230_V1-537`，
`VF230_V1_PHDCC27_VF_2024`）之條文，其**第 4 句與結論句所指之 feature 不同**：

```
第 4 句   The HMI layer shall evaluate the received Lane_Assist PROXI value to
          determine Cornering Lights feature availability.
結論句    If $Lane_Assist$ = [Not Present] or [Lane Departure Warning], the LTM
          or ETM shall not display the Lane Sense Warning customer setting
```

**`Cornering Lights` 與 `Lane Sense Warning` 為不同功能** ——
二者於 037 為不同之 Requirement Title 簇，雖同屬 Test Set `Lane and Lighting`。

**請確認**：`Lane_Assist` 之 PROXI 值所決定者為 `Cornering Lights` 之可用性、
`Lane Sense Warning` 之可用性，抑或二者皆是？

**影響**：pilot #1 之 **seq 240**。其驗證對象因上游條文自相矛盾而不確定。

**本層之處置（已定，不待覆文）**：依 **V23 §4.2 以結論句為準**
（結論句為該需求之處置條款），TC 之驗證對象為 `Lane Sense Warning` 之不顯示；
於 Remarks 具名該不一致與本 DR 編號。**不自行調和二者。**

**狀態：未送出**（送出屬 Pei，R-VF27）。

---

## DR-36（新，**Urgency Medium** —— `<Name>.Info` 訊號之歸屬；R-VF77 一開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-35**（R-VF10）。

**標的**：VF230 之 4 條 leaf（`SWE1-VC-TimeandDateSettings-003`／`-006`／`-007`／`-008`）
其條文所載之訊號採 `<Name>.Info` 命名空間：

```
Hour1_Setting.Info, Hour2_Setting.Info, Minute1_Setting.Info, Minute2_Setting.Info
GPS_Automatic_Time_Adj_Setup.Info
```

**實測**：二份 DBC（`PDT27_E2A_R4_BHCAN.dbc`／`PDT27_E2A_R5_FDCAN8.dbc`）
**查無同名訊號**。而 VF230 其餘 617 條之訊號皆為 `TELEMATIC_*`／`IPC_*`
（在 DBC 內可解）。

**所詢**：

1. `<Name>.Info` 是否為 **CAN 訊號**？若是，其在哪一份 DBC／哪一個 message？
2. 若否 —— 其為 **service 層介面**（條文言「send … to the Date & Time Service」）——
   則該 4 條之 TC **無法以 `Send CAN:` 書寫**，其刺激與斷言之手段為何？
3. `-003` 所列之 `Hour1`／`Hour2`／`Minute1`／`Minute2` 為**四個獨立訊號**，
   抑或同一時間值之四個欄位？其影響該條之等價類劃分。

**其阻塞者**：該 4 條依 **R-VF77 一**已列入 `data/vf230_isolated.tsv` 隔離，
**不入量產**（量產母體 574 已扣之）。**本 DR 未解則該 4 條不得解除隔離。**

**登記者**：執行層（38 輪 W-VF69 §4）。**送出屬 Pei**（R-VF27）。

---

## DR-37（新，**Urgency High** —— 46 條之條文只有 message、無訊號名；W-VF69 §5 開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-36**（R-VF10）。

**標的**：VF230 之 **46 條 leaf**（逐條列於 `docs/reports/vf230_wvf69_skipped.md` A 類）。
其條文之訊號引用**只到 message 一層**：

```
SWE1-VC-ParkSense-086
  … send the request using CarPropertyManager.setProperty() with the
  TELEMATIC_VEHICLE_SETUP signal value as Warn.
SWE1-VC-ParkSense-088
  HW supplier shall notify the IPC_VEHICLE_SETUP signal via VHAL interface.
```

`TELEMATIC_VEHICLE_SETUP` 為 **message**（DBC `msg_id 158`），其下有數十個訊號。
**條文未指出是哪一個。**

**本層已試之路徑及其結論**：以條文所帶之值反查該 message 內具該值之訊號 ——
**唯一解 13／多解 13／條文未帶值 20**。**多解者佔可反查者之半，
故反解即推測，本層不採用**（R-VF79 一：抽不出者回報「未查」，不得回報為「無」）。

**所詢**：該 46 條之訊號名各為何？其來源為 037 之補充、LID、抑或另有對映表？

**其阻塞者**：該 46 條**未生成任何 TC**。
**另具名一項與現有判定之抵觸**：該 46 條於 `vf230_writability.tsv` **全數判 W0**
（完全可寫），且 `value_source` 與 `blocker_class` **皆為空** ——
即 W-VF44 之 `B5-signal-absent` 路徑對「有 message 無 signal」之形態未觸發。
**本層未逕自改判**（其須重跑全量且屬分級之判準變更），登記為 **A-VF25**，請裁。

**登記者**：執行層（38 輪 W-VF69）。**送出屬 Pei**（R-VF27）。

---

## DR-38（新，**Urgency Medium** —— 2 條之條文動作句與其值極性相反；W-VF69 §5 開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-37**（R-VF10）。

**標的**：

```
SWE1-VC-SuspensionServiceMode-004
  When the customer chooses to **enable** the Suspension Service Mode setting …
  CarPropertyManager shall invoke setProperty() with propId = Susp_Tire_Jack_Req
  and value = [OFF]. … Then the HMI/LTM/ETM shall update the Suspension Service
  Mode customer setting status to **OFF** …

SWE1-VC-RearGuidanceLightswithCargoLights-017
  … chooses to **disable** … 而其值為 **Enable**
```

即**動作句之動詞與其 `value`／結論句之極性相反**。

**所詢**：何者為誤植 —— 動作句之動詞，抑或其值？

**本層之處置（未待答即照 V23 §4.2）**：**以結論句為準**
（結論句為該需求之處置條款），於該 TC 之 Remarks 逐字具名其不一致與本 DR 編號，
**不自行調和二者**。`SuspensionServiceMode-004` 即本組 seq **268**，已具名。
另一條不在本組 150 之內。

**其形態**：與 **A-VF18**（`LaneSenseWarning-014`，DR-35）同族。
**全母體之量測**：可抽之 497 條中，此形態 **2 條**（偵測式為
`chooses to (enable|disable)` 與值之極性比對，**其為已知集合，非全集**）。

**登記者**：執行層（38 輪 W-VF69）。**送出屬 Pei**（R-VF27）。

---

## DR-39（新，**Urgency High** —— 條文未指名值時該訊號應送何值；R-VF81 三開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-38**（R-VF10）。

**標的**：**128 條 leaf**（逐條列於 `data/vf230_isolated.tsv` 之
「R-VF81 三：未指名值且無語意對應」類），其中 **訊號上行型 100 條**、
訊號送出型 28 條。

**其形態**：條文只述「HMI 應依所收到之值更新顯示」而**不指名任何具體值**，例如

```
SWE1-VC-…（訊號上行型）
  HW supplier shall notify the IPC_VEHICLE_SETUP.<Sig> signal via VHAL interface.
  … The HMI layer shall evaluate the received signal and update/display the
  <Setting> setting information accordingly.
```

**所詢**：條文未指名值時，該訊號應以何值為被驗分區？

1. 取 DBC 值域之**任一分區**（如 pilot #2 seq 264／265 之作法，該二條已通過覆核）？
2. 取**全部分區**（每值一條 TC）？
3. 抑或其值須另有來源（037 之補充、Verification Criteria）？

**其阻塞者**：該 128 條**未生成任何 TC**。

> **標的自 128 縮為 28（W-VF71 第 1 項施行 R-VF91 後）**：
> `R-VF91` 一將 `R-VF81` 三之適用範圍限縮為**訊號送出型**，
> 二令訊號上行型之未指名值改依 canon §8.4.1 之佔位形式處理。
> **訊號上行型 100 條已解除隔離並回歸母體**（其 TC 已生成，
> `input_test_data` 逐字列 DBC 有效值域全集、取列舉首值為代表值）。
> **本 DR 之現行標的為訊號送出型 28 條** —— 其第一款適用而無語意對應，維持隔離。
> 本條**維持開立**（R-VF91 五）：其所詢「條文未指名值時該送何值」仍為真問題，
> R-VF91 為其覆文到達前之可執行處置，非其替代。

**另具名一項條文之交互後果**：R-VF81 第一款以「條文之動作動詞」定語意側，
而**訊號上行型之刺激來自 HW、顧客不執行任何動作**，故其條文結構上不會有動作動詞，
**第一款對該形態恆不適用、第三款恆成立**。
**pilot #2 已核可之 seq 264／265 正屬此類** —— 照 R-VF81 字面，
該二條須改為 PENDING，**即該條回頭否定了兩條已通過覆核之 pilot 條**。
**本輪未改動 pilot #2**，具名待裁。

**登記者**：執行層（38 輪 W-VF70）。**送出屬 Pei**（R-VF27）。

---

## DR-40（新，**Urgency Medium** —— 8 條之條文值與 DBC 值域不符；W-VF70 §2 開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-39**（R-VF10）。

**標的與逐條成因**：見 `docs/reports/vf230_wvf70_cclass.md`。

| 成因 | 條數 | 例 |
|---|---|---|
| **(a) DBC 值域拼字** | 1 | `Eng_Off_Pwr_Delay_Req`：條文 `Forty_Five_Sec`／DBC **`Fourty_Five_Sec`**（`Fourty` 非英文正詞，**DBC 側誤**） |
| **(b) 條文誤植** | 7 | `Power_Tailgate_Enable_Req` 條文 `Disable`／DBC `Disabled`（差一字尾，2 條）；`DRLEnable_Req` 條文 `Early` 而值域為 `False`／`True`（1 條）；`Trail_Brk_Type_Req` 條文 `One`～`Four` 而值域為 `Heavy_Electric` 等制動型別（4 條） |

**所詢**：各條以何者為準 —— 條文抑或 DBC？(a) 是否為 DBC 之勘誤？

**本層之處置**：**只判不改**（V30 §5.2）。該 8 條列入隔離、未生成 TC。
**具名一項本層曾犯之錯**：首版於值對不上時自動改取「同條文內值域能容納該值之
另一訊號」，致 `TrailerBrakeType032` 之 `Trail_Brk_Type_Req` 被偷換為
後句另一情境之 `Trail_Num_Req`，**產出驗錯訊號之 TC**。**已撤回**（見 A-VF28）。

**登記者**：執行層（38 輪 W-VF70）。**送出屬 Pei**（R-VF27）。

---

## DR-41（新，**Urgency Medium** —— PROXI 型 9 條之條文只述取值流程而不帶值；W-VF71 第 3 項開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-40**（R-VF10）。
> **登記，未送出。**

**標的**：**9 條 leaf**（PROXI 型，`data/vf230_isolated.tsv` 之
「事實不足以書寫（R-VF80 一）」類內）：

```
SWE1-VC-4AUXSwitches-027          SWE1-VC-ConsumptionUnit-032
SWE1-VC-ChargePowerLevel-044      SWE1-VC-ChargePowerLevel-045
SWE1-VC-EngineOffPowerDelay-044   SWE1-VC-EngineOffPowerDelay-045
SWE1-VC-RearSeatReminder-053      SWE1-VC-RearSeatReminder-054
SWE1-VC-Language-060
```

**其形態**：條文完整敘述 PROXI 之**取值鏈路**（HMI → VehicleConfigManager →
VehicleConfigService → SystemProperties），**而自始至終不出現任何具體值**——
既無 `If <Param> = [ <Value> ]`，亦無 `receives the value <Value> via signal`。

```
SWE1-VC-4AUXSwitches-027
  The HMI layer shall send a request to VehicleConfigManager to retrieve the
  AUX_Switch_Types configuration value. VehicleConfigManager shall communicate
  with VehicleConfigService to obtain the requested configuration value.
  VehicleConfigService shall read and verify the AUX_Switch_Types configuration
  value from SystemProperties and/or HW configuration data. …
```

**所詢**：PROXI 參數之條文未帶值時，該參數應以何值為被驗分區？

1. 自 PROXI 表之該參數值域取一代表值（即 **R-VF91 二**對訊號上行型之處置，
   平移至 PROXI 側）？
2. 每值一條 TC？
3. 抑或其值須另有來源（037 之補充、Verification Criteria）？

**其與 DR-39 之別**：DR-39 問**訊號**側（DBC 值域），本條問 **PROXI** 側
（PROXI 表值域）。二者之來源檔不同、值域形態不同，**故不併案**。

**其阻塞者**：該 9 條**未生成任何 TC**。

> **本條之標的數自 11 更正為 9（W-VF71 第 3 項實測）**：
> V34 §4 第 3 項載「B 類 11 條，含 2 條連參數名都抽不出者」。
> **實測該 2 條（`SWE1-VC-TurnSignalActivatedBlindSpotCameraView-065／066`）
> 之參數名 `Turn_Signal_Camera_View` 逐字在條文內，且在 PROXI 表內** ——
> 其抽不出係本層之抽取式只認 `retrieve the … configuration`，
> 而該 2 條之條文以**參數名起首**（`Turn_Signal_Camera_View PROXI configuration.`）。
> **即本層讀不到而報為資料所缺** —— `A-VF13`／`A-VF21`／`A-VF25`／`A-VF27` 之同族。
> 抽取式已放寬（`PROXI_CLAUSE_LEAD`，附 5 個假陰／假陽錨點），**該 2 條已回收入母體**。
> **不以其入 DR** —— 問上游一個本層自己讀不到的東西，是問錯問題。

---

## DR-42（新，**Urgency Medium** —— 同家族之二對 leaf 其條文逐字相同；W-VF72 開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-41**（R-VF10）。**登記，未送出。**

**標的**：**2 對 4 條 leaf**

```
SWE1-VC-ParkSenseBasedCameraActivation-078  ／ -080
SWE1-VC-AutoOnDriverComfort-2Option-103     ／ -104
```

**其形態**：同一 leaf 家族內之二條 leaf，其 `desc` **逐字相同**
（以 sha1 比對，非目視），其 PROXI 參數與值亦相同。

```
-078 ／ -080  參數 Parksense_Camera_View  值 "Absent"   sha1 同
-103 ／ -104  參數 Heated_Seats           值 "Absent"   sha1 同
```

**其後果**：二者所生之 TC **逐字相同**，
而 canon §4.3 逐字令「two sibling tc_titles that read identically = **FAIL**」。

**所詢**：該二對是否應為**一條**需求？抑或其差異存在於 037 而未進 035 之 `desc`？

**本層之處置**：**保留首條、隔離次條**（`-080`／`-104`），登記於
`data/vf230_isolated.tsv`。**未造區辨 token 消解之** ——
二條文既逐字相同，任何區辨皆為本層所造，
**即以造值消解不符**（`R-VF92` 二、`R-VF79` 一之同一禁令）。

**其阻塞者**：該 2 條未生成 TC。**另 2 條（首條）已生成，不受影響。**

---

## DR-43（新，**Urgency Medium** —— `Trail_Num` 之無效值處理：條文所稱之無效值屬他訊號，且該訊號無可送之無效 raw；W-VF73 開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-42**（R-VF10）。**登記，未送出。**

**標的**：`SWE1-VC-TrailerNumber-065`（1 條）

**條文逐字**：

```
When the LTM or ETM receives the IPC_VEHICLE_SETUP.Trail_Num signal with the
value [GOOSE] or [FIFTH], $IPC_VEHICLE_SETUP.Trail_Num$, Then the HMI shall
treat the received value as invalid, shall not display the invalid enumeration,
and shall continue displaying the previously received valid Trailer Number
value until a valid signal value is received.
```

**二項實測與條文不符**（皆以獨立路徑直讀 `inputs/PDT27_E2A_R5_FDCAN8.dbc`）：

1. **`GOOSE`／`FIFTH` 不屬 `Trail_Num`。** 該二標籤實屬
   `SelTrlrStyle`／`TrlrStyle_1`–`TrlrStyle_4`（**拖車樣式**，
   值域 `NONE／TRAILER／BOAT／CAR／CARGO／DUMP／EQUIPMENT／FLAT／GOOSE／…`），
   而 `Trail_Num` 為**拖車數量**，值域僅 `One／Two／Three／Four`。

2. **`Trail_Num` 結構上不存在可送之無效值。** 其於 DBC 為
   `SG_ Trail_Num : 214|2@…` —— **2 bit**，四個 raw（0–3）**全部已定義**。
   即使條文所指之訊號正確，亦無 raw 可用以送出「無效列舉」。

**所詢**：

1. 本條所指之訊號是否應為 `SelTrlrStyle`（或 `TrlrStyle_n`）而非 `Trail_Num`？
2. 若確為 `Trail_Num`，則「無效值」指何者？（其 2 bit 四值全為有效列舉）

**本層之處置**：**維持隔離，不改取他訊號**（`R-VF92` 二：比對不符時不得改取
「能容納該值之另一訊號」——改取即換掉了條文明寫之驗證標的，產出驗錯對象之 TC）。
**與 `A-VF28`（`TrailerBrakeType032` 之自動換訊號）同族**，其教訓已成文。

**其阻塞者**：pilot #3 之「無效值處理」型 **1 條未生成**。
**書寫式本身不缺** —— 既有交付範例
`Invalid heated steering wheel status value is ignored`
（送有效值並記錄 → 送無效值 → 讀顯示確認未變）可依，**缺的是資料**。

---

## DR-44（新，**Urgency Medium** —— AUX Switch 之 35 對需求描述同一可測行為；W-VF74 開立）

> **開號依據**：全庫最大已用 DR 號為 **DR-43**（R-VF10）。**登記，未送出。**

**標的**：**35 對 70 條 leaf**，全數集中於 **AUX Switch 1–4 之三個屬性**
（`PowerMode`／`Type`／`HoldLastState`）。

**其形態**：同一屬性有**二條需求，措辭不同而描述同一可測行為**，
來自不同之 `src_ref`。實例（`SWITCH1PowerMode`）：

```
-005  src_ref SYS-RA-VF230_V1-2262
  The HMI layer shall capture the customer selection for the SWITCH 1 Power Mode
  setting and send the request using CarPropertyManager.setProperty() with the
  TELEMATIC_FD_1.AUX1_PWRMD_Req signal value as IGNITION. …

-030  src_ref SYS-RA-VF230_V1-2211
  When the customer chooses to set the SWITCH 1 Power Mode setting to Ignition on
  the LTM or ETM, the HMI layer shall send the updated customer preference to
  CarPropertyManager via the Android Car API. … HMI receives the … as IGNITION
  via signal, $TELEMATIC_FD_1.AUX1_PWRMD_Req$ …
```

**二者之差為敘述層次**（Android 屬性層寫法 vs 顧客動作寫法），
**其設定、訊號、值皆同**。

**其後果為可機械判定，不涉語意推測**：所生之二條 TC 之
`pre_conditions`／`test_procedure`／`expected_result`／`input_test_data`
**四欄逐字相同**，**僅 `test_item`（條文節錄）不同** ——
即**執行二者即做同一件事**，且其 `tc_title` 亦逐字相同（canon §4.3 FAIL）。

**所詢**：該 35 對是否為同一需求之二次描述？
若是，量產應涵蓋其一或二者？（若二者皆須涵蓋，其 TC 之區辨應以何為據？）

**本層之處置**：**保留首條、去重次條**（判準為可執行四欄之逐字相同），
去重清單逐條列於 `data/_vf230_wvf69_skipped_g3.json` 之 `exec_duplicate`。
**未造假區辨**（`R-VF92` 二：不得改取他標的以消解不符；
造一個區辨 token 即宣稱二者驗不同的東西，而實測其驗同一件事）。

**其阻塞者**：**無**。35 條去重後量產仍涵蓋該 35 個行為（由其成對之另一條承擔），
**故本 DR 不阻塞交付**，僅求確認上游是否有意如此。

<details><summary>35 對之逐條清單</summary>

```
SWE1-VC-SWITCH1PowerMode-005                   同 SWE1-VC-SWITCH1PowerMode-030
SWE1-VC-SWITCH1PowerMode-006                   同 SWE1-VC-SWITCH1PowerMode-031
SWE1-VC-SWITCH1PowerMode-007                   同 SWE1-VC-SWITCH1PowerMode-032
SWE1-VC-SWITCH2PowerMode-009                   同 SWE1-VC-SWITCH2PowerMode-034
SWE1-VC-SWITCH2PowerMode-010                   同 SWE1-VC-SWITCH2PowerMode-035
SWE1-VC-SWITCH2PowerMode-011                   同 SWE1-VC-SWITCH2PowerMode-036
SWE1-VC-SWITCH3PowerMode-013                   同 SWE1-VC-SWITCH3PowerMode-038
SWE1-VC-SWITCH3PowerMode-014                   同 SWE1-VC-SWITCH3PowerMode-039
SWE1-VC-SWITCH3PowerMode-015                   同 SWE1-VC-SWITCH3PowerMode-040
SWE1-VC-SWITCH4PowerMode-017                   同 SWE1-VC-SWITCH4PowerMode-042
SWE1-VC-SWITCH4PowerMode-018                   同 SWE1-VC-SWITCH4PowerMode-043
SWE1-VC-SWITCH4PowerMode-019                   同 SWE1-VC-SWITCH4PowerMode-044
SWE1-VC-SWITCH1Type-030                        同 SWE1-VC-SWITCH1Type-003
SWE1-VC-SWITCH1Type-031                        同 SWE1-VC-SWITCH1Type-004
SWE1-VC-SWITCH2Type-033                        同 SWE1-VC-SWITCH2Type-006
SWE1-VC-SWITCH2Type-034                        同 SWE1-VC-SWITCH2Type-007
SWE1-VC-SWITCH2Type-035                        同 SWE1-VC-SWITCH2Type-008
SWE1-VC-SWITCH3Type-037                        同 SWE1-VC-SWITCH3Type-010
SWE1-VC-SWITCH3Type-038                        同 SWE1-VC-SWITCH3Type-011
SWE1-VC-SWITCH3Type-039                        同 SWE1-VC-SWITCH3Type-012
SWE1-VC-SWITCH4Type-041                        同 SWE1-VC-SWITCH4Type-014
SWE1-VC-SWITCH4Type-042                        同 SWE1-VC-SWITCH4Type-015
SWE1-VC-SWITCH4Type-043                        同 SWE1-VC-SWITCH4Type-016
SWE1-VC-SWITCH1HoldLastState-054               同 SWE1-VC-SWITCH1HoldLastState-018
SWE1-VC-SWITCH1HoldLastState-055               同 SWE1-VC-SWITCH1HoldLastState-019
SWE1-VC-SWITCH1HoldLastState-056               同 SWE1-VC-SWITCH1HoldLastState-020
SWE1-VC-SWITCH2HoldLastState-058               同 SWE1-VC-SWITCH2HoldLastState-022
SWE1-VC-SWITCH2HoldLastState-059               同 SWE1-VC-SWITCH2HoldLastState-023
SWE1-VC-SWITCH2HoldLastState-060               同 SWE1-VC-SWITCH2HoldLastState-024
SWE1-VC-SWITCH3HoldLastState-062               同 SWE1-VC-SWITCH3HoldLastState-026
SWE1-VC-SWITCH3HoldLastState-063               同 SWE1-VC-SWITCH3HoldLastState-027
SWE1-VC-SWITCH3HoldLastState-064               同 SWE1-VC-SWITCH3HoldLastState-028
SWE1-VC-SWITCH4HoldLastState-066               同 SWE1-VC-SWITCH4HoldLastState-030
SWE1-VC-SWITCH4HoldLastState-067               同 SWE1-VC-SWITCH4HoldLastState-031
SWE1-VC-SWITCH4HoldLastState-068               同 SWE1-VC-SWITCH4HoldLastState-032
```

</details>
