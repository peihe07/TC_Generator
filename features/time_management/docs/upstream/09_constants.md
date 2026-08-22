# 09 上繳 —— 死常數處置、A-TM25 量值更正、常數表 v2 之技術意見

執行層，2026-08-22。對應下放包 `docs/handoff/09_constants.md`。

---

## 0. 執行結果一覽

| 任務 | 內容 | 狀態 |
|---|---|---|
| T1 | R-TM59 入 `RULINGS.md` | 完成 |
| T2 | A-TM25 量值更正（原值加刪除線保留） | 完成 |
| T3 | `write_back.py` 單一來源重構；紅綠 **8/8** | 完成 |
| T4 | 四處 TODO 修訂（#1 #3 #7 #8） | 完成 |
| T5 | DR-8 / DR-9 / DR-10 登記 | 完成（**DR-7 成空號**，見 §4） |
| T6 | `tm_constants.py` **未建**（依令）；v2 技術意見見 §5 | 完成 |
| T7 | 驗證 | 完成 |
| T8 | 本包 | 完成 |

**增量（R-TM46）**：`## R-TM` **+1**（61 → 62）；`## A-TM` **0**（25）；
`## G-TM` **0**（3）。與下放包所訂增量相同。

**核心成果**：`--write` 之 unresolved **實測為空**。

**本包三項須先看**：§2 之「雙來源實為三來源」、**§5.1 之三條新常數與需求
所述行為不符**（v2 之時區/DST 四條中三條）、**§5.3 我在 `08` §6.2 的一處
量測錯誤**（005 並不涉 12H/24H 格式）。

---

## 1. T3 核心成果 —— `--write` 之 unresolved 為空

```
$ python3 write_back.py --feature-dir features/time_management
source        : FM-WI-FSM-036-A01 …_20260817_ext.xlsx
  SHA256      : 6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2
sheet         : 'Test Case Specification 測試用例規範', header row 9
columns       : req_id=D, tc_id=F, test_group=G, test_set=H, test_item=I,
                pre_conditions=J, input_test_data=K, test_procedure=L,
                expected_result=M, spec_reference=N, tc_ref_id=O, priority=P,
                design_method=R, functional_safety=S, author=AA, remarks=AH
rows          : 0 TCs at rows 10-10
tc_id         : 起點序號 0；本批 NR1L-TimeAndDate-001 … NR1L-TimeAndDate-000

內容常數        : 全部已決 —— unresolved 為空（R-TM57 / R-TM59）

DRY RUN —— 未寫出任何檔案。加 --write 才實際寫入。
```

**一項顯示層瑕疵（本包發現，未逕改）**：`rows = 0` 時末號印為
`NR1L-TimeAndDate-000`（`start_seq + rows` = 0）。不影響寫入（0 列不寫），
但輸出上是個不存在的編號。修法明確（rows = 0 時不印區間），
但屬 `run()` 之顯示邏輯，非本包指派範圍，**列入未驗清單 A 區**。

---

## 2. T3 —— 「雙來源」實為**三來源**

R-TM59 述「模組層讀入之值與 `write_rows` 實際使用者須為同一來源」，
即認定有兩處。實測有**三處**各自讀取：

| # | 位置 | 原本 |
|---|---|---|
| 1 | 模組層 `TC_ID_FORMAT = None` | 死常數，從不被讀 |
| 2 | `write_rows` | `fmt = wbk["tc_id_format"]` |
| 3 | **`run()` 之 tc_id 預覽列印** | `cfg['write_back']['tc_id_format'].format(...)` **兩次** |

第 3 處是本包實作時才發現的 —— `08` §5 我只 grep 了識別字
`TC_ID_FORMAT`，而該處用的是字典鍵字面量，grep 不到。
**這正是同族的量測盲點**：以識別字搜尋，找不到以字面量存取的第二條路徑。

三處已全部改走唯一入口 `resolve_tc_id_format(cfg)`。

### 2.1 三項超出指令之設計決定，逐項說明理由

**(a) `TC_ID_FORMAT` 之保留值刻意不是格式字串**，而是來源指標
`"<see feature.yaml: write_back.tc_id_format>"`。

