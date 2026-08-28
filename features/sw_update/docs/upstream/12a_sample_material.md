# 上繳材料 12a —— GT-A2 分層隨機取樣之人裁材料（30 列）

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/13_stratified_gt.md` §五 T26b
- 依據：**R-SU17(a)**（GT-A2 分層隨機）
- 母包：`docs/upstream/12_stratified_gt.md`

> **執行層不作判斷。** 各列之正解由分析層逐列裁定；裁定後入
> `GROUND_TRUTH.md` 之 GT-A2 節。
>
> ⚠ **本批之分層鍵為「首選候選之 CFTS 母章」，是代理變數而非正解之母章**
> —— 其所引入之新偏誤見母包 §7.1，**分析層宜先裁該偏誤是否可接受，
> 再投入 30 列之人裁**。

---

## T26b —— GT-A2 分層隨機取樣材料（30 列）

- 分層鍵：**首選候選之 CFTS 母章**（R-SU17(a) 之「CFTS 母章」；正解之母章在人裁前未知，**此處以路徑 A 之 top1 章為代理**）
- 抽樣池：311 − GT-A1 28 − GT-B 4 − 無候選列 = **279** 列，落於 **44** 個層
- 取樣碼：`random.Random(26)`；先 `shuffle` 層序（**未觸及之章優先於已觸及之章**），再 `sample` 層內全序，取每層第 1 列（不足 30 時再取第 2 列）
- 每層至多 2 列（R-SU17(a)）；本批實際每層 30 列 × 1 層

### 章涵蓋對照

| | 章數 | 佔 87 |
|---|---:|---:|
| GT-A1（定向，28 列） | 12 | 14% |
| **GT-A2 本批（30 列）** | **30** | **34%** |
| GT-A2 新增之章（GT-A1 未觸及） | 30 | 34% |
| 二者聯集 | 42 | 48% |
| 仍未觸及 | 45 | 52% |

> 分母 87 為全部章節物件；轄有需求物件者 57 章，以其為分母則本批涵蓋 53%、聯集 74%。

### 取樣清單

| # | 037 列 | 分層（首選章） | 該層池內列數 | 層別 |
|---:|---|---|---:|---|
| 1 | `SWE1-FOTA-363` | **4.10.2** | 7 | GT-A1 未觸及 |
| 2 | `SWE1-FOTA-355` | **4.6** | 7 | GT-A1 未觸及 |
| 3 | `SWE1-FOTA-274` | **4.5.3** | 5 | GT-A1 未觸及 |
| 4 | `SWE1-FOTA-359` | **4.10** | 2 | GT-A1 未觸及 |
| 5 | `SWE1-FOTA-195` | **4.5.5** | 2 | GT-A1 未觸及 |
| 6 | `SWE1-FOTA-117` | **5** | 17 | GT-A1 未觸及 |
| 7 | `SWE1-FOTA-167` | **4.10.5.1** | 27 | GT-A1 未觸及 |
| 8 | `SWE1-FOTA-350` | **4.5.4.1** | 1 | GT-A1 未觸及 |
| 9 | `SWE1-FOTA-265` | **4.4.2** | 2 | GT-A1 未觸及 |
| 10 | `SWE1-FOTA-090` | **9.3** | 5 | GT-A1 未觸及 |
| 11 | `SWE1-FOTA-083` | **2** | 12 | GT-A1 未觸及 |
| 12 | `SWE1-FOTA-293` | **4.7.3.1** | 2 | GT-A1 未觸及 |
| 13 | `SWE1-FOTA-268` | **4.4.3** | 3 | GT-A1 未觸及 |
| 14 | `SWE1-FOTA-134` | **4.11** | 7 | GT-A1 未觸及 |
| 15 | `SWE1-FOTA-066` | **4.6.2** | 2 | GT-A1 未觸及 |
| 16 | `SWE1-FOTA-007` | **7** | 6 | GT-A1 未觸及 |
| 17 | `SWE1-FOTA-272` | **4.5.4** | 2 | GT-A1 未觸及 |
| 18 | `SWE1-FOTA-104` | **9.1** | 23 | GT-A1 未觸及 |
| 19 | `SWE1-FOTA-190` | **4.5.2** | 2 | GT-A1 未觸及 |
| 20 | `SWE1-FOTA-151` | **4.8.1** | 8 | GT-A1 未觸及 |
| 21 | `SWE1-FOTA-011` | **7.1** | 6 | GT-A1 未觸及 |
| 22 | `SWE1-FOTA-139` | **4.10.5** | 7 | GT-A1 未觸及 |
| 23 | `SWE1-FOTA-147` | **6** | 4 | GT-A1 未觸及 |
| 24 | `SWE1-FOTA-297` | **4.8** | 2 | GT-A1 未觸及 |
| 25 | `SWE1-FOTA-128` | **4.13.4.1** | 1 | GT-A1 未觸及 |
| 26 | `SWE1-FOTA-126` | **4.13.4** | 1 | GT-A1 未觸及 |
| 27 | `SWE1-FOTA-279` | **4.5.1** | 1 | GT-A1 未觸及 |
| 28 | `SWE1-FOTA-376` | **4.4** | 5 | GT-A1 未觸及 |
| 29 | `SWE1-FOTA-375` | **4.9.1** | 9 | GT-A1 未觸及 |
| 30 | `SWE1-FOTA-366` | **4.10.1** | 7 | GT-A1 未觸及 |

---

### 人裁材料（格式同 `07a`／`08a`，前 5 候選）

> **執行層不作判斷。** 各列之正解由分析層逐列裁定。


---

#### 1. `SWE1-FOTA-363` — TC Communication Establishment

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-296`｜分層：**4.10.2**

