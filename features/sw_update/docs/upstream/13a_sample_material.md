# 上繳材料 13a —— GT-A2 重取樣之人裁材料（30 列）

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/14_reverse_sample.md` §五 T27a
- 依據：**R-SU17 v2(a)**（分層鍵改為 037 Heading 群）
- 母包：`docs/upstream/13_reverse_sample.md`

> **本冊取代 `12a_sample_material.md`。** `12a` 之 30 列因其分層鍵
> （路徑 A top1 章）已由 R-SU17 v2(a) 廢止而**全數作廢，不得人裁**。
>
> **執行層不作判斷。** 各列之正解由分析層逐列裁定；裁定後入
> `GROUND_TRUTH.md` 之 GT-A2 節。
>
> ⚠ 本批為**等額配置**（每層 1 列），逐列之抽中機率相差達 **52×**，
> 見下表。**不加權之比率是「每群一列」之比率，不是母體之比率。**

---

## T27a —— GT-A2 重取樣（分層鍵 = 037 Heading 群）

- 分層鍵：**037 之 Heading 群**（R-SU17 v2(a)）——其分佈來自上游文件結構，**與路徑 A 之輸出無關**
- **`12a` 之 30 列全數廢棄**（其分層鍵 top1 章已由 R-SU17 v2(a) 廢止）
- Heading 群 **45** 群（另 1 個前言偽節，所轄 0 列）；轄有 in-scope 列者 **36** 群
- 抽樣池：311 − GT-A1 28 − GT-B 4 = **279** 列，落於 **35** 個非空層
- 取樣碼：`random.Random(27)`；層序 `shuffle`，層內 `sample`，先每層取 1 列，不足 30 時再取第 2 列（**沿 R-SU17 v1(a) 之每層至多 2 列**—— v2(a) 未另定，執行層沿用並揭露）

### 群大小分佈（45 群，依所轄 in-scope 列數）

| 列數 | 群數 |
|---:|---:|
| 70 | 1 |
| 36 | 1 |
| 26 | 1 |
| 16 | 1 |
| 15 | 1 |
| 14 | 1 |
| 13 | 1 |
| 12 | 1 |
| 11 | 1 |
| 10 | 1 |
| 7 | 2 |
| 6 | 5 |
| 5 | 1 |
| 4 | 3 |
| 3 | 5 |
| 2 | 2 |
| 1 | 8 |
| 0 | 9 |

最大群 **70** 列（`SWE1-FOTA-309` OMA-DM Security）、最小群 **0** 列 —— R-SU17 v2(a) 所揭露之殘餘偏誤於本批之量值見 §抽中機率。

### 章涵蓋對照

| | 群數 | 佔 45 |
|---|---:|---:|
| **本批（30 列）涵蓋之 Heading 群** | **30** | **67%** |
| 轄有 in-scope 列而未抽中者 | 6 | — |
| 無 in-scope 列（結構上不可抽） | 9 | 20% |

### ⚠ 每列之抽中機率（等額配置之殘餘偏誤，量值）

等額配置（每層 1 列）使**小群之列被抽中之機率遠高於大群之列**。任何以本批所作之比率估計若不加權，即以群為單位而非以列為單位。**逐列之抽中機率列於下表，供日後作加權估計（Horvitz–Thompson）之用。**

| # | 037 列 | Heading 群 | 標題 | 群內池列數 | 抽中機率 |
|---:|---|---|---|---:|---:|
| 1 | `SWE1-FOTA-049` | `SWE1-FOTA-038` | OTA download via Wi-Fi | 15 | **0.067** |
| 2 | `SWE1-FOTA-012` | `SWE1-FOTA-009` | Critical Updates | 6 | **0.167** |
| 3 | `SWE1-FOTA-093` | `SWE1-FOTA-091` | Installation Progress | 4 | **0.250** |
| 4 | `SWE1-FOTA-169` | `SWE1-FOTA-168` | Vehicle-Initiated Session Flow | 1 | **1.000** |
| 5 | `SWE1-FOTA-037` | `SWE1-FOTA-024` | Critical Updates | 8 | **0.125** |
| 6 | `SWE1-FOTA-228` | `SWE1-FOTA-214` | HU FOTA with TBM | 34 | **0.029** |
| 7 | `SWE1-FOTA-288` | `SWE1-FOTA-287` | OTA client Flows | 3 | **0.333** |
| 8 | `SWE1-FOTA-130` | `SWE1-FOTA-129` | User Experience (UX)/HMI | 6 | **0.167** |
| 9 | `SWE1-FOTA-199` | `SWE1-FOTA-192` | Bus communications | 3 | **0.333** |
| 10 | `SWE1-FOTA-187` | `SWE1-FOTA-185` | OTA client sessions | 1 | **1.000** |
| 11 | `SWE1-FOTA-255` | `SWE1-FOTA-251` | High Level FOTA Diagram | 6 | **0.167** |
| 12 | `SWE1-FOTA-007` | `SWE1-FOTA-001` | Firmware Over-the-air Updates (FOTA) | 6 | **0.167** |
| 13 | `SWE1-FOTA-210` | `SWE1-FOTA-202` | OTA Architecture Requirements | 10 | **0.100** |
| 14 | `SWE1-FOTA-066` | `SWE1-FOTA-058` | Connection to Wi-Fi network | 12 | **0.083** |
| 15 | `SWE1-FOTA-201` | `SWE1-FOTA-200` | OTA Client Configuration options | 1 | **1.000** |
| 16 | `SWE1-FOTA-128` | `SWE1-FOTA-127` | Download Descriptor Format | 1 | **1.000** |
| 17 | `SWE1-FOTA-268` | `SWE1-FOTA-266` | OTA Client Configuration options | 4 | **0.250** |
| 18 | `SWE1-FOTA-279` | `SWE1-FOTA-278` | User initiated sessions | 1 | **1.000** |
| 19 | `SWE1-FOTA-162` | `SWE1-FOTA-137` | Deployment flow | 26 | **0.038** |
| 20 | `SWE1-FOTA-191` | `SWE1-FOTA-188` | User initiated sessions | 3 | **0.333** |
| 21 | `SWE1-FOTA-081` | `SWE1-FOTA-078` | Media Reflash Requirements | 5 | **0.200** |
| 22 | `SWE1-FOTA-057` | `SWE1-FOTA-055` | Non-Critical Updates | 2 | **0.500** |
| 23 | `SWE1-FOTA-286` | `SWE1-FOTA-285` | OTA Client Performance Requirements | 1 | **1.000** |
| 24 | `SWE1-FOTA-121` | `SWE1-FOTA-110` | TBM FOTA Reflash | 14 | **0.071** |
| 25 | `SWE1-FOTA-275` | `SWE1-FOTA-271` | OTA server initiated sessions | 6 | **0.167** |
| 26 | `SWE1-FOTA-108` | `SWE1-FOTA-096` | Pre-Installation | 13 | **0.077** |
| 27 | `SWE1-FOTA-305` | `SWE1-FOTA-291` | Bearer selection: | 15 | **0.067** |
| 28 | `SWE1-FOTA-264` | `SWE1-FOTA-263` | OTA Architecture Requirements | 2 | **0.500** |
| 29 | `SWE1-FOTA-090` | `SWE1-FOTA-086` | Post-Installation | 3 | **0.333** |
| 30 | `SWE1-FOTA-350` | `SWE1-FOTA-309` | OMA-DM Security | 52 | **0.019** |

抽中機率之極差：**0.019 – 1.000**（比值 **52×**）。等額配置下最大群之列被抽中之機率為最小群之 1/52。

### 人裁材料索引

材料全文見 `docs/upstream/13a_sample_material.md`。


---

### 1. `SWE1-FOTA-049` — Return to Wi-Fi Download Screen After Connection Failure

- Heading 群：`SWE1-FOTA-038` OTA download via Wi-Fi｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-031`｜群內池列數 15

