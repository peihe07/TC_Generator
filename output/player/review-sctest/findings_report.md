# ASPICE SWE.6 Review Findings — FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS025_PlayerFunctions_20260625(done).xlsx

- Sheet: `Test Case Specification&Result`
- Total TCs: 157
- Total Req groups: 83
- Reviewed at: 2026-06-26T09:19:02.908829+00:00

## Batch Summary

- Pass: 134
- Pass with issues: 23
- Fail: 0

> Tier 1：共 83 個 Req group，其中 0 個出現 Critical 拆解問題，5 個無英文 spec句（§6.6）。 Tier 2：0 個 Critical 對齊問題，多集中於 Final Step 工具未讀結果或數值未引用 spec。 Tier 3：25 筆寫作層違規（多為禁用動詞、模糊用語、Design Method 缺漏）。 修正順序建議：先補完 Tier 1 拆解 → 重審 → 再依 Tier 2 / Tier 3 finding 個別調整。

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

### Row 10 · NR1L-Player-001 — verdict: `pass`

### Row 11 · NR1L-Player-002 — verdict: `pass`

### Row 12 · NR1L-Player-003 — verdict: `pass`

### Row 13 · NR1L-Player-004 — verdict: `pass`

### Row 14 · NR1L-Player-005 — verdict: `pass`

### Row 15 · NR1L-Player-006 — verdict: `pass`

### Row 16 · NR1L-Player-007 — verdict: `pass`

### Row 17 · NR1L-Player-008 — verdict: `pass`

### Row 18 · NR1L-Player-009 — verdict: `pass`

### Row 19 · NR1L-Player-010 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 20 · NR1L-Player-011 — verdict: `pass_with_issues`
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員

### Row 21 · NR1L-Player-012 — verdict: `pass`

### Row 22 · NR1L-Player-013 — verdict: `pass`

### Row 23 · NR1L-Player-014 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 24 · NR1L-Player-015 — verdict: `pass`

### Row 25 · NR1L-Player-016 — verdict: `pass`

### Row 26 · NR1L-Player-017 — verdict: `pass`

### Row 27 · NR1L-Player-018 — verdict: `pass`

### Row 28 · NR1L-Player-019 — verdict: `pass`

### Row 29 · NR1L-Player-020 — verdict: `pass`

### Row 30 · NR1L-Player-021 — verdict: `pass`

### Row 31 · NR1L-Player-022 — verdict: `pass`

### Row 32 · NR1L-Player-023 — verdict: `pass`

### Row 33 · NR1L-Player-024 — verdict: `pass`

### Row 34 · NR1L-Player-025 — verdict: `pass`

### Row 35 · NR1L-Player-026 — verdict: `pass`

### Row 36 · NR1L-Player-027 — verdict: `pass`

### Row 37 · NR1L-Player-028 — verdict: `pass_with_issues`
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 38 · NR1L-Player-029 — verdict: `pass`

### Row 39 · NR1L-Player-030 — verdict: `pass`

### Row 40 · NR1L-Player-031 — verdict: `pass`

### Row 41 · NR1L-Player-032 — verdict: `pass`

### Row 42 · NR1L-Player-033 — verdict: `pass`

### Row 43 · NR1L-Player-034 — verdict: `pass`

### Row 44 · NR1L-Player-035 — verdict: `pass`

### Row 45 · NR1L-Player-036 — verdict: `pass`

### Row 46 · NR1L-Player-037 — verdict: `pass`

### Row 47 · NR1L-Player-038 — verdict: `pass`

### Row 48 · NR1L-Player-039 — verdict: `pass`

### Row 49 · NR1L-Player-040 — verdict: `pass`

### Row 50 · NR1L-Player-041 — verdict: `pass`

### Row 51 · NR1L-Player-042 — verdict: `pass`

### Row 52 · NR1L-Player-043 — verdict: `pass`

### Row 53 · NR1L-Player-044 — verdict: `pass`

### Row 54 · NR1L-Player-045 — verdict: `pass`

### Row 55 · NR1L-Player-046 — verdict: `pass`

### Row 56 · NR1L-Player-047 — verdict: `pass`

### Row 57 · NR1L-Player-048 — verdict: `pass`

### Row 58 · NR1L-Player-049 — verdict: `pass`

### Row 59 · NR1L-Player-050 — verdict: `pass`

### Row 60 · NR1L-Player-051 — verdict: `pass`

### Row 61 · NR1L-Player-052 — verdict: `pass`

### Row 62 · NR1L-Player-053 — verdict: `pass`

### Row 63 · NR1L-Player-054 — verdict: `pass`

### Row 64 · NR1L-Player-055 — verdict: `pass`

### Row 65 · NR1L-Player-056 — verdict: `pass`

### Row 66 · NR1L-Player-057 — verdict: `pass`

### Row 67 · NR1L-Player-058 — verdict: `pass`

### Row 68 · NR1L-Player-059 — verdict: `pass`

### Row 69 · NR1L-Player-060 — verdict: `pass`

### Row 70 · NR1L-Player-061 — verdict: `pass`

### Row 71 · NR1L-Player-062 — verdict: `pass`

### Row 72 · NR1L-Player-063 — verdict: `pass`

### Row 73 · NR1L-Player-064 — verdict: `pass`

### Row 74 · NR1L-Player-065 — verdict: `pass`

### Row 75 · NR1L-Player-066 — verdict: `pass`

### Row 76 · NR1L-Player-067 — verdict: `pass`

### Row 77 · NR1L-Player-068 — verdict: `pass`

### Row 78 · NR1L-Player-069 — verdict: `pass`