**Requirement Description 全文**：

> The WiFiUpdateService shall establish and maintain communication with the TC client for OTA update operations.

**路徑 A（語料 v2）前 5 候選**：

1. `4907569` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.473**
   > FOTA client shall establish communication with TC client.

2. `4907402` — 章 **4.6.1** Connection to Wi-Fi network — 分 **0.245**
   > The HU shall establish a Wi-Fi connection with saved Wi-Fi networks for OTA updates

3. `4907504` — 章 **4.8.1** Communication Security — 分 **0.183**
   > OTA client shall NOT initiate communication to any unauthorized server.

4. `4907567` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.154**
   > Server initiated session - Communication between FOTA Client &amp; TC

5. `4907361` — 章 **4.5.2** User initiated sessions — 分 **0.131**
   > OTA client SHALL define event handling interface for communication with HMI and be able to respond to user input for support of these requirements.


---

#### 2. `SWE1-FOTA-355` — Download Precondition Data Provision

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-283`｜分層：**4.6**

**Requirement Description 全文**：

> The WiFiUpdateService shall provide the vehicle and system data required by the SWMC to validate the download preconditions.

**路徑 A（語料 v2）前 5 候選**：

1. `4907396` — 章 **4.6** OTA download via Wi-Fi — 分 **0.179**
   > When HU detects that a software Download is available, on the next ignition off, if HU meets the preconditions for download via Wi-Fi, HU will check if there is an existing Wi-Fi network saved.

2. `4907305` — 章 **4.4** OTA Client Architecture — 分 **0.169**
   > Deployment Agent is responsible for parsing the deployment package meta data and handing off individual software update package files to their relevant installers. It shall be able to map, parse, and signal individual installers and handle dependencies between the software components. It also shall validate the signature of the deployment package to validate that it is a Chrysler generated DP.

3. `4907701` — 章 **4.13.1** SCOMO Support — 分 **0.130**
   > The OTA client shall reboot if required for updating firmware on the host ECU.

4. `4907563` — 章 **4.10.1** Self Registration Flow — 分 **0.115**
   > 5. The OTA server will validate the domain name and PIN code and will use them and the vehicle identification information to register the vehicle in the server in the correct domain/account.

5. `4907296` — 章 **4.4** OTA Client Architecture — 分 **0.104**
   > Push Handler allows the vehicle to receive server-initiated updates. This component registers to receive WAP Push SMS, and provides SMS to the protocol stack. When an SMS is received, Vehicle Manager may start the client-initiated session to check for available updates. This component is required only if server-initiated update is required. This component may also be required to support MQTT.


---

#### 3. `SWE1-FOTA-274` — OTA Communication / Vehicle-Initiated Session

- Heading：`SWE1-FOTA-271` OTA server initiated sessions｜Sub Cat：Service｜Source：`SYS-RA-FOTA-418`｜分層：**4.5.3**

**Requirement Description 全文**：

> SWMC shall maintain configurable polling parameters and initiate periodic communication with the Server when network connectivity is available.

**路徑 A（語料 v2）前 5 候選**：

1. `4907367` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.341**
   > The polling interval for periodic vehicle initiated operation shall be configurable from the server. See appendix B for more configurable intervals.

2. `4907366` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.331**
   > The polling interval for periodic vehicle initiated operation is RECOMMENDED to be configurable from the server. See appendix B for more configurable intervals.

3. `4907504` — 章 **4.8.1** Communication Security — 分 **0.313**
   > OTA client shall NOT initiate communication to any unauthorized server.

4. `4907301` — 章 **4.4** OTA Client Architecture — 分 **0.155**
   > Data connection &amp; Socket interface. This component is the same as for the Vehicle Manager. It provides the connectivity to the server.

5. `4907567` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.141**
   > Server initiated session - Communication between FOTA Client &amp; TC


---

#### 4. `SWE1-FOTA-359` — OTA Flow Concurrency Control

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-289`｜分層：**4.10**

**Requirement Description 全文**：

> The SWMC shall ignore any request to start a new OTA update flow when an OTA update session is already active and shall ensure that the current session is not interrupted.

**路徑 A（語料 v2）前 5 候選**：

1. `4907553` — 章 **4.10** Session Flows — 分 **0.384**
   > While the OTA client is in the middle of another flow, it SHOULD ignore any other attempt to start a new flow and it shall not interrupt the current flow.

2. `4907677` — 章 **4.12** Interrupt Handling — 分 **0.270**
   > If a session is active and the vehicle receives an additional NIA, the OTA client ignores the notification and queues it without interrupting the current active session.

3. `4907556` — 章 **4.10.1** Self Registration Flow — 分 **0.244**
   > The OTA client shall have a method to register itself to the OTA server during its initial OTA session, if it is not already registered to an OTA server.

4. `4907595` — 章 **4.10.4** User-Initiated Session Flow — 分 **0.206**
   > The user-initiated session flow is as follows:

5. `4907574` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.205**
   > The server-initiated session flow is as follows:


---

#### 5. `SWE1-FOTA-195` — Separate OTA Client from Physical Bus Communication Stack

- Heading：`SWE1-FOTA-192` Bus communications｜Sub Cat：Service｜Source：`SYS-RA-FOTA-428`｜分層：**4.5.5**

**Requirement Description 全文**：

