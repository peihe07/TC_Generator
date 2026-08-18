# 覆核用全文 — 未經第二人讀過之 40 條

- 產出層：執行層｜2026-08-18｜**供分析層逐條覆核**（21 包作業 6）
- 範圍：`TC-017 ～ TC-027`（第一批 11 條，C-6 所列）
  ＋ `TC-045 ～ TC-073`（第二批 29 條）
- 格式同 20 輪 §10；**每條含 spec 原文**，使覆核不必回查 `outline_map.json`

> 讀法建議：先讀「spec 原文」，再讀 ER —— 出處對照表（18／19 輪）
> 查的是「這句話有沒有來源」，**本檔要覆核的是「這句話對不對」**。

共 **40 條**。

---

## NR1L-UserProfiles-017 — SWE1-HMI-PROF-085（9.1 / Editing）

**spec 原文（`pdf_text`）**：

> EDPR1.) When on the “Edit Profile” tab, options pertaining to the active Profile will be listed in the order according to Table EDPR1. Tutorials will be a list item in the Edit Profile tab and there will be a circled number 1 next to Resume Tutorials. It will be removed as a line item once the user has completed setup assistant (See Tutorials HMI) Stellantis Connected Account will link to Connected Profile app, “More Settings” will link to “My Profile” Vehicle Settings, Tutorials will link to Tutorials (see Tutorials Logic and Flow).

**must_carry（PDF p14）**：there will be a circled number 1 next to Resume Tutorials. It will be removed as a list item once the user has completed setup assistant (See Tutorials HMI)

**must_carry（PDF p14）**：“ Stellantis Account” “Memory Seat” (If applicable) “Welcome Pop Up” “Delete Profile” “What is linked to my Profile?”

**037 description**：EDPR1.) When on the “Edit Profile” tab, options pertaining to the active Profile will be listed in the order according to Table EDPR1. Tutorials will be a list item in the Edit Profile tab. Connected Account will link to Connected Profile app, “More Settings” will link to “My Profile” Vehicle Settin

| 欄 | 值 |
|---|---|
| tc_title / test_item | Edit Profile tab lists options in Table EDPR1 order |
| pre_conditions | 1. The vehicle is an R1 High variant<br>2. A Driver Profile is active and setup assistant is not completed for it |
| input_test_data | NA |
| test_procedure | 1. Open the Profile section and select the “Edit Profile” tab<br>2. Read the option list and check that the items appear in the Table EDPR1 order |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. The options are listed in the Table EDPR1 order: Resume Setup (only if not complete), Edit Name, Edit Avatar, Connected Account, Memory Seat (if applicable), Welcome Pop Up, Delete Profile, What is linked to my Profile?, Tutorials, More Settings; and a circled number 1 is shown next to Resume Tutorials |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.1 |
| priority | **P2** — Edit Profile 清單之順序；呈現層 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | R1 High：清單第四項之 label 依 spec 9.3.2 之變體覆寫，採 Connected Account（R-U35 (c)）。列項順序取自 must_carry 之 Table EDPR1（PDF p14） |

**reasoning**：驗證目標：9.1（EDPR1）—— Edit Profile 分頁之選項須依 Table EDPR1 之順序列出，且 Resume Tutorials 旁有圈號 1。關鍵情境條件：圈號 1 之顯示以「setup assistant 未完成」為前提，故列 pre-condition；列項字串取自補句表之 Table EDPR1（PDF p14），非自擬。為什麼這樣切：本 leaf 之單位為「順序」，各項之連結去向（Connected Account → app、More Settings → My Profile）屬 9.1 之其他斷言與 11.3.1／9.8 之 leaf，本 TC 不代測。刻意略過：**本 TC 以 R1 High 為條件**，故 label 用 Connected Account；非 R1 High 車上該項為 Stellantis Account，其對照未生成（取樣單位為 leaf）。

---

## NR1L-UserProfiles-018 — SWE1-HMI-PROF-086（9.1.1 / Editing）

**spec 原文（`pdf_text`）**：

> EDPR1.1) 8.4inch screen size will not show the username and avatar to the left of the Edit Profile List (8.4" will show the username in the Edit Username line like “Edit username: [username]”).

**037 description**：EDPR1.1) 8.4inch screen size will not show the username and avatar to the left of the Edit Profile List (8.4" will show the username in the Edit Username line like “Edit username: [username]”).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Username and avatar hidden left of the 8.4-inch edit list |
| pre_conditions | 1. The vehicle has an 8.4-inch screen<br>2. A Driver Profile with a username is active |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Read the screen and check that no username or avatar is shown left of the list |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. No username or avatar is shown to the left of the Edit Profile List, and the username appears in the Edit Username line as “Edit username: [username]” |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.1.1 |
| priority | **P2** — 8.4 吋版面之呈現差異 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.1.1（EDPR1.1）—— 8.4 吋螢幕不在清單左側顯示 username 與 avatar，改於 Edit Username 該行顯示。關鍵情境條件：螢幕尺寸為條件本身，列 pre-condition；兩個觀察點（左側不顯示／該行顯示）為同一條件之兩個結果，併為一條 ER。為什麼這樣切：其他尺寸之版面屬 9.1 之常態，本 leaf 只管 8.4 吋之差異。

---

## NR1L-UserProfiles-019 — SWE1-HMI-PROF-087（9.1.2 / Editing）

**spec 原文（`pdf_text`）**：

> EDPR1.2) Memory seat status is not available if vehicle is not equipped with memory seats.

**037 description**：EDPR1.2) Memory seat status is not available if vehicle is not equipped with memory seats.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Memory seat status hidden when seats are not equipped |
| pre_conditions | 1. The vehicle is not equipped with memory seats<br>2. A Driver Profile is active |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Read the option list and check that no memory seat status is shown |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. No memory seat status is available in the list |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.1.2 |
| priority | **P2** — 未配備時之呈現隱藏 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.1.2（EDPR1.2）—— 未配備記憶座椅之車輛不顯示記憶座椅狀態。關鍵情境條件：車輛配置為條件本身，列 pre-condition。為什麼這樣切：已配備車輛之記憶座椅狀態與其操作屬 9.5.x 之 leaf，本 TC 只驗其不存在。

---

## NR1L-UserProfiles-020 — SWE1-HMI-PROF-088（9.2 / Editing）

**spec 原文（`pdf_text`）**：

> EDPR2.) Don’t show the Connected Profile options/info or Stellantis Connected Account button for regions without the <Brand> app. Do not show Connected Profile options/info or Stellantis Connected Account button if the vehicle does not support the connected profile feature.

**037 description**：EDPR2.) Don’t show the Connected Profile options/info or Connected Account button for regions without the <Brand> app. Do not show Connected Profile options/info or Connected Account button if the vehicle does not support the connected profile feature.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Connected Account hidden for unsupported regions |
| pre_conditions | 1. The vehicle is in a region without the brand app<br>2. A Driver Profile is active |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab<br>2. Read the option list and check that no account button or Connected Profile info is shown |
| expected_result | 1. The “Edit Profile” tab is displayed<br>2. No Connected Profile options or info and no Stellantis Connected Account button are shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.2 |
| priority | **P1** — 區域／車型配置之非主路徑分支 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | label 逐字取自 9.2。R1 High 車上該按鈕之 label 可能顯示為 Connected Account；**兩者指同一個按鈕**，本 TC 驗其**不顯示**，label 形式不影響判定（J-7）。該覆寫是否及於本節已列 RD 查詢（併 DR #3 送出） |

**reasoning**：驗證目標：9.2（EDPR2）—— 無 <Brand> app 之區域不顯示 Connected Profile 之選項／資訊與 Connected Account 按鈕。關鍵情境條件：條文有兩個獨立條件（區域無 app／車輛不支援），本 TC 取「區域」一側；車輛不支援一側之條件相同而觸發不同，由 11.3（CPA1）之 leaf 承擔（其文為 do not show if the vehicle does not support connectivity）。為什麼這樣切：兩個條件若併於一條 TC，失敗時分不出是哪一個條件沒生效。

---

## NR1L-UserProfiles-021 — SWE1-HMI-PROF-089（9.3 / Editing）

