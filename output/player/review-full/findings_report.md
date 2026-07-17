# ASPICE SWE.6 Review Findings — FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS025_PlayerFunctions_20260625(done).xlsx

- Sheet: `Test Case Specification&Result`
- Total TCs: 157
- Total Req groups: 83
- Reviewed at: 2026-06-27T07:05:12.140326+00:00

## Batch Summary

- Pass: 80
- Pass with issues: 65
- Fail: 12

> Tier 1：共 83 個 Req group，其中 32 個出現 Critical 拆解問題，0 個無英文 spec句（§6.6）。 Tier 2：12 個 Critical 對齊問題，多集中於 Final Step 工具未讀結果或數值未引用 spec。 Tier 3：26 筆寫作層違規（多為禁用動詞、模糊用語、Design Method 缺漏）。 修正順序建議：先補完 Tier 1 拆解 → 重審 → 再依 Tier 2 / Tier 3 finding 個別調整。

## Tier 1 — Per Requirement Findings

### [§6.3] SWE1-PLA-001 — Critical
- Issue: Req 明確定義 3 種錯誤類型（No Supported Files Found, USB Device File Read Error, 其他錯誤為 Generic Error），但僅有 PU0003 測試用例，缺少 PU0024 及 PU0005 相關測試，enumeration 覆蓋不全。
- Scope TCs: NR1L-Player-001, NR1L-Player-002
- Suggestion: 請分別補充 USB Device File Read Error（PU0024）、Generic Error（PU0005） 的異常彈窗測試用例或將其關聯至正確需求。

### [§6.3] SWE1-PLA-002 — Critical
- Issue: Req 定義三種 Pop Up 類型，但僅測試 PU0024，缺少 PU0003 (No Supported Files Found) 及 PU0005 (Generic Error) 測試，enumeration 覆蓋不足。
- Scope TCs: NR1L-Player-003, NR1L-Player-004
- Suggestion: 請補齊 No Supported Files Found（PU0003）、Generic Error（PU0005）相關錯誤類型測試用例，確保三種異常皆有驗證。

### [§6.3] SWE1-PLA-003 — Critical
- Issue: Req 指定 Generic Error (PU0005) 為 catch-all，但僅測試 Generic Error，缺少 PU0003（No Supported Files Found）及 PU0024 (File Read Error) 等其他錯誤彈窗驗證，enumeration 覆蓋不全。
- Scope TCs: NR1L-Player-005
- Suggestion: 建議補齊 PU0003、PU0024 該類相關異常彈窗的測試用例。

### [§6.3] SWE1-PLA-004 — Critical
- Issue: Req spec句『the only controls available are the Source Tab and Audio Tab, all other buttons will be greyed out』明確列出 AUX 模式下所有播放控制應不可用，實做 TC 僅覆蓋 Source Tab、Audio Tab、Browse Tab、Tune Knob，尚缺如 Seek/Shuffle/Repeat/其他（如曲目選單）控制未覆蓋 greyed out 狀態。
- Scope TCs: NR1L-Player-008, NR1L-Player-009, NR1L-Player-010
- Suggestion: 應依各 Source Control 功能（如 Seek up/down、Repeat、Shuffle、Track List）逐一撰寫負向 TC 驗證：在 AUX 模式下按下這些控制時，均為灰階且無作用。

### [§6.3] SWE1-PLA-005 — Critical
- Issue: Req spec句要求 Apple Music Radio Stations 在 USB、BT 與 CarPlay 皆須支援瀏覽，目前群組內僅驗證 USB 來源，缺少 BT 與 CarPlay 覆蓋。
- Scope TCs: NR1L-Player-012, NR1L-Player-013, NR1L-Player-014
- Suggestion: 建議另新增針對 BT 與 CarPlay 的 Apple Music Radio Stations browse 行為之測項，確保列舉覆蓋完整。

### [§6.3] SWE1-PLA-006-01, SWE1-PLA-006-02, SWE1-PLA-006-03 — Critical
- Issue: Repeat 模式需求僅拆出 Repeat All（預設）、Repeat Song 兩態，各自描述 List 結束播放行為，但未明確覆蓋所有 Repeat 枚舉值(Repeat All、Repeat Song)下的所有 edge 步驟，尤其缺少非最後曲目在 Repeat Song 下的處理。
- Scope TCs: NR1L-Player-016, NR1L-Player-017, NR1L-Player-018, NR1L-Player-019
- Suggestion: 建議再檢查 Repeat Song 態時，是否有涵蓋『非最後曲目播放完畢後是否正確重播同一首』的情境測試，並於 TCs 補齊對應覆蓋。

### [§6.3] SWE1-PLA-007 — Critical
- Issue: Req spec句及 Domain Pack 定義 Repeat 為 All 與 Song 兩種狀態，但本 Req group 僅測試 Repeat 功能是否可控，未分別覆蓋 'Repeat All' 與 'Repeat Song' 狀態。
- Scope TCs: NR1L-Player-021
- Suggestion: 建議拆分並新增兩個覆蓋 Repeat All 與 Repeat Song 狀態下的 TC，確保兩種模式皆有驗證。

### [§6.1] SWE1-PLA-011 — Critical
- Issue: Req spec句 提到『display/not display additional metadata』的正反兩條路徑，但本群組僅測試有 metadata 的檔案，缺少『無 metadata』狀況下的負向測試用例。
- Scope TCs: NR1L-Player-029, NR1L-Player-030
- Suggestion: 建議擴充測試用例，加入 1 個『currently playing file 沒有任何 metadata』時，Info 功能未顯示 (或顯示預設/空資料) 的負向情境。

### [§6.3] SWE1-PLA-014-03 — Critical
- Issue: Req spec句『啟用僅有對應清單首字母的按鍵』涉及枚舉「只啟用清單首字母存在的字元」，但現有 TCs 僅檢查特定存在和完全不存在情境，未覆蓋如只有單一首字母、多元字母等 Intelligent Character Filtering boundary。
- Scope TCs: NR1L-Player-043, NR1L-Player-044, NR1L-Player-045
- Suggestion: 建議新增 TC 檢查：僅有 A 開頭歌曲時，僅 A 啟用、其餘禁用；有 A、C、D 開頭時，僅 A、C、D 啟用；若有空清單也須檢查所有停用狀態。

