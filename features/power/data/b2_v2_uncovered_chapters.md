# B2 v2 — A-PW16 九章判定素材（R-P38：被引用之錨點 vs leaf）

> 取代 `b2_uncovered_chapters.md`（該檔以「章 vs leaf」比對，單位有誤）。
> 依 R-P27 與 05 §I：本檔**不建議任何處置**。
> 依 R-P41(a)：事實部分全部由 `scripts/build_b2.py` 產生；
> 判讀欄為人工，以該腳本之 `JUDGEMENTS` 常數保存並隨腳本版控。

## 判定總表

| 章節 | 標題 | 錨點總數 | 被引用 | 未被引用 | 引用之 leaf | 判定 |
|---|---|---|---|---|---|---|
| §1.6.2.1 | TLM algorithm requirements | 2 | **2** | 0 | `SWE-PM-001`, `SWE-PM-002`, `SWE-PM-003`, `SWE-PM-004`, `SWE-PM-005`, `SWE-PM-006`, `SWE-PM-007`, `SWE-PM-008`, `SWE-PM-009` | **無法判定** |
| §1.6.2.1.4 | Stolen Vehicle Mode | 2 | **1** | 1 | `SWE-PM-003` | **未涵蓋** |
| §1.6.2.1.9 | Logistic Idle | 4 | **3** | 1 | `SWE-PM-008` | **部分涵蓋** |
| §1.6.2.1.10 | Logistic Standby | 2 | **2** | 0 | `SWE-PM-008` | **部分涵蓋** |
| §1.6.2.1.11 | Logistic Sleep | 2 | **2** | 0 | `SWE-PM-008` | **部分涵蓋** |
| §1.6.2.1.14 | TLM modules and functionalities depending on operative state | 8 | **1** | 7 | `SWE-PM-001`, `SWE-PM-002`, `SWE-PM-003`, `SWE-PM-004`, `SWE-PM-005`, `SWE-PM-006`, `SWE-PM-007`, `SWE-PM-008`, `SWE-PM-009` | **部分涵蓋** |
| §1.6.2.1.15.1 | ICS Wakeup Reasons by POWER Button Pressed | 3 | **1** | 2 | `SWE-PM-004` | **涵蓋** |
| §1.6.3.1.1 | SwitchOff_Timeout_Setting.Req management | 3 | **3** | 0 | `SWE-PM-057` | **涵蓋（一分支例外）** |
| §1.8.1.1.1 | ID 1 Description | 5 | **3** | 2 | `SWE-PM-057` | **涵蓋** |

---

## §1.6.2.1 — TLM algorithm requirements　`{4941353}`

### 該章之全部需求錨點（2 個）

| 錨點 id | 是否被引用 | 引用之 leaf | 內文首 120 字元 |
|---|---|---|---|
| `4941354` | **是** | `SWE-PM-001`, `SWE-PM-002`, `SWE-PM-003`, `SWE-PM-004`, `SWE-PM-005`, `SWE-PM-006`, `SWE-PM-007`, `SWE-PM-008`, `SWE-PM-009` | CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource |
| `4941355` | **是** | `SWE-PM-001`, `SWE-PM-002`, `SWE-PM-003`, `SWE-PM-004`, `SWE-PM-005`, `SWE-PM-006`, `SWE-PM-007`, `SWE-PM-008`, `SWE-PM-009` | CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource |

**被引用之錨點**（2）：`4941354`, `4941355`

**未被引用之錨點**（0）：**無**

### 被引用錨點之全文（判讀單位，R-P38）

#### `4941354`　引用者：`SWE-PM-001`, `SWE-PM-002`, `SWE-PM-003`, `SWE-PM-004`, `SWE-PM-005`, `SWE-PM-006`, `SWE-PM-007`, `SWE-PM-008`, `SWE-PM-009`

metadata：`4941354: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:R1H, VP2R84, VP3, R1L-R, VP2R7, VP2, VP1, VP465, VP5R120, High, VP0, VP2R5, VP4R7, VP484, VP384, CTS1_2, VP365, VP2.5, VP4, R1M, VP4R84, VP1.5, R1L] [EE Architecture:Atlantis High, Atlantis Mid]`

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

#### `4941355`　引用者：`SWE-PM-001`, `SWE-PM-002`, `SWE-PM-003`, `SWE-PM-004`, `SWE-PM-005`, `SWE-PM-006`, `SWE-PM-007`, `SWE-PM-008`, `SWE-PM-009`

metadata：`4941355: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM, RRM] [Market:All] [Radio:R1L-R, VP2R7, R1L, VP2R5, VP2R84] [EE Architecture:Atlantis High, Atlantis Mid]`

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### 引用本章之 leaf 之 Requirement Description（全文）

#### `SWE-PM-001` — Full-Operation

```
* HW supplier shall notify 'Full-Operation' power state through custom power interface
* MD power service shall apply power policy corresponding to full operation to enable all features. Ensure
 - Display is on
 - Audio un-muted
 - BT on
 - Tuner on
 - USB on
 - AUX on
* All applications and services shall subscribe to power state and policy change notification and take necessary action to enable features
```

Verification Criteria：

```
Vehicle equiped with CAN
HU in Sleep state
```

Verification Method：

```
Change Ingition from Off to other value

HU shall boot and show HMI screen

Select Audio source and audio shall be heard

Shall be able to pair smartphone and use AACP features
```

#### `SWE-PM-002` — Idle

```
* HW supplier shall notify 'Idle' power state through custom power interface
* MD power service shall apply power policy corresponding to Idle. Ensure
 - Display is off
 - audio is muted except for ADAS related chimes
 - Bluetooth is on
 - Tuner is on
 - USB is off
 - AUX is off
* All applications and services shall subscribe to power state and policy change notification and take necessary action to enable / disable feature.
*  Disable features which require to display on HMI
* Display shall be turned on to show Rear Camera image, Antitheft HMI
* Ensure audio is muted for all the sources
* Phone call features are active through BT / AACP to recieve calls
```

Verification Criteria：

```
Vehicle equiped with CAN
HU in Full-Operation
```

Verification Method：

