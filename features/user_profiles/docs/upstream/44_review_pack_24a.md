# 覆核用全文 ＋ ER 出處對照 — 第五批 前半（`135`–`145`）

> **⚠ 本檔已於 55 輪重出取代 → `55_review_pack_24a.md`。**
> 成因：`test_item` 自 55 輪起為**兩段**，而本檔只印首段 ——
> **覆核者看不到實際交付的那一欄**。新檔印出整個 `test_item`。
> **不得以本檔作覆核依據**。原文以下保留不刪。

- 產出層：執行層｜2026-08-18｜**供分析層逐條覆核**
- 本檔 **11 條**；另半在 `44_review_pack_24b.md`
- 由 `scripts/build_review_pack.py` 產生，不經人手轉錄
- **本檔取代 `40_review_pack_24a.md`**（AA-1，44 包）——該檔無語料指紋，`--verify` 一律判過期

> 讀法：先讀「spec 原文」與「037 description」，再讀 ER ——
> 「這句話對不對」是本檔要問的；「這句話有沒有來源」見 §0 之出處對照。

## 0.0 語料指紋（AA-1，44 包）—— 產生輪次：**44**

> **本表是本 pack 之保鮮期。** 覆核前先跑：
> `python3 scripts/build_review_pack.py --verify <本檔>` ——
> **不符即「pack 已過期，拒絕採信」**，須重出後再讀。
> 指紋之範圍即本 pack 所轉錄之每一個欄位（含 spec 原文、037 description、reasoning）。

| tc_id | digest |
|---|---|
| `NR1L-UserProfiles-135` | `dcfaa3e38c16` |
| `NR1L-UserProfiles-136` | `0011ec5d1d9a` |
| `NR1L-UserProfiles-137` | `3124ae530738` |
| `NR1L-UserProfiles-138` | `b68bf11414e3` |
| `NR1L-UserProfiles-139` | `b4e94adced40` |
| `NR1L-UserProfiles-140` | `ce7c1d2e1213` |
| `NR1L-UserProfiles-141` | `bc9a4e380685` |
| `NR1L-UserProfiles-142` | `cbc421ff2ec9` |
| `NR1L-UserProfiles-143` | `1a922483286f` |
| `NR1L-UserProfiles-144` | `7620f3da7141` |
| `NR1L-UserProfiles-145` | `8e7243731ff7` |

## 0. ER 出處對照

| 項 | 數 |
|---|---|
| 引號字面值（ER ＋ pre_conditions）| **3** |
| 逐字溯得到被引之節或其 must_carry | **1** |
| 經 `UI_LOCATORS` 登記表溯源 | **2** |
| **未溯得者** | **0** |
| 全條無引號字面值者 | **8 條** |

| tc_id | 節 | 字面值 | 欄位 | 出處 |
|---|---|---|---|---|
| `NR1L-UserProfiles-136` | 5.12.1 | 「All Profiles」| ER | `UI_LOCATORS` 登記：其來源為 **5.1** |
| `NR1L-UserProfiles-137` | 5.12.2 | 「Edit Profile」| ER | `UI_LOCATORS` 登記：其來源為 **5.1** |
| `NR1L-UserProfiles-145` | 5.15 | 「All Profiles」| ER | 逐字見於 **5.15** |

---

## 1. 逐條全文

### NR1L-UserProfiles-135 — SWE1-HMI-PROF-036（5.12 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR1.) Profile order will default based on the order in which the Profiles have been added (defaults to the left and new Profiles added to the right)

**037 description**：ALLPR1.) Profile order will default based on the order in which the Profiles have been added (defaults to the left and new Profiles added to the right)

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile order defaults to the order of creation |
| pre_conditions | 1. Only the default Driver Profiles exist on the vehicle<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Create a new Driver Profile named Alex<br>2. Create a second new Driver Profile named Bea<br>3. Open the “All Profiles” tab and read the order of the Profiles |
| expected_result | 1. Driver Profile Alex is created<br>2. Driver Profile Bea is created<br>3. The default Profiles are shown on the left, then Alex, then Bea on the right |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.12 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — All Profiles 之預設排序；清單之呈現順序 |
| remarks | **兩條新 profile 是必要的**：只造一條時，「新者在右」與「新者在最右」無從分辨，而一個把新 profile 插在最左之實作，單條測不出來。Alex／Bea 為測試設置（J-12）—— 條文未指定名稱。 |

