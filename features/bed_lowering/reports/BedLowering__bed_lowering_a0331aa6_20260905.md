# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_BedLowering_20260902.xlsx

- 來源：`features/bed_lowering/output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_BedLowering_20260902.xlsx`（唯讀）
- 資料列數：151
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`bed_lowering`（P 採 R-1 v3；另跑 Q／R／T）

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
| H | ER 模糊語 (er) | 7 | 7 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 151 | 151 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 153 | 150 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 0 | 0 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 151 | 151 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 11 | 10 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| X | 導航路徑無固定入口（§5.8／R-G71） | 169 | 124 | 每行 | 未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改** |

**總計：行計 642**（列計不加總——同一列可觸發多項檢查）

## 明細

### H — ER 模糊語 (er)（行計 7／列計 7）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 19 | NR1L-BLM-010 | er | 關係模糊語 'matches' | ing vehicle posture matches the DJ/D2 HMI reference figure |
| 107 | NR1L-BLM-098 | er | 關係模糊語 'matches' | he Apps menu screen matches the defined Apps menu screen layout |
| 122 | NR1L-BLM-113 | er | 關係模糊語 'matches' | The status-bar icon matches the Bed Lowering status indication defined in the re |
| 124 | NR1L-BLM-115 | er | 關係模糊語 'matches' | The cluster screen matches the Bed Lowering active-state reference figure |
| 127 | NR1L-BLM-118 | er | 關係模糊語 'matches' | The cluster screen matches the Bed Lowering completion-state reference figure |
| 134 | NR1L-BLM-125 | er | 關係模糊語 'corresponds to' | The highlight state corresponds to the reported execution status, serving as its |
| 144 | NR1L-BLM-135 | er | 關係模糊語 'matches' | VIC message wording matches the SYS1 normalised text of NRL-193702 ⏎ 4. The EVIC m |

