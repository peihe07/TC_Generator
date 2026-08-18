# 覆核用全文 ＋ ER 出處對照 — 第五批 後半（`146`–`156`）

- 產出層：執行層｜2026-08-18｜**供分析層逐條覆核**
- 本檔 **11 條**；另半在 `40_review_pack_24a.md`
- 格式同 21／23／29／34／35 輪；**本輪起由 `scripts/build_review_pack.py` 產生，不再手打轉錄**

> 讀法：先讀「spec 原文」與「037 description」，再讀 ER ——
> 「這句話對不對」是本檔要問的；「這句話有沒有來源」見 §0 之出處對照。

## 0. ER 出處對照

| 項 | 數 |
|---|---|
| 引號字面值（ER ＋ pre_conditions）| **7** |
| 逐字溯得到被引之節或其 must_carry | **3** |
| 經 `UI_LOCATORS` 登記表溯源 | **4** |
| **未溯得者** | **0** |
| 全條無引號字面值者 | **7 條** |

| tc_id | 節 | 字面值 | 欄位 | 出處 |
|---|---|---|---|---|
| `NR1L-UserProfiles-146` | 5.15.1 | 「All Profiles」| ER | 逐字見於 **5.15.1** |
| `NR1L-UserProfiles-147` | 5.16 | 「Edit Profile」| ER | 逐字見於 **5.16** |
| `NR1L-UserProfiles-155` | 6.5 | 「All Profiles」| ER | 逐字見於 **6.5** |
| `NR1L-UserProfiles-155` | 6.5 | 「Edit Profile」| pre | `UI_LOCATORS` 登記：其來源為 **5.1** |
| `NR1L-UserProfiles-156` | 6.6 | 「Edit Profile」| ER | `UI_LOCATORS` 登記：其來源為 **5.1** |
| `NR1L-UserProfiles-156` | 6.6 | 「Edit Profile」| ER | `UI_LOCATORS` 登記：其來源為 **5.1** |
| `NR1L-UserProfiles-156` | 6.6 | 「Edit Profile」| pre | `UI_LOCATORS` 登記：其來源為 **5.1** |

---

## 1. 逐條全文

### NR1L-UserProfiles-146 — SWE1-HMI-PROF-044（5.15.1 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR5.1) If the username is too long to be displayed within the All Profiles username space, follow the Core HMI Logic and Flow truncation rules.

**037 description**：ALLPR5.1) If the username is too long to be displayed within the All Profiles username space, follow the Core HMI Logic and Flow truncation rules.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Long usernames are truncated on the All Profiles tab |
| pre_conditions | 1. A Driver Profile whose username exceeds the All Profiles username space exists<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab<br>2. Read the displayed username and compare it with the stored username |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. The username is shown truncated, following the Core HMI Logic and Flow truncation rules |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.15.1 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P3** — 過長 username 之截斷；規則在外部文件 |
| remarks | **截斷規則不在本 spec** —— 5.15.1 只說「依 Core HMI Logic and Flow 之截斷規則」，該文件不在本 feature 之輸入內。依 §8.4.1 **不自擬規則**：ER 斷言「有截斷且依該文件」，**其逐條符合性須以該文件覆核**，本條不代為判定。此為**上游文件依賴**，已記於上繳之獨立判斷 ——與「037 未產出 leaf」之情形不同，不援引 R-U56。 |

**reasoning**：驗證目標：5.15.1（ALLPR5.1）—— 過長之 username 依 Core HMI 之規則截斷。關鍵情境條件：username 須確實超出可顯示寬度，否則截斷不會發生而本條恆綠。為什麼這樣切：**可判定之部分只有「有沒有截斷」**；「截得對不對」之權威在外部文件，把它寫進 ER 等於把一個本文件無法判定之斷言偽裝成可判定。

---

### NR1L-UserProfiles-147 — SWE1-HMI-PROF-045（5.16 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR6.) A cloud icon will show next to the profile avatar on the All Profiles tab and Edit Profile tab if the profile is connected with an Connected account (See Connected Personal Account HMI).