**reasoning**：驗證目標：5.12（ALLPR1）—— profile 之預設順序依加入之先後，預設者在左、新增者依序往右。關鍵情境條件：起始須**只有預設 profile**，否則「預設者在左」之比較無基準。為什麼這樣切：本 leaf 之單位為**建立順序**；預設者彼此之順序屬 `SWE1-HMI-PROF-037`，編輯連結後之不變屬 `SWE1-HMI-PROF-038`。

---

### NR1L-UserProfiles-136 — SWE1-HMI-PROF-037（5.12.1 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR1.1) Default Profiles will be in order of memory seat link (Ex: mem seat 1 + Driver 1 will be the first Profile on the left)

**037 description**：ALLPR1.1) Default Profiles will be in order of memory seat link (Ex: mem seat 1 + Driver 1 will be the first Profile on the left)

| 欄 | 值 |
|---|---|
| tc_title / test_item | Default Profiles ordered by their memory seat link |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. Only the default Driver Profiles exist on the vehicle<br>3. Driver 1 is linked to memory seat 1<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab<br>2. Read the default Profiles and check their order from the left |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. Driver 1, linked to memory seat 1, is the first Profile from the left |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.12.1 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 預設 profile 依記憶座椅連結排序；呈現順序 |
| remarks | **盲區（R-G11）**：能分辨「依座椅連結排序」與「依名稱排序」之設置，須有一個座椅連結順序**不同於**名稱順序之車輛；而 5.12.2 已定編輯連結不改順序，**故該設置無法以編輯造出**，出廠即如此之車輛亦不在手上。本條遂只驗條文自己舉的例（`Ex: mem seat 1 + Driver 1`）——**一個依名稱排序之實作會通過本條**，此為已知且不可避免之限制。編號 1 出自條文之例，非測試設置。 |

**reasoning**：驗證目標：5.12.1（ALLPR1.1）—— 預設 profile 依其記憶座椅連結排序。關鍵情境條件：車輛須有記憶座椅，否則連結不存在。為什麼這樣切：本 leaf 之單位為**預設者彼此之順序**；新增者之落點屬 `SWE1-HMI-PROF-036`。**刻意略過**：排序依據之判別力見 remarks 之盲區聲明 ——以現有可造之設置無法將其與名稱排序區分開。

---

### NR1L-UserProfiles-137 — SWE1-HMI-PROF-038（5.12.2 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR1.2) Editing memory seat preferences/links will not change the order of the Profiles

**037 description**：ALLPR1.2) Editing memory seat preferences/links will not change the order of the Profiles

| 欄 | 值 |
|---|---|
| tc_title / test_item | Editing a memory seat link leaves the order unchanged |
| pre_conditions | 1. Three Driver Profiles exist on the vehicle<br>2. The vehicle is equipped with memory seats<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and record the order of the Profiles<br>2. Open the “Edit Profile” tab of the second Profile<br>3. Change the memory seat link of that Profile<br>4. Open the “All Profiles” tab and compare the order with step 1 |
| expected_result | 1. The order of the Profiles is recorded<br>2. The “Edit Profile” tab of the second Profile is displayed<br>3. The memory seat link of that Profile is changed<br>4. The order of the Profiles is unchanged from the order recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.12.2 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P3** — 編輯座椅連結後順序不變；罕觸發之呈現穩定性 |
| remarks | **取中間位置之 profile**：改第一個或最後一個時，「順序未變」與「往兩端移動被邊界擋住」不可分辨。三個 profile 為使中間位置存在（J-12 之測試設置）。 |

**reasoning**：驗證目標：5.12.2（ALLPR1.2）—— 編輯記憶座椅連結不改變 profile 之順序。關鍵情境條件：須先**記錄**原順序，否則「未變」無對照。為什麼這樣切：本 leaf 之單位為**編輯後之不變性**。`design_method` 取功能測試而非狀態轉換：本條所驗者為一個狀態改變（座椅連結）之**旁效不發生**，受檢之順序本身並未遷移 —— 標狀態轉換會使該欄與斷言不符（K-4a）。

---

### NR1L-UserProfiles-138 — SWE1-HMI-PROF-039（5.13 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR2.) If Default Profiles are restored (without clearing all Profiles) add restored Defaults to the right.

