# 上繳包 14 — pilot rev4 ＋ 寫回 dry-run（未執行 splice）

執行層 → 分析層。2026-08-15。回應下放包 `22_rev3_review.md` §5。

**結論：八項作業全部完成。lint 31 → 32 gate，全 PASS。
dry-run 報告已產，未呼叫寫入路徑、未產新檔、`DELIVERY.sha256` 未增列。**

---

## 0. 置頂

| # | 事項 |
|---|---|
| **甲** | **R-C25 首次全批適用：機械掃描命中 4 條，套用兩問測試後只有 1 條為真** —— 即 22 §1 已裁之 TC-014。另 3 條（001／003／007）經逐條判定**落點確在 pre_conditions**，不改。掃描是詞彙型工具，**它產生的是候選不是結論** |
| **乙** | **dry-run 發現一項寫回前必須知道的事：14 列全部 `customHeight=True, height=14.0`（單行）** —— 與 `wrapText=True` 併用時 Excel 折行但列不長高。內容完整，但**列表視圖只見首行**；估算需 9–23 行。兩個 BLOCKED row 之 Remarks（216／226 字元）僅可見 `[BLOCKED-SPEC] Long-press logic is…` |
| **丙** | 該列高**非本 pipeline 所設** —— 範本 `SWQT_20260121` 原本即如此，A-CF07 之清列只動五格值未動列高。故任何處置都是**對範本呈現之改動**，屬 Tier 2 |

---

## 1. R-C25／R-C26 貼入 ＋ TC-014 修正

`RULINGS.md` 現載 **R-C1 ~ R-C26 + R-C4-1 + R-C5-1**，共 **28 條**。

TC-014 之 PC3（`The lumbar/bolster level is already at its maximum`）已刪，
**procedure 與 ER 未動**（22 §5.2）。PC 由 4 行降為 3 行。

生成器內留註解記其判定路徑，使下一個讀者不必回查往返包：

```python
# R-C25: PC3 qualified under §8.5 (13.6's trigger IS the at-maximum state)
# but its 落點 is the procedure — step 1 must establish that state anyway
# (§7 FF: include setup, don't assume hidden state), so §4.5 puts the fact
# there and not in pre_conditions as well. Qualification != placement.
```

---

## 2. 甲 —— R-C25 之首次全批適用

### 2.1 掃描方法

對 12 條非 BLOCKED row（BLOCKED row 無 procedure，不適用），逐一比對每個
`pre_conditions` 行與每個 `test_procedure`／`expected_result` 行之實詞重疊
（去除停用字、source class 標籤、節次括號）。**判為候選之門檻**：
共同實詞 ≥ 3 且佔該 PC 行之 ≥ 55%。

### 2.2 命中 4 條（5 對），逐條套用兩問測試

R-C25 之判定順序：**先問資格（§8.5：是不是 spec trigger），
再問落點（§7／§4.5：誰建立它）。**

| # | TC | PC 行 | 對應行 | 重疊 | 資格 | 落點 | 判定 |
|---|---|---|---|---|---|---|---|
| 1 | **014** | `The lumbar/bolster level is already at its maximum` | ER1 `The lumbar/bolster is at its maximum level`／ER2 | 75% | ✅ spec trigger（13.6 之行為即「到達上限後再按」） | **procedure** —— 步驟 1 `Press "+" repeatedly until it stops increasing` **必須**建立該狀態（§7 FF） | **刪 PC3** ✅ |
| 2 | 001 | `The lower screen is not in the stowed position` | ER1 `The tab shown on the lower screen is not the Seats tab` | 60% | ✅ | **pre_conditions** —— procedure 未建立收合狀態；步驟只有「記錄目前分頁」與「按 `"-"`」 | **不改** |
| 3 | 003 | `The user is already in the climate section on the main head unit` | proc 1 `Note which tab is currently shown in the climate section on the head unit` | 57% | ✅ | **pre_conditions** —— 步驟 1 是**在該區段內觀察**，預設使用者已在該處，不建立它 | **不改** |
| 4 | 007 | `A lumbar/bolster adjustment type is currently the selected option` | proc 1 `Record which lumbar/bolster adjustment type is the selected option` | 83% | ✅ | **pre_conditions** —— 步驟 1 **記錄**而非建立；四種類型中恆有一個為選定項，無需步驟建立 | **不改** |

**結論：檢出 4 條，實際須改 1 條（TC-014），另 3 條經判定不改。**

### 2.3 為什麼三條是誤報 —— 這件事本身值得記

三個誤報之成因各不相同：

