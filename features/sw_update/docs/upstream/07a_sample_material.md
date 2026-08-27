# 上繳包 07a —— T21b 人裁樣本材料（20 列）

> 主包：`07_ground_truth.md`。本檔為材料傾印，**執行層不作任何對應判斷**。
>
> ⚠ **A-SU4 污染標記**：候選物件之全文若含內嵌之 Description 宣告
> （14/487 物件、佔需求物件文字 19.5%），已於該候選標 `⚠A-SU4 污染`。
> 其 TF-IDF 分數以受污染之語料算出，**分數本身不可信**，
> 惟其**全文摘錄仍為逐字原文**，供人裁時直接閱讀判斷。


取樣碼：`309` 群前 6、`291` 群前 3、`178` 群前 2、`259` 群全 3，其餘 6 列自 `random.Random(0).sample(sorted(pool), 6)`。

**執行層不作任何對應判斷** —— 以下僅為材料。


---

### 1. `SWE1-FOTA-310` — OMA-DM Message Integrity Verification

- 所屬 Heading：`SWE1-FOTA-309` OMA-DM Security
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-340`

**Requirement Description 全文**：

> SWMC shall perform integrity verification of received OMA-DM messages before processing them. SWMC shall reject messages that fail the integrity verification.

**路徑 A 前 5 候選**：

1. `4907509` — 章 **4.8.2** OMA-DM Security — 分 **0.366**
   > Integrity check of OMA-DM messages shall be done upon reception.

2. `4907503` — 章 **4.8.1** Communication Security — 分 **0.216**
   > It SHALL only respond to messages received from an authenticated source.

3. `4907519` — 章 **4.8.3** Deployment Package Security — 分 **0.212**
   > The OTA client shall support interaction with signature verification systems/libraries provided by FCA for deployment package signature verification.

4. `4907515` — 章 **4.8.3** Deployment Package Security — 分 **0.211**
   > The OTA client shall ensure integrity of the deployment package before it is installed, immediately pre installation.

5. `4907514` — 章 **4.8.3** Deployment Package Security — 分 **0.196**
   > The OTA client shall verify integrity of the deployment package once it is received from the server, immediately post download.


---

### 2. `SWE1-FOTA-311` — DM Tree Encryption and Protection

- 所屬 Heading：`SWE1-FOTA-309` OMA-DM Security
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-339`

**Requirement Description 全文**：

> SWMC shall store the DM Tree in an encrypted format to prevent plaintext access. If a proprietary communication protocol is used, SWMC shall store the associated configuration data in an encrypted format.

**路徑 A 前 5 候選**：

