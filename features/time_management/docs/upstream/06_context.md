# 上繳 06 — context 層六類編碼、單一來源模組，self-test 21/21 + 7/7

執行層 → 分析層。對應 `docs/handoff/06_context.md`。2026-08-21。

T1–T5 全數完成。**兩支 self-test 皆通過**（`lint_tcs` 21/21、
`build_batch_context` 7/7）。條數增量 R-TM **+2**、G-TM **0**、A-TM **0**。

**兩項須先講**：

1. **C-5 首次實作抓到 0 個訊號，全部 22 片皆然** —— 物件之需求文字在
   **物件行之後續段落**，而我只讀了物件行（那是屬性列）。已修正並驗證。
   見 §3.3
2. **R-TM51 判準 (a) 對其自身舉例逐字命中** —— 物件 `4814098`、網段
   `BH-CAN`、六個 `$GPSDateTm*$`，與條文所舉完全一致。見 §3.4

---

## 1. T5 驗證（R-TM31 列明細；R-TM46 增量 + 前後實測值）

```
R-TM50  RULINGS.md:1884      R-TM51  RULINGS.md:1914
G-TM1 更正                    RULINGS.md:1850
R-TM48 依據 1 逐字引入         RULINGS.md:1799（結構性不可複驗之標示）/ :1806
A-TM20 記載更正                ANOMALIES.md:1074
快照 README 更正               scripts_snapshot_20260821/README.md:21
context 產生器之 DR 佔位        build_batch_context.py，5 處
來源標記（四支）               build_batch_context / tm_rulings / write_back / lint_tcs 各 1

條數（前 → 後，增量）
  ## R-TM   52 → 54   +2   期望 +2   OK
  ## G-TM    3 →  3   +0   期望 +0   OK
  ## A-TM   24 → 24   +0   期望 +0   OK

self-test
  lint_tcs.py             21 / 21
  build_batch_context.py   7 /  7
```

## 2. T4(2) — **C-1 / C-2 與 lint 層之單一來源：`scripts/tm_rulings.py`**

`06` §4.2 要求兩層不得各寫一份。**實作方式**：新建
`features/time_management/scripts/tm_rulings.py`（132 行，**只含裁決值、
不含邏輯**），兩層皆匯入之。

**實證（非宣稱）**：

```
lint_tcs.BOUNDARY_SIGNALS is tm_rulings.BOUNDARY_SIGNALS → True
lint_tcs.SPEC_GAP_LEAVES  is tm_rulings.SPEC_GAP_LEAVES  → True
lint_tcs.TEST_SETS        is tm_rulings.TEST_SETS        → True

lint_tcs.py 內之本地重複定義計數 → 0
```

`is` 為同一物件之比對，非值相等 —— **兩層讀的是同一個記憶體物件**，
結構上不可能漂移。

**模組所含**：`TEST_SET_OF` / `TEST_SETS`（R-TM17）、`BATCHES`（Part VII）、
`SPEC_GAP` / `SPEC_GAP_LEAVES` / `spec_gap_placeholder()`（A-TM13 +
R-TM41 訂正）、`BOUNDARY_SIGNALS` / `BOUNDARY_NOTES`（R-TM23 + R-TM25）、
`SEGMENT_PLACEHOLDER`（R-TM49）、`TEST_ITEM_TOKEN_MAX`（canon §4.3.1）、
`TEST_GROUP`（R-TM8）、`SPEC_REF_PREFIX`（R-TM40）。

**檔頭載明每一項之依據與「誰讀它」**，使日後增修者知道改動會同時影響
兩層。

### 2.1 一項本包新增之區辨：`BOUNDARY_NOTES`

五條界線中，**只有三條有訊號層之歸屬**（011 / 008 / 014）；
另兩條（004↔010、014↔022、018↔011 之非訊號部分）之區辨在**觸發源與
規則歸屬**，無訊號名可比對。

故拆為兩表：`BOUNDARY_SIGNALS`（lint 可自動偵測）與 `BOUNDARY_NOTES`
（僅 context 之敘述指示，**lint 層對其無自動判準**）。

**此區辨原先隱含於「五條界線」一語中而未明說** —— B4 只實作了三條，
另兩條無人負責。現於 context 層以敘述補上，並於模組註解明記
「lint 層對其無自動判準」，使該缺口可見而非被「五條都做了」之說法掩蓋。

