# FW036 Diagnostics — framework（Layer 1–3）

規範依據：IN §4.1（三層框架）、IN §4.2（Test Set）、FO §0（Tier 2：Test Set derivation 屬 Pei 簽核）。
Layer 2 名稱逐字取下放包 `CDD-01 §5` 之 21 組草案，經 **R-DIAG9(amend)(b)** 合併為 **20 組**；
**未改任何名稱**（#11 `Audio Output Settings` 併入 #14 `Audio Tone Settings`，其名不留）。

**狀態：`DRAFT`** —— 待 CDD-02 pilot 後依 canon §4.1 LOCK。

母體：037 `SWE1_Diagnostics_V1 (3).xlsx`（sha16 `d317a38f249b7bd8`）**389 列／166 源**
（R-DIAG8(amend)）；追溯索引 CFTS004（sha16 `ffcb202fff92007e`）404 列。

---

## Part I — Layer 1（Test Group）

依 **R-DIAG9(a)**：一本 workbook，**一個** Test Group。

| # | Test Group | ABBR（TC ID `NR1L-{ABBR}-{nnn}`，R-G42）| 037 母體 | 列 |
|---:|---|---|---|---:|
| 1 | `Diagnostics` | `DIAG` | `diagnostics_037_swra_v1_3` | 389 |

## Part II — Layer 2（Test Set，寫入工作簿）—— **20 組**

聚合軸為 **DID 家族**（R-DIAG9(b)）：一個或數個相鄰 DID = 一 Test Set。
跨母節同 DID 依 **R-DIAG9(amend)(c)** 合一（6 個：`$5000`／`$5001`／`$5008`／`$5009`／`$500A`／`$500C`），
Layer 3 各自保留母節。

`OoS` = R-DIAG3 之 Out of Scope 列（不產 TC，計入列數不計入產出）。
`PEND` = `nrc_coverage.tsv` 之 `PENDING_DR1`（R-DIAG5(amend) 後之殘餘）。

| # | Test Set | DID | L3 | 列 | pos | neg | uns | OoS | 產出 | PEND |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `SXM Module Version` | $2843 | 1 | 57 | 19 | 19 | 19 | 0 | **57** | 0 |
| 2 | `SXM Signal Quality` | $2840 $2841 $2842 | 3 | 72 | 34 | 34 | 4 | 0 | **72** | 0 |
| 3 | `SXM Subscription` | $2844 $2845 $2846 $2847 $2848 | 5 | 37 | 13 | 12 | 12 | 0 | **37** | 1 |
| 4 | `SXM Package Routines` | $0307 $0309 | 2 | 13 | 10 | 2 | 1 | 0 | **13** | 0 |
| 5 | `GPS Signal Data` | $2812 | 1 | 34 | 12 | 11 | 11 | 0 | **34** | 0 |
| 6 | `Camera Brightness` | $283F | 1 | 6 | 2 | 2 | 2 | 0 | **6** | 0 |
| 7 | `ECU Internal Settings` | $280C | 1 | 8 | 5 | 3 | 0 | 0 | **8** | 0 |
| 8 | `Media Hub Config` | $2870 | 1 | 6 | 3 | 2 | 1 | 0 | **6** | 0 |
| 9 | `Button Interfaces` | $1820 $1821 | 2 | 7 | 4 | 2 | 1 | 0 | **7** | 0 |
| 10 | `Screen Test Pattern` | $1801 | 1 | 4 | 2 | 1 | 1 | 1 | **3** | 0 |
| 11 | `Buzzer Control` | $5000 | 2 | 40 | 14 | 13 | 13 | 0 | **40** | 0 |
| 12 | `Speaker Quadrant Selection` | $5001 | 2 | 21 | 7 | 8 | 6 | 0 | **21** | 0 |
| 13 | `Audio Tone Settings` | $180C $5002 $5003 $5004 $5005 $5006 | 6 | 28 | 14 | 7 | 7 | 0 | **28** | 0 |
| 14 | `Tuner Control` | $5008 $5009 $500C | 6 | 22 | 7 | 8 | 7 | 0 | **22** | 0 |
| 15 | `Mode Selection` | $500A | 2 | 9 | 3 | 3 | 3 | 0 | **9** | 0 |
| 16 | `In Motion Menu Control` | $500B | 1 | 6 | 3 | 2 | 1 | 0 | **6** | 0 |
| 17 | `Video Input` | $500D $5100 | 2 | 5 | 4 | 1 | 0 | 0 | **5** | 0 |
| 18 | `AV Signal Detection` | $0312 | 1 | 10 | 5 | 2 | 3 | 0 | **10** | 2 |
| 19 | `Audio Measure AC` | $031B | 1 | 3 | 1 | 1 | 1 | 0 | **3** | 0 |
| 20 | `Clear Key Sense PIN` | $030A | 1 | 1 | 1 | 0 | 0 | 0 | **1** | 0 || **合計** | **20 組** | **42 DID 節** | **42** | **389** | **163** | **133** | **93** | **1** | **388** | **3** |

### §4.1.3 決策測試

| 判準 | 命中 |
|---|---|
| `< 3 TC` | **#20 `Clear Key Sense PIN`（1）** —— §4.2 genuine outlier（Routine 母節下唯一之非 SXM／非 AV 常式，無同域可併），R-DIAG9(amend)(b) 裁定維持獨立 |
| `> 80 TC` | 無（最大 #2 `SXM Signal Quality` = 72）|

4 列以下但未觸發者：#10 `Screen Test Pattern`（4 列，實產 **3**）／#17 `Video Input`（5）／#19 `Audio Measure AC`（3）。

