# 覆核用全文 — 第四批 26 條（34 包作業 3）

- 產出層：執行層｜2026-08-18｜**供分析層逐條覆核**
- 範圍：`NR1L-UserProfiles-109` ～ `134` —— **ch5 之 `PRACC` 群 25 leaf
  ＋ `030-01` 之反向配對 1**
- 格式同 21／23／29 輪（含 spec 原文、must_carry 與 037 description）

> 讀法：先讀「spec 原文」與「037 description」，再讀 ER ——
> **本檔要覆核的是「這句話對不對」**；「有沒有來源」為 `34_provenance5.md`
> （未溯得者 0）。

## 生成時已跑之五支對應關係掃描（結果見 `34_batch04.md` §3）

| 掃描 | 本批之待判／紅 |
|---|---|
| T-1（步驟 ↔ ER）| 0 |
| U-2（步驟 ↔ ER 反向）| 0 |
| U-1（斷言 ↔ 分支）| 3 待判，逐條判為綠 |
| V-1（步驟 ↔ 條文時序）| 2 待判，逐條判為綠 |
| W-1（前提 ↔ ER）| 0（本批未新增）|

共 **26 條**。

---

## NR1L-UserProfiles-109 — SWE1-HMI-PROF-018-01（5.1 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC7.) When in the Profile section, there will be two tabs; “All Profiles” and “Edit Profile”. The default tab is the “All Profiles” tab, but the system will latch on whichever tab was last used within and over key cycles, per Profile, when entered through pushing the Profile button. While in the Profile section and the user presses the Profile button again, the user will be taken to the All Profiles tab, if not already on that tab.

**037 description**：The default tab is the “All Profiles” tab.

| 欄 | 值 |
|---|---|
| tc_title / test_item | All Profiles is the default tab of the Profile section |
| pre_conditions | 1. The active Driver Profile has never opened the Profile section on this vehicle<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the Profile button in the status bar<br>2. Read the Profile section and check that the “All Profiles” tab is shown |
| expected_result | 1. The Profile section is opened<br>2. The “All Profiles” tab is the tab shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.1 |
| priority | **P2** — Profile 區之預設分頁；導覽之呈現 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | pre-condition 指定「該 profile 從未開過 Profile 區」——**否則 5.1 之 latch 行為（`SWE1-HMI-PROF-018-02`）會蓋過預設值**，測到的將是上次之分頁而非預設分頁。 |

**reasoning**：驗證目標：5.1（PRACC7）—— Profile 區之**預設**分頁為 “All Profiles”。關鍵情境條件：latch 行為以「上次用過之分頁」為準，故須以「從未開過」排除之，預設值方可觀察。為什麼這樣切：037 對 5.1 切三個 leaf；本 leaf 之單位為**預設值**，latch 屬 `SWE1-HMI-PROF-018-02`、再按回位屬 `SWE1-HMI-PROF-018-03`。

---

## NR1L-UserProfiles-110 — SWE1-HMI-PROF-018-02（5.1 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC7.) When in the Profile section, there will be two tabs; “All Profiles” and “Edit Profile”. The default tab is the “All Profiles” tab, but the system will latch on whichever tab was last used within and over key cycles, per Profile, when entered through pushing the Profile button. While in the Profile section and the user presses the Profile button again, the user will be taken to the All Profiles tab, if not already on that tab.

**037 description**：The system will latch on whichever tab was last used within and over key cycles, per Profile, when entered through pushing the Profile button.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Last used tab remembered per Profile across key cycles |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Activate Driver Profile A and open the “Edit Profile” tab<br>2. Switch the ignition off and then on again<br>3. Press the Profile button and check that the “Edit Profile” tab is shown |
| expected_result | 1. Driver Profile A is active and the “Edit Profile” tab is shown<br>2. The ignition is off and then on again with Driver Profile A active<br>3. The “Edit Profile” tab is shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.1 |
| priority | **P1** — 分頁選擇之跨 key cycle 記憶；逐 profile 之狀態保留 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | 條文之 latch 有兩個範圍（`within and over key cycles`）與一個**逐 profile** 之限定。本 TC 取**跨 key cycle** 一側 ——其為兩者中較難成立者（同一 key cycle 內之保留為其必要條件）。**逐 profile 之隔離未於本條驗**：另一 profile 之分頁是否互不影響，條文有述而 037 未為其另切 leaf ——依 **R-U56** 為 OUT-OF-SCOPE，不列缺口。 |

**reasoning**：驗證目標：5.1（PRACC7）之 latch —— 系統記住上次使用之分頁，跨 key cycle 仍然有效。關鍵情境條件：**須先離開預設分頁**（開 “Edit Profile”），否則 latch 與預設值之結果相同，無從分辨。為什麼這樣切：取跨 key cycle 一側；**若只驗同一 key cycle 內之保留，一個把分頁存在揮發性記憶體之實作會通過**。

---

## NR1L-UserProfiles-111 — SWE1-HMI-PROF-018-03（5.1 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC7.) When in the Profile section, there will be two tabs; “All Profiles” and “Edit Profile”. The default tab is the “All Profiles” tab, but the system will latch on whichever tab was last used within and over key cycles, per Profile, when entered through pushing the Profile button. While in the Profile section and the user presses the Profile button again, the user will be taken to the All Profiles tab, if not already on that tab.

**037 description**：While in the Profile section and the user presses the Profile button again, the user will be taken to the All Profiles tab, if not already on that tab.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Pressing the Profile button again returns to All Profiles |
| pre_conditions | 1. The Profile section is open on the “Edit Profile” tab<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the Profile button in the status bar<br>2. Read the Profile section and check that the “All Profiles” tab is shown |
| expected_result | 1. The Profile button is pressed while the “Edit Profile” tab is open<br>2. The “All Profiles” tab is shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.1 |
| priority | **P3** — 再按 Profile 鍵之回位；罕用導覽 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文之 `if not already on that tab` 為適用條件；本 TC 以 pre-condition 固定為「不在該分頁」，使回位可觀察。已在該分頁時再按之行為條文未述，依 §8.4.1 不推定。 |

**reasoning**：驗證目標：5.1（PRACC7）末句 —— 於 Profile 區內再按 Profile 鍵，回到 “All Profiles” 分頁。關鍵情境條件：起始須**不在**該分頁（§8.7.3 之條件本身）。為什麼這樣切：本 leaf 之單位為**再按之回位**；首次進入之分頁判定屬 `SWE1-HMI-PROF-018-01` 與 `SWE1-HMI-PROF-018-02`。

