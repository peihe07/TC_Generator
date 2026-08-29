# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/probe_all17/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
- 資料列數：17
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`sw_update`（P 採 R-1 v3；另跑 Q／R／T）

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 0 | 0 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item 括號下半) | 0 | 0 | 每次命中 | 已校準（R-6b 範圍：Media 錨值 1→0） |
| D | PC 違規 (pre) | 0 | 0 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 0 | 0 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 0 | 0 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 0 | 0 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 20 | 7 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 20 | 15 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |

**總計：行計 40**（列計不加總——同一列可觸發多項檢查）

## 明細

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 20／列計 7）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | newR1L-SU-003 | pre | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 list of safety-related notification conditions applicable dur |
| 12 | newR1L-SU-003 | proc | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 step to bring one safety-related condition into effect |
| 12 | newR1L-SU-003 | er | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 observable state showing the safety-related condition is in e |
| 17 | newR1L-SU-008 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of identifying the boundaries between the update check, |
| 17 | newR1L-SU-008 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to record the head unit screen content with the check, d |
| 17 | newR1L-SU-008 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence delimiting the check, download and instal |
| 18 | newR1L-SU-009 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of distinguishing the automatic download request from t |
| 18 | newR1L-SU-009 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe that the deployment package download request  |
| 18 | newR1L-SU-009 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the download request has been issued |
| 19 | newR1L-SU-010 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to observe the point at which deployment package downloa |
| 19 | newR1L-SU-010 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the download completion point |
| 20 | newR1L-SU-011 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of injecting a socket read or write error during OTA se |
| 20 | newR1L-SU-011 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to inject a socket read or write error during the update |
| 20 | newR1L-SU-011 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the socket error has occurred |
| 23 | newR1L-SU-014 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of placing the vehicle into the emergency state (accide |
| 23 | newR1L-SU-014 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to place the vehicle into the emergency state while the  |
| 23 | newR1L-SU-014 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the vehicle is in the emergency stat |
| 26 | newR1L-SU-017 | pre | PENDING 佔位（DR-SU3） | 3. PENDING: DR-SU3 upstream confirmation whether this requirement's verification |
| 26 | newR1L-SU-017 | proc | PENDING 佔位（DR-SU3） | 1. PENDING: DR-SU3 step to exercise the coordination behaviour separately from t |
| 26 | newR1L-SU-017 | er | PENDING 佔位（DR-SU3） | 1. PENDING: DR-SU3 observable outcome attributable to the coordination behaviour |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 20／列計 15）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-001 | expected_result | 與 newR1L-SU-002 之觀測窗相同（availability-check → version-change）且違例類有交集 | progress-notification |
| 10 | newR1L-SU-001 | expected_result | 與 newR1L-SU-008 之觀測窗相同（availability-check → version-change）且違例類有交集 | progress-notification／prompt |
| 11 | newR1L-SU-002 | expected_result | 與 newR1L-SU-001 之觀測窗相同（availability-check → version-change）且違例類有交集 | progress-notification |
| 11 | newR1L-SU-002 | expected_result | 與 newR1L-SU-008 之觀測窗相同（availability-check → version-change）且違例類有交集 | progress-notification |
| 12 | newR1L-SU-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | newR1L-SU-005 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-006 | expected_result | 與 newR1L-SU-008 之觀測窗相同（availability-check → version-change）且違例類有交集 | confirmation-screen |
| 16 | newR1L-SU-007 | expected_result | 與 newR1L-SU-008 之觀測窗相同（availability-check → version-change）且違例類有交集 | confirmation-screen |
| 17 | newR1L-SU-008 | expected_result | 與 newR1L-SU-001 之觀測窗相同（availability-check → version-change）且違例類有交集 | progress-notification／prompt |
| 17 | newR1L-SU-008 | expected_result | 與 newR1L-SU-002 之觀測窗相同（availability-check → version-change）且違例類有交集 | progress-notification |
| 17 | newR1L-SU-008 | expected_result | 與 newR1L-SU-006 之觀測窗相同（availability-check → version-change）且違例類有交集 | confirmation-screen |
| 17 | newR1L-SU-008 | expected_result | 與 newR1L-SU-007 之觀測窗相同（availability-check → version-change）且違例類有交集 | confirmation-screen |
| 18 | newR1L-SU-009 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | newR1L-SU-011 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-012 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | newR1L-SU-013 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | newR1L-SU-014 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | newR1L-SU-015 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | newR1L-SU-016 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | newR1L-SU-017 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