**spec 原文（`pdf_text`）**：

> EDPR3.) While vehicle is in motion, the following will be greyed out and cannot be selected/completed: Deleting a Profile, editing username, editing avatar, Tutorials, Resume Setup, and viewing info of what is linked to a Profile.

**037 description**：EDPR3.) While vehicle is in motion, the following will be greyed out and cannot be selected/completed: Deleting a Profile, editing username, editing avatar, Tutorials, Resume Setup, and viewing info of what is linked to a Profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Edit options greyed out while the vehicle is in motion |
| pre_conditions | 1. A Driver Profile is active and the “Edit Profile” tab is displayed<br>2. The vehicle is stationary on a test track and can be brought into motion |
| input_test_data | NA |
| test_procedure | 1. Read the option list and record which items are selectable<br>2. Bring the vehicle into motion<br>3. Read the option list and check that the restricted items are greyed out |
| expected_result | 1. The options recorded in step 1 are selectable while stationary<br>2. The vehicle is in motion<br>3. Deleting a Profile, editing username, editing avatar, Tutorials, Resume Setup, and viewing info of what is linked to a Profile are greyed out and cannot be selected |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3 |
| priority | **P0** — 行車中受限項目不可選取 —— **防線成立本身**（§10.2 safety；D-UP16-01 附二） |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | （空） |

**reasoning**：驗證目標：9.3（EDPR3）—— 行車中六個項目變灰且不可選取。關鍵情境條件：判準為靜止→行進之狀態轉換（§12 首匹配 → 狀態轉換），故以步驟 1 之靜止狀態為基準線（§5.6）。為什麼這樣切：六個項目為同一觸發之同一結果，依 §5.7 併為一條 ER；選取時之 bonk 與訊息屬 9.3.1、進行中被中斷屬 9.3.2，兩者觸發不同。

---

## NR1L-UserProfiles-022 — SWE1-HMI-PROF-090（9.3.1 / Editing）

**spec 原文（`pdf_text`）**：

> EDPR3.1) If any items listed above are selected while vehicle in motion, a bonk tone will be played along with the message “Function not available while vehicle in Motion.”

**037 description**：EDPR3.1) If any items listed above are selected while vehicle in motion, a bonk tone will be played along with the message “Function not available while vehicle in Motion.”

| 欄 | 值 |
|---|---|
| tc_title / test_item | Bonk tone and message when a restricted item is selected |
| pre_conditions | 1. A Driver Profile is active and the “Edit Profile” tab is displayed<br>2. The vehicle is in motion on a test track |
| input_test_data | NA |
| test_procedure | 1. Select the greyed-out “Delete Profile” item<br>2. Read the screen and check that the bonk tone and the message are presented |
| expected_result | 1. The selection is not accepted<br>2. A bonk tone is played and “Function not available while vehicle in Motion.” is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3.1<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3 |
| priority | **P2** — 限制之回饋（音效與訊息）呈現 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：9.3.1（EDPR3.1）—— 行車中選取受限項目時播放 bonk 音並顯示指定訊息。關鍵情境條件：受測動作為對已變灰項目之選取，屬不被允許之操作（§12 首匹配 → 負向測試）；受限項目之清單出自 9.3，故併列該節。為什麼這樣切：本 leaf 之單位為「回饋」，項目是否變灰屬 9.3、進行中被中斷屬 9.3.2。

---

## NR1L-UserProfiles-023 — SWE1-HMI-PROF-091-02（9.3.2 / Editing）

**spec 原文（`pdf_text`）**：

> EDPR3.2) If user is in the process of viewing/doing any of the above listed items, system should return to previous available page and play the bonk and show the message specified above. ****R1 High Only: "Stellantis Account" to be replaced with "Connected Account"

**must_carry（PDF p14）**：****R1 High Only: "Stellantis Account" to be replaced with "Connected Account"

**037 description**：When the system interrupts an active task and returns to the previous page due to the vehicle being in motion, it must concurrently play a "bonk" audio tone and display the specific warning message: “Function not available while vehicle in Motion.”.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Bonk tone and message accompany the interruption in motion |
| pre_conditions | 1. A Driver Profile is active and the Edit Profile tab is available<br>2. The vehicle is stationary on a test track and can be brought into motion |
| input_test_data | NA |
| test_procedure | 1. Open the Edit Profile tab and start editing the Profile username<br>2. Bring the vehicle into motion<br>3. Read the screen and check that the bonk tone and the message are presented |
| expected_result | 1. The username editing page is displayed<br>2. The vehicle is in motion and the task is interrupted<br>3. A bonk tone is played and “Function not available while vehicle in Motion.” is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3.2<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3.1 |
| priority | **P2** — 同上；本條之單位為回饋本身 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | sibling 軸：本條驗**回饋**，091-01 驗**返回前一頁** —— 同一觸發之兩個結果，分屬兩個 037 leaf（§8.2.1）。9.3.2 之變體覆寫為**列級**（Table EDPR1 之該列），本 TC 不含帳號 label，故不設變體前提 |

**reasoning**：驗證目標：9.3.2（EDPR3.2）之回饋部分 —— 進行中被中斷時播 bonk 並顯示訊息。關鍵情境條件：同 091-01 之狀態轉換（靜止→行進），差別在觀察點：091-01 觀察頁面返回，本條觀察音效與訊息。為什麼這樣切：037 為 9.3.2 切出兩個 leaf，一葉一 TC（§8.2.1）；訊息字串出自 9.3.1，故併列該節。

---

## NR1L-UserProfiles-024 — SWE1-HMI-PROF-092（9.4 / Editing）

**spec 原文（`pdf_text`）**：

> EDPR5.) Pressing anywhere on the avatar or anywhere on the “Change Avatar” line will initiate a screen that allows the user to choose a new Avatar (similar to popup during New Profile Setup

**037 description**：EDPR5.) Pressing anywhere on the avatar or anywhere on the “Change Avatar” line will initiate a screen that allows the user to choose a new Avatar (similar to popup during New Profile Setup

| 欄 | 值 |
|---|---|
| tc_title / test_item | Avatar selection screen opens from avatar or Change Avatar |
| pre_conditions | 1. A Driver Profile is active and the “Edit Profile” tab is displayed<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press anywhere on the avatar<br>2. Read the screen and check that the avatar selection screen is displayed<br>3. Return to the “Edit Profile” tab<br>4. Press anywhere on the “Change Avatar” line and check that the same screen is displayed |
| expected_result | 1. The avatar is pressed<br>2. The avatar selection screen is displayed<br>3. The “Edit Profile” tab is displayed<br>4. The avatar selection screen is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.4 |
| priority | **P2** — avatar 選擇畫面之開啟 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.4（EDPR5）—— 按 avatar 或按「Change Avatar」該行皆開啟 avatar 選擇畫面。關鍵情境條件：條文明列兩個入口，兩者為**不同觸發同一結果**，故於一條 TC 內各驗一次（非拆兩條 —— 拆了會產生兩條除入口外全同之 TC）。為什麼這樣切：該畫面之內容屬 9.4.1、離開不存之行為屬 9.4.2。

---

## NR1L-UserProfiles-025 — SWE1-HMI-PROF-093（9.4.1 / Editing）

**spec 原文（`pdf_text`）**：

> EDPR5.1) The screen will show the currently selected Avatar highlighted and provide the option to choose from all other available avatars

**037 description**：EDPR5.1) The screen will show the currently selected Avatar highlighted and provide the option to choose from all other available avatars

| 欄 | 值 |
|---|---|
| tc_title / test_item | Current avatar highlighted among the available avatars |
| pre_conditions | 1. A Driver Profile with a selected avatar is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the avatar selection screen from the “Edit Profile” tab<br>2. Read the screen and check that the current avatar is highlighted |
| expected_result | 1. The avatar selection screen is displayed<br>2. The currently selected avatar is highlighted and all other available avatars are offered |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.4.1 |
| priority | **P2** — avatar 畫面之呈現細節 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.4.1（EDPR5.1）—— 選擇畫面須標示目前 avatar，並提供其餘可用 avatar。關鍵情境條件：pre-condition 要求該 profile 已有 avatar，否則「目前之 avatar」無從觀察。為什麼這樣切：畫面之開啟屬 9.4，本 leaf 只管其內容。

