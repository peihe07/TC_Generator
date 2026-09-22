# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_ComfortHMI_20260922_v2.xlsx

- 來源：`features/comfort/sandbox/delivery/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_ComfortHMI_20260922_v2.xlsx`（唯讀）
- 資料列數：476
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`comfort`（P 採 R-1 v3；另跑 Q／R／T）

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
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（R-3 = 50，canon §4.3.1 明文；超限依 R-DIAG21 摘句，不豁免） |
| M | 空欄三態 | 10 | 5 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v2 | 0 | 0 | 每次命中 | 已校準（SWC 0708：195 —— proc 11／er 184，見上繳 09） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 1486 | 469 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 0 | 0 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 443 | 443 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| X | 導航路徑無固定入口（§5.8／R-G71） | 337 | 275 | 每行 | 未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改** |
| Y | PROXI 舊式（R-G70 v4.1：`$Param$ is set to` 為 VF230 同義舊式） | 0 | 0 | 每行 | 未校準（R-G70 v4.1，GC-10 新增）—— **WARN 只報不改**；既有交付本不回修（R-TM13），回修依 R-G72 |

**總計：行計 2276**（列計不加總——同一列可觸發多項檢查）

## 明細

### M — 空欄三態（行計 10／列計 5）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 116 | NR1L-ComfortHMI-466 | proc | 空欄（非 NA、非 PENDING:） |  |
| 116 | NR1L-ComfortHMI-466 | er | 空欄（非 NA、非 PENDING:） |  |
| 204 | NR1L-ComfortHMI-194 | proc | 空欄（非 NA、非 PENDING:） |  |
| 204 | NR1L-ComfortHMI-194 | er | 空欄（非 NA、非 PENDING:） |  |
| 269 | NR1L-ComfortHMI-259 | proc | 空欄（非 NA、非 PENDING:） |  |
| 269 | NR1L-ComfortHMI-259 | er | 空欄（非 NA、非 PENDING:） |  |
| 287 | NR1L-ComfortHMI-277 | proc | 空欄（非 NA、非 PENDING:） |  |
| 287 | NR1L-ComfortHMI-277 | er | 空欄（非 NA、非 PENDING:） |  |
| 289 | NR1L-ComfortHMI-279 | proc | 空欄（非 NA、非 PENDING:） |  |
| 289 | NR1L-ComfortHMI-279 | er | 空欄（非 NA、非 PENDING:） |  |

