# 11 上繳 —— 素材補入、LID 表 Atlantis High 欄實測、UI 標籤查證

執行層，2026-08-22。對應下放包 `docs/handoff/11_lid.md`。

---

## 0. 執行結果一覽

| 任務 | 內容 | 狀態 |
|---|---|---|
| T1 | 八份素材複製 + SHA256 兩側比對 | 完成，**八檔全部一致** |
| T2 | `DATA_REQUESTS.md` 新增九列；DR-6 解除條件；**DR-6b 未建**（見 §2.3） | 完成 |
| T3 | LID 表 19 個 LID 逐一實測（Atl-H 欄）；PROXI 六參數 | 完成，**兩處與分析層探測對差相符** |
| T4 | UI 標籤查證 | 完成 —— **三項中一項不符、二項確認** |
| T5 | 驗證 | 完成 |
| T6 | 本包 | 完成 |

**本包三項須先看**：§3.2 之 `DateTmFormat2`（第六個 Atl-H 空值，
**不在 R-TM62 射程**）、**§4 之設定頁正式名為 `Clock` 而非
`"Time and Date"`**、以及 **§3.4 我在 PROXI 上讀錯欄、差點報出一個
反向的錯誤結論**。

---

## 1. T1 —— 八份素材，SHA256 兩側逐檔比對

```
OK  4814254- 4561062- CFTSMV015_CIP_R1_O833_116_inline.rtf   ac9be886…    89,141 B
OK  4814255- 4561063- CFTSMV015_CIP_R1_O882_117_inline.rtf   0163cf7d…   154,078 B
OK  4814256- 4561064- CFTSMV015_CIP_R1_O922_118_inline.rtf   186a6c7f…   154,078 B
OK  R1LR_Atl-H_…_CFTS _015 Time and Date_20250910_1122.reqifz 488469ce…   336,074 B
OK  SR24 R1 Market Configuration Table v1.6.xlsx              ae4cf0b9…   279,779 B
OK  HMI Settings List R1 SR24 Post 2A (June 15 2023).xlsx     a2533bf3…   371,268 B
OK  R1LR_Atl-H_…_CFTS_036_HMI Framework_SR26_20250909-1815.doc adcb4ca8…    92,160 B
OK  R1LR_Atl-H_…_CFTS_014 Internationalization…_20250909-1851.doc e0ad80c2… 526,848 B

八檔全部一致: True
```

`inputs/` 由 5 檔增為 **13 檔**。複製前逐檔確認來源存在（無一 MISS）。

**一項可注意者**：`…_O882_117_inline.rtf` 與 `…_O922_118_inline.rtf`
**檔案大小相同（154,078 B）但 SHA256 不同**（`0163cf7d…` vs `186a6c7f…`）
—— 兩者為不同內容，非重複檔。若只比大小會誤判為重複。

---

## 2. T2 —— DATA_REQUESTS

新增九列（DR-6 更新 + DR-12 部分 RECEIVED + DR-13…DR-19 七份素材）。
inline RTF 三份依指令併為一列（DR-14），註明三個檔名。

### 2.1 DR-6 已解除（對 14 個 LID）

實測 14 個時間日期 LID 在 Atlantis High 欄**全部有值，CAN 一律為 `FD`**。
故 segment 之來源已具備，取自 `data/lid_atlantis_high.tsv`。

### 2.2 素材之服務對象已逐份標註

七份新素材中**四份本包未解析**（RTF 三份、ReqIF、Market Config、
CFTS_036、CFTS_014），只登記 RECEIVED 與推測之服務 leaf。
**「未評估」已逐列寫明**，不以 RECEIVED 掩蓋未讀之事實。

### 2.3 DR-6b **未建立** —— 依 R-TM62

`11` T2 指派新增 DR-6b。但 `12` §1 之 R-TM62 **明文取消該登記**
（五個 TLM LID 為「本架構無此對映」而非缺件）。

執行順序為 `11` → `12`，惟兩包同時在手，故**未建立一個隨即被取消的
登記**。已於 `DATA_REQUESTS.md` 記其始末，使日後讀者不會以為遺漏。

---

## 3. T3 —— LID 表實測

### 3.1 與分析層 §2.1 之對差：**兩筆皆相符**

