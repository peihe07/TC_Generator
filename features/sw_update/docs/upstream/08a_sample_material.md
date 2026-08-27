# 上繳包 08a —— T22d 地面真值擴充材料（30 列）

> 主包：`08_corpus_v2.md`。本檔為材料傾印，**執行層不作任何對應判斷**。
>
> 候選之分數與全文皆出自**語料 v2**（A-SU4 處分 §二，43 個 Description 已併入宿主）。
> **A-SU4 之污染已消除**，本批無 `⚠A-SU4 污染` 標記。

取樣：`292` 1 列、`309` 群另 8、`214` 群 6、`137` 群 6、`110` 群 3，其餘自 `random.Random(2).sample(pool, n)`。**執行層不作判斷。**


---

### 1. `SWE1-FOTA-292` — Configurable Network Priority Support

- Heading：`SWE1-FOTA-291` Bearer selection:｜Sub Cat：Service｜Source：`SYS-RA-FOTA-384`

**Requirement Description 全文**：

> WiFiUpdateService shall manage the configured network priority and select the appropriate network for OTA communication. WiFiUpdateService shall establish the network connection and enable SWMC to communicate with the OTA Server

**路徑 A（語料 v2）前 5 候選**：

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

### 2. `SWE1-FOTA-317` — User-Initiated Network Deactivation Handling

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-192`

**Requirement Description 全文**：

> The WiFiUpdateService shall handle user-initiated deactivation of mobile data usage or an active Wi-Fi connection reported by SWMC during OTA server communication, flashing, or software component update.

**路徑 A（語料 v2）前 5 候選**：

1. `4907669` — 章 **4.12** Interrupt Handling — 分 **0.346**
   > 3. The end-user deactivates data usage or active Wi-Fi connection

2. `4907665` — 章 **4.12** Interrupt Handling — 分 **0.190**
   > There are several kinds of interrupts that can be handled while an OTA client is connected to the OTA server and while flashing or updating a software component. This section describes how to handle interrupts and how the client should interact with the OTA server when interrupts are resolved.

3. `4907567` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.187**
   > Server initiated session - Communication between FOTA Client &amp; TC

4. `4907559` — 章 **4.10.1** Self Registration Flow — 分 **0.179**
   > 1. The OTA client runs the server-initiated session, client-initiated session or user-initiated session.

5. `4907301` — 章 **4.4** OTA Client Architecture — 分 **0.164**
   > Data connection &amp; Socket interface. This component is the same as for the Vehicle Manager. It provides the connectivity to the server.


---

### 3. `SWE1-FOTA-318` — Emergency State Handling

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-193`

**Requirement Description 全文**：

> The WiFiUpdateService shall handle the vehicle emergency state (accident detection) notified by the appropriate system component during OTA server communication, flashing, or software component update.

**路徑 A（語料 v2）前 5 候選**：

1. `4907670` — 章 **4.12** Interrupt Handling — 分 **0.575**
   > 4. The vehicle is in an emergency state(accident detection)

2. `4907665` — 章 **4.12** Interrupt Handling — 分 **0.220**
   > There are several kinds of interrupts that can be handled while an OTA client is connected to the OTA server and while flashing or updating a software component. This section describes how to handle interrupts and how the client should interact with the OTA server when interrupts are resolved.

3. `4907524` — 章 **4.9.1** Update Agent Requirements — 分 **0.198**
   > Update Agent component shall be able to handle both file system and binary image updates.

4. `4907368` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.178**
   > Detection of ECU configuration changes, such as detection of manual diagnostic reflash or component replacement by service technician SHALL trigger a vehicle initiated session. This trigger shall be handled with the same event based interface into the OTA client.01

5. `4907642` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.160**
   > Emergency Call shall be functional at all times during the download and post installation process.


---

### 4. `SWE1-FOTA-319` — Power Loss Handling

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-194`

**Requirement Description 全文**：

> The WiFiUpdateService shall coordinate the handling of condition during OTA server communication, flashing, or software component update by interacting with SWMC and the appropriate installer component.

**路徑 A（語料 v2）前 5 候選**：

1. `4907380` — 章 **4.5.4.1** SMS/MQTT Push Support — 分 **0.174**
   > Communication and update implementation to individual components shall be the responsibility of the implementation of the abstracted installer of the relevant component type. Some examples would be the application installer providing an application to the host OS's application manager or an ECU update installer managing the serial communication with HU daughter board required for re-flash.

2. `4907707` — 章 **4.13.1** SCOMO Support — 分 **0.173**
   > OTA client shall support hand off ECU components to appropriate ECU installers for individual bus communication. 4. Map Update Data(MOTA): The OTA client shall be able to install map updates, which the OTA server provides in a deployment package format. The OTA client shall support hand off to a Map management installer

3. `4907361` — 章 **4.5.2** User initiated sessions — 分 **0.168**
   > OTA client SHALL define event handling interface for communication with HMI and be able to respond to user input for support of these requirements.

4. `4907665` — 章 **4.12** Interrupt Handling — 分 **0.166**
   > There are several kinds of interrupts that can be handled while an OTA client is connected to the OTA server and while flashing or updating a software component. This section describes how to handle interrupts and how the client should interact with the OTA server when interrupts are resolved.

5. `4907590` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.155**
   > 8. After installation pre-condition check the OTA client shall parse the deployment package and invoke installers (see Deployment Flow) and update agents for the component types in the deployment package, to deploy the software updates.


---

### 5. `SWE1-FOTA-320` — Host System Disconnection Handling

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-195`

**Requirement Description 全文**：

> The WiFiUpdateService shall detect end-user physical disconnection of the host system (HU/TBM) during OTA server communication, flashing, or software component update and notify SWMC. The SWMC shall handle the OTA session based on the notification and report the update status to the WiFiUpdateService.

