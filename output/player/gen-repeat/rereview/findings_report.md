# ASPICE SWE.6 Review Findings — generated_tcs.xlsx

- Sheet: `Test Case Specification&Result`
- Total TCs: 8
- Total Req groups: 6
- Reviewed at: 2026-06-28T04:57:38.981480+00:00

## Batch Summary

- Pass: 5
- Pass with issues: 3
- Fail: 0

> Tier 1：共 6 個 Req group，其中 2 個出現 Critical 拆解問題，0 個無英文 spec句（§6.6）。 Tier 2：0 個 Critical 對齊問題，多集中於 Final Step 工具未讀結果或數值未引用 spec。 Tier 3：6 筆寫作層違規（多為禁用動詞、模糊用語、Design Method 缺漏）。 修正順序建議：先補完 Tier 1 拆解 → 重審 → 再依 Tier 2 / Tier 3 finding 個別調整。

## Tier 1 — Per Requirement Findings

### [§6.5] SWE1-PLA-032 — Critical
- Issue: 同 Req group 內多個 TC 引用不同版本的 spec句，Traceability 已斷裂
- Scope TCs: GEN-0004, GEN-0005
- Suggestion: 確認 canonical 版本並讓所有 TC 對齊；不要自動覆寫，請 reviewer 對應 Polarion / SWRA 確認

### [§6.5] SWE1-PLA-033 — Critical
- Issue: 同 Req group 內多個 TC 引用不同版本的 spec句，Traceability 已斷裂
- Scope TCs: GEN-0006, GEN-0007
- Suggestion: 確認 canonical 版本並讓所有 TC 對齊；不要自動覆寫，請 reviewer 對應 Polarion / SWRA 確認

## Tier 2 + Tier 3 — Per TC Findings

### Row 10 · GEN-0001 — verdict: `pass`

### Row 11 · GEN-0002 — verdict: `pass`

### Row 12 · GEN-0003 — verdict: `pass`

### Row 13 · GEN-0004 — verdict: `pass_with_issues`
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員

### Row 14 · GEN-0005 — verdict: `pass`

### Row 15 · GEN-0006 — verdict: `pass_with_issues`
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員

### Row 16 · GEN-0007 — verdict: `pass`

### Row 17 · GEN-0008 — verdict: `pass_with_issues`
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