---

## NR1L-UserProfiles-026 — SWE1-HMI-PROF-094（9.4.2 / Editing）

**spec 原文（`pdf_text`）**：

> EDPR5.2) Exiting without saving will not result in an Avatar change

**037 description**：EDPR5.2) Exiting without saving will not result in an Avatar change

| 欄 | 值 |
|---|---|
| tc_title / test_item | Avatar unchanged when the screen is exited without saving |
| pre_conditions | 1. A Driver Profile with a selected avatar is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the avatar selection screen and record the current avatar<br>2. Select a different avatar without saving<br>3. Exit the screen without saving<br>4. Read the “Edit Profile” tab and check that the avatar recorded in step 1 is still in use |
| expected_result | 1. The avatar selection screen is displayed and the current avatar is recorded<br>2. The different avatar is selected on the screen<br>3. The screen is exited without saving<br>4. The avatar recorded in step 1 is still in use |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.4.2 |
| priority | **P1** — 未存即離開不得改動 avatar —— **失效即使用者資料被意外變更** |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：9.4.2（EDPR5.2）—— 未儲存即離開不得造成 avatar 變更。關鍵情境條件：須先在畫面上選了別的 avatar 才有「未存即離開」可言，故步驟 2 為必要之設置，非多餘。為什麼這樣切：儲存後之變更屬 9.4 之正向路徑，本 leaf 只管未儲存之路徑；失效之後果是使用者資料被意外變更，故判 P1 而非 P2。

---

## NR1L-UserProfiles-027 — SWE1-HMI-PROF-095（9.5 / Editing）

**spec 原文（`pdf_text`）**：

> EDPR6.) Swapping memory seat preference means the active Profile will be linked to that memory seat button/position until another change is made.

**037 description**：EDPR6.) Swapping memory seat preference means the active Profile will be linked to that memory seat button/position until another change is made.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Active Profile linked to the swapped memory seat position |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. Two Driver Profiles exist and Profile A is active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab and read the memory seat linked to Profile A<br>2. Swap the memory seat preference to another position<br>3. Read the memory seat status and check that Profile A is linked to the new position |
| expected_result | 1. The memory seat currently linked to Profile A is recorded<br>2. The memory seat preference is swapped<br>3. Profile A is linked to the newly selected memory seat position |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.5 |
| priority | **P0** — 記憶座椅連結＝PLP 3.5 之偏好；本條為其規則本身 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | sibling 軸（9.5.x 四條）：本條＝**交換之通則**；9.5.1＝前置**已**連結之分支；9.5.2＝前置**未**連結之分支；9.5.3＝「none」選項之可用性 |

**reasoning**：驗證目標：9.5（EDPR6）—— 交換記憶座椅偏好後，現用 profile 連結至該座椅位置，直到下一次變更。關鍵情境條件：判準為連結狀態之轉換（§12 首匹配 → 狀態轉換），以步驟 1 之原連結為基準線（§5.6）。為什麼這樣切：本條為通則，9.5.1／9.5.2 為其依前置狀態分出之兩個分支，037 已為三者各切一 leaf，一葉一 TC（§8.2.1）。

---

## NR1L-UserProfiles-045 — SWE1-HMI-PROF-113（12.1 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL1.) The system should store any updated preferences until Valet Mode is exited. The system should treat Exiting Valet Mode like deleting the profile and activating Valet Mode like creating a new Profile from the default preferences.

**037 description**：PVAL1.) The system should store any updated preferences until Valet Mode is exited. The system should treat Exiting Valet Mode like deleting the profile and activating Valet Mode like creating a new Profile from the default preferences.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode starts from defaults and restores on exit |
| pre_conditions | 1. A Driver Profile with customized preferences is active<br>2. Valet Mode is not active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the preferences of the active Profile<br>2. Activate Valet Mode<br>3. Read the preferences and change one of them<br>4. Exit Valet Mode<br>5. Read the preferences and check that they match those recorded in step 1 |
| expected_result | 1. The preferences of the active Profile are recorded<br>2. Valet Mode is active and its preferences are the default ones, not those recorded in step 1<br>3. The changed preference is stored while Valet Mode is active<br>4. Valet Mode is exited<br>5. The preferences match those recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.1 |
| priority | **P0** — Valet 進出時之偏好儲存與重設 —— 核心五類之二者交會 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | （空） |

**reasoning**：驗證目標：12.1（PVAL1）—— 啟用 Valet Mode 視同以預設偏好建立新 profile，退出視同刪除該 profile；期間之變更只存到退出為止。關鍵情境條件：須有一個已客製化之 profile 作為基準線，否則「預設 vs 客製」分不出來（§5.6）。為什麼這樣切：進入與退出雖為兩個觸發，但條文以「像建立／像刪除」成對定義，**只驗一半則另一半之語意不成立** —— 同 13.2 之處置（§5.7 之例外，具名）。

---

## NR1L-UserProfiles-046 — SWE1-HMI-PROF-114（12.1.1 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL1.1) Status bar will always need to return to the default status bar setup when Valet Mode is active so the Profile icon is always visible. Reference Core HMI Logic and Flow for Status Bar default specifications.

**037 description**：PVAL1.1) Status bar will always need to return to the default status bar setup when Valet Mode is active so the Profile icon is always visible. Reference Core HMI Logic and Flow for Status Bar default specifications.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Status bar returns to its default setup in Valet Mode |
| pre_conditions | 1. The status bar is configured away from its default setup<br>2. Valet Mode is not active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the current status bar setup<br>2. Activate Valet Mode<br>3. Read the status bar and check that it shows the default setup with the Profile icon visible |
| expected_result | 1. The current status bar setup is recorded<br>2. Valet Mode is active<br>3. The status bar shows the default setup and the Profile icon is visible |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.1.1 |
| priority | **P2** — 狀態列之預設版面；呈現層 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.1.1（PVAL1.1）—— Valet Mode 啟用時狀態列須回到預設版面，使 Profile 圖示恆可見。關鍵情境條件：pre-condition 要求狀態列先偏離預設，否則「回到預設」與「本來就是預設」無從分辨。為什麼這樣切：預設版面之細節條文委派 Core HMI Logic and Flow，本 TC 只驗其回到預設且 Profile 圖示可見（§8.4.1 不代擬他份文件之內容）。

---

## NR1L-UserProfiles-047 — SWE1-HMI-PROF-115（12.2 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL2.) Valet Mode can only be activated through the button on the All Profiles tab of the Profile section.

**037 description**：PVAL2.) Valet Mode can only be activated through the button on the All Profiles tab of the Profile section. (image: %E5%9C%96%E7%89%87_919753979.png)

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode activates only from the All Profiles tab |
| pre_conditions | 1. Valet Mode is not active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab and read the option list<br>2. Open the vehicle settings and read the option list<br>3. Open the “All Profiles” tab and check that the Valet Mode button is present there |
| expected_result | 1. No Valet Mode activation control is present on the “Edit Profile” tab<br>2. No Valet Mode activation control is present in the vehicle settings<br>3. The Valet Mode button is present on the “All Profiles” tab |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.2 |
| priority | **P1** — 啟用入口之限制；非主路徑分支 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.2（PVAL2）—— Valet Mode 只能經 All Profiles 分頁之按鈕啟用。關鍵情境條件：「只能」之驗證須同時看兩側 ——別處沒有（步驟 1、2）與該處有（步驟 3）；**只驗該處有，一個到處都能啟用之實作也會通過**（§7）。為什麼這樣切：受檢之他處取 Edit Profile 分頁與車輛設定兩個最可能之位置；**窮舉所有畫面不可行**，此為抽樣，已於上繳具名。

---

## NR1L-UserProfiles-048 — SWE1-HMI-PROF-116（12.2.1 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL2.1) Valet Mode button is greyed out while the vehicle is in motion. If the button is pushed while greyed out, a popup will indicate that the function is not available (Pop-up ID PU0091).

