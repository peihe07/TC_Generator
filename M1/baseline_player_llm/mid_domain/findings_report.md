# ASPICE SWE.6 Review Findings — sample_mid.xlsx

- Sheet: `Test Case Specification&Result`
- Total TCs: 13
- Total Req groups: 9
- Reviewed at: 2026-06-25T14:09:22.893497+00:00

## Batch Summary

- Pass: 0
- Pass with issues: 12
- Fail: 1

> Tier 1：共 9 個 Req group，其中 2 個出現 Critical 拆解問題，0 個無英文 spec句（§6.6）。 Tier 2：1 個 Critical 對齊問題，多集中於 Final Step 工具未讀結果或數值未引用 spec。 Tier 3：65 筆寫作層違規（多為禁用動詞、模糊用語、Design Method 缺漏）。 修正順序建議：先補完 Tier 1 拆解 → 重審 → 再依 Tier 2 / Tier 3 finding 個別調整。

## Tier 1 — Per Requirement Findings

### [§6.3] SWE1-PLA-030-01 — Critical
- Issue: Req spec句定義 Repeat mode 為一組列舉（Repeat All、Repeat One Track），但本群組僅有 'Repeat All' 相關 TC，缺少 'Repeat One Track' 覆蓋。
- Scope TCs: NR1L-Player-094, NR1L-Player-095
- Suggestion: 建議補新增針對 Repeat One Track 模式的測試用例，確保該列舉值的行為有被驗證。

### [§6.3] SWE1-PLA-030-02 — Critical
- Issue: Req 權責定義在 CFTS025 §3.1.1.4.2.7，Repeat modes 僅分為『Repeat All』與『Repeat One Track』兩種，但本 Req 群組僅針對 Repeat All 覆蓋，缺少 Repeat One Track 層面的 TC，未涵蓋全部列舉值。
- Scope TCs: NR1L-Player-096, NR1L-Player-097
- Suggestion: 建議新增一組專門驗證 Repeat One Track（或 Repeat Song）模式下行為的測試用例，依 Domain Pack『Repeat modes』定義；需涵蓋『單曲循環』的播放與模式轉換。

## Tier 2 + Tier 3 — Per TC Findings

### Row 10 · NR1L-Player-086 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 未標註測試設計方法，且流程明顯為功能驗證情境，請補上適用設計方法。

### Row 11 · NR1L-Player-087 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 未標註設計方法；本流程明確屬於功能情境驗證。

### Row 12 · NR1L-Player-088 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 未標註設計方法，本用例明顯屬於特殊情境流程（快倒帶搭配無法偵測播放時間）。

### Row 13 · NR1L-Player-089 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 未標註設計方法，且驗證項目屬於情境流程，建議補上。

### Row 14 · NR1L-Player-090 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未填寫，該用例屬於完整流程驗證，應補設計方法。

### Row 15 · NR1L-Player-091 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（25 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未填寫，且本用例為單一驗證情境（未針對邊界或多種列舉值），應為 Scenario / Use Case。

### Row 16 · NR1L-Player-092 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未填寫，且本用例為單一驗證情境，屬於 Scenario / Use Case。

### Row 17 · NR1L-Player-093 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（25 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未填寫，本用例步驟多且屬於一般情境驗證，建議明確填列 Scenario / Use Case。

### Row 18 · NR1L-Player-094 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§7.2] Major** (expected_result): ER 僅驗證 Repeat mode 回到 Repeat All（預設），但未覆蓋 Repeat One Track，缺列舉完整性。
- **[§8.5.3] Major** (design_method): 設計方法未填寫，且只針對 Repeat All 單一驗證，屬 Scenario / Use Case。

### Row 19 · NR1L-Player-095 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§7.2] Major** (expected_result): ER 僅驗證 Repeat All 狀態下到底時自動環迴，未涵蓋 Repeat One Track/切換與單曲重複行為，列舉覆蓋不足。
- **[§8.5.3] Major** (design_method): 設計方法未填寫，本例為情境流程，應為 Scenario / Use Case。

### Row 20 · NR1L-Player-096 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): Test Procedure 為正常流程但 Design Method 未標註，未對應 BVA 或 Scenario。

### Row 21 · NR1L-Player-097 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): Test Procedure 為正常操作但 Design Method 欄位未填，寫法不一致。

### Row 22 · NR1L-Player-098 — verdict: `fail`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§7.1] Critical** (test_item): Test Item 涵蓋『Repeat Song』模式（即 Repeat One Track），但其依附的 Req Spec 為『Repeat All』，功能範圍與 Req spec句不一致，造成追蹤性斷裂。
- **[§8.5.3] Major** (design_method): Test Procedure 為完整步驟操作但 Design Method 欄未填，缺少明確設計標註。
