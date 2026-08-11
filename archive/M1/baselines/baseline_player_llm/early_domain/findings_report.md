# ASPICE SWE.6 Review Findings — sample10.xlsx

- Sheet: `Test Case Specification&Result`
- Total TCs: 9
- Total Req groups: 4
- Reviewed at: 2026-06-25T14:19:54.215106+00:00

## Batch Summary

- Pass: 0
- Pass with issues: 9
- Fail: 0

> Tier 1：共 4 個 Req group，其中 4 個出現 Critical 拆解問題，1 個無英文 spec句（§6.6）。 Tier 2：0 個 Critical 對齊問題，多集中於 Final Step 工具未讀結果或數值未引用 spec。 Tier 3：31 筆寫作層違規（多為禁用動詞、模糊用語、Design Method 缺漏）。 修正順序建議：先補完 Tier 1 拆解 → 重審 → 再依 Tier 2 / Tier 3 finding 個別調整。

## Tier 1 — Per Requirement Findings

### [§6.6] SWE1-PLA-004 — Major
- Issue: 本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過
- Scope TCs: NR1L-Player-008, NR1L-Player-009
- Suggestion: 從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用

### [§6.3] SWE1-PLA-001 — Critical
- Issue: Req 規格要求 PU0003 trigger 為「No Supported Files Found」發生時，但現有 TC 僅驗證全部檔案皆為不支援格式情境，未涵蓋其他媒體類型（如 USB-AUX/CD/BTSA）或其他可觸發此 popup 之來源。
- Scope TCs: NR1L-Player-001, NR1L-Player-002
- Suggestion: 依 Domain Pack 『Player sources』枚舉，須於每個支援 source（如 External CD/HU AUX/HU USB/HU BTSA）分別檢驗無支援檔案時系統能彈出 PU0003。建議以同樣邏輯補齊 other sources case。

### [§6.3] SWE1-PLA-002 — Critical
- Issue: Req 規格要求 PU0024 trigger 為『USB Device File Read Error』，現有 TC 皆僅驗證 USB source，未涵蓋所有 Player sources（AUX、CD、BTSA）之讀取異常情境。
- Scope TCs: NR1L-Player-003, NR1L-Player-004
- Suggestion: 應補齊各來源（CD/AUX/BTSA）發生單一檔案讀取錯誤時的顯示行為驗證（如 EX: 在 CD 發生 unreadable track 亦需跳出 PU0024）。

### [§6.3] SWE1-PLA-003 — Critical
- Issue: Req 規格規定 PU0005 generic error 須涵蓋所有來源與情境，現有 TC 僅針對 USB source 驗證，未涵蓋所有支援來源 (如 CD/AUX/BTSA)。
- Scope TCs: NR1L-Player-005
- Suggestion: 請於各 Player source (CD/AUX/BTSA) 分別建構造成 generic error（非 PU0003/PU0024 情境）之情形以驗證 PU0005 Popup 行為。

### [§6.3] SWE1-PLA-003 — Critical
- Issue: Req 為所有錯誤未被上層覆蓋時都需顯示 PU0005，但目前僅測試 USB 發生錯誤時的Popup，未覆蓋 Player subgroup 其它來源 (External CD、HU AUX、HU BTSA) 發生同類錯誤時之行為。
- Scope TCs: NR1L-Player-006, NR1L-Player-007
- Suggestion: 建議為 External CD、HU AUX、HU BTSA 三個來源各補一組發生未明確定義錯誤時顯示 PU0005 的測試用例。

## Tier 2 + Tier 3 — Per TC Findings

### Row 10 · NR1L-Player-001 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未標示，且本 TC 屬於典型異常情境驗證，建議補充為 Error-Handling 或 Enumeration。

### Row 11 · NR1L-Player-002 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未標示，該 TC 係針對異常訊息及格式比對，應標註為 Enumeration/Message Verification。

### Row 12 · NR1L-Player-003 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未標示，本用例為異常情境之來源覆蓋，建議註明 Boundary & Error-Handling。

### Row 13 · NR1L-Player-004 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（24 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 未標註設計方法，且本測試屬於錯誤訊息提示細項驗證，建議標註為 Enumeration/Message Verification。

### Row 14 · NR1L-Player-005 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（33 words），超出 14 words / 35 chars 上限
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未標註，且用例針對所有 generic error case，建議補標記為 Enumeration / Error-Handling。

### Row 15 · NR1L-Player-006 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（33 words），超出 14 words / 35 chars 上限
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法缺少與測試步驟形式一致性，TC以標準流程驗證 Popup 行為但未標註 Design Method。

### Row 16 · NR1L-Player-007 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（33 words），超出 14 words / 35 chars 上限
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未標註，流程性驗證且測試步驟與規格貼合，應標記設計方法。

### Row 17 · NR1L-Player-008 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 未標註設計方法，該用例屬流程驗證且步驟明確。

### Row 18 · NR1L-Player-009 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 未提供設計方法分類，該測試是步驟型流程驗證。
