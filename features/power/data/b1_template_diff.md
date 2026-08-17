# B1 — 範本全屬性比對（R-P79 / G56 / G57）

> 全程以 `zipfile` 直讀 `xl/*.xml`，**未經 openpyxl 寫入路徑、未呼叫 `save()`**（11 §I；R-G3）。
> 產生指令：`python features/power/scripts/build_template_diff.py`

## (a) 資料驗證（DV）—— G56

### Power（part `xl/worksheets/sheet6.xml`，DV 4 條）

| ns | sqref | type | formula1 | 涵蓋欄 | 語義 |
|---|---|---|---|---|---|
| main | `AG10:AG13` | list | `"Pass, Fail, Pending,Block,NA"` | AG | **?AG** |
| main | `Q10:Q221 R10:R11 P10:P11` | list | `"P0,P1,P2,P3"` | P, Q, R | **estimated_time(1)、estimated_time(2)、priority** |
| main | `U10:AA221` | list | `"0,1"` | U | **vehicle** |
| x14 | `S10:S221` | list | `Reference!$C$4:$C$12` | S | **design_method** |

### Comfort（part `xl/worksheets/sheet6.xml`，DV 4 條）

| ns | sqref | type | formula1 | 涵蓋欄 | 語義 |
|---|---|---|---|---|---|
| main | `P10:Q601` | list | `"P0,P1,P2,P3"` | P | **priority** |
| main | `AF10:AF601` | list | `"Pass, Fail, Pending,Block,NA"` | AF | **?AF** |
| main | `T10:Z601` | list | `"0,1"` | T | **vehicle** |
| x14 | `R10:R601` | list | `下拉選單!$A$1:$A$9` | R | **design_method** |

### Privacy（part `xl/worksheets/sheet6.xml`，DV 5 條）

| ns | sqref | type | formula1 | 涵蓋欄 | 語義 |
|---|---|---|---|---|---|
| main | `P10:Q11` | list | `"P0,P1,P2,P3"` | P | **priority** |
| main | `T10:Z11` | list | `"0,1"` | T | **vehicle** |
| main | `AF10:AF11` | list | `"Pass, Fail, Pending,Block,NA"` | AF | **?AF** |
| x14 | `R11:R20` | list | `下拉選單!$A$1:$A$11` | R | **design_method** |
| x14 | `R10` | list | `下拉選單!$A$1:$A$9` | R | **design_method** |

## (b) 分頁清單 —— G57

| # | Power | Comfort | Privacy |
|---|---|---|---|
| 1 | `Cover_old`（隱藏） | `Cover_old`（隱藏） | `Cover_old`（隱藏） |
| 2 | `ChangeHistory_old`（隱藏） | `ChangeHistory_old`（隱藏） | `ChangeHistory_old`（隱藏） |
| 3 | `Cover 封面` | `Cover 封面` | `Cover 封面` |
| 4 | `ChangeHistory 修訂履歷` | `ChangeHistory 修訂履歷` | `ChangeHistory 修訂履歷` |
| 5 | `Product Document 記錄封面頁` | `Product Document 記錄封面頁` | `Product Document 記錄封面頁` |
| 6 | `Test Case Specification&Result` | `Test Case Specification 測試用例規範` | `Test Case Specification 測試用例規範` |
| 7 | `Reference`（隱藏） | `Reference`（隱藏） | `Reference`（隱藏） |
| 8 | `Test Case Framework` | `QS Suggestion`（隱藏） | `QS Suggestion`（隱藏） |
| 9 | `QS Suggestion`（隱藏） | `下拉選單`（隱藏） | `下拉選單`（隱藏） |
| 10 | `下拉選單`（隱藏） | — | — |

## (c) 合併儲存格 —— G57

| feature | 筆數 | 內容（前 8 筆）|
|---|---|---|
| Power | **5** | `['U8:AA8', 'AC7:AI7', 'A1:AF1', 'B7:AB7', 'D5:F5']` |
| Comfort | **4** | `['T8:Z8', 'AB7:AH7', 'A1:AE1', 'B7:AA7']` |
| Privacy | **4** | `['T8:Z8', 'AB7:AH7', 'A1:AE1', 'B7:AA7']` |

## (d) 條件式格式 —— G57

| feature | 筆數 | 內容（前 8 筆）|
|---|---|---|
| Power | **1** | `[('H10:H145', ['colorScale'])]` |
| Comfort | **0** | `[]` |
| Privacy | **0** | `[]` |

## (e) 凍結窗格 —— G57

| feature | 筆數 | 內容（前 8 筆）|
|---|---|---|
| Power | **0** | `[]` |
| Comfort | **0** | `[]` |
| Privacy | **0** | `[]` |

## (f) 公式 —— G57

| feature | 筆數 | 內容（前 8 筆）|
|---|---|---|
| Power | **0** | `[]` |
| Comfort | **592** | `[('B10', 'IF(ISBLANK($D10),"",ROW()-9)'), ('B11', 'IF(ISBLANK($D11),"",ROW()-9)'), ('B12', ''), ('B13', ''), ('B14', ''), ('B15', ''), ('B16', ''), ('B17', '')]` |
| Privacy | **11** | `[('B10', 'IF(ISBLANK($D10),"",ROW()-9)'), ('B11', 'IF(ISBLANK($D11),"",ROW()-9)'), ('B12', ''), ('B13', ''), ('B14', ''), ('B15', ''), ('B16', ''), ('B17', '')]` |

## (e2) 欄寬 —— G57

| feature | 定義筆數 |
|---|---|
| Power | 37 |
| Comfort | 34 |
| Privacy | 34 |