**037 description**：PVAL2.1) Valet Mode button is greyed out while the vehicle is in motion. If the button is pushed while greyed out, a popup will indicate that the function is not available (Pop-up ID PU0091).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode button greyed out while the vehicle is in motion |
| pre_conditions | 1. Valet Mode is not active<br>2. The vehicle is stationary on a test track and can be brought into motion |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and read the Valet Mode button<br>2. Bring the vehicle into motion<br>3. Read the Valet Mode button and press it<br>4. Read the screen and check that the unavailability popup is displayed |
| expected_result | 1. The Valet Mode button is selectable while stationary<br>2. The vehicle is in motion<br>3. The Valet Mode button is greyed out<br>4. PU0091 indicates that the function is not available |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.2.1 |
| priority | **P0** — 行車中不得啟用 Valet Mode —— **防線成立本身**（§10.2 safety） |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | （空） |

**reasoning**：驗證目標：12.2.1（PVAL2.1）—— 行車中 Valet Mode 按鈕變灰；按下已變灰之按鈕時顯示 PU0091。關鍵情境條件：以靜止時可選為基準線（§5.6），判準為靜止→行進之狀態轉換（§12 首匹配 → 狀態轉換）。為什麼這樣切：變灰與按下之提示為同一條件下之兩個結果，037 未再切分，故併為一條（§5.7）。

---

## NR1L-UserProfiles-049 — SWE1-HMI-PROF-117（12.3 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL3.) To activate Valet Mode a 4 digit one-time PIN is required to be entered.

**037 description**：PVAL3.) To activate Valet Mode a 4 digit one-time PIN is required to be entered.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Four-digit PIN required to activate Valet Mode |
| pre_conditions | 1. Valet Mode is not active<br>2. The vehicle is stationary |
| input_test_data | PIN: a 4-digit one-time PIN chosen at activation |
| test_procedure | 1. Open the “All Profiles” tab and press the Valet Mode button<br>2. Read the screen and check that a 4-digit PIN entry is required<br>3. Enter a 4-digit PIN and confirm<br>4. Read the screen and check that Valet Mode is active |
| expected_result | 1. The Valet Mode activation is started<br>2. A 4-digit PIN entry is requested before activation<br>3. The 4-digit PIN is accepted<br>4. Valet Mode is active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.3 |
| priority | **P0** — 啟用之 PIN —— Valet Mode 之防護本身 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.3（PVAL3）—— 啟用 Valet Mode 須輸入 4 位一次性 PIN。關鍵情境條件：ER2 明寫「在啟用之前」要求 PIN ——若寫成「輸入 PIN 後啟用」，一個先啟用再問 PIN 之實作也會通過（§7）。為什麼這樣切：停用側之同一 PIN 屬 12.3.1，PIN 錯誤之次數上限屬 12.9，皆不在本條。

---

## NR1L-UserProfiles-050 — SWE1-HMI-PROF-118（12.3.1 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL3.1) To get out of Valet Mode the same 4 digit PIN needs to be entered

**037 description**：PVAL3.1) To get out of Valet Mode the same 4 digit PIN needs to be entered

| 欄 | 值 |
|---|---|
| tc_title / test_item | Same four-digit PIN required to leave Valet Mode |
| pre_conditions | 1. Valet Mode is active and was activated with a known 4-digit PIN<br>2. The vehicle is stationary |
| input_test_data | PIN: the same 4-digit PIN used at activation; one differing 4-digit PIN |
| test_procedure | 1. Start the Valet Mode deactivation<br>2. Enter a 4-digit PIN that differs from the activation PIN<br>3. Enter the same 4-digit PIN used at activation<br>4. Read the screen and check that Valet Mode is no longer active |
| expected_result | 1. The PIN entry for deactivation is displayed<br>2. The differing PIN is rejected and Valet Mode is still active<br>3. The same PIN as at activation is accepted<br>4. Valet Mode is no longer active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.3.1 |
| priority | **P0** — 停用之 PIN —— 同上 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.3.1（PVAL3.1）—— 退出 Valet Mode 須輸入**與啟用時相同**之 PIN。關鍵情境條件：「相同」之驗證須有一個不同之 PIN 作對照（§7）——只驗正確 PIN 可退出，一個任何 4 位數都接受之實作也會通過。為什麼這樣切：錯誤次數之上限屬 12.9，本條只驗「須相同」。

---

## NR1L-UserProfiles-051 — SWE1-HMI-PROF-119（12.3.2 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL3.2) Disconnecting the battery will override and reset Valet mode and the system will load the last known Driver Profile at the next key on.

**037 description**：PVAL3.2) Disconnecting the battery will override and reset Valet mode and the system will load the last known Driver Profile at the next key on.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Battery disconnect resets Valet Mode at the next key on |
| pre_conditions | 1. Valet Mode is active<br>2. The last known Driver Profile before Valet Mode is recorded<br>3. The vehicle is stationary and the battery can be disconnected on the bench |
| input_test_data | Fault injected: battery disconnected while Valet Mode is active |
| test_procedure | 1. Disconnect the vehicle battery<br>2. Reconnect the battery and switch the key on<br>3. Read the active Profile and check that Valet Mode is no longer active |
| expected_result | 1. The battery is disconnected<br>2. The vehicle powers up at key on<br>3. Valet Mode is not active and the last known Driver Profile is loaded |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.3.2 |
| priority | **P1** — 斷電後之重設與 profile 接續；spec 明訂之行為，非漏洞 |
| design_method | 基礎故障注入 (Fault Injection Lite) |
| remarks | （空） |

**reasoning**：驗證目標：12.3.2（PVAL3.2）—— 斷開電瓶會覆寫並重設 Valet Mode，下次 key on 時載入最後已知之 Driver Profile。關鍵情境條件：斷電為可模擬之故障（§12 首匹配 → 基礎故障注入）；「最後已知 profile」須於 pre-condition 先記錄，否則無比對對象。**來源標示（J-4）**：`key on` 之觀察點與 `ignition cycle` 同屬 **R-U21** 之「設定→key cycle→讀回」形態，惟本條之 key on 為**條文明述**（`at the next key on`），故其權威為 spec 而非裁決。

---

## NR1L-UserProfiles-052 — SWE1-HMI-PROF-120（12.3.3 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL3.3) The system should return to previous Profile after exiting/deactivating Valet Mode

**037 description**：PVAL3.3) The system should return to previous Profile after exiting/deactivating Valet Mode

| 欄 | 值 |
|---|---|
| tc_title / test_item | Previous Profile restored after Valet Mode is exited |
| pre_conditions | 1. Driver Profile A is active and Valet Mode is not active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the active Profile<br>2. Activate Valet Mode<br>3. Deactivate Valet Mode<br>4. Read the active Profile and check that it matches the one recorded in step 1 |
| expected_result | 1. Driver Profile A is recorded as active<br>2. Valet Mode is active<br>3. Valet Mode is deactivated<br>4. Driver Profile A is active again |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.3.3 |
| priority | **P1** — 退出後之 profile 接續 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | （空） |

**reasoning**：驗證目標：12.3.3（PVAL3.3）—— 退出 Valet Mode 後回到先前之 profile。關鍵情境條件：以步驟 1 之記錄為基準線（§5.6）。為什麼這樣切：Valet Mode 期間之偏好處置屬 12.1，本條只驗退出後之 profile 接續。

---

## NR1L-UserProfiles-053 — SWE1-HMI-PROF-121（12.4 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL4) If during the initiation of Valet Mode, and/or activation/deactivation of the Valet PIN the user presses another portion of the screen, treat as a cancel command.

**037 description**：PVAL4) If during the initiation of Valet Mode, and/or activation/deactivation of the Valet PIN the user presses another portion of the screen, treat as a cancel command.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Pressing elsewhere cancels the Valet PIN entry |
| pre_conditions | 1. Valet Mode is not active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Start the Valet Mode activation so that the PIN entry is displayed<br>2. Press another portion of the screen outside the PIN entry<br>3. Read the screen and check that the PIN entry is cancelled |
| expected_result | 1. The PIN entry is displayed<br>2. The press outside the PIN entry is treated as a cancel command<br>3. The PIN entry is closed and Valet Mode is not active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.4 |
| priority | **P2** — PIN 輸入之取消路徑 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.4（PVAL4）—— PIN 輸入期間按畫面他處視為取消。關鍵情境條件：條文涵蓋啟用與停用兩側之 PIN，本條取啟用側；停用側之取消行為相同，未另切 TC（037 未為其切 leaf）。為什麼這樣切：ER3 併驗「未進入 Valet Mode」—— 只驗畫面關閉，一個關掉畫面卻已啟用之實作會通過（§7）。

