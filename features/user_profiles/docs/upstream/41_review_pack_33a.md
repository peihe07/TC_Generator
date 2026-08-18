# 覆核用全文 ＋ ER 出處對照 — 第六批 前半（`157`–`173`）

- 產出層：執行層｜2026-08-18｜**供分析層逐條覆核**
- 本檔 **17 條**；另半在 `41_review_pack_33b.md`
- 由 `scripts/build_review_pack.py` 產生，不經人手轉錄

> 讀法：先讀「spec 原文」與「037 description」，再讀 ER ——
> 「這句話對不對」是本檔要問的；「這句話有沒有來源」見 §0 之出處對照。

## 0. ER 出處對照

| 項 | 數 |
|---|---|
| 引號字面值（ER ＋ pre_conditions）| **3** |
| 逐字溯得到被引之節或其 must_carry | **1** |
| 經 `UI_LOCATORS` 登記表溯源 | **2** |
| **未溯得者** | **0** |
| 全條無引號字面值者 | **16 條** |

| tc_id | 節 | 字面值 | 欄位 | 出處 |
|---|---|---|---|---|
| `NR1L-UserProfiles-161` | 7.3 | 「All Profiles」| ER | 逐字見於 **7.3** |
| `NR1L-UserProfiles-161` | 7.3 | 「Edit Profile」| ER | `UI_LOCATORS` 登記：其來源為 **5.1** |
| `NR1L-UserProfiles-161` | 7.3 | 「Edit Profile」| pre | `UI_LOCATORS` 登記：其來源為 **5.1** |

---

## 1. 逐條全文

### NR1L-UserProfiles-157 — SWE1-HMI-PROF-056（7.1 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL1.) Unless user has selected to turn off welcome popups, the Head Unit will display a “welcome” popup at ignition on and any time a Profile is activated.

**037 description**：PRWEL1.) Unless user has selected to turn off welcome popups, the Head Unit will display a “welcome” popup at ignition on and any time a Profile is activated.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Welcome popup shown at ignition on and on activation |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle<br>2. The Welcome popup setting is on for both Profiles<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Switch the ignition on and read the screen<br>2. Activate Driver Profile B and read the screen |
| expected_result | 1. A welcome popup is displayed at ignition on<br>2. A welcome popup is displayed for Driver Profile B |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.1 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P1** — welcome popup 之兩個觸發；ch7 之入口條文 |
| remarks | **條文列兩個觸發**（`at ignition on` 與 `any time a Profile is activated`），依 §7 兩者皆須走到 —— 故本條兩步。`Unless user has selected to turn off welcome popups` 為適用條件（§8.7.3），以 pre-condition 固定為開啟；**關閉後不再顯示一側由 `SWE1-HMI-PROF-051`（6.3.2）承擔**。**X-1**：步驟 2 之切換所觸發者（5.3.1 之 PU0580）**即 ER2 所斷言者** —— 標的而非干擾。 |

**reasoning**：驗證目標：7.1（PRWEL1）—— 除非使用者關閉，welcome popup 於電門開啟時與任何 profile 被啟用時顯示。關鍵情境條件：兩個 profile 之設定皆為開啟，否則第二個觸發無從觀察。為什麼這樣切：本 leaf 之單位為**顯示之觸發**；popup 之內容屬 7.2／7.2.1，其清除屬 7.4。

---

### NR1L-UserProfiles-158 — SWE1-HMI-PROF-057（7.1.1 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL1.1) If the active Profile has not completed the Tutorials, and has not chosen to exit Tutorials, show “welcome” popup PU0841. Pressing X will show popup PU0611 giving the option to remind me later or don’t show again.

**037 description**：PRWEL1.1) If the active Profile has not completed the Tutorials, and has not chosen to exit Tutorials, show “welcome” popup PU0841. Pressing X will show popup PU0611 giving the option to remind me later or don’t show again.

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU0841 shown when Tutorials are not complete |
| pre_conditions | 1. The active Driver Profile has not completed the Tutorials<br>2. The active Driver Profile has not chosen to exit the Tutorials<br>3. The Welcome popup setting is on for that Profile<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Switch the ignition on and read the popup shown<br>2. Press X on the popup and read the popup shown |
| expected_result | 1. Welcome popup PU0841 is displayed<br>2. Popup PU0611 is displayed, offering to remind me later or not show again |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.1.1 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 未完成 Tutorials 時之 PU0841 與其 X 之後續 |
| remarks | **兩個 pre-condition 是條文之兩個合取條件** —— `has not completed` 與 `has not chosen to exit`；少任一個，PU0841 之適用條件即不成立，而本條會測到別的 popup。PU0841／PU0611 之**內文不寫**（R-U27 同型）：spec 只給 id 與其選項名稱，未給文字。 |