## 3. T4(1) — C-1 至 C-6 之實作位置與資料來源

| # | 實作 | 資料來源 |
|---|---|---|
| C-1 | `build()` 之 `boundary` 段 | `tm_rulings.BOUNDARY_SIGNALS` / `BOUNDARY_NOTES` |
| C-2 | `build_spec_reference()` 之 `gap` 段 | `tm_rulings.SPEC_GAP` + `spec_gap_placeholder()` |
| C-3 | `build_spec_reference()` | SYS2 第 5 欄 × 037 引用 × CFTS015 物件全集 |
| C-4 | `build()` 之 `test_item` 段 | `data/leaf_descriptions.txt`（R-TM24 唯一來源）+ `TEST_ITEM_TOKEN_MAX` |
| C-5 | `build_signals()` | CFTS015 物件 body（訊號名、網段候選）+ `SEGMENT_PLACEHOLDER` |
| C-6 | `build()` 之 `test_set` | `tm_rulings.TEST_SET_OF` |

**不進入 context 者**（依 `06` §4.1）：`tc_id`、`functional_safety`、
`priority` 分佈 —— 且已於 context 之 `constraints` 段明文告知生成端
**不得產出**，非僅省略。

### 3.3 **C-5 首次實作抓到 0 個訊號 —— 診斷與修正**

首次跑完後逐批檢視，**22 片全部 `訊號 0`**。

**成因**：`load_spec_objects()` 以 `OBJ_RE` 匹配物件行後，只存該行本身。
但物件行是**屬性列**：

```
4813974: [Artifact Type:Subsystem Functional Requirement] [State:Approved]
         [ECU:RRM, ETM, LTM] [Market:All] …
```

**需求文字在其下一段**：

```
When the CAN transitions from sleep to wake, the HU shall recall the last
known format and send this format over the CAN using the following
signal: $DateTmFormat$ …
```

訊號名 `$X$` 出現於 body 而非屬性列 —— 只存屬性列則必然抓到零個。

**修正**：`load_spec_objects()` 累積物件行之後、下一物件行之前之全部段落
為 `body`，`build_signals()` 改讀 `body`。並加一道守衛：

```python
if not any(v["body"] for v in out.values()):
    raise ContextError("全部物件之 body 皆空 …… body 全空則 C-5 必然抓到零個訊號")
```

**該守衛之必要性**：本次是我逐批檢視才發現，而 self-test 之 C-5 綠向
（`all("signals" in l ...)`）**只檢查鍵存在，不檢查內容非空** ——
與 `05R` 之 `lint_required_fields` 只檢查鍵存在同型。**若無守衛，
下次同型錯誤仍會全綠。**

**修正後之實測**（全 22 片）：

| 有訊號者 | 訊號數 | 有網段候選 | 標 PENDING |
|---|---|---|---|
| 004 / 014 | 6 / 6 | **6 / 6** | 0 / 0 |
| 015 / 017 | 6 / 5 | 0 | 6 / 5 |
| 002 / 009 | 3 / 3 | 0 | 3 / 3 |
| 008 / 010 | 2 / 2 | 0 | 2 / 2 |
| 011 / 018 | 1 / 1 | 0 | 1 / 1 |
| 其餘 12 片 | 0 | 0 | 0 |

即 **29 個訊號中 12 個有網段候選、17 個標 `PENDING: DR-6`** ——
與「本 feature 無 DBC」之事實一致，非一律填也非一律 PENDING（R-TM49 要求）。

### 3.4 **R-TM51 判準 (a) 對其自身舉例逐字命中**

R-TM51 舉例：

> ✓ 物件 4814098：`use a GPS.data internal signal to set a BH-CAN
>   message with correct UTC time and date.` 其後列 $GPSDateTm*$ 六訊號

**實測輸出**：

```
$GPSDateTmDay$      候選=BH-CAN  來源物件=4814098
$GPSDateTmHour$     候選=BH-CAN  來源物件=4814098
$GPSDateTmMinute$   候選=BH-CAN  來源物件=4814098
$GPSDateTmMonth$    候選=BH-CAN  來源物件=4814098
$GPSDateTmSecond$   候選=BH-CAN  來源物件=4814098
$GPSDateTmYear$     候選=BH-CAN  來源物件=4814098

原句：use a GPS.data internal signal to set a BH-CAN message with correct
      UTC time and date.$GPSDateTmHour$ $GPSDateTmMinute$ …
```