```
Pres front panel on-off button / ICS Power button.

Display shall show blank screen, audio shall be muted except for ADAS chimes.

Shall allow phone call and activate Siri through SWC
```

#### `SWE-PM-003` — Partial Operation

```
* HW supplier shall notify 'Partial Operation' power state through custom power interface
* MD power service shall apply power policy corresponding to Partial Operation. Ensure
 - Display is off except to show Antitheft screen
 - audio shall be muted except for ADAS related chimes
 - Bluetooth is off
 - Tuner is on
 - USB is off
 - AUX is off
* All applications and services shall subscribe to power state and policy change notification and be ready in background once partial operation state is notified.
*  Disable features which require to display on HMI
* Ensure audio is muted for all the sources
```

Verification Criteria：

```
Vehicle equiped with CAN
HU in Sleep state
```

Verification Method：

```
Change STATUS_BH_BCM2.RemStActvSts to "Remote Start Active"

Observe $Telematic_Power$ = "Partial_Operation"
```

#### `SWE-PM-004` — Timed

```
* HW supplier shall notify 'Timed' power state through custom power interface
* MD power service shall apply power policy corresponding to Timed power state. Ensure
 - Display is on
 - Audio un-muted
 - BT on
 - Tuner on
 - USB on
 - AUX on
* All applications and services shall subscribe to power state and policy change notification and take necessary action to enable / disable features
* User settings option shall be disable in Timed power state
```

Verification Criteria：

```
Vehicle equiped with CAN

HU in Full-Operation state
```

Verification Method：

```
Change SWITCH_OFF_DOOR setting to OFF

Change SwitchOff_Timeout_Setting.Req to non-zero

Change ignition state to Off

Observe HU enters into Timed power state, HMI and audio function normal

User setting are not modifiable
```

#### `SWE-PM-005` — Standby

```
* HW supplier shall notify 'Standby' power state through custom power interface
* MD power service shall apply power policy corresponding to Standby power state. Ensure
 - Display is Off, except to show splash
 - Audio muted
 - BT Off
 - Tuner Off
 - USB Off
 - AUX Off
* All applications and services shall subscribe to power state and policy change notification and take necessary action to enable / disable features
```

Verification Criteria：

```
Vehicle equiped with CAN

HU in Sleep state
```

Verification Method：

```
Open the door and close the door

Observe Splash on screen

Observe $Telematic_Power$ = "Standby"
```

#### `SWE-PM-006` — Sleep

```
* HW supplier shall notify 'Sleep' power  state through custom power interface
* MD power service shall apply power policy corresponding to Standby power state. Ensure
 - Display is Off, except to show splash
 - Audio muted
 - BT Off
 - Tuner Off
 - USB Off
 - AUX Off
* Transiting to sleep state, all apps and service prepare to shutdown (or STR)
```

Verification Criteria：

```
Vehicle equiped with CAN

HU in Sleep state
```

Verification Method：

```
Observe HU screen turned off and CAN NW activity will be turned OFF
```

#### `SWE-PM-007` — Bench

```
* HW supplier shall notify 'Bench' state through custom power interface
* subcomponents shall ensure all features are available for development / testing
```

Verification Criteria：

```
Vehicle not equiped with CAN or engineering line is active
```

Verification Method：

```
Change ignition state from Off to On

HU shall boot till HMI and all features are available
```

#### `SWE-PM-008` — Logistic Mode

```
* HW supplier shall notify Logistic state (Logistic Idle/ Logistic Standby / Lgistic Sleep) though custom power state interface
* subcomponents shall ensure no features are availabel and prepare to shutdown
```

Verification Criteria：

```
Vehicle equiped with CAN
```

Verification Method：

```
Change signal STATUS_BH_BCM1.PowerModeSts to "Logistic_Mode_On"

HU shall shutdown and no functionalities available
```

#### `SWE-PM-009` — Init state

```
* HW supplier shall notify Init power state though custom power state interface
* subcomponents shall stop activities upon receiving Init power state, until exiting this state
* Settings service shall restore settings to before init state values after exiting init state
```

Verification Criteria：

```
Vehicle equiped with CAN

HU in full operation state
```

Verification Method：

```
Perform voltag spike / drop EMC test as per CS.00244 and observe the behavior
```

### 判讀（人工）

**判定：無法判定**

被引用之兩個錨點 `4941354`、`4941355` 之文字層內容各只有一行 `CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource` 與 `CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource`，即其實質內容為嵌入之 inline RTF 物件，**不在 R-P17 之文字層內**。既無可判讀之行為敘述，即無從與任何 leaf 之 Description 比對。（此即 R-P39 所要清點之情形。）

### 本章全文（不截斷，630 字元）

```
4941354: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:R1H, VP2R84, VP3, R1L-R, VP2R7, VP2, VP1, VP465, VP5R120, High, VP0, VP2R5, VP4R7, VP484, VP384, CTS1_2, VP365, VP2.5, VP4, R1M, VP4R84, VP1.5, R1L] [EE Architecture:Atlantis High, Atlantis Mid]
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
4941355: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM, RRM] [Market:All] [Radio:R1L-R, VP2R7, R1L, VP2R5, VP2R84] [EE Architecture:Atlantis High, Atlantis Mid]
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

---

## §1.6.2.1.4 — Stolen Vehicle Mode　`{4941398}`

### 該章之全部需求錨點（2 個）

| 錨點 id | 是否被引用 | 引用之 leaf | 內文首 120 字元 |
|---|---|---|---|
| `4941399` | 否 | — | When the HU receives the High priority Stolen Vehicle SMS, it shall enter stolen vehicle mode. The HU shall keep powered |
| `4941400` | **是** | `SWE-PM-003` | the R1 HU shall not enter stolen vehicle mode under any condition |

**被引用之錨點**（1）：`4941400`

**未被引用之錨點**（1）：`4941399`

### 被引用錨點之全文（判讀單位，R-P38）

#### `4941400`　引用者：`SWE-PM-003`

metadata：`4941400: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM] [Market:All] [Model Year:2022, 2021, 2024, 2023, 2025] [Radio:R1L, R1H, R1M, R1L-R] [EE Architecture:Atlantis High, Atlantis Mid]`

```
the R1 HU shall not enter stolen vehicle mode under any condition
```

### 引用本章之 leaf 之 Requirement Description（全文）

#### `SWE-PM-003` — Partial Operation

```
* HW supplier shall notify 'Partial Operation' power state through custom power interface
* MD power service shall apply power policy corresponding to Partial Operation. Ensure
 - Display is off except to show Antitheft screen
 - audio shall be muted except for ADAS related chimes
 - Bluetooth is off
 - Tuner is on
 - USB is off
 - AUX is off