**reasoning**：驗證目標：7.1.1（PRWEL1.1）—— 未完成 Tutorials 之 profile 顯示 PU0841；按 X 則顯示 PU0611。關鍵情境條件：Tutorials 未完成**且**未選擇退出。為什麼這樣切：兩個 popup 為**同一條路徑之前後兩步**，依 §5.7 併為一條之兩個 ER 行；PU0611 之兩個選項之後果分屬 6.3.1／6.3.2，本條只驗其被提供。

---

### NR1L-UserProfiles-159 — SWE1-HMI-PROF-058（7.2 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL2.) The small welcome popup will show the active (logged in) Profile username and avatar, with options to switch users, or close the popup.

**037 description**：PRWEL2.) The small welcome popup will show the active (logged in) Profile username and avatar, with options to switch users, or close the popup. (image: %E5%9C%96%E7%89%87_1746377947.png)

| 欄 | 值 |
|---|---|
| tc_title / test_item | Small welcome popup shows username, avatar and options |
| pre_conditions | 1. The active Driver Profile has a username and an avatar<br>2. The small welcome popup version applies to this vehicle<br>3. The Welcome popup setting is on for that Profile<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Switch the ignition on and read the popup shown<br>2. Read the popup and check the username, the avatar and the options |
| expected_result | 1. The small welcome popup is displayed<br>2. The active Profile's username and avatar are shown with options to switch users or close the popup |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.2 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 小版 welcome popup 之內容與兩個選項 |
| remarks | **「小版」與「大版」之選用條件條文未載** —— 7.2 與 7.2.1 各自描述其內容，未說何時用哪一個。依 §8.4.1 不推定，以 pre-condition 具名為本車適用小版，**該條件本身不由本條驗**。大版之內容屬 `SWE1-HMI-PROF-059-01`（`NR1L-UserProfiles-007`）。兩個選項**按下之後**之行為屬 7.3（`SWE1-HMI-PROF-061`）。 |

**reasoning**：驗證目標：7.2（PRWEL2）—— 小版 welcome popup 顯示現用 profile 之username 與 avatar，並提供切換使用者與關閉兩個選項。關鍵情境條件：該 profile 須有 username 與 avatar，否則「顯示了什麼」不可觀察。為什麼這樣切：四項內容為**同一畫面之並列斷言**，§5.7 併驗。

---

### NR1L-UserProfiles-160 — SWE1-HMI-PROF-060（7.2.2 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL2.2) Closing the popup will not have the prompts from the default Welcome popup for “Remind me Later” and “Don’t Show me Again”. Pressing X in the custom Welcome popup will be treated as “Remind me Later”.

**037 description**：PRWEL2.2) Closing the popup will not have the prompts from the default Welcome popup for “Remind me Later” and “Don’t Show me Again”. Pressing X in the custom Welcome popup will be treated as “Remind me Later”.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Closing a custom welcome popup acts as Remind me Later |
| pre_conditions | 1. Two Driver Profiles exist and Driver Profile A is customized<br>2. The custom welcome popup of Driver Profile A is displayed<br>3. The Welcome popup setting is on for both Profiles<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press X on the custom welcome popup<br>2. Read the screen and check which popups are displayed<br>3. Activate Driver Profile B, then activate Driver Profile A again<br>4. Read the screen and check whether the popup is displayed |
| expected_result | 1. The custom welcome popup is closed<br>2. No popup offering Remind me Later or Don’t Show me Again is displayed<br>3. Driver Profile A is active again<br>4. The custom welcome popup of Driver Profile A is displayed again |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.2.2 |
| design_method | 狀態轉換 (State Transition Testing) |
| priority | **P3** — 自訂 popup 關閉時不再詢問；罕見分支 |
| remarks | **ER4 是「視同 Remind me Later」之唯一可觀察形式** —— 6.3.1 定 Remind me Later 為「關到該 profile 下次被啟用」；只驗 ER1／ER2（關了、沒問），一個**永久關閉**之實作會通過（§8.3）。故步驟 3 切走再切回。**與 `SWE1-HMI-PROF-051`（Don’t Show me Again）之結果相反** ——那一條之同位置斷言為「不再顯示」。**X-1**：步驟 3 之切換會觸發 5.3.1 之 PU0580，而該 popup **即 ER3／ER4 所涉者** —— 標的而非干擾。 |

