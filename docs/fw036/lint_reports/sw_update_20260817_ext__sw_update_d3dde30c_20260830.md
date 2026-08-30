# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/batch12/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
- 資料列數：14
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
| U | PENDING 佔位（四欄全掃，含 ER 側） | 48 | 13 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 13 | 13 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 1 | 1 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 62**（列計不加總——同一列可觸發多項檢查）

## 明細

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 48／列計 13）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-166 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the update deployment method configured for  |
| 10 | newR1L-SU-166 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the deployment method configured for each target |
| 10 | newR1L-SU-166 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the deployment method configured for e |
| 11 | newR1L-SU-167 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading which installer was selected for each target |
| 11 | newR1L-SU-167 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of distinguishing this selection from the dispatch veri |
| 11 | newR1L-SU-167 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installer selected for each target component |
| 11 | newR1L-SU-167 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this selection from the di |
| 12 | newR1L-SU-168 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the order in which the components of a deplo |
| 12 | newR1L-SU-168 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the order in which the components were installed |
| 12 | newR1L-SU-168 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the components were installed in the |
| 13 | newR1L-SU-169 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of calling the update progress API of the SW updater HA |
| 13 | newR1L-SU-169 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to call the update progress API for the IOC, GNSS and tu |
| 13 | newR1L-SU-169 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the progress API returned the progre |
| 14 | newR1L-SU-170 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the API interface provided by the Redbend  |
| 14 | newR1L-SU-170 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to read the API interface provided by the Redbend SWMC f |
| 14 | newR1L-SU-170 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence of the API interface provided for Update  |
| 15 | newR1L-SU-171 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the installed image is judged identical to |
| 15 | newR1L-SU-171 | pre | PENDING 佔位（DR-SU6） | 5. PENDING: DR-SU6 means of obtaining the reference deployment image for the sam |
| 15 | newR1L-SU-171 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to compare the installed software image with the referen |
| 15 | newR1L-SU-171 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the installed image is identical to  |
| 16 | newR1L-SU-172 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of staging a campaign whose target is the Update Agent  |
| 16 | newR1L-SU-172 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the Update Agent version on the head unit |
| 16 | newR1L-SU-172 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to stage a campaign whose target is the Update Agent its |
| 16 | newR1L-SU-172 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Update Agent version before and after the up |
| 16 | newR1L-SU-172 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a campaign targeting the Update Agen |
| 16 | newR1L-SU-172 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the Update Agent version changed aft |
| 17 | newR1L-SU-173 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of configuring a target component to use the A/B update |
| 17 | newR1L-SU-173 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which slot a component was installed into |
| 17 | newR1L-SU-173 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to configure a target component to use the A/B update me |
| 17 | newR1L-SU-173 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read which slot the component was installed into |
| 17 | newR1L-SU-173 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the component is configured for the  |
| 17 | newR1L-SU-173 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the slot the component was installed i |
| 18 | newR1L-SU-174 | pre | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 criterion by which a consistent state is judged after an inte |
| 18 | newR1L-SU-174 | proc | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 check that the head unit is in a consistent state after the i |
| 18 | newR1L-SU-174 | er | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 observable evidence that the head unit is in a consistent sta |
| 19 | newR1L-SU-175 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the safety mechanism is judged present in  |
| 19 | newR1L-SU-175 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to exercise the safety mechanism that prevents the SOC f |
| 19 | newR1L-SU-175 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the safety mechanism prevented the S |
| 21 | newR1L-SU-177 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 list of differential update technologies approved by FCA and  |
| 21 | newR1L-SU-177 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading which differential technology was used for a |
| 21 | newR1L-SU-177 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read which differential update technology was used |
| 21 | newR1L-SU-177 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the differential update technology tha |
| 22 | newR1L-SU-178 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the resulting image is judged to match the |
| 22 | newR1L-SU-178 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to read the integrity information validated for the resu |
| 22 | newR1L-SU-178 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the resulting firmware image was val |
| 23 | newR1L-SU-179 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the validity check the Update Agent perfor |
| 23 | newR1L-SU-179 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the result of the validity check performed after |
| 23 | newR1L-SU-179 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the validity check performed after the |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 13／列計 13）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-166 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | newR1L-SU-167 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | newR1L-SU-168 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | newR1L-SU-169 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | newR1L-SU-170 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-171 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | newR1L-SU-172 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | newR1L-SU-173 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | newR1L-SU-174 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | newR1L-SU-175 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-177 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | newR1L-SU-178 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | newR1L-SU-179 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### W — ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 15 | newR1L-SU-171 | er | 比較關係 'identical to'，而 test_item 上半無數值 | installed image is identical to the reference deployment image |