---

## NR1L-UserProfiles-112 — SWE1-HMI-PROF-019（5.1.1 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC7.1) When on the “All Profiles” tab, all available users will be shown. The active user will be highlighted and larger than the others. There will be options to add new Profiles, switch active Profiles, and go into Valet Mode.

**037 description**：PRACC7.1) When on the “All Profiles” tab, all available users will be shown. The active user will be highlighted and larger than the others. There will be options to add new Profiles, switch active Profiles, and go into Valet Mode.

| 欄 | 值 |
|---|---|
| tc_title / test_item | All Profiles tab shows every user and the three options |
| pre_conditions | 1. Three Driver Profiles exist on the vehicle<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab<br>2. Read the user list and check that every Profile is shown<br>3. Read the screen and check the three options offered |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. All three Driver Profiles are shown and the active one is highlighted and larger than the others<br>3. Options to add a new Profile, to switch the active Profile and to enter Valet Mode are present |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.1.1 |
| priority | **P1** — All Profiles 主畫面之內容與三個入口 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | **ER2 併驗 highlighted 與 larger 兩者** —— 條文寫的是`highlighted **and** larger than the others`；只驗其一，另一半失效不會被發現。profile 數（3）為**測試設置**（J-12）：條文只寫 all available users，未指定數目；取 3 是為使「其他人」為複數。 |

**reasoning**：驗證目標：5.1.1（PRACC7.1）—— All Profiles 分頁顯示全部使用者、現用者放大並 highlight，並提供三個入口。關鍵情境條件：至少三個 profile，使「其他人」為複數，`larger than the others` 方為可觀察之比較。為什麼這樣切：三個入口為同一畫面之並列斷言，依 §5.7 併為一條之 ER3。刻意略過：各入口按下後之行為分屬 5.3／5.6／12.x，本條只驗其**存在**。

---

## NR1L-UserProfiles-113 — SWE1-HMI-PROF-020-01（5.1.2 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC7.2) An icon and the following string will always show in the “All Profiles” screen: “This icon is associated to settings that are specific to your profile and are not shared across the vehicle”. All settings that are tied to the profile and are inside the settings screen will show this icon (both inside the My Profile tab and all the other tabs). This logic is not applicable for 7” screens.

**037 description**：For screens larger than 7", the “All Profiles” screen must permanently display a specific profile settings icon alongside the exact string: “This icon is associated to settings that are specific to your profile and are not shared across the vehicle”.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile-specific settings icon and string always on All Profiles |
| pre_conditions | 1. The vehicle screen is larger than 7 inches<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab<br>2. Read the screen and check the icon and its string |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. An icon is shown together with the string “This icon is associated to settings that are specific to your profile and are not shared across the vehicle” |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.1.2 |
| priority | **P2** — profile 專屬設定圖示與其說明字串之常駐 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文末句 `This logic is not applicable for 7” screens` 為**適用條件**（M-3 之三分法，非覆寫），故以 pre-condition 排除 7 吋。037 之 leaf 標題亦已載 `Large Screens`。字串逐字引自 5.1.2，未改寫（§8.4.1）。 |

**reasoning**：驗證目標：5.1.2（PRACC7.2）前半 —— “All Profiles” 畫面**恆**顯示該圖示與其字串。關鍵情境條件：螢幕大於 7 吋，否則本條不適用。為什麼這樣切：037 對 5.1.2 切兩個 leaf —— 本 leaf 為 **All Profiles 畫面上之常駐**，設定畫面內之標示屬 `SWE1-HMI-PROF-020-02`。

---

## NR1L-UserProfiles-114 — SWE1-HMI-PROF-020-02（5.1.2 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC7.2) An icon and the following string will always show in the “All Profiles” screen: “This icon is associated to settings that are specific to your profile and are not shared across the vehicle”. All settings that are tied to the profile and are inside the settings screen will show this icon (both inside the My Profile tab and all the other tabs). This logic is not applicable for 7” screens.

**037 description**：For screens larger than 7", any setting that is tied to a user profile must be marked with the aforementioned specific icon. This applies globally inside the settings screen, including both the “My Profile” tab and all other applicable tabs.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile-tied settings marked with the icon in the settings screen |
| pre_conditions | 1. The vehicle screen is larger than 7 inches<br>2. At least one profile-tied setting exists in the “My Profile” tab and one in another tab |
| input_test_data | NA |
| test_procedure | 1. Open the settings screen and the “My Profile” tab<br>2. Read the profile-tied setting and check for the icon<br>3. Open another settings tab and check that its profile-tied setting carries the icon |
| expected_result | 1. The settings screen is displayed on the “My Profile” tab<br>2. The profile-tied setting carries the icon<br>3. The profile-tied setting in the other tab also carries the icon |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.1.2 |
| priority | **P2** — 設定畫面內各 profile 專屬項之圖示標示 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文明言 `both inside the My Profile tab **and all the other tabs**` —— **ER 兩處併驗**：只驗 My Profile 一處，一個只在該分頁標圖示之實作會通過。 |

**reasoning**：驗證目標：5.1.2（PRACC7.2）後半 —— 設定畫面內所有繫於 profile 之設定項皆標該圖示，涵蓋 “My Profile” 分頁與其他分頁。關鍵情境條件：pre-condition 要求兩個分頁**各有**一個 profile 專屬設定，否則「其他分頁」一側無從觀察。為什麼這樣切：與 `SWE1-HMI-PROF-020-01` 之分野在**位置** ——前者為 All Profiles 畫面之常駐，本條為設定畫面內之逐項標示。

---

## NR1L-UserProfiles-115 — SWE1-HMI-PROF-021-02（5.2 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC8.) There can be up to five (5) Driver Profiles per vehicle, plus a Valet Mode Profile. When the Maximum number of Profiles (5) is reached,: the Add New Profile button will not be present, and the icon and the string described in note PRACC7.2 will not be present either. A text will be displayed instead informing the user they must first delete a Profile before creating a new one: “Max Profiles reached. Delete to create a new one.” (PU0584)