**reasoning**：驗證目標：7.2.2（PRWEL2.2）—— 自訂 welcome popup 之關閉不出現Remind me Later／Don’t Show me Again 之詢問，且按 X 視同前者。關鍵情境條件：popup 須為**自訂** profile 之 popup ——預設 profile 之 popup 行為在 6.3.1，兩者相反。為什麼這樣切：`design_method` 取狀態轉換 ——本條驗的是一個**壓抑狀態之建立與其於再啟用時之解除**。

---

### NR1L-UserProfiles-161 — SWE1-HMI-PROF-061（7.3 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL3.) Pressing “Switch Users” on the Welcome popup will take the user to the All Profiles tab of the Profiles section. Pressing on the avatar of the text “Welcome [username]” will take the user to the last known tab in the Profile Section.

**037 description**：PRWEL3.) Pressing “Switch Users” on the Welcome popup will take the user to the All Profiles tab of the Profiles section. Pressing on the avatar of the text “Welcome [username]” will take the user to the last known tab in the Profile Section.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Welcome popup links to All Profiles or the last known tab |
| pre_conditions | 1. The welcome popup of the active Profile is displayed<br>2. The last known tab of the active Profile is the “Edit Profile” tab<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press “Switch Users” on the welcome popup<br>2. Read the screen and check which tab is shown<br>3. Return to the welcome popup and press the “Welcome [username]” text<br>4. Read the screen and check which tab is shown |
| expected_result | 1. The Profile section is opened<br>2. The “All Profiles” tab is displayed<br>3. The Profile section is opened again<br>4. The “Edit Profile” tab, the last known tab, is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.3 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — welcome popup 之兩個導向入口 |
| remarks | **條文列兩個入口而其去向不同**（Switch Users → All Profiles；avatar 或 Welcome 文字 → 上次分頁），依 §7 兩者皆須走到。上次分頁固定為 “Edit Profile”，**使兩個去向可分辨** ——若上次分頁本就是 All Profiles，兩個入口之結果相同。方括號 `[username]` **逐字引自 7.3**（§11 之 profile-scoped 例外，D-UP22-01）。**與 `SWE1-HMI-PROF-054`／`-055`（6.5／6.6）之關係**：那兩條之 popup 為 ch6 之預設 Welcome popup，本條為 ch7 之welcome popup；037 各自切了 leaf，故各自成條（§8.2.1）。 |

**reasoning**：驗證目標：7.3（PRWEL3）—— welcome popup 之兩個入口各自之去向。關鍵情境條件：上次分頁不得為 “All Profiles”。為什麼這樣切：兩個入口為同一句之列舉且去向不同，**併為一條方能在同一組前提下比較兩者**；分立則兩條之 pre-condition 相同而各驗一半。

---

### NR1L-UserProfiles-162 — SWE1-HMI-PROF-062-01（7.4 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL4.) The Welcome Popup (Default and custom) will clear when the vehicle is in motion or after 30 seconds or if the user interacts with the screen (whichever comes first) and not return until that Profile gets reactivated.

**037 description**：The Welcome Popup (both Default and custom) must automatically clear as soon as the system detects that the vehicle is in motion.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Welcome popup clears as soon as the vehicle moves |
| pre_conditions | 1. The welcome popup of the active Profile is displayed<br>2. The vehicle is stationary<br>3. The vehicle can be brought into motion on the test site |
| input_test_data | NA |
| test_procedure | 1. Bring the vehicle into motion<br>2. Read the screen and check whether the popup is displayed |
| expected_result | 1. The vehicle is in motion<br>2. The welcome popup is cleared |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.4 |
| design_method | 狀態轉換 (State Transition Testing) |
| priority | **P0** — 行車中 welcome popup 須自動清除 —— **遮蔽駕駛視野之防線本身**（§10.2 safety） |
| remarks | **取 motion 一側而非 30 秒一側**：條文之三個清除觸發（motion／30 秒／互動）為 `whichever comes first`，故本條須在 30 秒**之內**使車輛移動，否則清除之原因不可歸屬。30 秒一側屬 `SWE1-HMI-PROF-062-02`（`NR1L-UserProfiles-008`），互動一側屬 `SWE1-HMI-PROF-062-03`。**判 P0**：行車中之畫面遮蔽屬 §10.2 之 safety 條件，與 `SWE1-HMI-PROF-029`／`031` 同類 —— 本條驗的是**防線成立本身**。 |

