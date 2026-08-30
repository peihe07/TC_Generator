# 13 — SYS2 反向掃描（下放包 13 作業 B）

**性質**：只量不裁。本報告**不作任何「應否納入驗證範圍」之判斷**（範圍屬分析層）。
**DUT**：Radio `R1L`／EE `Atlantis High`／ECU `LTM`／變體 `Disassociated`（R-ICS37(a) 過渡採認；`Disassociated` 即 'Silver Box'，外接 DCSD，見 RULINGS.md:1071／1142）。

## 0. 量測基礎（可複現）

| 項 | 值 |
|---|---|
| 檔 | `features/ics_management/inputs/SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx` |
| 讀法 | `openpyxl.load_workbook(..., data_only=True, read_only=True)` |
| 分頁 | `Basic Report`（另有 `Polarion`／`_polarion` 二分頁，為工具用） |
| 表頭列 | 第 1 列 |
| 資料列 | xlsx 第 2～334 列，**333 列**（與下放包 12 之 333 相符） |
| 來源欄 | `SYS2 來源需求項目ID  Source Requirement items` |
| 正規化 | NBSP(U+00A0)→space、所有 `Zs` 類→space、collapse 連續空白、strip；**呈現時引原文** |
| 腳本 | `features/ics_management/scripts/sys2_reverse_scan_13.py`（本包新建） |

以上讀法（檔／sheet／表頭列／欄名）**逐項沿用** `scripts/sys2_87_probe_12.py`，以確保與前十二包可比。

**數字紀律**：本報告所有數字皆自列舉長度取得（`len()`／`Counter`），無一手估。

---

## §1 來源欄空白之 Functional Requirement 列 —— 逐一

### §1-0 先確認「23」

以本次獨立量測重數：

- 來源欄（正規化後）為空字串之列：**31**
- 其中 `Category` 正規化後小寫等於 `functional requirement` 者：**23**

**23 確認成立**，與上繳包 12 §3-5 之數一致。無差異可具名。

補充（下放包未問，但必要）：31 − 23 = **8 列**同樣來源欄空白，但 `Category` 非 FR：
`Heading` 2／`Information` 3／`Out of scope` 3。詳 §4-2。

**結構事實**：這 31 列在 xlsx 中之列號為 **58～88 連續無斷**（`[58,59,…,88]`）。
即：來源欄空白者並非散落全表，而是**單一連續區塊**。詳 §4-1。

### §1-1 判定表（四欄）

欄義：
- **層**：HW 供應商介面／HMI 軟體側行為／不可判
- **介面位置**：HU↔DCSD 之間／DCSD 內部／不可判
- **HMI 軟體側可驗證**：是／否／不可判

| # | xlsx 列 | ID | Document ID | Category | 子分類 | SW/HW/System | 層 | 介面位置 | HMI 軟體側可驗證 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 58 | NRL-163104 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | DCSD 內部 | 否 |
| 2 | 59 | NRL-163105 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | DCSD 內部 | 否 |
| 3 | 60 | NRL-163106 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | DCSD 內部 | 否 |
| 4 | 61 | NRL-163107 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | DCSD 內部 | 否 |
| 5 | 65 | NRL-180511 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 6 | 66 | NRL-180512 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | HU↔DCSD | **不可判** |
| 7 | 67 | NRL-180513 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 8 | 68 | NRL-180514 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | DCSD 內部 | 否 |
| 9 | 69 | NRL-180515 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 10 | 71 | NRL-180517 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 11 | 73 | NRL-180519 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 12 | 74 | NRL-180520 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 13 | 76 | NRL-180522 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `System` | **不可判** | **不可判** | **是** |
| 14 | 77 | NRL-180523 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 15 | 78 | NRL-180524 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 16 | 79 | NRL-180525 | `SR26_20250813-1632` | `Functional Requirement` | `ICS / DCSD (CFTS020)` | `System` | HW 供應商介面 | HU↔DCSD | 否 |
| 17 | 80 | NRL-180526 | **（空）** | `Functional Requirement` | **（空）** | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 18 | 82 | NRL-180528 | **（空）** | `Functional Requirement` | **（空）** | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 19 | 83 | NRL-180529 | **（空）** | `Functional Requirement` | **（空）** | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 20 | 84 | NRL-180530 | **（空）** | `Functional Requirement` | **（空）** | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 21 | 86 | NRL-180532 | **（空）** | `Functional Requirement` | **（空）** | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 22 | 87 | NRL-180533 | **（空）** | `Functional Requirement` | **（空）** | `HW` | HW 供應商介面 | HU↔DCSD | 否 |
| 23 | 88 | NRL-180534 | **（空）** | `Functional Requirement` | **（空）** | `HW` | HW 供應商介面 | HU↔DCSD | 否 |

**分佈（自列舉長度）**：

- 層：HW 供應商介面 **22**／HMI 軟體側行為 **0**／不可判 **1**（#13）
- 介面位置：HU↔DCSD **17**／DCSD 內部 **5**（#1–#4、#8）／不可判 **1**（#13）
- HMI 軟體側可驗證：是 **1**（#13）／否 **21**／不可判 **1**（#6）

