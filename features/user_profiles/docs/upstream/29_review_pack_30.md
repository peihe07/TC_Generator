# 覆核用全文 — 第三批 30 條（29 包作業 2）

- 產出層：執行層｜2026-08-18｜**供分析層逐條覆核**
- 範圍：`NR1L-UserProfiles-079` ～ `108` —— **ch4 剩餘 26 ＋ `009` 之負向配對 1
  ＋ A-UP13 附掛 3**（批界依 R-4 如此書寫，不寫「第三批 ＝ ch4」）
- 格式同 21／23 輪之 review pack（含 spec 原文、must_carry 與 037 description）

> 讀法：先讀「spec 原文」與「037 description」，再讀 ER ——
> **本檔要覆核的是「這句話對不對」**，不是「有沒有來源」
> （後者為 `28_provenance4.md`，已交，未溯得者 0）。

## 生成時之四項先具名處置（覆核時請一併看）

| 項 | 落點 |
|---|---|
| `002-02` 之 popup 內文**不寫**（R-U27，DR #4 未到齊）| `TC-082` |
| `005` 之順序斷言須可區分（**ER2 ＋ ER3 併存才成立**）| `TC-088` |
| 委派一律指名 leaf id（D-1）| 5 處，`audit_delegation` 紅 0 |
| PLP 併列之代價聲明隨引用欄同讀（J-1）| `TC-079`／`080`／`088`／`100` |

共 **30 條**。

---

## NR1L-UserProfiles-079 — SWE1-HMI-PROF-001-02（4.1 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC1.) The system will store and recall each unique Driver Profile’s preferences: see list of linked content above. If a feature is unavailable for a vehicle or region, ignore requirement.

**037 description**：system shall recall stored preferences when profile is activated.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Stored preferences recalled when a Driver Profile is activated |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle<br>2. The features carrying the preferences under test are available for the vehicle and the region |
| input_test_data | Preferences under test: Cluster Home screen (3.1), SiriusXM 360L Listener Profile (3.2) |
| test_procedure | 1. Activate Driver Profile A and record the two preferences<br>2. Activate Driver Profile B<br>3. Activate Driver Profile A and check that the two preferences match the values recorded in step 1 |
| expected_result | 1. Driver Profile A is active and the two preference values are recorded<br>2. Driver Profile B is active<br>3. Driver Profile A is active and the two preferences match the values recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.1; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.1; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.2; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.3; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.4; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.5 |
| priority | **P0** — 偏好之回復機制本身 —— R-U5 核心五類之一 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 引用欄併列 `3.1`–`3.5`（PLP 表，R-U22／R-U46）。**併列不等於該五列皆已被驗證** —— 覆蓋率不得以引用欄推定（J-1／D-UP17-01）；本 TC 實際受測之列項見 input_test_data。 本 leaf 之單位為**啟用時之回復**；儲存側由 `SWE1-HMI-PROF-001-01` 承擔（pilot 之 TC-001）。 |

**reasoning**：驗證目標：4.1（PRACC1）之回復側 —— profile 啟用時回復其已儲存之偏好。關鍵情境條件：受測偏好取自 PLP 表 3.1／3.2 之逐字列項，非自擬（§8.4.1）；條文之「feature 不可用則忽略」以 pre-condition 限定該二項在本車可用。為什麼這樣切：037 對 4.1 切三個 leaf，本 leaf（-02）之單位為**啟用時之回復**，一葉一 TC（§8.2.1）。**中間切至 Profile B 是必要的** —— 若不切走，「回復」與「值本來就在畫面上」無從分辨。刻意略過：不可用項目之略過屬 `SWE1-HMI-PROF-001-03`；儲存側屬 `SWE1-HMI-PROF-001-01`。

---

## NR1L-UserProfiles-080 — SWE1-HMI-PROF-001-03（4.1 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC1.) The system will store and recall each unique Driver Profile’s preferences: see list of linked content above. If a feature is unavailable for a vehicle or region, ignore requirement.

**037 description**：If a feature is unavailable for a vehicle or region, system shall skip storing & recalling that item.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Unavailable features skipped when storing and recalling |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle<br>2. At least one preference in the PLP table belongs to a feature not available for this vehicle or region |
| input_test_data | Preference under test: a PLP item whose feature is absent on this vehicle |
| test_procedure | 1. Activate Driver Profile A and record the option list of profile-linked preferences<br>2. Activate Driver Profile B, then activate Driver Profile A<br>3. Read the option list and check that the unavailable item is neither stored nor recalled |
| expected_result | 1. Driver Profile A is active and the option list is recorded<br>2. Driver Profile A is active again<br>3. The unavailable item is absent from the list and no error is raised for it |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.1; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.1; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.2; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.3; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.4; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.5 |
| priority | **P2** — 不可用項目之略過 —— 例外處理，非儲存機制本身 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 引用欄併列 `3.1`–`3.5`（PLP 表，R-U22／R-U46）。**併列不等於該五列皆已被驗證** —— 覆蓋率不得以引用欄推定（J-1／D-UP17-01）；本 TC 實際受測之列項見 input_test_data。 本條驗**略過**，故其受測列項為「該車不具備之功能」—— 其為配置相依，pre-condition 以能力而非以特定列項指定。 |

**reasoning**：驗證目標：4.1（PRACC1）末句 —— feature 於本車或本區域不可用時，略過該項之儲存與回復。關鍵情境條件：受測對象是「不存在之功能」，故 pre-condition 以**能力**描述而非指定某一列 —— 指定列會使本 TC 只能在特定車上跑。為什麼這樣切：**ER 併驗「不報錯」** —— 只驗「該項不在」，一個略過該項但同時拋出錯誤之實作會通過，而條文說的是 ignore。刻意略過：可用項目之儲存與回復屬 `SWE1-HMI-PROF-001-01` 與 `SWE1-HMI-PROF-001-02`。

---

## NR1L-UserProfiles-081 — SWE1-HMI-PROF-002-01（4.1.1 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC1.2) For the “Restore Settings to Default” vehicle setting, when selected, only restore the active Profile’s settings to default state (do not reset all Profiles’ settings to default). “Restore Settings to Default” will not delete profile username or avatar. PU1087 is displayed when users confirm Setting restore to default by pressing Yes in pop-up PU_0118. PU1088 is displayed when settings have been successfully restored to default. PU1088 is displayed if HU or TBM do not confirm complete default restoring.

**037 description**：Restore active Profile's default values, but do not delete username & avatar.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Restore Settings to Default affects only the active Profile |
| pre_conditions | 1. Two Driver Profiles exist, each with a username and an avatar<br>2. Both Profiles have at least one vehicle setting changed from its default |
| input_test_data | NA |
| test_procedure | 1. Activate Driver Profile A and record its setting, username and avatar<br>2. Select “Restore Settings to Default” and confirm it<br>3. Read Driver Profile A and check its setting, username and avatar<br>4. Activate Driver Profile B and check that its setting is unchanged |
| expected_result | 1. Driver Profile A is active and its values are recorded<br>2. The restore completes for Driver Profile A<br>3. The setting of Driver Profile A is back to default while its username and avatar are unchanged<br>4. The setting of Driver Profile B is unchanged |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.1.1 |
| priority | **P0** — 回復預設時**不得波及他 profile 與 username／avatar** —— 資料遺失風險項 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文有三個斷言：只回復現用 profile、不重設全部 profile、不刪 username 與 avatar —— **三者為同一操作之三個結果**，依 §5.7 併為一條 TC。步驟 4 之 Profile B 即「不重設全部」之觀察點。 |