- **001**：兩個句子共用「lower screen / not」三個詞，但**陳述的是不同的事**
  （螢幕之收合狀態 vs 螢幕上顯示哪個分頁）。純粹是詞彙碰撞。
- **003**：重疊詞是**觀察發生的地點**（climate section on the head unit），
  不是被斷言的事實。PC 斷言「使用者在那裡」，步驟斷言「那裡顯示什麼」。
- **007**：**最接近真陽性**。83% 重疊，且兩句主詞相同。區別在
  **存在 vs 身分**：PC 說「有一個選定項」，步驟說「記下是哪一個」。
  若步驟改為「選擇 Back Bolster」（建立），落點才會移到 procedure。

**掃描門檻調高不能解決 007，調低會漏掉 014** —— 詞彙重疊與「同一事實」
之間沒有可靠的閾值。R-C25 之兩問測試是判準，掃描只負責產生候選；
兩者分工正如 22 §4 所記之「判準 vs 用詞禁令」。

---

## 3. `marker-whitelist` gate（R-C26）

白名單取 profile §5.1 之具名二列：`NR1L-ComfortHMI-010`、
`NR1L-ComfortHMI-012`，寫死於 lint 並附註「增列須經裁定」。

lint 現輸出兩行豁免相關資訊，皆為具名回報而非靜默：

```
- PASS — rows exempted as BLOCKED-SPEC (proc-min-steps, proc-er-1to1):
         ['NR1L-ComfortHMI-010', 'NR1L-ComfortHMI-012']
- PASS — marker whitelist (profile §5.1):
         ['NR1L-ComfortHMI-010', 'NR1L-ComfortHMI-012']
```

**反向驗證**：對未列白名單之 `NR1L-ComfortHMI-004` 掛上 `[BLOCKED-SPEC]`
並清空其 procedure／ER：

```
[FAIL] marker-whitelist: NR1L-ComfortHMI-004: carries [BLOCKED-SPEC] but is
       not in profile §5.1's named whitelist; an exemption-granting marker
       cannot be self-issued (R-C26)
```

**且豁免回報行同時顯示 `['NR1L-ComfortHMI-004', ...]`** —— 即該列確實取得了
豁免（proc-min-steps 未對它報錯），但 `marker-whitelist` 攔下它。
**兩道機制各司其職**：R-C24 使豁免可見，R-C26 使豁免不可自取。
還原後回到 32/32。

---

## 4. RUNBOOK 已記「判準 vs 用詞禁令」（22 §4）

連同兩條實務推論一併寫入：

1. **寫 gate 時先問它檢查的是表徵還是判準** —— 檢查表徵者能擋住重複同一個
   字面錯誤，擋不住同一個判斷錯誤換個寫法
2. **改動點不等於審視點** —— rev2 親手改過的 ER 仍帶 `is recorded`；
   TC-014 之 PC 區塊因 rev2／rev3 皆未改動而三輪未被重讀。
   前者是「改過所以以為看過」，後者是「沒改過所以沒看」

22 §1.2 把這兩者並列為互為佐證，我接受該歸納 —— 它們是同一個盲點的兩面。

---

## 5. 寫回 dry-run 報告（未執行 splice）

## A. 目標列範圍

- workbook：`output/…_Comfort_20260815_prepared.xlsx`（A-CF07 已清列，Pei 已確認）
- 工作表：`Test Case Specification 測試用例規範` · header row 9
- 模式：**BLANK — append from first data row**（profile §0.1）
- 首列 **row 10**；14 條佔 **row 10 – row 23**
- B 欄公式 `=IF(ISBLANK($D{r}),"",ROW()-9)` 自動編號 1–14，**不寫入**

## B. 每欄之填入值

| 欄 | header | 來源欄位 | 14 列之值 |
|---|---|---|---|
| D | Requirement or Design ID 需 | `req_id` | 逐列不同（14 個相異值） |
| F | Test Case ID 測試用例ID | `tc_id` | 逐列不同（14 個相異值） |
| G | Test Group 測試組 | `test_group` | 全列相同：`Comfort` |
| H | Test Set 測試集 | `test_set` | 全列相同：`Seat Control Tab` |
| I | Test Item 測試項目 | `test_item` | 逐列不同（14 個相異值） |
| J | Pre-Conditions 先前條件 | `pre_conditions` | 逐列不同（12 個相異值） |
| K | Input Test Data 輸入條件 | `input_test_data` | 全列相同：`NA` |
| L | Test procedure 測試程序 | `test_procedure` | 逐列不同；**2 列為空**（BLOCKED row） |
| M | Expected Result 預期結果 | `expected_result` | 逐列不同；**2 列為空**（BLOCKED row） |
| N | Specification Reference 規格 | `specification_reference` | 逐列不同（7 個相異值） |
| P | Test Case Priority 測試用例優先級 | `priority` | 逐列不同（2 個相異值） |
| R | Test Case Design Methods 測 | `design_method` | 逐列不同（4 個相異值） |
| S | Functional Safety 功能安全 | `functional_safety` | 全列相同：`NA` |
| AH | Remarks 備註 | `remarks` | 12 列空字串；**2 列 `[BLOCKED-SPEC]…`** |

