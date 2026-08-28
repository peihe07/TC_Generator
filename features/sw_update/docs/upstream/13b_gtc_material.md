# 上繳材料 13b —— GT-C 反向樣本材料（50 個 CFTS 物件）

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/14_reverse_sample.md` §五 T27b
- 依據：**R-SU17 v2(d)**（GT-C：CFTS 側驅動之反向樣本）
- 母包：`docs/upstream/13_reverse_sample.md`

> **執行層不裁定有無對應。** 分析層逐一反向裁定「037 中有無列對應之」；
> 裁定結果入 `GROUND_TRUTH.md` 之 GT-C 節。
>
> 判斷之二種結果須分開記：
> **(甲) 037 有列對應而路徑 A 未把它排進前 5** —— 路徑 A 之缺口；
> **(乙) 037 無列對應** —— 屬 R-SU3 之範圍事實（規格有而 037 未納入），**非缺陷**。

---


## T27b —— GT-C 反向樣本材料（CFTS 側驅動）

- 母體：**45 個未觸及且可測之章**（R-SU17 v2 §(c) 之更正值），共 371 個需求物件
- 每章抽 1 個；**MOTA 一族（8、8.1、8.2、8.3、8.4）每章抽 2 個**（R-SU17 v2(d)「必須納入本批」）
- 取樣碼：`random.Random(271).sample(該章物件, n)`
- 本批 **50 個物件**，涵蓋 **45 / 45** 章

- **反向分數**：對每個 CFTS 物件，計其與 037 全 311 列 `Requirement Description` 之 TF-IDF cosine，取最高之 3 列。**與路徑 A 同一計分函式**，故「路徑 A 看不看得見此物件」可由此讀出。

> **執行層不裁定有無對應。** 分析層逐一反向裁定「037 中有無列對應之」；裁定結果入 `GROUND_TRUTH.md` 之 GT-C 節。

### 取樣清單

| # | 章 | 標題 | ObjectID | 該章物件數 | 最高反向分 |
|---:|---|---|---|---:|---:|
| 1 | **2** | Common Reflash Requirements | `4907258` | 16 | 0.302 |
| 2 | **4.4** | OTA Client Architecture | `4907311` | 22 | 0.255 |
| 3 | **4.4.2** | OTA Client Configuration options | `4907340` | 6 | 0.435 |
| 4 | **4.4.3** | Operating Environment | `4907350` | 8 | 0.103 |
| 5 | **4.5.1** | OTA Communication Protocols | `4907355` | 1 | 0.520 |
| 6 | **4.5.2** | User initiated sessions | `4907360` | 3 | 0.248 |
| 7 | **4.5.3** | Vehicle initiated sessions | `4907368` | 5 | 0.412 |
| 8 | **4.5.4** | OTA server initiated sessions | `4907370` | 1 | 0.553 |
| 9 | **4.5.4.1** | SMS/MQTT Push Support | `4907373` | 10 | 0.189 |
| 10 | **4.5.5** | Bus communications | `4907386` | 8 | 0.352 |
| 11 | **4.6** | OTA download via Wi-Fi | `4907399` | 5 | 0.246 |
| 12 | **4.6.2** | Non-Critical Updates | `4907414` | 2 | 0.444 |
| 13 | **4.6.3** | Software Download via Wi-Fi | `4907430` | 17 | 0.364 |
| 14 | **4.7** | OTA Client Application | `4907435` | 1 | 0.268 |
| 15 | **4.7.2** | OTA client Flows | `4907444` | 4 | 0.217 |
| 16 | **4.7.3.1** | Critical Updates | `4907472` | 8 | 0.194 |
| 17 | **4.7.3.3** | Regular Updates | `4907489` | 1 | 0.202 |
| 18 | **4.8** | Security | `4907493` | 7 | 0.000 |
| 19 | **4.8.1** | Communication Security | `4907503` | 8 | 0.560 |
| 20 | **4.9.1** | Update Agent Requirements | `4907528` | 16 | 0.258 |
| 21 | **4.10** | Session Flows | `4907554` | 3 | 0.401 |
| 22 | **4.10.1** | Self Registration Flow | `4907563` | 8 | 0.139 |
| 23 | **4.10.2** | Server-Initiated Session Flow | `4907565` | 13 | 0.373 |
| 24 | **4.10.4** | User-Initiated Session Flow | `4907597` | 4 | 0.121 |
| 25 | **4.10.5** | Deployment Flow | `4907603` | 9 | 0.184 |
| 26 | **4.10.5.1** | Installation and Download Condit | `4907611` | 41 | 0.581 |
| 27 | **4.11** | User Experience (UX)/HMI | `4907660` | 12 | 0.588 |
| 28 | **4.13.1** | SCOMO Support | `4907702` | 8 | 0.129 |
| 29 | **4.13.4** | FCA Specific Tree structure (DDF | `4907742` | 1 | 0.221 |
| 30 | **4.13.4.1** | Appendix A Download Descriptor F | `4907744` | 1 | 0.568 |
| 31 | **4.13.4.2** | Appendix B Configurable Paramete | `4907765` | 1 | 0.192 |
| 32 | **4.13.4.3** | Appendix C OTA Commands | `4907769` | 1 | 0.160 |
| 33 | **5** | TBM FOTA Reflash Requirements | `4907780` | 22 | 0.533 |
| 34 | **6** | TBM Algorithm Requirements | `4907814` | 14 | 0.159 |
| 35 | **7** | Firmware Over-the-air Updates (F | `4907823` | 8 | 0.117 |
| 36 | **7.1** | Critical Updates | `4907828` | 8 | 0.340 |
| 37 | **8** | Maps Over-the-air Updates (MOTA) | `4907839` | 3 | 0.167 |
| 38 | **8** | Maps Over-the-air Updates (MOTA) | `4907837` | 3 | 0.210 |
| 39 | **8.1** | Non-Critical Updates | `4907849` | 22 | 0.177 |
| 40 | **8.1** | Non-Critical Updates | `4907861` | 22 | 0.402 |
| 41 | **8.2** | Route Planning Updates | `4907864` | 2 | 0.189 |
| 42 | **8.2** | Route Planning Updates | `4907865` | 2 | 0.229 |
| 43 | **8.3** | User Initiated Updates | `4907868` | 4 | 0.222 |
| 44 | **8.3** | User Initiated Updates | `4907869` | 4 | 0.160 |
| 45 | **8.4** | MOTA Client Initiated Updates | `4907874` | 6 | 0.272 |
| 46 | **8.4** | MOTA Client Initiated Updates | `4907873` | 6 | 0.208 |
| 47 | **9.1** | Pre-Installation | `4907894` | 16 | 0.472 |
| 48 | **9.2** | Installation Progress | `4907900` | 7 | 0.789 |
| 49 | **9.3** | Post-Installation | `4907910` | 5 | 0.226 |
| 50 | **9.4.1** | Pre-Installation | `4907915` | 3 | 0.268 |

最高反向分之分布：中位數 **0.248**、最低 0.000、最高 0.789。

**MOTA 一族（10 個物件）之最高反向分**：中位數 **0.210**、最低 0.160、最高 0.402 —— 與全批中位數 0.248 之比較見上繳包 §自評。


---

## 逐物件材料


---

### 1. `4907258` — 章 **2** Common Reflash Requirements

**物件全文**（逐字）：

> When two or more different types of FOTA updates are available for installation at the same time, the HU shall honor the FOTA updates based on priority as below.1.FOTA Rest of the Vehicle updates2.HU FOTA3.TBM FOTA4. Maps over-the-air updates

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-217` — Prioritize FOTA Updates Based on Defined Update Type Hierarchy — 分 **0.302**
   > The Arbiter Service shall detect the availability of multiple FOTA update types including Rest of Vehicle FOTA, HU FOTA, TBM FOTA, and Map OTA updates. When two or more update types are available simultaneously, the Arbiter Service shall determine update execution priority using the following order:…

2. `SWE1-FOTA-123` — Clear TBM FOTA UI on No Updates Available — 分 **0.158**
   > The TBM Update Service shall retrieve $TBMUpdate$ using the TBM FW Service and detect when the value indicates No_Updates_Available. Upon detecting$TBMUpdate$ = [No_Updates_Available], the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall clear all active TBM FOTA-related pop-…

