# 08 上繳 —— functional_safety、D5、樣式常數之複驗與實作

執行層，2026-08-22。對應下放包 `docs/handoff/08_style.md`。

---

## 0. 執行結果一覽

| 任務 | 內容 | 狀態 |
|---|---|---|
| T1 | R-TM57 / R-TM58 入 `RULINGS.md`；R-TM9-A2 訂正段加刪除線保留並指向 R-TM58 | 完成 |
| T2 | A-TM24 → RESOLVED（附依據摘要）；A-TM25 新增＋索引 | 完成 |
| T3 | `CONST_FUNCTIONAL_SAFETY = "NA"`，撤 TODO；紅綠 | 完成 |
| T4 | `lint_d5_scope` 改判；一綠四紅 | 完成 |
| T5 | design_method 雙語字串逐字＋位元組比對 | 完成，子集成立 |
| T6 | `tm_constants.py` **未建**（依令）；技術面意見見 §6 | 完成 |
| T7 | 驗證 | 完成 |
| T8 | 本包 | 完成 |

**增量（R-TM46）**：`## R-TM` **+2**（59 → 61）；`## A-TM` **+1**（24 → 25）；
`## G-TM` **0**（3）。與下放包所訂增量相同。

**本包三項須先看**：§1.1 之六項獨立複驗（全符）、§3 之 A-TM25 量值差異
（兩處都比分析層所報更嚴重）、**§5 之兩個死常數**（推翻「B1 只等 §3.4
過目」之結論）。

---

## 1. 交付件實測 —— 執行層獨立複驗

Pei 之授權及於分析層；執行層確認同一檔案可讀，**故未採信轉述，全部重測**
（R-TM31 之精神：轉述之數字不可歸屬）。讀取為 `data_only=True` 之唯讀
載入，**未對該檔寫入任何內容**。

### 1.1 六項全符

| 項 | 分析層所報 | 執行層複驗 | 判定 |
|---|---|---|---|
| 資料列數 | 189 | 189（以 F 欄 `Test Case ID` 判定） | 符 |
| S 欄 functional_safety | `{'NA': 189}` | `{'NA': 189}` 單值無例外 | 符 |
| D5 | `None`；C5 = `範圍 Scope：` | `None`；C5 = `'範圍 Scope：'` | 符 |
| D2 / J5 | `'newR1L'` / `'2025/10/17'` | 同 | 符 |
| priority 分佈 | P0 38 / P1 66 / P2 71 / P3 14 | 同（合計 189） | 符 |
| Input Test Data = NA | 159/189（84%） | 159/189 | 符 |

**一處我自己的初判錯誤，已自行更正**：首次量測時取「末列之 tc_id」得
`NR1L-UserProfiles-073`，一度以為與下放包所稱之 `-001 … -189` 不符、
懷疑一個 tc_id 對應多列。重測後：**189 個相異 tc_id、連續 001…189、
一列一 id**，下放包正確。成因是**列序非 id 序**（交付後經過重排），
末列剛好是 073。

此事的可記取之處：`ids[-1]` 隱含「列序即編號序」之假設。判定編號範圍
應取 `min`/`max` 或驗連續性，不取首末列。**已在本次以連續性驗證取代。**

### 1.2 rev C 版面對映（34 欄）逐欄複驗

表頭列 = 9，資料自列 10 起。與 FORMS.md 之母本對映一致：

```
  B No.#     C Requirement/Design ID (Polarion)   D Requirement/Design ID
  E Test Case ID (TestRail)      F Test Case ID   G Test Group   H Test Set
  I Test Item   J Pre-Conditions   K Input Test Data   L Test procedure
  M Expected Result   N Specification Reference   O Test Case Reference ID
  P Test Case Priority   Q Estimated Test Time   R Test Case Design Methods
  S Functional Safety   T–Z 車型七欄   AA Test Case Author   AB Test Version
  AC Test Vehicle   AD Test Period   AE Tester   AF Test Result
  AG Defect ID   AH Remarks
```

