# ASPICE SWE.6 Review Findings — FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS012_DealerMode_20260417(done).xlsx

- Sheet: `Test Case Specification&Result`
- Total TCs: 125
- Total Req groups: 60
- Reviewed at: 2026-06-26T07:20:06.311813+00:00

## Batch Summary

- Pass: 1
- Pass with issues: 124
- Fail: 0

> Tier 1：共 60 個 Req group，其中 2 個出現 Critical 拆解問題，4 個無英文 spec句（§6.6）。 Tier 2：0 個 Critical 對齊問題，多集中於 Final Step 工具未讀結果或數值未引用 spec。 Tier 3：248 筆寫作層違規（多為禁用動詞、模糊用語、Design Method 缺漏）。 修正順序建議：先補完 Tier 1 拆解 → 重審 → 再依 Tier 2 / Tier 3 finding 個別調整。

## Tier 1 — Per Requirement Findings

### [§6.6] SWE1-DEAL-002 — Major
- Issue: 本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過
- Scope TCs: newR1L-DealerMode-016, newR1L-DealerMode-017, newR1L-DealerMode-018, newR1L-DealerMode-019, newR1L-DealerMode-020
- Suggestion: 從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用

### [§6.6] SWE1-DEAL-003 — Major
- Issue: 本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過
- Scope TCs: newR1L-DealerMode-021, newR1L-DealerMode-022
- Suggestion: 從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用

### [§6.4] SWE1-DEAL-005 — Major
- Issue: 群組內存在 2+ TC 的 Test Item 完全一致，缺少可區分 sibling 的 scenario tag
- Scope TCs: newR1L-DealerMode-027, newR1L-DealerMode-028
- Suggestion: 在 Test Item 加上 scenario tag（例：Cold boot / .mp4 / =limit）讓 sibling 一眼可辨

### [§6.6] SWE1-DEAL-018 — Major
- Issue: 本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過
- Scope TCs: newR1L-DealerMode-056, newR1L-DealerMode-057
- Suggestion: 從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用

### [§6.5] SWE1-DEAL-034-03 — Critical
- Issue: 同 Req group 內多個 TC 引用不同版本的 spec句，Traceability 已斷裂
- Scope TCs: newR1L-DealerMode-113, newR1L-DealerMode-114, newR1L-DealerMode-115
- Suggestion: 確認 canonical 版本並讓所有 TC 對齊；不要自動覆寫，請 reviewer 對應 Polarion / SWRA 確認

### [§6.5] SWE1-DEAL-034-05 — Critical
- Issue: 同 Req group 內多個 TC 引用不同版本的 spec句，Traceability 已斷裂
- Scope TCs: newR1L-DealerMode-117, newR1L-DealerMode-118
- Suggestion: 確認 canonical 版本並讓所有 TC 對齊；不要自動覆寫，請 reviewer 對應 Polarion / SWRA 確認

### [§6.6] SWE1-DEAL-035 — Major
- Issue: 本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過
- Scope TCs: newR1L-DealerMode-119, newR1L-DealerMode-120, newR1L-DealerMode-121, newR1L-DealerMode-122, newR1L-DealerMode-123
- Suggestion: 從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用

## Tier 2 + Tier 3 — Per TC Findings

