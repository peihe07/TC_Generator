# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/batch15/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
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
| U | PENDING 佔位（四欄全掃，含 ER 側） | 42 | 12 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 12 | 12 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 54**（列計不加總——同一列可觸發多項檢查）

## 明細

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 42／列計 12）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-213 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the network availability notification sent |
| 10 | newR1L-SU-213 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the network availability notification sent from  |
| 10 | newR1L-SU-213 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network availability notification  |
| 11 | newR1L-SU-214 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the URL the SWMC used to download the depl |
| 11 | newR1L-SU-214 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 11 | newR1L-SU-214 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the URL the SWMC used to download the deployment |
| 11 | newR1L-SU-214 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the URL the SWMC used to download the  |
| 12 | newR1L-SU-215 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the Download Descriptor the SWMC read and  |
| 12 | newR1L-SU-215 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 12 | newR1L-SU-215 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Download Descriptor the SWMC read and the UR |
| 12 | newR1L-SU-215 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the Download Descriptor the SWMC read  |
| 13 | newR1L-SU-216 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which independence from the operating system and |
| 13 | newR1L-SU-216 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the storage went through the abstract  |
| 13 | newR1L-SU-216 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the storage was independent of the o |
| 14 | newR1L-SU-217 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the invocation of the Redbend Update Agent |
| 14 | newR1L-SU-217 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the invocation of the Redbend Update Agent for t |
| 14 | newR1L-SU-217 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the invocation of the Redbend Update A |
| 15 | newR1L-SU-218 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the protocol the SWMC used to communicate  |
| 15 | newR1L-SU-218 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 15 | newR1L-SU-218 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the protocol the SWMC used to communicate with t |
| 15 | newR1L-SU-218 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the protocol the SWMC used to communic |
| 16 | newR1L-SU-219 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the Download Descriptor processed when a p |
| 16 | newR1L-SU-219 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of configuring a proprietary communication protocol |
| 16 | newR1L-SU-219 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Download Descriptor processed when a proprie |
| 16 | newR1L-SU-219 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the Download Descriptor processed when |
| 17 | newR1L-SU-220 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the vehicle properties the WiFiUpdateServi |
| 17 | newR1L-SU-220 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the vehicle properties the WiFiUpdateService ret |
| 17 | newR1L-SU-220 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the vehicle properties the WiFiUpdateS |
| 18 | newR1L-SU-221 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the installer invoked for the installation |
| 18 | newR1L-SU-221 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 18 | newR1L-SU-221 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installer invoked for the installation metho |
| 18 | newR1L-SU-221 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the installer invoked for the installa |
| 19 | newR1L-SU-222 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the ECU reference IDs used to associate th |
| 19 | newR1L-SU-222 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the ECU reference IDs used to associate the upda |
| 19 | newR1L-SU-222 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the ECU reference IDs used to associat |
| 20 | newR1L-SU-223 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which portability with the Android operating sys |
| 20 | newR1L-SU-223 | proc | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 step to establish that the Redbend Update Agent is portable w |
| 20 | newR1L-SU-223 | er | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 observable evidence that the Redbend Update Agent is portable |
| 21 | newR1L-SU-224 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the OMA-DM protocol stack the SWMC used to |
| 21 | newR1L-SU-224 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 21 | newR1L-SU-224 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the OMA-DM protocol stack the SWMC used towards  |
| 21 | newR1L-SU-224 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the OMA-DM protocol stack the SWMC use |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 12／列計 12）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-213 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | newR1L-SU-214 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | newR1L-SU-215 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | newR1L-SU-216 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | newR1L-SU-217 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-218 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | newR1L-SU-219 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | newR1L-SU-220 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | newR1L-SU-221 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | newR1L-SU-222 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | newR1L-SU-223 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-224 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

