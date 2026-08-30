# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/batch21/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
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
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 49 | 16 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 16 | 16 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |

**總計：行計 65**（列計不加總——同一列可觸發多項檢查）

## 明細

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 49／列計 16）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-301 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the network the WiFiUpdateService selected |
| 10 | newR1L-SU-301 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the network the WiFiUpdateService selected and t |
| 10 | newR1L-SU-301 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the network the WiFiUpdateService sele |
| 11 | newR1L-SU-302 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the update type the WiFiUpdateService dete |
| 11 | newR1L-SU-302 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the update type the WiFiUpdateService determined |
| 11 | newR1L-SU-302 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the update type the WiFiUpdateService  |
| 12 | newR1L-SU-303 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the update mode the WiFiUpdateService dete |
| 12 | newR1L-SU-303 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the update mode the WiFiUpdateService determined |
| 12 | newR1L-SU-303 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the update mode the WiFiUpdateService  |
| 13 | newR1L-SU-304 | pre | PENDING 佔位（DR-SU2） | 4. PENDING: DR-SU2 means of observing the classification the service applied whe |
| 13 | newR1L-SU-304 | proc | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 step to read the classification the service applied when ./Ex |
| 13 | newR1L-SU-304 | er | PENDING 佔位（DR-SU2） | 2. PENDING: DR-SU2 observable evidence of the classification the service applied |
| 14 | newR1L-SU-305 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the signature and integrity verification t |
| 14 | newR1L-SU-305 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the signature and integrity verification the SWD |
| 14 | newR1L-SU-305 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the signature and integrity verificati |
| 15 | newR1L-SU-306 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the protocol used between the head unit an |
| 15 | newR1L-SU-306 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the protocol used between the head unit and the  |
| 15 | newR1L-SU-306 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the protocol used between the head uni |
| 16 | newR1L-SU-307 | pre | PENDING 佔位（DR-SU6） | 4. PENDING: DR-SU6 means of observing the validation the SWMC applied before pas |
| 16 | newR1L-SU-307 | proc | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 step to read the validation the SWMC applied before passing u |
| 16 | newR1L-SU-307 | er | PENDING 佔位（DR-SU6） | 2. PENDING: DR-SU6 observable evidence of the validation the SWMC applied before |
| 17 | newR1L-SU-308 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the TLS handshake between the head unit an |
| 17 | newR1L-SU-308 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the TLS handshake between the head unit and the  |
| 17 | newR1L-SU-308 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the TLS handshake between the head uni |
| 18 | newR1L-SU-309 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the order of the authentication and the se |
| 18 | newR1L-SU-309 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the order of the authentication and the session  |
| 18 | newR1L-SU-309 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the order of the authentication and th |
| 19 | newR1L-SU-310 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the authentication information the SWMC tr |
| 19 | newR1L-SU-310 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the authentication information the SWMC transmit |
| 19 | newR1L-SU-310 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the authentication information the SWM |
| 20 | newR1L-SU-311 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the vehicle details the WiFiUpdateService  |
| 20 | newR1L-SU-311 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the vehicle details the WiFiUpdateService provid |
| 20 | newR1L-SU-311 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the vehicle details the WiFiUpdateServ |
| 21 | newR1L-SU-312 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the source validation the SWMC performed o |
| 21 | newR1L-SU-312 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the source validation the SWMC performed on rece |
| 21 | newR1L-SU-312 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the source validation the SWMC perform |
| 22 | newR1L-SU-313 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the authorisation check the SWMC performed |
| 22 | newR1L-SU-313 | pre | PENDING 佔位（DR-SU7） | 5. PENDING: DR-SU7 means of presenting an unauthorised OTA Server to the head un |
| 22 | newR1L-SU-313 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the authorisation check the SWMC performed on th |
| 22 | newR1L-SU-313 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the authorisation check the SWMC perfo |
| 23 | newR1L-SU-314 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the communication ports the head unit keep |
| 23 | newR1L-SU-314 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the communication ports the head unit keeps open |
| 23 | newR1L-SU-314 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the communication ports the head unit  |
| 24 | newR1L-SU-315 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the authentication algorithm applied at th |
| 24 | newR1L-SU-315 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the authentication algorithm applied at the appl |
| 24 | newR1L-SU-315 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the authentication algorithm applied a |
| 25 | newR1L-SU-316 | pre | PENDING 佔位（DR-SU7） | 4. PENDING: DR-SU7 means of observing the security mechanisms applied when a pro |
| 25 | newR1L-SU-316 | proc | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 step to read the security mechanisms applied when a proprieta |
| 25 | newR1L-SU-316 | er | PENDING 佔位（DR-SU7） | 2. PENDING: DR-SU7 observable evidence of the security mechanisms applied when a |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 16／列計 16）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-SU-301 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | newR1L-SU-302 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | newR1L-SU-303 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | newR1L-SU-304 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | newR1L-SU-305 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | newR1L-SU-306 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | newR1L-SU-307 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | newR1L-SU-308 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | newR1L-SU-309 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | newR1L-SU-310 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | newR1L-SU-311 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | newR1L-SU-312 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | newR1L-SU-313 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | newR1L-SU-314 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | newR1L-SU-315 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | newR1L-SU-316 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