**一項須提醒**：`tc_id` 落在 **F 欄**（`Test Case ID`），**E 欄為
`Test Case ID (TestRail)` 且全空**。`write_back.BLANK_BY_DECISION` 已
正確記為「E (TestRail ID): assigned downstream」—— 與交付件實況相符。

---

## 2. T1 / T2 —— 條文與異常

### 2.1 R-TM9-A2 訂正段之處置

依 R-TM13 **加刪除線保留、未刪除**，並在段首加引述框指向 R-TM58，
段末對佔位字串 `PENDING: DR-2 037 正式報告檔名` 加刪除線並註記
「DR-2 本身不受影響 —— 037 身分仍未定，仍隨 RD-1 上問」。

**此處值得記一句**：被撤回的是**分析層自己**於 `05Z` 所作之訂正，
而該訂正當時的理由（canon §8.4.3）在條文層面並沒有錯 —— 錯的是
**射程判斷**（把逐列 TC 欄之規則套到工作簿層之表頭格）。
規則正確、適用範圍錯誤，是與「規則錯誤」不同的一種失效。

### 2.2 A-TM24 結案之依據鏈

三個來源中，來源 1（母本 S 欄 DV）於 `05Z` 實測**不成立**（S 欄不在任何
DV 之 sqref 內）；本次取用**來源 2**（既定慣例），且有第二條獨立證據
同向（037 Categorization 22/22 皆 `Functional`，SYS2 與 037 皆無
ASIL / FTTI 欄）。來源 3（Pei 裁）未動用。

**「標記掛錯條文」之部分亦一併結清**：`TODO(R-TM10-A1)` 已撤除，
改為指向 R-TM57 之註解，並寫明「值與 Privacy 之 R30-3 巧合相同但依據
不同」——使日後讀者不會把本 feature 之實測結論誤判為援引他 feature。

---

## 3. A-TM25 —— 二項牴觸複驗成立，但量值都更嚴重

| 項 | 分析層 | 執行層複驗 |
|---|---|---|
| (a) 彎引號 `“…”` | 「用 `“All Profiles”`」（未給數） | **436 處**（J 44 / L 200 / M 192）；**直雙引號 0 處** |
| (b) `check whether` | 7 次 | **11 處、10 列**（全在 L 欄 test_procedure） |

**(a) 的性質與分析層之描述不同**：不是「有些地方用了彎引號」，而是
**直雙引號在五個文字欄中一次都沒出現**。交付件在此項上並非混用，
而是整體採用另一套形式。這使 A-TM25 之影響面比原判為大：本 feature
若依 canon 用直引號，差異會出現在**每一條含 UI 標籤的 TC**，而非零星幾條。

**(b) 之逐處明細**（R-TM31：列出不只計數）：

```
列98  L: 4. Read the screen and check whether the popup is displayed
列100 L: 2. Read the screen and check whether the popup is displayed
列102 L: 2. Read the screen and check whether the popup is displayed
列103 L: 4. Read the screen and check whether the popup is displayed
列104 L: 2. Read the screen and check whether the popup is displayed
列104 L: 4. Read the screen and check whether the popup is displayed   ← 同列兩處
列105 L: 2. Read the screen and check whether the popup is displayed
列116 L: 3. Read the Next button and check whether it is available
列123 L: 2. Read the count and check whether it reaches ten
列128 L: 3. Read the status bar and check whether the icon changed
列130 L: 4. Read the username field and check whether it matches step 1
```

11 處分佈於 10 列（列 104 有兩處）。分析層之 7 很可能來自「相異字串」
或單欄計數 —— 但兩種算法我都試不出 7，**故只回報差異，不臆測成因**。

**一項對分析層有利的補充**：canon §5.1 其餘禁用主要動詞
（`confirm whether`、`observe whether`、`see if`、`observe`、`verify`）
實測 **0 處**。交付件只在 `check whether` 這一項上牴觸 canon，
其餘措辭紀律良好 —— A-TM25 的範圍比「交付件與 canon 不合」窄得多。