**路徑 A（語料 v2）前 5 候選**：

1. `4907279` — 章 **4.2.3** HU FOTA with TBM — 分 **0.174**
   > When TBM receives a notification from the server that an update is available, the TBM shall send $HUReflash$ = [Update Available] to the HU.

2. `4907665` — 章 **4.12** Interrupt Handling — 分 **0.161**
   > There are several kinds of interrupts that can be handled while an OTA client is connected to the OTA server and while flashing or updating a software component. This section describes how to handle interrupts and how the client should interact with the OTA server when interrupts are resolved.

3. `4907802` — 章 **6** TBM Algorithm Requirements — 分 **0.154**
   > When TBM has completed the download of a FOTA update with notification package, then the TBM shall send $TBMUpdate$ = [Update_Available]

4. `4907811` — 章 **6** TBM Algorithm Requirements — 分 **0.151**
   > During any Ignition conditions, When an update installation has been successfully completed, then the TBM shall send $TBMUpdate$ = [Update_End] for &lt;T_FOTA_END&gt;

5. `4907606` — 章 **4.10.5** Deployment Flow — 分 **0.147**
   > 5. The installers then notify the OTA client of their update status, in the event of a failure they also provide individual ECU DP status codes.


---

### 6. `SWE1-FOTA-321` — Interruption Recovery Handling

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-196`

**Requirement Description 全文**：

> The WiFiUpdateService shall detect the resolution of an interruption and notify SWMC to continue the OTA update session based on the current session state. The SWMC shall gracefully handle the interruption and continue operation in accordance with the session state.

**路徑 A（語料 v2）前 5 候選**：

1. `4907673` — 章 **4.12** Interrupt Handling — 分 **0.220**
   > Table 4-6 shows the OTA client action, depending on the session state, after a resolved interruption. These are RECOMMENDED actions; however the interrupts themselves shall be gracefully handled so that the OTA client continues operation. Table 4-6: Interrupt Handling for Recoverable Interrupts State Action Before management session 1 Abort the session. 2 Start the retry mechanism. The OTA client …

2. `4907554` — 章 **4.10** Session Flows — 分 **0.183**
   > If an interruption occurs during any of the steps before the download completes successfully, the OTA client shall save the state of the download, and shall retry to resume the download.

3. `4907591` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.178**
   > 9. If an interruption occurs during any of the steps before the installation completes successfully, the OTA client shall save the state of the installation, and shall retry to resume the installation.

4. `4907320` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.160**
   > OTA client shall have access to diagnostic information about the current state of the vehicle, including ignition state, battery voltage, vehicle speed, current draw, and others as determined by a pre-condition script for the specific vehicle.

5. `4907645` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.146**
   > In case the vehicle is driven during the installation, the update shall continue until complete.


---

### 7. `SWE1-FOTA-322` — Insufficient Storage Space Handling

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-198`

**Requirement Description 全文**：

> The WiFiUpdateService shall detect insufficient storage space on the target unit before or during the software update process and notify SWMC. The SWMC shall abort the current OTA update session and report the failure to the OTA server.

**路徑 A（語料 v2）前 5 候選**：

1. `4907676` — 章 **4.12** Interrupt Handling — 分 **0.369**
   > In the event that there is insufficient space on the unit hosting the OTA client for storing the deployment package after receiving the size of the package in the download descriptor (DD), the client shall abort the current session and report the failure to the server. The server MAY report back to the client a message for the user on how to resolve.

2. `4907686` — 章 **4.12.2** Report Persistency — 分 **0.220**
   > The OTA client shall send a report to the OTA server when the session completes, whether successfully or with a failure.

3. `4907673` — 章 **4.12** Interrupt Handling — 分 **0.178**
   > Table 4-6 shows the OTA client action, depending on the session state, after a resolved interruption. These are RECOMMENDED actions; however the interrupts themselves shall be gracefully handled so that the OTA client continues operation. Table 4-6: Interrupt Handling for Recoverable Interrupts State Action Before management session 1 Abort the session. 2 Start the retry mechanism. The OTA client …

4. `4907687` — 章 **4.12.2** Report Persistency — 分 **0.165**
   > If an interrupt occurs before a report is sent to the OTA server and acknowledged, the OTA client shall save the report and wait until the report can be resent.

5. `4907606` — 章 **4.10.5** Deployment Flow — 分 **0.145**
   > 5. The installers then notify the OTA client of their update status, in the event of a failure they also provide individual ECU DP status codes.


---

