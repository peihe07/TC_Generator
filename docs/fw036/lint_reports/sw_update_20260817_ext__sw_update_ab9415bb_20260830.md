# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/batch8/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
- 資料列數：13
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
| U | PENDING 佔位（四欄全掃，含 ER 側） | 34 | 9 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 11 | 11 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 45**（列計不加總——同一列可觸發多項檢查）

## 明細

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 34／列計 9）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-110 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the session result  |
| 10 | newR1L-SU-110 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the session result recorded on the OTA Server fo |
| 10 | newR1L-SU-110 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read the session result recorded on the OTA Server fo |
| 10 | newR1L-SU-110 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the session result recorded on the OTA |
| 10 | newR1L-SU-110 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the session result recorded on the OTA |
| 11 | newR1L-SU-111 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the session reports |
| 11 | newR1L-SU-111 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read whether the session report of the interrupted se |
| 11 | newR1L-SU-111 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence that the session report of the interrupte |
| 12 | newR1L-SU-112 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement and SWE1-FOTA-331 are t |
| 12 | newR1L-SU-112 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to distinguish the resend verified here from the resend  |
| 12 | newR1L-SU-112 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this resend from the one v |
| 13 | newR1L-SU-113 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the retry attempts  |
| 13 | newR1L-SU-113 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 value of the configured retry parameter that governs the numb |
| 13 | newR1L-SU-113 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the retry attempts made for the unacknowledged s |
| 13 | newR1L-SU-113 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the retry attempts made for the unackn |
| 14 | newR1L-SU-114 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making an ECU reflash fail during the installation |
| 14 | newR1L-SU-114 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading, on the OTA Server side, the failure report  |
| 14 | newR1L-SU-114 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the ECU reflash fail during the installation |
| 14 | newR1L-SU-114 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the deployment package status code, the ECU faul |
| 14 | newR1L-SU-114 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the ECU reflash failed during the in |
| 14 | newR1L-SU-114 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the deployment package status code, th |
| 15 | newR1L-SU-115 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the update status c |
| 15 | newR1L-SU-115 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read the update status codes and software version inf |
| 15 | newR1L-SU-115 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the update status codes and software v |
| 16 | newR1L-SU-116 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the final software  |
| 16 | newR1L-SU-116 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 16 | newR1L-SU-116 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the final software update result received by the |
| 16 | newR1L-SU-116 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the final software update result recei |
| 19 | newR1L-SU-119 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the ignition cycle counter associated with F |
| 19 | newR1L-SU-119 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the ignition cycle counter while FOTA package da |
| 19 | newR1L-SU-119 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the ignition cycle counter while FOTA  |
| 22 | newR1L-SU-122 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reaching the state in which the FOTA package could n |
| 22 | newR1L-SU-122 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to reach the state in which the FOTA package could not b |
| 22 | newR1L-SU-122 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the FOTA package could not be downlo |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 11／列計 11）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-110 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | newR1L-SU-111 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | newR1L-SU-112 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | newR1L-SU-113 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | newR1L-SU-114 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-115 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | newR1L-SU-116 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | newR1L-SU-117 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | newR1L-SU-119 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | newR1L-SU-120 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | newR1L-SU-122 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

