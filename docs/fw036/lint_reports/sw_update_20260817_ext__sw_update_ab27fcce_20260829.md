# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/batch5/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
- 資料列數：12
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
| U | PENDING 佔位（四欄全掃，含 ER 側） | 18 | 5 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 7 | 7 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 2 | 2 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 27**（列計不加總——同一列可觸發多項檢查）

## 明細

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 18／列計 5）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | newR1L-SU-056 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 12 | newR1L-SU-056 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the network bearer used for the download afte |
| 12 | newR1L-SU-056 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network bearer used for the downlo |
| 14 | newR1L-SU-058 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 14 | newR1L-SU-058 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the network bearer used for the download whil |
| 14 | newR1L-SU-058 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network bearer used for the downlo |
| 15 | newR1L-SU-059 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 15 | newR1L-SU-059 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the network bearer used for the resumed downl |
| 15 | newR1L-SU-059 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network bearer used for the resume |
| 16 | newR1L-SU-060 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reaching the end of the one week Wi-Fi attempt perio |
| 16 | newR1L-SU-060 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 16 | newR1L-SU-060 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to reach the end of the one week Wi-Fi attempt period |
| 16 | newR1L-SU-060 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to observe the network bearer used for the download afte |
| 16 | newR1L-SU-060 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable state showing that the Wi-Fi attempt period has el |
| 16 | newR1L-SU-060 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the network bearer used for the downlo |
| 17 | newR1L-SU-061 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing a critical update session from a sile |
| 17 | newR1L-SU-061 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to observe that the session in progress is a critical up |
| 17 | newR1L-SU-061 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the session in progress is a critica |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 7／列計 7）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-054 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | newR1L-SU-055 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | newR1L-SU-056 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | newR1L-SU-058 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-059 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | newR1L-SU-060 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-065 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### W — ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）（行計 2／列計 2）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-054 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ed ⏎ 4. Version_after differs from Version_initial while no configured Wi-Fi netwo |
| 16 | newR1L-SU-060 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ad ⏎ 5. Version_after differs from Version_initial after the Wi-Fi attempt period |

