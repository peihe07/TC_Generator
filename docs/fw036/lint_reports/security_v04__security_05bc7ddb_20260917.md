# lint036 報告：security_v04.xlsx

- 來源：`features/security/sandbox/merged/security_v04.xlsx`（唯讀）
- 資料列數：100
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`security`（P 採 R-1 v3；另跑 Q／R／T）

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
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v2 | 0 | 0 | 每次命中 | 已校準（SWC 0708：195 —— proc 11／er 184，見上繳 09） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 0 | 0 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 4 | 4 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| X | 導航路徑無固定入口（§5.8／R-G71） | 0 | 0 | 每行 | 未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改** |
| Y | PROXI 舊式（R-G70 v4.1：`$Param$ is set to` 為 VF230 同義舊式） | 0 | 0 | 每行 | 未校準（R-G70 v4.1，GC-10 新增）—— **WARN 只報不改**；既有交付本不回修（R-TM13），回修依 R-G72 |
| SC | 步驟無執行通道／ER 無觀察手段（R-SEC7，Security profile 專屬） | 0 | 0 | 每編號步驟／每 ER 行 | 未校準（R-SEC7，SEC-02 新增）—— **feature 專屬**，僅 `--profile security` 啟用。對既有語料之假陽性率 Procedure 98.4%／ER 74.9%（九本 1,700 列實測，SEC-01 上繳包 8-2），**故絕不可入 PROFILE_CHECKS**；對 Security 自身之假陽性率待 Pilot |
| SS | Remarks 無 `source:` 標記／資產佔位之 `X-` 代號未載於 Remarks（R-SEC4(a)／R-SEC21(e)，Security profile 專屬） | 0 | 0 | 每列 | 未校準（R-SEC4(a)，SEC-02 新增；R-SEC21(e) 判項 SEC-08 增列）—— **feature 專屬**。判準面之偏差：R-SEC4(a) 原文為「於 reasoning 註明來源」，而 reasoning 在生成側 JSON、不在工作簿；本檢查改以 **Remarks 欄**之 `source:` 標記為判準，待 Pei 覆核（SEC-02 上繳包自報）。R-SEC14(c)：`<…>` 佔位不報 |

**總計：行計 5**（列計不加總——同一列可觸發多項檢查）

## 明細

### H — ER 模糊語 (er)（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 23 | NR1L-CP-012 | er | 關係模糊語 'align with' | satisfy "logs must align with Logdog requirements (Error-level only for defects |

### W — ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）（行計 4／列計 4）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | NR1L-CP-003 | er | 比較關係 'identical to'，而 test_item 上半無數值 | s a "Subject:" line identical to the subject name in SecurityAssets/oem-certs/ce |
| 13 | NR1L-CP-004 | er | 比較關係 'identical to'，而 test_item 上半無數值 | :" line that is not identical to the subject name in SecurityAssets/oem-certs/ce |
| 14 | NR1L-CP-005 | er | 比較關係 'identical to'，而 test_item 上半無數值 | s an "Issuer:" line identical to the issuer name in SecurityAssets/oem-certs/cer |
| 15 | NR1L-CP-006 | er | 比較關係 'identical to'，而 test_item 上半無數值 | :" line that is not identical to the issuer name in SecurityAssets/oem-certs/cer |

