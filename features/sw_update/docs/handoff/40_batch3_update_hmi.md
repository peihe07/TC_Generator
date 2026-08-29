# 下放包 40 —— 條文凍結生效、`Update HMI` 6 列之 TC（10 個）

- 日期：2026-08-29
- 方向：分析層 → 執行層
- 前一包：`39_batch1_audit.md`
- 對應上繳：`docs/upstream/34_batch1_audit.md`（T52 未執行者併入本輪，見 §五）
- 裁定狀態：**Pei 2026-08-29 准條文凍結**；本包**不新增、不修訂任何條文**

---

## 一、條文凍結（Pei 裁，2026-08-29）

自本包起生效，比照 `display` 之 R-DM57：

1. **不新增條文、不修訂條文** —— 除非發現 **TC 內容錯誤**（不是方法瑕疵）
2. 執行層之方法自評照舊寫，**一律進 `BACKLOG.md`，不即刻立條**
3. **執行層對符合下列**全部**條件者逕行並回報，不待裁**：
   - 不改變驗證單元
   - 不改變錨
   - 不增刪 `PENDING`
   - 理由可自既有條文直接導出
4. **分析層之改寫指令一律給整列全文**，不再給逐句差分
   （成因：下放包 39 §3.1 之逐句差分丟掉 `recorded screen content`）

**現行條文 43 條、留存 26 條，凍結於此。**

---

## 二、上繳包 33 之二項逕行 —— 追認

| 項 | 裁 |
|---|---|
| `002` ER 末行改採最小改法（保留 `The recorded screen content contains no …`） | **准，逕行**。其三層後果（斷開 R-SU36、失去觀測窗、掉出 `I-cross`）之診斷正確 |
| DR-SU1 之 `Leaves served` 與 `Batch impact` 更新為三列 | **准，逕行**。一筆實際擋三列之 DR 於台帳顯示只擋一列，會直接誤導優先序判讀 |

---

## 三、`Update HMI` 6 列 → 10 個 TC

**共通**：`input_test_data` 全為 `NA`；六列皆非 105 列、非 126 內部列；
Layer 3 provisional 為 `4.11 User Experience (UX)/HMI`（GT 未涵蓋，得於本批就地修正）。

**共通 pre_conditions 第 1 行**（除另載者）：
```
1. The head unit is connected to a Wi-Fi network with internet access
```

---

### TC-18 `newR1L-SU-018` ← `SWE1-FOTA-130`（English）

**test_item**
```
The MCPU platform software shall provide localization support for the three languages required for the NAFTA region. The supported languages shall include English, North American French, and North American Spanish.
(Update text shown in English when English is the configured language)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package is staged on the OTA Server for this head unit
3. The head unit language setting is set to English
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Open the SW Update screen on the head unit
3. Check that the update-related text and messages on the SW Update screen are shown in English
```
**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The SW Update screen is displayed on the head unit
3. The update-related text and messages on the SW Update screen are shown in English
```
**specification_reference**
```
CFTS057-4907653
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P2`

---

### TC-19 `newR1L-SU-019` ← `SWE1-FOTA-130`（North American French）

**test_item**
```
The MCPU platform software shall provide localization support for the three languages required for the NAFTA region. The supported languages shall include English, North American French, and North American Spanish.
(Update text shown in North American French when that language is configured)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package is staged on the OTA Server for this head unit
3. The head unit language setting is set to North American French
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Open the SW Update screen on the head unit
3. Check that the update-related text and messages on the SW Update screen are shown in North American French
```
**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The SW Update screen is displayed on the head unit
3. The update-related text and messages on the SW Update screen are shown in North American French
```
**specification_reference**
```
CFTS057-4907653
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P2`

---

### TC-20 `newR1L-SU-020` ← `SWE1-FOTA-130`（North American Spanish）