**Requirement Description 全文**：

> The WiFi Update Service shall monitor Wi-Fi network connection status using WiFi Manager and Connectivity Manager. Upon detecting a Wi-Fi connection failure, the WiFi Update Service through Connectivity Manager shall notify the HMI of the connection failure status. The HMI shall provide an option for the user to navigate back to the software download via Wi-Fi screen when Wi-Fi connection establishment is unsuccessful. Upon user selection of the back option, the HMI shall navigate to the software download via Wi-Fi screen.

**路徑 A（語料 v2）前 5 候選**：

1. `4907428` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.326**
   > User shall be able to go back to the software download via Wi-Fi, if connection is not successful (see HMI)

2. `4907826` — 章 **7.1** Critical Updates — 分 **0.275**
   > User shall be able to navigate to software download via Wi-Fi from the pop up or from the settings menu (kindly see the HMI)

3. `4907301` — 章 **4.4** OTA Client Architecture — 分 **0.234**
   > Data connection &amp; Socket interface. This component is the same as for the Vehicle Manager. It provides the connectivity to the server.

4. `4907417` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.232**
   > Upon entering software downloads via Wi-Fi, user shall be able to check enable software download via Wi-Fi

5. `4907421` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.226**
   > If user selects no then HU shall go back to software download via Wi-Fi page


---

### 2. `SWE1-FOTA-012` — Resume FOTA Critical Update via Wi-Fi During Body OFF Mode

- Heading 群：`SWE1-FOTA-009` Critical Updates｜Sub Cat：Service｜Source：`SYS-RA-FOTA-004`｜群內池列數 6

**Requirement Description 全文**：

> The WiFi Update Service shall monitor the vehicle operational power mode using the vehicle property $OperationalModeSts$ through CarPropertyManager. If a critical FOTA package download over the embedded modem (TBM network) is interrupted when the vehicle transitions to Body OFF mode, the WiFi Update Service shall use WifiManager to determine the availability of previously configured Wi-Fi networks. If a previously configured Wi-Fi network is available during Body OFF mode, the WiFi Update Service shall request WifiManager to establish Wi-Fi connectivity and shall use ConnectivityManager to monitor and validate network connectivity. The WiFi Update Service shall request SWMC to resume the interrupted FOTA package download from the last successfully downloaded package state. *Body on mode when $OperationalModeSts$ = Ignition_on or Ignition_pre_start or Ignition_start or Ignition_Cranking or Iginiton_on_Engine_on else Body off when $OperationalModeSts$ =Initialization or Ignition_Off_WithoutKey or Ignition_Off or Ignition_Acc or Ignition_Pre_Acc or Ignition_Pre_Off or Automatic_Cranking or Automatic_Stop or Key_Authenticated or Not_Used Body on mode SNA

**路徑 A（語料 v2）前 5 候選**：

1. `4907831` — 章 **7.1** Critical Updates — 分 **0.365**
   > If the download of FOTA critical update over TBM gets interrupted when the vehicle transitions to Body OFF mode*, the HU shall check for an available, saved and configured Wi-Fi network to resume the download during Body OFF mode. * Please refer to CFTS009 for Power moding states

2. `4907829` — 章 **7.1** Critical Updates — 分 **0.365**
   > If the download of FOTA critical update over TBM gets interrupted when the vehicle transitions to Body OFF mode*, the HU shall check for an available, saved and configured Wi-Fi network to resume the download during Body OFF mode. * Please refer to CFTS009 for Power moding states

3. `4907828` — 章 **7.1** Critical Updates — 分 **0.314**
   > If the download of FOTA critical update gets interrupted when the vehicle transitions to Body OFF mode*, the download shall resume over TBM at the next Body ON mode* Please refer to CFTS009 for Power moding states

4. `4907398` — 章 **4.6** OTA download via Wi-Fi — 分 **0.265**
   > Pre Conditions for FOTA via Wifi:➢ Vehicle’s battery is above 65% State of Charge ($IBS_SOC$ &gt; [65]). If $IBS_SOC$ not available in the vehicle's DBC check: Vehicle in with motor running ($OperationalModeSts$ = [Ignition_On_Engine_On]) for 30 minutes.➢ Ignition position is OFF ($PowerMode$ = [IGN_OFF]).

5. `4907874` — 章 **8.4** MOTA Client Initiated Updates — 分 **0.244**
   > If the update is downloaded via Wi-Fi with Body OFF mode, the installation shall happen at the next Body ON mode.


---

### 3. `SWE1-FOTA-093` — Display Reverted Pop-up on Rollback Success