**037 description**：ALLPR6.) A cloud icon will show next to the profile avatar on the All Profiles tab and Edit Profile tab if the profile is connected with an Connected account (See Connected Personal Account HMI).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Cloud icon marks Profiles linked to a Connected account |
| pre_conditions | 1. The vehicle is equipped with connectivity<br>2. Driver Profile A is connected with a Connected account<br>3. Driver Profile B is not connected with a Connected account<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and read the avatars of both Profiles<br>2. Open the “Edit Profile” tab of Driver Profile A and read its avatar |
| expected_result | 1. A cloud icon is next to the avatar of Driver Profile A and not next to Driver Profile B<br>2. A cloud icon is next to the avatar on the “Edit Profile” tab |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.16 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — connected 帳號之 cloud icon 標示 |
| remarks | **B profile 為對照** —— 只驗 A 有 icon 時，一個「所有 profile 都掛 cloud icon」之實作會通過；條文之 `if the profile is connected` 是**條件**，其判別力全在未連結者身上。**兩個分頁併驗**：條文一句列出 All Profiles 與 Edit Profile 兩處，依 §5.7 併為一條之兩個 ER 行。**本條之 label 依 RD #5 之答覆可能調整**（39 包作業 2 之命中：本節寫 `Connected account`）。 |

**reasoning**：驗證目標：5.16（ALLPR6）—— 與 Connected 帳號連結之 profile，其 avatar 旁顯示 cloud icon。關鍵情境條件：須同時存在已連結與未連結之 profile。為什麼這樣切：條文之 `(See Connected Personal Account HMI)` 指向他文件之**帳號連結流程**，本條不涉其如何連上，只驗**連上之後之標示**。

---

### NR1L-UserProfiles-148 — SWE1-HMI-PROF-046（6.1 / Defaults）

**spec 原文（`pdf_text`）**：

> NOPR0.) R1 High Only: this passage is not meant to be implemented. CPA will not be launched and it will be accessible from the Edit Profile screen only. Therefore, after choosing the avatar, the system will keep current preferences and will begin Tutorials (refer to Tutorials L&F)

**037 description**：NOPR0.) R1 High Only: this passage is not meant to be implemented. CPA will not be launched and it will be accessible from the Edit Profile screen only. Therefore, after choosing the avatar, the system will keep current preferences and will begin Tutorials (refer to Tutorials L&F)

| 欄 | 值 |
|---|---|
| tc_title / test_item | R1 High keeps preferences and begins Tutorials after avatar |
| pre_conditions | 1. The vehicle is an R1 High variant<br>2. A New Profile Setup is in progress at the avatar step<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the current preferences of the active Driver Profile<br>2. Choose an avatar and press Save & Continue<br>3. Read the screen shown after the avatar step<br>4. Read the preferences and compare them with those recorded in step 1 |
| expected_result | 1. The current preferences are recorded<br>2. The avatar is chosen and the avatar step ends<br>3. Tutorials begin and no Connected Personal Account login is launched<br>4. The preferences are unchanged from those recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.1 |
| design_method | 情境 / 用例 (Scenario / Use Case Testing) |
| priority | **P1** — R1 High 之流程分歧本身 —— 誤啟 CPA 即為錯誤變體行為 |
| remarks | **變體 axis `r1h-cpa-6.1`**：本條為 R1 High 側。base 側（`Is CPA present?` 為是時啟動 CPA 登入）**在 037 內無 leaf** —— 它只出現於 PDF p9 之流程圖，依 R-U56 不造，已於 `audit_variant_pairs.AXES` 由 `pending` 改為具名不配（述詞 `no-other-side-leaf` 實測）。條文尚有 `it will be accessible from the Edit Profile screen only` 一句 —— 該全稱之**反向**（他處不得進入 CPA）本條不涵蓋，其入口清單不可窮舉，已記為 ch11 之覆蓋事項（`SWE1-HMI-PROF-110` 為其正向）。 |

**reasoning**：驗證目標：6.1（NOPR0）—— R1 High 上 CPA 不啟動；選完 avatar 後保留現有偏好並進入 Tutorials。關鍵情境條件：車型須為 R1 High —— 本條之全部內容皆以此為前提。為什麼這樣切：`design_method` 取情境／用例 ——本條驗的是**一段流程之走向**（avatar → 不進 CPA → 進 Tutorials），非單一畫面之功能點。**ER4 之偏好比對不可省**：條文說的是 `keep current preferences`，一個「跳過 CPA 但把偏好重設為預設」之實作，只驗 Tutorials 有沒有開會通過（§8.3）。

