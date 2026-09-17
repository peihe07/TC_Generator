# lint036 報告：diagnostics_pilot01.xlsx

- 來源：`features/diagnostics/sandbox/pilot01/diagnostics_pilot01.xlsx`（唯讀）
- 資料列數：14
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`diagnostics`（P 採 R-1 v3；另跑 Q／R／T）

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
| I | test_item 括號下半缺失 | 1 | 1 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 3 | 1 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v2 | 0 | 0 | 每次命中 | 已校準（SWC 0708：195 —— proc 11／er 184，見上繳 09） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 1 | 1 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 15 | 13 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 14 | 14 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| X | 導航路徑無固定入口（§5.8／R-G71） | 0 | 0 | 每行 | 未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改** |
| Y | PROXI 舊式（R-G70 v4.1：`$Param$ is set to` 為 VF230 同義舊式） | 0 | 0 | 每行 | 未校準（R-G70 v4.1，GC-10 新增）—— **WARN 只報不改**；既有交付本不回修（R-TM13），回修依 R-G72 |
| P-DIAG | `$XXXX` 非本 feature 之 DID 白名單（R-DIAG5(a)，Diagnostics profile 專屬） | 0 | 0 | 每列每欄每 token | 未校準（R-DIAG5(a)，CDD-01_A 新增）—— **feature 專屬**，僅 `--profile diagnostics` 啟用。 |
| U-DIAG | UDS 位元組串格式／`7F` 後缺 `(<label>)`（R-DIAG5(b)，Diagnostics profile 專屬） | 0 | 0 | 每列每位元組串 | 未校準（R-DIAG5(b)，CDD-01_A 新增）—— **feature 專屬**。 |
| R1-DIAG | Requirement ID 欄非單一 SWE1 ID（R-DIAG1(a)，Diagnostics profile 專屬） | 0 | 0 | 每列 | 未校準（R-DIAG1(a)，CDD-01_A 新增）—— **feature 專屬**。 |
| Z | Vehicle Model 七欄 1／0（R-CAM2，Camera profile 專屬） | 7 | 1 | 每列每欄；七欄全缺時每 sheet 記一筆 | 未校準（R-CAM2，CAM-02 新增）—— **feature 專屬**，僅 `--profile camera` 啟用；既有八本無此七欄，未啟用即不檢查（`Z=0` 在未啟用時是沉默，不是核可） |
| RM-DIAG | Remarks 非 R-DIAG 所定之五種定型句（Diagnostics profile 專屬） | 0 | 0 | 每列每段 | 未校準（R-DIAG3(amend)／R-DIAG6／R-DIAG7(a)，CDD-01_A 新增）—— **feature 專屬**。 |

**總計：行計 41**（列計不加總——同一列可觸發多項檢查）

## 明細

### I — test_item 括號下半缺失（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 23 | NR1L-DIAG-014 | test_item | 缺括號下半 | AMP shall process any chimes, and the HU shall switch phone call to cell phone. |

### M — 空欄三態（行計 3／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 23 | NR1L-DIAG-014 | pre | 空欄（非 NA、非 PENDING:） |  |
| 23 | NR1L-DIAG-014 | proc | 空欄（非 NA、非 PENDING:） |  |
| 23 | NR1L-DIAG-014 | er | 空欄（非 NA、非 PENDING:） |  |

### R — Pre-Condition 版面（未編號行／多條件並列）（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 23 | NR1L-DIAG-014 | pre | 未編號行 |  |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 15／列計 13）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-DIAG-001 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 11 | NR1L-DIAG-002 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 12 | NR1L-DIAG-003 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 13 | NR1L-DIAG-004 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 14 | NR1L-DIAG-005 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 15 | NR1L-DIAG-006 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 15 | NR1L-DIAG-006 | proc | PENDING 佔位（DR-DIAG-4） | 1. PENDING: DR-DIAG-4 $5000 controlOptionRecord encoding for tone selection |
| 15 | NR1L-DIAG-006 | er | PENDING 佔位（DR-DIAG-4） | 1. PENDING: DR-DIAG-4 $5000 controlOptionRecord encoding for tone selection |
| 16 | NR1L-DIAG-007 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 17 | NR1L-DIAG-008 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 18 | NR1L-DIAG-009 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 19 | NR1L-DIAG-010 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 20 | NR1L-DIAG-011 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 21 | NR1L-DIAG-012 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |
| 22 | NR1L-DIAG-013 | pre | PENDING 佔位（DR-DIAG-3） | 3. PENDING: DR-DIAG-3 diagnostic session prerequisite |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 14／列計 14）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-DIAG-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | NR1L-DIAG-002 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | NR1L-DIAG-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | NR1L-DIAG-004 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | NR1L-DIAG-005 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | NR1L-DIAG-006 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | NR1L-DIAG-007 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | NR1L-DIAG-008 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | NR1L-DIAG-009 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | NR1L-DIAG-010 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | NR1L-DIAG-011 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | NR1L-DIAG-012 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | NR1L-DIAG-013 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | NR1L-DIAG-014 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### Z — Vehicle Model 七欄 1／0（R-CAM2，Camera profile 專屬）（行計 7／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 23 | NR1L-DIAG-014 | vehicle_model[HDCC27] | R-CAM2(a)：七欄每列須填 `1` 或 `0`，不留空、不用其他符號 | (空) |
| 23 | NR1L-DIAG-014 | vehicle_model[DT27] | R-CAM2(a)：七欄每列須填 `1` 或 `0`，不留空、不用其他符號 | (空) |
| 23 | NR1L-DIAG-014 | vehicle_model[VF(ProMaster)637] | R-CAM2(a)：七欄每列須填 `1` 或 `0`，不留空、不用其他符號 | (空) |
| 23 | NR1L-DIAG-014 | vehicle_model[Commander (598)] | R-CAM2(a)：七欄每列須填 `1` 或 `0`，不留空、不用其他符號 | (空) |
| 23 | NR1L-DIAG-014 | vehicle_model[Regengade (5210)] | R-CAM2(a)：七欄每列須填 `1` 或 `0`，不留空、不用其他符號 | (空) |
| 23 | NR1L-DIAG-014 | vehicle_model[Toro(2261)] | R-CAM2(a)：七欄每列須填 `1` 或 `0`，不留空、不用其他符號 | (空) |
| 23 | NR1L-DIAG-014 | vehicle_model[Fastack (376)] | R-CAM2(a)：七欄每列須填 `1` 或 `0`，不留空、不用其他符號 | (空) |