> The SWMC and WiFi Update Service shall use generic communication interfaces provided through the platform abstraction layer for vehicle bus communication. The SWMC and WiFi Update Service shall not directly depend on specific physical bus communication stack implementations such as CAN, Ethernet, or LIN. The system architecture shall separate OTA client logic from the underlying bus communication stack implementation to support modularity and maintainability. The generic communication interfaces shall be reusable by other software services and utilities within the platform.

**路徑 A（語料 v2）前 5 候選**：

1. `4907386` — 章 **4.5.5** Bus communications — 分 **0.352**
   > It is RECOMMENDED that the specific physical layer bus communications stack implementation (CAN/Ethernet/LIN/etc) on the host ECU (HU, TBM, etc) be separated from the OTA client such that other utilities can use them.

2. `4907381` — 章 **4.5.4.1** SMS/MQTT Push Support — 分 **0.279**
   > It is RECOMMENDED that any physical layer communications stack implementation (Serial/USB/CAN/Ethernet/LIN/etc) on the host module be separated from the OTA client such that other utilities can use them.

3. `4907385` — 章 **4.5.5** Bus communications — 分 **0.263**
   > Abstraction of bus communication shall be made such that the specific bus communications standard and physical addresses of the ECU's can be modified on a model to model basis.

4. `4907328` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.160**
   > Network communication shall be completed via an exposed socket interface to the underlying protocol stack in order to allow for portability to multiple platforms.

5. `4907569` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.157**
   > FOTA client shall establish communication with TC client.


---

#### 6. `SWE1-FOTA-117` — Display TBM Update Start Screen on Ignition OFF

- Heading：`SWE1-FOTA-110` TBM FOTA Reflash｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-142`｜分層：**5**

**Requirement Description 全文**：

> The TBM Update Service shall retrieve $TBMUpdate$ using the TBM FW Service and detect when the value indicates Update_start. The TBM Update Service shall retrieve $OperationalModeSts$ using CarPropertyManager. If $TBMupdate$ = [Update_start] and $OperationalModeSts$ indicates Body OFF, the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall display the TBM update screen *Body on mode when $OperationalModeSts$ = Ignition_on or Ignition_pre_start or Ignition_start or Ignition_Cranking or Iginiton_on_Engine_on else Body off when $OperationalModeSts$ =Initialization or Ignition_Off_WithoutKey or Ignition_Off or Ignition_Acc or Ignition_Pre_Acc or Ignition_Pre_Off or Automatic_Cranking or Automatic_Stop or Key_Authenticated or Not_Used Body on mode SNA

**路徑 A（語料 v2）前 5 候選**：

1. `4907787` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.357**
   > When the HU receives $TBMupdate$ = [Update_start], on ignition off the HU show the TBM update screen on the HMI. Kindly see the HMI.

2. `4907783` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.316**
   > When HU receives $TBMupdate$ = [Update_Available] from the from TBM, on ignition off the HU shall show the TBM FOTA update pop-up screen to the user. Kindly see the HMI.

3. `4907788` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.267**
   > When the HU receives $TBMupdate$ = [Forced_Update], on ignition off the HU show the forced TBM update screen on the HMI. Kindly see the HMI.

4. `4907874` — 章 **8.4** MOTA Client Initiated Updates — 分 **0.234**
   > If the update is downloaded via Wi-Fi with Body OFF mode, the installation shall happen at the next Body ON mode.

5. `4907398` — 章 **4.6** OTA download via Wi-Fi — 分 **0.229**
   > Pre Conditions for FOTA via Wifi:➢ Vehicle’s battery is above 65% State of Charge ($IBS_SOC$ &gt; [65]). If $IBS_SOC$ not available in the vehicle's DBC check: Vehicle in with motor running ($OperationalModeSts$ = [Ignition_On_Engine_On]) for 30 minutes.➢ Ignition position is OFF ($PowerMode$ = [IGN_OFF]).


---

#### 7. `SWE1-FOTA-167` — Handle Installation Failure and Unrecoverable State UI

- Heading：`SWE1-FOTA-137` Deployment flow｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-271`｜分層：**4.10.5.1**

**Requirement Description 全文**：

> The Update Engine Manager and SW Updater Manager shall report installation failure status to the WiFi Update Service/USB Update Service. Upon receiving installation failure status, the WiFi Update Service shall notify the SW Update HMI. The SW Update HMI shall present installation failure handling options according to the HMI specification. If the Update Engine or SW Updater Manager reports an unrecoverable installation state, the WiFi Update/USB Update Service Service shall notify the SW Update HMI. The SW Update HMI shall display the unrecoverable failure pop-up.

**路徑 A（語料 v2）前 5 候選**：

1. `4907650` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.269**
   > If the installation fails, the HU shall follow the provided HMI. If the HU is unrecoverable, it shall display the pop up indicated in the HMI

2. `4907606` — 章 **4.10.5** Deployment Flow — 分 **0.231**
   > 5. The installers then notify the OTA client of their update status, in the event of a failure they also provide individual ECU DP status codes.

3. `4907902` — 章 **9.2** Installation Progress — 分 **0.189**
   > When the HU receives $FOTA_Status$ = [FOTA Failure Complete] , the HU shall display the "Walk Home Scenario pop-up"Please refer to HMI

4. `4907904` — 章 **9.2** Installation Progress — 分 **0.168**
   > When the HU receives $FOTA_Status$ = [Successful FOTA Update] , the HU shall display the software update complete pop-up, PU0416Please refer to HMI

5. `4907896` — 章 **9.1** Pre-Installation — 分 **0.168**
   > When the HU is in the pre-installation flow, if $FOTA_Status$ &lt;&gt; [Waiting for HMI Acceptance], the HU shall interrupt the current pre-installation flow and display appropriate HMI based on current $FOTA_Status$