**本 DUT 之關係（事實陳述，非範圍判斷）**：DUT 變體為 `Disassociated`（外接 DCSD），
故「HU↔DCSD 之間」之介面在本 DUT 上**物理存在**（17 列）；「DCSD 內部」之 5 列
描述之為顯示模組本體／面板規格（`System-HW` 欄逐字寫 `HW supplier shall support…`）。
本報告到此為止，不推導其驗證歸屬。

### §1-2 逐列逐字引（`SYS2 MD Feedback` 及必要之 `Description`）

引文一律取儲存格原文。xlsx 內之 `_x000D_` 為 openpyxl 對原始 CR 之逸出表示，原樣保留；
`\n` 為實際換行，以真實換行呈現。

---

**#1 NRL-163104**（列 58）
`Description`：
```
Display Specification for 8.4
```
`SYS2 MD Feedback`：**（空儲存格，`None`）—— 查無**
判：層＝HW 供應商介面（面板尺寸／解析度／DCSD type code）；介面位置＝DCSD 內部；HMI 軟體側可驗證＝否。

---

**#2 NRL-163105**（列 59）
`Description`：
```
Display Specification for 10.1L
```
`SYS2 MD Feedback`：**（空儲存格）—— 查無**
判：同 #1。

---

**#3 NRL-163106**（列 60）
`Description`：
```
Display Specification for 10.1P
```
`SYS2 MD Feedback`：**（空儲存格）—— 查無**
判：同 #1。

---

**#4 NRL-163107**（列 61）
`Description`：
```
Display Specification for 10.25
```
`SYS2 MD Feedback`：**（空儲存格）—— 查無**
判：同 #1。

---

**#5 NRL-180511**（列 65）
`Description`：
```
Radio Must wait 1200ms after IGN Off->ON before 1st Backchannel communication._x000D_
Radio reads DCSD Version data after 1200ms.
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：層＝HW 供應商介面（LVDS Backchannel 起始時序）；介面位置＝HU↔DCSD；
HMI 軟體側可驗證＝否（標的為 Version data 之 backchannel 讀取，無 HMI 表面）。

---

**#6 NRL-180512**（列 66）
`Description`：
```
Radio can only read Touch data after 1800ms from IGN ON 
```
（註：原文結尾有一個尾隨空白，原樣保留。）
`SYS2 MD Feedback`：
```
04/13: Requesting the HW supplier to review the system requirement.
```
判：層＝HW 供應商介面；介面位置＝HU↔DCSD；
HMI 軟體側可驗證＝**不可判**。理由具名：條文之受詞為 Radio 之 touch data 讀取時機
（I2C／backchannel 層），非 HMI 之行為；然其後果（IGN ON 後 1800ms 內觸控不生效）
在 HMI 上為可觀察。條文本身未言明觀察面，故不可判。**不作調和。**
另註：本列之 `SYS2 MD Feedback` 逐字為「Requesting the HW supplier to review」，
即 SYS2 自身標示此列**尚在 HW 供應商覆核中**，非已接受（與其餘 18 列之
「HW supplier have accepted」不同）。

---

**#7 NRL-180513**（列 67）
`Description`：
```
DCSD is the Slave (Device)._x000D_
SOC I2C address: 0x12 (Write:0x24 / Read:0x25)
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：層＝HW 供應商介面（I2C 位址）；介面位置＝HU↔DCSD；HMI 軟體側可驗證＝否。

---

**#8 NRL-180514**（列 68）
`Description`：
```
The following display models support Touch Capability: 5-Point Multitouch, 11-Bit Resolution_x000D_
_x000D_
DCSD8.4_Landscape5MT (0x03)_x000D_
DCSD10.1_Landscape5MT (0x04)_x000D_
DCSD10.1_Portrait5MT (0x0C)_x000D_
DCSD10.25Landscape5MT (0x0A)_x000D_
Refer to "1.2 Display Type Table" section of  DCSD_and_HU_LVDS_Backchannel_Protocol_v4.1.pdf_x000D_
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：層＝HW 供應商介面（顯示模組觸控能力與 type code）；介面位置＝DCSD 內部；
HMI 軟體側可驗證＝否。
**外部參照具名**：本列指名 `DCSD_and_HU_LVDS_Backchannel_Protocol_v4.1.pdf`。
該檔**不在** `spec-index/sources/`（查無；`ls` 已確認，見 §2-3）。

---

**#9 NRL-180515**（列 69）
`Description`：
```
The radio may implement retries for message request with 100ms interval for Version Data and _x000D_
17ms interval for touch data.
```
`SYS2 MD Feedback`（原文首字元為換行，原樣保留）：
```

04/13: HW supplier have accepted the requirement
Number if retries 3 OK as suggested by Harman,
```
判：層＝HW 供應商介面（重試間隔）；介面位置＝HU↔DCSD；HMI 軟體側可驗證＝否。
另註：`Description` 用語為 `may implement`（非 shall），且 `Category` 仍為 `Functional Requirement`。

---

**#10 NRL-180517**（列 71）
`Description`：
```
Supported DCSD Touch Backchannel Configuration (I2C-based):_x000D_
Case 2: Radio operates as I2C Master and DCSD operates as I2C Slave._x000D_
_x000D_
The following display models support Case 2 ONLY:_x000D_
DCSD8.4_Landscape5MT (0x03)_x000D_
DCSD10.1_Landscape5MT (0x04)_x000D_
DCSD10.1_Portrait5MT (0x0C)_x000D_
DCSD10.25Landscape5MT (0x0A)_x000D_
Refer to "1.2 Display Type Table" section of  DCSD_and_HU_LVDS_Backchannel_Protocol_v4.1.pdf
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：層＝HW 供應商介面（I2C 主從組態）；介面位置＝HU↔DCSD；HMI 軟體側可驗證＝否。

