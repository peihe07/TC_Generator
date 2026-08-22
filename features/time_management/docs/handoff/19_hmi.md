# 下放包 19 — HMI Settings List R1L-R (2026-02-13) 之比對

分析層 → 執行層。往返編號 `19`。對應上繳 `docs/upstream/19_hmi.md`。

Pei 提供 `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx`。
**Spec Release 欄逐字為 `R1L-R`，日期 2026-02-13** ——
較先前所用之 `R1 SR24 Post 2A (June 15 2023)` 新兩年半，且為 R1L-R 專屬。

---

## 1. 五個已寫入之 UI 標籤 —— **全部未變**

B1–B3 之 49 條 TC 使用之標籤，逐字比對新版 §7 Clock：

| 已寫入 | 新版 (2026-02-13) | 判定 |
|---|---|---|
| `Clock`（設定頁） | §7 標題 `7. Clock` | 相符（惟見 §3）|
| `Sync Time with GPS` | 7-1，On/Off Checkbox，Technical Ref `CFTS015` | **逐字相符** |
| `Set Time Hours` | 7-2，`-/+ selector with value in middle` | **逐字相符** |
| `Set Time Minutes` | 7-3，`-/+ selector`，Options `00-59` | **逐字相符** |
| `Time Format` | 7-4，`2 radio buttons`，Options `12 hrs , 24 hrs` | **逐字相符** |

**B1–B3 之標籤無須改寫。** 先前之疑慮（舊版標籤可能已過時）解除。

### 1.1 附帶取得之值域（先前為自擬或無來源者）

| 項 | 新版之 Options 欄逐字 | 影響 |
|---|---|---|
| `Set Time Hours` | `1-12 (12 hr)` / `00-23 (24hr)` | B1 TC#2 用 23:59 為 BVA 上界 —— **與此相符**，且現在有來源 |
| `Set Time Minutes` | `00-59` | 同上 |
| `Time Format` | `12 hrs , 24 hrs` | **011 之選項值有來源了**（B3 曾自 LID 表 Format 欄取 `FORMAT_24H`，那是訊號值不是 UI 值，兩者不同）|

**`Greys out with sync option selected`** 於 7-2 與 7-3 皆有 ——
B1 TC#3 之 ER（greyed out）之來源自此確認，且**兩項各自獨立標註**，
非單一註記涵蓋兩者。

## 2. **DR-12 解除**

先前無來源之「HU 時鐘顯示開關」，新版為：

```
7-5  Show Time in Status Bar | On/Off Checkbox | CFTS015
     Info Popup: Displays the digital clock in the status bar.
```

**DR-12 之 1 處佔位改為真值 `"Show Time in Status Bar"`。**

**另有兩項相近但屬他 CFTS，不得混用**：

```
7-7  Show Time During Screen Off            | CFTS022
7-7  Show Time and Date During Screen Off   | CFTS022
```

**Technical Reference 為 CFTS022 非 CFTS015** —— 依 §8.4.2，
螢幕關閉時之時鐘顯示屬 CFTS022 之範圍，**本 feature 不得測**。
此二項登記為範圍外，不寫入任何 TC。

## 3. **新問題：設定頁名可能不是 `Clock`**

§7 之標題列附註逐字：

```
when Set Date setting is implemented, rename settings section from "Clock" to, "Clock & Date"
```

而**同一份文件之 7-6 即為 `Set Date`**（且有三種區域排序，見 §4）。
即該條件之前件在本版已成立。

**故設定頁名為 `Clock` 或 `Clock & Date` 取決於「Set Date 是否實作」**，
而該註記本身未說明其於 R1L-R 是否已實作 —— 只說「實作時改名」。

**影響**：B1–B3 之 49 條中，凡 `Open the "Clock" settings` 者皆受影響
（B1 至少 6 條）。

```
A-TM28（PENDING，Tier 2 —— 呈 Pei）

HMI Settings List R1L-R (2026-02-13) §7 之標題附註：
`when Set Date setting is implemented, rename settings section from
"Clock" to, "Clock & Date"`。

同文件 7-6 即為 `Set Date`（三種區域排序皆列出），前件似已成立，
但該註記未言明 R1L-R 是否已實作。

**兩種讀法**：
(a) 該註記為給 HMI 團隊之施工指示，文件本身尚未改名 → 頁名為 `Clock`
(b) Set Date 既已列入本版，改名條件成立 → 頁名應為 `Clock & Date`

**分析層不裁**：此為 UI 事實，須由能看到實機或 HMI 團隊者確認。
B1–B3 現寫 `Clock`（依 §7 標題字面），若應為 `Clock & Date`，
至少 6 條之 procedure 與 ER 須改。

**登記為 DR-12b**，Urgency High —— 其成本隨 TC 數增加，
寫回後改動成本更高（R-TM64 同一考量）。
```

## 4. **B4 之 015 現有完整來源 —— 且日期格式有三種區域變體**

B4 之 015（Manual Date Handling）先前無 UI 標籤來源。新版 7-6 提供：