### [§6.1] SWE1-PLA-014-05 — Critical
- Issue: Req spec句涉及『選擇字母→重定位』的二元行為，但僅驗證有效選擇，缺少無法選擇（不可用字母/disabled 字元）的負向情境測試。
- Scope TCs: NR1L-Player-047, NR1L-Player-048
- Suggestion: 建議新增用例驗證：按下無對應任何項目的字元時 Alphajump softkey 為灰階不可選，且無任何動作發生。

### [§6.3] SWE1-PLA-014-03 — Critical
- Issue: Spec句及領域定義明確指出 Alphajump 畫面僅啟用『存在於目前清單首字母的字元』，本 TC 僅以範例 A/C/D 作檢查，未完整覆蓋所有可能首字母組合。
- Scope TCs: NR1L-Player-059
- Suggestion: 建議增補至少兩個額外的 TC：一、僅有 1 個首字母（如全部曲目均以 Z 開頭時）；二、多組散佈(非連續字母)情境，確保未在清單首的字符一律 disabled。

### [§6.3] SWE1-PLA-014-05 — Critical
- Issue: Req spec句需覆蓋所有 Alphajump 字母子集情形，但本群組僅以『多於一個項目的字母』為例，未驗證僅有一個項目或該字母不存在於清單的情境，且未驗證 Intelligent Character Filtering 邊界。
- Scope TCs: NR1L-Player-061, NR1L-Player-062
- Suggestion: 建議增加以下情境的 TC：1. Alphajump 清單中不存在選定字母時是否允許選取/呈現 (Intelligent Character Filtering)；2. 僅有一個項目的字母情形；3. 非合法/灰階字母無法被選取。另可參考 Domain Pack: name: Alphajump 字元 | enum: ['只啟用清單首字母存在的字元'] 驗證過濾邏輯。

### [§6.3] SWE1-PLA-019 — Critical
- Issue: Req spec句明確列出『Current, First and Last track #s』『Play Time Position』『File Metadata』三類資料缺失時的顯示行為，現有 TCs 僅各自覆蓋單一資料型態，未針對『所有資料皆同時缺失』的情境建立 TC，Enumeration 涵蓋不全。
- Scope TCs: NR1L-Player-067, NR1L-Player-068, NR1L-Player-069, NR1L-Player-070
- Suggestion: 建議新增一筆 TC，針對 BTSA 裝置完全不提供檔案編號、播放時間與檔案中繼資料，同時驗證三類顯示行為（曲號=0、播放時間=0:00:00、Metadata 欄位為 null/unknown）是否正確。

### [§6.3] SWE1-PLA-020 — Critical
- Issue: Req spec句要求 Apple Music Radio station 必須可於 USB、BT 和 CarPlay 連線下瀏覽，但本群組 TC 僅覆蓋 Apple device 連線成功的正常流程，未驗證裝置不支援 Apple Music Radio 或其他類型裝置的情境，且對於 Apple Music Radio station 內的 Playlist、Genre、Artist、Songs 等子分類項目未逐一覆蓋所有 enumeration。
- Scope TCs: NR1L-Player-071, NR1L-Player-072, NR1L-Player-073, NR1L-Player-074, NR1L-Player-075
- Suggestion: 建議依照 Apple Music Radio station 可瀏覽的所有情境進行 enumeration 覆蓋，包含各 connection type（USB、BT、CarPlay）下 Apple device 與不同支援狀態裝置、以及 Apple Music Radio station 的 Playlist、Genre、Artist、Songs、Album 等各子項目。另補上『Apple device 不支援 Music Radio 情境下 Browse 不顯示音樂電台』的負向測試。

### [§6.3] SWE1-PLA-021 — Critical
- Issue: Req spec句 (PC1.1) 明列所有 Play Controls 功能 (Skip Forward/Skip Back, Play/Pause, Repeat, Shuffle, Progress Bar)，但本 Req 群組僅涵蓋 Skip Forward/Skip Back，未覆蓋 Play/Pause、Repeat、Shuffle、Progress Bar。
- Scope TCs: NR1L-Player-076, NR1L-Player-077, NR1L-Player-079, NR1L-Player-080
- Suggestion: 應補齊 Play Controls 所有子功能之測試用例，建議針對 Play/Pause, Repeat, Shuffle, 以及 Progress Bar 各自新增一組 TC。

### [§6.1] SWE1-PLA-024-02 — Critical
- Issue: 根據需求 Skip Back (SWE1-PLA-024-02) 的規格句，Skip Back 行為需同時涵蓋『小於3秒時回前一曲』與『大於3秒時回本曲起頭』的二元邏輯，但現有 TC 僅驗證 3 秒界線兩側行為，缺少 3 秒整時的邊界情境。
- Scope TCs: NR1L-Player-081, NR1L-Player-082
- Suggestion: 建議新增邊界 TC，專門驗證 Skip Back 發生於『剛好 3 秒』時，預期播放行為是否落在規格定義的其中之一，確認產品實作無歧義。

### [§6.3] SWE1-PLA-027 — Critical
- Issue: Req spec句中 Play Controls 為多項組合功能（Skip Forward/Skip Back, Play/Pause, Repeat, Shuffle, Progress Bar），但本 Req group 僅針對 Play/Pause 進行驗證，未覆蓋其餘控制項。
- Scope TCs: NR1L-Player-089, NR1L-Player-090
- Suggestion: 建議補充針對 Skip Forward、Skip Back、Repeat、Shuffle、Progress Bar 之個別控制驗證的測試案例，確保每一功能皆有覆蓋。

### [§6.3] SWE1-PLA-030-01 — Critical
- Issue: Req 明確限制 Repeat mode 僅有 'Repeat All' 及 'Repeat Song' 兩種狀態，但本 Req group 只驗證了 Repeat All，缺少 Repeat Song 的覆蓋測試。
- Scope TCs: NR1L-Player-094, NR1L-Player-095
- Suggestion: 建議新增一筆針對 Repeat Song (標籤顯示『Repeat Song』，功能切換與邏輯) 的 TC，以完整覆蓋所有 Repeat mode。