### 8. `SWE1-FOTA-323` — Concurrent NIA Handling

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-199`

**Requirement Description 全文**：

> The SWMC shall queue an incoming NIA received during an active OTA update session without interrupting the current session and shall process the queued NIA after the active session is completed.

**路徑 A（語料 v2）前 5 候選**：

1. `4907677` — 章 **4.12** Interrupt Handling — 分 **0.553**
   > If a session is active and the vehicle receives an additional NIA, the OTA client ignores the notification and queues it without interrupting the current active session.

2. `4907439` — 章 **4.7.1** OTA Client Performance Requirements — 分 **0.269**
   > OTA client MAY NOT negatively impact the HMI performance when an active management session or download session is in process.

3. `4907565` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.199**
   > Server-initiated sessions shall start automatically after the OTA server sends an NIA via SMS or MQTT to the OTA client.

4. `4907575` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.186**
   > 1. “Shoulder tap” message is received and queued by the OTA client.

5. `4907582` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.182**
   > 1. Vehicle polling timer causes a vehicle-initiated session to be queued.


---

### 9. `SWE1-FOTA-324` — Partial Download Preservation

- Heading：`SWE1-FOTA-309` OMA-DM Security｜Sub Cat：Service｜Source：`SYS-RA-FOTA-201`

**Requirement Description 全文**：

> The SWMC shall preserve the partially downloaded deployment package when an interruption occurs before the download is completed to support continuation of the OTA update session.

**路徑 A（語料 v2）前 5 候選**：

1. `4907679` — 章 **4.12.1** Resuming a Download — 分 **0.499**
   > If an interrupt occurs before a download completes, the OTA client shall save the partially downloaded deployment package.

2. `4907554` — 章 **4.10** Session Flows — 分 **0.290**
   > If an interruption occurs during any of the steps before the download completes successfully, the OTA client shall save the state of the download, and shall retry to resume the download.

3. `4907591` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.238**
   > 9. If an interruption occurs during any of the steps before the installation completes successfully, the OTA client shall save the state of the installation, and shall retry to resume the installation.

4. `4907471` — 章 **4.7.3.1** Critical Updates — 分 **0.233**
   > 2. When the deployment package is downloaded, the OTA client shall display a deployment confirmation screen. The deployment shall start after a confirmation screen or when a timeout occurs.

5. `4907680` — 章 **4.12.1** Resuming a Download — 分 **0.229**
   > If an interrupt occurs before a download completes, the OTA client shall suspend the session, write to the log, and wait until the download can resume.


---

### 10. `SWE1-FOTA-215` — Trigger TBM Update Check on Scheduled Event

- Heading：`SWE1-FOTA-214` HU FOTA with TBM｜Sub Cat：Service｜Source：`SYS-RA-FOTA-505`

**Requirement Description 全文**：

> The TBM Update Service shall detect the scheduled update-check trigger for TBM FOTA. Upon trigger, the TBM Update Service shall set $HUFOTACheck$ = [Check for updates] and transmit the signal to TBM through TBM FW Service.

**路徑 A（語料 v2）前 5 候選**：

1. `4907281` — 章 **4.2.3** HU FOTA with TBM — 分 **0.494**
   > If FOTA Client on the HU is scheduled for a check for the update the HU shall send $HUFOTACheck$ = [Check for updates] to the TBM.

2. `4907368` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.270**
   > Detection of ECU configuration changes, such as detection of manual diagnostic reflash or component replacement by service technician SHALL trigger a vehicle initiated session. This trigger shall be handled with the same event based interface into the OTA client.01

3. `4907809` — 章 **6** TBM Algorithm Requirements — 分 **0.229**
   > During $PowerMode$ = [IGN_LK], IF TBM receives $UpdateAction$ = [Update_Now] OR a Silent Update is ready to install, thenStart TBM FOTA Update procedure-TBM shall set &lt;POSTPONE_TIME&gt; = [0]-TBM shall set $TBMUpdate$ = [Update_Start]

4. `4907806` — 章 **6** TBM Algorithm Requirements — 分 **0.224**
   > When TBM has completed the download of TBM FOTA Silent update package, then the TBM shall send $TBMUpdate$ = [Silent_Update]

5. `4907802` — 章 **6** TBM Algorithm Requirements — 分 **0.215**
   > When TBM has completed the download of a FOTA update with notification package, then the TBM shall send $TBMUpdate$ = [Update_Available]


---

### 11. `SWE1-FOTA-216` — Trigger Server Update Check on HUReflash Availability Signal

- Heading：`SWE1-FOTA-214` HU FOTA with TBM｜Sub Cat：Service｜Source：`SYS-RA-FOTA-506/SYS-RA-FOTA-507`

**Requirement Description 全文**：

> When $TBM_present$ = [present], the SWMC shall perform OTA server update availability checks for the TBM FOTA session. When the OTA server reports an available TBM update, the SWMC shall notify the TBM Update Service. Upon receiving update availability status from SWMC, the TBM Update Service shall set $HUReflash$ = [Update Available] and shall initiate the TBM FOTA update

**路徑 A（語料 v2）前 5 候選**：

1. `4907279` — 章 **4.2.3** HU FOTA with TBM — 分 **0.354**
   > When TBM receives a notification from the server that an update is available, the TBM shall send $HUReflash$ = [Update Available] to the HU.

2. `4907776` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.301**
   > These requirements are valid if $TBM_present$ = [present]

3. `4907278` — 章 **4.2.3** HU FOTA with TBM — 分 **0.301**
   > These requirements are valid if $TBM_present$ = [present]

4. `4907280` — 章 **4.2.3** HU FOTA with TBM — 分 **0.254**
   > If HU receives $HUReflash$ = [Update Available], HU shall check the server if to check for an update.

5. `4907802` — 章 **6** TBM Algorithm Requirements — 分 **0.244**
   > When TBM has completed the download of a FOTA update with notification package, then the TBM shall send $TBMUpdate$ = [Update_Available]


---

### 12. `SWE1-FOTA-217` — Prioritize FOTA Updates Based on Defined Update Type Hierarchy

- Heading：`SWE1-FOTA-214` HU FOTA with TBM｜Sub Cat：Service｜Source：`SYS-RA-FOTA-518`

**Requirement Description 全文**：

> The Arbiter Service shall detect the availability of multiple FOTA update types including Rest of Vehicle FOTA, HU FOTA, TBM FOTA, and Map OTA updates. When two or more update types are available simultaneously, the Arbiter Service shall determine update execution priority using the following order: Rest of Vehicle FOTA updates HU FOTA updates TBM FOTA updates Map OTA updates The Arbiter Service shall permit execution of only the highest priority update session and shall defer lower priority update sessions until the active higher priority update is completed or cleared. The WiFi Update Service, TBM Update Service, ROV Update Service, and Map Update Service shall execute or defer update processing according to the priority decision provided by the Arbiter Service.

**路徑 A（語料 v2）前 5 候選**：

1. `4907258` — 章 **2** Common Reflash Requirements — 分 **0.302**
   > When two or more different types of FOTA updates are available for installation at the same time, the HU shall honor the FOTA updates based on priority as below.1.FOTA Rest of the Vehicle updates2.HU FOTA3.TBM FOTA4. Maps over-the-air updates

2. `4907457` — 章 **4.7.3** Main Update Configuration Options — 分 **0.281**
   > update priority shall be followed as listed below. lower priority updates shall not be installed until any pending higher priority updates are completed.1. Critical2. Regular3. Silent

3. `4907837` — 章 **8** Maps Over-the-air Updates (MOTA) — 分 **0.210**
   > FOTA update has priority over MOTA. The HU shall notify the MOTA Client to restrict a MOTA update, when processing FOTA update

4. `4907802` — 章 **6** TBM Algorithm Requirements — 分 **0.194**
   > When TBM has completed the download of a FOTA update with notification package, then the TBM shall send $TBMUpdate$ = [Update_Available]

5. `4907656` — 章 **4.11** User Experience (UX)/HMI — 分 **0.192**
   > User experience shall be same for all update types and updates (regular/critical/silent) SHOULD be configurable from the server so that the FOTA service administrator can select the relevant option depending on the type and urgency of the update being performed.


---

### 13. `SWE1-FOTA-218` — Maintain FMVSS 111 Rear Visibility Compliance During FOTA

- Heading：`SWE1-FOTA-214` HU FOTA with TBM｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-519`

