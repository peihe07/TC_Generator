# 上繳包 17 —— pilot 材料、五列定案後之重跑、0 列群清單程式化

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/18_pilot_material.md`
  （SHA256 `9109ce304a09686582cd9ea0f6e00748cb64ccc03db67e20c6e630f4ade8bd1e`，135 行）
- 未結 DR：**0 筆**｜新登 anomaly：**0 筆**
- `scripts/layer2_close.py` 增 T31d；`scripts/islands.py` 增 T31b

## 本輪四個主結果

1. **三重閉合、孤島檢查、0 列群比對三項全過。** 孤島 **7 → 5**，
   **新產生 0 個**；`359` 改置使 `359` 與 `360` 之孤島身分**同時**解除。
2. **§六.6 之答案：切分更整，不更碎。** `Session Management` 之連續段數
   **4 → 3**、`Interruption Handling` **維持 3**；`309` 群內之總段數 **16 → 15**。
3. **下放包 §4.1 之 pilot 組成有一處誤**：稱「含 HMI 列 1（`177`）與 Service 列 8」，
   **實測 HMI 2（`177`、`183`）／Service 7**。此**強化**而非削弱其選定依據。
4. **`176` 之首選分與機制 3 之門檻是同一個浮點數**（`0.26716366259482566`）——
   因門檻取自母體之**實測百分位值**，故**恆有一列坐在界上**，
   其是否被攔取決於 `<` 與 `≤` 之別。**該列恰為 pilot 之 GT 列**。§5.2。

---

## 1. T31e —— T-抄 核對結果

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU21 v2 | 364 | **OK** | `9681ce41952e` |

逐字 append，**既有 34 個條文區塊未受影響** ✅（現 35 塊）。
索引表現行 **22 條**（R-SU21→**v2**）；留存不得引用者 **13 條**
（新增 `R-SU21`(v1)：「0 列 Heading 群為 8 群」之計數與其列舉）。
與下放包 18 §五 T31e 所定之數一致。

`PLAYBOOK.md` §7 追加二則：
- **(15)**「寫『關於零之條文』時，其列舉須以程式產生」——
  並指出其與 (13) 之分工：(13) 是**檢查式**對零無感，(15) 是**條文之列舉**對零無感，
  **同一個錯，載體不同**。
- **(16)**「空測通過與實測通過是兩件事」—— 並指出其比 (8) 更難察覺之處：
  (8) 是「跑了但沒抓到」，(16) 是**「根本沒跑到」**而輸出看起來完全正常。

---

## 2. T31b —— pilot 材料：`Silent Update`（9 列）

- Test Set：**`Silent Update`**｜Layer 3 provisional：**`4.7.3.2` Silent Updates**（GT 支持：`176`／`179`／`180`）
- 所轄：(`SWE1-FOTA-170`, 175–177) + (`SWE1-FOTA-178`, 全群 179–184) —— **跨 2 個 Heading 群**
- 機制 3 之門檻（R-SU14 v4(c)）：首選分 < **0.267**

### 概覽

| # | 037 列 | Heading 群 | Sub Cat | Priority | 首選分 | 機制 3 | GT | 標題 |
|---:|---|---|---|---|---:|:--:|:--:|---|
| 1 | `SWE1-FOTA-175` | `SWE1-FOTA-170` | Service | High | 0.278 | — | — | Execute Silent Update Without User Int |
| 2 | `SWE1-FOTA-176` | `SWE1-FOTA-170` | Service | High | 0.267 | — | **✅ GT-A1** | Restrict Silent Session Notifications  |
| 3 | `SWE1-FOTA-177` | `SWE1-FOTA-170` | HMI | High | 0.282 | — | — | Restrict Opt-Out and Deferral Options  |
| 4 | `SWE1-FOTA-179` | `SWE1-FOTA-178` | Service | High | 0.200 | **⚠ 攔下** | **✅ GT-A1** | Start Silent Update Download Automatic |
| 5 | `SWE1-FOTA-180` | `SWE1-FOTA-178` | Service | Low | 0.386 | — | **✅ GT-A1** | Optionally Suppress Download Confirmat |
| 6 | `SWE1-FOTA-181` | `SWE1-FOTA-178` | Service | High | 0.317 | — | — | Start Silent Update Installation Immed |
| 7 | `SWE1-FOTA-182` | `SWE1-FOTA-178` | Service | Low | 0.376 | — | — | Optionally Suppress Deployment Confirm |
| 8 | `SWE1-FOTA-183` | `SWE1-FOTA-178` | HMI | High | 0.410 | — | — | Display Silent Update Completion and W |
| 9 | `SWE1-FOTA-184` | `SWE1-FOTA-178` | Service | High | 0.311 | — | — | Apply Silent Update to All Session Flo |

- 落入機制 3（低分偵測器）者：**1** 列 —— `179`（其階段二應出前 20 候選）
- 有 GT-A1 人裁正解者：**3** 列 —— `176`→`4907476`,`4907477`、`179`→`4907481`、`180`→`4907482`
- 其正解為**列舉區塊成員**者：**0** 列（無）
- **自證錨**（R-SU13 v2 支柱 3）：本 9 列中**無**（自證錨之已知實例為 `313`，不在本組）

---

### 逐列材料

> **執行層不撰寫 TC、不裁定錨。** 本節為分析層起草 pilot TC 之材料。


---

#### 1. `SWE1-FOTA-175` — Execute Silent Update Without User Interaction

- Heading 群：`SWE1-FOTA-170` Deployment Package Security｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-360/SYS-RA-FOTA-361`
- 首選分 **0.278** —— ≥ 0.267，不落入機制 3