**037 description**：ALLPR2.) If Default Profiles are restored (without clearing all Profiles) add restored Defaults to the right.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Restored default Profiles are added to the right |
| pre_conditions | 1. Two custom Driver Profiles exist on the vehicle<br>2. Not all default Driver Profiles are present<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and record the order of the Profiles<br>2. Restore the default Driver Profiles without clearing all Profiles<br>3. Open the “All Profiles” tab and read where the restored Defaults are |
| expected_result | 1. The order of the Profiles is recorded<br>2. The default Driver Profiles are restored and the custom Profiles remain<br>3. The restored Defaults are to the right of the Profiles recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.13 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 回復預設時新增者之落點；順序規則之分支 |
| remarks | **ER2 併驗「自訂 profile 仍在」** —— 條文之適用條件為`without clearing all Profiles`；若回復連帶清掉自訂者，本條所測之情境根本沒有發生，而只驗順序不會發現。回復預設之**入口**條文未載，依 §8.4.1 不自擬 ——執行時依實車之回復入口，其位置記於執行紀錄。 |

**reasoning**：驗證目標：5.13（ALLPR2）—— 未清除全部 profile 而回復預設者時，回復之預設 profile 加在最右。關鍵情境條件：須有自訂 profile 留存，且**至少一個預設者不在**，回復方為可觀察之事件。為什麼這樣切：本 leaf 為「不清全部」之分支；「清全部」之分支屬 `SWE1-HMI-PROF-040`，兩者之結果相反，故不可併為一條。

---

### NR1L-UserProfiles-139 — SWE1-HMI-PROF-040（5.13.1 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR2.1) If all Profiles are cleared and the default Profiles are restored, return to default order

**037 description**：ALLPR2.1) If all Profiles are cleared and the default Profiles are restored, return to default order

| 欄 | 值 |
|---|---|
| tc_title / test_item | Clearing all Profiles returns Defaults to default order |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. Two custom Driver Profiles exist on the vehicle<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the settings and select Clear Personal Data<br>2. Press Yes on each confirmation popup PU0626/PU_0129<br>3. Open the “All Profiles” tab and read the order of the default Profiles |
| expected_result | 1. The Clear Personal Data setting is selected<br>2. All Profiles are cleared and the default Profiles are restored<br>3. The default Profiles are ordered by their memory seat link, from the left |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.13.1; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.12.1; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.13.2 |
| design_method | 情境 / 用例 (Scenario / Use Case Testing) |
| priority | **P2** — 全清後回到預設順序；清除流程之後續狀態 |
| remarks | ER3 之「default order」其內容不在 5.13.1（該節只寫`return to default order`），故**併列 5.12.1** 於引用欄，並將其內容（依記憶座椅連結）逐字寫入 ER —— 否則本條無從判定。PU0626 為 5.13.2 之確認 popup，本條之 procedure 須處理它，**故一併列 5.13.2**（X-1 之同型處置）。**PU0626 與 PU_0129 之關係條文未定**（RD #8）。**41 包 §四授權逕行修正**：步驟改為「於**每一個**確認 popup PU0626/PU_0129 按 Yes」—— 兩者若為同一個，該步驟即按一次；若為兩段確認，該步驟即按兩次。**兩種讀法下本條都不會假失敗**，且驗證目標未變（§四之界線）。清除後之**現用 profile 落點**屬 `SWE1-HMI-PROF-041-01`／`SWE1-HMI-PROF-041-02`，本條只驗**順序**。 |

**reasoning**：驗證目標：5.13.1（ALLPR2.1）—— 全部 profile 被清除且預設者回復後，回到預設順序。關鍵情境條件：須先存在自訂 profile 且其順序已偏離預設，否則「回到」無從觀察。為什麼這樣切：`design_method` 取情境／用例 ——本條走的是一條**跨節之流程**（5.13.2 之清除 → 5.13.1 之順序 →5.12.1 之順序內容），非單一功能點。

---

### NR1L-UserProfiles-140 — SWE1-HMI-PROF-041-01（5.13.2 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR2.2) Using the “Clear Personal Data” setting (and confirming from popup PU0626) will delete all profiles from the vehicle and restore the defaults. The new active profile will be associated with the current memory seat position (ex: if memory seat 2 is active, go to Driver 2 default profile). If there are no memory seats, Driver 1 should be the new active profile. PU1089 is displayed when users confirm data clearing by pressing Yes/Ok in pop-up PU_0129. PU1090 is displayed when data have been successfully cleared. PU1091 is displayed if HU or TBM do not confirm complete data clearing.