**Requirement Description 全文**：

> The SW Update HMI and WiFi Update Service logic shall ensure that rear-visibility related software functions required for FMVSS 111 compliance, including backup camera display availability, video continuity, and mandatory overlays, remain operational during all phases of software update execution.

**路徑 A（語料 v2）前 5 候選**：

1. `4907255` — 章 **2** Common Reflash Requirements — 分 **0.221**
   > During all FOTA processes, the system shall be compliant with FMVSS 111.

2. `4907253` — 章 **2** Common Reflash Requirements — 分 **0.214**
   > While the backup camera is displayed, the radio shall support all of the standard overlays

3. `4907252` — 章 **2** Common Reflash Requirements — 分 **0.176**
   > While the backup camera is displayed, the radio shall not interrupt the backup camera feed during a radio reflash event.

4. `4907243` — 章 **2** Common Reflash Requirements — 分 **0.176**
   > The radio shall display the backup camera and specified overlays within two seconds of detecting that the vehicle is in reverse gear.

5. `4907254` — 章 **2** Common Reflash Requirements — 分 **0.174**
   > If a reboot is required during a radio update, the backup camera shall still be fully functional within two seconds.


---

### 14. `SWE1-FOTA-219` — Preserve Backup Camera Availability During Update Reboot

- Heading：`SWE1-FOTA-214` HU FOTA with TBM｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-520`

**Requirement Description 全文**：

> The SW Update HMI and WiFi Update Service logic shall defer non-emergency reboot execution requested during software update when reverse gear is active. If reboot execution proceeds, the assigned update service shall restore backup camera functionality and associated display path within 2 seconds of reverse gear detection.

**路徑 A（語料 v2）前 5 候選**：

1. `4907243` — 章 **2** Common Reflash Requirements — 分 **0.374**
   > The radio shall display the backup camera and specified overlays within two seconds of detecting that the vehicle is in reverse gear.

2. `4907254` — 章 **2** Common Reflash Requirements — 分 **0.307**
   > If a reboot is required during a radio update, the backup camera shall still be fully functional within two seconds.

3. `4907670` — 章 **4.12** Interrupt Handling — 分 **0.179**
   > 4. The vehicle is in an emergency state(accident detection)

4. `4907252` — 章 **2** Common Reflash Requirements — 分 **0.161**
   > While the backup camera is displayed, the radio shall not interrupt the backup camera feed during a radio reflash event.

5. `4907701` — 章 **4.13.1** SCOMO Support — 分 **0.150**
   > The OTA client shall reboot if required for updating firmware on the host ECU.


---

### 15. `SWE1-FOTA-220` — Prevent Backup Camera Feed Interruption During Reflash

- Heading：`SWE1-FOTA-214` HU FOTA with TBM｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-522`

**Requirement Description 全文**：

> The SW Update HMI and WiFi Update Service logic shall prevent software reflash activities from interrupting the active backup camera video feed and shall preserve backup camera display priority while the reverse camera view is active during a radio reflash event.

**路徑 A（語料 v2）前 5 候選**：

1. `4907252` — 章 **2** Common Reflash Requirements — 分 **0.583**
   > While the backup camera is displayed, the radio shall not interrupt the backup camera feed during a radio reflash event.

2. `4907253` — 章 **2** Common Reflash Requirements — 分 **0.360**
   > While the backup camera is displayed, the radio shall support all of the standard overlays

3. `4907243` — 章 **2** Common Reflash Requirements — 分 **0.310**
   > The radio shall display the backup camera and specified overlays within two seconds of detecting that the vehicle is in reverse gear.

4. `4907254` — 章 **2** Common Reflash Requirements — 分 **0.268**
   > If a reboot is required during a radio update, the backup camera shall still be fully functional within two seconds.

5. `4907244` — 章 **2** Common Reflash Requirements — 分 **0.181**
   > The radio shall meet the requirement ID 4907243 during a radio reflash event irrespective of update method. i.e. USB vs FOTA and MOTA**If equipped


---

### 16. `SWE1-FOTA-138` — Extract Deployment Package and Route Component Packages

- Heading：`SWE1-FOTA-137` Deployment flow｜Sub Cat：Service｜Source：`SYS-RA-FOTA-231`