- Heading 群：`SWE1-FOTA-091` Installation Progress｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-111`｜群內池列數 4

**Requirement Description 全文**：

> The ROV Update Service shall retrieve FOTA_Status using CarPropertyManager. If FOTA_Status indicates FOTA FailureRollback Successful($FOTA_Status$ = [FOTA FailureRollback Successful]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the “Reverted” pop-up after successful rollback.

**路徑 A（語料 v2）前 5 候選**：

1. `4907901` — 章 **9.2** Installation Progress — 分 **0.611**
   > When the HU receives $FOTA_Status$ = [FOTA FailureRollback Successful] , the HU shall display the "Reverted pop-up"Please refer to HMI

2. `4907904` — 章 **9.2** Installation Progress — 分 **0.393**
   > When the HU receives $FOTA_Status$ = [Successful FOTA Update] , the HU shall display the software update complete pop-up, PU0416Please refer to HMI

3. `4907880` — 章 **9.1** Pre-Installation — 分 **0.325**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

4. `4907884` — 章 **9.1** Pre-Installation — 分 **0.315**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

5. `4907909` — 章 **9.3** Post-Installation — 分 **0.289**
   > The HU shall cache $FOTA_Status$ = [Successful FOTA Update] and What's new details to display until next Body ON mode.


---

### 4. `SWE1-FOTA-169` — Parse Deployment Package and Invoke Component Installers

- Heading 群：`SWE1-FOTA-168` Vehicle-Initiated Session Flow｜Sub Cat：Service｜Source：`SYS-RA-FOTA-285`｜群內池列數 1

**Requirement Description 全文**：

> The WiFi Update Service after successful installation precondition validation, analyze the deployment package manifest received from SWMC and identify the target component type for each contained component package. The WiFi Update Service/USB Update Service shall invoke the appropriate installer or update agent for each identified component package. The WiFi Update Service/USB Update Service shall forward MCPU firmware packages to the Update Engine for installation. The WiFi Update Service/USB Update Service shall forward peripheral component packages to the SW Updater Manager for installation and deployment processing.

**路徑 A（語料 v2）前 5 候選**：

1. `4907590` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.215**
   > 8. After installation pre-condition check the OTA client shall parse the deployment package and invoke installers (see Deployment Flow) and update agents for the component types in the deployment package, to deploy the software updates.

2. `4907331` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.186**
   > Download Manager component of the OTA client shall support reliable download of the deployment package.

3. `4907306` — 章 **4.4** OTA Client Architecture — 分 **0.175**
   > Installers are responsible for deployment of specific software component types and for hand off to update agents or platform installation mechanisms relevant for that component type. Installers are responsible for retrieving individual software versions of all managed components of the relevant type, as well as implementing the specific communications protocol (CAN, LIN, etc) with the component or…

4. `4907248` — 章 **2** Common Reflash Requirements — 分 **0.158**
   > For both USB and FOTA software updates, the HU shall permit only update packages to be downloaded which are intended for the HU hardware variant.

5. `4907453` — 章 **4.7.3** Main Update Configuration Options — 分 **0.154**
   > Update type:


---

### 5. `SWE1-FOTA-037` — Enforce Critical Update Flow with Postpone Only Option

- Heading 群：`SWE1-FOTA-024` Critical Updates｜Sub Cat：Service｜Source：`SYS-RA-FOTA-389`｜群內池列數 8

**Requirement Description 全文**：

> The WiFi Update Service shall identify update packages classified as Critical Update from metadata received through SWMC and shall override configured network bearer preference rules to continue update processing using available supported network bearers. The WiFi Update Service shall trigger the SW Update HMI to present the mandatory critical update interaction flow. During Critical Update execution, the SW Update HMI shall not provide a Reject option and shall allow the user to postpone installation only until the next vehicle restart. The WiFi Update Service shall apply the Critical Update workflow for safety-related update sessions.

**路徑 A（語料 v2）前 5 候選**：

1. `4907454` — 章 **4.7.3** Main Update Configuration Options — 分 **0.427**
   > Critical update: Ignore network bearer rules and proceed with the update. End user/HMI flow shall be followed, but the user should not be given an option to reject the update – only to postpone it to the next vehicle restart. This is intended for critical safety-related updates.

2. `4907456` — 章 **4.7.3** Main Update Configuration Options — 分 **0.288**
   > Regular update: Non-silent, non-critical update. End-user/HMI flow shall be followed, and Network bearer rules apply.

3. `4907464` — 章 **4.7.3** Main Update Configuration Options — 分 **0.271**
   > Bearer preference rules SHALL be ignored during critical updates.

4. `4907455` — 章 **4.7.3** Main Update Configuration Options — 分 **0.252**
   > Silent update: An update that does not display any notifications during the session (there is no end-user interaction)—the end-user cannot reject the update. Network bearer rules for minimizing download cost apply.

5. `4907886` — 章 **9.1** Pre-Installation — 分 **0.181**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI


---

### 6. `SWE1-FOTA-228` — Use FOTA_Status from SGW as Master HMI Trigger Signal

- Heading 群：`SWE1-FOTA-214` HU FOTA with TBM｜Sub Cat：Service｜Source：`SYS-RA-VF747_V2-1066`｜群內池列數 34

**Requirement Description 全文**：

> The ROV FOTA AppService shall receive $FOTA_MASTER.FOTA_Status$ from the Secure Gateway (SGW) through the vehicle property interface using CarProperty Manager. The ROV FOTA AppService shall use $FOTA_MASTER.FOTA_Status$ as the primary control signal for ROV FOTA HMI activity handling.

**路徑 A（語料 v2）前 5 候選**：

1. `4907880` — 章 **9.1** Pre-Installation — 分 **0.232**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

2. `4907884` — 章 **9.1** Pre-Installation — 分 **0.228**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

3. `4907900` — 章 **9.2** Installation Progress — 分 **0.201**
   > The HU shall populate the installation percentage and estimated time remaining progress in the pop-up, "Installation Progress ROV" based on the status received from SGW_FOTA_HMI_ETM.4215

4. `4907889` — 章 **9.1** Pre-Installation — 分 **0.187**
   > If the user selects 'What's New' option on "ROV Forced Update Available A" or "ROV Forced Update Availbale B" pop-up, the HU shall display the pop-up (PU0410) with what's new details based on the information received from SGW_FOTA_HMI_ETM.4215.Please refer to the latest Software Updates FOTA HMI L&amp;F.

5. `4907886` — 章 **9.1** Pre-Installation — 分 **0.180**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI


---

### 7. `SWE1-FOTA-288` — OTA Server Command and Configuration Handling

- Heading 群：`SWE1-FOTA-287` OTA client Flows｜Sub Cat：Service｜Source：`SYS-RA-FOTA-394`｜群內池列數 3

**Requirement Description 全文**：

> SWMC shall receive and process server commands for software update management. SWMC shall retrieve, interpret, and apply configuration parameters received from the server, including session-specific and global configuration settings.

**路徑 A（語料 v2）前 5 候選**：

1. `4907449` — 章 **4.7.3** Main Update Configuration Options — 分 **0.304**
   > The OTA client shall follow commands received from the OTA server on how to manage each update as defined in this section. There are several configuration options that MAY be set by the OTA server; some are defined by per session, others are global settings.

2. `4907439` — 章 **4.7.1** OTA Client Performance Requirements — 分 **0.170**
   > OTA client MAY NOT negatively impact the HMI performance when an active management session or download session is in process.

3. `4907342` — 章 **4.4.2** OTA Client Configuration options — 分 **0.163**
   > OTA client shall abstract the installer components of the deployment manager such that the specific installation method can be either, differential update, full image update, or read and differential apply depending on the ECU and vehicle configuration.

4. `4907585` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.155**
   > 3. OTA server MAY request the client for a complete or partial software inventory. The OTA client shall retrieve the required software inventory and provide it to the server.

5. `4907323` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.154**
   > Vehicle make shall be based on &lt;Brand_Configuration_2&gt; proxi parameters. Software Component and Management Object (SCOMO) standards SHOULD be complied with according to OMA DM SCOMO specification [OMA-TS-DM-SCOMO-V1_0-20111206-A] to ensure OTA client interoperability with standard-based OTA servers unless a proprietary communications protocol is used. OTA client implementation shall allow fo…


---

### 8. `SWE1-FOTA-130` — Support NAFTA Region Languages for SW Update HMI

- Heading 群：`SWE1-FOTA-129` User Experience (UX)/HMI｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-216`｜群內池列數 6

**Requirement Description 全文**：

> The MCPU platform software shall provide localization support for the three languages required for the NAFTA region. The supported languages shall include English, North American French, and North American Spanish. The HMI shall display update-related text and messages using the language currently configured in language settings.

**路徑 A（語料 v2）前 5 候選**：

1. `4907653` — 章 **4.11** User Experience (UX)/HMI — 分 **0.378**
   > HU shall support all 3 languages supported in the NAFTA region.

2. `4907316` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.102**
   > The OTA client shall be able to display download descriptor information to the HMI, if available, including text description and update size.

3. `4907744` — 章 **4.13.4.1** Appendix A Download Descriptor Format — 分 **0.100**
   > The Download Descriptor (DD) describes the deployment package that the OTA server sends to the vehicle. The DD is a simple XML file that contains the parameters listed in the following table. Table A-1: Download Descriptor Parameters Name Description installParam An installation parameter associated with the download package. It contains an embedded XML with the &lt;installerType&gt; tag, which co…

4. `4907495` — 章 **4.8** Security — 分 **0.085**
   > FOTA software shall only be available in NAFTA vehicles with embedded cell modems, all FOTA software shall be removed from the HU otherwise.

5. `4907826` — 章 **7.1** Critical Updates — 分 **0.084**
   > User shall be able to navigate to software download via Wi-Fi from the pop up or from the settings menu (kindly see the HMI)


---

### 9. `SWE1-FOTA-199` — Transmit Tester Present During External ECU Reflash

- Heading 群：`SWE1-FOTA-192` Bus communications｜Sub Cat：Service｜Source：`SYS-RA-FOTA-435`｜群內池列數 3

**Requirement Description 全文**：

> The ROV Update Service shall transmit periodic diagnostic Tester Present messages to external ECUs through the vehicle communication interface during any active reflash operation to maintain the diagnostic programming session. The service shall stop transmission after reflash completion, abort, or timeout.

**路徑 A（語料 v2）前 5 候選**：

1. `4907393` — 章 **4.5.5** Bus communications — 分 **0.355**
   > OTA client implementation that is managing external ECU's shall transmit diagnostic message indicating a Tester Present (ex: 0x3E on CAN) when it is attempting to perform any reflash operation.

2. `4907394` — 章 **4.5.5** Bus communications — 分 **0.284**
   > OTA client shall NOT attempt to transmit reflash commands when another diagnostic tool is attached and broadcasting the Tester Present command. If present, the OTA client shall wait until the tester is disconnected, revalidate the target software version for relevancy of the update file, and continue its reflash process.

