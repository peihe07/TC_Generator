# ASPICE SWE.6 Review Findings — sample10.xlsx

- Sheet: `Test Case Specification&Result`
- Total TCs: 9
- Total Req groups: 4
- Reviewed at: 2026-06-25T13:03:40.006341+00:00

## Batch Summary

- Pass: 0
- Pass with issues: 9
- Fail: 0

> Tier 1：共 4 個 Req group，其中 1 個出現 Critical 拆解問題，1 個無英文 spec句（§6.6）。 Tier 2：0 個 Critical 對齊問題，多集中於 Final Step 工具未讀結果或數值未引用 spec。 Tier 3：28 筆寫作層違規（多為禁用動詞、模糊用語、Design Method 缺漏）。 修正順序建議：先補完 Tier 1 拆解 → 重審 → 再依 Tier 2 / Tier 3 finding 個別調整。

## Tier 1 — Per Requirement Findings

### [§6.6] SWE1-PLA-004 — Major
- Issue: 本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過
- Scope TCs: NR1L-Player-008, NR1L-Player-009
- Suggestion: 從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用

### [§6.3] SWE1-PLA-001 — Critical
- Issue: Req 為所有不支援的檔案格式需顯示錯誤訊息，但本群組僅針對 .txt 與 .pdf 測試，少測試其他常見未支援格式例如 .exe、.apk、亂碼副檔名等，無法證明全面覆蓋。
- Scope TCs: NR1L-Player-001, NR1L-Player-002
- Suggestion: 請新增 TC 覆蓋更多種類的不支援檔案格式，例如 .exe、.apk、無法辨識的副檔名等，以完善枚舉覆蓋。

## Tier 2 + Tier 3 — Per TC Findings

### Row 10 · NR1L-Player-001 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法缺漏，且流程屬於條件驗證與錯誤分支，不應空白。

### Row 11 · NR1L-Player-002 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法欄位缺漏，條件覆蓋應標註設計思路。

### Row 12 · NR1L-Player-003 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未填，流程已達 6 步，應有明確檢驗思路。

### Row 13 · NR1L-Player-004 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未註明，流程為錯誤分支驗證應標註 Scenario。

### Row 14 · NR1L-Player-005 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（33 words），超出 14 words / 35 chars 上限
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未設定，複合條件判斷建議標註實際設計方法。

### Row 15 · NR1L-Player-006 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（33 words），超出 14 words / 35 chars 上限
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 16 · NR1L-Player-007 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（33 words），超出 14 words / 35 chars 上限
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§7.2] Major** (expected_result): ER 部分未涵蓋 Req 中提及的錯誤訊息格式（"(Device Name) error"），僅驗證 popup 是否持續顯示未及細節。

### Row 17 · NR1L-Player-008 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.4.2] Major** (expected_result): Expected Result 步驟數與 Test Procedure 不一致，無法 1:1 對應，可能造成驗證漏失或混淆。

### Row 18 · NR1L-Player-009 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