## C. 留白欄之具名清單

- **B** No.# 序號 —— 範本公式自動編號 —— 不寫入（profile §0.1：清 B 會刪掉編號機制）
- **C** Requirement or Design ID (Pola —— Requirement or Design ID (Polarion) —— 本 feature 無 Polarion id 對應
- **E** Test Case ID (TestRail) 測試用例 I —— Test Case ID (TestRail) —— 無 TestRail 對應
- **O** Test Case Reference ID 測項參考ID —— Test Case Reference ID —— BLANK 工作簿無既有序列可續（feature.yaml tc_ref_id_value=NEW，本批不填）
- **Q** Estimated Test Time (mins) 預估測 —— Estimated Test Time —— `UNRULED_BLANK`（profile §3.7）
- **T** HDCC27 Atl-Hi —— Vehicle Model 起始欄 —— 一律留白（profile §3.9 / Privacy R30-4）
- **T–Z**（7 欄）—— Vehicle Model 全區留白；**A-PV15 適用**：範本止於 27 世代，本專案為 HDCC28，不得對映
- **AB–AG** —— 測試執行結果欄（test_version/vehicle/period/tester/result/defect_id），生成階段不填

## D. BLOCKED row 兩列於 xlsx 之呈現（§9.2 第 1 項）

### D.1 樣式探測 —— 讀範本 row 10 之既有格式，不寫入

| 欄 | wrap_text | vertical | 欄寬 |
|---|---|---|---|
| I | `True` | `center` | 16.5 |
| J | `True` | `center` | 17.8 |
| L | `True` | `center` | 17.8 |
| M | `True` | `center` | 18.5 |
| AH | `True` | `center` | 11.8 |

row 10 之 `row_dimensions.height`：`14.0`（`None` = 自動）

### D.2 `NR1L-ComfortHMI-010` → **row 19**

- `L` / `M`（procedure / ER）：**寫入空字串** —— 儲存格存在、值為空，非「跳過不寫」。B 欄公式依 `$D19` 非空而給號，故該列仍計入序號
- `AH` Remarks 長度 **216 字元**，**無換行字元**（`\n` 出現 0 次）
- 該欄 `wrapText=True` → Excel 於欄寬內自動折行，列高自動增加
- 實測：AH 欄寬 `11.8`；以該寬度容納 216 字元需約 **19 行**

### D.2 `NR1L-ComfortHMI-012` → **row 21**

- `L` / `M`（procedure / ER）：**寫入空字串** —— 儲存格存在、值為空，非「跳過不寫」。B 欄公式依 `$D21` 非空而給號，故該列仍計入序號
- `AH` Remarks 長度 **226 字元**，**無換行字元**（`\n` 出現 0 次）
- 該欄 `wrapText=True` → Excel 於欄寬內自動折行，列高自動增加
- 實測：AH 欄寬 `11.8`；以該寬度容納 226 字元需約 **20 行**


### D.3 ⚠️ 列高：14 列全部 `customHeight=True, height=14.0`（單行）

實測 row 10–23 **全部**帶顯式列高 14.0（sheet 預設 13.0），且 `customHeight=True`。
與 `wrapText=True` 併用時，Excel **折行但列不長高** —— 多行內容只顯示第一行。

**內容不會遺失**（儲存格值完整），但**交付件之可讀性受影響**。逐列估算：

> **「需行數」之量測條件與限制（24 §4.4 追記）**
> 算法：`ceil(len(該欄文字) / 欄寬)` 逐行加總，取 I/J/L/M/AH 之最大。
> **未計字型、比例字寬、CJK 全形**，故為粗估。
> **跨檔不可比**：home 之 row 135 估 77 行，其實際列高 78pt（約 5–6 行文字）
> —— 該檔 I 欄寬 51.2 且內容為英文比例字，等寬假設嚴重高估。
> 本欄**只能用於同一檔內之相對比較**，不得跨檔比較絕對值。

| row | tc_id | 需行數（I/J/L/M/AH 取最大） | 可見 |
|---|---|---|---|
| 10 | NR1L-ComfortHMI-001 | **17** | 1 行 |
| 11 | NR1L-ComfortHMI-002 | **21** | 1 行 |
| 12 | NR1L-ComfortHMI-003 | **22** | 1 行 |
| 13 | NR1L-ComfortHMI-004 | **9** | 1 行 |
| 14 | NR1L-ComfortHMI-005 | **20** | 1 行 |
| 15 | NR1L-ComfortHMI-006 | **23** | 1 行 |
| 16 | NR1L-ComfortHMI-007 | **12** | 1 行 |
| 17 | NR1L-ComfortHMI-008 | **18** | 1 行 |
| 18 | NR1L-ComfortHMI-009 | **19** | 1 行 |
| 19 | NR1L-ComfortHMI-010 **[BLOCKED]** | **19** | 1 行 |
| 20 | NR1L-ComfortHMI-011 | **23** | 1 行 |
| 21 | NR1L-ComfortHMI-012 **[BLOCKED]** | **20** | 1 行 |
| 22 | NR1L-ComfortHMI-013 | **19** | 1 行 |
| 23 | NR1L-ComfortHMI-014 | **16** | 1 行 |

**兩個 BLOCKED row 尤甚**：其 `L`／`M` 為空（不需高度），但 `AH` Remarks 216／226 字元於 11.8 欄寬需約 19／20 行，僅顯示首行 `[BLOCKED-SPEC] Long-press logic is…`。marker 本身可見，說明文字不可見。

**處置屬 Tier 2，本包不決定。** 三個方向：
1. 寫回時清除該 14 列之 `customHeight`，交由 Excel 自動調高
2. 寫回時逐列設定顯式高度（需選一個估算公式，其與 Excel 實際排版未必一致）
3. 維持現狀 —— 內容完整、可點選儲存格檢視，接受列表視圖只見首行

**與範本之關係**：此列高非本 pipeline 所設 —— 範本 `SWQT_20260121` 原本即如此（A-CF07 之清列只動五格值，未動列高）。故任何處置都是**對範本呈現之改動**，須併同考量交付方之預期。

---

## 6. lint ＋ §9 自評 —— 僅列變動項

### 6.1 lint：31 → 32 gate

新增 `marker-whitelist`（R-C26）。原 31 個維持 PASS。

```
files: 7   TCs: 14   vocabulary: 9 strings   valid outlines: 129
32 / 32 gates PASS; 0 finding(s) across 14 TCs
```

### 6.2 §9 自評（依 R-C23，每項具名獨立依據）—— 僅一項變動

| # | §9 項目 | rev3 | rev4 | 獨立依據 |
|---|---|---|---|---|
| 3 | Pre-Condition 為 state/env、為 spec trigger 非隱含環境前提 | PASS | **PASS，且依據改變** | rev3 之依據為「每行標 source class（`source-class` gate）」。**該 gate 只驗標籤存在，不驗落點是否正確** —— TC-014 之 PC3 標籤正確而落點錯誤，且它通過了該 gate 三輪。rev4 之依據改為：**全批 12 條 × 每個 PC 行逐一套用 R-C25 兩問測試**（§2.2 之表即其結果），非依賴任何 gate |

**其餘 16 項自評不變**。

**第 3 項之依據更換，是 R-C23 的第二個實例**：舊依據（gate 通過）落在
R-C23 所禁之範圍內 —— 該 gate 的涵蓋範圍不含落點判定，而我用它當依據時
並未察覺這個缺口。這次的依據是一次逐條的人工判定，其結果（4 候選 / 1 真）
本身即為證據。

---

## 7. 寫回 dry-run —— 已產報告，未執行

**未呼叫 `xlsx_surgical` 之任何寫入函式**（`surgical_save`／`copy_unchanged`
皆未觸及）；**未產生新檔**；`DELIVERY.sha256` **未增列**，仍 2 筆 OK。

探測方式為 `openpyxl.load_workbook` **唯讀取值與樣式**，全程未 `save()`。

報告見 §5。其三項重點：

1. **目標列 row 10–23**，B 欄公式自動編號 1–14，不寫入
2. **留白欄已具名**：B／C／E／O／Q／T–Z／AB–AG，各附理由
3. **⚠️ 列高問題**（乙）—— 見下

### 7.1 乙 —— 列高：本包最實質之 dry-run 發現

14 列全部 `customHeight=True, height=14.0`，而 `wrapText=True`。
Excel 於此組合下**折行但不長高**。逐列估算需 **9–23 行**，實際可見 **1 行**。

**內容不會遺失** —— 儲存格值完整，點選即見。受影響的是**列表視圖之可讀性**。

**兩個 BLOCKED row 尤甚**：其 `L`／`M` 為空不需高度，但 `AH` Remarks
216／226 字元於 11.8 欄寬需約 19／20 行 —— 首行可見
`[BLOCKED-SPEC] Long-press logic is…`，**marker 看得到，說明看不到**。
而 R-C24 要求 Remarks 承載「擁有該內容之文件名 ＋ 何以無餘留」，
那正是看不到的部分。

**三個方向，本包不決定**（Tier 2）：

| # | 方向 | 代價 |
|---|---|---|
| 1 | 寫回時清除 14 列之 `customHeight`，交 Excel 自動調高 | 改動範本之呈現；列高將差異極大（9–23 行），表格外觀變動 |
| 2 | 逐列設定顯式高度 | 需選一估算公式，其與 Excel 實際排版未必一致；且仍是改動範本 |
| 3 | 維持現狀 | 交付件列表視圖只見首行；BLOCKED row 之說明實質不可見 |

**丙 —— 此列高非本 pipeline 所設**：範本 `SWQT_20260121` 原本即如此，
A-CF07 之清列只動五格值、未動列高。故三個方向**都是對範本呈現之改動**
（方向 3 是「不改」，但那意味著接受一個已知的可讀性損失）。
須併同考量交付方之預期 —— 既有四個 feature 之交付件是否也是如此，
本包未查（見 §8.2）。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 8.1 已驗

1. R-C25 兩問測試對全批 12 條之每個 PC 行（掃描 4 候選 → 1 真 3 誤報，
   誤報成因逐條分析）。
2. `marker-whitelist` gate 之反向驗證，含「豁免仍生效但白名單攔下」之並存。
3. TC-014 PC 由 4 行降 3 行；procedure／ER 逐字未動。
4. 14 列之 `customHeight`／`height`／`wrapText`／欄寬實測。
5. 兩個 BLOCKED row 之 Remarks 長度與所需行數。
6. `DELIVERY.sha256` 未增列（仍 2 筆 OK）；`output/` 未新增檔案。

### 8.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **既有四個 feature 之交付件是否同樣列高受限** | 本包只查 Comfort 之範本 | **中** —— 若 Privacy／SXM 之已交付件亦如此而客戶未反映，方向 3 即有前例；若不然，則本 feature 之處置不宜與之分歧。**一次唯讀掃描可解**，本包未做因未指示 |
| 2 | **Excel 實際排版與估算行數之差距** | 估算以「字元數 ÷ 欄寬」為之，未計字型、比例字寬、CJK 全形 | 中 —— 影響方向 2 之可行性，不影響「單行顯示不足」之結論 |
| 3 | **007 之落點判定** | R-C25 兩問測試之答案為「pre_conditions」，但 83% 重疊為四者最高 | **中** —— 我判「存在 vs 身分」為實質區別。若分析層認為步驟 1 已足以蘊含該 PC，則 PC2 應刪。**這是本輪最可能被推翻的判定** |
| 4 | 其餘 14 組是否有同型 §4.5 重複 | 本批只有 Seat Control Tab | 中 —— R-C25 自此適用全批次，掃描腳本可重用 |

**第 3 項需要說清楚**：TC-007 之 PC2 與步驟 1 主詞相同、句式近似，
我以「PC 斷言存在、步驟記錄身分」判其非重複。**該區別是真的，但很細** ——
若分析層採較嚴之讀法（步驟 1 記錄了哪一個，即已蘊含有一個），PC2 應刪。
我把判定寫在這裡而非默默保留，正是因為它可能是第五次同型 defect。

### 8.3 執行層對「本包可否結案」之判斷

**可結案，dry-run 待覆核。**

rev4 之 defect 已修、R-C25 首次全批適用已完成並逐條說明、`marker-whitelist`
已加並反向驗證、RUNBOOK 已記。

**寫回不執行**（22 §5.7）；其實際執行須 Pei 裁定交付形式、位置、送達
（Tier 3），於 dry-run 覆核通過後另行下放。

**覆核時建議優先看**：
1. §7.1 之列高三方向 —— 這是唯一需要在寫回前定案的事
2. §8.2 第 3 項之 TC-007 判定
3. §8.2 第 1 項 —— 是否要我掃既有四個 feature 之交付件列高作為前例