**test_item**
```
The MCPU platform software shall provide localization support for the three languages required for the NAFTA region. The supported languages shall include English, North American French, and North American Spanish.
(Update text shown in North American Spanish when that language is configured)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package is staged on the OTA Server for this head unit
3. The head unit language setting is set to North American Spanish
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Open the SW Update screen on the head unit
3. Check that the update-related text and messages on the SW Update screen are shown in North American Spanish
```
**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The SW Update screen is displayed on the head unit
3. The update-related text and messages on the SW Update screen are shown in North American Spanish
```
**specification_reference**
```
CFTS057-4907653
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P2`

> **拆三之依據**（IN §8.3 資料軸；§8.2.2 RD sub-id ≠ TC 數）：
> 三語言為三個獨立之部分失效 —— 法語正常而西語不正常時，
> 單一 TC 之判決不可辨。三 TC 同 trace `SWE1-FOTA-130`。
> **本列為肯定式全稱（各語言皆須支援），依 R-SU33(d) 需逐 X 確認，
> 不適用觀測窗法。**

---

### TC-21 `newR1L-SU-021` ← `SWE1-FOTA-131`

**test_item**
```
The WiFi Update Service shall retrieve update type configuration from the OTA server for each update campaign using SWMC. The WiFi Update Service shall control the applicable update flow according to the server-defined update type configuration.
(Update flow follows the update type configured on the server)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update campaign configured on the OTA Server with update type Regular is available for this head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Record the SW Update screens shown on the head unit as continuous video capture until the update finishes
3. Reconfigure the update campaign on the OTA Server to update type Silent and restore the head unit to its pre-update software version
4. Trigger an update availability check to the OTA Server
5. Check that the recorded screen content of the first run contains the opt-in screen and that no opt-in screen is shown in the second run
```
**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The SW Update screens shown until the update finishes are recorded as continuous video capture
3. The update campaign on the OTA Server is set to update type Silent and the head unit software version is back at its pre-update value
4. The update availability check completes and an update is reported as available
5. The recorded screen content of the first run contains the opt-in screen; the second run shows no opt-in screen
```
**specification_reference**
```
CFTS057-4907453
CFTS057-4907656
```
**design_method**：`狀態轉換 (State Transition Testing)`｜**priority**：`P1`

> **驗證單元**：本列所有者為「**伺服器所設之類型決定所適用之流程**」，
> 非各類型自身之行為（後者屬 `Silent Update` 與 `Update Policy` 二組，
> IN §8.2.1 不擴入）。故其判定為**二次執行之流程相異**，而非任一流程之細節。

---

### TC-22 `newR1L-SU-022` ← `SWE1-FOTA-132`

**test_item**
```
Before initiating the update download, the SWMC shall check the customer acceptance status from the FCA IT customer preference database. The SWMC shall block update download initiation until terms and conditions acceptance is confirmed.
(Download blocked and guidance shown when terms and conditions are not accepted)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package whose Download Descriptor requires terms and conditions acceptance is staged on the OTA Server for this head unit
3. The customer preference record for this vehicle shows the terms and conditions as not accepted
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Read the software version shown on the head unit and record it as Version_after
4. Check that the SW Update screen shows guidance on how to accept the terms and conditions and that Version_after equals Version_initial
```
**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. Version_after is recorded
4. The SW Update screen shows guidance on how to accept the terms and conditions; Version_after equals Version_initial
```
**specification_reference**
```
CFTS057-4907657
```
**design_method**：`負向測試 (Negative / Invalid)`｜**priority**：`P1`

---

### TC-23 `newR1L-SU-023` ← `SWE1-FOTA-133`（顯示）

**test_item**
```
The SW Update HMI shall display the release notes information, update-related information, and associated links during the opt-in and download screens.
(Release notes and links shown on the opt-in and download screens)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package whose Download Descriptor contains release notes and at least one link is staged on the OTA Server for this head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Open the opt-in screen on the head unit
3. Open the download screen on the head unit
4. Check that both the opt-in screen and the download screen show the release notes text and the link contained in the Download Descriptor
```
**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The opt-in screen is displayed on the head unit
3. The download screen is displayed on the head unit
4. The opt-in screen and the download screen both show the release notes text and the link contained in the Download Descriptor
```
**specification_reference**
```
CFTS057-4907660
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P2`

---

### TC-24 `newR1L-SU-024` ← `SWE1-FOTA-133`（互動）

