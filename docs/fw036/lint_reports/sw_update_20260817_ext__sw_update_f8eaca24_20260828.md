# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx

- 來源：`features/sw_update/sandbox/pilot01/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（唯讀）
- 資料列數：5
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
| K | CJK 字元 | 3 | 1 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 3 | 1 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 3 | 1 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |

**總計：行計 9**（列計不加總——同一列可觸發多項檢查）

## 明細

### K — CJK 字元（行計 3／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | newR1L-SU-003 | pre | 含 CJK 字元 | ⏎ 3. PENDING: DR-SU1 靜默期間之安全相關通知條件清單 |
| 12 | newR1L-SU-003 | proc | 含 CJK 字元 | ⏎ 3. PENDING: DR-SU1 觸發一項安全相關條件之步驟 ⏎ 4. Check that the safety-related notification |
| 12 | newR1L-SU-003 | er | 含 CJK 字元 | ⏎ 3. PENDING: DR-SU1 安全相關條件之成立狀態 ⏎ 4. The safety-related notification is displayed |

### T — PENDING 說明非英文（行計 3／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | newR1L-SU-003 | pre | PENDING 說明含非 ASCII 字元 ['靜', '默', '期'] | 3. PENDING: DR-SU1 靜默期間之安全相關通知條件清單 |
| 12 | newR1L-SU-003 | proc | PENDING 說明含非 ASCII 字元 ['觸', '發', '一'] | 3. PENDING: DR-SU1 觸發一項安全相關條件之步驟 |
| 12 | newR1L-SU-003 | er | PENDING 說明含非 ASCII 字元 ['安', '全', '相'] | 3. PENDING: DR-SU1 安全相關條件之成立狀態 |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 3／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | newR1L-SU-003 | pre | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 靜默期間之安全相關通知條件清單 |
| 12 | newR1L-SU-003 | proc | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 觸發一項安全相關條件之步驟 |
| 12 | newR1L-SU-003 | er | PENDING 佔位（DR-SU1） | 3. PENDING: DR-SU1 安全相關條件之成立狀態 |