| LID | 分析層探測 | 執行層對 `inputs/` 重測 | 判定 |
|---|---|---|---|
| `DateTmHour` | `TELEMATIC_FD_1.Hour1_TLM` / `Hour2_TLM`，CAN=FD，4 bits each | 同 | **符** |
| `DateTmFormat` | `TELEMATIC_FD_10.DateTmFormat`，CAN=FD，`0=NDEF0/1=FORMAT_12H/2=FORMAT_24H/3=FORMAT_0`，SNA=7 | 同，且完整值域另有 `4=FORMAT_1 / 5=FORMAT_2 / 6=FORMAT_3 / 7=SNA` | **符**（分析層只列前四項，非錯誤，是節錄） |

**架構欄確認**：`CAN Mapping` 分頁列 2 之分組逐字為
`A LID Information / F Powernet / K CUSW / P Atlantis / U Compact /
**Z Atlantis High** / AE Comments`。本 feature 取 **Z–AD（26–30）**，
與 A-TM26 所述一致。

### 3.2 **`DateTmFormat2` —— 第六個 Atl-H 空值，不在 R-TM62 射程**

```
DateTmFormat2   Atlantis High 欄（26-30）全空
                Powernet 欄  = 'Radio_A3.DateTmFormat2'
                Usage Comment = 'For PHEV'
                來源列 408
```

R-TM62 之射程**明文限於五個 `TLM_MANAGED_TIME_DATE_*`**。
本項不在其內，故執行層**不逕行套用** —— 於 tsv 記為 `(EMPTY)`
而非 `N/A (R-TM62)`，兩者在 tsv 中可區分。

**三種可能之處置，執行層不擇**：(i) 同 R-TM62 視為不適用；
(ii) 視為缺件登記 DR；(iii) 該 LID 本 feature 根本不用（`For PHEV`
之註記暗示其為 PHEV 專屬，而 `DateTmFormat` 已涵蓋一般情形）。
**提請裁定。** 若採 (iii)，本項連 tsv 都不必列。

### 3.3 全 19 個 LID 之實測（R-TM31：列全集）

`data/lid_atlantis_high.tsv`，19 資料列 × 7 欄，`ArchColumn` 一律記
`Atlantis High (col 26-30)`（A-TM26 之強制記錄）或 `N/A (R-TM62)`。

| 分組 | LID | Atl-H SignalName | CAN |
|---|---|---|---|
| 時間 | `DateTmHour` | `TELEMATIC_FD_1.Hour1_TLM` / `Hour2_TLM` | FD |
| | `DateTmMinute` | `…Minute1_TLM` / `…Minute2_TLM` | FD |
| | `DateTmSecond` | `…Second1_TLM` / `…Second2_TLM` | FD |
| | `DateTmFormat` | `TELEMATIC_FD_10.DateTmFormat` | FD |
| | `DateTmFormat2` | **(EMPTY)** | — |
| 日期 | `DateTmYear` | `…Year1_TLM` … `…Year4_TLM`（四個） | FD |
| | `DateTmMonth` | `…Month1_TLM` / `…Month2_TLM` | FD |
| | `DateTmDay` | `…Day1_TLM` / `…Day2_TLM` | FD |
| GPS | `GPSDateTmHour` | `TELEMATIC_FD_1.GPS_UTC_Hour` | FD |
| | `GPSDateTmMinute` | `…GPS_UTC_Minute` | FD |
| | `GPSDateTmSecond` | `…GPS_UTC_Second` | FD |
| | `GPSDateTmYear` | `…GPS_Date_Year` | FD |
| | `GPSDateTmMonth` | `…GPS_Date_Month` | FD |
| | `GPSDateTmDay` | `…GPS_Date_Day` | FD |
| TLM | `TLM_MANAGED_TIME_DATE_Hour` … `_Year`（五個） | `N/A (R-TM62)` | — |

**14 個有值、1 個空、5 個 N/A**。全部 CAN 皆為 `FD`（無 CAN-B / CAN-C）。

### 3.3.1 **`$DateTmHour$` 在 Atl-H 是兩個 4-bit BCD 數位** —— 分析層警示成立

```
Format = '4 bits each / 0 to 9 (digit 1) / 0 to 9 (digit 2)'
```

而 CFTS015 物件 `4813930` 之敘述為
`minimum value of 0 hours … maximum value of 23 hours`（單一 0–23 值）。

