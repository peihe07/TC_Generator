# 05_coverage_gaps —— ICS Management 覆蓋缺口清單

> 下放包 05 作業 D。**本檔不生 TC、不改任何 TC JSON、不動任何素材檔、不代擬裁決條文。**
> 本檔**不自取 `A-` 或 `DR-` 新編號**：需新編號者一律寫 `A-ICS?` 並說明，取號屬分析層。
> 依 R-ICS23(a)：短按／長按之定義**不得以 FPDM 之條文充當**，故本檔不列任何
> 「可暫用 4819593／4819599 之定義」之建議。
> 本檔全部數字為實測，量測腳本 `scripts/gap_probe_05.py`（新建，唯讀）。

- 執行日：2026-08-29
- 產出者：執行層（下放包 05 作業 D）

---

## §0 掃描條件

### 0.1 實際執行之指令

| # | 指令 | 用途 |
|---|---|---|
| 1 | `python3 features/ics_management/scripts/cfts020_probe.py --section 1.8.1.3 --json` | `1.8.1.3` 逐物件三軸實值與 R-ICS2 v2(b) 判定（下放包 05 明令自行實測，**不抄 `03_cfts020_recon_v2.md`**）|
| 2 | `python3 features/ics_management/scripts/gap_probe_05.py` | §1／§3／§4 之全部數字：全文關鍵詞掃描、RD 覆蓋矩陣、VC 對照、裸按壓步驟計數 |
| 3 | `python3 features/ics_management/scripts/cfts020_probe.py --object 4819541 --full` | §5-1 之單物件複驗 |

`cfts020_probe.py` 為既有腳本，**唯讀執行、未修改**（sha256 `22d5e7f4…`）。
`gap_probe_05.py` 以 `importlib` 依路徑載入該檔並呼叫其 `parse()`，
**判準沿用該檔，不重寫**（sha256 `0356b01f…`）。

### 0.2 比對之欄位

| 面 | 來源 | 欄位 |
|---|---|---|
| CFTS020 物件 | `inputs/R1LR_Atl-H_26PI1.5 … CFTS_020 ICS and DCSD _20260310-1533.docx` 之 `word/document.xml` | `ECU` / `Radio` / `EE Architecture` / `Artifact Type` / `State` |
| RD 全集 | `inputs/ICS_Management_…_SWRA.xlsx`（sha256 `b853c336…`）分頁 `SWE1 Requirements` | A 欄（`SWE-ICS-nnn`）、C 欄 `Requirement Title`、**Q 欄 `Verification Criteria`**、R 欄 `Verification Method` |
| SWE1 ID 全集（含 011／012） | 同檔分頁 `SYS2 Traceability` | A 欄 `SWE1 ID`、C 欄 `Sys-RA-Feature-ID(s)`、E 欄 `SWE1 Requirement Title` |
| 現有 TC | `generated/b01`～`b04` 之 `b0N_tcs.json` | `tcs[].req_id`、`tc_title`、`test_set`、`specification_reference`、`design_method`、`has_pending`、`test_procedure` |

### 0.3 大小寫與詞界

- **物件軸值比對**：沿用 `cfts020_probe.py` —— **區分大小寫之精確字串集合交集**，
  不作正規化、不作前綴比對；軸不存在記 `None`（**不視為空集合**，R-ICS9(b)）。
- **關鍵詞全文掃描**（`Short Press` / `Long Press` / `<Tpress>`）：
  **區分大小寫之子字串比對**，**不作詞界（`\b`）限制、不去連字號、不作換行壓平**
  —— 來源為 docx 之 `word/document.xml`，物件本文於抽取時已為單行，
  故 A-ICS32 之 PDF 斷詞問題於本掃描不成立。
  另同時以 `casefold()` 之不分大小寫掃一次，二組數字皆報（§2-1-3）。
- **RD ID**：`strip()` 後以 `^SWE-ICS-\d{3}$` 完全比對；`SWE1 ID` 以 `^SWE1-ICS-\d{3}$`。
- **`req_id` 比對**：逐字（不正規化）；`SWE-ICS-nnn`（SWRA 需求分頁形制）
  與 `SWE1-ICS-nnn`（SYS2 Traceability 形制）**為不同字面**，
  本檔於矩陣中以尾三碼對齊並具名其形制差異，**未逕自視為同一鍵**。
- **裸按壓步驟**：`test_procedure` 逐行，行內含 `Press the ICS`
  且該行**不含** `and hold`、亦**不含** ` for `（前後各一空白）者計入；
  三者皆為區分大小寫之子字串比對。

### 0.4 母數（實測）

| 項 | 值 |
|---|---|
| CFTS020 物件母數 | **2180** |
| `1.8.1.3`（含子節）物件數 | **24** |
| SWRA `SWE1 Requirements` 之 RD 數 | **10**（001～010） |
| SYS2 Traceability 之 SWE1 ID 數 | **12**（001～012） |
| 現有 TC 總數（b01～b04） | **23** |

> **註**：下放包 05 之敘述為「`SWE-ICS-001`～`012`」，但實測 `SWE1 Requirements`
> 分頁僅至 **010**；011／012 僅存於 `SYS2 Traceability`。此即 DR-ICS2 所問之缺列，
> 本檔之 §3 矩陣仍列滿 012 列，011／012 之「RD 欄」記為**需求分頁查無**。

---

## §1 缺口總表

編號欄之 `G1`～`G7` 為**本報告內之行號，非台帳編號**。
「台帳號」欄僅 G1 有既存號（A-ICS33）；其餘寫 `A-ICS?`，取號屬分析層。

