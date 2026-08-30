# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/batch18/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
- 資料列數：16
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`sw_update`（P 採 R-1 v3；另跑 Q／R／T）

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 0 | 0 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 1 | 1 | 每次命中 | 已校準 |
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
| U | PENDING 佔位（四欄全掃，含 ER 側） | 39 | 9 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 9 | 9 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 49**（列計不加總——同一列可觸發多項檢查）

## 明細

### B — ER 情態詞 (er)（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 15 | newR1L-SU-260 | er | 情態詞 'should' | er that the vehicle should not be driven |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 39／列計 9）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-255 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the precondition evaluation the service pe |
| 10 | newR1L-SU-255 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1 |
| 10 | newR1L-SU-255 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the precondition evaluation the service performe |
| 10 | newR1L-SU-255 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the precondition evaluation the servic |
| 13 | newR1L-SU-258 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the installation failure status reported t |
| 13 | newR1L-SU-258 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of making an installation fail |
| 13 | newR1L-SU-258 | pre | PENDING 佔位（DR-SU3） | 6. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 13 | newR1L-SU-258 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installation failure status reported through |
| 13 | newR1L-SU-258 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the installation failure status report |
| 14 | newR1L-SU-259 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which eCall availability during an update is jud |
| 14 | newR1L-SU-259 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of exercising eCall on the bench without placing an eme |
| 14 | newR1L-SU-259 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that eCall functionality remained operation |
| 14 | newR1L-SU-259 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that eCall functionality remained operati |
| 16 | newR1L-SU-261 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the OTA session status the service set aft |
| 16 | newR1L-SU-261 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of making an installation fail |
| 16 | newR1L-SU-261 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the OTA session status the service set after an  |
| 16 | newR1L-SU-261 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the OTA session status the service set |
| 17 | newR1L-SU-262 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of producing a vehicle motion event while an installati |
| 17 | newR1L-SU-262 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to produce a vehicle motion event while the installation |
| 17 | newR1L-SU-262 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the installation continued without interruption |
| 17 | newR1L-SU-262 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of a vehicle motion event during the inst |
| 17 | newR1L-SU-262 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the installation continued without i |
| 19 | newR1L-SU-264 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the installation failure status reported b |
| 19 | newR1L-SU-264 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of making an installation fail |
| 19 | newR1L-SU-264 | pre | PENDING 佔位（DR-SU3） | 6. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 19 | newR1L-SU-264 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installation failure status reported by the  |
| 19 | newR1L-SU-264 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the installation failure status report |
| 20 | newR1L-SU-265 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the value set on $HUFOTACheck$ and its tra |
| 20 | newR1L-SU-265 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the value set on $HUFOTACheck$ and its transmiss |
| 20 | newR1L-SU-265 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the value set on $HUFOTACheck$ and its |
| 21 | newR1L-SU-266 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the availability response the SWMC receive |
| 21 | newR1L-SU-266 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the availability response the SWMC received from |
| 21 | newR1L-SU-266 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the availability response the SWMC rec |
| 22 | newR1L-SU-267 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of staging two or more update types simultaneously for  |
| 22 | newR1L-SU-267 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 configured priority order between the update types |
| 22 | newR1L-SU-267 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to stage two update types simultaneously |
| 22 | newR1L-SU-267 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 check that the update type with the higher configured priorit |
| 22 | newR1L-SU-267 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that two update types are available simul |
| 22 | newR1L-SU-267 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the higher priority update type ran  |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 9／列計 9）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-255 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | newR1L-SU-258 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | newR1L-SU-259 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | newR1L-SU-261 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | newR1L-SU-262 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | newR1L-SU-264 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | newR1L-SU-265 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-266 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | newR1L-SU-267 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