### Row 79 · NR1L-Player-070 — verdict: `pass`

### Row 80 · NR1L-Player-071 — verdict: `pass`

### Row 81 · NR1L-Player-072 — verdict: `pass`

### Row 82 · NR1L-Player-073 — verdict: `pass`

### Row 83 · NR1L-Player-074 — verdict: `pass`

### Row 84 · NR1L-Player-075 — verdict: `pass`

### Row 85 · NR1L-Player-076 — verdict: `pass`

### Row 86 · NR1L-Player-077 — verdict: `pass`

### Row 87 · NR1L-Player-078 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限

### Row 88 · NR1L-Player-079 — verdict: `pass`

### Row 89 · NR1L-Player-080 — verdict: `pass`

### Row 90 · NR1L-Player-081 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限

### Row 91 · NR1L-Player-082 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限

### Row 92 · NR1L-Player-083 — verdict: `pass`

### Row 93 · NR1L-Player-084 — verdict: `pass`

### Row 94 · NR1L-Player-085 — verdict: `pass`

### Row 95 · NR1L-Player-086 — verdict: `pass`

### Row 96 · NR1L-Player-087 — verdict: `pass`

### Row 97 · NR1L-Player-088 — verdict: `pass`

### Row 98 · NR1L-Player-089 — verdict: `pass`

### Row 99 · NR1L-Player-090 — verdict: `pass`

### Row 100 · NR1L-Player-091 — verdict: `pass`

### Row 101 · NR1L-Player-092 — verdict: `pass`

### Row 102 · NR1L-Player-093 — verdict: `pass`

### Row 103 · NR1L-Player-094 — verdict: `pass`

### Row 104 · NR1L-Player-095 — verdict: `pass`

### Row 105 · NR1L-Player-096 — verdict: `pass`

### Row 106 · NR1L-Player-097 — verdict: `pass`

### Row 107 · NR1L-Player-098 — verdict: `pass`

### Row 108 · NR1L-Player-99 — verdict: `pass`

### Row 109 · NR1L-Player-100 — verdict: `pass`

### Row 110 · NR1L-Player-101 — verdict: `pass`

### Row 111 · NR1L-Player-102 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 112 · NR1L-Player-103 — verdict: `pass`

### Row 113 · NR1L-Player-104 — verdict: `pass`

### Row 114 · NR1L-Player-105 — verdict: `pass`

### Row 115 · NR1L-Player-106 — verdict: `pass`

### Row 116 · NR1L-Player-107 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 117 · NR1L-Player-108 — verdict: `pass`

### Row 118 · NR1L-Player-109 — verdict: `pass`

### Row 119 · NR1L-Player-110 — verdict: `pass`

### Row 120 · NR1L-Player-111 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 121 · NR1L-Player-112 — verdict: `pass`

### Row 122 · NR1L-Player-113 — verdict: `pass`

### Row 123 · NR1L-Player-114 — verdict: `pass`

### Row 124 · NR1L-Player-115 — verdict: `pass`

### Row 125 · NR1L-Player-116 — verdict: `pass`

### Row 126 · NR1L-Player-117 — verdict: `pass`

### Row 127 · NR1L-Player-118 — verdict: `pass`

### Row 128 · NR1L-Player-119 — verdict: `pass`

### Row 129 · NR1L-Player-120 — verdict: `pass`

### Row 130 · NR1L-Player-121 — verdict: `pass`

### Row 131 · NR1L-Player-122 — verdict: `pass`

### Row 132 · NR1L-Player-123 — verdict: `pass`

### Row 133 · NR1L-Player-124 — verdict: `pass`

### Row 134 · NR1L-Player-125 — verdict: `pass`

### Row 135 · NR1L-Player-126 — verdict: `pass`

### Row 136 · NR1L-Player-127 — verdict: `pass`

### Row 137 · NR1L-Player-128 — verdict: `pass`

### Row 138 · NR1L-Player-129 — verdict: `pass`

### Row 139 · NR1L-Player-130 — verdict: `pass`

### Row 140 · NR1L-Player-131 — verdict: `pass`

### Row 141 · NR1L-Player-132 — verdict: `pass`

### Row 142 · NR1L-Player-133 — verdict: `pass`

### Row 143 · NR1L-Player-134 — verdict: `pass`

### Row 144 · NR1L-Player-135 — verdict: `pass`

### Row 145 · NR1L-Player-136 — verdict: `pass`

### Row 146 · NR1L-Player-137 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限

### Row 147 · NR1L-Player-138 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限

### Row 148 · NR1L-Player-139 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限

### Row 149 · NR1L-Player-140 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定

### Row 150 · NR1L-Player-141 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限

### Row 151 · NR1L-Player-142 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）

### Row 152 · NR1L-Player-143 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）

### Row 153 · NR1L-Player-144 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員

### Row 154 · NR1L-Player-145 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）

### Row 155 · NR1L-Player-146 — verdict: `pass`

### Row 156 · NR1L-Player-147 — verdict: `pass`

### Row 157 · NR1L-Player-148 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）

### Row 158 · NR1L-Player-149 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）

### Row 159 · NR1L-Player-150 — verdict: `pass_with_issues`
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員

### Row 160 · NR1L-Player-151 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）

### Row 161 · NR1L-Player-152 — verdict: `pass`

### Row 162 · NR1L-Player-153 — verdict: `pass`

### Row 163 · NR1L-Player-154 — verdict: `pass`

### Row 164 · NR1L-Player-155 — verdict: `pass`

### Row 165 · NR1L-Player-156 — verdict: `pass`

### Row 166 · NR1L-Player-157 — verdict: `pass`