---

**#11 NRL-180519**（列 73）
`Description`：
```
The GPIO-0 signal is normally high and goes low with the interrupt generation from the DCSD to the Radio.
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：層＝HW 供應商介面（GPIO 電氣位準／中斷）；介面位置＝HU↔DCSD；HMI 軟體側可驗證＝否。

---

**#12 NRL-180520**（列 74）
`Description`：
```
The DCSD will reset the GPOI-0 to high after the Radio master request for the touch data or a 100ms of no response from the radio from a previous touch interrupt.
```
（原文拼作 `GPOI-0`，原樣保留。）
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：層＝HW 供應商介面；介面位置＝HU↔DCSD；HMI 軟體側可驗證＝否。

---

**#13 NRL-180522**（列 76）—— **本節唯一之「是」**
`Description`：
```
Do not filter out duplicate touch (same coordinates) events during continuous press specifically during dragging/swipe.  Needed for Apple CarPlay™ Certfication
```
（原文 `Certfication` 拼字如此、`press.` 後為二個空白，原樣保留。）
`SYS2 MD Feedback`：**（空儲存格，`None`）—— 查無**
判：
- 層＝**不可判**。理由具名：`SW/HW/System` 欄逐字為 `System`（非 `HW`，與其餘 21 列不同）；
  條文以否定祈使句「Do not filter out」書寫，**未具名執行主體**（可能為 DCSD 韌體、
  HU 觸控驅動、或 HMI 輸入堆疊），故層別不可自條文斷定。
- 介面位置＝**不可判**（同上，主體未具名，無從斷定在 HU↔DCSD 之間抑或 DCSD 內部）。
- HMI 軟體側可驗證＝**是**。理由具名：所述行為（連續按壓／拖曳／滑動期間，
  相同座標之重複觸控事件不得被過濾）之**成立與否可於 HMI 軟體側以 drag/swipe
  操作直接觀察**；且條文自身指名之目的為 `Apple CarPlay™ Certfication`，
  該認證之受測面為 HMI／投射應用層。

**本列即 §3 之 E19 觸發列。**

---

**#14 NRL-180523**（列 77）
`Description`：
```
Tx Cycle rate :  _x000D_
 Minimum Tx cycle is fixed to 15ms _x000D_
_x000D_
Maximum Response cycle 16.6ms (60hz)  including radio latency
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：層＝HW 供應商介面（傳輸週期）；介面位置＝HU↔DCSD；HMI 軟體側可驗證＝否。

---

**#15 NRL-180524**（列 78）
`Description`：
```
Message and timing definitions for touch
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
[20-Jan] Rework done. Removed Capacitative button reqs.
```
判：層＝HW 供應商介面（訊息與時序定義）；介面位置＝HU↔DCSD；HMI 軟體側可驗證＝否。
另註：本列之 SYS2 `Verifiability (Y/N/NA)` 欄逐字為 `NA`（見 §4-3）。

---

**#16 NRL-180525**（列 79）
`Description`：
```
3.2.2 “INT Type” Message (Message ID: 0x10) 
```
（原文用彎引號 `“ ”`，且結尾有尾隨空白，原樣保留。）
`SYS2 MD Feedback`：
```
[20-Jan] Rework done. Removed Capacitative button reqs.
```
判：層＝HW 供應商介面（backchannel 訊息 ID）；介面位置＝HU↔DCSD；HMI 軟體側可驗證＝否。
另註：`SW/HW/System` 為 `System`、`Verifiability` 為 `NA`；`Description` 實為一節標題文字，
但 `Category` 為 `Functional Requirement`（非 `Heading`）。

---

**#17 NRL-180526**（列 80）
`Document ID`：**（空儲存格）—— 查無**；`子分類`：**（空儲存格）—— 查無**
`Description`：
```
Typically the radio will respond within 1-2ms of the interrupt being set._x000D_
_x000D_
If HU has not responded to the interrupt before the next touch sample (15ms) _x000D_
then the interrupt shall stay set, the old point should be discarded and _x000D_
a new point should be loaded. If HU then responds to interrupt, the new data point only is sent.
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：層＝HW 供應商介面（中斷回應時序）；介面位置＝HU↔DCSD；HMI 軟體側可驗證＝否
（「舊點丟棄」發生於 DCSD 之緩衝，HMI 側不可觀察其丟棄事實）。

---

**#18 NRL-180528**（列 82）
`Document ID`／`子分類`：**（皆空）—— 查無**
`Description`：
```
For signle touch scenario,_x000D_
During touch press event, only touch1 point will have valid coordinates as below: _x000D_
touch #1(x, y), _x000D_
touch #2(0,0), _x000D_
touch #3(0,0), _x000D_
touch #4(0,0), _x000D_
touch #5(0,0)_x000D_
touch #1 press bit = 1; touch 2,3,4,5 press bit = 0_x000D_
_x000D_
when touch released, DCSD transmit touch coordinates of (0,0) with press bit = 0.  _x000D_
No touch events reported while all pressed coordinates =0
```
（原文 `signle` 拼字如此，原樣保留。）
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：層＝HW 供應商介面（backchannel 觸控封包欄位語意）；介面位置＝HU↔DCSD；
HMI 軟體側可驗證＝否（座標與 press bit 為封包內容，HMI 側僅見經 HU 驅動轉譯後之事件）。

---

**#19 NRL-180529**（列 83）
`Document ID`／`子分類`：**（皆空）—— 查無**
`Description`：
```
During multi touch drag, All 5 touch points are sent on every message
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：同 #18。