**037 description**：When the Maximum number of Profiles (5) is reached,: the Add New Profile button will not be present, and the icon and the string described in note PRACC7.2 will not be present either.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Add New button and icon hidden at the maximum Profile count |
| pre_conditions | 1. Five Driver Profiles exist on the vehicle<br>2. The vehicle screen is larger than 7 inches |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab<br>2. Read the screen and check that the Add New Profile button and the icon are absent |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. No Add New Profile button is present and neither the icon nor the string “This icon is associated to settings that are specific to your profile and are not shared across the vehicle” is shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.2; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.1.2 |
| priority | **P1** — 達上限時新增入口之隱藏；上限管理之分支 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | **ER 併驗按鈕與圖示／字串兩者** —— 條文寫的是`the Add New Profile button will not be present, **and** the icon and the string described in note PRACC7.2 will not be present either`。螢幕尺寸之 pre-condition 為使「圖示原本會在」成立（5.1.2 於 7 吋不適用）—— **否則圖示不在是因為螢幕，不是因為上限**。 |

**reasoning**：驗證目標：5.2（PRACC8）之中段 —— 達 5 個 profile 上限時，新增按鈕與 PRACC7.2 之圖示／字串皆不顯示。關鍵情境條件：螢幕須大於 7 吋 —— **這一點是本條之關鍵**：7 吋螢幕上該圖示本來就不顯示（5.1.2），屆時「圖示不在」證不了任何事。為什麼這樣切：037 對 5.2 切三個 leaf；上限之**數目**屬 `SWE1-HMI-PROF-021-01`（`NR1L-UserProfiles-003`），替代文字屬 `SWE1-HMI-PROF-021-03`。

---

## NR1L-UserProfiles-116 — SWE1-HMI-PROF-021-03（5.2 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC8.) There can be up to five (5) Driver Profiles per vehicle, plus a Valet Mode Profile. When the Maximum number of Profiles (5) is reached,: the Add New Profile button will not be present, and the icon and the string described in note PRACC7.2 will not be present either. A text will be displayed instead informing the user they must first delete a Profile before creating a new one: “Max Profiles reached. Delete to create a new one.” (PU0584)

**037 description**：When the Maximum number of Profiles (5) is reached,:A text will be displayed instead informing the user they must first delete a Profile before creating a new one: “Max Profiles reached. Delete to create a new one.” (PU0584)

| 欄 | 值 |
|---|---|
| tc_title / test_item | Max Profiles reached text shown in place of the Add New entry |
| pre_conditions | 1. Five Driver Profiles exist on the vehicle<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab<br>2. Read the screen and check the text shown in place of the Add New entry |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. The text “Max Profiles reached. Delete to create a new one.” (PU0584) is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.2 |
| priority | **P2** — 達上限時之替代文字（PU0584） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 字串與 PU id 逐字引自 5.2。與 `SWE1-HMI-PROF-021-02` 之分野：該條驗**什麼不見了**，本條驗**取而代之顯示了什麼** —— 兩者為同一情境之兩個斷言，037 切兩個 leaf 故不合併（§8.2.1）。 |

**reasoning**：驗證目標：5.2（PRACC8）末句 —— 達上限時改顯示一段告知使用者須先刪除之文字。關鍵情境條件：五個 profile 已存在（上限本身）。為什麼這樣切：**只驗「按鈕不見了」，一個什麼都不顯示之實作會通過** ——條文要求的是**替代顯示**，故本條必須獨立於 `021-02`。

---

## NR1L-UserProfiles-117 — SWE1-HMI-PROF-022（5.3 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC9.) When on the “All Profiles” tab, selecting another Profile username or avatar will switch system to that Profile and the newly active Profile will then be in the highlighted state.

**037 description**：PRACC9.) When on the “All Profiles” tab, selecting another Profile username or avatar will switch system to that Profile and the newly active Profile will then be in the highlighted state.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Selecting another Profile switches to it and highlights it |
| pre_conditions | 1. Two Driver Profiles exist and Driver Profile A is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and record which Profile is highlighted<br>2. Select the username of Driver Profile B<br>3. Read the tab and check that Driver Profile B is active and highlighted |
| expected_result | 1. Driver Profile A is highlighted and recorded as the active Profile<br>2. Driver Profile B is selected<br>3. Driver Profile B is the active Profile and is highlighted instead of the Profile recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.3 |
| priority | **P0** — 自 All Profiles 分頁切換 profile —— R-U5 核心五類之一 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | 條文之選取對象為 `Profile username **or** avatar` ——本 TC 取 username 一側；avatar 一側之觸發相同而**入口不同**，條文以 or 並列，**未另切 leaf**，故不另生成（§8.2.1）。**ER3 併驗「不再是步驟 1 所記者」** —— 只驗 B 被 highlight，一個把兩者都 highlight 之實作會通過。 |

**reasoning**：驗證目標：5.3（PRACC9）—— 於 All Profiles 分頁選取另一 profile，系統切換至該 profile 且其進入 highlight 狀態。關鍵情境條件：步驟 1 記錄原本被 highlight 者，使「highlight 移轉」而非「本來就 highlight」可分辨（§5.6）。為什麼這樣切：切換之**後續呈現**（載入訊息與 welcome popup）屬 `SWE1-HMI-PROF-023`；分頁停留屬 `SWE1-HMI-PROF-024`。

---

## NR1L-UserProfiles-118 — SWE1-HMI-PROF-023（5.3.1 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC9.1) When switched, the Profile loading (new message) will be shown, then the Welcome popup message for the newly selected Profile will show (if turned on for that Profile) for 5 seconds (which is different than on vehicle entry)(popup PU0580).

**037 description**：PRACC9.1) When switched, the Profile loading (new message) will be shown, then the Welcome popup message for the newly selected Profile will show (if turned on for that Profile) for 5 seconds (which is different than on vehicle entry)(popup PU0580).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Loading message then welcome popup shown after a switch |
| pre_conditions | 1. Two Driver Profiles exist and the welcome popup is turned on for Driver Profile B<br>2. Driver Profile A is active and the vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and select Driver Profile B<br>2. Read the screen and check that the Profile loading message is shown<br>3. Read the screen after loading and check the welcome popup and how long it stays |
| expected_result | 1. Driver Profile B is selected<br>2. The Profile loading message is shown<br>3. The welcome popup PU0580 for Driver Profile B is shown for 5 seconds |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.3.1 |
| priority | **P2** — 切換過程之載入訊息與 welcome popup |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文之 `(if turned on for that Profile)` 為適用條件，以 pre-condition 固定為已開啟 —— 否則 popup 不出現而本條假失敗。**順序為條文所載**（loading **then** welcome），ER2／ER3 依序斷言。`5 seconds` 與 `PU0580` 逐字引自 5.3.1。 |

