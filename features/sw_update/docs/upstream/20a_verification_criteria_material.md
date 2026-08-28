# 上繳材料 20a —— `Verification Criteria` 逐列全文（126 + 32 列）

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/21_verification_criteria.md` §四 T34a／T34b
- 依據：**R-SU27(a)**（VC 為 R-SU25(c) 外部可觀測後果之候選來源）
- 母包：`docs/upstream/20_verification_criteria.md`

> **執行層不裁定其觀測面。** 分析層逐列裁其可觀測後果（R-SU25(c)）。
>
> ⚠ **R-SU27(a)1**：本欄**不得 verbatim 抄入任何 TC 欄位**；
> `test_item` 上半之 verbatim 仍取 `Requirement Description`。
>
> ⚠ **R-SU27(a)2**：其所述之觀測面若本身為內部狀態，
> **不因其出自上游而成為合法之觀測面** —— R-SU25(b) 不因本條而放寬。
> **實測：126 個內部列中 105 列（83%）之 VC 亦無外部面**（母包 §2）。

---

## T34a —— 126 個內部列之 `Verification Criteria` 傾印

- 內部列 **126**（上繳包 19 §T33b）
- 其中 `Verification Criteria` **為空者 1 列**：`267`
- `Telematics Client` 之 5 列置於最前（下放包 21 §二 #3 待判）

> **執行層不裁定其觀測面。** 本節為分析層逐列裁定之材料。

> ⚠ 本欄之語形含 `Monitor`／`Observe` —— 二者為 **IN §5.1 之禁用步驟動詞**（`lint036.RE_A`）。取用其所述之觀測面時須改寫動詞，見上繳包 20 §自評。

### 0. 本欄能否供給觀測面 —— 先量再傾印

| 量 | 值 |
|---|---:|
| VC 之總行數（310 列） | 1103 |
| 行首為 IN §5.1 禁用動詞者 | **247（22%）** |
| **126 內部列中，其 VC 含外部面語形者** | **21／126（17%）** |
| **126 內部列中，其 VC 亦無任何外部面者** | **105／126（83%）** |
| 對照：185 非內部列中，其 VC 含外部面者 | 172／185（93%） |

行首動詞（前 10）：

| 動詞 | 行數 | IN §5.1 |
|---|---:|:--:|
| `Confirm` | 137 | — |
| `Observe` | 92 | **禁用** |
| `Verify` | 90 | **禁用** |
| `Ensure` | 82 | — |
| `Check` | 66 | — |
| `Examine` | 51 | — |
| `Recreate` | 48 | — |
| `Monitor` | 39 | **禁用** |
| `Evaluate` | 37 | — |
| `Review` | 36 | — |

> **本表即下放包 21 §五.6 之答案**：本欄之觀測面與需求本文**同源** —— 需求提及外部面者其 VC 亦提及（93%），需求未提者其 VC 多半亦未提（83%）。詳見上繳包 20 §自評。

### 甲 —— `Telematics Client`（5 列，全組皆內部列）


---

#### 1. `SWE1-FOTA-363` — TC Communication Establishment

- Test Set：**`Telematics Client`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Initiate an OTA update operation that requires communication with the TC client.
>
> Check that communication with the TC client is established successfully.
>
> Ensure that communication with the TC client is maintained throughout the OTA operation.
>


---

#### 2. `SWE1-FOTA-364` — TC Subscription for OTA Updates

- Test Set：**`Telematics Client`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Establish communication with the TC client.
>
> Check that the callback is registered successfully with the topic set to "FOTA".
>
> Ensure that the callback registration uses an empty value for the intent parameter.
>


---

#### 3. `SWE1-FOTA-365` — Server-Initiated Session Handling from TC

- Test Set：**`Telematics Client`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Send a server-initiated OTA notification through the TC client.
>
> Check that the OTA session request is received successfully.
>
> Ensure that the received session request is forwarded for OTA session execution.
>


---

#### 4. `SWE1-FOTA-366` — FOTA Update Availability Check

- Test Set：**`Telematics Client`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Send a server-initiated OTA session request through the TC client.
>
> Check that the OTA server is queried for available FOTA updates.
>
> Ensure that the FOTA update availability check is performed after the session request is received.
>


---

#### 5. `SWE1-FOTA-367` — Server-Initiated Session Forwarding from TC

- Test Set：**`Telematics Client`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Send a server-initiated OTA session request through the TC client.
>
> Check that the received session request is forwarded successfully.
>
> Ensure that the OTA session request is queued when it cannot be executed immediately.
>


### 乙 —— 其餘 121 列（依 037 列序）


---

#### 1. `SWE1-FOTA-005` — Reset Ignition Cycle Counter on Successful Wi-Fi Data Reception

- Test Set：**`FOTA Overview`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Ensure ignition cycle counter values are maintained and retained across FOTA download recovery attempts.
>
> Simulate Wi-Fi connectivity loss and interrupted FOTA data reception during firmware download.
>
> Restore Wi-Fi connectivity and resume active FOTA data reception.
>
> Verify that the ignition cycle counter is reset when stable Wi-Fi connectivity and active FOTA data transfer are re-established.
>


---

#### 2. `SWE1-FOTA-008` — Fallback to Embedded Modem After Wi-Fi Connection or Download Timeout

- Test Set：**`FOTA Overview`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Ensure previously configured Wi-Fi networks are used for automatic connectivity establishment during FOTA package download.
>
> Simulate unsuccessful Wi-Fi connection establishment and interrupted FOTA package download conditions over Wi-Fi.
>
> Maintain the failure condition continuously for 7 consecutive days using timer simulation or accelerated testing.
>
> Verify that FOTA package download transitions from Wi-Fi to embedded modem download handling after the configured timeout condition.
>


---

#### 3. `SWE1-FOTA-010` — Fallback to TBM Network for FOTA Download

- Test Set：**`Update Policy`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Ensure available Wi-Fi networks and previously configured Wi-Fi network presence are evaluated during FOTA download processing.
>
> Simulate absence of previously configured Wi-Fi networks in the available network list.
>
> Ensure FOTA package download initiation switches to the embedded modem (TBM network) when Wi-Fi connectivity is unavailable.
>
> Simulate incomplete or failed FOTA package download over Wi-Fi and verify continuation of download using the embedded modem network.
>


---

#### 4. `SWE1-FOTA-012` — Resume FOTA Critical Update via Wi-Fi During Body OFF Mode

- Test Set：**`Update Policy`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Ensure vehicle operational power mode transitions between Body ON and Body OFF are monitored during critical FOTA package download.
>
> Simulate interruption of embedded modem download during transition to Body OFF mode.
>
> Ensure availability of previously configured Wi-Fi networks is evaluated during Body OFF mode.
>
> Verify interrupted FOTA package download resumes over Wi-Fi from the last successfully downloaded package state after Wi-Fi connectivity establishment.
>


---

#### 5. `SWE1-FOTA-014` — Trigger Critical download via TBM Network

- Test Set：**`Update Policy`**｜`Verification Method`：`Unit Test / Integration Test / System TestPower Mode Validation TestingNetwork Path Validation Testing`

**`Verification Criteria` 全文**：

> Confirm correct detection of Body ON operational states during update processing.
>
> Check Critical Update handling based on received update metadata.
>
> Observe network transition to TBM connectivity during Critical Update execution.
>
> Review successful FOTA package download initiation after network availability.
>


---

#### 6. `SWE1-FOTA-019` — Restrict Embedded Modem Download Start to IGN_RUN State

- Test Set：**`Session Flows`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Review vehicle power mode handling for IGN_RUN and Engine Auto-Stop operational conditions.
>
> Observe firmware download initiation behavior during valid embedded modem download conditions.
>
> Check download restriction behavior when neither IGN_RUN nor Engine Auto-Stop ACTIVE condition is present.
>
> Confirm embedded modem download initiation occurs only under the configured operational states.
>


---

#### 7. `SWE1-FOTA-025` — Start Critical Update Automatically in Background

- Test Set：**`Update Policy`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Review update metadata handling after Download Descriptor retrieval.
>
> Check correct identification and classification of Critical Update packages from received metadata.
>
> Observe automatic deployment package download initiation for Critical Updates without user interaction.
>
> Confirm deployment processing continues in background mode during Critical Update execution.
>


---

#### 8. `SWE1-FOTA-026` — Treat Server-Flagged Update Session as Critical

- Test Set：**`Update Policy`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Review update session configuration and metadata processing from the downloaded Download Descriptor.
>
> Check handling of server command values related to update session type classification.
>
> Trigger a Download Descriptor containing Critical Update session information.
>
> Confirm the active update session transitions to Critical Update classification based on the received server command.
>


---

#### 9. `SWE1-FOTA-028` — Fallback to Mobile Network After One Week Wi-Fi Attempt

- Test Set：**`Update Policy`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Evaluate software package classification handling using metadata received from the Download Descriptor.
>
> Track Wi-Fi connectivity establishment and Non-Critical FOTA package download behavior over Wi-Fi.
>
> Analyze timeout handling when Wi-Fi connectivity or package download completion exceeds the configured one-week duration.
>
> Inspect transition of FOTA package download from Wi-Fi to the lowest cost supported mobile network method after timeout expiry
>


---

#### 10. `SWE1-FOTA-033` — Ignore Bearer Preference Rules for Critical Updates

- Test Set：**`Update Policy`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Identify Critical Update scenarios and evaluate network bearer selection behavior during deployment package download.
>
> Measure handling of configured bearer preference rules during active Critical Update sessions.
>
> Track download continuation behavior when different supported network bearers become available.
>
> Confirm deployment package download proceeds using any available supported network bearer for Critical Updates.
>


---

#### 11. `SWE1-FOTA-034` — Enforce OTA Update Priority Order

- Test Set：**`Update Policy`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Analyze OTA update classification handling for Critical, Regular, and Silent update types using received metadata.
>
> Observe installation blocking behavior when a lower priority update is requested during an active higher priority update session.
>
> Examine update sequencing and scheduling flow for multiple pending OTA updates with different priorities.
>
> Validate lower priority update installation occurs only after completion or clearance of higher priority update sessions.
>


---

#### 12. `SWE1-FOTA-047` — Store Wi-Fi Network Credentials for Future Connection

- Test Set：**`Wi-Fi Download`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Examine Wi-Fi credential persistence behavior after successful Wi-Fi connection establishment.
>
> Review storage handling for SSID, security type, encryption type, and passphrase information.
>
> Analyze retention of saved Wi-Fi network configuration across subsequent connection attempts.
>
> Monitor automatic Wi-Fi reconnection behavior using previously stored network credentials and configuration data.
>


---

#### 13. `SWE1-FOTA-054` — Switch from Client Mode to Host Mode Within 15 Seconds

- Test Set：**`Wi-Fi Download`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Evaluate detection handling for software download disablement and software download session exit conditions.
>
> Follow transition workflow initiated for switching the M-CPU platform from Client Mode to Host Mode.
>
> Measure mode transition duration after disable or exit request processing.
>
> Confirm Host Mode restoration completes within the configured 15-second timing requirement.
>


---

#### 14. `SWE1-FOTA-057` — Wi-Fi Download Timeout Handling During IGN_OFF Timed Mode

- Test Set：**`Wi-Fi Download`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Analyze timed download mode handling during vehicle ignition state transitions.
>
> Observe Wi-Fi download session timer activation after transition to IGN_OFF while timed download mode remains active.
>
> Track active FOTA download session duration during the current ignition cycle.
>
> Validate termination of the Wi-Fi download session and restoration of Host Mode when the 30-minute session limit is exceeded.
>


---

#### 15. `SWE1-FOTA-061` — Wi-Fi Network Range Validation for OTA Connection

- Test Set：**`Wi-Fi Download`**｜`Verification Method`：`Unit Testing/ Integration Testing/ System Testing`

**`Verification Criteria` 全文**：

> Review handling of configured Wi-Fi network information together with current Wi-Fi scan results.
>
> Examine evaluation flow for determining whether configured Wi-Fi networks are currently available.
>
> Observe filtering behavior for Wi-Fi networks detected outside the supported connection range.
>
> Check that Wi-Fi connectivity attempts are initiated only for configured networks identified as available and within range.
>


---

#### 16. `SWE1-FOTA-067` — Check Wi-Fi Preconditions and Saved Network on Next IGN_OFF

- Test Set：**`Wi-Fi Download`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Examine software download availability detection flow during OTA update processing.
>
> Monitor vehicle power mode transitions and identify handling of the next IGN_OFF event.
>
> Evaluate software download via Wi-Fi precondition assessment during IGN_OFF processing.
>
> Inspect availability detection for previously configured Wi-Fi networks with valid stored credentials after all preconditions are satisfied.
>


---

#### 17. `SWE1-FOTA-070` — Initiate FOTA Download via Wi-Fi When Preconditions Are Met

- Test Set：**`Wi-Fi Download`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Inspect validation flow for software download via Wi-Fi preconditions before connection establishment.
>
> Determine availability handling for previously configured Wi-Fi networks with valid stored credentials.
>
> Observe Wi-Fi connectivity establishment behavior after all required download conditions are fulfilled.
>
> Track FOTA package download initiation flow from the OTA server after successful Wi-Fi connection establishment
>


---

#### 18. `SWE1-FOTA-071` — Switch to Next Wi-Fi Network After Connection Timeout

- Test Set：**`Wi-Fi Download`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Examine Wi-Fi network selection handling based on configured network priority order.
>
> Monitor timing behavior for Wi-Fi connection establishment attempts using the configured 3-minute duration.
>
> Reproduce unsuccessful Wi-Fi connection scenarios and assess connection termination handling after timeout expiry.
>
> Follow fallback connection flow and confirm transition to the next configured Wi-Fi network in the priority chain.
>


---

#### 19. `SWE1-FOTA-080` — Receive Firmware Update from TBM via USB Connection

- Test Set：**`USB Update`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Assess OTA firmware download handling when Wi-Fi connectivity is unavailable and TBM network bearer usage is required.
>
> Observe USB 2.0 communication establishment between the host platform and TBM during network interface initialization.
>
> Review network configuration and activation flow over the USB communication interface.
>
> Track OTA firmware download session behavior using network connectivity provided through the TBM interface.
>


---

#### 20. `SWE1-FOTA-107` — Calculate and Report Remaining Time to Scheduled Install

- Test Set：**`ROV Installation`**｜`Verification Method`：`Unit Test / Integration Test / System TestTime Synchronization TestingScheduler Validation Testing`

**`Verification Criteria` 全文**：

> Examine storage handling for scheduled installation time associated with the update event.
>
> Observe retrieval of current system time during scheduled installation processing.
>
> Analyze remaining time calculation behavior between scheduled installation time and current system time.
>
> Confirm $HU_Scheduled_Install$ is updated with the calculated remaining installation time value.
>


---

#### 21. `SWE1-FOTA-111` — Enable TBM Update Functions Only When TBM Is Present

- Test Set：**`TBM Reflash`**｜`Verification Method`：`Unit Test / Integration Test / System TestVariant Configuration Testing`

**`Verification Criteria` 全文**：

> Inspect $TBM_present$ retrieval handling during TBM feature initialization flow.
>
> Recreate scenarios where $TBM_present$ reports the present state.
>
> Observe activation behavior for TBM-specific FOTA functionalities after valid TBM detection.
>
> Confirm TBM-related update operations are permitted only when the TBM presence condition is satisfied.
>


---

#### 22. `SWE1-FOTA-126` — Support Remote Configuration of OTA Flow Parameters

- Test Set：**`Configurable Parameters`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Examine configurable OTA workflow parameter handling within the SWMC during update operation processing.
>
> Reproduce OTA server interactions that provide updated parameter values for OTA workflow control.
>
> Assess parameter update handling when communication occurs through supported proprietary protocol mechanisms.
>
> Confirm received parameter values are applied correctly to the corresponding OTA workflow behavior after update synchronization.
>


---

#### 23. `SWE1-FOTA-138` — Extract Deployment Package and Route Component Packages

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Analyze deployment package manifest processing to identify included component packages during update preparation flow.
>
> Observe extraction handling and installation method determination for different component package types.
>
> Recreate installation scenarios containing both MCPU and peripheral component update packages.
>
> Confirm MCPU packages are routed for Update Engine installation processing while peripheral packages are forwarded through the peripheral update installation flow.
>


---

#### 24. `SWE1-FOTA-139` — Collect Installer Status and Report ECU Failure Codes

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Monitor installation status reporting behavior for both MCPU and peripheral component installation flows during update execution.
>
> Recreate installation failure scenarios and observe generation of ECU deployment package status codes for failed components.
>
> Examine collection and maintenance of installation status information and failure codes within the WiFi Update Service.
>
> Confirm installation result information and associated failure status details are forwarded correctly to the SWMC after installation processing.
>


---

#### 25. `SWE1-FOTA-143` — Continue Download During IGN OFF Extended Wake Period

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Monitor ignition status and $PowerMode$ transitions during active deployment package download sessions.
>
> Recreate key-off scenarios where $PowerMode$ transitions to IGN_OFF while package download is in progress.
>
> Observe extended wake mode request handling for continued deployment package download after ignition off.
>
> Confirm the deployment package download session is terminated when the 30-minute extended wake duration expires before download completion.
>


---

#### 26. `SWE1-FOTA-146` — Block Installation When IBS_SOC Accuracy Is Invalid

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Examine $IBS_SOC_ACCURACY$ retrieval handling during installation precondition evaluation flow.
>
> Reproduce invalid battery accuracy conditions where $IBS_SOC_ACCURACY$ = [0] or [SNA].
>
> Observe installation control behavior when battery state of charge accuracy information is invalid or unavailable.
>
> Confirm installation initiation remains blocked until a valid $IBS_SOC_ACCURACY$ value becomes available.
>


---

#### 27. `SWE1-FOTA-147` — Start Installation Only in IGN_OFF Power Mode

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Monitor $PowerMode$ retrieval behavior during installation precondition evaluation processing.
>
> Recreate vehicle power state transitions across supported $PowerMode$ conditions.
>
> Observe installation control handling when $PowerMode$ differs from IGN_OFF.
>
> Confirm installation initiation is permitted only when $PowerMode$ = [IGN_OFF].
>


---

#### 28. `SWE1-FOTA-151` — Block Installation During Active Download Session

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Monitor deployment package download session status notifications received from the SWMC.
>
> Recreate active deployment package download scenarios during software installation request handling.
>
> Observe installation blocking behavior while deployment package download sessions remain active.
>
> Confirm software installation becomes permitted only after all deployment package download sessions are completed, cancelled, failed, or terminated.
>


---

#### 29. `SWE1-FOTA-157` — Retry Installation Once After Failure

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Unit Test / Integration Test / System TestFailure Recovery Testing`