---

## NR1L-UserProfiles-054 — SWE1-HMI-PROF-122（12.5 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL5.) Valet Mode will be indicated in the status bar with a lock symbol combined with the Profile icon.

**037 description**：PVAL5.) Valet Mode will be indicated in the status bar with a lock symbol combined with the Profile icon.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Lock symbol shown with the Profile icon in Valet Mode |
| pre_conditions | 1. Valet Mode is not active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read the Profile icon in the status bar<br>2. Activate Valet Mode<br>3. Read the status bar and check that the lock symbol is combined with the Profile icon |
| expected_result | 1. The Profile icon is shown without a lock symbol<br>2. Valet Mode is active<br>3. The status bar shows a lock symbol combined with the Profile icon |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.5 |
| priority | **P2** — 狀態列之 Valet 指示；呈現層 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.5（PVAL5）—— Valet Mode 於狀態列以鎖頭圖示結合 Profile 圖示表示。關鍵情境條件：以啟用前之圖示為基準線（§5.6），否則「有鎖頭」與「本來就有」分不出。為什麼這樣切：狀態列之預設版面屬 12.1.1，本條只驗該指示。

---

## NR1L-UserProfiles-055 — SWE1-HMI-PROF-123（12.6 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL6.) When Valet Mode is active and the user pushes the Profile button in the status bar, a popup will indicate “Function not available while in Valet Mode. Do you want to deactivate Valet Mode”

**037 description**：PVAL6.) When Valet Mode is active and the user pushes the Profile button in the status bar, a popup will indicate “Function not available while in Valet Mode. Do you want to deactivate Valet Mode”

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile button in Valet Mode offers to deactivate |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the Profile button in the status bar<br>2. Read the popup and check that it offers to deactivate Valet Mode |
| expected_result | 1. The Profile button is pressed<br>2. A popup indicates “Function not available while in Valet Mode. Do you want to deactivate Valet Mode” |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.6 |
| priority | **P2** — Valet 中按 Profile 鍵之提示 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.6（PVAL6）—— Valet Mode 中按狀態列之 Profile 鍵時，以 popup 告知功能不可用並詢問是否停用。關鍵情境條件：popup 文字逐字取自條文，含其未加問號之原樣（§8.4.1）。為什麼這樣切：按下「是」之後續退出流程屬 12.3.1／12.9，本條只驗該提示。

---

## NR1L-UserProfiles-056 — SWE1-HMI-PROF-124（12.7 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL7.) When in Valet mode, pushing the memory seat buttons will only change the seat position but will not load the associated Driver Profile.

**037 description**：PVAL7.) When in Valet mode, pushing the memory seat buttons will only change the seat position but will not load the associated Driver Profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Memory seat buttons move the seat without loading a Profile |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. Driver Profile A is linked to memory seat 1 and its position differs from the current seat position<br>3. Valet Mode is active<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the active Profile and the seat position<br>2. Press the memory seat 1 button<br>3. Read the seat position and the active Profile and check that only the seat position changed |
| expected_result | 1. The active Profile is the Valet Mode Profile and the seat position is recorded<br>2. The memory seat 1 button is pressed<br>3. The seat moves to the memory seat 1 position and the active Profile is still the Valet Mode Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.7 |
| priority | **P0** — **Valet 下不得載入車主 profile** —— 失效即隔離被繞過 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | **來源標示（J-12）**：`memory seat 1` 之編號為測試設置，條文只說 `the memory seat buttons` |

**reasoning**：驗證目標：12.7（PVAL7）—— Valet Mode 中按記憶座椅鍵只改座椅位置，不載入其所連之 Driver Profile。關鍵情境條件：pre-condition 要求該座椅所連 profile 之位置與現況不同，否則座椅有沒有動看不出來。為什麼這樣切：失效之後果是 **Valet 使用者載入了車主之 profile**，即隔離被繞過，故依 D-UP16-01 判 P0。

---

## NR1L-UserProfiles-057 — SWE1-HMI-PROF-125-01（12.8 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL8.) Only HVAC and Media sections will be available when Valet Mode is on. Projection mode and native HFP will be disabled. VR will not be active and the following areas will be locked out: Home Screen, Apps Drawer, Phone, Vehicle category, Navigation. It will not be possible to interact with the Status Bar with the exception of the Valet Profile and HVAC icons. In Media, the Device Manager will be locked out. All non interactable items will be greyed out.

**037 description**：When Valet Mode is active, only the HVAC (Climate) and Media sections shall remain accessible to the user. However, as an explicit exception within the Media section, the "Device Manager" feature must be completely locked out.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Device Manager locked out inside Media in Valet Mode |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the Media section<br>2. Select Device Manager<br>3. Read the screen and check that Device Manager is locked out |
| expected_result | 1. The Media section is available in Valet Mode<br>2. The Device Manager entry is greyed out<br>3. Device Manager cannot be opened |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8 |
| priority | **P0** — Device Manager 之鎖定 —— 車主資產之防線本身 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：12.8（PVAL8）之 Media 例外 —— Media 區可用，惟其中之 Device Manager 被鎖住。關鍵情境條件：ER1 併驗 Media 本身可用 —— **那是本條之對照組**（§7）：若整個 Media 都打不開，Device Manager 打不開就沒有意義。為什麼這樣切：037 為 12.8 切出四個 leaf，本條依其 description 之單位（Device Manager 之例外）生成；**該 leaf 之標題與描述錯位，見 A-UP11**。

---

## NR1L-UserProfiles-058 — SWE1-HMI-PROF-125-02（12.8 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL8.) Only HVAC and Media sections will be available when Valet Mode is on. Projection mode and native HFP will be disabled. VR will not be active and the following areas will be locked out: Home Screen, Apps Drawer, Phone, Vehicle category, Navigation. It will not be possible to interact with the Status Bar with the exception of the Valet Profile and HVAC icons. In Media, the Device Manager will be locked out. All non interactable items will be greyed out.

**037 description**：During Valet Mode, Projection mode (e.g., CarPlay/Android Auto) and native HFP (Hands-Free Profile / Bluetooth Calling) must be disabled. Furthermore, VR (Voice Recognition) must not be active, and the following specific HMI areas must be strictly locked out: Home Screen, Apps Drawer, Phone, Vehicle

| 欄 | 值 |
|---|---|
| tc_title / test_item | Projection, native HFP and VR disabled in Valet Mode |
| pre_conditions | 1. A projection-capable device is connected to the head unit<br>2. Valet Mode is active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Attempt to start projection mode from the head unit<br>2. Attempt to place a call over native HFP<br>3. Press the voice recognition control<br>4. Open the Media section and check that it is available |
| expected_result | 1. Projection mode is disabled and does not start<br>2. Native HFP is disabled and no call is placed<br>3. Voice recognition is not active<br>4. The Media section is available |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8 |
| priority | **P0** — Projection／HFP／VR 之停用 —— 阻擋 valet 使用者觸及車主之手機連線 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：12.8（PVAL8）—— Valet Mode 中 Projection、native HFP 停用，VR 不啟動。關鍵情境條件：三者為條文並列之停用項，同一條件下之三個結果，依 §5.7 併為一條 TC 之三條 ER。為什麼這樣切：**ER4 為 §7 之對照** —— 以「Media 仍可用」證明本條測到的是選擇性停用，而非整機不可用。**未另切負向 TC**：對照置於同一 TC（§5.6），理由見上繳 19 §6。

---

## NR1L-UserProfiles-059 — SWE1-HMI-PROF-125-03（12.8 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL8.) Only HVAC and Media sections will be available when Valet Mode is on. Projection mode and native HFP will be disabled. VR will not be active and the following areas will be locked out: Home Screen, Apps Drawer, Phone, Vehicle category, Navigation. It will not be possible to interact with the Status Bar with the exception of the Valet Profile and HVAC icons. In Media, the Device Manager will be locked out. All non interactable items will be greyed out.