**reasoning**：驗證目標：4.1.1（PRACC1.2）—— 「Restore Settings to Default」只回復現用 profile 之設定，不重設其他 profile，且不刪 username 與 avatar。關鍵情境條件：pre-condition 要求**兩個** profile 皆有偏離預設之設定 ——**只有一個 profile 時，「不重設全部」無從觀察**。為什麼這樣切：三個斷言同屬一次操作之結果（§5.7）；**若只驗「A 回到預設」，一個把全部 profile 都重設之實作會通過**。刻意略過：回復過程之提示 popup 屬 `SWE1-HMI-PROF-002-02`。

---

## NR1L-UserProfiles-082 — SWE1-HMI-PROF-002-02（4.1.1 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC1.2) For the “Restore Settings to Default” vehicle setting, when selected, only restore the active Profile’s settings to default state (do not reset all Profiles’ settings to default). “Restore Settings to Default” will not delete profile username or avatar. PU1087 is displayed when users confirm Setting restore to default by pressing Yes in pop-up PU_0118. PU1088 is displayed when settings have been successfully restored to default. PU1088 is displayed if HU or TBM do not confirm complete default restoring.

**037 description**：When user pressing Yes in pop-up PU_0118, PU1087 is displayed. PU1088 shows when restore completes.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Progress popups shown during Restore Settings to Default |
| pre_conditions | 1. A Driver Profile is active with at least one setting changed from its default<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Select “Restore Settings to Default”<br>2. Press Yes on the confirmation popup and check that PU1087 is displayed<br>3. Wait for the restore to end and check that PU1088 is displayed |
| expected_result | 1. The confirmation popup PU0118 is displayed<br>2. PU1087 is displayed<br>3. PU1088 is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.1.1 |
| priority | **P2** — 回復進度之提示（PU1087／PU1088）；呈現層 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | **本批唯一帶上游未決事項生成者（R-U27）**：DR #4 所缺為 `PU1087`／`PU1088` 之 popup **內文**，而其**觸發條件**已載於 spec（p6）。故本 TC 之 ER 只斷言該二 popup **顯示**，**不寫其上之文字** —— 不得以鄰近 PU id 推定內容（§8.4.1）。DR #4 到齊後，ER 得補其逐字內容。 |

**reasoning**：驗證目標：4.1.1 之後三句 —— 於 PU0118 按 Yes 後顯示 PU1087，回復完成後顯示 PU1088。關鍵情境條件：須有可回復之設定，否則流程不會被觸發。為什麼這樣切：本 leaf 之單位為**流程提示**，回復之實際效果屬 `SWE1-HMI-PROF-002-01`。**寫作限制（R-U27）**：popup 之內文未到齊，本 TC 只驗其顯示與時序，**不驗其文字** —— 已於 remarks 具名。刻意略過：條文另有「HU 或 TBM 未確認完成時亦顯示 PU1088」一句，其觸發為**異常路徑**，需注入未確認之情境（§12 之故障注入），與本條之正常路徑不同觸發（§5.7），037 未為其另切 leaf ——依 R-U56 為 OUT-OF-SCOPE，不列缺口。

---

## NR1L-UserProfiles-083 — SWE1-HMI-PROF-003（4.2 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC2.) A user can set up or customize a profile by inputting a username and avatar choice., but Profile setup/customization will not be required in order to use/interact with the head unit.

**037 description**：PRACC2.) A user can set up or customize a profile by inputting a username and avatar choice., but Profile setup/customization will not be required in order to use/interact with the head unit.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Head unit usable without setting up a Profile |
| pre_conditions | 1. The vehicle is on its default Profile with no username or avatar entered<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the Profile section and read the setup entry point<br>2. Leave the Profile section without entering a username or an avatar<br>3. Operate Media and Climate and check that both respond without a profile setup prompt |
| expected_result | 1. An entry point for entering a username and an avatar is available<br>2. The Profile section is left with no setup performed<br>3. Media and Climate respond and no setup prompt blocks them |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.2 |
| priority | **P1** — 未設定 profile 仍可使用主機 —— 主要功能之可用性 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文之兩半（可設定／設定非必要）為同一節之正反兩面，**併為一條**：ER1 驗其可設定，ER3 驗其非必要。受測之兩個功能（Media、Climate）為**測試設置之選擇**（J-12），非條文所指定 —— 條文寫的是 use/interact with the head unit。 |

**reasoning**：驗證目標：4.2（PRACC2）—— 使用者**得**以 username 與 avatar 設定 profile，但設定**非**使用主機之前提。關鍵情境條件：pre-condition 明訂尚未輸入 username 與 avatar，否則「非必要」無從觀察。為什麼這樣切：**只驗「可設定」則條文之重點（非必要）未被測** ——而那一半才是會被實作漏掉的。來源標示：Media 與 Climate 為**測試設置**（J-12），非 spec 指定。

---

## NR1L-UserProfiles-084 — SWE1-HMI-PROF-004-01（4.3 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC3.) All user preferences associated with a Profile will be stored by the system and remembered over key cycles. Profile preferences will be restored when the Profile is activated/chosen to be used (e.g., through memory seat buttons, key fob, or Head Unit).

**037 description**：System shall store and remember all user preferences associated with a Profile over key cycles.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile preferences remembered across a key cycle |
| pre_conditions | 1. A Driver Profile is active<br>2. The vehicle is stationary |
| input_test_data | Preference under test: Cluster Home screen (3.1) |
| test_procedure | 1. Set the preference under test to a new value and record it<br>2. Switch the ignition off and then on again<br>3. Read the preference and check that it matches the recorded value |
| expected_result | 1. The preference accepts the new value and it is recorded<br>2. The ignition is off and then on again with the same Driver Profile active<br>3. The preference matches the value recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.3 |
| priority | **P0** — 偏好跨 key cycle 之儲存 —— 核心五類之一 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | `key cycle` 之操作定義取 R-U21（設定 → key cycle → 讀回）——**其權威為裁決而非 spec**；4.3 之條文只寫 remembered over key cycles，未定義該循環之操作方式。 |

**reasoning**：驗證目標：4.3（PRACC3）之儲存側 —— 偏好跨 key cycle 保留。關鍵情境條件：**同一 profile 全程作用中** —— 若中途切換 profile，測到的會是 4.3.1 之切換前儲存，不是跨 key cycle。為什麼這樣切：037 對 4.3 切四個 leaf，本 leaf（-01）之單位為**跨 key cycle 之保留**；三條回復途徑分屬 -02／-03／-04。來源標示：`key cycle` 之操作定義出自 **R-U21（裁決）**，非 spec（J-4）。

---

## NR1L-UserProfiles-085 — SWE1-HMI-PROF-004-02（4.3 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC3.) All user preferences associated with a Profile will be stored by the system and remembered over key cycles. Profile preferences will be restored when the Profile is activated/chosen to be used (e.g., through memory seat buttons, key fob, or Head Unit).

**037 description**：System shall restore profile preferences when the Profile is activated via HU selection.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Preferences restored when a Profile is chosen on the head unit |
| pre_conditions | 1. Two Driver Profiles exist, each with a different value of the preference under test<br>2. The vehicle is stationary |
| input_test_data | Preference under test: Cluster Home screen (3.1) |
| test_procedure | 1. Activate Driver Profile A and record the preference<br>2. Activate Driver Profile B from the “All Profiles” tab<br>3. Read the preference and check that it matches Driver Profile B's own value |
| expected_result | 1. Driver Profile A is active and its preference is recorded<br>2. Driver Profile B is active<br>3. The preference matches Driver Profile B's own value and differs from the value recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.3 |
| priority | **P0** — 自主機選取後之回復 —— 回復機制本身 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | 三條回復途徑（主機選取／記憶座椅鍵／key fob）為 037 之三個 leaf，分屬 `SWE1-HMI-PROF-004-02`／`-03`／`-04`；本條為**主機選取**一途。 |