```
7-6    Set Date (DD/MM/YY)  |  >  | CFTS015 | "(DD/MM/YY)" 為動態，隨當前日期更新
7-6.1  Set Date Day    | -/+ selector | 1-31  | CFTS015
7-6.2  Set Date Month  | -/+ selector | 1-12  | CFTS015
7-6.3  Set Date Year   | -/+ selector |       | CFTS015

同節另列兩種排序：
  Set Date (MM/DD/YY) —— 子項序為 Month, Day, Year
  Set Date (YY/MM/DD) —— 子項序為 Year, Month, Day
```

**三種排序為區域變體**（對應 CFTS015 4814005 之
`The HU shall implement the date format based on the PROXI parameter
$Country_Code$`，並指向 R1 Market Configuration Table）。

**B4 生成時之要求**：

1. 標籤用 `Set Date Day` / `Set Date Month` / `Set Date Year`（逐字）
2. **父項名依區域而異** —— 不得寫死其一。三種皆為合法值，
   TC 若不限定區域，父項寫 `Set Date`（不含括號之格式標示）；
   若限定區域，則加 Pre-Condition 之 `$Country_Code$` 條件並用對應排序
3. **子項之順序隨父項而異**，procedure 之步驟序須與所選排序一致
4. 另有註記 `Set Date is only shown for vehicles in which the cluster does
   not have data needed to…`（截斷）—— **完整文字須執行層讀出**，
   其可能是 015 之一項顯示前提

## 5. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — 素材落地

新版 HMI Settings List 複製進 `inputs/`（分析層無使用者端複製能力）：

```bash
# 來源路徑請 Pei 提供；分析層僅見沙箱複本
cp "<來源>/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx" \
   features/time_management/inputs/
```

**舊版（SR24 2023）若在 `inputs/` 內，不刪除**，改於
`DATA_REQUESTS.md` 標為 SUPERSEDED 並註明取代者（R-TM13）。

### T2 — `DATA_REQUESTS.md`

- **DR-12 → RESOLVED**，值為 `Show Time in Status Bar`（7-5，CFTS015）
- **新增 DR-12b**（§3），Urgency High
- 舊版 HMI Settings List 標 SUPERSEDED

### T3 — `ANOMALIES.md`：新增 A-TM28（§3）

### T4 — B1–B3 之一處修正

DR-12 之 1 處佔位（B1 007 之 HU 時鐘顯示開關）改為
`"Show Time in Status Bar"`，並於 reasoning 註明來源
（HMI Settings List R1L-R 2026-02-13 §7-5）。

**`Clock` 之頁名不動** —— 待 A-TM28 裁定（§3）。

### T5 — 逐字複驗（**對 `inputs/` 之檔案，非沙箱複本**）

分析層之 §1–§4 全部跑在 Pei 上傳之沙箱複本。**執行層須對 `inputs/`
之檔案重測**，逐項對差：

1. §1 之五個標籤逐字相符
2. §1.1 之三組值域
3. §2 之 7-5 與兩個 CFTS022 項
4. §3 之標題附註全文
5. §4 之三種排序與其子項序
6. **§4(4) 之截斷註記全文**（`Set Date is only shown for vehicles…`）

**任一不符即回報並停。**

### T6 — 上繳

`docs/upstream/19_hmi.md`。**依 R-TM74 列逐 T 對照表。**

### 不得執行者

- 不動 git；不寫回工作簿
- **不改 `Clock` 之頁名**（待 A-TM28）
- **不寫入 CFTS022 之兩項**（§2，範圍外）
- 不刪除舊版 HMI Settings List
- 不碰 `features/vehicle_setting/`

---

## 6. 呈報 Pei

**這份文件之價值高於預期**：解掉 DR-12、確認五個標籤未變（先前之疑慮解除）、
補上 B4 之 015 全部所需標籤與值域。

**但翻出一個新問題（A-TM28）**：§7 標題附註說「Set Date 實作時，
把 `Clock` 改名為 `Clock & Date`」，而同一份文件裡 Set Date 已列入 ——
**前件似已成立，但文件本身仍寫 `Clock`。**

這需要能看到實機或問 HMI 團隊的人確認。**B1–B3 至少 6 條寫了
`Open the "Clock" settings`，寫回後再改成本更高。**

另請留意 §2：`Show Time During Screen Off` 之 Technical Reference 是
**CFTS022 不是 CFTS015** —— 那是別的 feature 的範圍，我方不測。
這類「看起來相關但屬他 CFTS」的項目，是 §8.4.2 最容易被誤收的形態。

## 7. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| A-TM28 | anomaly，PENDING，Tier 2 | §3 | ✅ T3 |
| DR-12 → RESOLVED | 缺件解除 | §2 | ✅ T2 + T4 |
| DR-12b | 新缺件 | §3 | ✅ T2 |

分析層本包未動 git、未改任何腳本、未改任何 TC。
§1–§4 之比對跑在沙箱複本，T5 為對 `inputs/` 之重測。