---

### NR1L-UserProfiles-149 — SWE1-HMI-PROF-047（6.2 / Defaults）

**spec 原文（`pdf_text`）**：

> NOPR1.) At vehicle entry or initiation of a newly active Profile, there will be a Welcome popup. There will be prompts for the user to customize the default Profile(s) within the default Welcome Popup (see above).

**037 description**：NOPR1.) At vehicle entry or initiation of a newly active Profile, there will be a Welcome popup. There will be prompts for the user to customize the default Profile(s) within the default Welcome Popup (see above). (image: %E5%9C%96%E7%89%87_1670526527.png)

| 欄 | 值 |
|---|---|
| tc_title / test_item | Welcome popup at vehicle entry prompts to customize |
| pre_conditions | 1. Only the default Driver Profiles exist on the vehicle<br>2. The Welcome popup setting is on for the active Profile<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Switch the ignition on and read the screen<br>2. Read the popup and check the prompt to customize the Profile |
| expected_result | 1. A Welcome popup is displayed upon vehicle entry<br>2. The popup prompts the user to customize the default Driver Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.2 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P1** — 入車之 Welcome popup 與自訂提示；ch6 之入口 |
| remarks | **條文列兩個觸發**（`At vehicle entry` 與 `initiation of a newly active Profile`）。本條取**入車**一側；**新啟用 profile 一側由 `SWE1-HMI-PROF-023`（`NR1L-UserProfiles-118`）承擔** —— 該 leaf 為 5.3.1 之「切換 profile 後顯示 welcome popup」。§7 之列舉配對於此以跨節委派完成，非漏測。自訂提示之**按下之後**屬 6.4（`SWE1-HMI-PROF-052`），本條只驗提示之存在。 |

**reasoning**：驗證目標：6.2（NOPR1）—— 入車或新 profile 啟用時顯示 Welcome popup，且其中含自訂預設 profile 之提示。關鍵情境條件：現用者須為**預設** profile ——自訂提示之對象即為預設 profile，自訂者身上不成立。為什麼這樣切：本 leaf 之單位為**提示之存在**；popup 之按鈕組成屬 6.3（`SWE1-HMI-PROF-049`），兩者同一個 popup 而斷言不同，依 037 之切法各自成條。

---

### NR1L-UserProfiles-150 — SWE1-HMI-PROF-049（6.3 / Defaults）

**spec 原文（`pdf_text`）**：

> NOPR2.) Until popups are turned off, there will be a popup upon vehicle entry to informed the user which Profile is in use, with a button to switch users, and, for default Profile(s), a button to “Get Started” to customize the active Profile.

**037 description**：NOPR2.) Until popups are turned off, there will be a popup upon vehicle entry to informed the user which Profile is in use, with a button to switch users, and, for default Profile(s), a button to “Get Started” to customize the active Profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Welcome popup shows the Profile, Switch Users and Get Started |
| pre_conditions | 1. The active Driver Profile is a default Profile<br>2. The Welcome popup setting is on for that Profile<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Switch the ignition on and read the popup shown<br>2. Read the popup and check the Profile name and the buttons offered |
| expected_result | 1. A Welcome popup is displayed upon vehicle entry<br>2. The popup names the active Profile and offers Switch Users and Get Started |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.3 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P1** — Welcome popup 之內容與兩個入口 |
| remarks | **Get Started 只在預設 profile 上出現**（條文之 `for default Profile(s)`）。本條取預設一側；**自訂 profile 一側之popup 組成屬 7.2（`SWE1-HMI-PROF-058`），於第六批生成** ——此處不宣稱其已被驗。`Until popups are turned off` 為適用條件（§8.7.3），以 pre-condition 固定為「開啟」；**關閉之後之行為屬 `SWE1-HMI-PROF-051`**。 |

**reasoning**：驗證目標：6.3（NOPR2）—— Welcome popup 告知現用 profile，並提供 Switch Users 與（預設 profile 時）Get Started。關鍵情境條件：popup 設定須為開啟，且現用者為預設 profile。為什麼這樣切：三個內容項為**同一畫面之並列斷言**，§5.7 併驗；兩個按鈕**按下之後**之行為分屬 6.4／6.5，本條只驗其存在與 profile 名稱之正確。