**兩者形態不同**，影響 009（`validate hour (0–23), minute (0–59),
second (0–59)`）之期望值寫法：在 Atl-H，「hour = 23」是
`Hour1_TLM = 2` 且 `Hour2_TLM = 3`，不是單一訊號等於 23。

**同樣形態者**：Minute / Second / Month / Day（各兩個數位）、
**Year（四個數位）**。GPS 系列則為單一 8/16-bit 值
（`GPSDateTmHour` = `8 bit signal / 0 - 23 hours`），**與 DateTm 系列不同**。

**執行層未改任何 TC 措辭**（尚未生成），但此為 B1 生成時之硬約束，
已列入 `13` T5 之生成前確認。

### 3.3.2 SNA 欄 —— 僅 `DateTmFormat` 有值

19 個 LID 中只有 `DateTmFormat` 之 SNA = `7`，其餘全空。
canon §8.7.5 之訊號三件組為 `<Signal> in <MESSAGE> on <segment>`，
**不含 SNA**，故不阻塞。但 022（SNA Handling）之期望值需要 SNA 值 ——
**除 `DateTmFormat` 外無來源**，列入未驗清單。

### 3.4 **PROXI 六參數 —— 我讀錯欄，差點報出反向的錯誤結論**

首次量測我用欄 26–30 讀 `Proxi & Configuration` 分頁，六個參數
**全部為空**，正要報「Atl-H 不支援這六個 PROXI 參數」。

實際上，**該分頁之架構分組與 `CAN Mapping` 不同**：

```
CAN Mapping          : F Powernet | K CUSW | P Atlantis | U Compact | Z Atlantis High | AE Comments
Proxi & Configuration: F Powernet | K CUSW | P **Atlantis & Atlantis High** | U Compact | Z Comments
```

**在 Proxi 分頁，Atlantis High 與 Atlantis 合併於 P–T（16–20），
而 Z 欄是 Comments。** 我讀到的「全空」是讀了 Comments 區的必然結果。

**這是 A-TM26 的鏡像陷阱**：A-TM26 警告「取第一組 Powernet 會錯」，
而此處是「把同一活頁簿另一分頁的欄號直接套用」——
**錯誤同樣不報錯、同樣產出形態合理的結果**（全空看起來像一個有意義的
結論，甚至與 R-TM62 的形態相符，可以直接寫進報告）。

**建議 A-TM26 之判準擴充**：`ArchColumn` 之記錄須含**分頁名**，
不能只記欄號 —— 已於 `data/proxi_atlantis_high.tsv` 記為
`Atlantis & Atlantis High (col 16-20, Proxi sheet)`。

### 3.5 PROXI 六參數之值域（正確欄）—— 全部有值

| 參數 | Signal | CAN | 值域（節錄） |
|---|---|---|---|
| `NAV_Presence` | `NAV_Presence` | PROXI | `0 = Absent / 1 = Present` |
| `GPS_Presence` | `GPS_Presence` | PROXI | `Proxi: GPS_Presence / 0= Absent / 1= Present` |
| `Cluster_Display_Type` | `Cluster_Display_Type` | PROXI | `0 = No Display Available / 1 = Base Display / 2 = Medium Display / 3 = High Display / 4 = TFT B/W Display / …` |
| `Country_Code` | `Car_Configuration_16.Country_Code` | PROXI | （Format 欄空） |
| `VC_VEH_LINE` | `Car_Configuration_15.Vehicle_Line_Configuration` | `None: / Proxi` | `0 = Invalid / 51 = 343 / 52 = 327FL / 53 = 226 / 80 = PF / 81 = KL/K4 / …` |
| `Hybrid_Type` | `Hybrid_Type` | （空） | `0 = Not Applicable / 1 = BEV / 2 = HEV / 3 = PHEV / …` |

**這解除了 `10` §1.2 之 G3 缺口的一半**：002 / 019 之前置條件現有值域
來源（`NAV_Presence = 1 (Present)` 等可寫）。**另一半仍缺** ——
「如何設定 PROXI 參數」之操作方式無來源，屬設備能力，同 DR-8/9/10 之族。

---

## 4. T4 —— UI 標籤查證（**三項中一項不符**）

來源：`HMI Settings List R1 SR24 Post 2A (June 15 2023).xlsx`，
`Settings` 分頁。**本 feature 之設定頁為第 7 節。**