**reasoning**：驗證目標：4.3（PRACC3）之回復側，途徑為**自主機選取 profile**。關鍵情境條件：pre-condition 要求兩個 profile 之該偏好**值不同** ——值相同則「有回復」與「沒動過」無從分辨。為什麼這樣切：**ER3 併驗「與步驟 1 所記之值不同」** ——只驗「等於 B 之值」，一個根本不切換 profile 之實作若兩值恰同也會通過。刻意略過：另二途徑屬 `SWE1-HMI-PROF-004-03`（記憶座椅鍵）與 `SWE1-HMI-PROF-004-04`（key fob）。

---

## NR1L-UserProfiles-086 — SWE1-HMI-PROF-004-03（4.3 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC3.) All user preferences associated with a Profile will be stored by the system and remembered over key cycles. Profile preferences will be restored when the Profile is activated/chosen to be used (e.g., through memory seat buttons, key fob, or Head Unit).

**037 description**：System shall restore profile preferences when the Profile is activated via memory seat button.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Preferences restored when activated by a memory seat button |
| pre_conditions | 1. Two Driver Profiles exist, each linked to a different memory seat button<br>2. The two Profiles hold different values of the preference under test |
| input_test_data | Preference under test: Cluster Home screen (3.1) |
| test_procedure | 1. Activate Driver Profile A and record the preference<br>2. Select memory seat button 2, which is linked to Driver Profile B<br>3. Read the preference and check that it matches Driver Profile B's own value |
| expected_result | 1. Driver Profile A is active and its preference is recorded<br>2. Driver Profile B is active<br>3. The preference matches Driver Profile B's own value and differs from the value recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.3 |
| priority | **P1** — 記憶座椅鍵之回復途徑；主要功能之另一入口 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | 記憶座椅鍵之編號（2）為**測試設置**（J-12），非條文指定 ——4.3 只寫 through memory seat buttons。座椅與 profile 之連結規則屬 4.5.1／9.5.x，本條以其為前提。 |

**reasoning**：驗證目標：4.3（PRACC3）之回復側，途徑為**記憶座椅鍵**。關鍵情境條件：兩 profile 各連一個座椅鍵且該偏好值不同，使切換之效果可觀察。為什麼這樣切：三途徑各為一 leaf；本條不代測另二者。來源標示：座椅鍵編號為測試設置（J-12），非 spec 指定。

---

## NR1L-UserProfiles-087 — SWE1-HMI-PROF-004-04（4.3 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC3.) All user preferences associated with a Profile will be stored by the system and remembered over key cycles. Profile preferences will be restored when the Profile is activated/chosen to be used (e.g., through memory seat buttons, key fob, or Head Unit).

**037 description**：System shall restore profile preferences when the Profile is activated via key fob detection.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Preferences restored when a Profile is detected by key fob |
| pre_conditions | 1. Two Driver Profiles exist, each associated with a different key fob<br>2. The two Profiles hold different values of the preference under test |
| input_test_data | Preference under test: Cluster Home screen (3.1) |
| test_procedure | 1. Activate Driver Profile A and record the preference<br>2. Present the key fob associated with Driver Profile B<br>3. Read the preference and check that it matches Driver Profile B's own value |
| expected_result | 1. Driver Profile A is active and its preference is recorded<br>2. Driver Profile B is active<br>3. The preference matches Driver Profile B's own value and differs from the value recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.3 |
| priority | **P1** — key fob 偵測之回復途徑；主要功能之另一入口 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | key fob 與 profile 之關聯機制 spec 未於本節詳述，本條以其為 pre-condition；**其建立方式不在本 TC 之範圍**。 |

**reasoning**：驗證目標：4.3（PRACC3）之回復側，途徑為 **key fob 偵測**。關鍵情境條件：兩 profile 各關聯一支 key fob 且偏好值不同。為什麼這樣切：三途徑各為一 leaf；本條不代測另二者。刻意略過：key fob 關聯之建立流程 spec 於本節未述，不推定（§8.4.1）。

---

## NR1L-UserProfiles-088 — SWE1-HMI-PROF-005（4.3.1 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC3.1) If a Profile is switched within a key cycle, any changed preferences will be saved before the new Profile is loaded.

**037 description**：PRACC3.1) If a Profile is switched within a key cycle, any changed preferences will be saved before the new Profile is loaded.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Changed preferences saved before the next Profile loads |
| pre_conditions | 1. Two Driver Profiles exist, each with a recorded value of the preference under test<br>2. The two recorded values are different from each other |
| input_test_data | Preference under test: Cluster Home screen (3.1) |
| test_procedure | 1. Activate Driver Profile A and change the preference to a new value, then record it<br>2. Activate Driver Profile B and read the preference<br>3. Activate Driver Profile A and check that the preference matches the value recorded in step 1 |
| expected_result | 1. Driver Profile A is active and the changed value is recorded<br>2. Driver Profile B is active and its preference is its own value, not the value recorded in step 1<br>3. Driver Profile A is active and the preference matches the value recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.3.1; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.1; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.2; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.3; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.4; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.5 |
| priority | **P0** — 切換前先存 —— 失效即已變更之偏好遺失（資料遺失風險） |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | 引用欄併列 `3.1`–`3.5`（PLP 表，R-U22／R-U46）。**併列不等於該五列皆已被驗證** —— 覆蓋率不得以引用欄推定（J-1／D-UP17-01）；本 TC 實際受測之列項見 input_test_data。 **ER2 是順序之判別點**：若儲存發生在 Profile B 載入**之後**，A 之變更會落到 B 上 —— ER2 即在排除該實作。ER3 單獨只能證「有存到」，證不了「存在載入之前」。 |

**reasoning**：驗證目標：4.3.1（PRACC3.1）—— 同一 key cycle 內切換 profile 時，已變更之偏好**在新 profile 載入之前**先行儲存。關鍵情境條件：兩 profile 之該偏好值不同，且步驟 1 之新值與 B 之值不同。為什麼這樣切：**條文之重點是「先後」，而先後不能只用「回來還在」證明** ——「A 回來還在」（ER3）與「存在載入之前」相容，也與「載入之後才存」相容。**能分開兩者的是 ER2**：若實作在 B 載入後才寫入，那筆變更會被寫進 B（或覆蓋 B 之值）；故 ER2 斷言 **B 顯示的是 B 自己的值，不是步驟 1 所記之值**。兩條 ER 併存才構成順序之斷言 —— 這是本條與 4.3 之 -01 的分野。來源標示：受測偏好取自 PLP 表 3.1（§8.4.1）。

---

## NR1L-UserProfiles-089 — SWE1-HMI-PROF-006-01（4.4 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC4.) At the start of a new key cycle, Head Unit will load last known Profile unless a different Profile is detected or initiated (through the key fob or memory seat buttons).

