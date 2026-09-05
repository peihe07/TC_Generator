# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_VehicleCategory_20260902_working.xlsx

- 來源：`features/vehicle_category/output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_VehicleCategory_20260902_working.xlsx`（唯讀）
- 資料列數：126
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`vehicle_category`（P 採 R-1 v3；另跑 Q／R／T）

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
| H | ER 模糊語 (er) | 1 | 1 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 16 | 16 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 5 | 5 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 14 | 14 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 34 | 34 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 122 | 122 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 4 | 4 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| X | 導航路徑無固定入口（§5.8／R-G71） | 189 | 123 | 每行 | 未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改** |

**總計：行計 385**（列計不加總——同一列可觸發多項檢查）

## 明細

### H — ER 模糊語 (er)（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 33 | NR1L-VC-024 | er | 關係模糊語 'matches' | The recorded layout matches the PDO graphics reference |

### K — CJK 字元（行計 16／列計 16）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 18 | NR1L-VC-009 | pre | 含 CJK 字元 | he mapping table ⏎ 2. 保留散文：The vehicle under test is equipped with the Specialty f |
| 19 | NR1L-VC-010 | pre | 含 CJK 字元 | rows under test ⏎ 2. 保留散文：The vehicle is equipped with the Specialty features lis |
| 20 | NR1L-VC-011 | pre | 含 CJK 字元 | rows under test ⏎ 2. 保留散文：The vehicle is equipped with the Specialty features lis |
| 21 | NR1L-VC-012 | pre | 含 CJK 字元 | rows under test ⏎ 2. 保留散文：The vehicle is equipped with the Specialty features lis |
| 22 | NR1L-VC-013 | pre | 含 CJK 字元 | rows under test ⏎ 2. 保留散文：The vehicle is equipped with the Specialty features lis |
| 27 | NR1L-VC-018 | pre | 含 CJK 字元 | ashboard feature ⏎ 3. 保留散文：The vehicle is equipped with a landscape display ⏎ 4. NO_ |
| 28 | NR1L-VC-019 | pre | 含 CJK 字元 | shboard features ⏎ 3. 保留散文：The vehicle is equipped with a landscape display ⏎ 4. NO_ |
| 29 | NR1L-VC-020 | pre | 含 CJK 字元 | shboard features ⏎ 3. 保留散文：The vehicle is equipped with a landscape display ⏎ 4. NO_ |
| 30 | NR1L-VC-021 | pre | 含 CJK 字元 | shboard features ⏎ 3. 保留散文：The vehicle is equipped with a portrait display ⏎ 4. NO_M |
| 31 | NR1L-VC-022 | pre | 含 CJK 字元 | shboard features ⏎ 3. 保留散文：The vehicle is equipped with a portrait display ⏎ 4. NO_M |
| 32 | NR1L-VC-023 | pre | 含 CJK 字元 | shboard features ⏎ 3. 保留散文：The vehicle is equipped with a portrait display ⏎ 4. NO_M |
| 33 | NR1L-VC-024 | pre | 含 CJK 字元 | tures to display ⏎ 3. 保留散文：The vehicle is equipped with a portrait display |
| 47 | NR1L-VC-038 | pre | 含 CJK 字元 | ttons under test ⏎ 2. 保留散文：The vehicle is equipped with the Controls buttons under |
| 48 | NR1L-VC-039 | pre | 含 CJK 字元 | ttons under test ⏎ 2. 保留散文：The vehicle is equipped with the Controls buttons under |
| 49 | NR1L-VC-040 | pre | 含 CJK 字元 | ttons under test ⏎ 2. 保留散文：The vehicle is equipped with the Controls buttons under |
| 50 | NR1L-VC-041 | pre | 含 CJK 字元 | ttons under test ⏎ 2. 保留散文：The vehicle is equipped with the Controls buttons under |