### [§6.3] SWE1-PLA-030-02 — Critical
- Issue: Req 已明確規定 Repeat 功能必須支援 'Repeat All' 與 'Repeat Song' 兩種模式，但本群組僅包含 Repeat All 模式覆蓋，缺少對 Repeat Song 模式下的完整覆蓋，未驗證所有列舉值。
- Scope TCs: NR1L-Player-096, NR1L-Player-097
- Suggestion: 建議新增專屬於 'Repeat Song' 模式的 TC，驗證 HU 是否正確執行只重複單一曲目播放的行為，同時再確認 'Repeat Song' 狀態下 UI 顯示符合要求。

### [§6.3] SWE1-PLA-033 — Critical
- Issue: Req spec句涉及 Repeat mode，但本群組僅有 Repeat OFF 狀態的覆蓋，未覆蓋 Repeat Song 及 Repeat All 兩個有效模式，缺少完整 Repeat mode 枚舉案例。
- Scope TCs: NR1L-Player-101
- Suggestion: 請補齊：Repeat Song 與 Repeat All 狀態的 test case，確保所有 Repeat mode 被測試。

### [§6.3] SWE1-PLA-034 — Critical
- Issue: Repeat 功能於 BTSA 異常 (不可用/unavailable) 狀態才有覆蓋，但未覆蓋其他有效模式 (Repeat All, Repeat Song)，導致枚舉缺口。
- Scope TCs: NR1L-Player-102
- Suggestion: 補充 Repeat All 及 Repeat Song 狀態的測試案例(已於 domain 枚舉內定義所有 Repeat mode)，以完整 cover 枚舉情境。

### [§6.3] SWE1-PLA-043 — Critical
- Issue: Req spec句符合支援媒體來源與不支援來源兩類，但現有TC未明確涵蓋所有 Player sources 枚舉類型(USB, SD-Card, BTSA, MTP, 及 unsupported source)。
- Scope TCs: NR1L-Player-114, NR1L-Player-115
- Suggestion: 請補足 USB、SD-Card、BTSA、MTP 各來源皆有『支援』與『不支援』範例，特別標註不支援的來源種類（目前 test_item 僅以 supported/unsupported 模糊表達，應依枚舉列舉所有來源）。

### [§6.3] SWE1-PLA-043 — Critical
- Issue: Req spec句要求顯示/隱藏 "Currently Playing Playlist"，但對於所有支援來源 (External CD, HU USB, HU BTSA, MTP, SD-card 等) 只涵蓋部分情境，部份來源(如External CD, MTP, SD-Card)未驗證。
- Scope TCs: NR1L-Player-116, NR1L-Player-117, NR1L-Player-118, NR1L-Player-119, NR1L-Player-120
- Suggestion: 建議新增針對 External CD, MTP, SD-Card 等所有支援/不支援來源的 playlist 顯示/隱藏覆蓋用例，以及來源切換時的高亮狀態。

### [§6.3] SWE1-PLA-017 — Critical
- Issue: Req spec句 明確列出「Scroll Up/Down」與「Page Up/Down」兩種捲動方式，但本群組僅測試了 Page Down，缺少 Page Up 測試用例，Enumeration 覆蓋不全。
- Scope TCs: NR1L-Player-133, NR1L-Player-134, NR1L-Player-135
- Suggestion: 建議補充 Page Up 行為專屬的獨立用例，驗證向上翻頁的行為是否正確。

### [§6.3] SWE1-PLA-052 — Critical
- Issue: Demo Video 行為有多個枚舉情境（載入播放、Exit Lock 不可退出、repeat 循環、點火後不自動續播、清除個資停用），但本 Req group 僅覆蓋部份分支，缺少『Demo Video 被刪除時 Dealer Mode 停用』以及『Ignition reset 後 Demo 不自動續播』等覆蓋面。
- Scope TCs: NR1L-Player-137, NR1L-Player-138, NR1L-Player-139
- Suggestion: 建議新增兩個測試用例：(1) 清除個資後檢查 Demo Video 功能停用，(2) 斷電/點火循環後 Demo Video 不自動續播。

### [§6.3] SWE1-PLA-017 — Critical
- Issue: 需求句提及 Page Up 及 Page Down 兩個分支，但本 Req group 僅測試 Page Up，未覆蓋 Page Down 頻道。
- Scope TCs: NR1L-Player-136
- Suggestion: 補新增一支 Page Down 測試用例（執行 Page Down 後應下移一頁內容）

### [§6.3] SWE1-PLA-052 — Critical
- Issue: Req spec 定義 Demo Video 跨 ignition cycle 的多重行為 (載入播放、Exit Lock、repeat 循環、點火後不自動播放、清除個資停用)，本 req group 僅覆蓋『點火循環後不自動續播』，缺少『Exit Lock 不可退出』『repeat 循環』『清除個資移除 demo』等 branch 的 TC。
- Scope TCs: NR1L-Player-141
- Suggestion: 建議需補齊以下未覆蓋分支的 TC：
1. 設定 Exit Lock ON 時，播放中不可退出 Demo，要播放結束才結束。
2. Demo 設為 repeat 循環時，確認會自動循環播放。
3. 清除個資 (Clear Personal Data) 後 Demo Video 不可顯示與播放。

### [§6.3] SWE1-PLA-054 — Critical
- Issue: 需求句提及需顯示Weather及POI兩種應用之模板，但本Req僅以一個TC覆蓋，未分別驗證Weather與POI兩類第三方應用icon。
- Scope TCs: NR1L-Player-146
- Suggestion: 建議將Weather和POI各自新增一支TC進行覆蓋，分別驗證兩種icon對應正確模板顯示。

### [§6.3] SWE1-PLA-054 — Critical
- Issue: 需求句提及需顯示Weather及POI兩種應用之模板，但本Req僅以一個TC覆蓋，未分別驗證Weather與POI兩類第三方應用icon。
- Scope TCs: NR1L-Player-146
- Suggestion: 建議將Weather和POI各自新增一支TC進行覆蓋，分別驗證兩種icon對應正確模板顯示。