R-TM59 要求「不刪除該識別字，保留痕跡」。但若保留一份**真的格式字串**，
痕跡是留下了，**雙來源也一併留下了** —— 日後誤用者會靜默產出看似正常
的 tc_id。改為指標後，誤用立即失敗。

**(b) `resolve_tc_id_format` 另加一項未要求之檢查：格式須含 `{n`。**

無序號欄位之格式會使全部列拿到同一個 tc_id，而 `check_written_back`
（G-TM3）逐列比對預期值時**兩側同錯**，驗不出來。此為 R-TM21
（檢查須能失敗）之直接應用。

**(c) `assert_tc_id_single_source` 抽為可獨立呼叫之守衛**（R-TM56）：
一行 `assert_tc_id_single_source(cfg, "<壞值>")` 即可觸發，紅向 2 即以此
構造，不經由 `run()` 之間接路徑。

### 2.2 紅綠 8/8

```
── 綠向 ──
PASS 綠 1 (resolve 取得 yaml 之值): 'NR1L-TimeAndDate-{n:03d}'
PASS 綠 2 (守衛：用值與唯一入口相同 → 不 raise)
PASS 綠 3 (unresolved 清單為空): []

── 紅向 ──
PASS 紅 1 (yaml 缺 tc_id_format → raise)
PASS 紅 1b(格式不含 {n} → raise)                    ← 本包自加
PASS 紅 2 (write_rows 另讀一份、與入口分岔 → 守衛抓到)
PASS 紅 3 (CONST 改為 None → 被攔)
PASS 紅 3 (CONST 改為 空字串 → 被攔)                ← 新判準之證明
```

`v == ""` 之新判準已證實生效（`08` §4.1 紅向 2 之射程缺口已補）。

---

## 3. T1 / T2 / T4

### T2 —— A-TM25 量值更正

原記之 (a)(b) 二行**加刪除線保留**（R-TM13），條末追加更正區塊全文。
**條數不變（25）。**

分析層已說明「7」之成因：該數為單一步驟字串
（`Read the screen and check whether the popup is displayed`）之出現頻次。
與 `08` §3 所述「兩種算法都試不出 7」相符 —— 我試的是「相異字串數」與
「全部出現數」，實際條件是「特定單一字串之出現數」，屬第三種。

**執行層自訂之對應作法**：本包起，凡回報計數，一律於同一行內附量測條件
（哪個欄、相異或全部、有無閾值、是否分大小寫）。本包各處已照此辦理。

### T4 —— 四處 TODO 修訂（改前／改後）

| # | 位置 | 改前 | 改後 |
|---|---|---|---|
| 1 | `write_back.py:18` docstring | 「三常數標 `TODO(R-TM10-A1)`，待本 feature 條文決定」 | 逐項列現況：`CONST_FUNCTIONAL_SAFETY` 已決（R-TM57，並註明與 Privacy 巧合同值但依據不同）、`tc_id_format` 已決（R-TM32／單一來源 R-TM59）、`PLACEHOLDER_BODY` 仍 TODO 但無使用點 |
| 3 | `write_back.py:69` `TC_ID_FORMAT` | `TODO(R-TM10-A1)` + `= None` | TODO 撤除；改為來源指標，附 R-TM59 之依據與「原為死常數」之記載 |
| 7 | `write_back.py:328` unresolved 列印 | 「TODO(R-TM10-A1) 未決之內容常數：…」 | 「未決之內容常數（其值屬 TC 內容…）」；且清單為空時改印「全部已決 —— unresolved 為空」 |
| 8 | `lint_tcs.py:13` docstring | 「Test Set 值、priority 預設一律留 `TODO(R-TM10-A1)`」 | 逐項列現況：Test Set 已實作、priority 值域已實作、priority 分佈標 `TODO(內容裁決)`、步驟措辭已確定自訂且擬定中、ER 樣板**刻意不做** |

其餘九處維持不動。**修訂後全 feature 之 `TODO(` 計數：14 處**
（`write_back.py` 5、`lint_tcs.py` 9、其餘二支 0）—— 較 `08` 之 13 處
多 1，成因是 #1 之 docstring 由一句改為逐項表列，其中一列引用了
`TODO(R-TM10-A1)` 字樣。**非新增未決項。**