### L — test_item 上半過長 (>50 tokens)（行計 5／列計 5）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 34 | NR1L-VC-025 | test_item | 上半 55 tokens > 50 | CO2.) Possible items to be placed in the Controls tab include, but are not limit |
| 47 | NR1L-VC-038 | test_item | 上半 61 tokens > 50 | Rear Sunshade \| Activates Feature (button only highlights when pressed ) ⏎  ⏎ Screen |
| 48 | NR1L-VC-039 | test_item | 上半 60 tokens > 50 | Mirror Dimmer \| Off, On (if unavailable – greyed out) ⏎  ⏎ Headrest Fold - 2nd Row \| |
| 49 | NR1L-VC-040 | test_item | 上半 68 tokens > 50 | (Pass Screen Screen Off) \| Pass Screen Screen On/Pass Screen Screen Off Turns Pa |
| 50 | NR1L-VC-041 | test_item | 上半 74 tokens > 50 | Bed Lowering \| Activates Feature (button highlights when feature engaged) ⏎  ⏎ Drive |

### R — Pre-Condition 版面（未編號行／多條件並列）（行計 14／列計 14）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 74 | NR1L-VC-065 | pre | 多條件並列於同一行 | 1. The language-change pop-up is displayed and the system has not completed chan |
| 75 | NR1L-VC-066 | pre | 多條件並列於同一行 | 1. The language-change pop-up is displayed and the system has not completed chan |
| 77 | NR1L-VC-068 | pre | 多條件並列於同一行 | 1. A language change has been made and the system has completed changing the voi |
| 78 | NR1L-VC-069 | pre | 多條件並列於同一行 | 1. A language change has been made and the system has not completed changing the |
| 115 | NR1L-VC-106 | pre | 多條件並列於同一行 | 1. The vehicle is in Key Off and the Settings key-off access pop-up is displayed |
| 116 | NR1L-VC-107 | pre | 多條件並列於同一行 | 1. The vehicle is in Key Off and the Settings key-off access pop-up is displayed |
| 125 | NR1L-VC-116 | pre | 多條件並列於同一行 | 1. The vehicle under test is stationary and the user is part way through the FOT |
| 126 | NR1L-VC-117 | pre | 多條件並列於同一行 | 1. The in-motion popup raised during a FOTA via Wi-Fi flow is displayed, and the |
| 127 | NR1L-VC-118 | pre | 多條件並列於同一行 | 1. The in-motion popup raised during a FOTA via Wi-Fi flow is displayed, and the |
| 128 | NR1L-VC-119 | pre | 多條件並列於同一行 | 1. The vehicle is in Run and the Settings tab is open |
| 129 | NR1L-VC-120 | pre | 多條件並列於同一行 | 1. The vehicle is in Run and a Settings category that is not available in Key Of |
| 131 | NR1L-VC-122 | pre | 多條件並列於同一行 | 1. The Key Off transition pop-up is displayed, and the Settings screen the user  |
| 132 | NR1L-VC-123 | pre | 多條件並列於同一行 | 1. The Key Off transition pop-up is displayed, and the Settings screen the user  |
| 134 | NR1L-VC-125 | pre | 多條件並列於同一行 | 1. The vehicle is in motion and the greyed out line for EPB Service mode is disp |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 34／列計 34）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-VC-001 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 11 | NR1L-VC-002 | pre | PENDING 佔位（DR-49） | 3. PENDING: DR-49 |
| 12 | NR1L-VC-003 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 15 | NR1L-VC-006 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 16 | NR1L-VC-007 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 23 | NR1L-VC-014 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 24 | NR1L-VC-015 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 26 | NR1L-VC-017 | proc | PENDING 佔位（DR-VC9） | 3. Record the order of the content listed under the Dashboard tab and compare it |
| 29 | NR1L-VC-020 | proc | PENDING 佔位（DR-VC9） | 3. Record where the features beyond the first two are placed and compare their l |
| 33 | NR1L-VC-024 | proc | PENDING 佔位（DR-VC9） | 3. Compare the recorded layout against PENDING: DR-VC9 PDO graphics |
| 34 | NR1L-VC-025 | proc | PENDING 佔位（DR-VC9） | 2. Record the items listed in the Controls tab and compare them against PENDING: |
| 38 | NR1L-VC-029 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 39 | NR1L-VC-030 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 40 | NR1L-VC-031 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 42 | NR1L-VC-033 | proc | PENDING 佔位（DR-VC1） | 3. Record the popup that opens and compare its identifier against PENDING: DR-VC |
| 61 | NR1L-VC-052 | proc | PENDING 佔位（DR-VC8） | 3. Enter a wrong 4-digit PIN and dismiss the resulting warning, repeating this u |
| 85 | NR1L-VC-076 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 86 | NR1L-VC-077 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 87 | NR1L-VC-078 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 89 | NR1L-VC-080 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 91 | NR1L-VC-082 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 92 | NR1L-VC-083 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 97 | NR1L-VC-088 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 102 | NR1L-VC-093 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 105 | NR1L-VC-096 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 106 | NR1L-VC-097 | pre | PENDING 佔位（DR-49） | 2. PENDING: DR-49 |
| 121 | NR1L-VC-112 | proc | PENDING 佔位（DR-VC10） | 1. Place the vehicle in Key Off and open Software Updates through PENDING: DR-VC |
| 122 | NR1L-VC-113 | er | PENDING 佔位（DR-VC10） | 3. The setting is not entered and a pop-up is displayed whose text is PENDING: D |
| 123 | NR1L-VC-114 | proc | PENDING 佔位（DR-VC10） | 1. Record the pop-up that is displayed and compare its text against PENDING: DR- |
| 124 | NR1L-VC-115 | proc | PENDING 佔位（DR-VC10） | 1. Record the pop-up that is displayed and compare its text against PENDING: DR- |
| 125 | NR1L-VC-116 | er | PENDING 佔位（DR-VC10） | 3. A pop-up is displayed whose text is PENDING: DR-VC10 PU0091 popup string |
| 126 | NR1L-VC-117 | proc | PENDING 佔位（DR-VC10） | 1. Record the popup that is displayed and compare its text against PENDING: DR-V |
| 127 | NR1L-VC-118 | proc | PENDING 佔位（DR-VC10） | 1. Record the popup that is displayed and compare its text against PENDING: DR-V |
| 134 | NR1L-VC-125 | er | PENDING 佔位（DR-VC10） | 2. The Service mode screen is not entered and a pop-up is displayed whose text i |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 122／列計 122）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-VC-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | NR1L-VC-002 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | NR1L-VC-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | NR1L-VC-004 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | NR1L-VC-005 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | NR1L-VC-006 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | NR1L-VC-007 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | NR1L-VC-008 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | NR1L-VC-009 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | NR1L-VC-010 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | NR1L-VC-011 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | NR1L-VC-012 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | NR1L-VC-013 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | NR1L-VC-014 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | NR1L-VC-015 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | NR1L-VC-016 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | NR1L-VC-017 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 27 | NR1L-VC-018 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 28 | NR1L-VC-019 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 29 | NR1L-VC-020 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 30 | NR1L-VC-021 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 31 | NR1L-VC-022 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 32 | NR1L-VC-023 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 33 | NR1L-VC-024 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 34 | NR1L-VC-025 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 35 | NR1L-VC-026 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 36 | NR1L-VC-027 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 37 | NR1L-VC-028 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 38 | NR1L-VC-029 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 39 | NR1L-VC-030 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 40 | NR1L-VC-031 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 41 | NR1L-VC-032 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 42 | NR1L-VC-033 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 43 | NR1L-VC-034 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 44 | NR1L-VC-035 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 45 | NR1L-VC-036 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 46 | NR1L-VC-037 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 47 | NR1L-VC-038 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 48 | NR1L-VC-039 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 49 | NR1L-VC-040 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 50 | NR1L-VC-041 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 51 | NR1L-VC-042 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 52 | NR1L-VC-043 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 53 | NR1L-VC-044 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 54 | NR1L-VC-045 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 55 | NR1L-VC-046 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 57 | NR1L-VC-048 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 58 | NR1L-VC-049 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 59 | NR1L-VC-050 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 60 | NR1L-VC-051 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 62 | NR1L-VC-053 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 63 | NR1L-VC-054 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 64 | NR1L-VC-055 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 65 | NR1L-VC-056 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 66 | NR1L-VC-057 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 67 | NR1L-VC-058 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 68 | NR1L-VC-059 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 69 | NR1L-VC-060 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 70 | NR1L-VC-061 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 71 | NR1L-VC-062 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 72 | NR1L-VC-063 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 73 | NR1L-VC-064 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 74 | NR1L-VC-065 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 76 | NR1L-VC-067 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 77 | NR1L-VC-068 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 79 | NR1L-VC-070 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 80 | NR1L-VC-071 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 81 | NR1L-VC-072 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 82 | NR1L-VC-073 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 83 | NR1L-VC-074 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 84 | NR1L-VC-075 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 85 | NR1L-VC-076 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 86 | NR1L-VC-077 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 87 | NR1L-VC-078 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 88 | NR1L-VC-079 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 89 | NR1L-VC-080 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 90 | NR1L-VC-081 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 91 | NR1L-VC-082 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 92 | NR1L-VC-083 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 93 | NR1L-VC-084 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 94 | NR1L-VC-085 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 95 | NR1L-VC-086 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 96 | NR1L-VC-087 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 97 | NR1L-VC-088 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 98 | NR1L-VC-089 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 99 | NR1L-VC-090 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 100 | NR1L-VC-091 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 101 | NR1L-VC-092 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 102 | NR1L-VC-093 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 103 | NR1L-VC-094 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 104 | NR1L-VC-095 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 105 | NR1L-VC-096 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 106 | NR1L-VC-097 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 107 | NR1L-VC-098 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 108 | NR1L-VC-099 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 109 | NR1L-VC-100 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 110 | NR1L-VC-101 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 111 | NR1L-VC-102 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 112 | NR1L-VC-103 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 113 | NR1L-VC-104 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 114 | NR1L-VC-105 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 115 | NR1L-VC-106 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 116 | NR1L-VC-107 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 117 | NR1L-VC-108 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 118 | NR1L-VC-109 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 119 | NR1L-VC-110 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 120 | NR1L-VC-111 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 121 | NR1L-VC-112 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 122 | NR1L-VC-113 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 123 | NR1L-VC-114 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 124 | NR1L-VC-115 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 125 | NR1L-VC-116 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 126 | NR1L-VC-117 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 127 | NR1L-VC-118 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 128 | NR1L-VC-119 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 129 | NR1L-VC-120 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 130 | NR1L-VC-121 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 131 | NR1L-VC-122 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 132 | NR1L-VC-123 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 133 | NR1L-VC-124 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 134 | NR1L-VC-125 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 135 | NR1L-VC-126 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### W — ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）（行計 4／列計 4）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 33 | NR1L-VC-024 | er | 比較關係 'matches'，而 test_item 上半無數值 | The recorded layout matches the PDO graphics reference |
| 53 | NR1L-VC-044 | er | 比較關係 'differs from'，而 test_item 上半無數值 | second keypad popup differs from the first in its instruction text only, and its |
| 67 | NR1L-VC-058 | er | 比較關係 'identical to'，而 test_item 上半無數值 | h recorded value is identical to the baseline recorded in step 2 |
| 69 | NR1L-VC-060 | er | 比較關係 'identical to'，而 test_item 上半無數值 | ed personal data is identical to the baseline recorded in step 2 |