### K — CJK 字元（行計 151／列計 151）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-BLM-001 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 11 | NR1L-BLM-002 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 12 | NR1L-BLM-003 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 13 | NR1L-BLM-004 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 14 | NR1L-BLM-005 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 15 | NR1L-BLM-006 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 16 | NR1L-BLM-007 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 17 | NR1L-BLM-008 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 18 | NR1L-BLM-009 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 19 | NR1L-BLM-010 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 20 | NR1L-BLM-011 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 21 | NR1L-BLM-012 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 22 | NR1L-BLM-013 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 23 | NR1L-BLM-014 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 24 | NR1L-BLM-015 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 25 | NR1L-BLM-016 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 26 | NR1L-BLM-017 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 27 | NR1L-BLM-018 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 28 | NR1L-BLM-019 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 29 | NR1L-BLM-020 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 30 | NR1L-BLM-021 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 31 | NR1L-BLM-022 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 32 | NR1L-BLM-023 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 33 | NR1L-BLM-024 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 34 | NR1L-BLM-025 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 35 | NR1L-BLM-026 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 36 | NR1L-BLM-027 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 37 | NR1L-BLM-028 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 38 | NR1L-BLM-029 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 39 | NR1L-BLM-030 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 40 | NR1L-BLM-031 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 41 | NR1L-BLM-032 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 42 | NR1L-BLM-033 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 43 | NR1L-BLM-034 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 44 | NR1L-BLM-035 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 45 | NR1L-BLM-036 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 46 | NR1L-BLM-037 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 47 | NR1L-BLM-038 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 48 | NR1L-BLM-039 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 49 | NR1L-BLM-040 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 50 | NR1L-BLM-041 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 51 | NR1L-BLM-042 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 52 | NR1L-BLM-043 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 53 | NR1L-BLM-044 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 54 | NR1L-BLM-045 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 55 | NR1L-BLM-046 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 56 | NR1L-BLM-047 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 57 | NR1L-BLM-048 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 58 | NR1L-BLM-049 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 59 | NR1L-BLM-050 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 60 | NR1L-BLM-051 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 61 | NR1L-BLM-052 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 62 | NR1L-BLM-053 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 63 | NR1L-BLM-054 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 64 | NR1L-BLM-055 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 65 | NR1L-BLM-056 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 66 | NR1L-BLM-057 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 67 | NR1L-BLM-058 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 68 | NR1L-BLM-059 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 69 | NR1L-BLM-060 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 70 | NR1L-BLM-061 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 71 | NR1L-BLM-062 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 72 | NR1L-BLM-063 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 73 | NR1L-BLM-064 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 74 | NR1L-BLM-065 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 75 | NR1L-BLM-066 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 76 | NR1L-BLM-067 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 77 | NR1L-BLM-068 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 78 | NR1L-BLM-069 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 79 | NR1L-BLM-070 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 80 | NR1L-BLM-071 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 81 | NR1L-BLM-072 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 82 | NR1L-BLM-073 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 83 | NR1L-BLM-074 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 84 | NR1L-BLM-075 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 85 | NR1L-BLM-076 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 86 | NR1L-BLM-077 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 87 | NR1L-BLM-078 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 88 | NR1L-BLM-079 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 89 | NR1L-BLM-080 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 90 | NR1L-BLM-081 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 91 | NR1L-BLM-082 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 92 | NR1L-BLM-083 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 93 | NR1L-BLM-084 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 94 | NR1L-BLM-085 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 95 | NR1L-BLM-086 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 96 | NR1L-BLM-087 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 97 | NR1L-BLM-088 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 98 | NR1L-BLM-089 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 99 | NR1L-BLM-090 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 100 | NR1L-BLM-091 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 101 | NR1L-BLM-092 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 102 | NR1L-BLM-093 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 103 | NR1L-BLM-094 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 104 | NR1L-BLM-095 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 105 | NR1L-BLM-096 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 106 | NR1L-BLM-097 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 107 | NR1L-BLM-098 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 108 | NR1L-BLM-099 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 109 | NR1L-BLM-100 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 110 | NR1L-BLM-101 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 111 | NR1L-BLM-102 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 112 | NR1L-BLM-103 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 113 | NR1L-BLM-104 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 114 | NR1L-BLM-105 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 115 | NR1L-BLM-106 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 116 | NR1L-BLM-107 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 117 | NR1L-BLM-108 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 118 | NR1L-BLM-109 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 119 | NR1L-BLM-110 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 120 | NR1L-BLM-111 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 121 | NR1L-BLM-112 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 122 | NR1L-BLM-113 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 123 | NR1L-BLM-114 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 124 | NR1L-BLM-115 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 125 | NR1L-BLM-116 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 126 | NR1L-BLM-117 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 127 | NR1L-BLM-118 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 128 | NR1L-BLM-119 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 129 | NR1L-BLM-120 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 130 | NR1L-BLM-121 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 131 | NR1L-BLM-122 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 132 | NR1L-BLM-123 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 133 | NR1L-BLM-124 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 134 | NR1L-BLM-125 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 135 | NR1L-BLM-126 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 136 | NR1L-BLM-127 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 137 | NR1L-BLM-128 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 138 | NR1L-BLM-129 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 139 | NR1L-BLM-130 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 140 | NR1L-BLM-131 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 141 | NR1L-BLM-132 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 142 | NR1L-BLM-133 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 143 | NR1L-BLM-134 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 144 | NR1L-BLM-135 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 145 | NR1L-BLM-136 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 146 | NR1L-BLM-137 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 147 | NR1L-BLM-138 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 148 | NR1L-BLM-139 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 149 | NR1L-BLM-140 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 150 | NR1L-BLM-141 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 151 | NR1L-BLM-142 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 152 | NR1L-BLM-143 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 153 | NR1L-BLM-144 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 154 | NR1L-BLM-145 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 155 | NR1L-BLM-146 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 156 | NR1L-BLM-147 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 157 | NR1L-BLM-148 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 158 | NR1L-BLM-149 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 159 | NR1L-BLM-150 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |
| 160 | NR1L-BLM-151 | pre | 含 CJK 字元 | ody_Types = PENDING（待 VS-SL-02 §1 之裁定） |

