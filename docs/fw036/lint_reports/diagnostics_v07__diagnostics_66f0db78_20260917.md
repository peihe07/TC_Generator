# lint036 報告：diagnostics_v07.xlsx

- 來源：`features/diagnostics/sandbox/merged/diagnostics_v07.xlsx`（唯讀）
- 資料列數：544
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
| U | PENDING 佔位（四欄全掃，含 ER 側） | 3 | 2 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| Y | PROXI 舊式（R-G70 v4.1：`$Param$ is set to` 為 VF230 同義舊式） | 0 | 0 | 每行 | 未校準（R-G70 v4.1，GC-10 新增）—— **WARN 只報不改**；既有交付本不回修（R-TM13），回修依 R-G72 |
| P-DIAG | `$XXXX` 非本 feature 之 DID 白名單（R-DIAG5(a)，Diagnostics profile 專屬） | 0 | 0 | 每列每欄每 token | 未校準（R-DIAG5(a)，CDD-01_A 新增）—— **feature 專屬**，僅 `--profile diagnostics` 啟用。 |
| U-DIAG | UDS 位元組串格式／`7F` 後缺 `(<label>)`（R-DIAG5(b)，Diagnostics profile 專屬） | 0 | 0 | 每列每位元組串 | 未校準（R-DIAG5(b)，CDD-01_A 新增）—— **feature 專屬**。 |
| R1-DIAG | Requirement ID 欄非單一 SWE1 ID（R-DIAG1(a)，Diagnostics profile 專屬） | 0 | 0 | 每列 | 未校準（R-DIAG1(a)，CDD-01_A 新增）—— **feature 專屬**。 |
| Z | Vehicle Model 七欄 1／0（R-CAM2，Camera profile 專屬） | 0 | 0 | 每列每欄；七欄全缺時每 sheet 記一筆 | 未校準（R-CAM2，CAM-02 新增）—— **feature 專屬**，僅 `--profile camera` 啟用；既有八本無此七欄，未啟用即不檢查（`Z=0` 在未啟用時是沉默，不是核可） |
| RM-DIAG | Remarks 非 R-DIAG 所定之五種定型句（Diagnostics profile 專屬） | 0 | 0 | 每列每段 | 未校準（R-DIAG3(amend)／R-DIAG6／R-DIAG7(a)，CDD-01_A 新增）—— **feature 專屬**。 |
| SEC-DIAG | I/O Control（0x2F）之 TC 缺 security Pre-Condition（R-DIAG13，Diagnostics profile 專屬） | 0 | 0 | 每列 | 未校準（R-DIAG13，CDD-04 新增；R-DIAG13(amend) 排除 unsupported 型）—— **feature 專屬**；母體依母節反查（追補 A §一）。 |
| KEY-DIAG | 按鍵狀態 DID 之觸發鍵為 Power／Dark（R-DIAG14，Diagnostics profile 專屬） | 0 | 0 | 每列每次命中 | 未校準（R-DIAG14，CDD-04 新增）—— **feature 專屬**。 |
| PC-DIAG | Pre-Condition 含動作詞（R-DIAG18，Diagnostics profile 專屬） | 0 | 0 | 每列每行 | 未校準（R-DIAG18，CDD-06 新增）—— **feature 專屬**；IN §4.4 之機械守門。 |
| RT-DIAG | 常式之位元組式不合 `31 0<sub> <RID>`（R-DIAG20，Diagnostics profile 專屬） | 0 | 0 | 每列每行 | 未校準（R-DIAG20，CDD-08 新增）—— **feature 專屬**；母體依 Routine 母節反查（27 列）。 |
| NEG-DIAG | 長度軸 negative 之請求串同於正向串／描述行未綴省末 byte（R-DIAG22，Diagnostics profile 專屬） | 0 | 0 | 每列每項 | 未校準（R-DIAG22，CDD-09 新增）—— **feature 專屬**；**跨列**檢查，正向請求集合取自同 sheet。 |

**總計：行計 3**（列計不加總——同一列可觸發多項檢查）

## 明細

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 3／列計 2）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 290 | NR1L-DIAG-281 | proc | PENDING 佔位（DR-DIAG-1） | 2. PENDING: DR-DIAG-1 failure mode and NRC for the expected audio test tone vali |
| 290 | NR1L-DIAG-281 | er | PENDING 佔位（DR-DIAG-1） | 2. PENDING: DR-DIAG-1 failure mode and NRC for the expected audio test tone vali |
| 306 | NR1L-DIAG-297 | er | PENDING 佔位（DR-DIAG-1） | 1. PENDING: DR-DIAG-1 NRC value for an unsuccessful Sirius XM package ID applica |

