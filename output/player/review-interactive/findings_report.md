# ASPICE SWE.6 Review Findings — FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS025_PlayerFunctions_20260625(done).xlsx

- Sheet: `Test Case Specification&Result`
- Total TCs: 157
- Total Req groups: 83
- Reviewed at: 2026-06-27T08:10:54.594867+00:00

## Batch Summary

- Pass: 105
- Pass with issues: 47
- Fail: 5

> Tier 1：共 83 個 Req group，其中 24 個出現 Critical 拆解問題，0 個無英文 spec句（§6.6）。 Tier 2：5 個 Critical 對齊問題，多集中於 Final Step 工具未讀結果或數值未引用 spec。 Tier 3：25 筆寫作層違規（多為禁用動詞、模糊用語、Design Method 缺漏）。 修正順序建議：先補完 Tier 1 拆解 → 重審 → 再依 Tier 2 / Tier 3 finding 個別調整。

## Tier 1 — Per Requirement Findings

### [§6.3] SWE1-PLA-001 — Critical
- Issue: 三類 Error popup 僅測 PU0003,缺 PU0024、PU0005。
- Scope TCs: NR1L-Player-001, NR1L-Player-002
- Suggestion: 每 PU 類型各補 TC;PU0005 catch-all 另驗。

### [§6.3] SWE1-PLA-002 — Critical
- Issue: 僅測 PU0024/PU0005,缺 PU0003(No Supported Files)。
- Scope TCs: NR1L-Player-003, NR1L-Player-004, NR1L-Player-005
- Suggestion: 補 PU0003 TC。

### [§6.3] SWE1-PLA-003 — Critical
- Issue: 僅測 PU0005,缺 PU0003、PU0024。
- Scope TCs: NR1L-Player-006, NR1L-Player-007
- Suggestion: 補兩類 popup TC。

### [§6.3] SWE1-PLA-005 — Critical
- Issue: Browse 僅測 Radio/Artist,缺 Folders/Playlists/Songs/Albums/Genre。
- Scope TCs: NR1L-Player-012, NR1L-Player-013, NR1L-Player-014
- Suggestion: 每分類補獨立 TC。

### [§6.3] SWE1-PLA-006 — Critical
- Issue: Repeat 僅測 USB,缺 BTSA、External CD 來源。
- Scope TCs: NR1L-Player-016, NR1L-Player-017, NR1L-Player-018, NR1L-Player-019
- Suggestion: Repeat×來源矩陣補齊。

### [§6.3] SWE1-PLA-007 — Critical
- Issue: Play Controls/Repeat 僅 USB、未分 All/Song 兩模式。
- Scope TCs: NR1L-Player-020, NR1L-Player-021
- Suggestion: 補來源 + Repeat All/Song 各驗。

### [§6.3] SWE1-PLA-010-01 — Critical
- Issue: Shuffle 僅 USB、缺來源切換維持與 CD/AUX/BTSA。
- Scope TCs: NR1L-Player-024, NR1L-Player-025, NR1L-Player-026, NR1L-Player-027, NR1L-Player-028
- Suggestion: Shuffle 狀態×來源補齊。

### [§6.3] SWE1-PLA-015 — Critical
- Issue: 僅 USB folder,缺 DAP 類別瀏覽。
- Scope TCs: NR1L-Player-036, NR1L-Player-037, NR1L-Player-038, NR1L-Player-039, NR1L-Player-040
- Suggestion: 補 DAP category nav TC。

### [§6.3] SWE1-PLA-014-03 — Critical
- Issue: Alphajump 僅測部分字母,缺『存在字元啟用/不存在灰階』完整覆蓋。
- Scope TCs: NR1L-Player-043, NR1L-Player-044, NR1L-Player-045, NR1L-Player-059
- Suggestion: 用已知首字母分布驗全字元。

### [§6.3] SWE1-PLA-014-05 — Critical
- Issue: Alphajump 僅單字元跳轉,缺所有首字母+灰階。
- Scope TCs: NR1L-Player-047, NR1L-Player-048, NR1L-Player-061, NR1L-Player-062
- Suggestion: 補多字元與不可選情境。