* All applications and services shall subscribe to power state and policy change notification and be ready in background once partial operation state is notified.
*  Disable features which require to display on HMI
* Ensure audio is muted for all the sources
```

Verification Criteria：

```
Vehicle equiped with CAN
HU in Sleep state
```

Verification Method：

```
Change STATUS_BH_BCM2.RemStActvSts to "Remote Start Active"

Observe $Telematic_Power$ = "Partial_Operation"
```

### 判讀（人工）

**判定：未涵蓋**

本章兩個錨點中**僅 `4941400` 被引用**（`SWE-PM-003` 經 `Sys-RA-PM-0031`）；`4941399` 未被任何 leaf 引用。`4941400` 逐字為「the R1 HU shall not enter stolen vehicle mode under any condition」，`Radio` 欄含本專案車型 `R1L`。`SWE-PM-003`（Partial Operation）之 Description 全文無 stolen vehicle 相關敘述。**判讀單位訂正後之結論**：未涵蓋者為一條**否定需求**（不得進入該模式），非「防盜功能」——A-PW16 稱本章為「實質功能章節」不準確。未被引用之 `4941399`（描述進入條件，`Radio` 欄 `VP4R7, VP4R84` 不含 R1L）不在本 feature 範圍內。

### 本章全文（不截斷，864 字元）

```
4941399: [Artifact Type:Subsystem Functional Requirement] [State:New] [ECU:ETM] [Market:All] [Model Year:2017] [Radio:VP4R7, VP4R84] [EE Architecture:Atlantis Mid, Atlantis High]
When the HU receives the High priority Stolen Vehicle SMS, it shall enter stolen vehicle mode. The HU shall keep powered only the components needed to send the GPS location and maintain a 7 day timer. The HU shall remain in this state until it receives the SMS indicating the Stolen Vehicle has been recovered, 7 days has passed, or until the Battery drains and the HU can no longer remain powered.
4941400: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM] [Market:All] [Model Year:2022, 2021, 2024, 2023, 2025] [Radio:R1L, R1H, R1M, R1L-R] [EE Architecture:Atlantis High, Atlantis Mid]
the R1 HU shall not enter stolen vehicle mode under any condition
```

---

## §1.6.2.1.9 — Logistic Idle　`{4941425}`

### 該章之全部需求錨點（4 個）

| 錨點 id | 是否被引用 | 引用之 leaf | 內文首 120 字元 |
|---|---|---|---|
| `4941426` | **是** | `SWE-PM-008` | In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Igni |
| `4941427` | **是** | `SWE-PM-008` | This status is related to TLM, FPDM AMP, ICS, and DTV OFF with Logistic Mode active. |
| `4941428` | **是** | `SWE-PM-008` | TLM and AMP has not to reproduce any audio source and the user can't do any setting. |
| `4941429` | 否 | — | Audio and Telematic modules shall be in this mode when they receive $Telematic_Power$ = [Logistic_On]. |

**被引用之錨點**（3）：`4941426`, `4941427`, `4941428`

**未被引用之錨點**（1）：`4941429`

### 被引用錨點之全文（判讀單位，R-P38）

#### `4941426`　引用者：`SWE-PM-008`

metadata：`4941426: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, RRM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]`

```
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On,
```

#### `4941427`　引用者：`SWE-PM-008`

metadata：`4941427: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, FPDM, LTM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]`

```
This status is related to TLM, FPDM AMP, ICS, and DTV OFF with Logistic Mode active.
```

#### `4941428`　引用者：`SWE-PM-008`

metadata：`4941428: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM, AMP, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]`

```
TLM and AMP has not to reproduce any audio source and the user can't do any setting.
```

### 引用本章之 leaf 之 Requirement Description（全文）

#### `SWE-PM-008` — Logistic Mode

```
* HW supplier shall notify Logistic state (Logistic Idle/ Logistic Standby / Lgistic Sleep) though custom power state interface
* subcomponents shall ensure no features are availabel and prepare to shutdown
```

Verification Criteria：

```
Vehicle equiped with CAN
```

Verification Method：

```
Change signal STATUS_BH_BCM1.PowerModeSts to "Logistic_Mode_On"

HU shall shutdown and no functionalities available
```

### 判讀（人工）

**判定：部分涵蓋**

四個錨點中 `4941426` / `4941427` / `4941428` 被引用（皆 `SWE-PM-008`），`4941429`（`$Telematic_Power$` = [Logistic_On]）**未被引用，不在判讀範圍內**。`SWE-PM-008` Description 逐字列出三個狀態名「Logistic Idle/ Logistic Standby / Lgistic Sleep」——**狀態名稱涵蓋**。但被引用錨點之實質內容 —— `4941426` 之「In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On」、`4941427` 之「related to TLM, FPDM AMP, ICS, and DTV OFF with Logistic Mode active」、`4941428` 之「TLM and AMP has not to reproduce any audio source and the user can't do any setting」——在 Description 中皆無對應文字。

### 本章全文（不截斷，1216 字元）

```
4941426: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, RRM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On,
4941427: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, FPDM, LTM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
This status is related to TLM, FPDM AMP, ICS, and DTV OFF with Logistic Mode active.
4941428: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM, AMP, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
TLM and AMP has not to reproduce any audio source and the user can't do any setting.
4941429: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:TBM, CDM, DCSD, DVD, DTV, MHU, AMP, VRM, TBM2, ANC] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
Audio and Telematic modules shall be in this mode when they receive $Telematic_Power$ = [Logistic_On].
```

---

## §1.6.2.1.10 — Logistic Standby　`{4941430}`

### 該章之全部需求錨點（2 個）

| 錨點 id | 是否被引用 | 引用之 leaf | 內文首 120 字元 |
|---|---|---|---|
| `4941431` | **是** | `SWE-PM-008` | In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off, |
| `4941432` | **是** | `SWE-PM-008` | This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network active |

**被引用之錨點**（2）：`4941431`, `4941432`

**未被引用之錨點**（0）：**無**

### 被引用錨點之全文（判讀單位，R-P38）

#### `4941431`　引用者：`SWE-PM-008`

metadata：`4941431: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, ETM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]`

```
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
```

#### `4941432`　引用者：`SWE-PM-008`

metadata：`4941432: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]`

```
This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network active
```

### 引用本章之 leaf 之 Requirement Description（全文）

#### `SWE-PM-008` — Logistic Mode

```
* HW supplier shall notify Logistic state (Logistic Idle/ Logistic Standby / Lgistic Sleep) though custom power state interface
* subcomponents shall ensure no features are availabel and prepare to shutdown
```

Verification Criteria：

```
Vehicle equiped with CAN
```

Verification Method：

```
Change signal STATUS_BH_BCM1.PowerModeSts to "Logistic_Mode_On"

