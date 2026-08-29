# 07 — ETM 是否即本 DUT（R-ICS22 v2(c) 先決驗證）

- 日期：2026-08-29
- 依據：`features/ics_management/RULINGS.md` `## R-ICS22 v2` (c)
  「**先決問題：ETM 是否即本 DUT**。本條之成立繫於『DUT 之 DBC 節點名為 ETM』…
  執行層於 b06 須**先驗此一前提**（取 SYSAD／SWRA／LID 三路交叉），不成立即停並報，
  佔位維持、本條不適用。」
- 探針：`features/ics_management/scripts/etm_probe_07.py`（新建，唯讀）
- 本報告不改任何 TC JSON、不改任何裁決檔。

---

## §0 掃描條件

### 0.1 docx 抽取法（SYSAD／CFTS020／CFTS022 共用）

讀 `word/document.xml` → `</w:p>` 換為換行、`</w:tc>` 換為 tab →
`re.sub(r"<[^>]+>", "", xml)` 去標籤 → `html.unescape`。
以 `\n` 切為段落陣列，段落序號 `pN` 即該陣列之 0-based index。

| 檔 | 段落總數 |
| --- | --- |
| SYSAD v1.0 | 1410 |
| CFTS020 | 5204 |
| CFTS022 | （未計；命中見 §1.3） |

### 0.2 關鍵詞與大小寫

- docx 全文掃：`ETM`／`LTM`／`SGW`／`TBM`（**大小寫敏感**，子字串比對）。
  另以大小寫**不敏感**之 `etm|ltm|sgw|tbm|telemat` 覆核 SYSAD（結果同，見 §1.1）。
- SWRA 掃：`ETM`／`LTM`／`SGW`／`TBM` 以**詞邊界**正則
  `(?<![A-Z0-9])KW(?![A-Z0-9])` 對 `str(cell).upper()` 比對（避免 `SYSTEM` 誤中）；
  另以純子字串再掃一輪 `ETM|LTM|SGW|TBM|Head Unit|HU |DUT|node|Node|ECU|Telemat|TGW_DISP_STAT|CAN-FD|FDCAN|BHCAN|ICS`。
- 屬性軸抽取：`\[ECU:([^\]]*)\]` 與 `\[Radio:([^\]]*)\]`，逗號切分後 strip。

### 0.3 LID 表頭自驗（本次實測，非沿用）

檔：`forms/Logical Identifiers and CAN Mapping v1_78.xlsx`，openpyxl `data_only=True`。
分頁 `CAN Mapping`，`dims = A1:AI2627`。

- 列 1：`c1 = "CAN Mapping"`（標題列）
- **列 2 = 群組列**：`c1=LID Information`、`c6=Powernet`、`c11=CUSW`、
  `c16=Atlantis`、**`c26=Atlantis High`**、`c31=Comments`
- **列 3 = 欄名列**：`c26=Signal Name`、`c27=CAN`、`c28=Format`、`c29=SNA`、`c30=VFs`
- **資料自列 4 起**（`r4 c1 = 2ndHdRstRelRq`）

→ 與前輪所記一致：**群組列 2、`Atlantis High` 起 c26、欄名列 3、資料自列 4**。

### 0.4 DBC 開檔

`latin-1` 開檔（非 UTF-8）。訊息邊界以**下一個 `BO_ ` 行**判定，不用空行切塊。
節點全集取 `BU_:` 行；發送者取 `BO_ <id> <name>: <dlc> <sender>` 之末欄。

---

## §1 SYSAD 路

檔：`features/ics_management/inputs/SYS3_CFTS020_ICS_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx`

### 1.1 `ETM` 於 SYSAD 全文 **查無**

大小寫敏感掃 `ETM`／`LTM`／`SGW`／`TBM`／`node`／`Node`／`DBC`：
**total hits = 0，total paragraphs = 1410**。
大小寫不敏感掃 `etm|ltm|sgw|tbm|telemat`：僅 2 命中，均為 `Telemat`，且皆非 `ETM`：

```
p217	Telematics Module
p535	Telematics ECU
```

**SYSAD 全文無 `ETM` 一詞，亦無任何 DBC 節點名清單。**

### 1.2 SYSAD 之縮寫表（§3.1）逐字：無 ETM，Telematics 之縮寫是 `TLM`

```
p166	HU
p167	Head Unit
p172	ICS
p173	Integrated Control System
p216	TLM
p217	Telematics Module
```