---

#### 8. `SWE1-FOTA-350` — Session Precondition Evaluation

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-278`｜分層：**4.5.4.1**

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


---

#### 9. `SWE1-FOTA-265` — Installer Association Using ECU Reference IDs

- Heading：`SWE1-FOTA-263` OTA Architecture Requirements｜Sub Cat：Service｜Source：`SYS-RA-FOTA-445`｜分層：**4.4.2**

**Requirement Description 全文**：

> SWMC shall provide the deployment package and ECU reference information to WiFiUpdateService. WiFiUpdateService/USBUpdateService shall retrieve or use the configured ECU reference IDs (such as part number, CAN address, or equivalent identifiers) to associate the deployment package update file with the appropriate installer and invoke the selected installer.

**路徑 A（語料 v2）前 5 候選**：

1. `4907343` — 章 **4.4.2** OTA Client Configuration options — 分 **0.473**
   > It is RECOMMENDED that the individual installers for a specific ECU type can dynamically retrieve or be assigned with have a list of hard coded reference IDs (FCA part number, CAN Address, etc) such that the deployment manager can associate an update file within a deployment package to a specific installer.

2. `4907587` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.180**
   > 5. OTA client SHALL download the DD and use the information in it to prompt HMI for acceptance of the deployment package.

3. `4907707` — 章 **4.13.1** SCOMO Support — 分 **0.168**
   > OTA client shall support hand off ECU components to appropriate ECU installers for individual bus communication. 4. Map Update Data(MOTA): The OTA client shall be able to install map updates, which the OTA server provides in a deployment package format. The OTA client shall support hand off to a Map management installer

4. `4907590` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.162**
   > 8. After installation pre-condition check the OTA client shall parse the deployment package and invoke installers (see Deployment Flow) and update agents for the component types in the deployment package, to deploy the software updates.

5. `4907342` — 章 **4.4.2** OTA Client Configuration options — 分 **0.138**
   > OTA client shall abstract the installer components of the deployment manager such that the specific installation method can be either, differential update, full image update, or read and differential apply depending on the ECU and vehicle configuration.


---

#### 10. `SWE1-FOTA-090` — Cache and Display “What’s New” After Successful Update Until Next Body ON

- Heading：`SWE1-FOTA-086` Post-Installation｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-104`｜分層：**9.3**

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

#### 11. `SWE1-FOTA-083` — Select Update Source Based on Latest Software Version

- Heading：`SWE1-FOTA-078` Media Reflash Requirements｜Sub Cat：Service｜Source：`SYS-RA-FOTA-069`｜分層：**2**

**Requirement Description 全文**：

> The SWMC shall provide the available FOTA package version information to the WiFi Update Service. The USB update pacakge shall provide the available USB update package version information to the WiFi Update Service. The WiFi Update Service shall forward the received update package version information to the Arbiter Service. The Arbiter Service shall compare the version information of update packages available from FOTA and USB update methods. If multiple update methods provide update packages with different version numbers, the Arbiter Service shall select the update package with the highest version number. The Arbiter Service shall prioritize the selected update source and reject the update request from the lower version update source for installation.

**路徑 A（語料 v2）前 5 候選**：

1. `4907247` — 章 **2** Common Reflash Requirements — 分 **0.263**
   > if there are 2 or more update methods available at the same time (FOTA, USB stick, etc.) having same version number radio shall honor the software downloaded via FOTA.

2. `4907246` — 章 **2** Common Reflash Requirements — 分 **0.244**
   > When a FOTA update is ready to install and an USB update is available at the same time, the HU shall honor the latest software version release available.

3. `4907517` — 章 **4.8.3** Deployment Package Security — 分 **0.210**
   > For differential updates, the OTA client shall ensure the source version of the update is identical to the version on the target ECU/HU. For a compound firmware deployment package that holds differential updates for multiple elements, OTA client shall ensure this for every differential update in the package.

4. `4907249` — 章 **2** Common Reflash Requirements — 分 **0.195**
   > NAV shall compare the existing Map version with available Map Update and always honor the higher Map version

5. `4907248` — 章 **2** Common Reflash Requirements — 分 **0.169**
   > For both USB and FOTA software updates, the HU shall permit only update packages to be downloaded which are intended for the HU hardware variant.


---

#### 12. `SWE1-FOTA-293` — DDF Update Type Processing

- Heading：`SWE1-FOTA-291` Bearer selection:｜Sub Cat：Service｜Source：`SYS-RA-FOTA-380`｜分層：**4.7.3.1**

**Requirement Description 全文**：

> SWMC shall provide the Deployment Descriptor File (DDF) to WiFiUpdateService. WiFiUpdateService shall evaluate the DDF parameters to determine the update type. If the update type parameter is not present in the DDF, WiFiUpdateService shall classify the update as a non-critical update.

**路徑 A（語料 v2）前 5 候選**：

1. `4907473` — 章 **4.7.3.1** Critical Updates — 分 **0.347**
   > If the DDF does not include whether the update is critical or not, the HU shall treat the update as a non-critical update

2. `4907453` — 章 **4.7.3** Main Update Configuration Options — 分 **0.291**
   > Update type:

3. `4907487` — 章 **4.7.3.2** Silent Updates — 分 **0.280**
   > If the DDF does not include whether the update is silent or not, the HU shall treat the update as a non-silent update

4. `4907472` — 章 **4.7.3.1** Critical Updates — 分 **0.176**
   > Critical and non-critical updates shall be defined by the server

