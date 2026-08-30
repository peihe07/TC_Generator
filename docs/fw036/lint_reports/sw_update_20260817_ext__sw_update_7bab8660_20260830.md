# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/batch19/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
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
| F | 方括號佔位 (proc) | 2 | 1 | 每次命中 | 已校準 |
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
| U | PENDING 佔位（四欄全掃，含 ER 側） | 48 | 12 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 8 | 8 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 58**（列計不加總——同一列可觸發多項檢查）

## 明細

### F — 方括號佔位 (proc)（行計 2／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 16 | newR1L-SU-277 | proc | 方括號佔位 '[Prohibited]' | elay_Prohibited$ to [Prohibited] ⏎ 2. Record the head unit screen content as conti |
| 16 | newR1L-SU-277 | proc | 方括號佔位 '[Prohibited]' | elay_Prohibited$ to [Prohibited] is set |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 48／列計 12）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-271 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the compatibility check the service perfor |
| 10 | newR1L-SU-271 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the compatibility check the service performed be |
| 10 | newR1L-SU-271 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the compatibility check the service pe |
| 11 | newR1L-SU-272 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of making a software update and a map update available  |
| 11 | newR1L-SU-272 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make a software update and a map update available at  |
| 11 | newR1L-SU-272 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 check that the software update session runs before the map up |
| 11 | newR1L-SU-272 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that both update types are available |
| 11 | newR1L-SU-272 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the software update ran first |
| 14 | newR1L-SU-275 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of setting $FOTA_MASTER.FOTA_Status$ to "No FOTA Event" |
| 14 | newR1L-SU-275 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to set $FOTA_MASTER.FOTA_Status$ to "No FOTA Event" |
| 14 | newR1L-SU-275 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit shows no forced update HMI while $FO |
| 14 | newR1L-SU-275 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that $FOTA_MASTER.FOTA_Status$ to "No FOT |
| 14 | newR1L-SU-275 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit shows no forced update |
| 15 | newR1L-SU-276 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of setting $FOTA_MASTER.FOTA_Cancellation_Reason$ to a  |
| 15 | newR1L-SU-276 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to set $FOTA_MASTER.FOTA_Cancellation_Reason$ to a cance |
| 15 | newR1L-SU-276 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the stored cancellation rea |
| 15 | newR1L-SU-276 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that $FOTA_MASTER.FOTA_Cancellation_Reaso |
| 15 | newR1L-SU-276 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit displays the stored ca |
| 16 | newR1L-SU-277 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of setting $FOTA_MASTER.Delay_Prohibited$ to [Prohibite |
| 16 | newR1L-SU-277 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to set $FOTA_MASTER.Delay_Prohibited$ to [Prohibited] |
| 16 | newR1L-SU-277 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit offers no delay option and requires  |
| 16 | newR1L-SU-277 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that $FOTA_MASTER.Delay_Prohibited$ to [P |
| 16 | newR1L-SU-277 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit offers no delay option |
| 17 | newR1L-SU-278 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the source from which the ROV FOTA AppServ |
| 17 | newR1L-SU-278 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the source from which the ROV FOTA AppService re |
| 17 | newR1L-SU-278 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the source from which the ROV FOTA App |
| 18 | newR1L-SU-279 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the HMI information carried on the Etherne |
| 18 | newR1L-SU-279 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the HMI information carried on the Ethernet mess |
| 18 | newR1L-SU-279 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the HMI information carried on the Eth |
| 19 | newR1L-SU-280 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of setting $FOTA_MASTER.FOTA_Status$ to "Waiting for HM |
| 19 | newR1L-SU-280 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to set $FOTA_MASTER.FOTA_Status$ to "Waiting for HMI Acc |
| 19 | newR1L-SU-280 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit prompts the user to accept, delay or |
| 19 | newR1L-SU-280 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that $FOTA_MASTER.FOTA_Status$ to "Waitin |
| 19 | newR1L-SU-280 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit prompts the user to ac |
| 21 | newR1L-SU-282 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the update progress information the servic |
| 21 | newR1L-SU-282 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the update progress information the service extr |
| 21 | newR1L-SU-282 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the update progress information the se |
| 22 | newR1L-SU-283 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the estimated TBM update time the service  |
| 22 | newR1L-SU-283 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 22 | newR1L-SU-283 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the estimated TBM update time the service extrac |
| 22 | newR1L-SU-283 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the estimated TBM update time the serv |
| 23 | newR1L-SU-284 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the WhatsNew information the service extra |
| 23 | newR1L-SU-284 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 23 | newR1L-SU-284 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the WhatsNew information the service extracted f |
| 23 | newR1L-SU-284 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the WhatsNew information the service e |
| 24 | newR1L-SU-285 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the MQTT subscription the SWMC made toward |
| 24 | newR1L-SU-285 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the MQTT subscription the SWMC made towards the  |
| 24 | newR1L-SU-285 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the MQTT subscription the SWMC made to |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 8／列計 8）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-271 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | newR1L-SU-272 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | newR1L-SU-278 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | newR1L-SU-279 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-282 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | newR1L-SU-283 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | newR1L-SU-284 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | newR1L-SU-285 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