**Requirement Description 全文**：

> The WiFi Update Service shall validate update metadata received from SWMC and determine whether the update type is identified as Silent Update. When the update type is identified as Silent Update, the WiFi Update Service shall automatically execute the update in background mode. The WiFi Update Service shall not trigger the SW Update HMI for progress notifications, update prompts, or customer-facing interaction during Silent Update execution.

**路徑 A（語料 v2）前 5 候選**：

1. `4907475` — 章 **4.7.3.2** Silent Updates — 分 **0.278**
   > Silent updates run automatically without any progress notifications or end user interaction.

2. `4907453` — 章 **4.7.3** Main Update Configuration Options — 分 **0.265**
   > Update type:

3. `4907476` — 章 **4.7.3.2** Silent Updates — 分 **0.244**
   > Silent updates shall not display progress notifications and shall NOT require end-user interaction.

4. `4907487` — 章 **4.7.3.2** Silent Updates — 分 **0.226**
   > If the DDF does not include whether the update is silent or not, the HU shall treat the update as a non-silent update

5. `4907618` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.208**
   > Download of the file shall not be customer facing.


---

#### 2. `SWE1-FOTA-176` — Restrict Silent Session Notifications to Safety-Required Cases

- Heading 群：`SWE1-FOTA-170` Deployment Package Security｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-362`
- **GT-A1 已裁正解**：`4907476`、`4907477`（章 4.7.3.2）
- 首選分 **0.267** —— ≥ 0.267，不落入機制 3

**Requirement Description 全文**：

> During a Silent Update session, the WiFi Update Service shall not trigger the SW Update HMI for update progress notifications. During a Silent Update session, the WiFi Update Service shall allow user notification only when required to satisfy safety-related requirements.

**路徑 A（語料 v2）前 5 候選**：

1. `4907476` — 章 **4.7.3.2** Silent Updates — 分 **0.267** ← **GT 正解**
   > Silent updates shall not display progress notifications and shall NOT require end-user interaction.

2. `4907486` — 章 **4.7.3.2** Silent Updates — 分 **0.258**
   > Silent update shall be applicable for all session flows.

3. `4907455` — 章 **4.7.3** Main Update Configuration Options — 分 **0.248**
   > Silent update: An update that does not display any notifications during the session (there is no end-user interaction)—the end-user cannot reject the update. Network bearer rules for minimizing download cost apply.

4. `4907477` — 章 **4.7.3.2** Silent Updates — 分 **0.247** ← **GT 正解**
   > During silent sessions the user SHALL NOT be notified unless necessary for safety requirements.

5. `4907475` — 章 **4.7.3.2** Silent Updates — 分 **0.244**
   > Silent updates run automatically without any progress notifications or end user interaction.


---

#### 3. `SWE1-FOTA-177` — Restrict Opt-Out and Deferral Options in HMI

- Heading 群：`SWE1-FOTA-170` Deployment Package Security｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-363`
- 首選分 **0.282** —— ≥ 0.267，不落入機制 3

**Requirement Description 全文**：

> If the SW Update HMI is available, the assigned update service shall not present the user with options to opt out of or defer the update.

**路徑 A（語料 v2）前 5 候選**：

1. `4907662` — 章 **4.11** User Experience (UX)/HMI — 分 **0.282**
   > After the download is complete, the user is shown the deployment package details, the HMI SHOULD provide the user with opt in options: Install or schedule later.Kindly see the latest HMI for pop up.

2. `4907478` — 章 **4.7.3.2** Silent Updates — 分 **0.261**
   > If an HMI is available, the user SHALL NOT be presented with a choice of opting out or deferring the update.

3. `4907776` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.255**
   > These requirements are valid if $TBM_present$ = [present]

4. `4907278` — 章 **4.2.3** HU FOTA with TBM — 分 **0.255**
   > These requirements are valid if $TBM_present$ = [present]

5. `4907589` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.206**
   > 7. After deployment package is downloaded and validated (FCA signature check), the client shall prompt the HMI for user acceptance. The user MAY be allowed to defer the update a number of pre-defined times.