5. `4907456` — 章 **4.7.3** Main Update Configuration Options — 分 **0.145**
   > Regular update: Non-silent, non-critical update. End-user/HMI flow shall be followed, and Network bearer rules apply.


---

#### 13. `SWE1-FOTA-268` — Platform-Independent OMA-DM Communication Support

- Heading：`SWE1-FOTA-266` OTA Client Configuration options｜Sub Cat：Service｜Source：`SYS-RA-FOTA-441`｜分層：**4.4.3**

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

#### 14. `SWE1-FOTA-134` — Display Post-Download Installation Options

- Heading：`SWE1-FOTA-129` User Experience (UX)/HMI｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-224`｜分層：**4.11**

**Requirement Description 全文**：

> The SWMC shall detect completion of the deployment package download. After completion of the download, the SWMC shall provide deployment package details to the SW Update HMI through WiFi Update Service. The SW Update HMI shall display the deployment package details to the user . The SW Update HMI shall provide opt-in options including “Install” and “Schedule Later”.

**路徑 A（語料 v2）前 5 候選**：

1. `4907662` — 章 **4.11** User Experience (UX)/HMI — 分 **0.509**
   > After the download is complete, the user is shown the deployment package details, the HMI SHOULD provide the user with opt in options: Install or schedule later.Kindly see the latest HMI for pop up.

2. `4907661` — 章 **4.11** User Experience (UX)/HMI — 分 **0.263**
   > After the DD is downloaded and the user is shown the update details, the HMI SHOULD provide the user with in the relevant options: Download, Cancel, or Later. Download proceeds with the download, cancel rejects the download and causes the OTA client to report to the server, and Later defers the download until the next start of the client or key event.

3. `4907588` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.224**
   > 6. After acceptance, the OTA client shall check for download pre-conditions and then download the deployment package.

4. `4907886` — 章 **9.1** Pre-Installation — 分 **0.220**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI

5. `4907483` — 章 **4.7.3.2** Silent Updates — 分 **0.216**
   > 2. After the deployment package is downloaded, its deployment shall start immediately.


---

#### 15. `SWE1-FOTA-066` — Display No Saved WiFi Network Pop-up on Next IGN_OFF

- Heading：`SWE1-FOTA-058` Connection to Wi-Fi network｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-043`｜分層：**4.6.2**

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

#### 16. `SWE1-FOTA-007` — Display Wi-Fi Download Pop-up for Non-Critical Update

- Heading：`SWE1-FOTA-001` Firmware Over-the-air Updates (FOTA)｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-008`｜分層：**7**

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

#### 17. `SWE1-FOTA-272` — Vehicle Event Interface Support

- Heading：`SWE1-FOTA-271` OTA server initiated sessions｜Sub Cat：Service｜Source：`SYS-RA-FOTA-416`｜分層：**4.5.4**

**Requirement Description 全文**：

> SWMC shall support event interface to receive server-initiated session requests from the Server.

**路徑 A（語料 v2）前 5 候選**：

1. `4907370` — 章 **4.5.4** OTA server initiated sessions — 分 **0.553**
   > OTA client shall support an event interface in order to receive server initiated sessions.

2. `4907559` — 章 **4.10.1** Self Registration Flow — 分 **0.378**
   > 1. The OTA client runs the server-initiated session, client-initiated session or user-initiated session.

3. `4907574` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.347**
   > The server-initiated session flow is as follows:

4. `4907359` — 章 **4.5.2** User initiated sessions — 分 **0.285**
   > OTA client shall be able to respond to HMI initiated session event requesting to check the OTA server for latest updates.

5. `4907567` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.284**
   > Server initiated session - Communication between FOTA Client &amp; TC


---

#### 18. `SWE1-FOTA-104` — Display BEV/PHEV Schedule Update Popup on Schedule Selection

- Heading：`SWE1-FOTA-096` Pre-Installation｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-123`｜分層：**9.1**

**Requirement Description 全文**：

> The ROV Update Service shall retrieve $Hybrid_Type$ using CarPropertyManager. The ROV FOTA HMI shall capture user selection from the “ROV Forced Update Available A” or “ROV Forced Update Available B” pop-up. If $Hybrid_Type$ = [BEV] or [PHEV]and the user selects Schedule Update, the ROV FOTA HMI shall display the “Schedule Update pop-up (PUXXX3)”.

**路徑 A（語料 v2）前 5 候選**：

1. `4907887` — 章 **9.1** Pre-Installation — 分 **0.747**
   > When the $Hybrid_Type$ = [BEV] or [PHEV] and if the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then the HU shall display "Schedule Update popup" (PUXXX3).Please refer to the latest Software Updates FOTA HMI L&amp;F.

2. `4907888` — 章 **9.1** Pre-Installation — 分 **0.708**
   > When the $Hybrid_Type$ = [BEV] or [PHEV] or [FCEV] or [REPB] and if the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then the HU shall display "Schedule Update popup" (PUXXX3).Please refer to the latest Software Updates FOTA HMI L&amp;F.

3. `4907886` — 章 **9.1** Pre-Installation — 分 **0.605**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI

4. `4907884` — 章 **9.1** Pre-Installation — 分 **0.421**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

5. `4907889` — 章 **9.1** Pre-Installation — 分 **0.381**
   > If the user selects 'What's New' option on "ROV Forced Update Available A" or "ROV Forced Update Availbale B" pop-up, the HU shall display the pop-up (PU0410) with what's new details based on the information received from SGW_FOTA_HMI_ETM.4215.Please refer to the latest Software Updates FOTA HMI L&amp;F.