### [§6.3] SWE1-PLA-055 — Critical
- Issue: 需求句與說明內容涉及多個tab分類（All tab以及其他適用tab），現有TC僅於App Drawer單一tab下驗證，未涵蓋所有適用tab出現icon。
- Scope TCs: NR1L-Player-147
- Suggestion: 建議補足於所有需求規定的App Drawer tab進行icon顯示的驗證，各tab分開測試。

### [§6.3] SWE1-PLA-056 — Critical
- Issue: 需求句同時涵蓋disable和delete/uninstall兩種移除路徑，目前TC僅個別覆蓋，需明確成對覆蓋每一種App移除操作，並於所有tab驗證icon之移除。
- Scope TCs: NR1L-Player-148, NR1L-Player-149
- Suggestion: 建議針對『停用』與『刪除/解除安裝』各自補齊所有tab驗證，確認每一移除方式皆依規定移除所有App Drawer tab之icon。

### [§6.1] SWE1-PLA-059 — Critical
- Issue: Req spec句為『show the settings button only if the app supports the settings interface』，屬於支援/不支援二元條件，本群組兩支TC各覆蓋正向（有顯示）與負向（沒顯示）情境，覆蓋面完整，無需補充。
- Scope TCs: NR1L-Player-153, NR1L-Player-154
- Suggestion: 此二元條件覆蓋已充足，無需新增TC。

## Tier 2 + Tier 3 — Per TC Findings

### Row 10 · NR1L-Player-001 — verdict: `pass`

### Row 11 · NR1L-Player-002 — verdict: `pass`

### Row 12 · NR1L-Player-003 — verdict: `pass`

### Row 13 · NR1L-Player-004 — verdict: `pass`

### Row 14 · NR1L-Player-005 — verdict: `fail`
- **[§7.1] Critical** (test_item): Test Item 內容說明 generic read error，但根據 Domain Pack，此 Generic Error 為 catch-all，應用於排除 No Supported Files Found 和 USB File Read Error 之外的所有異常。TC 並未明確說明排除條件，易造成誤解與不精確覆蓋。
- **[§7.2] Major** (expected_result): ER 僅驗證 popup 出現，未確保該 Error 並非屬於 PU0003/P U0024 分類。根據 Req，須驗證 catch-all 邏輯，即非前述兩類異常才顯示 PU0005，否則覆蓋不完全。

### Row 15 · NR1L-Player-006 — verdict: `pass`

### Row 16 · NR1L-Player-007 — verdict: `pass`

### Row 17 · NR1L-Player-008 — verdict: `fail`
- **[§7.6] Critical** (expected_result): ER 僅驗證 Source/Audio Tab 可點擊，並未覆蓋所有『剩下』控制項確認為灰色且不可用，未完整對應規格要求。

### Row 18 · NR1L-Player-009 — verdict: `fail`
- **[§7.6] Critical** (expected_result): ER 僅驗證 Browse Tab disabled，缺乏全面檢查所有『剩下』控制項（如 Seek/Shuffle/Repeat/Track List…）是否都為灰色無作用，與規格不符。

### Row 19 · NR1L-Player-010 — verdict: `fail`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§7.6] Critical** (expected_result): ER 僅驗證 Tune knob 無作用，但缺乏所有『剩下』控制項（如 Seek/Shuffle/Repeat/Track List…）是否均為灰色無作用的檢查，未達規格全面覆蓋。

### Row 20 · NR1L-Player-011 — verdict: `pass_with_issues`
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員

### Row 21 · NR1L-Player-012 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 缺少『Apple Music Radio Stations』分類，未完全涵蓋 Req spec 中須支援的所有 Browse 分類列舉。
- **[§7.3] Major** (pre_conditions): Pre-Cond 直接陳述 Apple device 已支援 Apple Music，與 Req trigger 重疊，缺少測試前置條件差異化。

### Row 22 · NR1L-Player-013 — verdict: `pass_with_issues`
- **[§7.3] Major** (pre_conditions): Pre-Cond 直接敘述『支援 Apple Music 並已含 Apple Music Radio Stations』等於已 trigger，與 Req 重複。

### Row 23 · NR1L-Player-014 — verdict: `fail`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§7.3] Major** (pre_conditions): Pre-Cond 敘述『支援 Apple Music 並含 artist metadata』等於已達成部分 Req trigger，與 Spec 重複，缺乏前置限制。
- **[§7.1] Critical** (test_item): Test Item 結果僅描述 artist list 顯示，未覆蓋 Apple Music Radio Stations 或 browsing 行為，與 Spec 主要 outcome 不符。
- **[§7.2] Major** (expected_result): ER 僅驗證 artist list 展示，未涵蓋 Apple Music Radio Stations browse 支援，未 fully cover Spec。

### Row 24 · NR1L-Player-015 — verdict: `pass`

### Row 25 · NR1L-Player-016 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): 最後一步『Playback automatically continues from the first media file』未明列須無中斷且無需用戶操作，部分列出但未完全對應 Req 規範之『by default whenever playback is initiated』與『Repeat All』兩要素。

### Row 26 · NR1L-Player-017 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): 第 8 步僅敘述『Playback automatically continues with the next media file』，但未驗證『Repeat All』狀態指示，且缺乏對錯誤/中斷情境的驗證，未完全涵蓋 Req 敘述全部 outcome。

### Row 27 · NR1L-Player-018 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 第 8 步雖有涵蓋『playback automatically restarts from the first media file』，但未明確要求 Repeat All 狀態指示高亮，以及無中斷、無用戶操作與無錯誤。

### Row 28 · NR1L-Player-019 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): 第 8 步僅強調同首曲目自動重播，未驗證『Repeat Song』高亮狀態以及播放過程中不得切換其他曲目或出現中斷/錯誤情形，部分 outcome 未涵蓋。

### Row 29 · NR1L-Player-020 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): Play Controls 項目列舉需完整包含 Skip Forward/Skip Back, Play/Pause, Repeat, Shuffle, Progress Bar，現有 ER 雖有條列 a~f，但未驗證控制實際可用性及狀態（如 Repeat/Shuffle 應為 enabled），缺少全部 outcome 的驗證。