**本條未化為 lint 判準**：措辭層之閘門仍在 `TODO(R-TM10-A1)` 下，
本包未逕行實作。現階段 (a)(b) 的遵守只靠生成期之 context 指示，
**無自動攔截**。列入未驗清單 A 區。

---

## 4. T3 / T4 —— 紅綠

### 4.1 T3 `CONST_FUNCTIONAL_SAFETY`（write_back 無自測入口，以獨立腳本實跑）

```
綠向：CONST_FUNCTIONAL_SAFETY = 'NA'
  unresolved = ['PLACEHOLDER_BODY', 'TC_ID_FORMAT']
  PASS —— 本項已不在 unresolved 內

紅向：暫改回 None → ['CONST_FUNCTIONAL_SAFETY', 'PLACEHOLDER_BODY', 'TC_ID_FORMAT']
  PASS —— 檢查未被削弱，仍攔得住

紅向 2（自加）：值改為空字串 '' → ['PLACEHOLDER_BODY', 'TC_ID_FORMAT']
  空字串**不**被攔（判準為 `v is None`）—— 現行檢查之已知射程，
  非本包引入。列入未驗清單 A 區。
```

**下放包 T3 稱綠向為「unresolved 檢查不再攔」—— 此描述不準確**：
`--write` **仍被攔**，因 unresolved 尚有另兩項。準確的綠向是
「`CONST_FUNCTIONAL_SAFETY` 已不在 unresolved 清單內」，我以此為判準。
其後果見 §5。

### 4.2 T4 `lint_d5_scope`（一綠四紅，全通過）

```
PASS B1 綠向 (D5 為空 → 不報): 未誤報
PASS B1 紅向 (A-H26 形態：他 feature 之 037 檔名) → spec-scope-pending
PASS B1 紅向 (以 feature 名組值（R-TM9-A2 所禁）) → d5-scope
PASS B1 紅向 (填 NA（canon §8.4.3：NA 僅限確認不適用）) → d5-scope
PASS B1 紅向 (殘留之 PENDING 佔位（R-TM58 撤回）) → spec-scope-pending
```

紅向以**新建之臨時工作簿**構造（`tempfile.TemporaryDirectory` 內
`openpyxl.Workbook()` 新建後 `save`），**未對任何既有工作簿存回** ——
禁令針對的是以 openpyxl 存回母本／交付件而破壞 x14 dropdown，
新建臨時檔不在其射程內。此點刻意說明，以免被誤讀為違反禁令。

**新增 `D5_037_RE` 只判形態不判歸屬**，理由寫在註解裡：
「是 037 檔名」不等於「是**本**工作簿之 037」—— A-H26 的缺陷值本身
就是一個形態完全合法的 037 檔名。故該支路報 `spec-scope-pending`
（須人工確認歸屬）而非放行。若只判形態就放行，A-H26 這類缺陷會漏網。

**一項連帶效果**：改判前 D5 空必報 `d5-scope`，lint 主流程之
`return 1 if any(...)` 因而**恆為 1**；改判後 D5 空即零發現，主流程
`exit=0`。這是判準改變的必然結果，本包未另行更動主流程。

---

## 5. **B1 之啟動不只等 §3.4** —— 兩個死常數擋在前面

下放包 §5 稱「A-TM24 與 R-TM10-A1 兩項阻塞，本包後皆解除。
**B1 之啟動只等 §3.4 過目。**」**實測不成立。**

```
$ grep -n "TC_ID_FORMAT\|PLACEHOLDER_BODY" write_back.py
  17: （docstring 中之說明）
  67: PLACEHOLDER_BODY = None
  70: TC_ID_FORMAT = None
 325: ("PLACEHOLDER_BODY", PLACEHOLDER_BODY),
 326: ("TC_ID_FORMAT", TC_ID_FORMAT)) if v is None]
```

**兩者只出現在「宣告」與「unresolved 檢查」之中，從不被讀用。**