---

#### 4. `SWE1-FOTA-179` — Start Silent Update Download Automatically

- Heading 群：`SWE1-FOTA-178` For a silent update, the OTA client follows these steps for the download｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-366`
- **GT-A1 已裁正解**：`4907481`（章 4.7.3.2）
- 首選分 **0.200** —— **< 0.267，落入機制 3**，階段二應出前 20 候選

**Requirement Description 全文**：

> The SWMC shall provide the downloaded Download Descriptor (DD) metadata to the WiFi Update Service after update availability is confirmed. The WiFi Update Service shall analyze the DD metadata to determine whether the update type is classified as Silent Update. If the DD metadata indicates a Silent Update, the WiFi Update Service shall automatically request SWMC to initiate deployment package download.

**路徑 A（語料 v2）前 5 候選**：

1. `4907481` — 章 **4.7.3.2** Silent Updates — 分 **0.200** ← **GT 正解**
   > 1. The download of the deployment package shall start automatically.

2. `4907487` — 章 **4.7.3.2** Silent Updates — 分 **0.200**
   > If the DDF does not include whether the update is silent or not, the HU shall treat the update as a non-silent update

3. `4907806` — 章 **6** TBM Algorithm Requirements — 分 **0.199**
   > When TBM has completed the download of TBM FOTA Silent update package, then the TBM shall send $TBMUpdate$ = [Silent_Update]

4. `4907453` — 章 **4.7.3** Main Update Configuration Options — 分 **0.187**
   > Update type:

5. `4907656` — 章 **4.11** User Experience (UX)/HMI — 分 **0.176**
   > User experience shall be same for all update types and updates (regular/critical/silent) SHOULD be configurable from the server so that the FOTA service administrator can select the relevant option depending on the type and urgency of the update being performed.


---

#### 5. `SWE1-FOTA-180` — Optionally Suppress Download Confirmation Screen

- Heading 群：`SWE1-FOTA-178` For a silent update, the OTA client follows these steps for the download｜Sub Cat：Service｜Priority：Low｜Source：`SYS-RA-FOTA-367`
- **GT-A1 已裁正解**：`4907482`（章 4.7.3.2）
- 首選分 **0.386** —— ≥ 0.267，不落入機制 3

**Requirement Description 全文**：

> When the update type is identified as Silent Update, the WiFi Update Service shalll not trigger the SW Update HMI to display a download confirmation screen. The WiFi Update Service shall automatically request SWMC to initiate deployment package download without user interaction.

**路徑 A（語料 v2）前 5 候選**：

1. `4907470` — 章 **4.7.3.1** Critical Updates — 分 **0.386**
   > 1. The download of the deployment package shall start automatically; The OTA client SHALL NOT display a download confirmation screen.

2. `4907482` — 章 **4.7.3.2** Silent Updates — 分 **0.285** ← **GT 正解**
   > The OTA client MAY NOT display a download confirmation screen.

3. `4907475` — 章 **4.7.3.2** Silent Updates — 分 **0.277**
   > Silent updates run automatically without any progress notifications or end user interaction.

4. `4907484` — 章 **4.7.3.2** Silent Updates — 分 **0.272**
   > The OTA client MAY NOT display a deployment confirmation screen.

5. `4907481` — 章 **4.7.3.2** Silent Updates — 分 **0.261**
   > 1. The download of the deployment package shall start automatically.


---

#### 6. `SWE1-FOTA-181` — Start Silent Update Installation Immediately After Download

- Heading 群：`SWE1-FOTA-178` For a silent update, the OTA client follows these steps for the download｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-368`
- 首選分 **0.317** —— ≥ 0.267，不落入機制 3

**Requirement Description 全文**：

> The SWMC shall notify the WiFi Update Service upon successful completion of deployment package download for update packages classified as Silent Update. Upon receiving deployment package download completion status, the WiFi Update Service shall immediately start installation prechecks and deployment.

**路徑 A（語料 v2）前 5 候選**：

1. `4907483` — 章 **4.7.3.2** Silent Updates — 分 **0.317**
   > 2. After the deployment package is downloaded, its deployment shall start immediately.

2. `4907481` — 章 **4.7.3.2** Silent Updates — 分 **0.262**
   > 1. The download of the deployment package shall start automatically.

3. `4907470` — 章 **4.7.3.1** Critical Updates — 分 **0.201**
   > 1. The download of the deployment package shall start automatically; The OTA client SHALL NOT display a download confirmation screen.

4. `4907515` — 章 **4.8.3** Deployment Package Security — 分 **0.195**
   > The OTA client shall ensure integrity of the deployment package before it is installed, immediately pre installation.

5. `4907514` — 章 **4.8.3** Deployment Package Security — 分 **0.192**
   > The OTA client shall verify integrity of the deployment package once it is received from the server, immediately post download.


---