**037 description**：System shall load last active profile at key-on.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Last known Profile loaded at the start of a key cycle |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle<br>2. No key fob associated with another Profile is present and no memory seat button is pressed at key-on |
| input_test_data | NA |
| test_procedure | 1. Activate Driver Profile B and record which Profile is active<br>2. Switch the ignition off and then on again<br>3. Read the active Profile and check that it matches the Profile recorded in step 1 |
| expected_result | 1. Driver Profile B is active and is recorded as the last known Profile<br>2. The ignition is off and then on again<br>3. Driver Profile B is active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.4 |
| priority | **P0** — key cycle 起始之 profile 載入 —— 切換機制本身 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | pre-condition 明列「無 key fob 偵測、未按記憶座椅鍵」——**該二者為條文所載之覆寫條件**，不排除則本條測不到預設路徑。覆寫側分屬 `SWE1-HMI-PROF-006-02`／`SWE1-HMI-PROF-006-03`。 |

**reasoning**：驗證目標：4.4（PRACC4）之預設路徑 —— 新 key cycle 起始載入上次之 profile。關鍵情境條件：**兩個覆寫條件皆須排除**（§8.7.3）；不排除則失敗時分不出是預設路徑壞了還是覆寫誤觸發。為什麼這樣切：037 對 4.4 切三個 leaf —— 預設路徑與兩個覆寫各一。刻意略過：覆寫由 `SWE1-HMI-PROF-006-02`（key fob）與 `SWE1-HMI-PROF-006-03`（記憶座椅鍵）承擔。

---

## NR1L-UserProfiles-090 — SWE1-HMI-PROF-006-02（4.4 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC4.) At the start of a new key cycle, Head Unit will load last known Profile unless a different Profile is detected or initiated (through the key fob or memory seat buttons).

**037 description**：If key fob profile detected, override last active profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Key fob detection overrides the last known Profile at key-on |
| pre_conditions | 1. Two Driver Profiles exist and Driver Profile B was the last active one<br>2. A key fob associated with Driver Profile A is available |
| input_test_data | NA |
| test_procedure | 1. Switch the ignition off<br>2. Present the key fob for Driver Profile A and switch on<br>3. Read the active Profile and check that it is Driver Profile A rather than the last known one |
| expected_result | 1. The ignition is off with Driver Profile B as the last known Profile<br>2. The ignition is on and the key fob is detected<br>3. Driver Profile A is active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.4 |
| priority | **P1** — key fob 之覆寫分支 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | §7 之列舉配對：正向為 `SWE1-HMI-PROF-006-01`（無覆寫則載入上次）。**兩條並存才擋得住一個永遠載入上次之實作**。 |

**reasoning**：驗證目標：4.4（PRACC4）之覆寫側，觸發為 **key fob 偵測**。關鍵情境條件：上次作用中之 profile 與 key fob 所指者**必須不同** ——相同則覆寫與否無從分辨。為什麼這樣切：與 `SWE1-HMI-PROF-006-01` 構成 §7 之配對。刻意略過：記憶座椅鍵之覆寫屬 `SWE1-HMI-PROF-006-03`。

---

## NR1L-UserProfiles-091 — SWE1-HMI-PROF-006-03（4.4 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC4.) At the start of a new key cycle, Head Unit will load last known Profile unless a different Profile is detected or initiated (through the key fob or memory seat buttons).

**037 description**：If memory seat button pressed, override last active profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Memory seat button overrides the last known Profile at key-on |
| pre_conditions | 1. Two Driver Profiles exist and Driver Profile B was the last active one<br>2. Driver Profile A is linked to memory seat button 1 |
| input_test_data | NA |
| test_procedure | 1. Switch the ignition off and then on again<br>2. Select memory seat button 1<br>3. Read the active Profile and check that it is Driver Profile A rather than the last known one |
| expected_result | 1. The ignition is off and then on again with Driver Profile B active<br>2. Memory seat button 1 is pressed<br>3. Driver Profile A is active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.4 |
| priority | **P1** — 記憶座椅鍵之覆寫分支 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | §7 之列舉配對：正向為 `SWE1-HMI-PROF-006-01`。座椅鍵編號（1）為**測試設置**（J-12）—— 4.4 只寫 memory seat buttons。 |

**reasoning**：驗證目標：4.4（PRACC4）之覆寫側，觸發為**記憶座椅鍵**。關鍵情境條件：上次作用中者與座椅鍵所連者不同。為什麼這樣切：與 `SWE1-HMI-PROF-006-01` 構成 §7 之配對；與 `SWE1-HMI-PROF-006-02` 之差別在觸發來源，兩者不合併（§5.7）。來源標示：座椅鍵編號為測試設置（J-12）。

---

## NR1L-UserProfiles-092 — SWE1-HMI-PROF-007-01（4.5 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC5.) If no custom Profile is set up, or all profiles are deleted, there will always be a default, non-connected profile in the vehicle. For first time use this default is called “Driver 1”. If Driver 1 Profile was customized (even if the name was maintained as Driver 1) and then all profiles have been deleted from the Head Unit, the default “Driver 1” Profile will return as the single profile in the vehicle (unless there are 2 or more memory seat buttons).

**037 description**：System shall create default Driver1 profile when no custom profiles exist.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Default non-connected Profile present when none is set up |
| pre_conditions | 1. The vehicle has no custom Driver Profile set up<br>2. The vehicle has fewer than 2 memory seat buttons |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab<br>2. Read the Profile list and check that a default Profile named “Driver 1” is present |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. A default Profile named “Driver 1” is present and it is not a connected Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.5 |
| priority | **P0** — 預設 profile 之存在保證 —— profile 建立之底線 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | **ER2 併驗 non-connected** —— 條文寫的是 a default, non-connected profile；只驗「有一個叫 Driver 1 的 profile」，一個把它建成連網 profile 之實作會通過。座椅數之 pre-condition 為排除 4.5.1 之多預設情形。 |

**reasoning**：驗證目標：4.5（PRACC5）首句 —— 未設定任何自訂 profile 時，車上恆有一個預設、非連網之 profile，首次使用時名為 “Driver 1”。關鍵情境條件：座椅鍵少於 2 個 —— 否則 4.5.1 會使預設 profile 有多個，與本條之「單一預設」情境混淆。為什麼這樣切：037 對 4.5 切三個 leaf；本 leaf 之單位為**預設之存在**。刻意略過：刪除後之重建屬 `SWE1-HMI-PROF-007-02`；重建後之單一形態屬 `SWE1-HMI-PROF-007-03`。

---

## NR1L-UserProfiles-093 — SWE1-HMI-PROF-007-02（4.5 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC5.) If no custom Profile is set up, or all profiles are deleted, there will always be a default, non-connected profile in the vehicle. For first time use this default is called “Driver 1”. If Driver 1 Profile was customized (even if the name was maintained as Driver 1) and then all profiles have been deleted from the Head Unit, the default “Driver 1” Profile will return as the single profile in the vehicle (unless there are 2 or more memory seat buttons).

**037 description**：If Driver1 was customized and delected, system shall recreate default Driver1.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Default Driver 1 recreated after all Profiles are deleted |
| pre_conditions | 1. The default Profile has been customized and its name is still “Driver 1”<br>2. The vehicle has fewer than 2 memory seat buttons |
| input_test_data | NA |
| test_procedure | 1. Delete every Profile from the head unit<br>2. Open the “All Profiles” tab<br>3. Read the Profile list and check that a default “Driver 1” Profile is present again |
| expected_result | 1. Every Profile is deleted<br>2. The “All Profiles” tab is displayed<br>3. A default “Driver 1” Profile is present and its preferences are at their default values |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.5 |
| priority | **P0** — 全部刪除後之預設重建 —— 資料遺失後之回復 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | **ER3 併驗「偏好為預設值」** —— 條文之 default 指的是**重建出一個預設 profile**，不是把原客製 profile 改名留下；只驗名稱，一個保留原客製內容之實作會通過。回復之範圍細節屬 `SWE1-HMI-PROF-012`（4.5.4）。 |

