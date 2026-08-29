# 下放包 44 —— 四項裁定、ROV-B 七列（`100` 拆二）

- 日期：2026-08-29
- 方向：分析層 → 執行層
- 前一包：`43_rov_a_v2.md`；對應上繳：`docs/upstream/39_rov_b.md`
- **條文凍結中：本包不新增、不修訂任何條文**（43 條／留存 26 不變）

---

## 一、四項裁定

### #1 T56b 之回測條件 —— **准，改記為「配對不變」**

執行層之判讀正確：**條件與其目的相衝突** ——
改語形抽取之目的就是讓舊表收不到之 `until` 子句被收到，
**凡有此類子句之列必然改變**；`029` 不是唯一一個，只是唯一一個被預期到的。

**真正該不變者是配對（檢查之判決），而配對確實 0 增 0 減；
改變者是「未比對」之揭露清單，其縮短正是本次修改之成效。**

**不回退。** 其後各次同型回測一律以「**配對不變**」為條件。

> 併記其實作上之正確處：`IX_END_ALIAS` **只收由裁定導出之等價，不收語形近似**，
> 且於原始碼註明其為裁定 —— 此為 R-SU34 v3(b) 之正確落地。

### #2 `$FOTA_Delay$` 之二種拼法 —— **裁為同一值之二種寫法**

依據（二側皆有，非單側筆誤）：
- **037 側**：`097` 用 `[Not_Prohibited]`、`101` 用 `[Not Prohibited]`，**指涉同一條件**
- **CFTS 側**：`4907880` 用 `[Not_Prohibited]`、`4907884` 用 `[Not Prohibited]`，
  **二者為同一情境之相鄰二條**

**故其值域為二值**（`Prohibited`／`Not Prohibited`），**非三值**。

**用法**：`test_item` 上半依該列原文逐字（不統一）；
**步驟與 ER 不引用該屬性值**（其不可觀測，見 #3），故本裁定不影響任何欄位之文字。
`REASONING.md` 記其為同義。

### #3 ROV-B 之屬性值 —— **一律不以屬性值為 ER 之判定對象**

三個屬性（`$FOTA_Status$`／`$FOTA_Delay$`／`$FOTA_Install$`）皆為
CarPropertyManager 之車輛屬性，**台架不可觀測**（同 `028` 之成因）。

**裁定**：其於 `test_item` 上半**保留**（037 逐字，R-S4）；
**於 procedure 與 ER 一律改以其外部表徵**（彈窗、畫面、安裝是否開始）。

**B-10 之對照表不必先建全表** —— ROV-B 六列所需之對照逐列可查，
其表徵皆為彈窗名或畫面，**已見於 037 與 CFTS 之原文**，不需另建。

### #4 `100` 之 Timeout／Cancel —— **准，拆二**

依 IN §8.2.2：逾時正常而取消不正常時，單一 TC 之判決不可辨。
拆為 `newR1L-SU-034`（逾時）／`newR1L-SU-035`（取消），同 trace `SWE1-FOTA-100`。

---

## 二、ROV-B 七列

**共通**：`input_test_data` 全為 `NA`；六列皆非 105 列；
Layer 3 provisional 為 `9.1 Pre-Installation`（GT 未涵蓋）。

**共通 pre_conditions 第 1–2 行**：
```
1. The head unit is connected to a Wi-Fi network with internet access
2. The vehicle is in Body ON mode
```

---

### TC-32 `newR1L-SU-032` ← `SWE1-FOTA-097`

**test_item**
```
If FOTA_Status indicates Waiting for HMI Acceptance ($FOTA_Status$ = [Waiting for HMI Acceptance]) and FOTA_Delay indicates Not_Prohibited($FOTA_Delay$ = [Not_Prohibited]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall show “ROV Forced Update Available A” pop-up.
(Forced Update Available A pop-up shown when deferral is permitted)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. The vehicle is in Body ON mode
3. An ROV forced update campaign whose deferral policy permits deferral is staged for this vehicle
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger the ROV update availability notification to the head unit
2. Check that the head unit displays the "ROV Forced Update Available A" pop-up
```
**expected_result**
```
1. The ROV update availability notification is delivered to the head unit
2. The head unit displays the "ROV Forced Update Available A" pop-up
```
**specification_reference**
```
CFTS057-4907880
```
**design_method**：`決策表 (Decision Table Testing)`｜**priority**：`P1`

---

### TC-33 `newR1L-SU-033` ← `SWE1-FOTA-099`