### Row 30 · NR1L-Player-021 — verdict: `pass`

### Row 31 · NR1L-Player-022 — verdict: `pass`

### Row 32 · NR1L-Player-023 — verdict: `fail`
- **[§7.1] Critical** (test_item): Test Item 所描述的 Repeat All 狀態顯示為 'OFF'，但根據 Domain Pack，Repeat All 應為高亮/ON 狀態並標籤為『Repeat All』，與實際規格描述不符。
- **[§7.2] Major** (expected_result): ER 僅確認 Repeat control 顯示 ON 狀態及標籤, 未涵蓋 Repeat All 狀態下播放行為應正確循環全部清單 (依 Domain Pack 行為定義)。
- **[§7.6] Major** (test_procedure): 測試步驟僅檢查操作後 Repeat control 狀態，並未覆蓋 Repeat All 行為分支（即到播放清單尾端自動重播第一首），未涵蓋規格要求循環播放功能。

### Row 33 · NR1L-Player-024 — verdict: `pass`

### Row 34 · NR1L-Player-025 — verdict: `pass`

### Row 35 · NR1L-Player-026 — verdict: `fail`
- **[§7.1] Critical** (test_item): Test Item 除了主句『toggle the Shuffle mode On or Off』，還包含 PC1.1/PC5.3/括號補充多條資訊，導致驗證目標不明確且混雜多條件。

### Row 36 · NR1L-Player-027 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): Expected Result 僅述及 split screen 顯示 playlist，未明確驗證列出的內容是否『隨機化』，對應 Req 實際 outcome 僅於後文簡單帶過，缺乏直接驗證 randomized sequence 的 observable 結果。

### Row 37 · NR1L-Player-028 — verdict: `pass_with_issues`
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§7.2] Major** (expected_result): Expected Result 第七步僅說明『shown in randomized sequence while Shuffle mode is ON』，欄位內容重複 Test Procedure，未明確驗證是否完整顯示 Now Playing playlist 所有曲目。

### Row 38 · NR1L-Player-029 — verdict: `pass`

### Row 39 · NR1L-Player-030 — verdict: `pass`

### Row 40 · NR1L-Player-031 — verdict: `pass`

### Row 41 · NR1L-Player-032 — verdict: `pass`

### Row 42 · NR1L-Player-033 — verdict: `pass`

### Row 43 · NR1L-Player-034 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 未覆蓋到 Req spec句完整描述的結果。Spec 包含『This will transition the user back to the Playing Tab and will close the Track window』，但 ER 僅驗證播放指定曲目未驗證 UI 狀態遷移。
- **[§7.6] Major** (expected_result): ER 僅驗證播放是否切換，未檢查 UI 是否跳回 Playing Tab 與 Track 視窗有無關閉，對應 spec 明列的行為未完整驗證（現實規格落 gap）。

### Row 44 · NR1L-Player-035 — verdict: `pass`

### Row 45 · NR1L-Player-036 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): Expected Result 僅驗證進入 Browse tab 及顯示 top-level folder/file list，未包含 Category structure navigation 或選取元素的具體結果，漏掉 Req 規範『navigate the Category structure and select items』.

### Row 46 · NR1L-Player-037 — verdict: `pass`

### Row 47 · NR1L-Player-038 — verdict: `pass`

### Row 48 · NR1L-Player-039 — verdict: `pass`

### Row 49 · NR1L-Player-040 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): ER 只描述『unsupported file formats are not displayed』，但未對應 Domain Pack 與規格定義的三類錯誤 popup(PU0003, PU0024, PU0005)的行為，缺少對產生 error popup (如遇損毀檔案或非支援但被掃描到情境) 的驗證。這會漏掉 spec 定義的所有可觀察異常反應。

### Row 50 · NR1L-Player-041 — verdict: `pass`

### Row 51 · NR1L-Player-042 — verdict: `pass`

### Row 52 · NR1L-Player-043 — verdict: `pass`

### Row 53 · NR1L-Player-044 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅說明『有啟用字元及禁用字元』，但未明確列出所有現有 item 首字母必須全啟用且其餘必須禁用，易產生不完整覆蓋。

### Row 54 · NR1L-Player-045 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): 預期結果寫『Alphajump softkey is disabled or not displayed』，但根據 Domain Pack Intelligent Character Filtering 定義（只啟用清單存在首字母的字元），空清單時所有字母都應禁用/所有按鍵皆灰，非必然『不顯示』或『disable』，TC 未涵蓋此關鍵 boundary。

### Row 55 · NR1L-Player-046 — verdict: `pass`

### Row 56 · NR1L-Player-047 — verdict: `pass_with_issues`
- **[§7.1] Major** (test_item): Test Item 僅描述有效字母被選取時的結果，未涵蓋規格明示之『只啟用存在於清單首字母的字元』，易導致未檢查無法選的 disabled 字母情境。

### Row 57 · NR1L-Player-048 — verdict: `pass_with_issues`
- **[§7.1] Major** (test_item): Test Item 僅描述有效字元選取後目前播放持續，未說明若選取無效字元是否可點擊（規格明文提 Intelligent Character Filtering），疏漏對 disabled 字元/無反應的驗證。

### Row 58 · NR1L-Player-049 — verdict: `pass`

### Row 59 · NR1L-Player-050 — verdict: `pass`

### Row 60 · NR1L-Player-051 — verdict: `pass`

### Row 61 · NR1L-Player-052 — verdict: `pass`

### Row 62 · NR1L-Player-053 — verdict: `pass`

### Row 63 · NR1L-Player-054 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_item): TC 直接假設系統會自動過濾不支援的 items，但在 Domain Pack 或規格句未定義系統行為需排除『unsupported items』，屬於推論特定產品邏輯，超出規格內容。

### Row 64 · NR1L-Player-055 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_item): TC 假設系統要自動過濾 empty category，但規格句和 Domain Pack 未提及有此排除機制，屬於產品層推論，超出台灣規範內容。

### Row 65 · NR1L-Player-056 — verdict: `pass`

### Row 66 · NR1L-Player-057 — verdict: `pass`

### Row 67 · NR1L-Player-058 — verdict: `pass`