**Requirement Description 全文**：

> The WiFi Update Service shall analyze the deployment package and perform preliminary analysis of the package manifest to identify the component packages included in the deployment package. The WiFi Update Service shall extract the component packages and determine the appropriate installation method for each component type. The WiFi Update Service shall forward MCPU update packages to the Update Engine for installation. The WiFi Update Service shall forward peripheral component packages to the SW Updater Manager and SW Updater Service to SW Updater HAL for peripheral update installation processing.

**路徑 A（語料 v2）前 5 候選**：

1. `4907605` — 章 **4.10.5** Deployment Flow — 分 **0.210**
   > 4. Deployment package is parsed for preliminary analysis and the relevant installers are invoked to (optionally extract and) install the updates in the package using the installation methods relevant for the different component types addressed by each installer

2. `4907513` — 章 **4.8.3** Deployment Package Security — 分 **0.183**
   > The OTA client shall support handling of FCA signed deployment packages.

3. `4907331` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.182**
   > Download Manager component of the OTA client shall support reliable download of the deployment package.

4. `4907341` — 章 **4.4.2** OTA Client Configuration options — 分 **0.157**
   > OTA client shall support handling of deployment packages regardless of transport mechanism.

5. `4907590` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.149**
   > 8. After installation pre-condition check the OTA client shall parse the deployment package and invoke installers (see Deployment Flow) and update agents for the component types in the deployment package, to deploy the software updates.


---

### 17. `SWE1-FOTA-139` — Collect Installer Status and Report ECU Failure Codes

- Heading：`SWE1-FOTA-137` Deployment flow｜Sub Cat：Service｜Source：`SYS-RA-FOTA-232`

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

### 18. `SWE1-FOTA-140` — Determine Installation Start Time After Download

