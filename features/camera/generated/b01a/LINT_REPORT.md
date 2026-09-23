# lint036 報告：b01a_lint.xlsx

- 來源：`b01a_lint.xlsx`（唯讀）—— **lint 專用暫存簿**，由本目錄之 22 份 json
  以母本第 9 列欄序組成，落於 session scratchpad，**未寫回任何交付工作簿**。
  組簿工具 `features/camera/scripts/lint_batch.py`
- 資料列數：22
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`camera`（P 採 R-1 v3；另跑 Q／R／T）

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
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v2 | 0 | 0 | 每次命中 | 已校準（SWC 0708：195 —— proc 11／er 184，見上繳 09） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 16 | 10 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 22 | 22 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| X | 導航路徑無固定入口（§5.8／R-G71） | 4 | 4 | 每行 | 未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改** |
| Y | PROXI 舊式（R-G70 v4.1：`$Param$ is set to` 為 VF230 同義舊式） | 0 | 0 | 每行 | 未校準（R-G70 v4.1，GC-10 新增）—— **WARN 只報不改**；既有交付本不回修（R-TM13），回修依 R-G72 |
| Z | Vehicle Model 七欄 1／0（R-CAM2，Camera profile 專屬） | 0 | 0 | 每列每欄；七欄全缺時每 sheet 記一筆 | 未校準（R-CAM2，CAM-02 新增）—— **feature 專屬**，僅 `--profile camera` 啟用；既有八本無此七欄，未啟用即不檢查（`Z=0` 在未啟用時是沉默，不是核可） |

**總計：行計 42**（列計不加總——同一列可觸發多項檢查）

## 明細

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 16／列計 10）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | NR1L-RVCHMI-003 | pre | PENDING 佔位（DR-CAM-r） | 3. PENDING: DR-CAM-r the equipment flag for the "Enhanced Camera App" feature is |
| 14 | NR1L-RVCHMI-005 | proc | PENDING 佔位（DR-CAM-g） | 1. PENDING: DR-CAM-g open the Controls screen |
| 14 | NR1L-RVCHMI-005 | er | PENDING 佔位（DR-CAM-g） | 1. PENDING: DR-CAM-g the Controls screen is displayed |
| 16 | NR1L-RVCHMI-007 | pre | PENDING 佔位（DR-CAM-r） | 3. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sour |
| 18 | NR1L-RVCHMI-009 | pre | PENDING 佔位（DR-CAM-r） | 3. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sour |
| 18 | NR1L-RVCHMI-009 | proc | PENDING 佔位（DR-CAM-g） | 1. PENDING: DR-CAM-g open the Controls screen |
| 18 | NR1L-RVCHMI-009 | er | PENDING 佔位（DR-CAM-g） | 1. PENDING: DR-CAM-g the Controls screen is displayed |
| 19 | NR1L-RVCHMI-010 | pre | PENDING 佔位（DR-CAM-r） | 3. PENDING: DR-CAM-r the equipment flags for the "Camera App" and "Enhanced Came |
| 19 | NR1L-RVCHMI-010 | proc | PENDING 佔位（DR-CAM-g） | 1. PENDING: DR-CAM-g open the Controls screen |
| 19 | NR1L-RVCHMI-010 | er | PENDING 佔位（DR-CAM-g） | 1. PENDING: DR-CAM-g the Controls screen is displayed |
| 20 | NR1L-RVCHMI-011 | pre | PENDING 佔位（DR-CAM-r） | 3. PENDING: DR-CAM-r the equipment flags for the "Camera App" and "Enhanced Came |
| 21 | NR1L-RVCHMI-012 | pre | PENDING 佔位（DR-CAM-r） | 4. PENDING: DR-CAM-r the equipment flag for the "Enhanced Camera App" feature is |
| 22 | NR1L-RVCHMI-013 | pre | PENDING 佔位（DR-CAM-r） | 3. PENDING: DR-CAM-r the equipment flag for the "Enhanced Camera App" feature is |
| 25 | NR1L-RVCHMI-016 | pre | PENDING 佔位（DR-CAM-s） | 3. PENDING: DR-CAM-s the method to place the HU display into the thermal protect |
| 31 | NR1L-RVCHMI-022 | proc | PENDING 佔位（DR-CAM-g） | 1. PENDING: DR-CAM-g the entry path to the Controls screen (Vehicle Page) is not |
| 31 | NR1L-RVCHMI-022 | er | PENDING 佔位（DR-CAM-g） | 1. PENDING: DR-CAM-g the Controls screen (Vehicle Page) is displayed |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 22／列計 22）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-RVCHMI-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | NR1L-RVCHMI-002 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | NR1L-RVCHMI-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | NR1L-RVCHMI-004 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | NR1L-RVCHMI-005 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | NR1L-RVCHMI-006 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | NR1L-RVCHMI-007 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | NR1L-RVCHMI-008 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | NR1L-RVCHMI-009 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | NR1L-RVCHMI-010 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | NR1L-RVCHMI-011 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | NR1L-RVCHMI-012 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | NR1L-RVCHMI-013 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | NR1L-RVCHMI-014 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | NR1L-RVCHMI-015 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | NR1L-RVCHMI-016 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | NR1L-RVCHMI-017 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 27 | NR1L-RVCHMI-018 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 28 | NR1L-RVCHMI-019 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 29 | NR1L-RVCHMI-020 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 30 | NR1L-RVCHMI-021 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 31 | NR1L-RVCHMI-022 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### X — 導航路徑無固定入口（§5.8／R-G71）（行計 4／列計 4）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 14 | NR1L-RVCHMI-005 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Select the Rear View Camera soft control on the Controls screen |
| 18 | NR1L-RVCHMI-009 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the Controls screen and check that no Rear View Camera soft control is o |
| 19 | NR1L-RVCHMI-010 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Select the Rear View Camera soft control on the Controls screen |
| 31 | NR1L-RVCHMI-022 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Select the associated button in the «Controls» screen (Vehicle Page) |

