# 下放包 11 — 素材補入、LID 表之架構欄陷阱、DR-6 解除路徑

分析層 → 執行層。往返編號 `11`。對應上繳 `docs/upstream/11_lid.md`。

Pei 已將 `Logical Identifiers and CAN Mapping v1_76.xlsx` 放入 `inputs/`
（實測確認），並指示複製其餘素材。

**本包最重要的是 §2：LID 表有五組架構欄，取錯一組則每一條訊號斷言都錯，
而錯的那組正好是最容易取到的第一組。**

---

## 1. 素材複製（分析層無此能力，須執行層為之）

分析層之 Filesystem 工具無「使用者端 → 使用者端」之複製能力
（`copy_file_user_to_claude` 只複製到分析層沙箱），**故本項只能由執行層執行**。

```bash
cd /Users/peihe/Work_Projects/TC_Generator
SRC="/Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/25PI3.5"
DST="features/time_management/inputs"

# (1) CFTS015 三份 inline RTF —— 與已收之 CFTS 文件同層，Phase 0 漏掃
cp "$SRC/Reference Docs/CFTS015/"*.rtf "$DST/"

# (2) CFTS015 ReqIF 匯出
cp "$SRC/Sub System/Cabin/R1LR_Atl-H_25PI3.5_Cabin_CFTS _015 Time and Date_20250910_1122.reqifz" "$DST/"

# (3) R1 Market Configuration Table
cp "$SRC/Reference Docs/ECU Specific Reference Documents/SR24 R1 Market Configuration Table v1.6.xlsx" "$DST/"

# (4) HMI Settings List —— UI 標籤之候選來源
cp "$SRC/HMI/HMI Settings List R1 SR24 Post 2A (June 15 2023).xlsx" "$DST/"

# (5) CFTS_036 HMI Framework
cp "$SRC/Sub System/Activation and Configuration/R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_036_HMI Framework_SR26_20250909-1815.doc" "$DST/"

# (6) CFTS_014 Internationalization Localization —— 時間/日期格式依地區
cp "$SRC/Sub System/Cabin/R1LR_Atl-H_25PI3.5_Cabin_CFTS_014 Internationalization Localization_SR26_20250909-1851.doc" "$DST/"

ls -la "$DST"
```

**複製後逐檔記 SHA256**，與來源比對（`cmp` 或 `shasum` 兩側），
確認複本一致。

## 2. **LID 表之架構欄陷阱 —— A-TM26**

分析層已對 Pei 補入之 LID 表做唯讀探測。`CAN Mapping` 分頁 2626 列 LID，
**其第 2 列為架構分組列**：

| 欄區 | 架構 |
|---|---|
| 1–5 | LID Information（LID 名、Function、Object Text、Arch Basis）|
| **6–10** | **Powernet** |
| 11–15 | CUSW |
| 16–20 | Atlantis |
| 21–25 | Compact |
| **26–30** | **Atlantis High** ← **本 feature** |
| 31 | Comments |

**本 feature 為 R1LR Atl-H（Atlantis High），須取 26–30 欄。**

實測對照（同一 LID，兩個架構欄之值完全不同）：

| LID | **Powernet（欄 6–7）** | **Atlantis High（欄 26–27）** |
|---|---|---|
| `DateTmHour` | `Clock_Date.DateTmHour` / **CAN-C** | `TELEMATIC_FD_1.Hour1_TLM`+`Hour2_TLM` / **FD** |
| `DateTmFormat` | `Clock_Date.DateTmFormat` / **CAN-B** | `TELEMATIC_FD_10.DateTmFormat` / **FD** |

```
A-TM26（PENDING → 立即適用，Tier 2 —— 本包即納入判準）

LID 表 `CAN Mapping` 分頁有五組架構欄（Powernet / CUSW / Atlantis /
Compact / Atlantis High），同一 LID 在各組之 Signal Name 與 CAN 網段
**完全不同**。

本 feature 為 Atlantis High，**須取欄 26–30**。

**風險**：欄 6–10（Powernet）為由左至右第一組，是最容易取到的一組，
且其值形態合理（`Clock_Date.DateTmHour` / `CAN-C`）—— 取錯不會報錯、
不會缺值、看起來完全正常，**但每一條訊號斷言之 MESSAGE 與 segment 皆錯**。

此為本 feature 一路在防之形態的又一實例：**錯誤實作會產出合法外觀之值**
（同 A-TM21(a) 之欄位對映、A-TM22 之 member 對映）。

**強制判準**：凡自 LID 表取值者，須於同一處記錄「取自哪一組架構欄」，
且 lint 須驗其取自 Atlantis High。無此記錄之取值一律視為未驗。
```