**reasoning**：驗證目標：5.3.1（PRACC9.1）—— 切換後先顯示載入訊息，再顯示該 profile 之 welcome popup，持續 5 秒。關鍵情境條件：目標 profile 之 welcome popup 須為開啟狀態。為什麼這樣切：**兩個顯示之先後是條文明載者**，故 ER 分兩條依序斷言；併為一條會失去順序（同 `TC-088` 之理由）。刻意略過：條文之 `which is different than on vehicle entry` 為對照說明，其另一情境屬 ch7 之 welcome flow。

---

## NR1L-UserProfiles-119 — SWE1-HMI-PROF-024（5.3.2 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC9.2) If a Profile is switched while in the “All Profiles” tab, the screen will remain in the All Profiles tab (even if last known Profile tab was “Edit Profile” for newly active Profile).

**037 description**：PRACC9.2) If a Profile is switched while in the “All Profiles” tab, the screen will remain in the All Profiles tab (even if last known Profile tab was “Edit Profile” for newly active Profile).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Screen stays on All Profiles after switching Profile |
| pre_conditions | 1. Two Driver Profiles exist and the last used tab of Driver Profile B is the “Edit Profile” tab<br>2. Driver Profile A is active and the vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and select Driver Profile B<br>2. Read the screen and check that the “All Profiles” tab is shown |
| expected_result | 1. Driver Profile B is the active Profile<br>2. The “All Profiles” tab is still shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.3.2 |
| priority | **P2** — 切換後之分頁停留 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | **pre-condition 之「B 之上次分頁為 Edit Profile」是本條之關鍵** ——條文括號明言 `even if last known Profile tab was “Edit Profile” for newly active Profile`；不設此前提，本條與 latch（`SWE1-HMI-PROF-018-02`）之結果無從分辨。 |

**reasoning**：驗證目標：5.3.2（PRACC9.2）—— 於 All Profiles 分頁切換 profile 後，畫面仍停留在 All Profiles 分頁。關鍵情境條件：新 profile 之 latch 分頁**須為 Edit Profile** ——那是條文括號所指之情形，**也是唯一能證明本條之情境**：若 B 之上次分頁本來就是 All Profiles，停留與 latch 之結果相同。為什麼這樣切：本條與 `SWE1-HMI-PROF-018-02` 為**互相衝突之兩條規則**，037 各切一個 leaf；本條驗的是「切換情境下 5.3.2 勝過 latch」。

---

## NR1L-UserProfiles-120 — SWE1-HMI-PROF-025（5.3.3 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC9.3.) While a new Profile is loading, the user cannot try to select another profile.

**037 description**：PRACC9.3.) While a new Profile is loading, the user cannot try to select another profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Selecting another Profile blocked while one is loading |
| pre_conditions | 1. Three Driver Profiles exist on the vehicle<br>2. Driver Profile A is active and the vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and select Driver Profile B<br>2. Attempt to select Driver Profile C while Driver Profile B is still loading<br>3. Read the screen and check which Profile becomes active |
| expected_result | 1. Driver Profile B is selected and starts loading<br>2. The attempt to select Driver Profile C is not accepted<br>3. Driver Profile B is the active Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.3.3 |
| priority | **P1** — 載入中不得再選另一 profile；避免載入競態 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | **ER3 併驗「最後作用中者為 B」** —— 只驗「C 之選取不被接受」，一個把選取吞掉卻仍切到 C 之實作會通過。三個 profile 為**測試設置**（J-12）：條文只寫 another profile，取三個是為使「載入中之目標」與「被擋之目標」為不同兩者。 |

**reasoning**：驗證目標：5.3.3（PRACC9.3）—— 一個 profile 載入期間，使用者不能再選另一個。關鍵情境條件：須有第三個 profile 作為被擋之對象，否則「再選一個」與「重選同一個」混淆。為什麼這樣切：受測動作為載入期間之選取（§12 首匹配 → 負向測試）。刻意略過：載入之時長條文未述，本條不對其設限（§8.4.1）。

---

## NR1L-UserProfiles-121 — SWE1-HMI-PROF-026（5.4 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC10.) Editing a Profile is only available for the active Profile, in the “Edit Profile” tab. When on the All Profile Tab, pressing on the active Profile avatar or username after that Profile is already active and highlighted, will take the user to the “Edit Profile” tab.

**037 description**：PRACC10.) Editing a Profile is only available for the active Profile, in the “Edit Profile” tab. When on the All Profile Tab, pressing on the active Profile avatar or username after that Profile is already active and highlighted, will take the user to the “Edit Profile” tab.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Pressing the active Profile opens the Edit Profile tab |
| pre_conditions | 1. Driver Profile A is active and highlighted on the “All Profiles” tab<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the avatar of the active Driver Profile<br>2. Read the screen and check which tab is shown |
| expected_result | 1. The avatar of the active Driver Profile is pressed<br>2. The “Edit Profile” tab is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.4 |
| priority | **P2** — 自現用 profile 進入 Edit Profile 之入口 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文首句 `Editing a Profile is **only** available for the active Profile` 為**全稱限制**。其反向由 `SWE1-HMI-PROF-022` 承擔 —— 該 leaf 驗「選取另一個 profile 會 switch system to that Profile」，即「不進入編輯」之另一面。 |

**reasoning**：驗證目標：5.4（PRACC10）後半 —— 於 All Profiles 分頁按下**已作用中且已 highlight** 之 profile，進入 “Edit Profile” 分頁。關鍵情境條件：條文明言 `after that Profile is already active and highlighted`，故 pre-condition 固定之。為什麼這樣切：**「只能編輯現用 profile」之限制不另立 TC** ——按非現用者之行為由 5.3 定義為切換，`SWE1-HMI-PROF-022` 已驗其確實切換而非進入編輯。

---

## NR1L-UserProfiles-122 — SWE1-HMI-PROF-027-01（5.5 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC11.) The Memory seat status displayed under each applicable Profile avatar will show which memory seat number is programmed to which Profile. The number of Memory seats will be vehicle dependent (currently up to 3). When the number of Profiles exceeds the number of Memory seats on a vehicle, the New Profile(s) will not be linked to any memory seats unless the user initiates a swap of Memory seat preferences (at least two out of the five profiles will not be associated with a Memory seat preference). Valet Mode Profile will not be allowed to link to Memory seat positions.