**物件 id、網段名、訊號組三者與條文所舉完全一致。**

**陰性對照**：`011` 之 `$DateTmFormat$` 標
`PENDING: DR-6` —— 其物件 4813974 之 body 只說 `over the CAN`，
無具體網段名，故 `SEGMENT_RE` 零命中，判準 (a) 不成立。
**該片正確地未被填值。**

### 3.5 C-5 之實作限制（已於檔頭與 context 之 `rule` 明示）

R-TM51 判準 **(a) 同物件**為純位置判斷，已自動化；
判準 **(b) 同述語**為句法判斷，**程式無法可靠自動化**。

故產生器**列出候選並附原句**，`segment` 欄留 `null` 交生成端依 (b) 判定；
**不自行斷定 (b) 成立**。(a) 不成立者直接填佔位。

此設計使「有來源」與「杜撰」在成品上可區分 —— context 給的是候選與原句，
生成端須於 reasoning 註明來源物件 id（R-TM51 要求）。

## 4. T4(4) — context 範例（`-001`，B1）

```json
{
  "leaf": "SWE-RA-TIME&DATE-001",
  "title": "Manual Time Setting",
  "test_group": "Time and Date",
  "test_set": "Manual Setting",
  "test_item": {
    "upper_verbatim": "The software shall allow user to set time via HMI and update internal time counters when GPS sync is disabled",
    "upper_token_count": 20,
    "upper_token_max": 50,
    "rule": "canon §4.3.1 兩段式。上半為需求原句 verbatim（來源限 data/leaf_descriptions.txt，R-TM24），token 上限 50，超限須摘句…下半為你所擬之測試目的，獨立成行，格式 `(...)`。缺括號下半 = FAIL，不得出貨。同一 leaf 衍生之多列，其括號內容不得逐字相同。"
  },
  "specification_reference": {
    "format": "CFTS015-{7 位物件 id}",
    "candidates_upper_bound": ["4813919", "4813920", "4813984", "4814069"],
    "rendered": "CFTS015-4813919, 4813920, 4813984, 4814069",
    "scope_note": "本清單為該 leaf 之聯集上限，非每條 TC 之預設值 —— canon §10.7：只列該 TC 直接驗證或作為 setup 依賴之物件…排列：前綴僅敘明一次、升冪、禁用 `;`。"
  },
  "signals": { "form": "<Signal> in <MESSAGE> on <segment>", "rule": "…", "signals": {} }
}
```

**`rendered` 已為 canon §10.7 之排列形式**（前綴一次、升冪、無 `;`）。

**`-005` 之 C-2 段**（B2）：

```json
"gap": {
  "objects": ["6151328"],
  "sys_ra": "SYS-RA-TIME&DATE-221",
  "note": "GPS_Presence=[Absent] 時之內部時鐘精度",
  "placeholder": "PENDING: DR-5 CFTS015 缺件物件 6151328",
  "instruction": "物件 6151328 於 CFTS015 SR26 全檔零命中（A-TM13）。該部分無章節可引：不得以鄰近物件填充（§8.4.1），亦不得留空（canon §8.4.3）——於 Remarks 寫 `PENDING: DR-5 CFTS015 缺件物件 6151328`。"
}
```

**`candidates_upper_bound` 為 `["4813936"]` 單一物件**，佔位在其之外
—— 即「一個真值 + 一個佔位」，佔位不取代真值（R-TM41 訂正之執行層補充）。

## 5. T4(3) — self-test red-green

```
PASS 綠向 C-1 界線      PASS 綠向 C-2 缺口      PASS 綠向 C-3 spec_ref
PASS 綠向 C-4 test_item PASS 綠向 C-5 訊號      PASS 綠向 C-6 Test Set
PASS 紅向 抽掉 leaf_descriptions.txt：/tmp/…/data/leaf_descriptions.txt 不存在 ——
     該檔為 test_item 上半之唯一許可來源（R-TM24）…

自驗：7 / 7
```

