# 26 — Comfort HMI / R-C36・R-C37、移除 5 條過嚴 PC、第十四軸、單一來源

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 37
- 結果：5 條之 EMEA 排除式 PC 與 `16.2` 引用**已移除**；第十四軸增列，
  `2.7.1` 生成（`-065`）；`INTERFACE_AXIS_REVIEW` 抽為單一 TSV 且
  **抽出前後 19 檔逐位元組相同**；sibling 候選產生器**首次執行即找到
  三對未登記之 sibling**。lint **40/40 PASS，0 finding，65 條**。
  **未寫回、未開新批。**

---

## 1. R-C36、R-C37 貼入

`RULINGS.md` 現有 **39 個**逐字條文區塊。兩條各附來源說明。

---

## 2. 5 條過嚴之 EMEA 排除式 PC —— 已移除

| tc_id | 節 | 移除後之 `specification_reference` |
|---|---|---|
| `-015`／`-016`／`-017` | 3.1 | `3.1; 2.14` |
| `-031` | 3.4 | `3.4; 2.14` |
| `-041` | 2.1 | `2.1; 2.14; 6.3` |

**其餘維持**：全 65 條中現有 **45 條**帶 EMEA 排除式 PC，
**45 條**帶 `16.2` 引用 —— 兩數相同，證明該引用與該 PC **一對一**，
無殘留（引用之唯一理由即該 PC）。

移除係以節級開關實作（`NO_CH16_COUNTERPART = {"2.1","3.1","3.4"}`），
非逐條手改 —— 日後鏡射表若再改判，改一處即可。

`reasoning` 逐節記其依據，例如 3.1：

> **EMEA ICS 排除式 PC 已依 37 §1 移除** —— `ch16_mirror_map.tsv` 判 3.1 為
> no-counterpart（16.12 ICE11 為 5 states 單選，非 tri-mode 之三鍵組合），
> 原排除建立在「ch2／ch3 於 ch16 有對應」此一對本節為假之前提上。

`data/interface_axis_review.tsv` 之 `emea_ics` 欄同步更新為移除後之判定。

### 2.1 `3.3` 之 `partial` 依 R-C36 逐條判定 —— 排除**成立**，維持

`-029`／`-030` 之可觀察行為為「climate off 期間 MAX DEF／REAR DEF 之
可用性」，而 16.10 ICE9 明寫

> grey out remaining buttons **except for Front/Max defrost and rear defrost**

—— **落在 ch16 涵蓋之那一部分**，故排除式 PC 成立。判定與理由已寫入
`interface_axis_review` 之 `emea_ics` 欄，非僅存於本上繳包。

---

## 3. `ch16_mirror_map.tsv` —— `partial` 八列增分界欄

新增第五欄 `涵蓋與未涵蓋之行為分界`，**八個 `partial` 列全數填妥**
（實測未填 0）。非 `partial` 列留空。

例（`16.4 ↔ 2.5`）：

> 涵蓋：RECIRC 之 on/off 狀態。未涵蓋：C4 之可用性灰化
> （`gray out when recirc availability status from CCM denotes that`）
> 與 recirc 可自動開啟 AC

**`Climate Modes` 與 `Airflow and Defrost` 生成前所需之五節
（2.4／2.5／2.8／2.9／2.13）分界已備妥**，屆時 R-C36 之逐條判定有可引之
依據，不需重讀 ch16。

---

## 4. 第十四軸 ＋ `2.7.1` 生成

profile §3.2 增第十四軸「前排 HVAC 風速範圍」，值 `Off, 1-7`（2.7 `C6.`）／
`Off, 1-8`（2.7.1 `C6.1`），**功能型**，逐軸類別表同步增列。
另附引用段記「兩值分屬兩節而非推論補齊」與「既有影響 0 條」。

**`-065`** 生成（`SWE1-HVAC-011`，`Temperature and Fan` 19/19 完成）：