HU shall shutdown and no functionalities available
```

### 判讀（人工）

**判定：部分涵蓋**

狀態名稱涵蓋（同 §1.6.2.1.9）。被引用錨點之區辨條件「Ignition Pre Off, Ignition Off」＋「Logistic Mode active **AND network active**」在 Description 中無對應；Description 僅有「subcomponents shall ensure no features are availabel and prepare to shutdown」，未區分 network 狀態。

### 本章全文（不截斷，562 字元）

```
4941431: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, ETM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
4941432: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network active
```

---

## §1.6.2.1.11 — Logistic Sleep　`{4941433}`

### 該章之全部需求錨點（2 個）

| 錨點 id | 是否被引用 | 引用之 leaf | 內文首 120 字元 |
|---|---|---|---|
| `4941434` | **是** | `SWE-PM-008` | In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off, |
| `4941435` | **是** | `SWE-PM-008` | This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network off. |

**被引用之錨點**（2）：`4941434`, `4941435`

**未被引用之錨點**（0）：**無**

### 被引用錨點之全文（判讀單位，R-P38）

#### `4941434`　引用者：`SWE-PM-008`

metadata：`4941434: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, RRM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]`

```
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
```

#### `4941435`　引用者：`SWE-PM-008`

metadata：`4941435: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, RRM, ETM, FPDM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]`

```
This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network off.
```

### 引用本章之 leaf 之 Requirement Description（全文）

#### `SWE-PM-008` — Logistic Mode

```
* HW supplier shall notify Logistic state (Logistic Idle/ Logistic Standby / Lgistic Sleep) though custom power state interface
* subcomponents shall ensure no features are availabel and prepare to shutdown
```

Verification Criteria：

```
Vehicle equiped with CAN
```

Verification Method：

```
Change signal STATUS_BH_BCM1.PowerModeSts to "Logistic_Mode_On"