---

**#20 NRL-180530**（列 84）
`Document ID`／`子分類`：**（皆空）—— 查無**
`Description`：
```
For Multi touch drag scenario,_x000D_
when touches released, DCSD transmit touch coordinates of (0,0) with press bit = 0.  _x000D_
No touch events reported while all pressed coordinates =0
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：同 #18。

---

**#21 NRL-180532**（列 86）
`Document ID`／`子分類`：**（皆空）—— 查無**
`Description`：
```
During multi touch, Continously report data touch at display frame rate of  16.6ms while any touch pressed exist even if duplicate touch coordinates
```
（原文 `Continously` 拼字如此，原樣保留。）
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：層＝HW 供應商介面；介面位置＝HU↔DCSD；HMI 軟體側可驗證＝否。
**具名關聯**：本列與 #13（NRL-180522）為同一主題之兩面 —— #21 規定 **DCSD 端「必須送出」**
重複座標，#13 規定 **「不得過濾掉」** 重複座標。#21 主體具名為 DCSD，#13 主體未具名。
本報告僅陳述此對應，不推導其歸屬。

---

**#22 NRL-180533**（列 87）
`Document ID`／`子分類`：**（皆空）—— 查無**
`Description`：
```
During multi touch, when touch#1 released, DCSD transmit immediately remaining  touch point(s). 
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：同 #18。

---

**#23 NRL-180534**（列 88）
`Document ID`／`子分類`：**（皆空）—— 查無**
`Description`：
```
During multi touch, when touch#2 released, DCSD transmit touch #1 and touch #2 coordinates of (0,0) with press bit = 0 . _x000D_
No touch events reported while all pressed coordinates =0
```
`SYS2 MD Feedback`：
```
04/13: HW supplier have accepted the requirement
```
判：同 #18。

---

## §2 擴掃 —— 掃描起點盲區之完整盤點

### §2-1 首要更正：下放包之前提與實測不符（不調和）

下放包 §2 令「來源欄**非空但不指向 CFTS020／CFTS022** 之列，逐列列出其**來源文件為何**
（CFTS019？HMI L&F？SYSAD？其他？）」。

**實測**：SYS2 `Basic Report` 之來源欄 `SYS2 來源需求項目ID  Source Requirement items`
**從不含任何文件名稱字串**。302 個非空儲存格全部只含 7 位數字（部分為字串型、
部分為數值型，例如列 13 之儲存格值為整數 `4819353` 而非字串 `'4819353'`）。

- 全表含字串 `CFTS020`／`CFTS022`（大小寫、底線、空白正規化後）於來源欄之列數：**0**
- 來源欄含 `CFTS019`／`HMI L&F`／`SYSAD` 或任何文件名之列數：**0 —— 查無**

故「來源文件為何」一問**在此欄上無法回答**，因該欄不承載文件名。
本報告改以**唯一可行之等價量測**回答：將來源欄之 7 位 ID 解析回 CFTS020／CFTS022 之物件集合。
**此為量測方法之替代，非對下放包之調和；差異已具名於此。**

### §2-2 來源桶總盤點（互斥，逐列一桶）

**桶 A —— 依來源欄之文法形態**

| 桶 | 列數 |
|---|---|
| 純 7 位 ID（無文件名） | **302** |
| 空白 | **31** |
| 含 `CFTS020` 文件名 | **0** |
| 含 `CFTS022` 文件名 | **0** |
| 其他（非空、非 ID、非文件名） | **0** |
| **合計** | **333** |

**桶 B —— 將 7 位 ID 解析回文件（CFTS020 物件 2180 個、CFTS022 物件 336 個，
以 `^(\d{7}): \[` 物件頭解析 `word/document.xml`）**

| 桶 | 列數 | Category 分佈 |
|---|---|---|
| 全數落在 CFTS020 之 2180 物件內 | **260** | `Out of Scope` 116／`Information` 81／`Functional Requirement` 56／`Out of scope` 4／`Heading` 2／`Functional requirement` 1 |
| 全數落在 CFTS022 之 336 物件內 | **0** | — |
| 全數落在兩者之物件集合之外 | **42** | `Heading` 41／`Information` 1 |
| CFTS020／CFTS022 混合 | **0** | — |
| 空白 | **31** | `Functional Requirement` 23／`Information` 3／`Out of scope` 3／`Heading` 2 |
| **合計** | **333** | |

**桶 C —— 那 42 列究係何來源？（已查實，非推測）**

42 列之 7 位 ID **全部可在 CFTS020 docx 之 `word/document.xml` 內文中找到**
（實測：8 個抽樣 ID `4819125`／`4819126`／`4819128`／`4819352`／`4819620`／
`4819538`／`4819920`／`4821060` 之 `in_alltokens` 皆為 `True`），但**皆非物件頭**
（`in_heads` 皆為 `False`）。CFTS020 docx 全文出現之相異 7 位 token 為 **2645** 種，
其中物件頭僅 **2180** 種，差 **465** 種。

