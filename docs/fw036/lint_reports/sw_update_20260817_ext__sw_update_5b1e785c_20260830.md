# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/batch9/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
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
| U | PENDING 佔位（四欄全掃，含 ER 側） | 50 | 12 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 10 | 10 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 60**（列計不加總——同一列可觸發多項檢查）

## 明細

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 50／列計 12）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-123 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the times at which  |
| 10 | newR1L-SU-123 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the polling times recorded on the OTA Server for |
| 10 | newR1L-SU-123 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the polling times recorded on the OT |
| 11 | newR1L-SU-124 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of setting and of reading the polling interval configur |
| 11 | newR1L-SU-124 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to set the polling interval configuration parameter to a |
| 11 | newR1L-SU-124 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to change the polling interval configuration parameter t |
| 11 | newR1L-SU-124 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the polling interval configuration p |
| 11 | newR1L-SU-124 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the polling interval configuration p |
| 12 | newR1L-SU-125 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the queue of vehicle-initiated OTA session |
| 12 | newR1L-SU-125 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of vehicle-initiated OTA sessions afte |
| 12 | newR1L-SU-125 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that a vehicle-initiated OTA session is h |
| 13 | newR1L-SU-126 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the queue of OTA update sessions held by t |
| 13 | newR1L-SU-126 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of OTA update sessions while the batte |
| 13 | newR1L-SU-126 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read the queue of OTA update sessions after the batte |
| 13 | newR1L-SU-126 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the session is held in the queue whi |
| 13 | newR1L-SU-126 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence that the session leaves the queue once th |
| 14 | newR1L-SU-127 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 14 | newR1L-SU-127 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 14 | newR1L-SU-127 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the OTA Server started a session tow |
| 14 | newR1L-SU-127 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 comparison of the screens of the server-started session with  |
| 15 | newR1L-SU-128 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of sending a software inventory request from the OTA Se |
| 15 | newR1L-SU-128 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the software invent |
| 15 | newR1L-SU-128 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send a complete software inventory request from the O |
| 15 | newR1L-SU-128 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the software inventory received by the OTA Serve |
| 15 | newR1L-SU-128 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the software inventory request reach |
| 15 | newR1L-SU-128 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the software inventory received by the |
| 16 | newR1L-SU-129 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the order in which the Deployment Descript |
| 16 | newR1L-SU-129 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the order in which the Deployment Description an |
| 16 | newR1L-SU-129 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the Deployment Description was downl |
| 18 | newR1L-SU-131 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the vehicle and system data handed from th |
| 18 | newR1L-SU-131 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the vehicle and system data handed to the SWMC f |
| 18 | newR1L-SU-131 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the vehicle and system data handed to  |
| 19 | newR1L-SU-132 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the notification sent from the SWMC to the |
| 19 | newR1L-SU-132 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the notification sent to the WiFiUpdateService a |
| 19 | newR1L-SU-132 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the notification sent to the WiFiUpdat |
| 20 | newR1L-SU-133 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 20 | newR1L-SU-133 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 20 | newR1L-SU-133 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a server-started update flow is runn |
| 21 | newR1L-SU-134 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 21 | newR1L-SU-134 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of distinguishing this queueing from the one verified b |
| 21 | newR1L-SU-134 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 21 | newR1L-SU-134 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of OTA session requests received throu |
| 21 | newR1L-SU-134 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request arrived through th |
| 21 | newR1L-SU-134 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this queued request from t |
| 22 | newR1L-SU-135 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 22 | newR1L-SU-135 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of distinguishing this session from the one verified by |
| 22 | newR1L-SU-135 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 22 | newR1L-SU-135 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to compare the screens of that session with those of a h |
| 22 | newR1L-SU-135 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the session was started through the  |
| 22 | newR1L-SU-135 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this session from the one  |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 10／列計 10）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-123 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | newR1L-SU-124 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | newR1L-SU-126 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-128 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | newR1L-SU-129 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | newR1L-SU-131 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | newR1L-SU-132 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | newR1L-SU-133 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-134 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | newR1L-SU-135 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

