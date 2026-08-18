# 上繳 17（B）— pilot 16 條之 ER 逐句出處對照

- 產出層：執行層｜2026-08-18｜對象：分析層（**判讀由分析層為之**）
- 下放包：`17_batch01.md` 作業 B
- 對照對象：`generated/` 之 16 條 TC，**共 55 句 ER**
- 出處基準：`outline_map.json` 之 **`pdf_text`**（R-U35 (a)）；
  表格類另註 **PDF 版面**（`scripts/render_spec_region.py`）

## 0. 判讀方式與四種關係

| 關係 | 意義 |
|---|---|
| **逐字引用** | ER 之該部分與 spec 字串**完全相同**（含引號內之 label、popup 字串）|
| **改寫自** | 語意相同、措辭調整（時態、主被動、拆句）|
| **由該句推得** | spec 未直說，但**由該句可推出**；推理步驟於備註載明 |
| **無直接出處** | spec 沒有這句話。**逐條具名，不以「合理推得」帶過** |

`無直接出處` 再分兩型（**這個分型是本表最重要的產出**）：

- **(步)＝步驟回聲** —— 該 ER 只是複述其步驟做了什麼（setup／transition 之結果），
  不承載驗證。**其無出處是正常的**，但須看得出來哪些 ER 不承載驗證。
- **(缺)＝真缺口** —— 該 ER **承載驗證**卻無 spec 依據。**這是本表要找的東西。**

## 0.1 總計

| 關係 | 句數 |
|---|---|
| 逐字引用 | 9 |
| 改寫自 | 20 |
| 由該句推得 | 8 |
| **無直接出處（步）步驟回聲** | **14** |
| **無直接出處（缺）真缺口** | **4** |
| 合計 | **55** |

**四個真缺口集中於兩個形態**，見 §3。

---

## 1. 逐條對照

### NR1L-UserProfiles-001（4.1，PRACC1）

`pdf_text`：`PRACC1.) The system will store and recall each unique Driver Profile’s preferences: see list of linked content above. If a feature is unavailable for a vehicle or region, ignore requirement.`

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | Driver Profile A is active | —— | —— | **無直接出處（步）** |
| 2 | The three preferences accept the new values | —— | —— | **無直接出處（步）** |
| 3 | The values set in step 2 are recorded | —— | —— | **無直接出處（步）** |
| 4 | Driver Profile A is active again | —— | —— | **無直接出處（步）** |
| 5 | The three preferences match the values recorded in step 3 | 4.1 | `will store and recall each unique Driver Profile’s preferences` | **改寫自** |

**字面值之出處**：`input_test_data` 之三項偏好名稱
（`Cluster Home screen`／`SiriusXM 360L Listener Profile`／`Nav Saved destinations`）
**逐字取自 3.1／3.2／3.4 之 `pdf_text`**（PLP 表列項）。

### NR1L-UserProfiles-002（4.1.1，PRACC1.2）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | PU_0118 is displayed | 4.1.1 | `by pressing Yes in pop-up PU_0118` | **由該句推得**（要能按 Yes，該 popup 須先顯示）|
| 2 | PU1087 is displayed | 4.1.1 | `PU1087 is displayed when users confirm Setting restore to default` | **改寫自** |
| 3 | The head unit does not receive the completion confirmation | —— | —— | **無直接出處（步）**（注入之故障）|
| 4 | PU1088 is displayed | 4.1.1 | `PU1088 is displayed if HU or TBM do not confirm complete default restoring` | **逐字引用** |

**字面值**：`PU_0118`／`PU1087`／`PU1088` **三者皆逐字取自 4.1.1 同一段**
（含 `PU_0118` 之底線寫法 —— 差異在 spec 本身，見 16 輪 S-1）。