**結論（確定）**：這 42 列**並非另一份來源文件**，而是 CFTS020 內之**節標題／章節錨**，
其 ID 不被 `cfts020_probe.py` 之物件頭正則 `^(\d{7}): \[` 收錄。
其 `Description` 逐一即為 CFTS020 之節標題文字，例如：
`'ICS and DCSD [CFTSMV020_CIP_R3]'`、`'Revision Notes'`、`'Introduction'`、
`'DCSD and HU HMI Communication'`、`'Screen Touch Event Interrupts for DCSD'`、
`'Capacitive Multi-touch Screen Gesture support '` 等。

42 列逐列（`ID` ／來源 ID ／`Category` ／`Document ID` ／`Description`）：

| # | ID | 來源 ID | Category | Document ID | Description |
|---|---|---|---|---|---|
| 1 | NRL-52839 | 4819125 | Heading | SR26_20250813-1632 | `ICS and DCSD [CFTSMV020_CIP_R3]` |
| 2 | NRL-52840 | 4819126 | Heading | SR26_20250813-1632 | `Revision Notes` |
| 3 | NRL-52842 | 4819128 | Heading | SR26_20250813-1632 | `Introduction` |
| 4 | NRL-52849 | 4819352 | Heading | SR26_20250813-1632 | `HU Behavior when receiving Implausible Signal Values` |
| 5 | NRL-52851 | 4819620 | Heading | SR26_20250813-1632 | `DCSD and HU HMI Communication` |
| 6 | NRL-52857 | 4820119 | Heading | SR26_20250813-1632 | `DTC Maturation Criteria` |
| 7 | NRL-52858 | 4820121 | Heading | SR26_20250813-1632 | `Networking DTC's` |
| 8 | NRL-52859 | 4820122 | Heading | SR26_20250813-1632 | `BH-CAN Loss of Communication` |
| 9 | NRL-52867 | 4820947 | Heading | SR26_20250813-1632 | `Multi-stage' DCSD Display Hot Algorithm` |
| 10 | NRL-52872 | 4821012 | Heading | SR26_20250813-1632 | `DCSD Display Status Behavior` |
| 11 | NRL-52873 | 4821019 | Heading | SR26_20250813-1632 | `Rear Camera Interrupts` |
| 12 | NRL-52875 | 4821021 | Heading | SR26_20250813-1632 | `HU and DCSD Screen ON behavior` |
| 13 | NRL-52877 | 4821025 | Heading | SR26_20250813-1632 | `Rear Camera Events` |
| 14 | NRL-52880 | 4821035 | Heading | SR26_20250813-1632 | `Rear Camera Interrupts` |
| 15 | NRL-52883 | 4821041 | Heading | SR26_20250813-1632 | `Screen Touch Event Interrupts for DCSD` |
| 16 | NRL-52885 | 4821046 | Heading | SR26_20250813-1632 | `HU 3-second Timer Times Out` |
| 17 | NRL-52887 | 4821050 | Heading | SR26_20250813-1632 | `HU and DCSD Screen OFF state Behavior` |
| 18 | NRL-52888 | 4821051 | Heading | SR26_20250813-1632 | `Rear Camera Events` |
| 19 | NRL-52892 | 4821060 | Heading | SR26_20250813-1632 | `Screen Touch Events` |
| 20 | NRL-402565 | 4819538 | Heading | SR26_20260310-1748 | `ICS HMI Communication ` |
| 21 | NRL-402566 | 4819542 | **Information** | SR26_20260310-1749 | `Push Button Data Transfer ` |
| 22 | NRL-402567 | 4819556 | Heading | SR26_20260310-1750 | `HU behavior in response to ICS POWER hardkey pressed events` |
| 23 | NRL-402568 | 4819570 | Heading | SR26_20260310-1751 | `HU behavior in response to ICS SCREEN OFF hardkey press events ` |
| 24 | NRL-402569 | 4819577 | Heading | SR26_20260310-1752 | `Rotary Knob Data Transfer {4819577}` |
| 25 | NRL-402572 | 4819592 | Heading | SR26_20260310-1755 | `Short Press Event ` |
| 26 | NRL-402573 | 4819609 | Heading | SR26_20260310-1756 | `Press and Move Event ` |
| 27 | NRL-402574 | 4819615 | Heading | SR26_20260310-1757 | `Stuck Button Behavior ` |
| 28 | NRL-402578 | 4819627 | Heading | SR26_20260310-1761 | `DCSD Display Status Behavior ` |
| 29 | NRL-402579 | 4819634 | Heading | SR26_20260310-1762 | `Rear Camera Interrupts` |
| 30 | NRL-402580 | 4819636 | Heading | SR26_20260310-1763 | `HU and DCSD Screen ON behavior ` |
| 31 | NRL-402581 | 4819640 | Heading | SR26_20260310-1764 | `Rear Camera Events` |
| 32 | NRL-402582 | 4819647 | Heading | SR26_20260310-1765 | `HU and DCSD Transitioning to Screen OFF behavior` |
| 33 | NRL-402583 | 4819650 | Heading | SR26_20260310-1766 | `Rear Camera Interrupts ` |
| 34 | NRL-402584 | 4819656 | Heading | SR26_20260310-1767 | `Screen Touch Event Interrupts for DCSD ` |
| 35 | NRL-402585 | 4819665 | Heading | SR26_20260310-1768 | `HU and DCSD Screen OFF state Behavior ` |
| 36 | NRL-402586 | 4819666 | Heading | SR26_20260310-1769 | `Rear Camera Events ` |
| 37 | NRL-402587 | 4819675 | Heading | SR26_20260310-1770 | `Screen Touch Events ` |
| 38 | NRL-402588 | 4819848 | Heading | SR26_20260310-1771 | `DCSD Display Hot Behavior ` |
| 39 | NRL-402590 | 4819858 | Heading | SR26_20260310-1773 | `Multi-stage' DCSD Display Hot Algorithm ` |
| 40 | NRL-402591 | 4819870 | Heading | SR26_20260310-1774 | `Touch Screen Event Communication and X-Y Coord System ` |
| 41 | NRL-402593 | 4819913 | Heading | SR26_20260310-1776 | `(Press,) Drag and Drop Event ` |
| 42 | NRL-402595 | 4819920 | Heading | SR26_20260310-1778 | `Capacitive Multi-touch Screen Gesture support ` |