---

#### 19. `SWE1-FOTA-190` — Display No Update Available Status on HMI

- Heading：`SWE1-FOTA-188` User initiated sessions｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-413`｜分層：**4.5.2**

**Requirement Description 全文**：

> The SWMC shall provide the update availability check result to the WiFi Update Service after OTA server communication is completed. When SWMC reports that no software update is available, the WiFi Update Service shall notify the SW Update HMI. The SW Update HMI shall display a message indicating that the vehicle software is up to date and that no updates are available.

**路徑 A（語料 v2）前 5 候選**：

1. `4907360` — 章 **4.5.2** User initiated sessions — 分 **0.248**
   > In the event that no update is available, the OTA client shall be able to inform the HMI (if existing) that the vehicle is up to date and that no updates are available.

2. `4907280` — 章 **4.2.3** HU FOTA with TBM — 分 **0.215**
   > If HU receives $HUReflash$ = [Update Available], HU shall check the server if to check for an update.

3. `4907572` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.207**
   > FOTA client shall check the server for an available FOTA update on receiving callback message from TC.

4. `4907333` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.204**
   > If HMI is available, OTA client shall be able to update the HMI of the download progress.

5. `4907873` — 章 **8.4** MOTA Client Initiated Updates — 分 **0.195**
   > When an update is available, NAV shall notify the HU and requests for a connection


---

#### 20. `SWE1-FOTA-151` — Block Installation During Active Download Session

- Heading：`SWE1-FOTA-137` Deployment flow｜Sub Cat：Service｜Source：`SYS-RA-FOTA-254`｜分層：**4.8.1**

**Requirement Description 全文**：

> The SWMC shall notify the WiFi Update Service when a deployment package download session is in progress. Upon receiving an active download session indication from SWMC, the WiFi Update Service shall prevent software installation initiation. The WiFi Update Service shall allow software installation only after SWMC indicates that all active deployment package download sessions are completed, cancelled, failed, or otherwise terminated.

**路徑 A（語料 v2）前 5 候選**：

1. `4907500` — 章 **4.8.1** Communication Security — 分 **0.195**
   > OTA client shall authenticate the server upon initiation of a session.

2. `4907588` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.167**
   > 6. After acceptance, the OTA client shall check for download pre-conditions and then download the deployment package.

3. `4907444` — 章 **4.7.2** OTA client Flows — 分 **0.163**
   > The following OTA client flows SHALL be supported by the OTA client depending on Compliance field in the below table: Table 4-4: OTA client sessions Flow Compliance Description More Information Self-registration shall The OTA client shall register itself to the OTA server during the initial OTA session. Self Registration Flow Background session shall Upon receiving a shoulder tap informing of a ba…

4. `4907802` — 章 **6** TBM Algorithm Requirements — 分 **0.159**
   > When TBM has completed the download of a FOTA update with notification package, then the TBM shall send $TBMUpdate$ = [Update_Available]

5. `4907590` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.158**
   > 8. After installation pre-condition check the OTA client shall parse the deployment package and invoke installers (see Deployment Flow) and update agents for the component types in the deployment package, to deploy the software updates.


---

#### 21. `SWE1-FOTA-011` — User Navigation to Wi-Fi Software Download

- Heading：`SWE1-FOTA-009` Critical Updates｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-005`｜分層：**7.1**

**Requirement Description 全文**：

> The HMI shall navigate to the software download via Wi-Fi screen when the user selects the Wi-Fi software download entry from the Settings menu. The HMI shall provide navigation to the software download via Wi-Fi screen when the user selects the update pop-up notification. Upon user confirmation to start software download via Wi-Fi, the HMI shall transmit a download initiation request to the WiFi Update Service.

**路徑 A（語料 v2）前 5 候選**：

1. `4907826` — 章 **7.1** Critical Updates — 分 **0.521**
   > User shall be able to navigate to software download via Wi-Fi from the pop up or from the settings menu (kindly see the HMI)

2. `4907421` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.376**
   > If user selects no then HU shall go back to software download via Wi-Fi page

3. `4907417` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.333**
   > Upon entering software downloads via Wi-Fi, user shall be able to check enable software download via Wi-Fi

4. `4907470` — 章 **4.7.3.1** Critical Updates — 分 **0.318**
   > 1. The download of the deployment package shall start automatically; The OTA client SHALL NOT display a download confirmation screen.

5. `4907428` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.314**
   > User shall be able to go back to the software download via Wi-Fi, if connection is not successful (see HMI)


---

#### 22. `SWE1-FOTA-139` — Collect Installer Status and Report ECU Failure Codes

- Heading：`SWE1-FOTA-137` Deployment flow｜Sub Cat：Service｜Source：`SYS-RA-FOTA-232`｜分層：**4.10.5**

**Requirement Description 全文**：

> The Update Engine shall report MCPU installation status information to the WiFi Update Service during the installation process. The SW Updater Manager shall report peripheral component installation status information to the WiFi Update Service during the installation process. If an installation failure occurs, the corresponding installer component shall provide the individual ECU deployment package status code associated with the failed component. The WiFi Update Service shall collect and maintain the installation status and ECU deployment package status codes received from the installer components. The WiFi Update Service shall provide the installation result and failure status information to SWMC.

**路徑 A（語料 v2）前 5 候選**：

1. `4907606` — 章 **4.10.5** Deployment Flow — 分 **0.275**
   > 5. The installers then notify the OTA client of their update status, in the event of a failure they also provide individual ECU DP status codes.