### 2.1 Atlantis High 之實測值（供 C-5 使用）

**須由執行層對 `inputs/` 之檔案重測後方為基線**（分析層跑在沙箱複本）。

分析層探測所得，Atlantis High 欄：

- `DateTmHour` → `TELEMATIC_FD_1.Hour1_TLM` / `Hour2_TLM`，CAN=**FD**
  （4 bits each，digit 1 / digit 2）
- `DateTmFormat` → `TELEMATIC_FD_10.DateTmFormat`，CAN=**FD**
  （`0=NDEF0 / 1=FORMAT_12H / 2=FORMAT_24H / 3=FORMAT_0`，SNA=7）

**注意 `$DateTmHour$` 在 Atlantis High 是兩個 4-bit 數位訊號而非單一
8-bit 值** —— 這與 CFTS015 之 `4813930`（`minimum value of 0 hours …
maximum value of 23 hours`）之敘述形態不同。**TC 之期望值寫法受此影響**，
執行層須於 T3 逐 LID 確認。

### 2.2 `TLM_MANAGED_TIME_DATE_*` 五 LID —— **Atlantis High 欄為空**

五個 TLM LID 只在**欄 16–20（Atlantis）**有值：

```
TLM_MANAGED_TIME_DATE_Hour → TLM_MANAGED_TIME_DATE.Hour1_TLM_Master … / CAN-B
（Day / Minute / Month / Year 同形）
```

**Atlantis High 欄（26–30）無值。**

這與 framework Part VII 之既有觀察一致（21 個可達章節全落 `1.3.1.*` 與
`1.5.2.*`，而 `1.5.2.*` 為 **LTM / Atlantis Mid** 之章節）——
**即本 feature 之 leaf 有一部分其實錨在 Atlantis Mid 之需求上。**

**這是一個尚未裁定之範圍問題，本包只登記不裁**：017 / 020 之
`TLM_MANAGED_*` 斷言，其架構欄該取 Atlantis 還是視為不適用於 Atl-H？
**屬範圍界定，Tier 3，呈 Pei**（見 §5）。

## 3. DR-6 之解除路徑

DR-6（CAN 網段依據）之缺件為「DBC 或 EE 架構文件」。
**LID 表提供 `CAN` 欄，即 segment 之權威來源** —— 依既有慣例，
LID 表為 CAN 訊號對映之第一權威。

**故 DR-6 可解除，但有兩個前提**：

1. 取值須來自 **Atlantis High 欄**（A-TM26）
2. 該 LID 在 Atlantis High 欄**有值**；無值者（如五個 TLM LID）
   仍為 `PENDING`，其成因由「無來源文件」改為「來源文件對本架構無對應」
   —— **兩者是不同的缺件，佔位字串須區分**

`R-TM49` 之例外條款（CFTS 內文明述網段者可直接用）**與 LID 表併行時，
以 LID 表優先** —— 前者是敘述，後者是對映表。若兩者衝突，回報不逕採。

---

## 4. 指令

### T0 / T1 — 素材複製與 SHA 比對

依 §1。逐檔回報來源與複本之 SHA256。

### T2 — `DATA_REQUESTS.md`：六列新增 + DR-6 更新

新增六列（inline RTF 三份可併為一列，註明三個檔名），Status 一律
`RECEIVED（2026-08-22，Pei 補入）`，並註明各自服務之 leaf。

**DR-6 依 §3 更新**：來源已到（LID 表），解除條件改為
「(i) 取自 Atlantis High 欄 (ii) 該 LID 在該欄有值」。
新增子項 **DR-6b**：Atlantis High 欄無值之 LID（五個 TLM_MANAGED_*）
之處置，其成因為「來源文件對本架構無對應」，**與 DR-6 不同**。

### T3 — LID 表逐 LID 實測（**對 `inputs/` 之檔案**）

對本 feature 用到之全部 LID，逐一取 **Atlantis High 欄（26–30）** 之
Signal Name / CAN / Format / SNA，產出
`data/lid_atlantis_high.tsv`，欄位：

```
LID  |  ArchColumn  |  SignalName  |  CAN  |  Format  |  SNA  |  SourceRow
```