---

## 4. T5 —— DR 登記，**DR-7 成空號**

DR-8 / DR-9 / DR-10 已入 `DATA_REQUESTS.md` 之主表與 `PENDING` 錨對照表。

**但本 feature 之既有 DR 最大號為 6**（實測：全 feature 目錄曾用之號為
DR-2 / DR-5 / DR-6，DR-7 零命中），故下一個可用號本應為 **7**。

下放包 §5 T5 明文指定 8 / 9 / 10，**執行層依令配號，未自行前移** ——
DR 號為識別碼，改動指定值須經裁定。指令雖有「若既有 DR 已用到 8 以上，
順延並回報」之但書，只涵蓋向後順延，未涵蓋向前補位。

**DR-7 因此成為未使用之空號**，已於 `DATA_REQUESTS.md` 明記，
使日後讀者不會誤認為遺失之登記。**提請裁定**：改配 7/8/9，或維持並保留
註記。空號不影響 `PENDING` 佔位之指向唯一性，故未逕改。

---

## 5. T6 —— 常數表 v2 之技術意見（`tm_constants.py` 依令未建）

### 5.1 **時區/DST 四條新常數中，三條與需求所述之行為不符**

這是本包最重要的技術意見。逐字比對 leaf 描述：

```
012 Time Zone Handling
    The software shall determine and apply time zone **automatically using
    GPS** and retain last known value on restart

013 DST Handling
    The software shall **automatically** adjust daylight saving time
    **based on time zone rules**
```

**兩片所述皆為自動行為，無使用者操作。** 對照 v2：

| 常數 | 措辭 | 判定 |
|---|---|---|
| `SET_TIME_ZONE = 'Open the "Time and Date" settings and set the time zone'` | 手動設時區 | **與 012 不符** —— 012 說時區由 GPS 自動決定。若 UI 根本無手動時區設定，此步驟不可執行；即使有，它測的也不是 012 所述之能力 |
| `DST_ON = 'Set "Daylight Saving Time" to ON'` | 手動開關 DST | **與 013 不符** —— 013 說 DST 依時區規則自動調整 |
| `DST_OFF` | 同上 | 同上 |
| `CROSS_TIME_ZONE = 'Move the vehicle position across a time zone boundary'` | 改變位置 | **唯一與 012 相符者** —— 012 之觸發源就是 GPS 位置 |

**要測 012 / 013，正確的操作是改變 GPS 位置與時間（使其跨越時區邊界或
DST 切換點），不是撥 UI 開關。** 而那正好是 `CROSS_TIME_ZONE` ——
即分析層 §3.3 保留具體措辭、且設備能力存疑的那一條。

**故 DR-10 之「位置設定」不是附帶一問，而是關鍵路徑**：003（GPS Time
Calculation，逐字含 `using GPS UTC, time zone, and DST`）、012、013
**三片**的測試都依賴它。下放包 §3.3 稱「若連位置都不能設，003 整片皆不可
測」——**實為三片**。

**建議**（擬定屬分析層）：三條改為佔位或刪除，另立 DST 邊界之觸發措辭，
其可執行性同樣依賴 DR-10。

### 5.2 `SET_FORMAT_12H` / `SET_FORMAT_24H` —— 可執行，無異議

```
011 Time Format Handling
    The software shall store, recall, and broadcast time format (12H/24H)
    across wake cycles
```

需求明言 12H/24H 為可設定之格式，二常數措辭清楚可執行。
**但缺一條「跨喚醒週期」之驗證所需操作** —— 011 之核心是 store/recall
across wake cycles，須配合 `KEY_OFF` / `KEY_ON` 或 sleep/wake（後者依賴
DR-9）。此為組合問題，非單一常數之缺失。

### 5.3 **更正我在 `08` §6.2 的一處量測錯誤**

`08` §6.2 我報「12H/24H 格式：**005、011** 兩片」。**005 是錯的。**

```
005 Internal Clock Accuracy
    The software shall maintain internal clock with ±2 sec accuracy
    per 24 hours when GPS is unavailable
```