### NR1L-UserProfiles-003（5.2，PRACC8 ＋ 5.1.2，PRACC7.2）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | The Add New Profile button is present while four Driver Profiles exist | 5.2 | `When the Maximum number of Profiles (5) is reached,: the Add New Profile button will not be present` | **由該句推得** ⚠ |
| 2 | The fifth Driver Profile is created | 5.2 | `There can be up to five (5) Driver Profiles per vehicle` | **改寫自** |
| 3a | The Add New Profile button is not present | 5.2 | `the Add New Profile button will not be present` | **逐字引用** |
| 3b | the icon and the string “This icon is associated to settings that are specific to your profile and are not shared across the vehicle” are not present | 5.2 ＋ **5.1.2** | 5.2：`the icon and the string described in note PRACC7.2 will not be present either`；5.1.2：`An icon and the following string will always show…: “This icon is associated…”` | **逐字引用**（字串取自 5.1.2）|
| 3c | “Max Profiles reached. Delete to create a new one.” (PU0584) is displayed | 5.2 | `“Max Profiles reached. Delete to create a new one.” (PU0584)` | **逐字引用** |

> ⚠ **ER1 之推理須具名**：spec 只寫「達上限時按鈕不在」，
> **並未寫「未達上限時按鈕在」**。ER1 是取其反面作為基準線（§5.6）。
> 屬**合理但非明文**之推得 —— 分類為「由該句推得」而非「改寫自」，
> 即為了讓這一步看得見。

### NR1L-UserProfiles-004（5.9，PRACC15）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | Driver Profile A is active | —— | —— | **無直接出處（步）** |
| 2 | The seat, mirror and steering wheel positions are adjusted | —— | —— | **無直接出處（步）** |
| 3 | No memory seat set or save control is pressed | 5.9 | `Pushing the memory seat set/save hard or soft controls is not required` | **改寫自** |
| 4 | The vehicle completes the ignition cycle | —— | —— | **無直接出處（缺）① —— 見 §3.1** |
| 5 | The three positions match those set in step 2 | 5.9 | `The Driver Profile Preferences will be saved locally to the vehicle automatically` | **由該句推得** |

**字面值**：受測偏好名 `Memory Profiles (Seats, mirrors, steering wheel)`
**逐字取自 3.5 之 `pdf_text`**。

### NR1L-UserProfiles-005（6.2.1，NOPR1.1）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | The default Profiles, including Driver 1, are recorded | 6.2.1 | `Driver 1 and any other default Profiles` | **改寫自** |
| 2 | The new Driver Profile is created and no default Profile is customized | 6.2.1 | `The user does not need to customize the Default Profile(s) before creating a different new Profile` | **改寫自** |
| 3 | The default Profiles recorded in step 1 are still present | 6.2.1 | `will remain on the vehicle until a user customizes or deletes it` | **改寫自** |

### NR1L-UserProfiles-006（6.4.1，NOPR3.1）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | The “Get Started” button is displayed | 6.4.1 | `pressing “Get Started”` | **由該句推得** |
| 2 | PU0585 is displayed and the Connected Account Login/Register screen is not displayed | 6.4.1 | `will show PU0585 and will not show Connected Account Login/Register Screen` | **逐字引用** |

### NR1L-UserProfiles-007（7.2.1，PRWEL2.1）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | The large welcome popup is displayed | 7.2.1 | `The large welcome popup will show…` | **由該句推得** |
| 2 | Driver Profile A’s username and avatar are displayed, and the other available Profile is displayed with its avatar, username and memory seat assignment | 7.2.1 | `will show the active (logged in) Profile username and avatar, and display other available profiles, including avatar, username, and memory seat assignment if applicable` | **改寫自** |

### NR1L-UserProfiles-008（7.4，PRWEL4）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | The Welcome Popup is displayed and the timer is started | —— | —— | **無直接出處（步）** |
| 2 | The Welcome Popup is still displayed at 29 seconds | —— | —— | **無直接出處（缺）② —— 見 §3.2** |
| 3 | The Welcome Popup is cleared at 30 seconds | 7.4 | `will clear when the vehicle is in motion or after 30 seconds or if the user interacts with the screen (whichever comes first)` | **改寫自** |

