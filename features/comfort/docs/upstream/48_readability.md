# 48 — Comfort HMI / 行號雙層驗證、兩段式 PC、`spec-derived` 之弱量測

- 產出層：執行層｜2026-08-16｜對象：分析層
- 承接：下放包 70
- 結果：四項全數落實。`pc-line-numbering` 保留，**寫回後 assertion 增第 14 項**
  （J 欄行號連續，383 列 PASS）。兩段式格式寫入 profile §3.2.3，
  **21 行中 5 行採用**，逐條判定之理由見 §2.2；gate 之檢查對象改為 ` — ` 之前，
  **兩向 mutation 驗證：改逐字半 FAIL、改可讀半不 FAIL**。
  `spec-derived` 最短 20 行量測上線（列印不 FAIL），**其前 20 名全部逐一查核，
  無一為虛假對應**（§3.2）。標點嚴格性之預裁寫入 profile §3.2.3。
  lint **54/54 PASS，383 條**。ENTRY 019 已產出。

---

## 0. 下放包四項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | 保留 `pc-line-numbering`；寫回後 assertion 增行號連續一項 | ✅ §1 |
| 2 | profile §3.2.3 記兩段式格式，逐條判可讀性並回報採用清單 | ✅ §2 |
| 3 | 加 `spec-derived` 最短 20 行量測（列印，不 FAIL）| ✅ §3 —— **去重後為 20 種寫法，見 §3.1 之偏離** |
| 4 | 標點嚴格性之處置記入 profile §3.2.3 | ✅ §4 |
| — | 上繳 48 | 本件 |

---

## 1. 行號之雙層驗證

`pc-line-numbering`（JSON 層）保留。寫回後 assertion 增第 14 項：

```
- PASS — J 欄 pre_conditions 之行號自 1 起連續（70 §1）:
  expected `[]`, measured `[]` — 383 rows read back from the workbook
```

**為何同一項不變式驗兩次**：那五條之缺失在 JSON 與工作簿裡同時存在了兩輪
（ENTRY 016／017），**兩邊都沒有人出聲**。第一次驗的是我產出的資料，
**第二次讀的是客戶會讀的那一份** —— 兩者之間隔著 `xlsx_surgical` 之寫入路徑，
而那條路徑本身也可能出錯。

---

## 2. 兩段式 PC

### 2.1 格式與其可驗性

```
[spec-verbatim] <逐字片段> — <可讀之狀態句> (節次)
```

gate 檢查 ` — ` 之前；其後之狀態句不受檢查，**且不得引入條文未有之事實**
（§8.4.1 照舊）。

**反向驗證（實跑，兩向）**：

| 動 | 結果 |
|---|---|
| 改**逐字半**（`landscaped` → `landscape`）| **FAIL** — `is not a contiguous quotation of 17.4` |
| 改**可讀半**（`the vehicle has one of those screens` → `the vehicle under test has such a screen`）| **PASS** — 54/54 |

**兩向都測，才知道那條分界線落在正確的位置**：只測前者，會誤以為整行受檢；
只測後者，會誤以為整行不受檢。

### 2.2 逐條判定與採用清單（21 行）

| 採兩段式（**5 行**）| 節 | 逐字片段 | 判定理由 |
|---|---|---|---|
| `098` | 14.14 | `For vehicles with dual zone climate versions with dual airflow modes on 8.4", 10.1" Landscape, 10.25" and 12.3" radios` | 介系詞 `For` 起首，**無主謂結構**，單獨讀是條文片段 |
| `127-01`／`127-02` | 17.4 | `For 8.4/10.1/12 landscaped screens` | 同上 |
| `128-01`／`128-02` | 17.5 | `For dual zone climate with dual airflow modes equipped vehicles` | 同上 |

| 維持單段（**16 行**）| 逐字片段 | 判定理由 |
|---|---|---|
| `004-01`／`004-02` | `Some vehicles with dual zone climate … can have a configuration for dual AUTO modes` | 主詞 `Some vehicles` ＋ 動詞 `can have` |
| `007-01`／`007-02` | `Some vehicles have a configuration for a 3 state toggle recirc button: Auto, Manual, Open` | 主謂完整 |
| `040-01`…`043`（7 行）| `On some vehicles (See CFTS043 for details), there are additional Rear Climate controls and shortcuts` | 介系詞起首**但有 `there are` 之主謂**，可自成句 |
| `096-01`／`096-02`／`096-03` | `If the hard controls are knobs that turn`／`… are UP/DOWN toggles` | 條件子句，**本身即條件之標準形式** |
| `125-08` | `12' Portrait 50% widget also includes fan speed` | 主謂完整 |
| `126-02` | `On the 50% widget, these features are separated between driver and passenger` | 介系詞起首**但有主謂** |

> **分界不是「以什麼字起首」，是「有沒有主謂」** ——
> `On some vehicles …, there are …` 與 `On the 50% widget, these features are …`
> 都以介系詞起首而讀得通，`For 8.4/10.1/12 landscaped screens` 讀不通。

---

## 3. `spec-derived` 之最短量測

### 3.1 一處偏離（須報備）

70 §3 指示「列印最短之 20 **行**」。實作為**依 節×措辭 去重後之 20 種寫法**，
每種帶其列數（`×n`）與一個範例 tc_id。