HU shall shutdown and no functionalities available
```

### 判讀（人工）

**判定：部分涵蓋**

狀態名稱涵蓋（同上）。被引用錨點之區辨條件為「Ignition Pre Off, Ignition Off」＋「Logistic Mode active **AND network off**」。**§1.6.2.1.10 與 §1.6.2.1.11 之唯一差異即 network active / off**，而 `SWE-PM-008` Description 不含 `network` 一詞，故無法據以區分此二章。

### 本章全文（不截斷，566 字元）

```
4941434: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, RRM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
4941435: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, RRM, ETM, FPDM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network off.
```

---

## §1.6.2.1.14 — TLM modules and functionalities depending on operative state　`{4941451}`

### 該章之全部需求錨點（8 個）

| 錨點 id | 是否被引用 | 引用之 leaf | 內文首 120 字元 |
|---|---|---|---|
| `4941452` | 否 | — | TLM modules details depending on TLM internal status are described: |
| `4941453` | **是** | `SWE-PM-001`, `SWE-PM-002`, `SWE-PM-003`, `SWE-PM-004`, `SWE-PM-005`, `SWE-PM-006`, `SWE-PM-007`, `SWE-PM-008`, `SWE-PM-009` | TLM Internal State / Source / Audio Power amplifier / Display / Illumination / BoosterOUT / Antenna / Analog tuner / Ant |
| `4941454` | 否 | — | (*): with exception of:- Front_Panel_OnOff.Req icon (i.e. TLM Power button);- Splash Screen visualization;- HMI Antithef |
| `4941455` | 否 | — | (*): with exception of:- Splash Screen visualization;- HMI Antitheft Screens (if Antitheft feature is present: see {VF21 |
| `4941456` | 否 | — | - rear view camera images |
| `4941457` | 否 | — | (**): with exception of - HMI Antitheft Screens (if Antitheft feature is present: see {VF210}) |
| `4941458` | 否 | — | - rear view camera images (see the description of TLM transition from Standby/Sleep due to an Ignition On event in par.  |
| `4941459` | 否 | — | (***): with exception of Advanced Driving Assistance System requests (if available and integrated with TLM in the vehicl |

**被引用之錨點**（1）：`4941453`

**未被引用之錨點**（7）：`4941452`, `4941454`, `4941455`, `4941456`, `4941457`, `4941458`, `4941459`

### 被引用錨點之全文（判讀單位，R-P38）

#### `4941453`　引用者：`SWE-PM-001`, `SWE-PM-002`, `SWE-PM-003`, `SWE-PM-004`, `SWE-PM-005`, `SWE-PM-006`, `SWE-PM-007`, `SWE-PM-008`, `SWE-PM-009`

metadata：`4941453: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]`

```
TLM Internal State
Source
Audio Power amplifier
Display / Illumination
BoosterOUT
Antenna / Analog tuner
Antenna / Digital tuner
MCU (USB)
MCU (AUX)
Full-Operation
TLM plays the audio active source (Tuner, USB, AUX_IN, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Full-Operation
TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music streaming or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Idle
OFF (None)
ON (Muted) (***)
OFF (*) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Partial Operation
OFF (None)
OFF
OFF(**) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
OFF
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Timed
TLM plays the audio active source (Tuner, USB, AUX_IN, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Timed
TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music streaming or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Standby
OFF (None)
OFF
OFF (**) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
OFF
OFF Refer to {CFTS024} for further details about Antenna power supply
OFF Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Sleep
OFF (None)
OFF
OFF (**) DCSD powered off, screen off, no backlight
OFF
OFF Refer to {CFTS024} for further details about Antenna power supply
OFF Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Bench
LTM plays the audio active source (Tuner, USB, AUX_IN or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Logistic Idle
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Logistic Standby
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Logistic Sleep
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Init
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
```

### 引用本章之 leaf 之 Requirement Description（全文）

#### `SWE-PM-001` — Full-Operation

```
* HW supplier shall notify 'Full-Operation' power state through custom power interface
* MD power service shall apply power policy corresponding to full operation to enable all features. Ensure
 - Display is on
 - Audio un-muted
 - BT on
 - Tuner on
 - USB on
 - AUX on
* All applications and services shall subscribe to power state and policy change notification and take necessary action to enable features
```

Verification Criteria：

```
Vehicle equiped with CAN
HU in Sleep state
```

Verification Method：

```
Change Ingition from Off to other value

HU shall boot and show HMI screen

Select Audio source and audio shall be heard

Shall be able to pair smartphone and use AACP features
```

#### `SWE-PM-002` — Idle

```
* HW supplier shall notify 'Idle' power state through custom power interface
* MD power service shall apply power policy corresponding to Idle. Ensure
 - Display is off
 - audio is muted except for ADAS related chimes
 - Bluetooth is on
 - Tuner is on
 - USB is off
 - AUX is off
* All applications and services shall subscribe to power state and policy change notification and take necessary action to enable / disable feature.
*  Disable features which require to display on HMI
* Display shall be turned on to show Rear Camera image, Antitheft HMI
* Ensure audio is muted for all the sources
* Phone call features are active through BT / AACP to recieve calls
```

Verification Criteria：

```
Vehicle equiped with CAN
HU in Full-Operation
```

Verification Method：

```
Pres front panel on-off button / ICS Power button.

Display shall show blank screen, audio shall be muted except for ADAS chimes.

Shall allow phone call and activate Siri through SWC
```

#### `SWE-PM-003` — Partial Operation

```
* HW supplier shall notify 'Partial Operation' power state through custom power interface
* MD power service shall apply power policy corresponding to Partial Operation. Ensure
 - Display is off except to show Antitheft screen
 - audio shall be muted except for ADAS related chimes
 - Bluetooth is off
 - Tuner is on
 - USB is off
 - AUX is off
* All applications and services shall subscribe to power state and policy change notification and be ready in background once partial operation state is notified.
*  Disable features which require to display on HMI
* Ensure audio is muted for all the sources
```

Verification Criteria：

```
Vehicle equiped with CAN
HU in Sleep state
```

Verification Method：

```
Change STATUS_BH_BCM2.RemStActvSts to "Remote Start Active"

Observe $Telematic_Power$ = "Partial_Operation"
```

#### `SWE-PM-004` — Timed

```
* HW supplier shall notify 'Timed' power state through custom power interface
* MD power service shall apply power policy corresponding to Timed power state. Ensure
 - Display is on
 - Audio un-muted
 - BT on
 - Tuner on
 - USB on
 - AUX on
* All applications and services shall subscribe to power state and policy change notification and take necessary action to enable / disable features
* User settings option shall be disable in Timed power state
```

Verification Criteria：

```
Vehicle equiped with CAN

HU in Full-Operation state
```

Verification Method：

```
Change SWITCH_OFF_DOOR setting to OFF

Change SwitchOff_Timeout_Setting.Req to non-zero

Change ignition state to Off

Observe HU enters into Timed power state, HMI and audio function normal

User setting are not modifiable
```

#### `SWE-PM-005` — Standby

```
* HW supplier shall notify 'Standby' power state through custom power interface
* MD power service shall apply power policy corresponding to Standby power state. Ensure
 - Display is Off, except to show splash
 - Audio muted
 - BT Off
 - Tuner Off
 - USB Off
 - AUX Off
* All applications and services shall subscribe to power state and policy change notification and take necessary action to enable / disable features
```

Verification Criteria：

```
Vehicle equiped with CAN

HU in Sleep state
```

Verification Method：

```
Open the door and close the door

Observe Splash on screen

Observe $Telematic_Power$ = "Standby"
```

#### `SWE-PM-006` — Sleep

```
* HW supplier shall notify 'Sleep' power  state through custom power interface
* MD power service shall apply power policy corresponding to Standby power state. Ensure
 - Display is Off, except to show splash
 - Audio muted
 - BT Off
 - Tuner Off
 - USB Off
 - AUX Off
* Transiting to sleep state, all apps and service prepare to shutdown (or STR)
```

Verification Criteria：

```
Vehicle equiped with CAN

HU in Sleep state
```

Verification Method：

```
Observe HU screen turned off and CAN NW activity will be turned OFF
```

#### `SWE-PM-007` — Bench

```
* HW supplier shall notify 'Bench' state through custom power interface
* subcomponents shall ensure all features are available for development / testing
```

Verification Criteria：

```
Vehicle not equiped with CAN or engineering line is active
```

Verification Method：

```
Change ignition state from Off to On

HU shall boot till HMI and all features are available
```

#### `SWE-PM-008` — Logistic Mode

```
* HW supplier shall notify Logistic state (Logistic Idle/ Logistic Standby / Lgistic Sleep) though custom power state interface
* subcomponents shall ensure no features are availabel and prepare to shutdown
```

Verification Criteria：

```
Vehicle equiped with CAN
```

Verification Method：

```
Change signal STATUS_BH_BCM1.PowerModeSts to "Logistic_Mode_On"

HU shall shutdown and no functionalities available
```

#### `SWE-PM-009` — Init state

```
* HW supplier shall notify Init power state though custom power state interface
* subcomponents shall stop activities upon receiving Init power state, until exiting this state
* Settings service shall restore settings to before init state values after exiting init state
```

Verification Criteria：

```
Vehicle equiped with CAN

HU in full operation state
```

Verification Method：

```
Perform voltag spike / drop EMC test as per CS.00244 and observe the behavior
```

### 判讀（人工）

**判定：部分涵蓋**

**八個錨點中僅 `4941453` 被引用**（九條 leaf 共同引用），其餘七個（`4941452`、`4941454`–`4941459`）未被任何 leaf 引用，不在判讀範圍內。`4941453` 之內容為該章之 TLM 狀態 × 模組對照表。`SWE-PM-001`–`009` 之 Description 逐條列舉各狀態下之模組狀態（`Display is on` / `Audio un-muted` / `BT on` / `Tuner on` / `USB on` / `AUX on`），與表中 Source／Audio Power amplifier／Display／tuner／USB／AUX 各欄可對應。但 **BoosterOUT**、**Antenna 之 Analog / Digital 分列**，以及 `Display / Illumination` 欄所引之「as defined in CFTS020 and VF668」與 DCSD touch coordinate 行為，在九條 Description 中皆無對應文字。

### 本章全文（不截斷，6450 字元）

```
4941452: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, DCSD, ETM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
TLM modules details depending on TLM internal status are described:
4941453: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]
TLM Internal State
Source
Audio Power amplifier
Display / Illumination
BoosterOUT
Antenna / Analog tuner
Antenna / Digital tuner
MCU (USB)
MCU (AUX)
Full-Operation
TLM plays the audio active source (Tuner, USB, AUX_IN, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Full-Operation
TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music streaming or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Idle
OFF (None)
ON (Muted) (***)
OFF (*) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Partial Operation
OFF (None)
OFF
OFF(**) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
OFF
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Timed
TLM plays the audio active source (Tuner, USB, AUX_IN, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Timed
TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music streaming or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Standby
OFF (None)
OFF
OFF (**) DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
OFF
OFF Refer to {CFTS024} for further details about Antenna power supply
OFF Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Sleep
OFF (None)
OFF
OFF (**) DCSD powered off, screen off, no backlight
OFF
OFF Refer to {CFTS024} for further details about Antenna power supply
OFF Refer to {VF654} for further details about Antenna power supply
OFF
OFF
Bench
LTM plays the audio active source (Tuner, USB, AUX_IN or Phone Call, etc)
ON (Not muted)
ON DCSD follows behavior related to intensity and display status as defined in CFTS020 and VF668 DCSD sends touch coordinates
ON
ON Refer to {CFTS024} for further details about Antenna power supply
ON Refer to {VF654} for further details about Antenna power supply
ON (if present) Refer to {VF652} for further details about USB presence
ON (if present) Refer to {VF652} for further details about AUX_IN presence
Logistic Idle
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Logistic Standby
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Logistic Sleep
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
Init
OFF (None)
OFF
OFF DCSD powered off, screen off, no backlight
OFF
OFF
OFF
OFF
OFF
4941454: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, DCSD, LTM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
(*): with exception of:- Front_Panel_OnOff.Req icon (i.e. TLM Power button);- Splash Screen visualization;- HMI Antitheft Screens (if Antitheft feature is present: see {VF210}).
4941455: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, RRM, DCSD, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
(*): with exception of:- Splash Screen visualization;- HMI Antitheft Screens (if Antitheft feature is present: see {VF210}).
4941456: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, LTM, DCSD, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
- rear view camera images
4941457: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:DCSD, ETM, LTM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
(**): with exception of - HMI Antitheft Screens (if Antitheft feature is present: see {VF210})
4941458: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:DCSD, ETM, RRM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
- rear view camera images (see the description of TLM transition from Standby/Sleep due to an Ignition On event in par. "TLM_Status.Info and $Telematic_Power$")
4941459: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, LTM, RRM, DCSD] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
(***): with exception of Advanced Driving Assistance System requests (if available and integrated with TLM in the vehicle)
```

---

## §1.6.2.1.15.1 — ICS Wakeup Reasons by POWER Button Pressed　`{4941660}`

### 該章之全部需求錨點（3 個）

| 錨點 id | 是否被引用 | 引用之 leaf | 內文首 120 字元 |
|---|---|---|---|
| `4941661` | 否 | — | Wakeup by ICS Power Button Pressed:  While vehicle is asleep (or awake with ignition in off state), pressing Power butto |
| `4941662` | 否 | — | In “Timed Mode” the following features shall be disabled: Customer setting screens (already included in VF665), HVAC scr |
| `4941663` | **是** | `SWE-PM-004` | In “Timed Mode” the Customer setting screens shall be disabled. |

**被引用之錨點**（1）：`4941663`

**未被引用之錨點**（2）：`4941661`, `4941662`

### 被引用錨點之全文（判讀單位，R-P38）

#### `4941663`　引用者：`SWE-PM-004`

metadata：`4941663: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM] [Market:All] [Model Year:2017] [Radio:R1L-R, R1L] [EE Architecture:Atlantis High, Atlantis Mid]`

```
In “Timed Mode” the Customer setting screens shall be disabled.
```

### 引用本章之 leaf 之 Requirement Description（全文）

#### `SWE-PM-004` — Timed

```
* HW supplier shall notify 'Timed' power state through custom power interface
* MD power service shall apply power policy corresponding to Timed power state. Ensure
 - Display is on
 - Audio un-muted
 - BT on
 - Tuner on
 - USB on
 - AUX on
* All applications and services shall subscribe to power state and policy change notification and take necessary action to enable / disable features
* User settings option shall be disable in Timed power state
```

Verification Criteria：

```
Vehicle equiped with CAN

HU in Full-Operation state
```

Verification Method：

```
Change SWITCH_OFF_DOOR setting to OFF

Change SwitchOff_Timeout_Setting.Req to non-zero

Change ignition state to Off

Observe HU enters into Timed power state, HMI and audio function normal

User setting are not modifiable
```

### 判讀（人工）

**判定：涵蓋**

**判讀單位訂正後結論改變。** 本章三個錨點中**僅 `4941663` 被引用**（`SWE-PM-004`）；`4941661`、`4941662` 未被任何 leaf 引用。`4941663` 之內文全文為「In “Timed Mode” the Customer setting screens shall be disabled.」，其 `Radio` 欄為 `R1L-R, R1L`（本專案車型專屬）。`SWE-PM-004`（Timed）Description 末句「User settings option shall be disable in Timed power state」與之**逐句對應**。v1 以「章 vs leaf」比對時，據未被引用之 `4941661`（ICS POWER 按鍵 wakeup 路徑、CAN 喚醒、`CLIMATIC_PANEL.Radio_Btn0`、250 ms、`ActiveLoadSlave`）與 `4941662` 判為「部分涵蓋」——**該二錨點不在本 feature 範圍內**，其未涵蓋不構成 coverage hole。此為 R-P38 訂正單位後之實質差異。

### 本章全文（不截斷，1748 字元）

```
4941661: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ICS, LTM, RRM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
Wakeup by ICS Power Button Pressed:  While vehicle is asleep (or awake with ignition in off state), pressing Power button on ICS shall cause the radio to turn on and enter “Timed Mode”.  When Power button is pressed on ICS, the ICS shall wake CAN and send signal CLIMATIC_PANEL.Radio_Btn0= pressed  for 250 ms after CAN wake and radio shell keep bus active in “Timed Mode” until one of the exit conditions of  “Timed Mode” becomes true as defined in this CFTS. when ICS wakes up the CAN Bus, ICS shall set its network management message with SystemStatus signal  set to Wake_up. The Radio shall keep CAN Bus active and shall set ActiveLoadSlave =true per CAN standards
4941662: [Artifact Type:Subsystem Functional Requirement] [State:New] [ECU:ICS, RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:VP465, VP384, VP365, VP2R84, R1H, VP4R7, R1M, VP1, VP4R84, VP2R5, VP2, CTS1_2, VP5R120, VP2.5, High, VP1.5, VP0, VP2R7, VP3, VP484, VP4] [EE Architecture:Atlantis Mid, Atlantis High]
In “Timed Mode” the following features shall be disabled: Customer setting screens (already included in VF665), HVAC screens (grey out HVAC main menu softkey), Manual 911 call (Mirror is not powered for NAFTA with key off).In “Timed Mode” the HU shall desabled all HVAC functionalities (all HVAC  HMI should be grayed out).
4941663: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM] [Market:All] [Model Year:2017] [Radio:R1L-R, R1L] [EE Architecture:Atlantis High, Atlantis Mid]
In “Timed Mode” the Customer setting screens shall be disabled.
```

---

## §1.6.3.1.1 — SwitchOff_Timeout_Setting.Req management　`{4941705}`

### 該章之全部需求錨點（3 個）

| 錨點 id | 是否被引用 | 引用之 leaf | 內文首 120 字元 |
|---|---|---|---|
| `4941706` | **是** | `SWE-PM-057` | For the case of LTM High Radio not present, the user can select SwitchOff_Timeout_Setting.Req value equal to "00 minutes |
| `4941707` | **是** | `SWE-PM-057` | Timeout1 parameter is equal to the value set by the user through SwitchOff_Timeout_Setting.Req. |
| `4941708` | **是** | `SWE-PM-057` | So, user can set SwitchOff_Timeout_Setting.Req to "00 minutes" OR to "20 minutes" IF PROXI parameter "Switch_Off_Time" i |

**被引用之錨點**（3）：`4941706`, `4941707`, `4941708`

**未被引用之錨點**（0）：**無**

### 被引用錨點之全文（判讀單位，R-P38）

#### `4941706`　引用者：`SWE-PM-057`

metadata：`4941706: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]`

```
For the case of LTM High Radio not present, the user can select SwitchOff_Timeout_Setting.Req value equal to "00 minutes" OR equal to the value specified by PROXI parameter "Switch_Off_Time". For case of LTM High Radio present, see Auto_SwitchOn_Setting.Req management section
```

#### `4941707`　引用者：`SWE-PM-057`

metadata：`4941707: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]`

```
Timeout1 parameter is equal to the value set by the user through SwitchOff_Timeout_Setting.Req.
```

#### `4941708`　引用者：`SWE-PM-057`

metadata：`4941708: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, LTM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]`

```
So, user can set SwitchOff_Timeout_Setting.Req to "00 minutes" OR to "20 minutes" IF PROXI parameter "Switch_Off_Time" is equal to "20 minutes".
```

### 引用本章之 leaf 之 Requirement Description（全文）

#### `SWE-PM-057` — Proxi Parameter management

```
The System UI shall read the PROXI parameter Switch_Off_Time using the interface provided by the hardware supplier and shall use the hardware supplier’s interface to set the user-selected value to SwitchOff_Timeout_Setting.Req.

