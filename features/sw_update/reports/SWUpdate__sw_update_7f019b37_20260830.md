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
| 90 | newR1L-SU-081 | test_item | 首字小寫 'he' | he WiFiUpdateService shall ensure that sufficient physical storage space is avai |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 712／列計 195）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-001 | pre | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 confirmation that no safety-related notification condition ap |
| 11 | newR1L-SU-002 | pre | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 confirmation that no safety-related notification condition ap |
| 12 | newR1L-SU-003 | pre | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 list of safety-related notification conditions applicable dur |
| 12 | newR1L-SU-003 | proc | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 step to bring one safety-related condition into effect |
| 12 | newR1L-SU-003 | er | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 observable state showing the safety-related condition is in e |
| 17 | newR1L-SU-008 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of identifying the boundaries between the update check, |
| 17 | newR1L-SU-008 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to record the head unit screen content with the check, d |
| 17 | newR1L-SU-008 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence delimiting the check, download and instal |
| 18 | newR1L-SU-009 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of distinguishing the automatic download request from t |
| 18 | newR1L-SU-009 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe that the deployment package download request  |
| 18 | newR1L-SU-009 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the download request has been issued |
| 19 | newR1L-SU-010 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to observe the point at which deployment package downloa |
| 19 | newR1L-SU-010 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the download completion point |
| 20 | newR1L-SU-011 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of injecting a socket read or write error during OTA se |
| 20 | newR1L-SU-011 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to inject a socket read or write error during the update |
| 20 | newR1L-SU-011 | proc | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 20 | newR1L-SU-011 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the socket error has occurred |
| 20 | newR1L-SU-011 | er | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 21 | newR1L-SU-012 | proc | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 21 | newR1L-SU-012 | er | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 22 | newR1L-SU-013 | proc | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 22 | newR1L-SU-013 | er | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 23 | newR1L-SU-014 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of placing the vehicle into the emergency state (accide |
| 23 | newR1L-SU-014 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to place the vehicle into the emergency state while the  |
| 23 | newR1L-SU-014 | proc | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 23 | newR1L-SU-014 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the vehicle is in the emergency stat |
| 23 | newR1L-SU-014 | er | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 24 | newR1L-SU-015 | proc | PENDING 佔位（DR-SU4） | 6. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 24 | newR1L-SU-015 | er | PENDING 佔位（DR-SU4） | 6. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 25 | newR1L-SU-016 | proc | PENDING 佔位（DR-SU4） | 6. PENDING: DR-SU4 step to check the observable state showing that the head unit |
| 25 | newR1L-SU-016 | er | PENDING 佔位（DR-SU4） | 6. PENDING: DR-SU4 observable state showing that the head unit continues operati |
| 26 | newR1L-SU-017 | pre | PENDING 佔位（DR-SU3） | 3. PENDING: DR-SU3 upstream confirmation whether this requirement's verification |
| 26 | newR1L-SU-017 | proc | PENDING 佔位（DR-SU3） | 1. PENDING: DR-SU3 step to exercise the coordination behaviour separately from t |
| 26 | newR1L-SU-017 | er | PENDING 佔位（DR-SU3） | 1. PENDING: DR-SU3 observable outcome attributable to the coordination behaviour |
| 30 | newR1L-SU-021 | pre | PENDING 佔位（DR-SU5） | 3. PENDING: DR-SU5 bench procedure for running the same head unit against two up |
| 30 | newR1L-SU-021 | proc | PENDING 佔位（DR-SU5） | 3. PENDING: DR-SU5 step to return the head unit to a comparable starting state a |
| 30 | newR1L-SU-021 | er | PENDING 佔位（DR-SU5） | 3. PENDING: DR-SU5 observable state showing the head unit is back at a comparabl |
| 39 | newR1L-SU-030 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making an ROV update fail and roll back on the test  |
| 39 | newR1L-SU-030 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the update fail so that the rollback completes s |
| 39 | newR1L-SU-030 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable state showing $FOTA_Status$ = [FOTA FailureRollbac |
| 40 | newR1L-SU-031 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making an ROV update fail without a successful rollb |
| 40 | newR1L-SU-031 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the update fail so that the failure completes wi |
| 40 | newR1L-SU-031 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable state showing $FOTA_Status$ = [FOTA Failure Comple |
| 61 | newR1L-SU-052 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing this routing path from the one verifi |
| 61 | newR1L-SU-052 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe which service forwarded the version informati |
| 61 | newR1L-SU-052 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the routing path taken by the version  |
| 62 | newR1L-SU-053 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing this routing path from the one verifi |
| 62 | newR1L-SU-053 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe which service forwarded the version informati |
| 62 | newR1L-SU-053 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the routing path taken by the version  |
| 65 | newR1L-SU-056 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 65 | newR1L-SU-056 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the network bearer used for the download afte |
| 65 | newR1L-SU-056 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network bearer used for the downlo |
| 67 | newR1L-SU-058 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 67 | newR1L-SU-058 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the network bearer used for the download whil |
| 67 | newR1L-SU-058 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network bearer used for the downlo |
| 68 | newR1L-SU-059 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 68 | newR1L-SU-059 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the network bearer used for the resumed downl |
| 68 | newR1L-SU-059 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network bearer used for the resume |
| 69 | newR1L-SU-060 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reaching the end of the one week Wi-Fi attempt perio |
| 69 | newR1L-SU-060 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which network bearer the head unit is usin |
| 69 | newR1L-SU-060 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to reach the end of the one week Wi-Fi attempt period |
| 69 | newR1L-SU-060 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to observe the network bearer used for the download afte |
| 69 | newR1L-SU-060 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable state showing that the Wi-Fi attempt period has el |
| 69 | newR1L-SU-060 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the network bearer used for the downlo |
| 70 | newR1L-SU-061 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing a critical update session from a sile |
| 70 | newR1L-SU-061 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to observe that the session in progress is a critical up |
| 70 | newR1L-SU-061 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the session in progress is a critica |
| 75 | newR1L-SU-066 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package whose digital signature |
| 75 | newR1L-SU-066 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package whose digital signature or |
| 75 | newR1L-SU-066 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged deployment package has an |
| 76 | newR1L-SU-067 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a differential deployment package whose decl |
| 76 | newR1L-SU-067 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a differential deployment package whose declare |
| 76 | newR1L-SU-067 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged differential package decl |
| 77 | newR1L-SU-068 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the invocation of the signature verificati |
| 77 | newR1L-SU-068 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the invocation of the signature verification  |
| 77 | newR1L-SU-068 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the invocation of the signature verifi |
| 78 | newR1L-SU-069 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package containing multiple upd |
| 78 | newR1L-SU-069 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package containing multiple update |
| 78 | newR1L-SU-069 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that one contained update file of the sta |
| 79 | newR1L-SU-070 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging an OMA-DM message that fails integrity verif |
| 79 | newR1L-SU-070 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage an OMA-DM message that fails integrity verifica |
| 79 | newR1L-SU-070 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the head unit received an OMA-DM mes |
| 80 | newR1L-SU-071 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the stored format of the DM Tree |
| 80 | newR1L-SU-071 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the stored format of the DM Tree |
| 80 | newR1L-SU-071 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the stored format of the DM Tree |
| 81 | newR1L-SU-072 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package whose content fails int |
| 81 | newR1L-SU-072 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package whose content fails integr |
| 81 | newR1L-SU-072 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged deployment package fails  |
| 82 | newR1L-SU-073 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of staging a deployment package that fails authenticity |
| 82 | newR1L-SU-073 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to stage a deployment package that fails authenticity ve |
| 82 | newR1L-SU-073 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the staged deployment package fails  |
| 87 | newR1L-SU-078 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the vehicle conditions passed from the WiF |
| 87 | newR1L-SU-078 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to observe the vehicle conditions passed from the WiFiUp |
| 87 | newR1L-SU-078 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the vehicle conditions passed from the |
| 110 | newR1L-SU-101 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of placing a Wi-Fi network on the WiFi Manager exclusio |
| 110 | newR1L-SU-101 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to place the access point shown with more signal bars on |
| 110 | newR1L-SU-101 | proc | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 check that the head unit connects to the remaining access poi |
| 110 | newR1L-SU-101 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that a network is on the exclusion list |
| 110 | newR1L-SU-101 | er | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 observable evidence distinguishing this connection from the o |
| 111 | newR1L-SU-102 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the signal strength category assigned to a |
| 111 | newR1L-SU-102 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 values of the predefined Wi-Fi signal strength thresholds tha |
| 111 | newR1L-SU-102 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the signal strength category assigned to each ac |
| 111 | newR1L-SU-102 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the signal strength category assigned  |
| 115 | newR1L-SU-106 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing that the preconditions for software downlo |
| 115 | newR1L-SU-106 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the outcome of the precondition evaluation at th |
| 115 | newR1L-SU-106 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the preconditions for software downl |
| 119 | newR1L-SU-110 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the session result  |
| 119 | newR1L-SU-110 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the session result recorded on the OTA Server fo |
| 119 | newR1L-SU-110 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read the session result recorded on the OTA Server fo |
| 119 | newR1L-SU-110 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the session result recorded on the OTA |
| 119 | newR1L-SU-110 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the session result recorded on the OTA |
| 120 | newR1L-SU-111 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the session reports |
| 120 | newR1L-SU-111 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read whether the session report of the interrupted se |
| 120 | newR1L-SU-111 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence that the session report of the interrupte |
| 121 | newR1L-SU-112 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement and SWE1-FOTA-331 are t |
| 121 | newR1L-SU-112 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to distinguish the resend verified here from the resend  |
| 121 | newR1L-SU-112 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this resend from the one v |
| 122 | newR1L-SU-113 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the retry attempts  |
| 122 | newR1L-SU-113 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 value of the configured retry parameter that governs the numb |
| 122 | newR1L-SU-113 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the retry attempts made for the unacknowledged s |
| 122 | newR1L-SU-113 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the retry attempts made for the unackn |
| 123 | newR1L-SU-114 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making an ECU reflash fail during the installation |
| 123 | newR1L-SU-114 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading, on the OTA Server side, the failure report  |
| 123 | newR1L-SU-114 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the ECU reflash fail during the installation |
| 123 | newR1L-SU-114 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the deployment package status code, the ECU faul |
| 123 | newR1L-SU-114 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the ECU reflash failed during the in |
| 123 | newR1L-SU-114 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the deployment package status code, th |
| 124 | newR1L-SU-115 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the update status c |
| 124 | newR1L-SU-115 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read the update status codes and software version inf |
| 124 | newR1L-SU-115 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence of the update status codes and software v |
| 125 | newR1L-SU-116 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the final software  |
| 125 | newR1L-SU-116 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 125 | newR1L-SU-116 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the final software update result received by the |
| 125 | newR1L-SU-116 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the final software update result recei |
| 128 | newR1L-SU-119 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the ignition cycle counter associated with F |
| 128 | newR1L-SU-119 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the ignition cycle counter while FOTA package da |
| 128 | newR1L-SU-119 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the ignition cycle counter while FOTA  |
| 131 | newR1L-SU-122 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reaching the state in which the FOTA package could n |
| 131 | newR1L-SU-122 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to reach the state in which the FOTA package could not b |
| 131 | newR1L-SU-122 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the FOTA package could not be downlo |
| 132 | newR1L-SU-123 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the times at which  |
| 132 | newR1L-SU-123 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the polling times recorded on the OTA Server for |
| 132 | newR1L-SU-123 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the polling times recorded on the OT |
| 133 | newR1L-SU-124 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of setting and of reading the polling interval configur |
| 133 | newR1L-SU-124 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to set the polling interval configuration parameter to a |
| 133 | newR1L-SU-124 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to change the polling interval configuration parameter t |
| 133 | newR1L-SU-124 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the polling interval configuration p |
| 133 | newR1L-SU-124 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the polling interval configuration p |
| 134 | newR1L-SU-125 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the queue of vehicle-initiated OTA session |
| 134 | newR1L-SU-125 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of vehicle-initiated OTA sessions afte |
| 134 | newR1L-SU-125 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that a vehicle-initiated OTA session is h |
| 135 | newR1L-SU-126 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the queue of OTA update sessions held by t |
| 135 | newR1L-SU-126 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of OTA update sessions while the batte |
| 135 | newR1L-SU-126 | proc | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 step to read the queue of OTA update sessions after the batte |
| 135 | newR1L-SU-126 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the session is held in the queue whi |
| 135 | newR1L-SU-126 | er | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 observable evidence that the session leaves the queue once th |
| 136 | newR1L-SU-127 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 136 | newR1L-SU-127 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 136 | newR1L-SU-127 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the OTA Server started a session tow |
| 136 | newR1L-SU-127 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 comparison of the screens of the server-started session with  |
| 137 | newR1L-SU-128 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of sending a software inventory request from the OTA Se |
| 137 | newR1L-SU-128 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading, on the OTA Server side, the software invent |
| 137 | newR1L-SU-128 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send a complete software inventory request from the O |
| 137 | newR1L-SU-128 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the software inventory received by the OTA Serve |
| 137 | newR1L-SU-128 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the software inventory request reach |
| 137 | newR1L-SU-128 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the software inventory received by the |
| 138 | newR1L-SU-129 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the order in which the Deployment Descript |
| 138 | newR1L-SU-129 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the order in which the Deployment Description an |
| 138 | newR1L-SU-129 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the Deployment Description was downl |
| 140 | newR1L-SU-131 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the vehicle and system data handed from th |
| 140 | newR1L-SU-131 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the vehicle and system data handed to the SWMC f |
| 140 | newR1L-SU-131 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the vehicle and system data handed to  |
| 141 | newR1L-SU-132 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the notification sent from the SWMC to the |
| 141 | newR1L-SU-132 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the notification sent to the WiFiUpdateService a |
| 141 | newR1L-SU-132 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the notification sent to the WiFiUpdat |
| 142 | newR1L-SU-133 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 142 | newR1L-SU-133 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 142 | newR1L-SU-133 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a server-started update flow is runn |
| 143 | newR1L-SU-134 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 143 | newR1L-SU-134 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of distinguishing this queueing from the one verified b |
| 143 | newR1L-SU-134 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 143 | newR1L-SU-134 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of OTA session requests received throu |
| 143 | newR1L-SU-134 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request arrived through th |
| 143 | newR1L-SU-134 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this queued request from t |
| 144 | newR1L-SU-135 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server start a session towards this h |
| 144 | newR1L-SU-135 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of distinguishing this session from the one verified by |
| 144 | newR1L-SU-135 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server start a session towards this head |
| 144 | newR1L-SU-135 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to compare the screens of that session with those of a h |
| 144 | newR1L-SU-135 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the session was started through the  |
| 144 | newR1L-SU-135 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this session from the one  |
| 145 | newR1L-SU-136 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing that TBM-specific FOTA functionality is al |
| 145 | newR1L-SU-136 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of placing the vehicle in a state where $TBM_present$ d |
| 145 | newR1L-SU-136 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether TBM-specific FOTA functionality is allow |
| 145 | newR1L-SU-136 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that TBM-specific FOTA functionality is a |
| 148 | newR1L-SU-139 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of changing the estimated update duration through softw |
| 152 | newR1L-SU-143 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of staging a forced telematics box module update campai |
| 152 | newR1L-SU-143 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to stage a forced telematics box module update campaign |
| 152 | newR1L-SU-143 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the forced telematics box m |
| 152 | newR1L-SU-143 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a forced telematics box module updat |
| 152 | newR1L-SU-143 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the forced telematics box module updat |
| 154 | newR1L-SU-145 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making a telematics box module update fail during it |
| 154 | newR1L-SU-145 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the telematics box module update fail during its |
| 154 | newR1L-SU-145 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the rollback success pop-up |
| 154 | newR1L-SU-145 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the telematics box module update fai |
| 154 | newR1L-SU-145 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the rollback success pop-up after the  |
| 156 | newR1L-SU-147 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making a telematics box module update fail during it |
| 156 | newR1L-SU-147 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to make the telematics box module update fail during its |
| 156 | newR1L-SU-147 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the telematics box module u |
| 156 | newR1L-SU-147 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the telematics box module update fai |
| 156 | newR1L-SU-147 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the telematics box module update failu |
| 158 | newR1L-SU-149 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing the No_Update state from the No_Updat |
| 158 | newR1L-SU-149 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to bring $TBMUpdate$ to the No_Update state rather than  |
| 158 | newR1L-SU-149 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this clearing from the one |
| 162 | newR1L-SU-153 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of placing the SW Update HMI in an unavailable state on |
| 162 | newR1L-SU-153 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to place the SW Update HMI in an unavailable state |
| 162 | newR1L-SU-153 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the deployment package download continues to compl |
| 162 | newR1L-SU-153 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the SW Update HMI is unavailable |
| 162 | newR1L-SU-153 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the download completed with no user  |
| 163 | newR1L-SU-154 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing which installer each component package of  |
| 163 | newR1L-SU-154 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read which installer received the MCPU firmware packa |
| 163 | newR1L-SU-154 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the MCPU firmware package was handed |
| 164 | newR1L-SU-155 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the event handling interface between the S |
| 164 | newR1L-SU-155 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the event sent from the SW Update HMI to the WiF |
| 164 | newR1L-SU-155 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the event sent from the SW Update HMI  |
| 165 | newR1L-SU-156 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request to this |
| 165 | newR1L-SU-156 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of distinguishing this interface from the one verified  |
| 165 | newR1L-SU-156 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request to this he |
| 165 | newR1L-SU-156 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the session request received through the event i |
| 165 | newR1L-SU-156 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the OTA Server sent a session reques |
| 165 | newR1L-SU-156 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this reception from the on |
| 166 | newR1L-SU-157 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request to this |
| 166 | newR1L-SU-157 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the notification from SWMC to WiFiUpdateSe |
| 166 | newR1L-SU-157 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request to this he |
| 166 | newR1L-SU-157 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the notification sent from SWMC to WiFiUpdateSer |
| 166 | newR1L-SU-157 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the OTA Server sent a session reques |
| 166 | newR1L-SU-157 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the notification sent from SWMC to WiF |
| 167 | newR1L-SU-158 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of injecting a vehicle event that blocks software deplo |
| 167 | newR1L-SU-158 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing that the event was evaluated before deploy |
| 167 | newR1L-SU-158 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to inject a vehicle event that blocks software deploymen |
| 167 | newR1L-SU-158 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read whether the injected event was evaluated before  |
| 167 | newR1L-SU-158 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that a blocking vehicle event was injecte |
| 167 | newR1L-SU-158 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the event was evaluated before deplo |
| 168 | newR1L-SU-159 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of reading the polling parameters held by the SWMC |
| 168 | newR1L-SU-159 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing this requirement from SWE1-FOTA-347,  |
| 168 | newR1L-SU-159 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the polling parameters held by the SWMC |
| 168 | newR1L-SU-159 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the polling parameters held by the SWM |
| 169 | newR1L-SU-160 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of sending a polling interval parameter from the OTA Se |
| 169 | newR1L-SU-160 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the polling interval currently applied by th |
| 169 | newR1L-SU-160 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send a new polling interval parameter from the OTA Se |
| 169 | newR1L-SU-160 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the polling interval applied by the SWMC after t |
| 169 | newR1L-SU-160 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the polling interval parameter reach |
| 169 | newR1L-SU-160 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the polling interval applied by the  |
| 170 | newR1L-SU-161 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of updating polling parameters from the OTA Server |
| 170 | newR1L-SU-161 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of distinguishing this update from the one verified by  |
| 170 | newR1L-SU-161 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to update the polling parameters from the OTA Server |
| 170 | newR1L-SU-161 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the polling parameters used in the next vehicle- |
| 170 | newR1L-SU-161 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the polling parameters were updated  |
| 170 | newR1L-SU-161 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this from the update verif |
| 171 | newR1L-SU-162 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of configuring a proprietary communication protocol ins |
| 171 | newR1L-SU-162 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the protocol used between the head unit an |
| 171 | newR1L-SU-162 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to configure a proprietary communication protocol instea |
| 171 | newR1L-SU-162 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the protocol used for the communication with the |
| 171 | newR1L-SU-162 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a proprietary communication protocol |
| 171 | newR1L-SU-162 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that HTTP and TLS were used for the commu |
| 172 | newR1L-SU-163 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of sending a configuration command from the OTA Server  |
| 172 | newR1L-SU-163 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the configuration parameters applied by the  |
| 172 | newR1L-SU-163 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send a session-specific configuration parameter from  |
| 172 | newR1L-SU-163 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the configuration parameters applied by the SWMC |
| 172 | newR1L-SU-163 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the configuration command reached th |
| 172 | newR1L-SU-163 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the SWMC applied the parameter that  |
| 173 | newR1L-SU-164 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of sending a server URL and port configuration command  |
| 173 | newR1L-SU-164 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the server address used by the head unit for |
| 173 | newR1L-SU-164 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send a new server URL and port from the OTA Server |
| 173 | newR1L-SU-164 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the server address used by the next communicatio |
| 173 | newR1L-SU-164 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the new server URL and port reached  |
| 173 | newR1L-SU-164 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the next session used the updated se |
| 174 | newR1L-SU-165 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of sending an invalid server URL and port configuration |
| 174 | newR1L-SU-165 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the server address stored and used by the he |
| 174 | newR1L-SU-165 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send an invalid server URL and port from the OTA Serv |
| 174 | newR1L-SU-165 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the server address used by the head unit after t |
| 174 | newR1L-SU-165 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that an invalid server configuration reac |
| 174 | newR1L-SU-165 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the head unit kept the previously st |
| 175 | newR1L-SU-166 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the update deployment method configured for  |
| 175 | newR1L-SU-166 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the deployment method configured for each target |
| 175 | newR1L-SU-166 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the deployment method configured for e |
| 176 | newR1L-SU-167 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading which installer was selected for each target |
| 176 | newR1L-SU-167 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of distinguishing this selection from the dispatch veri |
| 176 | newR1L-SU-167 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installer selected for each target component |
| 176 | newR1L-SU-167 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this selection from the di |
| 177 | newR1L-SU-168 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the order in which the components of a deplo |
| 177 | newR1L-SU-168 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the order in which the components were installed |
| 177 | newR1L-SU-168 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the components were installed in the |
| 178 | newR1L-SU-169 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of calling the update progress API of the SW updater HA |
| 178 | newR1L-SU-169 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to call the update progress API for the IOC, GNSS and tu |
| 178 | newR1L-SU-169 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the progress API returned the progre |
| 179 | newR1L-SU-170 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the API interface provided by the Redbend  |
| 179 | newR1L-SU-170 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to read the API interface provided by the Redbend SWMC f |
| 179 | newR1L-SU-170 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence of the API interface provided for Update  |
| 180 | newR1L-SU-171 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the installed image is judged identical to |
| 180 | newR1L-SU-171 | pre | PENDING 佔位（DR-SU6） | 5. PENDING: DR-SU6 means of obtaining the reference deployment image for the sam |
| 180 | newR1L-SU-171 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to compare the installed software image with the referen |
| 180 | newR1L-SU-171 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the installed image is identical to  |
| 181 | newR1L-SU-172 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of staging a campaign whose target is the Update Agent  |
| 181 | newR1L-SU-172 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the Update Agent version on the head unit |
| 181 | newR1L-SU-172 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to stage a campaign whose target is the Update Agent its |
| 181 | newR1L-SU-172 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Update Agent version before and after the up |
| 181 | newR1L-SU-172 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a campaign targeting the Update Agen |
| 181 | newR1L-SU-172 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the Update Agent version changed aft |
| 182 | newR1L-SU-173 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of configuring a target component to use the A/B update |
| 182 | newR1L-SU-173 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing which slot a component was installed into |
| 182 | newR1L-SU-173 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to configure a target component to use the A/B update me |
| 182 | newR1L-SU-173 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read which slot the component was installed into |
| 182 | newR1L-SU-173 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the component is configured for the  |
| 182 | newR1L-SU-173 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the slot the component was installed i |
| 183 | newR1L-SU-174 | pre | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 criterion by which a consistent state is judged after an inte |
| 183 | newR1L-SU-174 | proc | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 check that the head unit is in a consistent state after the i |
| 183 | newR1L-SU-174 | er | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 observable evidence that the head unit is in a consistent sta |
| 184 | newR1L-SU-175 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the safety mechanism is judged present in  |
| 184 | newR1L-SU-175 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to exercise the safety mechanism that prevents the SOC f |
| 184 | newR1L-SU-175 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the safety mechanism prevented the S |
| 186 | newR1L-SU-177 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 list of differential update technologies approved by FCA and  |
| 186 | newR1L-SU-177 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading which differential technology was used for a |
| 186 | newR1L-SU-177 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read which differential update technology was used |
| 186 | newR1L-SU-177 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the differential update technology tha |
| 187 | newR1L-SU-178 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the resulting image is judged to match the |
| 187 | newR1L-SU-178 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to read the integrity information validated for the resu |
| 187 | newR1L-SU-178 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the resulting firmware image was val |
| 188 | newR1L-SU-179 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the validity check the Update Agent perfor |
| 188 | newR1L-SU-179 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the result of the validity check performed after |
| 188 | newR1L-SU-179 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the validity check performed after the |
| 189 | newR1L-SU-180 | pre | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 observable indication on the head unit that the OTA client co |
| 189 | newR1L-SU-180 | proc | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 check that the session continued from the state it held when  |
| 189 | newR1L-SU-180 | er | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 observable evidence that the session continued from its previ |
| 190 | newR1L-SU-181 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading, on the OTA Server side, the failure reporte |
| 191 | newR1L-SU-182 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of sending an NIA to this head unit during an active se |
| 191 | newR1L-SU-182 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the queue of received NIAs |
| 191 | newR1L-SU-182 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to send an NIA to the head unit while the session is act |
| 191 | newR1L-SU-182 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read whether the NIA was processed only after the ses |
| 191 | newR1L-SU-182 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that an NIA arrived during the active ses |
| 191 | newR1L-SU-182 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the NIA was processed after the sess |
| 192 | newR1L-SU-183 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the partially downloaded deployment packag |
| 192 | newR1L-SU-183 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read whether the partially downloaded package is stil |
| 192 | newR1L-SU-183 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the partially downloaded package is  |
| 193 | newR1L-SU-184 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the log entry recorded for an interruption |
| 193 | newR1L-SU-184 | pre | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable indication that the session is suspended rather th |
| 193 | newR1L-SU-184 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the log entry recorded for the interruption |
| 193 | newR1L-SU-184 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the log entry recorded for the interru |
| 194 | newR1L-SU-185 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the HTTP request used when a download is r |
| 194 | newR1L-SU-185 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to read the HTTP request the head unit used to resume th |
| 194 | newR1L-SU-185 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the resumed download used an HTTP by |
| 195 | newR1L-SU-186 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is verified by SWE1-FOT |
| 195 | newR1L-SU-186 | proc | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 step to verify this requirement separately from SWE1-FOTA-328 |
| 195 | newR1L-SU-186 | er | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 observable evidence separating this requirement from SWE1-FOT |
| 197 | newR1L-SU-188 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 value of the configured retry count for resuming an interrupt |
| 197 | newR1L-SU-188 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading the logged failure after the retry count is  |
| 197 | newR1L-SU-188 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 step to wait until the configured retry count is reached and  |
| 197 | newR1L-SU-188 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the session was aborted after the co |
| 198 | newR1L-SU-189 | pre | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 criterion by which a resumed installation is distinguished fr |
| 198 | newR1L-SU-189 | proc | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 check that the installation resumed from its saved state rath |
| 198 | newR1L-SU-189 | er | PENDING 佔位（DR-SU4） | 3. PENDING: DR-SU4 observable evidence that the installation resumed from its sa |
| 200 | newR1L-SU-191 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1 |
| 200 | newR1L-SU-191 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the saved download state |
| 200 | newR1L-SU-191 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to interrupt the download at a step other than the one u |
| 200 | newR1L-SU-191 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the saved download state for an interr |
| 201 | newR1L-SU-192 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the communication between the WiFiUpdateSe |
| 201 | newR1L-SU-192 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether communication with the TC client is esta |
| 201 | newR1L-SU-192 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that communication with the TC client is  |
| 202 | newR1L-SU-193 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the callback registration made with the TC |
| 202 | newR1L-SU-193 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the callback registration parameters used with t |
| 202 | newR1L-SU-193 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the callback was registered with the |
| 203 | newR1L-SU-194 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request through |
| 203 | newR1L-SU-194 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 203 | newR1L-SU-194 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request through th |
| 203 | newR1L-SU-194 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read that the request was forwarded to the SWMC for e |
| 203 | newR1L-SU-194 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request arrived through th |
| 203 | newR1L-SU-194 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the request was forwarded to the SWM |
| 204 | newR1L-SU-195 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request through |
| 204 | newR1L-SU-195 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of reading, on the OTA Server side, the availability ch |
| 204 | newR1L-SU-195 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request through th |
| 204 | newR1L-SU-195 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the availability check the SWMC made towards the |
| 204 | newR1L-SU-195 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request arrived through th |
| 204 | newR1L-SU-195 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the availability check made towards th |
| 205 | newR1L-SU-196 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the OTA Server send a session request that ca |
| 205 | newR1L-SU-196 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the queue of received session requests |
| 205 | newR1L-SU-196 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the OTA Server send a session request while it c |
| 205 | newR1L-SU-196 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the queue of received session requests |
| 205 | newR1L-SU-196 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a session request could not be execu |
| 205 | newR1L-SU-196 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the request is held in the queue |
| 206 | newR1L-SU-197 | pre | PENDING 佔位（DR-SU6） | 3. PENDING: DR-SU6 criterion by which the absence of a dependency on a specific  |
| 206 | newR1L-SU-197 | proc | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 step to establish that the OTA client does not depend on a sp |
| 206 | newR1L-SU-197 | er | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 observable evidence that the OTA client does not depend on a  |
| 207 | newR1L-SU-198 | pre | PENDING 佔位（DR-SU6） | 5. PENDING: DR-SU6 list of the diagnostic trouble codes that count as intended d |
| 207 | newR1L-SU-198 | proc | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 check that DTC_after contains no code outside the list of cod |
| 207 | newR1L-SU-198 | er | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 observable evidence that DTC_after contains no unintended cod |
| 208 | newR1L-SU-199 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of recording the diagnostic messages on the vehicle com |
| 208 | newR1L-SU-199 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the diagnostic messages sent to the external ECU |
| 208 | newR1L-SU-199 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of periodic Tester Present messages durin |
| 209 | newR1L-SU-200 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the messages exchanged between distributed |
| 209 | newR1L-SU-200 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the session information and workflow events exch |
| 209 | newR1L-SU-200 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the messages exchanged between the com |
| 211 | newR1L-SU-202 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1 |
| 211 | newR1L-SU-202 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 list of the vehicle-specific preconditions and their configur |
| 211 | newR1L-SU-202 | proc | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 step to verify this requirement separately from the individua |
| 211 | newR1L-SU-202 | er | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 observable evidence separating this requirement from the indi |
| 212 | newR1L-SU-203 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the VIN the WiFi Update Service read for t |
| 212 | newR1L-SU-203 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the VIN the service used for the OTA workflow |
| 212 | newR1L-SU-203 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the VIN used for the OTA workflow |
| 213 | newR1L-SU-204 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the vehicle brand the service provided to  |
| 213 | newR1L-SU-204 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 213 | newR1L-SU-204 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the brand value provided to the SWMC from the VC |
| 213 | newR1L-SU-204 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the brand value taken from the VC_VEH_ |
| 214 | newR1L-SU-205 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of observing the brand value the service read from the  |
| 214 | newR1L-SU-205 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 214 | newR1L-SU-205 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the brand value provided to the SWMC from the pr |
| 214 | newR1L-SU-205 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the brand value taken from the proxi p |
| 215 | newR1L-SU-206 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading which installer each component package was r |
| 215 | newR1L-SU-206 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 215 | newR1L-SU-206 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installer that received the MCPU firmware pa |
| 215 | newR1L-SU-206 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence distinguishing this routing from the one  |
| 216 | newR1L-SU-207 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the installation order and the installer sta |
| 216 | newR1L-SU-207 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 216 | newR1L-SU-207 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether a dependent component waited for its pre |
| 216 | newR1L-SU-207 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that a dependent component waited for its |
| 217 | newR1L-SU-208 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of the  |
| 217 | newR1L-SU-208 | proc | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 step to verify this requirement separately from the individua |
| 217 | newR1L-SU-208 | er | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 observable evidence separating this requirement from the indi |
| 218 | newR1L-SU-209 | pre | PENDING 佔位（DR-SU6） | 3. PENDING: DR-SU6 criterion by which portability across frameworks is judged on |
| 218 | newR1L-SU-209 | proc | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 step to establish that the HMI architecture supports portabil |
| 218 | newR1L-SU-209 | er | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 observable evidence that the HMI architecture supports portab |
| 220 | newR1L-SU-211 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of recording the protocol exchange between the head uni |
| 220 | newR1L-SU-211 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the protocol exchange between the head unit and  |
| 220 | newR1L-SU-211 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the exchange follows the OMA-DM SCOM |
| 221 | newR1L-SU-212 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of reading the SCOMO management of the individual compo |
| 221 | newR1L-SU-212 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read how the individual components were managed throu |
| 221 | newR1L-SU-212 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the SCOMO management of the individual |
| 222 | newR1L-SU-213 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the network availability notification sent |
| 222 | newR1L-SU-213 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the network availability notification sent from  |
| 222 | newR1L-SU-213 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network availability notification  |
| 223 | newR1L-SU-214 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the URL the SWMC used to download the depl |
| 223 | newR1L-SU-214 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 223 | newR1L-SU-214 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the URL the SWMC used to download the deployment |
| 223 | newR1L-SU-214 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the URL the SWMC used to download the  |
| 224 | newR1L-SU-215 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the Download Descriptor the SWMC read and  |
| 224 | newR1L-SU-215 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 224 | newR1L-SU-215 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Download Descriptor the SWMC read and the UR |
| 224 | newR1L-SU-215 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the Download Descriptor the SWMC read  |
| 225 | newR1L-SU-216 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which independence from the operating system and |
| 225 | newR1L-SU-216 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the storage went through the abstract  |
| 225 | newR1L-SU-216 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the storage was independent of the o |
| 226 | newR1L-SU-217 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the invocation of the Redbend Update Agent |
| 226 | newR1L-SU-217 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the invocation of the Redbend Update Agent for t |
| 226 | newR1L-SU-217 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the invocation of the Redbend Update A |
| 227 | newR1L-SU-218 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the protocol the SWMC used to communicate  |
| 227 | newR1L-SU-218 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 227 | newR1L-SU-218 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the protocol the SWMC used to communicate with t |
| 227 | newR1L-SU-218 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the protocol the SWMC used to communic |
| 228 | newR1L-SU-219 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the Download Descriptor processed when a p |
| 228 | newR1L-SU-219 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of configuring a proprietary communication protocol |
| 228 | newR1L-SU-219 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Download Descriptor processed when a proprie |
| 228 | newR1L-SU-219 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the Download Descriptor processed when |
| 229 | newR1L-SU-220 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the vehicle properties the WiFiUpdateServi |
| 229 | newR1L-SU-220 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the vehicle properties the WiFiUpdateService ret |
| 229 | newR1L-SU-220 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the vehicle properties the WiFiUpdateS |
| 230 | newR1L-SU-221 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the installer invoked for the installation |
| 230 | newR1L-SU-221 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 230 | newR1L-SU-221 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installer invoked for the installation metho |
| 230 | newR1L-SU-221 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the installer invoked for the installa |
| 231 | newR1L-SU-222 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the ECU reference IDs used to associate th |
| 231 | newR1L-SU-222 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the ECU reference IDs used to associate the upda |
| 231 | newR1L-SU-222 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the ECU reference IDs used to associat |
| 232 | newR1L-SU-223 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which portability with the Android operating sys |
| 232 | newR1L-SU-223 | proc | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 step to establish that the Redbend Update Agent is portable w |
| 232 | newR1L-SU-223 | er | PENDING 佔位（DR-SU6） | 1. PENDING: DR-SU6 observable evidence that the Redbend Update Agent is portable |
| 233 | newR1L-SU-224 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the OMA-DM protocol stack the SWMC used to |
| 233 | newR1L-SU-224 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 233 | newR1L-SU-224 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the OMA-DM protocol stack the SWMC used towards  |
| 233 | newR1L-SU-224 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the OMA-DM protocol stack the SWMC use |
| 234 | newR1L-SU-225 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the image update ran independently of any  |
| 234 | newR1L-SU-225 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the image update ran independently of  |
| 234 | newR1L-SU-225 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the image update ran independently o |
| 235 | newR1L-SU-226 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the file-system update ran independently o |
| 235 | newR1L-SU-226 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the file-system update ran independent |
| 235 | newR1L-SU-226 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the file-system update ran independe |
| 236 | newR1L-SU-227 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing whether the SWMC is in its idle state |
| 236 | newR1L-SU-227 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether the SWMC is in its idle state |
| 236 | newR1L-SU-227 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of whether the SWMC is in its idle state |
| 237 | newR1L-SU-228 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the CPU and RAM utilisation while idle cou |
| 237 | newR1L-SU-228 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the CPU and RAM utilisation while idle |
| 237 | newR1L-SU-228 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the CPU and RAM utilisation while id |
| 238 | newR1L-SU-229 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which the HMI performance during a background do |
| 238 | newR1L-SU-229 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the HMI performance during a backgroun |
| 238 | newR1L-SU-229 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that the HMI performance during a backgro |
| 239 | newR1L-SU-230 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which navigation and radio count as not impacted |
| 239 | newR1L-SU-230 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that navigation and radio count as not impa |
| 239 | newR1L-SU-230 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that navigation and radio count as not im |
| 240 | newR1L-SU-231 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the status report the SWMC sent on complet |
| 240 | newR1L-SU-231 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 240 | newR1L-SU-231 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the status report the SWMC sent on completion, r |
| 240 | newR1L-SU-231 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the status report the SWMC sent on com |
| 242 | newR1L-SU-233 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the classification the WiFi Update Service |
| 242 | newR1L-SU-233 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the classification the WiFi Update Service appli |
| 242 | newR1L-SU-233 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the classification the WiFi Update Ser |
| 244 | newR1L-SU-235 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the bearer the head unit used for a critic |
| 244 | newR1L-SU-235 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the bearer the head unit used for a critical upd |
| 244 | newR1L-SU-235 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the bearer the head unit used for a cr |
| 245 | newR1L-SU-236 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1 |
| 246 | newR1L-SU-237 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the parameter values the SWMC received fro |
| 246 | newR1L-SU-237 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the parameter values the SWMC received from the  |
| 246 | newR1L-SU-237 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the parameter values the SWMC received |
| 247 | newR1L-SU-238 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the Download Descriptor the SWMC parsed an |
| 247 | newR1L-SU-238 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the Download Descriptor the SWMC parsed and the  |
| 247 | newR1L-SU-238 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the Download Descriptor the SWMC parse |
| 248 | newR1L-SU-239 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the component packages extracted from the  |
| 248 | newR1L-SU-239 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 248 | newR1L-SU-239 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the component packages extracted from the deploy |
| 248 | newR1L-SU-239 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the component packages extracted from  |
| 249 | newR1L-SU-240 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the MCPU installation status the Update En |
| 249 | newR1L-SU-240 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the MCPU installation status the Update Engine r |
| 249 | newR1L-SU-240 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the MCPU installation status the Updat |
| 254 | newR1L-SU-245 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which `not impact other systems, screens, or veh |
| 254 | newR1L-SU-245 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the download did not impact other syst |
| 254 | newR1L-SU-245 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that no other system, screen or vehicle f |
| 262 | newR1L-SU-253 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of observing the transition request the WiFi Update Ser |
| 264 | newR1L-SU-255 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the precondition evaluation the service pe |
| 264 | newR1L-SU-255 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of SWE1 |
| 264 | newR1L-SU-255 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the precondition evaluation the service performe |
| 264 | newR1L-SU-255 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the precondition evaluation the servic |
| 267 | newR1L-SU-258 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the installation failure status reported t |
| 267 | newR1L-SU-258 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of making an installation fail |
| 267 | newR1L-SU-258 | pre | PENDING 佔位（DR-SU3） | 6. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 267 | newR1L-SU-258 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installation failure status reported through |
| 267 | newR1L-SU-258 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the installation failure status report |
| 268 | newR1L-SU-259 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which eCall availability during an update is jud |
| 268 | newR1L-SU-259 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of exercising eCall on the bench without placing an eme |
| 268 | newR1L-SU-259 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that eCall functionality remained operation |
| 268 | newR1L-SU-259 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence that eCall functionality remained operati |
| 270 | newR1L-SU-261 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the OTA session status the service set aft |
| 270 | newR1L-SU-261 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of making an installation fail |
| 270 | newR1L-SU-261 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the OTA session status the service set after an  |
| 270 | newR1L-SU-261 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the OTA session status the service set |
| 271 | newR1L-SU-262 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of producing a vehicle motion event while an installati |
| 271 | newR1L-SU-262 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to produce a vehicle motion event while the installation |
| 271 | newR1L-SU-262 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the installation continued without interruption |
| 271 | newR1L-SU-262 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of a vehicle motion event during the inst |
| 271 | newR1L-SU-262 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the installation continued without i |
| 273 | newR1L-SU-264 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the installation failure status reported b |
| 273 | newR1L-SU-264 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of making an installation fail |
| 273 | newR1L-SU-264 | pre | PENDING 佔位（DR-SU3） | 6. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 273 | newR1L-SU-264 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installation failure status reported by the  |
| 273 | newR1L-SU-264 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the installation failure status report |
| 274 | newR1L-SU-265 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the value set on $HUFOTACheck$ and its tra |
| 274 | newR1L-SU-265 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the value set on $HUFOTACheck$ and its transmiss |
| 274 | newR1L-SU-265 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the value set on $HUFOTACheck$ and its |
| 275 | newR1L-SU-266 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the availability response the SWMC receive |
| 275 | newR1L-SU-266 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the availability response the SWMC received from |
| 275 | newR1L-SU-266 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the availability response the SWMC rec |
| 276 | newR1L-SU-267 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of staging two or more update types simultaneously for  |
| 276 | newR1L-SU-267 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 configured priority order between the update types |
| 276 | newR1L-SU-267 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to stage two update types simultaneously |
| 276 | newR1L-SU-267 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 check that the update type with the higher configured priorit |
| 276 | newR1L-SU-267 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that two update types are available simul |
| 276 | newR1L-SU-267 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the higher priority update type ran  |
| 280 | newR1L-SU-271 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the compatibility check the service perfor |
| 280 | newR1L-SU-271 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the compatibility check the service performed be |
| 280 | newR1L-SU-271 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the compatibility check the service pe |
| 281 | newR1L-SU-272 | pre | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 means of making a software update and a map update available  |
| 281 | newR1L-SU-272 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make a software update and a map update available at  |
| 281 | newR1L-SU-272 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 check that the software update session runs before the map up |
| 281 | newR1L-SU-272 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that both update types are available |
| 281 | newR1L-SU-272 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the software update ran first |
| 284 | newR1L-SU-275 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the FOTA Master to report no FOTA event on it |
| 284 | newR1L-SU-275 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the FOTA Master to report no FOTA event on its s |
| 284 | newR1L-SU-275 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit shows no forced update HMI in that s |
| 284 | newR1L-SU-275 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence of the FOTA Master to report no FOTA even |
| 284 | newR1L-SU-275 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit shows no forced update |
| 285 | newR1L-SU-276 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the FOTA Master to report a cancellation reas |
| 285 | newR1L-SU-276 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the FOTA Master to report a cancellation reason  |
| 285 | newR1L-SU-276 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the stored cancellation rea |
| 285 | newR1L-SU-276 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence of the FOTA Master to report a cancellati |
| 285 | newR1L-SU-276 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit displays the stored ca |
| 286 | newR1L-SU-277 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the FOTA Master to report that delaying the u |
| 286 | newR1L-SU-277 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the FOTA Master to report that delaying the upda |
| 286 | newR1L-SU-277 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit offers no delay option and requires  |
| 286 | newR1L-SU-277 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence of the FOTA Master to report that delayin |
| 286 | newR1L-SU-277 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit offers no delay option |
| 287 | newR1L-SU-278 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the source from which the ROV FOTA AppServ |
| 287 | newR1L-SU-278 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the source from which the ROV FOTA AppService re |
| 287 | newR1L-SU-278 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the source from which the ROV FOTA App |
| 288 | newR1L-SU-279 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the HMI information carried on the Etherne |
| 288 | newR1L-SU-279 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the HMI information carried on the Ethernet mess |
| 288 | newR1L-SU-279 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the HMI information carried on the Eth |
| 289 | newR1L-SU-280 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of making the FOTA Master to report that it is waiting  |
| 289 | newR1L-SU-280 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to make the FOTA Master to report that it is waiting for |
| 289 | newR1L-SU-280 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit prompts the user to accept, delay or |
| 289 | newR1L-SU-280 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence of the FOTA Master to report that it is w |
| 289 | newR1L-SU-280 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that the head unit prompts the user to ac |
| 291 | newR1L-SU-282 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the update progress information the servic |
| 291 | newR1L-SU-282 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the update progress information the service extr |
| 291 | newR1L-SU-282 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the update progress information the se |
| 292 | newR1L-SU-283 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the estimated TBM update time the service  |
| 292 | newR1L-SU-283 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 292 | newR1L-SU-283 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the estimated TBM update time the service extrac |
| 292 | newR1L-SU-283 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the estimated TBM update time the serv |
| 293 | newR1L-SU-284 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the WhatsNew information the service extra |
| 293 | newR1L-SU-284 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 293 | newR1L-SU-284 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the WhatsNew information the service extracted f |
| 293 | newR1L-SU-284 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the WhatsNew information the service e |
| 294 | newR1L-SU-285 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the MQTT subscription the SWMC made toward |
| 294 | newR1L-SU-285 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the MQTT subscription the SWMC made towards the  |
| 294 | newR1L-SU-285 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the MQTT subscription the SWMC made to |
| 296 | newR1L-SU-287 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the installation progress information carr |
| 296 | newR1L-SU-287 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the installation progress information carried on |
| 296 | newR1L-SU-287 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the installation progress information  |
| 297 | newR1L-SU-288 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the cancellation reason value the ROV Upda |
| 297 | newR1L-SU-288 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of making the FOTA Master report a cancellation reason |
| 297 | newR1L-SU-288 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the cancellation reason value the ROV Update Ser |
| 297 | newR1L-SU-288 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the cancellation reason value the ROV  |
| 299 | newR1L-SU-290 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 value of the configured response handling period |
| 299 | newR1L-SU-290 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to wait for the configured response handling period and  |
| 299 | newR1L-SU-290 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the notification is treated as not a |
| 300 | newR1L-SU-291 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the values of FOTA_TBM_Notification, FOTA_ |
| 300 | newR1L-SU-291 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the values of FOTA_TBM_Notification, FOTA_TBM_Fo |
| 300 | newR1L-SU-291 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the values of FOTA_TBM_Notification, F |
| 301 | newR1L-SU-292 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of setting the FOTA_TBM_Notification indicator |
| 301 | newR1L-SU-292 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to set the FOTA_TBM_Notification indicator while the veh |
| 301 | newR1L-SU-292 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the TBM update notification |
| 301 | newR1L-SU-292 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the FOTA_TBM_Notification indicator  |
| 301 | newR1L-SU-292 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the TBM update notification |
| 302 | newR1L-SU-293 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of setting the FOTA_TBM_Forced indicator |
| 302 | newR1L-SU-293 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to set the FOTA_TBM_Forced indicator while the vehicle i |
| 302 | newR1L-SU-293 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that the head unit displays the forced TBM update scree |
| 302 | newR1L-SU-293 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the FOTA_TBM_Forced indicator is set |
| 302 | newR1L-SU-293 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence of the forced TBM update screen |
| 303 | newR1L-SU-294 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 criterion by which conformance to the HMI logic and flow spec |
| 303 | newR1L-SU-294 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to establish that the user interface followed the HMI lo |
| 303 | newR1L-SU-294 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence of conformance to the HMI logic and flow  |
| 304 | newR1L-SU-295 | pre | PENDING 佔位（DR-SU3） | 4. PENDING: DR-SU3 confirmation whether this requirement is the umbrella of the  |
| 304 | newR1L-SU-295 | proc | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 step to verify this requirement separately from the individua |
| 304 | newR1L-SU-295 | er | PENDING 佔位（DR-SU3） | 2. PENDING: DR-SU3 observable evidence separating this requirement from the indi |
| 306 | newR1L-SU-297 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of sending a New Installation Announcement to this head |
| 306 | newR1L-SU-297 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to send a New Installation Announcement to this head uni |
| 306 | newR1L-SU-297 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 check that an OTA update session started without any action o |
| 306 | newR1L-SU-297 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that a New Installation Announcement reac |
| 306 | newR1L-SU-297 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that a session started without any action |
| 307 | newR1L-SU-298 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the session trigger notifications received |
| 307 | newR1L-SU-298 | pre | PENDING 佔位（DR-SU3） | 5. PENDING: DR-SU3 confirmation of what distinguishes this requirement from SWE1 |
| 307 | newR1L-SU-298 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the session trigger notifications received throu |
| 307 | newR1L-SU-298 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the session trigger notifications rece |
| 308 | newR1L-SU-299 | pre | PENDING 佔位（DR-SU2） | 5. PENDING: DR-SU2 means of staging a deployment package whose integrity validat |
| 308 | newR1L-SU-299 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to stage a deployment package whose integrity validation |
| 308 | newR1L-SU-299 | proc | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 check that no installation started for the package that fails |
| 308 | newR1L-SU-299 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that the staged package fails its integri |
| 308 | newR1L-SU-299 | er | PENDING 佔位（DR-SU2） | 3. PENDING: DR-SU2 observable evidence that no installation started |
| 309 | newR1L-SU-300 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of producing an ECU configuration change event such as  |
| 309 | newR1L-SU-300 | proc | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 step to produce an ECU configuration change event |
| 309 | newR1L-SU-300 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read whether the WiFi Update Service received the eve |
| 309 | newR1L-SU-300 | er | PENDING 佔位（DR-SU2） | 1. PENDING: DR-SU2 observable evidence that an ECU configuration change event oc |
| 309 | newR1L-SU-300 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence that the event reached the WiFi Update Se |
| 310 | newR1L-SU-301 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the network the WiFiUpdateService selected |
| 310 | newR1L-SU-301 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the network the WiFiUpdateService selected and t |
| 310 | newR1L-SU-301 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network the WiFiUpdateService sele |
| 311 | newR1L-SU-302 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the update type the WiFiUpdateService dete |
| 311 | newR1L-SU-302 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the update type the WiFiUpdateService determined |
| 311 | newR1L-SU-302 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the update type the WiFiUpdateService  |
| 312 | newR1L-SU-303 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the update mode the WiFiUpdateService dete |
| 312 | newR1L-SU-303 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the update mode the WiFiUpdateService determined |
| 312 | newR1L-SU-303 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the update mode the WiFiUpdateService  |
| 313 | newR1L-SU-304 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the classification the service applied whe |
| 313 | newR1L-SU-304 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the classification the service applied when ./Ex |
| 313 | newR1L-SU-304 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the classification the service applied |
| 314 | newR1L-SU-305 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the signature and integrity verification t |
| 314 | newR1L-SU-305 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the signature and integrity verification the SWD |
| 314 | newR1L-SU-305 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the signature and integrity verificati |
| 315 | newR1L-SU-306 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the protocol used between the head unit an |
| 315 | newR1L-SU-306 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the protocol used between the head unit and the  |
| 315 | newR1L-SU-306 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the protocol used between the head uni |
| 316 | newR1L-SU-307 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 means of observing the validation the SWMC applied before pas |
| 316 | newR1L-SU-307 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to read the validation the SWMC applied before passing u |
| 316 | newR1L-SU-307 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence of the validation the SWMC applied before |
| 317 | newR1L-SU-308 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the TLS handshake between the head unit an |
| 317 | newR1L-SU-308 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the TLS handshake between the head unit and the  |
| 317 | newR1L-SU-308 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the TLS handshake between the head uni |
| 318 | newR1L-SU-309 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the order of the authentication and the se |
| 318 | newR1L-SU-309 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the order of the authentication and the session  |
| 318 | newR1L-SU-309 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the order of the authentication and th |
| 319 | newR1L-SU-310 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the authentication information the SWMC tr |
| 319 | newR1L-SU-310 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the authentication information the SWMC transmit |
| 319 | newR1L-SU-310 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the authentication information the SWM |
| 320 | newR1L-SU-311 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the vehicle details the WiFiUpdateService  |
| 320 | newR1L-SU-311 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the vehicle details the WiFiUpdateService provid |
| 320 | newR1L-SU-311 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the vehicle details the WiFiUpdateServ |
| 321 | newR1L-SU-312 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the source validation the SWMC performed o |
| 321 | newR1L-SU-312 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the source validation the SWMC performed on rece |
| 321 | newR1L-SU-312 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the source validation the SWMC perform |
| 322 | newR1L-SU-313 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the authorisation check the SWMC performed |
| 322 | newR1L-SU-313 | pre | PENDING 佔位（DR-SU7） | 5. PENDING: DR-SU7 means of presenting an unauthorised OTA Server to the head un |
| 322 | newR1L-SU-313 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the authorisation check the SWMC performed on th |
| 322 | newR1L-SU-313 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the authorisation check the SWMC perfo |
| 323 | newR1L-SU-314 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the communication ports the head unit keep |
| 323 | newR1L-SU-314 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the communication ports the head unit keeps open |
| 323 | newR1L-SU-314 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the communication ports the head unit  |
| 324 | newR1L-SU-315 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the authentication algorithm applied at th |
| 324 | newR1L-SU-315 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the authentication algorithm applied at the appl |
| 324 | newR1L-SU-315 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the authentication algorithm applied a |
| 325 | newR1L-SU-316 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the security mechanisms applied when a pro |
| 325 | newR1L-SU-316 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the security mechanisms applied when a proprieta |
| 325 | newR1L-SU-316 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the security mechanisms applied when a |
| 326 | newR1L-SU-317 | pre | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 which start point the 30 minutes is counted from: the start o |
| 326 | newR1L-SU-317 | proc | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 step to record the start point from which the 30 minutes is c |
| 326 | newR1L-SU-317 | proc | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 check that the download session ends and the head unit hotspo |
| 326 | newR1L-SU-317 | er | PENDING 佔位（DR-SU4） | 4. PENDING: DR-SU4 observable evidence of the start point from which the 30 minu |
| 326 | newR1L-SU-317 | er | PENDING 佔位（DR-SU4） | 5. PENDING: DR-SU4 observable evidence that the download session ended and the h |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 218／列計 213）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-001 | expected_result | 與 newR1L-SU-002 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification |
| 10 | newR1L-SU-001 | expected_result | 與 newR1L-SU-008 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification／prompt |
| 11 | newR1L-SU-002 | expected_result | 與 newR1L-SU-001 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification |
| 11 | newR1L-SU-002 | expected_result | 與 newR1L-SU-008 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification |
| 12 | newR1L-SU-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-006 | expected_result | 與 newR1L-SU-008 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | confirmation-screen |
| 16 | newR1L-SU-007 | expected_result | 與 newR1L-SU-008 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | confirmation-screen |
| 17 | newR1L-SU-008 | expected_result | 與 newR1L-SU-001 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification／prompt |
| 17 | newR1L-SU-008 | expected_result | 與 newR1L-SU-002 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | progress-notification |
| 17 | newR1L-SU-008 | expected_result | 與 newR1L-SU-006 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | confirmation-screen |
| 17 | newR1L-SU-008 | expected_result | 與 newR1L-SU-007 之觀測窗相同（availability-check → software-version-changes）且違例類有交集 | confirmation-screen |
| 18 | newR1L-SU-009 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | newR1L-SU-011 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-012 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | newR1L-SU-013 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | newR1L-SU-014 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | newR1L-SU-017 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 27 | newR1L-SU-018 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 28 | newR1L-SU-019 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 29 | newR1L-SU-020 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 31 | newR1L-SU-022 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 32 | newR1L-SU-023 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 33 | newR1L-SU-024 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 35 | newR1L-SU-026 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 36 | newR1L-SU-027 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 39 | newR1L-SU-030 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 40 | newR1L-SU-031 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 41 | newR1L-SU-032 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 44 | newR1L-SU-035 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 45 | newR1L-SU-036 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 46 | newR1L-SU-037 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 47 | newR1L-SU-038 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 48 | newR1L-SU-039 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 49 | newR1L-SU-040 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 50 | newR1L-SU-041 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 51 | newR1L-SU-042 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 52 | newR1L-SU-043 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 53 | newR1L-SU-044 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 54 | newR1L-SU-045 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 55 | newR1L-SU-046 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 56 | newR1L-SU-047 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 57 | newR1L-SU-048 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 58 | newR1L-SU-049 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 59 | newR1L-SU-050 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 61 | newR1L-SU-052 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 62 | newR1L-SU-053 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 63 | newR1L-SU-054 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 64 | newR1L-SU-055 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 65 | newR1L-SU-056 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 67 | newR1L-SU-058 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 68 | newR1L-SU-059 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 69 | newR1L-SU-060 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 74 | newR1L-SU-065 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 75 | newR1L-SU-066 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 76 | newR1L-SU-067 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 77 | newR1L-SU-068 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 78 | newR1L-SU-069 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 79 | newR1L-SU-070 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 80 | newR1L-SU-071 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 81 | newR1L-SU-072 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 82 | newR1L-SU-073 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 84 | newR1L-SU-075 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 85 | newR1L-SU-076 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 86 | newR1L-SU-077 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 87 | newR1L-SU-078 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 88 | newR1L-SU-079 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 90 | newR1L-SU-081 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 91 | newR1L-SU-082 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 111 | newR1L-SU-102 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 115 | newR1L-SU-106 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 119 | newR1L-SU-110 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 120 | newR1L-SU-111 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 121 | newR1L-SU-112 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 122 | newR1L-SU-113 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 123 | newR1L-SU-114 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 124 | newR1L-SU-115 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 125 | newR1L-SU-116 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 126 | newR1L-SU-117 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 128 | newR1L-SU-119 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 129 | newR1L-SU-120 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 131 | newR1L-SU-122 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 132 | newR1L-SU-123 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 133 | newR1L-SU-124 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 135 | newR1L-SU-126 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 137 | newR1L-SU-128 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 138 | newR1L-SU-129 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 140 | newR1L-SU-131 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 141 | newR1L-SU-132 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 142 | newR1L-SU-133 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 143 | newR1L-SU-134 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 144 | newR1L-SU-135 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 145 | newR1L-SU-136 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 152 | newR1L-SU-143 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 154 | newR1L-SU-145 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 156 | newR1L-SU-147 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 158 | newR1L-SU-149 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 162 | newR1L-SU-153 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 163 | newR1L-SU-154 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 164 | newR1L-SU-155 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 165 | newR1L-SU-156 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 166 | newR1L-SU-157 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 167 | newR1L-SU-158 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 168 | newR1L-SU-159 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 169 | newR1L-SU-160 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 170 | newR1L-SU-161 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 171 | newR1L-SU-162 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 172 | newR1L-SU-163 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 173 | newR1L-SU-164 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 174 | newR1L-SU-165 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 175 | newR1L-SU-166 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 176 | newR1L-SU-167 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 177 | newR1L-SU-168 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 178 | newR1L-SU-169 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 179 | newR1L-SU-170 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 180 | newR1L-SU-171 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 181 | newR1L-SU-172 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 182 | newR1L-SU-173 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 183 | newR1L-SU-174 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 184 | newR1L-SU-175 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 186 | newR1L-SU-177 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 187 | newR1L-SU-178 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 188 | newR1L-SU-179 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 189 | newR1L-SU-180 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 191 | newR1L-SU-182 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 192 | newR1L-SU-183 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 193 | newR1L-SU-184 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 194 | newR1L-SU-185 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 195 | newR1L-SU-186 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 198 | newR1L-SU-189 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 200 | newR1L-SU-191 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 201 | newR1L-SU-192 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 202 | newR1L-SU-193 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 203 | newR1L-SU-194 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 204 | newR1L-SU-195 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 205 | newR1L-SU-196 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 206 | newR1L-SU-197 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 207 | newR1L-SU-198 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 208 | newR1L-SU-199 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 209 | newR1L-SU-200 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 211 | newR1L-SU-202 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 212 | newR1L-SU-203 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 213 | newR1L-SU-204 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 214 | newR1L-SU-205 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 215 | newR1L-SU-206 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 216 | newR1L-SU-207 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 217 | newR1L-SU-208 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 218 | newR1L-SU-209 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
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
| 242 | newR1L-SU-233 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 244 | newR1L-SU-235 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 246 | newR1L-SU-237 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 247 | newR1L-SU-238 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 248 | newR1L-SU-239 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 249 | newR1L-SU-240 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 254 | newR1L-SU-245 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 264 | newR1L-SU-255 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 267 | newR1L-SU-258 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 268 | newR1L-SU-259 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 270 | newR1L-SU-261 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 271 | newR1L-SU-262 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 273 | newR1L-SU-264 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 274 | newR1L-SU-265 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 275 | newR1L-SU-266 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 276 | newR1L-SU-267 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 280 | newR1L-SU-271 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 281 | newR1L-SU-272 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 287 | newR1L-SU-278 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 288 | newR1L-SU-279 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 291 | newR1L-SU-282 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 292 | newR1L-SU-283 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 293 | newR1L-SU-284 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 294 | newR1L-SU-285 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 296 | newR1L-SU-287 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 297 | newR1L-SU-288 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 299 | newR1L-SU-290 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 300 | newR1L-SU-291 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
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
| 325 | newR1L-SU-316 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### W — ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）（行計 21／列計 20）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-001 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ed ⏎ 5. Version_after differs from Version_initial; the recorded screen content co |
| 14 | newR1L-SU-005 | er | 比較關係 'differs from'，而 test_item 上半無數值 | wn on the head unit differs from Version_initial ⏎ 4. The head unit displays the u |
| 17 | newR1L-SU-008 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ed ⏎ 5. Version_after differs from Version_initial; the recorded screen content, t |
| 19 | newR1L-SU-010 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ed ⏎ 6. Version_after differs from Version_initial; no user input occurred between |
| 31 | newR1L-SU-022 | er | 比較關係 'equals'，而 test_item 上半無數值 | ions; Version_after equals Version_initial |
| 48 | newR1L-SU-039 | er | 比較關係 'greater than'，而 test_item 上半無數值 | strument cluster is greater than zero ⏎ 2. The "Update Now" selection is made on t |
| 48 | newR1L-SU-039 | er | 比較關係 'greater than'，而 test_item 上半無數值 | strument cluster is greater than zero |
| 50 | newR1L-SU-041 | er | 比較關係 'equals'，而 test_item 上半無數值 | d ⏎ 3. Time_remaining equals the difference between Time_scheduled and Time_now, c |
| 59 | newR1L-SU-050 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 4. Version_after equals the version of the package staged on the OTA Server |
| 63 | newR1L-SU-054 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ed ⏎ 4. Version_after differs from Version_initial while no configured Wi-Fi netwo |
| 69 | newR1L-SU-060 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ad ⏎ 5. Version_after differs from Version_initial after the Wi-Fi attempt period |
| 75 | newR1L-SU-066 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged deployment package h |
| 76 | newR1L-SU-067 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged differential package |
| 78 | newR1L-SU-069 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while one contained update file of th |
| 79 | newR1L-SU-070 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the head unit received an OMA-D |
| 81 | newR1L-SU-072 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged deployment package f |
| 82 | newR1L-SU-073 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while the staged deployment package f |
| 85 | newR1L-SU-076 | er | 比較關係 'equals'，而 test_item 上半無數值 | d and Version_after equals Version_initial |
| 86 | newR1L-SU-077 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 5. Version_after equals Version_initial while one of the two configured condi |
| 90 | newR1L-SU-081 | er | 比較關係 'equals'，而 test_item 上半無數值 | ed ⏎ 4. Version_after equals Version_initial while the space left on the head unit |
| 180 | newR1L-SU-171 | er | 比較關係 'identical to'，而 test_item 上半無數值 | installed image is identical to the reference deployment image |

