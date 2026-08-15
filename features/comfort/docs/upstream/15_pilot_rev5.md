# 上繳包 15 — pilot rev5：TC-007 判定、Owner 前置、列高前例量測

執行層 → 分析層。2026-08-15。回應下放包 `23_rev4_review.md` §5。

**結論：七項作業全部完成。lint 32 gate 全 PASS。寫回仍未執行。**

---

## 0. 置頂

| # | 事項 |
|---|---|
| **甲** | **TC-007 判定規則之答案為「否」—— 我 rev4 的判定是錯的。** 13.2.1／13.3.1 皆無「恆有一個選定項」或預設值之明文；13.3.1 說的是「**last selected**」，那預設有過一次選擇**行為**，不是預設有選定**項**。PC2 屬 §7 FF 之假定隱藏狀態，已刪，procedure 增一步 |
| **乙** | **列高前例之答案是「混合」，且分界線清楚** —— **Privacy 之實際交付件（hash 相符）與 Comfort 同樣受限**（11 列全部 `height=14.0`，需 25–35 行）；home／SXM **不受限**（逐列高度 65–409pt）。分界在**起始範本**：Privacy 與 Comfort 同用空白範本 `SWQT_20260121`，home／SXM 起自已調版之 instance |
| **丙** | 「客戶未見反映」**我無從驗證** —— 我能證明的只有「Privacy 以此形態交付且該 hash 即交付件」。是否曾被反映，不在 repo 內 |

---

## 1. R-C27 貼入

`RULINGS.md` 現載 **R-C1 ~ R-C27 + R-C4-1 + R-C5-1**，共 **29 條**。

---

## 2. 甲 —— TC-007：判定規則之套用與引文

### 2.1 兩節全文（引，供覆核）

**`13.2.1`**（152 字元，全文）：

> LS1.1) The 4 types of adjustments the user will be able to alter for
> lumbar/bolster will be: Lumbar In/Out, Lumbar Up/Down, Back Bolster,
> Thigh Bolster.

**`13.3.1`**（406 字元，全文）：

> LS2.1) The user last selected lumbar/bolster selection will be latching
> during a keycycle, after a keycycle, and after the lower screen has been
> stowed/retracted. If the lower screen displayed the last selected option as
> Back Bolster , then the user retracts the lower screen, the next time they
> press the door (-, +) buttons or enter the seat tab on the HU, Back Bolster
> will still be the selected option.

### 2.2 判定：**否**

> 條文是否明文陳述「恆有一個調整類型為選定項」或給出預設選定項？

- **13.2.1** 僅列舉四種類型（`will be: …`）。**未言何者為預設，未言恆有一個
  為選定項。**
- **13.3.1** 之主詞為 `The user **last selected** … selection` 與
  `the **last selected** option`。**「上次選定」預設的是曾發生過一次選擇
  行為，不是預設隨時存在一個選定項。** 條文全篇未給初始狀態。

**併附機械佐證**：對 ch13 全七節掃 `default`／`initial(ly)`／`always`／
`pre-select` 四詞 —— **零命中**。`select` 系詞僅出現於 13.3.1，且皆在
`last selected` 之語境。

### 2.3 我 rev4 的論證錯在哪裡

rev4 §2.2 我寫：「四種類型中恆有一個為選定項，無需步驟建立」。

**那是推論，不是條文。** 而且它推反了 —— 13.3.1 的 `last selected` 不但沒有
保證恆有選定項，反而**要求先有一次選擇**才有「上次」可言。我把一個需要被
建立的前置條件，讀成了一個本來就存在的初始狀態。

23 §1 的處置我接受，且其形式值得記：**分析層不裁，因為它讀不到全文**
（僅 60 字截斷，依 R-C18 不得據以判落點）。它給的是**判定規則**與
**引文要求**，把判定連同其可覆核性一起下放。這比直接裁一個可能錯的結論好。

### 2.4 處置

| | rev4 | rev5 |
|---|---|---|
| `pre_conditions` | 2 行（含 PC2 `A lumbar/bolster adjustment type is currently the selected option`） | **1 行**（PC2 已刪） |
| `test_procedure` 1 | `Record which lumbar/bolster adjustment type is the selected option` | **`Select "Lumbar Up/Down" on the Seats tab`** |
| `expected_result` 1 | `The selected option before the keycycle is shown` | **`"Lumbar Up/Down" is shown as the selected option`** |
| `expected_result` 3 | `The selected option is the one shown in step 1` | **`The selected option is "Lumbar Up/Down"`** |

**選定哪一個類型**：取 `Lumbar Up/Down`。四個名稱皆由 13.2.1 明文給出，
故非造值；屬 interaction data，歸 procedure（§4.5）。**刻意不取 Back
Bolster** —— 那是 13.3.1 之具名例子，已由 TC-008 覆蓋；兩條取不同類型
使 sibling 區隔更清楚（§4.3）。