### 1.3 SYSAD 之 DUT 定位逐字

```
p123	The purpose of this document is to define and structure the system architecture
    required to realize the Display functionalities in the Head Unit.
p272	SYSAD-ICSAPP (ICS Application) reads ICSPowerButton, ICSScreenOffButton, and
    ICS_KNOB1_VAL (user input handling) and generates display and audio requests (trigger action).
p273	At Platform Layer,SYSAD-ICSCLIENTSERVICE reads ICSPowerButton and ICSScreenOffButton
    (input evaluation) and determines TGW_DISP_STAT and RQ_DISP_INTS (display state decision).
p1215	SYSAD-VCPU transmits ICS signals through CAN for communication.
```

系統分解表（Table 6）中，`TLM` 是**本 DUT 以外之另一元件**：

```
p534	SYSAD-TLM
p535	Telematics ECU
p536	Partial
p537	Sets Volume_Knob_Val.Info and Mute.Req
p538	reuse ECU add ICS handling
p557	TLM ECU (executes volume and mute behavior using Volume_Knob_Val.Info and Mute.Req)
p1217	SYSAD-TLM receives Volume_Knob_Val.Info and Mute.Req and executes audio behavior.
```

**SYSAD 路之所據**：本 DUT 為 Head Unit 上之 ICS 軟體（產生 `TGW_DISP_STAT`，
由 VCPU 經 CAN 送出）；文件內**未出現 `ETM`**，且其唯一之 Telematics 元件縮寫為
`TLM`，且 `TLM` 被列為**接收 DUT 輸出之他方 ECU**。
→ **SYSAD 路對「DUT 之 DBC 節點名為 ETM」不提供任何正面所據；且其 TLM 之定位與
「ETM 即 DUT」相斥（若 ETM＝Telematics 模組，則 SYSAD 將其置於 DUT 之外）。**

---

## §2 SWRA 路

檔：`features/ics_management/inputs/ICS_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`
（openpyxl `data_only=True`，**三個分頁全掃**）

| 分頁 | dims |
| --- | --- |
| `SWE1 Requirements` | A1:R224 |
| `SYS2 Traceability` | A1:E19 |
| `Excluded NRLs (HW-only)` | A1:D32 |

### 2.1 `ETM`／`LTM`／`SGW`／`TBM` 於三分頁 **全數查無**

詞邊界掃：三分頁 **0 命中**。
子字串掃之計數（三分頁合計）：

```
Counter({'ICS': 87, 'HU ': 2, 'TGW_DISP_STAT': 2, 'Telemat': 1})
```

即 `ETM` = 0、`LTM` = 0、`SGW` = 0、`TBM` = 0。

### 2.2 SWRA 對 DUT 之逐字所據

```
SWE1 Requirements  r12 c4:
  The ICS software shall monitor $ICSPowerButton$ using the HW API and manage display
  ON/OFF operational state according to display operational logic, Telematic_Power state
  handling, and HMI flow requirements.

SWE1 Requirements  r17 c4:
  The ICS software shall maintain $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$
  <> [0% Intensity] during HU Screen ON operational state and shall update gateway
  display status according to display operational mode.

Excluded NRLs (HW-only)  r8 c4:
  $TGW_DISP_STAT$ and $RQ_DISP_INTS$ low-level signal transmission handling is below
  HAL scope and managed by HW supplier.
```

**SWRA 路之所據**：確認 R-ICS22 v2 前言所引之「SWRA 011 載 DUT 維持並送出
`$TGW_DISP_STAT$`」（= r17 c4）為真；但 SWRA **通篇不含任何 DBC 節點名**
（`ETM`／`LTM`／`SGW`／`TBM` 皆 0 命中），僅以「the ICS software」「HU」指稱 DUT。
→ **SWRA 路對「節點名為 ETM」查無 —— 既不支持亦不否證，屬證據不存在。**

---

## §3 LID 路

檔：`forms/Logical Identifiers and CAN Mapping v1_78.xlsx`，分頁 `CAN Mapping`
（表頭自驗見 §0.3）。

### 3.1 `TGW_DISP_STAT` 之列：**列 2084**（逐欄逐字）