| 欄 | 值 |
|---|---|
| tc_title | `Front HVAC fan range runs to 8 on vehicles configured for it`（12 字）|
| PC | 1 `[spec-verbatim] The vehicle's front hvac fan speed range is Off, 1-8 (2.7.1)`；2 第十三軸排除；3 EMEA 排除 |
| spec_ref | `2.7.1; 2.7; 2.14; 16.2` |
| design_method | 邊界值分析（上界）|

`2.7` 依 R-C29 併入 spec_ref —— 其為 `1-7` 對照值之出處。

**`WITHHELD` 現為空集合**，`Temperature and Fan` 無停下項。

---

## 5. `INTERFACE_AXIS_REVIEW` 抽為單一來源 —— 驗畢

`data/interface_axis_review.tsv`（20 節），四個 generator 由該檔讀入。
實測 `INTERFACE_AXIS_REVIEW = {` 之字面定義現為 **0 份**。

### 5.1 逐位元組驗證 —— 且我第一次驗錯了

**第一次比對報 19 檔全數 DIFF。** 追查後：基準目錄 `/tmp/base` **是一個
既存的檔案而非目錄**（`-rw------- 1179 bytes`），`mkdir` 失敗、`cp` 未成，
`cmp` 遂與不存在的檔案比對而全報差異。

**基準根本沒被建立，那 19 個 DIFF 是假的。**

改用 scratchpad 重做，並以**抽出前之字面值**重建 before：

1. 現行（讀 TSV）之輸出存為 `after/`
2. 四個 generator 暫時還原為字面值版，重跑，輸出存為 `before/`
3. 還原為 TSV 版
4. `cmp` 逐檔比對

```
PASS — 19 檔 / 64 條逐位元組相同
```

**若我只看第一次的輸出就回報，會得出「抽出改變了內容」這個假結論，
而且方向恰好相反 —— 它會讓我去找一個不存在的 bug。**
一個失敗的比對，其失敗原因可能在比對本身。

---

## 6. sibling 候選產生器 —— 首次執行即找到三對

`scripts/sibling_candidates.py` ＋ `data/pending_sibling.tsv`。

方法：**不同 Test Set** 之節對，其 `full_text` 共有至少一個條文自有之
大寫語彙。`--for "<Test Set>"` 用於某組完成之日。

### 6.1 對 `Temperature and Fan` 執行之結果

候選 5 對，**已判 1、未判 4**。逐項判定並入表：

| 節對 | 判定 | 理由 |
|---|---|---|
| `2.6` ↔ **`7.4`** | **sibling** | **新發現。** CR4 逐句重述 C5 之溫度區間、HI/LO 取代度數、Metric 半度增量，及 temp slider／status bar／temp popup 之一致性 |
| `2.6.1` ↔ **`7.4`** | **sibling** | **新發現。** CR4 亦逐句重述 C5.1 之箭頭 1 增量、長按快移、滑桿把手判定與 SYNC 連動 |
| `2.6.1` ↔ **`7.7`** | **sibling** | CR7 述 SYNC 並擴及後排（`Fan speed and blower are sync'd front to back`）|
| `2.6.1` ↔ `2.11` | sibling | 既有 |
| `2.6.1` ↔ `16.6.1` | **not-sibling** | 鏡射關係而非 §4.6 sibling —— 兩者不會同時出現於同一車輛 |
| `2.6.1` ↔ `16.11` | **not-sibling** | 同上；語彙重疊來自 `SYNC` 一詞 |

`PENDING_SIBLING` 由 1 對增為 **4 對**，gate 改為讀該 TSV，
故表與 gate 為單一來源。

### 6.2 `7.4` 這一對值得單獨說

`7.4`（CR4，`Rear Climate`）**逐句重述** 2.6 與 2.6.1 之規則，
差異軸為**前排 vs 後排 climate screen**。而它另含一項實質差異：

> CR4：`long press = fast move ((hold longer that **500 ms**))`
> C5.1：`Long press = fast move`（**無門檻**）