**reasoning**：驗證目標：7.4（PRWEL4）之 motion 分支 —— 車輛開始移動時，welcome popup 自動清除。關鍵情境條件：popup 須在顯示中，且移動須發生在 30 秒逾時之前。為什麼這樣切：三個觸發互斥於歸因（`whichever comes first`），**不可併為一條** —— 併了就無從判定是哪一個造成清除。

---

### NR1L-UserProfiles-163 — SWE1-HMI-PROF-062-03（7.4 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL4.) The Welcome Popup (Default and custom) will clear when the vehicle is in motion or after 30 seconds or if the user interacts with the screen (whichever comes first) and not return until that Profile gets reactivated.

**037 description**：The Welcome Popup (both Default and custom) must clear immediately if the user interacts with the screen before the 30-second timeout or before the vehicle is in motion.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Welcome popup clears immediately on screen interaction |
| pre_conditions | 1. The welcome popup of the active Profile is displayed<br>2. The vehicle is stationary |
| input_test_data | Screen pressed about five seconds after the popup appears, that is before the 30-second timeout |
| test_procedure | 1. Press the screen while the welcome popup is displayed<br>2. Read the screen and check whether the popup is displayed |
| expected_result | 1. The screen is pressed while the welcome popup is displayed<br>2. The welcome popup is cleared |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.4 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 使用者互動時之立即清除 |
| remarks | **互動之時點寫在 `input_test_data`** —— 條文之三個觸發為`whichever comes first`，若互動發生在第 30 秒附近，清除之原因即不可歸屬。該時點為**測試方法所要求之值**（J-4），非條文之值，故不寫入 ER。車輛須靜止：否則 motion 分支（`SWE1-HMI-PROF-062-01`）會先於互動成立。 |

**reasoning**：驗證目標：7.4（PRWEL4）之互動分支 —— 使用者觸碰畫面即清除。關鍵情境條件：互動須明確早於 30 秒逾時，且車輛靜止。為什麼這樣切：同 `062-01` —— 三個觸發之歸因不可混。

---

### NR1L-UserProfiles-164 — SWE1-HMI-PROF-062-04（7.4 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL4.) The Welcome Popup (Default and custom) will clear when the vehicle is in motion or after 30 seconds or if the user interacts with the screen (whichever comes first) and not return until that Profile gets reactivated.

**037 description**：Once the Welcome Popup is cleared (whether by vehicle motion, timeout, or screen interaction), it must NOT return to the screen for the duration of the current session. It will only return when that specific Profile gets reactivated (e.g., next key cycle or profile switch).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Cleared welcome popup returns only on reactivation |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle<br>2. The welcome popup of Driver Profile A is displayed<br>3. The Welcome popup setting is on for both Profiles<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the screen to clear the welcome popup<br>2. Open and close the Profile section, then read the screen<br>3. Activate Driver Profile B, then activate Driver Profile A again<br>4. Read the screen and check whether the popup is displayed |
| expected_result | 1. The welcome popup is cleared<br>2. The welcome popup does not return during the current session<br>3. Driver Profile A is active again<br>4. The welcome popup of Driver Profile A is displayed again |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.4 |
| design_method | 狀態轉換 (State Transition Testing) |
| priority | **P2** — 清除後於本 session 內不再返回 |
| remarks | **ER2 與 ER4 缺一不可**：只驗 ER2 者，一個永不再顯示之實作會通過；只驗 ER4 者，一個每次回到主畫面就重彈之實作會通過。**盲區（R-G11）**：`for the duration of the current session` 之「session」條文未定義其邊界。步驟 2 以一次畫面往返代表之，**那是抽樣而非窮舉** —— 更長之 session 內是否返回，本條不保證。**X-1**：步驟 3 之切換會觸發 5.3.1 之 PU0580，而該 popup **即 ER3／ER4 所涉者** —— 標的而非干擾。 |

