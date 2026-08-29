# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/batch6/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
- 資料列數：16
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
| J | 行首大寫 | 1 | 1 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 27 | 9 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 14 | 14 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 9 | 9 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 51**（列計不加總——同一列可觸發多項檢查）

## 明細

### J — 行首大寫（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 25 | newR1L-SU-081 | test_item | 首字小寫 'he' | he WiFiUpdateService shall ensure that sufficient physical storage space is avai |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 27／列計 9）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-066 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package whose digital signature |
| 10 | newR1L-SU-066 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package whose digital signature or |
| 10 | newR1L-SU-066 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged deployment package has an |
| 11 | newR1L-SU-067 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a differential deployment package whose decl |
| 11 | newR1L-SU-067 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a differential deployment package whose declare |
| 11 | newR1L-SU-067 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged differential package decl |
| 12 | newR1L-SU-068 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the invocation of the signature verificati |
| 12 | newR1L-SU-068 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the invocation of the signature verification  |
| 12 | newR1L-SU-068 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the invocation of the signature verifi |
| 13 | newR1L-SU-069 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package containing multiple upd |
| 13 | newR1L-SU-069 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package containing multiple update |
| 13 | newR1L-SU-069 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that one contained update file of the sta |
| 14 | newR1L-SU-070 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging an OMA-DM message that fails integrity verif |
| 14 | newR1L-SU-070 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage an OMA-DM message that fails integrity verifica |
| 14 | newR1L-SU-070 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the head unit received an OMA-DM mes |
| 15 | newR1L-SU-071 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the stored format of the DM Tree |
| 15 | newR1L-SU-071 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the stored format of the DM Tree |
| 15 | newR1L-SU-071 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the stored format of the DM Tree |
| 16 | newR1L-SU-072 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package whose content fails int |
| 16 | newR1L-SU-072 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package whose content fails integr |
| 16 | newR1L-SU-072 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged deployment package fails  |
| 17 | newR1L-SU-073 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package that fails authenticity |
| 17 | newR1L-SU-073 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package that fails authenticity ve |
| 17 | newR1L-SU-073 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged deployment package fails  |
| 22 | newR1L-SU-078 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the vehicle conditions passed from the WiF |
| 22 | newR1L-SU-078 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the vehicle conditions passed from the WiFiUp |
| 22 | newR1L-SU-078 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the vehicle conditions passed from the |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 14／列計 14）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-066 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | newR1L-SU-067 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | newR1L-SU-068 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | newR1L-SU-069 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | newR1L-SU-070 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-071 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | newR1L-SU-072 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | newR1L-SU-073 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | newR1L-SU-075 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | newR1L-SU-076 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-077 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | newR1L-SU-078 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | newR1L-SU-079 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | newR1L-SU-081 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### W — ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）（行計 9／列計 9）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-066 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged deployment package h |
| 11 | newR1L-SU-067 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged differential package |
| 13 | newR1L-SU-069 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while one contained update file of th |
| 14 | newR1L-SU-070 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the head unit received an OMA-D |
| 16 | newR1L-SU-072 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged deployment package f |
| 17 | newR1L-SU-073 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged deployment package f |
| 20 | newR1L-SU-076 | er | 比較關係 'equals'，而 test_item 上半無數值 | d and Version_after equals Version_initial |
| 21 | newR1L-SU-077 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while one of the two configured condi |
| 25 | newR1L-SU-081 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 4. Version_after equals Version_initial while the space left on the head unit |