**同一行為在兩節有不同的具體程度，而只有一節給了數值。**
`-055`（`-009-04`，長按快移）之 ER 現為「The temperature changes with a
fast move」，未寫入門檻 —— 依 R-C22 正確；但若 500 ms 亦適用於前排，
該 ER 可以更具體。**已入表，待 `Rear Climate` 生成時依 §4.6 一併判定。**

### 6.3 不完整性之明示（R-C37）

產生器每次執行印出：

```
!! NOT a completeness proof (R-C37): this list comes from lexical overlap
!! and cannot surface a sibling pair that shares none of the vocabulary
!! above. A clean run means 'no candidate by this method', never 'no
!! siblings remain'.
```

lint 亦增一行具名回報：

```
- PASS — the pending-sibling table is produced by lexical overlap and is NOT
  a completeness proof (R-C37); run scripts/sibling_candidates.py when a
  Test Set completes
```

**排除之語彙亦具名而非靜默丟棄**：`AUTO`／`FAN`／`HI`／`HVAC`／`LO`／
`MODE`／`TEMPERATURE` 七詞因配對率過高而排除，每次執行印出該清單。

### 6.4 `reviewed_at`

表內每列記 `reviewed_at = 129`（覆核當時之全 feature 節數），
使「這張表在哪一輪被覆核過」由檔案可答。

---

## 7. `A-CF13` 第一項增記復現

`2.15` 與 `16.17` 之 `C16.` 撞號**已為 A-CF13 第一項**（下放包 20 登記），
本輪由鏡射表獨立再撞。**未新登 anomaly**，於該項增記：

> **復現本身是證據**：同一撞號在**兩條不相干的作業路徑**上各被撞一次
> ——第一次由 Layer 3 map 之標籤掃描，第二次由 ch16 鏡射之逐節比對。
> 表示它不是邊緣情形，Phase 4 全面展開時會反覆出現。

並記候選 gate 之不加理由：**實測 65 條之 `specification_reference` 皆為
`{STEM}_{outline}` 形式，無一以條款標籤為引用鍵**，故加 gate 即為對尚未
發生之事設檢查。

---

## 8. `RUNBOOK.md` —— 「答了」不等於「答對了」

逐字記入 §8 末項之自陳，並加一段推論：

> 凡「記錄一個判斷」型的 gate，其綠燈只證明欄位被填了。
> 要驗答案本身，需要的是**另一份獨立導出的資料**（此處即鏡射表），
> 而不是更嚴的欄位檢查。

同源標註：R-C23、`axis-value-count`（驗登記而非驗判斷）。

---

## 9. lint 與 §9 自評（僅變動項，依 R-C23）

```
40 / 40 gates PASS; 0 finding(s) across 65 TCs
```

四個 generator 連續重跑，輸出不變。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 3 | PC | **變** | 5 條各減一行（EMEA 排除）；`-065` 新增 3 行。實測 PC 內無動作動詞 → 0 命中 |
| 12 | 溯源、§8.2.1 | **變** | `-065` 之 `req_id` 於 037 存在（`SWE1-HVAC-011`）；引 2.7 之 `1-7` 作對照而不驗 2.7 之行為（2.7 之五條各自成條）|
| 16 | `specification_reference` | **變** | 5 條各移除 `16.2`；`-065` 為四節。實測「帶 EMEA PC 之條數」與「帶 16.2 引用之條數」皆 45，**一對一無殘留** |
| 2 | tc_title | **變**（`-065`）| 12 字，token `Front HVAC fan range` 與同節其他條互斥 |
| 13 | design_method | **變**（`-065`）| 邊界值分析 —— 驗上界為 8，procedure 為「升至不再增加」，形狀即 BVA |
| 10 | ER 可觀察 | **變**（`-065`）| **依 R-C23 明說：依據不是 `er-subject-net`**。三行 ER 主詞為 `The climate screen`／`The fan speed`，皆系統側 |

其餘 11 項未變。

---

## 10. 進度

