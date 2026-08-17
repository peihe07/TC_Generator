# B1 — `workbook.columns` 三方交叉驗證（R-P73 / R-P74）

> **本檔為 10 包最重要之產出；寫回之開放與否繫於此。**
> 三份工作簿皆以 `read_only=True` 讀取，未寫入任何一份（10 §I）。

## 1. 三份來源

| feature | 分頁 | 欄數 | 資料列 | 狀態 |
|---|---|---|---|---|
| **Power** | `Test Case Specification&Result` | **35** | 0（BLANK，G10） | 待產出 |
| Comfort | `Test Case Specification 測試用例規範` | 34 | 466 | **已交付、已驗收** |
| Privacy | `Test Case Specification 測試用例規範` | 34 | 11 | **已交付、已驗收** |

> **第一項發現：分頁名不同。** Power 為 `Test Case Specification&Result`，
> Comfort / Privacy 為 `Test Case Specification 測試用例規範`。
> 二者為不同範本版本，非同一檔之差異。

## 2. r9 標頭逐欄三方對照（G52）

| 欄 | Power | Comfort | Privacy | 一致 |
|---|---|---|---|---|
| A | — | — | — | ✓ |
| B | `No.# 序號` | `No.# 序號` | `No.# 序號` | ✓ |
| C | `Requirement or Design ID (Polarion) 設計/需求 ID (Polarion)` | `Requirement or Design ID (Polarion) 設計/需求 ID (Polarion)` | `Requirement or Design ID (Polarion) 設計/需求 ID (Polarion)` | ✓ |
| D | `Requirement or Design ID 需求/設計 ID` | `Requirement or Design ID 需求/設計 ID` | `Requirement or Design ID 需求/設計 ID` | ✓ |
| E | `Test Case ID (TestRail) 測試用例 ID (TestRail)` | `Test Case ID (TestRail) 測試用例 ID (TestRail)` | `Test Case ID (TestRail) 測試用例 ID (TestRail)` | ✓ |
| F | `Test Case ID 測試用例ID` | `Test Case ID 測試用例ID` | `Test Case ID 測試用例ID` | ✓ |
| G | `Test Group 測試組` | `Test Group 測試組` | `Test Group 測試組` | ✓ |
| H | `Test Set 測試集` | `Test Set 測試集` | `Test Set 測試集` | ✓ |
| I | `Test Item 測試項目` | `Test Item 測試項目` | `Test Item 測試項目` | ✓ |
| J | `Pre-Conditions 先前條件` | `Pre-Conditions 先前條件` | `Pre-Conditions 先前條件` | ✓ |
| K | `Input Test Data 輸入條件` | `Input Test Data 輸入條件` | `Input Test Data 輸入條件` | ✓ |
| L | `Test procedure 測試程序` | `Test procedure 測試程序` | `Test procedure 測試程序` | ✓ |
| M | `Expected Result 預期結果` | `Expected Result 預期結果` | `Expected Result 預期結果` | ✓ |
| N | `Specification Reference  規格參考` | `Specification Reference  規格參考` | `Specification Reference  規格參考` | ✓ |
| O | `Test Case Reference ID 測項參考ID` | `Test Case Reference ID 測項參考ID` | `Test Case Reference ID 測項參考ID` | ✓ |
| P | `Estimated Test Time (mins) 預估測試時間 （分鐘）` | `Test Case Priority 測試用例優先級別` | `Test Case Priority 測試用例優先級別` | **✗** |
| Q | `Test Case Priority 測試用例優先級別` | `Estimated Test Time (mins) 預估測試時間 （分鐘）` | `Estimated Test Time (mins) 預估測試時間 （分鐘）` | **✗** |
| R | `Estimated Test Time (mins) 預估測試時間 （分鐘）` | `Test Case Design  Methods 測試用例設計方法` | `Test Case Design  Methods 測試用例設計方法` | **✗** |
| S | `Test Case Design  Methods 測試用例設計方法` | `Functional Safety 功能安全` | `Functional Safety 功能安全` | **✗** |
| T | `Functional Safety 功能安全` | `HDCC27 Atl-Hi` | `HDCC27 Atl-Hi` | **✗** |
| U | `HDCC27 Atl-Hi` | `DT27 Atl-Hi` | `DT27 Atl-Hi` | **✗** |
| V | `DT27 Atl-Hi` | `VF(ProMaster)637 Atl-Mi` | `VF(ProMaster)637 Atl-Mi` | **✗** |
| W | `VF(ProMaster)637 Atl-Mi` | `Commander (598) Atl-Mi` | `Commander (598) Atl-Mi` | **✗** |
| X | `Commander (598) Atl-Mi` | `Regengade (5210) Atl-Mi` | `Regengade (5210) Atl-Mi` | **✗** |
| Y | `Regengade (5210) Atl-Mi` | `Toro(2261) Atl-Mi` | `Toro(2261) Atl-Mi` | **✗** |
| Z | `Toro(2261) Atl-Mi` | `Fastack (376) Atl-Mi` | `Fastack (376) Atl-Mi` | **✗** |
| AA | `Fastack (376) Atl-Mi` | `Test Case Author 測試案例作者` | `Test Case Author 測試案例作者` | **✗** |
| AB | `Test Case Author 測試案例作者` | `Test Version 測試版號` | `Test Version 測試版號` | **✗** |
| AC | `Test Version 測試版號` | `Test Vehicle (Bench) 測試車型(Bench)` | `Test Vehicle (Bench) 測試車型(Bench)` | **✗** |
| AD | `Test Vehicle (Bench) 測試車型(Bench)` | `Test Period 測試期間` | `Test Period 測試期間` | **✗** |
| AE | `Test Period 測試期間` | `Tester 測試者` | `Tester 測試者` | **✗** |
| AF | `Tester 測試者` | `Test Result 測試結果` | `Test Result 測試結果` | **✗** |
| AG | `Test Result 測試結果` | `Defect ID 缺陷ID` | `Defect ID 缺陷ID` | **✗** |
| AH | `Defect ID 缺陷ID` | `Remarks 備註` | `Remarks 備註` | **✗** |
| AI | `Remarks 備註` | — | — | **✗** |