#### 7. `SWE1-FOTA-182` — Optionally Suppress Deployment Confirmation Screen

- Heading 群：`SWE1-FOTA-178` For a silent update, the OTA client follows these steps for the download｜Sub Cat：Service｜Priority：Low｜Source：`SYS-RA-FOTA-369`
- 首選分 **0.376** —— ≥ 0.267，不落入機制 3

**Requirement Description 全文**：

> The WiFi Update Service shall not trigger the SW Update HMI to display a deployment confirmation screen when the update type is identified as Silent Update. The WiFi Update Service shall automatically initiate deployment of the downloaded package without user interaction.

**路徑 A（語料 v2）前 5 候選**：

1. `4907470` — 章 **4.7.3.1** Critical Updates — 分 **0.376**
   > 1. The download of the deployment package shall start automatically; The OTA client SHALL NOT display a download confirmation screen.

2. `4907471` — 章 **4.7.3.1** Critical Updates — 分 **0.351**
   > 2. When the deployment package is downloaded, the OTA client shall display a deployment confirmation screen. The deployment shall start after a confirmation screen or when a timeout occurs.

3. `4907484` — 章 **4.7.3.2** Silent Updates — 分 **0.322**
   > The OTA client MAY NOT display a deployment confirmation screen.

4. `4907475` — 章 **4.7.3.2** Silent Updates — 分 **0.300**
   > Silent updates run automatically without any progress notifications or end user interaction.

5. `4907482` — 章 **4.7.3.2** Silent Updates — 分 **0.260**
   > The OTA client MAY NOT display a download confirmation screen.


---

#### 8. `SWE1-FOTA-183` — Display Silent Update Completion and What's New Details

- Heading 群：`SWE1-FOTA-178` For a silent update, the OTA client follows these steps for the download｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-370`
- 首選分 **0.410** —— ≥ 0.267，不落入機制 3

**Requirement Description 全文**：

> The Update Engine and SW Updater Manager shall notify the WiFi Update Service/USB Update Service upon successful completion of deploymentof Silent Update. Upon receiving deployment success status, the WiFi Update Service/USB Update Service shall retrieve the “What’s New” details associated with the deployed package metadata. The WiFi Update Service/USB Update Service shall notify the SW Update HMI to display the update success notification together with the “What’s New” details for the completed update.

**路徑 A（語料 v2）前 5 候選**：

1. `4907485` — 章 **4.7.3.2** Silent Updates — 分 **0.410**
   > 3. When the update completes, the OTA client will display a success notification and what's new details.

2. `4907909` — 章 **9.3** Post-Installation — 分 **0.284**
   > The HU shall cache $FOTA_Status$ = [Successful FOTA Update] and What's new details to display until next Body ON mode.

3. `4907634` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.268**
   > If the user selects 'What's New' option, the HU shall display the pop-up (PU0410) with what's new details based on information received from the downloaded deployment package details.Please refer to latest Software Updates FOTA HMI L&amp;F.

4. `4907908` — 章 **9.3** Post-Installation — 分 **0.231**
   > When the user selects 'What's New' option, the HU shall display the pop-up, PU0410 with What's new details based on information received from SGW_FOTA_HMI_ETM.4215Please refer to HMI

5. `4907889` — 章 **9.1** Pre-Installation — 分 **0.205**
   > If the user selects 'What's New' option on "ROV Forced Update Available A" or "ROV Forced Update Availbale B" pop-up, the HU shall display the pop-up (PU0410) with what's new details based on the information received from SGW_FOTA_HMI_ETM.4215.Please refer to the latest Software Updates FOTA HMI L&amp;F.


---

#### 9. `SWE1-FOTA-184` — Apply Silent Update to All Session Flows

- Heading 群：`SWE1-FOTA-178` For a silent update, the OTA client follows these steps for the download｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-371`
- 首選分 **0.311** —— ≥ 0.267，不落入機制 3

**Requirement Description 全文**：

> The WiFi Update Service shall apply Silent Update execution rules to all supported update session flows, including update check, deployment package download and installation processing. During Silent Update execution, the WiFi Update Service shall not trigger the SW Update HMI for customer-facing interaction, progress notifications, prompts, or confirmation flows unless required for safety-related conditions.

**路徑 A（語料 v2）前 5 候選**：

1. `4907486` — 章 **4.7.3.2** Silent Updates — 分 **0.311**
   > Silent update shall be applicable for all session flows.

2. `4907455` — 章 **4.7.3** Main Update Configuration Options — 分 **0.281**
   > Silent update: An update that does not display any notifications during the session (there is no end-user interaction)—the end-user cannot reject the update. Network bearer rules for minimizing download cost apply.

3. `4907476` — 章 **4.7.3.2** Silent Updates — 分 **0.245**
   > Silent updates shall not display progress notifications and shall NOT require end-user interaction.

4. `4907618` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.244**
   > Download of the file shall not be customer facing.