TheSystem UI shall also provide an option for the user to select:

"Case1: System UI provides an option for user to select SwitchOff_Timeout_setting.Req to 00 min or 20 min in TLM menu when Switch_off_Time is pre configured in vehicle to 20 min using proxi configuration

Case2: System UI provides an option for user to select SwitchOff_Timeout_setting.Req to 00 min or 60 min in TLM menu when Switch_off_Time is pre configured in vehicle to 60 min using proxi configuration

Case3: System UI provides an option for user to select SwitchOff_Timeout_setting.Req to 00 min or 180 min in TLM menu when Switch_off_Time is pre configured in vehicle to 180 min using proxi configuration

Hw supplier provides interface to read proxi value which is already set in Switch_off_time parameter and it also provides to set the Switchoff_timeout_setting.Req

The System UI reads PROXI parameter Switch_off_time through the interface provided by hardware supplier

The System UI can set the user selected value to Switchoff_timeout_setting.Req"
```

Verification Criteria：

```
"Switch_Off_Time" parameter  is set  to "20 or 60 or 180 minutes" in PROXI
```

Verification Method：

```
Case1: User shall be able to select 00 min or 20 min
When HU shall stay in Timed mode for 20 min if User selects 20 min

Case2: User shall be able to select 00 min or 60 min
When HU shall stay in Timed mode for 60 min if User selects 60 min