### R — Pre-Condition 版面（未編號行／多條件並列）（行計 1486／列計 469）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-ComfortHMI-001 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 10 | NR1L-ComfortHMI-001 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 11 | NR1L-ComfortHMI-002 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 11 | NR1L-ComfortHMI-002 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 12 | NR1L-ComfortHMI-003 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 12 | NR1L-ComfortHMI-003 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 13 | NR1L-ComfortHMI-004 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 13 | NR1L-ComfortHMI-004 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 14 | NR1L-ComfortHMI-005 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 14 | NR1L-ComfortHMI-005 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 15 | NR1L-ComfortHMI-006 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 15 | NR1L-ComfortHMI-006 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 16 | NR1L-ComfortHMI-007 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 16 | NR1L-ComfortHMI-007 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 17 | NR1L-ComfortHMI-008 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 17 | NR1L-ComfortHMI-008 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 17 | NR1L-ComfortHMI-008 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 18 | NR1L-ComfortHMI-009 | pre | 多條件並列於同一行 | 3. The vehicle is not a single zone climate configuration, for which Sync is not |
| 18 | NR1L-ComfortHMI-009 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 18 | NR1L-ComfortHMI-009 | pre | 多條件並列於同一行 | 5. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 19 | NR1L-ComfortHMI-010 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 19 | NR1L-ComfortHMI-010 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 20 | NR1L-ComfortHMI-011 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 21 | NR1L-ComfortHMI-012 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 21 | NR1L-ComfortHMI-012 | pre | 多條件並列於同一行 | 5. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 22 | NR1L-ComfortHMI-013 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 22 | NR1L-ComfortHMI-013 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 22 | NR1L-ComfortHMI-013 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 23 | NR1L-ComfortHMI-014 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 23 | NR1L-ComfortHMI-014 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 24 | NR1L-ComfortHMI-015 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 24 | NR1L-ComfortHMI-015 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 24 | NR1L-ComfortHMI-015 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 24 | NR1L-ComfortHMI-015 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 25 | NR1L-ComfortHMI-016 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 25 | NR1L-ComfortHMI-016 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 25 | NR1L-ComfortHMI-016 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 25 | NR1L-ComfortHMI-016 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 26 | NR1L-ComfortHMI-017 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 26 | NR1L-ComfortHMI-017 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 26 | NR1L-ComfortHMI-017 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 26 | NR1L-ComfortHMI-017 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 27 | NR1L-ComfortHMI-018 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 27 | NR1L-ComfortHMI-018 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 27 | NR1L-ComfortHMI-018 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 27 | NR1L-ComfortHMI-018 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 28 | NR1L-ComfortHMI-019 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 28 | NR1L-ComfortHMI-019 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 28 | NR1L-ComfortHMI-019 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 28 | NR1L-ComfortHMI-019 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 29 | NR1L-ComfortHMI-020 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 29 | NR1L-ComfortHMI-020 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 29 | NR1L-ComfortHMI-020 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 29 | NR1L-ComfortHMI-020 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 30 | NR1L-ComfortHMI-021 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 30 | NR1L-ComfortHMI-021 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 30 | NR1L-ComfortHMI-021 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 30 | NR1L-ComfortHMI-021 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 31 | NR1L-ComfortHMI-022 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 31 | NR1L-ComfortHMI-022 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 31 | NR1L-ComfortHMI-022 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 31 | NR1L-ComfortHMI-022 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 32 | NR1L-ComfortHMI-023 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 32 | NR1L-ComfortHMI-023 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 32 | NR1L-ComfortHMI-023 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 32 | NR1L-ComfortHMI-023 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 33 | NR1L-ComfortHMI-024 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 33 | NR1L-ComfortHMI-024 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 33 | NR1L-ComfortHMI-024 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 33 | NR1L-ComfortHMI-024 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 34 | NR1L-ComfortHMI-025 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 34 | NR1L-ComfortHMI-025 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 34 | NR1L-ComfortHMI-025 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 35 | NR1L-ComfortHMI-026 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 35 | NR1L-ComfortHMI-026 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 35 | NR1L-ComfortHMI-026 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 36 | NR1L-ComfortHMI-027 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 36 | NR1L-ComfortHMI-027 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 36 | NR1L-ComfortHMI-027 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 37 | NR1L-ComfortHMI-028 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 37 | NR1L-ComfortHMI-028 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 37 | NR1L-ComfortHMI-028 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 37 | NR1L-ComfortHMI-028 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 38 | NR1L-ComfortHMI-029 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 38 | NR1L-ComfortHMI-029 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 38 | NR1L-ComfortHMI-029 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 38 | NR1L-ComfortHMI-029 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 39 | NR1L-ComfortHMI-030 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 39 | NR1L-ComfortHMI-030 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 39 | NR1L-ComfortHMI-030 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 39 | NR1L-ComfortHMI-030 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 40 | NR1L-ComfortHMI-031 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 40 | NR1L-ComfortHMI-031 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 40 | NR1L-ComfortHMI-031 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 40 | NR1L-ComfortHMI-031 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 41 | NR1L-ComfortHMI-032 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 41 | NR1L-ComfortHMI-032 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 41 | NR1L-ComfortHMI-032 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 41 | NR1L-ComfortHMI-032 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 42 | NR1L-ComfortHMI-033 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 42 | NR1L-ComfortHMI-033 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 42 | NR1L-ComfortHMI-033 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 42 | NR1L-ComfortHMI-033 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 43 | NR1L-ComfortHMI-034 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 43 | NR1L-ComfortHMI-034 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 43 | NR1L-ComfortHMI-034 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 43 | NR1L-ComfortHMI-034 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 44 | NR1L-ComfortHMI-035 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 44 | NR1L-ComfortHMI-035 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 44 | NR1L-ComfortHMI-035 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 44 | NR1L-ComfortHMI-035 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 45 | NR1L-ComfortHMI-036 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 45 | NR1L-ComfortHMI-036 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 45 | NR1L-ComfortHMI-036 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 46 | NR1L-ComfortHMI-037 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 46 | NR1L-ComfortHMI-037 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 46 | NR1L-ComfortHMI-037 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 47 | NR1L-ComfortHMI-038 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 47 | NR1L-ComfortHMI-038 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 47 | NR1L-ComfortHMI-038 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 48 | NR1L-ComfortHMI-039 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 48 | NR1L-ComfortHMI-039 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 49 | NR1L-ComfortHMI-040 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 49 | NR1L-ComfortHMI-040 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 50 | NR1L-ComfortHMI-041 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 50 | NR1L-ComfortHMI-041 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 51 | NR1L-ComfortHMI-042 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 51 | NR1L-ComfortHMI-042 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 52 | NR1L-ComfortHMI-043 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 52 | NR1L-ComfortHMI-043 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 53 | NR1L-ComfortHMI-044 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 53 | NR1L-ComfortHMI-044 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 54 | NR1L-ComfortHMI-045 | pre | 多條件並列於同一行 | 1. The vehicle is not a single zone climate configuration, for which Sync is not |
| 54 | NR1L-ComfortHMI-045 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 54 | NR1L-ComfortHMI-045 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 55 | NR1L-ComfortHMI-046 | pre | 多條件並列於同一行 | 1. The vehicle is not a single zone climate configuration, for which Sync is not |
| 55 | NR1L-ComfortHMI-046 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 55 | NR1L-ComfortHMI-046 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 56 | NR1L-ComfortHMI-047 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 56 | NR1L-ComfortHMI-047 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 57 | NR1L-ComfortHMI-048 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 57 | NR1L-ComfortHMI-048 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 58 | NR1L-ComfortHMI-049 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 58 | NR1L-ComfortHMI-049 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 59 | NR1L-ComfortHMI-050 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 59 | NR1L-ComfortHMI-050 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 60 | NR1L-ComfortHMI-051 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 60 | NR1L-ComfortHMI-051 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 61 | NR1L-ComfortHMI-052 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 61 | NR1L-ComfortHMI-052 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 62 | NR1L-ComfortHMI-053 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 62 | NR1L-ComfortHMI-053 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 63 | NR1L-ComfortHMI-054 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 63 | NR1L-ComfortHMI-054 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 63 | NR1L-ComfortHMI-054 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 64 | NR1L-ComfortHMI-055 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 64 | NR1L-ComfortHMI-055 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 65 | NR1L-ComfortHMI-056 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 65 | NR1L-ComfortHMI-056 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 66 | NR1L-ComfortHMI-057 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 66 | NR1L-ComfortHMI-057 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 67 | NR1L-ComfortHMI-058 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 67 | NR1L-ComfortHMI-058 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 68 | NR1L-ComfortHMI-059 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 68 | NR1L-ComfortHMI-059 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 69 | NR1L-ComfortHMI-060 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 69 | NR1L-ComfortHMI-060 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 70 | NR1L-ComfortHMI-061 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 70 | NR1L-ComfortHMI-061 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 71 | NR1L-ComfortHMI-062 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 72 | NR1L-ComfortHMI-063 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 72 | NR1L-ComfortHMI-063 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 72 | NR1L-ComfortHMI-063 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 72 | NR1L-ComfortHMI-063 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 73 | NR1L-ComfortHMI-064 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 73 | NR1L-ComfortHMI-064 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 73 | NR1L-ComfortHMI-064 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 73 | NR1L-ComfortHMI-064 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 74 | NR1L-ComfortHMI-065 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 74 | NR1L-ComfortHMI-065 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 74 | NR1L-ComfortHMI-065 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 74 | NR1L-ComfortHMI-065 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 75 | NR1L-ComfortHMI-066 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 75 | NR1L-ComfortHMI-066 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 75 | NR1L-ComfortHMI-066 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 75 | NR1L-ComfortHMI-066 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 76 | NR1L-ComfortHMI-067 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 76 | NR1L-ComfortHMI-067 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 76 | NR1L-ComfortHMI-067 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 76 | NR1L-ComfortHMI-067 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 77 | NR1L-ComfortHMI-068 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 77 | NR1L-ComfortHMI-068 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 77 | NR1L-ComfortHMI-068 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 77 | NR1L-ComfortHMI-068 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 78 | NR1L-ComfortHMI-069 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 78 | NR1L-ComfortHMI-069 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 78 | NR1L-ComfortHMI-069 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 78 | NR1L-ComfortHMI-069 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 79 | NR1L-ComfortHMI-070 | pre | 多條件並列於同一行 | 1. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 79 | NR1L-ComfortHMI-070 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 79 | NR1L-ComfortHMI-070 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 79 | NR1L-ComfortHMI-070 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 80 | NR1L-ComfortHMI-071 | pre | 多條件並列於同一行 | 1. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 80 | NR1L-ComfortHMI-071 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 80 | NR1L-ComfortHMI-071 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 80 | NR1L-ComfortHMI-071 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 81 | NR1L-ComfortHMI-072 | pre | 多條件並列於同一行 | 1. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 81 | NR1L-ComfortHMI-072 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 81 | NR1L-ComfortHMI-072 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 81 | NR1L-ComfortHMI-072 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 82 | NR1L-ComfortHMI-073 | pre | 多條件並列於同一行 | 1. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 82 | NR1L-ComfortHMI-073 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 82 | NR1L-ComfortHMI-073 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 82 | NR1L-ComfortHMI-073 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 83 | NR1L-ComfortHMI-074 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 83 | NR1L-ComfortHMI-074 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 83 | NR1L-ComfortHMI-074 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 83 | NR1L-ComfortHMI-074 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 84 | NR1L-ComfortHMI-075 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 84 | NR1L-ComfortHMI-075 | pre | 多條件並列於同一行 | 2. The vehicle is equipped with MAX DEF (3.2) and with rear defrost, which is ab |
| 84 | NR1L-ComfortHMI-075 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 84 | NR1L-ComfortHMI-075 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 84 | NR1L-ComfortHMI-075 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 85 | NR1L-ComfortHMI-076 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 85 | NR1L-ComfortHMI-076 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 85 | NR1L-ComfortHMI-076 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 85 | NR1L-ComfortHMI-076 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 86 | NR1L-ComfortHMI-077 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 86 | NR1L-ComfortHMI-077 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 86 | NR1L-ComfortHMI-077 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 86 | NR1L-ComfortHMI-077 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 87 | NR1L-ComfortHMI-078 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 87 | NR1L-ComfortHMI-078 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 87 | NR1L-ComfortHMI-078 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 87 | NR1L-ComfortHMI-078 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 88 | NR1L-ComfortHMI-079 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 88 | NR1L-ComfortHMI-079 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 88 | NR1L-ComfortHMI-079 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 88 | NR1L-ComfortHMI-079 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 89 | NR1L-ComfortHMI-080 | pre | 多條件並列於同一行 | 1. The vehicle is not a single zone climate configuration, for which Sync is not |
| 89 | NR1L-ComfortHMI-080 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 89 | NR1L-ComfortHMI-080 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 89 | NR1L-ComfortHMI-080 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 90 | NR1L-ComfortHMI-081 | pre | 多條件並列於同一行 | 1. The vehicle is not a single zone climate configuration, for which Sync is not |
| 90 | NR1L-ComfortHMI-081 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 90 | NR1L-ComfortHMI-081 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 90 | NR1L-ComfortHMI-081 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 91 | NR1L-ComfortHMI-082 | pre | 多條件並列於同一行 | 1. The vehicle is not a single zone climate configuration, for which Sync is not |
| 91 | NR1L-ComfortHMI-082 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 91 | NR1L-ComfortHMI-082 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 91 | NR1L-ComfortHMI-082 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 92 | NR1L-ComfortHMI-083 | pre | 多條件並列於同一行 | 1. The vehicle is not a single zone climate configuration, for which Sync is not |
| 92 | NR1L-ComfortHMI-083 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 92 | NR1L-ComfortHMI-083 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 92 | NR1L-ComfortHMI-083 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 93 | NR1L-ComfortHMI-084 | pre | 多條件並列於同一行 | 1. The vehicle is not a single zone climate configuration, for which Sync is not |
| 93 | NR1L-ComfortHMI-084 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 93 | NR1L-ComfortHMI-084 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 93 | NR1L-ComfortHMI-084 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 94 | NR1L-ComfortHMI-085 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 94 | NR1L-ComfortHMI-085 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 94 | NR1L-ComfortHMI-085 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 95 | NR1L-ComfortHMI-086 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 95 | NR1L-ComfortHMI-086 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 95 | NR1L-ComfortHMI-086 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 96 | NR1L-ComfortHMI-087 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 96 | NR1L-ComfortHMI-087 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 96 | NR1L-ComfortHMI-087 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 97 | NR1L-ComfortHMI-088 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 97 | NR1L-ComfortHMI-088 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 97 | NR1L-ComfortHMI-088 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 98 | NR1L-ComfortHMI-089 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 98 | NR1L-ComfortHMI-089 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 98 | NR1L-ComfortHMI-089 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 99 | NR1L-ComfortHMI-090 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 99 | NR1L-ComfortHMI-090 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 99 | NR1L-ComfortHMI-090 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 100 | NR1L-ComfortHMI-091 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 100 | NR1L-ComfortHMI-091 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 100 | NR1L-ComfortHMI-091 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 101 | NR1L-ComfortHMI-092 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 101 | NR1L-ComfortHMI-092 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 101 | NR1L-ComfortHMI-092 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 102 | NR1L-ComfortHMI-093 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 102 | NR1L-ComfortHMI-093 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 102 | NR1L-ComfortHMI-093 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 103 | NR1L-ComfortHMI-094 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 103 | NR1L-ComfortHMI-094 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 103 | NR1L-ComfortHMI-094 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 104 | NR1L-ComfortHMI-095 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 104 | NR1L-ComfortHMI-095 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 104 | NR1L-ComfortHMI-095 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 105 | NR1L-ComfortHMI-096 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 105 | NR1L-ComfortHMI-096 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 105 | NR1L-ComfortHMI-096 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 106 | NR1L-ComfortHMI-097 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 106 | NR1L-ComfortHMI-097 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 106 | NR1L-ComfortHMI-097 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 107 | NR1L-ComfortHMI-098 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 107 | NR1L-ComfortHMI-098 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 107 | NR1L-ComfortHMI-098 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 108 | NR1L-ComfortHMI-099 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 108 | NR1L-ComfortHMI-099 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 108 | NR1L-ComfortHMI-099 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 109 | NR1L-ComfortHMI-100 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 109 | NR1L-ComfortHMI-100 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 109 | NR1L-ComfortHMI-100 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 110 | NR1L-ComfortHMI-101 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 110 | NR1L-ComfortHMI-101 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 110 | NR1L-ComfortHMI-101 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 111 | NR1L-ComfortHMI-102 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 111 | NR1L-ComfortHMI-102 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 111 | NR1L-ComfortHMI-102 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 112 | NR1L-ComfortHMI-103 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 112 | NR1L-ComfortHMI-103 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 112 | NR1L-ComfortHMI-103 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 113 | NR1L-ComfortHMI-104 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 113 | NR1L-ComfortHMI-104 | pre | 多條件並列於同一行 | 5. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 113 | NR1L-ComfortHMI-104 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 114 | NR1L-ComfortHMI-105 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 114 | NR1L-ComfortHMI-105 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 114 | NR1L-ComfortHMI-105 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 115 | NR1L-ComfortHMI-106 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 115 | NR1L-ComfortHMI-106 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 115 | NR1L-ComfortHMI-106 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 116 | NR1L-ComfortHMI-466 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 116 | NR1L-ComfortHMI-466 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 116 | NR1L-ComfortHMI-466 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 117 | NR1L-ComfortHMI-107 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 117 | NR1L-ComfortHMI-107 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 118 | NR1L-ComfortHMI-108 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 118 | NR1L-ComfortHMI-108 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 119 | NR1L-ComfortHMI-109 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 120 | NR1L-ComfortHMI-110 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 121 | NR1L-ComfortHMI-111 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 122 | NR1L-ComfortHMI-112 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 122 | NR1L-ComfortHMI-112 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 122 | NR1L-ComfortHMI-112 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 122 | NR1L-ComfortHMI-112 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 123 | NR1L-ComfortHMI-113 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 123 | NR1L-ComfortHMI-113 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 123 | NR1L-ComfortHMI-113 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 123 | NR1L-ComfortHMI-113 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 124 | NR1L-ComfortHMI-114 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 124 | NR1L-ComfortHMI-114 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 125 | NR1L-ComfortHMI-115 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 126 | NR1L-ComfortHMI-116 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 127 | NR1L-ComfortHMI-117 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 128 | NR1L-ComfortHMI-118 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 129 | NR1L-ComfortHMI-119 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 130 | NR1L-ComfortHMI-120 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 131 | NR1L-ComfortHMI-121 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 132 | NR1L-ComfortHMI-122 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 132 | NR1L-ComfortHMI-122 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 133 | NR1L-ComfortHMI-123 | pre | 多條件並列於同一行 | 3. The vehicle is not a single zone climate configuration, for which Sync is not |
| 133 | NR1L-ComfortHMI-123 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 133 | NR1L-ComfortHMI-123 | pre | 多條件並列於同一行 | 5. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 134 | NR1L-ComfortHMI-124 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 134 | NR1L-ComfortHMI-124 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 135 | NR1L-ComfortHMI-125 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 135 | NR1L-ComfortHMI-125 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 136 | NR1L-ComfortHMI-126 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 136 | NR1L-ComfortHMI-126 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 137 | NR1L-ComfortHMI-127 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 137 | NR1L-ComfortHMI-127 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 138 | NR1L-ComfortHMI-128 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 138 | NR1L-ComfortHMI-128 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 139 | NR1L-ComfortHMI-129 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 139 | NR1L-ComfortHMI-129 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 140 | NR1L-ComfortHMI-130 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 140 | NR1L-ComfortHMI-130 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 141 | NR1L-ComfortHMI-131 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 141 | NR1L-ComfortHMI-131 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 142 | NR1L-ComfortHMI-132 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 142 | NR1L-ComfortHMI-132 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 143 | NR1L-ComfortHMI-133 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 143 | NR1L-ComfortHMI-133 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 144 | NR1L-ComfortHMI-134 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 144 | NR1L-ComfortHMI-134 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 145 | NR1L-ComfortHMI-135 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 146 | NR1L-ComfortHMI-136 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 147 | NR1L-ComfortHMI-137 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 147 | NR1L-ComfortHMI-137 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 147 | NR1L-ComfortHMI-137 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 147 | NR1L-ComfortHMI-137 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 148 | NR1L-ComfortHMI-138 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 148 | NR1L-ComfortHMI-138 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 148 | NR1L-ComfortHMI-138 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 148 | NR1L-ComfortHMI-138 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 149 | NR1L-ComfortHMI-139 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 149 | NR1L-ComfortHMI-139 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 149 | NR1L-ComfortHMI-139 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 149 | NR1L-ComfortHMI-139 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 150 | NR1L-ComfortHMI-140 | pre | 多條件並列於同一行 | 1. The front climate screen is open and the climate system is on |
| 150 | NR1L-ComfortHMI-140 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 150 | NR1L-ComfortHMI-140 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 150 | NR1L-ComfortHMI-140 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 151 | NR1L-ComfortHMI-141 | pre | 多條件並列於同一行 | 1. The front climate screen is open and the climate system is on |
| 151 | NR1L-ComfortHMI-141 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 151 | NR1L-ComfortHMI-141 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 151 | NR1L-ComfortHMI-141 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 152 | NR1L-ComfortHMI-142 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 152 | NR1L-ComfortHMI-142 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 152 | NR1L-ComfortHMI-142 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 152 | NR1L-ComfortHMI-142 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 153 | NR1L-ComfortHMI-143 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 153 | NR1L-ComfortHMI-143 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 153 | NR1L-ComfortHMI-143 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 153 | NR1L-ComfortHMI-143 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 154 | NR1L-ComfortHMI-144 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 154 | NR1L-ComfortHMI-144 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 154 | NR1L-ComfortHMI-144 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 154 | NR1L-ComfortHMI-144 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 155 | NR1L-ComfortHMI-145 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 155 | NR1L-ComfortHMI-145 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 155 | NR1L-ComfortHMI-145 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 155 | NR1L-ComfortHMI-145 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 156 | NR1L-ComfortHMI-146 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 156 | NR1L-ComfortHMI-146 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 156 | NR1L-ComfortHMI-146 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 156 | NR1L-ComfortHMI-146 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 157 | NR1L-ComfortHMI-147 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 157 | NR1L-ComfortHMI-147 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 157 | NR1L-ComfortHMI-147 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 157 | NR1L-ComfortHMI-147 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 158 | NR1L-ComfortHMI-148 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 158 | NR1L-ComfortHMI-148 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 158 | NR1L-ComfortHMI-148 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 158 | NR1L-ComfortHMI-148 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 159 | NR1L-ComfortHMI-149 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 159 | NR1L-ComfortHMI-149 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 159 | NR1L-ComfortHMI-149 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 159 | NR1L-ComfortHMI-149 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 160 | NR1L-ComfortHMI-150 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 160 | NR1L-ComfortHMI-150 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 160 | NR1L-ComfortHMI-150 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 160 | NR1L-ComfortHMI-150 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 161 | NR1L-ComfortHMI-151 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 161 | NR1L-ComfortHMI-151 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 161 | NR1L-ComfortHMI-151 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 161 | NR1L-ComfortHMI-151 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 162 | NR1L-ComfortHMI-152 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 162 | NR1L-ComfortHMI-152 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 162 | NR1L-ComfortHMI-152 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 162 | NR1L-ComfortHMI-152 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 163 | NR1L-ComfortHMI-153 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 163 | NR1L-ComfortHMI-153 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 163 | NR1L-ComfortHMI-153 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 163 | NR1L-ComfortHMI-153 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 164 | NR1L-ComfortHMI-154 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 164 | NR1L-ComfortHMI-154 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 164 | NR1L-ComfortHMI-154 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 164 | NR1L-ComfortHMI-154 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 165 | NR1L-ComfortHMI-155 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 165 | NR1L-ComfortHMI-155 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 165 | NR1L-ComfortHMI-155 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 165 | NR1L-ComfortHMI-155 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 166 | NR1L-ComfortHMI-156 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 166 | NR1L-ComfortHMI-156 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 166 | NR1L-ComfortHMI-156 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 166 | NR1L-ComfortHMI-156 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 167 | NR1L-ComfortHMI-157 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 167 | NR1L-ComfortHMI-157 | pre | 多條件並列於同一行 | 2. The vehicle is not a single zone climate configuration, for which Sync is not |
| 167 | NR1L-ComfortHMI-157 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 167 | NR1L-ComfortHMI-157 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 167 | NR1L-ComfortHMI-157 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 168 | NR1L-ComfortHMI-158 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 168 | NR1L-ComfortHMI-158 | pre | 多條件並列於同一行 | 2. The vehicle is not a single zone climate configuration, for which Sync is not |
| 168 | NR1L-ComfortHMI-158 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 168 | NR1L-ComfortHMI-158 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 168 | NR1L-ComfortHMI-158 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 169 | NR1L-ComfortHMI-159 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 169 | NR1L-ComfortHMI-159 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 169 | NR1L-ComfortHMI-159 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 169 | NR1L-ComfortHMI-159 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 170 | NR1L-ComfortHMI-160 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 170 | NR1L-ComfortHMI-160 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 170 | NR1L-ComfortHMI-160 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 170 | NR1L-ComfortHMI-160 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 171 | NR1L-ComfortHMI-161 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 171 | NR1L-ComfortHMI-161 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 171 | NR1L-ComfortHMI-161 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 171 | NR1L-ComfortHMI-161 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 172 | NR1L-ComfortHMI-162 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 172 | NR1L-ComfortHMI-162 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 172 | NR1L-ComfortHMI-162 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 172 | NR1L-ComfortHMI-162 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 173 | NR1L-ComfortHMI-163 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 173 | NR1L-ComfortHMI-163 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 173 | NR1L-ComfortHMI-163 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 173 | NR1L-ComfortHMI-163 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 174 | NR1L-ComfortHMI-164 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 174 | NR1L-ComfortHMI-164 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 174 | NR1L-ComfortHMI-164 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 174 | NR1L-ComfortHMI-164 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 175 | NR1L-ComfortHMI-165 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 175 | NR1L-ComfortHMI-165 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 175 | NR1L-ComfortHMI-165 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 175 | NR1L-ComfortHMI-165 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 176 | NR1L-ComfortHMI-166 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 176 | NR1L-ComfortHMI-166 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 176 | NR1L-ComfortHMI-166 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 176 | NR1L-ComfortHMI-166 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 177 | NR1L-ComfortHMI-167 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 177 | NR1L-ComfortHMI-167 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 177 | NR1L-ComfortHMI-167 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 177 | NR1L-ComfortHMI-167 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 178 | NR1L-ComfortHMI-168 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 178 | NR1L-ComfortHMI-168 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 178 | NR1L-ComfortHMI-168 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 178 | NR1L-ComfortHMI-168 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 179 | NR1L-ComfortHMI-169 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 179 | NR1L-ComfortHMI-169 | pre | 多條件並列於同一行 | 2. The vehicle is not a single zone climate configuration, for which Sync is not |
| 179 | NR1L-ComfortHMI-169 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 179 | NR1L-ComfortHMI-169 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 179 | NR1L-ComfortHMI-169 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 180 | NR1L-ComfortHMI-170 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 180 | NR1L-ComfortHMI-170 | pre | 多條件並列於同一行 | 2. The vehicle is not a single zone climate configuration, for which Sync is not |
| 180 | NR1L-ComfortHMI-170 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 180 | NR1L-ComfortHMI-170 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 180 | NR1L-ComfortHMI-170 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 181 | NR1L-ComfortHMI-171 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 181 | NR1L-ComfortHMI-171 | pre | 多條件並列於同一行 | 2. The vehicle is not a single zone climate configuration, for which Sync is not |
| 181 | NR1L-ComfortHMI-171 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 181 | NR1L-ComfortHMI-171 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 181 | NR1L-ComfortHMI-171 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 182 | NR1L-ComfortHMI-172 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 182 | NR1L-ComfortHMI-172 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 182 | NR1L-ComfortHMI-172 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 182 | NR1L-ComfortHMI-172 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 183 | NR1L-ComfortHMI-173 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 183 | NR1L-ComfortHMI-173 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 183 | NR1L-ComfortHMI-173 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 183 | NR1L-ComfortHMI-173 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 184 | NR1L-ComfortHMI-174 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 184 | NR1L-ComfortHMI-174 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 184 | NR1L-ComfortHMI-174 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 184 | NR1L-ComfortHMI-174 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 185 | NR1L-ComfortHMI-175 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 185 | NR1L-ComfortHMI-175 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 185 | NR1L-ComfortHMI-175 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 185 | NR1L-ComfortHMI-175 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 186 | NR1L-ComfortHMI-176 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 186 | NR1L-ComfortHMI-176 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 186 | NR1L-ComfortHMI-176 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 186 | NR1L-ComfortHMI-176 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 187 | NR1L-ComfortHMI-177 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 187 | NR1L-ComfortHMI-177 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 187 | NR1L-ComfortHMI-177 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 187 | NR1L-ComfortHMI-177 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 188 | NR1L-ComfortHMI-178 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 188 | NR1L-ComfortHMI-178 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 188 | NR1L-ComfortHMI-178 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 188 | NR1L-ComfortHMI-178 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 189 | NR1L-ComfortHMI-179 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 189 | NR1L-ComfortHMI-179 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 189 | NR1L-ComfortHMI-179 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 189 | NR1L-ComfortHMI-179 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 190 | NR1L-ComfortHMI-180 | pre | 多條件並列於同一行 | 1. The rear climate screen is open and the climate system is on |
| 190 | NR1L-ComfortHMI-180 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 190 | NR1L-ComfortHMI-180 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 190 | NR1L-ComfortHMI-180 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 191 | NR1L-ComfortHMI-181 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 191 | NR1L-ComfortHMI-181 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 191 | NR1L-ComfortHMI-181 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 192 | NR1L-ComfortHMI-182 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 192 | NR1L-ComfortHMI-182 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 192 | NR1L-ComfortHMI-182 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 193 | NR1L-ComfortHMI-183 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 193 | NR1L-ComfortHMI-183 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 193 | NR1L-ComfortHMI-183 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 194 | NR1L-ComfortHMI-184 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 194 | NR1L-ComfortHMI-184 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 194 | NR1L-ComfortHMI-184 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 195 | NR1L-ComfortHMI-185 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 195 | NR1L-ComfortHMI-185 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 195 | NR1L-ComfortHMI-185 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 196 | NR1L-ComfortHMI-186 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 196 | NR1L-ComfortHMI-186 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 196 | NR1L-ComfortHMI-186 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 197 | NR1L-ComfortHMI-187 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 197 | NR1L-ComfortHMI-187 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 197 | NR1L-ComfortHMI-187 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 198 | NR1L-ComfortHMI-188 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 198 | NR1L-ComfortHMI-188 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 198 | NR1L-ComfortHMI-188 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 199 | NR1L-ComfortHMI-189 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 199 | NR1L-ComfortHMI-189 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 199 | NR1L-ComfortHMI-189 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 200 | NR1L-ComfortHMI-190 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 200 | NR1L-ComfortHMI-190 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 200 | NR1L-ComfortHMI-190 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 201 | NR1L-ComfortHMI-191 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 201 | NR1L-ComfortHMI-191 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 201 | NR1L-ComfortHMI-191 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 202 | NR1L-ComfortHMI-192 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 202 | NR1L-ComfortHMI-192 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 202 | NR1L-ComfortHMI-192 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 203 | NR1L-ComfortHMI-193 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 203 | NR1L-ComfortHMI-193 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 204 | NR1L-ComfortHMI-194 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 204 | NR1L-ComfortHMI-194 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 205 | NR1L-ComfortHMI-195 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 205 | NR1L-ComfortHMI-195 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 206 | NR1L-ComfortHMI-196 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 206 | NR1L-ComfortHMI-196 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 207 | NR1L-ComfortHMI-197 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 207 | NR1L-ComfortHMI-197 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 208 | NR1L-ComfortHMI-198 | pre | 多條件並列於同一行 | 2. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 208 | NR1L-ComfortHMI-198 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 209 | NR1L-ComfortHMI-199 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 209 | NR1L-ComfortHMI-199 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 210 | NR1L-ComfortHMI-200 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 210 | NR1L-ComfortHMI-200 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 211 | NR1L-ComfortHMI-201 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 211 | NR1L-ComfortHMI-201 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 212 | NR1L-ComfortHMI-202 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 212 | NR1L-ComfortHMI-202 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 213 | NR1L-ComfortHMI-203 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 213 | NR1L-ComfortHMI-203 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 214 | NR1L-ComfortHMI-204 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 214 | NR1L-ComfortHMI-204 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 215 | NR1L-ComfortHMI-205 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 215 | NR1L-ComfortHMI-205 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 215 | NR1L-ComfortHMI-205 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 216 | NR1L-ComfortHMI-206 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 216 | NR1L-ComfortHMI-206 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 217 | NR1L-ComfortHMI-207 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 217 | NR1L-ComfortHMI-207 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 218 | NR1L-ComfortHMI-208 | pre | 多條件並列於同一行 | 1. The vehicle is an EV vehicle, on which ECO HVAC is used |
| 218 | NR1L-ComfortHMI-208 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 219 | NR1L-ComfortHMI-209 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 219 | NR1L-ComfortHMI-209 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 219 | NR1L-ComfortHMI-209 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 219 | NR1L-ComfortHMI-209 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 220 | NR1L-ComfortHMI-210 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 220 | NR1L-ComfortHMI-210 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 220 | NR1L-ComfortHMI-210 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 220 | NR1L-ComfortHMI-210 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 221 | NR1L-ComfortHMI-211 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 221 | NR1L-ComfortHMI-211 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 221 | NR1L-ComfortHMI-211 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 221 | NR1L-ComfortHMI-211 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 222 | NR1L-ComfortHMI-212 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 222 | NR1L-ComfortHMI-212 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 222 | NR1L-ComfortHMI-212 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 222 | NR1L-ComfortHMI-212 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 223 | NR1L-ComfortHMI-213 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 223 | NR1L-ComfortHMI-213 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 223 | NR1L-ComfortHMI-213 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 223 | NR1L-ComfortHMI-213 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 224 | NR1L-ComfortHMI-214 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 224 | NR1L-ComfortHMI-214 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 224 | NR1L-ComfortHMI-214 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 224 | NR1L-ComfortHMI-214 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 225 | NR1L-ComfortHMI-215 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 225 | NR1L-ComfortHMI-215 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 225 | NR1L-ComfortHMI-215 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 225 | NR1L-ComfortHMI-215 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 226 | NR1L-ComfortHMI-216 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 226 | NR1L-ComfortHMI-216 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 226 | NR1L-ComfortHMI-216 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 226 | NR1L-ComfortHMI-216 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 227 | NR1L-ComfortHMI-217 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 227 | NR1L-ComfortHMI-217 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 228 | NR1L-ComfortHMI-218 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 228 | NR1L-ComfortHMI-218 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 228 | NR1L-ComfortHMI-218 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 228 | NR1L-ComfortHMI-218 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 229 | NR1L-ComfortHMI-219 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 229 | NR1L-ComfortHMI-219 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 229 | NR1L-ComfortHMI-219 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 229 | NR1L-ComfortHMI-219 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 230 | NR1L-ComfortHMI-220 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 230 | NR1L-ComfortHMI-220 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 231 | NR1L-ComfortHMI-221 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 231 | NR1L-ComfortHMI-221 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 231 | NR1L-ComfortHMI-221 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 231 | NR1L-ComfortHMI-221 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 232 | NR1L-ComfortHMI-222 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 232 | NR1L-ComfortHMI-222 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 232 | NR1L-ComfortHMI-222 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 232 | NR1L-ComfortHMI-222 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 233 | NR1L-ComfortHMI-223 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 233 | NR1L-ComfortHMI-223 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 233 | NR1L-ComfortHMI-223 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 233 | NR1L-ComfortHMI-223 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 234 | NR1L-ComfortHMI-224 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 234 | NR1L-ComfortHMI-224 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 234 | NR1L-ComfortHMI-224 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 234 | NR1L-ComfortHMI-224 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 235 | NR1L-ComfortHMI-225 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 235 | NR1L-ComfortHMI-225 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 235 | NR1L-ComfortHMI-225 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 235 | NR1L-ComfortHMI-225 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 236 | NR1L-ComfortHMI-226 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 236 | NR1L-ComfortHMI-226 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 236 | NR1L-ComfortHMI-226 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 236 | NR1L-ComfortHMI-226 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 237 | NR1L-ComfortHMI-227 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 237 | NR1L-ComfortHMI-227 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 237 | NR1L-ComfortHMI-227 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 237 | NR1L-ComfortHMI-227 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 238 | NR1L-ComfortHMI-228 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 238 | NR1L-ComfortHMI-228 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 238 | NR1L-ComfortHMI-228 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 238 | NR1L-ComfortHMI-228 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 239 | NR1L-ComfortHMI-229 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 239 | NR1L-ComfortHMI-229 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 239 | NR1L-ComfortHMI-229 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 239 | NR1L-ComfortHMI-229 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 240 | NR1L-ComfortHMI-230 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 240 | NR1L-ComfortHMI-230 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 240 | NR1L-ComfortHMI-230 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 240 | NR1L-ComfortHMI-230 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 241 | NR1L-ComfortHMI-231 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 241 | NR1L-ComfortHMI-231 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 241 | NR1L-ComfortHMI-231 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 241 | NR1L-ComfortHMI-231 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 242 | NR1L-ComfortHMI-232 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 242 | NR1L-ComfortHMI-232 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 242 | NR1L-ComfortHMI-232 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 242 | NR1L-ComfortHMI-232 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 243 | NR1L-ComfortHMI-233 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 243 | NR1L-ComfortHMI-233 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 243 | NR1L-ComfortHMI-233 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 243 | NR1L-ComfortHMI-233 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 244 | NR1L-ComfortHMI-234 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 244 | NR1L-ComfortHMI-234 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 244 | NR1L-ComfortHMI-234 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 244 | NR1L-ComfortHMI-234 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 245 | NR1L-ComfortHMI-235 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 245 | NR1L-ComfortHMI-235 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 245 | NR1L-ComfortHMI-235 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 245 | NR1L-ComfortHMI-235 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 246 | NR1L-ComfortHMI-236 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 246 | NR1L-ComfortHMI-236 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 246 | NR1L-ComfortHMI-236 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 246 | NR1L-ComfortHMI-236 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 247 | NR1L-ComfortHMI-237 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 247 | NR1L-ComfortHMI-237 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 247 | NR1L-ComfortHMI-237 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 247 | NR1L-ComfortHMI-237 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 248 | NR1L-ComfortHMI-238 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 248 | NR1L-ComfortHMI-238 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 248 | NR1L-ComfortHMI-238 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 248 | NR1L-ComfortHMI-238 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 249 | NR1L-ComfortHMI-239 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 249 | NR1L-ComfortHMI-239 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 249 | NR1L-ComfortHMI-239 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 249 | NR1L-ComfortHMI-239 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 250 | NR1L-ComfortHMI-240 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 250 | NR1L-ComfortHMI-240 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 250 | NR1L-ComfortHMI-240 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 250 | NR1L-ComfortHMI-240 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 251 | NR1L-ComfortHMI-241 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 251 | NR1L-ComfortHMI-241 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 251 | NR1L-ComfortHMI-241 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 251 | NR1L-ComfortHMI-241 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 252 | NR1L-ComfortHMI-242 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 252 | NR1L-ComfortHMI-242 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 252 | NR1L-ComfortHMI-242 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 252 | NR1L-ComfortHMI-242 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 253 | NR1L-ComfortHMI-243 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 253 | NR1L-ComfortHMI-243 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 254 | NR1L-ComfortHMI-244 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 254 | NR1L-ComfortHMI-244 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 255 | NR1L-ComfortHMI-245 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 255 | NR1L-ComfortHMI-245 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 256 | NR1L-ComfortHMI-246 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 256 | NR1L-ComfortHMI-246 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 256 | NR1L-ComfortHMI-246 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 256 | NR1L-ComfortHMI-246 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 257 | NR1L-ComfortHMI-247 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 257 | NR1L-ComfortHMI-247 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 257 | NR1L-ComfortHMI-247 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 257 | NR1L-ComfortHMI-247 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 258 | NR1L-ComfortHMI-248 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 258 | NR1L-ComfortHMI-248 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 258 | NR1L-ComfortHMI-248 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 258 | NR1L-ComfortHMI-248 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 259 | NR1L-ComfortHMI-249 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 259 | NR1L-ComfortHMI-249 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 259 | NR1L-ComfortHMI-249 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 259 | NR1L-ComfortHMI-249 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 260 | NR1L-ComfortHMI-250 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 260 | NR1L-ComfortHMI-250 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 260 | NR1L-ComfortHMI-250 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 260 | NR1L-ComfortHMI-250 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 261 | NR1L-ComfortHMI-251 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 261 | NR1L-ComfortHMI-251 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 261 | NR1L-ComfortHMI-251 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 261 | NR1L-ComfortHMI-251 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 262 | NR1L-ComfortHMI-252 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 262 | NR1L-ComfortHMI-252 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 262 | NR1L-ComfortHMI-252 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 262 | NR1L-ComfortHMI-252 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 263 | NR1L-ComfortHMI-253 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 263 | NR1L-ComfortHMI-253 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 263 | NR1L-ComfortHMI-253 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 263 | NR1L-ComfortHMI-253 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 264 | NR1L-ComfortHMI-254 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 264 | NR1L-ComfortHMI-254 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 264 | NR1L-ComfortHMI-254 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 264 | NR1L-ComfortHMI-254 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 265 | NR1L-ComfortHMI-255 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 265 | NR1L-ComfortHMI-255 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 265 | NR1L-ComfortHMI-255 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 265 | NR1L-ComfortHMI-255 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 266 | NR1L-ComfortHMI-256 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 266 | NR1L-ComfortHMI-256 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 267 | NR1L-ComfortHMI-257 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 267 | NR1L-ComfortHMI-257 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 267 | NR1L-ComfortHMI-257 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 267 | NR1L-ComfortHMI-257 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 268 | NR1L-ComfortHMI-258 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 268 | NR1L-ComfortHMI-258 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 268 | NR1L-ComfortHMI-258 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 268 | NR1L-ComfortHMI-258 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 269 | NR1L-ComfortHMI-259 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 269 | NR1L-ComfortHMI-259 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 270 | NR1L-ComfortHMI-260 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 270 | NR1L-ComfortHMI-260 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 270 | NR1L-ComfortHMI-260 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 270 | NR1L-ComfortHMI-260 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 271 | NR1L-ComfortHMI-261 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 271 | NR1L-ComfortHMI-261 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 271 | NR1L-ComfortHMI-261 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 271 | NR1L-ComfortHMI-261 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 272 | NR1L-ComfortHMI-262 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 272 | NR1L-ComfortHMI-262 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 272 | NR1L-ComfortHMI-262 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 272 | NR1L-ComfortHMI-262 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 273 | NR1L-ComfortHMI-263 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 273 | NR1L-ComfortHMI-263 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 273 | NR1L-ComfortHMI-263 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 273 | NR1L-ComfortHMI-263 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 274 | NR1L-ComfortHMI-264 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 274 | NR1L-ComfortHMI-264 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 274 | NR1L-ComfortHMI-264 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 274 | NR1L-ComfortHMI-264 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 275 | NR1L-ComfortHMI-265 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 275 | NR1L-ComfortHMI-265 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 275 | NR1L-ComfortHMI-265 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 275 | NR1L-ComfortHMI-265 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 276 | NR1L-ComfortHMI-266 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 276 | NR1L-ComfortHMI-266 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 276 | NR1L-ComfortHMI-266 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 276 | NR1L-ComfortHMI-266 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 277 | NR1L-ComfortHMI-267 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 277 | NR1L-ComfortHMI-267 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 277 | NR1L-ComfortHMI-267 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 277 | NR1L-ComfortHMI-267 | pre | 多條件並列於同一行 | 5. The vehicle is not a front-climate-only vehicle, for which the comfort tabs a |
| 280 | NR1L-ComfortHMI-270 | pre | 多條件並列於同一行 | 5. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 280 | NR1L-ComfortHMI-270 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 282 | NR1L-ComfortHMI-272 | pre | 多條件並列於同一行 | 3. The Seats tab is not currently shown, and the lumbar/bolster level is away fr |
| 286 | NR1L-ComfortHMI-276 | pre | 多條件並列於同一行 | 3. The Seats tab is open and the lumbar/bolster level is away from both its mini |
| 287 | NR1L-ComfortHMI-277 | pre | 多條件並列於同一行 | 2. The Seats tab is open and the lumbar/bolster level is away from both its mini |
| 288 | NR1L-ComfortHMI-278 | pre | 多條件並列於同一行 | 3. The popup or tab change has already been triggered, so the next press is appl |
| 289 | NR1L-ComfortHMI-279 | pre | 多條件並列於同一行 | 2. The Seats tab is open and the lumbar/bolster level is away from both its mini |
| 290 | NR1L-ComfortHMI-280 | pre | 多條件並列於同一行 | 3. The Seats tab is open and the lumbar/bolster level is away from both its mini |
| 292 | NR1L-ComfortHMI-282 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 292 | NR1L-ComfortHMI-282 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 292 | NR1L-ComfortHMI-282 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 292 | NR1L-ComfortHMI-282 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 293 | NR1L-ComfortHMI-283 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 293 | NR1L-ComfortHMI-283 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 293 | NR1L-ComfortHMI-283 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 293 | NR1L-ComfortHMI-283 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 294 | NR1L-ComfortHMI-284 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 294 | NR1L-ComfortHMI-284 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 294 | NR1L-ComfortHMI-284 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 294 | NR1L-ComfortHMI-284 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 295 | NR1L-ComfortHMI-285 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 295 | NR1L-ComfortHMI-285 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 295 | NR1L-ComfortHMI-285 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 295 | NR1L-ComfortHMI-285 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 296 | NR1L-ComfortHMI-286 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 296 | NR1L-ComfortHMI-286 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 296 | NR1L-ComfortHMI-286 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 296 | NR1L-ComfortHMI-286 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 297 | NR1L-ComfortHMI-287 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 297 | NR1L-ComfortHMI-287 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 297 | NR1L-ComfortHMI-287 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 297 | NR1L-ComfortHMI-287 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 298 | NR1L-ComfortHMI-288 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 298 | NR1L-ComfortHMI-288 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 298 | NR1L-ComfortHMI-288 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 298 | NR1L-ComfortHMI-288 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 299 | NR1L-ComfortHMI-289 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 299 | NR1L-ComfortHMI-289 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 299 | NR1L-ComfortHMI-289 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 299 | NR1L-ComfortHMI-289 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 300 | NR1L-ComfortHMI-290 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 300 | NR1L-ComfortHMI-290 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 300 | NR1L-ComfortHMI-290 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 300 | NR1L-ComfortHMI-290 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 301 | NR1L-ComfortHMI-291 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 301 | NR1L-ComfortHMI-291 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 301 | NR1L-ComfortHMI-291 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 301 | NR1L-ComfortHMI-291 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 302 | NR1L-ComfortHMI-292 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 302 | NR1L-ComfortHMI-292 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 302 | NR1L-ComfortHMI-292 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 302 | NR1L-ComfortHMI-292 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 303 | NR1L-ComfortHMI-293 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 303 | NR1L-ComfortHMI-293 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 303 | NR1L-ComfortHMI-293 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 303 | NR1L-ComfortHMI-293 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 304 | NR1L-ComfortHMI-294 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 304 | NR1L-ComfortHMI-294 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 304 | NR1L-ComfortHMI-294 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 304 | NR1L-ComfortHMI-294 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 305 | NR1L-ComfortHMI-295 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 305 | NR1L-ComfortHMI-295 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 305 | NR1L-ComfortHMI-295 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 305 | NR1L-ComfortHMI-295 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 306 | NR1L-ComfortHMI-296 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 306 | NR1L-ComfortHMI-296 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 306 | NR1L-ComfortHMI-296 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 306 | NR1L-ComfortHMI-296 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 307 | NR1L-ComfortHMI-297 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 307 | NR1L-ComfortHMI-297 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 307 | NR1L-ComfortHMI-297 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 307 | NR1L-ComfortHMI-297 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 308 | NR1L-ComfortHMI-298 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 308 | NR1L-ComfortHMI-298 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 308 | NR1L-ComfortHMI-298 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 308 | NR1L-ComfortHMI-298 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 309 | NR1L-ComfortHMI-299 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 309 | NR1L-ComfortHMI-299 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 309 | NR1L-ComfortHMI-299 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 310 | NR1L-ComfortHMI-300 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 310 | NR1L-ComfortHMI-300 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 310 | NR1L-ComfortHMI-300 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 311 | NR1L-ComfortHMI-301 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 311 | NR1L-ComfortHMI-301 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 311 | NR1L-ComfortHMI-301 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 312 | NR1L-ComfortHMI-302 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 312 | NR1L-ComfortHMI-302 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 312 | NR1L-ComfortHMI-302 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 313 | NR1L-ComfortHMI-303 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 313 | NR1L-ComfortHMI-303 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 313 | NR1L-ComfortHMI-303 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 314 | NR1L-ComfortHMI-304 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 314 | NR1L-ComfortHMI-304 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 314 | NR1L-ComfortHMI-304 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 315 | NR1L-ComfortHMI-305 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 315 | NR1L-ComfortHMI-305 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 315 | NR1L-ComfortHMI-305 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 316 | NR1L-ComfortHMI-306 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 316 | NR1L-ComfortHMI-306 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 316 | NR1L-ComfortHMI-306 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 317 | NR1L-ComfortHMI-307 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 317 | NR1L-ComfortHMI-307 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 317 | NR1L-ComfortHMI-307 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 318 | NR1L-ComfortHMI-308 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 318 | NR1L-ComfortHMI-308 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 318 | NR1L-ComfortHMI-308 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 319 | NR1L-ComfortHMI-309 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 319 | NR1L-ComfortHMI-309 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 319 | NR1L-ComfortHMI-309 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 320 | NR1L-ComfortHMI-310 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 320 | NR1L-ComfortHMI-310 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 320 | NR1L-ComfortHMI-310 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 321 | NR1L-ComfortHMI-311 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 321 | NR1L-ComfortHMI-311 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 321 | NR1L-ComfortHMI-311 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 322 | NR1L-ComfortHMI-312 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 322 | NR1L-ComfortHMI-312 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 322 | NR1L-ComfortHMI-312 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 323 | NR1L-ComfortHMI-313 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 323 | NR1L-ComfortHMI-313 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 323 | NR1L-ComfortHMI-313 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 324 | NR1L-ComfortHMI-314 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 324 | NR1L-ComfortHMI-314 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 324 | NR1L-ComfortHMI-314 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 325 | NR1L-ComfortHMI-315 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 325 | NR1L-ComfortHMI-315 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 325 | NR1L-ComfortHMI-315 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 326 | NR1L-ComfortHMI-316 | pre | 多條件並列於同一行 | 2. The vehicle is an R1Low vehicle, for which the FAN Speed Pop-up is shown |
| 326 | NR1L-ComfortHMI-316 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 326 | NR1L-ComfortHMI-316 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 326 | NR1L-ComfortHMI-316 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 327 | NR1L-ComfortHMI-317 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 327 | NR1L-ComfortHMI-317 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 327 | NR1L-ComfortHMI-317 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 328 | NR1L-ComfortHMI-318 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 328 | NR1L-ComfortHMI-318 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 328 | NR1L-ComfortHMI-318 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 329 | NR1L-ComfortHMI-319 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 329 | NR1L-ComfortHMI-319 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 329 | NR1L-ComfortHMI-319 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 330 | NR1L-ComfortHMI-320 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 330 | NR1L-ComfortHMI-320 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 330 | NR1L-ComfortHMI-320 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 331 | NR1L-ComfortHMI-321 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 331 | NR1L-ComfortHMI-321 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 331 | NR1L-ComfortHMI-321 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 332 | NR1L-ComfortHMI-322 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 332 | NR1L-ComfortHMI-322 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 332 | NR1L-ComfortHMI-322 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 333 | NR1L-ComfortHMI-323 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 333 | NR1L-ComfortHMI-323 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 333 | NR1L-ComfortHMI-323 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 333 | NR1L-ComfortHMI-323 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 334 | NR1L-ComfortHMI-324 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 334 | NR1L-ComfortHMI-324 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 334 | NR1L-ComfortHMI-324 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 334 | NR1L-ComfortHMI-324 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 335 | NR1L-ComfortHMI-325 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 335 | NR1L-ComfortHMI-325 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 335 | NR1L-ComfortHMI-325 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 335 | NR1L-ComfortHMI-325 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 336 | NR1L-ComfortHMI-326 | pre | 多條件並列於同一行 | 1. The head unit is on and the climate system is on |
| 336 | NR1L-ComfortHMI-326 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 336 | NR1L-ComfortHMI-326 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 336 | NR1L-ComfortHMI-326 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 337 | NR1L-ComfortHMI-327 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 337 | NR1L-ComfortHMI-327 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 337 | NR1L-ComfortHMI-327 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 338 | NR1L-ComfortHMI-328 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 338 | NR1L-ComfortHMI-328 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 338 | NR1L-ComfortHMI-328 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 339 | NR1L-ComfortHMI-329 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 339 | NR1L-ComfortHMI-329 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 340 | NR1L-ComfortHMI-330 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 340 | NR1L-ComfortHMI-330 | pre | 多條件並列於同一行 | 2. The vehicle is not a single zone climate configuration, for which Sync is not |
| 340 | NR1L-ComfortHMI-330 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 341 | NR1L-ComfortHMI-331 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 341 | NR1L-ComfortHMI-331 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 342 | NR1L-ComfortHMI-332 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 342 | NR1L-ComfortHMI-332 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 343 | NR1L-ComfortHMI-333 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 343 | NR1L-ComfortHMI-333 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 344 | NR1L-ComfortHMI-334 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 344 | NR1L-ComfortHMI-334 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 344 | NR1L-ComfortHMI-334 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 345 | NR1L-ComfortHMI-335 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 345 | NR1L-ComfortHMI-335 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 346 | NR1L-ComfortHMI-336 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 346 | NR1L-ComfortHMI-336 | pre | 多條件並列於同一行 | 2. The vehicle has an ATC climate system, in which AUTO is shown |
| 346 | NR1L-ComfortHMI-336 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 346 | NR1L-ComfortHMI-336 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 347 | NR1L-ComfortHMI-337 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 347 | NR1L-ComfortHMI-337 | pre | 多條件並列於同一行 | 2. The vehicle has an ATC climate system, in which AUTO is shown |
| 347 | NR1L-ComfortHMI-337 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 347 | NR1L-ComfortHMI-337 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 348 | NR1L-ComfortHMI-338 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 348 | NR1L-ComfortHMI-338 | pre | 多條件並列於同一行 | 2. The vehicle has an ATC climate system, in which AUTO is shown |
| 348 | NR1L-ComfortHMI-338 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 348 | NR1L-ComfortHMI-338 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 349 | NR1L-ComfortHMI-339 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 349 | NR1L-ComfortHMI-339 | pre | 多條件並列於同一行 | 2. The vehicle has an ATC climate system, in which AUTO is shown |
| 349 | NR1L-ComfortHMI-339 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 349 | NR1L-ComfortHMI-339 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 350 | NR1L-ComfortHMI-340 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 350 | NR1L-ComfortHMI-340 | pre | 多條件並列於同一行 | 2. The vehicle has an ATC climate system, in which AUTO is shown |
| 350 | NR1L-ComfortHMI-340 | pre | 多條件並列於同一行 | 5. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 350 | NR1L-ComfortHMI-340 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 351 | NR1L-ComfortHMI-341 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 351 | NR1L-ComfortHMI-341 | pre | 多條件並列於同一行 | 2. The vehicle has an ATC climate system, in which AUTO is shown |
| 351 | NR1L-ComfortHMI-341 | pre | 多條件並列於同一行 | 5. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 351 | NR1L-ComfortHMI-341 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 352 | NR1L-ComfortHMI-342 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 352 | NR1L-ComfortHMI-342 | pre | 多條件並列於同一行 | 2. The vehicle has an ATC climate system, in which AUTO is shown |
| 352 | NR1L-ComfortHMI-342 | pre | 多條件並列於同一行 | 5. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 352 | NR1L-ComfortHMI-342 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 353 | NR1L-ComfortHMI-343 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 353 | NR1L-ComfortHMI-343 | pre | 多條件並列於同一行 | 2. The vehicle has an ATC climate system, in which AUTO is shown |
| 353 | NR1L-ComfortHMI-343 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 353 | NR1L-ComfortHMI-343 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 354 | NR1L-ComfortHMI-344 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 354 | NR1L-ComfortHMI-344 | pre | 多條件並列於同一行 | 2. The vehicle has an ATC climate system, in which AUTO is shown |
| 354 | NR1L-ComfortHMI-344 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 354 | NR1L-ComfortHMI-344 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 355 | NR1L-ComfortHMI-345 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 355 | NR1L-ComfortHMI-345 | pre | 多條件並列於同一行 | 2. The vehicle has an ATC climate system, in which AUTO is shown |
| 355 | NR1L-ComfortHMI-345 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 355 | NR1L-ComfortHMI-345 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 356 | NR1L-ComfortHMI-346 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 356 | NR1L-ComfortHMI-346 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 356 | NR1L-ComfortHMI-346 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 357 | NR1L-ComfortHMI-347 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 357 | NR1L-ComfortHMI-347 | pre | 多條件並列於同一行 | 4. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 357 | NR1L-ComfortHMI-347 | pre | 多條件並列於同一行 | 5. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 357 | NR1L-ComfortHMI-347 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 358 | NR1L-ComfortHMI-348 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 358 | NR1L-ComfortHMI-348 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 358 | NR1L-ComfortHMI-348 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 359 | NR1L-ComfortHMI-349 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 359 | NR1L-ComfortHMI-349 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 359 | NR1L-ComfortHMI-349 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 360 | NR1L-ComfortHMI-350 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 360 | NR1L-ComfortHMI-350 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 360 | NR1L-ComfortHMI-350 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 361 | NR1L-ComfortHMI-351 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 361 | NR1L-ComfortHMI-351 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 361 | NR1L-ComfortHMI-351 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 362 | NR1L-ComfortHMI-352 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 362 | NR1L-ComfortHMI-352 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 362 | NR1L-ComfortHMI-352 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 363 | NR1L-ComfortHMI-353 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 363 | NR1L-ComfortHMI-353 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 363 | NR1L-ComfortHMI-353 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 364 | NR1L-ComfortHMI-354 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 364 | NR1L-ComfortHMI-354 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 365 | NR1L-ComfortHMI-355 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 365 | NR1L-ComfortHMI-355 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 365 | NR1L-ComfortHMI-355 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 366 | NR1L-ComfortHMI-356 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 366 | NR1L-ComfortHMI-356 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 366 | NR1L-ComfortHMI-356 | pre | 多條件並列於同一行 | 3. The vehicle is not a single zone climate configuration, for which Sync is not |
| 367 | NR1L-ComfortHMI-357 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 367 | NR1L-ComfortHMI-357 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 367 | NR1L-ComfortHMI-357 | pre | 多條件並列於同一行 | 3. The vehicle is not a single zone climate configuration, for which Sync is not |
| 367 | NR1L-ComfortHMI-357 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 368 | NR1L-ComfortHMI-358 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 368 | NR1L-ComfortHMI-358 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 368 | NR1L-ComfortHMI-358 | pre | 多條件並列於同一行 | 3. The vehicle is not a single zone climate configuration, for which Sync is not |
| 368 | NR1L-ComfortHMI-358 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 369 | NR1L-ComfortHMI-359 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 369 | NR1L-ComfortHMI-359 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 369 | NR1L-ComfortHMI-359 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 370 | NR1L-ComfortHMI-360 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 370 | NR1L-ComfortHMI-360 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 370 | NR1L-ComfortHMI-360 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 371 | NR1L-ComfortHMI-361 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 371 | NR1L-ComfortHMI-361 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 371 | NR1L-ComfortHMI-361 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 372 | NR1L-ComfortHMI-362 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 372 | NR1L-ComfortHMI-362 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 372 | NR1L-ComfortHMI-362 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 373 | NR1L-ComfortHMI-363 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 373 | NR1L-ComfortHMI-363 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 373 | NR1L-ComfortHMI-363 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 374 | NR1L-ComfortHMI-364 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 374 | NR1L-ComfortHMI-364 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 374 | NR1L-ComfortHMI-364 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 375 | NR1L-ComfortHMI-365 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 375 | NR1L-ComfortHMI-365 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 375 | NR1L-ComfortHMI-365 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 376 | NR1L-ComfortHMI-366 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 376 | NR1L-ComfortHMI-366 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 376 | NR1L-ComfortHMI-366 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 377 | NR1L-ComfortHMI-367 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 377 | NR1L-ComfortHMI-367 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 378 | NR1L-ComfortHMI-368 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 378 | NR1L-ComfortHMI-368 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 378 | NR1L-ComfortHMI-368 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 379 | NR1L-ComfortHMI-369 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 379 | NR1L-ComfortHMI-369 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 379 | NR1L-ComfortHMI-369 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 380 | NR1L-ComfortHMI-370 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 380 | NR1L-ComfortHMI-370 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 380 | NR1L-ComfortHMI-370 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 381 | NR1L-ComfortHMI-371 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 381 | NR1L-ComfortHMI-371 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 381 | NR1L-ComfortHMI-371 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 382 | NR1L-ComfortHMI-372 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 382 | NR1L-ComfortHMI-372 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 382 | NR1L-ComfortHMI-372 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 383 | NR1L-ComfortHMI-373 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 383 | NR1L-ComfortHMI-373 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 383 | NR1L-ComfortHMI-373 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 384 | NR1L-ComfortHMI-374 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 384 | NR1L-ComfortHMI-374 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 384 | NR1L-ComfortHMI-374 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 385 | NR1L-ComfortHMI-375 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 385 | NR1L-ComfortHMI-375 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 385 | NR1L-ComfortHMI-375 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 386 | NR1L-ComfortHMI-376 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 386 | NR1L-ComfortHMI-376 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 386 | NR1L-ComfortHMI-376 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 387 | NR1L-ComfortHMI-377 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 387 | NR1L-ComfortHMI-377 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 387 | NR1L-ComfortHMI-377 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 388 | NR1L-ComfortHMI-378 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 388 | NR1L-ComfortHMI-378 | pre | 多條件並列於同一行 | 3. The vehicle is not a single zone climate configuration, for which Sync is not |
| 388 | NR1L-ComfortHMI-378 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 388 | NR1L-ComfortHMI-378 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 389 | NR1L-ComfortHMI-379 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 389 | NR1L-ComfortHMI-379 | pre | 多條件並列於同一行 | 3. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 389 | NR1L-ComfortHMI-379 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 389 | NR1L-ComfortHMI-379 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 390 | NR1L-ComfortHMI-380 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 390 | NR1L-ComfortHMI-380 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 390 | NR1L-ComfortHMI-380 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 391 | NR1L-ComfortHMI-381 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 391 | NR1L-ComfortHMI-381 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 391 | NR1L-ComfortHMI-381 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 392 | NR1L-ComfortHMI-382 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 392 | NR1L-ComfortHMI-382 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 392 | NR1L-ComfortHMI-382 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 393 | NR1L-ComfortHMI-383 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 393 | NR1L-ComfortHMI-383 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 393 | NR1L-ComfortHMI-383 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 394 | NR1L-ComfortHMI-384 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 394 | NR1L-ComfortHMI-384 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 394 | NR1L-ComfortHMI-384 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 395 | NR1L-ComfortHMI-385 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 395 | NR1L-ComfortHMI-385 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 395 | NR1L-ComfortHMI-385 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 396 | NR1L-ComfortHMI-386 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 396 | NR1L-ComfortHMI-386 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 396 | NR1L-ComfortHMI-386 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 397 | NR1L-ComfortHMI-387 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 397 | NR1L-ComfortHMI-387 | pre | 多條件並列於同一行 | 2. The vehicle has an ATC climate system, in which AUTO is shown |
| 397 | NR1L-ComfortHMI-387 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 397 | NR1L-ComfortHMI-387 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 398 | NR1L-ComfortHMI-388 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 398 | NR1L-ComfortHMI-388 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 398 | NR1L-ComfortHMI-388 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 399 | NR1L-ComfortHMI-389 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 399 | NR1L-ComfortHMI-389 | pre | 多條件並列於同一行 | 2. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 399 | NR1L-ComfortHMI-389 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 399 | NR1L-ComfortHMI-389 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 400 | NR1L-ComfortHMI-390 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 400 | NR1L-ComfortHMI-390 | pre | 多條件並列於同一行 | 2. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 400 | NR1L-ComfortHMI-390 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 400 | NR1L-ComfortHMI-390 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 401 | NR1L-ComfortHMI-391 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 401 | NR1L-ComfortHMI-391 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 401 | NR1L-ComfortHMI-391 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 402 | NR1L-ComfortHMI-392 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 402 | NR1L-ComfortHMI-392 | pre | 多條件並列於同一行 | 3. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 402 | NR1L-ComfortHMI-392 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 402 | NR1L-ComfortHMI-392 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 403 | NR1L-ComfortHMI-393 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 403 | NR1L-ComfortHMI-393 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 403 | NR1L-ComfortHMI-393 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 404 | NR1L-ComfortHMI-394 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 404 | NR1L-ComfortHMI-394 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 404 | NR1L-ComfortHMI-394 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 405 | NR1L-ComfortHMI-395 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 405 | NR1L-ComfortHMI-395 | pre | 多條件並列於同一行 | 2. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 405 | NR1L-ComfortHMI-395 | pre | 多條件並列於同一行 | 3. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 405 | NR1L-ComfortHMI-395 | pre | 多條件並列於同一行 | 5. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 405 | NR1L-ComfortHMI-395 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 406 | NR1L-ComfortHMI-396 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 406 | NR1L-ComfortHMI-396 | pre | 多條件並列於同一行 | 3. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 406 | NR1L-ComfortHMI-396 | pre | 多條件並列於同一行 | 5. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 406 | NR1L-ComfortHMI-396 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 407 | NR1L-ComfortHMI-397 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 407 | NR1L-ComfortHMI-397 | pre | 多條件並列於同一行 | 3. The vehicle is equipped with rear defrost, which is absent on some soft top v |
| 407 | NR1L-ComfortHMI-397 | pre | 多條件並列於同一行 | 5. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 407 | NR1L-ComfortHMI-397 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 408 | NR1L-ComfortHMI-398 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 408 | NR1L-ComfortHMI-398 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 408 | NR1L-ComfortHMI-398 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 409 | NR1L-ComfortHMI-399 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 409 | NR1L-ComfortHMI-399 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 409 | NR1L-ComfortHMI-399 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 410 | NR1L-ComfortHMI-400 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 410 | NR1L-ComfortHMI-400 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 410 | NR1L-ComfortHMI-400 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 411 | NR1L-ComfortHMI-401 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 411 | NR1L-ComfortHMI-401 | pre | 多條件並列於同一行 | 2. The vehicle is not a single zone climate configuration, for which Sync is not |
| 411 | NR1L-ComfortHMI-401 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 411 | NR1L-ComfortHMI-401 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 412 | NR1L-ComfortHMI-402 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 412 | NR1L-ComfortHMI-402 | pre | 多條件並列於同一行 | 2. The vehicle is not a single zone climate configuration, for which Sync is not |
| 412 | NR1L-ComfortHMI-402 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 412 | NR1L-ComfortHMI-402 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 413 | NR1L-ComfortHMI-403 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 413 | NR1L-ComfortHMI-403 | pre | 多條件並列於同一行 | 2. The vehicle is not a single zone climate configuration, for which Sync is not |
| 413 | NR1L-ComfortHMI-403 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 413 | NR1L-ComfortHMI-403 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 414 | NR1L-ComfortHMI-404 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 414 | NR1L-ComfortHMI-404 | pre | 多條件並列於同一行 | 2. The vehicle is not a single zone climate configuration, for which Sync is not |
| 414 | NR1L-ComfortHMI-404 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 414 | NR1L-ComfortHMI-404 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 415 | NR1L-ComfortHMI-405 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 415 | NR1L-ComfortHMI-405 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 415 | NR1L-ComfortHMI-405 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 416 | NR1L-ComfortHMI-406 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 416 | NR1L-ComfortHMI-406 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 416 | NR1L-ComfortHMI-406 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 417 | NR1L-ComfortHMI-407 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 417 | NR1L-ComfortHMI-407 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 417 | NR1L-ComfortHMI-407 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 418 | NR1L-ComfortHMI-408 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 418 | NR1L-ComfortHMI-408 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 418 | NR1L-ComfortHMI-408 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 419 | NR1L-ComfortHMI-409 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 419 | NR1L-ComfortHMI-409 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 419 | NR1L-ComfortHMI-409 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 420 | NR1L-ComfortHMI-410 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 420 | NR1L-ComfortHMI-410 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 420 | NR1L-ComfortHMI-410 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 421 | NR1L-ComfortHMI-411 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 421 | NR1L-ComfortHMI-411 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 421 | NR1L-ComfortHMI-411 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 422 | NR1L-ComfortHMI-412 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 422 | NR1L-ComfortHMI-412 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 422 | NR1L-ComfortHMI-412 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 423 | NR1L-ComfortHMI-413 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 423 | NR1L-ComfortHMI-413 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 423 | NR1L-ComfortHMI-413 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 424 | NR1L-ComfortHMI-414 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 424 | NR1L-ComfortHMI-414 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 424 | NR1L-ComfortHMI-414 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 425 | NR1L-ComfortHMI-415 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 425 | NR1L-ComfortHMI-415 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 425 | NR1L-ComfortHMI-415 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 426 | NR1L-ComfortHMI-416 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 426 | NR1L-ComfortHMI-416 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 426 | NR1L-ComfortHMI-416 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 427 | NR1L-ComfortHMI-417 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 427 | NR1L-ComfortHMI-417 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 427 | NR1L-ComfortHMI-417 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 428 | NR1L-ComfortHMI-418 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 428 | NR1L-ComfortHMI-418 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 428 | NR1L-ComfortHMI-418 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 429 | NR1L-ComfortHMI-419 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 429 | NR1L-ComfortHMI-419 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 429 | NR1L-ComfortHMI-419 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 430 | NR1L-ComfortHMI-420 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 430 | NR1L-ComfortHMI-420 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 430 | NR1L-ComfortHMI-420 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 431 | NR1L-ComfortHMI-421 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 431 | NR1L-ComfortHMI-421 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 431 | NR1L-ComfortHMI-421 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 432 | NR1L-ComfortHMI-422 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 432 | NR1L-ComfortHMI-422 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 432 | NR1L-ComfortHMI-422 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 433 | NR1L-ComfortHMI-423 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 433 | NR1L-ComfortHMI-423 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 433 | NR1L-ComfortHMI-423 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 434 | NR1L-ComfortHMI-424 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 434 | NR1L-ComfortHMI-424 | pre | 多條件並列於同一行 | 3. The vehicle is not a single zone climate configuration, for which Sync is not |
| 434 | NR1L-ComfortHMI-424 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 434 | NR1L-ComfortHMI-424 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 435 | NR1L-ComfortHMI-425 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 435 | NR1L-ComfortHMI-425 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 435 | NR1L-ComfortHMI-425 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 436 | NR1L-ComfortHMI-426 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 436 | NR1L-ComfortHMI-426 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 436 | NR1L-ComfortHMI-426 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 437 | NR1L-ComfortHMI-427 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 437 | NR1L-ComfortHMI-427 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 437 | NR1L-ComfortHMI-427 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 438 | NR1L-ComfortHMI-428 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 438 | NR1L-ComfortHMI-428 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 438 | NR1L-ComfortHMI-428 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 439 | NR1L-ComfortHMI-429 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 439 | NR1L-ComfortHMI-429 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 439 | NR1L-ComfortHMI-429 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 440 | NR1L-ComfortHMI-430 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 440 | NR1L-ComfortHMI-430 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 440 | NR1L-ComfortHMI-430 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 441 | NR1L-ComfortHMI-431 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 441 | NR1L-ComfortHMI-431 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 441 | NR1L-ComfortHMI-431 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 442 | NR1L-ComfortHMI-432 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 442 | NR1L-ComfortHMI-432 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 442 | NR1L-ComfortHMI-432 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 443 | NR1L-ComfortHMI-433 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 443 | NR1L-ComfortHMI-433 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 443 | NR1L-ComfortHMI-433 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 444 | NR1L-ComfortHMI-434 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 444 | NR1L-ComfortHMI-434 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 444 | NR1L-ComfortHMI-434 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 445 | NR1L-ComfortHMI-435 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 445 | NR1L-ComfortHMI-435 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 445 | NR1L-ComfortHMI-435 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 446 | NR1L-ComfortHMI-436 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 446 | NR1L-ComfortHMI-436 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 446 | NR1L-ComfortHMI-436 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 447 | NR1L-ComfortHMI-437 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 447 | NR1L-ComfortHMI-437 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 447 | NR1L-ComfortHMI-437 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 448 | NR1L-ComfortHMI-438 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 448 | NR1L-ComfortHMI-438 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 448 | NR1L-ComfortHMI-438 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 449 | NR1L-ComfortHMI-439 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 449 | NR1L-ComfortHMI-439 | pre | 多條件並列於同一行 | 2. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 450 | NR1L-ComfortHMI-440 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 450 | NR1L-ComfortHMI-440 | pre | 多條件並列於同一行 | 2. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 451 | NR1L-ComfortHMI-441 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 451 | NR1L-ComfortHMI-441 | pre | 多條件並列於同一行 | 2. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 452 | NR1L-ComfortHMI-442 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 452 | NR1L-ComfortHMI-442 | pre | 多條件並列於同一行 | 2. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 453 | NR1L-ComfortHMI-443 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 453 | NR1L-ComfortHMI-443 | pre | 多條件並列於同一行 | 2. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 454 | NR1L-ComfortHMI-444 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 454 | NR1L-ComfortHMI-444 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 454 | NR1L-ComfortHMI-444 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 455 | NR1L-ComfortHMI-445 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 455 | NR1L-ComfortHMI-445 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 455 | NR1L-ComfortHMI-445 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 456 | NR1L-ComfortHMI-446 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 456 | NR1L-ComfortHMI-446 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 456 | NR1L-ComfortHMI-446 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 457 | NR1L-ComfortHMI-447 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 457 | NR1L-ComfortHMI-447 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 457 | NR1L-ComfortHMI-447 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 458 | NR1L-ComfortHMI-448 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 458 | NR1L-ComfortHMI-448 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 458 | NR1L-ComfortHMI-448 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 459 | NR1L-ComfortHMI-449 | pre | 多條件並列於同一行 | 2. The vehicle is equipped with MAX A/C, whose screens are used when CCM relays  |
| 459 | NR1L-ComfortHMI-449 | pre | 多條件並列於同一行 | 3. The vehicle is not a single zone climate configuration, for which Sync is not |
| 459 | NR1L-ComfortHMI-449 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 459 | NR1L-ComfortHMI-449 | pre | 多條件並列於同一行 | 5. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 459 | NR1L-ComfortHMI-449 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 460 | NR1L-ComfortHMI-450 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 460 | NR1L-ComfortHMI-450 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 460 | NR1L-ComfortHMI-450 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 461 | NR1L-ComfortHMI-451 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 461 | NR1L-ComfortHMI-451 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 461 | NR1L-ComfortHMI-451 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 462 | NR1L-ComfortHMI-452 | pre | 多條件並列於同一行 | 2. The vehicle is not a single zone climate configuration, for which Sync is not |
| 462 | NR1L-ComfortHMI-452 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 462 | NR1L-ComfortHMI-452 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 462 | NR1L-ComfortHMI-452 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 463 | NR1L-ComfortHMI-453 | pre | 多條件並列於同一行 | 2. The vehicle is equipped with MAX A/C, whose screens are used when CCM relays  |
| 463 | NR1L-ComfortHMI-453 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 463 | NR1L-ComfortHMI-453 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 463 | NR1L-ComfortHMI-453 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 464 | NR1L-ComfortHMI-454 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 464 | NR1L-ComfortHMI-454 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 464 | NR1L-ComfortHMI-454 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 465 | NR1L-ComfortHMI-455 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 465 | NR1L-ComfortHMI-455 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 465 | NR1L-ComfortHMI-455 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 466 | NR1L-ComfortHMI-456 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 466 | NR1L-ComfortHMI-456 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 466 | NR1L-ComfortHMI-456 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 467 | NR1L-ComfortHMI-457 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 467 | NR1L-ComfortHMI-457 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 467 | NR1L-ComfortHMI-457 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 468 | NR1L-ComfortHMI-458 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 468 | NR1L-ComfortHMI-458 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 468 | NR1L-ComfortHMI-458 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 469 | NR1L-ComfortHMI-459 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 469 | NR1L-ComfortHMI-459 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 469 | NR1L-ComfortHMI-459 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 470 | NR1L-ComfortHMI-460 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 470 | NR1L-ComfortHMI-460 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 470 | NR1L-ComfortHMI-460 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 471 | NR1L-ComfortHMI-461 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 471 | NR1L-ComfortHMI-461 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 471 | NR1L-ComfortHMI-461 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 472 | NR1L-ComfortHMI-462 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 472 | NR1L-ComfortHMI-462 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 472 | NR1L-ComfortHMI-462 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 473 | NR1L-ComfortHMI-463 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 473 | NR1L-ComfortHMI-463 | pre | 多條件並列於同一行 | 5. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 473 | NR1L-ComfortHMI-463 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 474 | NR1L-ComfortHMI-464 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 474 | NR1L-ComfortHMI-464 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 474 | NR1L-ComfortHMI-464 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 475 | NR1L-ComfortHMI-465 | pre | 多條件並列於同一行 | 4. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 475 | NR1L-ComfortHMI-465 | pre | 多條件並列於同一行 | 5. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 475 | NR1L-ComfortHMI-465 | pre | 多條件並列於同一行 | 6. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 476 | NR1L-ComfortHMI-467 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 476 | NR1L-ComfortHMI-467 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 476 | NR1L-ComfortHMI-467 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 476 | NR1L-ComfortHMI-467 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 477 | NR1L-ComfortHMI-468 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 477 | NR1L-ComfortHMI-468 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 477 | NR1L-ComfortHMI-468 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 477 | NR1L-ComfortHMI-468 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 478 | NR1L-ComfortHMI-469 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 478 | NR1L-ComfortHMI-469 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 479 | NR1L-ComfortHMI-470 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 479 | NR1L-ComfortHMI-470 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 480 | NR1L-ComfortHMI-471 | pre | 多條件並列於同一行 | 1. The vehicle is not a single zone climate configuration, for which Sync is not |
| 480 | NR1L-ComfortHMI-471 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 480 | NR1L-ComfortHMI-471 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 480 | NR1L-ComfortHMI-471 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 481 | NR1L-ComfortHMI-472 | pre | 多條件並列於同一行 | 3. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 481 | NR1L-ComfortHMI-472 | pre | 多條件並列於同一行 | 4. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 481 | NR1L-ComfortHMI-472 | pre | 多條件並列於同一行 | 5. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 482 | NR1L-ComfortHMI-473 | pre | 多條件並列於同一行 | 2. The Seats tab is open and the lumbar/bolster level is away from both its mini |
| 483 | NR1L-ComfortHMI-474 | pre | 多條件並列於同一行 | 1. The vehicle is an EMEA ICS vehicle, whose climate interface is specified in c |
| 483 | NR1L-ComfortHMI-474 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 483 | NR1L-ComfortHMI-474 | pre | 多條件並列於同一行 | 3. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 484 | NR1L-ComfortHMI-475 | pre | 多條件並列於同一行 | 1. The vehicle has an ATC climate system, in which AUTO is shown |
| 484 | NR1L-ComfortHMI-475 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 484 | NR1L-ComfortHMI-475 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 484 | NR1L-ComfortHMI-475 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |
| 485 | NR1L-ComfortHMI-476 | pre | 多條件並列於同一行 | 1. The climate screen is open and the climate system is on |
| 485 | NR1L-ComfortHMI-476 | pre | 多條件並列於同一行 | 2. The vehicle does not have 3 knob HVAC controls with ICS, for which no HVAC sc |
| 485 | NR1L-ComfortHMI-476 | pre | 多條件並列於同一行 | 3. The vehicle is not an EMEA ICS vehicle, whose climate interface is specified  |
| 485 | NR1L-ComfortHMI-476 | pre | 多條件並列於同一行 | 4. The vehicle is not configured with a non-foldable secondary lower screen cont |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 443／列計 443）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-ComfortHMI-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | NR1L-ComfortHMI-002 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | NR1L-ComfortHMI-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | NR1L-ComfortHMI-004 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | NR1L-ComfortHMI-005 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | NR1L-ComfortHMI-006 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | NR1L-ComfortHMI-007 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | NR1L-ComfortHMI-008 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | NR1L-ComfortHMI-009 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | NR1L-ComfortHMI-010 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | NR1L-ComfortHMI-011 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | NR1L-ComfortHMI-012 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | NR1L-ComfortHMI-013 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | NR1L-ComfortHMI-014 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | NR1L-ComfortHMI-015 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | NR1L-ComfortHMI-016 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | NR1L-ComfortHMI-017 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 27 | NR1L-ComfortHMI-018 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 28 | NR1L-ComfortHMI-019 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 29 | NR1L-ComfortHMI-020 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 30 | NR1L-ComfortHMI-021 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 31 | NR1L-ComfortHMI-022 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 32 | NR1L-ComfortHMI-023 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 33 | NR1L-ComfortHMI-024 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 34 | NR1L-ComfortHMI-025 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 35 | NR1L-ComfortHMI-026 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 36 | NR1L-ComfortHMI-027 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 37 | NR1L-ComfortHMI-028 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 38 | NR1L-ComfortHMI-029 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 39 | NR1L-ComfortHMI-030 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 40 | NR1L-ComfortHMI-031 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 41 | NR1L-ComfortHMI-032 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 42 | NR1L-ComfortHMI-033 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 43 | NR1L-ComfortHMI-034 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 44 | NR1L-ComfortHMI-035 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 45 | NR1L-ComfortHMI-036 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 47 | NR1L-ComfortHMI-038 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 48 | NR1L-ComfortHMI-039 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 49 | NR1L-ComfortHMI-040 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 50 | NR1L-ComfortHMI-041 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 51 | NR1L-ComfortHMI-042 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 52 | NR1L-ComfortHMI-043 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 53 | NR1L-ComfortHMI-044 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 54 | NR1L-ComfortHMI-045 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 55 | NR1L-ComfortHMI-046 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 56 | NR1L-ComfortHMI-047 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 57 | NR1L-ComfortHMI-048 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 58 | NR1L-ComfortHMI-049 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 59 | NR1L-ComfortHMI-050 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 60 | NR1L-ComfortHMI-051 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 61 | NR1L-ComfortHMI-052 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 62 | NR1L-ComfortHMI-053 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 63 | NR1L-ComfortHMI-054 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 64 | NR1L-ComfortHMI-055 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 65 | NR1L-ComfortHMI-056 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 66 | NR1L-ComfortHMI-057 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 67 | NR1L-ComfortHMI-058 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 70 | NR1L-ComfortHMI-061 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 72 | NR1L-ComfortHMI-063 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 73 | NR1L-ComfortHMI-064 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 74 | NR1L-ComfortHMI-065 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 75 | NR1L-ComfortHMI-066 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 76 | NR1L-ComfortHMI-067 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 77 | NR1L-ComfortHMI-068 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 78 | NR1L-ComfortHMI-069 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 79 | NR1L-ComfortHMI-070 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 80 | NR1L-ComfortHMI-071 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 81 | NR1L-ComfortHMI-072 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 82 | NR1L-ComfortHMI-073 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 83 | NR1L-ComfortHMI-074 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 84 | NR1L-ComfortHMI-075 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 85 | NR1L-ComfortHMI-076 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 86 | NR1L-ComfortHMI-077 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 87 | NR1L-ComfortHMI-078 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 88 | NR1L-ComfortHMI-079 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 89 | NR1L-ComfortHMI-080 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 90 | NR1L-ComfortHMI-081 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 91 | NR1L-ComfortHMI-082 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 92 | NR1L-ComfortHMI-083 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 93 | NR1L-ComfortHMI-084 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 94 | NR1L-ComfortHMI-085 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 95 | NR1L-ComfortHMI-086 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 96 | NR1L-ComfortHMI-087 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 97 | NR1L-ComfortHMI-088 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 98 | NR1L-ComfortHMI-089 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 99 | NR1L-ComfortHMI-090 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 100 | NR1L-ComfortHMI-091 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 101 | NR1L-ComfortHMI-092 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 102 | NR1L-ComfortHMI-093 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 103 | NR1L-ComfortHMI-094 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 104 | NR1L-ComfortHMI-095 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 105 | NR1L-ComfortHMI-096 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 106 | NR1L-ComfortHMI-097 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 107 | NR1L-ComfortHMI-098 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 108 | NR1L-ComfortHMI-099 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 109 | NR1L-ComfortHMI-100 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 110 | NR1L-ComfortHMI-101 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 111 | NR1L-ComfortHMI-102 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 112 | NR1L-ComfortHMI-103 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 113 | NR1L-ComfortHMI-104 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 114 | NR1L-ComfortHMI-105 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 115 | NR1L-ComfortHMI-106 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 116 | NR1L-ComfortHMI-466 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 117 | NR1L-ComfortHMI-107 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 118 | NR1L-ComfortHMI-108 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 119 | NR1L-ComfortHMI-109 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 120 | NR1L-ComfortHMI-110 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 121 | NR1L-ComfortHMI-111 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 122 | NR1L-ComfortHMI-112 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 123 | NR1L-ComfortHMI-113 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 124 | NR1L-ComfortHMI-114 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 125 | NR1L-ComfortHMI-115 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 126 | NR1L-ComfortHMI-116 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 127 | NR1L-ComfortHMI-117 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 128 | NR1L-ComfortHMI-118 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 132 | NR1L-ComfortHMI-122 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 133 | NR1L-ComfortHMI-123 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 135 | NR1L-ComfortHMI-125 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 136 | NR1L-ComfortHMI-126 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 137 | NR1L-ComfortHMI-127 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 138 | NR1L-ComfortHMI-128 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 139 | NR1L-ComfortHMI-129 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 140 | NR1L-ComfortHMI-130 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 141 | NR1L-ComfortHMI-131 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 142 | NR1L-ComfortHMI-132 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 143 | NR1L-ComfortHMI-133 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 144 | NR1L-ComfortHMI-134 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 145 | NR1L-ComfortHMI-135 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 146 | NR1L-ComfortHMI-136 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 147 | NR1L-ComfortHMI-137 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 148 | NR1L-ComfortHMI-138 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 149 | NR1L-ComfortHMI-139 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 150 | NR1L-ComfortHMI-140 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 151 | NR1L-ComfortHMI-141 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 152 | NR1L-ComfortHMI-142 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 153 | NR1L-ComfortHMI-143 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 154 | NR1L-ComfortHMI-144 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 155 | NR1L-ComfortHMI-145 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 156 | NR1L-ComfortHMI-146 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 157 | NR1L-ComfortHMI-147 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 158 | NR1L-ComfortHMI-148 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 159 | NR1L-ComfortHMI-149 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 160 | NR1L-ComfortHMI-150 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 161 | NR1L-ComfortHMI-151 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 162 | NR1L-ComfortHMI-152 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 163 | NR1L-ComfortHMI-153 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 164 | NR1L-ComfortHMI-154 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 165 | NR1L-ComfortHMI-155 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 166 | NR1L-ComfortHMI-156 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 167 | NR1L-ComfortHMI-157 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 168 | NR1L-ComfortHMI-158 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 169 | NR1L-ComfortHMI-159 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 170 | NR1L-ComfortHMI-160 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 171 | NR1L-ComfortHMI-161 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 173 | NR1L-ComfortHMI-163 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 174 | NR1L-ComfortHMI-164 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 175 | NR1L-ComfortHMI-165 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 176 | NR1L-ComfortHMI-166 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 177 | NR1L-ComfortHMI-167 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 178 | NR1L-ComfortHMI-168 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 179 | NR1L-ComfortHMI-169 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 180 | NR1L-ComfortHMI-170 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 181 | NR1L-ComfortHMI-171 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 182 | NR1L-ComfortHMI-172 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 183 | NR1L-ComfortHMI-173 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 184 | NR1L-ComfortHMI-174 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 185 | NR1L-ComfortHMI-175 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 186 | NR1L-ComfortHMI-176 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 187 | NR1L-ComfortHMI-177 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 188 | NR1L-ComfortHMI-178 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 189 | NR1L-ComfortHMI-179 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 190 | NR1L-ComfortHMI-180 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 191 | NR1L-ComfortHMI-181 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 192 | NR1L-ComfortHMI-182 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 193 | NR1L-ComfortHMI-183 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 194 | NR1L-ComfortHMI-184 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 195 | NR1L-ComfortHMI-185 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 196 | NR1L-ComfortHMI-186 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 197 | NR1L-ComfortHMI-187 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 198 | NR1L-ComfortHMI-188 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 199 | NR1L-ComfortHMI-189 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 200 | NR1L-ComfortHMI-190 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 201 | NR1L-ComfortHMI-191 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 202 | NR1L-ComfortHMI-192 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 203 | NR1L-ComfortHMI-193 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 204 | NR1L-ComfortHMI-194 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 208 | NR1L-ComfortHMI-198 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 219 | NR1L-ComfortHMI-209 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 220 | NR1L-ComfortHMI-210 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 221 | NR1L-ComfortHMI-211 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 222 | NR1L-ComfortHMI-212 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 223 | NR1L-ComfortHMI-213 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 224 | NR1L-ComfortHMI-214 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 225 | NR1L-ComfortHMI-215 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 226 | NR1L-ComfortHMI-216 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 227 | NR1L-ComfortHMI-217 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 228 | NR1L-ComfortHMI-218 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 229 | NR1L-ComfortHMI-219 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 230 | NR1L-ComfortHMI-220 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 231 | NR1L-ComfortHMI-221 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 232 | NR1L-ComfortHMI-222 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 233 | NR1L-ComfortHMI-223 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 234 | NR1L-ComfortHMI-224 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 235 | NR1L-ComfortHMI-225 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 236 | NR1L-ComfortHMI-226 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 237 | NR1L-ComfortHMI-227 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 238 | NR1L-ComfortHMI-228 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 239 | NR1L-ComfortHMI-229 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 240 | NR1L-ComfortHMI-230 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 241 | NR1L-ComfortHMI-231 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 242 | NR1L-ComfortHMI-232 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 243 | NR1L-ComfortHMI-233 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 244 | NR1L-ComfortHMI-234 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 245 | NR1L-ComfortHMI-235 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 246 | NR1L-ComfortHMI-236 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 247 | NR1L-ComfortHMI-237 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 248 | NR1L-ComfortHMI-238 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 249 | NR1L-ComfortHMI-239 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 250 | NR1L-ComfortHMI-240 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 251 | NR1L-ComfortHMI-241 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 252 | NR1L-ComfortHMI-242 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 253 | NR1L-ComfortHMI-243 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 254 | NR1L-ComfortHMI-244 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 255 | NR1L-ComfortHMI-245 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 256 | NR1L-ComfortHMI-246 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 257 | NR1L-ComfortHMI-247 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 258 | NR1L-ComfortHMI-248 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 259 | NR1L-ComfortHMI-249 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 260 | NR1L-ComfortHMI-250 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 261 | NR1L-ComfortHMI-251 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 262 | NR1L-ComfortHMI-252 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 263 | NR1L-ComfortHMI-253 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 264 | NR1L-ComfortHMI-254 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 265 | NR1L-ComfortHMI-255 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 266 | NR1L-ComfortHMI-256 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 267 | NR1L-ComfortHMI-257 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 268 | NR1L-ComfortHMI-258 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 269 | NR1L-ComfortHMI-259 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 270 | NR1L-ComfortHMI-260 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 271 | NR1L-ComfortHMI-261 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 272 | NR1L-ComfortHMI-262 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 273 | NR1L-ComfortHMI-263 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 274 | NR1L-ComfortHMI-264 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 275 | NR1L-ComfortHMI-265 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 276 | NR1L-ComfortHMI-266 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 277 | NR1L-ComfortHMI-267 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 278 | NR1L-ComfortHMI-268 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 279 | NR1L-ComfortHMI-269 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 280 | NR1L-ComfortHMI-270 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 281 | NR1L-ComfortHMI-271 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 282 | NR1L-ComfortHMI-272 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 283 | NR1L-ComfortHMI-273 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 284 | NR1L-ComfortHMI-274 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 285 | NR1L-ComfortHMI-275 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 286 | NR1L-ComfortHMI-276 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 287 | NR1L-ComfortHMI-277 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 288 | NR1L-ComfortHMI-278 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 289 | NR1L-ComfortHMI-279 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 292 | NR1L-ComfortHMI-282 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 294 | NR1L-ComfortHMI-284 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 295 | NR1L-ComfortHMI-285 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 296 | NR1L-ComfortHMI-286 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 297 | NR1L-ComfortHMI-287 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 298 | NR1L-ComfortHMI-288 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 299 | NR1L-ComfortHMI-289 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 300 | NR1L-ComfortHMI-290 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 301 | NR1L-ComfortHMI-291 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 302 | NR1L-ComfortHMI-292 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 303 | NR1L-ComfortHMI-293 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 304 | NR1L-ComfortHMI-294 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 305 | NR1L-ComfortHMI-295 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 306 | NR1L-ComfortHMI-296 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 307 | NR1L-ComfortHMI-297 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 308 | NR1L-ComfortHMI-298 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 309 | NR1L-ComfortHMI-299 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 310 | NR1L-ComfortHMI-300 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 311 | NR1L-ComfortHMI-301 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 312 | NR1L-ComfortHMI-302 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 313 | NR1L-ComfortHMI-303 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 314 | NR1L-ComfortHMI-304 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 315 | NR1L-ComfortHMI-305 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 316 | NR1L-ComfortHMI-306 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 317 | NR1L-ComfortHMI-307 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 319 | NR1L-ComfortHMI-309 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 320 | NR1L-ComfortHMI-310 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 321 | NR1L-ComfortHMI-311 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 323 | NR1L-ComfortHMI-313 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 324 | NR1L-ComfortHMI-314 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 325 | NR1L-ComfortHMI-315 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 326 | NR1L-ComfortHMI-316 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 327 | NR1L-ComfortHMI-317 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 328 | NR1L-ComfortHMI-318 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 329 | NR1L-ComfortHMI-319 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 330 | NR1L-ComfortHMI-320 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 331 | NR1L-ComfortHMI-321 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 332 | NR1L-ComfortHMI-322 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 333 | NR1L-ComfortHMI-323 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 334 | NR1L-ComfortHMI-324 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 335 | NR1L-ComfortHMI-325 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 336 | NR1L-ComfortHMI-326 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 337 | NR1L-ComfortHMI-327 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 338 | NR1L-ComfortHMI-328 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 339 | NR1L-ComfortHMI-329 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 340 | NR1L-ComfortHMI-330 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 341 | NR1L-ComfortHMI-331 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 342 | NR1L-ComfortHMI-332 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 343 | NR1L-ComfortHMI-333 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 344 | NR1L-ComfortHMI-334 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 345 | NR1L-ComfortHMI-335 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 346 | NR1L-ComfortHMI-336 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 347 | NR1L-ComfortHMI-337 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 348 | NR1L-ComfortHMI-338 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 349 | NR1L-ComfortHMI-339 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 350 | NR1L-ComfortHMI-340 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 351 | NR1L-ComfortHMI-341 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 352 | NR1L-ComfortHMI-342 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 353 | NR1L-ComfortHMI-343 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 354 | NR1L-ComfortHMI-344 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 355 | NR1L-ComfortHMI-345 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 356 | NR1L-ComfortHMI-346 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 357 | NR1L-ComfortHMI-347 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 358 | NR1L-ComfortHMI-348 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 359 | NR1L-ComfortHMI-349 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 360 | NR1L-ComfortHMI-350 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 361 | NR1L-ComfortHMI-351 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 362 | NR1L-ComfortHMI-352 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 363 | NR1L-ComfortHMI-353 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 364 | NR1L-ComfortHMI-354 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 365 | NR1L-ComfortHMI-355 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 366 | NR1L-ComfortHMI-356 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 367 | NR1L-ComfortHMI-357 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 368 | NR1L-ComfortHMI-358 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 369 | NR1L-ComfortHMI-359 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 370 | NR1L-ComfortHMI-360 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 371 | NR1L-ComfortHMI-361 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 372 | NR1L-ComfortHMI-362 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 373 | NR1L-ComfortHMI-363 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 374 | NR1L-ComfortHMI-364 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 375 | NR1L-ComfortHMI-365 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 376 | NR1L-ComfortHMI-366 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 377 | NR1L-ComfortHMI-367 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 378 | NR1L-ComfortHMI-368 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 379 | NR1L-ComfortHMI-369 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 380 | NR1L-ComfortHMI-370 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 381 | NR1L-ComfortHMI-371 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 384 | NR1L-ComfortHMI-374 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 385 | NR1L-ComfortHMI-375 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 386 | NR1L-ComfortHMI-376 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 387 | NR1L-ComfortHMI-377 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 388 | NR1L-ComfortHMI-378 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 389 | NR1L-ComfortHMI-379 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 391 | NR1L-ComfortHMI-381 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 392 | NR1L-ComfortHMI-382 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 393 | NR1L-ComfortHMI-383 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 394 | NR1L-ComfortHMI-384 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 395 | NR1L-ComfortHMI-385 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 396 | NR1L-ComfortHMI-386 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 397 | NR1L-ComfortHMI-387 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 398 | NR1L-ComfortHMI-388 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 399 | NR1L-ComfortHMI-389 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 400 | NR1L-ComfortHMI-390 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 401 | NR1L-ComfortHMI-391 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 402 | NR1L-ComfortHMI-392 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 403 | NR1L-ComfortHMI-393 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 404 | NR1L-ComfortHMI-394 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 405 | NR1L-ComfortHMI-395 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 406 | NR1L-ComfortHMI-396 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 407 | NR1L-ComfortHMI-397 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 408 | NR1L-ComfortHMI-398 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 409 | NR1L-ComfortHMI-399 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 410 | NR1L-ComfortHMI-400 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 411 | NR1L-ComfortHMI-401 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 412 | NR1L-ComfortHMI-402 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 413 | NR1L-ComfortHMI-403 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 414 | NR1L-ComfortHMI-404 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 415 | NR1L-ComfortHMI-405 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 416 | NR1L-ComfortHMI-406 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 417 | NR1L-ComfortHMI-407 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 418 | NR1L-ComfortHMI-408 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 419 | NR1L-ComfortHMI-409 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 420 | NR1L-ComfortHMI-410 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 421 | NR1L-ComfortHMI-411 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 422 | NR1L-ComfortHMI-412 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 423 | NR1L-ComfortHMI-413 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 424 | NR1L-ComfortHMI-414 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 425 | NR1L-ComfortHMI-415 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 426 | NR1L-ComfortHMI-416 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 427 | NR1L-ComfortHMI-417 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 428 | NR1L-ComfortHMI-418 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 429 | NR1L-ComfortHMI-419 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 430 | NR1L-ComfortHMI-420 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 431 | NR1L-ComfortHMI-421 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 432 | NR1L-ComfortHMI-422 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 433 | NR1L-ComfortHMI-423 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 434 | NR1L-ComfortHMI-424 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 435 | NR1L-ComfortHMI-425 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 436 | NR1L-ComfortHMI-426 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 437 | NR1L-ComfortHMI-427 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 438 | NR1L-ComfortHMI-428 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 439 | NR1L-ComfortHMI-429 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 440 | NR1L-ComfortHMI-430 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 441 | NR1L-ComfortHMI-431 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 442 | NR1L-ComfortHMI-432 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 443 | NR1L-ComfortHMI-433 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 444 | NR1L-ComfortHMI-434 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 445 | NR1L-ComfortHMI-435 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 446 | NR1L-ComfortHMI-436 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 447 | NR1L-ComfortHMI-437 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 448 | NR1L-ComfortHMI-438 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 449 | NR1L-ComfortHMI-439 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 450 | NR1L-ComfortHMI-440 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 451 | NR1L-ComfortHMI-441 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 452 | NR1L-ComfortHMI-442 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 453 | NR1L-ComfortHMI-443 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 454 | NR1L-ComfortHMI-444 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 456 | NR1L-ComfortHMI-446 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 457 | NR1L-ComfortHMI-447 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 458 | NR1L-ComfortHMI-448 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 459 | NR1L-ComfortHMI-449 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 460 | NR1L-ComfortHMI-450 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 461 | NR1L-ComfortHMI-451 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 462 | NR1L-ComfortHMI-452 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 463 | NR1L-ComfortHMI-453 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 464 | NR1L-ComfortHMI-454 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 465 | NR1L-ComfortHMI-455 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 466 | NR1L-ComfortHMI-456 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 467 | NR1L-ComfortHMI-457 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 469 | NR1L-ComfortHMI-459 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 470 | NR1L-ComfortHMI-460 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 471 | NR1L-ComfortHMI-461 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 472 | NR1L-ComfortHMI-462 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 474 | NR1L-ComfortHMI-464 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 475 | NR1L-ComfortHMI-465 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 476 | NR1L-ComfortHMI-467 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 477 | NR1L-ComfortHMI-468 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 478 | NR1L-ComfortHMI-469 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 479 | NR1L-ComfortHMI-470 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 480 | NR1L-ComfortHMI-471 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 481 | NR1L-ComfortHMI-472 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 482 | NR1L-ComfortHMI-473 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 483 | NR1L-ComfortHMI-474 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 484 | NR1L-ComfortHMI-475 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 485 | NR1L-ComfortHMI-476 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### X — 導航路徑無固定入口（§5.8／R-G71）（行計 337／列計 275）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 15 | NR1L-ComfortHMI-006 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 16 | NR1L-ComfortHMI-007 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than the climate screen |
| 17 | NR1L-ComfortHMI-008 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than the climate screen |
| 19 | NR1L-ComfortHMI-010 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen outside the climate main category |
| 20 | NR1L-ComfortHMI-011 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen outside the climate main category |
| 21 | NR1L-ComfortHMI-012 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen outside the climate main category |
| 22 | NR1L-ComfortHMI-013 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 23 | NR1L-ComfortHMI-014 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 23 | NR1L-ComfortHMI-014 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Change the fan speed on the climate screen |
| 24 | NR1L-ComfortHMI-015 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 25 | NR1L-ComfortHMI-016 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 26 | NR1L-ComfortHMI-017 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Set a fan speed and an airflow mode from the climate screen with AUTO off |
| 27 | NR1L-ComfortHMI-018 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select an airflow mode on the climate screen |
| 27 | NR1L-ComfortHMI-018 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Turn front defrost on from the climate screen |
| 28 | NR1L-ComfortHMI-019 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the state of the "A/C" button on the climate screen with AUTO off and re |
| 29 | NR1L-ComfortHMI-020 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 30 | NR1L-ComfortHMI-021 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 31 | NR1L-ComfortHMI-022 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 32 | NR1L-ComfortHMI-023 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 33 | NR1L-ComfortHMI-024 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 34 | NR1L-ComfortHMI-025 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 34 | NR1L-ComfortHMI-025 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the climate screen for an "AUTO" button |
| 35 | NR1L-ComfortHMI-026 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 37 | NR1L-ComfortHMI-028 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "A/C" on the climate screen |
| 38 | NR1L-ComfortHMI-029 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "A/C" off and "AUTO" off from the climate screen |
| 39 | NR1L-ComfortHMI-030 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 40 | NR1L-ComfortHMI-031 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "A/C" off from the climate screen and note the "A/C" button |
| 41 | NR1L-ComfortHMI-032 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "RECIRC" on the climate screen |
| 42 | NR1L-ComfortHMI-033 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "RECIRC" button on the climate screen |
| 43 | NR1L-ComfortHMI-034 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "A/C" off and "RECIRC" off from the climate screen |
| 44 | NR1L-ComfortHMI-035 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 47 | NR1L-ComfortHMI-038 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "RECIRC" control on the climate screen |
| 48 | NR1L-ComfortHMI-039 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 49 | NR1L-ComfortHMI-040 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the temperature on the climate screen |
| 50 | NR1L-ComfortHMI-041 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the temperature on the climate screen |
| 52 | NR1L-ComfortHMI-043 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than the climate screen |
| 56 | NR1L-ComfortHMI-047 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 57 | NR1L-ComfortHMI-048 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 58 | NR1L-ComfortHMI-049 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the temperature shown on the climate screen and record it |
| 59 | NR1L-ComfortHMI-050 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the temperature shown on the climate screen and record it |
| 60 | NR1L-ComfortHMI-051 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the temperature shown on the climate screen and record it |
| 63 | NR1L-ComfortHMI-054 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 64 | NR1L-ComfortHMI-055 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than the climate screen |
| 65 | NR1L-ComfortHMI-056 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 65 | NR1L-ComfortHMI-056 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press the fan up button on the climate screen |
| 66 | NR1L-ComfortHMI-057 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 66 | NR1L-ComfortHMI-057 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Touch a fan segment on the climate screen |
| 67 | NR1L-ComfortHMI-058 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 67 | NR1L-ComfortHMI-058 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Slide across the fan segments on the climate screen |
| 68 | NR1L-ComfortHMI-059 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 68 | NR1L-ComfortHMI-059 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press the fan down button on the climate screen repeatedly until the fan spee |
| 69 | NR1L-ComfortHMI-060 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 70 | NR1L-ComfortHMI-061 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 71 | NR1L-ComfortHMI-062 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 71 | NR1L-ComfortHMI-062 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the number of fan segments on the climate screen |
| 72 | NR1L-ComfortHMI-063 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "FRONT DEF" on the climate screen |
| 73 | NR1L-ComfortHMI-064 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "A/C" off from the climate screen and note the "A/C" button |
| 74 | NR1L-ComfortHMI-065 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed on the climate screen and record it |
| 75 | NR1L-ComfortHMI-066 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select an airflow mode on the climate screen |
| 76 | NR1L-ComfortHMI-067 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "FRONT DEF" on from the climate screen |
| 77 | NR1L-ComfortHMI-068 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 78 | NR1L-ComfortHMI-069 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "FRONT DEF" on from the climate screen |
| 78 | NR1L-ComfortHMI-069 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the "RECIRC" button on the climate screen |
| 79 | NR1L-ComfortHMI-070 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "REAR DEFROST" on the climate screen |
| 80 | NR1L-ComfortHMI-071 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "REAR DEFROST" button on the climate screen |
| 81 | NR1L-ComfortHMI-072 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "REAR DEFROST" on from the climate screen |
| 82 | NR1L-ComfortHMI-073 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "REAR DEFROST" off from the climate screen and read the exterior rear-vi |
| 83 | NR1L-ComfortHMI-074 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 84 | NR1L-ComfortHMI-075 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 85 | NR1L-ComfortHMI-076 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 86 | NR1L-ComfortHMI-077 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 87 | NR1L-ComfortHMI-078 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed on the climate screen and record it |
| 87 | NR1L-ComfortHMI-078 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Turn the climate system off using the climate power button on the climate scr |
| 88 | NR1L-ComfortHMI-079 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 89 | NR1L-ComfortHMI-080 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "SYNC" on the climate screen |
| 90 | NR1L-ComfortHMI-081 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the climate screen |
| 91 | NR1L-ComfortHMI-082 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the climate screen |
| 92 | NR1L-ComfortHMI-083 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the climate screen |
| 92 | NR1L-ComfortHMI-083 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Change the airflow mode from the climate screen |
| 93 | NR1L-ComfortHMI-084 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the climate screen |
| 94 | NR1L-ComfortHMI-085 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 95 | NR1L-ComfortHMI-086 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 96 | NR1L-ComfortHMI-087 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 97 | NR1L-ComfortHMI-088 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 98 | NR1L-ComfortHMI-089 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select an airflow mode on the climate screen |
| 100 | NR1L-ComfortHMI-091 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select the "Face" airflow mode on the climate screen |
| 101 | NR1L-ComfortHMI-092 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select the "Feet" airflow mode on the climate screen |
| 108 | NR1L-ComfortHMI-099 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Climate main screen |
| 109 | NR1L-ComfortHMI-100 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than Climate main |
| 110 | NR1L-ComfortHMI-101 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than Climate main |
| 111 | NR1L-ComfortHMI-102 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than Climate main |
| 112 | NR1L-ComfortHMI-103 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than Climate main |
| 112 | NR1L-ComfortHMI-103 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press the Mode hard control from a screen other than Climate main and read th |
| 113 | NR1L-ComfortHMI-104 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Rear Climate screen |
| 114 | NR1L-ComfortHMI-105 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX A/C" on the climate screen |
| 115 | NR1L-ComfortHMI-106 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the climate parameters shown on the climate screen |
| 117 | NR1L-ComfortHMI-107 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 117 | NR1L-ComfortHMI-107 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the temperature control on the climate screen |
| 118 | NR1L-ComfortHMI-108 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 118 | NR1L-ComfortHMI-108 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the climate screen for an "Auto" control over the set temperature |
| 119 | NR1L-ComfortHMI-109 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the head unit menu |
| 119 | NR1L-ComfortHMI-109 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Read the head unit menu for an HVAC interaction that duplicates the 3 knob HV |
| 120 | NR1L-ComfortHMI-110 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the head unit menu |
| 120 | NR1L-ComfortHMI-110 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Read the menu bar for HVAC icons |
| 121 | NR1L-ComfortHMI-111 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the head unit menu |
| 121 | NR1L-ComfortHMI-111 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Read the menu bar for HVAC icons |
| 124 | NR1L-ComfortHMI-114 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen and read the fan speed |
| 126 | NR1L-ComfortHMI-116 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Tri-Mode Climate screen |
| 127 | NR1L-ComfortHMI-117 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Tri-Mode Climate screen |
| 128 | NR1L-ComfortHMI-118 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Tri-Mode Climate screen |
| 132 | NR1L-ComfortHMI-122 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 132 | NR1L-ComfortHMI-122 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the front defrost control label on the climate screen |
| 133 | NR1L-ComfortHMI-123 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen with MAX DEF not active |
| 143 | NR1L-ComfortHMI-133 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "MAX DEF" button on the climate screen |
| 143 | NR1L-ComfortHMI-133 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the "REAR DEF" button on the climate screen |
| 144 | NR1L-ComfortHMI-134 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the climate functions other than "MAX DEF" and "REAR DEF" on the climate |
| 145 | NR1L-ComfortHMI-135 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 145 | NR1L-ComfortHMI-135 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the climate screen for the rear defrost button |
| 146 | NR1L-ComfortHMI-136 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the head unit menu |
| 146 | NR1L-ComfortHMI-136 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Read the head unit menu for the comfort section |
| 147 | NR1L-ComfortHMI-137 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the rear climate screen |
| 148 | NR1L-ComfortHMI-138 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the rear climate screen |
| 149 | NR1L-ComfortHMI-139 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the rear climate screen |
| 150 | NR1L-ComfortHMI-140 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Display the front climate screen |
| 150 | NR1L-ComfortHMI-140 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the front screen |
| 151 | NR1L-ComfortHMI-141 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Change the rear temperature using the rear climate controls while the front c |
| 151 | NR1L-ComfortHMI-141 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Open the rear climate screen |
| 152 | NR1L-ComfortHMI-142 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the rear climate screen |
| 162 | NR1L-ComfortHMI-152 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the rear climate screen |
| 163 | NR1L-ComfortHMI-153 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the rear climate screen |
| 164 | NR1L-ComfortHMI-154 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the rear climate screen |
| 171 | NR1L-ComfortHMI-161 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the rear climate screen |
| 173 | NR1L-ComfortHMI-163 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press the climate power button on the screen |
| 174 | NR1L-ComfortHMI-164 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the rear climate off on the rear climate screen |
| 174 | NR1L-ComfortHMI-164 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the screen |
| 177 | NR1L-ComfortHMI-167 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the rear climate screen |
| 191 | NR1L-ComfortHMI-181 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the rear climate screen |
| 193 | NR1L-ComfortHMI-183 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Open the Rear Climate tab |
| 193 | NR1L-ComfortHMI-183 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Open the driver side climate dropdown menu in the status bar |
| 199 | NR1L-ComfortHMI-189 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the driver side climate dropdown menu |
| 200 | NR1L-ComfortHMI-190 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Open the Rear Climate tab |
| 201 | NR1L-ComfortHMI-191 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Read the Rear Climate button in the dropdown menu |
| 202 | NR1L-ComfortHMI-192 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the driver side climate dropdown menu |
| 203 | NR1L-ComfortHMI-193 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 208 | NR1L-ComfortHMI-198 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 212 | NR1L-ComfortHMI-202 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select an airflow mode on the climate screen |
| 213 | NR1L-ComfortHMI-203 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the fan speed indication on the climate screen |
| 214 | NR1L-ComfortHMI-204 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the AUTO state on the climate screen |
| 230 | NR1L-ComfortHMI-220 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Auto Comfort Settings for the heated and vented seats |
| 232 | NR1L-ComfortHMI-222 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the screen for a seat zone popup |
| 237 | NR1L-ComfortHMI-227 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press the seat zone soft button in the comfort screen |
| 249 | NR1L-ComfortHMI-239 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the screen and the heated seat level |
| 278 | NR1L-ComfortHMI-268 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Read which tab is currently shown on the lower screen and record it |
| 280 | NR1L-ComfortHMI-270 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Read which tab is currently shown in the climate section on the head unit and |
| 281 | NR1L-ComfortHMI-271 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Open the Seats tab |
| 281 | NR1L-ComfortHMI-271 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Read the list of lumbar and bolster adjustment types offered on the Seats tab |
| 284 | NR1L-ComfortHMI-274 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Select "Lumbar Up/Down" on the Seats tab |
| 284 | NR1L-ComfortHMI-274 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Open the Seats tab and read the selected option |
| 285 | NR1L-ComfortHMI-275 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Retract the lower screen |
| 292 | NR1L-ComfortHMI-282 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Set the climate off using the hard key while the head unit is not on the clim |
| 293 | NR1L-ComfortHMI-283 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Change the fan speed using the fan speed hard control from a screen other tha |
| 294 | NR1L-ComfortHMI-284 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the RVC screen |
| 295 | NR1L-ComfortHMI-285 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Change the fan speed using the fan speed hard control from a screen other tha |
| 296 | NR1L-ComfortHMI-286 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Change the fan speed using the fan speed hard control from a screen other tha |
| 298 | NR1L-ComfortHMI-288 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Change the fan speed using the fan speed hard control and read the screen |
| 299 | NR1L-ComfortHMI-289 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a NAV screen |
| 299 | NR1L-ComfortHMI-289 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Open a Projection screen |
| 302 | NR1L-ComfortHMI-292 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Touch the selectable item of the bottom pop-up and read the screen |
| 307 | NR1L-ComfortHMI-297 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the screen for an HVAC pop-up |
| 308 | NR1L-ComfortHMI-298 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Change the fan speed using the fan speed hard control from a screen other tha |
| 308 | NR1L-ComfortHMI-298 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the screen for an HVAC pop-up |
| 312 | NR1L-ComfortHMI-302 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Change the temperature on the lower HVAC screen |
| 326 | NR1L-ComfortHMI-316 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the screen for a fan speed pop-up |
| 327 | NR1L-ComfortHMI-317 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the screen for an airflow mode pop-up |
| 328 | NR1L-ComfortHMI-318 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the screen for a climate on/off pop-up |
| 329 | NR1L-ComfortHMI-319 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the screen for an AUTO pop-up |
| 337 | NR1L-ComfortHMI-327 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 338 | NR1L-ComfortHMI-328 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 339 | NR1L-ComfortHMI-329 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than the climate screen |
| 340 | NR1L-ComfortHMI-330 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the climate screen |
| 341 | NR1L-ComfortHMI-331 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen outside the climate main category |
| 342 | NR1L-ComfortHMI-332 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Open a screen outside the climate main category |
| 343 | NR1L-ComfortHMI-333 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen outside the climate main category |
| 344 | NR1L-ComfortHMI-334 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 344 | NR1L-ComfortHMI-334 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Change the fan speed using the fan speed control on the climate screen |
| 345 | NR1L-ComfortHMI-335 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Change the fan speed using the fan speed control on the climate screen |
| 346 | NR1L-ComfortHMI-336 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 347 | NR1L-ComfortHMI-337 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select an airflow mode on the climate screen |
| 348 | NR1L-ComfortHMI-338 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 349 | NR1L-ComfortHMI-339 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Set a fan speed and an airflow mode from the climate screen with AUTO off |
| 350 | NR1L-ComfortHMI-340 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "MAX A/C" on from the climate screen |
| 351 | NR1L-ComfortHMI-341 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 352 | NR1L-ComfortHMI-342 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 353 | NR1L-ComfortHMI-343 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 354 | NR1L-ComfortHMI-344 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 355 | NR1L-ComfortHMI-345 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen and read the "A/C" button |
| 356 | NR1L-ComfortHMI-346 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 356 | NR1L-ComfortHMI-346 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the climate screen for an "AUTO" button |
| 357 | NR1L-ComfortHMI-347 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press each of "MAX A/C", "A/C", "RECIRC", "MAX DEF" and "REAR DEFROST" on the |
| 358 | NR1L-ComfortHMI-348 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen on a vehicle whose model the system detects |
| 359 | NR1L-ComfortHMI-349 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen on a vehicle whose model the system cannot detect |
| 360 | NR1L-ComfortHMI-350 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Open the climate screen |
| 361 | NR1L-ComfortHMI-351 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Open the climate screen |
| 362 | NR1L-ComfortHMI-352 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Adjust the temperature to its highest position on the climate screen |
| 363 | NR1L-ComfortHMI-353 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 363 | NR1L-ComfortHMI-353 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Adjust the temperature on the climate screen |
| 364 | NR1L-ComfortHMI-354 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than the climate screen |
| 365 | NR1L-ComfortHMI-355 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Change the temperature using the temperature hard control from a screen other |
| 366 | NR1L-ComfortHMI-356 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the climate screen |
| 367 | NR1L-ComfortHMI-357 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the climate screen |
| 368 | NR1L-ComfortHMI-358 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the climate screen |
| 369 | NR1L-ComfortHMI-359 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the temperature shown on the climate screen and record it |
| 369 | NR1L-ComfortHMI-359 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press the temperature up arrow on the climate screen |
| 370 | NR1L-ComfortHMI-360 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the temperature shown on the climate screen and record it |
| 371 | NR1L-ComfortHMI-361 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the temperature shown on the climate screen and record it |
| 372 | NR1L-ComfortHMI-362 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the temperature shown on the climate screen and record it |
| 375 | NR1L-ComfortHMI-365 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Adjust the fan speed across its whole range on the climate screen |
| 376 | NR1L-ComfortHMI-366 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 376 | NR1L-ComfortHMI-366 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Change the fan speed on the climate screen |
| 377 | NR1L-ComfortHMI-367 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than the climate screen |
| 378 | NR1L-ComfortHMI-368 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 378 | NR1L-ComfortHMI-368 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press the fan up button on the climate screen |
| 379 | NR1L-ComfortHMI-369 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 379 | NR1L-ComfortHMI-369 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Touch a fan segment on the climate screen |
| 380 | NR1L-ComfortHMI-370 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 380 | NR1L-ComfortHMI-370 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Slide across the fan segments on the climate screen |
| 381 | NR1L-ComfortHMI-371 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 382 | NR1L-ComfortHMI-372 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 382 | NR1L-ComfortHMI-372 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press the fan down button on the climate screen repeatedly until the fan spee |
| 383 | NR1L-ComfortHMI-373 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 384 | NR1L-ComfortHMI-374 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "A/C" off on the climate screen |
| 384 | NR1L-ComfortHMI-374 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Select an airflow mode other than Windshield on the climate screen |
| 385 | NR1L-ComfortHMI-375 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Set the fan speed below its highest setting on the climate screen |
| 387 | NR1L-ComfortHMI-377 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Set "RECIRC" to closed on the climate screen |
| 388 | NR1L-ComfortHMI-378 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" off from the climate screen |
| 389 | NR1L-ComfortHMI-379 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "REAR DEFROST" off from the climate screen |
| 390 | NR1L-ComfortHMI-380 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select a known airflow mode on the climate screen |
| 391 | NR1L-ComfortHMI-381 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX DEF" on the climate screen |
| 395 | NR1L-ComfortHMI-385 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX DEF" on the climate screen |
| 397 | NR1L-ComfortHMI-387 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX DEF" on the climate screen |
| 398 | NR1L-ComfortHMI-388 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX DEF" on the climate screen |
| 399 | NR1L-ComfortHMI-389 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "REAR DEFROST" on the climate screen |
| 400 | NR1L-ComfortHMI-390 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "REAR DEFROST" button on the climate screen |
| 401 | NR1L-ComfortHMI-391 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the climate screen and the status bar |
| 402 | NR1L-ComfortHMI-392 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 403 | NR1L-ComfortHMI-393 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 404 | NR1L-ComfortHMI-394 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 405 | NR1L-ComfortHMI-395 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 406 | NR1L-ComfortHMI-396 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 407 | NR1L-ComfortHMI-397 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 408 | NR1L-ComfortHMI-398 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 409 | NR1L-ComfortHMI-399 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 410 | NR1L-ComfortHMI-400 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn the climate system off using the climate power button on the climate scr |
| 411 | NR1L-ComfortHMI-401 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the climate screen |
| 412 | NR1L-ComfortHMI-402 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the climate screen |
| 413 | NR1L-ComfortHMI-403 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the ICS climate screen |
| 414 | NR1L-ComfortHMI-404 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the ICS climate screen |
| 415 | NR1L-ComfortHMI-405 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select the "Face" airflow mode on the climate screen |
| 417 | NR1L-ComfortHMI-407 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select the "Feet" airflow mode on the climate screen |
| 418 | NR1L-ComfortHMI-408 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select the "Face" airflow mode on the climate screen |
| 419 | NR1L-ComfortHMI-409 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select the "Face" airflow mode on the climate screen |
| 420 | NR1L-ComfortHMI-410 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open Climate main on the climate screen |
| 421 | NR1L-ComfortHMI-411 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open Climate main on the climate screen |
| 422 | NR1L-ComfortHMI-412 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than Climate main |
| 423 | NR1L-ComfortHMI-413 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than Climate main |
| 424 | NR1L-ComfortHMI-414 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press the Mode hard control from a screen other than Climate main |
| 425 | NR1L-ComfortHMI-415 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press the Mode hard control from a screen other than Climate main |
| 425 | NR1L-ComfortHMI-415 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press the fan speed hard control and read the screen |
| 426 | NR1L-ComfortHMI-416 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open a screen other than Climate main |
| 426 | NR1L-ComfortHMI-416 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press the Mode hard control and read the displayed screen |
| 427 | NR1L-ComfortHMI-417 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the main category label on the climate screen and record it |
| 428 | NR1L-ComfortHMI-418 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Rear Climate screen and note the front airflow mode |
| 429 | NR1L-ComfortHMI-419 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "A/C" off from the climate screen |
| 430 | NR1L-ComfortHMI-420 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Select an airflow mode other than Face on the climate screen |
| 431 | NR1L-ComfortHMI-421 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Set the fan speed below its highest setting on the climate screen |
| 433 | NR1L-ComfortHMI-423 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Set "RECIRC" to open on the climate screen |
| 434 | NR1L-ComfortHMI-424 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" off from the climate screen |
| 435 | NR1L-ComfortHMI-425 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX A/C" on the climate screen |
| 436 | NR1L-ComfortHMI-426 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX A/C" on the climate screen |
| 437 | NR1L-ComfortHMI-427 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX A/C" on the climate screen |
| 438 | NR1L-ComfortHMI-428 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX A/C" on the climate screen |
| 439 | NR1L-ComfortHMI-429 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX A/C" on the climate screen |
| 442 | NR1L-ComfortHMI-432 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX A/C" on the climate screen |
| 443 | NR1L-ComfortHMI-433 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Press "MAX A/C" on the climate screen |
| 444 | NR1L-ComfortHMI-434 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 444 | NR1L-ComfortHMI-434 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Change the temperature using the temperature hard control from a screen other |
| 445 | NR1L-ComfortHMI-435 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 445 | NR1L-ComfortHMI-435 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the temperature control on the climate screen |
| 446 | NR1L-ComfortHMI-436 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen |
| 446 | NR1L-ComfortHMI-436 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the climate screen for an "AUTO" control over the set temperature |
| 449 | NR1L-ComfortHMI-439 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the controls screen |
| 450 | NR1L-ComfortHMI-440 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the controls screen |
| 451 | NR1L-ComfortHMI-441 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the controls screen |
| 452 | NR1L-ComfortHMI-442 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the controls screen |
| 453 | NR1L-ComfortHMI-443 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Leave the controls screen |
| 453 | NR1L-ComfortHMI-443 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Enter the controls screen |
| 454 | NR1L-ComfortHMI-444 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the climate screen and read the fan speed indicator |
| 455 | NR1L-ComfortHMI-445 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the home screen |
| 455 | NR1L-ComfortHMI-445 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Move through the Comfort widget screens until the first screen is shown again |
| 456 | NR1L-ComfortHMI-446 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the home screen |
| 456 | NR1L-ComfortHMI-446 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the first Comfort widget screen |
| 457 | NR1L-ComfortHMI-447 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the home screen |
| 457 | NR1L-ComfortHMI-447 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Move to the second Comfort widget screen |
| 458 | NR1L-ComfortHMI-448 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Move the Comfort widget to its second screen |
| 458 | NR1L-ComfortHMI-448 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Leave the home screen |
| 458 | NR1L-ComfortHMI-448 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Open the home screen |
| 459 | NR1L-ComfortHMI-449 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the home screen |
| 459 | NR1L-ComfortHMI-449 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the Climate screen of the Comfort widget |
| 465 | NR1L-ComfortHMI-455 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the Climate screen of the Comfort widget |
| 466 | NR1L-ComfortHMI-456 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the home screen |
| 466 | NR1L-ComfortHMI-456 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Move to the second Comfort widget screen |
| 467 | NR1L-ComfortHMI-457 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the second screen of the 50% Comfort widget |
| 467 | NR1L-ComfortHMI-457 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the Comfort features on that screen |
| 468 | NR1L-ComfortHMI-458 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the home screen |
| 468 | NR1L-ComfortHMI-458 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Move through the Comfort widget screens until the first screen is shown again |
| 471 | NR1L-ComfortHMI-461 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Comfort widget on the home screen |
| 473 | NR1L-ComfortHMI-463 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the home screen |
| 473 | NR1L-ComfortHMI-463 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Move through the Comfort widget screens until the first screen is shown again |
| 474 | NR1L-ComfortHMI-464 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the home screen |
| 474 | NR1L-ComfortHMI-464 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the first Comfort widget screen |
| 475 | NR1L-ComfortHMI-465 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the home screen |
| 475 | NR1L-ComfortHMI-465 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Move to the second Comfort widget screen |
| 476 | NR1L-ComfortHMI-467 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 477 | NR1L-ComfortHMI-468 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 478 | NR1L-ComfortHMI-469 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the temperature shown on the climate screen and record it |
| 478 | NR1L-ComfortHMI-469 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Long-press the temperature up arrow on the climate screen |
| 479 | NR1L-ComfortHMI-470 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the fan speed shown on the climate screen and record it |
| 480 | NR1L-ComfortHMI-471 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "SYNC" on from the climate screen |
| 480 | NR1L-ComfortHMI-471 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Change the fan speed from the climate screen |
| 481 | NR1L-ComfortHMI-472 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Climate main screen |
| 481 | NR1L-ComfortHMI-472 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press the Mode hard control while on the Climate main screen and read the mai |
| 482 | NR1L-ComfortHMI-473 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Long press "+" on the Seats tab of the touch screen |
| 482 | NR1L-ComfortHMI-473 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Release "+" on the touch screen |
| 483 | NR1L-ComfortHMI-474 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Read the temperature shown on the climate screen and record it |
| 483 | NR1L-ComfortHMI-474 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Press and hold the temperature up arrow on the climate screen |
| 484 | NR1L-ComfortHMI-475 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "AUTO" on from the climate screen |
| 485 | NR1L-ComfortHMI-476 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Turn "A/C" off from the climate screen and note the "A/C" button |