紅向以 `shutil.copytree` 複製 feature 目錄至 `/tmp` 後刪除該檔構造，
**不觸及來源**。

**綠向之強度限制（如實記）**：C-1 至 C-6 之綠向多為「該鍵存在」而非
「內容正確」。**C-5 之首次錯誤（抓到 0 個訊號）正是綠向通過而人工檢視
才發現者** —— 已於 `load_spec_objects()` 加守衛使該類錯誤 raise，
但**其餘五類之綠向仍為存在性檢查**。提請下一包評估是否收緊。

## 6. T6 — 該驗而未驗者（五全集）

### 6.1 依全集 2（寫入後複查）

| 檔案 | 複查 | 結果 |
|---|---|---|
| `RULINGS.md` | 條數 + 四處位置 | 54；:1799 / :1850 / :1884 / :1914 |
| `ANOMALIES.md` | 條數 + 記載更正位置 | 24；:1074 |
| 快照 README | 更正註記位置 | :21 |
| `tm_rulings.py` | `py_compile` + `is` 三項實證 | 通過 |
| `lint_tcs.py` | `py_compile` + self-test + 重複定義計數 | 21/21；0 |
| `build_batch_context.py` | `py_compile` + self-test + 逐批 C-5 實測 | 7/7 |

**一次 `str.replace` 因 assert 失敗而未寫入**（切片順序錯誤導致第三個
assert 不成立）—— 檔案完全未動，重做後成功。**assert 前置再次發揮作用。**

### 6.2 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | **C-1 至 C-4、C-6 之綠向強度** | §5，多為存在性檢查。C-5 已加守衛，其餘未加 |
| 2 | **兩條無訊號歸屬之界線（`BOUNDARY_NOTES`）** | lint 層**無自動判準**，僅 context 敘述。§2.1 |
| 3 | A-TM24 `functional_safety` | 來源 1 已否定，待 Pei |
| 4 | R-TM10-A1 步驟措辭、ER 樣板 | 仍無候選，B1 之硬阻塞 |
| 5 | R-TM47 之寫入（Part VII `Workbook sync`） | 全域檔，`05Z` 起暫不動 |
| 6 | `surgical_save` 寫入路徑 | 仍從未執行 |
| 7 | 其餘各包之「可驗而未驗」清單重判 | R-TM50 之作業影響，僅本包兩項已重判 |

### 6.3 依全集 4（陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| 單一來源生效 | `is` 三項皆 True，而修正前三項皆 False | 有 |
| C-5 修正後有內容 | 修正前全 22 片皆 0，修正後 10 片有訊號、12 片仍 0（無訊號者本應為 0） | 有 |
| R-TM51 (a) 命中其舉例 | `011` 之同一判準正確標 PENDING → 非一律填值 | 有 |
| 紅向能報錯 | 綠向六項同時通過 → 非一律報錯 | 有 |

### 6.4 依全集 5（設計說明之可驗性）

`06` §1.1 之分析層自陳（「我未要求任何佐證即據以立條」）—— 執行層已記入
G-TM1 更正之回報段，並補一層：**該陳述由執行層提供，故雙方各有一半**。
`00Z` §2 所立之「上繳陳述受查證義務拘束」對雙方同時失效，
**是本次能延續三輪之結構性原因**。

`06` §2 之 R-TM50 —— 執行層已更正自身標示法，並提請重判其餘各包之
「可驗而未驗」清單（見 6.2 項 7）。**本包僅重判 R-TM48 之依據 1、2。**

## 7. 本包未動之事項

未動 git。**未生成任何 TC**。未改 `backend/`、未改 canon、未改
`docs/fw036/framework.md`。未修改 `data/spec_reference_candidates.txt` 原檔。
未將 `CFTS015-6151328` / `-6151331` 寫入任何欄位（C-2 反而主動以佔位標之）。
**未填 `functional_safety` 之值**。**未杜撰任何 CAN 網段** —— 29 個訊號中
17 個標 `PENDING: DR-6`，12 個給候選與原句交生成端依 R-TM51(b) 判定。
未動 `TODO(R-TM10-A1)` 之步驟措辭常數與 ER 樣板。
未碰 `features/vehicle_setting/`。未送出 RD-1。