真正被使用的 tc_id 格式來自 `feature.yaml`：

```yaml
  tc_id_format: "NR1L-TimeAndDate-{n:03d}"   # R-TM32
```

`write_rows` 讀的是 `cfg["write_back"]["tc_id_format"]`，**不是**模組層
的 `TC_ID_FORMAT`。也就是說：

- `TC_ID_FORMAT` 之值**早已由 R-TM32 裁定並落在 feature.yaml**，
  模組層那個 `None` 是**未同步的殘留**，卻仍會使 `--write` raise
- `PLACEHOLDER_BODY` 尚無任何使用點（BLOCKED 佔位之寫入路徑未實作）

**故 `--write` 現在被兩個不影響任何實際輸出的常數擋著。**

**執行層未逕改**：撤除或改寫這兩個常數等於變更 `TODO(R-TM10-A1)` 之
處置範圍，屬條文範圍（R-TM29：R-TM10-A1 拘束 TC 內容，不拘束工具 ——
但「這兩個標記該不該撤」本身是條文問題）。**提請裁定**，三個選項：

| 選項 | 內容 |
|---|---|
| (a) | `TC_ID_FORMAT` 刪除（死碼），`PLACEHOLDER_BODY` 保留 TODO 但移出 unresolved（因無使用點，其未決不影響任何寫入） |
| (b) | `TC_ID_FORMAT` 改為自 `feature.yaml` 讀入以消除雙來源；`PLACEHOLDER_BODY` 同 (a) |
| (c) | 兩者皆維持，B1 之寫回延後至各自條文定案 |

**執行層傾向 (b)**：雙來源（模組常數 + yaml）本身即是本 feature 一路在
防的漂移形態 —— 現在恰好是「一處已裁定、另一處還是 None」，而 lint 不會
發現，因為兩處從不比對。(a) 直接刪除也可，但會失去「這裡曾經有個值」的
痕跡。**此為技術面意見，選擇權在分析層／Pei。**

---

## 6. T6 —— `tm_constants.py` **未建**（依令），技術面意見

依指令**未建檔**。以下**只就技術面**（措辭是否可執行、是否有遺漏之高頻
情境）陳述，不就內容是否恰當表態。

### 6.1 措辭可執行性 —— 一項存疑

| 常數 | 意見 |
|---|---|
| `GPS_LOST = 'Remove the GPS antenna to make the GPS signal unavailable'` | **存疑**：Bench 環境是否有可拔除之 GPS 天線，未經確認。若實車有而 Bench 無，此步驟在 Bench 上不可執行。替代做法（GPS 模擬器設為無效、遮蔽罩）之可用性同樣未知 —— **這是設備問題，不是措辭問題**，須向測試團隊確認。`GPS_RESTORE` 同 |
| `CAN_SLEEP = 'Wait until the CAN bus enters sleep'` | 「wait until」無可觀察之終止條件，測試者無從判斷何時算完成。canon §5.1 要求可執行；建議補上判準（如診斷工具之匯流排狀態），但**該判準涉 CAN 網段細節，不得杜撰**——故此處只指出缺口 |
| `KEY_OFF` / `KEY_ON` 與 `BATTERY_RECONNECT` | 三者可執行，措辭清楚。但 **018 需要區分之情境有三種**（reset、斷電、點火循環），常數只涵蓋後兩種，缺 **ECU reset**（軟體重置，不斷電）。若 018 之 TC 需測 reset，無常數可用 |
| `READ_HU_TIME` / `READ_IPC_TIME` | 措辭合 §5.1（`Read … and record it`，`record` 為 preferred verb）。可執行 |
| 其餘（`SET_TIME_MANUAL`、`SET_DATE_MANUAL`、`GPS_SYNC_ON/OFF`） | 無技術問題，直引號、無句尾句點、動作+目標齊備 |

### 6.2 遺漏之高頻情境 —— 以 22 片之描述關鍵詞實測