**test_item**
```
The ROV FOTA HMI shall capture the user selection from the “ROV Forced Update Available B” pop-up. If the user selects Update Now, the ROV FOTA HMI shall notify the ROV Update Service.
(Installation starts when the user selects Update Now)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. The vehicle is in Body ON mode
3. An ROV forced update campaign is staged for this vehicle and the "ROV Forced Update Available B" pop-up is displayed on the head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Select "Update Now" on the "ROV Forced Update Available B" pop-up
2. Record the head unit screen content as continuous video capture until the installation ends
3. Check that the head unit starts the installation after "Update Now" is selected
```
**expected_result**
```
1. The "ROV Forced Update Available B" pop-up closes
2. The head unit screen content until the installation ends is recorded as continuous video capture
3. The recorded screen content shows the installation starting after "Update Now" is selected
```
**specification_reference**
```
CFTS057-4907882
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

> **`REASONING.md` 須記**：安裝進度畫面於本 TC **僅作為「安裝已開始」之
> 可觀測表徵，本 TC 不驗該畫面** —— 其驗證屬 `SWE1-FOTA-092`（IN §8.2.1）。
> 取此表徵而不取 `$FOTA_Install$ = [Accepted]` 之依據：後者為 CarPropertyManager
> 屬性，台架不可觀測（R-SU25(b)）。

---

### TC-34 `newR1L-SU-034` ← `SWE1-FOTA-100`（逾時）

**test_item**
```
The ROV FOTA HMI shall start a response timer upon displaying the "ROV Forced Update Available B" pop-up. If no user selection is received within the configured timeout, the ROV FOTA HMI shall notify the ROV Update Service.
(Installation withheld after the pop-up closes on timeout)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. The vehicle is in Body ON mode
3. An ROV forced update campaign is staged for this vehicle and the "ROV Forced Update Available B" pop-up is displayed on the head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Record the head unit screen content as continuous video capture from the moment the pop-up is displayed
2. Leave the "ROV Forced Update Available B" pop-up without selecting any option until it closes
3. Check that the head unit does not start the installation after the pop-up has closed without any user selection
```
**expected_result**
```
1. The head unit screen content from the moment the pop-up is displayed is recorded as continuous video capture
2. The "ROV Forced Update Available B" pop-up closes without any user selection
3. The recorded screen content shows no installation starting after the pop-up has closed without any user selection
```
**specification_reference**
```
CFTS057-4907883
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

> **不寫逾時之秒數** —— 037 稱 `the configured timeout` 而未給值，
> 寫任何秒數即造值（§8.4.1）。其可觀測之界為「彈窗關閉」。

---

### TC-35 `newR1L-SU-035` ← `SWE1-FOTA-100`（取消）

**test_item**
```
The ROV FOTA HMI shall start a response timer upon displaying the "ROV Forced Update Available B" pop-up. If the user cancels the pop-up, the ROV FOTA HMI shall notify the ROV Update Service.
(Installation withheld after the user cancels the pop-up)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. The vehicle is in Body ON mode
3. An ROV forced update campaign is staged for this vehicle and the "ROV Forced Update Available B" pop-up is displayed on the head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Record the head unit screen content as continuous video capture from the moment the pop-up is displayed
2. Cancel the "ROV Forced Update Available B" pop-up
3. Check that the head unit does not start the installation after the user has cancelled the pop-up
```
**expected_result**
```
1. The head unit screen content from the moment the pop-up is displayed is recorded as continuous video capture
2. The "ROV Forced Update Available B" pop-up closes after being cancelled by the user
3. The recorded screen content shows no installation starting after the user has cancelled the pop-up
```
**specification_reference**
```
CFTS057-4907883
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

> **TC-34 vs TC-35 之區分**（R-SU41(b)）：其 Final Step 之判定對象分別為
> `after the pop-up has closed **without any user selection**` 與
> `after the user **has cancelled** the pop-up` —— **觸發側之狀態已在判定對象內**，
> 遮住其餘內容仍可看出驗的是不同的事。

---

### TC-36 `newR1L-SU-036` ← `SWE1-FOTA-101`

**test_item**
```
The ROV FOTA HMI shall allow the user to cancel or ignore the "ROV Forced Update Available A" popup only when FOTA_Status is equal to Waiting for HMI Acceptance and FOTA_Delay is equal to Not_Prohibited.($FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited])
(Cancel available on the pop-up when deferral is permitted)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. The vehicle is in Body ON mode
3. An ROV forced update campaign whose deferral policy permits deferral is staged for this vehicle and the "ROV Forced Update Available A" pop-up is displayed on the head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Cancel the "ROV Forced Update Available A" pop-up
2. Check that the pop-up closes and the head unit returns to the screen shown before the pop-up
```
**expected_result**
```
1. The "ROV Forced Update Available A" pop-up offers a cancel control and closes when it is cancelled
2. The head unit returns to the screen shown before the pop-up
```
**specification_reference**
```
CFTS057-4907884
```
**design_method**：`決策表 (Decision Table Testing)`｜**priority**：`P1`

> **範圍紀律**：本列之末句「若任一條件不滿足則不允許取消或忽略」——
> 其 `FOTA_Delay = Prohibited` 之分支為 **`SWE1-FOTA-102`** 所轄（TC-37）、
> 其 `FOTA_Status ≠ Waiting` 之分支為 **`SWE1-FOTA-109`** 所轄，
> **本 TC 不涵蓋**（IN §8.2.1）。

---

### TC-37 `newR1L-SU-037` ← `SWE1-FOTA-102`

**test_item**
```
The ROV FOTA HMI shall not allow the user to skip, ignore, or dismiss the forced update. The ROV FOTA HMI shall enforce the lockout behavior until the user schedules the update.
(No skip, ignore or dismiss offered when deferral is prohibited)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. The vehicle is in Body ON mode
3. An ROV forced update campaign whose deferral policy prohibits deferral is staged for this vehicle and the forced update pop-up is displayed on the head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Attempt to close the forced update pop-up without selecting the schedule option
2. Check that the pop-up remains displayed and offers no skip control, no ignore control and no dismiss control
```
**expected_result**
```
1. The forced update pop-up does not close
2. The pop-up remains displayed and offers no skip control, no ignore control and no dismiss control
```
**specification_reference**
```
CFTS057-4907885
```
**design_method**：`決策表 (Decision Table Testing)`｜**priority**：`P1`

> **錨定依據**：路徑 A 之首選為 `4907884`（分 0.566）——
> 其述**允許**取消或忽略之條件，**與本列之規定相反**。
> 正解為候選 **#4 `4907885`**（`FOTA_Delay = [Prohibited]` 時強制排程並鎖定使用者）。
> **本列為 R-SU14 v5「不取首選為錨」之又一實例**，與 `177` 同型。

---

### TC-38 `newR1L-SU-038` ← `SWE1-FOTA-103`

**test_item**
```
The ROV FOTA HMI shall capture user selection for "Schedule Update" from the "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up. Upon receiving the user selection, then ROV Update Service shall transition the flow to the Schedule Update HMI.
(Schedule Update screen opened from the forced update pop-up)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. The vehicle is in Body ON mode
3. An ROV forced update campaign is staged for this vehicle and the "ROV Forced Update Available A" pop-up is displayed on the head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Select "Schedule Update" on the "ROV Forced Update Available A" pop-up
2. Check that the head unit displays the Schedule Update screen
```
**expected_result**
```
1. The "ROV Forced Update Available A" pop-up closes
2. The head unit displays the Schedule Update screen
```
**specification_reference**
```
CFTS057-4907886
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