判定路徑已寫入生成器註解，下一個讀者不必回查往返包。

### 2.5 這是同一形態的第五次

23 §1 末段之觀察成立，但我要補一個區別：**前四次是「多寫了一個不該在
pre_conditions 的東西」，這一次是「寫了一個條文沒給的狀態」。**

前者違反 §4.5（落點）／§4.4（step-controlled state）；本次違反 §7 FF
（假定隱藏狀態）—— 那是更前面的一道：不是放錯欄位，是**那個事實根本
沒有來源**。

---

## 3. R-C27 —— Remarks 依可見性排序

### 3.1 改寫後之兩列

```
[BLOCKED-SPEC] Owner: HMI Core Logic and Flow requirement N0 — long-press
logic is defined there; with that delegation removed this requirement has no
content verifiable against the Comfort HMI specification alone
```

```
[BLOCKED-SPEC] Owner: CFTS044 — the equivalence to the previous 4-way rocker
hard control is defined there; with that delegation removed this requirement
has no content verifiable against the Comfort HMI specification alone
```

**首 60 字元之可見內容**：

| tc_id | 首 60 字元 |
|---|---|
| `NR1L-ComfortHMI-010` | `[BLOCKED-SPEC] Owner: HMI Core Logic and Flow requirement N0` |
| `NR1L-ComfortHMI-012` | `[BLOCKED-SPEC] Owner: CFTS044 — the equivalence to the previ` |

**marker 與擁有者皆落在可見範圍內** —— R-C27 之判準（截斷於首行時讀者是否
仍取得該欄位存在之目的所要傳達者）成立。

### 3.2 gate 增 `Owner:` 檢查 ＋ 反向驗證

`blocked-remarks` 增一項：`Owner:` 須出現於 Remarks 前 **60 字元**內
（`OWNER_WINDOW` 常數，與可見行寬對齊）。

反向驗證 —— 把 `Owner:` 移到句尾（內容完全相同，僅順序不同）：

```
[FAIL] blocked-remarks: NR1L-ComfortHMI-010: 'Owner:' must appear within the
       first 60 characters of Remarks (R-C27); measured head =
       '[BLOCKED-SPEC] Long-press logic is defined elsew'
```

**該 gate 檢查的是順序而非內容** —— 兩個版本字數相近、資訊等量，只有排序
不同，而 gate 抓的正是排序。這是 22 §4「判準 vs 用詞禁令」之正面用例：
判準是「關鍵資訊在不在可見範圍」，不是「有沒有寫某個字」。

---

## 4. 乙 —— 既有交付件之列高量測（23 §2）

### 4.1 量測條件與結果

### 量測條件

- 工具：`openpyxl.load_workbook`（非 read_only —— 需樣式），全程未 `save()`
- 量測欄：`customHeight` / `height` / `wrapText`（取 I 欄）/ 欄寬
- 資料列定義：header row 9 之後、D 欄（req_id）非空之列
- 需行數估算：`ceil(len(該欄文字) / 欄寬)` 逐行加總，取 I/J/L/M/AH 之最大

| 檔案 | SHA256(16) | 資料列數 | customHeight=True | height 相異值 | wrapText(I) |
|---|---|---|---|---|---|
| home（done region 144 列） | `1895fb2a2b44f06c` | 216 | **216 / 216** | {91.0: 44, 117.0: 6, 65.0: 27, 104.0: 21, 78.0: 48, 143.0: 2, 103.0: 2, 409.5: 1, 79.0: 2, 98.0: 14, 112.0: 14, 196.0: 1, 154.0: 4, 126.0: 10, 168.0: 2, 140.0: 5, 210.0: 1, 70.0: 3, 84.0: 8, 224.0: 1} | `True` |
| Privacy 交付件 regen-v1 | `ad595ed0cad24375` | 11 | **11 / 11** | {14.0: 11} | `True` |
| SXM 交付件 | `0b9cb4f65f86bac2` | 215 | **215 / 215** | {112.0: 31, 126.0: 74, 140.0: 48, 98.0: 9, 168.0: 16, 154.0: 21, 84.0: 1, 196.0: 6, 182.0: 9} | `True` |
| Comfort prepared（本 feature，對照） | `b68117a211b08009` | 0 | **0 / 0** | {} | `True` |

### 內容最長之三列 —— 其估算所需行數 vs 實際列高

**home（done region 144 列）**（欄寬 I=51.2 J=34.2 L=52.3 M=41.0 AH=9.0）

| row | 估算需行數 | height | customHeight | 可見 |
|---|---|---|---|---|
| 135 | **77** | 78.0 | `True` | 1 行 |
| 190 | **15** | 154.0 | `True` | 1 行 |
| 126 | **15** | 104.0 | `True` | 1 行 |