3. `4907368` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.212**
   > Detection of ECU configuration changes, such as detection of manual diagnostic reflash or component replacement by service technician SHALL trigger a vehicle initiated session. This trigger shall be handled with the same event based interface into the OTA client.01

4. `4907388` — 章 **4.5.5** Bus communications — 分 **0.172**
   > ECU installer shall follow FCA reflash Pre-Program sequence in relevant E/E architecture reflash requirement in order to avoid other ECUs setting loss of communication DTC faults. This shall be sent globally before beginning an external ECU reflash. Example of sequence in below diagram:

5. `4907814` — 章 **6** TBM Algorithm Requirements — 分 **0.150**
   > When TBM receives a 10 03 Diagnostic Request from FOTA Master ($F5 Diagnostic Address), TBM moves into Extended Diagnostic Session without activating Maintenance Mode.


---

### 10. `SWE1-FOTA-187` — Execute OTA Session with or without HMI Availability

- Heading 群：`SWE1-FOTA-185` OTA client sessions｜Sub Cat：Service｜Source：`SYS-RA-FOTA-397`｜群內池列數 1

**Requirement Description 全文**：

> The SWMC and WiFi Update Service shall support OTA session execution regardless of SW Update HMI availability. When the SW Update HMI is unavailable, the WiFi Update Service shall interact with SWMC to continue deployment package download, installation, retry, and completion processing without user input.

**路徑 A（語料 v2）前 5 候選**：

1. `4907443` — 章 **4.7.2** OTA client Flows — 分 **0.239**
   > OTA client shall support the same flows regardless whether there is HMI or not. If there is no HMI, then the OTA client shall implement a pre-defined flow in order to progress the session regardless of user input.

2. `4907333` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.164**
   > If HMI is available, OTA client shall be able to update the HMI of the download progress.

3. `4907442` — 章 **4.7.2** OTA client Flows — 分 **0.141**
   > This section provides an overview for the OTA client flows. Foreground processes display notifications to, and receive input from, the end-user HMI. Background processes proceed without any end-user interaction or HMI.

4. `4907659` — 章 **4.11** User Experience (UX)/HMI — 分 **0.139**
   > Different HMI shall be displayed according to the phase: from the session initiation to completion of a deployment package download (success) or interruption of the download (failure). Specific HMI implementation shall defer to document [VP4-8.4 Refresh SR18 HMI Logic and Flow] documentation.

5. `4907645` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.137**
   > In case the vehicle is driven during the installation, the update shall continue until complete.


---

### 11. `SWE1-FOTA-255` — SWMC Download Manager Integration

- Heading 群：`SWE1-FOTA-251` High Level FOTA Diagram｜Sub Cat：Service｜Source：`SYS-RA-FOTA-492`｜群內池列數 6

**Requirement Description 全文**：

> SWMC shall reliably download the deployment package using the URL obtained from the Download Descriptor. Upon successful download, SWMC shall provide the deployment package to WiFiUpdateService for further OTA update processing.

**路徑 A（語料 v2）前 5 候選**：

1. `4907332` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.415**
   > OTA client shall download the package from the URL provided in the Download Descriptor.

2. `4907300` — 章 **4.4** OTA Client Architecture — 分 **0.294**
   > Download Agent is responsible for reliable downloading of the deployment package (DP) from the URL provided in the deployment package download descriptor (DD), and providing information about download progress.

3. `4907331` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.231**
   > Download Manager component of the OTA client shall support reliable download of the deployment package.

4. `4907481` — 章 **4.7.3.2** Silent Updates — 分 **0.224**
   > 1. The download of the deployment package shall start automatically.

5. `4907588` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.219**
   > 6. After acceptance, the OTA client shall check for download pre-conditions and then download the deployment package.


---

### 12. `SWE1-FOTA-007` — Display Wi-Fi Download Pop-up for Non-Critical Update

- Heading 群：`SWE1-FOTA-001` Firmware Over-the-air Updates (FOTA)｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-008`｜群內池列數 6

**Requirement Description 全文**：

> The WiFi Update Service shall retrieve saved Wi-Fi network information from WiFi Manager and determine whether a previously configured Wi-Fi network is available. The WiFi Update Service shall retrieve the software package classification from the metadata of the downloaded Deployment Descriptor (DD) received from SWMC. The WiFi Update Service shall monitor the ignition status using CarPropertyManager and maintain the FOTA package download attempt count. If: the software package classification is Non-Critical, IgnitionStatus = OFF, and either no previously configured Wi-Fi network is available or the FOTA package download attempt count is greater than or equal to 7, the WiFi Update Service shall request SW Update HMI to display the Wi-Fi pop-up notification.

**路徑 A（語料 v2）前 5 候選**：

1. `4907821` — 章 **7** Firmware Over-the-air Updates (FOTA) — 分 **0.280**
   > Triggering Conditions: - A non-critical software package available - Ignition status == off - No Wi-Fi network saved or DL attempt has been made seven times See HMI for the pop-up

2. `4907818` — 章 **7** Firmware Over-the-air Updates (FOTA) — 分 **0.208**
   > If there is a Wi-Fi network saved, HU will attempt to download the package with in 7 ignition cycles before showing a pop-up to the user to connect to a Wi-Fi network for software download (Kindly see HMI, and below or triggering conditions)

3. `4907399` — 章 **4.6** OTA download via Wi-Fi — 分 **0.204**
   > If there is an existing Wi-Fi network saved, and HU meets the precondition for download via Wi-Fi then HU shall attempt to download the software package via Wi-Fi network

4. `4907802` — 章 **6** TBM Algorithm Requirements — 分 **0.184**
   > When TBM has completed the download of a FOTA update with notification package, then the TBM shall send $TBMUpdate$ = [Update_Available]

5. `4907831` — 章 **7.1** Critical Updates — 分 **0.179**
   > If the download of FOTA critical update over TBM gets interrupted when the vehicle transitions to Body OFF mode*, the HU shall check for an available, saved and configured Wi-Fi network to resume the download during Body OFF mode. * Please refer to CFTS009 for Power moding states


---

### 13. `SWE1-FOTA-210` — Execute Component Dependency and Installation Order from Server Metadata

- Heading 群：`SWE1-FOTA-202` OTA Architecture Requirements｜Sub Cat：Service｜Source：`SYS-RA-FOTA-488`｜群內池列數 10

**Requirement Description 全文**：

> The WiFi Update Service shall parse dependency and installation sequence information from deployment package metadata received through SWMC and shall control component installation sequencing according to the specified dependency order. The WiFi Update Service shall prevent installation of dependent components until prerequisite component installation is successfully completed based on installer status feedback.

**路徑 A（語料 v2）前 5 候選**：

1. `4907327` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.264**
   > OTA implementation shall allow for dependency handling between software components, including installation order. The OTA client shall follow dependency instructions it receives from the server.

2. `4907811` — 章 **6** TBM Algorithm Requirements — 分 **0.184**
   > During any Ignition conditions, When an update installation has been successfully completed, then the TBM shall send $TBMUpdate$ = [Update_End] for &lt;T_FOTA_END&gt;

3. `4907590` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.182**
   > 8. After installation pre-condition check the OTA client shall parse the deployment package and invoke installers (see Deployment Flow) and update agents for the component types in the deployment package, to deploy the software updates.

4. `4907352` — 章 **4.4.3** Operating Environment — 分 **0.179**
   > Update Agent component shall NOT be dependent on any high level OS in order to perform a file-system update.

5. `4907351` — 章 **4.4.3** Operating Environment — 分 **0.174**
   > Update Agent component shall NOT be dependent on any high level OS in order to perform an image update.


---

### 14. `SWE1-FOTA-066` — Display No Saved WiFi Network Pop-up on Next IGN_OFF

- Heading 群：`SWE1-FOTA-058` Connection to Wi-Fi network｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-043`｜群內池列數 12