### Row 10 · newR1L-DealerMode-001 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 11 · newR1L-DealerMode-002 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 12 · newR1L-DealerMode-003 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 13 · newR1L-DealerMode-004 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 14 · newR1L-DealerMode-005 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 15 · newR1L-DealerMode-006 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 16 · newR1L-DealerMode-007 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 17 · newR1L-DealerMode-008 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 18 · newR1L-DealerMode-009 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 19 · newR1L-DealerMode-010 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 20 · newR1L-DealerMode-011 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 21 · newR1L-DealerMode-012 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 22 · newR1L-DealerMode-013 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 23 · newR1L-DealerMode-014 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 24 · newR1L-DealerMode-015 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 25 · newR1L-DealerMode-016 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 26 · newR1L-DealerMode-017 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 27 · newR1L-DealerMode-018 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 28 · newR1L-DealerMode-019 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 29 · newR1L-DealerMode-020 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（20 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 30 · newR1L-DealerMode-021 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 31 · newR1L-DealerMode-022 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 32 · newR1L-DealerMode-023 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 33 · newR1L-DealerMode-024 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 34 · newR1L-DealerMode-025 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 35 · newR1L-DealerMode-026 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 36 · newR1L-DealerMode-027 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（42 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 37 · newR1L-DealerMode-028 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（42 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 38 · newR1L-DealerMode-029 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（16 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 39 · newR1L-DealerMode-030 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（26 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 40 · newR1L-DealerMode-031 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 41 · newR1L-DealerMode-032 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 42 · newR1L-DealerMode-033 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 43 · newR1L-DealerMode-034 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 44 · newR1L-DealerMode-035 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 45 · newR1L-DealerMode-036 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 46 · newR1L-DealerMode-037 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 47 · newR1L-DealerMode-038 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 48 · newR1L-DealerMode-039 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 49 · newR1L-DealerMode-040 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 50 · newR1L-DealerMode-041 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 51 · newR1L-DealerMode-042 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 52 · newR1L-DealerMode-043 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 53 · newR1L-DealerMode-044 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 54 · newR1L-DealerMode-045 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 55 · newR1L-DealerMode-046 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（28 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 56 · newR1L-DealerMode-047 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 57 · newR1L-DealerMode-048 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 58 · newR1L-DealerMode-049 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 59 · newR1L-DealerMode-050 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 60 · newR1L-DealerMode-051 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 61 · newR1L-DealerMode-052 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 62 · newR1L-DealerMode-053 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 63 · newR1L-DealerMode-054 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 64 · newR1L-DealerMode-055 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 65 · newR1L-DealerMode-056 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 66 · newR1L-DealerMode-057 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 67 · newR1L-DealerMode-058 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 68 · newR1L-DealerMode-059 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 69 · newR1L-DealerMode-060 — verdict: `pass_with_issues`
- **[§8.3.3] Major** (test_procedure): Test Procedure 只有 1 個步驟，無法呈現可重現的測試流程
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 70 · newR1L-DealerMode-061 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 71 · newR1L-DealerMode-062 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 72 · newR1L-DealerMode-063 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 73 · newR1L-DealerMode-064 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（17 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 74 · newR1L-DealerMode-065 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（17 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 75 · newR1L-DealerMode-066 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（16 words），超出 14 words / 35 chars 上限
- **[§8.2.1] Major** (pre_conditions): Pre-Condition 含動作動詞（Insert / Press / 插入 / 按下 等），動作應放 Test Procedure
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 76 · newR1L-DealerMode-067 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（16 words），超出 14 words / 35 chars 上限
- **[§8.2.1] Major** (pre_conditions): Pre-Condition 含動作動詞（Insert / Press / 插入 / 按下 等），動作應放 Test Procedure
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 77 · newR1L-DealerMode-068 — verdict: `pass_with_issues`
- **[§8.2.1] Major** (pre_conditions): Pre-Condition 含動作動詞（Insert / Press / 插入 / 按下 等），動作應放 Test Procedure
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 78 · newR1L-DealerMode-069 — verdict: `pass_with_issues`
- **[§8.2.1] Major** (pre_conditions): Pre-Condition 含動作動詞（Insert / Press / 插入 / 按下 等），動作應放 Test Procedure
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 79 · newR1L-DealerMode-070 — verdict: `pass_with_issues`
- **[§8.2.1] Major** (pre_conditions): Pre-Condition 含動作動詞（Insert / Press / 插入 / 按下 等），動作應放 Test Procedure
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 80 · newR1L-DealerMode-071 — verdict: `pass_with_issues`
- **[§8.2.1] Major** (pre_conditions): Pre-Condition 含動作動詞（Insert / Press / 插入 / 按下 等），動作應放 Test Procedure
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 81 · newR1L-DealerMode-072 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 82 · newR1L-DealerMode-073 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 83 · newR1L-DealerMode-074 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 84 · newR1L-DealerMode-075 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 85 · newR1L-DealerMode-076 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 86 · newR1L-DealerMode-077 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 87 · newR1L-DealerMode-078 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（44 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 88 · newR1L-DealerMode-079 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（44 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 89 · newR1L-DealerMode-080 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（44 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 90 · newR1L-DealerMode-081 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（40 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 91 · newR1L-DealerMode-082 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（40 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 92 · newR1L-DealerMode-083 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（40 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 93 · newR1L-DealerMode-084 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（40 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 94 · newR1L-DealerMode-085 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 95 · newR1L-DealerMode-086 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 96 · newR1L-DealerMode-087 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 97 · newR1L-DealerMode-088 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 98 · newR1L-DealerMode-089 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 99 · newR1L-DealerMode-090 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 100 · newR1L-DealerMode-091 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 101 · newR1L-DealerMode-092 — verdict: `pass`

### Row 102 · newR1L-DealerMode-093 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 103 · newR1L-DealerMode-094 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 104 · newR1L-DealerMode-095 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 105 · newR1L-DealerMode-096 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 106 · newR1L-DealerMode-097 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 107 · newR1L-DealerMode-098 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 108 · newR1L-DealerMode-099 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 109 · newR1L-DealerMode-100 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 110 · newR1L-DealerMode-101 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 111 · newR1L-DealerMode-102 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 112 · newR1L-DealerMode-103 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 113 · newR1L-DealerMode-104 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（17 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 114 · newR1L-DealerMode-105 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（17 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 115 · newR1L-DealerMode-106 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（17 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 116 · newR1L-DealerMode-107 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（17 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 117 · newR1L-DealerMode-108 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 118 · newR1L-DealerMode-109 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 119 · newR1L-DealerMode-110 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 120 · newR1L-DealerMode-111 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 121 · newR1L-DealerMode-112 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 122 · newR1L-DealerMode-113 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 123 · newR1L-DealerMode-114 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（17 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 124 · newR1L-DealerMode-115 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（17 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 125 · newR1L-DealerMode-116 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 126 · newR1L-DealerMode-117 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 127 · newR1L-DealerMode-118 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 128 · newR1L-DealerMode-119 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 129 · newR1L-DealerMode-120 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 130 · newR1L-DealerMode-121 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 131 · newR1L-DealerMode-122 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 132 · newR1L-DealerMode-123 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 133 · newR1L-DealerMode-124 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限

### Row 134 · newR1L-DealerMode-125 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