**037 description**：The system must display the programmed memory seat number under each applicable Profile's avatar to indicate which seat position is linked to that specific Profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Memory seat number shown under the linked Profile avatar |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. Driver Profile A is linked to a memory seat position |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab<br>2. Read the area under the avatar of Driver Profile A and check the memory seat number shown |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. The memory seat number linked to Driver Profile A is shown under its avatar |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.5 |
| priority | **P2** — 記憶座椅編號於 avatar 下之呈現 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | ER 不寫座椅編號之數值 —— 條文只述「顯示哪一個座椅編號連到哪一個 profile」，**未指定編號**；寫死數值會使本 TC 只能在特定佈署上跑。 |

**reasoning**：驗證目標：5.5（PRACC11）首句 —— 每個適用 profile 之 avatar 下方顯示其所連之記憶座椅編號。關鍵情境條件：至少一個 profile 已連座椅，否則無可顯示者。為什麼這樣切：037 對 5.5 切三個 leaf —— 本 leaf 為**呈現**；超出座椅數之預設不連結屬 `SWE1-HMI-PROF-027-02`，Valet 之限制屬 `SWE1-HMI-PROF-027-03`。

---

## NR1L-UserProfiles-123 — SWE1-HMI-PROF-027-02（5.5 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC11.) The Memory seat status displayed under each applicable Profile avatar will show which memory seat number is programmed to which Profile. The number of Memory seats will be vehicle dependent (currently up to 3). When the number of Profiles exceeds the number of Memory seats on a vehicle, the New Profile(s) will not be linked to any memory seats unless the user initiates a swap of Memory seat preferences (at least two out of the five profiles will not be associated with a Memory seat preference). Valet Mode Profile will not be allowed to link to Memory seat positions.

**037 description**：The number of memory seats is vehicle-dependent (up to 3). When the total number of created Profiles exceeds the available physical memory seats, any newly created Profile(s) shall default to having NO memory seat linked. To link a seat to these new profiles, the user must explicitly initiate a "swap" of memory seat preferences.

| 欄 | 值 |
|---|---|
| tc_title / test_item | New Profile gets no memory seat when seats are outnumbered |
| pre_conditions | 1. The vehicle has 3 memory seats and each is linked to a Driver Profile<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Create one more Driver Profile<br>2. Open the “All Profiles” tab<br>3. Read the area under the new Profile avatar and check its memory seat status |
| expected_result | 1. The new Driver Profile is created<br>2. The “All Profiles” tab is displayed<br>3. No memory seat is linked to the new Driver Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.5 |
| priority | **P1** — profile 數超過座椅數時之預設不連結 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 座椅數（3）取自條文之 `currently up to 3`，非自擬。條文另載 `unless the user initiates a swap of Memory seat preferences` —— 該互換屬 9.5.x 之 leaf，本條不代測。 |

**reasoning**：驗證目標：5.5（PRACC11）中段 —— profile 數超過車上記憶座椅數時，新建之 profile 預設不連任何座椅。關鍵情境條件：**全部座椅皆已被連走**，否則新 profile 不連座椅可能只是因為還有空位。為什麼這樣切：本 leaf 之單位為**新 profile 之預設不連結**；互換之途徑屬他節，具名不代測。

---

## NR1L-UserProfiles-124 — SWE1-HMI-PROF-027-03（5.5 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC11.) The Memory seat status displayed under each applicable Profile avatar will show which memory seat number is programmed to which Profile. The number of Memory seats will be vehicle dependent (currently up to 3). When the number of Profiles exceeds the number of Memory seats on a vehicle, the New Profile(s) will not be linked to any memory seats unless the user initiates a swap of Memory seat preferences (at least two out of the five profiles will not be associated with a Memory seat preference). Valet Mode Profile will not be allowed to link to Memory seat positions.

**037 description**：Valet Mode Profile will not be allowed to link to Memory seat positions.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode Profile cannot be linked to a memory seat |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. A Valet Mode Profile is present and at least one memory seat is unlinked |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” screen for the Valet Mode Profile<br>2. Attempt to link the unlinked memory seat to the Valet Mode Profile<br>3. Read the seat links and check that the Valet Mode Profile holds none |
| expected_result | 1. The Valet Mode Profile screen is displayed<br>2. The attempt is not accepted<br>3. No memory seat position is linked to the Valet Mode Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.5 |
| priority | **P1** — Valet Mode Profile 不得連結座椅位置 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | **ER3 斷言「一個都沒有」而非「這一個沒連上」** ——後者容許實作改連到別的座椅位置，那同樣違反條文（同 `NR1L-UserProfiles-105` 之形狀）。若該畫面根本不提供連結入口，步驟 2 之「嘗試」即為「找不到入口」，ER2 仍成立 —— **條文說的是不得連結，未規定以何種方式阻止**。 |

**reasoning**：驗證目標：5.5（PRACC11）末句 —— Valet Mode Profile 不得連結記憶座椅位置。關鍵情境條件：須有未被連走之座椅，否則「不得連」與「沒得連」混淆。為什麼這樣切：受測動作為一個**不被允許之連結**（§12 首匹配 → 負向）。**ER3 為全稱形式**：該 profile 之座椅連結數恆為零。

---

## NR1L-UserProfiles-125 — SWE1-HMI-PROF-028（5.6 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC12.) Choosing the “Add New” text or the “+” icon will initiate the new Profile setup process. Completing a new Profile Setup means that the new Profile becomes the active Profile. Adding a new Profile from the “All Profiles” tab will return the user to the All Profiles tab after setup is complete.

**037 description**：PRACC12.) Choosing the “Add New” text or the “+” icon will initiate the new Profile setup process. Completing a new Profile Setup means that the new Profile becomes the active Profile. Adding a new Profile from the “All Profiles” tab will return the user to the All Profiles tab aft er setup is complete.

| 欄 | 值 |
|---|---|
| tc_title / test_item | New Profile setup from All Profiles ends on that tab |
| pre_conditions | 1. Fewer than five Driver Profiles exist on the vehicle<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and press the “Add New” text<br>2. Complete the new Profile setup process<br>3. Read the active Profile and check that it is the new one<br>4. Read the screen and check that the “All Profiles” tab is shown |
| expected_result | 1. The new Profile setup process is initiated<br>2. The new Profile setup is completed<br>3. The new Driver Profile is the active Profile<br>4. The “All Profiles” tab is shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.6 |
| priority | **P0** — 自 All Profiles 分頁建立新 profile —— 核心五類之一 |
| design_method | 情境 / 用例 (Scenario / Use Case Testing) |
| remarks | 條文三句為**同一次流程之三個結果**（啟動／成為現用／回到該分頁），依 §5.7 併為一條；其跨越四個步驟與兩個功能（建立與導覽），故 design_method 取情境／用例（§12）。`“Add New”` 與 `“+”` 為條文並列之兩個入口，本 TC 取前者；後者之觸發相同，**037 未另切 leaf**，故不另生成。 |