**Requirement Description 全文**：

> The HMI shall receive no-saved-network status from the WiFi Manager when no Wi-Fi network is saved. Upon the next transition of $PowerMode$ t= [IGN_OFF] received through CarProperty Manager, the HMI shall display the pop-up .

**路徑 A（語料 v2）前 5 候選**：

1. `4907414` — 章 **4.6.2** Non-Critical Updates — 分 **0.444**
   > If there is no Wi-Fi network saved, then HU shall display a pop – up on next $PowerMode$ = [IGN_OFF]. (Kindly see the triggering conditions)

2. `4907821` — 章 **7** Firmware Over-the-air Updates (FOTA) — 分 **0.265**
   > Triggering Conditions: - A non-critical software package available - Ignition status == off - No Wi-Fi network saved or DL attempt has been made seven times See HMI for the pop-up

3. `4907832` — 章 **7.1** Critical Updates — 分 **0.264**
   > During Requirement ID 4907831, the HU shall only check for saved and available Wi-Fi network to resume the download and shall not display any pop-up to the user to configure Wi-Fi network.

4. `4907830` — 章 **7.1** Critical Updates — 分 **0.264**
   > During Requirement ID 4907829, the HU shall only check for saved and available Wi-Fi network to resume the download and shall not display any pop-up to the user to configure Wi-Fi network.

5. `4907807` — 章 **6** TBM Algorithm Requirements — 分 **0.251**
   > During $PowerMode$ = [IGN_LK]


---

### 15. `SWE1-FOTA-201` — Support Transport-Agnostic Handling of Deployment Packages

- Heading 群：`SWE1-FOTA-200` OTA Client Configuration options｜Sub Cat：Service｜Source：`SYS-RA-FOTA-447`｜群內池列數 1

**Requirement Description 全文**：

> The SWMC shall support communication between OTA client components distributed across multiple host systems through defined common communication interfaces. The SWMC shall exchange OTA session information, deployment package status, workflow events, and control messages through standardized communication interfaces between distributed OTA client components. The communication interfaces between distributed SWMC components shall be independent of the underlying host platform implementation and shall be exposed according to FCA integration requirements.

**路徑 A（語料 v2）前 5 候選**：

1. `4907340` — 章 **4.4.2** OTA Client Configuration options — 分 **0.435**
   > In the event that the OTA client components are on multiple host systems (tethered phone for example), common communications interfaces shall be defined in order to communicate between components and should be exposed to FCA.

2. `4907567` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.268**
   > Server initiated session - Communication between FOTA Client &amp; TC

3. `4907338` — 章 **4.4.2** OTA Client Configuration options — 分 **0.179**
   > The OTA client shall be configurable to support various implementation methods. The OTA client shall support a configuration where it is available both fully embedded on a HU or the components may be split between a tethered mobile phone and HU. The OTA client shall support configurations where back channel communication to an OTA server is not available, such as in the case where the deployment p…

4. `4907328` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.176**
   > Network communication shall be completed via an exposed socket interface to the underlying protocol stack in order to allow for portability to multiple platforms.

5. `4907569` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.162**
   > FOTA client shall establish communication with TC client.


---

### 16. `SWE1-FOTA-128` — Parse Download Descriptor XML and Extract Deployment Parameters

- Heading 群：`SWE1-FOTA-127` Download Descriptor Format｜Sub Cat：Service｜Source：`SYS-RA-FOTA-181`｜群內池列數 1

**Requirement Description 全文**：

> The SWMC shall parse the Download Descriptor provided with the update. The SWMC shall process the Download Descriptor as an XML file. The SWMC shall extract deployment package parameters and metadata from the Download Descriptor. The SWMC shall use the extracted parameters and metadata from below mentioned parameters to control from below and execute the OTA update workflow. installParam --> Installation parameter associated with the download package; contains embedded XML with `<installerType>` tag and comma-separated installer types wrapped inside `<![CDATA[]]>`. DDVersion --> Defines the version of the Download Descriptor. description --> Short textual description of the package in format: `<Name>,<Version>,<Filename>;...;Settings`. objectURI --> URL used to download the package. size --> Size of the download package in bytes. type --> MIME media type of the download package. vendor --> Information about the organization providing the package. installNotifyURI --> URL used to send installation success/failure status reports. infoURL --> URL containing additional information about the package. message --> Multi-language consumer message describing package changes and affected vehicle modules; displayed based on HU language, default language is English (US).

**路徑 A（語料 v2）前 5 候選**：

1. `4907744` — 章 **4.13.4.1** Appendix A Download Descriptor Format — 分 **0.568**
   > The Download Descriptor (DD) describes the deployment package that the OTA server sends to the vehicle. The DD is a simple XML file that contains the parameters listed in the following table. Table A-1: Download Descriptor Parameters Name Description installParam An installation parameter associated with the download package. It contains an embedded XML with the &lt;installerType&gt; tag, which co…

2. `4907332` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.308**
   > OTA client shall download the package from the URL provided in the Download Descriptor.

3. `4907300` — 章 **4.4** OTA Client Architecture — 分 **0.270**
   > Download Agent is responsible for reliable downloading of the deployment package (DP) from the URL provided in the deployment package download descriptor (DD), and providing information about download progress.

4. `4907316` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.234**
   > The OTA client shall be able to display download descriptor information to the HMI, if available, including text description and update size.

5. `4907293` — 章 **4.4** OTA Client Architecture — 分 **0.215**
   > Communciations Protocol Stack. The OTA client may implement OMA-DM or an approved proprietary protocol to negotiate with the server, authenticate the vehicle, provide information about the vehicle to the server, and retrieve the Download Descriptor (DD) [OMA-SUP-XSD_dd-V2_0-20110329-A]. The DD contains URL of Deployment Package (DP) and metadata that is needed for the user interface and may affect…


---

### 17. `SWE1-FOTA-268` — Platform-Independent OMA-DM Communication Support

- Heading 群：`SWE1-FOTA-266` OTA Client Configuration options｜Sub Cat：Service｜Source：`SYS-RA-FOTA-441`｜群內池列數 4

**Requirement Description 全文**：

> SWMC shall communicate with the OTA Server using platform-independent OMA-DM compliant protocols. When a proprietary communication protocol is configured, SWMC shall support the platform-independent proprietary communication protocol for OTA communication.

**路徑 A（語料 v2）前 5 候選**：

1. `4907347` — 章 **4.4.3** Operating Environment — 分 **0.394**
   > OMA-DM standards themselves are designed to be platform-independent. This is achieved by using platform-independent protocols and technologies (TCP/IP, XML, SyncML, WAP, etc.). Also, some vehicle-dependent things may be customized within the protocol (device-management tree, extensions, installers, etc.). If proprietary communications are approved they shall also be platform-independent.

2. `4907355` — 章 **4.5.1** OTA Communication Protocols — 分 **0.361**
   > The OTA client is RECOMMENDED to use the open communication protocols defined in Table 4-3 to communicate with the server solution interface. HTTP and TLS protocols are REQUIRED if a proprietary communication protocol is used in place of OMA-DM. Table 4-3: Communication Protocols Originator Destination Protocol Specification Version OTA Client DM Server OMA DM 1.2.1 OMA-TS-DM-Protocol-V1_2-2006042…

3. `4907314` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.338**
   > It is RECOMMENDED that the OTA client implement the open OMA-DM protocol specification [OMA-TS-DM-Protocol-V1_2-20060424-C] in order to communicate with with the server. Use of non-open proprietary communication protocol MAY be allowed if approved by FCA.

4. `4907535` — 章 **4.9.1** Update Agent Requirements — 分 **0.280**
   > UA shall be platform independent with a well defined porting layer API interface to enable integrating it into any platform.