5. `4907477` — 章 **4.7.3.2** Silent Updates — 分 **0.234**
   > During silent sessions the user SHALL NOT be notified unless necessary for safety requirements.


---

## 3. T31a —— 三重閉合與孤島列之重跑（§2.1 更動後）

> 依 R-SU10 v2：(i) 列數、(ii) 群數、(iii) 列 id 集合，**三者缺一不可**。

### (i) 列數閉合

| # | Test Set | 所轄 (Heading id, 列區間) | 列數 | 下放包 16 §4.1 | |
|---:|---|---|---:|---:|:--:|
| 1 | `Wi-Fi Download` | 038、055、058 | **29** | 29 | ✅ |
| 2 | `Update Policy` | 009、024 | **17** | 17 | ✅ |
| 3 | `Silent Update` | 178、`175`–`177` | **9** | 9 | ✅ |
| 4 | `Deployment Flow` | 137 | **26** | 26 | ✅ |
| 5 | `Session Flows` | 016、017、018、168、185、188、271、278、287 | **16** | 16 | ✅ |
| 6 | `Client Architecture` | 072、073、192、200、202、251、259、263、266、280、285 | **35** | 35 | ✅ |
| 7 | `Bearer Selection` | 291 | **16** | 16 | ✅ |
| 8 | `ROV Installation` | 085、086、091、096 | **20** | 20 | ✅ |
| 9 | `TBM Reflash` | 110 | **14** | 14 | ✅ |
| 10 | `HU FOTA via TBM` | 214 | **36** | 36 | ✅ |
| 11 | `USB Update` | 020、074、076、078 | **5** | 5 | ✅ |
| 12 | `Update HMI` | 129 | **6** | 6 | ✅ |
| 13 | `Configurable Parameters` | 125、127 | **2** | 2 | ✅ |
| 14 | `FOTA Overview` | 001 | **6** | 6 | ✅ |
| 15 | `Integrity Verification` | 022、`171`–`174`、`310`–`312`、`338` | **8** | 8 | ✅ |
| 16 | `Interruption Handling` | `313`、`315`–`329`、`357`、`359`–`360` | **19** | 19 | ✅ |
| 17 | `Status Reporting` | `330`–`334`、`339`、`358` | **7** | 7 | ✅ |
| 18 | `Deployment Conditions` | `336`–`337`、`340`–`341`、`343`–`346` | **8** | 8 | ✅ |
| 19 | `Session Management` | `347`–`356`、`361`、`368`–`369` | **13** | 13 | ✅ |
| 20 | `Telematics Client` | `363`–`367` | **5** | 5 | ✅ |
| 21 | `Update Agent` | `370`–`383` | **14** | 14 | ✅ |
| | **合計** | | **311** | 311 | ✅ |

### (ii) 群數閉合

- 21 組所涵蓋之 Heading id 聯集：**45**（應 45） —— ✅
- 45 群中未被任何組涵蓋者：**0** ✅
- 組中出現而不存在於 45 群者：**0** ✅

### (iii) 列 id 集合閉合

- 聯集大小：**311**（應 311） —— ✅
- 母體有而 Layer 2 無（漏）：**0** ✅
- Layer 2 有而母體無（溢）：**0** ✅
- 相交之組對：**0** ✅

### 跨章群之內部分割（R-SU10 v2(a)）

| Heading 群 | 列數 | 分屬之 Test Set | 組數 | 各組列數和 | |
|---|---:|---|---:|---:|:--:|
| `SWE1-FOTA-309` | 70 | `Integrity Verification`(4)、`Interruption Handling`(19)、`Status Reporting`(7)、`Deployment Conditions`(8)、`Session Management`(13)、`Telematics Client`(5)、`Update Agent`(14) | 7 | **70** | ✅ |
| `SWE1-FOTA-170` | 7 | `Silent Update`(3)、`Integrity Verification`(4) | 2 | **7** | ✅ |

---

**三重閉合結果：全部通過 ✅**
### 孤島列檢查（R-SU20）之重跑

### 種子回測（R-SU20 之偵測器；未過即停）

預期種子（下放包 18 §二定案後之 5 個）：`338`、`339`、`357`、`358`、`361`

- 本偵測器（strict）抓到 **5** 個；其中種子 **5/5**
- 種子未被抓到者：**0** ✅
- 種子外之新發現：**0**（無）

**種子回測通過** —— 5 個預期孤島全數重現，且無非預期之孤島。

### 改組前後之孤島變化（T31a）

| | 列數 | 037 列 |
|---|---:|---|
| 改組前（上繳包 15 §6.1） | 7 | `338`、`339`、`357`、`358`、`359`、`360`、`361` |
| 改組後（本輪） | **5** | `338`、`339`、`357`、`358`、`361` |
| **解除** | 2 | `359`、`360` |
| **新產生** | **0** | **無** |