**reasoning**：驗證目標：5.6（PRACC12）—— 自 All Profiles 分頁啟動新 profile 設定，完成後新 profile 成為現用者，且畫面回到 All Profiles 分頁。關鍵情境條件：profile 數須未達上限，否則入口不存在（5.2）。為什麼這樣切：**ER3 與 ER4 缺一不可** ——只驗「回到分頁」，一個沒把新 profile 設為現用之實作會通過；只驗「成為現用」，一個停在設定畫面之實作會通過。

---

## NR1L-UserProfiles-126 — SWE1-HMI-PROF-029（5.6.1 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC12.1) The “Add New” text or the “+” icon will be greyed out while the vehicle is in motion. If selected, a bonk tone will be played along with the message “Function not available while vehicle in Motion.”

**037 description**：PRACC12.1) The “Add New” text or the “+” icon will be greyed out while the vehicle is in motion. If selected, a bonk tone will be played along with the message “Function not available while vehicle in Motion.”

| 欄 | 值 |
|---|---|
| tc_title / test_item | Add New greyed out and blocked while the vehicle moves |
| pre_conditions | 1. Fewer than five Driver Profiles exist on the vehicle<br>2. The “All Profiles” tab is open |
| input_test_data | NA |
| test_procedure | 1. Read the “Add New” text and record whether it is selectable<br>2. Bring the vehicle into motion<br>3. Select the greyed-out “Add New” text and check that a bonk tone and a message are given |
| expected_result | 1. The “Add New” text is selectable and its state is recorded<br>2. The vehicle is in motion and the “Add New” text is greyed out<br>3. The selection is not accepted, a bonk tone is played and the message “Function not available while vehicle in Motion.” is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.6.1 |
| priority | **P0** — 行車中不得新增 profile —— **防線成立本身**（§10.2 safety；D-UP16-01 附二） |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | **ER3 併驗「不被接受」與「提示」兩者** —— 依 P-1 之分野（§8.7.4：視覺狀態不蘊含不可操作），**變灰本身不是防線**；**防線是「按下不生效」**，故其斷言不可省。訊息字串逐字引自 5.6.1。基準線（行車前可選）為 §5.6 之要求。 |

**reasoning**：驗證目標：5.6.1（PRACC12.1）—— 行車中 “Add New” 變灰；若被選取則播 bonk 並顯示不可用訊息。關鍵情境條件：步驟 1 之基準線使「變灰」與「本來就不可選」可分辨（§5.6）。為什麼這樣切：受測動作為對已變灰項目之按壓（§12 首匹配 → 負向測試）。**判級 P0**：行車中不得新增 profile 為分心防線，其**成立本身**（按下不生效）之斷言落在 ER3 前半（D-UP16-01 附二）。

---

## NR1L-UserProfiles-127 — SWE1-HMI-PROF-030-01（5.7 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC13.) Linking a Profile to a memory seat can only be done through the Edit Profile screen (unless it is linked by default). If the seat position is saved, it will not automatically save to the active Profile.

**037 description**：Unless it is linked by default, manually linking a Profile to a memory seat can only be done through the "Edit Profile" screen.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Memory seat linked to a Profile from the Edit Profile screen |
| pre_conditions | 1. Driver Profile A is active and has no memory seat linked<br>2. At least one memory seat position is unlinked |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” screen for Driver Profile A<br>2. Link the unlinked memory seat position to Driver Profile A<br>3. Read the seat links and check that the position is linked to Driver Profile A |
| expected_result | 1. The “Edit Profile” screen is displayed<br>2. The link is accepted<br>3. The memory seat position is linked to Driver Profile A |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.7 |
| priority | **P1** — 座椅連結之唯一入口；連結途徑之限制 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | §7 之列舉配對：反向為 `NR1L-UserProfiles-133`（自 Edit Profile 以外之途徑連結不成立）。條文之 `can **only** be done through the Edit Profile screen` 為**全稱限制** —— **只驗此處連得成，不足以證「只能」**。`(unless it is linked by default)` 為適用條件，以 pre-condition 之「A 尚未連任何座椅」排除預設連結之情形。 |

**reasoning**：驗證目標：5.7（PRACC13）首句之正向 —— 經 Edit Profile 畫面可將profile 連結至記憶座椅。關鍵情境條件：A 尚未連座椅且有空位，使連結之效果可觀察。為什麼這樣切：條文之限制詞為 `only`，**其反向由 `NR1L-UserProfiles-133` 承擔**；兩條並存才擋得住一個允許自他處連結之實作（§7）。

---

## NR1L-UserProfiles-128 — SWE1-HMI-PROF-030-02（5.7 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC13.) Linking a Profile to a memory seat can only be done through the Edit Profile screen (unless it is linked by default). If the seat position is saved, it will not automatically save to the active Profile.

**037 description**：If a memory seat position is saved, the system must not automatically save or link that seat position to the currently active Profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Saving a seat position does not link it to the active Profile |
| pre_conditions | 1. Driver Profile A is active and has no memory seat linked<br>2. A memory seat position is linked to Driver Profile B |
| input_test_data | NA |
| test_procedure | 1. Change the seat position<br>2. Save the position to the memory seat linked to Driver Profile B<br>3. Read the seat links and check that Driver Profile A still has none |
| expected_result | 1. The seat position is changed<br>2. The position is saved to the memory seat linked to Driver Profile B<br>3. No memory seat is linked to Driver Profile A |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.7 |
| priority | **P1** — 存座椅位置不得自動連到現用 profile |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文之 `it will not automatically save to the active Profile` 為**缺席斷言**；其正向（存到原本連結之 profile）屬 `SWE1-HMI-PROF-033`（5.10）。本條之 pre-condition 使 A（現用）原本無座椅 ——**若 A 本來就有座椅，「沒有自動連過去」無從觀察**。 |

**reasoning**：驗證目標：5.7（PRACC13）末句 —— 儲存座椅位置時，不會自動把該位置連到現用 profile。關鍵情境條件：現用 profile 原本**無**座椅連結，使「自動連過去」若發生即可見。為什麼這樣切：與 `SWE1-HMI-PROF-033` 之分野在斷言方向 ——該條驗**存到誰**（原連結者），本條驗**沒存到誰**（現用者）。