| 欄 | 群組（列 2） | 欄名（列 3） | 值 |
| --- | --- | --- | --- |
| c1 | LID Information | Logical Identifier | `TGW_DISP_STAT` |
| c2 | | Function | `HU display status` |
| c4 | | Arch Basis | `pnet` |
| c6 | Powernet | Signal Name | `TGW_A1.TGW_DISP_STAT` |
| c11 | CUSW | Signal Name | `TGW_STAT.TGW_DISP_STATSts` |
| c16 | Atlantis | Signal Name | `TELEMATIC_DISPLAY2.TGW_DISP_STATSts` |
| **c26** | **Atlantis High** | **Signal Name** | `TELEMATIC_DISPLAY2.TGW_DISP_STATSts`<br>`TELEMATIC_FD_4.TGW_DISP_STATSts ` |
| c27 | | CAN | `CAN-B`<br>`CAN-FD` |
| c29 | | SNA | `Fh` |
| c30 | | VFs | `688` |

### 3.2 LID **無發送節點欄**

`CAN Mapping` 之欄名列（列 3）全欄為
`Logical Identifier / Function / Object Text / Arch Basis / Transfer Function /
（每架構）Signal Name, CAN, Format, SNA, VFs / Usage Comment / Primary CFTS Usage /
Revision Flag / Revision Comments / Sort Tool`
—— **無 Sender／Transmitter／Node 欄**。故 LID 本身不能回答「本 DUT 之節點名」。

### 3.3 LID 唯一提及 ETM 之處（`Rev History` 分頁 r98 c4，逐字節錄）

```
ATL High
- BODY_CNTRL3.EBL_Stat is for DCSD in CAN-B
- BCM_FD_27.EBL_Stat is for ETM in FD CAN8
```

此條證明 LID 認 `ETM` 為 Atlantis High／FD CAN8 上之一個**具體 ECU**，
且與 `DCSD` 並列為不同 ECU。**但它談的是 `$EBL_Stat$`，與本 DUT 之識別無關。**

→ **LID 路之所據**：`TGW_DISP_STAT` 之 Function 為 `HU display status`，
Atlantis High 欄確為二候選並列（CAN-B／CAN-FD）；**LID 無發送節點資訊，
對「ETM 是否即本 DUT」查無所據。**

---

## §4 DBC 佐證（非三路之一）

二檔均以 `latin-1` 開檔。

### 4.1 `BU_:` 節點全集（逐字）

```
PDT27_E2A_R4_BHCAN.dbc
BU_: AMP ANC BCM DALM DCSD DDM DSM ECC ICS PDM PFTM PSM PSSM PTGM SGW SMMD SMMP

PDT27_E2A_R5_FDCAN8.dbc
BU_: ETM LTM SGW TBM
```

**BHCAN 有 `ICS` 節點，無 `ETM`／`LTM`；FDCAN8 有 `ETM`／`LTM`，無 `ICS`。**

### 4.2 目標 `BO_` 行逐字

```
BHCAN   BO_ 1500 TELEMATIC_DISPLAY2: 8 SGW
          SG_ TGW_DISP_STATSts : 0|4@0+ (1,0) [0|14] "" DCSD

FDCAN8  BO_ 1427 TELEMATIC_FD_4: 32 ETM
          SG_ TGW_DISP_STATSts : 79|4@0+ (1,0) [0|14] "" Vector__XXX
```

### 4.3 發送者計數（依 `BO_` 行末欄）

```
BHCAN : BCM 48, SGW 31, ECC 11, DSM 8, ICS 7, DDM 6, PTGM 5,
        AMP 4, DALM 4, DCSD 4, PDM 4, PFTM 4, PSM 4, PSSM 4, SMMD 4, SMMP 4, ANC 3
FDCAN8: SGW 208, TBM 84, ETM 31          （LTM 未出現 → LTM 發送 0 則，覆核 R-ICS22 v2 前言）
```

### 4.4 BHCAN 之 `ICS` 節點所發之 7 則（逐字）

```
BO_ 1504 CENTERSTACK1: 4 ICS
BO_ 1440 CENTERSTACK2: 4 ICS
BO_ 1505 CENTERSTACK4: 8 ICS
BO_ 2651930674 CFG_DATA_CODE_RSP_CENTERSTACK: 6 ICS
BO_ 1050 CLIMATIC_PANEL: 8 ICS
BO_ 2564485509 DIAGNOSTIC_RESPONSE_CENTERSTACK: 8 ICS
BO_ 2654208050 NWM_CENTERSTACK: 2 ICS
```