---

### NR1L-UserProfiles-151 — SWE1-HMI-PROF-050-01（6.3.1 / Defaults）

**spec 原文（`pdf_text`）**：

> NOPR2.1) Selecting “X” on the default Welcome popup will lead to another popup with options of “Remind me Later” and “Don’t Show me Again”. Selecting “Remind me Later” will close the popup until the next time that Profile is activated. Clicking outside the Welcome popup will close the popup without asking “Remind me Later” and “Don’t Show me Again”.

**037 description**：Selecting “X” on the default Welcome popup will lead to another popup with options of “Remind me Later” and “Don’t Show me Again”. Selecting “Remind me Later” will close the popup until the next time that Profile is activated.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Remind me Later closes the popup until next activation |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle<br>2. The Welcome popup setting is off for Driver Profile B<br>3. The Welcome popup of Driver Profile A is displayed<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press X on the Welcome popup and read the popup shown<br>2. Select Remind me Later on that popup<br>3. Activate Driver Profile B<br>4. Activate Driver Profile A again and read the screen |
| expected_result | 1. A popup offering Remind me Later and Don’t Show me Again is displayed<br>2. The Welcome popup is closed<br>3. Driver Profile B is active<br>4. The Welcome popup of Driver Profile A is displayed again |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.3.1 |
| design_method | 狀態轉換 (State Transition Testing) |
| priority | **P2** — Remind me Later 之關閉範圍 |
| remarks | **ER4 是本條之重點**：條文說的是「關到**該 profile 下次被啟用**為止」—— 只驗「按了會關」，一個永久關閉之實作會通過（§8.3）。**刻意不斷言 key cycle 內之顯示與否**：「key-on 是否算一次 activation」條文未定義，依 §8.4.1 保留歧義，不以本條推定。`Don’t Show me Again` 之後果屬 `SWE1-HMI-PROF-051`。**X-1（切換 profile 觸發 5.3.1 之 PU0580）**：步驟 3 切到 B 會顯示 B 之 welcome popup，故 pre-condition 指定 B 之 Welcome popup 設定為關閉 ——使步驟 4 所見之 popup 必屬 A，不會與 B 之 popup 混淆。 |

**reasoning**：驗證目標：6.3.1（NOPR2.1）—— 按 X 後之二次 popup，選 Remind me Later 關閉至該 profile 下次啟用。關鍵情境條件：須有第二個 profile，否則「切走再切回」這個唯一無歧義之 activation 造不出來。為什麼這樣切：`design_method` 取狀態轉換 ——本條驗的是一個**壓抑狀態之建立與其解除**，而解除之條件正是條文所定之 activation。

---

### NR1L-UserProfiles-152 — SWE1-HMI-PROF-050-02（6.3.1 / Defaults）

**spec 原文（`pdf_text`）**：

> NOPR2.1) Selecting “X” on the default Welcome popup will lead to another popup with options of “Remind me Later” and “Don’t Show me Again”. Selecting “Remind me Later” will close the popup until the next time that Profile is activated. Clicking outside the Welcome popup will close the popup without asking “Remind me Later” and “Don’t Show me Again”.

**037 description**：Selecting “X” on the default Welcome popup will lead to another popup with options of “Remind me Later” and “Don’t Show me Again”. Clicking outside the Welcome popup will close the popup without asking “Remind me Later” and “Don’t Show me Again”.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Clicking outside closes the popup without asking |
| pre_conditions | 1. The Welcome popup of the active Profile is displayed<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the screen outside the Welcome popup<br>2. Read the screen and check which popups are displayed |
| expected_result | 1. The Welcome popup is closed<br>2. No popup offering Remind me Later and Don’t Show me Again is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.3.1 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P3** — 點擊外部關閉且不再詢問 |
| remarks | **ER2 為缺席斷言** —— 條文之 `without asking` 只能以「那個 popup 沒有出現」證之。與 `SWE1-HMI-PROF-050-01` 同節不同分支：按 X 與點擊外部之結果**相反**（一個問、一個不問），故 037 切為兩個 leaf，本條不與其併。 |