| 情境 | 命中之片 | §3.4 有無對應常數 |
|---|---|---|
| 時區 / DST | **003、012、013**（3 片）| **無** |
| 12H/24H 格式切換 | **005、011**（2 片）| **無** |
| Master Clock 同步源選擇 | 002、020 | 無（`GPS_SYNC_ON/OFF` 只涵蓋 GPS 一種來源）|
| 手動設定 | 001、015 | 有 |
| GPS | 001–005、012、014、015、019 | 有 |
| CAN 傳輸 | 006、008、009、010、014、020 | 部分（sleep/wake 有，訊號送出無）|
| reset / 斷電 | 008、011、018、021 | 部分（缺 ECU reset）|

**最大缺口為時區 / DST**：三片（003 / 012 / 013）皆涉之，且 `Zone and DST`
是 Part VII 七個 Test Set 中的一整組，而 §3.4 **一個相關常數都沒有**。
其次是 **12H/24H 格式切換**（005 / 011 兩片，`Display` 組之核心）。

此二者不是措辭問題而是**覆蓋問題**：即使 §3.4 原樣通過，這五片的步驟
仍須逐 TC 自寫，常數表對其零助益。**建議補入，但擬定屬分析層。**

### 6.3 ER 不擬樣板 —— 同意，且補一項技術理由

下放包稱「樣板化會誘導套用而非依實際結果撰寫」。技術面另有一項支持：
`lint_step_er_count` 要求步驟數與 ER 行數 **1:1**，若 ER 樣板化，
違反 1:1 的方式會變成「湊行數」而非「補結果」，該閘會全綠而內容仍錯。
**這正是本 feature 反覆遇到的「結構通過而內容空洞」形態。**

---

## 7. T5 —— design_method 雙語字串逐字比對

母本 `下拉選單` A 欄 **9 條**（全集，R-TM31：列出不只計數）：

```
  A1: '功能測試 (Functional based ; no specific technique)'
  A2: '狀態轉換 (State Transition Testing)'
  A3: '決策表 (Decision Table Testing)'
  A4: '等價劃分 (Equivalence Partitioning, EP)'
  A5: '邊界值分析 (Boundary Value Analysis, BVA)'
  A6: '組合測試 (Combinatorial Testing ; Pairwise / t-wise)'
  A7: '情境 / 用例 (Scenario / Use Case Testing)'
  A8: '負向測試 (Negative / Invalid)'
  A9: '基礎故障注入 (Fault Injection Lite)'
```

交付件 R 欄實測 **6 種**（全集，含次數）：

```
  ×120  '功能測試 (Functional based ; no specific technique)'   → 母本 A1
  ×33   '狀態轉換 (State Transition Testing)'                   → 母本 A2
  ×16   '負向測試 (Negative / Invalid)'                         → 母本 A8
  ×9    '情境 / 用例 (Scenario / Use Case Testing)'              → 母本 A7
  ×8    '邊界值分析 (Boundary Value Analysis, BVA)'              → 母本 A5
  ×3    '基礎故障注入 (Fault Injection Lite)'                    → 母本 A9
```

**逐字比對：6/6 皆 IN 母本；子集成立 = True。**
母本有而交付件未用之 3 條：`決策表`、`等價劃分`、`組合測試`。

**位元組層級複驗**（逐字相同不等於位元組相同 —— 全形空格、NBSP、
不同的破折號在畫面上難分）：

```
交付 '功能測試 (Functi…'  e58a9f...6e6f2073706563
母本 A1                    e58a9f...6e6f2073706563   相同=True
交付 '基礎故障注入 (Faul…' e59fba...204c697465
母本 A9                    e59fba...204c697465       相同=True
```

**結論：我方 lint 之 `design_method` 詞彙表取自母本 `下拉選單` 為正確
來源**，且該來源與最近一次交付件之實際用值完全相容。T5 之停止條件未觸發。

---

## 8. T7 —— 驗證輸出（R-TM31：列明細）