**G52：三者一致之欄 15 / 35。**

- **A–O（15 欄）三者逐字相同。**
- **P 起至末欄（20 欄）Power 與另二者不同 —— 差異形態為「整體右移一格」。**
- **Comfort 與 Privacy 之 r9 完全一致**（34 欄，末欄 `AH` = Remarks）。

## 3. 差異之形態

Power 之 r9 = Comfort / Privacy 之 r9 **於 P 位置插入一欄
`Estimated Test Time (mins) 預估測試時間（分鐘）`**，其後每欄右移一格：

| 語義欄位 | Comfort / Privacy | **Power** | 位移 |
|---|---|---|---|
| Test Case Priority | P | **Q** | +1 |
| Estimated Test Time | Q | **R**（另於 P 多一個同名欄） | +1 |
| Test Case Design Methods | R | **S** | +1 |
| Functional Safety | S | **T** | +1 |
| 七個車型欄 | T–Z | **U–AA** | +1 |
| Test Case Author | AA | **AB** | +1 |
| Remarks | AH | **AI** | +1 |

## 4. G53 —— 兩個 `Estimated Test Time` 之權威（R-P74）

判準（R-P74 指定）：已交付之 Comfort / Privacy 實際填寫哪一欄。

| feature | 資料列 | `Estimated Test Time` 欄 | 非空列數 |
|---|---|---|---|
| Comfort | 466 | Q | **0 / 466** |
| Privacy | 11 | Q | **0 / 11** |

**結論：`Estimated Test Time` 於已交付件中從未被填寫。**

故 Power 之 P 與 R 兩欄之「權威」問題在實務上不存在 —— **二者皆留空**。
語義對應上，Power 之 **R** 對應 Comfort / Privacy 之 Q（同為右移後之原欄），
Power 之 **P** 為新插入者；但因該欄一律不填，此區分不影響寫回。

### 4.1 附帶查得之一項分歧（兩份「已知 good」之間）

| feature | 七個車型欄（Comfort/Privacy 之 T–Z） | 非空列數 |
|---|---|---|
| Comfort | 全部填 `1` | **466 / 466** |
| Privacy | 全部留空 | **0 / 11** |

**兩份已交付件對車型欄之處置相反。** Privacy 之留空符 R30-3 / R30-4；
Comfort 則逐列填 `1`。此分歧與 R-P54（Power 維持留白）直接相關，
於此登記為 **A-PW46**，本包不裁。

## 5. 結論 —— A-PW40 **成立**

Power 之 `workbook.columns` 應為：

```
req_id D / tc_id F / test_group G / test_set H / test_item I /
pre_conditions J / input_test_data K / test_procedure L / expected_result M /
spec_reference N / tc_ref_id O / estimated_time P / priority Q /
（R 為第二個 Estimated Test Time）/ design_method S / functional_safety T /
（U–AA 七個車型欄）/ author AB / remarks AI
```

**scaffold 之原值錯在兩層疊加**：

1. scaffold 記 priority `P` / design_method `Q` / functional_safety `R` / author `Z`
   —— 此為 **A-PV13 / R39-2 訂正之前**的版本。Privacy 已於該條訂正為
   design_method `R` / functional_safety `S` / author `AA`。
   **Power 之 scaffold 從未套用該訂正。**
2. Power 之範本又較 Comfort / Privacy 多插入一欄，其後再右移一格。

二者疊加即為 09 包 B2 所實測之結果。**第二來源佐證取得，A-PW40 成立。**

### 5.1 R-P73 之明確回答

**（a）成立** —— 三者 A–O 一致，差異僅在 P 起之整體位移，
且 Comfort 與 Privacy 二份已交付件互相印證（r9 完全相同）。
錯位者為 scaffold，非 Power 之 workbook。

09 包所填之對應（priority Q / design_method S / functional_safety T /
author AB / remarks AI ＋ `tc_id: F`）**與本次交叉結果完全一致**。
