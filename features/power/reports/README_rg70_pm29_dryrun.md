# `rg70_pm29_dryrun_20260905.tsv` —— 已被 `_v41.tsv` 取代

本表為 R-G70 v4.0 期（PROXI 方向未裁）之 pm_29 轉換 dry-run，**685 列**。
現行表為 `rg70_pm29_dryrun_20260905_v41.tsv`（**584 列**，v4.1 判準）。
本表保留供沿革比對，**不得作為轉換依據**。

差異 −101 之成因（`docs/fw036/handoff/down/20260905_GC-12.md` 二-5；依 `docs/fw036/handoff/down/20260905_GC-12_addendum.md` 之 1 節複驗，四項分佈逐項相符）：

| 成因 | 列數 |
|---|---:|
| PROXI —— 舊表列入、新表排除 | **85** |
| 規則寬窄差 —— `buserror` 97→86 | 11 |
| 規則寬窄差 —— `send` 112→109 | 3 |
| 規則寬窄差 —— `recv` 183→182 | 1 |
| 規則寬窄差 —— `bare` 208→207 | 1 |
| **合計** | **101** |

**85 那筆不是漏轉，是無需轉**：pm_29 之 85 行 PROXI **全數已為 v4.1 標準式**
（`2. PROXI Brand_Configuration_2 = Jeep`、`3. PROXI SWITCH_OFF_DOOR = enable`），
舊式 `PROXI $…$ is set to` **0 行**。舊表列入係當時 R-G70(e) 與 R-VS86 方向未裁，
執行層刻意不選邊 —— 該 85 列之 `new_text` **全部留空**、`klass` 全為 `needs_ruling`。
新表排除之，正確。

殘差 16 之主因為樣式寬窄：舊表之 `The signal $X$` 會收到非 bus-error 之 ER，
新表之 `buserror` 為專式。

## 兩表不可逐列 join —— 單位不同（`docs/fw036/handoff/down/20260905_GC-12_addendum.md` 2 節之延伸）

該補遺 2 節已指出 `col` 語意不同，實測尚有第二層差異，**兩者都要處理**：

| | 舊表 | 新表 |
|---|---|---|
| `col` | `lint036` 欄鍵（`pre`／`input`／`proc`／`er`）| **1-based Excel 欄號**：`10`→pre、`11`→input、`12`→proc、`13`→er |
| `row` | 同基準（10–399）| 同基準（10–399）|
| 一列之單位 | 一**行**（保留 `1. ` 編號前綴）| 一**命中片段**（去編號前綴），且含 `（保留；…）` 之不轉換項 |

故 `(row, col, old_text)` 與 `(row, old_text)` 兩種鍵**皆零命中**。
可行者為 **`(row, 正規化 col)` 之儲存格層級**：舊 483 格／新 413 格／交集 412 格，
只在舊表 **71** 格（85 PROXI ＋ 8 `sig-bare` ＋ 1 `buserror`；同格多行故格數少於列數）、
只在新表 **1** 格（`('23','er')` = `is registered without a bus error`）。

## 查詢式（R-G50）

```text
母體：本目錄之二表
正規化：新表 col 依 {10:pre, 11:input, 12:proc, 13:er} 映射；old_text 去 `^\s*\d+[.)]\s*`
鍵：(row, col)
結果：舊 483／新 413／交集 412／只舊 71／只新 1
類別層級：85（PROXI）＋ 16（bare 1／recv 1／send 3／buserror 11）＝ 101
```