---

## 三、本批之預期

| 項 | 值 |
|---|---|
| TC 數 | **7**（`032`–`038`） |
| 涵蓋 037 列 | **6**（`097`／`099`／`100`／`101`／`102`／`103`） |
| `PENDING` | **0** |
| 預期 lint | **20 項全 0 ＋ U=0 ＋ `I-cross` 實報** |
| 可交付 | **7 列** |

**全案可交付候選：14 ＋ 7 = 21 列。**

---

## 四、任務（T57）

| # | 任務 |
|---|---|
| T57a | **ROV-B 產出與 lint**：`sandbox/rov_b/` 產出 `newR1L-SU-032`–`038`。**預期 20 項全 0 ＋ U=0**，`I-cross` 實報 |
| T57b | **`test_item` 上半之逐字核對**：七份上半逐字比對 037 全文（含 `Not_Prohibited`／`Not Prohibited` 之各自原文、`( $FOTA_Status$ = …)` 之不規則空格） |
| T57c | **遮蔽測試**：`034` vs `035`、`036` vs `037` 二對須通過（其為本批最相近者）；併跑全 38 個 TC 之遮蔽測試，列出新增之相同配對 |
| T57d | **`REASONING.md` 補記**：`033` 之二事（§二 TC-33）、`036` 之範圍委派、`037` 之不取首選為錨、`$FOTA_Delay$` 二拼法為同義（§一 #2） |
| T57e | **ROV-C 五列之材料索引**（`089`／`098`／`107`／`108`／`109`）：`25a` 行號區間 ＋ 其 Description 中之全部 `$…$` 屬性名與值 |
| T57f | **git** |

**不在本輪**：ROV-C／D／E、`Interruption Handling` 其餘 12 列、寫回。

---

## 五、上繳包要求（`docs/upstream/39_rov_b.md`）

1. T57a 之 lint 全輸出 —— **本輪核心**
2. T57b 之逐字核對結果
3. T57c 之遮蔽測試（**全 38 個 TC**）
4. T57d／T57e／T57f 之結果
5. 未結 DR 清單（5 筆）
6. 獨立自評（入 BACKLOG）—— 特別回答：**`032`／`036`／`037` 三列之
   pre_conditions 皆以「deferral policy permits／prohibits deferral」描述其前提，
   而該政策實為 `$FOTA_Delay$` 之值 —— 台架上測試者如何確認該政策已生效？
   若無從確認，則三列之 pre_conditions 是一個不可驗之前提**