### NR1L-UserProfiles-009（8.7，NEWPR6）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | The username field shows the 11 characters typed | —— | —— | **無直接出處（步）** |
| 2 | The username field shows 12 characters | 8.7 | `The Maximum number of characters for a username is ~12 characters` | **改寫自**（`~12` → 12 之取值見 remarks 與 14 輪 §5）|
| 3 | The username field still shows 12 characters and the further character is not accepted | 8.7 | `the keyboard will not allow typing more` | **改寫自** |

### NR1L-UserProfiles-010（8.4.1，NEWPR3.1 ＋ 5.1.1，PRACC7.1）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | The username is accepted | —— | —— | **無直接出處（步）** |
| 2 | The avatar is selected | —— | —— | **無直接出處（步）** |
| 3 | The vehicle completes the ignition cycle | —— | —— | **無直接出處（缺）① —— 同 §3.1** |
| 4 | The Profile List is displayed | —— | —— | **無直接出處（步）** |
| 5 | The Profile carrying the username and avatar from steps 1 and 2 is listed | 8.4.1 ＋ **5.1.1** | 8.4.1：`the system will save the profile`；5.1.1：`When on the “All Profiles” tab, all available users will be shown` | **由該句推得** ⚠ |

> ⚠ **本輪之引用修正**：8.4.1 **只說系統會儲存，沒說它會出現在 Profile List**。
> 「列於 Profile List」這個觀察點出自 **5.1.1**，而該節原本**未被引用**。
> 依 F-1 之判準（驗證**或倚為 setup／觀察點**者須引用），
> 已於本輪補列 `5.1.1` 至 `REF_EXTRA`。
> **這是作業 B 挖出的第二種引用問題** —— F-1 是「多引了不相干的節」，
> 本項是「**少引了真正倚賴的節**」。同一個判準，兩個方向。

### NR1L-UserProfiles-011（9.3.2，EDPR3.2 ＋ 9.3.1，EDPR3.1）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | The username editing page is displayed | —— | —— | **無直接出處（步）** |
| 2 | The vehicle is in motion | —— | —— | **無直接出處（步）** |
| 3a | The previous available page is displayed | 9.3.2 | `system should return to previous available page` | **逐字引用** |
| 3b | the bonk tone is played | 9.3.2 ＋ 9.3.1 | 9.3.2：`play the bonk`；9.3.1：`a bonk tone will be played` | **改寫自** |
| 3c | “Function not available while vehicle in Motion.” is displayed | **9.3.1** | `the message “Function not available while vehicle in Motion.”` | **逐字引用** |

**字面值**：訊息字串逐字取自 **9.3.1**（9.3.2 以 `the message specified above` 指之）。
**變體覆寫**：must_carry（PDF p14）之 `R1 High Only: "Stellantis Account" →
"Connected Account"` 已注入，本 TC 之字面值未出現禁用字串（`lint_variant_labels` 語料 0 違規）。

### NR1L-UserProfiles-012（9.8，EDPR9）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | The “My Profile” Settings section is displayed | 9.8 | `will link directly to the “My Profile” Settings section` | **逐字引用**（label）|
| 2 | No back button to the Profile section is present on the “My Profile” Settings section | 9.8 | `will not have a back button to return to the Profile section` | **改寫自** |

**未寫入之 must_carry**：`PU0609` 之句（設定變更時提示）—— 其觸發為「變更設定」
而非「按 More Settings」，屬不同觸發且 037 無對應 leaf（13 輪 §5.5 第 2 項之缺口）。

### NR1L-UserProfiles-013（11.4，CPA2 ＋ **PDF p17 版面**）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | An info icon is displayed next to Connected Account | 11.4 | `Clicking on the info icon next to Connected Account in the Edit Profile tab` | **由該句推得** |
| 2a | The screen titled “What are the benefits of creating an Connected account?” | 11.4 | 同字串（含冠詞誤用）| **逐字引用** |
| 2b | two columns labeled Connected account and Local Profile | 11.4 | `will show two columns labeled Connected account and Local Profile` | **逐字引用** |
| 2c | “Synchronize your profile between multiple vehicles. The cloud will remember your preferences” | 11.4 | 同字串 | **逐字引用** |
| 2d | “Create a profile specific to this vehicle. The vehicle will remember your preferences” | 11.4 | 同字串 | **逐字引用** |
| 2e | 四列與其欄別（a–d）| **PDF p17 之 Table CPA2 版面** | 格線 6 條水平／4 條垂直、勾記 5 處之座標判定 | **逐字引用（版面）** |