（42 = 41 `Heading` + 1 `Information`；#21 NRL-402566 為唯一之 `Information`。）

### §2-3 來源文件是否已在 `spec-index/sources/`

`spec-index/sources/` 內共 **33** 個檔（`ls | wc -l` = 33）。逐項核對：

| 本線涉及之來源文件 | 是否在 `spec-index/sources/` | 備註 |
|---|---|---|
| CFTS020（`R1LR_Atl-H_26PI1.5 … CFTS_020 ICS and DCSD _20260310-1533.docx`） | **否**（在 `features/ics_management/inputs/`） | 本線以 `inputs/` 供給，非 spec-index |
| CFTS022（`… CFTS_022 Functional Specification_20260608-1205.docx`） | **否**（在 `inputs/`） | 同上 |
| SYS3 SYSAD（`SYS3_CFTS020_ICS_…SYSAD_v1.0.docx`） | **否**（在 `inputs/`） | 同上 |
| `ICS_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` | **否**（在 `inputs/`） | 同上 |
| **`DCSD_and_HU_LVDS_Backchannel_Protocol_v4.1.pdf`** | **否 —— 查無** | 由 §1 #8、#10 逐字指名；**全 repo 查無**（`find . -iname "*Backchannel*"`（排除 `.git`）回傳 **0** 筆） |
| CFTS019 | **否** | `spec-index/sources/` 與 `features/ics_management/inputs/` **皆查無**；惟 `features/audio_mgmt/inputs/`（另一產線）內存在 **8** 個 CFTS019 相關檔。SYS2 之來源欄指向 CFTS019 之列數為 **0** |
| HMI L&F 系列（33 檔） | **是** | `spec-index/sources/` 內之 33 檔全部為 HMI Logic&Flow／L&F 類，**無一被 SYS2 之來源欄引用**（引用列數 0） |

### §2-4 「十二包以來從未掃過之桶」

以「本線前十二包一律以 CFTS020 物件頭（2180）為掃描起點」為基準，逐桶標記：

| 桶 | 列數 | 前十二包是否掃過 |
|---|---|---|
| 來源 ID ∈ CFTS020 之 2180 物件頭 | **260** | **已掃過**（下放包 12 §4 反向查核之桶 ①②③④⑤ 即涵蓋此 260） |
| 來源 ID ∈ CFTS020 但為節標題錨（非物件頭） | **42** | **從未掃過** —— 起點盲區（一） |
| 來源欄空白 | **31**（其中 FR **23**） | **從未掃過** —— 起點盲區（二），即 A-ICS78 |
| 來源 ID ∈ CFTS022 | **0** | 不適用（查無此列） |

**盲區合計 42 + 31 = 73 列（佔 333 之 21.9%）**，其中 `Category` 為 FR 者
**23 列**（42 列中之 FR 數為 **0**）。

---

## §3 【E19 停下條件】

### **E19 觸發。**

§1 判定為「HMI 軟體側可驗證之行為＝是」之列數：**1**。

| 觸發列 | xlsx 列 | ID | 逐字 `Description` |
|---|---|---|---|
| §1 #13 | 76 | **NRL-180522** | `Do not filter out duplicate touch (same coordinates) events during continuous press specifically during dragging/swipe.  Needed for Apple CarPlay™ Certfication` |

另有 **1 列**判為「不可判」（§1 #6，NRL-180512，xlsx 列 66），依 E19 條文不計入觸發，
但一併具名以供分析層裁定。

**依 E19，執行層於此停下。**
本報告**不作任何範圍判斷**（不判 NRL-180522 應否納入驗證範圍、不判其歸 HW 或 SW 責任、
不生成任何 TC、不動任何錨、不對任何 DR 結案、不自取 `A-`／`DR-` 編號）。
範圍判斷屬分析層（Pei）。

---

## §4 下放包未預料之事

### §4-1 【高】31 個空白來源列為 xlsx 之單一連續區塊（列 58–88），無一例外

實測列號：`[58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88]`。
且此區塊內**無任何來源欄非空之列**（區塊內 31 列全空）。