### Row 68 · NR1L-Player-059 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_procedure): 雖舉例 A、C、D 首字母，但僅驗證部分字符啟用，沒有依據規範測出所有 boundary（如只有 1 字母、全 Disabled 的異常狀態等）。

### Row 69 · NR1L-Player-060 — verdict: `pass`

### Row 70 · NR1L-Player-061 — verdict: `pass`

### Row 71 · NR1L-Player-062 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 描述持續播放但未驗證游標指向正確項目，Req 明確要求游標應移動到以所選字母開頭第一個項目。本 TC 僅驗證 playback state 未變，漏掉游標移動關鍵驗證。
- **[§7.6] Major** (expected_result): 本 TC 僅驗證播放不中斷，未明確驗證 Domain Pack 所定 Intelligent Character Filtering 邏輯：若用戶選取不存在於清單的字母，該字母應不可點選/無反應，但此分支未被驗證。

### Row 72 · NR1L-Player-063 — verdict: `pass`

### Row 73 · NR1L-Player-064 — verdict: `pass`

### Row 74 · NR1L-Player-065 — verdict: `pass`

### Row 75 · NR1L-Player-066 — verdict: `pass`

### Row 76 · NR1L-Player-067 — verdict: `pass`

### Row 77 · NR1L-Player-068 — verdict: `pass`

### Row 78 · NR1L-Player-069 — verdict: `pass`

### Row 79 · NR1L-Player-070 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): 該 TC 只驗證播放時間格式（HH:MM:SS），但根據 Spec 該異常場景下所有未支援資料（如曲號與中繼資料）也應有特定顯示行為，TC 沒有對這些關鍵欄位進行 ER 覆蓋，漏驗規格明列的分支。

### Row 80 · NR1L-Player-071 — verdict: `pass`

### Row 81 · NR1L-Player-072 — verdict: `pass`

### Row 82 · NR1L-Player-073 — verdict: `pass`

### Row 83 · NR1L-Player-074 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅列出 Apple Music Radio category list 包含 Artists、Playlists、Songs、Albums、Genres 但未逐一確認每個類別的瀏覽/選取行為，導致規格『must be available through the HU Native Browse selection』的各子項目未被全部明確驗證。
- **[§7.6] Major** (expected_result): ER 僅檢查 Apple Music Radio 類別清單顯示，未逐一確認各 category（Artists、Playlists、Songs、Albums、Genres）下是否可進入且顯示內容清單，與規格定義『must be available through the HU Native Browse selection』之多層瀏覽行為有落差。

### Row 84 · NR1L-Player-075 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅以『A list corresponding to the selected Apple Music Radio category is displayed』泛述清單顯示結果，未明確定義每個 category 應有哪些影片或歌曲等內容，無法細查規格中各子項流程每一類都符合。
- **[§7.6] Major** (expected_result): ER 泛稱 list 顯示結果，未依據 Apple Music Radio 各 category 的不同類型細詳檢查實際顯示內容，和規格定義所有子類別皆 must be available through Browse 有明顯落差，漏驗證細項。

### Row 85 · NR1L-Player-076 — verdict: `pass`

### Row 86 · NR1L-Player-077 — verdict: `pass`

### Row 87 · NR1L-Player-078 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限

### Row 88 · NR1L-Player-079 — verdict: `pass`

### Row 89 · NR1L-Player-080 — verdict: `pass_with_issues`
- **[§7.6] Major** (expected_result): ER 最後對於 Skip Back command 的處理方式只寫『BTSA device processes the Skip Back command, and playback state is updated according to BTSA device behavior』，未明確檢查具體行為，造成驗證對象與 Domain Pack 不符。

### Row 90 · NR1L-Player-081 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§7.2] Major** (expected_result): ER 缺漏規格句明確要求的『Skip Back 按下時 <3 秒跳前一曲、=3 秒時行為』的完整預期結果，導致驗收行為定義不全。

### Row 91 · NR1L-Player-082 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（32 words），超出 14 words / 35 chars 上限
- **[§7.2] Major** (expected_result): ER 只驗證『>3 秒時回本曲起頭』，卻未對臨界值 3 秒或剛進入 3 秒時行為進行描述，少規格定義完整驗證行為。

### Row 92 · NR1L-Player-083 — verdict: `pass`

### Row 93 · NR1L-Player-084 — verdict: `pass`

### Row 94 · NR1L-Player-085 — verdict: `pass`

### Row 95 · NR1L-Player-086 — verdict: `pass`

### Row 96 · NR1L-Player-087 — verdict: `pass`

### Row 97 · NR1L-Player-088 — verdict: `pass`

### Row 98 · NR1L-Player-089 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅驗證 Play softkey 出現，未驗證 HU 是否真的完成 Play 指令、BTSA 播放狀態有變更，與 Req spec句所要求的『能夠對裝置執行 Play』不完全對齊。
- **[§7.6] Major** (test_procedure): Step 僅檢查 Play Controls 畫面顯示，未包含觸發 Play 指令之操作，驗證面與規格定義有落差（須驗證功能而不只是 UI 展示）。

### Row 99 · NR1L-Player-090 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅描述播放開始及 Play softkey 切換為 Pause，未明確驗證 BTSA 裝置端狀態已由 paused → playing；需明列車機送出 Play 指令且裝置實際恢復播放，完整承接規格要求的動作。

### Row 100 · NR1L-Player-091 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): Expected Result 僅驗證 Pause softkey 是否顯示，未明確包含 'Pause' softkey 顯示於 Play Controls area 的情境細節，與 Req 規格句略有落差。

### Row 101 · NR1L-Player-092 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): Expected Result 未明確描述只有在播放狀態下 Pause softkey 才會顯示於 Play Controls area，與 Req 期望細節未完全對齊。

### Row 102 · NR1L-Player-093 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): Expected Result 僅陳述 Play softkey 有顯示，未強調為 Pause 狀態下才顯示 Play softkey，與 Req 須於正確狀態下顯示條件對齊不足。

### Row 103 · NR1L-Player-094 — verdict: `pass`

### Row 104 · NR1L-Player-095 — verdict: `pass`