3. `SWE1-FOTA-112` — Display TBM Update Available Pop-up with Metadata — 分 **0.140**
   > The TBM Update Service shall retrieve $TBM_Update$ using the TBM FW Service and detect when the value indicates Update_Available. The TBM Update Service shall retrieve update metadata, including estimated installation time and “What’s New” information, via the TBM FW Service. If $TBM_Update$ = [Upda…


---

### 2. `4907311` — 章 **4.4** OTA Client Architecture

**物件全文**（逐字）：

> Flash driver. This component provides drivers to read and write flash memory. If the file system update is applicable it may contain a file system driver as well. Access to this component should be abstracted such that it is possible to use the update agent on multiple platforms and operating systems.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-257` — Abstract Storage Interface for Deployment Package — 分 **0.255**
   > SWMC shall provide the downloaded deployment package to WiFiUpdateService. WiFiUpdateService shall store the deployment package on the host module through the abstract file system/flash interface, independent of the operating system and flash driver.

2. `SWE1-FOTA-270` — Platform-Independent File System Update Support — 分 **0.165**
   > The Update Engine shall invoke the Redbend Update Agent (RBUA) to perform file-system updates. The Redbend Update Agent(RBUA) shall perform the file-system update independently of any high-level operating system.

3. `SWE1-FOTA-212` — Ensure Portability of HMI Architecture Across Frameworks and Operating — 分 **0.163**
   > The SW Update HMI shall be implemented using an architecture that supports portability across multiple HMI frameworks and operating systems. The SW Update HMI shall avoid dependencies on platform-specific components that restrict portability. The SW Update HMI shall use standardized interfaces and a…


---

### 3. `4907340` — 章 **4.4.2** OTA Client Configuration options

**物件全文**（逐字）：

> In the event that the OTA client components are on multiple host systems (tethered phone for example), common communications interfaces shall be defined in order to communicate between components and should be exposed to FCA.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-201` — Support Transport-Agnostic Handling of Deployment Packages — 分 **0.435**
   > The SWMC shall support communication between OTA client components distributed across multiple host systems through defined common communication interfaces. The SWMC shall exchange OTA session information, deployment package status, workflow events, and control messages through standardized communic…

2. `SWE1-FOTA-212` — Ensure Portability of HMI Architecture Across Frameworks and Operating — 分 **0.180**
   > The SW Update HMI shall be implemented using an architecture that supports portability across multiple HMI frameworks and operating systems. The SW Update HMI shall avoid dependencies on platform-specific components that restrict portability. The SW Update HMI shall use standardized interfaces and a…

3. `SWE1-FOTA-328` — Internal Network Interruption Recovery — 分 **0.162**
   > The SWMC shall resume the interrupted download upon receiving a data access resume or tethered phone connection event after the internal network interruption is cleared.


---

### 4. `4907350` — 章 **4.4.3** Operating Environment

**物件全文**（逐字）：

> Vehicle specific information retrieval shall be abstracted such that multiple vehicle architectures may be supported.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-253` — Multi-Component Software Management using SCOMO — 分 **0.103**
   > SWMC shall support the management of multiple software components using the SCOMO specification. SWMC shall provide the deployment package information to WiFiUpdateService. WiFiUpdateService shall process the deployment package and invoke the appropriate installers based on the update type.

2. `SWE1-FOTA-084` — Prioritize FOTA Update When Multiple Update Methods Have Same Version — 分 **0.103**
   > The SWMC shall provide the available FOTA package version information to the WiFi Update Service from Download Descriptor(DD). The USB package Download Descriptor shall provide the available USB update package version information to the WiFi Update Service. The WiFi Update Service shall forward the …

3. `SWE1-FOTA-082` — Prioritize FOTA Update When Multiple Update Methods Have Same Version — 分 **0.093**
   > The WiFi Update Service shall provide available FOTA package version information to the Arbiter Service. The USB Update Service shall provide available USB package version information to the Arbiter Service. The Arbiter Service shall compare the software version information of update packages availa…


---

### 5. `4907355` — 章 **4.5.1** OTA Communication Protocols

**物件全文**（逐字）：

> The OTA client is RECOMMENDED to use the open communication protocols defined in Table 4-3 to communicate with the server solution interface. HTTP and TLS protocols are REQUIRED if a proprietary communication protocol is used in place of OMA-DM. Table 4-3: Communication Protocols Originator Destination Protocol Specification Version OTA Client DM Server OMA DM 1.2.1 OMA-TS-DM-Protocol-V1_2-20060424-C OTA Client Download Server OMA DL 1.0 OMA-TS-DLOTA-V2_0_1-20110502-A OTA Client All server components HTTP/HTTPS 1.1 RFC2616 OTA Client All server components TLS 1.2 TLS 1.2

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-279` — Open Communication Protocol Support — 分 **0.520**
   > SWMC shall support communication with the server interface using the configured open communication protocols. SWMC shall support HTTP and TLS protocols when a proprietary communication protocol is configured instead of OMA-DM.

2. `SWE1-FOTA-268` — Platform-Independent OMA-DM Communication Support — 分 **0.361**
   > SWMC shall communicate with the OTA Server using platform-independent OMA-DM compliant protocols. When a proprietary communication protocol is configured, SWMC shall support the platform-independent proprietary communication protocol for OTA communication.

3. `SWE1-FOTA-298` — Proprietary Communication Protocol Support — 分 **0.247**
   > SWMC shall support OTA communication using the configured proprietary communication protocol. SWMC shall interface only with the approved proprietary communication protocol implementation.


---

### 6. `4907360` — 章 **4.5.2** User initiated sessions

**物件全文**（逐字）：

> In the event that no update is available, the OTA client shall be able to inform the HMI (if existing) that the vehicle is up to date and that no updates are available.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-190` — Display No Update Available Status on HMI — 分 **0.248**
   > The SWMC shall provide the update availability check result to the WiFi Update Service after OTA server communication is completed. When SWMC reports that no software update is available, the WiFi Update Service shall notify the SW Update HMI. The SW Update HMI shall display a message indicating tha…

2. `SWE1-FOTA-213` — Update HMI with OTA Download Progress — 分 **0.181**
   > The WiFi Update Service shall receive OTA package download progress status from SWMC and shall provide the download progress updates to the SW Update HMI. The SW Update HMI shall display the current OTA package download progress, including percentage or status indication, when the HMI is available.

3. `SWE1-FOTA-123` — Clear TBM FOTA UI on No Updates Available — 分 **0.156**
   > The TBM Update Service shall retrieve $TBMUpdate$ using the TBM FW Service and detect when the value indicates No_Updates_Available. Upon detecting$TBMUpdate$ = [No_Updates_Available], the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall clear all active TBM FOTA-related pop-…


---

### 7. `4907368` — 章 **4.5.3** Vehicle initiated sessions

**物件全文**（逐字）：

> Detection of ECU configuration changes, such as detection of manual diagnostic reflash or component replacement by service technician SHALL trigger a vehicle initiated session. This trigger shall be handled with the same event based interface into the OTA client.01

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-250` — Trigger Vehicle Initiated Session on ECU Configuration Change — 分 **0.412**
   > The WiFi Update Service shall receive ECU configuration change events, including VIN change, proxy configuration update, manual diagnostic reflash detection, or component replacement notifications through the vehicle event interface. Upon receipt of a valid change event, the WiFi Update Service shal…

2. `SWE1-FOTA-248` — Receive Server-Initiated Session Trigger Through TC Interface — 分 **0.280**
   > The WiFi Update Service shall maintain a communication interface with the TC client and shall receive server-initiated update session trigger notifications forwarded from the OTA server through the TC communication channel, then notify the to start server initiated session.

3. `SWE1-FOTA-215` — Trigger TBM Update Check on Scheduled Event — 分 **0.270**
   > The TBM Update Service shall detect the scheduled update-check trigger for TBM FOTA. Upon trigger, the TBM Update Service shall set $HUFOTACheck$ = [Check for updates] and transmit the signal to TBM through TBM FW Service.


---

### 8. `4907370` — 章 **4.5.4** OTA server initiated sessions

**物件全文**（逐字）：

> OTA client shall support an event interface in order to receive server initiated sessions.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-272` — Vehicle Event Interface Support — 分 **0.553**
   > SWMC shall support event interface to receive server-initiated session requests from the Server.

2. `SWE1-FOTA-277` — Server-Initiated Session Event Interface — 分 **0.391**
   > SWMC shall receive server-initiated session events from the Server through the event interface. SWMC shall notify WiFiUpdateService of the received server-initiated session to initiate the update

3. `SWE1-FOTA-369` — Server-Initiated Flow Alignment with Vehicle-Initiated Flow — 分 **0.351**
   > * The WiFiUpdateService shall receive server-initiated OTA session requests from the TC client and forward the request to the SWMC. * The SWMC shall execute server-initiated OTA update sessions using the same workflow as the vehicle-initiated OTA update flow after successful session initiation.


---

### 9. `4907373` — 章 **4.5.4.1** SMS/MQTT Push Support

**物件全文**（逐字）：

> The Head Unit shall be able to receive the SMS and identify it as a FOTA request and hand it off to the FOTA client

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-366` — FOTA Update Availability Check — 分 **0.189**
   > * The WiFiUpdateService shall receive server-initiated OTA session requests from the TC client and forward the request to the SWMC. *The SWMC shall check the OTA server for an available FOTA update upon receiving a session request from the WiFiUpdateService.

2. `SWE1-FOTA-365` — Server-Initiated Session Handling from TC — 分 **0.162**
   > The WiFiUpdateService shall receive server-initiated OTA session requests from the TC client and forward the session request to the SWMC for execution.

3. `SWE1-FOTA-367` — Server-Initiated Session Forwarding from TC — 分 **0.157**
   > * The WiFiUpdateService shall receive server-initiated OTA session requests from the TC client and forward the request to the SWMC. * The SWMC shall queue the received OTA update session request when it cannot be executed immediately.


---

### 10. `4907386` — 章 **4.5.5** Bus communications

**物件全文**（逐字）：

> It is RECOMMENDED that the specific physical layer bus communications stack implementation (CAN/Ethernet/LIN/etc) on the host ECU (HU, TBM, etc) be separated from the OTA client such that other utilities can use them.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-195` — Separate OTA Client from Physical Bus Communication Stack — 分 **0.352**
   > The SWMC and WiFi Update Service shall use generic communication interfaces provided through the platform abstraction layer for vehicle bus communication. The SWMC and WiFi Update Service shall not directly depend on specific physical bus communication stack implementations such as CAN, Ethernet, or…

2. `SWE1-FOTA-303` — Vehicle Information for Server Authentication — 分 **0.175**
   > WiFiUpdateService shall retrieve the required vehicle details through the Vehicle Integration Layer and provide them to SWMC. SWMC shall use the received vehicle details for application-layer authentication with the OTA Server.

3. `SWE1-FOTA-320` — Host System Disconnection Handling — 分 **0.101**
   > The WiFiUpdateService shall detect end-user physical disconnection of the host system (HU/TBM) during OTA server communication, flashing, or software component update and notify SWMC. The SWMC shall handle the OTA session based on the notification and report the update status to the WiFiUpdateServic…


---

### 11. `4907399` — 章 **4.6** OTA download via Wi-Fi

**物件全文**（逐字）：

> If there is an existing Wi-Fi network saved, and HU meets the precondition for download via Wi-Fi then HU shall attempt to download the software package via Wi-Fi network

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-039` — Provide Enable Wi-Fi Download Option on Wi-Fi Download Page — 分 **0.246**
   > The SW Update HMI shall provide a selectable option to enable software download via Wi-Fi when the user enters the software download via Wi-Fi page. The SW Update HMI shall allow the user to select the enable software download via Wi-Fi option from the software download via Wi-Fi page.

2. `SWE1-FOTA-011` — User Navigation to Wi-Fi Software Download — 分 **0.208**
   > The HMI shall navigate to the software download via Wi-Fi screen when the user selects the Wi-Fi software download entry from the Settings menu. The HMI shall provide navigation to the software download via Wi-Fi screen when the user selects the update pop-up notification. Upon user confirmation to …

3. `SWE1-FOTA-007` — Display Wi-Fi Download Pop-up for Non-Critical Update — 分 **0.204**
   > The WiFi Update Service shall retrieve saved Wi-Fi network information from WiFi Manager and determine whether a previously configured Wi-Fi network is available. The WiFi Update Service shall retrieve the software package classification from the metadata of the downloaded Deployment Descriptor (DD)…


---

### 12. `4907414` — 章 **4.6.2** Non-Critical Updates

**物件全文**（逐字）：

> If there is no Wi-Fi network saved, then HU shall display a pop – up on next $PowerMode$ = [IGN_OFF]. (Kindly see the triggering conditions)

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-066` — Display No Saved WiFi Network Pop-up on Next IGN_OFF — 分 **0.444**
   > The HMI shall receive no-saved-network status from the WiFi Manager when no Wi-Fi network is saved. Upon the next transition of $PowerMode$ t= [IGN_OFF] received through CarProperty Manager, the HMI shall display the pop-up .

2. `SWE1-FOTA-056` — Wi-Fi Download Pop-Up Trigger on IGN_OFF Without Saved Wi-Fi Network — 分 **0.187**
   > The WiFi Update Service shall determine the FOTA package classification using the software package metadata received in the Download Descriptor (DD) from SWMC. The WiFi Update Service shall monitor the vehicle power mode using the vehicle property $PowerMode$ through CarPropertyManager. The WiFi Upd…

3. `SWE1-FOTA-154` — Display Conditions Not Met With Specific Cancellation Reason — 分 **0.177**
   > The WiFi Update Service shall evaluate scheduled installation preconditions before initiating the scheduled installation process. The WiFi Update Service/USB Update Service shall monitor $PowerMode$, $IBS_SOC$, $IBS_SOC_ACCURACY$, and $OperationalModeSts$ using CarProperty Manager and CarPower Manag…


---

### 13. `4907430` — 章 **4.6.3** Software Download via Wi-Fi

**物件全文**（逐字）：

> User shall be able to refresh the list of Wi-Fi networks

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-051` — Refresh Available Wi-Fi Network List — 分 **0.364**
   > The HMI shall provide a refresh option for the available Wi-Fi network list. The HMI shall detect the user selection of the refresh option and request WiFi Manager to perform a new Wi-Fi scan. After completion of the Wi-Fi scan, WiFi Manager shall provide the updated available Wi-Fi network list to …

2. `SWE1-FOTA-044` — Display Password-Protected Wi-Fi Networks in Range — 分 **0.277**
   > The WiFi Update Service shall retrieve the list of available Wi-Fi networks from WiFi Manager after completion of a Wi-Fi scan operation. The WiFi Update Service shall identify password-protected Wi-Fi networks with the help of WiFi Manager from the available Wi-Fi network list based on the network …

3. `SWE1-FOTA-062` — Prioritize Wi-Fi Network Selection by Signal Strength After Filtering — 分 **0.210**
   > The WiFi Manager shall maintain an exclusion list for Wi-Fi network selection. The WiFi Update Service shall use WiFiManager scan results to exclude Wi-Fi networks that are not within range from the available Wi-Fi network list. The WiFi Manager shall exclude Wi-Fi networks present in the exclusion …


---

### 14. `4907435` — 章 **4.7** OTA Client Application

**物件全文**（逐字）：

> The OTA client's primary use case is managing firmware components. Update flow types include Critical, Silent, and Regular that are defined in this section.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-131` — Support Server-Configured Update Types With Consistent User Experience — 分 **0.268**
   > The WiFi Update Service shall retrieve update type configuration from the OTA server for each update campaign using SWMC. The supported update types shall include regular, critical, and silent updates. The WiFi Update Service shall apply the update flow behavior according to the received update type…

2. `SWE1-FOTA-035` — Execute Regular Update with HMI Flow and Bearer Rules — 分 **0.138**
   > The WiFi Update Service shall identify update packages classified as Regular Update based on Download Descriptor (DD) metadata received through SWMC. For update packages classified as non-silent and non-critical, the WiFi Update Service shall execute the update session using the standard end-user in…

3. `SWE1-FOTA-286` — OTA Flow Status Reporting — 分 **0.122**
   > SWMC shall generate and send a status report upon completion of each session or update flow. SWMC shall include the execution result indicating success or failure of the completed flow operation.


---

### 15. `4907444` — 章 **4.7.2** OTA client Flows

**物件全文**（逐字）：

> The following OTA client flows SHALL be supported by the OTA client depending on Compliance field in the below table: Table 4-4: OTA client sessions Flow Compliance Description More Information Self-registration shall The OTA client shall register itself to the OTA server during the initial OTA session. Self Registration Flow Background session shall Upon receiving a shoulder tap informing of a background session or responding to a vehicle event, the OTA client establishes an OTA session to check for updates. If an update is available, an update session is initiated. This includes the OTA session that opens communication between the OTA server and the OTA client, and the download of a deployment package. Server-Initiated Session Flow (if applicable) Vehicle-Initiated Session Flow Deployment Package Download Flow Foreground session RECOMMENDED End-users/drivers can initiate an OTA session to check for updates via HMI or other user interaction. If an update is available, an update session is initiated. This includes the OTA session that opens communication between the OTA server and the OTA client, and the download of a deployment package. User-Initiated Session Flow (if applicable) Deployment Package Download Flow Deployment Session shall Software package deployment may be triggered as an immediate continuation of a download session or by a manual launch of the OTA client application. Deployment Flow Note: (only when applicable depending on type of Software Update) OTA client boot session RECOMMENDED When the OTA client is started, such as when the Head Unit boots, it can initiate an OTA session with the OTA server. Boot Flow

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-369` — Server-Initiated Flow Alignment with Vehicle-Initiated Flow — 分 **0.217**
   > * The WiFiUpdateService shall receive server-initiated OTA session requests from the TC client and forward the request to the SWMC. * The SWMC shall execute server-initiated OTA update sessions using the same workflow as the vehicle-initiated OTA update flow after successful session initiation.

2. `SWE1-FOTA-248` — Receive Server-Initiated Session Trigger Through TC Interface — 分 **0.210**
   > The WiFi Update Service shall maintain a communication interface with the TC client and shall receive server-initiated update session trigger notifications forwarded from the OTA server through the TC communication channel, then notify the to start server initiated session.

3. `SWE1-FOTA-277` — Server-Initiated Session Event Interface — 分 **0.207**
   > SWMC shall receive server-initiated session events from the Server through the event interface. SWMC shall notify WiFiUpdateService of the received server-initiated session to initiate the update


---

### 16. `4907472` — 章 **4.7.3.1** Critical Updates

**物件全文**（逐字）：

> Critical and non-critical updates shall be defined by the server

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-026` — Treat Server-Flagged Update Session as Critical — 分 **0.194**
   > The WiFi Update Service shall evaluate update session configuration and metadata received through SWMC from the downloaded Download Descriptor (DD). When the server command in the Download Descriptor (DD) indicates the update session as Critical Update, the WiFi Update Service shall classify the act…

2. `SWE1-FOTA-223` — Suspend Update HMI While Reverse Camera Is Active — 分 **0.190**
   > The SW Update HMI and WiFi Update Service logic shall preserve backup camera display priority and suppress non-safety-critical update overlays during a radio reflash event irrespective of update method, including USB Update, WiFi FOTA, and MOTA when equipped. When reverse gear is active, backup came…

3. `SWE1-FOTA-035` — Execute Regular Update with HMI Flow and Bearer Rules — 分 **0.177**
   > The WiFi Update Service shall identify update packages classified as Regular Update based on Download Descriptor (DD) metadata received through SWMC. For update packages classified as non-silent and non-critical, the WiFi Update Service shall execute the update session using the standard end-user in…


---

### 17. `4907489` — 章 **4.7.3.3** Regular Updates

**物件全文**（逐字）：

> A regular update includes any update that is not critical or silent. The OTA client shall follow all HMI requirements and flows for regular updates and not skip any user input. See [VP4-8.4 Refresh SR18 HMI Logic and Flow].

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-131` — Support Server-Configured Update Types With Consistent User Experience — 分 **0.202**
   > The WiFi Update Service shall retrieve update type configuration from the OTA server for each update campaign using SWMC. The supported update types shall include regular, critical, and silent updates. The WiFi Update Service shall apply the update flow behavior according to the received update type…

2. `SWE1-FOTA-244` — Align FOTA HMI Implementation with Defined HMI Logic and Flow — 分 **0.183**
   > The SW Update HMI shall implement the FOTA user interface in accordance with the defined HMI logic and flow specifications. The SW Update HMI shall ensure that the user interaction, navigation flow, and screen behavior are consistent with the approved HMI design specifications.

3. `SWE1-FOTA-035` — Execute Regular Update with HMI Flow and Bearer Rules — 分 **0.175**
   > The WiFi Update Service shall identify update packages classified as Regular Update based on Download Descriptor (DD) metadata received through SWMC. For update packages classified as non-silent and non-critical, the WiFi Update Service shall execute the update session using the standard end-user in…


---

### 18. `4907493` — 章 **4.8** Security

**物件全文**（逐字）：

> See SD – SD.00080, and CS - CS.00167 for Wi-Fi Cybersecurity requirements

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-383` — Deployed Software Validation — 分 **0.000**
   > * For SOC, Redbend Update Agent shall verify the validity of the deployed software after installation to ensure that the software has been correctly and successfully applied. * For IOC,Tuner,GNSS,SXM installer agent shall verify the validity of the deployed software after installation to ensure that…

2. `SWE1-FOTA-382` — Pre-Update and post-update Differential Compatibility Verification — 分 **0.000**
   > * The WiFi Update service shall verify that the current firmware version of the target ECU matches the source firmware version specified in the differential update package before starting the update process. * The WiFi update service shall verify that the resulting firmware image after applying a di…

3. `SWE1-FOTA-381` — Differential Update Technology Support — 分 **0.000**
   > * The Redbend Update Agent shall support the use of the smallest approved differential update technology, as configured by FCA approval, in order to minimize data usage and update time.


---

### 19. `4907503` — 章 **4.8.1** Communication Security

**物件全文**（逐字）：

> It SHALL only respond to messages received from an authenticated source.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-304` — Authenticated Message Processing — 分 **0.560**
   > SWMC shall validate the authenticity of the message source before processing any received message. SWMC shall process and respond only to messages received from authenticated sources.

2. `SWE1-FOTA-310` — OMA-DM Message Integrity Verification — 分 **0.216**
   > SWMC shall perform integrity verification of received OMA-DM messages before processing them. SWMC shall reject messages that fail the integrity verification.

3. `SWE1-FOTA-083` — Select Update Source Based on Latest Software Version — 分 **0.129**
   > The SWMC shall provide the available FOTA package version information to the WiFi Update Service. The USB update pacakge shall provide the available USB update package version information to the WiFi Update Service. The WiFi Update Service shall forward the received update package version informatio…


---

### 20. `4907528` — 章 **4.9.1** Update Agent Requirements

**物件全文**（逐字）：

> Update Agent is RECOMMENDED to implement a failsafe for update interruptions, especially when using in-place differential updates.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-378` — Update Interruption Failsafe Mechanism — 分 **0.258**
   > The WifiUpdate service shall implement a failsafe mechanism to handle update interruptions to ensure the system can recover to a consistent state and installers also shall about to support for the recovery mechanism.

2. `SWE1-FOTA-381` — Differential Update Technology Support — 分 **0.165**
   > * The Redbend Update Agent shall support the use of the smallest approved differential update technology, as configured by FCA approval, in order to minimize data usage and update time.

3. `SWE1-FOTA-380` — Update Recovery Mechanism — 分 **0.140**
   > * The SW updater hall shall implement a recovery mechanism to resume or safely terminate IOC, GNSS, and Tuner updates in the event of power failure, communication loss, or any other interruption during the update process. * The Redbend Update Agent shall implement a recovery mechanism to resume or s…


---

### 21. `4907554` — 章 **4.10** Session Flows

**物件全文**（逐字）：

> If an interruption occurs during any of the steps before the download completes successfully, the OTA client shall save the state of the download, and shall retry to resume the download.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-331` — OTA Session Report Retry Handling — 分 **0.401**
   > The SWMC shall save the OTA session report when an interruption occurs before the report is successfully sent to and acknowledged by the OTA server, and shall resend the report when the interruption is resolved.

2. `SWE1-FOTA-360` — Download Interruption Recovery — 分 **0.394**
   > The SWMC shall detect interruptions occurring during any step of the download process before completion, shall save the current download state, and shall resume the download when the interruption condition is cleared.

3. `SWE1-FOTA-357` — Installation Interruption State Management — 分 **0.362**
   > * The Wifi Update service shall save the installation state when an interruption occurs before successful completion of the installation and shall resume the installation when the interruption condition is cleared. * The wifiupdate service shall report the installation status, including success, fai…


---

### 22. `4907563` — 章 **4.10.1** Self Registration Flow

**物件全文**（逐字）：

> 5. The OTA server will validate the domain name and PIN code and will use them and the vehicle identification information to register the vehicle in the server in the correct domain/account.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-372` — Dependency-Based Installation Ordering — 分 **0.139**
   > * The WiFiUpdateService shall validate the software component dependencies defined in the update metadata before initiating the installation. * The WiFiUpdateService shall ensure that software components are installed in the correct order based on their defined dependencies.

2. `SWE1-FOTA-303` — Vehicle Information for Server Authentication — 分 **0.138**
   > WiFiUpdateService shall retrieve the required vehicle details through the Vehicle Integration Layer and provide them to SWMC. SWMC shall use the received vehicle details for application-layer authentication with the OTA Server.

3. `SWE1-FOTA-355` — Download Precondition Data Provision — 分 **0.115**
   > The WiFiUpdateService shall provide the vehicle and system data required by the SWMC to validate the download preconditions.


---

### 23. `4907565` — 章 **4.10.2** Server-Initiated Session Flow

**物件全文**（逐字）：

> Server-initiated sessions shall start automatically after the OTA server sends an NIA via SMS or MQTT to the OTA client.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-247` — Automatically Start Server-Initiated Update Session on NIA Reception — 分 **0.373**
   > The SWMC shall detect a valid New Installation Announcement (NIA) received from the OTA server through MQTT or SMS transport and shall automatically trigger a server-initiated OTA update session through the WiFi Update Service without requiring user interaction.

2. `SWE1-FOTA-369` — Server-Initiated Flow Alignment with Vehicle-Initiated Flow — 分 **0.262**
   > * The WiFiUpdateService shall receive server-initiated OTA session requests from the TC client and forward the request to the SWMC. * The SWMC shall execute server-initiated OTA update sessions using the same workflow as the vehicle-initiated OTA update flow after successful session initiation.

3. `SWE1-FOTA-248` — Receive Server-Initiated Session Trigger Through TC Interface — 分 **0.212**
   > The WiFi Update Service shall maintain a communication interface with the TC client and shall receive server-initiated update session trigger notifications forwarded from the OTA server through the TC communication channel, then notify the to start server initiated session.


---

### 24. `4907597` — 章 **4.10.4** User-Initiated Session Flow

**物件全文**（逐字）：

> 2. Client checks pre-condition list and determines if it is able to proceed with the session. If not the user should be informed of this decision and the flow is ended.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-222` — Prioritize Software Update Over Map Update — 分 **0.121**
   > The Arbiter Service shall detect the simultaneous availability of software updates and map updates. When both software update and map update sessions are available at the same time, the Arbiter Service shall prioritize the software update session. The Arbiter Service shall defer or suppress map upda…

2. `SWE1-FOTA-051` — Refresh Available Wi-Fi Network List — 分 **0.111**
   > The HMI shall provide a refresh option for the available Wi-Fi network list. The HMI shall detect the user selection of the refresh option and request WiFi Manager to perform a new Wi-Fi scan. After completion of the Wi-Fi scan, WiFi Manager shall provide the updated available Wi-Fi network list to …

3. `SWE1-FOTA-354` — Download Acceptance Processing — 分 **0.108**
   > * The SWMC shall request download acceptance from the WiFiUpdateService after successfully downloading the Deployment Description (DD). * The WiFiUpdateService shall present the download acceptance request to the user through the HMI when all download preconditions are satisfied and shall provide th…


---

### 25. `4907603` — 章 **4.10.5** Deployment Flow

**物件全文**（逐字）：

> 2. The installation conditions are checked. If the conditions are not met, the end-user is informed about the problematic conditions and deployment is suspended until the conditions are met. The deployment proceeds as soon as the installation conditions are met.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-344` — Deployment Condition Validation and Notification — 分 **0.184**
   > * The SWMC shall evaluate the configured deployment conditions before deployment. If all conditions are satisfied, the SWMC shall continue the deployment; otherwise, the SWMC shall suspend the deployment and notify the WiFiUpdateService. * The WiFiUpdateService shall notify the end user of the deplo…

2. `SWE1-FOTA-154` — Display Conditions Not Met With Specific Cancellation Reason — 分 **0.183**
   > The WiFi Update Service shall evaluate scheduled installation preconditions before initiating the scheduled installation process. The WiFi Update Service/USB Update Service shall monitor $PowerMode$, $IBS_SOC$, $IBS_SOC_ACCURACY$, and $OperationalModeSts$ using CarProperty Manager and CarPower Manag…

3. `SWE1-FOTA-343` — Vehicle Condition Provision — 分 **0.157**
   > * The SWMC shall request the vehicle conditions specified in the deployment configuration file from the WiFiUpdateService. * The WiFiUpdateService shall provide the vehicle conditions specified in the deployment configuration file to the SWMC.


---

### 26. `4907611` — 章 **4.10.5.1** Installation and Download Conditions

**物件全文**（逐字）：

> The condition configuration file shall support a logical combination of multiple conditions and the specific values or value ranges shall be satisfied for the deployment to proceed.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-341` — Deployment Condition Evaluation — 分 **0.581**
   > The SWMC shall evaluate the logical combination of deployment conditions and verify that the configured values or value ranges are satisfied before proceeding with the deployment.

2. `SWE1-FOTA-345` — Vehicle Condition Provision for Download Control — 分 **0.234**
   > * The SWMC shall pause the deployment package download when one or more configured download conditions are not satisfied and shall resume the download when the conditions are satisfied. * The WiFiUpdateService shall provide the vehicle condition parameters required by the SWMC to evaluate the downlo…

3. `SWE1-FOTA-343` — Vehicle Condition Provision — 分 **0.210**
   > * The SWMC shall request the vehicle conditions specified in the deployment configuration file from the WiFiUpdateService. * The WiFiUpdateService shall provide the vehicle conditions specified in the deployment configuration file to the SWMC.


---

### 27. `4907660` — 章 **4.11** User Experience (UX)/HMI

**物件全文**（逐字）：

> After the download the OTA client shall display the approved for consumer view release notes information in the DD file along with any other information or links about the update. The end user shall be able to tap any links and interact with this information during the opt in and download screens.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-133` — Display Release Notes and Interactive Links from DD — 分 **0.588**
   > The SWMC shall parse the Download Descriptor after completion of the update download and extract consumer-approved release notes information, update-related information, and associated links. The SWMC shall provide the extracted release notes information and associated links to the SW Update HMI. Th…

2. `SWE1-FOTA-203` — Display Download Descriptor Information on HMI — 分 **0.166**
   > The SWMC shall provide Download Descriptor metadata to the WiFi Update Service after Download Descriptor from OTA server. The WiFi Update Service shall provide available update information from the Download Descriptor metadata to the SW Update HMI. The SW Update HMI shall display available update in…

3. `SWE1-FOTA-233` — Display Estimated Time for TBM Software Update — 分 **0.140**
   > The TBM Update Service shall receive the download descriptor (DD) file from SWMC and shall extract the estimated TBM software update time information from the DD metadata received from the GSDP. The TBM Update Service shall provide the extracted estimated TBM software update time information to the …


---

### 28. `4907702` — 章 **4.13.1** SCOMO Support

**物件全文**（逐字）：

> The update of firmware shall be fully failsafe, so that interrupt conditions defined in section power outage at any time during the update does not affect the final outcome.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-358` — Update Status Reporting to SWMC — 分 **0.129**
   > * The WifiUpdateservice shall report the software update status to the SWMC. * The SWMC shall send the final software update result to the OTA server upon completion of the update process.

2. `SWE1-FOTA-382` — Pre-Update and post-update Differential Compatibility Verification — 分 **0.109**
   > * The WiFi Update service shall verify that the current firmware version of the target ECU matches the source firmware version specified in the differential update package before starting the update process. * The WiFi update service shall verify that the resulting firmware image after applying a di…

3. `SWE1-FOTA-313` — Software Update Error Handling Coordination — 分 **0.104**
   > * The WiFiUpdateService shall coordinate the handling of the error conditions defined in System Requirements 4907672, 4907671, 4907670, 4907669, 4907668, and 4907667 by interacting with SWMC and the appropriate installer component during the software update process. * The SWMC shall handle the error…


---

### 29. `4907742` — 章 **4.13.4** FCA Specific Tree structure (DDF)

**物件全文**（逐字）：

> The specific device description framework format should be defined by the OTA server supporting the solution and the client shall reflect the nodes in the DM tree of the OTA client. FCA specific server configurable nodes and commands are defined in Appendix B and C. The specific values listed in the appendices are targeted for OMA-DM solution implementation. If using a proprietary protocol, the same values shall be configurable via another method.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-126` — Support Remote Configuration of OTA Flow Parameters — 分 **0.221**
   > The SWMC shall support configurable parameters used to control OTA workflow behavior. The SWMC shall support receiving updated parameter values from the OTA server. The SWMC shall ensure that supported parameter values remain configurable via the OTA server, including when a proprietary communicatio…

2. `SWE1-FOTA-298` — Proprietary Communication Protocol Support — 分 **0.158**
   > SWMC shall support OTA communication using the configured proprietary communication protocol. SWMC shall interface only with the approved proprietary communication protocol implementation.

3. `SWE1-FOTA-268` — Platform-Independent OMA-DM Communication Support — 分 **0.150**
   > SWMC shall communicate with the OTA Server using platform-independent OMA-DM compliant protocols. When a proprietary communication protocol is configured, SWMC shall support the platform-independent proprietary communication protocol for OTA communication.


---

### 30. `4907744` — 章 **4.13.4.1** Appendix A Download Descriptor Format

**物件全文**（逐字）：

> The Download Descriptor (DD) describes the deployment package that the OTA server sends to the vehicle. The DD is a simple XML file that contains the parameters listed in the following table. Table A-1: Download Descriptor Parameters Name Description installParam An installation parameter associated with the download package. It contains an embedded XML with the &lt;installerType&gt; tag, which contains a command-seperated list of installer types which are going to be updated. The embedded XML is wrapped with &lt;![CDATA[]]&gt; element. DDVersion Attribute defining the version of the Download Descriptor description A short textual description of the download package. It shall be in the following format: &lt;Name1&gt;,&lt;Version1&gt;,&lt;Filename1&gt;;&lt;Name2&gt;,&lt;Version2&gt;,&lt;Filename2&gt;;…;&lt;NameX&gt;,&lt;VersionX&gt;,&lt;FilenameX&gt;;Settings Where: ∙ Name – Component Name which is about to be updated ∙ Version – Version of the component ∙ Filename – the update file name ∙ Settings – indicates that this package contains also settings information objectURI Contains a URL address that should be used to download the package. size The number of bytes to be downloaded from the objectURI. In other words it is the size of the download package in bytes. type The MIME media type of the download package vendor Information over the organization that provides the download package installNotifyURI The URL to which an Installation Status Report is to be sent, either in case of a successful completion of the download, or in case of a failure. infoURL A URL for further describing the download package message The Download Descriptor file should also contain a message tag which would contain a consumer description of what new additional changes the download package contains and what module of the car it would update. This message needs to be in multiple language where each language would have its own xml tag. Depending upon the current language of the HU appropriate message would be shown in local language. Supported languages will be same as HU for that market. Default language would be English US. The following is a DD example: &lt;?xml version='1.0'?&gt; &lt;media xmlns="Fhttp://www.openmobilealliance.org/xmlns/dd"&gt; &lt;installParam&gt;&gt;&lt;![CDATA[&lt;InstallerType&gt;9,11,12&lt;/InstallerType&gt;]]&gt;&lt;/installParam&gt; &lt;DDVersion&gt;1.0&lt;/DDVersion&gt; &lt;description&gt;PCM_CONFIG,1.0.0.0, PCM_CONFIG_1.0.0.0[-1,null].bin;&lt;/description&gt; &lt;objectURI&gt;http://localhost/folder/file.dp&lt;/objectURI&gt; &lt;size&gt;1234567&lt;/size&gt; &lt;type&gt;application/octet-stream&lt;/type&gt; &lt;vendor&gt;FCA&lt;/vendor&gt; &lt;installNotifyURI&gt; http://localhost:8080/InstallNotify&amp;lt;/installNotifyURI&amp;gt; &lt;infoURL&gt;Fhttp://localhost:8080/Info &lt;/infoURL&gt; &lt; message&gt; &lt;en-us&gt; This install would update the Head Unit software&lt;/&gt; &lt;fr-ca&gt; Cette installation serait de mettre à jour le logiciel de l'unité Chef &lt;/&gt; &lt;/message&gt; &lt;/media&gt;

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-128` — Parse Download Descriptor XML and Extract Deployment Parameters — 分 **0.568**
   > The SWMC shall parse the Download Descriptor provided with the update. The SWMC shall process the Download Descriptor as an XML file. The SWMC shall extract deployment package parameters and metadata from the Download Descriptor. The SWMC shall use the extracted parameters and metadata from below me…

2. `SWE1-FOTA-203` — Display Download Descriptor Information on HMI — 分 **0.160**
   > The SWMC shall provide Download Descriptor metadata to the WiFi Update Service after Download Descriptor from OTA server. The WiFi Update Service shall provide available update information from the Download Descriptor metadata to the SW Update HMI. The SW Update HMI shall display available update in…

3. `SWE1-FOTA-255` — SWMC Download Manager Integration — 分 **0.139**
   > SWMC shall reliably download the deployment package using the URL obtained from the Download Descriptor. Upon successful download, SWMC shall provide the deployment package to WiFiUpdateService for further OTA update processing.


---

### 31. `4907765` — 章 **4.13.4.2** Appendix B Configurable Parameters

**物件全文**（逐字）：

> The OTA Client MAY support the following configurable parameters in its flows; The OTA client MAY support modification of these parameters via the OTA server. If a proprietary protocol is used these values SHALL still be server configurable. Table B-1: DM Tree Interval Descriptions Interval Description Default Value RecoveryPollingInterval Amount of time, in minutes, after an unsuccessful poll. If set to 0, the PollingIntervalInHours value is used. This value should be smaller than PollingIntervalInHours. /ext/FCA/RecoveryPollingInterval 1440 (One day) PostponeMaxTimes Maximum number of times that an end-user can postpone an action. If set to 0, end-user postponing has no limit. /ext/FCA/PostponeMaxTimes 3 MaxNetRetries The number of additional times (one retry is always made) to try to reconnect following: • Socket read / write errors • TCP timeout: ° Host cannot be reached ° Connection refusal ° Unresolved address No retries are made following a fatal error /ext/FCA/MaxNetRetries 3

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-347` — Vehicle-Initiated Polling Interval Configuration — 分 **0.192**
   > The SWMC shall support a configurable polling interval for vehicle-initiated OTA update sessions with a default value of 24 hours.

2. `SWE1-FOTA-126` — Support Remote Configuration of OTA Flow Parameters — 分 **0.165**
   > The SWMC shall support configurable parameters used to control OTA workflow behavior. The SWMC shall support receiving updated parameter values from the OTA server. The SWMC shall ensure that supported parameter values remain configurable via the OTA server, including when a proprietary communicatio…

3. `SWE1-FOTA-315` — Socket Read/Write Error Handling — 分 **0.143**
   > The SWMC shall detect and handle socket read/write errors during OTA server communication, flashing, or software component update, and shall report the error status to WiFiUpdateService.


---

### 32. `4907769` — 章 **4.13.4.3** Appendix C OTA Commands

**物件全文**（逐字）：

> The OTA shall support configuration for the following commands from the OTA server to manage the DM Tree. If a proprietary protocol is used these commands shall be supported in some way. Table C-1: DM Tree Commands Use-Case Operation Commands Sent (and Additional Notes) SCOMO Update (any) The following commands MAY be sent at the start of any operation except for Get Inventory or Get Firmware Version: • REPLACE on ./Ext/FCA/WiFiOnly This is set to one of the following: ° 0: If the operation is set to download whether or not it is within Wi-Fi range ° 1: If the operation is set to download only within Wi-Fi range • REPLACE on ./Ext/FCA/CriticalUpdate This is set to one of the following: ° 0: If the operation is not critical (priority 10) ° 1: If the operation is critical (priority 8) • REPLACE on ./Ext/FCA/SilentInstall This is set to one of the following: ° 0: If the operation potentially includes end-user interaction ° 1: If the operation is set for silent update (no end-user interaction) • REPLACE on ./Ext/FCA/ReserveDownloadTime Set to HH:MM-HH:MM, indicating the start and end times for operation download activity. For example, 00:00-23:59 indicates all times. • REPLACE on ./Ext/FCA/UpdateDateTime Set to HH:MM-HH:MM, indicating the start and end times for operation update activity. For example, 00:00-23:59 indicates all times. • REPLACE on ./Ext/FCA/Registered Indicates if the vehicle is registered in the OTA server. This setting is not guaranteed to be up to date. This is set to one of the following: ° 0: Not registered ° 1: Registered • REPLACE on ./SCOMO/Ext/PollingIntervalInHours This is set to one of the following: ° 0: No polling ° &gt;= 1: Polling interval, in hours The server sends the information in the following nodes to the OTA server at the start of any OTA Session: • /DevInfo/Ext/FCA/DomainName • /DevInfo/Ext/FCA/DomainPIN Domain name and PIN. Sent in DM Protocol Package 1. • /DevInfo/Lang Set to a language tag, as described by OMA [RFC1766]. Language codes are defined by the ISO standard ISO639. • /DevInfo/Mod: The server model name. • /DevInfo/Man: The vehicle make. • /DevInfo/DevId: The VIN, usually the VIN. Registration • GET on ./DMAcc/&lt;current account&gt;/SenderId The GCM ID. If empty, the server sends an alert to the OTA server asking for one. • EXEC on ./Ext/FCA/Notification After a GCM-enabled OTA client reports its GCM ID to the OTA server, the OTA server executes this node to report success. SCOMO Get Inventory • GET on ./SCOMO/Inventory/Deployed This gets the list of components. • GET on ./SCOMO/Inventory/Deployed/&lt;X&gt;/version This is repeated once for each component to get each component's version number. Update (any) • REPLACE on ./SCOMO/Download/DP/PkgURL This writes the DD URL. • EXEC on ./SCOMO/Download/DP/Operations/DownloadAndInstall This begins the update for all components in the deployment package. LAWMO Wipe • EXEC on ./LAWMO/Operations/Wipe This starts an asynchronous wipe operation. Lock • EXEC on ./LAWMO/Operations/FullyLock This starts an asynchronous lock operation. Unlock • EXEC on ./LAWMO/Operations/UnLock This starts an asynchronous unlock operation.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-295` — Silent Install Command Processing — 分 **0.160**
   > SWMC shall receive and process the Deployment Descriptor File (DDF) from the Server and provide the DDF information to WiFiUpdateService. WiFiUpdateService shall evaluate the ./Ext/FCA/SilentInstall parameter. If the ./Ext/FCA/SilentInstall parameter is set to 1, WiFiUpdateService shall classify the…

2. `SWE1-FOTA-275` — Server-Configurable Polling Interva — 分 **0.114**
   > SWMC shall support configuration of the polling interval for periodic vehicle-initiated sessions through parameters received from the server. SWMC shall update and apply the configured polling interval for polling operations.

3. `SWE1-FOTA-128` — Parse Download Descriptor XML and Extract Deployment Parameters — 分 **0.105**
   > The SWMC shall parse the Download Descriptor provided with the update. The SWMC shall process the Download Descriptor as an XML file. The SWMC shall extract deployment package parameters and metadata from the Download Descriptor. The SWMC shall use the extracted parameters and metadata from below me…


---

### 33. `4907780` — 章 **5** TBM FOTA Reflash Requirements

**物件全文**（逐字）：

> When HU receives $TBM_Update$ = [Update_Available] AND successfully receives information of WhatsNew and Estimated time for the TBM Software update from GSDP, then the HU shall display TBM FOTA update available pop-up. Please refer to the HMI L&amp;F.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-234` — Receive TBM Update Metadata from GSDP — 分 **0.533**
   > The TBM Update Service shall receive the downloaded download descriptor (DD) file from the GSDP through SWMC. The TBM Update Service shall extract the "WhatsNew" information and 'Estimated time' from the DD metadata. The TBM Update Service shall provide the extracted "WhatsNew" information and 'Esti…

2. `SWE1-FOTA-233` — Display Estimated Time for TBM Software Update — 分 **0.474**
   > The TBM Update Service shall receive the download descriptor (DD) file from SWMC and shall extract the estimated TBM software update time information from the DD metadata received from the GSDP. The TBM Update Service shall provide the extracted estimated TBM software update time information to the …

3. `SWE1-FOTA-112` — Display TBM Update Available Pop-up with Metadata — 分 **0.426**
   > The TBM Update Service shall retrieve $TBM_Update$ using the TBM FW Service and detect when the value indicates Update_Available. The TBM Update Service shall retrieve update metadata, including estimated installation time and “What’s New” information, via the TBM FW Service. If $TBM_Update$ = [Upda…


---

### 34. `4907814` — 章 **6** TBM Algorithm Requirements

**物件全文**（逐字）：

> When TBM receives a 10 03 Diagnostic Request from FOTA Master ($F5 Diagnostic Address), TBM moves into Extended Diagnostic Session without activating Maintenance Mode.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-225` — Suppress Forced Update HMI on No FOTA Event — 分 **0.159**
   > The ROV Update Service shall receive $FOTA_MASTER.FOTA_Status$ from FOTA Master through the vehicle property interface using CarProperty Manager. When the received value isFOTA_MASTER.FOTA_Status = "No FOTA Event" , the ROV Update Service shall suppress propagation of forced update triggers to the R…

2. `SWE1-FOTA-199` — Transmit Tester Present During External ECU Reflash — 分 **0.150**
   > The ROV Update Service shall transmit periodic diagnostic Tester Present messages to external ECUs through the vehicle communication interface during any active reflash operation to maintain the diagnostic programming session. The service shall stop transmission after reflash completion, abort, or t…

3. `SWE1-FOTA-198` — Prevent Unintended DTC During OTA Reflash Process — 分 **0.147**
   > The SWMC and WiFi Update Service shall coordinate OTA reflash sequencing with Update Engine, SW Updater Manager, and SW Updater Service such that no unintended diagnostic trouble codes (DTCs) are triggered during normal OTA reflash execution. Any temporary diagnostic monitor suppression required dur…


---

### 35. `4907823` — 章 **7** Firmware Over-the-air Updates (FOTA)

**物件全文**（逐字）：

> Flow of events Figure A for FOTA 4615847- CFTSMV057_CIP_R1_O3579_92_inline.rtf WrapperResource

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-211` — Display OTA Events Through HMI — 分 **0.117**
   > The SW Update HMI shall receive update status, progress, prompts, completion results, and error events from the WiFi Update Service and shall present the appropriate user interface flow for OTA update operations when HMI is available. The WiFi Update Service shall process user interaction events rec…

2. `SWE1-FOTA-273` — Vehicle Event Interface for Software Deployment — 分 **0.110**
   > SWMC shall provide an interface to receive and process vehicle events that may block software deployment. SWMC shall evaluate the received vehicle events before initiating or continuing the software deployment process.

3. `SWE1-FOTA-191` — Provide HMI Event Handling Interface for OTA Client — 分 **0.089**
   > The WiFi Update Service shall define an event handling interface for communication with the SW Update HMI. The SW Update HMI shall send user input events to the WiFi Update Service through the defined interface. The WiFi Update Service shall process the received user input events and shall initiate …


---

### 36. `4907828` — 章 **7.1** Critical Updates

**物件全文**（逐字）：

> If the download of FOTA critical update gets interrupted when the vehicle transitions to Body OFF mode*, the download shall resume over TBM at the next Body ON mode* Please refer to CFTS009 for Power moding states

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-015` — Resume Critical Download through TBM after Body OFF Transition — 分 **0.340**
   > The WiFi Update Service shall retrieve the $OperationalModeSts$ signal via the CarPropertyManager to determine the vehicle Body ON and Body OFF states. If a FOTA critical update download is interrupted due to a transition of $OperationalModeSts$ from Body ON to Body OFF, the WiFi Update Service shal…

2. `SWE1-FOTA-012` — Resume FOTA Critical Update via Wi-Fi During Body OFF Mode — 分 **0.314**
   > The WiFi Update Service shall monitor the vehicle operational power mode using the vehicle property $OperationalModeSts$ through CarPropertyManager. If a critical FOTA package download over the embedded modem (TBM network) is interrupted when the vehicle transitions to Body OFF mode, the WiFi Update…

3. `SWE1-FOTA-113` — Display TBM Update Available Pop-up on Ignition OFF — 分 **0.236**
   > The TBM Update Service shall retrieve $TBMUpdate$ using the TBM FW Service and detect when the value indicates Update_Available. The TBM Update Service shall retrieve OperationalModeSts using CarPropertyManager. If $TBMupdate$ = [Update_Available] and OperationalModeSts transitions from Body ON to B…


---

### 37. `4907839` — 章 **8** Maps Over-the-air Updates (MOTA)

**物件全文**（逐字）：

> The MOTA updates shall meet the cyber security standards as defined in 4907490: Security and CFTS084.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-308` — OMA-DM Security Compliance — 分 **0.167**
   > SWMC shall support the configured communication protocol and apply the required security mechanisms. If a proprietary communication protocol is used, SWMC shall apply equivalent security mechanisms.

2. `SWE1-FOTA-297` — Digital Signature and Transport Security Verification — 分 **0.133**
   > SWMC shall provide the downloaded deployment package to WiFiUpdateService. WiFiUpdateService shall use SWDLSecureLib to verify the digital signature and integrity of the deployment package. OTA update processing shall continue only after successful security verification, and no mechanism shall be pr…

3. `SWE1-FOTA-299` — SWMC Security Requirement Compliance — 分 **0.102**
   > SWMC shall enforce the OTA client security requirements and provide only validated OTA update information to WiFiUpdateService. WiFiUpdateService shall process only the OTA data validated by SWMC.


---

### 38. `4907837` — 章 **8** Maps Over-the-air Updates (MOTA)

**物件全文**（逐字）：

> FOTA update has priority over MOTA. The HU shall notify the MOTA Client to restrict a MOTA update, when processing FOTA update

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-217` — Prioritize FOTA Updates Based on Defined Update Type Hierarchy — 分 **0.210**
   > The Arbiter Service shall detect the availability of multiple FOTA update types including Rest of Vehicle FOTA, HU FOTA, TBM FOTA, and Map OTA updates. When two or more update types are available simultaneously, the Arbiter Service shall determine update execution priority using the following order:…

2. `SWE1-FOTA-082` — Prioritize FOTA Update When Multiple Update Methods Have Same Version — 分 **0.207**
   > The WiFi Update Service shall provide available FOTA package version information to the Arbiter Service. The USB Update Service shall provide available USB package version information to the Arbiter Service. The Arbiter Service shall compare the software version information of update packages availa…

3. `SWE1-FOTA-095` — Display Software Update Complete Pop-up — 分 **0.200**
   > The ROV Update Service shall read FOTA_Status using CarPropertyManager. If FOTA_Status indicates Successful FOTA Update($FOTA_Status$ = [Successful FOTA Update]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the software update completion pop-up PU0416.


---

### 39. `4907849` — 章 **8.1** Non-Critical Updates

**物件全文**（逐字）：

> When the type of connection is Wi-Fi first then TBM, NAV shall periodically check for the time stamp of the download package and if it is older than 7 days, NAV shall request HU for TBM connection to complete the download.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-008` — Fallback to Embedded Modem After Wi-Fi Connection or Download Timeout — 分 **0.177**
   > The WiFi Update Service shall use WiFi Manager and Connectivity Service to establish connectivity with a previously configured Wi-Fi network for FOTA package download managed by SWMC. The WiFi Update Service shall monitor the duration of Wi-Fi connection establishment attempts and FOTA package downl…

2. `SWE1-FOTA-233` — Display Estimated Time for TBM Software Update — 分 **0.136**
   > The TBM Update Service shall receive the download descriptor (DD) file from SWMC and shall extract the estimated TBM software update time information from the DD metadata received from the GSDP. The TBM Update Service shall provide the extracted estimated TBM software update time information to the …

3. `SWE1-FOTA-234` — Receive TBM Update Metadata from GSDP — 分 **0.132**
   > The TBM Update Service shall receive the downloaded download descriptor (DD) file from the GSDP through SWMC. The TBM Update Service shall extract the "WhatsNew" information and 'Estimated time' from the DD metadata. The TBM Update Service shall provide the extracted "WhatsNew" information and 'Esti…


---

### 40. `4907861` — 章 **8.1** Non-Critical Updates

**物件全文**（逐字）：

> If during a download, no MOTA data is being received over the Wi-Fi connection for 5 consecutive minutes and there is sufficient Wi-Fi signal strength, NAV shall notify HU to terminate the download session.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-003` — Terminate Wi-Fi Download Session Until Next Ignition ON Event — 分 **0.402**
   > The WiFi Update Service shall monitor FOTA data reception status from SWMC and Wi-Fi signal strength from WiFi Manager during firmware download over Wi-Fi. If FOTA data is not received while the Wi-Fi signal strength satisfies the configured threshold, the WiFi Update Service shall start and maintai…

2. `SWE1-FOTA-006` — Terminate Wi-Fi Download Session After Data Timeout — 分 **0.387**
   > The WiFi Update Service shall monitor FOTA data reception status from SWMC and Wi-Fi signal strength from WiFi Manager during firmware download over Wi-Fi. If FOTA data is not received while the Wi-Fi signal strength satisfies the configured threshold, the WiFi Update Service shall start a download …

3. `SWE1-FOTA-063` — Categorize Wi-Fi Networks Based on Signal Strength — 分 **0.197**
   > The WiFi Update Service shall retrieve the list of in-range Wi-Fi networks using WiFiManager scan results. The WiFi Manager shall evaluate the signal strength of each in-range Wi-Fi network. The WiFi Manager shall classify each Wi-Fi network into one of the following categories based on predefined W…


---

### 41. `4907864` — 章 **8.2** Route Planning Updates

**物件全文**（逐字）：

> When the user plans for a route which passes through outdated maps, NAV shall check for an available map update using TBM.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-113` — Display TBM Update Available Pop-up on Ignition OFF — 分 **0.189**
   > The TBM Update Service shall retrieve $TBMUpdate$ using the TBM FW Service and detect when the value indicates Update_Available. The TBM Update Service shall retrieve OperationalModeSts using CarPropertyManager. If $TBMupdate$ = [Update_Available] and OperationalModeSts transitions from Body ON to B…

2. `SWE1-FOTA-215` — Trigger TBM Update Check on Scheduled Event — 分 **0.178**
   > The TBM Update Service shall detect the scheduled update-check trigger for TBM FOTA. Upon trigger, the TBM Update Service shall set $HUFOTACheck$ = [Check for updates] and transmit the signal to TBM through TBM FW Service.

3. `SWE1-FOTA-112` — Display TBM Update Available Pop-up with Metadata — 分 **0.152**
   > The TBM Update Service shall retrieve $TBM_Update$ using the TBM FW Service and detect when the value indicates Update_Available. The TBM Update Service shall retrieve update metadata, including estimated installation time and “What’s New” information, via the TBM FW Service. If $TBM_Update$ = [Upda…


---

### 42. `4907865` — 章 **8.2** Route Planning Updates

**物件全文**（逐字）：

> If an update is available to download, the NAV shall queue that event and requests HU for Wi-Fi connection at BODY ON mode. HU shall provide a Wi-Fi connection only at the next Body OFF mode.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-015` — Resume Critical Download through TBM after Body OFF Transition — 分 **0.229**
   > The WiFi Update Service shall retrieve the $OperationalModeSts$ signal via the CarPropertyManager to determine the vehicle Body ON and Body OFF states. If a FOTA critical update download is interrupted due to a transition of $OperationalModeSts$ from Body ON to Body OFF, the WiFi Update Service shal…

2. `SWE1-FOTA-090` — Cache and Display “What’s New” After Successful Update Until Next Body — 分 **0.207**
   > The ROV Update Service shall retrieve FOTA_Status using CarPropertyManager and detect when the value indicates Successful FOTA Update.( $FOTA_Status$ = [Successful FOTA Update] ) Upon detection, the ROV Update Service shall cache the FOTA_Status and the “What’s New” details received from the deploym…

3. `SWE1-FOTA-012` — Resume FOTA Critical Update via Wi-Fi During Body OFF Mode — 分 **0.206**
   > The WiFi Update Service shall monitor the vehicle operational power mode using the vehicle property $OperationalModeSts$ through CarPropertyManager. If a critical FOTA package download over the embedded modem (TBM network) is interrupted when the vehicle transitions to Body OFF mode, the WiFi Update…


---

### 43. `4907868` — 章 **8.3** User Initiated Updates

**物件全文**（逐字）：

> During the User initiated map update, NAV shall check for the MOTA subscription type and accordingly request HU for Wi-Fi or TBM connection

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-189` — Initiate OTA Server Check from User HMI Request — 分 **0.222**
   > The SW Update HMI shall detect a user request for Check for Update and shall send the request to the WiFi Update Service. The WiFi Update Service shall request SWMC to establish communication with the OTA server and check for available software updates.

2. `SWE1-FOTA-366` — FOTA Update Availability Check — 分 **0.175**
   > * The WiFiUpdateService shall receive server-initiated OTA session requests from the TC client and forward the request to the SWMC. *The SWMC shall check the OTA server for an available FOTA update upon receiving a session request from the WiFiUpdateService.

3. `SWE1-FOTA-317` — User-Initiated Network Deactivation Handling — 分 **0.151**
   > The WiFiUpdateService shall handle user-initiated deactivation of mobile data usage or an active Wi-Fi connection reported by SWMC during OTA server communication, flashing, or software component update.


---

### 44. `4907869` — 章 **8.3** User Initiated Updates

**物件全文**（逐字）：

> When the MOTA subscription type is Wi-Fi, NAV shall request for Wi-Fi connection only

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-050` — Forget Saved Wi-Fi Network and Remove Credentials — 分 **0.160**
   > The HMI shall provide an option for the user to forget a saved Wi-Fi network. The HMI shall detect the user selection of the “Forget Network” option and send a network removal request to WiFi Manager. Upon receiving the request, WiFi Manager shall remove the stored Wi-Fi network configuration and as…

2. `SWE1-FOTA-189` — Initiate OTA Server Check from User HMI Request — 分 **0.155**
   > The SW Update HMI shall detect a user request for Check for Update and shall send the request to the WiFi Update Service. The WiFi Update Service shall request SWMC to establish communication with the OTA server and check for available software updates.

3. `SWE1-FOTA-047` — Store Wi-Fi Network Credentials for Future Connection — 分 **0.131**
   > Upon successful Wi-Fi connection establishment, WiFi Manager shall persist the Wi-Fi network credentials required for future automatic connection attempts. WiFi Manager shall store the following Wi-Fi network credential information: Network SSID, Security type, Encryption type, and Passphrase. Conne…


---

### 45. `4907874` — 章 **8.4** MOTA Client Initiated Updates

**物件全文**（逐字）：

> If the update is downloaded via Wi-Fi with Body OFF mode, the installation shall happen at the next Body ON mode.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-015` — Resume Critical Download through TBM after Body OFF Transition — 分 **0.272**
   > The WiFi Update Service shall retrieve the $OperationalModeSts$ signal via the CarPropertyManager to determine the vehicle Body ON and Body OFF states. If a FOTA critical update download is interrupted due to a transition of $OperationalModeSts$ from Body ON to Body OFF, the WiFi Update Service shal…

2. `SWE1-FOTA-090` — Cache and Display “What’s New” After Successful Update Until Next Body — 分 **0.248**
   > The ROV Update Service shall retrieve FOTA_Status using CarPropertyManager and detect when the value indicates Successful FOTA Update.( $FOTA_Status$ = [Successful FOTA Update] ) Upon detection, the ROV Update Service shall cache the FOTA_Status and the “What’s New” details received from the deploym…

3. `SWE1-FOTA-088` — Display Success Pop-up in Body ON Mode — 分 **0.244**
   > The ROV Update Service shall retrieve $FOTA_Status$ and $OperationalModeSts$ using CarPropertyManager. If FOTA_Status indicates successful FOTA update ( $FOTA_Status$ = [Successful FOTA Update]) completion and OperationalModeSts indicates Body ON mode, the ROV Update Service shall notify the ROV FOT…


---

### 46. `4907873` — 章 **8.4** MOTA Client Initiated Updates

**物件全文**（逐字）：

> When an update is available, NAV shall notify the HU and requests for a connection

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-272` — Vehicle Event Interface Support — 分 **0.208**
   > SWMC shall support event interface to receive server-initiated session requests from the Server.

2. `SWE1-FOTA-048` — Display Wi-Fi Connection Failure Prompt — 分 **0.200**
   > WiFi Manager and Connectivity Manager shall monitor Wi-Fi connection establishment status. Upon Wi-Fi connection failure, WiFi Manager shall notify the WiFi page of the connection failure status. The HMI shall display a prompt indicating that the Wi-Fi connection was not successful.

3. `SWE1-FOTA-190` — Display No Update Available Status on HMI — 分 **0.195**
   > The SWMC shall provide the update availability check result to the WiFi Update Service after OTA server communication is completed. When SWMC reports that no software update is available, the WiFi Update Service shall notify the SW Update HMI. The SW Update HMI shall display a message indicating tha…


---

### 47. `4907894` — 章 **9.1** Pre-Installation

**物件全文**（逐字）：

> When the scheduled time has been determined, the HU shall compare the current system time (defined in CFTS015) to the scheduled time and then send the difference in $HU_Scheduled_Install$

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-107` — Calculate and Report Remaining Time to Scheduled Install — 分 **0.472**
   > The ROV Update Service shall store the determined scheduled installation time for the update event. The ROV Update Service shall retrieve the current system time from the system time source. The ROV Update Service shall calculate the time difference between the scheduled installation time and the cu…

2. `SWE1-FOTA-338` — Pre-Deployment Package Authenticity Verification — 分 **0.154**
   > * The SWMC shall verify the authenticity of the deployment package after the download is completed. * The WiFiUpdateService shall verify the authenticity of the deployment package after user acceptance or when the scheduled installation time is reached, before initiating the deployment.

3. `SWE1-FOTA-148` — Display Estimated Installation Time in Popup PU0304 — 分 **0.149**
   > The WiFi Update Service shall retrieve the estimated installation time from the downloaded deployment package details from SWMC. The WiFi Update Service shall provide the estimated installation time data to the SW Update HMI. The SW Update HMI shall populate the estimated time for install in the pop…


---

### 48. `4907900` — 章 **9.2** Installation Progress

**物件全文**（逐字）：

> The HU shall populate the installation percentage and estimated time remaining progress in the pop-up, "Installation Progress ROV" based on the status received from SGW_FOTA_HMI_ETM.4215

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-237` — Populate Installation Progress Popup Using SGW Status Data — 分 **0.789**
   > The ROV Update Service shall receive installation progress status information from SGW_FOTA_HMI_ETM.4215 through CarProperty Manager. The ROV Update Service shall provide the installation percentage and estimated remaining installation time to the ROV FOTA HMI. The ROV FOTA HMI shall populate the "I…

2. `SWE1-FOTA-232` — Populate Installation Progress Popup Using SGW Status Data — 分 **0.675**
   > The ROV Update Service shall monitor update progress information received through the SGW_FOTA_HMI_ETM.4215 through CarPropertyManager interface. The ROV Update Service shall extract the installation percentage value and the estimated remaining time value from the received status information. The RO…

3. `SWE1-FOTA-229` — Process ROV HMI Information from Ethernet Message — 分 **0.493**
   > The ROV Update Service shall receive HMI information through the Ethernet message SGW_FOTA_HMI_ETM.4215 using CarProperty Manager. The received HMI information shall include estimated completion time, remaining time, progress information, and "What's New" information for ROV FOTA update processing a…


---

### 49. `4907910` — 章 **9.3** Post-Installation

**物件全文**（逐字）：

> If all the conditions to display pop-up are met, then the HU shall display the pop-up PU0303 once per ignition cycle.Please refer to HMI

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-154` — Display Conditions Not Met With Specific Cancellation Reason — 分 **0.226**
   > The WiFi Update Service shall evaluate scheduled installation preconditions before initiating the scheduled installation process. The WiFi Update Service/USB Update Service shall monitor $PowerMode$, $IBS_SOC$, $IBS_SOC_ACCURACY$, and $OperationalModeSts$ using CarProperty Manager and CarPower Manag…

2. `SWE1-FOTA-004` — Retry Wi-Fi Download for 7 Ignition Cycles Before Triggering Pop-up — 分 **0.181**
   > The WiFi Update Service shall use previously configured Wi-Fi network information from WiFi Manager and Connectivity Service to automatically establish Wi-Fi connectivity for FOTA package download using SWMC. The WiFi Update Service shall monitor ignition cycle transitions using the vehicle property…

3. `SWE1-FOTA-088` — Display Success Pop-up in Body ON Mode — 分 **0.169**
   > The ROV Update Service shall retrieve $FOTA_Status$ and $OperationalModeSts$ using CarPropertyManager. If FOTA_Status indicates successful FOTA update ( $FOTA_Status$ = [Successful FOTA Update]) completion and OperationalModeSts indicates Body ON mode, the ROV Update Service shall notify the ROV FOT…


---

### 50. `4907915` — 章 **9.4.1** Pre-Installation

**物件全文**（逐字）：

> When the scheduled time is reached, TBM shall send $Install_Time_Reached$ to SGW.

**037 全 311 列中對本物件分數最高之 3 列**：

1. `SWE1-FOTA-338` — Pre-Deployment Package Authenticity Verification — 分 **0.268**
   > * The SWMC shall verify the authenticity of the deployment package after the download is completed. * The WiFiUpdateService shall verify the authenticity of the deployment package after user acceptance or when the scheduled installation time is reached, before initiating the deployment.

2. `SWE1-FOTA-107` — Calculate and Report Remaining Time to Scheduled Install — 分 **0.259**
   > The ROV Update Service shall store the determined scheduled installation time for the update event. The ROV Update Service shall retrieve the current system time from the system time source. The ROV Update Service shall calculate the time difference between the scheduled installation time and the cu…

3. `SWE1-FOTA-148` — Display Estimated Installation Time in Popup PU0304 — 分 **0.164**
   > The WiFi Update Service shall retrieve the estimated installation time from the downloaded deployment package details from SWMC. The WiFi Update Service shall provide the estimated installation time data to the SW Update HMI. The SW Update HMI shall populate the estimated time for install in the pop…