意義（事實層）：這不是「零星漏填」，而是**一整段以外部來源整批匯入而未建追溯之區段**。
其 `子分類` 前 22 列為 `ICS / DCSD (CFTS020)`、`Document ID` 前 22 列為 `SR26_20250813-1632`，
自列 80（NRL-180526）起 **`Document ID` 與 `子分類` 二欄同時轉為空白**，直到區塊結束。
即區塊內部尚有**第二層斷裂**：列 58–79（22 列，有 Document ID）／列 80–88（9 列，全空）。

由 §1 之內容判，此區塊之主題為 **LVDS Backchannel／I2C 觸控介面規格**，
且 §1 #8、#10 逐字指名其真實出處為 `DCSD_and_HU_LVDS_Backchannel_Protocol_v4.1.pdf`。
**下放包預設此 23 列「無 CFTS020 追溯來源」，實測更強：它們有一個具名之外部來源文件，
而該文件不在本線任何輸入路徑內。**

### §4-2 【高】空白區塊中另有 8 列非 FR，其中 3 列 `Out of scope` 之理由逐字指向 DCSD 韌體

下放包只問 23 列 FR。實測空白區塊為 31 列，另 8 列逐一：

| ID | Category | Description（節錄） | `SYS2 MD Feedback`（節錄，逐字） |
|---|---|---|---|
| NRL-180508 | `Heading` | `2.3 LVDS Interface` | （空） |
| NRL-180509 | `Information` | `2.3.0 DCSD LVDS Overview (For R1 Radio Interface)  ` | （空） |
| NRL-180510 | `Out of scope` | `The DCSD must complete initialization of its DeSerializer within 1200ms of Startup` | `Out of scope reason:\nResponsibility for this functionality lies with DCSD firmware; it is out of scope for HW supplier a…` |
| NRL-180516 | `Out of scope` | `DCSD initialize of DeSerializer with temporal I2C master handling …` | 同上 |
| NRL-180518 | `Heading` | `2.2 Serializer Touch Interrupt PIN Definition` | （空） |
| NRL-180521 | `Information` | `The touch behavior and interrupt sequence is NOT dependent on the VERSION message request from the radio.` | （空） |
| NRL-180527 | `Out of scope` | `GPIO-0 cleared by DCSD after message type data transferred._x000D_\nState level back to original, ready for nex…` | 同上 |
| NRL-180531 | `Information` | `During multi touch, If 2 MULTI-TOUCH present, DCSD transmit touch event with new touch coordinate data.` | （空） |

**重要性**：SYS2 自身在同一區塊內**已對 3 列作出「DCSD firmware 責任、HW supplier 範圍外」之
明示裁定**（`Out of scope`），而對 23 列 FR **未作此裁定**。
此為 SYS2 內部之既存分界事實，分析層裁 A-ICS78 時應知其存在。本報告不引申。

### §4-3 【高】SYS2 自帶 `Verifiability` 與 `Verification Method` 欄，下放包完全未提及

SYS2 `Basic Report` 共 **81 欄**（索引 0–80），其中包含
`SYS2 驗證性 Verifiability (Y/N/NA)`、`SYS2 驗證性 Verifiability (Description)`、
`SYS2 驗證方法 (Verification Method)`、`SYS2 驗證標準 (Verification Criteria)`、
`SYS2 追蹤性  Traceability (Y/N/NA)` 等品質屬性欄。

23 列之實測分佈（自列舉取得）：

| `Verifiability` | 列數 | 對應之 §1 #（實測） |
|---|---|---|
| `Y` | **14** | #1–#14 |
| `NA` | **2** | #15（NRL-180524）、#16（NRL-180525） |
| （空白） | **7** | #17–#23（NRL-180526/28/29/30/32/33/34） |
| **合計** | **23** | |

`Verification Method` 於前 16 列逐字皆為 `1. System validation`（正規化後），後 7 列全空。

且 `Verification Criteria` 逐字寫的是 HU 側檢查語句，例如 NRL-163104：
```
* Check HU shall with interface with 8.4" display according to the requirement.
```

**重要性**：本線十二包一路自行推導「可驗證性」，而 SYS2 早已在同一份 xlsx 內
逐列標了 `Verifiability` 與 `Verification Method`，**且與空白 `Document ID`／`子分類` 之
斷裂點（列 80）完全對齊**（列 80 起三欄同時全空）。此欄組從未進入本線任何一包之量測。

### §4-4 【中】42 列節標題錨為第二個結構性盲區，且其中含 HMI 主題節

§2-2 桶 C 之 42 列全為 CFTS020 節標題錨，前十二包因物件頭正則而全數掃不到。
其節名中含明顯之 HMI 主題，例如
`DCSD and HU HMI Communication`／`ICS HMI Communication `／
`HU behavior in response to ICS POWER hardkey pressed events`／
`Capacitive Multi-touch Screen Gesture support `／`(Press,) Drag and Drop Event `。
其 `Category` 為 `Heading` 41 ／`Information` 1，**FR 為 0**。
CFTS020 docx 全文有 **2645** 種 7 位 token，物件頭僅 **2180** 種，
**未被 probe 收錄之 ID 種數為 465**；SYS2 引用到其中 42 個。
本報告不判此 42 列之處置。