**reasoning**：驗證目標：4.5（PRACC5）第三句 —— 客製過之 Driver 1 於全部 profile 被刪除後，預設 “Driver 1” 重新出現。關鍵情境條件：**pre-condition 明訂該預設曾被客製** ——條文特別寫 even if the name was maintained as Driver 1，即「名稱沒變」不等於「沒被客製」。為什麼這樣切：本 leaf 之單位為**重建**；重建後只有一個 profile 之形態屬 `SWE1-HMI-PROF-007-03`。

---

## NR1L-UserProfiles-094 — SWE1-HMI-PROF-007-03（4.5 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC5.) If no custom Profile is set up, or all profiles are deleted, there will always be a default, non-connected profile in the vehicle. For first time use this default is called “Driver 1”. If Driver 1 Profile was customized (even if the name was maintained as Driver 1) and then all profiles have been deleted from the Head Unit, the default “Driver 1” Profile will return as the single profile in the vehicle (unless there are 2 or more memory seat buttons).

**037 description**：The default “Driver 1” Profile will return as the single profile in the vehicle (unless there are 2 or more memory seat buttons).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Recreated Driver 1 is the single Profile on the vehicle |
| pre_conditions | 1. Every Profile has been deleted from the head unit<br>2. The vehicle has fewer than 2 memory seat buttons |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab<br>2. Read the Profile list and check that “Driver 1” is the only Profile present |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. “Driver 1” is present and no other Driver Profile is listed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.5 |
| priority | **P1** — 重建後之單一 profile 形態；其座椅數條件為分支 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文之 `(unless there are 2 or more memory seat buttons)` 為**適用條件**，以 pre-condition 固定為少於 2 個；座椅鍵 ≥ 2 之情形由 `SWE1-HMI-PROF-008`（4.5.1）承擔。 |

**reasoning**：驗證目標：4.5（PRACC5）第三句之後半 —— 重建之 “Driver 1” 為車上**唯一**之 profile。關鍵情境條件：條文自帶之例外（座椅鍵 ≥ 2）以 pre-condition 排除，使「唯一」之斷言成立。為什麼這樣切：與 `SWE1-HMI-PROF-007-02` 之分野在斷言對象 ——-02 驗**重建發生**，本條驗**重建後只有一個**。**ER2 為缺席斷言（無其他 profile）**，只驗 Driver 1 在，一個留下殘餘 profile 之實作會通過。

---

## NR1L-UserProfiles-095 — SWE1-HMI-PROF-008（4.5.1 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC5.1) If there are memory seat buttons, there will be a default Driver Profile for each memory seat position/button (e.g., if there are 2 memory seat buttons there will be two default Profiles: memory seat button 1 defaults as linked to “Driver 1” Profile, and memory seat button two defaults as linked to “Driver 2” Profile)

**037 description**：PRACC5.1) If there are memory seat buttons, there will be a default Driver Profile for each memory seat position/button (e.g., if there are 2 memory seat buttons there will be two default Profiles: memory seat button 1 defaults as linked to “Driver 1” Profile, and memory seat button two defaults as linked to “Driver 2” Profile)

| 欄 | 值 |
|---|---|
| tc_title / test_item | One default Profile per memory seat button |
| pre_conditions | 1. The vehicle has 2 memory seat buttons<br>2. No custom Driver Profile is set up on the vehicle |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab<br>2. Read the seat links and check that each button has its own default Profile |
| expected_result | 1. The “All Profiles” tab is displayed<br>2. Two default Profiles are present: “Driver 1” linked to memory seat button 1 and “Driver 2” linked to memory seat button 2 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.5.1 |
| priority | **P1** — 每個記憶座椅位置之預設 profile；配置相依之分支 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文以「2 個座椅鍵」為例（e.g.），本 TC 以其為 pre-condition ——**該數字取自條文之例，非自擬**。座椅鍵 ≥ 3 之情形條文未述，依 §8.4.1 不推定。 |

**reasoning**：驗證目標：4.5.1（PRACC5.1）—— 有記憶座椅鍵時，每個座椅位置各有一個預設 Driver Profile。關鍵情境條件：座椅鍵數以條文之例（2）固定，且無自訂 profile —— 否則預設之數目會被自訂者干擾。為什麼這樣切：**ER 逐一指名兩個連結**（Driver 1 ↔ 鍵 1、Driver 2 ↔ 鍵 2）；只驗「有兩個預設 profile」，一個把兩者都連到同一鍵之實作會通過。刻意略過：座椅鍵三個以上之情形條文未述（§8.4.1 保留）。

---

## NR1L-UserProfiles-096 — SWE1-HMI-PROF-009（4.5.2 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC5.2) The memory seat preferences can be swapped between Driver Profiles, but there will always be one Driver Profile per memory seat position.

**037 description**：PRACC5.2) The memory seat preferences can be swapped between Driver Profiles, but there will always be one Driver Profile per memory seat position.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Memory seat preferences swapped between Driver Profiles |
| pre_conditions | 1. Two Driver Profiles exist, each linked to its own memory seat position<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read and record which Profile is linked to each memory seat position<br>2. Swap the memory seat preferences between the two Profiles<br>3. Read the links and check that each Profile now holds the other's seat position |
| expected_result | 1. The two Profile-to-seat links are recorded<br>2. The swap is accepted<br>3. Each Profile is linked to the seat position recorded for the other Profile in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.5.2 |
| priority | **P1** — 記憶座椅偏好之互換；主要功能之進階操作 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | §7 之列舉配對：反向為 `NR1L-UserProfiles-104`（同一座椅位置不得連上第二個 profile）。條文之後半「**永遠只有一個** Driver Profile per memory seat position」為全稱，**只驗互換成功不足以證之** —— 故另立反向。 |

**reasoning**：驗證目標：4.5.2（PRACC5.2）前半 —— 記憶座椅偏好可於 profile 間互換。關鍵情境條件：兩 profile 各有其座椅位置，互換之效果方可觀察。為什麼這樣切：條文有兩個斷言（可互換／每位置恆只有一個），**後者為全稱且為限制**，其失效形態與前者相反 ——併於一條則失敗時分不出是哪一個沒生效（§7）。反向由 `NR1L-UserProfiles-104` 承擔。

---

## NR1L-UserProfiles-097 — SWE1-HMI-PROF-010-01（4.5.3 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC5.3) If a Profile linked to a memory seat position is attempted to be deleted, and there is one or more other Profiles available without memory seats linked to it/them, automatically reassign that memory seat to the next available Profile (prioritizing from left to right based on the order of the Profiles on the All Profiles Tab). If there are no Profile’s available to link a memory seat position to, a default Profile associated with that seat position will be automatically created/restored by the system.

**037 description**：If a Profile linked to a memory seat position is attempted to be deleted, and there is one or more other Profiles available without memory seats linked to it/them, automatically reassign that memory seat to the next available Profile (prioritizing from left to right based on the order of the Profiles on the All Profiles Tab).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Memory seat reassigned to the next available Profile on delete |
| pre_conditions | 1. Three Driver Profiles exist and only one of them is linked to a memory seat position<br>2. The two unlinked Profiles are ordered left to right on the “All Profiles” tab |
| input_test_data | NA |
| test_procedure | 1. Read and record the order of the unlinked Profiles<br>2. Delete the Profile linked to the memory seat position<br>3. Read the seat link and check that it moved to the leftmost unlinked Profile |
| expected_result | 1. The order of the unlinked Profiles is recorded<br>2. The linked Profile is deleted<br>3. The memory seat position is linked to the leftmost unlinked Profile recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.5.3 |
| priority | **P1** — 刪除時之座椅自動改派；非主路徑分支 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文之優先順序為 prioritizing from left to right based on the order of the Profiles on the All Profiles Tab —— **ER 指名「最左」而非「任一」**：只驗「改派給某個 profile」，一個隨機挑選之實作會通過。 |

