# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_SWUpdate_20260830.xlsx

- 來源：`features/sw_update/delivered/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_SWUpdate_20260830.xlsx`（唯讀）
- 資料列數：319
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
| U | PENDING 佔位（四欄全掃，含 ER 側） | 712 | 195 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 218 | 213 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 21 | 20 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 952**（列計不加總——同一列可觸發多項檢查）

## 明細

### J — 行首大寫（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 292 | newR1L-SU-283 | test_item | 首字小寫 'he' | he WiFiUpdateService shall ensure that sufficient physical storage space is avai |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 712／列計 195）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | newR1L-SU-003 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the ignition cycle counter associated with F |
| 12 | newR1L-SU-003 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the ignition cycle counter while FOTA package da |
| 12 | newR1L-SU-003 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the ignition cycle counter while FOTA  |
| 15 | newR1L-SU-006 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reaching the state in which the FOTA package could n |
| 15 | newR1L-SU-006 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to reach the state in which the FOTA package could not b |
| 15 | newR1L-SU-006 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the FOTA package could not be downlo |
| 18 | newR1L-SU-009 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 18 | newR1L-SU-009 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the network bearer used for the download afte |
| 18 | newR1L-SU-009 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network bearer used for the downlo |
| 20 | newR1L-SU-011 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 20 | newR1L-SU-011 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the network bearer used for the download whil |
| 20 | newR1L-SU-011 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network bearer used for the downlo |
| 21 | newR1L-SU-012 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 21 | newR1L-SU-012 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the network bearer used for the resumed downl |
| 21 | newR1L-SU-012 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network bearer used for the resume |
| 24 | newR1L-SU-015 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the classification the WiFi Update Service |
| 24 | newR1L-SU-015 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the classification the WiFi Update Service appli |
| 24 | newR1L-SU-015 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the classification the WiFi Update Ser |
| 26 | newR1L-SU-017 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reaching the end of the one week Wi-Fi attempt perio |
| 26 | newR1L-SU-017 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 26 | newR1L-SU-017 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to reach the end of the one week Wi-Fi attempt period |
| 26 | newR1L-SU-017 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to observe the network bearer used for the download afte |
| 26 | newR1L-SU-017 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable state showing that the Wi-Fi attempt period has el |
| 26 | newR1L-SU-017 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the network bearer used for the downlo |
| 27 | newR1L-SU-018 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing a critical update session from a sile |
| 27 | newR1L-SU-018 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to observe that the session in progress is a critical up |
| 27 | newR1L-SU-018 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the session in progress is a critica |
| 29 | newR1L-SU-020 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the bearer the head unit used for a critic |
| 29 | newR1L-SU-020 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the bearer the head unit used for a critical upd |
| 29 | newR1L-SU-020 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the bearer the head unit used for a cr |
| 32 | newR1L-SU-023 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1 |
| 50 | newR1L-SU-041 | pre | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 which start point the 30 minutes is counted from: the start o |
| 50 | newR1L-SU-041 | proc | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 step to record the start point from which the 30 minutes is c |
| 50 | newR1L-SU-041 | proc | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 check that the download session ends and the head unit hotspo |
| 50 | newR1L-SU-041 | er | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 observable evidence of the start point from which the 30 minu |
| 50 | newR1L-SU-041 | er | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable evidence that the download session ended and the h |
| 54 | newR1L-SU-045 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of placing a Wi-Fi network on the WiFi Manager exclusio |
| 54 | newR1L-SU-045 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to place the access point shown with more signal bars on |
| 54 | newR1L-SU-045 | proc | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 check that the head unit connects to the remaining access poi |
| 54 | newR1L-SU-045 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that a network is on the exclusion list |
| 54 | newR1L-SU-045 | er | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 observable evidence distinguishing this connection from the o |
| 55 | newR1L-SU-046 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the signal strength category assigned to a |
| 55 | newR1L-SU-046 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 values of the predefined Wi-Fi signal strength thresholds tha |
| 55 | newR1L-SU-046 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the signal strength category assigned to each ac |
| 55 | newR1L-SU-046 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the signal strength category assigned  |
| 59 | newR1L-SU-050 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing that the preconditions for software downlo |
| 59 | newR1L-SU-050 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the outcome of the precondition evaluation at th |
| 59 | newR1L-SU-050 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the preconditions for software downl |
| 66 | newR1L-SU-057 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing this routing path from the one verifi |
| 66 | newR1L-SU-057 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe which service forwarded the version informati |
| 66 | newR1L-SU-057 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the routing path taken by the version  |
| 67 | newR1L-SU-058 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing this routing path from the one verifi |
| 67 | newR1L-SU-058 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe which service forwarded the version informati |
| 67 | newR1L-SU-058 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the routing path taken by the version  |
| 72 | newR1L-SU-063 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making an ROV update fail and roll back on the test  |
| 72 | newR1L-SU-063 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the update fail so that the rollback completes s |
| 72 | newR1L-SU-063 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable state showing $FOTA_Status$ = [FOTA FailureRollbac |
| 73 | newR1L-SU-064 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making an ROV update fail without a successful rollb |
| 73 | newR1L-SU-064 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the update fail so that the failure completes wi |
| 73 | newR1L-SU-064 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable state showing $FOTA_Status$ = [FOTA Failure Comple |
| 89 | newR1L-SU-080 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing that TBM-specific FOTA functionality is al |
| 89 | newR1L-SU-080 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of placing the vehicle in a state where $TBM_present$ d |
| 89 | newR1L-SU-080 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether TBM-specific FOTA functionality is allow |
| 89 | newR1L-SU-080 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that TBM-specific FOTA functionality is a |
| 92 | newR1L-SU-083 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of changing the estimated update duration through softw |
| 98 | newR1L-SU-089 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of staging a forced telematics box module update campai |
| 98 | newR1L-SU-089 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to stage a forced telematics box module update campaign |
| 98 | newR1L-SU-089 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the forced telematics box m |
| 98 | newR1L-SU-089 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a forced telematics box module updat |
| 98 | newR1L-SU-089 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the forced telematics box module updat |
| 100 | newR1L-SU-091 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making a telematics box module update fail during it |
| 100 | newR1L-SU-091 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the telematics box module update fail during its |
| 100 | newR1L-SU-091 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the rollback success pop-up |
| 100 | newR1L-SU-091 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the telematics box module update fai |
| 100 | newR1L-SU-091 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the rollback success pop-up after the  |
| 102 | newR1L-SU-093 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making a telematics box module update fail during it |
| 102 | newR1L-SU-093 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the telematics box module update fail during its |
| 102 | newR1L-SU-093 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the telematics box module u |
| 102 | newR1L-SU-093 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the telematics box module update fai |
| 102 | newR1L-SU-093 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the telematics box module update failu |
| 104 | newR1L-SU-095 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing the No_Update state from the No_Updat |
| 104 | newR1L-SU-095 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to bring $TBMUpdate$ to the No_Update state rather than  |
| 104 | newR1L-SU-095 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this clearing from the one |
| 105 | newR1L-SU-096 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the parameter values the SWMC received fro |
| 105 | newR1L-SU-096 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the parameter values the SWMC received from the  |
| 105 | newR1L-SU-096 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the parameter values the SWMC received |
| 106 | newR1L-SU-097 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the Download Descriptor the SWMC parsed an |
| 106 | newR1L-SU-097 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Download Descriptor the SWMC parsed and the  |
| 106 | newR1L-SU-097 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the Download Descriptor the SWMC parse |
| 110 | newR1L-SU-101 | pre | PENDING 佔位（DR-SU5） | 3. PENDING: DR-SU5 bench procedure for running the same head unit against two up |
| 110 | newR1L-SU-101 | proc | PENDING 佔位（DR-SU5） | 3. PENDING: DR-SU5 step to return the head unit to a comparable starting state a |
| 110 | newR1L-SU-101 | er | PENDING 佔位（DR-SU5） | 3. PENDING: DR-SU5 observable state showing the head unit is back at a comparabl |
| 117 | newR1L-SU-108 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the component packages extracted from the  |
| 117 | newR1L-SU-108 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 117 | newR1L-SU-108 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the component packages extracted from the deploy |
| 117 | newR1L-SU-108 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the component packages extracted from  |
| 118 | newR1L-SU-109 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the MCPU installation status the Update En |
| 118 | newR1L-SU-109 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the MCPU installation status the Update Engine r |
| 118 | newR1L-SU-109 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the MCPU installation status the Updat |
| 123 | newR1L-SU-114 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which `not impact other systems, screens, or veh |
| 123 | newR1L-SU-114 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the download did not impact other syst |
| 123 | newR1L-SU-114 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that no other system, screen or vehicle f |
| 131 | newR1L-SU-122 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the transition request the WiFi Update Ser |
| 133 | newR1L-SU-124 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the precondition evaluation the service pe |
| 133 | newR1L-SU-124 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1 |
| 133 | newR1L-SU-124 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the precondition evaluation the service performe |
| 133 | newR1L-SU-124 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the precondition evaluation the servic |
| 136 | newR1L-SU-127 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the installation failure status reported t |
| 136 | newR1L-SU-127 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of making an installation fail |
| 136 | newR1L-SU-127 | pre | PENDING 佔位（DR-SU3） | 6. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 136 | newR1L-SU-127 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installation failure status reported through |
| 136 | newR1L-SU-127 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the installation failure status report |
| 137 | newR1L-SU-128 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which eCall availability during an update is jud |
| 137 | newR1L-SU-128 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of exercising eCall on the bench without placing an eme |
| 137 | newR1L-SU-128 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that eCall functionality remained operation |
| 137 | newR1L-SU-128 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that eCall functionality remained operati |
| 139 | newR1L-SU-130 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the OTA session status the service set aft |
| 139 | newR1L-SU-130 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of making an installation fail |
| 139 | newR1L-SU-130 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the OTA session status the service set after an  |
| 139 | newR1L-SU-130 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the OTA session status the service set |
| 140 | newR1L-SU-131 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of producing a vehicle motion event while an installati |
| 140 | newR1L-SU-131 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to produce a vehicle motion event while the installation |
| 140 | newR1L-SU-131 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the installation continued without interruption |
| 140 | newR1L-SU-131 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of a vehicle motion event during the inst |
| 140 | newR1L-SU-131 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the installation continued without i |
| 142 | newR1L-SU-133 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the installation failure status reported b |
| 142 | newR1L-SU-133 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of making an installation fail |
| 142 | newR1L-SU-133 | pre | PENDING 佔位（DR-SU3） | 6. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 142 | newR1L-SU-133 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installation failure status reported by the  |
| 142 | newR1L-SU-133 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the installation failure status report |
| 143 | newR1L-SU-134 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing which installer each component package of  |
| 143 | newR1L-SU-134 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read which installer received the MCPU firmware packa |
| 143 | newR1L-SU-134 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the MCPU firmware package was handed |
| 144 | newR1L-SU-135 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package whose digital signature |
| 144 | newR1L-SU-135 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package whose digital signature or |
| 144 | newR1L-SU-135 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged deployment package has an |
| 145 | newR1L-SU-136 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a differential deployment package whose decl |
| 145 | newR1L-SU-136 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a differential deployment package whose declare |
| 145 | newR1L-SU-136 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged differential package decl |
| 146 | newR1L-SU-137 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the invocation of the signature verificati |
| 146 | newR1L-SU-137 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the invocation of the signature verification  |
| 146 | newR1L-SU-137 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the invocation of the signature verifi |
| 147 | newR1L-SU-138 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package containing multiple upd |
| 147 | newR1L-SU-138 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package containing multiple update |
| 147 | newR1L-SU-138 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that one contained update file of the sta |
| 148 | newR1L-SU-139 | pre | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 confirmation that no safety-related notification condition ap |
| 149 | newR1L-SU-140 | pre | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 confirmation that no safety-related notification condition ap |
| 150 | newR1L-SU-141 | pre | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 list of safety-related notification conditions applicable dur |
| 150 | newR1L-SU-141 | proc | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 step to bring one safety-related condition into effect |
| 150 | newR1L-SU-141 | er | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 observable state showing the safety-related condition is in e |
| 152 | newR1L-SU-143 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of distinguishing the automatic download request from t |
| 152 | newR1L-SU-143 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe that the deployment package download request  |
| 152 | newR1L-SU-143 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the download request has been issued |
| 154 | newR1L-SU-145 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to observe the point at which deployment package downloa |
| 154 | newR1L-SU-145 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the download completion point |
| 157 | newR1L-SU-148 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of identifying the boundaries between the update check, |
| 157 | newR1L-SU-148 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to record the head unit screen content with the check, d |
| 157 | newR1L-SU-148 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence delimiting the check, download and instal |
| 158 | newR1L-SU-149 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of placing the SW Update HMI in an unavailable state on |
| 158 | newR1L-SU-149 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to place the SW Update HMI in an unavailable state |
| 158 | newR1L-SU-149 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the deployment package download continues to compl |
| 158 | newR1L-SU-149 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the SW Update HMI is unavailable |
| 158 | newR1L-SU-149 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the download completed with no user  |
| 161 | newR1L-SU-152 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the event handling interface between the S |
| 161 | newR1L-SU-152 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the event sent from the SW Update HMI to the WiF |
| 161 | newR1L-SU-152 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the event sent from the SW Update HMI  |
| 162 | newR1L-SU-153 | pre | PENDING 佔位（DR-SU6） | 3. PENDING: DR-SU6 criterion by which the absence of a dependency on a specific  |
| 162 | newR1L-SU-153 | proc | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 step to establish that the OTA client does not depend on a sp |
| 162 | newR1L-SU-153 | er | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 observable evidence that the OTA client does not depend on a  |
| 163 | newR1L-SU-154 | pre | PENDING 佔位（DR-SU6） | 5. PENDING: DR-SU6 list of the diagnostic trouble codes that count as intended d |
| 163 | newR1L-SU-154 | proc | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 check that DTC_after contains no code outside the list of cod |
| 163 | newR1L-SU-154 | er | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 observable evidence that DTC_after contains no unintended cod |
| 164 | newR1L-SU-155 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of recording the diagnostic messages on the vehicle com |
| 164 | newR1L-SU-155 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the diagnostic messages sent to the external ECU |
| 164 | newR1L-SU-155 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of periodic Tester Present messages durin |
| 165 | newR1L-SU-156 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the messages exchanged between distributed |
| 165 | newR1L-SU-156 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the session information and workflow events exch |
| 165 | newR1L-SU-156 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the messages exchanged between the com |
| 167 | newR1L-SU-158 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1 |
| 167 | newR1L-SU-158 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 list of the vehicle-specific preconditions and their configur |
| 167 | newR1L-SU-158 | proc | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 step to verify this requirement separately from the individua |
| 167 | newR1L-SU-158 | er | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 observable evidence separating this requirement from the indi |
| 168 | newR1L-SU-159 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the VIN the WiFi Update Service read for t |
| 168 | newR1L-SU-159 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the VIN the service used for the OTA workflow |
| 168 | newR1L-SU-159 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the VIN used for the OTA workflow |
| 169 | newR1L-SU-160 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the vehicle brand the service provided to  |
| 169 | newR1L-SU-160 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 169 | newR1L-SU-160 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the brand value provided to the SWMC from the VC |
| 169 | newR1L-SU-160 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the brand value taken from the VC_VEH_ |
| 170 | newR1L-SU-161 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the brand value the service read from the  |
| 170 | newR1L-SU-161 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 170 | newR1L-SU-161 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the brand value provided to the SWMC from the pr |
| 170 | newR1L-SU-161 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the brand value taken from the proxi p |
| 171 | newR1L-SU-162 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading which installer each component package was r |
| 171 | newR1L-SU-162 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 171 | newR1L-SU-162 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installer that received the MCPU firmware pa |
| 171 | newR1L-SU-162 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this routing from the one  |
| 172 | newR1L-SU-163 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the installation order and the installer sta |
| 172 | newR1L-SU-163 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 172 | newR1L-SU-163 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether a dependent component waited for its pre |
| 172 | newR1L-SU-163 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that a dependent component waited for its |
| 173 | newR1L-SU-164 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of the  |
| 173 | newR1L-SU-164 | proc | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 step to verify this requirement separately from the individua |
| 173 | newR1L-SU-164 | er | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 observable evidence separating this requirement from the indi |
| 174 | newR1L-SU-165 | pre | PENDING 佔位（DR-SU6） | 3. PENDING: DR-SU6 criterion by which portability across frameworks is judged on |
| 174 | newR1L-SU-165 | proc | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 step to establish that the HMI architecture supports portabil |
| 174 | newR1L-SU-165 | er | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 observable evidence that the HMI architecture supports portab |
| 176 | newR1L-SU-167 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the value set on $HUFOTACheck$ and its tra |
| 176 | newR1L-SU-167 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the value set on $HUFOTACheck$ and its transmiss |
| 176 | newR1L-SU-167 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the value set on $HUFOTACheck$ and its |
| 177 | newR1L-SU-168 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the availability response the SWMC receive |
| 177 | newR1L-SU-168 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the availability response the SWMC received from |
| 177 | newR1L-SU-168 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the availability response the SWMC rec |
| 178 | newR1L-SU-169 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of staging two or more update types simultaneously for  |
| 178 | newR1L-SU-169 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 configured priority order between the update types |
| 178 | newR1L-SU-169 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to stage two update types simultaneously |
| 178 | newR1L-SU-169 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 check that the update type with the higher configured priorit |
| 178 | newR1L-SU-169 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that two update types are available simul |
| 178 | newR1L-SU-169 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the higher priority update type ran  |
| 182 | newR1L-SU-173 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the compatibility check the service perfor |
| 182 | newR1L-SU-173 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the compatibility check the service performed be |
| 182 | newR1L-SU-173 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the compatibility check the service pe |
| 183 | newR1L-SU-174 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of making a software update and a map update available  |
| 183 | newR1L-SU-174 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make a software update and a map update available at  |
| 183 | newR1L-SU-174 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 check that the software update session runs before the map up |
| 183 | newR1L-SU-174 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that both update types are available |
| 183 | newR1L-SU-174 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the software update ran first |
| 186 | newR1L-SU-177 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the FOTA Master to report no FOTA event on it |
| 186 | newR1L-SU-177 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the FOTA Master to report no FOTA event on its s |
| 186 | newR1L-SU-177 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit shows no forced update HMI in that s |
| 186 | newR1L-SU-177 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence of the FOTA Master to report no FOTA even |
| 186 | newR1L-SU-177 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit shows no forced update |
| 187 | newR1L-SU-178 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the FOTA Master to report a cancellation reas |
| 187 | newR1L-SU-178 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the FOTA Master to report a cancellation reason  |
| 187 | newR1L-SU-178 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the stored cancellation rea |
| 187 | newR1L-SU-178 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence of the FOTA Master to report a cancellati |
| 187 | newR1L-SU-178 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit displays the stored ca |
| 188 | newR1L-SU-179 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the FOTA Master to report that delaying the u |
| 188 | newR1L-SU-179 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the FOTA Master to report that delaying the upda |
| 188 | newR1L-SU-179 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit offers no delay option and requires  |
| 188 | newR1L-SU-179 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence of the FOTA Master to report that delayin |
| 188 | newR1L-SU-179 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit offers no delay option |
| 189 | newR1L-SU-180 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the source from which the ROV FOTA AppServ |
| 189 | newR1L-SU-180 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the source from which the ROV FOTA AppService re |
| 189 | newR1L-SU-180 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the source from which the ROV FOTA App |
| 190 | newR1L-SU-181 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the HMI information carried on the Etherne |
| 190 | newR1L-SU-181 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the HMI information carried on the Ethernet mess |
| 190 | newR1L-SU-181 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the HMI information carried on the Eth |
| 191 | newR1L-SU-182 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the FOTA Master to report that it is waiting  |
| 191 | newR1L-SU-182 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the FOTA Master to report that it is waiting for |
| 191 | newR1L-SU-182 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit prompts the user to accept, delay or |
| 191 | newR1L-SU-182 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence of the FOTA Master to report that it is w |
| 191 | newR1L-SU-182 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit prompts the user to ac |
| 193 | newR1L-SU-184 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the update progress information the servic |
| 193 | newR1L-SU-184 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the update progress information the service extr |
| 193 | newR1L-SU-184 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the update progress information the se |
| 194 | newR1L-SU-185 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the estimated TBM update time the service  |
| 194 | newR1L-SU-185 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 194 | newR1L-SU-185 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the estimated TBM update time the service extrac |
| 194 | newR1L-SU-185 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the estimated TBM update time the serv |
| 195 | newR1L-SU-186 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the WhatsNew information the service extra |
| 195 | newR1L-SU-186 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 195 | newR1L-SU-186 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the WhatsNew information the service extracted f |
| 195 | newR1L-SU-186 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the WhatsNew information the service e |
| 196 | newR1L-SU-187 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the MQTT subscription the SWMC made toward |
| 196 | newR1L-SU-187 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the MQTT subscription the SWMC made towards the  |
| 196 | newR1L-SU-187 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the MQTT subscription the SWMC made to |
| 198 | newR1L-SU-189 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the installation progress information carr |
| 198 | newR1L-SU-189 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installation progress information carried on |
| 198 | newR1L-SU-189 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the installation progress information  |
| 199 | newR1L-SU-190 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the cancellation reason value the ROV Upda |
| 199 | newR1L-SU-190 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of making the FOTA Master report a cancellation reason |
| 199 | newR1L-SU-190 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the cancellation reason value the ROV Update Ser |
| 199 | newR1L-SU-190 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the cancellation reason value the ROV  |
| 201 | newR1L-SU-192 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 value of the configured response handling period |
| 201 | newR1L-SU-192 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to wait for the configured response handling period and  |
| 201 | newR1L-SU-192 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the notification is treated as not a |
| 202 | newR1L-SU-193 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the values of FOTA_TBM_Notification, FOTA_ |
| 202 | newR1L-SU-193 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the values of FOTA_TBM_Notification, FOTA_TBM_Fo |
| 202 | newR1L-SU-193 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the values of FOTA_TBM_Notification, F |
| 203 | newR1L-SU-194 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of setting the FOTA_TBM_Notification indicator |
| 203 | newR1L-SU-194 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to set the FOTA_TBM_Notification indicator while the veh |
| 203 | newR1L-SU-194 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the TBM update notification |
| 203 | newR1L-SU-194 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the FOTA_TBM_Notification indicator  |
| 203 | newR1L-SU-194 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the TBM update notification |
| 204 | newR1L-SU-195 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of setting the FOTA_TBM_Forced indicator |
| 204 | newR1L-SU-195 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to set the FOTA_TBM_Forced indicator while the vehicle i |
| 204 | newR1L-SU-195 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the forced TBM update scree |
| 204 | newR1L-SU-195 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the FOTA_TBM_Forced indicator is set |
| 204 | newR1L-SU-195 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the forced TBM update screen |
| 205 | newR1L-SU-196 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which conformance to the HMI logic and flow spec |
| 205 | newR1L-SU-196 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the user interface followed the HMI lo |
| 205 | newR1L-SU-196 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence of conformance to the HMI logic and flow  |
| 206 | newR1L-SU-197 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of the  |
| 206 | newR1L-SU-197 | proc | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 step to verify this requirement separately from the individua |
| 206 | newR1L-SU-197 | er | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 observable evidence separating this requirement from the indi |
| 208 | newR1L-SU-199 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of sending a New Installation Announcement to this head |
| 208 | newR1L-SU-199 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send a New Installation Announcement to this head uni |
| 208 | newR1L-SU-199 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 check that an OTA update session started without any action o |
| 208 | newR1L-SU-199 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a New Installation Announcement reac |
| 208 | newR1L-SU-199 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that a session started without any action |
| 209 | newR1L-SU-200 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the session trigger notifications received |
| 209 | newR1L-SU-200 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 209 | newR1L-SU-200 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the session trigger notifications received throu |
| 209 | newR1L-SU-200 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the session trigger notifications rece |
| 210 | newR1L-SU-201 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of staging a deployment package whose integrity validat |
| 210 | newR1L-SU-201 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to stage a deployment package whose integrity validation |
| 210 | newR1L-SU-201 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that no installation started for the package that fails |
| 210 | newR1L-SU-201 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the staged package fails its integri |
| 210 | newR1L-SU-201 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that no installation started |
| 211 | newR1L-SU-202 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of producing an ECU configuration change event such as  |
| 211 | newR1L-SU-202 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to produce an ECU configuration change event |
| 211 | newR1L-SU-202 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether the WiFi Update Service received the eve |
| 211 | newR1L-SU-202 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that an ECU configuration change event oc |
| 211 | newR1L-SU-202 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the event reached the WiFi Update Se |
| 212 | newR1L-SU-203 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of recording the protocol exchange between the head uni |
| 212 | newR1L-SU-203 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the protocol exchange between the head unit and  |
| 212 | newR1L-SU-203 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the exchange follows the OMA-DM SCOM |
| 213 | newR1L-SU-204 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the SCOMO management of the individual compo |
| 213 | newR1L-SU-204 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read how the individual components were managed throu |
| 213 | newR1L-SU-204 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the SCOMO management of the individual |
| 214 | newR1L-SU-205 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the network availability notification sent |
| 214 | newR1L-SU-205 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the network availability notification sent from  |
| 214 | newR1L-SU-205 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network availability notification  |
| 215 | newR1L-SU-206 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the URL the SWMC used to download the depl |
| 215 | newR1L-SU-206 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 215 | newR1L-SU-206 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the URL the SWMC used to download the deployment |
| 215 | newR1L-SU-206 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the URL the SWMC used to download the  |
| 216 | newR1L-SU-207 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the Download Descriptor the SWMC read and  |
| 216 | newR1L-SU-207 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 216 | newR1L-SU-207 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Download Descriptor the SWMC read and the UR |
| 216 | newR1L-SU-207 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the Download Descriptor the SWMC read  |
| 217 | newR1L-SU-208 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which independence from the operating system and |
| 217 | newR1L-SU-208 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the storage went through the abstract  |
| 217 | newR1L-SU-208 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the storage was independent of the o |
| 218 | newR1L-SU-209 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the invocation of the Redbend Update Agent |
| 218 | newR1L-SU-209 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the invocation of the Redbend Update Agent for t |
| 218 | newR1L-SU-209 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the invocation of the Redbend Update A |
| 219 | newR1L-SU-210 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the protocol the SWMC used to communicate  |
| 219 | newR1L-SU-210 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 219 | newR1L-SU-210 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the protocol the SWMC used to communicate with t |
| 219 | newR1L-SU-210 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the protocol the SWMC used to communic |
| 220 | newR1L-SU-211 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the Download Descriptor processed when a p |
| 220 | newR1L-SU-211 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of configuring a proprietary communication protocol |
| 220 | newR1L-SU-211 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Download Descriptor processed when a proprie |
| 220 | newR1L-SU-211 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the Download Descriptor processed when |
| 221 | newR1L-SU-212 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the vehicle properties the WiFiUpdateServi |
| 221 | newR1L-SU-212 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the vehicle properties the WiFiUpdateService ret |
| 221 | newR1L-SU-212 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the vehicle properties the WiFiUpdateS |
| 222 | newR1L-SU-213 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the installer invoked for the installation |
| 222 | newR1L-SU-213 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 222 | newR1L-SU-213 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installer invoked for the installation metho |
| 222 | newR1L-SU-213 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the installer invoked for the installa |
| 223 | newR1L-SU-214 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the ECU reference IDs used to associate th |
| 223 | newR1L-SU-214 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the ECU reference IDs used to associate the upda |
| 223 | newR1L-SU-214 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the ECU reference IDs used to associat |
| 224 | newR1L-SU-215 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which portability with the Android operating sys |
| 224 | newR1L-SU-215 | proc | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 step to establish that the Redbend Update Agent is portable w |
| 224 | newR1L-SU-215 | er | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 observable evidence that the Redbend Update Agent is portable |
| 225 | newR1L-SU-216 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the OMA-DM protocol stack the SWMC used to |
| 225 | newR1L-SU-216 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 225 | newR1L-SU-216 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the OMA-DM protocol stack the SWMC used towards  |
| 225 | newR1L-SU-216 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the OMA-DM protocol stack the SWMC use |
| 226 | newR1L-SU-217 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the image update ran independently of any  |
| 226 | newR1L-SU-217 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the image update ran independently of  |
| 226 | newR1L-SU-217 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the image update ran independently o |
| 227 | newR1L-SU-218 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the file-system update ran independently o |
| 227 | newR1L-SU-218 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the file-system update ran independent |
| 227 | newR1L-SU-218 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the file-system update ran independe |
| 228 | newR1L-SU-219 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request to this |
| 228 | newR1L-SU-219 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of distinguishing this interface from the one verified  |
| 228 | newR1L-SU-219 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request to this he |
| 228 | newR1L-SU-219 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the session request received through the event i |
| 228 | newR1L-SU-219 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the OTA Server sent a session reques |
| 228 | newR1L-SU-219 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this reception from the on |
| 229 | newR1L-SU-220 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of injecting a vehicle event that blocks software deplo |
| 229 | newR1L-SU-220 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing that the event was evaluated before deploy |
| 229 | newR1L-SU-220 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to inject a vehicle event that blocks software deploymen |
| 229 | newR1L-SU-220 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read whether the injected event was evaluated before  |
| 229 | newR1L-SU-220 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that a blocking vehicle event was injecte |
| 229 | newR1L-SU-220 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the event was evaluated before deplo |
| 230 | newR1L-SU-221 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of reading the polling parameters held by the SWMC |
| 230 | newR1L-SU-221 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing this requirement from SWE1-FOTA-347,  |
| 230 | newR1L-SU-221 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the polling parameters held by the SWMC |
| 230 | newR1L-SU-221 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the polling parameters held by the SWM |
| 231 | newR1L-SU-222 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of sending a polling interval parameter from the OTA Se |
| 231 | newR1L-SU-222 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the polling interval currently applied by th |
| 231 | newR1L-SU-222 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send a new polling interval parameter from the OTA Se |
| 231 | newR1L-SU-222 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the polling interval applied by the SWMC after t |
| 231 | newR1L-SU-222 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the polling interval parameter reach |
| 231 | newR1L-SU-222 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the polling interval applied by the  |
| 232 | newR1L-SU-223 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of updating polling parameters from the OTA Server |
| 232 | newR1L-SU-223 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing this update from the one verified by  |
| 232 | newR1L-SU-223 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to update the polling parameters from the OTA Server |
| 232 | newR1L-SU-223 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the polling parameters used in the next vehicle- |
| 232 | newR1L-SU-223 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the polling parameters were updated  |
| 232 | newR1L-SU-223 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this from the update verif |
| 233 | newR1L-SU-224 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request to this |
| 233 | newR1L-SU-224 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the notification from SWMC to WiFiUpdateSe |
| 233 | newR1L-SU-224 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request to this he |
| 233 | newR1L-SU-224 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the notification sent from SWMC to WiFiUpdateSer |
| 233 | newR1L-SU-224 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the OTA Server sent a session reques |
| 233 | newR1L-SU-224 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the notification sent from SWMC to WiF |
| 234 | newR1L-SU-225 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of configuring a proprietary communication protocol ins |
| 234 | newR1L-SU-225 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the protocol used between the head unit an |
| 234 | newR1L-SU-225 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to configure a proprietary communication protocol instea |
| 234 | newR1L-SU-225 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the protocol used for the communication with the |
| 234 | newR1L-SU-225 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a proprietary communication protocol |
| 234 | newR1L-SU-225 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that HTTP and TLS were used for the commu |
| 235 | newR1L-SU-226 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing whether the SWMC is in its idle state |
| 235 | newR1L-SU-226 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether the SWMC is in its idle state |
| 235 | newR1L-SU-226 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of whether the SWMC is in its idle state |
| 236 | newR1L-SU-227 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the CPU and RAM utilisation while idle cou |
| 236 | newR1L-SU-227 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the CPU and RAM utilisation while idle |
| 236 | newR1L-SU-227 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the CPU and RAM utilisation while id |
| 237 | newR1L-SU-228 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the HMI performance during a background do |
| 237 | newR1L-SU-228 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the HMI performance during a backgroun |
| 237 | newR1L-SU-228 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the HMI performance during a backgro |
| 238 | newR1L-SU-229 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which navigation and radio count as not impacted |
| 238 | newR1L-SU-229 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that navigation and radio count as not impa |
| 238 | newR1L-SU-229 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that navigation and radio count as not im |
| 239 | newR1L-SU-230 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the status report the SWMC sent on complet |
| 239 | newR1L-SU-230 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 239 | newR1L-SU-230 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the status report the SWMC sent on completion, r |
| 239 | newR1L-SU-230 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the status report the SWMC sent on com |
| 240 | newR1L-SU-231 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of sending a configuration command from the OTA Server  |
| 240 | newR1L-SU-231 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the configuration parameters applied by the  |
| 240 | newR1L-SU-231 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send a session-specific configuration parameter from  |
| 240 | newR1L-SU-231 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the configuration parameters applied by the SWMC |
| 240 | newR1L-SU-231 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the configuration command reached th |
| 240 | newR1L-SU-231 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the SWMC applied the parameter that  |
| 241 | newR1L-SU-232 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of sending a server URL and port configuration command  |
| 241 | newR1L-SU-232 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the server address used by the head unit for |
| 241 | newR1L-SU-232 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send a new server URL and port from the OTA Server |
| 241 | newR1L-SU-232 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the server address used by the next communicatio |
| 241 | newR1L-SU-232 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the new server URL and port reached  |
| 241 | newR1L-SU-232 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the next session used the updated se |
| 242 | newR1L-SU-233 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of sending an invalid server URL and port configuration |
| 242 | newR1L-SU-233 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the server address stored and used by the he |
| 242 | newR1L-SU-233 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send an invalid server URL and port from the OTA Serv |
| 242 | newR1L-SU-233 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the server address used by the head unit after t |
| 242 | newR1L-SU-233 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that an invalid server configuration reac |
| 242 | newR1L-SU-233 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the head unit kept the previously st |
| 243 | newR1L-SU-234 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the network the WiFiUpdateService selected |
| 243 | newR1L-SU-234 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the network the WiFiUpdateService selected and t |
| 243 | newR1L-SU-234 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network the WiFiUpdateService sele |
| 244 | newR1L-SU-235 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the update type the WiFiUpdateService dete |
| 244 | newR1L-SU-235 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the update type the WiFiUpdateService determined |
| 244 | newR1L-SU-235 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the update type the WiFiUpdateService  |
| 245 | newR1L-SU-236 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the update mode the WiFiUpdateService dete |
| 245 | newR1L-SU-236 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the update mode the WiFiUpdateService determined |
| 245 | newR1L-SU-236 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the update mode the WiFiUpdateService  |
| 246 | newR1L-SU-237 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the classification the service applied whe |
| 246 | newR1L-SU-237 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the classification the service applied when ./Ex |
| 246 | newR1L-SU-237 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the classification the service applied |
| 247 | newR1L-SU-238 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the signature and integrity verification t |
| 247 | newR1L-SU-238 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the signature and integrity verification the SWD |
| 247 | newR1L-SU-238 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the signature and integrity verificati |
| 248 | newR1L-SU-239 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the protocol used between the head unit an |
| 248 | newR1L-SU-239 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the protocol used between the head unit and the  |
| 248 | newR1L-SU-239 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the protocol used between the head uni |
| 249 | newR1L-SU-240 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 means of observing the validation the SWMC applied before pas |
| 249 | newR1L-SU-240 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to read the validation the SWMC applied before passing u |
| 249 | newR1L-SU-240 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence of the validation the SWMC applied before |
| 250 | newR1L-SU-241 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the TLS handshake between the head unit an |
| 250 | newR1L-SU-241 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the TLS handshake between the head unit and the  |
| 250 | newR1L-SU-241 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the TLS handshake between the head uni |
| 251 | newR1L-SU-242 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the order of the authentication and the se |
| 251 | newR1L-SU-242 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the order of the authentication and the session  |
| 251 | newR1L-SU-242 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the order of the authentication and th |
| 252 | newR1L-SU-243 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the authentication information the SWMC tr |
| 252 | newR1L-SU-243 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the authentication information the SWMC transmit |
| 252 | newR1L-SU-243 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the authentication information the SWM |
| 253 | newR1L-SU-244 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the vehicle details the WiFiUpdateService  |
| 253 | newR1L-SU-244 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the vehicle details the WiFiUpdateService provid |
| 253 | newR1L-SU-244 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the vehicle details the WiFiUpdateServ |
| 254 | newR1L-SU-245 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the source validation the SWMC performed o |
| 254 | newR1L-SU-245 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the source validation the SWMC performed on rece |
| 254 | newR1L-SU-245 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the source validation the SWMC perform |
| 255 | newR1L-SU-246 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the authorisation check the SWMC performed |
| 255 | newR1L-SU-246 | pre | PENDING 佔位（DR-SU7） | 5. PENDING: DR-SU7 means of presenting an unauthorised OTA Server to the head un |
| 255 | newR1L-SU-246 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the authorisation check the SWMC performed on th |
| 255 | newR1L-SU-246 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the authorisation check the SWMC perfo |
| 256 | newR1L-SU-247 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the communication ports the head unit keep |
| 256 | newR1L-SU-247 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the communication ports the head unit keeps open |
| 256 | newR1L-SU-247 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the communication ports the head unit  |
| 257 | newR1L-SU-248 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the authentication algorithm applied at th |
| 257 | newR1L-SU-248 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the authentication algorithm applied at the appl |
| 257 | newR1L-SU-248 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the authentication algorithm applied a |
| 258 | newR1L-SU-249 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the security mechanisms applied when a pro |
| 258 | newR1L-SU-249 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the security mechanisms applied when a proprieta |
| 258 | newR1L-SU-249 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the security mechanisms applied when a |
| 259 | newR1L-SU-250 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging an OMA-DM message that fails integrity verif |
| 259 | newR1L-SU-250 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage an OMA-DM message that fails integrity verifica |
| 259 | newR1L-SU-250 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the head unit received an OMA-DM mes |
| 260 | newR1L-SU-251 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the stored format of the DM Tree |
| 260 | newR1L-SU-251 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the stored format of the DM Tree |
| 260 | newR1L-SU-251 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the stored format of the DM Tree |
| 261 | newR1L-SU-252 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package whose content fails int |
| 261 | newR1L-SU-252 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package whose content fails integr |
| 261 | newR1L-SU-252 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged deployment package fails  |
| 262 | newR1L-SU-253 | pre | PENDING 佔位（DR-SU3） | 3. PENDING: DR-SU3 upstream confirmation whether this requirement's verification |
| 262 | newR1L-SU-253 | proc | PENDING 佔位（DR-SU3） | 1. PENDING: DR-SU3 step to exercise the coordination behaviour separately from t |
| 262 | newR1L-SU-253 | er | PENDING 佔位（DR-SU3） | 1. PENDING: DR-SU3 observable outcome attributable to the coordination behaviour |
| 263 | newR1L-SU-254 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of injecting a socket read or write error during OTA se |
| 263 | newR1L-SU-254 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to inject a socket read or write error during the update |
| 263 | newR1L-SU-254 | proc | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 263 | newR1L-SU-254 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the socket error has occurred |
| 263 | newR1L-SU-254 | er | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 264 | newR1L-SU-255 | proc | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 264 | newR1L-SU-255 | er | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 265 | newR1L-SU-256 | proc | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 265 | newR1L-SU-256 | er | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 266 | newR1L-SU-257 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of placing the vehicle into the emergency state (accide |
| 266 | newR1L-SU-257 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to place the vehicle into the emergency state while the  |
| 266 | newR1L-SU-257 | proc | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 266 | newR1L-SU-257 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the vehicle is in the emergency stat |
| 266 | newR1L-SU-257 | er | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 267 | newR1L-SU-258 | proc | PENDING 佔位（DR-SU4） | 6. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 267 | newR1L-SU-258 | er | PENDING 佔位（DR-SU4） | 6. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 268 | newR1L-SU-259 | proc | PENDING 佔位（DR-SU4） | 6. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 268 | newR1L-SU-259 | er | PENDING 佔位（DR-SU4） | 6. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 269 | newR1L-SU-260 | pre | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 observable indication on the head unit that the OTA client co |
| 269 | newR1L-SU-260 | proc | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 check that the session continued from the state it held when  |
| 269 | newR1L-SU-260 | er | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 observable evidence that the session continued from its previ |
| 270 | newR1L-SU-261 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading, on the OTA Server side, the failure reporte |
| 271 | newR1L-SU-262 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of sending an NIA to this head unit during an active se |
| 271 | newR1L-SU-262 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the queue of received NIAs |
| 271 | newR1L-SU-262 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to send an NIA to the head unit while the session is act |
| 271 | newR1L-SU-262 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read whether the NIA was processed only after the ses |
| 271 | newR1L-SU-262 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that an NIA arrived during the active ses |
| 271 | newR1L-SU-262 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the NIA was processed after the sess |
| 272 | newR1L-SU-263 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the partially downloaded deployment packag |
| 272 | newR1L-SU-263 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read whether the partially downloaded package is stil |
| 272 | newR1L-SU-263 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the partially downloaded package is  |
| 273 | newR1L-SU-264 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the log entry recorded for an interruption |
| 273 | newR1L-SU-264 | pre | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable indication that the session is suspended rather th |
| 273 | newR1L-SU-264 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the log entry recorded for the interruption |
| 273 | newR1L-SU-264 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the log entry recorded for the interru |
| 274 | newR1L-SU-265 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the HTTP request used when a download is r |
| 274 | newR1L-SU-265 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the HTTP request the head unit used to resume th |
| 274 | newR1L-SU-265 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the resumed download used an HTTP by |
| 275 | newR1L-SU-266 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is verified by SWE1-FOT |
| 275 | newR1L-SU-266 | proc | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 step to verify this requirement separately from SWE1-FOTA-328 |
| 275 | newR1L-SU-266 | er | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 observable evidence separating this requirement from SWE1-FOT |
| 277 | newR1L-SU-268 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 value of the configured retry count for resuming an interrupt |
| 277 | newR1L-SU-268 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading the logged failure after the retry count is  |
| 277 | newR1L-SU-268 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to wait until the configured retry count is reached and  |
| 277 | newR1L-SU-268 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the session was aborted after the co |
| 278 | newR1L-SU-269 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the session result  |
| 278 | newR1L-SU-269 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the session result recorded on the OTA Server fo |
| 278 | newR1L-SU-269 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read the session result recorded on the OTA Server fo |
| 278 | newR1L-SU-269 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the session result recorded on the OTA |
| 278 | newR1L-SU-269 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the session result recorded on the OTA |
| 279 | newR1L-SU-270 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the session reports |
| 279 | newR1L-SU-270 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read whether the session report of the interrupted se |
| 279 | newR1L-SU-270 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence that the session report of the interrupte |
| 280 | newR1L-SU-271 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement and SWE1-FOTA-331 are t |
| 280 | newR1L-SU-271 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to distinguish the resend verified here from the resend  |
| 280 | newR1L-SU-271 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this resend from the one v |
| 281 | newR1L-SU-272 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the retry attempts  |
| 281 | newR1L-SU-272 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 value of the configured retry parameter that governs the numb |
| 281 | newR1L-SU-272 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the retry attempts made for the unacknowledged s |
| 281 | newR1L-SU-272 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the retry attempts made for the unackn |
| 282 | newR1L-SU-273 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making an ECU reflash fail during the installation |
| 282 | newR1L-SU-273 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading, on the OTA Server side, the failure report  |
| 282 | newR1L-SU-273 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the ECU reflash fail during the installation |
| 282 | newR1L-SU-273 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the deployment package status code, the ECU faul |
| 282 | newR1L-SU-273 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the ECU reflash failed during the in |
| 282 | newR1L-SU-273 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the deployment package status code, th |
| 285 | newR1L-SU-276 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package that fails authenticity |
| 285 | newR1L-SU-276 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package that fails authenticity ve |
| 285 | newR1L-SU-276 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged deployment package fails  |
| 286 | newR1L-SU-277 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the update status c |
| 286 | newR1L-SU-277 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read the update status codes and software version inf |
| 286 | newR1L-SU-277 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the update status codes and software v |
| 289 | newR1L-SU-280 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the vehicle conditions passed from the WiF |
| 289 | newR1L-SU-280 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the vehicle conditions passed from the WiFiUp |
| 289 | newR1L-SU-280 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the vehicle conditions passed from the |
| 293 | newR1L-SU-284 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the times at which  |
| 293 | newR1L-SU-284 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the polling times recorded on the OTA Server for |
| 293 | newR1L-SU-284 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the polling times recorded on the OT |
| 294 | newR1L-SU-285 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of setting and of reading the polling interval configur |
| 294 | newR1L-SU-285 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to set the polling interval configuration parameter to a |
| 294 | newR1L-SU-285 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to change the polling interval configuration parameter t |
| 294 | newR1L-SU-285 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the polling interval configuration p |
| 294 | newR1L-SU-285 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the polling interval configuration p |
| 295 | newR1L-SU-286 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the queue of vehicle-initiated OTA session |
| 295 | newR1L-SU-286 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of vehicle-initiated OTA sessions afte |
| 295 | newR1L-SU-286 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that a vehicle-initiated OTA session is h |
| 296 | newR1L-SU-287 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the queue of OTA update sessions held by t |
| 296 | newR1L-SU-287 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of OTA update sessions while the batte |
| 296 | newR1L-SU-287 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read the queue of OTA update sessions after the batte |
| 296 | newR1L-SU-287 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the session is held in the queue whi |
| 296 | newR1L-SU-287 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence that the session leaves the queue once th |
| 297 | newR1L-SU-288 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 297 | newR1L-SU-288 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 297 | newR1L-SU-288 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the OTA Server started a session tow |
| 297 | newR1L-SU-288 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 comparison of the screens of the server-started session with  |
| 298 | newR1L-SU-289 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of sending a software inventory request from the OTA Se |
| 298 | newR1L-SU-289 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the software invent |
| 298 | newR1L-SU-289 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send a complete software inventory request from the O |
| 298 | newR1L-SU-289 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the software inventory received by the OTA Serve |
| 298 | newR1L-SU-289 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the software inventory request reach |
| 298 | newR1L-SU-289 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the software inventory received by the |
| 299 | newR1L-SU-290 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the order in which the Deployment Descript |
| 299 | newR1L-SU-290 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the order in which the Deployment Description an |
| 299 | newR1L-SU-290 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the Deployment Description was downl |
| 301 | newR1L-SU-292 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the vehicle and system data handed from th |
| 301 | newR1L-SU-292 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the vehicle and system data handed to the SWMC f |
| 301 | newR1L-SU-292 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the vehicle and system data handed to  |
| 302 | newR1L-SU-293 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the notification sent from the SWMC to the |
| 302 | newR1L-SU-293 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the notification sent to the WiFiUpdateService a |
| 302 | newR1L-SU-293 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the notification sent to the WiFiUpdat |
| 303 | newR1L-SU-294 | pre | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 criterion by which a resumed installation is distinguished fr |
| 303 | newR1L-SU-294 | proc | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 check that the installation resumed from its saved state rath |
| 303 | newR1L-SU-294 | er | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 observable evidence that the installation resumed from its sa |
| 304 | newR1L-SU-295 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the final software  |
| 304 | newR1L-SU-295 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 304 | newR1L-SU-295 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the final software update result received by the |
| 304 | newR1L-SU-295 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the final software update result recei |
| 306 | newR1L-SU-297 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1 |
| 306 | newR1L-SU-297 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the saved download state |
| 306 | newR1L-SU-297 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to interrupt the download at a step other than the one u |
| 306 | newR1L-SU-297 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the saved download state for an interr |
| 307 | newR1L-SU-298 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 307 | newR1L-SU-298 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 307 | newR1L-SU-298 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a server-started update flow is runn |
| 308 | newR1L-SU-299 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the communication between the WiFiUpdateSe |
| 308 | newR1L-SU-299 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether communication with the TC client is esta |
| 308 | newR1L-SU-299 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that communication with the TC client is  |
| 309 | newR1L-SU-300 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the callback registration made with the TC |
| 309 | newR1L-SU-300 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the callback registration parameters used with t |
| 309 | newR1L-SU-300 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the callback was registered with the |
| 310 | newR1L-SU-301 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request through |
| 310 | newR1L-SU-301 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 310 | newR1L-SU-301 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request through th |
| 310 | newR1L-SU-301 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read that the request was forwarded to the SWMC for e |
| 310 | newR1L-SU-301 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request arrived through th |
| 310 | newR1L-SU-301 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the request was forwarded to the SWM |
| 311 | newR1L-SU-302 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request through |
| 311 | newR1L-SU-302 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading, on the OTA Server side, the availability ch |
| 311 | newR1L-SU-302 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request through th |
| 311 | newR1L-SU-302 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the availability check the SWMC made towards the |
| 311 | newR1L-SU-302 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request arrived through th |
| 311 | newR1L-SU-302 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the availability check made towards th |
| 312 | newR1L-SU-303 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request that ca |
| 312 | newR1L-SU-303 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the queue of received session requests |
| 312 | newR1L-SU-303 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request while it c |
| 312 | newR1L-SU-303 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of received session requests |
| 312 | newR1L-SU-303 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request could not be execu |
| 312 | newR1L-SU-303 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the request is held in the queue |
| 313 | newR1L-SU-304 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 313 | newR1L-SU-304 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of distinguishing this queueing from the one verified b |
| 313 | newR1L-SU-304 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 313 | newR1L-SU-304 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of OTA session requests received throu |
| 313 | newR1L-SU-304 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request arrived through th |
| 313 | newR1L-SU-304 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this queued request from t |
| 314 | newR1L-SU-305 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 314 | newR1L-SU-305 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of distinguishing this session from the one verified by |
| 314 | newR1L-SU-305 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 314 | newR1L-SU-305 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to compare the screens of that session with those of a h |
| 314 | newR1L-SU-305 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the session was started through the  |
| 314 | newR1L-SU-305 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this session from the one  |
| 315 | newR1L-SU-306 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the update deployment method configured for  |
| 315 | newR1L-SU-306 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the deployment method configured for each target |
| 315 | newR1L-SU-306 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the deployment method configured for e |
| 316 | newR1L-SU-307 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading which installer was selected for each target |
| 316 | newR1L-SU-307 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of distinguishing this selection from the dispatch veri |
| 316 | newR1L-SU-307 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installer selected for each target component |
| 316 | newR1L-SU-307 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this selection from the di |
| 317 | newR1L-SU-308 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the order in which the components of a deplo |
| 317 | newR1L-SU-308 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the order in which the components were installed |
| 317 | newR1L-SU-308 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the components were installed in the |
| 318 | newR1L-SU-309 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of calling the update progress API of the SW updater HA |
| 318 | newR1L-SU-309 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to call the update progress API for the IOC, GNSS and tu |
| 318 | newR1L-SU-309 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the progress API returned the progre |
| 319 | newR1L-SU-310 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the API interface provided by the Redbend  |
| 319 | newR1L-SU-310 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to read the API interface provided by the Redbend SWMC f |
| 319 | newR1L-SU-310 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence of the API interface provided for Update  |
| 320 | newR1L-SU-311 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the installed image is judged identical to |
| 320 | newR1L-SU-311 | pre | PENDING 佔位（DR-SU6） | 5. PENDING: DR-SU6 means of obtaining the reference deployment image for the sam |
| 320 | newR1L-SU-311 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to compare the installed software image with the referen |
| 320 | newR1L-SU-311 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the installed image is identical to  |
| 321 | newR1L-SU-312 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of staging a campaign whose target is the Update Agent  |
| 321 | newR1L-SU-312 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the Update Agent version on the head unit |
| 321 | newR1L-SU-312 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to stage a campaign whose target is the Update Agent its |
| 321 | newR1L-SU-312 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Update Agent version before and after the up |
| 321 | newR1L-SU-312 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a campaign targeting the Update Agen |
| 321 | newR1L-SU-312 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the Update Agent version changed aft |
| 322 | newR1L-SU-313 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of configuring a target component to use the A/B update |
| 322 | newR1L-SU-313 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which slot a component was installed into |
| 322 | newR1L-SU-313 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to configure a target component to use the A/B update me |
| 322 | newR1L-SU-313 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read which slot the component was installed into |
| 322 | newR1L-SU-313 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the component is configured for the  |
| 322 | newR1L-SU-313 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the slot the component was installed i |
| 323 | newR1L-SU-314 | pre | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 criterion by which a consistent state is judged after an inte |
| 323 | newR1L-SU-314 | proc | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 check that the head unit is in a consistent state after the i |
| 323 | newR1L-SU-314 | er | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 observable evidence that the head unit is in a consistent sta |
| 324 | newR1L-SU-315 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the safety mechanism is judged present in  |
| 324 | newR1L-SU-315 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to exercise the safety mechanism that prevents the SOC f |
| 324 | newR1L-SU-315 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the safety mechanism prevented the S |
| 326 | newR1L-SU-317 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 list of differential update technologies approved by FCA and  |
| 326 | newR1L-SU-317 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading which differential technology was used for a |
| 326 | newR1L-SU-317 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read which differential update technology was used |
| 326 | newR1L-SU-317 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the differential update technology tha |
| 327 | newR1L-SU-318 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the resulting image is judged to match the |
| 327 | newR1L-SU-318 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to read the integrity information validated for the resu |
| 327 | newR1L-SU-318 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the resulting firmware image was val |
| 328 | newR1L-SU-319 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the validity check the Update Agent perfor |
| 328 | newR1L-SU-319 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the result of the validity check performed after |
| 328 | newR1L-SU-319 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the validity check performed after the |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 218／列計 213）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | newR1L-SU-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | newR1L-SU-004 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-006 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | newR1L-SU-007 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | newR1L-SU-008 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | newR1L-SU-009 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | newR1L-SU-011 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-012 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | newR1L-SU-015 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | newR1L-SU-017 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 29 | newR1L-SU-020 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 33 | newR1L-SU-024 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 34 | newR1L-SU-025 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 55 | newR1L-SU-046 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 59 | newR1L-SU-050 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 63 | newR1L-SU-054 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 64 | newR1L-SU-055 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 66 | newR1L-SU-057 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 67 | newR1L-SU-058 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 68 | newR1L-SU-059 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 69 | newR1L-SU-060 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 72 | newR1L-SU-063 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 73 | newR1L-SU-064 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 74 | newR1L-SU-065 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 75 | newR1L-SU-066 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 76 | newR1L-SU-067 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 79 | newR1L-SU-070 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 80 | newR1L-SU-071 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 81 | newR1L-SU-072 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 82 | newR1L-SU-073 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 83 | newR1L-SU-074 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 84 | newR1L-SU-075 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 85 | newR1L-SU-076 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 86 | newR1L-SU-077 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 87 | newR1L-SU-078 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 88 | newR1L-SU-079 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 89 | newR1L-SU-080 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 98 | newR1L-SU-089 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 100 | newR1L-SU-091 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 102 | newR1L-SU-093 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 104 | newR1L-SU-095 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 105 | newR1L-SU-096 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 106 | newR1L-SU-097 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 107 | newR1L-SU-098 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 108 | newR1L-SU-099 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 109 | newR1L-SU-100 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 111 | newR1L-SU-102 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 112 | newR1L-SU-103 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 113 | newR1L-SU-104 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 115 | newR1L-SU-106 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 116 | newR1L-SU-107 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 117 | newR1L-SU-108 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 118 | newR1L-SU-109 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 123 | newR1L-SU-114 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 133 | newR1L-SU-124 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 136 | newR1L-SU-127 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 137 | newR1L-SU-128 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 139 | newR1L-SU-130 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 140 | newR1L-SU-131 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 142 | newR1L-SU-133 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 143 | newR1L-SU-134 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 144 | newR1L-SU-135 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 145 | newR1L-SU-136 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 146 | newR1L-SU-137 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 147 | newR1L-SU-138 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 148 | newR1L-SU-139 | expected_result | 與 newR1L-SU-140 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification |
| 148 | newR1L-SU-139 | expected_result | 與 newR1L-SU-148 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification／prompt |
| 149 | newR1L-SU-140 | expected_result | 與 newR1L-SU-139 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification |
| 149 | newR1L-SU-140 | expected_result | 與 newR1L-SU-148 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification |
| 150 | newR1L-SU-141 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 152 | newR1L-SU-143 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 153 | newR1L-SU-144 | expected_result | 與 newR1L-SU-148 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | confirmation-screen |
| 155 | newR1L-SU-146 | expected_result | 與 newR1L-SU-148 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | confirmation-screen |
| 157 | newR1L-SU-148 | expected_result | 與 newR1L-SU-139 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification／prompt |
| 157 | newR1L-SU-148 | expected_result | 與 newR1L-SU-140 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification |
| 157 | newR1L-SU-148 | expected_result | 與 newR1L-SU-144 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | confirmation-screen |
| 157 | newR1L-SU-148 | expected_result | 與 newR1L-SU-146 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | confirmation-screen |
| 158 | newR1L-SU-149 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 161 | newR1L-SU-152 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 162 | newR1L-SU-153 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 163 | newR1L-SU-154 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 164 | newR1L-SU-155 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 165 | newR1L-SU-156 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 167 | newR1L-SU-158 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 168 | newR1L-SU-159 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 169 | newR1L-SU-160 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 170 | newR1L-SU-161 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 171 | newR1L-SU-162 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 172 | newR1L-SU-163 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 173 | newR1L-SU-164 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 174 | newR1L-SU-165 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 176 | newR1L-SU-167 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 177 | newR1L-SU-168 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 178 | newR1L-SU-169 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 182 | newR1L-SU-173 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 183 | newR1L-SU-174 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 189 | newR1L-SU-180 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 190 | newR1L-SU-181 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 193 | newR1L-SU-184 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 194 | newR1L-SU-185 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 195 | newR1L-SU-186 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 196 | newR1L-SU-187 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 198 | newR1L-SU-189 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 199 | newR1L-SU-190 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 201 | newR1L-SU-192 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 202 | newR1L-SU-193 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 205 | newR1L-SU-196 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 206 | newR1L-SU-197 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 208 | newR1L-SU-199 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 209 | newR1L-SU-200 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 210 | newR1L-SU-201 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 211 | newR1L-SU-202 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 212 | newR1L-SU-203 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 213 | newR1L-SU-204 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 214 | newR1L-SU-205 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 215 | newR1L-SU-206 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 216 | newR1L-SU-207 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 217 | newR1L-SU-208 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 218 | newR1L-SU-209 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 219 | newR1L-SU-210 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 220 | newR1L-SU-211 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 221 | newR1L-SU-212 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 222 | newR1L-SU-213 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 223 | newR1L-SU-214 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 224 | newR1L-SU-215 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 225 | newR1L-SU-216 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 226 | newR1L-SU-217 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 227 | newR1L-SU-218 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 228 | newR1L-SU-219 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 229 | newR1L-SU-220 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 230 | newR1L-SU-221 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 231 | newR1L-SU-222 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 232 | newR1L-SU-223 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 233 | newR1L-SU-224 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 234 | newR1L-SU-225 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 235 | newR1L-SU-226 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 236 | newR1L-SU-227 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 237 | newR1L-SU-228 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 238 | newR1L-SU-229 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 239 | newR1L-SU-230 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 240 | newR1L-SU-231 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 241 | newR1L-SU-232 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 242 | newR1L-SU-233 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 243 | newR1L-SU-234 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 244 | newR1L-SU-235 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 245 | newR1L-SU-236 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 246 | newR1L-SU-237 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 247 | newR1L-SU-238 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 248 | newR1L-SU-239 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 249 | newR1L-SU-240 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 250 | newR1L-SU-241 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 251 | newR1L-SU-242 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 252 | newR1L-SU-243 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 253 | newR1L-SU-244 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 254 | newR1L-SU-245 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 255 | newR1L-SU-246 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 256 | newR1L-SU-247 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 257 | newR1L-SU-248 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 258 | newR1L-SU-249 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 259 | newR1L-SU-250 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 260 | newR1L-SU-251 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 261 | newR1L-SU-252 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 262 | newR1L-SU-253 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 263 | newR1L-SU-254 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 264 | newR1L-SU-255 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 265 | newR1L-SU-256 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 266 | newR1L-SU-257 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 269 | newR1L-SU-260 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 271 | newR1L-SU-262 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 272 | newR1L-SU-263 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 273 | newR1L-SU-264 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 274 | newR1L-SU-265 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 275 | newR1L-SU-266 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 278 | newR1L-SU-269 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 279 | newR1L-SU-270 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 280 | newR1L-SU-271 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 281 | newR1L-SU-272 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 282 | newR1L-SU-273 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 284 | newR1L-SU-275 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 285 | newR1L-SU-276 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 286 | newR1L-SU-277 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 287 | newR1L-SU-278 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 288 | newR1L-SU-279 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 289 | newR1L-SU-280 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 290 | newR1L-SU-281 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 292 | newR1L-SU-283 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 293 | newR1L-SU-284 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 294 | newR1L-SU-285 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 296 | newR1L-SU-287 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 298 | newR1L-SU-289 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 299 | newR1L-SU-290 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 301 | newR1L-SU-292 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 302 | newR1L-SU-293 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 303 | newR1L-SU-294 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 304 | newR1L-SU-295 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 306 | newR1L-SU-297 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 307 | newR1L-SU-298 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 308 | newR1L-SU-299 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 309 | newR1L-SU-300 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 310 | newR1L-SU-301 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 311 | newR1L-SU-302 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 312 | newR1L-SU-303 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 313 | newR1L-SU-304 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 314 | newR1L-SU-305 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 315 | newR1L-SU-306 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 316 | newR1L-SU-307 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 317 | newR1L-SU-308 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 318 | newR1L-SU-309 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 319 | newR1L-SU-310 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 320 | newR1L-SU-311 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 321 | newR1L-SU-312 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 322 | newR1L-SU-313 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 323 | newR1L-SU-314 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 324 | newR1L-SU-315 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 326 | newR1L-SU-317 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 327 | newR1L-SU-318 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 328 | newR1L-SU-319 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### W — ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）（行計 21／列計 20）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 16 | newR1L-SU-007 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ed ⏎ 4. Version_after differs from Version_initial while no configured Wi-Fi netwo |
| 26 | newR1L-SU-017 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ad ⏎ 5. Version_after differs from Version_initial after the Wi-Fi attempt period |
| 64 | newR1L-SU-055 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 4. Version_after equals the version of the package staged on the OTA Server |
| 69 | newR1L-SU-060 | er | 比較關係 'greater than'，而 test_item 上半無數值 | strument cluster is greater than zero ⏎ 2. The "Update Now" selection is made on t |
| 69 | newR1L-SU-060 | er | 比較關係 'greater than'，而 test_item 上半無數值 | strument cluster is greater than zero |
| 86 | newR1L-SU-077 | er | 比較關係 'equals'，而 test_item 上半無數值 | d ⏎ 3. Time_remaining equals the difference between Time_scheduled and Time_now, c |
| 111 | newR1L-SU-102 | er | 比較關係 'equals'，而 test_item 上半無數值 | ions; Version_after equals Version_initial |
| 144 | newR1L-SU-135 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged deployment package h |
| 145 | newR1L-SU-136 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged differential package |
| 147 | newR1L-SU-138 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while one contained update file of th |
| 148 | newR1L-SU-139 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ed ⏎ 5. Version_after differs from Version_initial; the recorded screen content co |
| 154 | newR1L-SU-145 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ed ⏎ 6. Version_after differs from Version_initial; no user input occurred between |
| 156 | newR1L-SU-147 | er | 比較關係 'differs from'，而 test_item 上半無數值 | wn on the head unit differs from Version_initial ⏎ 4. The head unit displays the u |
| 157 | newR1L-SU-148 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ed ⏎ 5. Version_after differs from Version_initial; the recorded screen content, t |
| 259 | newR1L-SU-250 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the head unit received an OMA-D |
| 261 | newR1L-SU-252 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged deployment package f |
| 285 | newR1L-SU-276 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged deployment package f |
| 287 | newR1L-SU-278 | er | 比較關係 'equals'，而 test_item 上半無數值 | d and Version_after equals Version_initial |
| 288 | newR1L-SU-279 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while one of the two configured condi |
| 292 | newR1L-SU-283 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 4. Version_after equals Version_initial while the space left on the head unit |
| 320 | newR1L-SU-311 | er | 比較關係 'identical to'，而 test_item 上半無數值 | installed image is identical to the reference deployment image |