- Heading：`SWE1-FOTA-137` Deployment flow｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-234`

**Requirement Description 全文**：

> After the update downloaded, SWMC need to determine when it shall proceed to the depolyment with precondition mentioned. The WiFi Update Service shall verify that user approval is received through the HMI when user approval is required. The WiFi Update Service shall verify that the server-defined installation time slot is active. The WiFi Update Service shall verify that ignition conditions satisfy the deployment policy. The WiFi Update Service shall verify that the battery voltage exceeds the configured minimum threshold. The WiFi Update Service shall verify that the host system current draw exceeds the configured minimum threshold.

**路徑 A（語料 v2）前 5 候選**：

1. `4907609` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.498**
   > After an update is downloaded, the OTA client will need to determine when a deployment can proceed. By default, a deployment proceeds after the end-user has given approval, during a time slot specified by the server, the ignition conditions are met, the battery voltage is above a minimum threshold, the current draw of the host system is above a minimum threshold.

2. `4907514` — 章 **4.8.3** Deployment Package Security — 分 **0.172**
   > The OTA client shall verify integrity of the deployment package once it is received from the server, immediately post download.

3. `4907398` — 章 **4.6** OTA download via Wi-Fi — 分 **0.141**
   > Pre Conditions for FOTA via Wifi:➢ Vehicle’s battery is above 65% State of Charge ($IBS_SOC$ &gt; [65]). If $IBS_SOC$ not available in the vehicle's DBC check: Vehicle in with motor running ($OperationalModeSts$ = [Ignition_On_Engine_On]) for 30 minutes.➢ Ignition position is OFF ($PowerMode$ = [IGN_OFF]).

4. `4907604` — 章 **4.10.5** Deployment Flow — 分 **0.138**
   > 3. Deployment package signature verification is done to verify authenticity of the package.

5. `4907320` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.136**
   > OTA client shall have access to diagnostic information about the current state of the vehicle, including ignition state, battery voltage, vehicle speed, current draw, and others as determined by a pre-condition script for the specific vehicle.


---

### 19. `SWE1-FOTA-141` — Display Update Message and Reconfirm Package Before Installation

- Heading：`SWE1-FOTA-137` Deployment flow｜Sub Cat：Service｜Source：`SYS-RA-FOTA-239`

**Requirement Description 全文**：

> The WiFi Update Service shall extract the update message text from the Download Descriptor metadata Downloaded via SWMC and provide the message content to the SW Update HMI. The SW Update HMI shall display the update message together with the installation notification and installation action options when HMI interaction is supported. After the user accepts the installation through the SW Update HMI, the WiFi Update Service shall revalidate deployment package authenticity and integrity before installation initiation.

**路徑 A（語料 v2）前 5 候選**：

1. `4907614` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.323**
   > The update message from the message tag of Download Descriptor file to be shown to the consumer (if an HMI is shown for the update) along with the notification for the installation. Once user has accepted installation, system shall reconfirm file authenticity and completeness.

2. `4907515` — 章 **4.8.3** Deployment Package Security — 分 **0.202**
   > The OTA client shall ensure integrity of the deployment package before it is installed, immediately pre installation.

3. `4907316` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.202**
   > The OTA client shall be able to display download descriptor information to the HMI, if available, including text description and update size.

4. `4907867` — 章 **8.3** User Initiated Updates — 分 **0.173**
   > NAV shall provide capability for the user to download an available Map update through the HMI.

5. `4907662` — 章 **4.11** User Experience (UX)/HMI — 分 **0.169**
   > After the download is complete, the user is shown the deployment package details, the HMI SHOULD provide the user with opt in options: Install or schedule later.Kindly see the latest HMI for pop up.


---

### 20. `SWE1-FOTA-142` — Execute Background Download Without Customer Visibility

- Heading：`SWE1-FOTA-137` Deployment flow｜Sub Cat：Service｜Source：`SYS-RA-FOTA-242`

**Requirement Description 全文**：

> The WiFi Update Service shall perform deployment package download in background mode through the SWMC. The WiFi Update Service shall not trigger SW Update HMI to present customer-facing progress of deployment package download process.

**路徑 A（語料 v2）前 5 候選**：

1. `4907618` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.344**
   > Download of the file shall not be customer facing.

2. `4907333` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.236**
   > If HMI is available, OTA client shall be able to update the HMI of the download progress.

3. `4907300` — 章 **4.4** OTA Client Architecture — 分 **0.212**
   > Download Agent is responsible for reliable downloading of the deployment package (DP) from the URL provided in the deployment package download descriptor (DD), and providing information about download progress.

4. `4907481` — 章 **4.7.3.2** Silent Updates — 分 **0.202**
   > 1. The download of the deployment package shall start automatically.

5. `4907331` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.187**
   > Download Manager component of the OTA client shall support reliable download of the deployment package.


---

### 21. `SWE1-FOTA-143` — Continue Download During IGN OFF Extended Wake Period

- Heading：`SWE1-FOTA-137` Deployment flow｜Sub Cat：Service｜Source：`SYS-RA-FOTA-243`

**Requirement Description 全文**：

> The WiFi Update Service shall monitor ignition status using CarProperty Manager and $PowerMode$ using CarPower Manager. When an active deployment package download session,$PowerMode$ transitions to IGN_OFF state, the WiFi Update Service shall request extended wake mode to continue the package download for a maximum period of 30 minutes after key-off. If the deployment package download is incomplete when the extended wake period expires, the WiFi Update Service shall terminate the download session.

**路徑 A（語料 v2）前 5 候選**：

1. `4907619` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.264**
   > Once the download has started, it may be allowed to continue for an 'additional extended time' during Resume Mode while ignition is in OFF position. This 'additional extended time' is equal to no more than 30 minutes after key off.

2. `4907398` — 章 **4.6** OTA download via Wi-Fi — 分 **0.237**
   > Pre Conditions for FOTA via Wifi:➢ Vehicle’s battery is above 65% State of Charge ($IBS_SOC$ &gt; [65]). If $IBS_SOC$ not available in the vehicle's DBC check: Vehicle in with motor running ($OperationalModeSts$ = [Ignition_On_Engine_On]) for 30 minutes.➢ Ignition position is OFF ($PowerMode$ = [IGN_OFF]).

3. `4907620` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.222**
   > Once the download has started, it may be allowed to continue for an 'additional extended time' while ignition is in OFF position. This 'additional extended time' is equal to no more than 30 minutes after key off. Note: Please refer to CFTS009 for more details on Power modes

4. `4907331` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.221**
   > Download Manager component of the OTA client shall support reliable download of the deployment package.

5. `4907415` — 章 **4.6.2** Non-Critical Updates — 分 **0.195**
   > HU shall start the timer for download via Wi-Fi at ignition off when timed mode has expired. HU shall terminate the download session for the duration of ignition cycle after T = 30 minutes has expired and switch back to host mode.


---

### 22. `SWE1-FOTA-111` — Enable TBM Update Functions Only When TBM Is Present

- Heading：`SWE1-FOTA-110` TBM FOTA Reflash｜Sub Cat：Service｜Source：`SYS-RA-FOTA-152`

**Requirement Description 全文**：

> The TBM Update Service shall retrieve $TBM_present$ using CarPropertyManager. If $TBM_present$ = [present], the TBM Update Service shall allow execution of TBM-specific FOTA functionalities.

**路徑 A（語料 v2）前 5 候選**：

1. `4907776` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.475**
   > These requirements are valid if $TBM_present$ = [present]

2. `4907278` — 章 **4.2.3** HU FOTA with TBM — 分 **0.475**
   > These requirements are valid if $TBM_present$ = [present]

3. `4907806` — 章 **6** TBM Algorithm Requirements — 分 **0.232**
   > When TBM has completed the download of TBM FOTA Silent update package, then the TBM shall send $TBMUpdate$ = [Silent_Update]

4. `4907802` — 章 **6** TBM Algorithm Requirements — 分 **0.222**
   > When TBM has completed the download of a FOTA update with notification package, then the TBM shall send $TBMUpdate$ = [Update_Available]

5. `4907397` — 章 **4.6** OTA download via Wi-Fi — 分 **0.215**
   > For TBM to HU Wi-Fi client requirement Kindly see section ID 4762830 : Wi-Fi Client Mode Connection, present in CFTS021_Connection Manager.


---

### 23. `SWE1-FOTA-112` — Display TBM Update Available Pop-up with Metadata

- Heading：`SWE1-FOTA-110` TBM FOTA Reflash｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-149`

**Requirement Description 全文**：

> The TBM Update Service shall retrieve $TBM_Update$ using the TBM FW Service and detect when the value indicates Update_Available. The TBM Update Service shall retrieve update metadata, including estimated installation time and “What’s New” information, via the TBM FW Service. If $TBM_Update$ = [Update_Available] and the update metadata is successfully retrieved, the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall display the TBM FOTA update available pop-up .

**路徑 A（語料 v2）前 5 候選**：

1. `4907780` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.426**
   > When HU receives $TBM_Update$ = [Update_Available] AND successfully receives information of WhatsNew and Estimated time for the TBM Software update from GSDP, then the HU shall display TBM FOTA update available pop-up. Please refer to the HMI L&amp;F.

2. `4907783` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.287**
   > When HU receives $TBMupdate$ = [Update_Available] from the from TBM, on ignition off the HU shall show the TBM FOTA update pop-up screen to the user. Kindly see the HMI.

3. `4907802` — 章 **6** TBM Algorithm Requirements — 分 **0.281**
   > When TBM has completed the download of a FOTA update with notification package, then the TBM shall send $TBMUpdate$ = [Update_Available]