### R — Pre-Condition 版面（未編號行／多條件並列）（行計 153／列計 150）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-BLM-001 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 11 | NR1L-BLM-002 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 12 | NR1L-BLM-003 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 13 | NR1L-BLM-004 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 14 | NR1L-BLM-005 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 15 | NR1L-BLM-006 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 16 | NR1L-BLM-007 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 17 | NR1L-BLM-008 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 18 | NR1L-BLM-009 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 19 | NR1L-BLM-010 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 20 | NR1L-BLM-011 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 21 | NR1L-BLM-012 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 22 | NR1L-BLM-013 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 23 | NR1L-BLM-014 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 24 | NR1L-BLM-015 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 25 | NR1L-BLM-016 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 26 | NR1L-BLM-017 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 27 | NR1L-BLM-018 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 28 | NR1L-BLM-019 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 29 | NR1L-BLM-020 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 30 | NR1L-BLM-021 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 31 | NR1L-BLM-022 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 32 | NR1L-BLM-023 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 33 | NR1L-BLM-024 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 34 | NR1L-BLM-025 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 35 | NR1L-BLM-026 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 36 | NR1L-BLM-027 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 37 | NR1L-BLM-028 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 38 | NR1L-BLM-029 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 39 | NR1L-BLM-030 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 40 | NR1L-BLM-031 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 41 | NR1L-BLM-032 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 42 | NR1L-BLM-033 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 43 | NR1L-BLM-034 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 44 | NR1L-BLM-035 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 45 | NR1L-BLM-036 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 46 | NR1L-BLM-037 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 47 | NR1L-BLM-038 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 48 | NR1L-BLM-039 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 49 | NR1L-BLM-040 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 50 | NR1L-BLM-041 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 51 | NR1L-BLM-042 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 52 | NR1L-BLM-043 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 53 | NR1L-BLM-044 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 54 | NR1L-BLM-045 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 55 | NR1L-BLM-046 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 56 | NR1L-BLM-047 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 57 | NR1L-BLM-048 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 58 | NR1L-BLM-049 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 59 | NR1L-BLM-050 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 59 | NR1L-BLM-050 | pre | 多條件並列於同一行 | 4. The cabin is under nighttime ambient lighting and the display is in night mod |
| 60 | NR1L-BLM-051 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 60 | NR1L-BLM-051 | pre | 多條件並列於同一行 | 4. The cabin is under nighttime ambient lighting and the display is in night mod |
| 61 | NR1L-BLM-052 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 61 | NR1L-BLM-052 | pre | 多條件並列於同一行 | 4. The cabin is under nighttime ambient lighting and the display is in night mod |
| 62 | NR1L-BLM-053 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 63 | NR1L-BLM-054 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 64 | NR1L-BLM-055 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 65 | NR1L-BLM-056 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 66 | NR1L-BLM-057 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 67 | NR1L-BLM-058 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 68 | NR1L-BLM-059 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 69 | NR1L-BLM-060 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 70 | NR1L-BLM-061 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 71 | NR1L-BLM-062 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 72 | NR1L-BLM-063 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 73 | NR1L-BLM-064 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 74 | NR1L-BLM-065 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 75 | NR1L-BLM-066 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 76 | NR1L-BLM-067 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 77 | NR1L-BLM-068 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 78 | NR1L-BLM-069 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 79 | NR1L-BLM-070 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 80 | NR1L-BLM-071 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 81 | NR1L-BLM-072 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 82 | NR1L-BLM-073 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 83 | NR1L-BLM-074 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 84 | NR1L-BLM-075 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 85 | NR1L-BLM-076 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 86 | NR1L-BLM-077 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 87 | NR1L-BLM-078 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 88 | NR1L-BLM-079 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 89 | NR1L-BLM-080 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 90 | NR1L-BLM-081 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 91 | NR1L-BLM-082 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 92 | NR1L-BLM-083 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 93 | NR1L-BLM-084 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 94 | NR1L-BLM-085 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 95 | NR1L-BLM-086 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 96 | NR1L-BLM-087 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 97 | NR1L-BLM-088 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 98 | NR1L-BLM-089 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 99 | NR1L-BLM-090 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 100 | NR1L-BLM-091 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 101 | NR1L-BLM-092 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 102 | NR1L-BLM-093 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 103 | NR1L-BLM-094 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 104 | NR1L-BLM-095 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 105 | NR1L-BLM-096 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 107 | NR1L-BLM-098 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 108 | NR1L-BLM-099 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 109 | NR1L-BLM-100 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 110 | NR1L-BLM-101 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 111 | NR1L-BLM-102 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 112 | NR1L-BLM-103 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 113 | NR1L-BLM-104 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 114 | NR1L-BLM-105 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 115 | NR1L-BLM-106 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 116 | NR1L-BLM-107 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 117 | NR1L-BLM-108 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 118 | NR1L-BLM-109 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 119 | NR1L-BLM-110 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 120 | NR1L-BLM-111 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 121 | NR1L-BLM-112 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 122 | NR1L-BLM-113 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 123 | NR1L-BLM-114 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 124 | NR1L-BLM-115 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 125 | NR1L-BLM-116 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 126 | NR1L-BLM-117 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 127 | NR1L-BLM-118 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 128 | NR1L-BLM-119 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 129 | NR1L-BLM-120 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 130 | NR1L-BLM-121 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 131 | NR1L-BLM-122 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 132 | NR1L-BLM-123 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 133 | NR1L-BLM-124 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 134 | NR1L-BLM-125 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 135 | NR1L-BLM-126 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 136 | NR1L-BLM-127 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 137 | NR1L-BLM-128 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 138 | NR1L-BLM-129 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 139 | NR1L-BLM-130 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 140 | NR1L-BLM-131 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 141 | NR1L-BLM-132 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 142 | NR1L-BLM-133 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 143 | NR1L-BLM-134 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 144 | NR1L-BLM-135 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 145 | NR1L-BLM-136 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 146 | NR1L-BLM-137 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 147 | NR1L-BLM-138 | pre | 多條件並列於同一行 | 2. The vehicle is stationary and the engine is running |
| 148 | NR1L-BLM-139 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 149 | NR1L-BLM-140 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 150 | NR1L-BLM-141 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 151 | NR1L-BLM-142 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 152 | NR1L-BLM-143 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 153 | NR1L-BLM-144 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 154 | NR1L-BLM-145 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 155 | NR1L-BLM-146 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 156 | NR1L-BLM-147 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 157 | NR1L-BLM-148 | pre | 多條件並列於同一行 | 3. The vehicle is stationary and the engine is running |
| 158 | NR1L-BLM-149 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 159 | NR1L-BLM-150 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |
| 160 | NR1L-BLM-151 | pre | 多條件並列於同一行 | 3. The HU is out of reset and the Controls tab is reachable |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 151／列計 151）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-BLM-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | NR1L-BLM-002 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | NR1L-BLM-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | NR1L-BLM-004 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | NR1L-BLM-005 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | NR1L-BLM-006 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | NR1L-BLM-007 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | NR1L-BLM-008 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | NR1L-BLM-009 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | NR1L-BLM-010 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | NR1L-BLM-011 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | NR1L-BLM-012 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | NR1L-BLM-013 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | NR1L-BLM-014 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | NR1L-BLM-015 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | NR1L-BLM-016 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | NR1L-BLM-017 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 27 | NR1L-BLM-018 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 28 | NR1L-BLM-019 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 29 | NR1L-BLM-020 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 30 | NR1L-BLM-021 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 31 | NR1L-BLM-022 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 32 | NR1L-BLM-023 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 33 | NR1L-BLM-024 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 34 | NR1L-BLM-025 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 35 | NR1L-BLM-026 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 36 | NR1L-BLM-027 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 37 | NR1L-BLM-028 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 38 | NR1L-BLM-029 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 39 | NR1L-BLM-030 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 40 | NR1L-BLM-031 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 41 | NR1L-BLM-032 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 42 | NR1L-BLM-033 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 43 | NR1L-BLM-034 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 44 | NR1L-BLM-035 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 45 | NR1L-BLM-036 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 46 | NR1L-BLM-037 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 47 | NR1L-BLM-038 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 48 | NR1L-BLM-039 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 49 | NR1L-BLM-040 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 50 | NR1L-BLM-041 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 51 | NR1L-BLM-042 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 52 | NR1L-BLM-043 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 53 | NR1L-BLM-044 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 54 | NR1L-BLM-045 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 55 | NR1L-BLM-046 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 56 | NR1L-BLM-047 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 57 | NR1L-BLM-048 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 58 | NR1L-BLM-049 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 59 | NR1L-BLM-050 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 60 | NR1L-BLM-051 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 61 | NR1L-BLM-052 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 62 | NR1L-BLM-053 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 63 | NR1L-BLM-054 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 64 | NR1L-BLM-055 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 65 | NR1L-BLM-056 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 66 | NR1L-BLM-057 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 67 | NR1L-BLM-058 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 68 | NR1L-BLM-059 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 69 | NR1L-BLM-060 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 70 | NR1L-BLM-061 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 71 | NR1L-BLM-062 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 72 | NR1L-BLM-063 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 73 | NR1L-BLM-064 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 74 | NR1L-BLM-065 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 75 | NR1L-BLM-066 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 76 | NR1L-BLM-067 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 77 | NR1L-BLM-068 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 78 | NR1L-BLM-069 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 79 | NR1L-BLM-070 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 80 | NR1L-BLM-071 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 81 | NR1L-BLM-072 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 82 | NR1L-BLM-073 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 83 | NR1L-BLM-074 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 84 | NR1L-BLM-075 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 85 | NR1L-BLM-076 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 86 | NR1L-BLM-077 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 87 | NR1L-BLM-078 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 88 | NR1L-BLM-079 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 89 | NR1L-BLM-080 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 90 | NR1L-BLM-081 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 91 | NR1L-BLM-082 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 92 | NR1L-BLM-083 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 93 | NR1L-BLM-084 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 94 | NR1L-BLM-085 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 95 | NR1L-BLM-086 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 96 | NR1L-BLM-087 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 97 | NR1L-BLM-088 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 98 | NR1L-BLM-089 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 99 | NR1L-BLM-090 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 100 | NR1L-BLM-091 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 101 | NR1L-BLM-092 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 102 | NR1L-BLM-093 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 103 | NR1L-BLM-094 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 104 | NR1L-BLM-095 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 105 | NR1L-BLM-096 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 106 | NR1L-BLM-097 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 107 | NR1L-BLM-098 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 108 | NR1L-BLM-099 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 109 | NR1L-BLM-100 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 110 | NR1L-BLM-101 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 111 | NR1L-BLM-102 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 112 | NR1L-BLM-103 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 113 | NR1L-BLM-104 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 114 | NR1L-BLM-105 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 115 | NR1L-BLM-106 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 116 | NR1L-BLM-107 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 117 | NR1L-BLM-108 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 118 | NR1L-BLM-109 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 119 | NR1L-BLM-110 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 120 | NR1L-BLM-111 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 121 | NR1L-BLM-112 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 122 | NR1L-BLM-113 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 123 | NR1L-BLM-114 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 124 | NR1L-BLM-115 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 125 | NR1L-BLM-116 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 126 | NR1L-BLM-117 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 127 | NR1L-BLM-118 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 128 | NR1L-BLM-119 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 129 | NR1L-BLM-120 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 130 | NR1L-BLM-121 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 131 | NR1L-BLM-122 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 132 | NR1L-BLM-123 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 133 | NR1L-BLM-124 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 134 | NR1L-BLM-125 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 135 | NR1L-BLM-126 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 136 | NR1L-BLM-127 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 137 | NR1L-BLM-128 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 138 | NR1L-BLM-129 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 139 | NR1L-BLM-130 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 140 | NR1L-BLM-131 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 141 | NR1L-BLM-132 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 142 | NR1L-BLM-133 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 143 | NR1L-BLM-134 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 144 | NR1L-BLM-135 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 145 | NR1L-BLM-136 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 146 | NR1L-BLM-137 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 147 | NR1L-BLM-138 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 148 | NR1L-BLM-139 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 149 | NR1L-BLM-140 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 150 | NR1L-BLM-141 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 151 | NR1L-BLM-142 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 152 | NR1L-BLM-143 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 153 | NR1L-BLM-144 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 154 | NR1L-BLM-145 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 155 | NR1L-BLM-146 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 156 | NR1L-BLM-147 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 157 | NR1L-BLM-148 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 158 | NR1L-BLM-149 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 159 | NR1L-BLM-150 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 160 | NR1L-BLM-151 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### W — ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）（行計 11／列計 10）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 22 | NR1L-BLM-013 | er | 比較關係 'differ from'，而 test_item 上半無數值 | . The corner levels differ from the values recorded in step 1, showing the exist |
| 28 | NR1L-BLM-019 | er | 比較關係 'same as'，而 test_item 上半無數值 | Controls tab is the same as recorded in step 1 ⏎ 3. The screen opened from the Hom |
| 28 | NR1L-BLM-019 | er | 比較關係 'same as'，而 test_item 上半無數值 | een shortcut is the same as recorded in step 1, showing all three entry points u |
| 51 | NR1L-BLM-042 | er | 比較關係 'same as'，而 test_item 上半無數值 | r levels remain the same as recorded in step 1 ⏎ 6. A Bed Lowering unsuccessful in |
| 107 | NR1L-BLM-098 | er | 比較關係 'matches'，而 test_item 上半無數值 | he Apps menu screen matches the defined Apps menu screen layout |
| 122 | NR1L-BLM-113 | er | 比較關係 'matches'，而 test_item 上半無數值 | The status-bar icon matches the Bed Lowering status indication defined in the re |
| 124 | NR1L-BLM-115 | er | 比較關係 'matches'，而 test_item 上半無數值 | The cluster screen matches the Bed Lowering active-state reference figure |
| 127 | NR1L-BLM-118 | er | 比較關係 'matches'，而 test_item 上半無數值 | The cluster screen matches the Bed Lowering completion-state reference figure |
| 134 | NR1L-BLM-125 | er | 比較關係 'corresponds to'，而 test_item 上半無數值 | The highlight state corresponds to the reported execution status, serving as its |
| 138 | NR1L-BLM-129 | er | 比較關係 'differs from'，而 test_item 上半無數值 | t is turned off and differs from the state recorded in step 1 |
| 144 | NR1L-BLM-135 | er | 比較關係 'matches'，而 test_item 上半無數值 | VIC message wording matches the SYS1 normalised text of NRL-193702 ⏎ 4. The EVIC m |