Case3: User shall be able to select 00 min or 180 min
When HU shall stay in Timed mode for 180 min if User selects 180 min
```

### 判讀（人工）

**判定：涵蓋（一分支例外）**

`SWE-PM-057` Description 與被引用錨點 `4941708`（「user can set SwitchOff_Timeout_Setting.Req to "00 minutes" OR to "20 minutes" IF PROXI parameter "Switch_Off_Time" is equal to "20 minutes"」）逐句對應；其 Case1/2/3 亦對應 `4941707` 之 Timeout1 設定。**例外**：`4941706` 之分支「For case of LTM High Radio present, see Auto_SwitchOn_Setting.Req management section」指向另一章節，Description 無對應。

### 本章全文（不截斷，1040 字元）

```
4941706: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]
For the case of LTM High Radio not present, the user can select SwitchOff_Timeout_Setting.Req value equal to "00 minutes" OR equal to the value specified by PROXI parameter "Switch_Off_Time". For case of LTM High Radio present, see Auto_SwitchOn_Setting.Req management section
4941707: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]
Timeout1 parameter is equal to the value set by the user through SwitchOff_Timeout_Setting.Req.
4941708: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, LTM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]
So, user can set SwitchOff_Timeout_Setting.Req to "00 minutes" OR to "20 minutes" IF PROXI parameter "Switch_Off_Time" is equal to "20 minutes".
```

---

## §1.8.1.1.1 — ID 1 Description　`{4941812}`

### 該章之全部需求錨點（5 個）

| 錨點 id | 是否被引用 | 引用之 leaf | 內文首 120 字元 |
|---|---|---|---|
| `4941813` | 否 | — | The value of the  Switch_Off_Time out parameter is defined by PROXI in TLM node |
| `4941814` | **是** | `SWE-PM-057` | IF "Switch_Off_Time" parameter  is set  to "20 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 m |
| `4941815` | **是** | `SWE-PM-057` | IF "Switch_Off_Time" parameter  is set  to "60 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 m |
| `4941816` | 否 | — | （無內文） |
| `4941817` | **是** | `SWE-PM-057` | IF "Switch_Off_Time" parameter  is set  to "180 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00  |

**被引用之錨點**（3）：`4941814`, `4941815`, `4941817`

**未被引用之錨點**（2）：`4941813`, `4941816`

### 被引用錨點之全文（判讀單位，R-P38）

#### `4941814`　引用者：`SWE-PM-057`

metadata：`4941814: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, RRM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]`

```
IF "Switch_Off_Time" parameter  is set  to "20 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "20 min" in TLM menu; so Timeout1 is equal to "00 min" OR "20 minutes" respectively.
```

#### `4941815`　引用者：`SWE-PM-057`

metadata：`4941815: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]`

```
IF "Switch_Off_Time" parameter  is set  to "60 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "60 min" in TLM menu; so Timeout1 is equal to "00 min" OR "60 minutes" respectively.
```

#### `4941817`　引用者：`SWE-PM-057`

metadata：`4941817: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, RRM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]`

```
IF "Switch_Off_Time" parameter  is set  to "180 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "180 min" in TLM menu; so Timeout1 is equal to "00 min" OR "180 minutes" respectively.
```

### 引用本章之 leaf 之 Requirement Description（全文）

#### `SWE-PM-057` — Proxi Parameter management

```
The System UI shall read the PROXI parameter Switch_Off_Time using the interface provided by the hardware supplier and shall use the hardware supplier’s interface to set the user-selected value to SwitchOff_Timeout_Setting.Req.

