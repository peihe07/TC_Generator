# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/batch13/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
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
| U | PENDING 佔位（四欄全掃，含 ER 側） | 58 | 15 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 13 | 13 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 71**（列計不加總——同一列可觸發多項檢查）

## 明細

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 58／列計 15）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-180 | pre | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 observable indication on the head unit that the OTA client co |
| 10 | newR1L-SU-180 | proc | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 check that the session continued from the state it held when  |
| 10 | newR1L-SU-180 | er | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 observable evidence that the session continued from its previ |
| 11 | newR1L-SU-181 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading, on the OTA Server side, the failure reporte |
| 12 | newR1L-SU-182 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of sending an NIA to this head unit during an active se |
| 12 | newR1L-SU-182 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the queue of received NIAs |
| 12 | newR1L-SU-182 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to send an NIA to the head unit while the session is act |
| 12 | newR1L-SU-182 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read whether the NIA was processed only after the ses |
| 12 | newR1L-SU-182 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that an NIA arrived during the active ses |
| 12 | newR1L-SU-182 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the NIA was processed after the sess |
| 13 | newR1L-SU-183 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the partially downloaded deployment packag |
| 13 | newR1L-SU-183 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read whether the partially downloaded package is stil |
| 13 | newR1L-SU-183 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the partially downloaded package is  |
| 14 | newR1L-SU-184 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the log entry recorded for an interruption |
| 14 | newR1L-SU-184 | pre | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable indication that the session is suspended rather th |
| 14 | newR1L-SU-184 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the log entry recorded for the interruption |
| 14 | newR1L-SU-184 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the log entry recorded for the interru |
| 15 | newR1L-SU-185 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the HTTP request used when a download is r |
| 15 | newR1L-SU-185 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the HTTP request the head unit used to resume th |
| 15 | newR1L-SU-185 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the resumed download used an HTTP by |
| 16 | newR1L-SU-186 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is verified by SWE1-FOT |
| 16 | newR1L-SU-186 | proc | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 step to verify this requirement separately from SWE1-FOTA-328 |
| 16 | newR1L-SU-186 | er | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 observable evidence separating this requirement from SWE1-FOT |
| 18 | newR1L-SU-188 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 value of the configured retry count for resuming an interrupt |
| 18 | newR1L-SU-188 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading the logged failure after the retry count is  |
| 18 | newR1L-SU-188 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to wait until the configured retry count is reached and  |
| 18 | newR1L-SU-188 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the session was aborted after the co |
| 19 | newR1L-SU-189 | pre | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 criterion by which a resumed installation is distinguished fr |
| 19 | newR1L-SU-189 | proc | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 check that the installation resumed from its saved state rath |
| 19 | newR1L-SU-189 | er | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 observable evidence that the installation resumed from its sa |
| 21 | newR1L-SU-191 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1 |
| 21 | newR1L-SU-191 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the saved download state |
| 21 | newR1L-SU-191 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to interrupt the download at a step other than the one u |
| 21 | newR1L-SU-191 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the saved download state for an interr |
| 22 | newR1L-SU-192 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the communication between the WiFiUpdateSe |
| 22 | newR1L-SU-192 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether communication with the TC client is esta |
| 22 | newR1L-SU-192 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that communication with the TC client is  |
| 23 | newR1L-SU-193 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the callback registration made with the TC |
| 23 | newR1L-SU-193 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the callback registration parameters used with t |
| 23 | newR1L-SU-193 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the callback was registered with the |
| 24 | newR1L-SU-194 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request through |
| 24 | newR1L-SU-194 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 24 | newR1L-SU-194 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request through th |
| 24 | newR1L-SU-194 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read that the request was forwarded to the SWMC for e |
| 24 | newR1L-SU-194 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request arrived through th |
| 24 | newR1L-SU-194 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the request was forwarded to the SWM |
| 25 | newR1L-SU-195 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request through |
| 25 | newR1L-SU-195 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading, on the OTA Server side, the availability ch |
| 25 | newR1L-SU-195 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request through th |
| 25 | newR1L-SU-195 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the availability check the SWMC made towards the |
| 25 | newR1L-SU-195 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request arrived through th |
| 25 | newR1L-SU-195 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the availability check made towards th |
| 26 | newR1L-SU-196 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request that ca |
| 26 | newR1L-SU-196 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the queue of received session requests |
| 26 | newR1L-SU-196 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request while it c |
| 26 | newR1L-SU-196 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of received session requests |
| 26 | newR1L-SU-196 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request could not be execu |
| 26 | newR1L-SU-196 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the request is held in the queue |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 13／列計 13）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-180 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | newR1L-SU-182 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | newR1L-SU-183 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | newR1L-SU-184 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-185 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | newR1L-SU-186 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | newR1L-SU-189 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-191 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | newR1L-SU-192 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | newR1L-SU-193 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | newR1L-SU-194 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | newR1L-SU-195 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | newR1L-SU-196 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