4. `4907782` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.272**
   > HU shall display Estimated time for the TBM Software update based on the information received from the GSDP. Please refer to the HMI L&amp;F.

5. `4907279` — 章 **4.2.3** HU FOTA with TBM — 分 **0.264**
   > When TBM receives a notification from the server that an update is available, the TBM shall send $HUReflash$ = [Update Available] to the HU.


---

### 24. `SWE1-FOTA-113` — Display TBM Update Available Pop-up on Ignition OFF

- Heading：`SWE1-FOTA-110` TBM FOTA Reflash｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-146`

**Requirement Description 全文**：

> The TBM Update Service shall retrieve $TBMUpdate$ using the TBM FW Service and detect when the value indicates Update_Available. The TBM Update Service shall retrieve OperationalModeSts using CarPropertyManager. If $TBMupdate$ = [Update_Available] and OperationalModeSts transitions from Body ON to Body OFF, the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall display the TBM FOTA update available pop-up to the user.

**路徑 A（語料 v2）前 5 候選**：

1. `4907783` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.379**
   > When HU receives $TBMupdate$ = [Update_Available] from the from TBM, on ignition off the HU shall show the TBM FOTA update pop-up screen to the user. Kindly see the HMI.

2. `4907802` — 章 **6** TBM Algorithm Requirements — 分 **0.336**
   > When TBM has completed the download of a FOTA update with notification package, then the TBM shall send $TBMUpdate$ = [Update_Available]

3. `4907806` — 章 **6** TBM Algorithm Requirements — 分 **0.290**
   > When TBM has completed the download of TBM FOTA Silent update package, then the TBM shall send $TBMUpdate$ = [Silent_Update]

4. `4907780` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.286**
   > When HU receives $TBM_Update$ = [Update_Available] AND successfully receives information of WhatsNew and Estimated time for the TBM Software update from GSDP, then the HU shall display TBM FOTA update available pop-up. Please refer to the HMI L&amp;F.

5. `4907790` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.278**
   > When HU receives $TBMUpdate$ = [Update_End], HU shall display TBM update success pop-up. Please refer to the HMI L&amp;F.


---

### 25. `SWE1-FOTA-044` — Display Password-Protected Wi-Fi Networks in Range

- Heading：`SWE1-FOTA-038` OTA download via Wi-Fi｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-036`

**Requirement Description 全文**：

> The WiFi Update Service shall retrieve the list of available Wi-Fi networks from WiFi Manager after completion of a Wi-Fi scan operation. The WiFi Update Service shall identify password-protected Wi-Fi networks with the help of WiFi Manager from the available Wi-Fi network list based on the network security type. The WiFi Manager shall provide the list of password-protected Wi-Fi networks to the HMI. The HMI shall display the password-protected Wi-Fi networks that are within Wi-Fi range.

**路徑 A（語料 v2）前 5 候選**：

1. `4907423` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.502**
   > User shall be able to see all the password protected networks that are in range of the Wi-Fi

2. `4907430` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.277**
   > User shall be able to refresh the list of Wi-Fi networks

3. `4907405` — 章 **4.6.1** Connection to Wi-Fi network — 分 **0.239**
   > After exclusion of networks not in-range and networks on the exclusion list, Wi-Fi signal strength shall be the primary selection criteria.

4. `4907424` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.214**
   > User shall be able to enter password for the network selected. (Kindly see the HMI)

5. `4907420` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.213**
   > when the user selects yes the HU shall enable client mode and scan for available networks.


---

### 26. `SWE1-FOTA-065` — Wi-Fi Network Exclusion After Consecutive OTA Download Failures

- Heading：`SWE1-FOTA-058` Connection to Wi-Fi network｜Sub Cat：Service｜Source：`SYS-RA-FOTA-046`

**Requirement Description 全文**：

> The WiFi Update Service shall monitor OTA package download completion status through SWMC for each previously configured Wi-Fi network used for OTA package download. The WiFi Update Service shall maintain and persist a consecutive OTA download failure counter associated with each previously configured Wi-Fi network, and increment the counter for each OTA download failure. If OTA package download completion fails for 5 consecutive Wi-Fi connection attempts using the same previously configured Wi-Fi network, the WiFi Update Service shall request WiFiManager to remove the Wi-Fi network from the selectable known Wi-Fi network list. After removal of the failed Wi-Fi network, the WiFi Update Service shall select an alternative available Wi-Fi network through WiFiManager and ConnectivityManger for OTA package download.

**路徑 A（語料 v2）前 5 候選**：

1. `4907408` — 章 **4.6.1** Connection to Wi-Fi network — 分 **0.215**
   > If the HU connects to a known network, and is unable to complete the OTA download over 5 seperate consecutive connections, the HU shall drop that network from the known list and attempt to use another network to complete the download.

2. `4907410` — 章 **4.6.1** Connection to Wi-Fi network — 分 **0.182**
   > 1) “Download Rate” shall be defined as the number of bytes downloaded per second, for the time span starting from the beginning of the network connection attempt through the duration of the connection or completion of the download, whichever comes first. Note: Connection time has intentionally been factored into this calculation. 2) In the case where the HU has not previously assigned an “Effectiv…

3. `4907689` — 章 **4.12.2** Report Persistency — 分 **0.182**
   > In the event that the cause of the interrupt and resume of service are not known to the OTA client (for example, the DM Server went down and the OTA client has no indication that the network is back up until it tries to connect to the server), the OTA client shall try to resend the report according to the configured retry parameter.

4. `4907403` — 章 **4.6.1** Connection to Wi-Fi network — 分 **0.173**
   > Upon an attempt to download via Wi-Fi and when multiple networks are configured, the HU will select the “best” network from which to attempt to connect and download. This scenario defines the criteria for network selection.