**037 description**：In Valet Mode, user interaction with the Status Bar must be strictly limited. It shall not be possible to interact with any items on the Status Bar, with the sole exception of the Valet Profile icon and the HVAC icons.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Status bar interaction limited to Valet Profile and HVAC |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press a status bar item other than Valet Profile or HVAC<br>2. Read the screen and check that the item does not respond<br>3. Press the HVAC icon in the status bar and check that it responds |
| expected_result | 1. The other status bar item is pressed<br>2. The item does not respond and no screen change occurs<br>3. The HVAC icon responds |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8 |
| priority | **P0** — 狀態列互動之限制 —— 隔離之邊界本身 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：12.8（PVAL8）—— Valet Mode 中狀態列不可互動，**惟 Valet Profile 與 HVAC 圖示為例外**。關鍵情境條件：ER3 為 §7 之對照 —— 例外項須仍可用，否則「不可互動」與「整條狀態列壞掉」分不出。為什麼這樣切：本條依 037 之 description 生成（狀態列互動限制）；**該 leaf 之標題寫的是手套箱提示，與描述錯位，見 A-UP11**。

---

## NR1L-UserProfiles-060 — SWE1-HMI-PROF-125-04（12.8 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL8.) Only HVAC and Media sections will be available when Valet Mode is on. Projection mode and native HFP will be disabled. VR will not be active and the following areas will be locked out: Home Screen, Apps Drawer, Phone, Vehicle category, Navigation. It will not be possible to interact with the Status Bar with the exception of the Valet Profile and HVAC icons. In Media, the Device Manager will be locked out. All non interactable items will be greyed out.

**037 description**：To provide clear system status to the user, all items, icons, and buttons that are rendered non-interactable or locked out due to Valet Mode restrictions must be visually displayed in a "greyed out" state.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Non-interactable items greyed out in Valet Mode |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open a screen that contains locked-out items<br>2. Read the locked-out items and check that they are greyed out |
| expected_result | 1. The screen with locked-out items is displayed<br>2. All non-interactable items are greyed out |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8 |
| priority | **P2** — 不可互動項之變灰呈現 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.8（PVAL8）末句 —— 所有不可互動之項目一律變灰。關鍵情境條件：本條驗的是**呈現之一致性**，不是哪些項目被鎖（那屬 125-01～03）。為什麼這樣切：依 037 之 description 生成；**標題與描述錯位，見 A-UP11**。

---

## NR1L-UserProfiles-061 — SWE1-HMI-PROF-126-01（12.8.1 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL8.1) Valet Mode will enable “electronic” Glove Box Lock. If vehicle is equipped with Glove Box Lock, show PU0832 when prompting to enter Valet Mode. Glove Box Lock button is greyed out when Valet Mode is activated. If the Glove Box Lock button is pushed while greyed out, PU0833 will indicate that function is not available while in Valet Mode.

**037 description**：If the vehicle is equipped with an electronic Glove Box Lock, the system must display popup PU0832 when prompting the user to enter Valet Mode, informing them that the glove box will be locked.

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU0832 shown when prompting to enter Valet Mode |
| pre_conditions | 1. The vehicle is equipped with an electronic Glove Box Lock<br>2. Valet Mode is not active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and press the Valet Mode button<br>2. Read the prompt and check that PU0832 is displayed |
| expected_result | 1. The Valet Mode entry prompt is displayed<br>2. PU0832 informs the user that the glove box will be locked |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8.1 |
| priority | **P2** — 手套箱鎖之進入提示（PU0832） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.8.1（PVAL8.1）—— 配備電子手套箱鎖之車輛，在提示進入 Valet Mode 時顯示 PU0832。關鍵情境條件：車輛配置為條文明列之條件，列 pre-condition。為什麼這樣切：未配備手套箱鎖之車輛不顯示該提示，其對照未生成（取樣單位為 leaf，§8.4.2）。**本條依 037 之 description 生成；標題與描述錯位，見 A-UP11。**

---

## NR1L-UserProfiles-062 — SWE1-HMI-PROF-126-02（12.8.1 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL8.1) Valet Mode will enable “electronic” Glove Box Lock. If vehicle is equipped with Glove Box Lock, show PU0832 when prompting to enter Valet Mode. Glove Box Lock button is greyed out when Valet Mode is activated. If the Glove Box Lock button is pushed while greyed out, PU0833 will indicate that function is not available while in Valet Mode.

**037 description**：When Valet Mode is actively running, the electronic Glove Box Lock button must be visually rendered in a greyed-out (disabled) state.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Glove Box Lock button greyed out while Valet Mode is active |
| pre_conditions | 1. The vehicle is equipped with an electronic Glove Box Lock<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read the Glove Box Lock button before Valet Mode is activated<br>2. Activate Valet Mode<br>3. Read the Glove Box Lock button and check that it is greyed out |
| expected_result | 1. The Glove Box Lock button is selectable<br>2. Valet Mode is active<br>3. The Glove Box Lock button is greyed out |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8.1 |
| priority | **P0** — 手套箱鎖按鈕之變灰 —— 實體資產之防線執行手段 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.8.1（PVAL8.1）—— Valet Mode 啟用時手套箱鎖按鈕變灰。關鍵情境條件：以啟用前可選為基準線（§5.6）。為什麼這樣切：按下已變灰之按鈕之提示屬 126-03，本條只驗其變灰。**依 description 生成；標題與描述錯位，見 A-UP11。**

---

## NR1L-UserProfiles-063 — SWE1-HMI-PROF-126-03（12.8.1 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL8.1) Valet Mode will enable “electronic” Glove Box Lock. If vehicle is equipped with Glove Box Lock, show PU0832 when prompting to enter Valet Mode. Glove Box Lock button is greyed out when Valet Mode is activated. If the Glove Box Lock button is pushed while greyed out, PU0833 will indicate that function is not available while in Valet Mode.

**037 description**：If the user attempts to push the greyed-out Glove Box Lock button while Valet Mode is activated, the system must block the action and display popup PU0833 to indicate that the function is not available while in Valet Mode.

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU0833 shown when the greyed Glove Box Lock button is pressed |
| pre_conditions | 1. The vehicle is equipped with an electronic Glove Box Lock<br>2. Valet Mode is active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the greyed-out Glove Box Lock button<br>2. Read the screen and check that PU0833 is displayed |
| expected_result | 1. The press is not accepted and the glove box lock state does not change<br>2. PU0833 indicates that the function is not available while in Valet Mode |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8.1 |
| priority | **P1** — 按下已變灰之按鈕：其 ER1 併驗**鎖定狀態未變**（防線）、ER2 為提示（回饋）—— 兩者各半，取中 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：12.8.1（PVAL8.1）末句 —— 按下已變灰之手套箱鎖按鈕時顯示 PU0833。關鍵情境條件：受測動作為對已變灰項目之按壓（§12 首匹配 → 負向測試）。為什麼這樣切：ER1 併驗「鎖定狀態未變」——只驗 popup 出現，一個顯示 popup 卻仍執行動作之實作會通過（§7）。

---

## NR1L-UserProfiles-064 — SWE1-HMI-PROF-127（12.8.2 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL8.2) If the glove box is unlocked/locked prior to activating Valet Mode, the glove box will return to its last state upon deactivating Valet Mode.

**037 description**：PVAL8.2) If the glove box is unlocked/locked prior to activating Valet Mode, the glove box will return to its last state upon deactivating Valet Mode.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Glove box returns to its previous state after Valet Mode |
| pre_conditions | 1. The vehicle is equipped with an electronic Glove Box Lock<br>2. The glove box is unlocked<br>3. Valet Mode is not active<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the glove box lock state<br>2. Activate Valet Mode<br>3. Deactivate Valet Mode<br>4. Read the glove box lock state and check that it matches the state recorded in step 1 |
| expected_result | 1. The glove box is recorded as unlocked<br>2. Valet Mode is active and the glove box is locked<br>3. Valet Mode is deactivated<br>4. The glove box is unlocked again |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8.2 |
| priority | **P1** — 手套箱狀態之還原；退出後之狀態接續 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | （空） |