**reasoning**：驗證目標：4.5.3（PRACC5.3）前半 —— 刪除已連座椅之 profile 時，該座椅自動改派給下一個可用 profile，順序由左至右。關鍵情境條件：**須有兩個以上未連座椅之 profile** ——只有一個時，「由左至右」之優先順序無從觀察。為什麼這樣切：本 leaf 之單位為**有可用 profile 時之改派**；無可用 profile 之情形屬 `SWE1-HMI-PROF-010-02`。

---

## NR1L-UserProfiles-098 — SWE1-HMI-PROF-010-02（4.5.3 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC5.3) If a Profile linked to a memory seat position is attempted to be deleted, and there is one or more other Profiles available without memory seats linked to it/them, automatically reassign that memory seat to the next available Profile (prioritizing from left to right based on the order of the Profiles on the All Profiles Tab). If there are no Profile’s available to link a memory seat position to, a default Profile associated with that seat position will be automatically created/restored by the system.

**037 description**：If there are no Profile’s available to link a memory seat position to, a default Profile associated with that seat position will be automatically created/restored by the system.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Default Profile created when no Profile can take the seat |
| pre_conditions | 1. One Driver Profile exists and it is linked to a memory seat position<br>2. No other Driver Profile is available on the vehicle |
| input_test_data | NA |
| test_procedure | 1. Delete the Profile linked to the memory seat position<br>2. Open the “All Profiles” tab<br>3. Read the Profile list and check that a default Profile for that seat position is present |
| expected_result | 1. The linked Profile is deleted<br>2. The “All Profiles” tab is displayed<br>3. A default Profile associated with that seat position is present |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.5.3 |
| priority | **P1** — 無可用 profile 時之預設自動建立 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | §7 之列舉配對：正向為 `SWE1-HMI-PROF-010-01`（有可用 profile 則改派）。兩條之 pre-condition 互斥（有／無其他可用 profile），不重複覆蓋。 |

**reasoning**：驗證目標：4.5.3（PRACC5.3）後半 —— 無可用 profile 可連該座椅位置時，系統自動建立或回復一個與該位置關聯之預設 profile。關鍵情境條件：**車上只有一個 profile 且已連座椅** ——此為使條件成立之最小情境。為什麼這樣切：與 `SWE1-HMI-PROF-010-01` 構成 §7 之配對，兩者之 pre-condition 互斥。

---

## NR1L-UserProfiles-099 — SWE1-HMI-PROF-011（4.5.3.1 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC5.3.1) If a Profile linked to a memory seat position is deleted, the new active profile will be the profile that is now assigned to the current seat position.

**037 description**：PRACC5.3.1) If a Profile linked to a memory seat position is deleted, the new active profile will be the profile that is now assigned to the current seat position.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Newly assigned Profile becomes active after the linked one is deleted |
| pre_conditions | 1. Two Driver Profiles exist and Driver Profile A is linked to the current memory seat position<br>2. Driver Profile A is the active Profile |
| input_test_data | NA |
| test_procedure | 1. Delete Driver Profile A<br>2. Read and record which Profile now holds the seat position<br>3. Read the active Profile and check that it is the Profile recorded in step 2 |
| expected_result | 1. Driver Profile A is deleted<br>2. The current seat position is now linked to Driver Profile B<br>3. Driver Profile B is the active Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.5.3.1 |
| priority | **P1** — 刪除後之新現用 profile 判定 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | 本條與 `SWE1-HMI-PROF-010-01` 之分野：後者驗**座椅改派給誰**，本條驗**改派後誰成為現用 profile** —— 同一觸發之兩個結果，037 切為兩個 leaf（4.5.3 與 4.5.3.1），故不合併。 |

**reasoning**：驗證目標：4.5.3.1（PRACC5.3.1）—— 已連座椅之 profile 被刪除後，新現用 profile 為現在被指派到該座椅位置者。關鍵情境條件：被刪者須**同時是現用 profile 且連著現在的座椅位置** ——否則「新現用 profile」之判定與本條無關。為什麼這樣切：步驟 2 先讀出改派結果再於步驟 3 比對現用者，**使本條不依賴 `SWE1-HMI-PROF-010-01` 之改派規則是否正確** ——改派給誰由那條驗，本條只驗「改派給誰，誰就變成現用」。

---

## NR1L-UserProfiles-100 — SWE1-HMI-PROF-012（4.5.4 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC5.4) When default Driver 1-2 Profiles are restored, all Profile linked preferences are restored to the default state (as if the vehicle was just purchased).

**037 description**：PRACC5.4) When default Driver 1-2 Profiles are restored, all Profile linked preferences are restored to the default state (as if the vehicle was just purchased).

| 欄 | 值 |
|---|---|
| tc_title / test_item | All linked preferences reset when default Profiles are restored |
| pre_conditions | 1. The vehicle has 2 memory seat buttons with the default “Driver 1-2” Profiles<br>2. Both default Profiles have several profile-linked preferences changed from their defaults |
| input_test_data | Preferences under test: Cluster Home screen (3.1), SiriusXM 360L Listener Profile (3.2), Nav Saved destinations (3.4) |
| test_procedure | 1. Record the changed values of the three preferences for both default Profiles<br>2. Restore the default Driver Profiles<br>3. Read the three preferences for both Profiles and check that each is at its default value |
| expected_result | 1. The changed values are recorded for both default Profiles<br>2. The default Profiles are restored<br>3. The three preferences of both Profiles are at their default values and none holds a value recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.5.4; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.1; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.2; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.3; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.4; Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.5 |
| priority | **P0** — 預設回復時全部偏好歸零 —— 資料遺失風險項 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 引用欄併列 `3.1`–`3.5`（PLP 表，R-U22／R-U46）。**併列不等於該五列皆已被驗證** —— 覆蓋率不得以引用欄推定（J-1／D-UP17-01）；本 TC 實際受測之列項見 input_test_data。 條文之 as if the vehicle was just purchased 為**程度描述**，本 TC 以「三項 PLP 偏好皆回到預設值」為其可觀察之形式；**未宣稱已驗盡全部 PLP 列項**。 |

**reasoning**：驗證目標：4.5.4（PRACC5.4）—— 預設 Driver 1–2 profile 被回復時，所有 profile-linked 偏好回到預設狀態。關鍵情境條件：**兩個預設 profile 皆須有偏離預設之值** ——否則「回到預設」與「本來就是預設」無從分辨。為什麼這樣切：**ER3 併驗「無一項仍持步驟 1 所記之值」** ——只驗「等於預設值」，一個把預設值也改掉之實作可能仍通過。**代價聲明**：本條驗三項 PLP 列項，**非全部** ——全稱以單例驗證之限制見 D-UP16-02，其分母不得以引用欄推定（J-1）。

---

## NR1L-UserProfiles-101 — SWE1-HMI-PROF-013（4.6 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC6.) The Profile feature will have a button defaulted in the status bar (but status bar can be customized to remove it). The button icon will change depending on which profile is logged in.