| # | 台帳號 | 缺口描述（一行） | 受影響 TC 數 | 對應 DR |
|---|---|---|---|---|
| G1 | **A-ICS33** | `Short Press`／`Long Press` 之**行為定義**於 ICS 側無母條，`1.8.1.3` 之 24 物件中 23 判不適用 | **9**（10 個裸按壓步驟） | DR-ICS6（附問） |
| G2 | `A-ICS?` | `SWE-ICS-005`（ICSMuteButton）**完全無 TC**；成因為 SWRA Description +1 位移未解、CFTS020 無直載（R-ICS15(c) 不解鎖） | 0（該 RD 之 TC 數為 0） | DR-ICS1 |
| G3 | `A-ICS?` | `SWE-ICS-009`（Back_Button）**完全無 TC**；成因為唯一直載原句 4819554 之 `Market` 限 NAFTA，市場軸未定而凍結（R-ICS15(b)） | 0 | DR-ICS13 |
| G4 | `A-ICS?` | `SWE1-ICS-011`（HU Screen ON）**完全無 TC**，且 SWRA 需求分頁**缺列**（無 Description、無 VC） | 0 | DR-ICS2 |
| G5 | `A-ICS?` | `SWE1-ICS-012`（Rear View Camera Transition）**完全無 TC**，且需求分頁**缺列** | 0 | DR-ICS2 |
| G6 | `A-ICS?` | `SWE-ICS-004` 之 VC 明載 **browse／scroll／tune 三種操作**，現有 2 條僅取 browse 一種，且其行為以 `PENDING: DR-ICS6` 佔位；scroll／tune 無具名涵蓋 | 2 | DR-ICS6 |
| G7 | `A-ICS?` | `SWE-ICS-008` 之 VC 明載 `HMI navigation flow`，現有 1 條之目標畫面為 `PENDING: DR-ICS6` 佔位，末步僅斷言「畫面有變」而非「流向規定之畫面」 | 1 | DR-ICS6 |

另有二件**非覆蓋缺口**之實測不符（台帳字面與實測不一致），列於 §5，
一併寫 `A-ICS?`：`§5-1`（4819541 逐字載 `<Tpress> = 500 msec` 等六個時間變數值）、
`§5-2`（「23 皆為 `[ECU:FPDM]`」與實測之三分不符）。

---

## §2 逐筆缺口

每筆四個必要欄位：**① 缺口描述 ② 所缺母條之位置與其排除原因 ③ 受影響之 TC ④ 對應 DR**。

---

### G1 — A-ICS33（短按／長按定義缺口）

#### ① 缺口描述

CFTS020 `1.8.1.3 Button Press Events` 定義了三種按壓事件
（`Short Press Event`、`Long Press Event (a.k.a. Press and Hold Event)`、
`Press and Move Event`）。**該章之 24 個物件中 23 個依 R-ICS2 v2(b) 判不適用於本 DUT**，
唯一判適用者為章節引言（`Description` 型，無可驗行為）。
後果：本 feature **無母條可據以區別「短按」與「長按」**，
亦無母條界定按壓達何時長始構成何種事件。
現有 TC 之按壓步驟因此一律為**未定義時長之裸按壓**，
其「按下多久」在台架上無規格依據，屬**未涵蓋之驗證面**，非已驗而漏寫。

依 R-ICS23(a)，此為**採認之處置**（本 feature 不驗短長按之區別），
**不得以 FPDM 之條文充當** —— 4819593／4819599 等物件屬 `FPDM`／`CCDMF`，
為不同 ECU、不同適用域，本檔不列其為候選、不建議暫用。

#### ② 所缺母條之位置與其排除原因（逐物件實測表）

母條所在：`1.8.1.3.1 Short Press Event {4819592}`（§1.8.1.3.1）與
`1.8.1.3.2 Long Press Event (a.k.a. Press and Hold Event) {4819598}`（§1.8.1.3.2，含 `<Tpress>`）。

排除原因：**`[ECU:FPDM]`（及 `[ECU:CCDMF]`）—— 依 R-ICS2 v2(b)(ii) 之實質不適用，
不是軸缺**。ECU 軸**存在**且 ∩ `{ICS, LTM}` = ∅，故排除；
v2(b)(ii) 之「軸不存在時不視為不適用」在此**不成立**（軸是存在的）。

實測（指令 1，`--section 1.8.1.3 --json`，**逐物件列出，非抄報告**）：