```
(1) grep -n '^## R-TM5[78]' RULINGS.md
    2273:## R-TM57 — functional_safety = "NA"
    2308:## R-TM58 — D5 維持空白，撤回 PENDING 佔位

(2) grep -n '^| A-TM24\|^| A-TM25' ANOMALIES.md
    36:| A-TM24 | … | **RESOLVED**（R-TM57）| Tier 2 |
    37:| A-TM25 | 既有交付件與 canon 兩處牴觸（彎引號、check whether）| PENDING | Tier 2（呈 Pei）|

(3) grep -n 'CONST_FUNCTIONAL_SAFETY' write_back.py
    16   docstring：「不繼承其內容：Privacy 之 … (R30-3)」（原文，未改）
    64   CONST_FUNCTIONAL_SAFETY = "NA"          ← 本包
    223  ws.cell(..., value=CONST_FUNCTIONAL_SAFETY)   ← 實際寫入點
    324  unresolved 檢查

(5) lint_tcs --self-test          自驗：31 / 31
    （07 之 26 → +1 綠向 +4 紅向 = 31）
(6) build_batch_context --self-test   自驗：13 / 13
(7) lint 主流程（無 generated/）  exit=0   ← R-TM58 之連帶效果，見 §4.2
```

### 8.1 `TODO(R-TM10-A1)` 逐處列出並判定各自依據（T7 第 4 項）

| # | 位置 | 依據判定 |
|---|---|---|
| 1 | `write_back.py:18` docstring | **陳述句，非標記**。描述「Privacy 之三常數為其自身裁決」。已隨 §64 之改動而部分過時 —— `CONST_FUNCTIONAL_SAFETY` 已決。**建議下包修訂措辭** |
| 2 | `write_back.py:66` `PLACEHOLDER_BODY` | **標記正確但已無作用** —— 無使用點（§5） |
| 3 | `write_back.py:69` `TC_ID_FORMAT` | **標記已失效** —— 值已由 R-TM32 裁定並落在 feature.yaml（§5） |
| 4 | `write_back.py:74` C 欄 Polarion ID | **正確** —— 本 feature 有無 Polarion 匯出仍未定 |
| 5 | `write_back.py:77` Q 欄 Estimated Test Time | **正確** —— 待條文 |
| 6 | `write_back.py:78` T–Z 車型欄 | **正確** —— 待條文 |
| 7 | `write_back.py:328` unresolved 之列印字串 | **措辭已不精確** —— 該清單現含之兩項與 R-TM10-A1 之關係已變（§5） |
| 8 | `lint_tcs.py:13` docstring | **部分過時** —— Test Set 值（C1）與 priority 值域（C2）皆已實作，docstring 仍稱「一律留 TODO」 |
| 9 | `lint_tcs.py:279` | **已是結案註記**（記載該標記為何過時），非未決項 |
| 10 | `lint_tcs.py:507` 步驟措辭閘門 | **正確且現在更重要** —— A-TM25 之 (a)(b) 若要自動攔截，落點即此 |
| 11 | `lint_tcs.py:512` C1 | **已是結案註記** |
| 12 | `lint_tcs.py:518` priority 分佈 | **標記為 `TODO(內容裁決)` 而非 R-TM10-A1**，且註解已明寫二者之區分。正確 |
| 13 | `lint_tcs.py:521` Input Test Data 填法 | **正確** —— 交付件之 159/189 = NA 為佐證，但填法之條文未定，未逕行實作 |

**十三處中，四處已過時或失效**（#1 #3 #7 #8），**兩處已無作用**（#2 #3），
**七處仍正確**。過時者皆為本包及先前各包之進展所致，非原始錯誤。
**執行層未逕改任何一處** —— 撤除 TODO 標記屬條文範圍。

---

## 9. 未驗清單（R-TM54 三分）

### A. 可驗而未驗 —— 執行層能清