### 4.1 逐項結果

| v3 之標籤 | 有／無／近似 | 該表之逐字值 |
|---|---|---|
| `"Time and Date"`（設定頁名） | **無 —— 不符** | 設定頁逐字為 **`7. Clock`**；註記：`when Set Date setting is implemented, rename settings section from "Clock" to, "Clock & Date"` |
| `"Sync Time with GPS"` | **有（逐字相符）** | `Sync Time with GPS`｜`On/Off Checkbox`｜來源標 `CFTS015` |
| 12/24 小時設定項名 | **近似** | 項名為 `Time Format`，`2 radio buttons`，值為 **`12 hrs , 24 hrs`**（非 `12-hour` / `24-hour`） |
| 時區設定項 | **無 —— 全表零命中** | — |
| DST 設定項 | **無 —— 全表零命中** | — |

### 4.2 **時區 / DST 零命中 —— R-TM60 之第二個佐證，且更強**

下放包 T4 明言「若不存在，即為 R-TM60 刪除三條之第二個佐證」。

**實測不只是不存在於 Clock 頁，而是全表零命中**（四個分頁、
`time zone` 與 `daylight|dst` 兩組樣式）。而該表**逐項標明來源
CFTS**（Clock 頁全部項目標 `CFTS015`）—— 即該表確實涵蓋本 feature
之設定項，時區/DST 之缺席不是該表未收錄，是**確實沒有這兩個設定項**。

### 4.3 Clock 設定頁之完整項目（供常數表修訂用）

```
7. Clock          ← 設定頁名（Set Date 實作後改名 "Clock & Date"）
  1  Sync Time with GPS    On/Off Checkbox                        CFTS015
  2  Set Time Hours        -/+ selector    1-12 (12 hr) / 00-23 (24hr)  CFTS015
  3  Set Time Minutes      -/+ selector    00-59                   CFTS015
  4  Time Format           2 radio buttons  12 hrs , 24 hrs        CFTS015
                           2 radio buttons  AM, PM                 CFTS015
  5  Show Time in Status Bar  On/Off Checkbox                      CFTS015
  6  Set Date (DD/MM/YY)   >                                       CFTS015
     6.1/6.2/6.3  Set Date Day / Month / Year   -/+ selector       CFTS015
     （另有 MM/DD/YY 與 YY/MM/DD 兩種順序之對應項）
  7  Show Time During Screen Off / Show Time and Date During Screen Off   CFTS022
```

**「Set Time Hours」之值域隨格式而變**（`1-12 (12 hr)` / `00-23 (24hr)`），
且註記 `Greys out with sync option selected` —— 即 GPS 同步開啟時
手動設定項灰化。**這是 001 / 015 之前置條件的直接來源**
（`GPS_SYNC_OFF` 為手動設定之前提，spec 有據）。

### 4.4 未逕改常數表

依禁令 T4 只查證。**v3 之三處 UI 標籤中，兩處需修訂**
（`"Time and Date"` → `"Clock"`；`12-hour` → `"12 hrs"`），
`"Sync Time with GPS"` 無須改。**由分析層於下包修訂。**

**對 `13` §4 之影響**：`13` 稱「凡涉 UI 標籤者，若該標籤未見於 CFTS015
或 HMI Settings List，一律寫 `PENDING: DR-12`」。依本節實測，
**設定頁名、Sync 開關、格式項名三者皆有正式來源**，故 B1 生成時
該三者**不必寫 DR-12 佔位**，改用該表之逐字值。

---

## 5. T5 —— 驗證輸出

```
inputs/                                   13 檔（原 5 + 新 8）
wc -l data/lid_atlantis_high.tsv          20（表頭 1 + 19 資料列）
wc -l data/proxi_atlantis_high.tsv         7（表頭 1 + 6 資料列）
grep -c 'Atlantis High' lid_…tsv          14
grep -c 'N/A (R-TM62)'  lid_…tsv           5      （另 1 列為 (EMPTY)）
grep -c 'RECEIVED' DATA_REQUESTS.md        9
```

**tsv 健全性以可獨立呼叫之守衛驗證**（R-TM56）：
`assert_tsv_wellformed(path, ncols=7)` 逐列檢查欄數，19 列全數 7 欄。