2. `4907690` — 章 **4.12.2** Report Persistency — 分 **0.258**
   > In the event of an ECU reflash failure fault for any reason, error flags shall be reported back to the OTA server indicating the cause of the failure. This shall include the deployment package status code as well as any ECU fault codes and a CAN communication log that are a result of the failed operation.

3. `4907306` — 章 **4.4** OTA Client Architecture — 分 **0.189**
   > Installers are responsible for deployment of specific software component types and for hand off to update agents or platform installation mechanisms relevant for that component type. Installers are responsible for retrieving individual software versions of all managed components of the relevant type, as well as implementing the specific communications protocol (CAN, LIN, etc) with the component or…

4. `4907342` — 章 **4.4.2** OTA Client Configuration options — 分 **0.176**
   > OTA client shall abstract the installer components of the deployment manager such that the specific installation method can be either, differential update, full image update, or read and differential apply depending on the ECU and vehicle configuration.

5. `4907447` — 章 **4.7.2** OTA client Flows — 分 **0.175**
   > At the end of any flow, the OTA client shall send a report as to the status (success or failure) of the flow. See Report Persistency for specific requirements regarding reporting.


---

#### 23. `SWE1-FOTA-147` — Start Installation Only in IGN_OFF Power Mode

- Heading：`SWE1-FOTA-137` Deployment flow｜Sub Cat：Service｜Source：`SYS-RA-FOTA-250`｜分層：**6**

**Requirement Description 全文**：

> The WiFi Update Service/USB Update Service shall read the $PowerMode$ vehicle property through CarProperty Manager during installation precondition evaluation. The WiFi Update Service/USB Update Service shall permit installation start only when $PowerMode$ = [IGN_OFF].

**路徑 A（語料 v2）前 5 候選**：

1. `4907807` — 章 **6** TBM Algorithm Requirements — 分 **0.314**
   > During $PowerMode$ = [IGN_LK]

2. `4907801` — 章 **6** TBM Algorithm Requirements — 分 **0.274**
   > During $PowerMode$ = [IGN_OFF_ACC OR IGN_RUN OR IGN_START]

3. `4907628` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.271**
   > Installation process shall begin only if the ignition position is OFF ($PowerMode$ = [IGN_OFF]).

4. `4907810` — 章 **6** TBM Algorithm Requirements — 分 **0.248**
   > TBM shall start the FOTA update process only after the ignition has transitioned to $PowerMode$ = [IGN_LK]

5. `4907248` — 章 **2** Common Reflash Requirements — 分 **0.213**
   > For both USB and FOTA software updates, the HU shall permit only update packages to be downloaded which are intended for the HU hardware variant.


---

#### 24. `SWE1-FOTA-297` — Digital Signature and Transport Security Verification

- Heading：`SWE1-FOTA-291` Bearer selection:｜Sub Cat：Service｜Source：`SYS-RA-FOTA-352`｜分層：**4.8**

**Requirement Description 全文**：

> SWMC shall provide the downloaded deployment package to WiFiUpdateService. WiFiUpdateService shall use SWDLSecureLib to verify the digital signature and integrity of the deployment package. OTA update processing shall continue only after successful security verification, and no mechanism shall be provided to bypass or disable digital signature verification or transport security.

**路徑 A（語料 v2）前 5 候選**：

1. `4907494` — 章 **4.8** Security — 分 **0.551**
   > OTA client SHALL NOT implement any backdoor to bypass, disable, or circumvent the digital signature verification and transport security

2. `4907604` — 章 **4.10.5** Deployment Flow — 分 **0.389**
   > 3. Deployment package signature verification is done to verify authenticity of the package.

3. `4907519` — 章 **4.8.3** Deployment Package Security — 分 **0.376**
   > The OTA client shall support interaction with signature verification systems/libraries provided by FCA for deployment package signature verification.

4. `4907514` — 章 **4.8.3** Deployment Package Security — 分 **0.215**
   > The OTA client shall verify integrity of the deployment package once it is received from the server, immediately post download.

5. `4907483` — 章 **4.7.3.2** Silent Updates — 分 **0.209**
   > 2. After the deployment package is downloaded, its deployment shall start immediately.


---

#### 25. `SWE1-FOTA-128` — Parse Download Descriptor XML and Extract Deployment Parameters

- Heading：`SWE1-FOTA-127` Download Descriptor Format｜Sub Cat：Service｜Source：`SYS-RA-FOTA-181`｜分層：**4.13.4.1**

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

#### 26. `SWE1-FOTA-126` — Support Remote Configuration of OTA Flow Parameters

- Heading：`SWE1-FOTA-125` Appendix B Configurable Parameters｜Sub Cat：Service｜Source：`SYS-RA-FOTA-161`｜分層：**4.13.4**

**Requirement Description 全文**：

> The SWMC shall support configurable parameters used to control OTA workflow behavior. The SWMC shall support receiving updated parameter values from the OTA server. The SWMC shall ensure that supported parameter values remain configurable via the OTA server, including when a proprietary communication protocol is used. The SWMC shall apply the received parameter values to the corresponding OTA workflow behavior.

**路徑 A（語料 v2）前 5 候選**：

1. `4907742` — 章 **4.13.4** FCA Specific Tree structure (DDF) — 分 **0.221**
   > The specific device description framework format should be defined by the OTA server supporting the solution and the client shall reflect the nodes in the DM tree of the OTA client. FCA specific server configurable nodes and commands are defined in Appendix B and C. The specific values listed in the appendices are targeted for OMA-DM solution implementation. If using a proprietary protocol, the sa…