---

## NR1L-UserProfiles-129 — SWE1-HMI-PROF-031（5.8 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC14.) If the Profile is switched while the vehicle is in motion, the memory seat position will not change. A popup will indicate to the user that the seat could not adjust while the vehicle is in motion.

**037 description**：PRACC14.) If the Profile is switched while the vehicle is in motion, the memory seat position will not change. A popup will indicate to the user that the seat could not adjust while the vehicle is in motion.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Seat does not move when the Profile switches during motion |
| pre_conditions | 1. Two Driver Profiles exist, each linked to a different memory seat position<br>2. Driver Profile A is active and the vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read and record the current seat position<br>2. Bring the vehicle into motion<br>3. Switch to Driver Profile B and check that the seat position is unchanged |
| expected_result | 1. The current seat position is recorded<br>2. The vehicle is in motion<br>3. The seat position matches the position recorded in step 1 and a popup indicates that the seat could not adjust while the vehicle is in motion |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.8 |
| priority | **P0** — 行車中座椅不得移動 —— **防線成立本身**（§10.2 safety） |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | **ER3 併驗「座椅未動」與「提示」兩者** —— 前者為防線本身（§8.7.4 之分野），後者為其呈現；**只驗提示，一個顯示提示卻仍移動座椅之實作會通過**。popup 之 PU id 條文未給，故 ER 只述其**內容要旨**，不寫 PU 編號（§8.4.1 不推定）。 |

**reasoning**：驗證目標：5.8（PRACC14）—— 行車中切換 profile 時座椅位置不變，並以 popup 告知無法調整。關鍵情境條件：兩 profile 各連**不同**座椅位置 ——位置相同則「座椅未動」與「本來就一樣」無從分辨。**判級 P0**：行車中座椅不得移動為安全防線，其成立本身之斷言落在 ER3 前半（D-UP16-01 附二）。

---

## NR1L-UserProfiles-130 — SWE1-HMI-PROF-033（5.10 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC16.) Saving a new seat position through the memory seat set/save hard or soft controls will save that seat position to whichever Driver Profile is already linked to the associated memory seat.

**037 description**：PRACC16.) Saving a new seat position through the memory seat set/save hard or soft controls will save that seat position to whichever Driver Profile is already linked to the associated memory seat.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Saved seat position goes to the Profile linked to that seat |
| pre_conditions | 1. Driver Profile B is linked to a memory seat position<br>2. Driver Profile B is the active Profile |
| input_test_data | NA |
| test_procedure | 1. Change the seat position and record the new position<br>2. Save the position to the memory seat linked to Driver Profile B<br>3. Read the seat position stored for Driver Profile B and check that it matches |
| expected_result | 1. The new seat position is recorded<br>2. The position is saved to the memory seat linked to Driver Profile B<br>3. The seat position stored for Driver Profile B matches the position recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.10 |
| priority | **P1** — 存座椅位置之歸屬；儲存機制之對象判定 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 本條以**現用者即該座椅之連結者**為前提 ——現用者非連結者之情形屬 5.10.1（`SWE1-HMI-PROF-034-01`～`-03`），其行為不同（會先詢問）。 |

**reasoning**：驗證目標：5.10（PRACC16）—— 以記憶座椅之 set/save 控制儲存新位置時，存到**已連結該座椅**之 profile。關鍵情境條件：現用者與該座椅之連結者相同，使本條與 5.10.1 之詢問流程不重疊。為什麼這樣切：與 `SWE1-HMI-PROF-030-02` 之分野 ——該條驗**沒存到現用者**，本條驗**存到了連結者**。

---

## NR1L-UserProfiles-131 — SWE1-HMI-PROF-034-01（5.10.1 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC16.1) If a new seat position is saved to a Profile that is not currently active, a popup will prompt the user if they would like to switch their seat preference to the newly saved memory seat number (PU0588). If the user chooses yes, the previous Profile linked to this seat position will move to “None”, and if there is no seat position already linked to the active Profile the new seat preference will save for that Profile. If the active user chooses yes, and if they already have a memory seat position associated with their Profile, the original seat assignment for the active Profile will move to the next available Profile (prioritizing from left to right based on the order of the Profiles on the All Profiles Tab).

**037 description**：If a new seat position is saved to a memory seat number that is currently linked to a different (non-active) Profile, the system must display popup PU0588 prompting the user if they want to switch their seat preference to the newly saved memory seat number.

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU0588 prompt when saving a seat linked to another Profile |
| pre_conditions | 1. Driver Profile A is active and Driver Profile B is linked to a memory seat position<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Change the seat position<br>2. Save the position to the memory seat linked to Driver Profile B<br>3. Read the screen and check that PU0588 asks about switching the seat preference |
| expected_result | 1. The seat position is changed<br>2. The position is saved to the memory seat linked to Driver Profile B<br>3. PU0588 is displayed and asks whether to switch the seat preference to the newly saved memory seat number |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.10.1 |
| priority | **P2** — 跨 profile 存座椅時之詢問（PU0588） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | pre-condition 使**現用者非該座椅之連結者** ——那是 5.10.1 之觸發條件本身；現用者即連結者之情形屬 5.10。本條只驗**詢問出現**；選 Yes 之後果分屬 `SWE1-HMI-PROF-034-02`（現用者原無座椅）與 `-03`（原有座椅）。 |

**reasoning**：驗證目標：5.10.1（PRACC16.1）首句 —— 將新座椅位置存到**非現用** profile 所連之座椅時，以 PU0588 詢問是否改用該座椅。關鍵情境條件：現用者與該座椅之連結者**不同**，此為觸發條件。為什麼這樣切：037 對 5.10.1 切三個 leaf —— 詢問／兩種 Yes 之後果。

---

## NR1L-UserProfiles-132 — SWE1-HMI-PROF-034-02（5.10.1 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC16.1) If a new seat position is saved to a Profile that is not currently active, a popup will prompt the user if they would like to switch their seat preference to the newly saved memory seat number (PU0588). If the user chooses yes, the previous Profile linked to this seat position will move to “None”, and if there is no seat position already linked to the active Profile the new seat preference will save for that Profile. If the active user chooses yes, and if they already have a memory seat position associated with their Profile, the original seat assignment for the active Profile will move to the next available Profile (prioritizing from left to right based on the order of the Profiles on the All Profiles Tab).