### [§6.3] SWE1-PLA-019 — Critical
- Issue: 異常值分別測,缺『同時缺所有資訊』一次全驗(track#=0/time=00:00:00/metadata=Null)。
- Scope TCs: NR1L-Player-067, NR1L-Player-068, NR1L-Player-069, NR1L-Player-070
- Suggestion: 補全缺組合 TC。

### [§6.3] SWE1-PLA-020 — Critical
- Issue: Apple Music 僅測支援裝置,缺不支援裝置情境。
- Scope TCs: NR1L-Player-071, NR1L-Player-072, NR1L-Player-073, NR1L-Player-074, NR1L-Player-075
- Suggestion: 補不支援負向 TC。

### [§6.3] SWE1-PLA-021 — Critical
- Issue: Play Controls 僅 Skip Forward,缺 Skip Back。
- Scope TCs: NR1L-Player-076, NR1L-Player-077
- Suggestion: 補 Skip Back TC。

### [§6.3] SWE1-PLA-027 — Critical
- Issue: 僅 Play/Pause,缺 Repeat/Shuffle/Skip/Progress Bar。
- Scope TCs: NR1L-Player-089, NR1L-Player-090
- Suggestion: 逐子功能補 TC。

### [§6.3] SWE1-PLA-030-01 — Critical
- Issue: 僅 Repeat All,缺 Repeat Song(softkey ON)。
- Scope TCs: NR1L-Player-094, NR1L-Player-095
- Suggestion: 補 Repeat Song TC。

### [§6.3] SWE1-PLA-030-02 — Critical
- Issue: Repeat All 僅 BTSA,缺 USB/CD 來源。
- Scope TCs: NR1L-Player-096, NR1L-Player-097
- Suggestion: 補來源 TC。

### [§6.3] SWE1-PLA-030-03 — Critical
- Issue: Repeat Song 僅 BTSA,缺 USB/CD。
- Scope TCs: NR1L-Player-098
- Suggestion: 補來源 TC。

### [§6.3] SWE1-PLA-033 — Critical
- Issue: 僅測 OFF,缺 Repeat All/Song、Unavailable。
- Scope TCs: NR1L-Player-101
- Suggestion: 補各 Repeat 子態。

### [§6.3] SWE1-PLA-027 — Critical
- Issue: 僅 Shuffle On,缺 Shuffle Off。
- Scope TCs: NR1L-Player-103, NR1L-Player-104
- Suggestion: 補 Shuffle Off TC。

### [§6.3] SWE1-PLA-037 — Critical
- Issue: 僅 OFF,缺 ON、Unavailable。
- Scope TCs: NR1L-Player-106
- Suggestion: 補 Shuffle ON/Unavailable。

### [§6.3] SWE1-PLA-036 — Critical
- Issue: 僅 Unavailable,缺 ON/OFF。
- Scope TCs: NR1L-Player-107
- Suggestion: 補 Shuffle ON/OFF。

### [§6.3] SWE1-PLA-039 — Critical
- Issue: Metadata 僅 Song,缺 Podcast、Audio Book。
- Scope TCs: NR1L-Player-108, NR1L-Player-109, NR1L-Player-110
- Suggestion: 補媒體類型 TC。

### [§6.3] SWE1-PLA-043 — Critical
- Issue: Currently Playing Playlist 缺 External CD、HU AUX 來源。
- Scope TCs: NR1L-Player-116, NR1L-Player-117, NR1L-Player-118, NR1L-Player-119, NR1L-Player-120
- Suggestion: 補來源 TC。

### [§6.3] SWE1-PLA-056 — Critical
- Issue: App icon 移除僅 disable,缺 delete/uninstall 路徑。
- Scope TCs: NR1L-Player-147, NR1L-Player-148
- Suggestion: 補 delete 路徑 TC。

## Tier 2 + Tier 3 — Per TC Findings

### Row 10 · NR1L-Player-001 — verdict: `pass`

### Row 11 · NR1L-Player-002 — verdict: `pass`

### Row 12 · NR1L-Player-003 — verdict: `pass`

### Row 13 · NR1L-Player-004 — verdict: `pass`

### Row 14 · NR1L-Player-005 — verdict: `fail`
- **[§7.1] Critical** (test_item): Test Item 指向 PU0005,但內容對應需求為 PU0024,Req 覆蓋錯誤(traceability)。

### Row 15 · NR1L-Player-006 — verdict: `pass`

### Row 16 · NR1L-Player-007 — verdict: `pass`

### Row 17 · NR1L-Player-008 — verdict: `pass`

### Row 18 · NR1L-Player-009 — verdict: `pass`

### Row 19 · NR1L-Player-010 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 20 · NR1L-Player-011 — verdict: `pass_with_issues`
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員

### Row 21 · NR1L-Player-012 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_procedure): 僅顯示分類名稱,未驗各分類清單內容。

### Row 22 · NR1L-Player-013 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_procedure): 僅操作 Radio Stations,未切換驗證其他分類。

### Row 23 · NR1L-Player-014 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§7.2] Major** (expected_result): ER 僅驗 Artist list,未覆蓋規範其他必需分類。

### Row 24 · NR1L-Player-015 — verdict: `pass`

### Row 25 · NR1L-Player-016 — verdict: `pass`

### Row 26 · NR1L-Player-017 — verdict: `pass`

### Row 27 · NR1L-Player-018 — verdict: `pass`

### Row 28 · NR1L-Player-019 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_procedure): Step6 設 Repeat Song 但未檢查 softkey 顯示 ON。

### Row 29 · NR1L-Player-020 — verdict: `pass`

### Row 30 · NR1L-Player-021 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅驗 Repeat control 選取,未檢查 All/Song 兩模式狀態。

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

### Row 43 · NR1L-Player-034 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): Req 要求選曲後切回 Playing Tab 並關閉 Track window,ER 未覆蓋。

### Row 44 · NR1L-Player-035 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): ER 僅驗 UI 切換,未驗選曲後切回播放畫面且播放選中曲。

### Row 45 · NR1L-Player-036 — verdict: `pass`

### Row 46 · NR1L-Player-037 — verdict: `pass`

### Row 47 · NR1L-Player-038 — verdict: `pass`

### Row 48 · NR1L-Player-039 — verdict: `pass`

### Row 49 · NR1L-Player-040 — verdict: `fail`
- **[§7.6] Critical** (expected_result): ER 驗不支援檔不顯示,但 spec 僅定義顯示支援檔,隱藏未明定。

### Row 50 · NR1L-Player-041 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅述空資料夾不顯示,未列舉每個 selected item 行為。

### Row 51 · NR1L-Player-042 — verdict: `pass`

### Row 52 · NR1L-Player-043 — verdict: `pass`

### Row 53 · NR1L-Player-044 — verdict: `pass`

### Row 54 · NR1L-Player-045 — verdict: `pass`

### Row 55 · NR1L-Player-046 — verdict: `pass`

### Row 56 · NR1L-Player-047 — verdict: `pass`

### Row 57 · NR1L-Player-048 — verdict: `pass`

### Row 58 · NR1L-Player-049 — verdict: `pass`

### Row 59 · NR1L-Player-050 — verdict: `pass`

### Row 60 · NR1L-Player-051 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_procedure): 僅檢查 category 顯示,未驗 select items 行為。

### Row 61 · NR1L-Player-052 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): ER 僅驗顯示 sub-items,未驗選取後操作流程。

### Row 62 · NR1L-Player-053 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): 缺『選取 sub-item 並啟動播放』檢查。

### Row 63 · NR1L-Player-054 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_procedure): 僅驗 unsupported 未顯示,未涵蓋 DB 更新/重讀情境。

### Row 64 · NR1L-Player-055 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_procedure): 僅驗空等級未顯示,未涵蓋 rescan/DB 重整。

### Row 65 · NR1L-Player-056 — verdict: `pass`

### Row 66 · NR1L-Player-057 — verdict: `pass`

### Row 67 · NR1L-Player-058 — verdict: `pass`

### Row 68 · NR1L-Player-059 — verdict: `pass`

### Row 69 · NR1L-Player-060 — verdict: `pass`

### Row 70 · NR1L-Player-061 — verdict: `pass`

### Row 71 · NR1L-Player-062 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): ER 假設 Alphajump 會改變/中斷播放,spec 無此行為。

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

### Row 89 · NR1L-Player-080 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): ER『依 BTSA device behavior 更新』無法對齊具體 spec 結果。

### Row 90 · NR1L-Player-081 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限

### Row 91 · NR1L-Player-082 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限

### Row 92 · NR1L-Player-083 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_procedure): 長按應觸發 Fast Forward + 進度條變化,步驟缺 UI observable。

### Row 93 · NR1L-Player-084 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_procedure): 需驗 Fast Forward 狀態持續 + 滑桿動態更新。

### Row 94 · NR1L-Player-085 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_procedure): 滑桿應於長按結束後跳至新位置,缺明確 observable。

### Row 95 · NR1L-Player-086 — verdict: `pass`

### Row 96 · NR1L-Player-087 — verdict: `pass`

### Row 97 · NR1L-Player-088 — verdict: `pass`

### Row 98 · NR1L-Player-089 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): ER 僅驗 Play softkey 顯示,未驗實際發送 Play 指令並播放。

### Row 99 · NR1L-Player-090 — verdict: `pass`

### Row 100 · NR1L-Player-091 — verdict: `pass`

### Row 101 · NR1L-Player-092 — verdict: `pass`

### Row 102 · NR1L-Player-093 — verdict: `pass`

### Row 103 · NR1L-Player-094 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): ER 僅驗 Repeat All,缺 Repeat Song。

### Row 104 · NR1L-Player-095 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): ER 缺 Repeat Song 單曲循環。

### Row 105 · NR1L-Player-096 — verdict: `pass`

### Row 106 · NR1L-Player-097 — verdict: `pass`

### Row 107 · NR1L-Player-098 — verdict: `pass`

### Row 108 · NR1L-Player-99 — verdict: `pass`

### Row 109 · NR1L-Player-100 — verdict: `pass`

### Row 110 · NR1L-Player-101 — verdict: `pass`

### Row 111 · NR1L-Player-102 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 112 · NR1L-Player-103 — verdict: `pass`

### Row 113 · NR1L-Player-104 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): ER 要求每次隨機序列不同,spec 未要求且不可重現。

### Row 114 · NR1L-Player-105 — verdict: `pass`

### Row 115 · NR1L-Player-106 — verdict: `pass`

### Row 116 · NR1L-Player-107 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 117 · NR1L-Player-108 — verdict: `pass`

### Row 118 · NR1L-Player-109 — verdict: `pass`

### Row 119 · NR1L-Player-110 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_item): spec 未界定 Home vs Playing Tab 差異,可驗證性不足。

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

### Row 136 · NR1L-Player-127 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): ER 未驗 source-specific metadata 優先權顯示。

### Row 137 · NR1L-Player-128 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): 未驗 metadata 缺漏時的 fallback(缺 Song 顯示 Device Name)。

### Row 138 · NR1L-Player-129 — verdict: `pass`

### Row 139 · NR1L-Player-130 — verdict: `pass`

### Row 140 · NR1L-Player-131 — verdict: `pass`

### Row 141 · NR1L-Player-132 — verdict: `pass`

### Row 142 · NR1L-Player-133 — verdict: `pass`

### Row 143 · NR1L-Player-134 — verdict: `pass`

### Row 144 · NR1L-Player-135 — verdict: `pass`

### Row 145 · NR1L-Player-136 — verdict: `fail`
- **[§7.6] Critical** (test_procedure): 步驟用 Page Down 一次一頁,但 spec 為 one row at a time。

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
- **[§7.6] Major** (test_procedure): delete app 後僅檢查部分分頁,未驗所有分頁 icon 不存在。

### Row 159 · NR1L-Player-150 — verdict: `pass_with_issues`
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員

### Row 160 · NR1L-Player-151 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）

### Row 161 · NR1L-Player-152 — verdict: `pass`

### Row 162 · NR1L-Player-153 — verdict: `pass`

### Row 163 · NR1L-Player-154 — verdict: `pass`

### Row 164 · NR1L-Player-155 — verdict: `pass`

### Row 165 · NR1L-Player-156 — verdict: `fail`
- **[§7.6] Critical** (test_item): 僅測登入失敗,缺『已登入來源不跳登入 UI』正向分支。

### Row 166 · NR1L-Player-157 — verdict: `fail`
- **[§7.6] Critical** (test_item): 同上,缺正向二元分支。