**2e 之出處不是 `pdf_text`** —— 文字層把該表攤平，欄別在其中不存在。
其判讀由 `scripts/render_spec_region.py --regression` **可重跑複驗**（7/7 PASS）。

### NR1L-UserProfiles-014（11.5，CPA3）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | Driver Profile A is active | —— | —— | **無直接出處（步）** |
| 2 | The App Store app is recorded in Driver Profile A’s app tray | 11.5 | `it should only appear in the app tray for the local user that has installed it` | **由該句推得** |
| 3 | The App Store app is removed from Driver Profile A’s app tray | 11.5 | `If an App Store app is deleted, it would only be deleted for the user who has uninstalled it` | **改寫自** |
| 4 | Driver Profile B is active | —— | —— | **無直接出處（步）** |
| 5 | The App Store app is still present in Driver Profile B’s app tray | 11.5 | 同上（`only … for the user who has uninstalled it` 之反面）| **改寫自** |

### NR1L-UserProfiles-015（12.9，PVAL9）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | The Valet Mode deactivation screen is displayed | —— | —— | **無直接出處（步）** |
| 2 | Each of the nine incorrect PIN entries is rejected | 12.9 | `the user will have 10 attempts to type a 4 digit PIN` | **改寫自** |
| 3 | The deactivation screen still accepts a further PIN entry | —— | —— | **無直接出處（缺）② —— 同 §3.2** |
| 4 | The deactivation is cancelled on the tenth incorrect attempt and a further PIN entry is not accepted | 12.9 | `before system cancels the deactivation. The user can try again in 30min` | **改寫自** |

### NR1L-UserProfiles-016（13.2，PVALSPK2）

| ER | 原句 | 出處 | 片段 | 關係 |
|---|---|---|---|---|
| 1 | Any screen or popup that would allow a Valet Mode exit is blocked (PU0934) | 13.2 | `Any screens or popups that may allow a user to exit Valet Mode must be blocked (PU0934, etc)` | **逐字引用** |
| 2 | Valet Mode is still active after the SPAAK user’s attempt | 13.2 | `The SPAAK user cannot exit Valet Mode from the head unit` | **改寫自** |
| 3 | The owner’s remote deactivation is accepted | 13.2 | `Only the owner can deactivate Valet Mode remotely via app or website or other supported methods` | **改寫自** |
| 4 | Valet Mode is no longer active on the head unit | 13.2 | 同上 | **由該句推得** |

---

## 2. ER 中之字面值 —— 全部出處（作業 B 明文）

| 字面值 | 出現於 | 出處節次 | 關係 |
|---|---|---|---|
| `Cluster Home screen`／`SiriusXM 360L Listener Profile`／`Nav Saved destinations` | TC-001 資料欄 | 3.1／3.2／3.4 | 逐字 |
| `Memory Profiles (Seats, mirrors, steering wheel)` | TC-004 資料欄 | 3.5 | 逐字 |
| `PU_0118`／`PU1087`／`PU1088` | TC-002 | 4.1.1 | 逐字 |
| `“This icon is associated to settings that are specific to your profile and are not shared across the vehicle”` | TC-003 ER3 | **5.1.2** | 逐字 |
| `“Max Profiles reached. Delete to create a new one.”`／`PU0584` | TC-003 ER3 | 5.2 | 逐字 |
| `PU0585`／`Connected Account Login/Register Screen` | TC-006 ER2 | 6.4.1 | 逐字 |
| `“Function not available while vehicle in Motion.”` | TC-011 ER3 | **9.3.1** | 逐字 |
| `“My Profile”` | TC-012 ER1 | 9.8 | 逐字 |
| `“What are the benefits of creating an Connected account?”` 等四個字串 | TC-013 ER2 | 11.4 | 逐字 |
| Table CPA2 四列名與其欄別 | TC-013 ER2 | **PDF p17 版面** | 逐字（版面）|
| `PU0934` | TC-016 ER1 | 13.2 | 逐字 |
| `12`（字元上限）| TC-009 | 8.7（spec 為 `~12`）＋ 037 leaf（`12`）| **取 037 之值，已具名** |
| `30 seconds`／`10 attempts`／`5 (5) Driver Profiles` | TC-008／015／003 | 7.4／12.9／5.2 | 逐字 |