**037 description**：If the user chooses "Yes" on PU0588, and the active Profile does not currently have a memory seat linked, the new seat preference will save to the active Profile, and the previous Profile linked to this seat position will have its seat status moved to "None".

| 欄 | 值 |
|---|---|
| tc_title / test_item | Yes on PU0588 moves the seat to an unlinked active Profile |
| pre_conditions | 1. Driver Profile A is active and has no memory seat linked<br>2. Driver Profile B is linked to the memory seat position under test |
| input_test_data | NA |
| test_procedure | 1. Change the seat position and save it to the memory seat linked to Driver Profile B<br>2. Select Yes on PU0588<br>3. Read the seat links of both Profiles and check where the seat now belongs |
| expected_result | 1. PU0588 is displayed<br>2. Yes is selected on PU0588<br>3. The memory seat position is linked to Driver Profile A and the seat status of Driver Profile B is “None” |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.10.1 |
| priority | **P1** — 改派後之座椅歸屬（現用 profile 原無座椅） |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | **ER3 併驗兩側** —— A 得到該座椅、**且** B 之狀態變為 “None”；只驗 A 得到，一個讓兩個 profile 同時連著該座椅之實作會通過。`“None”` 逐字引自 5.10.1。與 `SWE1-HMI-PROF-034-03` 之分野：本條之現用者**原無**座椅。 |

**reasoning**：驗證目標：5.10.1（PRACC16.1）中段 —— 使用者選 Yes 且現用 profile 原本沒有連座椅時，該座椅改連現用 profile，原連結者變為 “None”。關鍵情境條件：現用者原本**無**座椅 —— 那是本 leaf 與 `-03` 之分界。為什麼這樣切：兩個結果（A 得到、B 變 None）為同一次選擇之兩面，依 §5.7 併於一條 ER。

---

## NR1L-UserProfiles-133 — SWE1-HMI-PROF-034-03（5.10.1 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC16.1) If a new seat position is saved to a Profile that is not currently active, a popup will prompt the user if they would like to switch their seat preference to the newly saved memory seat number (PU0588). If the user chooses yes, the previous Profile linked to this seat position will move to “None”, and if there is no seat position already linked to the active Profile the new seat preference will save for that Profile. If the active user chooses yes, and if they already have a memory seat position associated with their Profile, the original seat assignment for the active Profile will move to the next available Profile (prioritizing from left to right based on the order of the Profiles on the All Profiles Tab).

**037 description**：If the active user chooses "Yes" on PU0588 and they already have a memory seat associated with their Profile, the previous owner of the target seat moves to "None", the newly saved seat will link to the active Profile, and the original seat assignment of the active Profile will cascade/move to the next available Profile (prioritizing from left to right based on the order of the Profiles on the All Profiles Tab).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Yes on PU0588 passes the old seat to the next Profile |
| pre_conditions | 1. Driver Profile A is active and already linked to its own memory seat position<br>2. Driver Profile B is linked to the memory seat position under test and a further Profile has no seat linked |
| input_test_data | NA |
| test_procedure | 1. Change the seat position and save it to the memory seat linked to Driver Profile B<br>2. Select Yes on PU0588<br>3. Read the seat links of all Profiles and check where each seat now belongs |
| expected_result | 1. PU0588 is displayed<br>2. Yes is selected on PU0588<br>3. The memory seat position under test is linked to Driver Profile A, the seat status of Driver Profile B is “None” and the original seat of Driver Profile A is linked to the leftmost Profile without a seat |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.10.1 |
| priority | **P1** — 改派後之座椅歸屬（現用 profile 原有座椅） |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | **三個變動併於 ER3** —— 目標座椅改連 A、B 變 “None”、A 之原座椅改派給最左之無座椅 profile。條文之 `prioritizing from left to right based on the order of the Profiles on the All Profiles Tab` 使「最左」為明確對象 ——**只驗「改派給某人」，一個隨機挑選之實作會通過**（同 `NR1L-UserProfiles-097` 之理由）。pre-condition 要求另有一個無座椅之 profile，否則改派無對象。 |

**reasoning**：驗證目標：5.10.1（PRACC16.1）末句 —— 現用 profile **已有**座椅時選 Yes，其原座椅改派給下一個可用 profile（由左至右）。關鍵情境條件：須另有無座椅之 profile 作為改派對象。為什麼這樣切：與 `SWE1-HMI-PROF-034-02` 之分野在現用者**原有無座椅**；兩者為條文之兩個分支，037 各切一個 leaf。

---

## NR1L-UserProfiles-134 — SWE1-HMI-PROF-030-01-neg（5.7 / Profile List）

**spec 原文（`pdf_text`）**：

> PRACC13.) Linking a Profile to a memory seat can only be done through the Edit Profile screen (unless it is linked by default). If the seat position is saved, it will not automatically save to the active Profile.

**037 description**：Unless it is linked by default, manually linking a Profile to a memory seat can only be done through the "Edit Profile" screen.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Memory seat link refused outside the Edit Profile screen |
| pre_conditions | 1. Driver Profile A is active and has no memory seat linked<br>2. At least one memory seat position is unlinked |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and read its entries<br>2. Attempt to link the unlinked memory seat position from outside the “Edit Profile” screen<br>3. Read the seat links and check that Driver Profile A still has none |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. The attempt is not accepted<br>3. No memory seat position is linked to Driver Profile A |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.7 |
| priority | **P1** — 座椅連結之唯一入口 —— 全稱限制之反向 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | §7 之列舉配對：正向為 `NR1L-UserProfiles-127`（`SWE1-HMI-PROF-030-01`，自 Edit Profile 連得成）。條文之 `can **only** be done through the Edit Profile screen` 為全稱限制 —— **只驗正向不足以證之**，故另立本條（同 `009`／`105` 之形狀）。**若他處根本不提供連結入口，步驟 2 即為「找不到入口」，ER2 仍成立** —— 條文說的是不得自他處連結，未規定以何種方式阻止。 |

**reasoning**：驗證目標：5.7（PRACC13）之 `only` —— 記憶座椅之連結**不得**經 Edit Profile 以外之途徑完成。關鍵情境條件：A 無座椅且有空位，使「連上了」若發生即可見。為什麼這樣切：**全稱之限制只能以反向證之** ——正向（自 Edit Profile 連得成）與「他處也連得成」相容，故 `SWE1-HMI-PROF-030-01` 之正向不足以擋下該實作（§7）。**ER3 斷言「一個都沒連上」** 而非「這一次沒成功」，以排除連到別的座椅之實作。

---
