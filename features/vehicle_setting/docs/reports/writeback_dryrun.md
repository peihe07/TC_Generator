# writeback dry-run（W-120，42 輪）

母本：`FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS044_Vehicle Controls_20260819.xlsx`
分頁：`Test Case Specification 測試用例規範`；表頭列 9；資料列 10 起

**本輪不實寫**（67 包之閘：dry-run 通過 ＋ Pei 核可 ＋ 母本備份）。

## (1) 將寫入之列數

| 項 | 值 |
|---|---:|
| 將寫入 | **139** |
| 對照（交付累計） | 139 |
| 差 | **0** |

## (2) 逐欄非空數（16 欄）

| 欄 | 欄名 | 非空 | 應為 |
|---|---|---:|---:|
| `B` | No.# | 139 | 139 |
| `C` | Requirement or Design | 139 | 139 |
| `D` | Requirement or Design ID | 139 | 139 |
| `F` | Test Case ID | 139 | 139 |
| `G` | Test Group | 139 | 139 |
| `H` | Test Set | 139 | 139 |
| `I` | Test Item | 139 | 139 |
| `J` | Pre-Conditions | 139 | 139 |
| `K` | Input Test Data | 139 | 139 |
| `L` | Test procedure | 139 | 139 |
| `M` | Expected Result | 139 | 139 |
| `N` | Specification Reference | 139 | 139 |
| `P` | Test Case Priority | 139 | 139 |
| `R` | Test Case Design | 139 | 139 |
| `AA` | Test Case Author | 139 | 139 |
| `AH` | Remarks | 26 | 21 |

## (3) N 欄之多值列 —— 行數分布

| 行數 | 列數 |
|---:|---:|
| 1 | 132 |
| 2 | 7 |

## (4)–(7) 判準檢查（正常輸入 vs 錨點並列）

| 判準 | 應為 | 正常輸入 | 錨點（刻意違規） | 判 |
|---|---|---:|---:|---|
| (4) I 欄含空行 | 139 | 139 | 138 | PASS，可失敗 |
| (4) I 欄括號收尾 | 139 | 139 | 139 | PASS |
| (5) K 欄非 `NA` | 0 | 0 | 1 | PASS，可失敗 |
| (6) R 欄不在受控 9 值 | 0 | 0 | 1 | PASS，可失敗 |
| （附）N 欄逗號串接 | 0 | 0 | 1 | PASS，可失敗 |
| (7) AH 欄非空 | 21 | 26 | 26 | ⚠ 見上繳 37 §2 |

## (6) P 欄之三級計數

| 級 | 列數 |
|---|---:|
| P0 | 24 |
| P1 | 109 |
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