| | 數 |
|---|---|
| 驗證單位（leaf）| 403 |
| 已生成（leaf）| **61** |
| 已生成（TC）| **65** |
| 阻塞（leaf）| 2（DR #17／#20 之 2.1-01／-02）|
| 未開始（leaf）| 340 |

Test Set：`Seat Control Tab` 14/14、`Tri-Mode Climate` 14/14、
**`Temperature and Fan` 19/19（本輪完成）**、`Front Climate Anatomy` 14/16。

---

## 11. 「本包是否仍有該驗而未驗者」

依 R-C30。

1. **鏡射表之 `mirrored` 十五列，我未逐列複核其「涵蓋是否真的完整」。**
   `partial` 之八列已填分界，`mirrored` 則預設為「全涵蓋」。
   **搜尋範圍**：建表時逐節通讀，但比對之粒度為**首句與主要規則**，
   非逐句。若某 `mirrored` 節其實只涵蓋九成，它應為 `partial` 而現在不是
   —— 而 R-C36 只對 `partial` 要求 TC 層判定。**`mirrored` 是本表現在
   最弱的一格。**
2. **`7.4` 之 `500 ms` 門檻（§6.2）目前只入表未處置。**
   `-055` 之 ER 是否應寫入該門檻，要到 `Rear Climate` 生成時才判。
   **在那之前，該 TC 之 ER 比條文所能支持的更弱。**
3. **候選產生器只跑了 `--for "Temperature and Fan"`。**
   `Seat Control Tab`／`Tri-Mode Climate`／`Front Climate Anatomy`
   三組**已完成而未跑過該產生器** —— 它是本輪才做出來的。
   **搜尋範圍**：僅 `Temperature and Fan` 之一側。
   三組之候選未產生，**故「無其他 sibling」這句話對它們不成立**。
   建議下輪對三組各跑一次，本包未做（作業量已足一輪，37 §9 亦如此界定）。
4. **`sibling_candidates.py` 之 Test Set 解析**由 `framework.md` 之表格
   正規表示式讀出，含 `7.1 ~ 7.10` 型區間之展開。實測 129 節皆解析到組別
   （無空字串），但**該解析未經反向驗證** —— 若某節解析錯組，
   跨組判定即失效而無人知。
5. **第十四軸之「既有影響 0 條」係上一輪之實測**，本輪未重測。
   本輪新增之 `-065` 自身即該軸之使用者，其餘 64 條未變，故結論仍成立
   —— 但這是推論，不是重測。

---

## 12. 建議 commit message（git 未執行）

```
fix(comfort): drop 5 over-strict EMEA PCs; add axis 14; single-source tables

- add R-C36 (partial mirrors are judged per TC) and R-C37 (a universal
  claim needs samples from the negative side) to RULINGS
- remove the EMEA exclusion and its 16.2 citation from -015..-017, -031
  and -041; 45 TCs keep both, one-to-one with no residue
- 3.3's partial resolved per R-C36: ICE9 covers it, exclusion stands
- ch16_mirror_map: coverage-boundary column filled for all 8 partial rows
- profile: fourteenth axis (front HVAC fan range), function-type
- generate 2.7.1 as -065; Temperature and Fan now 19/19
- extract interface_axis_review to one TSV; before/after byte-identical
  across 19 files (the first comparison was itself broken — /tmp/base was
  a file, not a directory)
- add sibling_candidates.py and pending_sibling.tsv with reviewed_at; the
  first run found 2.6/2.6.1 <-> 7.4 and 2.6.1 <-> 7.7
- A-CF13 item one: record the independent recurrence via the mirror map
- lint 40/40 PASS, 0 findings across 65 TCs
```

---

## 13. 待分析層

1. **§11.1** —— `mirrored` 十五列是否須逐句複核（現為本表最弱處）。
2. **§11.3** —— 其餘三組是否須各跑一次候選產生器。
3. **§6.2** —— `7.4` 之 `500 ms` 是否適用於前排（影響 `-055` 之 ER）。
4. **§11.4** —— `sibling_candidates.py` 之組別解析是否須反向驗證。