**reasoning**：驗證目標：12.8.2（PVAL8.2）—— 手套箱於退出 Valet Mode 後回到進入前之狀態。關鍵情境條件：pre-condition 取「未上鎖」，使 ER2 之「Valet 中變為上鎖」與 ER4 之「回到未上鎖」皆可觀察；若進入前即上鎖，整條 TC 之三個狀態相同，什麼都驗不到。為什麼這樣切：Valet Mode 啟用手套箱鎖之行為屬 12.8.1，本條驗其還原。

---

## NR1L-UserProfiles-065 — SWE1-HMI-PROF-128-02（12.9 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL9.) For activation and deactivation, the user will have 10 attempts to type a 4 digit PIN before system cancels the deactivation. The user can try again in 30min.

**037 description**：Once the 10-attempt limit is reached, the system must strictly enforce a 30-minute lockout period. During this time, the user cannot attempt to enter a PIN to activate or deactivate Valet Mode.

| 欄 | 值 |
|---|---|
| tc_title / test_item | PIN entry blocked during the 30-minute lockout |
| pre_conditions | 1. Valet Mode is active and a 4-digit PIN is set<br>2. The vehicle is stationary |
| input_test_data | PIN attempts: 10 incorrect attempts, then a further attempt |
| test_procedure | 1. Open the Valet Mode deactivation screen<br>2. Enter an incorrect 4-digit PIN ten times<br>3. Attempt to enter a PIN again immediately<br>4. Read the screen and check that the PIN entry is not accepted |
| expected_result | 1. The Valet Mode deactivation screen is displayed<br>2. The tenth incorrect attempt cancels the deactivation<br>3. A further PIN entry is attempted<br>4. The PIN entry is not accepted and Valet Mode is still active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.9 |
| priority | **P0** — 鎖定期間不得輸入 PIN —— 防暴力嘗試之機制本身 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | 鎖定期為 30 分鐘；本 TC 只驗**鎖定生效**（不需等待），屆滿後之回復屬 128-03（需 30 分鐘等待） |

**reasoning**：驗證目標：12.9（PVAL9）之鎖定側 —— 10 次錯誤後之 30 分鐘內不受理 PIN。關鍵情境條件：本條刻意只驗「立刻再試不受理」，**不涉時間長度**，故無須等待 30 分鐘；長度之驗證由 128-03 承擔。為什麼這樣切：第 10 次取消本身屬 pilot 之 TC-015（12.9），本條為其後之狀態。

---

## NR1L-UserProfiles-066 — SWE1-HMI-PROF-128-03（12.9 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL9.) For activation and deactivation, the user will have 10 attempts to type a 4 digit PIN before system cancels the deactivation. The user can try again in 30min.

**037 description**：After the 30-minute lockout period has fully elapsed, the system must automatically lift the restriction, allowing the user to try entering the PIN again. The attempt counter must be reset.

| 欄 | 值 |
|---|---|
| tc_title / test_item | PIN entry restored after the 30-minute lockout elapses |
| pre_conditions | 1. Valet Mode is active and a 4-digit PIN is set<br>2. The vehicle is stationary and can remain powered for the duration of the test |
| input_test_data | Elapsed time after the tenth incorrect attempt: 29 min, 30 min |
| test_procedure | 1. Enter an incorrect 4-digit PIN ten times to trigger the lockout<br>2. Attempt a PIN entry after 29 minutes<br>3. Attempt a PIN entry after 30 minutes<br>4. Enter the correct PIN and check that Valet Mode is no longer active |
| expected_result | 1. The lockout is in effect after the tenth incorrect attempt<br>2. The PIN entry is not accepted at 29 minutes<br>3. The PIN entry is accepted at 30 minutes<br>4. Valet Mode is no longer active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.9 |
| priority | **P1** — 鎖定屆滿後之可用性回復 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| remarks | **執行成本：本 TC 需 30 分鐘等待**（J-8：照寫、不縮時、不刪除）。縮時屬測試實作之手段（bench 上如何撥時鐘），非 TC 內容之決定；排程時須計入。 |

**reasoning**：驗證目標：12.9（PVAL9）末句 —— 30 分鐘後可再試。關鍵情境條件：以 29 分（仍鎖定）與 30 分（可再試）構成邊界前後（§5.6）。**來源標示（J-4）**：ER2「29 分鐘時仍不受理」之權威為 **§5.6 之 BVA 界前基準線**，非條文 —— 12.9 只寫「30 分鐘後可再試」。為什麼這樣切：鎖定之生效屬 128-02，本條驗其屆滿與計數重置（ER4 以正確 PIN 成功退出證明計數已重置）。

---

## NR1L-UserProfiles-067 — SWE1-HMI-PROF-129（12.10 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL10.) For activation and deactivation, when on the PIN entry popup, grey out the Go button until 4 digits are entered. If Go is pressed while greyed out, play Bonk tone and display the popup “PIN must be 4 digits”.

**037 description**：PVAL10.) For activation and deactivation, when on the PIN entry popup, grey out the Go button until 4 digits are entered. If Go is pressed while greyed out, play Bonk tone and display the popup “PIN must be 4 digits”.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Go button greyed out until four digits are entered |
| pre_conditions | 1. The Valet Mode PIN entry popup is displayed<br>2. The vehicle is stationary |
| input_test_data | PIN digits entered: 3, then 4 |
| test_procedure | 1. Enter three digits and read the Go button<br>2. Press the Go button while it is greyed out<br>3. Read the screen and check the tone and the popup<br>4. Enter a fourth digit and read the Go button |
| expected_result | 1. The Go button is greyed out with three digits entered<br>2. The press is not accepted<br>3. A Bonk tone is played and the popup “PIN must be 4 digits” is displayed<br>4. The Go button is available with four digits entered |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.10 |
| priority | **P2** — Go 鍵之可用性與其提示 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：12.10（PVAL10）—— 未滿 4 碼前 Go 鍵變灰；此時按下播 Bonk 並顯示指定 popup。關鍵情境條件：ER4 為對照 —— 輸滿 4 碼後 Go 須可用，否則「未滿時變灰」與「永遠變灰」分不出（§7）。**來源標示（J-12）**：3 碼為測試設置（條文只說「未滿 4 碼」）。為什麼這樣切：兩個結果同屬「未滿 4 碼」此一條件，依 §5.7 併為一條。

---

## NR1L-UserProfiles-068 — SWE1-HMI-PROF-130（12.10.1 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVAL10.1) Once 4 digits are entered grey out all numeric buttons.

**037 description**：PVAL10.1) Once 4 digits are entered grey out all numeric buttons.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Numeric buttons greyed out once four digits are entered |
| pre_conditions | 1. The Valet Mode PIN entry popup is displayed<br>2. The vehicle is stationary |
| input_test_data | PIN digits entered: 4 |
| test_procedure | 1. Enter three digits and read the numeric buttons<br>2. Enter a fourth digit<br>3. Read the numeric buttons and check that they are greyed out |
| expected_result | 1. The numeric buttons are available with three digits entered<br>2. The fourth digit is entered<br>3. All numeric buttons are greyed out |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.10.1 |
| priority | **P3** — 輸滿 4 碼後數字鍵變灰 —— 呈現細節 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.10.1（PVAL10.1）—— 輸滿 4 碼後所有數字鍵變灰。關鍵情境條件：以 3 碼時可用為基準線（§5.6）。**來源標示（J-12）**：3 碼為測試設置。為什麼這樣切：Go 鍵之可用性屬 12.10，本條只管數字鍵。

---

## NR1L-UserProfiles-069 — SWE1-HMI-PROF-131（13.1 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVALSPK1.) When Valet mode is enabled by SPAAK, no PIN code will be required to enter or exit Valet Mode. For the SPAAK scenario, Valet Mode will automatically activate when it detects a SPAAK key with Valet Mode permissions.

**037 description**：PVALSPK1.) When Valet mode is enabled by SPAAK, no PIN code will be required to enter or exit Valet Mode. For the SPAAK scenario, Valet Mode will automatically activate when it detects a SPAAK key with Valet Mode permissions.