### X — 導航路徑無固定入口（§5.8／R-G71）（行計 189／列計 123）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-VC-001 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 10 | NR1L-VC-001 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record the tabs shown along the Vehicle Category tab bar |
| 11 | NR1L-VC-002 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen |
| 11 | NR1L-VC-002 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record which tab is active on entry |
| 12 | NR1L-VC-003 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 12 | NR1L-VC-003 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Leave the Vehicle Category screen |
| 12 | NR1L-VC-003 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Open the Vehicle Category screen again and record which tab is active |
| 13 | NR1L-VC-004 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 13 | NR1L-VC-004 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record the left-to-right order of the tabs along the tab bar |
| 14 | NR1L-VC-005 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 14 | NR1L-VC-005 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record the left-to-right order of every tab along the tab bar |
| 15 | NR1L-VC-006 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 15 | NR1L-VC-006 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Read the label shown on the Controls tab |
| 16 | NR1L-VC-007 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 16 | NR1L-VC-007 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Read the label shown on the Vehicle Settings tab |
| 17 | NR1L-VC-008 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 17 | NR1L-VC-008 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record which Specialty feature tabs are present on the tab bar |
| 18 | NR1L-VC-009 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 18 | NR1L-VC-009 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record every Specialty tab that is present, with its name and its left-to-rig |
| 19 | NR1L-VC-010 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 19 | NR1L-VC-010 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record the tab name and the left-to-right position of each Specialty feature  |
| 20 | NR1L-VC-011 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 20 | NR1L-VC-011 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record the tab name and the left-to-right position of each Specialty feature  |
| 21 | NR1L-VC-012 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 21 | NR1L-VC-012 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record the tab name and the left-to-right position of each Specialty feature  |
| 22 | NR1L-VC-013 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 22 | NR1L-VC-013 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record the tab name and the left-to-right position of each Specialty feature  |
| 23 | NR1L-VC-014 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 23 | NR1L-VC-014 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record whether a Cameras tab is present on the tab bar |
| 24 | NR1L-VC-015 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 25 | NR1L-VC-016 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 25 | NR1L-VC-016 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Select the Dashboard tab |
| 25 | NR1L-VC-016 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Record which apps are listed under the Dashboard tab |
| 26 | NR1L-VC-017 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 26 | NR1L-VC-017 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Select the Dashboard tab |
| 27 | NR1L-VC-018 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 27 | NR1L-VC-018 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Select the Dashboard tab |
| 28 | NR1L-VC-019 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 28 | NR1L-VC-019 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Select the Dashboard tab |
| 29 | NR1L-VC-020 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 29 | NR1L-VC-020 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Select the Dashboard tab |
| 30 | NR1L-VC-021 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 30 | NR1L-VC-021 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Select the Dashboard tab |
| 31 | NR1L-VC-022 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 31 | NR1L-VC-022 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Select the Dashboard tab |
| 32 | NR1L-VC-023 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 32 | NR1L-VC-023 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Select the Dashboard tab |
| 33 | NR1L-VC-024 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 33 | NR1L-VC-024 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Select the Dashboard tab and record the layout as displayed |
| 34 | NR1L-VC-025 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 35 | NR1L-VC-026 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 35 | NR1L-VC-026 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Record the position of the camera entries within the Controls menu |
| 36 | NR1L-VC-027 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 36 | NR1L-VC-027 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Record whether a Settings entry is present in the Controls list |
| 37 | NR1L-VC-028 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 37 | NR1L-VC-028 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the CONTROLS screen and the status bar |
| 38 | NR1L-VC-029 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Record whether a shortcut to settings is present and press it |
| 39 | NR1L-VC-030 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 40 | NR1L-VC-031 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 41 | NR1L-VC-032 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 42 | NR1L-VC-033 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 43 | NR1L-VC-034 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 43 | NR1L-VC-034 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Record the content shown on the head unit and on the lower screen |
| 44 | NR1L-VC-035 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 45 | NR1L-VC-036 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 46 | NR1L-VC-037 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 46 | NR1L-VC-037 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Record every button that is present in the Controls tab |
| 47 | NR1L-VC-038 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 48 | NR1L-VC-039 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 49 | NR1L-VC-040 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 50 | NR1L-VC-041 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 51 | NR1L-VC-042 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 52 | NR1L-VC-043 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 53 | NR1L-VC-044 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 54 | NR1L-VC-045 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 55 | NR1L-VC-046 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 56 | NR1L-VC-047 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 57 | NR1L-VC-048 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 58 | NR1L-VC-049 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 59 | NR1L-VC-050 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 60 | NR1L-VC-051 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 60 | NR1L-VC-051 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Press "OK" in the confirmation popup and record the screen that is displayed |
| 61 | NR1L-VC-052 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 62 | NR1L-VC-053 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 63 | NR1L-VC-054 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 63 | NR1L-VC-054 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Record every item in the Settings list and compare it against the setting nam |
| 64 | NR1L-VC-055 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Open the Phone settings through the Phone screens |
| 65 | NR1L-VC-056 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 66 | NR1L-VC-057 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 67 | NR1L-VC-058 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 68 | NR1L-VC-059 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 69 | NR1L-VC-060 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 70 | NR1L-VC-061 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 70 | NR1L-VC-061 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Open the Suspension settings and record the state of every suspension mode |
| 71 | NR1L-VC-062 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 71 | NR1L-VC-062 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Open the Suspension settings and record the state of every suspension mode |
| 72 | NR1L-VC-063 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 72 | NR1L-VC-063 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Open the language settings and select a language other than the current one |
| 73 | NR1L-VC-064 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 73 | NR1L-VC-064 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Open the language settings and select the target language named in the test d |
| 74 | NR1L-VC-065 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen while the system is still changing the voice commands |
| 74 | NR1L-VC-065 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen again |
| 75 | NR1L-VC-066 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen while the system is still changing the voice commands |
| 75 | NR1L-VC-066 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen again |
| 76 | NR1L-VC-067 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Record the screen that is displayed |
| 77 | NR1L-VC-068 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 1. Open the language settings screen |
| 78 | NR1L-VC-069 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 1. Open the language settings screen |
| 79 | NR1L-VC-070 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 79 | NR1L-VC-070 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Open the language settings and select Chinese |
| 80 | NR1L-VC-071 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 80 | NR1L-VC-071 | proc | 導航標的 'Menu' 而同 TC 無固定入口 | 2. Record the titles shown on the Left Menu Rail and compare them against the ca |
| 81 | NR1L-VC-072 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 81 | NR1L-VC-072 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Record the first level of the Settings and compare it against the categories  |
| 82 | NR1L-VC-073 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 83 | NR1L-VC-074 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 84 | NR1L-VC-075 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 85 | NR1L-VC-076 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 85 | NR1L-VC-076 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Record the order of the settings and compare it against the HMI Settings List |
| 86 | NR1L-VC-077 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 86 | NR1L-VC-077 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Leave the Settings screen idle without making a change and record whether it  |
| 86 | NR1L-VC-077 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Select a setting item and record whether the screen remains displayed |
| 87 | NR1L-VC-078 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 88 | NR1L-VC-079 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 88 | NR1L-VC-079 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen that opens |
| 89 | NR1L-VC-080 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 90 | NR1L-VC-081 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 91 | NR1L-VC-082 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 92 | NR1L-VC-083 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 93 | NR1L-VC-084 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 94 | NR1L-VC-085 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 95 | NR1L-VC-086 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 96 | NR1L-VC-087 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 96 | NR1L-VC-087 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Place a -/+ line in the down button state and touch the screen |
| 97 | NR1L-VC-088 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 97 | NR1L-VC-088 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Select an object in the settings list |
| 98 | NR1L-VC-089 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 99 | NR1L-VC-090 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 99 | NR1L-VC-090 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Repeat for Audio Settings and for Phone/Bluetooth Settings |
| 100 | NR1L-VC-091 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 101 | NR1L-VC-092 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 102 | NR1L-VC-093 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 103 | NR1L-VC-094 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 103 | NR1L-VC-094 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Select a setting whose change is rejected and remain on the Settings screen |
| 104 | NR1L-VC-095 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 104 | NR1L-VC-095 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Select a setting whose change is rejected and leave the Settings screen befor |
| 104 | NR1L-VC-095 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the popup that appears and the screen shown after closing it |
| 105 | NR1L-VC-096 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 106 | NR1L-VC-097 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 107 | NR1L-VC-098 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 108 | NR1L-VC-099 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 109 | NR1L-VC-100 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 110 | NR1L-VC-101 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 111 | NR1L-VC-102 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Settings" tab |
| 111 | NR1L-VC-102 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Choose an option from within the popup and record the screen shown |
| 112 | NR1L-VC-103 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Place the vehicle in Key Off and record whether the Settings tab can be opene |
| 112 | NR1L-VC-103 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Place the vehicle in Timed Mode and record whether the Settings tab can be op |
| 112 | NR1L-VC-103 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Place the vehicle in ACC and record whether the Settings tab can be opened |
| 113 | NR1L-VC-104 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Place the vehicle in Key Off and attempt to access the Settings tab |
| 114 | NR1L-VC-105 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen at the start of the observation period |
| 114 | NR1L-VC-105 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen at the end of the observation period |
| 115 | NR1L-VC-106 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen the attempt to enter the Settings tab was made from |
| 115 | NR1L-VC-106 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen that is displayed |
| 116 | NR1L-VC-107 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen the attempt to enter the Settings tab was made from |
| 116 | NR1L-VC-107 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen that is displayed |
| 117 | NR1L-VC-108 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Open the Phone settings from the Phone screens and record the screen that is  |
| 118 | NR1L-VC-109 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 1. Place the vehicle in Key Off and open the Phone settings through the Phone sc |
| 118 | NR1L-VC-109 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Record the screen that is displayed |
| 118 | NR1L-VC-109 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Repeat step 1 in ACC and record the screen that is displayed |
| 119 | NR1L-VC-110 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Open the Audio settings from the Media and record the screen that is displaye |
| 120 | NR1L-VC-111 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 1. Place the vehicle in Key Off and open the Audio settings through the Media |
| 120 | NR1L-VC-111 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Record the screen that is displayed |
| 120 | NR1L-VC-111 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Repeat step 1 in ACC and record the screen that is displayed |
| 121 | NR1L-VC-112 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Record the screen that is displayed |
| 121 | NR1L-VC-112 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Repeat step 1 in ACC and record the screen that is displayed |
| 123 | NR1L-VC-114 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen that is displayed |
| 124 | NR1L-VC-115 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen that is displayed |
| 125 | NR1L-VC-116 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the step of the FOTA via Wi-Fi flow that is on screen |
| 126 | NR1L-VC-117 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen that is displayed |
| 127 | NR1L-VC-118 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen that is displayed |
| 130 | NR1L-VC-121 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Leave the pop-up untouched for the observation period named in the test data  |
| 130 | NR1L-VC-121 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press the pop-up and each area around it where a close control would normally |
| 131 | NR1L-VC-122 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Record the Settings screen the user was on before the pop-up was triggered |
| 131 | NR1L-VC-122 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen that is displayed |
| 132 | NR1L-VC-123 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Record the Settings screen the user was on before the pop-up was triggered |
| 132 | NR1L-VC-123 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Record the screen that is displayed |
| 133 | NR1L-VC-124 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Vehicle Category screen and select the "Controls" tab |
| 133 | NR1L-VC-124 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Open the Brake Service screen while the vehicle is stationary and record how  |
| 134 | NR1L-VC-125 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Record whether the Service mode screen is entered, and record the pop-up that |
| 135 | NR1L-VC-126 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Display the screen that holds this feature's widget |