**reasoning**：驗證目標：7.4（PRWEL4）之後半 —— 清除後於本 session 內不返回，直到該 profile 再次被啟用。關鍵情境條件：須有第二個 profile，否則「再次啟用」這個唯一無歧義之解除條件造不出來。為什麼這樣切：`design_method` 取狀態轉換 ——清除建立一個壓抑狀態，再啟用解除之。

---

### NR1L-UserProfiles-165 — SWE1-HMI-PROF-063（7.4.1 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL4.1) The 30 seconds should not include when the vehicle is in remote start.

**037 description**：PRWEL4.1) The 30 seconds should not include when the vehicle is in remote start.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Remote start time does not count toward the 30 seconds |
| pre_conditions | 1. The vehicle is in remote start<br>2. The welcome popup of the active Profile is displayed<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Wait 30 seconds while the vehicle is in remote start<br>2. Read the screen and check whether the popup is displayed<br>3. Exit the remote start and wait 30 more seconds<br>4. Read the screen and check whether the popup is displayed |
| expected_result | 1. The vehicle stays in remote start for 30 seconds<br>2. The welcome popup is still displayed<br>3. The remote start ends and 30 seconds pass<br>4. The welcome popup is cleared |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.4.1 |
| design_method | 狀態轉換 (State Transition Testing) |
| priority | **P3** — 遙控起動期間不計入 30 秒；計時之排除條件 |
| remarks | **ER4 不可省** —— 只驗 ER2（遙控起動期間不清除），一個**根本沒有 30 秒計時**之實作會通過；ER4 證明計時仍在，只是排除了遙控起動之時間。步驟 3 之後須全程無互動且車輛靜止，否則清除可歸因於另兩個觸發。 |

**reasoning**：驗證目標：7.4.1（PRWEL4.1）—— 30 秒之計時不含遙控起動之時間。關鍵情境條件：popup 於遙控起動期間即已顯示。為什麼這樣切：`design_method` 取狀態轉換 ——本條之判定取決於**一次狀態離開**（退出遙控起動）之後計時才開始。

---

### NR1L-UserProfiles-166 — SWE1-HMI-PROF-064（7.5 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL5.) The Valet Mode welcome popup will have the same clear/timeout behavior as the other welcome popups. See Valet Mode section for additional information.

**037 description**：PRWEL5.) The Valet Mode welcome popup will have the same clear/timeout behavior as the other welcome popups. See Valet Mode section for additional information. (image: %E5%9C%96%E7%89%87_503778562.png)

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode welcome popup clears like the other popups |
| pre_conditions | 1. Valet Mode is active on the vehicle<br>2. The Valet Mode welcome popup is displayed<br>3. The vehicle is stationary |
| input_test_data | Screen pressed about five seconds after the popup appears |
| test_procedure | 1. Press the screen while the Valet Mode welcome popup is displayed<br>2. Read the screen and check whether the popup is displayed |
| expected_result | 1. The screen is pressed while the popup is displayed<br>2. The Valet Mode welcome popup is cleared |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.5 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — Valet Mode welcome popup 之清除行為同型 |
| remarks | **條文說的是「與其他 welcome popup 相同之清除／逾時行為」——即三個觸發**（motion／30 秒／互動）。本條取**互動**一側，**為抽樣而非窮舉**（§8.4.2）：另兩側之同型性不由本條保證。取互動一側之理由：三者中唯一**不需等待亦不需移動車輛**者，而 Valet Mode 下移動車輛另有 12.x 之限制介入。同型之三個觸發本身由 `SWE1-HMI-PROF-062-01`／`SWE1-HMI-PROF-062-03`／`SWE1-HMI-PROF-062-02` 各自驗證。 |

**reasoning**：驗證目標：7.5（PRWEL5）—— Valet Mode 之 welcome popup 具有與其他 welcome popup 相同之清除／逾時行為。關鍵情境條件：Valet Mode 須為作用中，且其 popup 在顯示中。為什麼這樣切：本 leaf 之單位為**同型性**；把三個觸發都走一遍等於把 7.4 重測一次，而 037 已為 7.4 切了獨立 leaf。

---

### NR1L-UserProfiles-167 — SWE1-HMI-PROF-065（8.1 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR0.) R1 High Only: this passage is not meant to be implemented. CPA will not be launched and it will be accessible from the Edit Profile screen only. Therefore, after step 4, the system will follow the request for preferences and will begin Tutorials (refer to Tutorials L&F).

**037 description**：NEWPR0.) R1 High Only: this passage is not meant to be implemented. CPA will not be launched and it will be accessible from the Edit Profile screen only. Therefore, after step 4, the system will follow the request for preferences and will begin Tutorials (refer to Tutorials L&F).

| 欄 | 值 |
|---|---|
| tc_title / test_item | R1 High begins Tutorials after the preferences step |
| pre_conditions | 1. The vehicle is an R1 High variant<br>2. A New Profile Setup is in progress<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Complete the New Profile Setup up to step 4<br>2. Read the screen and check that the preferences prompt is shown<br>3. Choose to create from current preferences<br>4. Read the screen shown after the preferences step |
| expected_result | 1. Step 4 of the New Profile Setup is completed<br>2. The prompt to choose current or default preferences is displayed<br>3. The choice is accepted<br>4. Tutorials begin and no Connected Personal Account login is launched |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.1 |
| design_method | 情境 / 用例 (Scenario / Use Case Testing) |
| priority | **P1** — R1 High 之流程分歧 —— 誤啟 CPA 即為錯誤變體行為 |
| remarks | **變體 axis `r1h-cpa-8.1`**：本條為 R1 High 側。base 側（`Is CPA present?` 為是 → 啟動 CPA 登入）**在 037 內無 leaf**，只見於 PDF p12 之流程圖，依 R-U56 不造；已於 `audit_variant_pairs.AXES` 由 `pending` 改為具名不配（述詞 `no-other-side-leaf` 實測）—— 同 `SWE1-HMI-PROF-046`。**ER4 之缺席斷言不可省**：只驗 Tutorials 有沒有開，一個**先開 CPA 再開 Tutorials** 之實作會通過（§8.3）。條文之 `accessible from the Edit Profile screen only` 一句，其正向屬 `SWE1-HMI-PROF-110`（11.3.1），本條不涵蓋其全稱反向。 |

**reasoning**：驗證目標：8.1（NEWPR0）—— R1 High 上，第 4 步之後依偏好請求並進入 Tutorials，CPA 不啟動。關鍵情境條件：車型須為 R1 High。為什麼這樣切：`design_method` 取情境／用例 ——本條驗的是設定流程末段之**走向**，跨偏好選擇與 Tutorials 兩處。

---

### NR1L-UserProfiles-168 — SWE1-HMI-PROF-066（8.2 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR1.) See flow for setting up a New Profile above. Connecting an account or downloading an existing Connected account are not pictured here.

**037 description**：NEWPR1.) See flow for setting up a New Profile above. Connecting an account or downloading an existing Connected account are not pictured here. (image: %E5%9C%96%E7%89%87_1102096521.png)

| 欄 | 值 |
|---|---|
| tc_title / test_item | New Profile Setup starts from the All Profiles tab |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and press the option to add a new Profile<br>2. Read the screen and check that the New Profile Setup started |
| expected_result | 1. The option to add a new Profile is pressed<br>2. The first step of the New Profile Setup is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.2 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P1** — New Profile Setup 之起始；ch8 之入口 |
| remarks | **8.2 之內容為對流程圖之指涉**（`See flow for setting up a New Profile above`）—— 圖之內容不逐字重述（§8.4.1）；各步驟之細節分屬 8.6–8.9，本條只驗**流程被起始**。條文另註 `Connecting an account or downloading an existing Connected account are not pictured here` —— 該句是說**圖上沒畫**，不是說該功能不存在；下載既有帳號一側屬 8.6（`SWE1-HMI-PROF-072`）。**本條之 label 依 RD #5 之答覆可能調整**（39 包作業 2 之命中：本節寫 `Connected account`）。 |

**reasoning**：驗證目標：8.2（NEWPR1）—— New Profile Setup 之起始。關鍵情境條件：profile 數未達上限，否則新增入口會被隱藏（5.2，`SWE1-HMI-PROF-021-02`）。為什麼這樣切：本 leaf 之單位為**起始**；起始之後之每一步各有其 leaf。

---

### NR1L-UserProfiles-169 — SWE1-HMI-PROF-067（8.3 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR2.) The Profile Setup processes is a series of popups. Specific popups can be found in the HMI Pop Up List.

**037 description**：NEWPR2.) The Profile Setup processes is a series of popups. Specific popups can be found in the HMI Pop Up List.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile Setup is presented as a series of popups |
| pre_conditions | 1. A New Profile Setup is in progress at its first step<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Complete each step of the New Profile Setup in turn<br>2. Read each screen and check that every step is a popup |
| expected_result | 1. Each step of the New Profile Setup is completed<br>2. Every step is presented as a popup |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.3 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 設定流程以 popup 串接之形態 |
| remarks | **具體之 popup id 不寫** —— 條文說 `Specific popups can be found in the HMI Pop Up List`，而該清單之逐步對映**不在本 feature 之輸入內**（`data/spec_popup_ids.tsv` 只記 id 與其出現節次，非流程對映）。依 §8.4.1 不自擬，ER 只驗**形態**。此為**上游文件依賴**，同 `SWE1-HMI-PROF-044` 之截斷規則 ——**不援引 R-U56**（本 leaf 存在，缺的是規則之權威文件）。 |

**reasoning**：驗證目標：8.3（NEWPR2）—— 設定流程以一連串 popup 呈現。關鍵情境條件：須自第一步走到最後一步，否則「每一步都是 popup」只驗了其中一步。為什麼這樣切：**可判定之部分只有「是不是 popup」** ——「是不是清單上的那一個 popup」之權威在外部文件。

---

### NR1L-UserProfiles-170 — SWE1-HMI-PROF-068（8.3.1 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR2.1) Pressing any other button (on main menu bar or status bar) while within the New Profile Setup will be treated the same as “Cancel” or “X” and give another popup asking if the user is sure they can to discard the New Profile setup.

**037 description**：NEWPR2.1) Pressing any other button (on main menu bar or status bar) while within the New Profile Setup will be treated the same as “Cancel” or “X” and give another popup asking if the user is sure they can to discard the New Profile setup.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Pressing another button during setup asks to discard |
| pre_conditions | 1. A New Profile Setup is in progress at the username step<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press a button on the status bar during the setup<br>2. Read the screen and check which popup is displayed |
| expected_result | 1. The status bar button is pressed during the New Profile Setup<br>2. A popup asking to confirm discarding the New Profile setup is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.3.1 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 設定中按他鍵視同取消並詢問；避免誤丟輸入 |
| remarks | **條文列兩處入口**（`main menu bar or status bar`）——本條取狀態列一側，**為抽樣**（§8.4.2）：主選單列一側之結果不由本條保證。取狀態列之理由：其於設定 popup 顯示期間仍可見（4.6），主選單列是否可見條文未述。**未驗「確認之後真的丟棄」** —— 條文只說「給另一個 popup 問」，丟棄之後果未述，依 §8.4.1 不推定。 |

**reasoning**：驗證目標：8.3.1（NEWPR2.1）—— 設定中按其他按鍵視同 Cancel／X，並出現確認丟棄之 popup。關鍵情境條件：設定須在進行中且已有輸入，否則「丟棄」無標的。為什麼這樣切：本 leaf 之單位為**該詢問之出現**。

---

### NR1L-UserProfiles-171 — SWE1-HMI-PROF-069-01（8.4 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR3.) Choosing an avatar will only show available options. When selecting an avatar, a default choice will be highlighted (the next available default – not used by another user) so that the user does not need to make a choice before saving/completing setup. No two Profile’s can use the same Avatar.

**037 description**：No two Profiles can use the same Avatar. When navigating to the avatar selection screen, the system must actively filter the list and only show available options that are not currently being used by any other existing Profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Avatars already in use are filtered out of the list |
| pre_conditions | 1. Two Driver Profiles exist, each with a different avatar<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab and record the avatars of both Profiles<br>2. Start a New Profile Setup and open the avatar selection screen<br>3. Read the avatar list and check that the recorded avatars are absent |
| expected_result | 1. The avatars of both Profiles are recorded<br>2. The avatar selection screen is displayed<br>3. Neither avatar recorded in step 1 is offered in the list |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.4 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P1** — avatar 不得重複 —— 清單須濾掉已用者 |
| remarks | **ER3 斷言「兩個都不在」而非「有一個不在」** —— 條文之 `No two Profiles can use the same Avatar` 是全稱；只檢一個，一個「只濾掉現用 profile 之 avatar」之實作會通過。**與 `SWE1-HMI-PROF-077`（8.8.1）之關係**：8.8.1 之 `As avatars are in use, they will not be shown` 與本 leaf 之過濾**是同一件事在兩節之兩次出現**；隱藏一側由本 leaf（`SWE1-HMI-PROF-069-01`）承擔，`SWE1-HMI-PROF-077` 只驗初始數目。 |