**reasoning**：驗證目標：6.3.1（NOPR2.1）末句 —— 點擊 popup 外部直接關閉，不出現 Remind me Later／Don’t Show me Again 之詢問。關鍵情境條件：Welcome popup 須在顯示中。為什麼這樣切：本條為**負向形態之斷言**，其判定不依賴二次 popup 之內容，故不因 RD 之 label 答覆而變（J-7）。

---

### NR1L-UserProfiles-153 — SWE1-HMI-PROF-051（6.3.2 / Defaults）

**spec 原文（`pdf_text`）**：

> NOPR2.2) Selecting “Don’t Show me Again” will turn off the setting for the “Welcome” popup for that Profile (which could be any Default or customized Profile).

**037 description**：NOPR2.2) Selecting “Don’t Show me Again” will turn off the setting for the “Welcome” popup for that Profile (which could be any Default or customized Profile).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Don’t Show me Again turns the popup off for that Profile |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle<br>2. The Welcome popup setting is on for both Profiles<br>3. The Welcome popup of Driver Profile A is displayed<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press X on the Welcome popup and read the popup shown<br>2. Select Don’t Show me Again and read the Welcome popup setting<br>3. Activate Driver Profile B and read the screen<br>4. Activate Driver Profile A again and read the screen |
| expected_result | 1. A popup offering Remind me Later and Don’t Show me Again is displayed<br>2. The Welcome popup setting of Driver Profile A is off<br>3. Driver Profile B is active and its Welcome popup is displayed<br>4. Driver Profile A is active and no Welcome popup is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.3.2 |
| design_method | 狀態轉換 (State Transition Testing) |
| priority | **P1** — Don’t Show me Again 關閉該 profile 之設定 —— **逐 profile 之範圍** |
| remarks | **ER3 是逐 profile 之隔離**：條文寫的是`turn off the setting … for that Profile`；一個把該設定存成**全域**之實作，只驗 A 不再顯示會通過（§8.3；同 `SWE1-HMI-PROF-018-02` 之 Z-1 形狀）。**ER4 與 `050-01` 之 ER4 相反** —— 兩條之判別力互為對照：Remind me Later 再啟用時回來，Don’t Show me Again 不回來。**X-1（切換 profile 觸發 5.3.1 之 PU0580）**：步驟 3 切到 B 所觸發之 welcome popup **即 ER3 所斷言者**，非未處理之干擾。 |

**reasoning**：驗證目標：6.3.2（NOPR2.2）—— 選 Don’t Show me Again 關閉**該 profile** 之 Welcome popup 設定。關鍵情境條件：須有第二個 profile 且其設定為開啟，逐 profile 之範圍方可觀察。為什麼這樣切：`design_method` 取狀態轉換 ——本條驗的是一個**持久設定之翻轉**，其效力須跨一次 profile 切換仍成立。

---

### NR1L-UserProfiles-154 — SWE1-HMI-PROF-052（6.4 / Defaults）

**spec 原文（`pdf_text`）**：

> NOPR3.) Pressing “Get Started” will initiate the New Profile Setup (but carry-over all current preferences linked to the active Profile, without a popup to confirm).

**037 description**：NOPR3.) Pressing “Get Started” will initiate the New Profile Setup (but carry-over all current preferences linked to the active Profile, without a popup to confirm).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Get Started starts setup and carries over preferences |
| pre_conditions | 1. The active Driver Profile is a default Profile<br>2. The Welcome popup with the Get Started button is displayed<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the current preferences of the active Driver Profile<br>2. Press Get Started on the Welcome popup<br>3. Read the screen and check that the New Profile Setup started<br>4. Read the preferences and compare them with those recorded in step 1 |
| expected_result | 1. The current preferences are recorded<br>2. The New Profile Setup is initiated<br>3. The first step of the New Profile Setup is displayed and no confirmation popup appeared<br>4. The preferences are unchanged from those recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.4 |
| design_method | 情境 / 用例 (Scenario / Use Case Testing) |
| priority | **P1** — Get Started 起始設定並沿用現有偏好 |
| remarks | **三個斷言各有其失效方式**：起始設定（ER2／ER3 前半）、**無確認 popup**（ER3 後半，條文之 `without a popup to confirm`）、**偏好沿用**（ER4）。缺任一者，條文之一部分即無人驗。設定流程本身之各步驟屬 ch8（`SWE1-HMI-PROF-066` 以下），本條只驗其**被起始**與偏好之沿用。 |