**已合併者**：原 #11 `Audio Output Settings`（`$180C`，單列 `SWE1-Diagnostics-056`，Functional Requirement，
**會產 TC**）併入 #13 `Audio Tone Settings` → 28 列。
下放包 CDD-01 §5 稱該單列為 Out of Scope 之 `-057`，**實測有誤**：`-057` 之 L3 為
`$1801 - Screen Test Pattern (Read/Write)`，歸 #10（R-DIAG3(amend)、審閱 A2）。

## Part III — Layer 3（**不入工作簿**，§4.1.5）

= CFTS004 之 `<母節> | $XXXX - <title>`，逐字。被 037 引用者 **42** 個
（R/W 23／I-O 14／Routine 5，R-DIAG9(amend)(a)）；CFTS004 總數 63，未被引用 21，
其中 `$5007 - Mid-Range Settings` 為 R-DIAG9(c) 條文「43 個」與實測 42 之差。

同一 Layer 3 內之 037 列依 **positive → negative → unsupported** 順序連續書寫（§4.1.4 TC sequencing）。

| L2 # | Test Set | Layer 3（CFTS004 `$XXXX - <title>` 逐字）| 037 列 |
|---:|---|---|---:|
| 1 | `SXM Module Version` | `$2843 - X65 Module Version (Read)` | 57 |
| 2 | `SXM Signal Quality` | `$2841 - X65 Signal Quality Diagnostics (Read)` | 35 |
| 2 | `SXM Signal Quality` | `$2842 - X65 Overlay Signal Quality Diagnostics (Read)` | 27 |
| 2 | `SXM Signal Quality` | `$2840 - X65 Antenna Status Diagnostics (Read)` | 10 |
| 3 | `SXM Subscription` | `$2848 - X65 Package Indication Select (Read)` | 3 |
| 3 | `SXM Subscription` | `$2847 - X65 Index ID (Read/Write)` | 4 |
| 3 | `SXM Subscription` | `$2846 - X65 Package Indication Validate (Read)` | 3 |
| 3 | `SXM Subscription` | `$2845 - X65 Event Indication (Read)` | 3 |
| 3 | `SXM Subscription` | `$2844 - X65 Subscription Status (Read)` | 24 |
| 4 | `SXM Package Routines` | `$0309 - X65 MPFA Select Routine` | 8 |
| 4 | `SXM Package Routines` | `$0307 - X65 MPFA Validate Routine` | 5 |
| 5 | `GPS Signal Data` | `$2812 - GPS Signal Data 1 (Read)` | 34 |
| 6 | `Camera Brightness` | `$283F - Camera Level Brightness (Read/Write)` | 6 |
| 7 | `ECU Internal Settings` | `$280C - ECU Current Internal Settings (Read/Write)` | 8 |
| 8 | `Media Hub Config` | `$2870 - Media Hub Config (Read)` | 6 |
| 9 | `Button Interfaces` | `$1820 - Push Button Control Interface (Read)` | 2 |
| 9 | `Button Interfaces` | `$1821 - Steering Wheel Module Interface (Read)` | 5 |
| 10 | `Screen Test Pattern` | `$1801 - Screen Test Pattern (Read/Write)` | 4 |
| 11 | `Buzzer Control` | `$5000 - Buzzer Control (Read)` | 1 |
| 11 | `Buzzer Control` | `$5000 - Buzzer Control` | 39 |
| 12 | `Speaker Quadrant Selection` | `$5001 - Speaker Quadrant Selection (Read)` | 3 |
| 12 | `Speaker Quadrant Selection` | `$5001 - Speaker Quadrant Selection` | 18 |
| 13 | `Audio Tone Settings` | `$180C - Radio Audio Output Settings` | 1 |
| 13 | `Audio Tone Settings` | `$5006 - Fade Settings` | 2 |
| 13 | `Audio Tone Settings` | `$5005 - Balance Settings` | 2 |
| 13 | `Audio Tone Settings` | `$5004 - Treble Settings` | 5 |
| 13 | `Audio Tone Settings` | `$5003 - Bass Settings` | 9 |
| 13 | `Audio Tone Settings` | `$5002 - Radio Volume` | 9 |
| 14 | `Tuner Control` | `$500C - SDAR Station Selection (Read)` | 3 |
| 14 | `Tuner Control` | `$5009 - Frequency Step Selection (Read)` | 3 |
| 14 | `Tuner Control` | `$5008 - Seek Status (Read)` | 3 |
| 14 | `Tuner Control` | `$500C - SDAR Station Selection` | 4 |
| 14 | `Tuner Control` | `$5009 - Frequency Step Selection` | 3 |
| 14 | `Tuner Control` | `$5008 - Seek Status` | 6 |
| 15 | `Mode Selection` | `$500A - Mode Selection (Read)` | 3 |
| 15 | `Mode Selection` | `$500A - Mode Selection` | 6 |
| 16 | `In Motion Menu Control` | `$500B - In Motion Menu Control` | 6 |
| 17 | `Video Input` | `$5100 - Video Input` | 3 |
| 17 | `Video Input` | `$500D - Video Input Settings` | 2 |
| 18 | `AV Signal Detection` | `$0312 - AV Signal Detection` | 10 |
| 19 | `Audio Measure AC` | `$031B - Audio Measure AC` | 3 |
| 20 | `Clear Key Sense PIN` | `$030A - Clear Key Sense PIN` | 1 |
---

## Part IV — 未鎖定項（LOCK 前須決）

| # | 項 | 去向 |
|---:|---|---|
| 1 | Layer 2 之 20 組名稱（Pei 未逐字簽核）| **[PEI]** |
| 2 | `PENDING_DR1` 3 列之 NRC（`SWE1-Diagnostics-156/157/237`）| DR-DIAG-1 |
| 3 | CDD-02 pilot 後之 TC 實數與批次切分 | CDD-02 |
