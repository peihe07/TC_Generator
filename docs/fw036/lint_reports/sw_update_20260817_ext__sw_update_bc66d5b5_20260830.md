# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/batch16/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
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
| U | PENDING 佔位（四欄全掃，含 ER 側） | 35 | 12 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 11 | 11 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 46**（列計不加總——同一列可觸發多項檢查）

## 明細

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 35／列計 12）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-225 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the image update ran independently of any  |
| 10 | newR1L-SU-225 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the image update ran independently of  |
| 10 | newR1L-SU-225 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the image update ran independently o |
| 11 | newR1L-SU-226 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the file-system update ran independently o |
| 11 | newR1L-SU-226 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the file-system update ran independent |
| 11 | newR1L-SU-226 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the file-system update ran independe |
| 12 | newR1L-SU-227 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing whether the SWMC is in its idle state |
| 12 | newR1L-SU-227 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether the SWMC is in its idle state |
| 12 | newR1L-SU-227 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of whether the SWMC is in its idle state |
| 13 | newR1L-SU-228 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the CPU and RAM utilisation while idle cou |
| 13 | newR1L-SU-228 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the CPU and RAM utilisation while idle |
| 13 | newR1L-SU-228 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the CPU and RAM utilisation while id |
| 14 | newR1L-SU-229 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the HMI performance during a background do |
| 14 | newR1L-SU-229 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the HMI performance during a backgroun |
| 14 | newR1L-SU-229 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the HMI performance during a backgro |
| 15 | newR1L-SU-230 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which navigation and radio count as not impacted |
| 15 | newR1L-SU-230 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that navigation and radio count as not impa |
| 15 | newR1L-SU-230 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that navigation and radio count as not im |
| 16 | newR1L-SU-231 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the status report the SWMC sent on complet |
| 16 | newR1L-SU-231 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 16 | newR1L-SU-231 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the status report the SWMC sent on completion, r |
| 16 | newR1L-SU-231 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the status report the SWMC sent on com |
| 18 | newR1L-SU-233 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the classification the WiFi Update Service |
| 18 | newR1L-SU-233 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the classification the WiFi Update Service appli |
| 18 | newR1L-SU-233 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the classification the WiFi Update Ser |
| 20 | newR1L-SU-235 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the bearer the head unit used for a critic |
| 20 | newR1L-SU-235 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the bearer the head unit used for a critical upd |
| 20 | newR1L-SU-235 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the bearer the head unit used for a cr |
| 21 | newR1L-SU-236 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1 |
| 22 | newR1L-SU-237 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the parameter values the SWMC received fro |
| 22 | newR1L-SU-237 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the parameter values the SWMC received from the  |
| 22 | newR1L-SU-237 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the parameter values the SWMC received |
| 23 | newR1L-SU-238 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the Download Descriptor the SWMC parsed an |
| 23 | newR1L-SU-238 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Download Descriptor the SWMC parsed and the  |
| 23 | newR1L-SU-238 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the Download Descriptor the SWMC parse |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 11／列計 11）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-225 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | newR1L-SU-226 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | newR1L-SU-227 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | newR1L-SU-228 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | newR1L-SU-229 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-230 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | newR1L-SU-231 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | newR1L-SU-233 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | newR1L-SU-235 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | newR1L-SU-237 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | newR1L-SU-238 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