**reasoning**：驗證目標：6.4（NOPR3）—— 按 Get Started 起始 New Profile Setup，沿用現用 profile 之全部偏好，且不出現確認 popup。關鍵情境條件：現用者為預設 profile（Get Started 只在其上出現），且偏好須先記錄。為什麼這樣切：`design_method` 取情境／用例 ——本條跨 popup 與設定流程兩個畫面族。**ER3 之缺席斷言不可省**：條文特別標明「不出現確認 popup」，那是與 6.3.1 之詢問行為刻意對比之設計。

---

### NR1L-UserProfiles-155 — SWE1-HMI-PROF-054（6.5 / Defaults）

**spec 原文（`pdf_text`）**：

> NOPR4.) Pressing “Switch Users” will take the user to the “All Profiles” tab in the Profile Section.

**037 description**：NOPR4.) Pressing “Switch Users” will take the user to the “All Profiles” tab in the Profile Section.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Switch Users opens the All Profiles tab |
| pre_conditions | 1. The Welcome popup with the Switch Users button is displayed<br>2. The last used tab of the active Profile is the “Edit Profile” tab<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press Switch Users on the Welcome popup<br>2. Read the screen and check which tab of the Profile section is shown |
| expected_result | 1. The Welcome popup is closed and the Profile section is opened<br>2. The “All Profiles” tab is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.5 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P1** — Switch Users 之導向 |
| remarks | **pre-condition 刻意把上次分頁設為 “Edit Profile”** ——否則 5.1 之 latch（上次分頁）與本條之「固定到 All Profiles」會給出相同結果，兩者不可分辨。此設置亦使本條與 `SWE1-HMI-PROF-055`（導向上次分頁）之判別力各自成立。 |

**reasoning**：驗證目標：6.5（NOPR4）—— 按 Switch Users 進入 Profile 區之“All Profiles” 分頁。關鍵情境條件：上次分頁須**不是** “All Profiles”。為什麼這樣切：本 leaf 為單一導向斷言；切換 profile 之後續行為屬 5.3（`SWE1-HMI-PROF-022`），本條只到達分頁為止。

---

### NR1L-UserProfiles-156 — SWE1-HMI-PROF-055（6.6 / Defaults）

**spec 原文（`pdf_text`）**：

> NOPR5.) Pressing the Avatar or “Welcome [username]” text will take the user to the last known tab in the Profile section.

**037 description**：NOPR5.) Pressing the Avatar or “Welcome [username]” text will take the user to the last known tab in the Profile section.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Avatar and Welcome text open the last known tab |
| pre_conditions | 1. The Welcome popup of the active Profile is displayed<br>2. The last known tab of the active Profile is the “Edit Profile” tab<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the Avatar on the Welcome popup<br>2. Read the screen and check which tab is shown<br>3. Return to the Welcome popup and press the “Welcome [username]” text<br>4. Read the screen and check which tab is shown |
| expected_result | 1. The Profile section is opened<br>2. The “Edit Profile” tab, the last known tab, is displayed<br>3. The Profile section is opened again<br>4. The “Edit Profile” tab, the last known tab, is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.6 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — Avatar 與 Welcome 文字之導向（上次分頁） |
| remarks | **條文列兩個入口**（Avatar 與 `Welcome [username]` 文字），依 §7 兩者皆須走到 —— 故本條四步而非兩步。方括號 `[username]` **逐字引自 6.6**（§11 之 profile-scoped 例外，D-UP22-01；G19 對照來源列驗證）。上次分頁固定為 “Edit Profile”，使本條與 `SWE1-HMI-PROF-054`（固定到 All Profiles）之結果相反而可分辨。 |

**reasoning**：驗證目標：6.6（NOPR5）—— 按 Avatar 或 “Welcome [username]” 文字，進入 Profile 區之**上次分頁**。關鍵情境條件：上次分頁須**不是**預設分頁 “All Profiles”，否則與 5.1 之預設值不可分辨。為什麼這樣切：兩個入口為同一句之列舉，§7 要求皆走到；併為一條而非兩條，因其 ER 逐字相同、pre-condition 亦同 —— 分立只會產生一對雙胞胎。

---