`359` 改置 `Interruption Handling` 後，**`359` 與 `360` 之孤島身分同時解除**（`359` 之後鄰 `360` 與其同組、`360` 之前鄰 `359` 與其同組）；**未製造任何新孤島**。

### ⚠ 「前鄰與後鄰皆不同」之解讀（須分析層確認）

| 解讀 | 孤島數 | 說明 |
|---|---:|---|
| **strict（採）**：只取內部列（前後鄰皆存在） | **5** | 群首／群尾／單列群無法評估此條件，故不計 |
| loose：缺鄰視為「不同」 | 13 | 使**每個單列群與每個群首／群尾**只要與鄰居不同即成孤島 —— 其中多數為 Test Set 之正常邊界，非證據 |

二者相差 **8** 列。strict 之產出全落於 `SWE1-FOTA-309` 等跨章群之內部，即 R-SU20(b) 所指「被自連續段中抽出」之情形。

### (a) 孤島清單，含 R-SU20(d) 之循環風險機器檢查

| 037 列 | 標題 | 其組 | 前鄰 | 後鄰 | 組名實詞見於標題 |
|---|---|---|---|---|---|
| `338` | Pre-Deployment Package Authenticity Verifica | `Integrity Verification` | 337(`Deployment Conditions`) | 339(`Status Reporting`) | **⚠ verification** |
| `339` | OTA Status Reporting via Backchannel | `Status Reporting` | 338(`Integrity Verification`) | 340(`Deployment Conditions`) | **⚠ status／reporting** |
| `357` | Installation Interruption State Management | `Interruption Handling` | 356(`Session Management`) | 358(`Status Reporting`) | **⚠ interruption** |
| `358` | Update Status Reporting to SWMC | `Status Reporting` | 357(`Interruption Handling`) | 359(`Interruption Handling`) | **⚠ status／reporting** |
| `361` | Server-Initiated OTA Background Execution | `Session Management` | 360(`Interruption Handling`) | 363(`Telematics Client`) | — |

**4/5** 個孤島之組名實詞出現於其標題。

> ⚠ **此檢查測得的是「循環之風險」，不是「循環之事實」**（見上繳包 16 §自評）：關鍵詞相符**未必**表示依據是關鍵詞 —— 下放包 17 §四即裁 `339`／`358` 之依據為「其對象為回報訊息」而**維持**，儘管二者皆被本檢查標記。

### (b) 各組於各跨章 Heading 群內之連續段數

| Heading 群 | Test Set | 段數 | 各段 |
|---|---|---:|---|
| `SWE1-FOTA-170` | `Integrity Verification` | 1 | 171–174 |
| `SWE1-FOTA-170` | `Silent Update` | 1 | 175–177 |
| `SWE1-FOTA-309` | `Interruption Handling` | **3** | 313–329、357、359–360 |
| `SWE1-FOTA-309` | `Status Reporting` | **3** | 330–334、339、358 |
| `SWE1-FOTA-309` | `Session Management` | **3** | 347–356、361、368–369 |
| `SWE1-FOTA-309` | `Integrity Verification` | **2** | 310–312、338 |
| `SWE1-FOTA-309` | `Deployment Conditions` | **2** | 336–337、340–346 |
| `SWE1-FOTA-309` | `Telematics Client` | 1 | 363–367 |
| `SWE1-FOTA-309` | `Update Agent` | 1 | 370–383 |

### (c) 聚集分佈

| 聚集 | 037 列 | 個數 | 跨度 |
|---:|---|---:|---:|
| 1 | `338`、`339` | 2 | 2 列 |
| 2 | `357`、`358` | 2 | 2 列 |
| 3 | `361` | 1 | 1 列 |

**5 個孤島聚為 3 處**（判準：孤島間之 037 列距 ≤ 2）。若切分照能力，錯誤應散開；**聚於少數幾處表示該段有系統性成因**（R-SU20(c)）。

> **R-SU20(e) 之限度（隨檢查一併陳述）**：孤島列指出「該處之依據需高於相鄰之先驗」，**不是「該處錯了」**。規格作者確有可能在連續數列中交替寫數種能力。判其對錯仍須讀該列之描述。

---

## 4. T31d —— 0 列 Heading 群清單之程式化

- 程式產生：**9** 群 —— `SWE1-FOTA-016`、`SWE1-FOTA-017`、`SWE1-FOTA-020`、`SWE1-FOTA-022`、`SWE1-FOTA-072`、`SWE1-FOTA-073`、`SWE1-FOTA-074`、`SWE1-FOTA-076`、`SWE1-FOTA-085`
- `framework.md` 所載：**9** 群
- 檔載而實測非 0：**0** ✅
- 實測為 0 而檔未載：**0** ✅

**比對結果：相符 ✅**（R-SU21 v2(b)：9 群）