**Privacy 交付件 regen-v1**（欄寬 I=16.5 J=17.8 L=17.8 M=18.5 AH=11.8）

| row | 估算需行數 | height | customHeight | 可見 |
|---|---|---|---|---|
| 14 | **35** | 14.0 | `True` | 1 行 |
| 11 | **27** | 14.0 | `True` | 1 行 |
| 18 | **25** | 14.0 | `True` | 1 行 |

**SXM 交付件**（欄寬 I=37.3 J=39.0 L=39.5 M=31.7 AH=11.8）

| row | 估算需行數 | height | customHeight | 可見 |
|---|---|---|---|---|
| 220 | **20** | 196.0 | `True` | 1 行 |
| 212 | **19** | 196.0 | `True` | 1 行 |
| 219 | **18** | 182.0 | `True` | 1 行 |

**Comfort prepared（本 feature，對照）**（欄寬 I=16.5 J=17.8 L=17.8 M=18.5 AH=11.8）

| row | 估算需行數 | height | customHeight | 可見 |
|---|---|---|---|---|


### 4.2 Projection —— 未量

`features/projection/` **無 `DELIVERY.sha256`、`output/` 無 xlsx**。
依 23 §2「不可達者如實記為未量，不以推測代替」，**記為未量**。

### 4.3 乙 —— 結果之解讀（陳述，**不依結果自行處置**，23 §5.4）

**分界線是起始範本，不是 feature：**

| 群組 | 起始檔 | 欄寬（I/J/L/M/AH） | 列高 | 受限？ |
|---|---|---|---|---|
| **Comfort** | 空白範本 `SWQT_20260121` | 16.5 / 17.8 / 17.8 / 18.5 / 11.8 | 全部 `14.0` | **是** |
| **Privacy** | **同一份空白範本** | **完全相同** | 全部 `14.0` | **是** |
| home | `_Home_20260809` instance | 51.2 / 34.2 / 52.3 / 41.0 / 9.0 | 逐列 65–409.5 | 否 |
| SXM | `_SXM_20260810` instance | 37.3 / 39.0 / 39.5 / 31.7 / 11.8 | 逐列 84–196 | 否 |

**Privacy 之受限檔即其實際交付件** —— `DELIVERY.sha256` ENTRY 003
（標「**已交付**」）所記之 hash 為 `ad595ed0cad24375…`，與我量測之
`regen-v1` **完全相同**，即同一份位元組。交付路徑為
`…/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/…_Privacy_20260813.xlsx`。

**home／SXM 不構成反例** —— 兩者起自已調版之 pre-filled instance，其欄寬與
列高皆非本 pipeline 產生。它們證明的是「調過版的檔看起來沒問題」，
不是「本 pipeline 產出的檔沒問題」。

### 4.4 丙 —— 我無從驗證「客戶未見反映」

23 §2 之判定規則首項為「既有交付件同樣受限**且未見客戶反映**」。

**前半我已量到，後半我證不了。** repo 內無客戶回饋之紀錄；
Privacy 之 `ANOMALIES.md`／`DATA_REQUESTS.md`／往返包皆未見列高相關條目
（已查）。**「沒有紀錄」不等於「沒有反映」**（R-C13 同型：陰性檢索只是
索引層事實）。

故我把兩件事分開陳述：

- **可證**：Privacy 以 `height=14.0` 之形態實際交付，且該形態與 Comfort 相同
- **不可證**：該形態是否曾被交付方反映或接受

判定規則之首項因此**只滿足一半**。這件事我不代為補齊。

---

## 5. lint ＋ §9 自評 —— 僅列變動項

### 5.1 lint：32 gate 全 PASS（gate 數不變，`blocked-remarks` 增一檢查項）

```
files: 7   TCs: 14   vocabulary: 9 strings   valid outlines: 129
32 / 32 gates PASS; 0 finding(s) across 14 TCs
- PASS — rows exempted as BLOCKED-SPEC: ['NR1L-ComfortHMI-010', 'NR1L-ComfortHMI-012']
- PASS — marker whitelist (profile §5.1): ['NR1L-ComfortHMI-010', 'NR1L-ComfortHMI-012']
```

### 5.2 §9 自評（依 R-C23）—— 兩項變動

| # | §9 項目 | rev4 | rev5 | 獨立依據 |
|---|---|---|---|---|
| 3 | Pre-Condition 為 state/env、為 spec trigger 非隱含環境前提 | PASS | **PASS，且範圍擴大** | rev4 之依據為「全批套用 R-C25 兩問測試」，但**兩問測試預設該狀態確為 spec trigger**（資格問題已答「是」才問落點）。TC-007 之 PC2 **連資格都不成立** —— 它不是 spec trigger，是無來源之假定。rev5 之依據改為：**每個 PC 行先查其來源節次之 full_text 有無對應明文**（§2.1 之引文即其一例），再問落點 |
| 12 | 追溯 RD、不擴張、**無造值**（§8.4.1） | PASS | **PASS，且理由改變** | rev4 之理由為「未寫任何級距量值」。rev5 另加：TC-007 之 `Lumbar Up/Down` 取自 13.2.1 之明文列舉，**非自選**；若取一個條文未列之名稱即為造值 |