**reasoning**：驗證目標：8.4（NEWPR3）—— avatar 清單只顯示未被使用者，兩個 profile 不得共用同一 avatar。關鍵情境條件：兩個 profile 之 avatar 須不同且已記錄，缺席斷言方有標的。為什麼這樣切：037 對 8.4 切兩個 leaf；本 leaf 為**過濾**，自動 highlight 屬 `SWE1-HMI-PROF-069-02`。

---

### NR1L-UserProfiles-172 — SWE1-HMI-PROF-069-02（8.4 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR3.) Choosing an avatar will only show available options. When selecting an avatar, a default choice will be highlighted (the next available default – not used by another user) so that the user does not need to make a choice before saving/completing setup. No two Profile’s can use the same Avatar.

**037 description**：When a user enters the avatar selection screen, the system must automatically highlight a default choice (which must be the next available default avatar not used by another user). This ensures the user does not have to explicitly tap/make a choice before saving or completing the setup.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Next available default avatar is highlighted automatically |
| pre_conditions | 1. Two Driver Profiles exist, each using one of the first default avatars<br>2. A New Profile Setup is in progress<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the avatar selection screen of the New Profile Setup<br>2. Read the screen and check which avatar is highlighted |
| expected_result | 1. The avatar selection screen is displayed<br>2. An avatar is highlighted without any choice being made, and it is the next available default avatar |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.4 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 預設 avatar 之自動 highlight |
| remarks | **ER2 併驗兩件事** —— 「未做任何選擇即已有一個被 highlight」與「它是下一個可用之預設 avatar」。只驗前者，一個**永遠 highlight 第一個（含已被使用者）**之實作會通過；只驗後者則測不到「不必先選」這個條文之目的（`so that the user does not need to make a choice`）。pre-condition 令兩個 profile 各佔一個前段預設 avatar，**使「下一個可用」與「第一個」不是同一個**。 |

**reasoning**：驗證目標：8.4（NEWPR3）—— 進入 avatar 選擇畫面時，系統自動 highlight 下一個未被使用之預設 avatar。關鍵情境條件：前段預設 avatar 須已被佔用，否則「下一個可用」與「第一個」不可分辨。為什麼這樣切：與 `069-01` 同節不同 leaf ——前者驗清單之內容，本條驗清單之初始選取狀態。

---

### NR1L-UserProfiles-173 — SWE1-HMI-PROF-071（8.5 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR4.) The same username can be used for multiple Driver Profiles. Add New Continue Save & Continue Cancel/”X” Cancel/”X” Yes/Cancel No/Go Back No Yes Yes, Keep Changes Restore default preferences

**037 description**：NEWPR4.) The same username can be used for multiple Driver Profiles.

| 欄 | 值 |
|---|---|
| tc_title / test_item | The same username can be used by two Driver Profiles |
| pre_conditions | 1. Driver Profile A exists with the username Alex<br>2. Two Driver Profiles exist on the vehicle<br>3. The vehicle is stationary |
| input_test_data | Username entered for the new Profile: Alex |
| test_procedure | 1. Start a New Profile Setup and enter the username Alex<br>2. Complete the setup<br>3. Open the “All Profiles” tab and read the usernames shown |
| expected_result | 1. The username Alex is accepted<br>2. The new Driver Profile is saved<br>3. Two Driver Profiles with the username Alex are shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.5 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P3** — 同名 username 之允許；罕用但明文 |
| remarks | **ER3 不可省** —— 只驗 ER1（輸入被接受），一個接受輸入卻在儲存時把第二個改名之實作會通過。Alex 為測試設置（J-12）：條文未指定名稱。**與 `SWE1-HMI-PROF-069-01` 之對比值得記**：avatar **不得**重複而 username **得**重複 ——兩者同在 ch8 而規則相反，故本條之 ER 須明說「兩個都在」。 |

**reasoning**：驗證目標：8.5（NEWPR4）—— 同一個 username 可用於多個 profile。關鍵情境條件：已存在一個使用該 username 之 profile。為什麼這樣切：本 leaf 為單一允許性斷言；username 之字元規則屬 8.7／8.7.2。

---