實作（`scripts/layer2_close.py::t31d`）：0 列群清單由 `group_by_heading()`
之產出直接導出，再以 regex 自 `framework.md` §「0 列 Heading 群」節取出所載之 id，
**雙向差集皆須為空**，不符即 `sys.exit`。

**此為 R-SU21 v2(b)「其列舉須以程式產生，不得人手列」之落地** ——
條文之清單自此**不再由人維護**：改動 037 或 Layer 2 後，
若某群變成／不再是 0 列，本項會在下一次跑閉合時直接擋下。

---

## 5. T31c —— `framework.md` 更新

已更新（281 行）。變更：

| 項 | 內容 |
|---|---|
| 效力分級表 | Layer 2 改為「全定稿（21 組，**無 provisional 列**）」 |
| Layer 2 定稿表 | `Interruption Handling` **19**（區間 `313`/`315`–`329`/`357`/`359`–`360`）、`Session Management` **13**（`347`–`356`/`361`/`368`–`369`）；其餘 19 組不變，合計 311 |
| 孤島列節 | 改為 **5 個／3 處聚集**，逐列補**記名依據**（取自 Description 之內容，非標題關鍵詞）；加「改組前後」對照表 |
| 新節「五列定案之記錄」 | 五列之前後歸屬與變動；`357` 之**雙職**警語（IN §8.2.2 得拆 2 TC，二者皆 trace 本列） |
| `PROVISIONAL-ROW` | **標記全部移除**；載明 R-SU20(f) 之要求已滿足 |
| 0 列群節 | 改 **9 群**，載明由程式產生並比對；R-SU21 v1(b) 之誤與 v2(b) 之更正 |
| Layer 3 | `Session Management` 一列補「**`361` 另併列 `4.7.1` 之可能**」（下放包 18 §二之族緣註記） |

### 5.1 ⚠ 下放包 §4.1 之 pilot 組成有一處誤

§4.1 稱 `Silent Update`「含 **HMI 列 1（`177`）** 與 **Service 列 8**」。

實測：**HMI 2 列（`177`、`183`）／Service 7 列**。
`SWE1-FOTA-183`（`Display Silent Update Completion and Warning`）之
`Sub Categorization` 為 **HMI**，§4.1 未計入。

**此誤之方向是有利的** —— pilot 之選定依據為「可同時試 UI 型與 Service 型」，
2 個 HMI 列比 1 個更能達成該目的，且 `183` 為顯示型（Completion/Warning 畫面）、
`177` 為限制型（Restrict Opt-Out and Deferral Options in HMI），
**二者之 UI 形態不同**，對 pilot 更有價值。**選定依據不受影響，記明數字。**

### 5.2 ⚠ `176` 之首選分**等於**機制 3 之門檻

實測：機制 3 之門檻（R-SU14 v4(c)，首選分第 20 百分位）為
`0.26716366259482566`；`SWE1-FOTA-176` 之首選分為
`0.26716366259482566` —— **同一個浮點數，非近似**。

成因是結構性的，**不是巧合**：門檻之定義為
`tops[int(n * 20 / 100)]`，即**取自母體之一個實測值**。
於是**恆有一列（該百分位所在之列）之分數恰等於門檻**，
其是否被攔完全取決於判準寫成 `< th` 還是 `≤ th`。
現行實作為 `<`，故 `176` **不被機制 3 攔下**。

**這是第三次同型之邊界脆弱**：
`292`（分 0.257 vs 第 15 百分位 0.256，差 0.001，上繳包 11）、
`260`（分差 0.00810 vs 第 10 百分位 0.00810，上繳包 12）、
本例（`176` 分數與門檻完全相等）。
前二次為分析層據以否證自身裁定之依據；本次**發生在 pilot 之 GT 列上**。

**其實害在本 pilot 為零**（`176` 之 GT 正解 `4907476`+`4907477` 皆在前 5，
非缺口列，攔不攔下都不改變其材料）。**但門檻之 `<`／`≤` 未經裁定**，
且該選擇恆定影響一列。**列入待確認。**

---

## 6. 未結 DR 清單

**空表。** 本輪 0 筆、無變動。

### 待分析層確認之事項（非 DR，無外部資料需求）

| # | 事項 | 出處 |
|---:|---|---|
| 1 | **機制 3 門檻之 `<` vs `≤`** —— 門檻取自實測百分位值，恆有一列坐在界上；現為 `<`，故 `176` 不被攔 | §5.2 |
| 2 | **下放包 §4.1 之 pilot 組成** HMI 1/Service 8 應為 **HMI 2（`177`,`183`）/Service 7** | §5.1 |
| 3 | **R-SU20(a)「連續」之解讀**（strict 得 5 vs loose 得 13）—— 上繳包 16 待確認 #1，未獲裁，本包沿用 strict | §3 |
| 4 | **TC ID 之命名未裁** —— pilot TC 起草前須有；`write_back_036.py` 之 TC 組裝段亦待此 | 上繳包 16 §5.1 |