### Row 105 · NR1L-Player-096 — verdict: `pass`

### Row 106 · NR1L-Player-097 — verdict: `pass`

### Row 107 · NR1L-Player-098 — verdict: `pass`

### Row 108 · NR1L-Player-99 — verdict: `pass_with_issues`
- **[§7.1] Major** (test_item): Test Item 強調播放控制中的 Repeat softkey 存在，但內容未直接對齊需求規定的 'Play' 功能，也未針對 'Repeat' 行為本身作驗證，與規格描述偏離。

### Row 109 · NR1L-Player-100 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): 預期結果僅檢查 Repeat softkey 是否高亮及標籤為 Repeat Song，未明確對應到規格定義的『Repeat Song/All 狀態下 Repeat button 高亮且標籤顯示正確』，對於 Repeat softkey 的『ON』狀態需進一步明確化。

### Row 110 · NR1L-Player-101 — verdict: `fail`
- **[§7.1] Critical** (test_item): Test Item 表述 outcome（"Repeat softkey is not highlighted and labeled as 'Repeat'"）與 Req spec句只徵求『display為OFF state』不全然對齊，未明確反映 domain 裡定義的狀態差別，且未指出高亮/label細節由PC4.1裁決（高亮/標籤區辨非OFF狀態）。

### Row 111 · NR1L-Player-102 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§7.2] Major** (expected_result): ER僅檢查 Repeat softkey disabled 及不可選，不完整涵蓋 Req spec句明確規範的"Unavailable" state 展示要求（應同時顯示softkey和明確icon標示 unavailable，且須符合 Disabled 標準）。

### Row 112 · NR1L-Player-103 — verdict: `fail`
- **[§7.1] Critical** (test_item): Test Item outcome描述啟用Shuffle, 但未具體驗證 domain 定義的Shuffle模式轉換（如Shuffle softkey標示亮起），也未點出mode切換與UI同步要求，與Req及domain描述落差。

### Row 113 · NR1L-Player-104 — verdict: `fail`
- **[§7.2] Major** (expected_result): ER未完整陳述 Shuffle On 應達成的 actual observable outcome（應具體驗證播放序隨機且 softkey 狀態為高亮），僅以和原始順序不同代表 Shuffle，缺乏充分驗證 Shuffle 功能。
- **[§7.6] Critical** (expected_result): ER未引用 domain 定義的 Shuffle On 必須 random 序列要求（僅以與原順序不同為準），忽略若在播放單曲時無法驗證隨機行為，錯過所有枚舉分支狀況。

### Row 114 · NR1L-Player-105 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER未註明同時符合 Shuffle On 須『softkey高亮』及『播放順序為亂數序』，僅validation UI，而domain明指功能行為應與 UI 狀態一致，屬於 outcome 要素未齊全。

### Row 115 · NR1L-Player-106 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): 預期結果第8步只確認 Shuffle mode disabled，未明確驗證該 softkey 為『未高亮』狀態，未覆蓋 Req 指定的 softkey/icon 狀態表現。

### Row 116 · NR1L-Player-107 — verdict: `fail`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句
- **[§7.1] Critical** (test_item): Test Item 敘述主軸為 Shuffle Unavailable 狀態，但 content_req 追蹤到的是 Shuffle On 狀態，與規格不符。

### Row 117 · NR1L-Player-108 — verdict: `pass`

### Row 118 · NR1L-Player-109 — verdict: `pass`

### Row 119 · NR1L-Player-110 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 缺少對『INFO screen 關閉或隱藏』的驗證，僅驗證顯示與內容，未覆蓋 spec 所述 display/hide 行為的切換。

### Row 120 · NR1L-Player-111 — verdict: `pass_with_issues`
- **[§8.3.5] Major** (test_procedure): Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句

### Row 121 · NR1L-Player-112 — verdict: `pass`

### Row 122 · NR1L-Player-113 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅描述 INFO 畫面未顯示及 INFO softkey 狀態 (clickable/Available+OFF)，但缺少檢查『按下INFO softkey時，未出現 info 畫面』及其他互動副作用，未完全對齊 Req 指定的互動行為。

### Row 123 · NR1L-Player-114 — verdict: `pass`

### Row 124 · NR1L-Player-115 — verdict: `pass`

### Row 125 · NR1L-Player-116 — verdict: `pass`

### Row 126 · NR1L-Player-117 — verdict: `pass`

### Row 127 · NR1L-Player-118 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅驗證 Currently Playing Playlist 是否顯示，未明確包含 playlist 內容完整性或對應來源資訊，未完全比對 Req 的顯示條件。

### Row 128 · NR1L-Player-119 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅驗證 Playlist 隱藏，缺少比對隱藏條件是否與來源類型正確對應，未驗證不支援情境下不可顯示。

### Row 129 · NR1L-Player-120 — verdict: `pass`

### Row 130 · NR1L-Player-121 — verdict: `pass`

### Row 131 · NR1L-Player-122 — verdict: `pass`

### Row 132 · NR1L-Player-123 — verdict: `pass`

### Row 133 · NR1L-Player-124 — verdict: `pass`

### Row 134 · NR1L-Player-125 — verdict: `pass`

### Row 135 · NR1L-Player-126 — verdict: `pass`

### Row 136 · NR1L-Player-127 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 未覆蓋 Req spec句中的「Categories Bank」與「Browse List」必要顯示內容，僅說明顯示 Metadata Browsing 畫面但未具體列出各欄位/內容。

### Row 137 · NR1L-Player-128 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅描述依 source-specific metadata priority 顯示 metadata，未具體比對『Device Name, Artist, Song, Album』皆須呈現，與 Req spec句之瀏覽 metadata 細節比對不詳。

### Row 138 · NR1L-Player-129 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 未明確檢查瀏覽畫面有無同時出現正確的 Fallback 規則（缺 Song metadata 時應顯示 Device Name），未比對規格之 fallback 條件。

### Row 139 · NR1L-Player-130 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅檢查顯示『Bluetooth』，未明確驗證缺 metadata 時 fallback 機制與顯示流程，與 Req 的 fallback chain 規範對齊度不足。

### Row 140 · NR1L-Player-131 — verdict: `pass`