`ArchColumn` 固定寫 `Atlantis High (col 26-30)` —— **A-TM26 之強制記錄**。

須涵蓋之 LID（取自 CFTS015 內文與 037，**全集**）：

```
DateTmHour  DateTmMinute  DateTmSecond  DateTmFormat  DateTmFormat2
DateTmYear  DateTmMonth   DateTmDay
GPSDateTmHour  GPSDateTmMinute  GPSDateTmSecond
GPSDateTmYear  GPSDateTmMonth   GPSDateTmDay
TLM_MANAGED_TIME_DATE_Hour  _Minute  _Day  _Month  _Year
```

**逐 LID 標明該欄有值或無值**（R-TM31：列全集不只計數）。
與分析層 §2.1 之兩筆探測結果對差，不符即回報。

**另須回報**：`Proxi & Configuration` 分頁（449 列）是否含
`NAV_Presence` / `GPS_Presence` / `Cluster_Display_Type` / `Country_Code`
/ `VC_VEH_LINE` / `Hybrid_Type` 六個 PROXI 參數 —— 若有，其值域即為
前置條件之來源，可望解除另一批未登記之缺口。

### T4 — 常數表 v3 之 UI 標籤查證（**HMI Settings List**）

以 `HMI Settings List R1 SR24 Post 2A (June 15 2023).xlsx` 查證
v3 中之 UI 標籤是否有正式來源：

```
"Time and Date"（設定頁名）    "Sync Time with GPS"
時間格式之 12/24 小時設定項名   時區設定項（若存在）
DST 設定項（若存在 —— 若不存在，即為 R-TM60 刪除三條之第二個佐證）
```

**逐項回報「有／無／近似」**，近似者附該表之逐字值。
**不逕改常數表** —— 依實測結果由分析層於下包修訂。

### T5 — 驗證

```bash
ls features/time_management/inputs/
grep -c '' features/time_management/data/lid_atlantis_high.tsv
grep -n 'Atlantis High' features/time_management/data/lid_atlantis_high.tsv | head -3
grep -n 'DR-6b\|RECEIVED' features/time_management/DATA_REQUESTS.md
```

### T6 — 上繳

`docs/upstream/11_lid.md`。依 R-TM54 三分列未驗清單。

### 不得執行者

- 不動 git（除非 Pei 直接指示）
- **不生成任何 TC**
- **不自 Powernet / CUSW / Atlantis / Compact 欄取值**（A-TM26）
- **不改常數表**（T4 只查證）
- 不裁 §2.2 之架構歸屬（Tier 3，呈 Pei）
- 不改 `backend/`、canon、`docs/fw036/framework.md`
- 不以 openpyxl 存回任何工作簿
- 不碰 `features/vehicle_setting/`

---

## 5. 呈報 Pei

1. **A-TM26 —— LID 表五組架構欄，取錯不會報錯。** Powernet 欄是最容易
   取到的第一組且值形態合理，取錯則每一條訊號斷言之 MESSAGE 與 segment
   皆錯。已納入強制判準。
2. **§2.2 範圍問題（Tier 3，要你裁）**：五個 `TLM_MANAGED_TIME_DATE_*`
   LID 在 **Atlantis High 欄無值**，只有 Atlantis(Mid) 欄有。
   而 framework 之 21 個可達章節中，`1.5.2.*` 整支是 LTM / Atlantis Mid。
   **即本 feature 有一部分 leaf 錨在 Atl-Mid 需求上。**
   017 / 020 之該類斷言：取 Atlantis 欄，或視為不適用於 Atl-H？
   這牽動 B3 批次之內容範圍。
3. **DR-6 可解除**（LID 表即 segment 之權威來源），但衍生 **DR-6b**
   —— 無 Atl-H 對應者之成因與 DR-6 不同，佔位字串須區分。
4. RD-1 Q-TM1–3 + N-TM1 仍待送出。

## 6. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| A-TM26 | anomaly，立即適用，強制判準 | §2 | ✅ T3 |
| DR-6 更新 + DR-6b | 缺件狀態變更與分項 | §3 | ✅ T2 |
| 六份素材登記 | RECEIVED | §1 | ✅ T1 + T2 |

分析層本包未動 git、未改任何腳本、未複製任何檔案（無該能力）。
§2 之探測跑在沙箱複本，T3 為對 `inputs/` 之重測。