5. `4907332` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.150**
   > OTA client shall download the package from the URL provided in the Download Descriptor.


---

### 27. `SWE1-FOTA-062` — Prioritize Wi-Fi Network Selection by Signal Strength After Filtering

- Heading：`SWE1-FOTA-058` Connection to Wi-Fi network｜Sub Cat：Service｜Source：`SYS-RA-FOTA-049`

**Requirement Description 全文**：

> The WiFi Manager shall maintain an exclusion list for Wi-Fi network selection. The WiFi Update Service shall use WiFiManager scan results to exclude Wi-Fi networks that are not within range from the available Wi-Fi network list. The WiFi Manager shall exclude Wi-Fi networks present in the exclusion list from Wi-Fi network selection. After network filtering is completed, the WiFiManager shall evaluate available Wi-Fi networks based on signal strength from WiFiManager scan results. The WiFi Update Service shall use Wi-Fi signal strength as the primary selection criterion and shall request the Connectivity Service to establish the Wi-Fi connection with the network.

**路徑 A（語料 v2）前 5 候選**：

1. `4907405` — 章 **4.6.1** Connection to Wi-Fi network — 分 **0.498**
   > After exclusion of networks not in-range and networks on the exclusion list, Wi-Fi signal strength shall be the primary selection criteria.

2. `4907404` — 章 **4.6.1** Connection to Wi-Fi network — 分 **0.256**
   > When selecting a Wi-Fi network for a connection attempt, the HU shall exclude network(s) that are not in-range.

3. `4907406` — 章 **4.6.1** Connection to Wi-Fi network — 分 **0.240**
   > Based on detected Wi-Fi signal strength, the HU shall assign each network determined to be in-range to one of these categories: a. High Signal Strength b. Medium Signal Strength c. Low Signal Strength

4. `4907430` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.210**
   > User shall be able to refresh the list of Wi-Fi networks

5. `4907420` — 章 **4.6.3** Software Download via Wi-Fi — 分 **0.203**
   > when the user selects yes the HU shall enable client mode and scan for available networks.


---

### 28. `SWE1-FOTA-268` — Platform-Independent OMA-DM Communication Support

- Heading：`SWE1-FOTA-266` OTA Client Configuration options｜Sub Cat：Service｜Source：`SYS-RA-FOTA-441`

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

### 29. `SWE1-FOTA-123` — Clear TBM FOTA UI on No Updates Available

- Heading：`SWE1-FOTA-110` TBM FOTA Reflash｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-136`

**Requirement Description 全文**：

> The TBM Update Service shall retrieve $TBMUpdate$ using the TBM FW Service and detect when the value indicates No_Updates_Available. Upon detecting$TBMUpdate$ = [No_Updates_Available], the TBM Update Service shall notify the TBM FOTA HMI. The TBM FOTA HMI shall clear all active TBM FOTA-related pop-ups and status bar displays.

**路徑 A（語料 v2）前 5 候選**：

1. `4907796` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.641**
   > When the HU receives $TBMUpdate$ = [No_Updates_Available], the HU shall clear all active TBM FOTA related pop ups and status bar displays.

2. `4907795` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.641**
   > When the HU receives $TBMUpdate$ = [No_Updates_Available], the HU shall clear all active TBM FOTA related pop ups and status bar displays.

3. `4907797` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.610**
   > When the HU receives $TBMUpdate$ = [No_Update], the HU shall clear all active TBM FOTA related pop ups and status bar displays.

4. `4907783` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.332**
   > When HU receives $TBMupdate$ = [Update_Available] from the from TBM, on ignition off the HU shall show the TBM FOTA update pop-up screen to the user. Kindly see the HMI.

5. `4907802` — 章 **6** TBM Algorithm Requirements — 分 **0.327**
   > When TBM has completed the download of a FOTA update with notification package, then the TBM shall send $TBMUpdate$ = [Update_Available]


---

### 30. `SWE1-FOTA-233` — Display Estimated Time for TBM Software Update

- Heading：`SWE1-FOTA-214` HU FOTA with TBM｜Sub Cat：HMI｜Source：`SYS-RA-FOTA-147`

**Requirement Description 全文**：

> The TBM Update Service shall receive the download descriptor (DD) file from SWMC and shall extract the estimated TBM software update time information from the DD metadata received from the GSDP. The TBM Update Service shall provide the extracted estimated TBM software update time information to the TBM FOTA HMI. The TBM FOTA HMI shall display the estimated TBM software update time using the information extracted from the DD metadata.

**路徑 A（語料 v2）前 5 候選**：

1. `4907779` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.551**
   > HU shall receive information of 'WhatsNew' and 'Estimated time' for the TBM Software update from GSDP.

2. `4907782` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.534**
   > HU shall display Estimated time for the TBM Software update based on the information received from the GSDP. Please refer to the HMI L&amp;F.

3. `4907780` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.474**
   > When HU receives $TBM_Update$ = [Update_Available] AND successfully receives information of WhatsNew and Estimated time for the TBM Software update from GSDP, then the HU shall display TBM FOTA update available pop-up. Please refer to the HMI L&amp;F.

4. `4907899` — 章 **9.2** Installation Progress — 分 **0.315**
   > The HU shall receive HMI information via Ethernet Message SGW_FOTA_HMI_ETM.4215 such as- Estimated completion time- Time remaining- Progress information- Whats new information

5. `4907781` — 章 **5** TBM FOTA Reflash Requirements — 分 **0.284**
   > When user selects WhatsNew button on the HU during a TBM software update, HU shall display WhatsNew information received from GSDP. Please refer to the HMI L&amp;F.