5. `4907504` — 章 **4.8.1** Communication Security — 分 **0.194**
   > OTA client shall NOT initiate communication to any unauthorized server.


---

### 18. `SWE1-FOTA-279` — Open Communication Protocol Support

- Heading 群：`SWE1-FOTA-278` User initiated sessions｜Sub Cat：Service｜Source：`SYS-RA-FOTA-409`｜群內池列數 1

**Requirement Description 全文**：

> SWMC shall support communication with the server interface using the configured open communication protocols. SWMC shall support HTTP and TLS protocols when a proprietary communication protocol is configured instead of OMA-DM.

**路徑 A（語料 v2）前 5 候選**：

1. `4907355` — 章 **4.5.1** OTA Communication Protocols — 分 **0.520**
   > The OTA client is RECOMMENDED to use the open communication protocols defined in Table 4-3 to communicate with the server solution interface. HTTP and TLS protocols are REQUIRED if a proprietary communication protocol is used in place of OMA-DM. Table 4-3: Communication Protocols Originator Destination Protocol Specification Version OTA Client DM Server OMA DM 1.2.1 OMA-TS-DM-Protocol-V1_2-2006042…

2. `4907314` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.319**
   > It is RECOMMENDED that the OTA client implement the open OMA-DM protocol specification [OMA-TS-DM-Protocol-V1_2-20060424-C] in order to communicate with with the server. Use of non-open proprietary communication protocol MAY be allowed if approved by FCA.

3. `4907505` — 章 **4.8.1** Communication Security — 分 **0.237**
   > OTA client shall not leave any open port or communication open in listening mode.

4. `4907569` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.183**
   > FOTA client shall establish communication with TC client.

5. `4907567` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.176**
   > Server initiated session - Communication between FOTA Client &amp; TC


---

### 19. `SWE1-FOTA-162` — Enable User-Initiated Retry After Installation Failure

- Heading 群：`SWE1-FOTA-137` Deployment flow｜Sub Cat：Service｜Source：`SYS-RA-FOTA-265`｜群內池列數 26

**Requirement Description 全文**：

> The Update Engine and SW Updater Service shall report installation failure status to the WiFi Update Service/USB Update Service through the installer status callback interface. The WiFi Update Service shall update the OTA session state when installation failure is detected. The SW Update HMI shall provide a retry option to the user after receiving installation failure status from the WiFi Update Service. Upon user selection of the retry option, the SW Update HMI shall notify the WiFi Update Service/USB Update Service . The WiFi Update Service/USB Update Service shall perform deployment precondition validation and re-initiate the update installation.

**路徑 A（語料 v2）前 5 候選**：

1. `4907606` — 章 **4.10.5** Deployment Flow — 分 **0.210**
   > 5. The installers then notify the OTA client of their update status, in the event of a failure they also provide individual ECU DP status codes.

2. `4907256` — 章 **2** Common Reflash Requirements — 分 **0.192**
   > HU shall be capable of receiving Firmware updates from the TBM through a USB 2.0 connection

3. `4907656` — 章 **4.11** User Experience (UX)/HMI — 分 **0.187**
   > User experience shall be same for all update types and updates (regular/critical/silent) SHOULD be configurable from the server so that the FOTA service administrator can select the relevant option depending on the type and urgency of the update being performed.

4. `4907591` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.168**
   > 9. If an interruption occurs during any of the steps before the installation completes successfully, the OTA client shall save the state of the installation, and shall retry to resume the installation.

5. `4907689` — 章 **4.12.2** Report Persistency — 分 **0.162**
   > In the event that the cause of the interrupt and resume of service are not known to the OTA client (for example, the DM Server went down and the OTA client has no indication that the network is back up until it tries to connect to the server), the OTA client shall try to resend the report according to the configured retry parameter.


---

### 20. `SWE1-FOTA-191` — Provide HMI Event Handling Interface for OTA Client