| 欄 | 值 |
|---|---|
| tc_title / test_item | SPAAK key activates Valet Mode without a PIN |
| pre_conditions | 1. A SPAAK key with Valet Mode permissions is available<br>2. Valet Mode is not active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Present the SPAAK key with Valet Mode permissions to the vehicle<br>2. Read the screen and check that Valet Mode is active without a PIN entry |
| expected_result | 1. The SPAAK key with Valet Mode permissions is detected<br>2. Valet Mode is active and no PIN entry was requested |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_13.1 |
| priority | **P0** — SPAAK 之自動啟用（免 PIN）—— Valet 進出 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：13.1（PVALSPK1）—— SPAAK 啟用之 Valet Mode 不需 PIN，偵測到具 Valet 權限之 SPAAK 鑰匙時自動啟用。關鍵情境條件：ER2 明寫「未要求 PIN」——只驗「已啟用」，一個仍要求 PIN 之實作也會通過。為什麼這樣切：SPAAK 下之退出限制屬 13.2，提示屬 13.3。

---

## NR1L-UserProfiles-070 — SWE1-HMI-PROF-132-01（13.2 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVALSPK2.) The SPAAK user cannot exit Valet Mode from the head unit. Only the owner can deactivate Valet Mode remotely via app or website or other supported methods (not on the head unit). Any screens or popups that may allow a user to exit Valet Mode must be blocked (PU0934, etc).

**037 description**：When Valet Mode is activated via SPAAK, the SPAAK user must not be able to exit Valet Mode from the head unit. Any screens, buttons, or popups (such as PU0934) that normally allow a user to exit Valet Mode must be strictly blocked or suppressed on the head unit.

| 欄 | 值 |
|---|---|
| tc_title / test_item | All head unit Valet exit paths blocked for the SPAAK user |
| pre_conditions | 1. Valet Mode is active under the SPAAK scenario<br>2. The user at the head unit is the SPAAK user<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the Valet Profile icon in the status bar<br>2. Open the “All Profiles” tab and look for a deactivation control<br>3. Read the screen and check that no head unit path exits Valet Mode |
| expected_result | 1. The Valet Profile icon does not open a deactivation flow<br>2. No deactivation control is available on the “All Profiles” tab<br>3. Valet Mode is still active and any popup that would allow an exit is blocked |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_13.2 |
| priority | **P0** — SPAAK 下主機退出之全面阻擋 —— 隔離被繞過即失效 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | sibling 軸：本條驗**主機各入口皆被阻擋**（窮舉入口）；pilot 之 TC-016 驗**車主遠端停用可行**（同節之另一 leaf） |

**reasoning**：驗證目標：13.2（PVALSPK2）之阻擋側 —— SPAAK 使用者無法自主機退出。關鍵情境條件：本條之單位是「**所有**主機路徑」，故步驟逐一走過狀態列圖示與 All Profiles 分頁兩個入口。為什麼這樣切：037 為 13.2 切出兩個 leaf —— 本條（阻擋）與 pilot 之 132-02（車主遠端停用）；一葉一 TC（§8.2.1）。刻意略過：**入口之窮舉不可能完備** —— 取兩個最可能者，已具名。

---

## NR1L-UserProfiles-071 — SWE1-HMI-PROF-133（13.3 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVALSPK3.) If the SPAAK user presses the Profiles icon with the lock, popup PU1573 will display.

**037 description**：PVALSPK3.) If the SPAAK user presses the Profiles icon with the lock, popup PU1573 will display.

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU1573 shown when the SPAAK user presses the locked icon |
| pre_conditions | 1. Valet Mode is active under the SPAAK scenario<br>2. The user at the head unit is the SPAAK user<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the Profiles icon with the lock in the status bar<br>2. Read the screen and check that PU1573 is displayed |
| expected_result | 1. The Profiles icon with the lock is pressed<br>2. PU1573 is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_13.3 |
| priority | **P2** — SPAAK 下按 Profile 圖示之提示（PU1573） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：13.3（PVALSPK3）—— SPAAK 使用者按下帶鎖之 Profiles 圖示時顯示 PU1573。關鍵情境條件：帶鎖之圖示即 12.5 所述之呈現，本條以其為操作對象。為什麼這樣切：非 SPAAK 情境下按同一圖示之行為屬 12.6（PU 不同），兩者之 pre-condition 互斥。刻意略過：PU1573 之內文未載於 spec，本 TC 只驗其顯示（同 R-U27 之處置）。

---

## NR1L-UserProfiles-072 — SWE1-HMI-PROF-134（14.1 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVALEX1.) When Valet Mode is active the welcome popup will indicate the vehicle is in Valet mode, with a button to deactivate it. Pressing the Valet Profile icon in the status bar or pressing on “Exit Valet Mode” button on the Valet Mode welcome popup will initiate the Exit Valet Mode process above.

**037 description**：PVALEX1.) When Valet Mode is active the welcome popup will indicate the vehicle is in Valet mode, with a button to deactivate it. Pressing the Valet Profile icon in the status bar or pressing on “Exit Valet Mode” button on the Valet Mode welcome popup will initiate the Exit Valet Mode process above.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet welcome popup indicates Valet Mode with an exit button |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Trigger the welcome popup<br>2. Read the popup and check its Valet indication and button<br>3. Press the “Exit Valet Mode” button and check that the PIN entry for deactivation is displayed |
| expected_result | 1. The welcome popup is displayed<br>2. The popup indicates that the vehicle is in Valet mode and shows a button to deactivate it<br>3. The 4 digit PIN entry for deactivating Valet Mode is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_14.1<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.3.1 |
| priority | **P1** — Valet welcome popup 之內容與退出入口 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文之「the Exit Valet Mode process **above**」其指涉對象**不在 ch14**（ch14 僅 14.1／14.2，本節即首條）—— 複位後為 12.3.1（同一 PIN 退出）與 12.6（停用詢問），故併列該二節。見上繳 19 §4 |

**reasoning**：驗證目標：14.1（PVALEX1）—— Valet Mode 中之 welcome popup 須指出車輛處於 Valet Mode 並提供停用按鈕，按下後進入退出流程。關鍵情境條件：ER3 之「退出流程」以 12.3.1 之 PIN 輸入為其可觀察形態；**該指涉之複位為本輪之查證結果**（R-U51 之判讀首次受檢）。為什麼這樣切：狀態列圖示亦可觸發同一流程（條文並列），本 TC 取 popup 之按鈕一側；圖示側之觸發屬 12.6 之 leaf。

---

## NR1L-UserProfiles-073 — SWE1-HMI-PROF-135（14.2 / Valet Mode）

**spec 原文（`pdf_text`）**：

> PVALEX2.) Valet Mode cannot be deactivated while the vehicle is in motion. If Profile section is attempted to be accessed while in Valet Mode while the vehicle is in motion, the user will see a popup (Pop-up ID PU0394). OK OK Yes Yes No No “X”

**037 description**：PVALEX2.) Valet Mode cannot be deactivated while the vehicle is in motion. If Profile section is attempted to be accessed while in Valet Mode while the vehicle is in motion, the user will see a popup (Pop-up ID PU0394).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode cannot be deactivated while the vehicle moves |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary on a test track and can be brought into motion |
| input_test_data | NA |
| test_procedure | 1. Bring the vehicle into motion<br>2. Attempt to access the Profile section<br>3. Read the screen and check that the unavailability popup is displayed and Valet Mode is still active |
| expected_result | 1. The vehicle is in motion<br>2. The Profile section is not accessible<br>3. PU0394 is displayed and Valet Mode is still active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_14.2 |
| priority | **P0** — **行車中不得停用** —— 失效即 Valet 可於行進中被解除 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：14.2（PVALEX2）—— 行車中不得停用 Valet Mode；行車中嘗試進入 Profile 區時顯示 PU0394。關鍵情境條件：受測動作為行進中之停用嘗試，屬不被允許之操作（§12 首匹配 → 負向測試）。為什麼這樣切：ER3 併驗「Valet Mode 仍啟用」——只驗 popup 出現，一個顯示 popup 卻仍解除之實作會通過（§7）。**本條之失效後果為行進中 Valet 可被解除** —— R-U5 之 rubric 無安全帶，依 D-UP16-01 就近判 P0，見上繳 19 §7。

---