**037 description**：PRACC6.) The Profile feature will have a button defaulted in the status bar (but status bar can be customized to remove it). The button icon will change depending on which profile is logged in. (image: %E5%9C%96%E7%89%87_1610819271.png) (image: %E5%9C%96%E7%89%87_19752790.png)

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile button present in the status bar by default |
| pre_conditions | 1. The status bar is at its default configuration<br>2. Two Driver Profiles exist with different avatars |
| input_test_data | NA |
| test_procedure | 1. Read the status bar and check that a Profile button is present<br>2. Activate the other Driver Profile<br>3. Read the status bar button and check that its icon changed with the active Profile |
| expected_result | 1. A Profile button is present in the status bar<br>2. The other Driver Profile is active<br>3. The Profile button icon differs from the icon read in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.6 |
| priority | **P2** — 狀態列按鈕之預設存在與其圖示變化；呈現層 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文之括號句（狀態列可被客製以移除該按鈕）為**另一觸發**，其行為由 `SWE1-HMI-PROF-016`（4.6.3）承擔；本條驗預設狀態。圖示之**內容**（avatar／首字母）屬 `SWE1-HMI-PROF-014`（4.6.1）。 |

**reasoning**：驗證目標：4.6（PRACC6）—— Profile 按鈕預設存在於狀態列，且其圖示隨作用中之 profile 改變。關鍵情境條件：兩 profile 之 avatar 不同，否則「圖示改變」無從觀察。為什麼這樣切：兩個斷言（預設存在／圖示隨 profile 變）為同一節之兩個結果，依 §5.7 併為一條之兩段。**ER3 以「與步驟 1 所讀不同」表述** —— 圖示之具體內容屬 4.6.1，本條只斷言其**改變**。

---

## NR1L-UserProfiles-102 — SWE1-HMI-PROF-014（4.6.1 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC6.1) When a customized Profile is active, the Profile button icon will indicate which profile is logged in (with avatar – if the avatar is just a color, the first character of the username will display in the center of the colored circle), as pictured above.

**037 description**：PRACC6.1) When a customized Profile is active, the Profile button icon will indicate which profile is logged in (with avatar – if the avatar is just a color, the first character of the username will display in the center of the colored circle), as pictured above.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile button icon shows the active customized Profile |
| pre_conditions | 1. A customized Driver Profile is active<br>2. The avatar of that Profile is a plain colour with no picture |
| input_test_data | NA |
| test_procedure | 1. Read the status bar Profile button<br>2. Read the button icon and check that it carries the first character of the username |
| expected_result | 1. The status bar Profile button is displayed<br>2. The button icon shows the coloured circle with the first character of the username in its centre |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.6.1 |
| priority | **P2** — 客製 profile 之圖示內容；呈現層 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文有兩種 avatar 形態（圖像／純色）；**本 TC 取純色一側**，因其斷言最具體（首字母置中）。圖像 avatar 之情形條文只寫 with avatar，未另述其呈現，依 §8.4.1 不推定，故不另立 TC。 |

**reasoning**：驗證目標：4.6.1（PRACC6.1）—— 客製 profile 作用中時，狀態列按鈕圖示指出登入者；avatar 為純色時，username 之首字元顯示於色圈中央。關鍵情境條件：**avatar 須為純色** —— 那是條文唯一給出具體呈現之分支。為什麼這樣切：**取條文最具體之一側** ——圖像 avatar 之呈現條文未述，寫進 ER 會是推定（§8.4.1）。刻意略過：按鈕之存在與圖示會變屬 `SWE1-HMI-PROF-013`。

---

## NR1L-UserProfiles-103 — SWE1-HMI-PROF-015（4.6.2 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC6.2) When the Profile section is open, the button will be in the active state (highlighted).

**037 description**：PRACC6.2) When the Profile section is open, the button will be in the active state (highlighted).

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile button highlighted while the Profile section is open |
| pre_conditions | 1. The status bar is at its default configuration<br>2. The Profile section is closed |
| input_test_data | NA |
| test_procedure | 1. Read the status bar Profile button and record its state<br>2. Open the Profile section<br>3. Read the Profile button and check that it is in the active state |
| expected_result | 1. The Profile button state is recorded<br>2. The Profile section is open<br>3. The Profile button is highlighted |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.6.2 |
| priority | **P3** — 開啟時之 highlight 狀態；UI 強化 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 以關閉狀態為基準線（§5.6）—— 只讀開啟後之狀態，一個永遠 highlight 之實作會通過。 |

**reasoning**：驗證目標：4.6.2（PRACC6.2）—— Profile 區開啟時，按鈕為 active （highlighted）狀態。關鍵情境條件：pre-condition 明訂 Profile 區起始為關閉，使開啟前後之對照成立。為什麼這樣切：**步驟 1 之基準線是必要的** ——無基準線則「highlight」與「本來就 highlight」無從分辨（§5.6）。刻意略過：按鈕被移除後之 highlight 屬 `SWE1-HMI-PROF-016`。

---

## NR1L-UserProfiles-104 — SWE1-HMI-PROF-016（4.6.3 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC6.3) If the Profile button is removed from the status bar (through status bar customization), the highlight states of the button still apply to it in the Status bar edit mode drawer and the app drawer.

**037 description**：PRACC6.3) If the Profile button is removed from the status bar (through status bar customization), the highlight states of the button still apply to it in the Status bar edit mode drawer and the app drawer.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Highlight states kept after the Profile button is removed |
| pre_conditions | 1. The Profile button has been removed from the status bar through status bar customization<br>2. The Profile section is closed |
| input_test_data | NA |
| test_procedure | 1. Open the status bar edit mode drawer and record its state<br>2. Open the Profile section from the app drawer<br>3. Read the Profile button in both the edit mode drawer and the app drawer and check its highlight |
| expected_result | 1. The Profile button is shown in the status bar edit mode drawer<br>2. The Profile section is open<br>3. The Profile button is highlighted in the status bar edit mode drawer and in the app drawer |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.6.3 |
| priority | **P3** — 移除後 highlight 於他處之保留；罕用情境 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文指名**兩個**位置（status bar edit mode drawer 與 app drawer），故 ER3 兩處併驗 —— 只驗其一，另一處失效不會被發現。 |

**reasoning**：驗證目標：4.6.3（PRACC6.3）—— Profile 按鈕自狀態列移除後，其 highlight 狀態仍適用於 status bar edit mode drawer 與 app drawer。關鍵情境條件：**按鈕須先被移除**（§8.7.3），否則本條與 4.6.2 同情境。為什麼這樣切：條文指名兩個位置，ER 逐一斷言。刻意略過：狀態列客製化之操作流程屬他 feature（Home），本條以其結果為前提。

---

## NR1L-UserProfiles-105 — SWE1-HMI-PROF-009-neg（4.5.2 / Preference Storage）

**spec 原文（`pdf_text`）**：

> PRACC5.2) The memory seat preferences can be swapped between Driver Profiles, but there will always be one Driver Profile per memory seat position.

**037 description**：PRACC5.2) The memory seat preferences can be swapped between Driver Profiles, but there will always be one Driver Profile per memory seat position.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Second Profile refused on an occupied memory seat position |
| pre_conditions | 1. Two Driver Profiles exist and Driver Profile A is linked to memory seat position 1<br>2. Driver Profile B is linked to another seat position |
| input_test_data | NA |
| test_procedure | 1. Read and record which Profile holds memory seat position 1<br>2. Attempt to link Driver Profile B to memory seat position 1 as well<br>3. Read the seat links and check that position 1 still holds exactly one Profile |
| expected_result | 1. Memory seat position 1 is recorded as linked to Driver Profile A<br>2. The attempt is not accepted as an additional link<br>3. Memory seat position 1 is linked to exactly one Driver Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.5.2 |
| priority | **P1** — 同一座椅位置不得連上第二個 profile —— 全稱限制之反向 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | §7 之列舉配對：正向為 `NR1L-UserProfiles-096`（`SWE1-HMI-PROF-009`，互換成功）。條文之「**there will always be one** Driver Profile per memory seat position」為全稱限制 —— **只驗互換成功不足以證之**，故另立本條。座椅位置編號（1）為測試設置（J-12）。 |