**`Verification Criteria` 全文**：

> Monitor installation failure status reporting behavior through the installer status callback interface from the Update Engine and SW Updater Service.
>
> Recreate failed deployment package installation scenarios requiring retry handling.
>
> Observe deployment precondition validation processing before retry installation initiation.
>
> Confirm retry handling is restricted to a maximum of one additional installation attempt for each failed installation session
>


---

#### 30. `SWE1-FOTA-160` — Ensure eCall Functionality During Download and Post-Installation

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Unit Test / Integration Test / System TestFailure Recovery Testing`

**`Verification Criteria` 全文**：

> Evaluate eCall operational continuity during FOTA download and post-installation processing with coordination between Connectivity Service and TBM Update Service.
>
> Recreate deployment package download and installation scenarios while eCall functionality remains active.
>
> Observe network, modem, and system resource utilization behavior during concurrent eCall and OTA update operations.
>
> Confirm the WiFi Update Service does not block, delay, or degrade resources required for eCall handling during deployment package download and installation processing.
>


---

#### 31. `SWE1-FOTA-163` — Continue Installation When Vehicle Starts Moving

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Unit Test / Integration Test / System TestVehicle State Transition Testing`

**`Verification Criteria` 全文**：

> Monitor vehicle motion state detection using $Speedometer$ or $OperationalModeSts$ during active software installation processing.
>
> Recreate vehicle movement scenarios while software installation is already in progress.
>
> Observe installation continuity behavior after vehicle motion conditions are detected during installation execution.
>
> Confirm the ongoing software installation continues without interruption, pause, or abort due to vehicle movement until installation completion.
>


---

#### 32. `SWE1-FOTA-165` — Post Installation Power Mode Handling

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Observe installation completion status notifications received from the Update Engine and SW Updater Manager.
>
> Recreate post-installation scenarios with different $PowerMode$ states after successful installation completion.
>
> Examine MCPU platform operational state handling when $PowerMode$ = [IGN_RUN].
>
> Confirm the WiFi Update Service/USB Update Service maintains full operation mode during IGN_RUN and initiates HU sleep mode transition when $PowerMode$ is not equal to IGN_RUN
>


---

#### 33. `SWE1-FOTA-169` — Parse Deployment Package and Invoke Component Installers

- Test Set：**`Session Flows`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Analyze deployment package manifest handling after successful installation precondition validation.
>
> Recreate deployment scenarios containing multiple component package types within the deployment package manifest.
>
> Observe installer or update agent invocation behavior for identified MCPU and peripheral component packages.
>
> Confirm MCPU firmware packages are forwarded to the Update Engine and peripheral component packages are routed to the SW Updater Manager for installation and deployment processing.
>


---

#### 34. `SWE1-FOTA-171` — Verification and Validation FCA Signed Deployment Packages

- Test Set：**`Integrity Verification`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Observe handling of downloaded FCA-signed deployment packages received from the SWMC for deployment preparation.
>
> Recreate deployment package verification scenarios using valid and invalid digital signatures and certificate chains.
>
> Examine SWDL Secure Library invocation behavior during signature verification and certificate validation processing.
>
> Confirm deployment package processing is permitted only after successful signature and certificate validation, and verify installation processing is blocked when validation fails.
>


---

#### 35. `SWE1-FOTA-173` — Integrate with Signature Verification Module for Deployment Packages

- Test Set：**`Integrity Verification`**｜`Verification Method`：`Unit Test / Integration Test / System TestSecurity Validation Testing`

**`Verification Criteria` 全文**：

> Examine interaction handling between the SWMC and the signature verification module during deployment package validation.
>
> Recreate deployment package verification scenarios using the defined signature verification interface.
>
> Observe response handling behavior returned from the signature verification module after validation processing.
>
> Confirm the SWMC determines subsequent deployment package processing based on the signature verification response result.
>


---

#### 36. `SWE1-FOTA-179` — Start Silent Update Download Automatically

- Test Set：**`Silent Update`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Inspect Download Descriptor metadata transfer handling between the SWMC and WiFi Update Service after update availability confirmation.
>
> Assess DD metadata analysis behavior for Silent Update classification detection.
>
> Validate automatic deployment package download request generation when Silent Update metadata is identified.
>
> Review SWMC interaction flow during automatic deployment package download initiation for Silent Update processing.
>


---

#### 37. `SWE1-FOTA-181` — Start Silent Update Installation Immediately After Download

- Test Set：**`Silent Update`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Assess deployment package download completion notification handling for update packages classified as Silent Update.
>
> Monitor communication flow between the SWMC and WiFi Update Service after successful download completion.
>
> Validate installation precheck initiation behavior immediately following deployment package download completion.
>
> Review automatic deployment startup processing for Silent Update packages without additional interaction flow.
>


---

#### 38. `SWE1-FOTA-205` — Validate Vehicle Preconditions Using Diagnostic Signals

- Test Set：**`Client Architecture`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Inspect retrieval of required vehicle diagnostic signals through CarProperty Manager during update precondition processing.
>
> Analyze evaluation handling for ignition state, battery voltage, vehicle speed, current draw, and additional vehicle-specific precondition signals.
>
> Verify update precondition assessment against configured download and installation requirements.
>
> Confirm software update download or installation is permitted only when all required preconditions are satisfied.
>


---

#### 39. `SWE1-FOTA-206` — Retrieve VIN from VIN_DATA Signal

- Test Set：**`Client Architecture`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Review $VIN_DATA$ retrieval handling through CarProperty Manager during OTA workflow execution.
>
> Validate extraction processing of the vehicle identification number (VIN) from the retrieved vehicle property.
>
> Examine VIN usage flow within OTA workflow handling operations.
>
> Ensure the extracted VIN is correctly obtained and made available for OTA workflow processing.
>


---

#### 40. `SWE1-FOTA-207` — Retrieve Vehicle Brand from VC_VEH_BRAND Signal

- Test Set：**`Client Architecture`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Analyze retrieval of the VC_VEH_BRAND vehicle property through CarProperty Manager during OTA workflow processing.
>
> Verify extraction and handling of vehicle brand information within the WiFi Update Service.
>
> Review transfer of vehicle brand details to SWMC for OTA server interaction activities.
>
> Confirm the vehicle brand information is utilized for server registration, campaign eligibility validation, and update session request processing.
>


---

#### 41. `SWE1-FOTA-208` — Retrieve Vehicle Brand from Brand Configuration Proxi Parameter

- Test Set：**`Client Architecture`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Inspect retrieval of vehicle brand data from the <Brand_Configuration_2> proxy parameter via CarProperty Manager during OTA workflow execution.
>
> Validate processing of the extracted brand value within the WiFi Update Service for OTA communication flow.
>
> Review transmission handling of vehicle brand information from WiFi Update Service toward SWMC for OTA operations.
>
> Ensure the retrieved brand value is correctly propagated to SWMC for OTA workflow processing.
>


---

#### 42. `SWE1-FOTA-209` — Route Software Components to Appropriate Installer Type

- Test Set：**`Client Architecture`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Analyze deployment package metadata processing to determine software component type for each update element within the WiFi Update Service.
>
> Evaluate installer interface selection logic based on identified component categories during OTA deployment execution.
>
> Verify routing behavior for MCPU firmware packages toward the Update Engine for firmware installation processing.
>
> Assess forwarding mechanism for peripheral component packages toward the SW Updater HAL for installation execution.
>


---

#### 43. `SWE1-FOTA-210` — Execute Component Dependency and Installation Order from Server Metadata

- Test Set：**`Client Architecture`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Review deployment metadata parsing for dependency rules and installation sequencing information received via SWMC.
>
> Analyze sequencing control logic used by the WiFi Update Service to execute component installation in the defined dependency order.
>
> Verify dependency enforcement behavior where installation steps are gated until prerequisite components complete successfully.
>
> Check installer status feedback handling to ensure dependent component installation is blocked until required prior installations are confirmed complete.
>


---

#### 44. `SWE1-FOTA-216` — Trigger Server Update Check on HUReflash Availability Signal

- Test Set：**`HU FOTA via TBM`**｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Validate OTA server update availability check execution for TBM FOTA sessions when $TBM_present$ = [present].
>
> Assess SWMC notification flow toward the TBM Update Service upon detection of an available TBM update.
>
> Verify TBM Update Service state handling where $HUReflash$ is set to [Update Available] upon receiving SWMC update availability status.
>
> Evaluate initiation sequence of TBM FOTA update following update availability confirmation from SWMC.
>


---

#### 45. `SWE1-FOTA-246` — Restrict Installation When Battery SOC Is Below Threshold

- Test Set：**`HU FOTA via TBM`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Check $IBS_SOC$ through CarProperty Manager right before starting the installation. If it drops below 65%, stop the installation from proceeding.
>
> If battery SOC data is not available, rely on $OperationalModeSts$ and allow installation only when the vehicle stays in Ignition_On_Engine_On continuously for 30 minutes.
>


---

#### 46. `SWE1-FOTA-249` — Verify Deployment Package Integrity Before Installation

- Test Set：**`HU FOTA via TBM`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Right before installation begins, call the SWDL Secure Library to check whether the downloaded package is clean and intact.
>
> If the verification doesn’t pass, stop the installation from starting and reject the package outright.
>


---

#### 47. `SWE1-FOTA-252` — OMA DM SCOMO Compliance for OTA Client

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure the system to use the proprietary communication protocol and confirm that communication is established successfully.
>
> Check that the update process completes successfully with the configured communication protocol
>


---

#### 48. `SWE1-FOTA-253` — Multi-Component Software Management using SCOMO

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Provide a deployment package containing different software component updates.
>
> Confirm that the deployment package is accepted for processing.
>
> Verify that the appropriate update process is selected based on the software component type.
>
> Ensure that each software component update is handled successfully.
>


---

#### 49. `SWE1-FOTA-255` — SWMC Download Manager Integration

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Provide a valid download URL for the deployment package.
>
> Verify that the deployment package is downloaded successfully.
>
> Confirm that the downloaded package is handed over for the next stage of update processing.
>
> Ensure that the download completes without interruption or data loss.
>


---

#### 50. `SWE1-FOTA-256` — Deployment Package Download Using Download Descriptor URL

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Provide a Download Descriptor containing a valid deployment package URL.
>
> Check that the package is downloaded from the URL specified in the Download Descriptor.
>
> Validate that the download completes successfully.
>
> Confirm that the downloaded package is forwarded for further update processing
>


---

#### 51. `SWE1-FOTA-258` — Update Agent Bootloader Integration

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Initiate an ECU firmware update.
>
> Observe that the update process starts successfully.
>
> Verify that the ECU firmware update completes successfully.
>
> Confirm that the ECU boots correctly with the updated firmware.
>


---

#### 52. `SWE1-FOTA-260` — OMA-DM Protocol Communication Support

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure the system to communicate using the OMA-DM protocol.
>
> Verify that communication with the OTA server is established successfully.
>
> Observe that the required communication events are generated during the update process.
>
> Ensure that the deployment package download is initiated successfully based on the communication events.
>


---

#### 53. `SWE1-FOTA-261` — Download Descriptor Processing Support

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Provide a valid OMA-DM Download Descriptor and verify that it is processed successfully.
>
> Configure a proprietary Download Descriptor and check that it is processed correctly.
>
> Confirm that the required deployment package information is extracted successfully.
>
> Validate that the deployment package download is initiated using the processed descriptor.
>


---

#### 54. `SWE1-FOTA-262` — Vehicle Property Access through Vehicle Integration Layer

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Request the required vehicle property information.
>
> Verify that the requested vehicle properties are retrieved successfully.
>
> Confirm that the retrieved information is available for vehicle identification.
>
> Check that the correct vehicle properties are returned for the target vehicle.
>


---

#### 55. `SWE1-FOTA-264` — Installer Abstraction for Multiple Update Methods

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Provide deployment package information for different installation methods.
>
> Verify that the correct installation method is selected for each update scenario.
>
> Check that the corresponding installation process is initiated based on the selected method.
>
> Confirm that the update completes successfully using the chosen installation method
>


---

#### 56. `SWE1-FOTA-267` — Portable Redbend Update Agent for Resource-Constrained Systems

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria`**：**(空)**


---

#### 57. `SWE1-FOTA-268` — Platform-Independent OMA-DM Communication Support

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure the system to use the OMA-DM communication protocol.
>
> Verify that communication with the OTA server is established successfully.
>
> Repeat the test using the configured proprietary communication protocol.
>
> Confirm that OTA communication is completed successfully with the selected communication protocol
>


---

#### 58. `SWE1-FOTA-269` — Platform-Independent Update Agent for Image Updates

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> nitiate an image update using a valid update package.
>
> Verify that the image update process starts successfully.
>
> Confirm that the image update completes successfully.
>
> Check that the updated image is applied correctly after the system restarts.
>


---

#### 59. `SWE1-FOTA-272` — Vehicle Event Interface Support

- Test Set：**`Session Flows`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Trigger a server-initiated session request.
>
> Verify that the event is received successfully.
>
> Check that the corresponding update process is initiated based on the received event.
>
> .
>


---

#### 60. `SWE1-FOTA-273` — Vehicle Event Interface for Software Deployment

- Test Set：**`Session Flows`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> * Generate a vehicle event that blocks software deployment.
>
> * Verify that the blocking event is detected successfully.
>
> * Confirm that the software deployment does not proceed while the blocking condition exists.
>
> * Clear the blocking event and ensure that the software deployment can continue successfully.
>


---

#### 61. `SWE1-FOTA-274` — OTA Communication / Vehicle-Initiated Session

- Test Set：**`Session Flows`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure a polling interval for OTA communication.
>
> Enable network connectivity and wait for the configured polling interval.
>
> Verify that communication with the OTA server is initiated automatically.
>
> Confirm that the polling activity follows the configured interval.
>


---

#### 62. `SWE1-FOTA-275` — Server-Configurable Polling Interva

- Test Set：**`Session Flows`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure the polling interval through the server.
>
> Verify that the updated polling interval is applied successfully.
>
> Confirm that periodic polling is performed using the configured interval.
>


---

#### 63. `SWE1-FOTA-277` — Server-Initiated Session Event Interface

- Test Set：**`Session Flows`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Trigger a server-initiated session event.
>
> Verify that the session event is received successfully.
>
> Confirm that the update process is initiated based on the received session event.
>


---

#### 64. `SWE1-FOTA-279` — Open Communication Protocol Support

- Test Set：**`Session Flows`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure the communication protocol for server communication.
>
> Verify that communication is established successfully using the configured protocol.
>
> When a proprietary communication protocol is used, confirm that communication is performed using HTTP and TLS.
>


---

#### 65. `SWE1-FOTA-281` — Idle State Resource Management

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Ensure that no active session, update operation, communication, or trigger event is present.
>
> Verify that the system enters the idle state.
>
> Trigger a valid event or request and confirm that normal operation resumes.
>


---

#### 66. `SWE1-FOTA-282` — Idle Resource Utilization

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Ensure the system in the idle state.
>
> Verify that CPU and RAM utilization remain at a minimal level while idle.
>
> Initiate an operation or event and confirm that system resources are utilized only during processing.
>


---

#### 67. `SWE1-FOTA-286` — OTA Flow Status Reporting

- Test Set：**`Client Architecture`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Complete a session or update operation.
>
> Verify that a status report is generated after the operation is completed.
>
> Confirm that the report indicates whether the operation was successful or failed.
>


---

#### 68. `SWE1-FOTA-288` — OTA Server Command and Configuration Handling

- Test Set：**`Session Flows`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Send a software update command from the server.
>
> Verify that the received command is processed successfully.
>
> Provide configuration parameters from the server and confirm that they are applied correctly.
>


---

#### 69. `SWE1-FOTA-289` — OTA Server URL and Port Configuration

- Test Set：**`Session Flows`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Update the server URL and port through a server configuration command.
>
> Verify that the new server URL and port are applied successfully.
>
> Confirm that subsequent communication is established using the updated server configuration
>


---

#### 70. `SWE1-FOTA-290` — OTA Server Configuration Rollback

- Test Set：**`Session Flows`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Update the server URL and port with a new configuration.
>
> Verify that the previous server configuration is stored before applying the new one.
>
> Provide an invalid server configuration and confirm that the previous server URL and port are restored.
>


---

#### 71. `SWE1-FOTA-297` — Digital Signature and Transport Security Verification

- Test Set：**`Bearer Selection`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Provide a deployment package with a valid digital signature.
>
> Verify that the digital signature and package integrity are validated before the update proceeds.
>
> Provide a deployment package with an invalid or modified digital signature and confirm that the update is rejected.
>


---

#### 72. `SWE1-FOTA-298` — Proprietary Communication Protocol Support

- Test Set：**`Bearer Selection`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure the approved proprietary communication protocol.
>
> Verify that communication with the OTA server is established using the configured protocol.
>
> Confirm that only the configured proprietary communication protocol is used for OTA communication.
>


---

#### 73. `SWE1-FOTA-299` — SWMC Security Requirement Compliance

- Test Set：**`Bearer Selection`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Provide valid OTA update information for processing.
>
> Verify that only validated OTA update information is accepted.
>
> Confirm that unvalidated or invalid OTA update information is rejected.
>


---

#### 74. `SWE1-FOTA-300` — TLS 1.2 Server Authentication Support

- Test Set：**`Bearer Selection`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Attempt to establish communication with a server supporting TLS 1.2.
>
> Verify that server authentication is completed successfully before communication is established.
>
> Confirm that communication is established only after successful server authentication.
>


---

#### 75. `SWE1-FOTA-301` — Server Authentication During Session Initiation

- Test Set：**`Bearer Selection`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Initiate an OTA communication session.
>
> Verify that the server is authenticated before the session is established.
>
> Confirm that the OTA communication session proceeds only after successful server authentication.
>


---

#### 76. `SWE1-FOTA-302` — SWMC Authentication Information Support

- Test Set：**`Bearer Selection`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Request authentication information from the OTA server.
>
> Verify that the required authentication information is provided.
>
> Confirm that the authentication information is transmitted through a secure communication channel.
>


---

#### 77. `SWE1-FOTA-303` — Vehicle Information for Server Authentication

- Test Set：**`Bearer Selection`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Retrieve the required vehicle details for authentication.
>
> Verify that the vehicle details are provided for server authentication.
>
> Confirm that server authentication is performed using the retrieved vehicle details.
>


---

#### 78. `SWE1-FOTA-305` — Authorized Server Communication

- Test Set：**`Bearer Selection`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure an authorized OTA server and initiate communication.
>
> Verify that communication is established only with the authorized server.
>
> Attempt to initiate communication with an unauthorized server and confirm that the request is rejected.
>


---

#### 79. `SWE1-FOTA-306` — Secure Communication Port Management

- Test Set：**`Bearer Selection`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Initiate an OTA communication session.
>
> Verify that only the required communication interfaces remain active during the session.
>
> Confirm that communication ports and listening interfaces are closed after the OTA operation is completed.
>


---

#### 80. `SWE1-FOTA-307` — Application Layer Authentication Support

- Test Set：**`Bearer Selection`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure the application-layer authentication algorithm.
>
> Verify that OTA communication is authenticated using the configured algorithm.
>
> When HMAC-SHA2 is configured, confirm that it is used for application-layer authentication
>


---

#### 81. `SWE1-FOTA-308` — OMA-DM Security Compliance

- Test Set：**`Bearer Selection`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure the communication protocol for OTA communication.
>
> Verify that the required security mechanisms are applied for the configured protocol.
>
> When a proprietary communication protocol is configured, confirm that equivalent security mechanisms are applied.
>


---

#### 82. `SWE1-FOTA-311` — DM Tree Encryption and Protection

- Test Set：**`Integrity Verification`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Store the DM Tree and verify that it is saved in an encrypted format.
>
> When a proprietary communication protocol is used, verify that the associated configuration data is stored in an encrypted format.
>
> Confirm that the stored data cannot be read in plaintext.
>


---

#### 83. `SWE1-FOTA-312` — Deployment Package Integrity Verification

- Test Set：**`Integrity Verification`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Download a deployment package from the OTA server.
>
> Verify that the deployment package integrity is checked immediately after it is received.
>
> Confirm that the deployment package is accepted for further processing only after successful integrity verification.
>


---

#### 84. `SWE1-FOTA-313` — Software Update Error Handling Coordination

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Trigger an error during OTA communication or software update.
>
> Verify that the error is handled appropriately.
>
> Confirm that the update status is reported after the error is processed.
>


---

#### 85. `SWE1-FOTA-315` — Socket Read/Write Error Handling

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Trigger a socket read or write error during OTA communication.
>
> Verify that the socket error is detected and handled appropriately.
>
> Confirm that the error status is reported after the error is detected.
>


---

#### 86. `SWE1-FOTA-316` — Network Loss Handling

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Simulate a network loss during OTA communication or software update.
>
> Verify that the network loss condition is detected and handled appropriately.
>
> Confirm that the network loss status is reported.
>


---

#### 87. `SWE1-FOTA-318` — Emergency State Handling

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Simulate a vehicle emergency state during an OTA operation.
>
> Verify that the emergency state is detected and handled appropriately.
>
> Confirm that the OTA operation responds according to the emergency condition.
>


---

#### 88. `SWE1-FOTA-319` — Power Loss Handling

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Simulate a power loss during an OTA operation.
>
> Verify that the power loss condition is handled appropriately.
>
> Confirm that the OTA operation responds according to the power loss condition.
>


---

#### 89. `SWE1-FOTA-321` — Interruption Recovery Handling

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Simulate an interruption during an OTA operation and then resolve the interruption.
>
> Verify that the interruption resolution is detected successfully.
>
> Confirm that the OTA session resumes according to the current session state
>


---

#### 90. `SWE1-FOTA-323` — Concurrent NIA Handling

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Start an OTA update session and send an additional NIA while the session is in progress.
>
> Check that the incoming NIA is queued without interrupting the active session.
>
> Ensure that the queued NIA is processed after the current OTA session is completed.
>


---

#### 91. `SWE1-FOTA-324` — Partial Download Preservation

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Interrupt the deployment package download before it is completed.
>
> Check that the partially downloaded package is retained.
>
> Ensure that the saved package is available to continue the download after the interruption is resolved.
>


---

#### 92. `SWE1-FOTA-327` — Download Resume Based on Interruption Type

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Introduce an interruption that supports download resumption.
>
> Check that the download resumes only when the interruption meets the defined resume conditions.
>
> Ensure that the download continues from the point of interruption.
>


---

#### 93. `SWE1-FOTA-328` — Internal Network Interruption Recovery

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Interrupt the download by disabling data access or disconnecting the tethered phone.
>
> Restore the data connection or reconnect the tethered phone.
>
> Observe that the interrupted download resumes automatically after the interruption is cleared.
>


---

#### 94. `SWE1-FOTA-329` — External Network Interruption Retry Handling

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Interrupt the download due to an external network failure.
>
> Observe that the download is retried according to the configured retry count.
>
> Ensure that the OTA session is aborted and the failure is logged after the maximum retry count is reached.
>


---

#### 95. `SWE1-FOTA-330` — OTA Session Completion Reporting

- Test Set：**`Status Reporting`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Complete an OTA session with a successful outcome.
>
> Repeat the session with a failure condition.
>
> Check that the session result is reported to the OTA server in both cases.
>


---

#### 96. `SWE1-FOTA-331` — OTA Session Report Retry Handling

- Test Set：**`Status Reporting`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Interrupt the OTA session before the session report is sent or acknowledged.
>
> Check that the session report is saved successfully.
>
> Restore the connection and ensure that the saved report is resent to the OTA server.
>


---

#### 97. `SWE1-FOTA-332` — OTA Session Report Resend

- Test Set：**`Status Reporting`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Save the OTA session report after an interruption occurs.
>
> Restore the condition that caused the interruption.
>
> Observe that the saved OTA session report is resent automatically.
>


---

#### 98. `SWE1-FOTA-333` — OTA Session Report Retry

- Test Set：**`Status Reporting`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Interrupt the transmission of the OTA session report when the service is unavailable.
>
> Observe that the report is retried according to the configured retry parameter.
>
> Ensure that the report is sent successfully once communication is restored.
>


---

#### 99. `SWE1-FOTA-341` — Deployment Condition Evaluation

- Test Set：**`Deployment Conditions`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure multiple deployment conditions with the required values or value ranges.
>
> Check that all configured conditions are evaluated before deployment.
>
> Ensure that deployment proceeds only when all configured conditions are satisfied.
>


---

#### 100. `SWE1-FOTA-345` — Vehicle Condition Provision for Download Control

- Test Set：**`Deployment Conditions`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Create a condition that requires the deployment package download to pause.
>
> Check that the download is paused while the condition exists.
>
> Restore the required conditions and ensure that the download resumes automatically.
>


---

#### 101. `SWE1-FOTA-347` — Vehicle-Initiated Polling Interval Configuration

- Test Set：**`Session Management`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure the polling interval for vehicle-initiated OTA sessions.
>
> Check that the default polling interval is set to 24 hours.
>
> Ensure that the polling interval can be updated to a new configured value.
>


---

#### 102. `SWE1-FOTA-349` — Polling Timer Monitoring

- Test Set：**`Session Management`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure the polling timer with a valid interval.
>
> Allow the polling timer to expire.
>
> Check that a vehicle-initiated OTA session is queued when the timer expires.
>


---

#### 103. `SWE1-FOTA-350` — Session Precondition Evaluation

- Test Set：**`Session Management`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure the required preconditions for an OTA update session.
>
> Introduce a condition where one or more preconditions are not satisfied.
>
> Ensure that the OTA update session is queued until all preconditions are satisfied.
>


---

#### 104. `SWE1-FOTA-355` — Download Precondition Data Provision

- Test Set：**`Session Management`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Initiate the download process after user acceptance.
>
> Check that the required vehicle and system data is obtained for download precondition validation.
>
> Ensure that the download proceeds only after the required data is available
>


---

#### 105. `SWE1-FOTA-356` — Deployment Package Notification

- Test Set：**`Session Management`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Complete the deployment package download.
>
> Check that the deployment package is validated successfully before deployment.
>
> Ensure that a notification is generated indicating that the validated deployment package is available for deployment.
>


---

#### 106. `SWE1-FOTA-357` — Installation Interruption State Management

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Interrupt the installation before it is completed.
>
> Check that the current installation state is saved.
>
> Restore the normal operating condition and ensure that the installation resumes from the saved state.
>
> Observe that the installation status is updated after the installation completes or fails.
>


---

#### 107. `SWE1-FOTA-358` — Update Status Reporting to SWMC

- Test Set：**`Status Reporting`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Complete the software update process.
>
> Check that the software update status is reported.
>
> Ensure that the final software update result is sent to the OTA server.
>


---

#### 108. `SWE1-FOTA-359` — OTA Flow Concurrency Control

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Start an OTA update session.
>
> Attempt to initiate another OTA update flow while the current session is in progress.
>
> Ensure that the new OTA update request is ignored and the active session continues without interruption.
>


---

#### 109. `SWE1-FOTA-360` — Download Interruption Recovery

- Test Set：**`Interruption Handling`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Interrupt the deployment package download before it is completed.
>
> Check that the current download state is saved.
>
> Restore the required conditions and ensure that the download resumes from the saved state.
>


---

#### 110. `SWE1-FOTA-361` — Server-Initiated OTA Background Execution

- Test Set：**`Session Management`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Initiate a server-initiated OTA update session.
>
> Observe that the OTA update executes as a background operation.
>
> Ensure that normal foreground system operations continue without interruption during the OTA update.
>


---

#### 111. `SWE1-FOTA-368` — OTA Session Precondition Evaluation and Queueing

- Test Set：**`Session Management`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Send a server-initiated OTA session request.
>
> Check that the configured preconditions are evaluated before starting the session.
>
> Ensure that the session is queued when the preconditions are not satisfied and starts after all preconditions are met.
>


---

#### 112. `SWE1-FOTA-369` — Server-Initiated Flow Alignment with Vehicle-Initiated Flow

- Test Set：**`Session Management`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Send a server-initiated OTA session request.
>
> Check that the server-initiated session follows the same workflow as the vehicle-initiated OTA update flow.
>
> Ensure that the OTA update proceeds successfully after the session is initiated.
>


---

#### 113. `SWE1-FOTA-370` — Update Deployment Method Support

- Test Set：**`Update Agent`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure different update deployment methods for the target modules.
>
> Check that the appropriate deployment method is selected based on the configured target module.
>
> Ensure that the update is deployed using the selected deployment method.
>


---

#### 114. `SWE1-FOTA-372` — Dependency-Based Installation Ordering

- Test Set：**`Update Agent`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Provide an update package containing software components with defined dependencies.
>
> Check that the software component dependencies are validated before installation.
>
> Ensure that the software components are installed in the defined dependency order.
>


---

#### 115. `SWE1-FOTA-373` — Update Progress API Provision

- Test Set：**`Update Agent`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Initiate a software update for a supported target.
>
> Check that the update progress information is available during the update.
>
> Ensure that the reported progress is updated until the installation is completed.
>


---

#### 116. `SWE1-FOTA-374` — UA Integration API Provision

- Test Set：**`Update Agent`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Initiate an OTA update operation that requires communication with the Update Agent.
>
> Check that the API interface is available for integration with the Update Agent.
>
> Ensure that OTA update operations are performed successfully through the API interface.
>


---

#### 117. `SWE1-FOTA-376` — Update Agent Self-Update Capability

- Test Set：**`Update Agent`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Initiate an OTA update for the Update Agent.
>
> Check that the Update Agent is updated successfully through the OTA update mechanism.
>
> Ensure that the updated Update Agent operates correctly after the update.
>


---

#### 118. `SWE1-FOTA-379` — Update Bricking Prevention

- Test Set：**`Update Agent`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Start an update for the target component.
>
> Introduce an interruption or failure during the update process.
>
> Ensure that the target component remains operational and is not permanently disabled after the interruption.
>


---

#### 119. `SWE1-FOTA-380` — Update Recovery Mechanism

- Test Set：**`Update Agent`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Introduce an interruption such as power loss or communication loss during the update process.
>
> Check that the recovery mechanism is invoked after the interruption.
>
> Ensure that the update resumes or terminates safely once the interruption is resolved.
>


---

#### 120. `SWE1-FOTA-381` — Differential Update Technology Support

- Test Set：**`Update Agent`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Configure an approved differential update package for the update.
>
> Check that the differential update mechanism is used during the update process.
>
> Ensure that the update completes successfully using the configured differential update technology.
>


---

#### 121. `SWE1-FOTA-383` — Deployed Software Validation

- Test Set：**`Update Agent`**｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Complete the software installation using a valid update package.
>
> Check that the deployed software is validated after the installation is completed.
>
> Ensure that the deployed software is confirmed to be correctly and successfully installed.
>


---

## T34b —— `HMI Validation Testing` 之 32 列（正向樣本）

- 命中 **32** 列；其中內部列 **0** 列 —— **交集為 0，完美分離**
- 用途：作為「有 HMI 可觀測面」之正向樣本，供分析層校準 R-SU25(c) 之取用方式

| # | 037 列 | Test Set | `Verification Method` 之串接 |
|---:|---|---|---|
| 1 | `SWE1-FOTA-097` | `ROV Installation` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 2 | `SWE1-FOTA-099` | `ROV Installation` | Unit Test / Integration Test / System TestHMI Validation TestingSignal Sequence Testing |
| 3 | `SWE1-FOTA-101` | `ROV Installation` | Unit Test / Integration Test / System TestHMI Validation TestingSignal Condition Testing |
| 4 | `SWE1-FOTA-102` | `ROV Installation` | Unit Test / Integration Test / System TestHMI Validation TestingPolicy State Testing |
| 5 | `SWE1-FOTA-103` | `ROV Installation` | Unit Test / Integration Test / System TestHMI Validation TestingNavigation Flow Testing |
| 6 | `SWE1-FOTA-104` | `ROV Installation` | Unit Test / Integration Test / System TestHMI Validation TestingVariant Testing |
| 7 | `SWE1-FOTA-105` | `ROV Installation` | Unit Test / Integration Test / System TestHMI Validation TestingVariant Testing |
| 8 | `SWE1-FOTA-108` | `ROV Installation` | Unit Test / Integration Test / System TestHMI Validation TestingNetwork Condition Testing |
| 9 | `SWE1-FOTA-114` | `TBM Reflash` | Unit Test / Integration Test / System TestHMI Validation TestingConfiguration Testing |
| 10 | `SWE1-FOTA-115` | `TBM Reflash` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 11 | `SWE1-FOTA-118` | `TBM Reflash` | Unit Test / Integration Test / System TestHMI Validation TestingIgnition State Transition Testing |
| 12 | `SWE1-FOTA-119` | `TBM Reflash` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 13 | `SWE1-FOTA-122` | `TBM Reflash` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 14 | `SWE1-FOTA-123` | `TBM Reflash` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 15 | `SWE1-FOTA-124` | `TBM Reflash` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 16 | `SWE1-FOTA-131` | `Update HMI` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 17 | `SWE1-FOTA-148` | `Deployment Flow` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 18 | `SWE1-FOTA-150` | `Deployment Flow` | Unit Test / Integration Test / System TestHMI Validation TestingPersistence / Power Cycle Testing |
| 19 | `SWE1-FOTA-154` | `Deployment Flow` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 20 | `SWE1-FOTA-155` | `Deployment Flow` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 21 | `SWE1-FOTA-156` | `Deployment Flow` | Unit Test / Integration Test / System TestHMI Validation TestingPower State Validation Testing |
| 22 | `SWE1-FOTA-162` | `Deployment Flow` | Unit Test / Integration Test / System TestFailure Recovery TestingHMI Validation Testing |
| 23 | `SWE1-FOTA-177` | `Silent Update` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 24 | `SWE1-FOTA-180` | `Silent Update` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 25 | `SWE1-FOTA-182` | `Silent Update` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 26 | `SWE1-FOTA-231` | `HU FOTA via TBM` | Unit Test / Integration Test / System TestHMI Validation TestingInterface Message Testing |
| 27 | `SWE1-FOTA-232` | `HU FOTA via TBM` | Unit Test / Integration Test / System TestHMI Validation TestingInterface Message Testing |
| 28 | `SWE1-FOTA-233` | `HU FOTA via TBM` | Unit Test / Integration Test / System TestHMI Validation Testing |
| 29 | `SWE1-FOTA-236` | `HU FOTA via TBM` | Unit Test / Integration Test / System TestHMI Validation TestingInterface Signal Testing |
| 30 | `SWE1-FOTA-237` | `HU FOTA via TBM` | Unit Test / Integration Test / System TestHMI Validation TestingInterface Message Testing |
| 31 | `SWE1-FOTA-242` | `HU FOTA via TBM` | Unit Test / Integration Test / System TestHMI Validation TestingInterface Signal Testing |
| 32 | `SWE1-FOTA-243` | `HU FOTA via TBM` | Unit Test / Integration Test / System TestHMI Validation TestingInterface Signal Testing |

### 逐列之 `Verification Criteria`


---

#### 1. `SWE1-FOTA-097` — Display Forced Update Available A Popup on Waiting Acceptance State

- Test Set：**`ROV Installation`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Assess combined handling of $FOTA_Status$ and $FOTA_Delay$ conditions during update acceptance flow.
>
> Recreate update scenarios where $FOTA_Status$ = [Waiting for HMI Acceptance] and $FOTA_Delay$ = [Not_Prohibited].
>
> Observe notification triggering behavior toward the ROV FOTA HMI under the configured conditions.
>
> Verify “ROV Forced Update Available A” pop-up presentation during valid forced update availability scenarios.
>


---

#### 2. `SWE1-FOTA-099` — Handle “Update Now” Selection for ROV Forced Update

- Test Set：**`ROV Installation`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingSignal Sequence Testing`

**`Verification Criteria` 全文**：

> Observe user interaction handling from the “ROV Forced Update Available B” pop-up during forced update flow.
>
> Perform Update Now selection and monitor notification transfer toward the ROV Update Service.
>
> Examine FOTA_Install state transition behavior after user acceptance handling.
>
> Confirm FOTA_Install changes to Accepted and subsequently resets to Nothing to report after processing completion.
>


---

#### 3. `SWE1-FOTA-101` — Allow Cancel or Ignore Action for Forced Update Popup A Under Permitted Delay State

- Test Set：**`ROV Installation`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingSignal Condition Testing`

**`Verification Criteria` 全文**：

> Analyze handling of $FOTA_Status$ and $FOTA_Delay$ conditions during “ROV Forced Update Available A” pop-up interaction flow.
>
> Generate scenarios where $FOTA_Status$ = [Waiting for HMI Acceptance] and $FOTA_Delay$ = [Not Prohibited].
>
> Observe user interaction behavior for cancel and ignore actions under valid popup conditions.
>
> Confirm cancel or ignore interaction is restricted when either required condition is not satisfied.
>


---

#### 4. `SWE1-FOTA-102` — Force Update Scheduling When Delay Is Prohibited

- Test Set：**`ROV Installation`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingPolicy State Testing`

**`Verification Criteria` 全文**：

> Recreate forced update conditions where $FOTA_Status$ = [Waiting for HMI Acceptance] and $FOTA_Delay$ = [Prohibited].
>
> Observe notification handling that triggers forced update scheduling flow toward the ROV FOTA HMI.
>
> Evaluate user interaction restrictions for skip, ignore, and dismiss operations during forced update handling.
>
> Confirm lockout behavior remains active until the user completes update scheduling through the required flow.
>


---

#### 5. `SWE1-FOTA-103` — Launch Schedule Update HMI for ROV Forced Update

- Test Set：**`ROV Installation`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingNavigation Flow Testing`

**`Verification Criteria` 全文**：

> Observe user interaction handling for “Schedule Update” selection from both forced update pop-up variants.
>
> Track notification flow generated after user selection from the ROV FOTA HMI.
>
> Examine transition handling initiated by the ROV Update Service after receiving the schedule request.
>
> Confirm navigation proceeds correctly from the forced update pop-up flow to the Schedule Update HMI.
>


---

#### 6. `SWE1-FOTA-104` — Display BEV/PHEV Schedule Update Popup on Schedule Selection

- Test Set：**`ROV Installation`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingVariant Testing`

**`Verification Criteria` 全文**：

> Examine $Hybrid_Type$ retrieval handling for BEV and PHEV vehicle configurations.
>
> Capture user interaction flow for “Schedule Update” selection from forced update pop-ups.
>
> Recreate scheduling scenarios for vehicles identified as BEV or PHEV.
>
> Confirm “Schedule Update” pop-up (PUXXX3) is displayed when valid hybrid type and user selection conditions are satisfied.
>


---

#### 7. `SWE1-FOTA-105` — Display Schedule Update Pop-up for Supported Powertrain Types

- Test Set：**`ROV Installation`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingVariant Testing`

**`Verification Criteria` 全文**：

> Review $Hybrid_Type$ evaluation handling for BEV, PHEV, FCEV, and REPB vehicle configurations.
>
> Observe user interaction flow for “Schedule Update” selection from forced update availability pop-ups.
>
> Reproduce update scheduling scenarios across supported hybrid vehicle types.
>
> Verify “Schedule Update” pop-up (PUXXX3) is displayed when supported vehicle type and schedule selection conditions are met.
>


---

#### 8. `SWE1-FOTA-108` — Display No Connectivity Pop-up for ROV Update

- Test Set：**`ROV Installation`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingNetwork Condition Testing`

**`Verification Criteria` 全文**：

> Capture user interaction flow for “Update Now” selection from the “ROV Forced Update Available B” pop-up.
>
> Recreate network conditions where $LTE_Status$ is outside supported connectivity states or $Cellsignal$ indicates weak or unavailable signal levels.
>
> Evaluate connectivity validation behavior before update initiation processing.
>
> Confirm “No Connectivity” pop-up is displayed and update initiation is blocked under invalid network conditions.
>


---

#### 9. `SWE1-FOTA-114` — Display Parameterized Default Update Time of 360 Seconds

- Test Set：**`TBM Reflash`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingConfiguration Testing`

**`Verification Criteria` 全文**：

> Examine estimated update duration handling between the TBM Update Service and TBM FOTA HMI.
>
> Validate default estimated update duration behavior using the configured 360-second value.
>
> Modify software parameterization values and observe configurable duration update handling.
>
> Confirm the TBM FOTA HMI displays the active configured estimated update duration during the relevant update flow.
>


---

#### 10. `SWE1-FOTA-115` — Trigger Immediate Update Action on User Selection

- Test Set：**`TBM Reflash`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Observe user interaction handling for “Update Now” selection within the TBM FOTA HMI flow.
>
> Track notification transfer from the TBM FOTA HMI toward the TBM Update Service after user selection.
>
> Examine $UpdateAction$ state update behavior following “Update Now” request processing.
>
> Confirm $UpdateAction$ = [Update Now] is transmitted correctly through the TBM FW Service.
>


---

#### 11. `SWE1-FOTA-118` — Display Forced TBM Update Screen on Ignition OFF

- Test Set：**`TBM Reflash`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingIgnition State Transition Testing`

**`Verification Criteria` 全文**：

> Evaluate $TBMUpdate$ monitoring behavior for detection of Forced_Update status conditions.
>
> Simulate Body OFF operational state transitions using $OperationalModeSts$ values.
>
> Track notification handling toward the TBM FOTA HMI when forced update conditions occur during Body OFF mode.
>
> Confirm the forced TBM update screen is displayed under valid forced update and Body OFF conditions.
>


---

#### 12. `SWE1-FOTA-119` — Display TBM Update Success Popup on Update Completion

- Test Set：**`TBM Reflash`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Monitor $TBMUpdate$ state changes for detection of Update_End completion conditions.
>
> Reproduce TBM update completion scenarios resulting in $TBMUpdate$ = [Update_End].
>
> Observe notification handling toward the TBM FOTA HMI after update completion detection.
>
> Confirm the TBM update success pop-up is displayed following successful TBM update completion.
>


---

#### 13. `SWE1-FOTA-122` — Display TBM Update Failure Screen

- Test Set：**`TBM Reflash`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Monitor $TBMUpdate$ status handling for detection of Update_Fail conditions during TBM update processing.
>
> Simulate TBM update failure scenarios resulting in $TBMUpdate$ = [Update_Fail].
>
> Analyze notification behavior toward the TBM FOTA HMI after update failure detection.
>
> Confirm the TBM update failure screen is displayed during valid TBM update failure conditions.
>


---

#### 14. `SWE1-FOTA-123` — Clear TBM FOTA UI on No Updates Available

- Test Set：**`TBM Reflash`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Observe $TBMUpdate$ monitoring behavior for detection of No_Updates_Available conditions.
>
> Recreate scenarios resulting in $TBMUpdate$ = [No_Updates_Available] through the TBM FW Service.
>
> Examine notification flow toward the TBM FOTA HMI after no-update status detection.
>
> Confirm all active TBM FOTA-related pop-ups and status bar indications are cleared after no-update status handling.
>


---

#### 15. `SWE1-FOTA-124` — Clear TBM FOTA UI on No Update State

- Test Set：**`TBM Reflash`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Track $TBMUpdate$ status evaluation for detection of No_Update conditions through the TBM FW Service.
>
> Reproduce update check scenarios resulting in $TBMUpdate$ = [No_Update].
>
> Observe notification handling toward the TBM FOTA HMI after no-update detection.
>
> Confirm all active TBM FOTA-related pop-ups and status bar displays are cleared after processing the no-update condition.
>


---

#### 16. `SWE1-FOTA-131` — Support Server-Configured Update Types With Consistent User Experience

- Test Set：**`Update HMI`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Examine update type configuration retrieval handling for OTA campaigns received from the OTA server.
>
> Recreate update scenarios using regular, critical, and silent update type configurations.
>
> Observe update flow behavior changes based on the configured update type and corresponding restrictions or notifications.
>
> Confirm the SW Update HMI maintains a consistent interaction flow while applying update-type-specific behaviors defined by the server configuration.
>


---

#### 17. `SWE1-FOTA-148` — Display Estimated Installation Time in Popup PU0304

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Observe estimated installation time extraction handling from downloaded deployment package details received through SWMC.
>
> Track transfer of estimated installation time information from the WiFi Update Service to the SW Update HMI.
>
> Recreate installation notification scenarios using different estimated installation duration values.
>
> Confirm the SW Update HMI populates the estimated installation time correctly within the installation pop-up.
>


---

#### 18. `SWE1-FOTA-150` — Enter Forced Update Lock State After Popup Dismissal Threshold

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingPersistence / Power Cycle Testing`

**`Verification Criteria` 全文**：

> Evaluate installation popup dismissal counter handling when the counter reaches the configured threshold of 20 occurrences.
>
> Recreate locked-state activation scenarios where network connectivity is available and the software update installation remains unscheduled.
>
> Observe Head Unit restriction behavior during the locked state, including allowed functions, supported hard keys, approved screens, audio restrictions, overlay handling, Screen Off recovery behavior, diagnostic mode support, and Rear View Camera display priority.
>
> Confirm the locked state persists across ignition cycles until update scheduling is completed, and verify that full Head Unit functionality, entertainment features, supported screens, softkeys, and audio capabilities are restored after successful update scheduling.
>


---

#### 19. `SWE1-FOTA-154` — Display Conditions Not Met With Specific Cancellation Reason

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Examine scheduled installation precondition evaluation handling before installation initiation processing.
>
> Recreate ignition, battery state of charge, battery accuracy, and engine-running condition scenarios using $PowerMode$, $IBS_SOC$, $IBS_SOC_ACCURACY$, and $OperationalModeSts$ signals.
>
> Observe cancellation reason generation and notification behavior for ignition and battery-related installation precondition failures.
>
> Confirm the SW Update HMI displays the “Conditions Not Met” pop-up with the appropriate cancellation reason received from the WiFi Update Service/USB Update Service.
>


---

#### 20. `SWE1-FOTA-155` — Display Cancellation Reason Based on Hybrid Type During Failed Scheduled Installation

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Analyze installation precondition evaluation behavior before scheduled installation initiation.
>
> Recreate installation cancellation scenarios caused by unmet installation conditions and cancellation reason value [7].
>
> Observe cancellation reason text selection behavior based on $Hybrid_Type$ values for xEV and ICE vehicle configurations.
>
> Confirm the SW Update HMI displays the “Conditions Not Met” pop-up with the correct cancellation reason text received from the WiFi Update Service/USB Update Service.
>


---

#### 21. `SWE1-FOTA-156` — Keep Display ON During Installation

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingPower State Validation Testing`

**`Verification Criteria` 全文**：

> Observe system power management request handling for maintaining the radio display in ON state after installation acceptance.
>
> Recreate installation-in-progress scenarios while display ON requests remain active through CarPower Manager.
>
> Examine coordination behavior between the WiFi Update Service/USB Update Service and the SW Update HMI during active installation processing.
>
> Confirm the installation-related user interface remains continuously displayed while the display ON request is active.
>


---

#### 22. `SWE1-FOTA-162` — Enable User-Initiated Retry After Installation Failure

- Test Set：**`Deployment Flow`**｜`Verification Method`：`Unit Test / Integration Test / System TestFailure Recovery TestingHMI Validation Testing`

**`Verification Criteria` 全文**：

> Examine installation failure status reporting behavior through the installer status callback interface from the Update Engine and SW Updater Service.
>
> Recreate OTA installation failure scenarios and observe OTA session state update handling within the WiFi Update Service.
>
> Observe retry option presentation and user interaction handling through the SW Update HMI after installation failure detection.
>
> Confirm deployment precondition validation is performed and update installation is re-initiated after the user selects the retry option.
>


---

#### 23. `SWE1-FOTA-177` — Restrict Opt-Out and Deferral Options in HMI

- Test Set：**`Silent Update`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Evaluate SW Update HMI behavior when the assigned update service is active and available.
>
> Inspect user interaction flow presented during mandatory update handling scenarios.
>
> Verify that opt-out and update deferral selections are restricted within the SW Update HMI.
>
> Ensure the assigned update service does not expose user options to reject, postpone, or defer the update process.
>


---

#### 24. `SWE1-FOTA-180` — Optionally Suppress Download Confirmation Screen

- Test Set：**`Silent Update`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Analyze Silent Update handling behavior during deployment package download preparation.
>
> Verify that the SW Update HMI does not display a download confirmation screen for Silent Update sessions.
>
> Review automatic deployment package download request handling initiated through the WiFi Update Service.
>
> Ensure deployment package download begins through SWMC without requiring any customer interaction.
>


---

#### 25. `SWE1-FOTA-182` — Optionally Suppress Deployment Confirmation Screen

- Test Set：**`Silent Update`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Review deployment handling behavior for update packages categorized as Silent Update.
>
> Check that the SW Update HMI does not present a deployment confirmation screen during Silent Update processing.
>
> Evaluate automatic deployment initiation flow for downloaded Silent Update packages.
>
> Confirm deployment execution proceeds without requiring customer interaction or approval actions.
>


---

#### 26. `SWE1-FOTA-231` — Display What’s New Popup on User Selection

- Test Set：**`HU FOTA via TBM`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingInterface Message Testing`

**`Verification Criteria` 全文**：

> Capture the user selection when they tap the “What’s New” option from the HMI input handler.
>
> Once selected, obtain the stored “What’s New” details from the cached SGW_FOTA_HMI_ETM message through CarProperty Manager.
>
> Ensure the PU0410 pop-up is shown and verify that the retrieved “What’s New” content is rendered correctly for the user.
>


---

#### 27. `SWE1-FOTA-232` — Populate Installation Progress Popup Using SGW Status Data

- Test Set：**`HU FOTA via TBM`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingInterface Message Testing`

**`Verification Criteria` 全文**：

> Keep an eye on update progress data coming through SGW_FOTA_HMI_ETM.4215 via the CarPropertyManager interface.
>
> Pull out the installation percentage and the estimated time still left from the received status payload.
>
> Pass this information to the HMI so it can update the Installation Progress ROV popup with current percentage and remaining time.
>
> Make sure the values stay fresh and get updated whenever new status information comes in.
>


---

#### 28. `SWE1-FOTA-233` — Display Estimated Time for TBM Software Update

- Test Set：**`HU FOTA via TBM`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Obtain the download descriptor (DD) file from SWMC and pull out the estimated TBM software update duration from the metadata received via GSDP.
>
> Pass this extracted timing information to the TBM FOTA HMI so it can be used for display.
>
> Ensure the HMI shows the estimated TBM update time clearly using the value derived from the DD metadata.
>


---

#### 29. `SWE1-FOTA-236` — Display What's New Pop-up for ROV Forced Update

- Test Set：**`HU FOTA via TBM`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingInterface Signal Testing`

**`Verification Criteria` 全文**：

> Capture when the user taps “What’s New” from either the Forced Update Available A or B pop-up on the HMI.
>
> Once selected, pull the stored “What’s New” content from SGW_FOTA_HMI_ETM.4215 .
>
> Show the PU0410 pop-up and render the retrieved “What’s New” details on the screen for the user.
>


---

#### 30. `SWE1-FOTA-237` — Populate Installation Progress Popup Using SGW Status Data

- Test Set：**`HU FOTA via TBM`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingInterface Message Testing`

**`Verification Criteria` 全文**：

> Pull in installation progress updates coming through SGW_FOTA_HMI_ETM.4215 via the CarProperty Manager interface.
>
> Extract the current install percentage and the estimated time still left from the received status data.
>
> Send these values to the HMI so it can update the “Installation Progress ROV” popup accordingly.
>
> Keep the progress display in sync by refreshing it every time new status updates arrive.
>


---

#### 31. `SWE1-FOTA-242` — Visualize TBM Update Pop-up via Visual Instructions

- Test Set：**`HU FOTA via TBM`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingInterface Signal Testing`

**`Verification Criteria` 全文**：

> Watch the FOTA_TBM_Notification flag continuously during TBM update handling.
>
> When it turns True, check the vehicle state using $OperationalModeSts$ through CarProperty Manager to confirm the system is in a valid Body ON condition.
>
> If both conditions are satisfied, trigger the HMI to show the update popup using FOTA_Visual_Instructions.Info.
>
> Treat the Body ON/OFF classification based on the provided ignition states, ensuring only valid ON states allow the popup to appear.
>


---

#### 32. `SWE1-FOTA-243` — Visualize Forced Update Pop-up via Visual Instructions

- Test Set：**`HU FOTA via TBM`**｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingInterface Signal Testing`

**`Verification Criteria` 全文**：

> Keep look on FOTA_TBM_Forced during TBM update handling.
>
> When it is True, check the vehicle status using $OperationalModeSts$ via CarProperty Manager to confirm the system is in a valid Body ON state.
>
> If both conditions match, trigger the HMI to show the Forced Update popup using FOTA_Visual_Instructions.Info.
>
> Use the given ignition states to decide Body ON/OFF, and allow the popup only when a proper ON state is detected.
>