| # | 項目 | 說明 |
|---|---|---|
| A1 | A-TM25 (a)(b) 無自動攔截 | 措辭閘門在 `TODO(R-TM10-A1):507` 下未實作。現階段只靠 context 指示 |
| A2 | unresolved 檢查對空字串無效 | 判準為 `v is None`，`""` 漏網（§4.1 紅向 2）。修法明確，但屬 write_back 之檢查邏輯，未逕改 |
| A3 | B-1 / B-2 及 B-3、B-5 未守之側 | 07 遺留。仍待 B1 pilot 檢查表，該表尚未產出 |
| A4 | 018 / 017 之 objects 未逐一複驗 | 07 遺留，本包未及 |
| A5 | `BOUNDARY_NOTES` 與 `BOUNDARY_SIGNALS` 對 018 之並存 | 07 遺留 |
| A6 | 交付件之 pre_conditions / ER 形式慣例（逐條編號、無句尾句點）未逐條驗 | 本包只驗了 §3.1 表中之引號與動詞二項，其餘形式項採信分析層 |

### B. 結構性不可複驗 —— 待 Pei

| # | 項目 |
|---|---|
| B1 | A-TM25：本 feature 依 canon 而與既有交付件外觀不同 —— 是否接受 |
| B2 | §3.4 步驟常數表之過目（含 §6 所列之三項技術意見） |
| B3 | §5 兩個死常數之處置（(a)/(b)/(c) 三選項）|
| B4 | RD-1 之送出 |

### C. 已解決 —— 註明包號後移除

| # | 項目 | 解決於 |
|---|---|---|
| C1 | `functional_safety` 之值（A-TM24）—— 07 包之 B 區第 1 項 | 本包 T3（R-TM57） |
| C2 | D5 之填法 —— 05Z 訂正之正確性存疑 | 本包 T4（R-TM58） |
| C3 | R-TM10-A1「無適用之既有常數」之證實 | 下放包 §3.2（交付件高頻步驟全為 User Profiles 專屬 UI）—— **執行層未複驗此項**，採信分析層之實測 |

**07 之 B 區第 2 項（R-TM10-A1 步驟措辭）狀態變更**：由「待 Pei 決定
解凍或自訂」變為**已確定自訂**（下放包 §3.2 證實無可抄者），但**擬定尚未完成**
—— §3.4 為 [PROPOSED]，故移入本包 B 區第 2 項而非 C 區。

---

## 10. 未執行者（下放包所禁，逐項確認）

- 未生成任何 TC
- **未建 `tm_constants.py`**
- 未修改既有交付件（**唯讀載入，未寫入**）
- 未改 `backend/`、canon、`docs/fw036/framework.md`
- 未將 022 加入 `BOUNDARY_SIGNALS`（R-TM55；lint 之陰性對照仍在，31/31 含該項）
- 未杜撰 CAN 網段（§6.1 之 `CAN_SLEEP` 缺口只指出，未補判準）
- 未碰 `features/vehicle_setting/`
- 未送出 RD-1
- 未動 git（R-TM36：待 Pei 直接指示）
- 未以 openpyxl 存回任何既有工作簿（§4.2 之臨時檔為新建，非存回）

---

## 11. 提請裁定

1. **§5 —— B1 之啟動不只等 §3.4**。`TC_ID_FORMAT` / `PLACEHOLDER_BODY`
   為死常數卻擋著 `--write`。三選項見 §5，執行層傾向 (b)。
2. **§3 —— A-TM25 之量值**：(a) 436 處且直引號 0 處（非混用而是整體
   採另一套形式）；(b) 11 處而非 7 處。是否更新 A-TM25 之條文區塊。
3. **§6.2 —— §3.4 之覆蓋缺口**：時區/DST（3 片）與 12H/24H 格式（2 片）
   無任何對應常數，`Zone and DST` 為七個 Test Set 之一整組。
4. **§6.1 —— `GPS_LOST` 之可執行性**與 `CAN_SLEEP` 之終止條件，
   須向測試團隊確認設備，非措辭可解。
5. **§8.1 —— 十三處 `TODO(R-TM10-A1)` 中四處已過時**，是否指派修訂。