TheSystem UI shall also provide an option for the user to select:

"Case1: System UI provides an option for user to select SwitchOff_Timeout_setting.Req to 00 min or 20 min in TLM menu when Switch_off_Time is pre configured in vehicle to 20 min using proxi configuration

Case2: System UI provides an option for user to select SwitchOff_Timeout_setting.Req to 00 min or 60 min in TLM menu when Switch_off_Time is pre configured in vehicle to 60 min using proxi configuration

Case3: System UI provides an option for user to select SwitchOff_Timeout_setting.Req to 00 min or 180 min in TLM menu when Switch_off_Time is pre configured in vehicle to 180 min using proxi configuration

Hw supplier provides interface to read proxi value which is already set in Switch_off_time parameter and it also provides to set the Switchoff_timeout_setting.Req

The System UI reads PROXI parameter Switch_off_time through the interface provided by hardware supplier

The System UI can set the user selected value to Switchoff_timeout_setting.Req"
```

Verification Criteria：

```
"Switch_Off_Time" parameter  is set  to "20 or 60 or 180 minutes" in PROXI
```

Verification Method：

```
Case1: User shall be able to select 00 min or 20 min
When HU shall stay in Timed mode for 20 min if User selects 20 min

Case2: User shall be able to select 00 min or 60 min
When HU shall stay in Timed mode for 60 min if User selects 60 min

Case3: User shall be able to select 00 min or 180 min
When HU shall stay in Timed mode for 180 min if User selects 180 min
```

### 判讀（人工）

**判定：涵蓋**

五個錨點中 `4941814` / `4941815` / `4941817` 被引用（皆 `SWE-PM-057`）；`4941813`（`Switch_Off_Time` 由 PROXI 於 TLM node 定義）與 `4941816` 未被引用。被引用者逐條為 `Switch_Off_Time` = 20 / 60 / 180 分鐘時之 `SwitchOff_Timeout_Setting.Req` 可選值。`SWE-PM-057` 之 Verification Method 逐字列出 Case1（00 或 20 min）、Case2（00 或 60 min）、Case3（00 或 180 min），Verification Criteria 為「"Switch_Off_Time" parameter is set to "20 or 60 or 180 minutes" in PROXI」。三個 case 完全對應。

### 本章全文（不截斷，1490 字元）

```
4941813: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, ETM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]
The value of the  Switch_Off_Time out parameter is defined by PROXI in TLM node
4941814: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, RRM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]
IF "Switch_Off_Time" parameter  is set  to "20 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "20 min" in TLM menu; so Timeout1 is equal to "00 min" OR "20 minutes" respectively.
4941815: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]
IF "Switch_Off_Time" parameter  is set  to "60 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "60 min" in TLM menu; so Timeout1 is equal to "00 min" OR "60 minutes" respectively.
4941816: [Artifact Type:Description] [State:New] [Model Year:2017]
4941817: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, RRM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]
IF "Switch_Off_Time" parameter  is set  to "180 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "180 min" in TLM menu; so Timeout1 is equal to "00 min" OR "180 minutes" respectively.
```
