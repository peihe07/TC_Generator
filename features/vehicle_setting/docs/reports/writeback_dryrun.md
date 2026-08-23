# writeback dry-run（W-120，42 輪）

母本：`FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS044_Vehicle Controls_20260819.xlsx`
分頁：`Test Case Specification 測試用例規範`；表頭列 9；資料列 10 起

**本輪不實寫**（67 包之閘：dry-run 通過 ＋ Pei 核可 ＋ 母本備份）。

## (1) 將寫入之列數

| 項 | 值 |
|---|---:|
| 將寫入 | **143** |
| 對照（交付累計） | 139 |
| 差 | **4** |

## (2) 逐欄非空數（16 欄）

| 欄 | 欄名 | 非空 | 應為 |
|---|---|---:|---:|
| `B` | No.# | 143 | 143 |
| `C` | Requirement or Design | 143 | 143 |
| `D` | Requirement or Design ID | 143 | 143 |
| `F` | Test Case ID | 143 | 143 |
| `G` | Test Group | 143 | 143 |
| `H` | Test Set | 143 | 143 |
| `I` | Test Item | 143 | 143 |
| `J` | Pre-Conditions | 143 | 143 |
| `K` | Input Test Data | 143 | 143 |
| `L` | Test procedure | 143 | 143 |
| `M` | Expected Result | 143 | 143 |
| `N` | Specification Reference | 143 | 143 |
| `P` | Test Case Priority | 143 | 143 |
| `R` | Test Case Design | 143 | 143 |
| `AA` | Test Case Author | 143 | 143 |
| `AH` | Remarks | 10 | 21 |

## (3) N 欄之多值列 —— 行數分布

| 行數 | 列數 |
|---:|---:|
| 1 | 136 |
| 2 | 7 |

## (4)–(7) 判準檢查（正常輸入 vs 錨點並列）

| 判準 | 應為 | 正常輸入 | 錨點（刻意違規） | 判 |
|---|---|---:|---:|---|
| (4) I 欄含空行 | 143 | 143 | 142 | PASS，可失敗 |
| (4) I 欄括號收尾 | 143 | 143 | 143 | PASS |
| (5) K 欄非 `NA` | 0 | 0 | 1 | PASS，可失敗 |
| (6) R 欄不在受控 9 值 | 0 | 0 | 1 | PASS，可失敗 |
| （附）N 欄逗號串接 | 0 | 0 | 1 | PASS，可失敗 |
| (7) AH 欄非空 | 21 | 10 | 10 | ⚠ 見上繳 37 §2 |

## (6) P 欄之三級計數

| 級 | 列數 |
|---|---:|
| P0 | 24 |
| P1 | 113 |
| P2 | 6 |

## (8) 母本現有列將被清空之欄範圍

母本現有資料列：**237**（清空範圍 B–AH）

| 欄 | 清空前非空 |
|---|---:|
| `B` | 237 |
| `C` | 0 |
| `D` | 237 |
| `F` | 0 |
| `G` | 0 |
| `H` | 237 |
| `I` | 237 |
| `J` | 0 |
| `K` | 0 |
| `L` | 191 |
| `M` | 191 |
| `N` | 237 |
| `P` | 0 |
| `R` | 0 |
| `AA` | 0 |
| `AH` | 0 |