**reasoning**：驗證目標：4.5.2（PRACC5.2）後半之全稱限制 ——每個記憶座椅位置**恆只有一個** Driver Profile。關鍵情境條件：該位置已被 A 佔用，B 另有其位 ——使「再連一個」成為明確之非法操作。為什麼這樣切：**全稱之限制只能以反向證之** ——正向（互換成功）與「允許一位置連兩個」相容，故 `SWE1-HMI-PROF-009` 之正向不足以擋下該實作（§7）。**ER3 斷言「恰好一個」而非「B 沒連上」** ——後者容許實作把 A 踢掉再連 B，那同樣違反條文。

---

## NR1L-UserProfiles-106 — SWE1-HMI-PROF-048-del（6.2.1 / Defaults）

**spec 原文（`pdf_text`）**：

> NOPR1.1) The user does not need to customize the Default Profile(s) before creating a different new Profile. Driver 1 and any other default Profiles will remain on the vehicle until a user customizes or deletes it.

**037 description**：NOPR1.1) The user does not need to customize the Default Profile(s) before creating a different new Profile. Driver 1 and any other default Profiles will remain on the vehicle until a user customizes or deletes it.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Default Profile no longer default after it is customized |
| pre_conditions | 1. The vehicle is on its default Profiles with no custom Profile set up<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and record the default Profiles present<br>2. Customize one default Profile with a username and an avatar<br>3. Read the Profile list and check that the customized one is no longer listed as a default |
| expected_result | 1. The default Profiles present are recorded<br>2. The chosen Profile carries the entered username and avatar<br>3. The customized Profile is no longer a default Profile while the other recorded defaults remain |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.2.1 |
| priority | **P1** — 預設 profile 於客製或刪除後之消失 —— 預設之生命週期 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | **A-UP13 行為 1（23 包 M-2 掃出，25 包定歸屬）**：6.2.1 之條文為 `Driver 1 and any other default Profiles will remain on the vehicle **until a user customizes or deletes it**`，而 `NR1L-UserProfiles-005` 只驗其前半（未客製化前仍在）。本條驗其後半 —— **兩條同一 leaf**。**不得與 `SWE1-HMI-PROF-007-02`（4.5）混淆**：該 leaf 驗「刪除全部後 Driver 1 重建」，本條驗「客製後該 profile 不再是預設」—— 兩件事。 |

**reasoning**：驗證目標：6.2.1（NOPR1.1）之後半 —— 預設 profile 留在車上，**直到使用者將其客製化或刪除**。關鍵情境條件：起始須為純預設狀態，且**保留另一個未被客製之預設**作為對照（ER3 之後半）。為什麼這樣切：**ER3 併驗「其餘預設仍在」** ——只驗「被客製者不再是預設」，一個把全部預設都清掉之實作會通過。本條與 `NR1L-UserProfiles-005` 同屬 `SWE1-HMI-PROF-048`，分驗該 description 之前後兩半。

---

## NR1L-UserProfiles-107 — SWE1-HMI-PROF-059-02（7.2.1 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL2.1) The large welcome popup will show the active (logged in) Profile username and avatar, and display other available profiles, including avatar, username, and memory seat assignment if applicable. Choosing “More Options” will take user to Edit Profile tab. If a different Profile is selected, show the applicable welcome popup for the new active profile.

**037 description**：Choosing the “More Options” button from the large welcome popup must navigate the user directly to the "Edit Profile" tab of the active profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | More Options on the welcome popup opens the Edit Profile tab |
| pre_conditions | 1. The large welcome popup is displayed for the active Driver Profile<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press “More Options” on the large welcome popup<br>2. Read the screen and check that the “Edit Profile” tab of the active Profile is displayed |
| expected_result | 1. The “More Options” button is pressed<br>2. The “Edit Profile” tab of the active Driver Profile is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.2.1 |
| priority | **P2** — 自 welcome popup 進入 Edit Profile 之導向；呈現層之入口 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | **A-UP13 行為 2**：23 輪記為「無人覆蓋」，25 輪查 037 後更正 —— 本行為有專屬 leaf （`SWE1-HMI-PROF-059-02`），當時只是尚未取樣。**ER2 併驗「現用 profile 之」分頁** —— 只驗「Edit Profile 開了」，一個開到別的 profile 之實作會通過。 |

**reasoning**：驗證目標：7.2.1（PRWEL2.1）之 `Choosing “More Options” will take user to Edit Profile tab`。關鍵情境條件：須為**大型** welcome popup —— 小型 popup（7.2）無此按鈕。為什麼這樣切：037 對 7.2.1 切三個 leaf，本 leaf 之單位即此一導向；popup 之內容屬 `SWE1-HMI-PROF-059-01`（`NR1L-UserProfiles-007`）。

---

## NR1L-UserProfiles-108 — SWE1-HMI-PROF-059-03（7.2.1 / Welcome Flow）

**spec 原文（`pdf_text`）**：

> PRWEL2.1) The large welcome popup will show the active (logged in) Profile username and avatar, and display other available profiles, including avatar, username, and memory seat assignment if applicable. Choosing “More Options” will take user to Edit Profile tab. If a different Profile is selected, show the applicable welcome popup for the new active profile.

**037 description**：If the user selects a different profile from the list of available profiles on the large welcome popup, the system must switch to that selected profile and subsequently display the applicable welcome popup for the newly active profile.

| 欄 | 值 |
|---|---|
| tc_title / test_item | Selecting another Profile switches and shows its welcome popup |
| pre_conditions | 1. The large welcome popup is displayed for Driver Profile A and lists Driver Profile B<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read and record the active Profile shown on the large welcome popup<br>2. Select Driver Profile B from the list on the popup<br>3. Read the screen and check that Driver Profile B is active with its own welcome popup |
| expected_result | 1. Driver Profile A is recorded as the active Profile<br>2. Driver Profile B is selected<br>3. Driver Profile B is the active Profile and the applicable welcome popup for it is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.2.1 |
| priority | **P1** — 自 welcome popup 切換 profile 並顯示新 popup —— 切換路徑之一 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | **A-UP13 行為 3**：同行為 2，有專屬 leaf （`SWE1-HMI-PROF-059-03`）而尚未取樣，25 輪更正記載。**ER3 併驗「切換」與「新 popup」兩者** —— 只驗 popup 換了，一個顯示 B 之 popup 卻未真正切換之實作會通過。popup 之尺寸取決於 7.2／7.2.1 之條件，故 ER 寫 the applicable welcome popup，不指定大小。 |

**reasoning**：驗證目標：7.2.1（PRWEL2.1）之 `If a different Profile is selected, show the applicable welcome popup for the new active profile`。關鍵情境條件：popup 須列出另一個 profile，否則選取無從發生。為什麼這樣切：**條文之 applicable 指其形態由別處決定** ——ER 照錄該不確定性，不推定為大型或小型（§8.4.1）。刻意略過：welcome popup 之尺寸判準屬 7.2／7.2.1 之其他斷言。

---