- Heading 群：`SWE1-FOTA-188` User initiated sessions｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-414`｜群內池列數 3

**Requirement Description 全文**：

> The WiFi Update Service shall define an event handling interface for communication with the SW Update HMI. The SW Update HMI shall send user input events to the WiFi Update Service through the defined interface. The WiFi Update Service shall process the received user input events and shall initiate the corresponding OTA workflow actions through interaction with SWMC when required. The WiFi Update Service shall provide appropriate responses or status updates to the SW Update HMI based on the processed HMI events.

**路徑 A（語料 v2）前 5 候選**：

1. `4907361` — 章 **4.5.2** User initiated sessions — 分 **0.392**
   > OTA client SHALL define event handling interface for communication with HMI and be able to respond to user input for support of these requirements.

2. `4907364` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.252**
   > OTA client shall define an interface in order to respond to vehicle events that may be blocking software deployment.

3. `4907867` — 章 **8.3** User Initiated Updates — 分 **0.186**
   > NAV shall provide capability for the user to download an available Map update through the HMI.

4. `4907654` — 章 **4.11** User Experience (UX)/HMI — 分 **0.157**
   > Please note that the OTA client vendor responsibility is limited to specifying the HMI interface API and to invoking that API or supporting the relevant events sent to/received from the HMI. The implementation of the HMI itself should match the host system. Therefore, this document is limited to specifying the requirements on these APIs and events as well as the internal logic of the OTA client an…

5. `4907489` — 章 **4.7.3.3** Regular Updates — 分 **0.157**
   > A regular update includes any update that is not critical or silent. The OTA client shall follow all HMI requirements and flows for regular updates and not skip any user input. See [VP4-8.4 Refresh SR18 HMI Logic and Flow].


---

### 21. `SWE1-FOTA-081` — Select Update Source Based on Latest Software Version

- Heading 群：`SWE1-FOTA-078` Media Reflash Requirements｜Sub Cat：Service｜Source：`SYS-RA-FOTA-069`｜群內池列數 5

**Requirement Description 全文**：

> The WiFi Update Service shall provide available FOTA package version information to the Arbiter Service. The USB Update Service shall provide available USB package version information to the Arbiter Service. The Arbiter Service shall compare the software version information of update packages available from FOTA and USB update methods. When multiple update methods provide update packages with different software versions, the Arbiter Service shall select the update package with the highest software version for deployment processing. The Arbiter Service shall prioritize the selected update source and shall reject or defer deployment processing from the lower version update source.

**路徑 A（語料 v2）前 5 候選**：

1. `4907246` — 章 **2** Common Reflash Requirements — 分 **0.270**
   > When a FOTA update is ready to install and an USB update is available at the same time, the HU shall honor the latest software version release available.

2. `4907247` — 章 **2** Common Reflash Requirements — 分 **0.265**
   > if there are 2 or more update methods available at the same time (FOTA, USB stick, etc.) having same version number radio shall honor the software downloaded via FOTA.

3. `4907517` — 章 **4.8.3** Deployment Package Security — 分 **0.217**
   > For differential updates, the OTA client shall ensure the source version of the update is identical to the version on the target ECU/HU. For a compound firmware deployment package that holds differential updates for multiple elements, OTA client shall ensure this for every differential update in the package.

4. `4907248` — 章 **2** Common Reflash Requirements — 分 **0.201**
   > For both USB and FOTA software updates, the HU shall permit only update packages to be downloaded which are intended for the HU hardware variant.

5. `4907249` — 章 **2** Common Reflash Requirements — 分 **0.188**
   > NAV shall compare the existing Map version with available Map Update and always honor the higher Map version


---

### 22. `SWE1-FOTA-057` — Wi-Fi Download Timeout Handling During IGN_OFF Timed Mode

- Heading 群：`SWE1-FOTA-055` Non-Critical Updates｜Sub Cat：Service｜Source：`SYS-RA-FOTA-043`｜群內池列數 2

**Requirement Description 全文**：

> The WiFi Update Service shall monitor the timed download mode status and vehicle ignition state using CarPropertyManager. When the vehicle transitions to IGN_OFF and timed download mode is active, the WiFi Update Service shall start a Wi-Fi download session timer. If the Wi-Fi download session duration exceeds 30 minutes during the current ignition cycle, the WiFi Update Service shall terminate the active FOTA download session and request WifiManager to transition the M-CPU platform from Client Mode to Host Mode. ConnectivityManager shall be used to monitor the network state transition.

**路徑 A（語料 v2）前 5 候選**：

1. `4907415` — 章 **4.6.2** Non-Critical Updates — 分 **0.431**
   > HU shall start the timer for download via Wi-Fi at ignition off when timed mode has expired. HU shall terminate the download session for the duration of ignition cycle after T = 30 minutes has expired and switch back to host mode.

2. `4907862` — 章 **8.1** Non-Critical Updates — 分 **0.295**
   > When the NAV notifies HU that MOTA data is not being received, HU shall terminate the download session for the duration of the Ignition cycle and switch to host mode.

3. `4907820` — 章 **7** Firmware Over-the-air Updates (FOTA) — 分 **0.233**
   > If during a download the HU detects that no FOTA data is not being received over the Wi-Fi connection for 5 consecutive minutes and there is sufficient Wi-Fi signal strength, the HU shall terminate the download session for the duration of the ignition cycle and switch to hostmode. .

4. `4907398` — 章 **4.6** OTA download via Wi-Fi — 分 **0.219**
   > Pre Conditions for FOTA via Wifi:➢ Vehicle’s battery is above 65% State of Charge ($IBS_SOC$ &gt; [65]). If $IBS_SOC$ not available in the vehicle's DBC check: Vehicle in with motor running ($OperationalModeSts$ = [Ignition_On_Engine_On]) for 30 minutes.➢ Ignition position is OFF ($PowerMode$ = [IGN_OFF]).

5. `4907831` — 章 **7.1** Critical Updates — 分 **0.186**
   > If the download of FOTA critical update over TBM gets interrupted when the vehicle transitions to Body OFF mode*, the HU shall check for an available, saved and configured Wi-Fi network to resume the download during Body OFF mode. * Please refer to CFTS009 for Power moding states


---

### 23. `SWE1-FOTA-286` — OTA Flow Status Reporting

- Heading 群：`SWE1-FOTA-285` OTA Client Performance Requirements｜Sub Cat：Service｜Source：`SYS-RA-FOTA-400`｜群內池列數 1

**Requirement Description 全文**：

> SWMC shall generate and send a status report upon completion of each session or update flow. SWMC shall include the execution result indicating success or failure of the completed flow operation.

**路徑 A（語料 v2）前 5 候選**：

1. `4907447` — 章 **4.7.2** OTA client Flows — 分 **0.347**
   > At the end of any flow, the OTA client shall send a report as to the status (success or failure) of the flow. See Report Persistency for specific requirements regarding reporting.

2. `4907690` — 章 **4.12.2** Report Persistency — 分 **0.246**
   > In the event of an ECU reflash failure fault for any reason, error flags shall be reported back to the OTA server indicating the cause of the failure. This shall include the deployment package status code as well as any ECU fault codes and a CAN communication log that are a result of the failed operation.

3. `4907592` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.230**
   > 10. After update is complete, client shall send the result of the update back to the server (see 4.11.2 Report Persistency).

4. `4907686` — 章 **4.12.2** Report Persistency — 分 **0.221**
   > The OTA client shall send a report to the OTA server when the session completes, whether successfully or with a failure.

5. `4907659` — 章 **4.11** User Experience (UX)/HMI — 分 **0.194**
   > Different HMI shall be displayed according to the phase: from the session initiation to completion of a deployment package download (success) or interruption of the download (failure). Specific HMI implementation shall defer to document [VP4-8.4 Refresh SR18 HMI Logic and Flow] documentation.


---

### 24. `SWE1-FOTA-121` — Display TBM Update End Screen

- Heading 群：`SWE1-FOTA-110` TBM FOTA Reflash｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-138`｜群內池列數 14

**Requirement Description 全文**：

> The TBM Update Service shall retrieve $TBMUpdate$ using the TBM FW Service and detect when the value indicates Update_End. Upon detecting $TBMupdate$ = [Update_End], the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall display the TBM update end screen.

**路徑 A（語料 v2）前 5 候選**：

1. `4907793` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.470**
   > When the HU receives $TBMupdate$ = [Update_End], the HU show the TBM update end screen on the HMI. Kindly see the HMI.

2. `4907790` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.388**
   > When HU receives $TBMUpdate$ = [Update_End], HU shall display TBM update success pop-up. Please refer to the HMI L&amp;F.

3. `4907811` — 章 **6** TBM Algorithm Requirements — 分 **0.377**
   > During any Ignition conditions, When an update installation has been successfully completed, then the TBM shall send $TBMUpdate$ = [Update_End] for &lt;T_FOTA_END&gt;

4. `4907783` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.366**
   > When HU receives $TBMupdate$ = [Update_Available] from the from TBM, on ignition off the HU shall show the TBM FOTA update pop-up screen to the user. Kindly see the HMI.

5. `4907789` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.358**
   > TBM shall send $TBMUpdate$ = [Update_End] when TBM SW update is successfully installed and at next IGN_ON.


---

### 25. `SWE1-FOTA-275` — Server-Configurable Polling Interva

- Heading 群：`SWE1-FOTA-271` OTA server initiated sessions｜Sub Cat：Service｜Source：`SYS-RA-FOTA-419`｜群內池列數 6

**Requirement Description 全文**：

> SWMC shall support configuration of the polling interval for periodic vehicle-initiated sessions through parameters received from the server. SWMC shall update and apply the configured polling interval for polling operations.

**路徑 A（語料 v2）前 5 候選**：

1. `4907579` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.359**
   > The vehicle-initiated session shall have a reconfigurable polling interval of 24 hours.

2. `4907367` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.351**
   > The polling interval for periodic vehicle initiated operation shall be configurable from the server. See appendix B for more configurable intervals.

3. `4907366` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.340**
   > The polling interval for periodic vehicle initiated operation is RECOMMENDED to be configurable from the server. See appendix B for more configurable intervals.

4. `4907580` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.232**
   > The polling interval for vehicle-initaited session shall always be reconfigurable and set in 'HOURS' format.

5. `4907582` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.221**
   > 1. Vehicle polling timer causes a vehicle-initiated session to be queued.


---

### 26. `SWE1-FOTA-108` — Display No Connectivity Pop-up for ROV Update

