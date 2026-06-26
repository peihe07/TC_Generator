# ASPICE SWE.6 Review Findings — FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS025_PlayerFunctions_20260625(done).xlsx

- Sheet: `Test Case Specification&Result`
- Total TCs: 157
- Total Req groups: 83
- Reviewed at: 2026-06-26T08:23:18.937753+00:00

## Batch Summary

- Pass: 0
- Pass with issues: 157
- Fail: 0

> Tier 1：共 83 個 Req group，其中 0 個出現 Critical 拆解問題，5 個無英文 spec句（§6.6）。 Tier 2：0 個 Critical 對齊問題，多集中於 Final Step 工具未讀結果或數值未引用 spec。 Tier 3：525 筆寫作層違規（多為禁用動詞、模糊用語、Design Method 缺漏）。 修正順序建議：先補完 Tier 1 拆解 → 重審 → 再依 Tier 2 / Tier 3 finding 個別調整。

## Tier 1 — Per Requirement Findings

### [§6.6] SWE1-PLA-004 — Major
- Issue: 本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過
- Scope TCs: NR1L-Player-008, NR1L-Player-009, NR1L-Player-010, NR1L-Player-011
- Suggestion: 從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用

### [§6.6] SWE1-PLA-022 — Major
- Issue: 本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過
- Scope TCs: NR1L-Player-078
- Suggestion: 從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用

### [§6.6] SWE1-PLA-024-01 — Major
- Issue: 本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過
- Scope TCs: NR1L-Player-081
- Suggestion: 從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用

### [§6.6] SWE1-PLA-024-02 — Major
- Issue: 本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過
- Scope TCs: NR1L-Player-082
- Suggestion: 從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用

### [§6.6] SWE1-PLA-052 — Major
- Issue: 本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過
- Scope TCs: NR1L-Player-137, NR1L-Player-138, NR1L-Player-139, NR1L-Player-140, NR1L-Player-141
- Suggestion: 從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用

## Tier 2 + Tier 3 — Per TC Findings