### §4-5 【中】`Category` 欄有大小寫不一致，足以令字面比對漏數

全表 `Category` 之相異值（正規化後）含**四組實質類別、六種字面**：
`Out of Scope` **116**／`Out of scope` **7**（4+3）／
`Functional Requirement` **79**（56+23）／`Functional requirement` **1**／
`Information` **85**（81+1+3）／`Heading` **45**（2+41+2）。
（116+7+79+1+85+45 = 333，與資料列數相符。）

**若以精確字串 `== "Functional Requirement"` 比對，將漏掉 1 列**（`Functional requirement`，
落在來源 ID ∈ CFTS020 之桶內，非 23 列之一）；
`Out of Scope` 與 `Out of scope` 之分裂則會令「範圍外」列數自 123 誤讀為 116 或 7。
本報告全程以 `.lower()` 比對，故 23 之數不受影響。**惟前十二包是否受影響，本報告未查。**

### §4-6 【中】來源欄之儲存格型別不一致（字串 vs 數值）

實測：多數來源儲存格為字串（如 `'4819125'`），但至少列 13 為**整數** `4819353`。
以 `str()` 後正則抽取可規避；**若前包曾用型別敏感之比對，可能漏列。本報告未回查前包。**

### §4-7 【低】`Description` 內含多處原文拼字錯誤與尾隨空白

實測具名：`signle`（#18）／`Continously`（#21）／`Certfication`（#13）／`GPOI-0`（#12，應為 GPIO-0）；
多列 `Description` 與 `Category` 值帶尾隨空白。逐字引用時已原樣保留。
影響：任何以 `Description` 作 key 之比對必須先正規化。

### §4-8 【低】`Type` 欄全表單一值

`Type` 欄 333 列逐一皆為 `SYS2_System Requirements Analysis`，無區辨力。

---

## §5 已知局限（逐項揭露）

1. **§1 之「層」「介面位置」「可驗證」三欄為本執行層之閱讀判斷**，非 SYS2 欄位值。
   SYS2 未提供「HW 供應商介面 vs HMI 軟體側」之欄位；判斷依據僅為
   `Description` 逐字內容 + `SW/HW/System` 欄。**此三欄不具量測之客觀性，
   與 §1-0 之「23」（純量測）性質不同，不應等同採信。**

2. **E19 觸發僅繫於單一列（NRL-180522）之判斷**。該列 `SW/HW/System` 為 `System`
   而非 `HW`，且條文未具名執行主體 —— 若分析層認定其主體為 DCSD 韌體，
   則「HMI 軟體側可驗證」之判可能翻轉。本報告已於 §1 #13 具名理由，
   **不代替分析層裁定**。

3. **`DCSD_and_HU_LVDS_Backchannel_Protocol_v4.1.pdf` 未取得**。§1 之 23 列
   有 2 列逐字轉引該文件之「1.2 Display Type Table」。未讀該文件前，
   無法判斷 23 列與該文件之涵蓋關係，亦無法判斷區塊是否有更多列源自該文件。

4. **CFTS022 之物件頭數量以本報告自行解析取得（336）**，未與前包（`cfts022_variant_11.py`／
   `cfts022_reverify_07.py`）之計數交叉核對。惟 CFTS022 之命中列數為 0，
   此數之精確與否不影響任何結論。

5. **§2-2 桶 C 之「42 列 ID 皆在 CFTS020 內文」以 8 個抽樣驗證，非 42 個全驗**。
   全體之 `in_alltokens` 未逐一列印。42 列之 `Description` 皆為 CFTS020 節標題文字之事實
   則為全數目視核對。

6. **未讀 `Polarion`／`_polarion` 二分頁**。沿用下放包 12 之說明視其為工具用分頁；
   本報告未自行驗證該二分頁確不含需求列。

7. **本次僅掃 SYS2**。SYS3 SYSAD（`inputs/SYS3_CFTS020_ICS_…SYSAD_v1.0.docx`）
   與 SWRA（`inputs/ICS_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`）
   **未作反向掃描**。二者是否亦有同類盲區，本報告不知。

8. **`Document ID` 欄之語意未經確認**。`SR26_20250813-1632` 與
   `SR26_20260310-1533`～`-1778` 二種形態並存，後者與 CFTS020 檔名末段
   `20260310-1533` 形態相同（疑為逐物件之流水識別），但**本報告未取得欄義定義，
   故未據以推論**。

9. **未執行任何 git 指令**（含唯讀）。本次自證未改檔之方式為：只呼叫 `Write` 建立
   本報告與 `scripts/sys2_reverse_scan_13.py` 二檔；其餘檔案僅以 `openpyxl`／
   `zipfile`／`importlib`（`read_only=True`）讀取。

10. **`cfts020_probe.py` 以 `importlib` 唯讀載入並呼叫 `parse()`，未修改該檔**；
    其判準（R-ICS2 v2(b)）之正確性沿用前包，本報告未重驗。

---

## 附：本包產出之檔（僅二）

- `features/ics_management/docs/reports/13_sys2_reverse_scan.md`（本檔）
- `features/ics_management/scripts/sys2_reverse_scan_13.py`

其餘任何檔（`RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／`ANALYSIS_LOCK.md`／
`feature.yaml`／`generated/**`／`FORMS.md`／`inputs/**`／`spec-index/**`）**一字未改**。