**未出現於任何 ER 之自擬字面值：0。**

---

## 3. 四個真缺口（**承載驗證卻無 spec 依據**）

### 3.1 缺口① —— `ignition cycle`（TC-004 ER4、TC-010 ER3）

spec **從未提及** ignition cycle。它是**執行層選定之觀察點**：
以「key cycle 後仍在」證明「已存於車端」（Service B 群，R-U21）。

- 5.9 之文為 `saved locally to the vehicle automatically`
- 8.4.1 之文為 `the system will save the profile`

**「已儲存」是狀態，不是可觀察事件** —— 要驗它必須選一個觀察方式，
而 spec 沒指定。**R-U21 指定了，spec 沒有。**

**處置建議**：不改（該觀察點是本 feature 之既定作法），
但**這兩句 ER 之權威是 R-U21，不是 spec** —— 覆核時應以此讀。

### 3.2 缺口② —— 邊界之「前一刻仍成立」（TC-008 ER2、TC-015 ER3）

| ER | 句 | spec 說了什麼 | spec 沒說什麼 |
|---|---|---|---|
| TC-008 ER2 | The Welcome Popup is **still displayed at 29 seconds** | 30 秒後清除 | **29 秒時仍在** |
| TC-015 ER3 | The deactivation screen **still accepts a further PIN entry**（第 9 次後）| 第 10 次取消 | **第 9 次後仍可續試** |

**兩句都是 BVA 之「界前基準線」（§5.6）**，其真值**由邊界之語意推得**，
而非由條文明述 —— 若系統在 25 秒就清除，spec 之字面仍為真（「30 秒後清除」
可讀成「不遲於 30 秒」），但 TC 會 FAIL。

**這是一個判準問題，不是一條 TC 的問題**：
凡以邊界值分析設計之 TC，其「界前」ER 皆屬此形態。本批 4 條 BVA
（TC-003／008／009／015）中，TC-003 之界前基準線亦同此形態（已標 ⚠），
TC-009 之 11 字元則因 spec 明寫「最少 1、上限 ~12」而有依據。

**處置建議（待裁）**：
1. 接受 —— BVA 之界前基準線視為方法之一部分，不要求逐句有出處；或
2. 於此類 ER 加註來源為「BVA 方法」而非 spec，使覆核者一眼分得出。

**執行層傾向第 2 案** —— 成本是一個註記欄，收益是這類句子不再混在
「spec 說的」裡面。

---

## 4. 本表之盲區（R-G11）

1. **「改寫自」與「由該句推得」之界線由人判**，無可測形式。
   本表之分野為：語意可由該句**單獨**得出 → 改寫自；
   需再走一步推理（如「要能按 Yes，該 popup 須先顯示」）→ 由該句推得。
2. **本表只查 ER**。`pre_conditions`／`test_procedure`／`input_test_data`
   之出處**未逐句對照**（作業 B 只要求 ER）。
   pre-condition 之字面值有其自身之風險 ——
   例如 TC-013 之「非中國市場」曾是範圍過寬（16 輪 F-2 更正）。
3. **「無直接出處（步）」之 14 句未再細查**其是否與步驟真的對應 ——
   那是 G9（步驟數＝ER 數）與人工覆核之事，非本表之判準。