### X — 導航路徑無固定入口（§5.8／R-G71）（行計 169／列計 124）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-BLM-001 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Check that "Bed Lowering" is present on the HU Controls tab |
| 10 | NR1L-BLM-001 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab |
| 11 | NR1L-BLM-002 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 12 | NR1L-BLM-003 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 13 | NR1L-BLM-004 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 14 | NR1L-BLM-005 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Check that "Bed Lowering" is present on the HU Controls tab |
| 14 | NR1L-BLM-005 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab |
| 15 | NR1L-BLM-006 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 16 | NR1L-BLM-007 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 17 | NR1L-BLM-008 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 18 | NR1L-BLM-009 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 19 | NR1L-BLM-010 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 21 | NR1L-BLM-012 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 22 | NR1L-BLM-013 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 23 | NR1L-BLM-014 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 24 | NR1L-BLM-015 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Open the Controls tab on the HU |
| 24 | NR1L-BLM-015 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Check that the Bed Lowering control is rendered as an on-screen soft button |
| 25 | NR1L-BLM-016 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the APPS menu on the HU |
| 25 | NR1L-BLM-016 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Check that the "Bed Lowering" soft button is available in the APPS menu |
| 26 | NR1L-BLM-017 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Open the Controls tab on the HU |
| 26 | NR1L-BLM-017 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Check that the "Bed Lowering" soft button is available in the Controls tab |
| 29 | NR1L-BLM-020 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the APPS menu on the HU |
| 30 | NR1L-BLM-021 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Check that "Bed Lowering" is offered on the HU Controls tab |
| 31 | NR1L-BLM-022 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 4. Check that "Bed Lowering" is offered on the HU Controls tab |
| 32 | NR1L-BLM-023 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Check that "Bed Lowering" is not offered for activation on the HU Controls ta |
| 33 | NR1L-BLM-024 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 4. Check that "Bed Lowering" is not offered for activation on the HU Controls ta |
| 34 | NR1L-BLM-025 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 4. Press "Bed Lowering" on the HU Controls tab and read $ASCM_FD_2.BDL_Enbl$ |
| 34 | NR1L-BLM-025 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 6. Press "Bed Lowering" on the HU Controls tab and check that $ASCM_FD_2.BDL_Enb |
| 35 | NR1L-BLM-026 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab and check that $ASCM_FD_2.BDL_Enb |
| 35 | NR1L-BLM-026 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 5. Press "Bed Lowering" on the HU Controls tab and check that $ASCM_FD_2.BDL_Enb |
| 36 | NR1L-BLM-027 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab and check that $ASCM_FD_2.BDL_Enb |
| 36 | NR1L-BLM-027 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 5. Press "Bed Lowering" on the HU Controls tab and check that $ASCM_FD_2.BDL_Enb |
| 37 | NR1L-BLM-028 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab |
| 38 | NR1L-BLM-029 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab |
| 39 | NR1L-BLM-030 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab to enter Bed Lowering Mode |
| 40 | NR1L-BLM-031 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab to enter Bed Lowering Mode |
| 41 | NR1L-BLM-032 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Record the appearance of the HU Controls tab before any press |
| 41 | NR1L-BLM-032 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab |
| 41 | NR1L-BLM-032 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 4. Check that the HU Controls tab differs visually from the appearance recorded  |
| 42 | NR1L-BLM-033 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab |
| 43 | NR1L-BLM-034 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab |
| 44 | NR1L-BLM-035 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab |
| 45 | NR1L-BLM-036 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab |
| 47 | NR1L-BLM-038 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Check that no equivalent in-progress status message is displayed on the HU sc |
| 56 | NR1L-BLM-047 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Bed Lowering feature screen on the HU |
| 57 | NR1L-BLM-048 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Bed Lowering feature screen on the HU |
| 58 | NR1L-BLM-049 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Bed Lowering feature screen on the HU |
| 59 | NR1L-BLM-050 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Bed Lowering feature screen on the HU |
| 60 | NR1L-BLM-051 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Bed Lowering feature screen on the HU |
| 61 | NR1L-BLM-052 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Bed Lowering feature screen on the HU |
| 62 | NR1L-BLM-053 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Bed Lowering feature screen on the HU |
| 63 | NR1L-BLM-054 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Bed Lowering feature screen on the HU |
| 64 | NR1L-BLM-055 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Bed Lowering feature screen on the HU |
| 65 | NR1L-BLM-056 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Bed Lowering feature screen on the HU |
| 66 | NR1L-BLM-057 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Open the Bed Lowering feature screen on the HU |
| 69 | NR1L-BLM-060 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Open the Controls tab on the HU |
| 69 | NR1L-BLM-060 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Check that a "Bed Lowering" enabling control is present in the Controls tab |
| 71 | NR1L-BLM-062 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Open the Controls tab on the HU |
| 71 | NR1L-BLM-062 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Select the "Bed Lowering" enabling control in the Controls tab |
| 72 | NR1L-BLM-063 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu on the HU |
| 72 | NR1L-BLM-063 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Check that "Bed Lowering" is listed within the Apps menu |
| 73 | NR1L-BLM-064 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu on the HU |
| 76 | NR1L-BLM-067 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 4. Press "Bed Lowering" on the HU Controls tab and read $ASCM_FD_2.BDL_Enbl$ |
| 76 | NR1L-BLM-067 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 6. Press "Bed Lowering" on the HU Controls tab and check that $ASCM_FD_2.BDL_Enb |
| 77 | NR1L-BLM-068 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab and check that $ASCM_FD_2.BDL_Enb |
| 77 | NR1L-BLM-068 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 5. Press "Bed Lowering" on the HU Controls tab and check that $ASCM_FD_2.BDL_Enb |
| 78 | NR1L-BLM-069 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab and check that $ASCM_FD_2.BDL_Enb |
| 78 | NR1L-BLM-069 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 5. Press "Bed Lowering" on the HU Controls tab and check that $ASCM_FD_2.BDL_Enb |
| 79 | NR1L-BLM-070 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab |
| 80 | NR1L-BLM-071 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab |
| 81 | NR1L-BLM-072 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 82 | NR1L-BLM-073 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 83 | NR1L-BLM-074 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 84 | NR1L-BLM-075 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to enter Bed Lowering Mode |
| 85 | NR1L-BLM-076 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 3. Check that "Bed Lowering" is present in the Apps menu |
| 86 | NR1L-BLM-077 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Check that "Bed Lowering" is present in the Controls tab |
| 88 | NR1L-BLM-079 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Check that "Bed Lowering" is not available on the HU Controls tab |
| 88 | NR1L-BLM-079 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 5. Check that "Bed Lowering" is available on the HU Controls tab |
| 89 | NR1L-BLM-080 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 3. Check that "Bed Lowering" is not available for selection in the Apps menu |
| 90 | NR1L-BLM-081 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Check that "Bed Lowering" is not available for selection in the Controls tab |
| 92 | NR1L-BLM-083 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the applicable head unit menu |
| 92 | NR1L-BLM-083 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Check that a dedicated Bed Lowering icon is present in that menu |
| 93 | NR1L-BLM-084 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the applicable head unit menu |
| 93 | NR1L-BLM-084 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Check that the Bed Lowering feature screen is displayed |
| 94 | NR1L-BLM-085 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the applicable head unit menu |
| 94 | NR1L-BLM-085 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Compare the position of the Bed Lowering icon against the defined menu locati |
| 95 | NR1L-BLM-086 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the applicable head unit menu |
| 95 | NR1L-BLM-086 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Compare the Bed Lowering icon against the other feature icons in the same men |
| 96 | NR1L-BLM-087 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab once |
| 97 | NR1L-BLM-088 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab once |
| 98 | NR1L-BLM-089 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab |
| 99 | NR1L-BLM-090 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab |
| 100 | NR1L-BLM-091 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab |
| 101 | NR1L-BLM-092 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab |
| 101 | NR1L-BLM-092 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Check that the selected state of the app icon is the on-screen indication tha |
| 102 | NR1L-BLM-093 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab and read the signal $ASCM_FD_2.BD |
| 102 | NR1L-BLM-093 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab a second time |
| 103 | NR1L-BLM-094 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab to enter Bed Lowering Mode |
| 103 | NR1L-BLM-094 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab a second time |
| 104 | NR1L-BLM-095 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab to enter Bed Lowering Mode |
| 104 | NR1L-BLM-095 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 4. Press "Bed Lowering" on the HU Controls tab a second time |
| 105 | NR1L-BLM-096 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab to enter Bed Lowering Mode |
| 105 | NR1L-BLM-096 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab a second time |
| 106 | NR1L-BLM-097 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to enter Bed Lowering Mode |
| 106 | NR1L-BLM-097 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 5. Press "Bed Lowering" on the HU Controls tab a second time |
| 107 | NR1L-BLM-098 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu on the HU |
| 107 | NR1L-BLM-098 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Compare the Apps menu screen against the defined layout |
| 108 | NR1L-BLM-099 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu on the HU |
| 108 | NR1L-BLM-099 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Check that the Bed Lowering feature is presented in the Apps menu according t |
| 109 | NR1L-BLM-100 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu on the HU |
| 109 | NR1L-BLM-100 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Check that "Bed Lowering" can be selected from the displayed Apps menu screen |
| 110 | NR1L-BLM-101 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu on the HU |
| 110 | NR1L-BLM-101 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Check that "Bed Lowering" appears as one of the selectable options in the App |
| 111 | NR1L-BLM-102 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu on the HU |
| 112 | NR1L-BLM-103 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu on the HU |
| 112 | NR1L-BLM-103 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Check that the HMI flow continues to the Bed Lowering feature screen |
| 113 | NR1L-BLM-104 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu on the HU |
| 114 | NR1L-BLM-105 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu on the HU |
| 114 | NR1L-BLM-105 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Select "Bed Lowering" from the Apps menu |
| 114 | NR1L-BLM-105 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Check that the head unit navigated to the Bed Lowering feature screen |
| 115 | NR1L-BLM-106 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu on the HU |
| 115 | NR1L-BLM-106 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Select "Bed Lowering" from the Apps menu |
| 115 | NR1L-BLM-106 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Check that the Bed Lowering feature screen is the next screen shown, with no  |
| 116 | NR1L-BLM-107 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the Apps menu and select "Bed Lowering" |
| 116 | NR1L-BLM-107 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Compare the Bed Lowering feature screen against the defined controls and stat |
| 117 | NR1L-BLM-108 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab |
| 118 | NR1L-BLM-109 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab |
| 119 | NR1L-BLM-110 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab |
| 119 | NR1L-BLM-110 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Open the Bed Lowering screen and check that the selected visual state of the  |
| 120 | NR1L-BLM-111 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab |
| 121 | NR1L-BLM-112 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab |
| 122 | NR1L-BLM-113 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab |
| 124 | NR1L-BLM-115 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Compare the cluster screen against the Bed Lowering active-state reference fi |
| 127 | NR1L-BLM-118 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Compare the cluster screen against the Bed Lowering completion-state referenc |
| 133 | NR1L-BLM-124 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab |
| 134 | NR1L-BLM-125 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab |
| 135 | NR1L-BLM-126 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab |
| 136 | NR1L-BLM-127 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press "Bed Lowering" on the HU Controls tab to issue the Bed Lowering command |
| 137 | NR1L-BLM-128 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab and check that the button highlig |
| 138 | NR1L-BLM-129 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab, check that the button highlight  |
| 139 | NR1L-BLM-130 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab and check that the button highlig |
| 140 | NR1L-BLM-131 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab and check that the button highlig |
| 140 | NR1L-BLM-131 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 4. Check that no other visual state on the HU Controls tab has changed |
| 141 | NR1L-BLM-132 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to enter the Bed Lowering flow |
| 142 | NR1L-BLM-133 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab to enter the Bed Lowering flow |
| 142 | NR1L-BLM-133 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Check that no equivalent message is displayed on the HU screen |
| 143 | NR1L-BLM-134 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab to enter the Bed Lowering flow |
| 144 | NR1L-BLM-135 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab to enter the Bed Lowering flow |
| 145 | NR1L-BLM-136 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the head unit menu configuration |
| 145 | NR1L-BLM-136 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Change the menu placement of the Bed Lowering feature entry |
| 145 | NR1L-BLM-136 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 3. Check that the new placement is applied to the menu structure |
| 146 | NR1L-BLM-137 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Record the current menu location of the Bed Lowering feature entry |
| 146 | NR1L-BLM-137 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Change the head unit menu configuration so that the entry moves |
| 147 | NR1L-BLM-138 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Change the head unit menu configuration so that the Bed Lowering entry moves |
| 147 | NR1L-BLM-138 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 2. Locate and select the Bed Lowering entry in its new menu location |
| 147 | NR1L-BLM-138 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Check that the Bed Lowering feature screen is displayed |
| 148 | NR1L-BLM-139 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 149 | NR1L-BLM-140 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 1. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 150 | NR1L-BLM-141 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 151 | NR1L-BLM-142 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 152 | NR1L-BLM-143 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 153 | NR1L-BLM-144 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 154 | NR1L-BLM-145 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 155 | NR1L-BLM-146 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 156 | NR1L-BLM-147 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 157 | NR1L-BLM-148 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 2. Press "Bed Lowering" on the HU Controls tab to request the Bed Lowering funct |
| 158 | NR1L-BLM-149 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Check that "Bed Lowering" is not present on the HU Controls tab |
| 159 | NR1L-BLM-150 | proc | 導航標的 'tab' 而同 TC 無固定入口 | 3. Press the "Bed Lowering" position on the HU Controls tab |
| 160 | NR1L-BLM-151 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 3. Check that "Bed Lowering" is not listed as an available feature in the Apps m |