005 完全不涉時間格式。我的關鍵詞是 `12.?h|24.?h|format`，
**命中的是 `24 hours` 這個字串**，與 12H/24H 格式無關。

**正確結論：涉 12H/24H 格式者只有 011 一片。**（時區/DST 之三片
003/012/013 不受此影響，該三項為 `time ?zone|daylight|DST` 命中，複核無誤。）

**這是 R-TM31 所指之同一類問題在我這邊的實例**：我報了「兩片」這個計數
並附了片號，看似可歸屬，但**未複核每一個命中是否為真命中**。
`08` §6.2 之表已列出量測方法（關鍵詞），這次得以自行發現 —— 若當時只寫
「兩片」而不寫方法，這個錯會留下來。

**005 另有一項無常數可用之情形**：其驗證需「24 小時內 ±2 秒」之長時量測，
v2 無對應常數，且該類步驟可能不宜常數化（時長與量測方式屬 TC 內容）。
**僅指出，不建議措辭。**

### 5.4 三條改 `PENDING: DR-n` —— 同意，並補一項理由

`GPS_LOST` / `GPS_RESTORE` / `CAN_SLEEP` / `ECU_RESET` 改為佔位，
執行層同意。分析層之理由為「推測無來源，屬 §8.4.1 所禁」。

**技術面補一項**：`ECU_RESET` 之佔位還有一層必要性 —— 018 逐字為
`after reset **or** battery reconnection`，**兩者是需求明列的兩種觸發**。
若因無操作方式而以 `BATTERY_RECONNECT` 代替 reset，該 TC 會**看起來**
覆蓋了 018 而實際只覆蓋一半，且 lint 無從發現（措辭合法、步驟完整）。
佔位使這個缺口保持可見。

### 5.5 v2 其餘各條 —— 無技術異議

`SET_TIME_MANUAL` / `SET_DATE_MANUAL` / `GPS_SYNC_ON` / `GPS_SYNC_OFF` /
`KEY_OFF` / `KEY_ON` / `BATTERY_RECONNECT` / `CAN_WAKE` /
`READ_HU_TIME` / `READ_IPC_TIME` / `READ_HU_DATE`：
動作+目標齊備、直雙引號、無句尾句點、無 §5.1 禁用動詞、可執行。

`READ_HU_DATE` 之新增填補了 `08` 未指出的一個缺口（016 Date Master
Function、017 Date Transmission 皆須讀日期而非讀時間）。

---

## 6. T7 —— 驗證輸出（R-TM31：列明細）

```
(1) grep -n '^## R-TM59' RULINGS.md
    2346:## R-TM59 — 死常數處置採 (b)

(2) grep -n '量值更正' ANOMALIES.md
    1535:（二項之量值於 2026-08-22 更正，見條末「量值更正」；牴觸之成立不變）
    1567:### 量值更正（2026-08-22，分析層，依 `08` 上繳 §3）
    1572:A-TM25 量值更正（2026-08-22，依 08 上繳 §3）

(3) grep -n 'TC_ID_FORMAT\|PLACEHOLDER_BODY' write_back.py
    17,25  docstring 之現況表列（T4 #1）
    78     PLACEHOLDER_BODY = None          ← TODO 保留，已移出 unresolved
    83,85  TC_ID_FORMAT = "<see feature.yaml: write_back.tc_id_format>"
    378    unresolved 之註解（說明二者為何不在清單內）
    → 兩者皆不再出現於 unresolved 之運算式中。

(4) DR-8 / DR-9 / DR-10 於 DATA_REQUESTS.md：6 處命中（主表 3 + 錨對照 3）

(5) TODO( 逐處：14 處
    write_back.py 5：docstring 現況表 1、PLACEHOLDER_BODY 1、
                     BLANK_BY_DECISION 3（C 欄 / Q 欄 / T–Z 欄）
    lint_tcs.py   9：docstring 現況表 2、C1 結案註記 2、步驟措辭閘門 1、
                     priority 分佈 2、二者之區分說明 1、Input Test Data 1
    build_batch_context.py 0、tm_rulings.py 0

(6) lint_tcs --self-test              自驗：31 / 31
(7) build_batch_context --self-test   自驗：13 / 13
```

---

## 7. 未驗清單（R-TM54 三分）

### A. 可驗而未驗 —— 執行層能清

| # | 項目 | 說明 |
|---|---|---|
| A1 | `rows = 0` 時 tc_id 區間印出 `-000` | §1；修法明確，非本包指派範圍 |
| A2 | A-TM25 (a)(b) 無自動攔截 | 措辭閘門仍在 `TODO(R-TM10-A1)` 下。**因 §5.1 之發現而更值得做** |
| A3 | B-1 / B-2 及 B-3、B-5 未守之側 | 07 遺留，待 B1 pilot 檢查表 |
| A4 | 018 / 017 之 objects 未逐一複驗 | 07 遺留 |
| A5 | `BOUNDARY_NOTES` 與 `BOUNDARY_SIGNALS` 對 018 之並存 | 07 遺留 |
| A6 | 交付件之 pre_conditions / ER 形式慣例未逐條驗 | 08 遺留 |
| A7 | v2 其餘各條與 22 片之逐片對應未全查 | 本包只逐字查了 003/005/011/012/013/018 六片，其餘採 `08` 之關鍵詞掃描結果 —— 而 §5.3 已證關鍵詞掃描會誤命中 |

### B. 結構性不可複驗 —— 待 Pei

| # | 項目 |
|---|---|
| B1 | 常數表 v2 之過目（**含 §5.1 之三條不符**） |
| B2 | A-TM25：本 feature 依 canon 而與既有交付件外觀不同 |
| B3 | DR-8/9/10 之答覆（設備能力）；**DR-10 為 003/012/013 三片之關鍵路徑** |
| B4 | DR-7 空號之處置 |
| B5 | RD-1 之送出 |

### C. 已解決 —— 註明包號後移除

| # | 項目 | 解決於 |
|---|---|---|
| C1 | 兩個死常數擋住 `--write`（08 §5） | 本包 T3（R-TM59），unresolved 實測為空 |
| C2 | unresolved 對空字串無效（08 A2） | 本包 T3，紅向已證 |
| C3 | 四處過時之 TODO（08 §8.1） | 本包 T4 |

---

## 8. 未執行者（下放包所禁，逐項確認）

- 未生成任何 TC
- **未建 `tm_constants.py`**
- 未修改既有交付件（本包未再讀取）
- 未改 `backend/`、canon、`docs/fw036/framework.md`
- 未將 022 加入 `BOUNDARY_SIGNALS`（陰性對照仍在，31/31 含該項）
- **未杜撰 ECU reset / CAN sleep / GPS 控制之操作方式** —— §5.1 只指出
  三條常數與需求不符，**未代擬替代措辭**
- 未碰 `features/vehicle_setting/`
- 未送出 RD-1
- 未動 git（R-TM36）
- 未修改任何既有上繳包 —— §5.3 對 `08` §6.2 之更正寫在本包，未回改 `08`

---

## 9. 提請裁定

1. **§5.1 —— v2 之 `SET_TIME_ZONE` / `DST_ON` / `DST_OFF` 與 012/013 所述
   之自動行為不符。** 要測該二片須改變 GPS 位置與時間，非撥 UI 開關。
   三條建議改佔位或刪除，替代措辭之擬定屬分析層。
2. **DR-10 之「位置設定」為 003 / 012 / 013 三片之關鍵路徑**，非一片。
   建議在 DR-10 之敘述中明列此三片。
3. **§5.3 —— 我在 `08` §6.2 報的「12H/24H：005、011 兩片」中 005 為誤命中**
   （命中 `24 hours`）。正確為**只有 011 一片**。是否需回改 `08` 之條文
   引用處（執行層未回改任何既有上繳包）。
4. **§4 —— DR-7 空號**：改配 7/8/9 或維持。
5. **§2 —— R-TM59 述「雙來源」實為三來源**，第三處以字典鍵字面量存取，
   識別字 grep 不到。是否值得立為條文（搜尋未決項須同時搜識別字與字面量）。