**必要，因為原始儲存格內含換行**（`TELEMATIC_FD_1.Hour1_TLM\n
TELEMATIC_FD_1.Hour2_TLM`）—— 直接寫入 tsv 會使一列裂成兩列而欄數不符。
首版即犯此錯，由該守衛攔下。換行以 ` / ` 取代，**不截斷資料**。

---

## 6. 未驗清單（R-TM54 三分）

### A. 可驗而未驗

| # | 項目 |
|---|---|
| A1 | 七份新素材中**四份未解析**（RTF ×3、ReqIF、Market Config、CFTS_036、CFTS_014）—— 只登記 RECEIVED |
| A2 | 022 之 SNA 期望值：除 `DateTmFormat`（SNA=7）外，19 個 LID 之 SNA 欄皆空，無來源 |
| A3 | `10` §1.2 之 G1（讀 CAN 訊號，9 片）、G2（注入無效值，3 片）、G4（VES 顯示）仍無操作來源 |
| A4 | G3 之另一半：PROXI 參數之**設定方式**（值域已得） |
| A5 | 07/08/09 遺留六項（B-1…B-6 未守側、018/017 objects、BOUNDARY_NOTES 重疊、交付件形式慣例、`-000` 顯示、A-TM25 無自動攔截） |

### B. 結構性不可複驗 —— 待 Pei

| # | 項目 |
|---|---|
| B1 | **`DateTmFormat2` 之處置**（§3.2，三選項） |
| B2 | 常數表 v3 之 UI 標籤修訂（§4.4，兩處需改） |
| B3 | DR-8/9/10 設備能力；G1–G4 之操作來源 |
| B4 | A-TM25、RD-1 送出 |

### C. 已解決

| # | 項目 | 解決於 |
|---|---|---|
| C1 | DR-6（CAN 網段依據）—— 對 14 個 LID | 本包 T3，CAN 一律 `FD` |
| C2 | v3 之 UI 標籤是否有正式來源（`10` A2） | 本包 T4 |
| C3 | PROXI 六參數之值域來源（`10` G3 之一半） | 本包 T3.5 |
| C4 | DR-6b 是否登記 | 依 R-TM62 不建，始末已記 |

---

## 7. 未執行者（下放包所禁，逐項確認）

- 未生成任何 TC
- **未自 Powernet / CUSW / Atlantis / Compact 欄取值** —— §3.4 之首次
  誤讀為 Proxi 分頁之 Comments 區，**非他架構欄**，且已更正
- **未改常數表**（T4 只查證，兩處需改之處只回報）
- **未裁 §2.2 之架構歸屬**（Tier 3）；`DateTmFormat2` 亦未逕裁
- 未改 `backend/`、canon、`docs/fw036/framework.md`
- **未以 openpyxl 存回任何工作簿** —— LID 表與 HMI 表皆 `read_only=True`
- 未碰 `features/vehicle_setting/`
- 未動 git（R-TM36）

---

## 8. 提請裁定

1. **`DateTmFormat2`（§3.2）**：Atl-H 欄為空但不在 R-TM62 射程。
   三選項：同 R-TM62 視為不適用／登記缺件／本 feature 根本不用（`For PHEV`）。
2. **A-TM26 之判準擴充（§3.4）**：`ArchColumn` 之記錄須含**分頁名**。
   同一活頁簿之不同分頁，其架構欄分組不同（Proxi 分頁把 Atlantis 與
   Atlantis High 合併於 16–20，Z 欄是 Comments）—— 套錯欄號同樣不報錯。
3. **常數表 v3 之 UI 標籤兩處需改（§4.4）**：
   `"Time and Date"` → `"Clock"`（Set Date 實作後為 `"Clock & Date"`）、
   `12-hour` → `"12 hrs"`。`"Sync Time with GPS"` 正確無須改。
4. **`13` §4 之 DR-12 佔位規則可放寬（§4.4）**：三個 UI 標籤皆有正式來源，
   B1 生成時不必寫佔位。
5. **009 之期望值形態（§3.3.1）**：`$DateTmHour$` 在 Atl-H 為兩個 4-bit
   BCD 數位而非單一 0–23 值，`DateTmYear` 為四個數位；GPS 系列則為單一
   8/16-bit 值。B1 生成須依此，不得照 CFTS015 敘述之單值形態寫。