**037 description**：When the “Clear Personal Data” setting is executed and confirmed, the system must delete all custom profiles and restore the defaults. If the vehicle is equipped with memory seats, the new active profile must automatically associate with the currently active memory seat position (e.g., if memory seat 2 is active, the system defaults to the "Driver 2" profile).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Active Profile after clearing follows the active memory seat |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. Memory seat 2 is the currently active seat position<br>3. Two custom Driver Profiles exist on the vehicle<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the settings and select Clear Personal Data<br>2. Press Yes on each confirmation popup PU0626/PU_0129<br>3. Read the status bar and check which Driver Profile is active |
| expected_result | 1. The Clear Personal Data setting is selected<br>2. The custom Profiles are deleted and the defaults are restored<br>3. Driver 2 is the active Driver Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.13.2 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P1** — 清除個人資料後之新現用 profile —— **資料刪除為不可逆**，落點錯即需重建全部設定 |
| remarks | **取 memory seat 2 而非 1**：條文之例即為 seat 2 → Driver 2，且**一個永遠落到 Driver 1 之實作**（即 `041-02` 之無座椅行為）在 seat 1 之設置下與正確實作不可分辨。**PU0626 與 PU_0129 之關係條文未定**（RD #8）。**41 包 §四授權逕行修正**：步驟改為「於**每一個**確認 popup PU0626/PU_0129 按 Yes」—— 兩者若為同一個，該步驟即按一次；若為兩段確認，該步驟即按兩次。**兩種讀法下本條都不會假失敗**，且驗證目標未變（§四之界線）。編號出自 5.13.2 之條文（`if memory seat 2 is active, go to Driver 2`），非測試設置。 |

**reasoning**：驗證目標：5.13.2 —— 清除個人資料後，新的現用 profile 與**當前之記憶座椅位置**對應。關鍵情境條件：車輛須有記憶座椅，且其當前位置**不是第一個**，落點方具判別力。為什麼這樣切：037 對 5.13.2 切四個 leaf；本 leaf 之單位為**有座椅時之落點**，無座椅之落點屬 `SWE1-HMI-PROF-041-02`。

---

### NR1L-UserProfiles-141 — SWE1-HMI-PROF-041-02（5.13.2 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR2.2) Using the “Clear Personal Data” setting (and confirming from popup PU0626) will delete all profiles from the vehicle and restore the defaults. The new active profile will be associated with the current memory seat position (ex: if memory seat 2 is active, go to Driver 2 default profile). If there are no memory seats, Driver 1 should be the new active profile. PU1089 is displayed when users confirm data clearing by pressing Yes/Ok in pop-up PU_0129. PU1090 is displayed when data have been successfully cleared. PU1091 is displayed if HU or TBM do not confirm complete data clearing.

**037 description**：When the “Clear Personal Data” setting is executed and confirmed on a vehicle without memory seats, the system must delete all custom profiles, restore the defaults, and the new active profile must default to "Driver 1".

| 欄 | 值 |
|---|---|
| tc_title / test_item | Active Profile defaults to Driver 1 without memory seats |
| pre_conditions | 1. The vehicle is not equipped with memory seats<br>2. Two custom Driver Profiles exist on the vehicle<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the settings and select Clear Personal Data<br>2. Press Yes on each confirmation popup PU0626/PU_0129<br>3. Read the status bar and check which Driver Profile is active |
| expected_result | 1. The Clear Personal Data setting is selected<br>2. The custom Profiles are deleted and the defaults are restored<br>3. Driver 1 is the active Driver Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.13.2 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P1** — 無記憶座椅車型之落點；同上之另一分支 |
| remarks | 與 `SWE1-HMI-PROF-041-01` 之差別只在**車型**（有無記憶座椅），而該差別為**條文自己切出之兩個分支**，非我方之變體對造：兩者之預期結果不同，且各有 037 之 leaf。**PU0626 與 PU_0129 之關係條文未定**（RD #8）。**41 包 §四授權逕行修正**：步驟改為「於**每一個**確認 popup PU0626/PU_0129 按 Yes」—— 兩者若為同一個，該步驟即按一次；若為兩段確認，該步驟即按兩次。**兩種讀法下本條都不會假失敗**，且驗證目標未變（§四之界線）。編號 1 出自 5.13.2 之條文（`Driver 1 should be the new active profile`）。 |

**reasoning**：驗證目標：5.13.2 —— 無記憶座椅之車輛，清除後之現用 profile 為 Driver 1。關鍵情境條件：車輛**無**記憶座椅 —— 這是本分支之成立條件本身。為什麼這樣切：與 `041-01` 同節不同分支；併為一條則兩個互斥之車型條件會落在同一個 pre-condition 內。

---