- Heading 群：`SWE1-FOTA-096` Pre-Installation｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-117`｜群內池列數 13

**Requirement Description 全文**：

> The ROV FOTA HMI shall capture user selection of “Update Now” from the “ROV Forced Update Available B” pop-up. The ROV Update Service shall retrieve $LTE_Status$ or $Cellsignal$ using CarPropertyManager. If ROV Update Service receives $LTE_Status$ <> [3G OR 4G OR H_Plus] OR $Cellsignal$ = [0 OR 1 OR SNA], the ROV Update HMI shall display the "No Connectivity" pop-up and prevent update initiation.

**路徑 A（語料 v2）前 5 候選**：

1. `4907895` — 章 **9.1** Pre-Installation — 分 **0.713**
   > HU shall display "No Connectivity pop-up", when the user selects 'Update Now' option on "ROV Forced Update Available B" pop-up and if the HU receives $LTE_Status$ &lt;&gt; [3G OR 4G OR H_Plus] OR $Cellsignal$ = [0 OR 1 OR SNA]Please refer to HMI

2. `4907884` — 章 **9.1** Pre-Installation — 分 **0.377**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

3. `4907886` — 章 **9.1** Pre-Installation — 分 **0.345**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI

4. `4907880` — 章 **9.1** Pre-Installation — 分 **0.345**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

5. `4907887` — 章 **9.1** Pre-Installation — 分 **0.294**
   > When the $Hybrid_Type$ = [BEV] or [PHEV] and if the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then the HU shall display "Schedule Update popup" (PUXXX3).Please refer to the latest Software Updates FOTA HMI L&amp;F.


---

### 27. `SWE1-FOTA-305` — Authorized Server Communication

- Heading 群：`SWE1-FOTA-291` Bearer selection:｜Sub Cat：Service｜Source：`SYS-RA-FOTA-344`｜群內池列數 15

**Requirement Description 全文**：

> SWMC shall verify that the target OTA Server is an authorized server before initiating communication. SWMC shall reject any communication request to an unauthorized server.

**路徑 A（語料 v2）前 5 候選**：

1. `4907504` — 章 **4.8.1** Communication Security — 分 **0.399**
   > OTA client shall NOT initiate communication to any unauthorized server.

2. `4907567` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.206**
   > Server initiated session - Communication between FOTA Client &amp; TC

3. `4907569` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.169**
   > FOTA client shall establish communication with TC client.

4. `4907514` — 章 **4.8.3** Deployment Package Security — 分 **0.159**
   > The OTA client shall verify integrity of the deployment package once it is received from the server, immediately post download.

5. `4907600` — 章 **4.10.5** Deployment Flow — 分 **0.138**
   > If deployed OTA, whether end-users can reject the deployment depends on the Critical Update and Silent Install flags that are set by the OTA server.


---

### 28. `SWE1-FOTA-264` — Installer Abstraction for Multiple Update Methods

- Heading 群：`SWE1-FOTA-263` OTA Architecture Requirements｜Sub Cat：Service｜Source：`SYS-RA-FOTA-446`｜群內池列數 2

**Requirement Description 全文**：

> SWMC shall determine the appropriate installation method and provide the Download Descriptor (DD) and deployment package information to WiFiUpdateService. WiFiUpdateService shall invoke the appropriate installer based on the installation method provided by SWMC.

**路徑 A（語料 v2）前 5 候選**：

1. `4907896` — 章 **9.1** Pre-Installation — 分 **0.194**
   > When the HU is in the pre-installation flow, if $FOTA_Status$ &lt;&gt; [Waiting for HMI Acceptance], the HU shall interrupt the current pre-installation flow and display appropriate HMI based on current $FOTA_Status$

2. `4907332` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.186**
   > OTA client shall download the package from the URL provided in the Download Descriptor.

3. `4907590` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.181**
   > 8. After installation pre-condition check the OTA client shall parse the deployment package and invoke installers (see Deployment Flow) and update agents for the component types in the deployment package, to deploy the software updates.

4. `4907300` — 章 **4.4** OTA Client Architecture — 分 **0.176**
   > Download Agent is responsible for reliable downloading of the deployment package (DP) from the URL provided in the deployment package download descriptor (DD), and providing information about download progress.

5. `4907342` — 章 **4.4.2** OTA Client Configuration options — 分 **0.160**
   > OTA client shall abstract the installer components of the deployment manager such that the specific installation method can be either, differential update, full image update, or read and differential apply depending on the ECU and vehicle configuration.


---

### 29. `SWE1-FOTA-090` — Cache and Display “What’s New” After Successful Update Until Next Body ON

- Heading 群：`SWE1-FOTA-086` Post-Installation｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-104`｜群內池列數 3

**Requirement Description 全文**：

> The ROV Update Service shall retrieve FOTA_Status using CarPropertyManager and detect when the value indicates Successful FOTA Update.( $FOTA_Status$ = [Successful FOTA Update] ) Upon detection, the ROV Update Service shall cache the FOTA_Status and the “What’s New” details received from the deployment package. The ROV Update Service shall retrieve OperationalModeSts using CarPropertyManager to determine the vehicle Body ON/OFF state. The ROV FOTA HMI shall display the cached “What’s New” information to the user. The ROV Update Service shall retain the cached data until the next transition to Body ON mode. *Body on mode when $OperationalModeSts$ = Ignition_on or Ignition_pre_start or Ignition_start or Ignition_Cranking or Iginiton_on_Engine_on else Body off when $OperationalModeSts$ =Initialization or Ignition_Off_WithoutKey or Ignition_Off or Ignition_Acc or Ignition_Pre_Acc or Ignition_Pre_Off or Automatic_Cranking or Automatic_Stop or Key_Authenticated or Not_Used Body on mode SNA

**路徑 A（語料 v2）前 5 候選**：

1. `4907909` — 章 **9.3** Post-Installation — 分 **0.432**
   > The HU shall cache $FOTA_Status$ = [Successful FOTA Update] and What's new details to display until next Body ON mode.

2. `4907874` — 章 **8.4** MOTA Client Initiated Updates — 分 **0.248**
   > If the update is downloaded via Wi-Fi with Body OFF mode, the installation shall happen at the next Body ON mode.

3. `4907889` — 章 **9.1** Pre-Installation — 分 **0.246**
   > If the user selects 'What's New' option on "ROV Forced Update Available A" or "ROV Forced Update Availbale B" pop-up, the HU shall display the pop-up (PU0410) with what's new details based on the information received from SGW_FOTA_HMI_ETM.4215.Please refer to the latest Software Updates FOTA HMI L&amp;F.

4. `4907634` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.218**
   > If the user selects 'What's New' option, the HU shall display the pop-up (PU0410) with what's new details based on information received from the downloaded deployment package details.Please refer to latest Software Updates FOTA HMI L&amp;F.

5. `4907398` — 章 **4.6** OTA download via Wi-Fi — 分 **0.215**
   > Pre Conditions for FOTA via Wifi:➢ Vehicle’s battery is above 65% State of Charge ($IBS_SOC$ &gt; [65]). If $IBS_SOC$ not available in the vehicle's DBC check: Vehicle in with motor running ($OperationalModeSts$ = [Ignition_On_Engine_On]) for 30 minutes.➢ Ignition position is OFF ($PowerMode$ = [IGN_OFF]).


---

### 30. `SWE1-FOTA-350` — Session Precondition Evaluation

- Heading 群：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-278`｜群內池列數 52

**Requirement Description 全文**：

> The SWMC shall evaluate the configured preconditions before initiating an OTA update session. If one or more preconditions are not satisfied, the SWMC shall queue the OTA update session until the preconditions are satisfied.

**路徑 A（語料 v2）前 5 候選**：

1. `4907378` — 章 **4.5.4.1** SMS/MQTT Push Support — 分 **0.201**
   > Upon receipt of a “shoulder tap”, the OTA client shall check in with the OTA server given that the OTA session connection pre-conditions are satisfied.

2. `4907379` — 章 **4.5.4.1** SMS/MQTT Push Support — 分 **0.182**
   > If given vehicle pre-conditions are not satisfied the OTA client shall queue the “shoulder tap” event so that it can be processed once the blocking pre-conditions are cleared.

3. `4907372` — 章 **4.5.4.1** SMS/MQTT Push Support — 分 **0.172**
   > The OTA client should support “shoulder tapping” session initiation during which the OTA server is able to ping the OTA client in order to check in to the server to see if there is an available operation. The OTA administrator shall be able to push OTA updates out to various vehicles on demand without waiting for a pre-determined polling interval or vehicle initiated event. The OTA client shall ha…

4. `4907396` — 章 **4.6** OTA download via Wi-Fi — 分 **0.156**
   > When HU detects that a software Download is available, on the next ignition off, if HU meets the preconditions for download via Wi-Fi, HU will check if there is an existing Wi-Fi network saved.

5. `4907680` — 章 **4.12.1** Resuming a Download — 分 **0.139**
   > If an interrupt occurs before a download completes, the OTA client shall suspend the session, write to the log, and wait until the download can resume.