**其餘 15 項自評不變。**

**第 3 項是本輪最實質的自評變動**：R-C25 之兩問測試我上一輪當成完整判準用，
**它其實預設了第一問已答「是」**。TC-007 通過了兩問測試（我當時答資格「是」），
但那個「是」本身沒有條文依據 —— 判準本身沒錯，是我把資格問題也用推論答了。

---

## 6. 寫回仍未執行

- **未呼叫 `xlsx_surgical` 任何寫入函式**；未產新檔；`DELIVERY.sha256` 仍
  2 筆 OK、無 ENTRY 002；`output/` 仍 1 檔。
- 列高量測全程 `load_workbook` 唯讀取值與樣式，**未 `save()`**。
- dry-run 報告之 Remarks 段已依 §3 之新措辭更新（見上繳 14 §5 之 D.2，
  首行可見內容由「marker + 說明開頭」變為「marker + Owner」）。

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 7.1 已驗

1. 13.2.1／13.3.1 全文，及 ch13 全七節之四詞掃描（零命中）。
2. TC-007 之 PC／procedure／ER 三處改動。
3. 兩個 Remarks 之首 60 字元可見內容。
4. `Owner:` gate 之反向驗證（同資訊、僅換順序即 FAIL）。
5. 四份工作簿之列高、欄寬、`customHeight`、`wrapText`，含 hash。
6. Privacy ENTRY 003 之 hash 與 regen-v1 相符（確認量到的是交付件本身）。
7. Privacy 之 ANOMALIES／DATA_REQUESTS／往返包無列高相關條目。

### 7.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **Projection 之交付件列高** | 無 `DELIVERY.sha256`、`output/` 無 xlsx —— **檔案不存在，如實記為未量**（23 §2 明示不以推測代替） | 低 —— Privacy 已提供同範本之直接前例 |
| 2 | **客戶是否曾反映列高** | repo 外之事實 | **中** —— 判定規則之首項因此只滿足一半（§4.4） |
| 3 | **估算行數與 Excel 實際排版之差距** | 估算未計字型、比例字寬、CJK 全形 | 中 —— 影響「需幾行」之精度，不影響「單行不足」之結論。home row 135 估 77 行而實高 78pt（約 5–6 行），差距明顯 |
| 4 | **其餘 14 組是否有同型 §7 FF 假定隱藏狀態** | 本批只有 Seat Control Tab | **中** —— rev5 之新依據（先查來源節 full_text 有無明文）尚未對其他組套用過 |
| 5 | TC-007 之 `Lumbar Up/Down` 是否為最佳選擇 | 四者皆合法，我取其一 | 低 —— 若分析層偏好其他類型，改一個字串 |

**第 3 項需要具體說明**：home 之 row 135 我估 77 行，而其實際列高 78pt
（約 5–6 行文字）。**估算明顯高估** —— 因為它按字元數除以欄寬，未計 home
之 I 欄寬達 51.2、且英文比例字寬遠小於等寬假設。故 §4.2 之「需行數」欄
**只能用於同一檔內之相對比較，不宜跨檔比較絕對值**。這一點我在 rev4 就
該說明而沒說。

**第 4 項是我主動提出的**：rev5 才確立「PC 之事實須在來源節 full_text 有
明文」這個依據，而它只對 Seat Control Tab 套用過。其餘 14 組於 Phase 4
展開時須以同一依據檢查 —— 這不是預防性建議，是本輪剛證明會出錯的地方。

### 7.3 執行層對「本包可否結案」之判斷

**可結案。** TC-007 已依判定規則處置並引文可覆核、Remarks 已依 R-C27 重排
並經反向驗證、列高前例已量並分開陳述可證與不可證者。

**寫回仍不執行。** 待兩事：

1. **列高方向之裁定** —— 量測結果為「同範本之 Privacy 交付件同樣受限」，
   但判定規則之第二半（客戶未見反映）我證不了，故不代為套用方向 3
2. **交付形式、位置、送達**（Tier 3，22 §5 末段）

**覆核時建議優先看**：
- §2.5 —— 本次與前四次是不同的違反（§7 FF 而非 §4.5），是否需分別記錄
- §4.4 —— 判定規則只滿足一半時的處置
- §7.2 第 4 項 —— 其餘 14 組是否需先以新依據掃一輪再展開