1. `4907510` ⚠**A-SU4 污染** — 章 **4.8.2** OMA-DM Security — 分 **0.247**
   > The OTA client shall encrypt the DM Tree so that is not plaintext readable. If proprietary protocol is implemented, any configuration data shall be encrypted and not plaintext. 4907511: [Artifact Type:Description] [State:Approved] [ECU:LTM, ETM] [Market:All] [Model Year:2024, 2022, 2018, 2025, 2019, 2020, 2017, 2021, 2023] [Radio:VP4R7, VP4R84, VP484, VP5R120, VP465, VP365, R1L, R1L-R, R1H, VP384,…

2. `4907375` — 章 **4.5.4.1** SMS/MQTT Push Support — 分 **0.183**
   > OTA client SHOULD parse and respond to the SMS NIA format given in OMA-DM specification or FCA approved proprietary format for the provided shoulder tap.

3. `4907426` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.129**
   > HU shall store valid credentials for usage on next time HU attempts to connect to that network

4. `4907315` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.122**
   > The OTA client SHOULD be able to receive and process the OMA-DM download descriptor format regarding deployment package download [OMA-SUP-XSD_dd-V2_0-20110329-A]. If OTA client utilizes a proprietary protocol, a substitute download descriptor shall be implemented following similar requirements.

5. `4907742` — 章 **4.13.4** FCA Specific Tree structure (DDF) — 分 **0.122**
   > The specific device description framework format should be defined by the OTA server supporting the solution and the client shall reflect the nodes in the DM tree of the OTA client. FCA specific server configurable nodes and commands are defined in Appendix B and C. The specific values listed in the appendices are targeted for OMA-DM solution implementation. If using a proprietary protocol, the sa…


---

### 3. `SWE1-FOTA-312` — Deployment Package Integrity Verification

- 所屬 Heading：`SWE1-FOTA-309` OMA-DM Security
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-335`

**Requirement Description 全文**：

> SWMC shall download the deployment package from the OTA Server and provide the downloaded deployment package to WiFiUpdateService. WiFiUpdateService shall perform the integrity verification of the deployment package immediately after receiving the package

**路徑 A 前 5 候選**：

1. `4907483` — 章 **4.7.3.2** Silent Updates — 分 **0.493**
   > 2. After the deployment package is downloaded, its deployment shall start immediately.

2. `4907514` — 章 **4.8.3** Deployment Package Security — 分 **0.396**
   > The OTA client shall verify integrity of the deployment package once it is received from the server, immediately post download.

3. `4907515` — 章 **4.8.3** Deployment Package Security — 分 **0.358**
   > The OTA client shall ensure integrity of the deployment package before it is installed, immediately pre installation.

4. `4907604` — 章 **4.10.5** Deployment Flow — 分 **0.285**
   > 3. Deployment package signature verification is done to verify authenticity of the package.

5. `4907588` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.281**
   > 6. After acceptance, the OTA client shall check for download pre-conditions and then download the deployment package.


---

### 4. `SWE1-FOTA-313` — Software Update Error Handling Coordination

- 所屬 Heading：`SWE1-FOTA-309` OMA-DM Security
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-188`

**Requirement Description 全文**：

> * The WiFiUpdateService shall coordinate the handling of the error conditions defined in System Requirements 4907672, 4907671, 4907670, 4907669, 4907668, and 4907667 by interacting with SWMC and the appropriate installer component during the software update process. * The SWMC shall handle the error conditions defined in System Requirements 4907672, 4907671, 4907670, 4907669, 4907668, and 4907667 during OTA server communication and software update execution, and shall report the update status to WiFiUpdateService.

**路徑 A 前 5 候選**：

1. `4907667` — 章 **4.12** Interrupt Handling — 分 **0.117**
   > 1. Socket read/write error

2. `4907702` — 章 **4.13.1** SCOMO Support — 分 **0.104**
   > The update of firmware shall be fully failsafe, so that interrupt conditions defined in section power outage at any time during the update does not affect the final outcome.

3. `4907705` — 章 **4.13.1** SCOMO Support — 分 **0.102**
   > The update of ECU data shall be fully failsafe, so that interrupt conditions defined in section power outage at any time during the update does not affect the final outcome.

4. `4907811` — 章 **6** TBM Algorithm Requirements — 分 **0.094**
   > During any Ignition conditions, When an update installation has been successfully completed, then the TBM shall send $TBMUpdate$ = [Update_End] for &lt;T_FOTA_END&gt;

5. `4907392` — 章 **4.5.5** Bus communications — 分 **0.093**
   > The OTA client, HU, and ECU's SHALL NOT set any DTC during the reflash process.


---

### 5. `SWE1-FOTA-315` — Socket Read/Write Error Handling

- 所屬 Heading：`SWE1-FOTA-309` OMA-DM Security
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-190`

**Requirement Description 全文**：

> The SWMC shall detect and handle socket read/write errors during OTA server communication, flashing, or software component update, and shall report the error status to WiFiUpdateService.

**路徑 A 前 5 候選**：

1. `4907667` — 章 **4.12** Interrupt Handling — 分 **0.481**
   > 1. Socket read/write error

2. `4907665` — 章 **4.12** Interrupt Handling — 分 **0.189**
   > There are several kinds of interrupts that can be handled while an OTA client is connected to the OTA server and while flashing or updating a software component. This section describes how to handle interrupts and how the client should interact with the OTA server when interrupts are resolved.

3. `4907301` — 章 **4.4** OTA Client Architecture — 分 **0.168**
   > Data connection &amp; Socket interface. This component is the same as for the Vehicle Manager. It provides the connectivity to the server.

4. `4907524` — 章 **4.9.1** Update Agent Requirements — 分 **0.152**
   > Update Agent component shall be able to handle both file system and binary image updates.

5. `4907311` — 章 **4.4** OTA Client Architecture — 分 **0.141**
   > Flash driver. This component provides drivers to read and write flash memory. If the file system update is applicable it may contain a file system driver as well. Access to this component should be abstracted such that it is possible to use the update agent on multiple platforms and operating systems.


---

### 6. `SWE1-FOTA-316` — Network Loss Handling

- 所屬 Heading：`SWE1-FOTA-309` OMA-DM Security
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-191`

**Requirement Description 全文**：

> The SWMC shall detect network loss conditions, including network errors, no data coverage, loss of Wi-Fi connection, phone tether disconnection, and embedded modem roaming, during OTA server communication, flashing, or software component update, and shall report the network loss status to WiFiUpdateService.

**路徑 A 前 5 候選**：

1. `4907668` — 章 **4.12** Interrupt Handling — 分 **0.586**
   > 2. Network loss: Network error or no data coverage, No Wi-Fi connection, Phone tether is disconnected, Embedded modem moves to roaming network

2. `4907671` — 章 **4.12** Interrupt Handling — 分 **0.196**
   > 5. Loss of power(battery disconnect)

3. `4907825` — 章 **7.1** Critical Updates — 分 **0.195**
   > If there is no Wi-Fi network saved or HU is not able to download the package then download shall happen via embedded modem or TBM

4. `4907822` — 章 **7** Firmware Over-the-air Updates (FOTA) — 分 **0.175**
   > If HU is not able to connect to a Wi-Fi network or unable to download the package for 7 days, then download shall happen via embedded modem

5. `4907526` — 章 **4.9.1** Update Agent Requirements — 分 **0.142**
   > Update Agent shall have a recovery mechanism in the event of a power failure, communications loss, or other event which interrupts the update.


---

### 7. `SWE1-FOTA-292` — Configurable Network Priority Support

- 所屬 Heading：`SWE1-FOTA-291` Bearer selection:
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-384`

**Requirement Description 全文**：

> WiFiUpdateService shall manage the configured network priority and select the appropriate network for OTA communication. WiFiUpdateService shall establish the network connection and enable SWMC to communicate with the OTA Server

**路徑 A 前 5 候選**：

1. `4907569` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.257**
   > FOTA client shall establish communication with TC client.

2. `4907400` — 章 **4.6** OTA download via Wi-Fi — 分 **0.256**
   > If an attempt to establish a connection to a Wi-Fi network has not succeeded within 3 minutes, the HU shall attempt a connection to the next network in the priority chain.(Kindly see section 4.6.1 for priority chain)

3. `4907402` — 章 **4.6.1** Connection to Wi-Fi network — 分 **0.218**
   > The HU shall establish a Wi-Fi connection with saved Wi-Fi networks for OTA updates

4. `4907403` — 章 **4.6.1** Connection to Wi-Fi network — 分 **0.203**
   > Upon an attempt to download via Wi-Fi and when multiple networks are configured, the HU will select the “best” network from which to attempt to connect and download. This scenario defines the criteria for network selection.

5. `4907850` — 章 **8.1** Non-Critical Updates — 分 **0.193**
   > When the NAV requests HU for a Wi-Fi connection, HU shall establish a connection when the ignition transitions to Body OFF mode and when the conditions to connect to Wi-Fi network are met.- Refer to 4907395: OTA download via Wi-Fi for Wi-Fi Connection Strategy


---

### 8. `SWE1-FOTA-293` — DDF Update Type Processing

- 所屬 Heading：`SWE1-FOTA-291` Bearer selection:
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-380`

**Requirement Description 全文**：

> SWMC shall provide the Deployment Descriptor File (DDF) to WiFiUpdateService. WiFiUpdateService shall evaluate the DDF parameters to determine the update type. If the update type parameter is not present in the DDF, WiFiUpdateService shall classify the update as a non-critical update.

**路徑 A 前 5 候選**：

1. `4907473` — 章 **4.7.3.1** Critical Updates — 分 **0.349**
   > If the DDF does not include whether the update is critical or not, the HU shall treat the update as a non-critical update

2. `4907487` — 章 **4.7.3.2** Silent Updates — 分 **0.281**
   > If the DDF does not include whether the update is silent or not, the HU shall treat the update as a non-silent update

3. `4907453` — 章 **4.7.3** Main Update Configuration Options — 分 **0.276**
   > Update type:

4. `4907472` — 章 **4.7.3.1** Critical Updates — 分 **0.177**
   > Critical and non-critical updates shall be defined by the server

5. `4907456` — 章 **4.7.3** Main Update Configuration Options — 分 **0.146**
   > Regular update: Non-silent, non-critical update. End-user/HMI flow shall be followed, and Network bearer rules apply.


---

### 9. `SWE1-FOTA-294` — DDF Silent Update Processing

- 所屬 Heading：`SWE1-FOTA-291` Bearer selection:
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-372`

**Requirement Description 全文**：

> SWMC shall read the Deployment Descriptor File (DDF) and provide the DDF information to WiFiUpdateService. WiFiUpdateService shall read the DDF parameters and determine the update mode. If the DDF does not specify the update as silent, WiFiUpdateService shall treat the update as a non-silent update.

**路徑 A 前 5 候選**：

1. `4907487` — 章 **4.7.3.2** Silent Updates — 分 **0.512**
   > If the DDF does not include whether the update is silent or not, the HU shall treat the update as a non-silent update

2. `4907473` — 章 **4.7.3.1** Critical Updates — 分 **0.403**
   > If the DDF does not include whether the update is critical or not, the HU shall treat the update as a non-critical update

3. `4907806` — 章 **6** TBM Algorithm Requirements — 分 **0.169**
   > When TBM has completed the download of TBM FOTA Silent update package, then the TBM shall send $TBMUpdate$ = [Silent_Update]

4. `4907456` — 章 **4.7.3** Main Update Configuration Options — 分 **0.165**
   > Regular update: Non-silent, non-critical update. End-user/HMI flow shall be followed, and Network bearer rules apply.

5. `4907486` — 章 **4.7.3.2** Silent Updates — 分 **0.145**
   > Silent update shall be applicable for all session flows.


---

### 10. `SWE1-FOTA-179` — Start Silent Update Download Automatically

- 所屬 Heading：`SWE1-FOTA-178` For a silent update, the OTA client follows these steps for the download
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-366`

**Requirement Description 全文**：

> The SWMC shall provide the downloaded Download Descriptor (DD) metadata to the WiFi Update Service after update availability is confirmed. The WiFi Update Service shall analyze the DD metadata to determine whether the update type is classified as Silent Update. If the DD metadata indicates a Silent Update, the WiFi Update Service shall automatically request SWMC to initiate deployment package download.

**路徑 A 前 5 候選**：

1. `4907481` — 章 **4.7.3.2** Silent Updates — 分 **0.201**
   > 1. The download of the deployment package shall start automatically.

2. `4907487` — 章 **4.7.3.2** Silent Updates — 分 **0.201**
   > If the DDF does not include whether the update is silent or not, the HU shall treat the update as a non-silent update

3. `4907806` — 章 **6** TBM Algorithm Requirements — 分 **0.200**
   > When TBM has completed the download of TBM FOTA Silent update package, then the TBM shall send $TBMUpdate$ = [Silent_Update]

4. `4907453` — 章 **4.7.3** Main Update Configuration Options — 分 **0.182**
   > Update type:

5. `4907656` — 章 **4.11** User Experience (UX)/HMI — 分 **0.173**
   > User experience shall be same for all update types and updates (regular/critical/silent) SHOULD be configurable from the server so that the FOTA service administrator can select the relevant option depending on the type and urgency of the update being performed.


---

### 11. `SWE1-FOTA-180` — Optionally Suppress Download Confirmation Screen

- 所屬 Heading：`SWE1-FOTA-178` For a silent update, the OTA client follows these steps for the download
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-367`

**Requirement Description 全文**：

> When the update type is identified as Silent Update, the WiFi Update Service shalll not trigger the SW Update HMI to display a download confirmation screen. The WiFi Update Service shall automatically request SWMC to initiate deployment package download without user interaction.

**路徑 A 前 5 候選**：

1. `4907470` — 章 **4.7.3.1** Critical Updates — 分 **0.387**
   > 1. The download of the deployment package shall start automatically; The OTA client SHALL NOT display a download confirmation screen.

2. `4907482` — 章 **4.7.3.2** Silent Updates — 分 **0.285**
   > The OTA client MAY NOT display a download confirmation screen.

3. `4907475` — 章 **4.7.3.2** Silent Updates — 分 **0.277**
   > Silent updates run automatically without any progress notifications or end user interaction.

4. `4907484` — 章 **4.7.3.2** Silent Updates — 分 **0.273**
   > The OTA client MAY NOT display a deployment confirmation screen.

5. `4907481` — 章 **4.7.3.2** Silent Updates — 分 **0.262**
   > 1. The download of the deployment package shall start automatically.


---

### 12. `SWE1-FOTA-260` — OMA-DM Protocol Communication Support

- 所屬 Heading：`SWE1-FOTA-259` Vehicle Properties
- Sub Categorization：(blank)｜Source Requirement ID：`SYS-RA-FOTA-476`

**Requirement Description 全文**：

> SWMC shall establish and manage communication with the OTA Server using the OMA-DM protocol. SWMC shall notify WiFiUpdateService of the OTA communication events required to initiate and manage the deployment package download.

**路徑 A 前 5 候選**：

1. `4907504` — 章 **4.8.1** Communication Security — 分 **0.313**
   > OTA client shall NOT initiate communication to any unauthorized server.

2. `4907569` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.305**
   > FOTA client shall establish communication with TC client.

3. `4907314` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.207**
   > It is RECOMMENDED that the OTA client implement the open OMA-DM protocol specification [OMA-TS-DM-Protocol-V1_2-20060424-C] in order to communicate with with the server. Use of non-open proprietary communication protocol MAY be allowed if approved by FCA.

4. `4907355` ⚠**A-SU4 污染** — 章 **4.5.1** OTA Communication Protocols — 分 **0.188**
   > The OTA client is RECOMMENDED to use the open communication protocols defined in Table 4-3 to communicate with the server solution interface. HTTP and TLS protocols are REQUIRED if a proprietary communication protocol is used in place of OMA-DM. 4907356: [Artifact Type:Description] [State:Approved] [ECU:LTM, ETM] [Market:All] [Model Year:2024, 2017, 2018, 2021, 2023, 2025, 2019, 2022, 2020] [Radio…

5. `4907294` — 章 **4.4** OTA Client Architecture — 分 **0.180**
   > Vehicle Integration Layer. This component shall be abstracted to provide the OTA client access to the vehicle properties and settings. OMA-DM defines a tree-like structure of settings, further detailed in this document, that may be read or written by the server. Some of these properties are required by the OMA-DM protocol to connect to the server (server URL, port, etc.), authenticate the vehicle …


---

### 13. `SWE1-FOTA-261` — Download Descriptor Processing Support

- 所屬 Heading：`SWE1-FOTA-259` Vehicle Properties
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-477`

**Requirement Description 全文**：

> SWMC to receive and process the OMA-DM Download Descriptor for deployment package downloads. When a proprietary communication protocol is used, theSWMC shall support processing of an equivalent Download Descriptor containing the required deployment package information.

**路徑 A 前 5 候選**：

1. `4907315` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.389**
   > The OTA client SHOULD be able to receive and process the OMA-DM download descriptor format regarding deployment package download [OMA-SUP-XSD_dd-V2_0-20110329-A]. If OTA client utilizes a proprietary protocol, a substitute download descriptor shall be implemented following similar requirements.

2. `4907332` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.335**
   > OTA client shall download the package from the URL provided in the Download Descriptor.

3. `4907300` — 章 **4.4** OTA Client Architecture — 分 **0.294**
   > Download Agent is responsible for reliable downloading of the deployment package (DP) from the URL provided in the deployment package download descriptor (DD), and providing information about download progress.

4. `4907293` — 章 **4.4** OTA Client Architecture — 分 **0.241**
   > Communciations Protocol Stack. The OTA client may implement OMA-DM or an approved proprietary protocol to negotiate with the server, authenticate the vehicle, provide information about the vehicle to the server, and retrieve the Download Descriptor (DD) [OMA-SUP-XSD_dd-V2_0-20110329-A]. The DD contains URL of Deployment Package (DP) and metadata that is needed for the user interface and may affect…

5. `4907481` — 章 **4.7.3.2** Silent Updates — 分 **0.210**
   > 1. The download of the deployment package shall start automatically.


---

### 14. `SWE1-FOTA-262` — Vehicle Property Access through Vehicle Integration Layer

- 所屬 Heading：`SWE1-FOTA-259` Vehicle Properties
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-479`

**Requirement Description 全文**：

> SWMC shall request the required vehicle properties from WiFiUpdateService. WiFiUpdateService shall retrieve the required vehicle properties through CarPropertyManager. CarPropertyManager shall access the Vehicle Integration Layer (VHAL/CarPropertyService) to obtain the vehicle properties and settings. WiFiUpdateService shall provide the retrieved vehicle property information to SWMC for unique vehicle identification.

**路徑 A 前 5 候選**：

1. `4907317` ⚠**A-SU4 污染** — 章 **4.4.1** OTA Architecture Requirements — 分 **0.244**
   > The client shall have access to the vehicle properties and settings via a Vehicle Integration Layer in order to uniquely identify the vehicle, specifically to the Required Vehicle Properties in Table 4-2. The properties MAY include the Optional Vehicle properties listed in Table 4-2, depending on eventual server implementation: 4907318: [Artifact Type:Description] [State:Approved] [ECU:LTM, ETM] […

2. `4907294` — 章 **4.4** OTA Client Architecture — 分 **0.196**
   > Vehicle Integration Layer. This component shall be abstracted to provide the OTA client access to the vehicle properties and settings. OMA-DM defines a tree-like structure of settings, further detailed in this document, that may be read or written by the server. Some of these properties are required by the OMA-DM protocol to connect to the server (server URL, port, etc.), authenticate the vehicle …

3. `4907585` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.138**
   > 3. OTA server MAY request the client for a complete or partial software inventory. The OTA client shall retrieve the required software inventory and provide it to the server.

4. `4907701` — 章 **4.13.1** SCOMO Support — 分 **0.091**
   > The OTA client shall reboot if required for updating firmware on the host ECU.

5. `4907296` — 章 **4.4** OTA Client Architecture — 分 **0.073**
   > Push Handler allows the vehicle to receive server-initiated updates. This component registers to receive WAP Push SMS, and provides SMS to the protocol stack. When an SMS is received, Vehicle Manager may start the client-initiated session to check for available updates. This component is required only if server-initiated update is required. This component may also be required to support MQTT.


---

### 15. `SWE1-FOTA-257` — Abstract Storage Interface for Deployment Package

- 所屬 Heading：`SWE1-FOTA-251` High Level FOTA Diagram
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-495`

**Requirement Description 全文**：

> SWMC shall provide the downloaded deployment package to WiFiUpdateService. WiFiUpdateService shall store the deployment package on the host module through the abstract file system/flash interface, independent of the operating system and flash driver.

**路徑 A 前 5 候選**：

1. `4907334` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.614**
   > OTA client shall have abstract interface to the flash driver/file system in order to store the deployment package on the host module. This shall not be OS or flash driver dependant.

2. `4907302` — 章 **4.4** OTA Client Architecture — 分 **0.453**
   > Flash/File System Driver. Since the downloaded deployment package shall be available to the Deployment Manager, the deployment package shall support the ability to store the package in a flash partition. The Flash Driver is necessary to provide write access to flash memory and/or the file system from the OS.

3. `4907308` — 章 **4.4** OTA Client Architecture — 分 **0.344**
   > Flash Driver. Since the local DP shall be parsed by both the deployment manager and the installer modules, the flash driver shall support the ability to read the deployment package file and optionally store the individual component update files for installation. The Flash Driver is necessary to provide R/W access to flash memory from the OS.

4. `4907311` — 章 **4.4** OTA Client Architecture — 分 **0.255**
   > Flash driver. This component provides drivers to read and write flash memory. If the file system update is applicable it may contain a file system driver as well. Access to this component should be abstracted such that it is possible to use the update agent on multiple platforms and operating systems.

5. `4907483` — 章 **4.7.3.2** Silent Updates — 分 **0.224**
   > 2. After the deployment package is downloaded, its deployment shall start immediately.


---

### 16. `SWE1-FOTA-284` — Low Priority Execution of SWMC

- 所屬 Heading：`SWE1-FOTA-280` Interface Definitions
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-406`

**Requirement Description 全文**：

> WiFiUpdateService shall execute SWMC as a low-priority background process while OTA communication is active, ensuring that normal host system functions such as HMI, navigation, and radio are not impacted.

**路徑 A 前 5 候選**：

1. `4907440` — 章 **4.7.1** OTA Client Performance Requirements — 分 **0.561**
   > OTA client shall be a low priority process when active such that it does not impact normal functionality of the host system (ex, navigation/radio shall not be impacted).

2. `4907627` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.173**
   > The download process shall not initiate while hibernation mode is active for SRT vehicles.

3. `4907466` — 章 **4.7.3.1** Critical Updates — 分 **0.152**
   > An update can be defined as critical—the update runs on the host system in the background automatically.

4. `4907439` — 章 **4.7.1** OTA Client Performance Requirements — 分 **0.141**
   > OTA client MAY NOT negatively impact the HMI performance when an active management session or download session is in process.

5. `4907566` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.130**
   > Server-Initiated flow shall run in the background.


---

### 17. `SWE1-FOTA-034` — Enforce OTA Update Priority Order

- 所屬 Heading：`SWE1-FOTA-024` Critical Updates
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-386`

**Requirement Description 全文**：

> The WiFi Update Service shall classify OTA updates according to the priority order Critical, Regular, and Silent based on metadata received from the Download Descriptor (DD) provided through SWMC. The WiFi Update Service shall prevent installation of a lower priority update while a higher priority update session is pending or in progress. The WiFi Update Service shall schedule installation of lower priority updates only after all higher priority update sessions are completed or cleared through coordination with the Arbiter Service.

**路徑 A 前 5 候選**：

1. `4907457` — 章 **4.7.3** Main Update Configuration Options — 分 **0.428**
   > update priority shall be followed as listed below. lower priority updates shall not be installed until any pending higher priority updates are completed.1. Critical2. Regular3. Silent

2. `4907656` — 章 **4.11** User Experience (UX)/HMI — 分 **0.202**
   > User experience shall be same for all update types and updates (regular/critical/silent) SHOULD be configurable from the server so that the FOTA service administrator can select the relevant option depending on the type and urgency of the update being performed.

3. `4907460` — 章 **4.7.3** Main Update Configuration Options — 分 **0.158**
   > The OTA client SHOULD support configurable network priorities in order to limit data costs for download sessions. The following is the RECOMMENDED network priority (as example):

4. `4907806` — 章 **6** TBM Algorithm Requirements — 分 **0.154**
   > When TBM has completed the download of TBM FOTA Silent update package, then the TBM shall send $TBMUpdate$ = [Silent_Update]

5. `4907886` — 章 **9.1** Pre-Installation — 分 **0.152**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI


---

### 18. `SWE1-FOTA-176` — Restrict Silent Session Notifications to Safety-Required Cases

- 所屬 Heading：`SWE1-FOTA-170` Deployment Package Security
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-362`

**Requirement Description 全文**：

> During a Silent Update session, the WiFi Update Service shall not trigger the SW Update HMI for update progress notifications. During a Silent Update session, the WiFi Update Service shall allow user notification only when required to satisfy safety-related requirements.

**路徑 A 前 5 候選**：

1. `4907476` — 章 **4.7.3.2** Silent Updates — 分 **0.267**
   > Silent updates shall not display progress notifications and shall NOT require end-user interaction.

2. `4907486` — 章 **4.7.3.2** Silent Updates — 分 **0.258**
   > Silent update shall be applicable for all session flows.

3. `4907455` — 章 **4.7.3** Main Update Configuration Options — 分 **0.248**
   > Silent update: An update that does not display any notifications during the session (there is no end-user interaction)—the end-user cannot reject the update. Network bearer rules for minimizing download cost apply.

4. `4907477` — 章 **4.7.3.2** Silent Updates — 分 **0.247**
   > During silent sessions the user SHALL NOT be notified unless necessary for safety requirements.

5. `4907475` — 章 **4.7.3.2** Silent Updates — 分 **0.244**
   > Silent updates run automatically without any progress notifications or end user interaction.


---

### 19. `SWE1-FOTA-347` — Vehicle-Initiated Polling Interval Configuration

- 所屬 Heading：`SWE1-FOTA-309` OMA-DM Security
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-274`

**Requirement Description 全文**：

> The SWMC shall support a configurable polling interval for vehicle-initiated OTA update sessions with a default value of 24 hours.

**路徑 A 前 5 候選**：

1. `4907579` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.495**
   > The vehicle-initiated session shall have a reconfigurable polling interval of 24 hours.

2. `4907367` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.364**
   > The polling interval for periodic vehicle initiated operation shall be configurable from the server. See appendix B for more configurable intervals.

3. `4907366` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.353**
   > The polling interval for periodic vehicle initiated operation is RECOMMENDED to be configurable from the server. See appendix B for more configurable intervals.

4. `4907580` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.315**
   > The polling interval for vehicle-initaited session shall always be reconfigurable and set in 'HOURS' format.

5. `4907370` — 章 **4.5.4** OTA server initiated sessions — 分 **0.246**
   > OTA client shall support an event interface in order to receive server initiated sessions.


---

### 20. `SWE1-FOTA-332` — OTA Session Report Resend

- 所屬 Heading：`SWE1-FOTA-309` OMA-DM Security
- Sub Categorization：Service｜Source Requirement ID：`SYS-RA-FOTA-210`

**Requirement Description 全文**：

> The SWMC shall resend the saved OTA session report when the cause of the interruption is resolved.

**路徑 A 前 5 候選**：

1. `4907688` — 章 **4.12.2** Report Persistency — 分 **0.315**
   > If the OTA client knows when the cause of the interrupt is removed (for example, the end-user enabled connectivity), the client shall attempt to resend the report as soon as the cause of the interrupt no longer exists.

2. `4907689` — 章 **4.12.2** Report Persistency — 分 **0.245**
   > In the event that the cause of the interrupt and resume of service are not known to the OTA client (for example, the DM Server went down and the OTA client has no indication that the network is back up until it tries to connect to the server), the OTA client shall try to resend the report according to the configured retry parameter.

3. `4907673` ⚠**A-SU4 污染** — 章 **4.12** Interrupt Handling — 分 **0.201**
   > Table 4-6 shows the OTA client action, depending on the session state, after a resolved interruption. These are RECOMMENDED actions; however the interrupts themselves shall be gracefully handled so that the OTA client continues operation. 4907674: [Artifact Type:Description] [State:Approved] [ECU:LTM, ETM] [Market:All] [Model Year:2023, 2024, 2025, 2020, 2018, 2019, 2021, 2022, 2017] [Radio:R1L, R…

4. `4907686` — 章 **4.12.2** Report Persistency — 分 **0.192**
   > The OTA client shall send a report to the OTA server when the session completes, whether successfully or with a failure.

5. `4907402` — 章 **4.6.1** Connection to Wi-Fi network — 分 **0.171**
   > The HU shall establish a Wi-Fi connection with saved Wi-Fi networks for OTA updates