### NR1L-UserProfiles-142 — SWE1-HMI-PROF-041-03（5.13.2 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR2.2) Using the “Clear Personal Data” setting (and confirming from popup PU0626) will delete all profiles from the vehicle and restore the defaults. The new active profile will be associated with the current memory seat position (ex: if memory seat 2 is active, go to Driver 2 default profile). If there are no memory seats, Driver 1 should be the new active profile. PU1089 is displayed when users confirm data clearing by pressing Yes/Ok in pop-up PU_0129. PU1090 is displayed when data have been successfully cleared. PU1091 is displayed if HU or TBM do not confirm complete data clearing.

**037 description**：During the "Clear Personal Data" process, the system must display specific pop-ups to indicate progress and success. PU1089 must be displayed when the user confirms data clearing (pressing Yes/Ok on the confirmation prompt PU0626/PU_0129). Upon successful completion of data clearing, PU1090 must be displayed.

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU1089 on confirmation and PU1090 on successful clearing |
| pre_conditions | 1. Two custom Driver Profiles exist on the vehicle<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the settings and select Clear Personal Data<br>2. Press Yes on each confirmation popup PU0626/PU_0129 and read the popup shown<br>3. Wait until the clearing ends and read the popup shown |
| expected_result | 1. The Clear Personal Data setting is selected<br>2. PU1089 is displayed<br>3. PU1090 is displayed once the data have been cleared |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.13.2 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 清除流程之進度與完成 popup；流程可見性 |
| remarks | **PU1089／PU1090 之內文不寫**（R-U27 同型）—— spec 只給 id，未給文字；ER 只斷言其顯示與時機。**RD #8 —— 41 包 §四授權逕行修正**：5.13.2 之確認 popup 同時寫了 PU0626（`confirming from popup PU0626`）與 PU_0129（`pressing Yes/Ok in pop-up PU_0129`），**兩者之關係條文未定義**。本條之步驟 2 取 PU_0129 ——因條文把「按 Yes/Ok 觸發 PU1089」這件事綁在 PU_0129 上。**本條之步驟 2 改為「於每一個確認 popup PU0626/PU_0129 按 Yes」** ——兩者若為同一個即按一次，若為兩段確認即按兩次；**兩種讀法下皆不假失敗**。RD #8 仍照送（上游知情），但不作為修正之前提。 |

**reasoning**：驗證目標：5.13.2 —— 清除流程之進度 popup（PU1089）與完成 popup（PU1090）。關鍵情境條件：須有可清之自訂資料，否則「完成」之時點不可觀察。為什麼這樣切：本 leaf 之單位為**成功路徑之兩個 popup**；失敗路徑之 PU1091 屬 `SWE1-HMI-PROF-041-04`，其成立條件（HU／TBM 不回報完成）與本條互斥。

---

### NR1L-UserProfiles-143 — SWE1-HMI-PROF-041-04（5.13.2 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR2.2) Using the “Clear Personal Data” setting (and confirming from popup PU0626) will delete all profiles from the vehicle and restore the defaults. The new active profile will be associated with the current memory seat position (ex: if memory seat 2 is active, go to Driver 2 default profile). If there are no memory seats, Driver 1 should be the new active profile. PU1089 is displayed when users confirm data clearing by pressing Yes/Ok in pop-up PU_0129. PU1090 is displayed when data have been successfully cleared. PU1091 is displayed if HU or TBM do not confirm complete data clearing.

**037 description**：If the Head Unit (HU) or Telematics Box Module (TBM) fails to confirm complete data clearing, the system must handle this exception by displaying the error/failure pop-up PU1091.

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU1091 shown when clearing is not confirmed complete |
| pre_conditions | 1. Two custom Driver Profiles exist on the vehicle<br>2. The vehicle is equipped with a Telematics Box Module<br>3. The vehicle is stationary |
| input_test_data | Fault injected: the Telematics Box Module withholds its completion report for the data clearing |
| test_procedure | 1. Open the settings and select Clear Personal Data<br>2. Press Yes on each confirmation popup PU0626/PU_0129<br>3. Suppress the completion report of the Telematics Box Module<br>4. Read the screen and check which popup is displayed |
| expected_result | 1. The Clear Personal Data setting is selected<br>2. PU1089 is displayed<br>3. The Telematics Box Module does not report complete data clearing<br>4. PU1091 is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.13.2 |
| design_method | 基礎故障注入 (Fault Injection Lite) |
| priority | **P1** — 清除未完成時之失敗告知 —— **缺此則使用者以為已清而實未清** |
| remarks | **故障注入之對象為 TBM 之完成回報**，非 HU —— 條文寫的是`if HU or TBM do not confirm`，兩者為**析取**；注入其一即足以使該條件成立，**HU 側之注入本條不涵蓋**（其結果不由本條保證）。注入手段（拔線／模擬器／診斷指令）條文未載，依 §8.4.1 不自擬，執行時之手段記於執行紀錄。PU1091 之內文不寫（同 `041-03`）。 |

**reasoning**：驗證目標：5.13.2 —— HU 或 TBM 未回報完成時，顯示失敗 popup PU1091。關鍵情境條件：清除流程須**確實已開始**（故步驟 2 之 PU1089 為中途之錨點），否則「失敗」與「根本沒開始」不可分辨。為什麼這樣切：`design_method` 取基礎故障注入 ——本條之成立條件**無法以正常操作造出**，須主動使一個模組不回報；這是本批唯一之故障注入條。

---

### NR1L-UserProfiles-144 — SWE1-HMI-PROF-042（5.14 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR3.) Pressing and holding the Avatar of any Profile will allow for dragging and reordering the Profiles (and will not result in that Profile being activated)

**037 description**：ALLPR3.) Pressing and holding the Avatar of any Profile will allow for dragging and reordering the Profiles (and will not res ult in that Profile being activated)

| 欄 | 值 |
|---|---|
| tc_title / test_item | Long press on an avatar drags and reorders Profiles |
| pre_conditions | 1. Three Driver Profiles exist on the vehicle<br>2. The first Driver Profile from the left is the active one<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and record the order of the Profiles<br>2. Press and hold the avatar of the second Profile<br>3. Drag that avatar to the leftmost position and release it<br>4. Read the tab and check the order and the active Profile |
| expected_result | 1. The order of the Profiles is recorded<br>2. The avatar of the second Profile becomes draggable<br>3. That Profile is placed leftmost and the others move right<br>4. The order differs from the one recorded in step 1 and the active Profile is unchanged |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.14 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P2** — 長按拖曳重排，且不得啟用該 profile |
| remarks | **ER4 併驗「未被啟用」** —— 條文之`(and will not result in that Profile being activated)` 與拖曳為**同一句之兩個斷言**，依 §5.7 併於本條；另立則兩條之 procedure 逐字相同，只 ER 差一行。**被拖者刻意取非現用之 profile**：若拖現用者，「未被啟用」恆真而無判別力。三個 profile 為使「其他人往右移」為可觀察之複數（J-12）。 |

**reasoning**：驗證目標：5.14（ALLPR3）—— 長按 avatar 可拖曳重排，且該操作**不得**啟用被按之 profile。關鍵情境條件：被拖者非現用者，且順序須先記錄。為什麼這樣切：兩個斷言同屬一句，§5.7 併驗；**壓力測試（§8.3）**：一個「長按即啟用並且順便可拖」之實作，只驗拖曳者會通過 —— ER4 之後半即為擋它而設。

---

### NR1L-UserProfiles-145 — SWE1-HMI-PROF-043（5.15 / Profile List）

**spec 原文（`pdf_text`）**：

> ALLPR5.) Usernames displayed on the All Profiles tab should be center justified under the associated avatar and not overlap with other usernames.

**037 description**：ALLPR5.) Usernames displayed on the All Profiles tab should be center justified under the associated avatar and not overlap with other usernames.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Usernames are center justified and do not overlap |
| pre_conditions | 1. Three Driver Profiles exist on the vehicle<br>2. The usernames of the three Profiles differ in length<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab<br>2. Read each username and check its position under its avatar<br>3. Read the usernames and check that none overlaps another |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. Each username is center justified under its associated avatar<br>3. No username overlaps another username |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.15 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| priority | **P3** — username 之對齊與不重疊；純版面 |
| remarks | **username 長度刻意不同** —— 等長時，置中與靠左之版面在多數字型下差異極小，且重疊不會發生；長度不同才使兩個斷言各自可觀察。過長者之**截斷**屬 `SWE1-HMI-PROF-044`，本條不涉。 |

**reasoning**：驗證目標：5.15（ALLPR5）—— username 於 avatar 下置中，且不相互重疊。關鍵情境條件：多個 profile 且 username 長短不一。為什麼這樣切：置中與不重疊為**同一句之並列斷言**，§5.7 併為一條；但拆為兩個 ER 行，使失敗時可指出是哪一半。

---