### 4.5 FDCAN8 之 `ETM` 所發之 31 則（訊息名，逐字）

```
CFG_DATA_CODE_RSP_ETM, CHARGE_SCHEDULE_HU1, CLIMATE_SCHEDULE_HU1,
DIAGNOSTIC_RESPONSE_FD_RVCM, DIAGNOSTIC_RESPONSE_FD_TELEMATIC,
DIAGNOSTIC_RESPONSE_RVCM, DIAGNOSTIC_RESPONSE_TELEMATIC,
DIAGNOSTIC_ROE_FD_TELEMATIC, DIAGNOSTIC_ROE_TELEMATIC, GLOB_TLM, HU_ACK,
HUReq_SSID, NM_ETM, PDC_INFO_FD_ETM, PLUG_AND_CHARGE_CONTRACT,
TELEMATIC_FD_1, TELEMATIC_FD_10, TELEMATIC_FD_11, TELEMATIC_FD_13,
TELEMATIC_FD_14, TELEMATIC_FD_15, TELEMATIC_FD_17, TELEMATIC_FD_18,
TELEMATIC_FD_19, TELEMATIC_FD_4, TELEMATIC_FD_5, TELEMATIC_FD_6,
TELEMATIC_FD_8, TELEMATIC_FD_9, TELEMATIC_VEHICLE_SETUP, V2X_HU
```

### 4.6 `Telematic_Power` 於二 DBC 皆查無

以正則 `Telematic_Power|TelematicPwr|Telematic_Pwr`（大小寫不敏感）掃二檔全文：
**BHCAN 0 命中、FDCAN8 0 命中**。
（記於此供回溯；R-ICS22 v2(b) 之「`$Telematic_Power$` 同理取 `TELEMATIC_FD_4` 側」
在本次實測中**於二 DBC 內找不到對應之 `SG_`**。此為附帶發現，非本任務裁決範圍。）

---

## §5 結論

### 5.1 判定：**不成立**（有明確反證）

「本 DUT 之 DBC 節點名為 `ETM`」**不成立**。

### 5.2 反證（決定性）：ECU 軸與 Radio 軸之排他配對

`framework.md` §「適用域（R-ICS2，暫定）」逐字：

```
`ECU ∋ {ICS, LTM}` ∧ `Radio ∋ {R1L, R1L-R, allSys}` ∧ `EE ∋ {Atlantis High, All}`
```

本 DUT 之 ECU 軸為 **`{ICS, LTM}`，不含 `ETM`**；Radio 軸為 `{R1L, R1L-R, allSys}`。
（Profile 檔名 `FW036_R1L_ICS_Profile.md`、二母文件檔名前綴 `R1LR_Atl-H` 同向。）

進一步，對 CFTS020＋CFTS022 之**單一 ECU 物件**（`[ECU:...]` 恰為一個值者）
作 ECU × Radio 共現實測：

| 排他 ECU | 物件數 | Radio 軸出現 `R1L`／`R1L-R` | Radio 軸出現 `R1M`／`R1H` |
| --- | --- | --- | --- |
| `LTM` 專屬 | 28 | 有 | **0（無一例外）** |
| `ETM` 專屬 | 59 | **0（無一例外）** | 有 |

**87 個排他物件，違例 0。** 逐字樣本：

```
CFTS022 p137  4914933: … [ECU:LTM] [Market:All] [Model Year:Default] [Radio:R1L] [EE Architecture:All]
CFTS022 p153  4914942: … [ECU:LTM] [Market:All] [Model Year:Default] [Radio:R1L-R, R1L] [EE Architecture:All]
CFTS022 p161  4914946: … [ECU:LTM] [Market:All] [Model Year:Default] [Radio:R1L-R, R1L] [EE Architecture:All]
CFTS022 p163  4914947: … [ECU:ETM] [Market:All] [Model Year:Default] [Radio:R1M, R1H] [EE Architecture:All]
CFTS022 p275  4915002: … [ECU:ETM] [Market:All] [Model Year:Default] [Radio:R1H] [EE Architecture:Atlantis High]
CFTS020 p2235 4820132: … [ECU:LTM] [Market:All] [Model Year:Default] [Radio:R1L-R, R1L] [EE Architecture:Atlantis Mid]
```

即在本專案二母文件之屬性體系中：
**`LTM` ↔ Radio `R1L`／`R1L-R`；`ETM` ↔ Radio `R1M`／`R1H`，二者互斥。**
本 DUT 為 **R1L-R**，故其 ECU 為 **`LTM`**，**不是 `ETM`**。