---

## 7. 獨立自評

### 7.1 §六.6 所問：`359` 改組後二組之連續段數如何變化，該變化是否使切分更碎

**答：更整，不更碎。且此結論可由三個互不相同的量同時支持。**

**(a) 連續段數**（`309` 群內）：

| Test Set | 改組前 | 改組後 | |
|---|---:|---:|---|
| `Session Management` | **4**（347–356、359、361、368–369） | **3**（347–356、361、368–369） | **↓1** |
| `Interruption Handling` | **3**（313–329、357、360） | **3**（313–329、357、**359–360**） | 持平 |
| 其餘五組 | 1/1/2/2/3 | 1/1/2/2/3 | 不變 |
| **總段數** | **16** | **15** | **↓1** |

`Session Management` 少一段；`Interruption Handling` 段數不變，
**但其中一段由單列（`360`）長成雙列（`359`–`360`）** ——
**段數持平而段長增加**，這是比段數更細的一個改善。

**(b) 孤島數**：7 → **5**，新產生 **0**。
`359` 與 `360` 之孤島身分**同時**解除 —— 因二者互為文件序鄰居，
一旦同組，彼此就成為對方的「同組鄰居」。
**一次改組解掉兩個孤島，是因為原本的錯把一對鄰居拆開了。**

**(c) 單列段之數量**（`309` 群內，實測）：

| | 單列段 | 明細 |
|---|---:|---|
| 改組前 | **7** | `338`、`339`、`357`、`358`、`359`、`360`、`361` |
| 改組後 | **5** | `338`、`339`、`357`、`358`、`361` |

**↓2** —— `359`／`360` 二個單列段合併為一個雙列段。

**三個量同向**，故「更整」不是單一指標的假象。

**但須說明其限度**：這三個量都是**同一個結構事實的不同投影**
（`359` 與 `360` 從分屬兩組變成同組），它們**必然同向**，
所以「三個量同向」不構成三重證據，只是同一件事說了三遍。
**真正獨立的證據只有一個**：下放包 18 §二對 `359` 給出的記名依據
（與 `323` 同一觸發面與保護目標，且 `323` 之 GT 正解在 `4.12`），
而那是**讀 Description 得到的，不是段數算出來的**。

**反過來說**：若某次改組使段數變多，那才是需要解釋的訊號 ——
段數是**單向**的健康指標（變好時不足以證明對，變壞時足以要求交代）。

### 7.2 本輪之方法有無「答不到卻看似答到」之處

**有，在 §3 之種子回測「5/5 通過」。**

上一輪之種子是 7 個**實際觀測到的**孤島 —— 那是真正的種子回測
（PLAYBOOK §7(10)：拿已知該被抓到的案例餵進去）。
本輪我把 `SEED_ISLANDS` 改成了 **5**，而那 5 個是**我依改組推算出來的預期值**，
不是獨立觀測。**於是「5/5 通過」實際上是「程式算出的結果等於我用同一套規則手算的結果」**
—— 它驗的是我沒算錯，不是偵測器沒壞。

**真正有鑑別力的那一格是「種子外之新發現 0 個」**，
因為那一格會抓到「改組製造了非預期之孤島」——
而 T31a 明令「新產生之孤島列須列出」，正是問這個。
我另加了「改組前後對照表」把解除 2 個／新產生 0 個分開列，
才把該問題答完整。

**若只看「5/5」，讀者會以為偵測器又被獨立驗證了一次；實際上本輪它沒有。**
上一輪之 7/7 才是。

### 7.3 一項我做了而下放包未要求的事

**§5.2 —— 量了 `176` 之首選分與機制 3 門檻的關係。**

T31b 只令「標示各列是否落入機制 3（門檻 0.267）」。照做就是印 `—` 或 `⚠ 攔下`，
`176` 之 0.267 會印成「—」（不攔），表格看起來完全正常。

我去比了未四捨五入的值，發現二者是**同一個浮點數**。
再回頭看門檻之定義才明白這是**結構性的**：門檻取自母體之實測百分位值，
所以那個位次上的列**必然**與門檻相等，`<` 與 `≤` 之差恆定影響它。

**記明此事之理由**：這是同型邊界脆弱的**第三次**，而前兩次都被當成
「巧合／脆弱」處理（`292` 差 0.001、`260` 差 0.00000）。
本次顯示它**根本不是巧合** —— 只要門檻取自實測值，
就永遠有一列坐在界上。**前兩次的「脆弱」其實是這個結構的兩個相鄰表現。**

**其實害在本輪為零**（`176` 非缺口列），我也未自行改判準 ——
`<` 與 `≤` 之選擇屬裁定。但**不記明它，這個結構性事實會在
某次它真的影響一個缺口列時才被發現**，而那時它會再度看起來像巧合。