### Row 141 · NR1L-Player-132 — verdict: `pass`

### Row 142 · NR1L-Player-133 — verdict: `pass`

### Row 143 · NR1L-Player-134 — verdict: `pass`

### Row 144 · NR1L-Player-135 — verdict: `pass_with_issues`
- **[§7.6] Major** (test_procedure): Test Procedure 僅驗證 Page Down 行為，未覆蓋 Page Up 項目，缺少完整 enumeration coverage。

### Row 145 · NR1L-Player-136 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER 僅驗證 list 向上/向下切換動作，缺漏特殊 UI 行為『unless otherwise specified by the HMI requirements』，若有其他分歧條件未列清應明確標示。

### Row 146 · NR1L-Player-137 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§7.2] Major** (expected_result): ER 僅驗證 Demo Video 播放與影音輸出，未包含『啟用 exit lock option 時僅不可手動退出，必須播完才能自動退出』的特殊分支，此分支需明確驗證。

### Row 147 · NR1L-Player-138 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§7.2] Major** (expected_result): ER 未明確呈現影片播完是否自動退出、exit lock 裝置重置後 Demo Video 是否不可自動恢復等應驗證規範行為。

### Row 148 · NR1L-Player-139 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§7.3] Major** (pre_conditions): Pre-Condition 已說明『Demo Video repeat / loop option is not set』，但此為 Req 的分支條件，建議該情境作為 test procedure 的條件分支展開；Pre-Cond 不應記錄測試目標直接狀態。
- **[§7.2] Major** (expected_result): ER 僅描述播放結束回返回 HU 畫面，未包含 ignition reset、個資清除情境行為（規格明文定義功能停用等分支結局）。

### Row 149 · NR1L-Player-140 — verdict: `pass_with_issues`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§8.4.1] Major** (expected_result): Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定
- **[§7.3] Major** (pre_conditions): Pre-Condition 指明 Demo Video repeat / loop option is not set，但本 TC 主要測試情境應為 repeat 啟用之下的分支，建議測試分支條件交由程序/描述展開。
- **[§7.2] Major** (expected_result): ER 未完整驗證 loop/repeat 狀態下 Demo Video 僅可由 Dealer Mode 正常退出，亦未檢查 ignition reset 或個資清除後 Demo Video 功能失效等分支。

### Row 150 · NR1L-Player-141 — verdict: `fail`
- **[§8.1.1] Major** (test_item): Test Item 過長（22 words），超出 14 words / 35 chars 上限
- **[§7.2] Major** (expected_result): ER 僅驗證 ignition 循環後 Demo Video 不自動恢復播放，未覆蓋 Req 內明確列出的其他 outcome (如 Exit Lock, repeat/playback 循環, 清除個資停用等多重條件)。
- **[§7.6] Critical** (expected_result): 現有步驟與 ER 僅針對點火循環，不含 Exit Lock、repeat 循環或清資停用功能，產生行為覆蓋落差。

### Row 151 · NR1L-Player-142 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§7.2] Major** (expected_result): ER 僅驗證快捷鍵有顯示，未覆蓋 Req 特別要求的 icon/action 需源自 Ignite Store 並由 standard Android shortcut channel 驗收，缺少 channels/action source outcome。

### Row 152 · NR1L-Player-143 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§7.2] Major** (expected_result): ER 僅驗證 shortcut icon 呈現與 label，未明確確認該 icon/action 是否資料來源自 Ignite Store、是否用 standard Android shortcut channel 安規。

### Row 153 · NR1L-Player-144 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員
- **[§7.2] Major** (expected_result): ER 僅驗證 shortcut 有顯示，漏檢是否經由 Ignite Store 提供，及 action/icon 是否跟 requirement 一致經由 Ignite Store 並符合 Android shortcut channel 標準。

### Row 154 · NR1L-Player-145 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§7.1] Major** (test_item): Test Item outcomes 未明確包含 Req 中 icon/action 必須來自 Ignite Store 並透過 standard Android shortcut channel 傳達，只描述 launch service，traceability 有落差。

### Row 155 · NR1L-Player-146 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER未明確分別驗證Weather與POI不同應用的模板顯示，僅以『selected Weather or POI service application』籠統描述，未檢查每一種應用均正確對映至各自模板，與需求列舉的兩個App名稱不對齊。

### Row 156 · NR1L-Player-147 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER僅驗證App Drawer單一tab中的icon顯示，未檢查需求指定的Other applicable tabs中icon是否同樣顯示，無法覆蓋全部分支。

### Row 157 · NR1L-Player-148 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§7.2] Major** (expected_result): ER僅驗證單一路徑（刪除）下icon於各tab消失，應補充明確於所有tab都檢查icon移除，並將disable/uninstall覆蓋做明確區分，以完全對應需求列舉的兩種移除情境。

### Row 158 · NR1L-Player-149 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）

### Row 159 · NR1L-Player-150 — verdict: `pass_with_issues`
- **[§8.3.1] Major** (test_procedure): 測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員

### Row 160 · NR1L-Player-151 — verdict: `pass_with_issues`
- **[§8.1.2] Major** (test_item): Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）
- **[§8.5.3] Major** (design_method): 設計方法標為『基礎故障注入』，但流程和步驟內容並未執行異常或故障注入，未貼合 BVA/負向/例外等專用技術，與內容不符。

### Row 161 · NR1L-Player-152 — verdict: `pass`

### Row 162 · NR1L-Player-153 — verdict: `pass`

### Row 163 · NR1L-Player-154 — verdict: `pass`

### Row 164 · NR1L-Player-155 — verdict: `pass`

### Row 165 · NR1L-Player-156 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER未明確驗證 authentication flow 與 failure interface 的完整互動流程，僅檢查 UI 樣式、文字內容，未依據需求規範驗證彈窗流程與行為。

### Row 166 · NR1L-Player-157 — verdict: `pass_with_issues`
- **[§7.2] Major** (expected_result): ER未完整驗證 authentication failure interface 的彈窗流程與操作互動，僅描述訊息內容與 retry 行為，未檢查失敗介面的版面與訊息是否符合 Android P 定義的 failure flow。