2. `4907459` — 章 **4.7.3** Main Update Configuration Options — 分 **0.186**
   > Wi-Fi only parameter: Set by the OTA server and passed to the OTA client, this parameter determines whether large downloads shall only proceed only vehicle has an active Wi-Fi connection or the ECU is connected via tethered phone.

3. `4907765` — 章 **4.13.4.2** Appendix B Configurable Parameters — 分 **0.165**
   > The OTA Client MAY support the following configurable parameters in its flows; The OTA client MAY support modification of these parameters via the OTA server. If a proprietary protocol is used these values SHALL still be server configurable. Table B-1: DM Tree Interval Descriptions Interval Description Default Value RecoveryPollingInterval Amount of time, in minutes, after an unsuccessful poll. If…

4. `4907365` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.161**
   > The OTA client shall poll the OTA server periodically, when backchannel is available, to ensure vehicle is up to date according to a configurable interval for each vehicle.

5. `4907355` — 章 **4.5.1** OTA Communication Protocols — 分 **0.132**
   > The OTA client is RECOMMENDED to use the open communication protocols defined in Table 4-3 to communicate with the server solution interface. HTTP and TLS protocols are REQUIRED if a proprietary communication protocol is used in place of OMA-DM. Table 4-3: Communication Protocols Originator Destination Protocol Specification Version OTA Client DM Server OMA DM 1.2.1 OMA-TS-DM-Protocol-V1_2-2006042…


---

#### 27. `SWE1-FOTA-279` — Open Communication Protocol Support

- Heading：`SWE1-FOTA-278` User initiated sessions｜Sub Cat：Service｜Source：`SYS-RA-FOTA-409`｜分層：**4.5.1**

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

#### 28. `SWE1-FOTA-376` — Update Agent Self-Update Capability

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-320`｜分層：**4.4**

**Requirement Description 全文**：

> * The Redbend SWMC shall support the ability to update its own software components (Update Agent) through the OTA update mechanism.

**路徑 A（語料 v2）前 5 候選**：

1. `4907309` — 章 **4.4** OTA Client Architecture — 分 **0.336**
   > The Update Agent has the following components:

2. `4907526` — 章 **4.9.1** Update Agent Requirements — 分 **0.225**
   > Update Agent shall have a recovery mechanism in the event of a power failure, communications loss, or other event which interrupts the update.

3. `4907530` — 章 **4.9.1** Update Agent Requirements — 分 **0.214**
   > Update Agent shall support self-updating of the Update Agent itself.

4. `4907867` — 章 **8.3** User Initiated Updates — 分 **0.164**
   > NAV shall provide capability for the user to download an available Map update through the HMI.

5. `4907341` — 章 **4.4.2** OTA Client Configuration options — 分 **0.152**
   > OTA client shall support handling of deployment packages regardless of transport mechanism.


---

#### 29. `SWE1-FOTA-375` — Deterministic Software Image Installation

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-319`｜分層：**4.9.1**

**Requirement Description 全文**：

> The WIFI update service shall ensure that the installed software image for a given target version is identical to the reference deployment image provided by the OTA server, so that the updated unit is equivalent to a freshly provisioned unit for the same target version.

**路徑 A（語料 v2）前 5 候選**：

1. `4907534` — 章 **4.9.1** Update Agent Requirements — 分 **0.534**
   > For image updates, the UA shall generate a bit-identical target version flash image on the updated unit, such that an updated unit is bit-identical to a new unit generated with the same target version.

2. `4907532` — 章 **4.9.1** Update Agent Requirements — 分 **0.376**
   > For file system updates, the UA shall generate a file structure on the updated ECU that is identical to the target file system used to generate the update, so that a new unit factory flashed with the target version would have an identical file structure to unit that was updated to that target version.

3. `4907517` — 章 **4.8.3** Deployment Package Security — 分 **0.282**
   > For differential updates, the OTA client shall ensure the source version of the update is identical to the version on the target ECU/HU. For a compound firmware deployment package that holds differential updates for multiple elements, OTA client shall ensure this for every differential update in the package.

4. `4907533` — 章 **4.9.1** Update Agent Requirements — 分 **0.230**
   > For file system updates, like updating the HU filesystem, the UA shall generate file system attributes and permissions (date, access and ownership) on the updated ECU that are identical to the attributes on the target file system used to generate the update, such that the file attributes and permissions on an updated unit are identical to a new unit manufactured with the same file system.

5. `4907646` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.225**
   > As long as the head unit has physical memory space, it shall download the most up to date firmware version available even if the previous version has not been installed.


---

#### 30. `SWE1-FOTA-366` — FOTA Update Availability Check

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-299`｜分層：**4.10.1**

**Requirement Description 全文**：

> * The WiFiUpdateService shall receive server-initiated OTA session requests from the TC client and forward the request to the SWMC. *The SWMC shall check the OTA server for an available FOTA update upon receiving a session request from the WiFiUpdateService.

**路徑 A（語料 v2）前 5 候選**：

1. `4907559` — 章 **4.10.1** Self Registration Flow — 分 **0.299**
   > 1. The OTA client runs the server-initiated session, client-initiated session or user-initiated session.

2. `4907572` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.276**
   > FOTA client shall check the server for an available FOTA update on receiving callback message from TC.

3. `4907500` — 章 **4.8.1** Communication Security — 分 **0.256**
   > OTA client shall authenticate the server upon initiation of a session.

4. `4907567` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.232**
   > Server initiated session - Communication between FOTA Client &amp; TC

5. `4907574` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.226**
   > The server-initiated session flow is as follows:

