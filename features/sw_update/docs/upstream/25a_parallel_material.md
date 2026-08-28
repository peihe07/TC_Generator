# 上繳包 25a —— T39c 併行線材料（`ROV Installation` 20 ＋ `Update HMI` 6 = 26 列）

- 日期：2026-08-28｜方向：執行層 → 分析層｜對應下放包：`handoff/26_batch1_tc.md` §六 T39c
- 本檔為**材料**，其判定與自評在 `25_batch1_review.md`

---

## T39c —— 併行線材料（`ROV Installation` 20 列 ＋ `Update HMI` 6 列）

- 依據：下放包 26 §2.4-3 —— 二組之 **105 列為 0**，不受 DR-SU2 之議題影響
- 機制 3 之門檻（R-SU23(b)，`≤` 為攔下）：首選分 **≤ 0.267**
- **執行層不撰寫 TC、不裁定錨**

### 閉合檢查（R-SU10 v2(d)：列數須與 framework 定稿相符）

| Test Set | framework 載 | 實測 | Heading 群 | |
|---|---:|---:|---|:--:|
| `ROV Installation` | 20 | **20** | `SWE1-FOTA-086`、`SWE1-FOTA-091`、`SWE1-FOTA-096`、`SWE1-FOTA-085` | ✅ |
| `Update HMI` | 6 | **6** | `SWE1-FOTA-129` | ✅ |
| **合計** | **26** | **26** | | ✅ |

- **105 列：0** —— **0，與 §2.4-3 之前提相符**
- 126 內部列（VC 有外部面）：**1** —— `SWE1-FOTA-107`

---

## 節 —— `ROV Installation`（20 列）

能力叢集：ROV 安裝三階段：安裝前、安裝進度、安裝後

| # | 037 列 | 標題 | Sub Cat | Priority | 105？ | 首選分 | 機制 3 |
|---:|---|---|---|---|:--:|---:|:--:|
| 1 | `SWE1-FOTA-088` | Display Success Pop-up in Body ON Mo | HMI | High | — | 0.268 | — |
| 2 | `SWE1-FOTA-089` | Enforce Vehicle Motion Lockout for R | Service | High | — | 0.382 | — |
| 3 | `SWE1-FOTA-090` | Cache and Display “What’s New” After | HMI | High | — | 0.432 | — |
| 4 | `SWE1-FOTA-092` | Display Installation Screens When FO | HMI | High | — | 0.581 | — |
| 5 | `SWE1-FOTA-093` | Display Reverted Pop-up on Rollback  | HMI | High | — | 0.611 | — |
| 6 | `SWE1-FOTA-094` | Display Walk Home Scenario Pop-up on | HMI | High | — | 0.633 | — |
| 7 | `SWE1-FOTA-095` | Display Software Update Complete Pop | HMI | High | — | 0.451 | — |
| 8 | `SWE1-FOTA-097` | Display Forced Update Available A Po | HMI | High | — | 0.772 | — |
| 9 | `SWE1-FOTA-098` | Dismiss Active Pop-up on Standby/Sle | HMI | Medium | — | 0.386 | — |
| 10 | `SWE1-FOTA-099` | Handle “Update Now” Selection for RO | Service | High | — | 0.583 | — |
| 11 | `SWE1-FOTA-100` | Handle Timeout or Cancel Action for  | HMI | High | — | 0.473 | — |
| 12 | `SWE1-FOTA-101` | Allow Cancel or Ignore Action for Fo | HMI | High | — | 0.729 | — |
| 13 | `SWE1-FOTA-102` | Force Update Scheduling When Delay I | HMI | High | — | 0.566 | — |
| 14 | `SWE1-FOTA-103` | Launch Schedule Update HMI for ROV F | Service | High | — | 0.644 | — |
| 15 | `SWE1-FOTA-104` | Display BEV/PHEV Schedule Update Pop | HMI | High | — | 0.747 | — |
| 16 | `SWE1-FOTA-105` | Display Schedule Update Pop-up for S | HMI | High | — | 0.747 | — |
| 17 | `SWE1-FOTA-106` | Display “Conditions Not Met” Pop-up  | HMI | High | — | 0.640 | — |
| 18 | `SWE1-FOTA-107` | Calculate and Report Remaining Time  | Service | High | — | 0.472 | — |
| 19 | `SWE1-FOTA-108` | Display No Connectivity Pop-up for R | HMI | High | — | 0.713 | — |
| 20 | `SWE1-FOTA-109` | Interrupt Pre-Installation Flow on S | HMI | High | — | 0.746 | — |

### `ROV Installation` —— 逐列材料


---

#### 1. `SWE1-FOTA-088` — Display Success Pop-up in Body ON Mode

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-107`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The ROV Update Service shall retrieve $FOTA_Status$ and $OperationalModeSts$ using CarPropertyManager. If FOTA_Status indicates successful FOTA update ( $FOTA_Status$ = [Successful FOTA Update]) completion and OperationalModeSts indicates Body ON mode, the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the PU0303 success pop-up. *Body on mode when $OperationalModeSts$ = Ignition_on or Ignition_pre_start or Ignition_start or Ignition_Cranking or Iginiton_on_Engine_on else Body off when $OperationalModeSts$ =Initialization or Ignition_Off_WithoutKey or Ignition_Off or Ignition_Acc or Ignition_Pre_Acc or Ignition_Pre_Off or Automatic_Cranking or Automatic_Stop or Key_Authenticated or Not_Used Body on mode SNA

**`Verification Criteria` 全文**：

> Review handling of $FOTA_Status$ and $OperationalModeSts$ during post-update processing flow.
>
> Recreate successful FOTA update completion scenarios while the vehicle remains in Body ON mode.
>
> Observe notification flow triggered toward the ROV FOTA HMI after successful update detection.
>
> Confirm PU0303 success pop-up presentation during valid successful FOTA update conditions.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907906` — 章 **9.3** Post-Installation — 分 **0.268**
   > The HU shall display pop-up, PU0303 after a successful FOTA update at Body ON mode. Refer to CFTS009 for power moding states

2. `4907909` — 章 **9.3** Post-Installation — 分 **0.267**
   > The HU shall cache $FOTA_Status$ = [Successful FOTA Update] and What's new details to display until next Body ON mode.

3. `4907874` — 章 **8.4** MOTA Client Initiated Updates — 分 **0.244**
   > If the update is downloaded via Wi-Fi with Body OFF mode, the installation shall happen at the next Body ON mode.

4. `4907904` — 章 **9.2** Installation Progress — 分 **0.239**
   > When the HU receives $FOTA_Status$ = [Successful FOTA Update] , the HU shall display the software update complete pop-up, PU0416Please refer to HMI

5. `4907398` — 章 **4.6** OTA download via Wi-Fi — 分 **0.236**
   > Pre Conditions for FOTA via Wifi:➢ Vehicle’s battery is above 65% State of Charge ($IBS_SOC$ &gt; [65]). If $IBS_SOC$ not available in the vehicle's DBC check: Vehicle in with motor running ($OperationalModeSts$ = [Ignition_On_Engine_On]) for 30 minutes.➢ Ignition position is OFF ($PowerMode$ = [IGN_OFF]).


---

#### 2. `SWE1-FOTA-089` — Enforce Vehicle Motion Lockout for ROV FOTA HMI

- 分類：非內部列｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-106`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The ROV Update Service shall retrieve the $Speedometer$ vehicle property using CarPropertyManager. If the Speedometer value is greater than zero, the ROV Update Service shall determine that the vehicle is in motion and enforce the vehicle speed lockout behavior. The ROV Update Service shall notify the ROV Update HMI of the vehicle-in-motion status.

**`Verification Criteria` 全文**：

> Monitor $Speedometer$ vehicle property handling during ROV update operation flow.
>
> Generate vehicle movement conditions with Speedometer values greater than zero.
>
> Evaluate vehicle speed lockout activation behavior when the vehicle is detected in motion.
>
> Track notification handling toward the ROV Update HMI for vehicle-in-motion status indication.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907907` — 章 **9.3** Post-Installation — 分 **0.382**
   > The HU shall monitor $Speedometer$ and implement the HU vehicle speed lockout behavior defined in Requirement ID 4915105 present in CFTS022 to support the 'vehicle in motion logic and flow' called out in HMI document, FOTA ROV Software Updates HMI Logic and Flow.

2. `4907886` — 章 **9.1** Pre-Installation — 分 **0.195**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI

3. `4907884` — 章 **9.1** Pre-Installation — 分 **0.189**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

4. `4907880` — 章 **9.1** Pre-Installation — 分 **0.164**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

5. `4907887` — 章 **9.1** Pre-Installation — 分 **0.153**
   > When the $Hybrid_Type$ = [BEV] or [PHEV] and if the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then the HU shall display "Schedule Update popup" (PUXXX3).Please refer to the latest Software Updates FOTA HMI L&amp;F.


---

#### 3. `SWE1-FOTA-090` — Cache and Display “What’s New” After Successful Update Until Next Body ON

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-104`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The ROV Update Service shall retrieve FOTA_Status using CarPropertyManager and detect when the value indicates Successful FOTA Update.( $FOTA_Status$ = [Successful FOTA Update] ) Upon detection, the ROV Update Service shall cache the FOTA_Status and the “What’s New” details received from the deployment package. The ROV Update Service shall retrieve OperationalModeSts using CarPropertyManager to determine the vehicle Body ON/OFF state. The ROV FOTA HMI shall display the cached “What’s New” information to the user. The ROV Update Service shall retain the cached data until the next transition to Body ON mode. *Body on mode when $OperationalModeSts$ = Ignition_on or Ignition_pre_start or Ignition_start or Ignition_Cranking or Iginiton_on_Engine_on else Body off when $OperationalModeSts$ =Initialization or Ignition_Off_WithoutKey or Ignition_Off or Ignition_Acc or Ignition_Pre_Acc or Ignition_Pre_Off or Automatic_Cranking or Automatic_Stop or Key_Authenticated or Not_Used Body on mode SNA

**`Verification Criteria` 全文**：

> Analyze successful FOTA update status detection and caching behavior for update completion information.
>
> Observe storage handling for $FOTA_Status$ and deployment package “What’s New” details after successful update completion.
>
> Examine Body ON and Body OFF operational state transitions during cached data retention processing.
>
> Confirm cached “What’s New” information remains available to the user until the next transition to Body ON mode.
>

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

#### 4. `SWE1-FOTA-092` — Display Installation Screens When FOTA Status Indicates Installing

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-114`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The ROV Update Service shall retrieve FOTA_Status using CarPropertyManager. If FOTA_Status indicates Installing FOTA Update( $FOTA_Status$ = [Installing FOTA Update]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the installation progress screens corresponding to the active update session.

**`Verification Criteria` 全文**：

> Track $FOTA_Status$ handling during active FOTA installation processing.
>
> Recreate update sessions where $FOTA_Status$ transitions to Installing FOTA Update.
>
> Inspect notification flow triggered toward the ROV FOTA HMI during installation state detection.
>
> Review installation progress screen presentation corresponding to the active update session.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907898` — 章 **9.2** Installation Progress — 分 **0.581**
   > When the HU receives $FOTA_Status$ = [Installing FOTA Update], the HU shall display installation screens.

2. `4907880` — 章 **9.1** Pre-Installation — 分 **0.319**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

3. `4907884` — 章 **9.1** Pre-Installation — 分 **0.316**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

4. `4907900` — 章 **9.2** Installation Progress — 分 **0.291**
   > The HU shall populate the installation percentage and estimated time remaining progress in the pop-up, "Installation Progress ROV" based on the status received from SGW_FOTA_HMI_ETM.4215

5. `4907904` — 章 **9.2** Installation Progress — 分 **0.286**
   > When the HU receives $FOTA_Status$ = [Successful FOTA Update] , the HU shall display the software update complete pop-up, PU0416Please refer to HMI


---

#### 5. `SWE1-FOTA-093` — Display Reverted Pop-up on Rollback Success

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-111`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The ROV Update Service shall retrieve FOTA_Status using CarPropertyManager. If FOTA_Status indicates FOTA FailureRollback Successful($FOTA_Status$ = [FOTA FailureRollback Successful]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the “Reverted” pop-up after successful rollback.

**`Verification Criteria` 全文**：

> Observe $FOTA_Status$ monitoring behavior during rollback completion scenarios.
>
> Generate FOTA failure rollback conditions resulting in FOTA FailureRollback Successful status.
>
> Evaluate notification handling toward the ROV FOTA HMI after successful rollback detection.
>
> Confirm “Reverted” pop-up presentation following successful rollback completion.
>

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

#### 6. `SWE1-FOTA-094` — Display Walk Home Scenario Pop-up on Failure Completion

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-110`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The ROV Update Service shall read FOTA_Status using CarPropertyManager. If FOTA_Status indicates FOTA Failure Complete($FOTA_Status$ = [FOTA Failure Complete]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the “Walk Home Scenario” pop-up.

**`Verification Criteria` 全文**：

> Examine $FOTA_Status$ state handling during FOTA failure completion scenarios.
>
> Reproduce conditions where $FOTA_Status$ changes to FOTA Failure Complete.
>
> Monitor notification flow toward the ROV FOTA HMI after failure completion detection.
>
> Validate display behavior of the “Walk Home Scenario” pop-up during FOTA failure conditions.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907902` — 章 **9.2** Installation Progress — 分 **0.633**
   > When the HU receives $FOTA_Status$ = [FOTA Failure Complete] , the HU shall display the "Walk Home Scenario pop-up"Please refer to HMI

2. `4907903` — 章 **9.2** Installation Progress — 分 **0.396**
   > During a FOTA ROV update failure, HU shall launch the Assist App when Assist button is selected by the user at “Walk Home Scenario” pop-up

3. `4907904` — 章 **9.2** Installation Progress — 分 **0.390**
   > When the HU receives $FOTA_Status$ = [Successful FOTA Update] , the HU shall display the software update complete pop-up, PU0416Please refer to HMI

4. `4907880` — 章 **9.1** Pre-Installation — 分 **0.342**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

5. `4907884` — 章 **9.1** Pre-Installation — 分 **0.332**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]


---

#### 7. `SWE1-FOTA-095` — Display Software Update Complete Pop-up

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-109`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The ROV Update Service shall read FOTA_Status using CarPropertyManager. If FOTA_Status indicates Successful FOTA Update($FOTA_Status$ = [Successful FOTA Update]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the software update completion pop-up PU0416.

**`Verification Criteria` 全文**：

> Review $FOTA_Status$ monitoring behavior for successful FOTA update completion states.
>
> Trigger successful update completion conditions with $FOTA_Status$ = [Successful FOTA Update].
>
> Analyze notification handling toward the ROV FOTA HMI after successful update detection.
>
> Confirm software update completion pop-up PU0416 is displayed during successful FOTA update scenarios.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907904` — 章 **9.2** Installation Progress — 分 **0.451**
   > When the HU receives $FOTA_Status$ = [Successful FOTA Update] , the HU shall display the software update complete pop-up, PU0416Please refer to HMI

2. `4907880` — 章 **9.1** Pre-Installation — 分 **0.364**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

3. `4907901` — 章 **9.2** Installation Progress — 分 **0.363**
   > When the HU receives $FOTA_Status$ = [FOTA FailureRollback Successful] , the HU shall display the "Reverted pop-up"Please refer to HMI

4. `4907884` — 章 **9.1** Pre-Installation — 分 **0.357**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

5. `4907909` — 章 **9.3** Post-Installation — 分 **0.306**
   > The HU shall cache $FOTA_Status$ = [Successful FOTA Update] and What's new details to display until next Body ON mode.


---

#### 8. `SWE1-FOTA-097` — Display Forced Update Available A Popup on Waiting Acceptance State

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-130`
- `Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**Requirement Description 全文**：

> The ROV Update Service shall read FOTA_Status and FOTA_Delay using CarPropertyManager. If FOTA_Status indicates Waiting for HMI Acceptance ($FOTA_Status$ = [Waiting for HMI Acceptance]) and FOTA_Delay indicates Not_Prohibited($FOTA_Delay$ = [Not_Prohibited]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall show “ROV Forced Update Available A” pop-up.

**`Verification Criteria` 全文**：

> Assess combined handling of $FOTA_Status$ and $FOTA_Delay$ conditions during update acceptance flow.
>
> Recreate update scenarios where $FOTA_Status$ = [Waiting for HMI Acceptance] and $FOTA_Delay$ = [Not_Prohibited].
>
> Observe notification triggering behavior toward the ROV FOTA HMI under the configured conditions.
>
> Verify “ROV Forced Update Available A” pop-up presentation during valid forced update availability scenarios.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907880` — 章 **9.1** Pre-Installation — 分 **0.772**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

2. `4907884` — 章 **9.1** Pre-Installation — 分 **0.672**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

3. `4907885` — 章 **9.1** Pre-Installation — 分 **0.496**
   > When the HU Receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Prohibited], the HU shall force the user to schedule an update and lock the user out per the requirements in the HMI.

4. `4907896` — 章 **9.1** Pre-Installation — 分 **0.325**
   > When the HU is in the pre-installation flow, if $FOTA_Status$ &lt;&gt; [Waiting for HMI Acceptance], the HU shall interrupt the current pre-installation flow and display appropriate HMI based on current $FOTA_Status$

5. `4907886` — 章 **9.1** Pre-Installation — 分 **0.311**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI


---

#### 9. `SWE1-FOTA-098` — Dismiss Active Pop-up on Standby/Sleep Transition

- 分類：非內部列｜Sub Cat：HMI｜Priority：Medium｜Source：`SYS-RA-FOTA-129`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The ROV Update Service shall retrieve the vehicle power mode information using CarPropertyManager. If the vehicle power mode indicates transition to Standby or Sleep mode, the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall dismiss any active FOTA-related pop-up.

**`Verification Criteria` 全文**：

> Evaluate vehicle power mode monitoring behavior during active ROV FOTA HMI operation.
>
> Trigger vehicle transitions into Standby and Sleep operating modes.
>
> Analyze notification handling generated during power state transition events.
>
> Verify active FOTA-related pop-ups are automatically dismissed after entering Standby or Sleep mode.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907881` — 章 **9.1** Pre-Installation — 分 **0.386**
   > The pop-up shall dismiss if the radio enters Standby/Sleep mode

2. `4907884` — 章 **9.1** Pre-Installation — 分 **0.256**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

3. `4907880` — 章 **9.1** Pre-Installation — 分 **0.249**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

4. `4907889` — 章 **9.1** Pre-Installation — 分 **0.241**
   > If the user selects 'What's New' option on "ROV Forced Update Available A" or "ROV Forced Update Availbale B" pop-up, the HU shall display the pop-up (PU0410) with what's new details based on the information received from SGW_FOTA_HMI_ETM.4215.Please refer to the latest Software Updates FOTA HMI L&amp;F.

5. `4907886` — 章 **9.1** Pre-Installation — 分 **0.240**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI


---

#### 10. `SWE1-FOTA-099` — Handle “Update Now” Selection for ROV Forced Update

- 分類：非內部列｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-128`
- `Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingSignal Sequence Testing`

**Requirement Description 全文**：

> The ROV FOTA HMI shall capture the user selection from the “ROV Forced Update Available B” pop-up. If the user selects Update Now, the ROV FOTA HMI shall notify the ROV Update Service. Upon receiving the user selection, the ROV Update Service shall set FOTA_Install to Accepted using CarPropertyManager. After setting FOTA_Install to Accepted, the ROV Update Service shall reset FOTA_Install to Nothing to report.

**`Verification Criteria` 全文**：

> Observe user interaction handling from the “ROV Forced Update Available B” pop-up during forced update flow.
>
> Perform Update Now selection and monitor notification transfer toward the ROV Update Service.
>
> Examine FOTA_Install state transition behavior after user acceptance handling.
>
> Confirm FOTA_Install changes to Accepted and subsequently resets to Nothing to report after processing completion.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907882` — 章 **9.1** Pre-Installation — 分 **0.583**
   > If the user selects 'Update Now' option on "ROV Forced Update Available B" pop-up, then HU shall send $FOTA_Install$ = [Accepted] before transitioning to $FOTA_Install$ = [Nothing to report]Please refer to HMI

2. `4907886` — 章 **9.1** Pre-Installation — 分 **0.371**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI

3. `4907884` — 章 **9.1** Pre-Installation — 分 **0.348**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

4. `4907883` — 章 **9.1** Pre-Installation — 分 **0.341**
   > If the user cancel the pop-up or does not select an option within the timeout, then the HU shall send $FOTA_Install$ = [Not Accepted] before transitioning to $FOTA_Install$ = [Nothing to report]Please refer to HMI

5. `4907887` — 章 **9.1** Pre-Installation — 分 **0.316**
   > When the $Hybrid_Type$ = [BEV] or [PHEV] and if the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then the HU shall display "Schedule Update popup" (PUXXX3).Please refer to the latest Software Updates FOTA HMI L&amp;F.


---

#### 11. `SWE1-FOTA-100` — Handle Timeout or Cancel Action for Install Decision

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-127`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The ROV FOTA HMI shall start a response timer upon displaying the "ROV Forced Update Available B" pop-up. If the user cancels the pop-up, the ROV FOTA HMI shall notify the ROV Update Service. If no user selection is received within the configured timeout, the ROV FOTA HMI shall notify the ROV Update Service. Upon receiving the cancellation or timeout notification, the ROV Update Service shall set FOTA_Install to Not Accepted using CarPropertyManager. ( $FOTA_Install$ = [Not Accepted]) After setting FOTA_Install to Not Accepted, the ROV Update Service shall reset FOTA_Install to Nothing to report.

**`Verification Criteria` 全文**：

> Monitor response timer activation behavior after display of the “ROV Forced Update Available B” pop-up.
>
> Reproduce user cancellation and no-response timeout scenarios during the active pop-up session.
>
> Inspect handling of cancellation and timeout notifications toward the ROV Update Service.
>
> Validate FOTA_Install transitions to Not Accepted and resets to Nothing to report after notification processing.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907882` — 章 **9.1** Pre-Installation — 分 **0.473**
   > If the user selects 'Update Now' option on "ROV Forced Update Available B" pop-up, then HU shall send $FOTA_Install$ = [Accepted] before transitioning to $FOTA_Install$ = [Nothing to report]Please refer to HMI

2. `4907883` — 章 **9.1** Pre-Installation — 分 **0.415**
   > If the user cancel the pop-up or does not select an option within the timeout, then the HU shall send $FOTA_Install$ = [Not Accepted] before transitioning to $FOTA_Install$ = [Nothing to report]Please refer to HMI

3. `4907884` — 章 **9.1** Pre-Installation — 分 **0.315**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

4. `4907886` — 章 **9.1** Pre-Installation — 分 **0.307**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI

5. `4907880` — 章 **9.1** Pre-Installation — 分 **0.279**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI


---

#### 12. `SWE1-FOTA-101` — Allow Cancel or Ignore Action for Forced Update Popup A Under Permitted Delay State

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-126`
- `Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingSignal Condition Testing`

**Requirement Description 全文**：

> The ROV Update Service shall read the values from FOTA_Status and FOTA_Delay. The ROV FOTA HMI shall allow the user to cancel or ignore the "ROV Forced Update Available A" popup only when FOTA_Status is equal to Waiting for HMI Acceptance and FOTA_Delay is equal to Not_Prohibited.($FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]) If either condition is not satisfied, the ROV FOTA HMI shall not allow cancel or ignore interaction for the popup.

**`Verification Criteria` 全文**：

> Analyze handling of $FOTA_Status$ and $FOTA_Delay$ conditions during “ROV Forced Update Available A” pop-up interaction flow.
>
> Generate scenarios where $FOTA_Status$ = [Waiting for HMI Acceptance] and $FOTA_Delay$ = [Not Prohibited].
>
> Observe user interaction behavior for cancel and ignore actions under valid popup conditions.
>
> Confirm cancel or ignore interaction is restricted when either required condition is not satisfied.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907884` — 章 **9.1** Pre-Installation — 分 **0.729**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

2. `4907880` — 章 **9.1** Pre-Installation — 分 **0.624**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

3. `4907885` — 章 **9.1** Pre-Installation — 分 **0.454**
   > When the HU Receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Prohibited], the HU shall force the user to schedule an update and lock the user out per the requirements in the HMI.

4. `4907887` — 章 **9.1** Pre-Installation — 分 **0.293**
   > When the $Hybrid_Type$ = [BEV] or [PHEV] and if the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then the HU shall display "Schedule Update popup" (PUXXX3).Please refer to the latest Software Updates FOTA HMI L&amp;F.

5. `4907896` — 章 **9.1** Pre-Installation — 分 **0.288**
   > When the HU is in the pre-installation flow, if $FOTA_Status$ &lt;&gt; [Waiting for HMI Acceptance], the HU shall interrupt the current pre-installation flow and display appropriate HMI based on current $FOTA_Status$


---

#### 13. `SWE1-FOTA-102` — Force Update Scheduling When Delay Is Prohibited

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-125`
- `Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingPolicy State Testing`

**Requirement Description 全文**：

> The ROV Update Service shall retrieve FOTA_Status and FOTA_Delay using CarPropertyManager. If $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Prohibited], the ROV Update Service shall notify the ROV FOTA HMI to enforce forced update scheduling. The ROV FOTA HMI shall require the user to proceed through the Schedule Update flow. The ROV FOTA HMI shall not allow the user to skip, ignore, or dismiss the forced update. The ROV FOTA HMI shall enforce the lockout behavior until the user schedules the update.

**`Verification Criteria` 全文**：

> Recreate forced update conditions where $FOTA_Status$ = [Waiting for HMI Acceptance] and $FOTA_Delay$ = [Prohibited].
>
> Observe notification handling that triggers forced update scheduling flow toward the ROV FOTA HMI.
>
> Evaluate user interaction restrictions for skip, ignore, and dismiss operations during forced update handling.
>
> Confirm lockout behavior remains active until the user completes update scheduling through the required flow.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907884` — 章 **9.1** Pre-Installation — 分 **0.566**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

2. `4907880` — 章 **9.1** Pre-Installation — 分 **0.532**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

3. `4907886` — 章 **9.1** Pre-Installation — 分 **0.411**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI

4. `4907885` — 章 **9.1** Pre-Installation — 分 **0.407**
   > When the HU Receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Prohibited], the HU shall force the user to schedule an update and lock the user out per the requirements in the HMI.

5. `4907887` — 章 **9.1** Pre-Installation — 分 **0.323**
   > When the $Hybrid_Type$ = [BEV] or [PHEV] and if the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then the HU shall display "Schedule Update popup" (PUXXX3).Please refer to the latest Software Updates FOTA HMI L&amp;F.


---

#### 14. `SWE1-FOTA-103` — Launch Schedule Update HMI for ROV Forced Update

- 分類：非內部列｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-124`
- `Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingNavigation Flow Testing`

**Requirement Description 全文**：

> The ROV FOTA HMI shall capture user selection for "Schedule Update" from the "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up. Upon receiving the user selection, then ROV Update Service shall transition the flow to the Schedule Update HMI.

**`Verification Criteria` 全文**：

> Observe user interaction handling for “Schedule Update” selection from both forced update pop-up variants.
>
> Track notification flow generated after user selection from the ROV FOTA HMI.
>
> Examine transition handling initiated by the ROV Update Service after receiving the schedule request.
>
> Confirm navigation proceeds correctly from the forced update pop-up flow to the Schedule Update HMI.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907886` — 章 **9.1** Pre-Installation — 分 **0.644**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI

2. `4907887` — 章 **9.1** Pre-Installation — 分 **0.517**
   > When the $Hybrid_Type$ = [BEV] or [PHEV] and if the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then the HU shall display "Schedule Update popup" (PUXXX3).Please refer to the latest Software Updates FOTA HMI L&amp;F.

3. `4907888` — 章 **9.1** Pre-Installation — 分 **0.491**
   > When the $Hybrid_Type$ = [BEV] or [PHEV] or [FCEV] or [REPB] and if the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then the HU shall display "Schedule Update popup" (PUXXX3).Please refer to the latest Software Updates FOTA HMI L&amp;F.

4. `4907884` — 章 **9.1** Pre-Installation — 分 **0.450**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

5. `4907880` — 章 **9.1** Pre-Installation — 分 **0.367**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI


---

#### 15. `SWE1-FOTA-104` — Display BEV/PHEV Schedule Update Popup on Schedule Selection

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-123`
- `Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingVariant Testing`

**Requirement Description 全文**：

> The ROV Update Service shall retrieve $Hybrid_Type$ using CarPropertyManager. The ROV FOTA HMI shall capture user selection from the “ROV Forced Update Available A” or “ROV Forced Update Available B” pop-up. If $Hybrid_Type$ = [BEV] or [PHEV]and the user selects Schedule Update, the ROV FOTA HMI shall display the “Schedule Update pop-up (PUXXX3)”.

**`Verification Criteria` 全文**：

> Examine $Hybrid_Type$ retrieval handling for BEV and PHEV vehicle configurations.
>
> Capture user interaction flow for “Schedule Update” selection from forced update pop-ups.
>
> Recreate scheduling scenarios for vehicles identified as BEV or PHEV.
>
> Confirm “Schedule Update” pop-up (PUXXX3) is displayed when valid hybrid type and user selection conditions are satisfied.
>

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

#### 16. `SWE1-FOTA-105` — Display Schedule Update Pop-up for Supported Powertrain Types

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-122`
- `Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingVariant Testing`

**Requirement Description 全文**：

> The ROV Update Service shall retrieve $Hybrid_Type$ using CarPropertyManager. The ROV FOTA HMI shall capture user selection from the “ROV Forced Update Available A” or “ROV Forced Update Available B” pop-up. If $Hybrid_Type$ = [BEV] or [PHEV] or [FCEV] or [REPB]Band the user selects Schedule Update, then ROV FOTA HMI shall display the “Schedule Update pop-up (PUXXX3)” .

**`Verification Criteria` 全文**：

> Review $Hybrid_Type$ evaluation handling for BEV, PHEV, FCEV, and REPB vehicle configurations.
>
> Observe user interaction flow for “Schedule Update” selection from forced update availability pop-ups.
>
> Reproduce update scheduling scenarios across supported hybrid vehicle types.
>
> Verify “Schedule Update” pop-up (PUXXX3) is displayed when supported vehicle type and schedule selection conditions are met.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907888` — 章 **9.1** Pre-Installation — 分 **0.747**
   > When the $Hybrid_Type$ = [BEV] or [PHEV] or [FCEV] or [REPB] and if the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then the HU shall display "Schedule Update popup" (PUXXX3).Please refer to the latest Software Updates FOTA HMI L&amp;F.

2. `4907887` — 章 **9.1** Pre-Installation — 分 **0.703**
   > When the $Hybrid_Type$ = [BEV] or [PHEV] and if the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then the HU shall display "Schedule Update popup" (PUXXX3).Please refer to the latest Software Updates FOTA HMI L&amp;F.

3. `4907886` — 章 **9.1** Pre-Installation — 分 **0.570**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI

4. `4907884` — 章 **9.1** Pre-Installation — 分 **0.396**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

5. `4907889` — 章 **9.1** Pre-Installation — 分 **0.358**
   > If the user selects 'What's New' option on "ROV Forced Update Available A" or "ROV Forced Update Availbale B" pop-up, the HU shall display the pop-up (PU0410) with what's new details based on the information received from SGW_FOTA_HMI_ETM.4215.Please refer to the latest Software Updates FOTA HMI L&amp;F.


---

#### 17. `SWE1-FOTA-106` — Display “Conditions Not Met” Pop-up with Cancellation Reason

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-120`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The ROV Update Service shall retrieve $FOTA_Cancellation_Reason$ using CarPropertyManager. The ROV Update Service shall determine the corresponding cancellation reason text based on the received enumeration and the last cached server-provided mapping. The ROV Update Service shall notify the ROV FOTA HMI with the cancellation reason text. The ROV FOTA HMI shall display the “Conditions Not Met” (PUxxx1) pop-up with the corresponding cancellation reason text.

**`Verification Criteria` 全文**：

> Monitor $FOTA_Cancellation_Reason$ retrieval handling during update cancellation scenarios.
>
> Evaluate cancellation reason mapping behavior using received enumeration values and cached server-provided mappings.
>
> Observe notification flow carrying cancellation reason text toward the ROV FOTA HMI.
>
> Confirm “Conditions Not Met” (PUxxx1) pop-up displays the correct cancellation reason text for the active cancellation condition.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907891` — 章 **9.1** Pre-Installation — 分 **0.640**
   > When the HU receives $FOTA_Cancellation_Reason$, the HU shall display "Conditions Not Met" (PUxxx1) pop-up with the cancellation reason text last cached from the server based on the enumeration received. Please refer to the latest Software Updates FOTA HMI L&amp;F.

2. `4907890` — 章 **9.1** Pre-Installation — 分 **0.640**
   > When the HU receives $FOTA_Cancellation_Reason$, the HU shall display "Conditions Not Met" (PUxxx1) pop-up with the cancellation reason text last cached from the server based on the enumeration received. Please refer to the latest Software Updates FOTA HMI L&amp;F.

3. `4907892` — 章 **9.1** Pre-Installation — 分 **0.366**
   > When the HU receives $FOTA_Cancellation_Reason$, the HU shall display "Conditions Not Met" pop-up with the cancellation reason text as mentioned in the table below based on the enumeration received in the $FOTA_Cancellation_Reason$If $Hybrid_Type$ = [BEV] or [PHEV] or [FCEV] or [REPB] and $FOTA_Cancellation_Reason$ = [10], then display the cancellation reason "xEV: Propulsion system active"If $Hybrid_Type$ != [BEV] o…

4. `4907636` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.348**
   > If the installation conditions are not met, the HU shall cancel the scheduled update and display the 'Conditions Not Met' pop-up with the cancellation reason text as mentioned in the table below.If $Hybrid_Type$ = [BEV] or [PHEV] or [FCEV] or [REPB] and value for cancellation reason text = [7], then display the cancellation reason 'xEV: Propulsion system active'.If $Hybrid_Type$ != [BEV] or [PHEV] or [FCEV] or [REPB]…

5. `4907635` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.310**
   > When a scheduled HU FOTA update did not occur due to the preconditions not being met, then the HU shall display "Conditions Not Met" pop-up with the cancellation reason.- If ignition position is NOT OFF, $PowerMode$ != [IGN_OFF], then HU shall display “Ignition not OFF” as the cancellation reason on the pop-up- If Vehicle’s battery is NOT above 65% State of Charge, $IBS_SOC$ !&gt; [65] AND $IBS_SOC_ACCURACY$ != [0] O…


---

#### 18. `SWE1-FOTA-107` — Calculate and Report Remaining Time to Scheduled Install

- 分類：**126 內部列**（VC 有外部面）｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-118`
- `Verification Method`：`Unit Test / Integration Test / System TestTime Synchronization TestingScheduler Validation Testing`

**Requirement Description 全文**：

> The ROV Update Service shall store the determined scheduled installation time for the update event. The ROV Update Service shall retrieve the current system time from the system time source. The ROV Update Service shall calculate the time difference between the scheduled installation time and the current system time. The ROV Update Service shall set $HU_Scheduled_Install$ with the calculated remaining time value using CarPropertyManager.

**`Verification Criteria` 全文**：

> Examine storage handling for scheduled installation time associated with the update event.
>
> Observe retrieval of current system time during scheduled installation processing.
>
> Analyze remaining time calculation behavior between scheduled installation time and current system time.
>
> Confirm $HU_Scheduled_Install$ is updated with the calculated remaining installation time value.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907894` — 章 **9.1** Pre-Installation — 分 **0.472**
   > When the scheduled time has been determined, the HU shall compare the current system time (defined in CFTS015) to the scheduled time and then send the difference in $HU_Scheduled_Install$

2. `4907915` — 章 **9.4.1** Pre-Installation — 分 **0.259**
   > When the scheduled time is reached, TBM shall send $Install_Time_Reached$ to SGW.

3. `4907900` — 章 **9.2** Installation Progress — 分 **0.228**
   > The HU shall populate the installation percentage and estimated time remaining progress in the pop-up, "Installation Progress ROV" based on the status received from SGW_FOTA_HMI_ETM.4215

4. `4907633` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.191**
   > If the user schedules an update, the HU shall wake up at the scheduled time and check the last known preinstallation conditions, if the conditions are met the HU shall start the installation

5. `4907886` — 章 **9.1** Pre-Installation — 分 **0.183**
   > If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Available B" pop-up, then HU shall continue through the Schedule Update HMI


---

#### 19. `SWE1-FOTA-108` — Display No Connectivity Pop-up for ROV Update

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-117`
- `Verification Method`：`Unit Test / Integration Test / System TestHMI Validation TestingNetwork Condition Testing`

**Requirement Description 全文**：

> The ROV FOTA HMI shall capture user selection of “Update Now” from the “ROV Forced Update Available B” pop-up. The ROV Update Service shall retrieve $LTE_Status$ or $Cellsignal$ using CarPropertyManager. If ROV Update Service receives $LTE_Status$ <> [3G OR 4G OR H_Plus] OR $Cellsignal$ = [0 OR 1 OR SNA], the ROV Update HMI shall display the "No Connectivity" pop-up and prevent update initiation.

**`Verification Criteria` 全文**：

> Capture user interaction flow for “Update Now” selection from the “ROV Forced Update Available B” pop-up.
>
> Recreate network conditions where $LTE_Status$ is outside supported connectivity states or $Cellsignal$ indicates weak or unavailable signal levels.
>
> Evaluate connectivity validation behavior before update initiation processing.
>
> Confirm “No Connectivity” pop-up is displayed and update initiation is blocked under invalid network conditions.
>

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

#### 20. `SWE1-FOTA-109` — Interrupt Pre-Installation Flow on Status Change

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-116`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The ROV Update Service shall retrieve $FOTA_Status$ using CarPropertyManager. During the pre-installation flow, if $FOTA_Status$ <> [Waiting for HMI Acceptance], the ROV Update Service shall interrupt the current pre-installation flow and shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the appropriate HMI based on current FOTA_Status.

**`Verification Criteria` 全文**：

> Monitor $FOTA_Status$ handling during active pre-installation processing flow.
>
> Reproduce status transition scenarios where $FOTA_Status$ changes from Waiting for HMI Acceptance to another state.
>
> Observe interruption behavior of the ongoing pre-installation flow after status change detection.
>
> Confirm the ROV FOTA HMI switches to the appropriate HMI screen corresponding to the updated $FOTA_Status$.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907896` — 章 **9.1** Pre-Installation — 分 **0.746**
   > When the HU is in the pre-installation flow, if $FOTA_Status$ &lt;&gt; [Waiting for HMI Acceptance], the HU shall interrupt the current pre-installation flow and display appropriate HMI based on current $FOTA_Status$

2. `4907880` — 章 **9.1** Pre-Installation — 分 **0.425**
   > When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU shall show "ROV Forced Update Available A" pop-up as defined in HMI

3. `4907884` — 章 **9.1** Pre-Installation — 分 **0.391**
   > User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Available A" only if the HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not Prohibited]

4. `4907898` — 章 **9.2** Installation Progress — 分 **0.300**
   > When the HU receives $FOTA_Status$ = [Installing FOTA Update], the HU shall display installation screens.

5. `4907900` — 章 **9.2** Installation Progress — 分 **0.285**
   > The HU shall populate the installation percentage and estimated time remaining progress in the pop-up, "Installation Progress ROV" based on the status received from SGW_FOTA_HMI_ETM.4215


---

## 節 —— `Update HMI`（6 列）

能力叢集：更新之使用者體驗與 HMI 呈現

| # | 037 列 | 標題 | Sub Cat | Priority | 105？ | 首選分 | 機制 3 |
|---:|---|---|---|---|:--:|---:|:--:|
| 1 | `SWE1-FOTA-130` | Support NAFTA Region Languages for S | HMI | High | — | 0.378 | — |
| 2 | `SWE1-FOTA-131` | Support Server-Configured Update Typ | Service | High | — | 0.300 | — |
| 3 | `SWE1-FOTA-132` | Enforce Terms and Conditions Accepta | HMI | High | — | 0.539 | — |
| 4 | `SWE1-FOTA-133` | Display Release Notes and Interactiv | HMI | High | — | 0.588 | — |
| 5 | `SWE1-FOTA-134` | Display Post-Download Installation O | HMI | High | — | 0.509 | — |
| 6 | `SWE1-FOTA-136` | Control Deployment Rejection Based o | HMI | High | — | 0.331 | — |

### `Update HMI` —— 逐列材料


---

#### 1. `SWE1-FOTA-130` — Support NAFTA Region Languages for SW Update HMI

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-216`
- `Verification Method`：`Unit Test / Integration Test / System TestLocalization Validation Testing`

**Requirement Description 全文**：

> The MCPU platform software shall provide localization support for the three languages required for the NAFTA region. The supported languages shall include English, North American French, and North American Spanish. The HMI shall display update-related text and messages using the language currently configured in language settings.

**`Verification Criteria` 全文**：

> Review localization support handling for update-related HMI content across NAFTA region language configurations.
>
> Reproduce language selection scenarios for English, North American French, and North American Spanish settings.
>
> Observe HMI behavior after changing the active system language configuration.
>
> Confirm update-related text and messages are displayed according to the currently configured language setting
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907653` — 章 **4.11** User Experience (UX)/HMI — 分 **0.378**
   > HU shall support all 3 languages supported in the NAFTA region.

2. `4907316` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.102**
   > The OTA client shall be able to display download descriptor information to the HMI, if available, including text description and update size.

3. `4907744` — 章 **4.13.4.1** Appendix A Download Descriptor Format — 分 **0.100**
   > The Download Descriptor (DD) describes the deployment package that the OTA server sends to the vehicle. The DD is a simple XML file that contains the parameters listed in the following table. Table A-1: Download Descriptor Parameters Name Description installParam An installation parameter associated with the download package. It contains an embedded XML with the &lt;installerType&gt; tag, which contains a command-sep…

4. `4907495` — 章 **4.8** Security — 分 **0.085**
   > FOTA software shall only be available in NAFTA vehicles with embedded cell modems, all FOTA software shall be removed from the HU otherwise.

5. `4907826` — 章 **7.1** Critical Updates — 分 **0.084**
   > User shall be able to navigate to software download via Wi-Fi from the pop up or from the settings menu (kindly see the HMI)


---

#### 2. `SWE1-FOTA-131` — Support Server-Configured Update Types With Consistent User Experience

- 分類：非內部列｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-219`
- `Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**Requirement Description 全文**：

> The WiFi Update Service shall retrieve update type configuration from the OTA server for each update campaign using SWMC. The supported update types shall include regular, critical, and silent updates. The WiFi Update Service shall apply the update flow behavior according to the received update type configuration. The SW Update HMI shall provide a consistent user interaction flow across supported update types while applying update-type-specific notifications, restrictions, and interaction behavior. The WiFi Update Service shall control the applicable update flow according to the server-defined update type configuration.

**`Verification Criteria` 全文**：

> Examine update type configuration retrieval handling for OTA campaigns received from the OTA server.
>
> Recreate update scenarios using regular, critical, and silent update type configurations.
>
> Observe update flow behavior changes based on the configured update type and corresponding restrictions or notifications.
>
> Confirm the SW Update HMI maintains a consistent interaction flow while applying update-type-specific behaviors defined by the server configuration.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907453` — 章 **4.7.3** Main Update Configuration Options — 分 **0.300**
   > Update type:

2. `4907656` — 章 **4.11** User Experience (UX)/HMI — 分 **0.299**
   > User experience shall be same for all update types and updates (regular/critical/silent) SHOULD be configurable from the server so that the FOTA service administrator can select the relevant option depending on the type and urgency of the update being performed.

3. `4907435` — 章 **4.7** OTA Client Application — 分 **0.268**
   > The OTA client's primary use case is managing firmware components. Update flow types include Critical, Silent, and Regular that are defined in this section.

4. `4907456` — 章 **4.7.3** Main Update Configuration Options — 分 **0.234**
   > Regular update: Non-silent, non-critical update. End-user/HMI flow shall be followed, and Network bearer rules apply.

5. `4907476` — 章 **4.7.3.2** Silent Updates — 分 **0.206**
   > Silent updates shall not display progress notifications and shall NOT require end-user interaction.


---

#### 3. `SWE1-FOTA-132` — Enforce Terms and Conditions Acceptance Before Download

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-220`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The SWMC shall determine whether terms and conditions acceptance is required based on the Download Descriptor metadata. Before initiating the update download, the SWMC shall check the customer acceptance status from the FCA IT customer preference database. If the customer has not accepted the required terms and conditions, the SWMC shall provide SW Update HMI guidance describing how the customer can complete the acceptance process. The SWMC shall block update download initiation until terms and conditions acceptance is confirmed.

**`Verification Criteria` 全文**：

> Analyze terms and conditions requirement evaluation using Download Descriptor metadata during update preparation flow.
>
> Reproduce customer acceptance status scenarios using accepted and non-accepted preference states from the customer preference database.
>
> Observe HMI guidance behavior presented when mandatory terms and conditions acceptance is incomplete.
>
> Confirm update download initiation remains blocked until required terms and conditions acceptance is successfully confirmed.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907657` — 章 **4.11** User Experience (UX)/HMI — 分 **0.539**
   > If acceptance of terms and conditions is required prior to downloading an update, the system SHALL check FCA IT's customer preference database prior to downloading update file. If customer has not accepted the terms and conditions, FOTA Client shall provide HMI to the customer to describe how to accept.

2. `4907588` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.266**
   > 6. After acceptance, the OTA client shall check for download pre-conditions and then download the deployment package.

3. `4907618` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.222**
   > Download of the file shall not be customer facing.

4. `4907587` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.172**
   > 5. OTA client SHALL download the DD and use the information in it to prompt HMI for acceptance of the deployment package.

5. `4907644` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.155**
   > Radio has to be recoverable by the customer to retry the update in case the installation is not successful.


---

#### 4. `SWE1-FOTA-133` — Display Release Notes and Interactive Links from DD

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-223`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The SWMC shall parse the Download Descriptor after completion of the update download and extract consumer-approved release notes information, update-related information, and associated links. The SWMC shall provide the extracted release notes information and associated links to the SW Update HMI. The SW Update HMI shall display the release notes information, update-related information, and associated links during the opt-in and download screens. The SW Update HMI shall support user interaction with embedded links displayed as part of the update information.

**`Verification Criteria` 全文**：

> Examine Download Descriptor parsing behavior for extraction of release notes, update-related information, and associated links after update download completion.
>
> Observe transfer of extracted release notes content and related links toward the SW Update HMI.
>
> Recreate opt-in and download flow scenarios to assess display of update information and embedded links.
>
> Confirm the SW Update HMI supports user interaction with displayed links during update information presentation.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907660` — 章 **4.11** User Experience (UX)/HMI — 分 **0.588**
   > After the download the OTA client shall display the approved for consumer view release notes information in the DD file along with any other information or links about the update. The end user shall be able to tap any links and interact with this information during the opt in and download screens.

2. `4907316` — 章 **4.4.1** OTA Architecture Requirements — 分 **0.201**
   > The OTA client shall be able to display download descriptor information to the HMI, if available, including text description and update size.

3. `4907899` — 章 **9.2** Installation Progress — 分 **0.160**
   > The HU shall receive HMI information via Ethernet Message SGW_FOTA_HMI_ETM.4215 such as- Estimated completion time- Time remaining- Progress information- Whats new information

4. `4907246` — 章 **2** Common Reflash Requirements — 分 **0.156**
   > When a FOTA update is ready to install and an USB update is available at the same time, the HU shall honor the latest software version release available.

5. `4907587` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.153**
   > 5. OTA client SHALL download the DD and use the information in it to prompt HMI for acceptance of the deployment package.


---

#### 5. `SWE1-FOTA-134` — Display Post-Download Installation Options

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-224`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The SWMC shall detect completion of the deployment package download. After completion of the download, the SWMC shall provide deployment package details to the SW Update HMI through WiFi Update Service. The SW Update HMI shall display the deployment package details to the user . The SW Update HMI shall provide opt-in options including “Install” and “Schedule Later”.

**`Verification Criteria` 全文**：

> Monitor deployment package download completion handling within the SWMC update workflow.
>
> Observe transfer of deployment package details from the SWMC to the SW Update HMI through the WiFi Update Service.
>
> Evaluate HMI behavior for displaying deployment package information after successful download completion.
>
> Confirm the SW Update HMI presents user opt-in actions including “Install” and “Schedule Later” options.
>

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

#### 6. `SWE1-FOTA-136` — Control Deployment Rejection Based on OTA Flags

- 分類：非內部列｜Sub Cat：HMI｜Priority：High｜Source：`SYS-RA-FOTA-227`
- `Verification Method`：`Integration Test`

**Requirement Description 全文**：

> The SWMC shall retrieve the Critical Update and Silent Install configuration flags from the OTA server deployment metadata. The SWMC shall determine whether end-user rejection of the OTA deployment is permitted based on the received Critical Update and Silent Install flag . The SW Update HMI shall allow or restrict user rejection options according to the deployment interaction policy received from the SWMC via WiFi Update Service.

**`Verification Criteria` 全文**：

> Examine retrieval handling for Critical Update and Silent Install configuration flags from OTA deployment metadata.
>
> Recreate deployment scenarios using different combinations of Critical Update and Silent Install policy configurations.
>
> Observe deployment interaction policy evaluation for allowing or restricting end-user rejection behavior.
>
> Confirm the SW Update HMI applies user rejection restrictions according to the deployment interaction policy received through the WiFi Update Service.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907600` — 章 **4.10.5** Deployment Flow — 分 **0.331**
   > If deployed OTA, whether end-users can reject the deployment depends on the Critical Update and Silent Install flags that are set by the OTA server.

2. `4907487` — 章 **4.7.3.2** Silent Updates — 分 **0.184**
   > If the DDF does not include whether the update is silent or not, the HU shall treat the update as a non-silent update

3. `4907473` — 章 **4.7.3.1** Critical Updates — 分 **0.177**
   > If the DDF does not include whether the update is critical or not, the HU shall treat the update as a non-critical update

4. `4907476` — 章 **4.7.3.2** Silent Updates — 分 **0.177**
   > Silent updates shall not display progress notifications and shall NOT require end-user interaction.

5. `4907456` — 章 **4.7.3** Main Update Configuration Options — 分 **0.176**
   > Regular update: Non-silent, non-critical update. End-user/HMI flow shall be followed, and Network bearer rules apply.