**test_item**
```
The SW Update HMI shall support user interaction with embedded links displayed as part of the update information.
(Embedded link responds when selected by the user)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package whose Download Descriptor contains release notes and at least one link is staged on the OTA Server for this head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Open the opt-in screen on the head unit
3. Select the link shown in the update information
4. Check that the head unit opens the content referenced by the selected link
```
**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The opt-in screen is displayed on the head unit
3. The link shown in the update information is selected
4. The head unit opens the content referenced by the selected link
```
**specification_reference**
```
CFTS057-4907660
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P2`

> **拆二之依據**（IN §8.2.2）：「顯示」與「可互動」為二個獨立之部分失效 ——
> 連結顯示而不可點選時，單一 TC 之判決不可辨。二 TC 同 trace `SWE1-FOTA-133`。

---

### TC-25 `newR1L-SU-025` ← `SWE1-FOTA-134`

**test_item**
```
After completion of the download, the SW Update HMI shall display the deployment package details to the user. The SW Update HMI shall provide opt-in options including "Install" and "Schedule Later".
(Install and Schedule Later offered after download completes)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package configured as a non-silent update is staged on the OTA Server for this head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Accept the update on the opt-in screen and wait until the download completes
3. Check that the head unit shows the deployment package details together with an "Install" option and a "Schedule Later" option
```
**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The download completes and the post-download screen is displayed on the head unit
3. The post-download screen shows the deployment package details, an "Install" option and a "Schedule Later" option
```
**specification_reference**
```
CFTS057-4907662
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

> **情態差異之記明**（比照 `180` 之處置）：CFTS `4907662` 用 `SHOULD provide`，
> 037 `SWE1-FOTA-134` 用 `shall provide`。**SWE.6 以 037 為需求本文**，
> TC 依 037 之強度撰寫；差異記於 reasoning，**不改二者、不發 DR**。

---

### TC-26 `newR1L-SU-026` ← `SWE1-FOTA-136`（允許拒絕）

**test_item**
```
The SWMC shall determine whether end-user rejection of the OTA deployment is permitted based on the received Critical Update and Silent Install flag. The SW Update HMI shall allow or restrict user rejection options according to the deployment interaction policy received from the SWMC via WiFi Update Service.
(Rejection option offered when the flags permit rejection)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update campaign with the Critical Update flag not set and the Silent Install flag not set is staged on the OTA Server for this head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Open the SW Update opt-in screen on the head unit
3. Check that the opt-in screen offers the user an option to reject the deployment
```
**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The SW Update opt-in screen is displayed on the head unit
3. The opt-in screen offers the user an option to reject the deployment
```
**specification_reference**
```
CFTS057-4907600
```
**design_method**：`決策表 (Decision Table Testing)`｜**priority**：`P1`

---

### TC-27 `newR1L-SU-027` ← `SWE1-FOTA-136`（限制拒絕）

**test_item**
```
The SWMC shall determine whether end-user rejection of the OTA deployment is permitted based on the received Critical Update and Silent Install flag. The SW Update HMI shall allow or restrict user rejection options according to the deployment interaction policy received from the SWMC via WiFi Update Service.
(Rejection option withheld when the Critical Update flag is set)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update campaign with the Critical Update flag set is staged on the OTA Server for this head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Open the SW Update opt-in screen on the head unit
3. Check that the opt-in screen offers the user no option to reject the deployment
```
**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The SW Update opt-in screen is displayed on the head unit
3. The opt-in screen offers the user no option to reject the deployment
```
**specification_reference**
```
CFTS057-4907600
```
**design_method**：`決策表 (Decision Table Testing)`｜**priority**：`P1`

> **配對之依據**（IN §7）：枚舉之支援情形須配至少一個未支援之負向 TC。
> 二 TC 同 trace `SWE1-FOTA-136`，其區分位於判定對象內（**offers … an option**
> vs **offers … no option**），滿足 R-SU41(b)。

---

## 四、本批之預期

| 項 | 值 |
|---|---|
| TC 數 | **10**（`018`–`027`） |
| 涵蓋 037 列 | **6**（`130`–`134`、`136`） |
| `PENDING` | **0** —— 本批無 105 列、無第三型、無第四型 |
| 預期 lint | **21 項全 0**（含 U=0） |

**本批為本 feature 首個預期全數可交付之批次。**

---

## 五、任務（T53，含 T52 未執行者）

| # | 任務 |
|---|---|
| T53a | **T52 之未執行項**：`001`／`002` 之改寫（下放包 39 §3.1，`002` 之 ER 末行採 §二之最小改法）、`003` 之 `reasoning`、DR-SU1 之情態問與三列影響範圍、DR-SU4 請求 1 之增註、暫態揭露改「R-SU41 全條」。lint 預期 pilot U=5 |
| T53b | **R-SU43 v2(b) 範圍重跑**（原 T52b）：擴大範圍後重跑 17 列回溯檢定，現行 6 列通過須逐列重驗 |
| T53c | **batch 3 產出與 lint**：`sandbox/batch03/` 產出 `newR1L-SU-018`–`027`。**預期 21 項全 0** |
| T53d | **`BACKLOG.md` 建檔**（凍結第 2 條）：本輪起之方法自評一律入此檔，格式為「觀察／出處／若解凍時之建議」 |
| T53e | **git** |

**不在本輪**：`ROV Installation` 20 列（材料已備於 `25a`）、`Interruption Handling` 其餘 12 列、寫回。

---

## 六、上繳包要求（`docs/upstream/35_batch3.md`）

1. T53c 之 lint 全輸出 —— **本輪核心**
2. T53a／T53b 之結果
3. `BACKLOG.md` 之首批條目
4. 未結 DR 清單（4 筆）
5. 獨立自評（**入 BACKLOG，不立條**）—— 特別回答：
   **TC-21 之 procedure 第 3 步要求「將 HU 還原至更新前之軟體版本」，
   該操作在台架上是否可行**；若不可行，本 TC 之二次執行設計即不成立