### Row 10 · NR1L-Player-001 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 11 · NR1L-Player-002 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 12 · NR1L-Player-003 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 13 · NR1L-Player-004 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 14 · NR1L-Player-005 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（33 words），超出 14 words / 35 chars 上限
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 15 · NR1L-Player-006 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（33 words），超出 14 words / 35 chars 上限
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 16 · NR1L-Player-007 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（33 words），超出 14 words / 35 chars 上限
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 17 · NR1L-Player-008 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 18 · NR1L-Player-009 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 19 · NR1L-Player-010 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 20 · NR1L-Player-011 — verdict: `pass_with_issues`
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 21 · NR1L-Player-012 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 22 · NR1L-Player-013 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 23 · NR1L-Player-014 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 24 · NR1L-Player-015 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（21 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 25 · NR1L-Player-016 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（21 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 26 · NR1L-Player-017 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（31 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 27 · NR1L-Player-018 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（31 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 28 · NR1L-Player-019 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（28 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 29 · NR1L-Player-020 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（16 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 30 · NR1L-Player-021 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（16 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 31 · NR1L-Player-022 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（17 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 32 · NR1L-Player-023 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 33 · NR1L-Player-024 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 34 · NR1L-Player-025 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 35 · NR1L-Player-026 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 36 · NR1L-Player-027 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 37 · NR1L-Player-028 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（21 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 38 · NR1L-Player-029 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 39 · NR1L-Player-030 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 40 · NR1L-Player-031 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 41 · NR1L-Player-032 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（16 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 42 · NR1L-Player-033 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（16 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 43 · NR1L-Player-034 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 44 · NR1L-Player-035 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 45 · NR1L-Player-036 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 46 · NR1L-Player-037 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 47 · NR1L-Player-038 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 48 · NR1L-Player-039 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 49 · NR1L-Player-040 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 50 · NR1L-Player-041 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 51 · NR1L-Player-042 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 52 · NR1L-Player-043 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 53 · NR1L-Player-044 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（21 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 54 · NR1L-Player-045 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（21 words），超出 14 words / 35 chars 上限
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 55 · NR1L-Player-046 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（16 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 56 · NR1L-Player-047 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（27 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 57 · NR1L-Player-048 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（27 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 58 · NR1L-Player-049 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 59 · NR1L-Player-050 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 60 · NR1L-Player-051 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 61 · NR1L-Player-052 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 62 · NR1L-Player-053 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 63 · NR1L-Player-054 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 64 · NR1L-Player-055 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 65 · NR1L-Player-056 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 66 · NR1L-Player-057 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 67 · NR1L-Player-058 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 68 · NR1L-Player-059 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（21 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 69 · NR1L-Player-060 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（16 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 70 · NR1L-Player-061 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（27 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 71 · NR1L-Player-062 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（27 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 72 · NR1L-Player-063 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（37 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 73 · NR1L-Player-064 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（37 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 74 · NR1L-Player-065 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（21 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 75 · NR1L-Player-066 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（27 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 76 · NR1L-Player-067 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（72 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 77 · NR1L-Player-068 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（72 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 78 · NR1L-Player-069 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（72 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 79 · NR1L-Player-070 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（72 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 80 · NR1L-Player-071 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 81 · NR1L-Player-072 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 82 · NR1L-Player-073 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 83 · NR1L-Player-074 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 84 · NR1L-Player-075 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 85 · NR1L-Player-076 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 86 · NR1L-Player-077 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 87 · NR1L-Player-078 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 88 · NR1L-Player-079 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 89 · NR1L-Player-080 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 90 · NR1L-Player-081 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 91 · NR1L-Player-082 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 92 · NR1L-Player-083 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 93 · NR1L-Player-084 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 94 · NR1L-Player-085 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 95 · NR1L-Player-086 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 96 · NR1L-Player-087 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 97 · NR1L-Player-088 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 98 · NR1L-Player-089 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 99 · NR1L-Player-090 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 100 · NR1L-Player-091 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（25 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 101 · NR1L-Player-092 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 102 · NR1L-Player-093 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（25 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 103 · NR1L-Player-094 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 104 · NR1L-Player-095 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 105 · NR1L-Player-096 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 106 · NR1L-Player-097 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 107 · NR1L-Player-098 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 108 · NR1L-Player-99 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 109 · NR1L-Player-100 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 110 · NR1L-Player-101 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 111 · NR1L-Player-102 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 112 · NR1L-Player-103 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 113 · NR1L-Player-104 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 114 · NR1L-Player-105 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 115 · NR1L-Player-106 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 116 · NR1L-Player-107 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 117 · NR1L-Player-108 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 118 · NR1L-Player-109 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 119 · NR1L-Player-110 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 120 · NR1L-Player-111 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（30 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 121 · NR1L-Player-112 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 122 · NR1L-Player-113 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（31 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 123 · NR1L-Player-114 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 124 · NR1L-Player-115 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 125 · NR1L-Player-116 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 126 · NR1L-Player-117 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 127 · NR1L-Player-118 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 128 · NR1L-Player-119 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 129 · NR1L-Player-120 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 130 · NR1L-Player-121 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（67 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 131 · NR1L-Player-122 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（67 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 132 · NR1L-Player-123 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（67 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 133 · NR1L-Player-124 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 134 · NR1L-Player-125 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 135 · NR1L-Player-126 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（21 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 136 · NR1L-Player-127 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 137 · NR1L-Player-128 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 138 · NR1L-Player-129 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 139 · NR1L-Player-130 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 140 · NR1L-Player-131 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 141 · NR1L-Player-132 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 142 · NR1L-Player-133 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（37 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 143 · NR1L-Player-134 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（37 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 144 · NR1L-Player-135 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（39 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 145 · NR1L-Player-136 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（39 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 146 · NR1L-Player-137 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 147 · NR1L-Player-138 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 148 · NR1L-Player-139 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 149 · NR1L-Player-140 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 150 · NR1L-Player-141 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 151 · NR1L-Player-142 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 152 · NR1L-Player-143 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 153 · NR1L-Player-144 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 154 · NR1L-Player-145 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 155 · NR1L-Player-146 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（16 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 156 · NR1L-Player-147 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（17 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 157 · NR1L-Player-148 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 158 · NR1L-Player-149 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 159 · NR1L-Player-150 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（17 words），超出 14 words / 35 chars 上限
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 160 · NR1L-Player-151 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（27 words），超出 14 words / 35 chars 上限
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 161 · NR1L-Player-152 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（28 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 162 · NR1L-Player-153 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 163 · NR1L-Player-154 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 164 · NR1L-Player-155 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（30 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 165 · NR1L-Player-156 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（30 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）

### Row 166 · NR1L-Player-157 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（30 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