**理由**：同一句排除式 PC 寫在數百列上（`16.2` 之 EMEA 排除 ×246、×96），
**逐行列印會讓 20 個名額被同一句話佔滿** —— 20 份同一個主張是一份清單。
去重後之 20 種涵蓋 9 個不同節、20 種不同措辭。

### 3.2 結果與逐項查核（**全部 20 種皆已核，無一虛假**）

| run | 節 | 措辭 | ×n | 該節是否確有對應（`[manual]` 查核）|
|---|---|---|---|---|
| 9 | 14.13 | The vehicle has a lower HVAC screen | 1 | ✅ `For vehicles with a lower hvac screen` |
| 9 | 2.14 | The climate system is MTC | 5 | ✅ `MTC screens/popups are to be used when CCM relays MTC functionality` |
| 9 | 2.7 | The front HVAC fan range … Off, 1-7 | 1 | ✅ `Fan ranges: Off, 1-7, 15h` |
| 10 | 16.2 | （非）EMEA ICS 車 | 246／96 | ✅ 該節即 ch16 之適用範圍句 |
| 10 | 3.2 | The vehicle is equipped with MAX A/C | 1 | ✅ `pressing MAX A/C turns MAX DEF off` —— **本項最值得查**：3.2 之主體是 MAX DEF，惟其末段確有 MAX A/C 之句 |
| 11 | 16.3／2.3 | ATC，AUTO 顯示 | 9／9 | ✅ `AUTO is not shown in MTC configurations` |
| 11 | 2.1 | 非僅前排氣候 | 52 | ✅ `If only Front climate is available … tabs will not be displayed` |
| 11 | 2.9 | 鏡面除霜可用 | 1 | ✅ `if this feature available` |
| 13 | 10.1 | EV 車，ECO HVAC | 15 | ✅ 該節即 ECO HVAC 之定義節 |
| 13 | 2.7 | 有風速硬控 | 2 | ✅ `hard control` 於該節出現 |
| 13 | 3.2 | 配備 MAX DEF | 30 | ✅ `On vehicles with MAX DEF` |
| 15 | 13.2／13.3／16.2／16.6／2.7 | 其餘五種 | 1–14 | ✅ 逐一命中（下螢幕、首次按壓、ATC／MTC 顯示、climate power 硬控）|
| 16 | 13.2 | 門板控制承載座椅鍵 | 10 | ✅ `pressed from the door control for lumbar & bolster` |

**結論：`spec-derived` 之低 run 全部來自「同義改寫」而非「無對應」。**
最低者 run=9，其對應仍明確 —— 這正是 70 §3 拒絕設門檻之理由：
**若以 run<10 為 FAIL，本輪會產生 7 個誤報與 0 個真陽性。**

---

## 4. 標點嚴格性之預裁已記入 profile §3.2.3

> 此類 FAIL 之正解為**改 PC 使其逐字**，**不得放寬 gate**。
> 理由同 R-C32；而此處連改判都不必：**gate 沒有錯，是引用不準。**

---

## 5. lint 與 §9 自評

```
54 / 54 gates PASS; 0 finding(s) across 383 TCs
```

寫回 assertion **14 項中 11 PASS、3 FAIL**（三者為範本容量，與 004～018 同源）。

TC **383**（不變）；leaf **378 / 403 ＝ 93.8%**（不變）；節 **123**（不變）。

**§9 十七項**：受影響者為 pre_conditions（項 3）之 5 行。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 3 | Pre-Condition | 變（5 行）| 兩段式（70 §2）；其逐字半未改一字，改的是其後所附之狀態句 |
| 其餘 | — | 不變 | |

ENTRY 019 已產出，標「範本容量待擴充」，**不送 Excel 四項確認**。

---

## 6. 「本包是否仍有該驗而未驗者」（R-C30）

1. **兩段式之「狀態句不得引入條文未有之事實」無機器檢查** ——
   `— the vehicle under test is such a vehicle` 這類回指句安全，
   但一句「— and the rear zone is enabled」會通過 gate 而違反 §8.4.1。
   現行三句皆為回指，**其安全性來自我怎麼寫，不來自檢查**。
2. **§2.2 之「有無主謂」由我判**，無機器判準；
   若日後有句子界於兩者之間（如 `When configured with X`），判定將再度靠讀。
3. **§3.2 之查核為 `[manual]` 之關鍵詞比對**，不是語意驗證：
   我確認了「該節提到那件事」，未確認「該節所說的正是這條 PC 所斷言的」。
4. **`spec-derived` 量測只涵蓋 PC 行**；`test-setup` 之對應性從未量過
   （其本就不出自條文，惟其中若混入應為 `spec-derived` 者，無人會發現）。
5. **寫回 assertion 之新項只驗行號，不驗行內容**與 JSON 是否一致 ——
   後者由既有第 4 項（14 欄逐格比對）涵蓋，惟 J 欄之**換行結構**兩者皆未逐字比。

---

## 7. 待分析層

1. **§6.1** —— 兩段式之狀態句是否需一道弱檢查（例如禁止其含條文未有之
   名詞），或維持人寫人讀。
2. **§3.1 之偏離**（去重後 20 種而非 20 行）請追認。
3. **§6.4** —— `test-setup` 是否值得同樣的最短量測，以發現「其實有出處卻
   標成 test-setup」之行。
4. **剩餘 25 個停下之 leaf** 分佈不變；依 70 §7 之預告，
   本層可隨時依指示彙整 RD-1 送件清單（逐項具名節次、所缺之物、
   其阻塞之 DR、得答覆後之處置）。
