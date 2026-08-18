# 覆核用全文 ＋ ER 出處對照 — 第六批 後半（`174`–`189`）

- 產出層：執行層｜2026-08-18｜**供分析層逐條覆核**
- 本檔 **16 條**；另半在 `41_review_pack_33a.md`
- 由 `scripts/build_review_pack.py` 產生，不經人手轉錄

> 讀法：先讀「spec 原文」與「037 description」，再讀 ER ——
> 「這句話對不對」是本檔要問的；「這句話有沒有來源」見 §0 之出處對照。

## 0. ER 出處對照

| 項 | 數 |
|---|---|
| 引號字面值（ER ＋ pre_conditions）| **7** |
| 逐字溯得到被引之節或其 must_carry | **7** |
| 經 `UI_LOCATORS` 登記表溯源 | **0** |
| **未溯得者** | **0** |
| 全條無引號字面值者 | **10 條** |

| tc_id | 節 | 字面值 | 欄位 | 出處 |
|---|---|---|---|---|
| `NR1L-UserProfiles-180` | 8.8 | 「Save & Continue」| ER | 逐字見於 **8.8** |
| `NR1L-UserProfiles-181` | 8.8 | 「Save」| ER | 逐字見於 **8.8** |
| `NR1L-UserProfiles-184` | 8.9 | 「Create from Current Preferences or Create from Default?」| ER | 逐字見於 **8.9** |
| `NR1L-UserProfiles-185` | 8.10 | 「All Profiles」| ER | 逐字見於 **8.10** |
| `NR1L-UserProfiles-186` | 8.10.1 | 「Edit Profile」| ER | 逐字見於 **8.10.1** |
| `NR1L-UserProfiles-186` | 8.10.1 | 「Edit Profile」| pre | 逐字見於 **8.10.1** |
| `NR1L-UserProfiles-188` | 8.11 | 「Edit Profile」| pre | 逐字見於 **8.11** |

---

## 1. 逐條全文

### NR1L-UserProfiles-174 — SWE1-HMI-PROF-072（8.6 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR5.) For connected vehicles, New Profile setup Step 1: create new or download existing

**037 description**：NEWPR5.) For connected vehicles, New Profile setup Step 1: create new or download existing

| 欄 | 值 |
|---|---|
| tc_title / test_item | Connected vehicles offer create new or download existing |
| pre_conditions | 1. The vehicle is equipped with connectivity<br>2. A New Profile Setup is in progress at its first step<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read the first step of the New Profile Setup<br>2. Read the screen and check the options offered |
| expected_result | 1. The first step of the New Profile Setup is displayed<br>2. The options to create new or to download an existing Profile are offered |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.6 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 連網車輛之第一步兩個選項 |
| remarks | **`For connected vehicles` 為適用條件**（§8.7.3）——以 pre-condition 固定為連網車輛。**非連網車輛之第一步條文未述**，依 §8.4.1 不推定，亦不列為覆蓋缺口（037 未為其切 leaf）。下載既有 profile **之後**之流程屬 8.7.1 之 Back 選項（`SWE1-HMI-PROF-074`），本條只驗選項之存在。 |

**reasoning**：驗證目標：8.6（NEWPR5）—— 連網車輛之設定第一步提供「建立新的或下載既有」兩個選項。關鍵情境條件：車輛須具連網能力。為什麼這樣切：本 leaf 之單位為**第一步之選項**。

---

### NR1L-UserProfiles-175 — SWE1-HMI-PROF-073-02（8.7 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR6.) Step 2: “Enter a username”. The Maximum number of characters for a username is ~12 characters, and the keyboard will not allow typing more. The minimum number of characters is 1 and the Next button will not be available until one character is typed. Username can be alphanumeric with spaces (spaces count toward the character limit).

**037 description**：The minimum number of characters for a username is 1. The "Next" button must remain disabled or unavailable as long as the input field is completely empty (0 characters), and must only become available once at least one character is typed.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Next button stays unavailable while the username is empty |
| pre_conditions | 1. A New Profile Setup is at the username step<br>2. The username field is empty<br>3. The vehicle is stationary |
| input_test_data | Username length: 0 → 1 characters |
| test_procedure | 1. Read the Next button while the username field is empty<br>2. Type one character into the username field<br>3. Read the Next button and check whether it is available |
| expected_result | 1. The Next button is not available<br>2. One character is shown in the username field<br>3. The Next button is available |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.7 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| priority | **P1** — username 下界 1 字元；Next 之啟用條件 |
| remarks | **邊界對為 0 → 1**（§5.6 之界前／界上兩讀）：只讀界上（1 字元時可按），一個**永遠可按**之實作會通過。本 leaf 為下界；上界 12 字元屬 `SWE1-HMI-PROF-073-01`（`NR1L-UserProfiles-009`），空格計入屬 `SWE1-HMI-PROF-073-03` —— **三者為同一條條文之三個界**。 |

**reasoning**：驗證目標：8.7（NEWPR6）—— username 之最小長度為 1，欄位為空時 Next 不可用。關鍵情境條件：起始須為完全空白之欄位。為什麼這樣切：`design_method` 取邊界值分析 ——判定完全取決於 0 與 1 這一個界。

---

### NR1L-UserProfiles-176 — SWE1-HMI-PROF-073-03（8.7 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR6.) Step 2: “Enter a username”. The Maximum number of characters for a username is ~12 characters, and the keyboard will not allow typing more. The minimum number of characters is 1 and the Next button will not be available until one character is typed. Username can be alphanumeric with spaces (spaces count toward the character limit).

**037 description**：The username can consist of alphanumeric characters and spaces. Spaces are considered valid characters and must count toward the 12-character maximum limit.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Spaces count toward the username character limit |
| pre_conditions | 1. A New Profile Setup is at the username step<br>2. The username field is empty<br>3. The vehicle is stationary |
| input_test_data | Username length: 12 → 13 characters (eleven letters plus one space, then one more character) |
| test_procedure | 1. Type eleven letters and one space into the username field<br>2. Read the field and record the characters accepted<br>3. Type one more character and read the username field |
| expected_result | 1. The eleven letters and the space are accepted<br>2. Twelve characters are shown in the username field<br>3. The keyboard does not allow a thirteenth character in the field |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.7 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| priority | **P2** — 空格計入 12 字元上限 |
| remarks | **空格放在第十二個位置** —— 若放在中間，一個「不計空格」之實作仍會在第十二個字母處停下，與正確實作**在此設置下不可分辨**；放在最後才使兩者分歧：不計空格者會再接受一個字母。上限 12 出自 8.7 之條文；本條與 `SWE1-HMI-PROF-073-01`（`NR1L-UserProfiles-009`）**驗的是同一個上限之兩種輸入**（純字母／含空格）。 |

**reasoning**：驗證目標：8.7（NEWPR6）—— 空格為合法字元且計入 12 字元上限。關鍵情境條件：空格須落在使兩種實作分歧之位置（見 remarks）。為什麼這樣切：`design_method` 取邊界值分析 ——判定取決於第 12／13 個字元之接受與否。

---

### NR1L-UserProfiles-177 — SWE1-HMI-PROF-074（8.7.1 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR6.1) Options to “Save” (which takes user to Step 3 – if in New Profile Setup Process), Cancel (which prompts a confirmation popup), and Back (only available if there was a previous step for downloading a connected Profile)

**037 description**：NEWPR6.1) Options to “Save” (which takes user to Step 3 – if in New Profile Setup Process), Cancel (which prompts a confirmation popup), and Back (only available if there was a previous step for downloading a connected Profile)

| 欄 | 值 |
|---|---|
| tc_title / test_item | Save, Cancel and Back options on the username step |
| pre_conditions | 1. The vehicle is equipped with connectivity<br>2. A New Profile Setup is at the username step<br>3. The setup was reached through the download step<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read the screen and record the options offered<br>2. Press Save and read the screen<br>3. Return to the username step and press Cancel<br>4. Read the screen and check which popup is displayed |
| expected_result | 1. Options to Save, Cancel and Back are offered<br>2. Step 3 of the New Profile Setup is displayed<br>3. Cancel is pressed<br>4. A confirmation popup is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.7.1 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — username 步驟之三個選項與其去向 |
| remarks | **pre-condition 之「經下載步驟而來」是 Back 之適用條件** —— 條文寫 `Back (only available if there was a previous step for downloading a connected Profile)`；不設此前提，ER1 之三個選項只會出現兩個，**而那不是缺陷**。**未驗「無前一步時 Back 不出現」** —— 那是同一句之反向，037 未為其切 leaf，依 R-U56 不造。Cancel 之確認 popup **按下之後**之後果屬 8.3.1（`SWE1-HMI-PROF-068`）。 |

**reasoning**：驗證目標：8.7.1（NEWPR6.1）—— username 步驟提供 Save／Cancel／Back 三個選項，Save 進到第 3 步，Cancel 出現確認 popup。關鍵情境條件：須有前一步（下載既有 profile），Back 方會出現。為什麼這樣切：三個選項為同一句之列舉，§7 要求皆走到；本條走 Save 與 Cancel 兩者之去向，Back 只驗其存在 ——**其去向即步驟 3 所走之回程**，重複驗證無新資訊。

---

### NR1L-UserProfiles-178 — SWE1-HMI-PROF-075（8.7.2 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR6.2) The username can have numbers and/or letters, but no special characters.

**037 description**：NEWPR6.2) The username can have numbers and/or letters, but no special characters.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Special characters are not accepted in a username |
| pre_conditions | 1. A New Profile Setup is at the username step<br>2. The username field is empty<br>3. The vehicle is stationary |
| input_test_data | Characters typed: letters, digits, then a special character |
| test_procedure | 1. Type letters and digits into the username field<br>2. Attempt to type a special character<br>3. Read the field and check which characters are shown |
| expected_result | 1. The letters and digits are accepted<br>2. The special character is not accepted<br>3. Only the letters and digits typed in step 1 are shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.7.2 |
| design_method | 負向測試 (Negative / Invalid) |
| priority | **P1** — 特殊字元不得輸入 —— **輸入驗證之防線本身** |
| remarks | **ER1 不可省** —— 只驗「特殊字元不被接受」，一個**什麼都不接受**之實作會通過（§8.3）。**ER3 斷言欄位之最終內容**：一個接受特殊字元卻不顯示之實作，只看 ER2 會通過而其儲存值已錯。條文未列舉何謂 special character，依 §8.4.1 不代其列舉；執行時所用之字元記於執行紀錄。 |

**reasoning**：驗證目標：8.7.2（NEWPR6.2）—— username 得為英數，不得含特殊字元。關鍵情境條件：同一次輸入中兼有合法與非法字元，使「擋的是特殊字元」而非「擋了全部」可分辨。為什麼這樣切：`design_method` 取負向測試 ——步驟 2 為對一個**不該生效之輸入**的嘗試。

---

### NR1L-UserProfiles-179 — SWE1-HMI-PROF-076-01（8.8 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR7.) Step 3: “Select an Avatar”. One will be highlighted, and if they choose a different avatar it will become highlighted instead. The selected avatar will show above the “Save & Continue” button on 8.4" screens and larger and the selected avatar will show next to the save button on 7" screens. Pushing the Save button will complete the Avatar selection.

**037 description**：In Step 3 ("Select an Avatar") of the New Profile setup, one avatar will be highlighted by default. If the user chooses a different avatar, the highlight must dynamically move to the newly selected avatar instead.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Highlight moves to the newly chosen avatar |
| pre_conditions | 1. A New Profile Setup is at the avatar step<br>2. One avatar is highlighted by default<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read the avatar screen and record which avatar is highlighted<br>2. Choose a different avatar<br>3. Read the screen and check which avatar is highlighted |
| expected_result | 1. The highlighted avatar is recorded<br>2. A different avatar is chosen<br>3. The chosen avatar is highlighted and the avatar recorded in step 1 is not |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.8 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P3** — highlight 隨選取移動；呈現層 |
| remarks | **ER3 之後半不可省** —— 只驗「新選者被 highlight」，一個**兩個都 highlight** 之實作會通過（同 `NR1L-UserProfiles-117` 之形狀）。預設 highlight 之**選定規則**屬 `SWE1-HMI-PROF-069-02`（8.4），本條只以其為起點。 |

**reasoning**：驗證目標：8.8（NEWPR7）—— 選了不同 avatar 時，highlight 隨之移動。關鍵情境條件：起始須已有一個被 highlight 者且已記錄。為什麼這樣切：037 對 8.8 切三個 leaf；本 leaf 為 highlight 之移動，兩個螢幕尺寸之版面屬 `SWE1-HMI-PROF-076-02`／`-03`。

---

### NR1L-UserProfiles-180 — SWE1-HMI-PROF-076-02（8.8 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR7.) Step 3: “Select an Avatar”. One will be highlighted, and if they choose a different avatar it will become highlighted instead. The selected avatar will show above the “Save & Continue” button on 8.4" screens and larger and the selected avatar will show next to the save button on 7" screens. Pushing the Save button will complete the Avatar selection.

**037 description**：For vehicles equipped with 8.4" screens and larger, the currently selected avatar must be displayed strictly above the save button. Additionally, the text on this button must be labeled as “Save & Continue”. Pushing this button will complete the Avatar selection process.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Avatar shown above the Save & Continue button on 8.4 inch |
| pre_conditions | 1. The vehicle screen is 8.4 inches or larger<br>2. A New Profile Setup is at the avatar step<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Choose an avatar<br>2. Read the screen and check the avatar position and the button text |
| expected_result | 1. The avatar is chosen<br>2. The chosen avatar is shown above the button and the button reads “Save & Continue” |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.8 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 8.4 吋以上之 avatar 位置與按鈕字樣 |
| remarks | **與 `SWE1-HMI-PROF-076-03` 為 §7 之列舉配對** —— 同一句切出之兩個螢幕尺寸，兩者之**位置與字樣皆不同**（上方／旁邊、`Save & Continue`／`Save`）。**兩者皆須造**：只造其一，一個在所有尺寸上都用同一版面之實作會通過其中一條。**此非變體覆寫**（`audit_variant_pairs` 之母體不含之）：spec 未以覆寫註記標示，而是**同一句正面寫出兩側** ——兩者之判別由 037 之 `SWE1-HMI-PROF-076-02` 與 `SWE1-HMI-PROF-076-03` 兩個 leaf 承擔。 |

**reasoning**：驗證目標：8.8（NEWPR7）—— 8.4 吋以上之螢幕，選定之 avatar 顯示於儲存鍵**上方**，鍵上字樣為 “Save & Continue”。關鍵情境條件：螢幕尺寸為 8.4 吋以上。為什麼這樣切：位置與字樣為同一句之並列斷言，§5.7 併於 ER2。

---

### NR1L-UserProfiles-181 — SWE1-HMI-PROF-076-03（8.8 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR7.) Step 3: “Select an Avatar”. One will be highlighted, and if they choose a different avatar it will become highlighted instead. The selected avatar will show above the “Save & Continue” button on 8.4" screens and larger and the selected avatar will show next to the save button on 7" screens. Pushing the Save button will complete the Avatar selection.

**037 description**：For vehicles equipped with 7" screens, the currently selected avatar must be displayed next to the save button. Additionally, the text on this button must be labeled simply as “Save”. Pushing this button will complete the Avatar selection process.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Avatar shown next to the Save button on 7 inch screens |
| pre_conditions | 1. The vehicle screen is 7 inches<br>2. A New Profile Setup is at the avatar step<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Choose an avatar<br>2. Read the screen and check the avatar position and the button text |
| expected_result | 1. The avatar is chosen<br>2. The chosen avatar is shown next to the button and the button reads “Save” |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.8 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 7 吋之 avatar 位置與按鈕字樣 |
| remarks | **與 `SWE1-HMI-PROF-076-02` 為 §7 之列舉配對**（見該條）。**ER2 之字樣斷言是本對之關鍵**：位置之「上方／旁邊」在 7 吋小螢幕上可能難以目視分辨，而字樣之 `Save` 與 `Save & Continue` 是二值的。 |

**reasoning**：驗證目標：8.8（NEWPR7）—— 7 吋螢幕，選定之 avatar 顯示於儲存鍵**旁邊**，鍵上字樣為 “Save”。關鍵情境條件：螢幕尺寸為 7 吋。為什麼這樣切：同 `076-02`，兩者互為配對之另一側。

---

### NR1L-UserProfiles-182 — SWE1-HMI-PROF-077（8.8.1 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR7.1) There will be at least 10 Avatars initially. As avatars are in use, they will not be shown as options for other users to choose.

**037 description**：NEWPR7.1) There will be at least 10 Avatars initially. As avatars are in use, they will not be shown as options for other users to choose.

| 欄 | 值 |
|---|---|
| tc_title / test_item | At least ten avatars are offered initially |
| pre_conditions | 1. A New Profile Setup is at the avatar step<br>2. No avatar is in use by another Driver Profile<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the avatar selection screen and count the avatars offered<br>2. Read the count and check whether it reaches ten |
| expected_result | 1. The avatars offered are counted<br>2. At least ten avatars are offered |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.8.1 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P1** — 初始 avatar 數目下界；選擇池之充足性 |
| remarks | **pre-condition 指定「無 avatar 被佔用」** —— 否則「至少十個」與「原本十一個而被隱藏一個」不可分辨，本條會把一個數目不足之實作判成通過。**「使用中者不顯示」一側由 `SWE1-HMI-PROF-069-01`（8.4）承擔** ——8.8.1 之該句與 8.4 之過濾**是同一件事在兩節之兩次出現**，依 §8.2.1 不重複造。分類是否影響一次可見之數目，條文未述；本條之計數為**跨分類之總數**，已於 reasoning 具名。 |

**reasoning**：驗證目標：8.8.1（NEWPR7.1）—— 初始至少提供 10 個 avatar。關鍵情境條件：無 avatar 被其他 profile 佔用。為什麼這樣切：本 leaf 之單位為**數目下界**；隱藏規則已由 `SWE1-HMI-PROF-069-01`（8.4）承擔。**計數之範圍**：條文只說 `at least 10 Avatars initially`，未說是否須於同一畫面可見；本條計跨分類之總數，**一個把十個分散在三個分類之實作會通過** —— 此為條文之留白。

---

### NR1L-UserProfiles-183 — SWE1-HMI-PROF-078（8.8.2 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR7.2) Avatars will be sorted into at least 3 categories. Pushing a category button will show the respective grouping of avatars. Categories apply to all screen sizes, 7" will have a separate screen for category selection, an example is pictured above.

**037 description**：NEWPR7.2) Avatars will be sorted into at least 3 categories. Pushing a category button will show the respective grouping of avatars. Categories apply to all screen sizes, 7" will have a separate screen for category selection, an example is pictured above.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Avatars are sorted into at least three categories |
| pre_conditions | 1. A New Profile Setup is at the avatar step<br>2. The vehicle screen is 8.4 inches or larger<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read the avatar screen and count the category buttons<br>2. Press one category button<br>3. Read the list and check which avatars are shown |
| expected_result | 1. At least three category buttons are offered<br>2. The category button is pressed<br>3. Only the avatars of that category are shown |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.8.2 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — avatar 之分類數與分類按鈕之作用 |
| remarks | **ER3 不可省** —— 只驗分類按鈕之數目，一個**按了沒反應**之實作會通過；條文明說`Pushing a category button will show the respective grouping`。**7 吋之獨立分類畫面未涵蓋**：條文寫 `7" will have a separate screen for category selection`，而 037 未為其另切 leaf —— 本條取 8.4 吋以上一側，**為抽樣，7 吋之分類畫面不由本條保證**。 |

**reasoning**：驗證目標：8.8.2（NEWPR7.2）—— avatar 至少分為 3 類，按下分類按鈕顯示該類之 avatar。關鍵情境條件：螢幕尺寸取 8.4 吋以上（分類與清單同畫面）。為什麼這樣切：數目與作用為同一句之兩個斷言，§5.7 併於一條。

---

### NR1L-UserProfiles-184 — SWE1-HMI-PROF-079（8.9 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR8.) The final step (for New Profile setup only) is prompting the user to choose to “Create from Current Preferences or Create from Default?”. If the user chooses to keep current preferences, carry-over all of the previously active Profile’s preferences and settings.

**037 description**：NEWPR8.) The final step (for New Profile setup only) is prompting the user to choose to “Create from Current Preferences or Create from Default?”. If the user chooses to keep current preferences, carry-over all of the previously active Profile’s preferences and settings.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Final setup step offers current or default preferences |
| pre_conditions | 1. Driver Profile A is the active Profile and has known preferences<br>2. A New Profile Setup is in progress<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the preferences of Driver Profile A<br>2. Complete the New Profile Setup up to its final step<br>3. Read the prompt shown at the final step<br>4. Choose to create from current preferences, then read the new Profile's preferences |
| expected_result | 1. The preferences of Driver Profile A are recorded<br>2. The final step of the New Profile Setup is displayed<br>3. The prompt reads “Create from Current Preferences or Create from Default?”<br>4. The new Profile's preferences match those recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.9 |
| design_method | 情境 / 用例 (Scenario / Use Case Testing) |
| priority | **P1** — 最終步之偏好選擇與沿用；新 profile 之初始狀態 |
| remarks | **ER4 是條文後半之唯一可觀察形式** —— `carry-over all of the previously active Profile’s preferences`；只驗提示文字（ER3），一個顯示該提示卻兩個選項都給預設值之實作會通過。**未走 `Create from Default` 一側**：條文只說選了 current 會沿用，未說選了 default 會如何（`Default` 之內容未定義），依 §8.4.1 不推定。此提示為 **New Profile setup only**（條文明載），編輯既有 profile 時不出現 —— 該側屬 8.10.1／8.11。 |

**reasoning**：驗證目標：8.9（NEWPR8）—— 設定之最終步提示選擇沿用現有偏好或採用預設；選前者則沿用前一個現用 profile 之全部偏好與設定。關鍵情境條件：前一個現用 profile 之偏好須先記錄。為什麼這樣切：`design_method` 取情境／用例 ——本條跨設定流程之末段與新 profile 之初始狀態兩處。

---

### NR1L-UserProfiles-185 — SWE1-HMI-PROF-080（8.10 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR9.) When New Profile setup is complete, the screen will return to the “All Profiles” tab. The new Profile will be the active Profile.

**037 description**：NEWPR9.) When New Profile setup is complete, the screen will return to the “All Profiles” tab. The new Profile will be the active Profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Setup completion returns to All Profiles with the new Profile |
| pre_conditions | 1. A New Profile Setup is at its final step<br>2. Driver Profile A is the active Profile<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Complete the New Profile Setup<br>2. Read the screen and check the tab shown and the active Profile |
| expected_result | 1. The New Profile Setup is completed<br>2. The “All Profiles” tab is shown and the new Profile is the active Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.10 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P1** — 設定完成後之去向與新 profile 之啟用 |
| remarks | **ER2 併驗畫面與現用者** —— 條文兩句（`return to the “All Profiles” tab`、`The new Profile will be the active Profile`）為同一個完成事件之兩個結果，§5.7 併驗。pre-condition 具名 A 為原現用者，**使「新 profile 成為現用者」是一次可觀察之改變**，而非恆真。狀態列圖示之更新屬 `SWE1-HMI-PROF-082`（8.10.2）。 |

**reasoning**：驗證目標：8.10（NEWPR9）—— 設定完成後回到 “All Profiles” 分頁，且新 profile 成為現用者。關鍵情境條件：設定前之現用者須為另一個 profile。為什麼這樣切：本 leaf 之單位為**完成之後果**；編輯（非新增）之回程屬 `SWE1-HMI-PROF-081`，其結果不同。

---

### NR1L-UserProfiles-186 — SWE1-HMI-PROF-081（8.10.1 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR9.1) Editing an existing Profile (from the Edit Profile screen) will return the user to the page of the “Edit Profile” tab they initiated the editing from.

**037 description**：NEWPR9.1) Editing an existing Profile (from the Edit Profile screen) will return the user to the page of the “Edit Profile” tab they initiated the editing from.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Editing returns to the originating Edit Profile page |
| pre_conditions | 1. Driver Profile A is the active Profile<br>2. The “Edit Profile” tab is open at the page holding the username option<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record which page of the “Edit Profile” tab is open<br>2. Select the option to edit the username and complete the edit<br>3. Read the screen and check which page is shown |
| expected_result | 1. The page of the “Edit Profile” tab is recorded<br>2. The username edit is completed<br>3. The page recorded in step 1 is shown again |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.10.1 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 自 Edit Profile 起始之編輯，其返回頁 |
| remarks | **與 `SWE1-HMI-PROF-080` 之結果相反** —— 新增完成回 “All Profiles”，編輯完成回**發起編輯之該頁**；兩者同為「完成之後去哪」而條文分兩節，故各自成條。**ER3 以步驟 1 所記者為準而非寫死頁名** —— 條文說的是 `the page … they initiated the editing from`，寫死頁名等於把一個相對斷言改成絕對斷言。 |

**reasoning**：驗證目標：8.10.1（NEWPR9.1）—— 自 Edit Profile 畫面發起之編輯，完成後回到發起之該頁。關鍵情境條件：發起頁須先記錄，否則「回到原頁」無對照。為什麼這樣切：本 leaf 為編輯路徑之回程。

---

### NR1L-UserProfiles-187 — SWE1-HMI-PROF-082（8.10.2 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR9.2) The icon in the status bar Profile button will update to match the new active Profile

**037 description**：NEWPR9.2) The icon in the status bar Profile button will update to match the new active Profile

| 欄 | 值 |
|---|---|
| tc_title / test_item | Status bar icon updates to the new active Profile |
| pre_conditions | 1. Two Driver Profiles exist with different avatars<br>2. Driver Profile A is the active Profile<br>3. A New Profile Setup is at its final step<br>4. The Welcome popup setting is off for all Profiles<br>5. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read the status bar and record the Profile button icon<br>2. Complete the New Profile Setup<br>3. Read the status bar and check whether the icon changed |
| expected_result | 1. The Profile button icon is recorded<br>2. The new Profile is created and becomes the active Profile<br>3. The Profile button icon matches the new Profile and differs from the icon recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.10.2 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P1** — 狀態列圖示隨新現用 profile 更新 |
| remarks | **與 `SWE1-HMI-PROF-013`（`NR1L-UserProfiles-101`，4.6）之分別**：那一條驗的是**切換 profile 時**圖示隨之改變，本條驗的是**新增完成時**。兩節各自明載，故各自成條（§8.2.1）。**X-1**：pre-condition 指定 Welcome popup 設定為關閉 ——新 profile 之啟用會觸發 7.1 之 welcome popup 而遮住狀態列，而本條之判定全在狀態列。 |

**reasoning**：驗證目標：8.10.2（NEWPR9.2）—— 狀態列之 Profile 鍵圖示更新為新的現用 profile。關鍵情境條件：原現用者之圖示須先記錄，且兩者之 avatar 不同。為什麼這樣切：本 leaf 之單位為**圖示之更新**；分頁之去向屬 `SWE1-HMI-PROF-080`。

---

### NR1L-UserProfiles-188 — SWE1-HMI-PROF-083（8.11 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR10.) If only the username or avatar are edited (initiated from the “Edit Profile” screen). Only show the relevant popup (ex: select edit Avatar, only give Avatar selection popup). In this case, the back arrow would be the same as canceling.

**037 description**：NEWPR10.) If only the username or avatar are edited (initiated from the “Edit Profile” screen). Only show the relevant popup (ex: select edit Avatar, only give Avatar selection popup). In this case, the back arrow would be the same as canceling.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Editing only the avatar shows only the avatar popup |
| pre_conditions | 1. Driver Profile A is the active Profile with a username and an avatar<br>2. The “Edit Profile” tab is open<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Select the option to edit the avatar<br>2. Read the screen and check which popups are shown<br>3. Press the back arrow and read the Profile |
| expected_result | 1. The avatar edit is started<br>2. Only the avatar selection popup is shown and no username popup appears<br>3. The edit is cancelled and the avatar is unchanged |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.11 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 只改 username 或 avatar 時之單一 popup |
| remarks | **ER2 之缺席斷言是本條之判別力** —— 只驗「avatar popup 有出現」，一個把整段新增流程都跑一遍之實作會通過。**ER3 驗的是「back arrow 等同取消」**：條文之 `the back arrow would be the same as canceling` ——只驗畫面關閉不足，須斷言**值未被寫入**。條文列 username 與 avatar 兩個入口，本條取 avatar 一側（條文自己舉的例即為 avatar），**username 一側為同型**，其結果不由本條保證。 |

**reasoning**：驗證目標：8.11（NEWPR10）—— 只編輯 username 或 avatar 時只顯示相關之 popup，且 back arrow 等同取消。關鍵情境條件：自 Edit Profile 畫面發起，而非自新增流程。為什麼這樣切：兩個斷言（只出現相關 popup／back 等同取消）為同一句之兩半，§5.7 併於一條。

---

### NR1L-UserProfiles-189 — SWE1-HMI-PROF-084（8.12 / Setup Flow）

**spec 原文（`pdf_text`）**：

> NEWPR11.) In the New Profile setup Process, the back arrow will take the user to the previous step (if applicable) and store any selections for when they go to that step again (until canceled) Avatars/icons are placeholders for final graphics Enter/Edit Username Choose/Edit Avatar - 7 inch Choose/Edit Avatar - 8.4 10.1 10.25 12 inch Category Selection Screen - 7 inch

**037 description**：NEWPR11.) In the New Profile setup Process, the back arrow will take the user to the previous step (if applicable) and store any selections for when they go to that step again (until canceled)

| 欄 | 值 |
|---|---|
| tc_title / test_item | Back arrow returns to the previous step keeping selections |
| pre_conditions | 1. A New Profile Setup is in progress at the username step<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Enter a username at the username step and record it<br>2. Continue to the avatar step and choose an avatar<br>3. Press the back arrow and read the username step<br>4. Read the username field and check whether it matches step 1 |
| expected_result | 1. The username is entered and recorded<br>2. The avatar step is displayed and an avatar is chosen<br>3. The username step is displayed again<br>4. The username field holds the username recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.12 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 返回鍵之上一步與選擇之保留 |
| remarks | **輸入動作留在 procedure 而非 pre-condition**（W-1）：ER4 所斷言者正是該輸入之保留，若把它寫成 pre-condition 之完成式，「保留」與「一開始就在那裡」不可分辨。`(until canceled)` 之取消側未驗 —— 條文未說取消後選擇何時清除，依 §8.4.1 不推定。`(if applicable)` 為適用條件：第一步無前一步，故本條自第二步（username）發起。 |

**reasoning**：驗證目標：8.12（NEWPR11）—— 設定流程中之返回鍵回到上一步，並保留已做之選擇。關鍵情境條件：上一步須已有輸入且已記錄。為什麼這樣切：`design_method` 取狀態轉換 ——`design_method` 取功能測試而非狀態轉換：所驗者為**值之保留**，畫面之來回不是系統狀態之遷移（K-4a）。

---

