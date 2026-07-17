# ASPICE SWE.6 Review Findings — sample_mid.xlsx

- Sheet: `Test Case Specification&Result`
- Total TCs: 13
- Total Req groups: 9
- Reviewed at: 2026-06-25T13:05:11.347757+00:00

## Batch Summary

- Pass: 0
- Pass with issues: 13
- Fail: 0

> Tier 1：共 9 個 Req group，其中 5 個出現 Critical 拆解問題，0 個無英文 spec句（§6.6）。 Tier 2：0 個 Critical 對齊問題，多集中於 Final Step 工具未讀結果或數值未引用 spec。 Tier 3：65 筆寫作層違規（多為禁用動詞、模糊用語、Design Method 缺漏）。 修正順序建議：先補完 Tier 1 拆解 → 重審 → 再依 Tier 2 / Tier 3 finding 個別調整。

## Tier 1 — Per Requirement Findings

### [§6.3] SWE1-PLA-027 — Critical
- Issue: 需求規格句列出了所有 Play Controls (Skip Forward/Back, Play/Pause, Repeat, Shuffle, Progress Bar)，但本群僅驗證 Play/Pause 功能，缺少對 Repeat、Shuffle、Skip Forward 的測試覆蓋。
- Scope TCs: NR1L-Player-089, NR1L-Player-090
- Suggestion: 建議依照規格列舉的每一項 Play Control (Skip Forward、Repeat、Shuffle) 補齊對應的 TC，確保全面覆蓋控制項功能測試。

### [§6.1] SWE1-PLA-028 — Critical
- Issue: Req spec句 屬於二元狀態（Play/Pause），但本群組僅有 Play 狀態並顯示 Pause softkey 的正向路徑，缺少 Pause 狀態時不顯示 Pause softkey 的負向驗證。
- Scope TCs: NR1L-Player-091
- Suggestion: 建議補上『音樂暫停狀態不顯示 Pause softkey、應顯示 Play softkey』之負向測試案例，可以根據目前 sibling TC 的格式提供驗證。

### [§6.3] SWE1-PLA-030-01 — Critical
- Issue: Req spec句描述『Repeat All』模式，但依其功能，Repeat 應涵蓋多種模式，現僅測『Repeat All』，未覆蓋其他 Repeat 模式（如 Repeat One、No Repeat），枚舉覆蓋不足。
- Scope TCs: NR1L-Player-094, NR1L-Player-095
- Suggestion: 需新增『Repeat One』與『No Repeat』兩種模式（如適用）之驗證 TC，確保重覆模式轉換完整覆蓋。

### [§6.1] SWE1-PLA-030-02 — Critical
- Issue: Req spec句描述『所有曲目連續播放且循環』，但本群 TC 僅覆蓋正常曲目切換（非末曲→下一首、末曲→首曲），缺乏播放清單僅含單一曲目時是否能循環（單曲所有情境）或播放清單為空（不支援）等負向路徑的驗證。
- Scope TCs: NR1L-Player-096, NR1L-Player-097
- Suggestion: 建議新增負向情境：1. 播放清單只含一首歌時，Repeat All 是否能正確循環切換；2. 播放清單為空時，應無法啟動 Repeat All 模式。

### [§6.1] SWE1-PLA-030-03 — Critical
- Issue: Req spec句為單曲循環播放，但缺乏曲目播放完畢後異常狀態（如媒體未重新啟動或進入暫停）等負向案例驗證。
- Scope TCs: NR1L-Player-098
- Suggestion: 建議新增負向驗證：當單曲播放結束後，若發生未重新播放（如停在結束點或進入暫停），應記錄為不符規。

## Tier 2 + Tier 3 — Per TC Findings

### Row 10 · NR1L-Player-086 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法欄位空白，且操作流程為具體步驟型，不符合預期設計方法規範。

### Row 11 · NR1L-Player-087 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法欄位空白，且流程步驟明顯為使用情境導向，與預期設計方法不一致。

### Row 12 · NR1L-Player-088 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（18 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未填，且此用例為多步驟檢查情境，應標示正確設計邏輯。

### Row 13 · NR1L-Player-089 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 缺少設計方法，且操作為典型情境導向流程，須明確標註。

### Row 14 · NR1L-Player-090 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（15 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法空白且實際步驟具使用案例特性，與設計方法規範不符。

### Row 15 · NR1L-Player-091 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（25 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法欄未填寫，且測試流程屬於典型狀態切換與功能檢查，應根據實際測試內容標註合適設計法（如 Scenario/Use Case），以符合 ASPICE 要求。

### Row 16 · NR1L-Player-092 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法欄未填寫，應依據實際測試步驟明列 Scenario / Use Case 或適用方法。

### Row 17 · NR1L-Player-093 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（25 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法欄未填寫，本 TC 屬於特定狀態驗證，應寫 Scenario / Use Case。

### Row 18 · NR1L-Player-094 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法欄未填，且涉及預設模式驗證，需明確歸屬設計方法。

### Row 19 · NR1L-Player-095 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（19 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法欄未填寫，且測試步驟為流程型操作，應選 Scenario / Use Case。

### Row 20 · NR1L-Player-096 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法為空，且本測試為流程型情境，應標明 Scenario / Use Case。

### Row 21 · NR1L-Player-097 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（29 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法未填寫，且步驟多、包覆流程合理性，應標示為 Scenario / Use Case。

### Row 22 · NR1L-Player-098 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§8.5.2] Major** (design_method): 缺少測試用例設計方法（Design Method）
- **[§8.5.3] Major** (design_method): 設計方法缺漏，test procedure 屬於完整流程，應採 Scenario / Use Case。