且 `ETM` 與 `ICS` 在 CFTS022 之 ECU 軸中**同列並存為不同值**，逐字：

```
CFTS022 p127  4914928: … [ECU:DVD, ETM, CDM, LTM, ICS] …
CFTS022 p178  4914955: … [ECU:DVD, LTM, ETM, RRM, ICS] …
CFTS022 p136  Notation Convention: The list of Component Acronyms referenced in this
              chapter are: RRM, LTM, ETM, ICS, AMP, CDM, FPDM, DVD, VES2, VES3, VRM,
              TBM, TBM2 and SCCM. …
```

→ `ETM`、`LTM`、`ICS` 為**三個不同之 Component Acronym**。本 DUT 之 ECU 軸
`{ICS, LTM}` 兩個候選**皆非 `ETM`**；無論 DUT 邊界最終收斂到 `ICS` 或 `LTM`，
「ETM 即本 DUT」皆不成立。

### 5.3 三路交叉之總表

| 路 | 對「DUT 節點名 = ETM」之所據 |
| --- | --- |
| SYSAD | **無正面所據，且方向相斥**。全文 0 次 `ETM`；Telematics 之縮寫為 `TLM`，且 `SYSAD-TLM (Telematics ECU)` 被列為**接收 DUT 輸出之他方元件**（§1.2／1.3） |
| SWRA | **查無**。三分頁 `ETM`／`LTM`／`SGW`／`TBM` 皆 0 命中；僅以 `the ICS software`／`HU` 指稱 DUT（§2.1／2.2） |
| LID | **查無**。`CAN Mapping` 無發送節點欄；唯一 `ETM` 之提及在 `Rev History` 且係 `$EBL_Stat$` 之事（§3.2／3.3） |
| （反證來源） | **`framework.md` 適用域 + CFTS020/022 之 ECU×Radio 排他實測**：DUT ECU ∈ {ICS, LTM}，`ETM` ↔ R1M/R1H，與本 DUT 之 R1L-R 互斥（§5.2） |

三路皆**未提供**任何支持所據；而母文件之屬性軸提供了**明確反證**。
故非「不足」，係「**不成立**」。

### 5.4 R-ICS22 v2 前言之新量測，於本次覆核之處置

R-ICS22 v2 前言以「FDCAN8 之 LTM 發送 0 則訊息」推想 `ETM` 即 DUT。
本次覆核 **確認該量測為真**（§4.3：FDCAN8 之 `BO_` 發送者統計中 `LTM` 不出現）。
但該事實之另一解讀同樣成立且與屬性軸相符：
**`PDT27_E2A_R5_FDCAN8.dbc` 對 `LTM` 節點僅宣告其存在（`BU_:`）而未配置任何發送訊息**，
即該 DBC 未涵蓋 R1L／R1L-R（LTM）變體之發送側。
「LTM 送 0 則」→「所以 DUT 一定是 ETM」在本專案屬性軸下不能成立。

### 5.5 對主實例之建議（不代擬裁決）

- R-ICS22 v2(c) 之前提**不成立** → 依該條文自身之指示：**停並報，12 處佔位維持，
  R-ICS22 v2(a)(b) 不適用**。
- 隨之未解者（**非本任務裁決範圍，僅列出**）：
  1. 若 DUT 節點名為 `LTM`，則二 DBC 中**無任何 `TGW_DISP_STAT` 之 DUT 發送側**
     （FDCAN8 之 LTM 發 0 則；BHCAN 無 LTM 節點）。R-ICS22 v2(a)「取 DUT 自身為
     發送者之那一條」在現有 DBC 上**無對應物**。
  2. `Telematic_Power` 於二 DBC 全文查無（§4.6），R-ICS22 v2(b) 之後半句
     亦失其實測基礎。
  3. DUT 之 ECU 邊界（`ICS` vs `LTM`）本即 DR-ICS9 待決（framework.md 自記
     「DUT 邊界待 DR-ICS9 上游確認」）。
- 若欲翻轉本判定，所缺之證據為：**一份指名本 DUT（R1L-R／Atlantis High）之
  DBC 節點名之上游文件**，或 **R1L-R 變體所綁定之 FD CAN DBC**（其中 DUT 應有
  發送訊息）。現有三路皆不含此資訊。