| ObjectID | § | Artifact Type | ECU | Radio | EE Architecture | v2 判定 | 理由（腳本輸出原文） |
|---|---|---|---|---|---|---|---|
| 4819588 | 1.8.1.3 | Description | **軸缺** | VP384, R1M, R1L, VP484, R1L-R, R1H, VP4R84 | Atlantis High, PowerNet, Atlantis Mid | **適用** | — |
| 4819589 | 1.8.1.3 | Subsystem Functional Requirement | FPDM | VP484, R1H, VP4R84, R1L-R, VP384, R1M, R1L | PowerNet, Atlantis Mid, Atlantis High | **不適用** | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819590 | 1.8.1.3 | Subsystem Functional Requirement | FPDM | VP4R84, R1L, R1L-R, VP484, VP384, R1M, R1H | PowerNet, Atlantis Mid, Atlantis High | **不適用** | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819591 | 1.8.1.3 | Subsystem Functional Requirement | FPDM | VP384, R1H, R1L-R, VP484, R1M, VP4R84, R1L | Atlantis Mid, Atlantis High, PowerNet | **不適用** | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819593 | 1.8.1.3.1 | Description | FPDM | VP4R84, VP484, R1L, R1H, R1L-R, R1M, VP384 | Atlantis Mid, Atlantis High, PowerNet | **不適用** | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819594 | 1.8.1.3.1 | Subsystem Functional Requirement | **軸缺** | VP384, VP484, VP4R84 | PowerNet | **不適用** | Radio ['VP384', 'VP484', 'VP4R84'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819595 | 1.8.1.3.1 | Subsystem Functional Requirement | FPDM | R1L, R1L-R, R1M, VP4R84, R1H, VP484, VP384 | Atlantis High, Atlantis Mid, PowerNet | **不適用** | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819596 | 1.8.1.3.1 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | **不適用** | Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819597 | 1.8.1.3.1 | Subsystem Functional Requirement | FPDM | R1L-R, R1L, R1M, R1H, VP484, VP4R84, VP384 | Atlantis High, PowerNet, Atlantis Mid | **不適用** | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819599 | 1.8.1.3.2 | Description | FPDM, CCDMF | VP4R84, R1H, R1L, R1L-R, R1M, VP484, VP384 | Atlantis Mid, PowerNet, Atlantis High | **不適用** | ECU ['FPDM', 'CCDMF'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819600 | 1.8.1.3.2 | Subsystem Functional Requirement | **軸缺** | R1M, R1H | Atlantis High | **不適用** | Radio ['R1M', 'R1H'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅ |
| 4819601 | 1.8.1.3.2 | Subsystem Functional Requirement | FPDM, CCDMF | VP484, R1M, R1L-R, VP384, R1H, R1L, VP4R84 | Atlantis High, Atlantis Mid, PowerNet | **不適用** | ECU ['FPDM', 'CCDMF'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819602 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF | VP384, R1H, VP4R84, R1M, R1L-R, VP484, R1L | Atlantis Mid, Atlantis High, PowerNet | **不適用** | ECU ['CCDMF'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819603 | 1.8.1.3.2 | Subsystem Functional Requirement | FPDM, CCDMF | VP384, R1L-R, VP484, R1L, R1H, VP4R84, R1M | Atlantis High, PowerNet, Atlantis Mid | **不適用** | ECU ['FPDM', 'CCDMF'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819604 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF, FPDM | VP384, R1M, VP484, R1L, VP4R84, R1H, R1L-R | Atlantis High, PowerNet, Atlantis Mid | **不適用** | ECU ['CCDMF', 'FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819605 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF, FPDM | R1L-R, VP4R84, R1M, VP384, R1H, VP484, R1L | Atlantis High, Atlantis Mid, PowerNet | **不適用** | ECU ['CCDMF', 'FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819606 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF | R1H, R1M, R1L-R, R1L, VP4R84, VP484, VP384 | Atlantis High, PowerNet, Atlantis Mid | **不適用** | ECU ['CCDMF'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819607 | 1.8.1.3.2 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | **不適用** | Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819608 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF, FPDM | VP4R84, VP384, R1L-R, R1L, R1H, VP484, R1M | PowerNet, Atlantis Mid, Atlantis High | **不適用** | ECU ['CCDMF', 'FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819610 | 1.8.1.3.3 | Description | FPDM | VP4R84, VP484, R1L-R, R1M, R1L, R1H, VP384 | Atlantis Mid, PowerNet, Atlantis High | **不適用** | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819611 | 1.8.1.3.3 | Subsystem Functional Requirement | FPDM | R1H, VP4R84, R1L-R, VP484, VP384, R1L, R1M | PowerNet, Atlantis High, Atlantis Mid | **不適用** | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819612 | 1.8.1.3.3 | Subsystem Functional Requirement | FPDM | R1M, R1L-R, R1H, VP484, VP384, R1L, VP4R84 | PowerNet, Atlantis Mid, Atlantis High | **不適用** | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |
| 4819613 | 1.8.1.3.3 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | **不適用** | Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819614 | 1.8.1.3.3 | Subsystem Functional Requirement | FPDM | R1L, VP384, VP484, R1L-R, VP4R84, R1H, R1M | Atlantis Mid, Atlantis High, PowerNet | **不適用** | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） |

**判定分佈（實測）**：適用 **1**、不適用 **23**（合計 24）。

**23 個不適用之成因三分（實測；與 R-ICS23(a) 之字面不符，見 §5-2）**：

| 成因 | 物件數 | ObjectID |
|---|---|---|
| ECU 軸含 `FPDM`（單獨或與 `CCDMF` 併列） | **16** | 4819589, 4819590, 4819591, 4819593, 4819595, 4819597, 4819599, 4819601, 4819603, 4819604, 4819605, 4819608, 4819610, 4819611, 4819612, 4819614 |
| ECU 軸僅 `CCDMF`（**不含 FPDM**） | **2** | 4819602, 4819606 |
| ECU 軸**缺**，因 `Radio`／`EE` 落空而不適用 | **5** | 4819594, 4819596, 4819600, 4819607, 4819613 |

唯一判適用者 4819588 之全文逐字：

> There are several button press events that can be applied to the physical (hardkeys) and virtual (touchscreen) softkey presses. These events are described below. Refer to specific sections in this specification for the applied behavior related to these events.

`Artifact Type` = `Description`，內容為章節引言且明文外指
（`Refer to specific sections … for the applied behavior`），**無可驗行為**，
故不能作為短長按定義之母條。

#### ②-補 全文複驗：ICS 側是否另有母條（實測，非推論）

指令 2 之全文掃描（母數 2180 物件）：

| 關鍵詞 | 區分大小寫命中物件數 | 其中**判適用**者 | 不分大小寫命中數 | 其中判適用者 | 命中之章節 |
|---|---|---|---|---|---|
| `Short Press` | 16 | **0（無）** | 61 | **0（無）** | 1.5.1.3, 1.5.1.3.1, 1.8.1.3, 1.8.1.3.1, 1.11.1.3, 1.11.1.3.1, 1.14.1.3, 1.14.1.3.1 |
| `Long Press` | 31 | **0（無）** | 42 | **0（無）** | 1.5.1, 1.5.1.3, 1.5.1.3.1, 1.5.1.3.2, 1.8.1.3, 1.8.1.3.1, 1.8.1.3.2, 1.11.1, 1.11.1.3, 1.11.1.3.1, 1.11.1.3.2, 1.14.1, 1.14.1.3, 1.14.1.3.1, 1.14.1.3.2 |
| `<Tpress>` | 25 | **1（4819541）** | 25 | **1（4819541）** | 1.5.1, 1.5.1.3.2, 1.8.1, 1.8.1.3.2, 1.11.1, 1.11.1.3.2, 1.14.1, 1.14.1.3.2 |

結論（實測）：
- **`Short Press` 與 `Long Press` 之行為定義，全文 2180 物件中無任何一個判適用者承載** ——
  A-ICS33 之核心（行為定義無母條）**經實測成立**。
- **`<Tpress>` 之「值」則有一個判適用之承載者：4819541**（§1.8.1，判**適用**）。
  此與 R-ICS23(a)／A-ICS33 字面之「`Long Press`（含 `<Tpress>`）於 ICS 側無母條」不符，
  詳 §5-1，具名回報，**不自行調和**。

#### ③ 受影響之 TC

判準：`test_procedure` 中存在**未定義按壓時長之裸按壓步驟**（掃法見 §0.3）。
實測 **10 個步驟，分佈於 9 條 TC**：

| req_id | tc_title | 裸按壓步驟（逐字） |
|---|---|---|
| SWE-ICS-006 | Power hardkey pressed while HU screen on | `2. Press the ICS "Power" button` |
| SWE-ICS-006 | Power hardkey pressed at Telematic Power full operation | `2. Press the ICS "Power" button` |
| SWE-ICS-006 | Power hardkey pressed while HU screen off | `3. Press the ICS "Power" button` |
| SWE-ICS-006 | Power hardkey pressed at Telematic Power idle | `2. Press the ICS "Power" button` |
| SWE-ICS-007 | Screen off hardkey starts the three second timer | `1. Press the ICS "Screen Off" button` |
| SWE-ICS-007 | Screen off hardkey pressed again within three seconds | `2. Press the ICS "Screen Off" button` |
| SWE-ICS-007 | Screen off hardkey pressed again within three seconds | `3. Press the ICS "Screen Off" button again 1 second after the first press` |
| SWE-ICS-007 | Three second period completed after screen off hardkey | `1. Press the ICS "Screen Off" button` |
| SWE-ICS-007 | Screen off hardkey pressed while HU screen off | `2. Press the ICS "Screen Off" button` |
| SWE-ICS-008 | Enter button pressed | `2. Press the ICS "Enter" button` |

**主受影響者**：`SWE-ICS-008` 之 `Enter button pressed`（b04 N1）——
其 `reasoning` 已具名 E6 並載明「只驗 `[pressed]` 訊號值之後果，不涉短按／長按之區別」
（R-ICS23(a) 採認）。**本檔不改 N1 之任何內容**（下放包明令）。

**不受影響者（具名）**：`SWE-ICS-010` 之 5 條。其按壓步驟皆載明時長
（`for more than 120 seconds`、`for exactly 120 seconds`、
`for more than PENDING: DR-ICS10 <Tstuck_button value>`），
時長由其自身之錨（DTCs Matrix r57 之 `Mature Time` / CFTS020-4819617）界定，
不依賴 `1.8.1.3` 之短長按定義。
`SWE-ICS-001`／`002`／`003`／`004` 為旋鈕面，無按壓步驟。

#### ④ 對應 DR

**DR-ICS6**（附問）。依 R-ICS23(a)：「登為覆蓋缺口 A-ICS33，並於 DR-ICS6 附問上游
是否有 ICS 側等價條文」。DR-ICS6 現行阻斷面為 `003, 004, 008, 009`，
其內容為「HMI Logic and Flow 之畫面流」；**按壓事件定義之附問尚未見於 DR-ICS6 之現行文字**
（實測 `DATA_REQUESTS.md` DR-ICS6 列，無 `Short Press`／`Long Press`／`Button Press Events` 字樣）。
本檔僅如實記錄，附問之落文屬分析層（`DATA_REQUESTS.md` 為本層禁區）。

---

### G2 — `A-ICS?`：`SWE-ICS-005`（ICSMuteButton）完全無 TC

#### ① 缺口描述
`SWE-ICS-005` 於 b01～b04 之 `req_id` 全集中**命中 0 次**（實測，指令 2）。
其 VC「Verify mute request generation when mute button is pressed.」全未涵蓋。
註：Mute 按鍵**確實出現於** `SWE-ICS-010` 之 5 條 TC（作為 stuck button 之操作對象），
但該 5 條之 `req_id` 為 `SWE-ICS-010`，驗的是 stuck 保護而非 mute request 之產生，
**不得計入 005 之覆蓋**。

#### ② 所缺母條之位置與其排除原因
母條**位置未定**，非「位置已知而被排除」：
- CFTS020 **無直載**（R-ICS15(c) 實測結論）；
- CFTS022 2.2.2 `{4914991}` 為候選但**適用性未驗**；
- SWRA 之 `Requirement Description` 為唯一候選原句，而該欄於 001/005/006/009/010
  呈 **+1 位移**（A-ICS1）—— 005 之 Description 實載 `$ICSPowerButton…`（實測 SWRA 行 12），
  與其 Title `ICS Buttons Management - ICSMuteButton` 不符。
排除原因為**來源不可信（位移未解）**，**不是 ECU／Radio／EE 之軸判定**。

#### ③ 受影響之 TC
0 條（該 RD 之 TC 數為 0）。台帳面之影響為 ASPICE 追溯鏈缺一列。

#### ④ 對應 DR
**DR-ICS1**（SWRA Description +1 位移，OPEN；催件排序列為上游急件，且註「005 恐繞不過」）。

---

### G3 — `A-ICS?`：`SWE-ICS-009`（Back_Button）完全無 TC

#### ① 缺口描述
`SWE-ICS-009` 於 b01～b04 之 `req_id` 全集中**命中 0 次**（實測）。
VC「Verify backward navigation handling after Back button press event.」全未涵蓋。

#### ② 所缺母條之位置與其排除原因
母條**位置已知**：CFTS020 `4819554`（Back_Button 之唯一直載原句）。
排除原因為 **`Market` 軸限 `NAFTA` 而本專案之市場軸未經量測**
（R-ICS15(b)：「未回前不得生成」；R-DD25 同族：不得以「有原句」充「在案」）。
**這是凍結，不是不適用** —— 與 G1 之實質不適用性質不同：
G1 已判定為不適用（不會再有 TC），G3 則待 DR 回覆後可能解凍。

#### ③ 受影響之 TC
0 條。連帶影響：`Menu Navigation` 這個 Test Set 現僅 1 條（N1），
其單薄之成因即 009 遭凍（R-ICS23(c) 已裁**不因此合併** Browse Control）。

#### ④ 對應 DR
**DR-ICS13**（市場軸為何；並確認 `Market` 屬性於本 DUT 之採認值域）。

---

### G4 — `A-ICS?`：`SWE1-ICS-011`（HU Screen ON）完全無 TC 且需求分頁缺列

#### ① 缺口描述
`SYS2 Traceability` 列 `SWE1-ICS-011` / `SYS-RA-ICS-011` /
`ICS Display State Management - HU Screen ON`（實測），
但 `SWE1 Requirements` 分頁**查無此 ID**（該分頁止於 010）。
故本 RD **既無 Requirement Description、亦無 Verification Criteria**，
且 b01～b04 之 `req_id` 全集中命中 0 次。

#### ② 所缺母條之位置與其排除原因
**排除原因為需求分頁缺列（資料缺件），不是軸判定、不是母文缺**。
CFTS020 側之 HU Screen ON／OFF 母條**存在且判適用**
（`1.8.1.1.1 {4819556}` 群、`1.8.1.1.3 {4819570}` 群，見 R-ICS15(a)），
現由 `SWE-ICS-006`／`007` 之 8 條 TC 承載；
但該 8 條之 `req_id` 為 006／007，**未追溯至 011**。
換言之：**行為面已有 TC，追溯面缺一條 RD** —— 二者不可互相抵充。

#### ③ 受影響之 TC
0 條掛在 011 名下；台帳面之 8 條（006 ×4、007 ×4）為行為上相鄰但追溯上無關者。

#### ④ 對應 DR
**DR-ICS2**（請補列或確認撤銷 011／012）。並與 **DR-ICS3**（SWRA／SYSAD 追溯鏈不對應）相關。

---

### G5 — `A-ICS?`：`SWE1-ICS-012`（Rear View Camera Transition）完全無 TC 且需求分頁缺列

#### ① 缺口描述
`SYS2 Traceability` 列 `SWE1-ICS-012` /
`ICS Display State Management - Rear View Camera Transition`（實測），
`SWE1 Requirements` 分頁**查無**。b01～b04 命中 0 次。
與 G4 之別：**012 之行為面亦全無 TC**（無任何相鄰承載者），為完全空白。

#### ② 所缺母條之位置與其排除原因
**排除原因為需求分頁缺列**。母文面另有一層不確定：
倒車顯影之母條未見於 CFTS020 之本 feature 適用範圍內；
`HeadUnitCameraSystems HMI Logic and Flow …` 一本已於 b04 作業 D 偵察並列出多頁 `rear view` 命中
（`04_source_recon_2.md`），但依 **R-ICS21(c)「偵察非納源」**，
該偵察**不得充 verbatim 來源、不得充錨**，故現階段仍屬母條未定。

#### ③ 受影響之 TC
0 條。

#### ④ 對應 DR
**DR-ICS2**（主）。母文面若於 011／012 補列後仍無來源，將另需納源之裁決（R-ICS21(c)），
**本檔不代擬**。

---

### G6 — `A-ICS?`：`SWE-ICS-004` 之 VC 三項操作僅涵蓋一項

#### ① 缺口描述
VC 逐字：`Verify browse, scroll and tune operations according to knob input value.`
明載 **browse／scroll／tune 三種操作**。
現有 2 條 TC（`Three detents counted in one rotation`、`Knob 2 signals acted on by the HU`）：
- 前者驗 detent 計數（送出面），未觸及三種操作之任一；
- 後者之 Pre-Condition 3 逐字為 `The HU shows a list screen on which browse behavior is defined`
  —— **限定於 browse**；其步驟 4 之期望行為為
  `PENDING: DR-ICS6 <HMI Logic and Flow browse, scroll and tune mapping for ICS_KNOB2>`。
故 **scroll 與 tune 二種操作無任何具名涵蓋**，browse 一種亦以佔位承載。

#### ② 所缺母條之位置與其排除原因
母條 `CFTS020-4819586` **判適用且已用為錨**（非排除）。
所缺者為其外指之**對照表**：條文本身只說「HU shall determine the corresponding
HMI screen to 'flow' to (Browse), if any, HMI screen to update (Scroll) or change in
Entertainment Audio state ('Tune')」，具體對照在 **HMI Logic and Flow**，
該文件**不在本 feature 之納源清單**（DR-ICS6 之現行縮圍描述即此）。
排除原因為**母文缺（外指文件未入庫）**，非軸判定、非不適用。

#### ③ 受影響之 TC
2 條（`SWE-ICS-004` 之全部）；其中 `Knob 2 signals acted on by the HU` 直接承載此缺口
（`has_pending` = true）。`05_pre_delivery_check.md` 另以強度面評此類 TC，本檔不重複其判。

#### ④ 對應 DR
**DR-ICS6**。

---

### G7 — `A-ICS?`：`SWE-ICS-008` 之 VC 導航流未具名涵蓋

#### ① 缺口描述
VC 逐字：`Verify HMI navigation flow after Enter button press event.`
現有 1 條（N1 `Enter button pressed`）之步驟 4 為
`Check that the HU flows to the screen defined for the current context
(target screen PENDING: DR-ICS6 <HMI Logic and Flow screen mapping for Enter_Button>)`，
ER 4 為 `The screen shown differs from the screen recorded in step 1`。
即：**只斷言「畫面有變」，未斷言「流向規定之那一個畫面」** ——
VC 所要求之 `navigation flow` 未被具名涵蓋。
（此為執行層依 IN §8.4.1「指名即造值」之正解，缺的是資料不是拿法。）

#### ② 所缺母條之位置與其排除原因
母條 `CFTS020-4819555` **判適用且已用為錨**（實測：ECU 軸缺、Radio 含 R1L／R1L-R、
EE 含 Atlantis High → v2(b) 適用）。
所缺者同 G6：外指之 **HMI Logic and Flow 畫面對照表**未入庫。
條文自身之 `if any` 明示「可能無對應畫面」，故連「是否必有目標畫面」都不能自證。
排除原因為**母文缺**，非軸判定。

#### ③ 受影響之 TC
1 條（N1）。**本檔不改 N1**。

#### ④ 對應 DR
**DR-ICS6**。

---

## §3 RD 覆蓋矩陣

`SWE-ICS-001`～`012`（含 011／012）。
「RD 於需求分頁」欄之 `是`／`缺列` 為實測（§0.4 之母數）。
形制註：需求分頁之鍵為 `SWE-ICS-nnn`，Traceability 之鍵為 `SWE1-ICS-nnn`，
本表以尾三碼對齊，**未逕自視為同一字面**。

| RD | Title（逐字） | RD 於需求分頁 | 於 Traceability | 現有 TC 數 | Test Set | 成因（無 TC 者）／備註 | 對應 DR |
|---|---|---|---|---|---|---|---|
| 001 | ICS Buttons Management - ICS_KNOB1_DIR | 是 | 是 | **2** | Volume Control | — | （DR-ICS1 涉其 Description，但已由 CFTS020 繞過）|
| 002 | ICS Buttons Management - ICS_KNOB1_VAL | 是 | 是 | **1** | Volume Control | 有 TC；帶 DR-ICS4／DR-ICS12 佔位 | DR-ICS4, DR-ICS12 |
| 003 | ICS Buttons Management - ICS_KNOB2_DIR | 是 | 是 | **4** | Browse Control | 有 TC；B1／B2 帶 DR-ICS12 佔位 | DR-ICS12 |
| 004 | ICS Buttons Management - ICS_KNOB2_VAL | 是 | 是 | **2** | Browse Control | 有 TC；**VC 三項僅涵蓋 browse**（G6） | DR-ICS6, DR-ICS12 |
| 005 | ICS Buttons Management - ICSMuteButton | 是 | 是 | **0** | —（未成立） | **來源不可信**：SWRA Description +1 位移未解；CFTS020 無直載；CFTS022 2.2.2 候選未驗（**凍結**，G2） | **DR-ICS1** |
| 006 | ICS Buttons Management - ICSPowerButton | 是 | 是 | **4** | Display Control | 有 TC；全數帶 DR-ICS8／DR-ICS16 面之訊號佔位 | DR-ICS8, DR-ICS16 |
| 007 | ICS Buttons Management - ICSScreenOffButton | 是 | 是 | **4** | Display Control | 有 TC；同上 | DR-ICS8, DR-ICS16 |
| 008 | ICS Buttons Management - Enter_Button | 是 | 是 | **1** | Menu Navigation | 有 TC；**VC 之目標畫面未具名**（G7）；並受 A-ICS33 影響（G1） | DR-ICS6 |
| 009 | ICS Buttons Management - Back_Button | 是 | 是 | **0** | —（未成立） | **凍結**：唯一直載原句 4819554 之 `Market` 限 NAFTA，市場軸未定（G3） | **DR-ICS13** |
| 010 | ICS Buttons Management - Stuck Button Protection | 是 | 是 | **5** | Stuck Button | 有 TC；2 條帶 DR-ICS10 佔位 | DR-ICS10, DR-ICS11 |
| 011 | ICS Display State Management - HU Screen ON | **缺列** | 是 | **0** | —（未成立） | **需求分頁缺列**（無 Description、無 VC）；母條存在且已由 006／007 承載，但追溯面未掛 011（G4） | **DR-ICS2**（並涉 DR-ICS3） |
| 012 | ICS Display State Management - Rear View Camera Transition | **缺列** | 是 | **0** | —（未成立） | **需求分頁缺列**；且母文面亦未定（`HeadUnitCameraSystems` 一本僅偵察，依 R-ICS21(c) 非納源）（G5） | **DR-ICS2** |

**小計（實測）**：

| 項 | 數 |
|---|---|
| RD 全集（以 Traceability 為準） | **12** |
| **有 TC 者** | **8**（001, 002, 003, 004, 006, 007, 008, 010） |
| **無 TC 者** | **4**（005, 009, 011, 012） |
| TC 總數 | **23** |
| 成因：來源不可信／位移凍結 | 1（005） |
| 成因：市場軸未定凍結 | 1（009） |
| 成因：需求分頁缺列 | 2（011, 012） |
| 成因：**不適用** | **0** —— 無任何 RD 之無 TC 成因為「實質不適用」 |

---

## §4 SWRA `Verification Criteria` 對照

VC 原文逐字取自 `SWE1 Requirements` 之 Q 欄（實測）。
「涵蓋判」之判準：VC 所列之**每個驗證點**是否有具名之 TC 步驟與 ER 對應；
以 `PENDING: DR-…` 佔位承載者記為 **部分涵蓋**（佔位不是涵蓋）。

| RD | Verification Criteria（逐字） | 現有 TC | 涵蓋判 | 未涵蓋之驗證點（具名） |
|---|---|---|---|---|
| 001 | `Verify correct knob direction detection during clockwise and counter-clockwise rotation.` | 2（`VOLUME knob rotated clock-wise`／`counter clock-wise`） | **涵蓋** | — （二方向各一條；觀察面為 `VOLUME POP_UP` 之音量階增減，屬 direction 之後果，非 DIR 訊號本身 —— 記為涵蓋，另註見下方 4-1） |
| 002 | `Verify volume adjustment information updates according to knob value input.` | 1（`Three detents rotated clock-wise`） | **部分涵蓋** | 最大音量階數為 `PENDING: DR-ICS4 <CFTS019 volume level range>`、detent 時窗為 `PENDING: DR-ICS12` —— 二佔位皆在 Pre-Condition，未定值前該條無法執行 |
| 003 | `Verify browse direction handling during knob rotation.` | 4（B1～B4） | **涵蓋** | — （CW／CCW／靜止／週期重送四態齊備） |
| 004 | `Verify browse, scroll and tune operations according to knob input value.` | 2（B5／B6） | **部分涵蓋** | **`scroll` 操作**、**`tune` 操作**二者無任何具名 TC（B6 之 Pre-Condition 限定 `list screen on which browse behavior is defined`）；`browse` 亦僅以 `PENDING: DR-ICS6` 承載 → **缺口 G6** |
| 005 | `Verify mute request generation when mute button is pressed.` | **0** | **未涵蓋** | **全部** —— `mute request generation` 無任何 TC → **缺口 G2** |
| 006 | `Verify display ON/OFF transition upon power button press event.` | 4 | **涵蓋** | — （ON→OFF 二條、OFF→ON 二條，四態齊備）；訊號面為佔位但主錨為 HMI 現象（R-ICS22(b)），不因此判未涵蓋 |
| 007 | `Verify Screen ON/OFF transition and timeout behavior using Screen OFF button.` | 4 | **涵蓋** | — （`timeout behavior` 由 `Screen off hardkey starts the three second timer` 與 `Three second period completed after screen off hardkey` 二條承載） |
| 008 | `Verify HMI navigation flow after Enter button press event.` | 1（N1） | **部分涵蓋** | **`navigation flow` 之目標畫面**：現僅斷言「畫面有變」，目標為 `PENDING: DR-ICS6` → **缺口 G7**；另按壓事件之時長面無母條 → **缺口 G1** |
| 009 | `Verify backward navigation handling after Back button press event.` | **0** | **未涵蓋** | **全部** → **缺口 G3** |
| 010 | `Verify actions are ignored after configured stuck button timeout condition.` | 5 | **部分涵蓋** | `configured … timeout` 之值為 `PENDING: DR-ICS10 <Tstuck_button value>`（`Press ignored during stuck condition` 步驟 3、`Button responsive after release` 步驟 1）；**驗證點本身（actions are ignored）已具名涵蓋**，缺的是門檻值 |
| 011 | **需求分頁缺列 —— 無 VC 可對照** | 0 | **無從判** | 掃法：`SWE1 Requirements` A 欄以 `^SWE-ICS-\d{3}$` 完全比對，011 **查無** → **缺口 G4** |
| 012 | **需求分頁缺列 —— 無 VC 可對照** | 0 | **無從判** | 同上，012 **查無** → **缺口 G5** |

**結論**：「RD 有 TC 但 VC 未被涵蓋」之情形**存在，共 2 條具名**：
**`SWE-ICS-004`（scroll／tune 二操作，G6）** 與 **`SWE-ICS-008`（navigation flow 之目標畫面，G7）**。
另有 `002` 與 `010` 屬「驗證點已具名涵蓋、但所需數值為 DR 佔位」，
性質與 004／008 不同（缺值 vs 缺驗證點），故未列入缺口總表。

### 4-1 觀察面之註（不列為缺口，僅具名）

`SWE-ICS-001` 之二條以 `VOLUME POP_UP` 之音量階增減承載「方向偵測」，
而非直接讀 `$ICS_KNOB1_DIR$` 訊號。VC 之字面為 `direction detection`，
其可觀察面依 R-DD3 同族之「SWQT 觀察面為 HMI 現象」判為適格，故記涵蓋。
惟其與 `SWE-ICS-003`（同為 direction，卻讀 `Radio_Knob2_DIR` 訊號）之觀察面不一致，
此不一致為既存事實，**本檔不自行調和**。

### 4-2 `Verification Method` 欄之對照（VC 以外之附帶實測）

| RD | Verification Method（逐字） | 現有 TC 之 `design_method` | 註 |
|---|---|---|---|
| 001 | `Functional Test` | Functional Based ×2 | 相符 |
| 002 | `Functional Test` | Functional Based ×1 | 相符 |
| 003 | `Functional Test` | Functional Based ×4 | 相符 |
| 004 | `Functional Test` | Functional Based ×2 | 相符 |
| 005 | `Functional Test` | —（0 條） | — |
| 006 | `Functional Test, Integration Test` | State Transition ×4 | **無 `Integration Test` 對應者**；`design_method` 與 `Verification Method` 為不同欄位形制，是否須對應**未見裁決** |
| 007 | `Functional Test` | State Transition ×3、Functional Based ×1 | 同上，形制差異 |
| 008 | `Functional Test` | Functional Based ×1 | 相符 |
| 009 | `Functional Test` | —（0 條） | — |
| 010 | `Functional Test, Robustness Test` | Fault Injection ×4、Boundary Value Analysis ×1 | Robustness 面由 Fault Injection 承載，形制不同名 |

`design_method`（IN 之設計方法）與 SWRA 之 `Verification Method` **是否須逐條對應，
現行台帳無條文**。故本檔**不判其為缺口**，僅具名以待裁。

---

## §5 實測與現行台帳字面之不符（非覆蓋缺口，具名回報）

依紀律「不自行調和不符」，以下二件如實記錄，寫 `A-ICS?`，不代擬條文、不自取號。

### 5-1 `A-ICS?`：`4819541` 判**適用**且逐字載 `<Tpress> = 500 msec` 等六個時間變數值

實測（指令 3）：

```
4819541  §1.8.1  Subsystem Functional Requirement  適用
    ECU=None
    Radio=['R1H', 'VP384', 'R1L', 'R1L-R', 'R1M', 'VP4R84', 'VP484']
    EE=['Atlantis Mid', 'PowerNet', 'Atlantis High']
    強度=正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN）
```

其本文逐字：

> For this section, the following time variables shall be used:<Tsend> = 150 msec<Tbutton> = 100 msec<TPeriodToCountKnobDetents> = initial value 50 msec. This is a parameter that is to be optimized by a 'parameter tuning process' when integration testing is performed.<Tpower> = 1.5 sec<Tstuck_button> = 120 sec<Tpress> = 500 msec.<TPeriodToSendNoChange> = 20 msec.

三點不符／相關，**皆不自行調和**：

1. **與 R-ICS23(a)／A-ICS33 之字面不符**：二者均書
   「`Short Press`／`Long Press`（含 `<Tpress>`）於 ICS 側無母條」。
   實測：`Short Press`／`Long Press` 之**行為定義**確無適用母條（§2 G1 ②-補 已證），
   但 **`<Tpress>` 之「值」有適用之承載者（4819541）**。
   即「含 `<Tpress>`」這一括號與實測不符；A-ICS33 之核心不受影響。
2. **疑涉 DR-ICS10**：其所問之 `<Tstuck_button>` 具體值，4819541 逐字載 `120 sec`。
   （DR-ICS10 之設問前提為「CFTS020-4819617 之 `<Tstuck_button>` 值未見」。）
3. **疑涉 DR-ICS12**：其所問之 `<TPeriodToCountKnobDetents>` 與 `<TPeriodToSendNoChange>`，
   4819541 逐字載 `initial value 50 msec`（並註明待整合測試之 parameter tuning）
   與 `20 msec`。

全 repo grep `4819541` 之結果：**僅 1 處命中**，
即 `docs/reports/03_cfts020_recon_v2.md:173` 之 v1→v2 差異表列，
**未於任何 handoff／upstream／RULINGS／DATA_REQUESTS 被討論過**。

**本檔不裁**：是否以 4819541 結 DR-ICS10／DR-ICS12、其值可否入 TC、
`initial value` 與 `parameter tuning` 之保留字如何處置，**皆屬分析層**。
執行層僅具名此物件與其逐字內容。

### 5-2 `A-ICS?`：「`1.8.1.3` 之 24 物件中 **23 為 `[ECU:FPDM]`**」與實測不符

R-ICS23(a) 逐字：「`1.8.1.3 Button Press Events` 之 24 物件中 23 為 `[ECU:FPDM]`」；
`docs/upstream/04_profile_signals_and_navigation.md` §4-4 逐字：
「本包逐一查其成因：**皆為 `[ECU:FPDM]`**」。

實測（§2 G1 ② 之三分表）：23 個不適用者中 —

- ECU 含 `FPDM`：**16**
- ECU 僅 `CCDMF`（不含 FPDM）：**2**（4819602、4819606）
- ECU **軸缺**，因 `Radio`／`EE` 落空而不適用：**5**（4819594、4819596、4819600、4819607、4819613）

**判定結果（23 不適用）相符；成因分類不符。**
其中 5 個軸缺者之排除**不是** v2(b)(ii) 之 ECU 判定，而是 Radio／EE 落空 ——
與「皆為實質不適用之 ECU 判定」之敘述不同。
惟此 5 個之本文皆為 `PowerNet` 支線之對應物件（如 4819594／4819596 為 4819595／4819597 之
PowerNet 版），其不適用之結論不因分類改變而動搖，故 **A-ICS33 之成立不受影響**。

**本檔不改 RULINGS.md、不改 ANOMALIES.md**（本層禁區）。

---

## §6 本檔之寫入範圍與未動之檔

**已寫**（僅此二檔）：
- `features/ics_management/docs/reports/05_coverage_gaps.md`（本檔，新建）
- `features/ics_management/scripts/gap_probe_05.py`（新建，唯讀腳本）

**未動**（逐項確認）：
`RULINGS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md`、`framework.md`、`ANALYSIS_LOCK.md`、
`docs/handoff/**`、repo 根之 `scripts/`／`docs/runtime/`／`docs/fw036/`、
`generated/**` 之任何 TC JSON（**含 N1**）、`features/ics_management/scripts/` 之任何既有檔、
`inputs/` 與 `spec-index/sources/` 之任何素材。
