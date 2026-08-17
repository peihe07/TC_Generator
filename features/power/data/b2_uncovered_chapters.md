# B2 (v1，已由 v2 取代) — A-PW16 之 9 章判定素材（R-P27）

> **已由 `b2_v2_uncovered_chapters.md` 取代（R-P38）。**
> 本檔以「章 vs leaf」比對，判讀單位有誤；保留為紀錄，不刪。
> v2 之單位為「被引用之錨點 vs leaf」，並改變了 §1.6.2.1.15.1 之判定（部分涵蓋 → 涵蓋）。

> 依 R-P27 與 04 §I：本檔**不建議任何處置**。逐章僅陳述
> 「涵蓋 / 部分涵蓋 / 未涵蓋 / 無法判定」與其逐字依據。

> 這 9 章為 03 包 G14 所查出「被丟棄之次章節中未被任何 leaf 主章節覆蓋」者。
> 依 **R-P24**，Layer 3 已改為記全集，故此 9 章**在 Layer 3 中已被記錄**
> （見 `data/layer3_full.tsv`）。本檔所判定者為另一問題：
> **其行為是否已被所屬 leaf 之 Requirement Description 涵蓋** —— 即 R-P27 所問之
> 「是否為真實 coverage hole」。

## 判定總表

| 章節 | 標題 | 所屬 leaf | 判定 |
|---|---|---|---|
| §1.6.2.1 | TLM algorithm requirements | SWE-PM-001 ~ 009（9 條） | **無法判定** |
| §1.6.2.1.4 | Stolen Vehicle Mode | SWE-PM-003 | **未涵蓋** |
| §1.6.2.1.9 | Logistic Idle | SWE-PM-008 | **部分涵蓋** |
| §1.6.2.1.10 | Logistic Standby | SWE-PM-008 | **部分涵蓋** |
| §1.6.2.1.11 | Logistic Sleep | SWE-PM-008 | **部分涵蓋** |
| §1.6.2.1.14 | TLM modules and functionalities depending on operative state | SWE-PM-001 ~ 009（9 條） | **部分涵蓋** |
| §1.6.2.1.15.1 | ICS Wakeup Reasons by POWER Button Pressed | SWE-PM-004 | **部分涵蓋** |
| §1.6.3.1.1 | SwitchOff_Timeout_Setting.Req management | SWE-PM-057 | **涵蓋（有一分支例外）** |
| §1.8.1.1.1 | ID 1 Description | SWE-PM-057 | **涵蓋** |

## 所屬 leaf 之 Requirement Description（全文）

### `SWE-PM-003` — Partial Operation

**Description**：

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

**Verification Criteria**：

```
Vehicle equiped with CAN
HU in Sleep state
```

**Verification Method**：

```
Change STATUS_BH_BCM2.RemStActvSts to "Remote Start Active"

Observe $Telematic_Power$ = "Partial_Operation"
```

### `SWE-PM-004` — Timed

**Description**：

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

**Verification Criteria**：

```
Vehicle equiped with CAN

HU in Full-Operation state
```

**Verification Method**：

```
Change SWITCH_OFF_DOOR setting to OFF

Change SwitchOff_Timeout_Setting.Req to non-zero

Change ignition state to Off

Observe HU enters into Timed power state, HMI and audio function normal

User setting are not modifiable
```

### `SWE-PM-008` — Logistic Mode

**Description**：

```
* HW supplier shall notify Logistic state (Logistic Idle/ Logistic Standby / Lgistic Sleep) though custom power state interface
* subcomponents shall ensure no features are availabel and prepare to shutdown
```

**Verification Criteria**：

```
Vehicle equiped with CAN
```

**Verification Method**：

```
Change signal STATUS_BH_BCM1.PowerModeSts to "Logistic_Mode_On"

HU shall shutdown and no functionalities available
```

### `SWE-PM-057` — Proxi Parameter management

**Description**：

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

**Verification Criteria**：

```
"Switch_Off_Time" parameter  is set  to "20 or 60 or 180 minutes" in PROXI
```

**Verification Method**：

```
Case1: User shall be able to select 00 min or 20 min
When HU shall stay in Timed mode for 20 min if User selects 20 min

Case2: User shall be able to select 00 min or 60 min
When HU shall stay in Timed mode for 60 min if User selects 60 min

Case3: User shall be able to select 00 min or 180 min
When HU shall stay in Timed mode for 180 min if User selects 180 min
```

> `SWE-PM-001`、`002`、`005`、`006`、`007`、`009` 之 Description 見
> `data/multi_chapter_leaves.md`（03 包 B1，各 300 字元）與 037 原檔。

---

## 逐章判讀

### §1.6.2.1 — TLM algorithm requirements　`{4941353}`

**所屬 leaf**：SWE-PM-001 ~ 009（9 條）　**判定：無法判定**

**逐字依據**：

本章文字層僅含兩個 inline RTF 之 WrapperResource 參照（`CFTSMV009_CIP_R4_O829_4_inline.rtf`、`…O1584_5_inline.rtf`），無任何可判讀之行為敘述。其實質內容為嵌入物件，不在文字層內。

**本章全文**（不截斷，633 字元）：

```
4941354: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:R1H, VP2R84, VP3, R1L-R, VP2R7, VP2, VP1, VP465, VP5R120, High, VP0, VP2R5, VP4R7, VP484, VP384, CTS1_2, VP365, VP2.5, VP4, R1M, VP4R84, VP1.5, R1L] [EE Architecture:Atlantis High, Atlantis Mid]
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
4941355: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM, RRM] [Market:All] [Radio:R1L-R, VP2R7, R1L, VP2R5, VP2R84] [EE Architecture:Atlantis High, Atlantis Mid]
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### §1.6.2.1.4 — Stolen Vehicle Mode　`{4941398}`

**所屬 leaf**：SWE-PM-003　**判定：未涵蓋**

**逐字依據**：

`SWE-PM-003`（Partial Operation）之 Description 全文無 stolen vehicle、SMS、GPS location、7 day timer 之任何敘述；僅出現 `Display is off except to show Antitheft screen`，與本章之進入／退出條件無對應。

**惟須並陳兩項決定性事實**：

（一）本章有兩個需求錨點，而 `SWE-PM-003` 經 `Sys-RA-PM-0031` **只引用 `4941400` 一個**
（見 `data/layer3_full.tsv` 該列 `hit_count=1`、`item_ids=4941400`）。
`4941399`（描述進入條件者）**未被任何 leaf 引用**。

（二）`4941400` 逐字為「the R1 HU shall not enter stolen vehicle mode under any condition」，
其 `Radio` 欄為 `R1L, R1H, R1M, R1L-R`（含本專案車型 **R1L**），`Model Year` 2021–2025。
而 `4941399` 之 `Radio` 欄為 `VP4R7, VP4R84`，**不含 R1L**。

故本章對本專案而言，其唯一在範圍內之需求是一條**否定需求**（不得進入該模式），
而非「Stolen Vehicle Mode 功能」本身。A-PW16 將本章列為未覆蓋章節之描述
（「實質功能章節」）在此一點上需要修正 —— 未被涵蓋者是那條否定需求，
不是一整個防盜功能。此為事實陳述，非處置建議。

**本章全文**（不截斷，867 字元）：

```
4941399: [Artifact Type:Subsystem Functional Requirement] [State:New] [ECU:ETM] [Market:All] [Model Year:2017] [Radio:VP4R7, VP4R84] [EE Architecture:Atlantis Mid, Atlantis High]
When the HU receives the High priority Stolen Vehicle SMS, it shall enter stolen vehicle mode. The HU shall keep powered only the components needed to send the GPS location and maintain a 7 day timer. The HU shall remain in this state until it receives the SMS indicating the Stolen Vehicle has been recovered, 7 days has passed, or until the Battery drains and the HU can no longer remain powered.
4941400: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM] [Market:All] [Model Year:2022, 2021, 2024, 2023, 2025] [Radio:R1L, R1H, R1M, R1L-R] [EE Architecture:Atlantis High, Atlantis Mid]
the R1 HU shall not enter stolen vehicle mode under any condition
```

### §1.6.2.1.9 — Logistic Idle　`{4941425}`

**所屬 leaf**：SWE-PM-008　**判定：部分涵蓋**

**逐字依據**：

`SWE-PM-008` 之 Description 逐字列出三個狀態名：「HW supplier shall notify Logistic state (Logistic Idle/ Logistic Standby / Lgistic Sleep)」—— **狀態名稱涵蓋**。

但本章之區辨條件「In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On」與「Audio and Telematic modules shall be in this mode when they receive `$Telematic_Power$` = [Logistic_On]」，在 Description 中**無任何對應文字**。

**本章全文**（不截斷，1223 字元）：

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

### §1.6.2.1.10 — Logistic Standby　`{4941430}`

**所屬 leaf**：SWE-PM-008　**判定：部分涵蓋**

**逐字依據**：

狀態名稱涵蓋（同上）。區辨條件「Ignition Pre Off, Ignition Off」＋「Logistic Mode active **AND network active**」在 Description 中無對應。Description 僅有「subcomponents shall ensure no features are availabel and prepare to shutdown」，未區分 network active/off。

**本章全文**（不截斷，565 字元）：

```
4941431: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, ETM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
4941432: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network active
```

### §1.6.2.1.11 — Logistic Sleep　`{4941433}`

**所屬 leaf**：SWE-PM-008　**判定：部分涵蓋**

**逐字依據**：

狀態名稱涵蓋（同上）。區辨條件「Ignition Pre Off, Ignition Off」＋「Logistic Mode active **AND network off**」在 Description 中無對應。

**§1.6.2.1.10 與 §1.6.2.1.11 之唯一差異即 network active / network off**；`SWE-PM-008` 之 Description 不含 network 一詞，故無法據以區分此二章。

**本章全文**（不截斷，569 字元）：

```
4941434: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, RRM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
4941435: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, RRM, ETM, FPDM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network off.
```

### §1.6.2.1.14 — TLM modules and functionalities depending on operative state　`{4941451}`

**所屬 leaf**：SWE-PM-001 ~ 009（9 條）　**判定：部分涵蓋**

**逐字依據**：

本章為一張「TLM Internal State × 模組」對照表，欄位含 Source／Audio Power amplifier／Display / Illumination／BoosterOUT／Antenna / Analog tuner／Antenna / Digital tuner／MCU (USB)／MCU (AUX)。

`SWE-PM-001`–`009` 之 Description 確實逐條列舉各狀態下之模組狀態（`Display is on`／`Audio un-muted`／`BT on`／`Tuner on`／`USB on`／`AUX on` 等），**與 Source／Audio／Display／tuner／USB／AUX 六欄可對應**。

但 **BoosterOUT** 與 **Antenna 之 Analog / Digital 分列**，以及 `Display / Illumination` 欄所引之「as defined in CFTS020 and VF668」與 DCSD touch coordinate 行為，在九條 Description 中皆無對應文字。

**本章全文**（不截斷，6590 字元）：

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

### §1.6.2.1.15.1 — ICS Wakeup Reasons by POWER Button Pressed　`{4941660}`

**所屬 leaf**：SWE-PM-004　**判定：部分涵蓋**

**逐字依據**：

`SWE-PM-004`（Timed）之 Description 末句「User settings option shall be disable in Timed power state」對應本章 `4941662` 之「In "Timed Mode" the following features shall be disabled: Customer setting screens…」。

但本章之主體 —— **wakeup 觸發路徑** —— 完全未涵蓋：ICS POWER 按鍵、CAN 喚醒、`CLIMATIC_PANEL.Radio_Btn0 = pressed` 維持 250 ms、`SystemStatus = Wake_up`、`ActiveLoadSlave = true`，`SWE-PM-004` Description 無一字提及。

**本章全文**（不截斷，1753 字元）：

```
4941661: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ICS, LTM, RRM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
Wakeup by ICS Power Button Pressed:  While vehicle is asleep (or awake with ignition in off state), pressing Power button on ICS shall cause the radio to turn on and enter “Timed Mode”.  When Power button is pressed on ICS, the ICS shall wake CAN and send signal CLIMATIC_PANEL.Radio_Btn0= pressed  for 250 ms after CAN wake and radio shell keep bus active in “Timed Mode” until one of the exit conditions of  “Timed Mode” becomes true as defined in this CFTS. when ICS wakes up the CAN Bus, ICS shall set its network management message with SystemStatus signal  set to Wake_up. The Radio shall keep CAN Bus active and shall set ActiveLoadSlave =true per CAN standards
4941662: [Artifact Type:Subsystem Functional Requirement] [State:New] [ECU:ICS, RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:VP465, VP384, VP365, VP2R84, R1H, VP4R7, R1M, VP1, VP4R84, VP2R5, VP2, CTS1_2, VP5R120, VP2.5, High, VP1.5, VP0, VP2R7, VP3, VP484, VP4] [EE Architecture:Atlantis Mid, Atlantis High]
In “Timed Mode” the following features shall be disabled: Customer setting screens (already included in VF665), HVAC screens (grey out HVAC main menu softkey), Manual 911 call (Mirror is not powered for NAFTA with key off).In “Timed Mode” the HU shall desabled all HVAC functionalities (all HVAC  HMI should be grayed out).
4941663: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM] [Market:All] [Model Year:2017] [Radio:R1L-R, R1L] [EE Architecture:Atlantis High, Atlantis Mid]
In “Timed Mode” the Customer setting screens shall be disabled.
```

### §1.6.3.1.1 — SwitchOff_Timeout_Setting.Req management　`{4941705}`

**所屬 leaf**：SWE-PM-057　**判定：涵蓋（有一分支例外）**

**逐字依據**：

`SWE-PM-057` 之 Description 與本章 `4941708`（「user can set SwitchOff_Timeout_Setting.Req to "00 minutes" OR to "20 minutes" IF PROXI parameter "Switch_Off_Time" is equal to "20 minutes"」）逐句對應；其 Case1/Case2/Case3 亦對應 `4941707` 之 Timeout1 設定。

**例外**：`4941706` 之分支「For case of LTM High Radio present, see Auto_SwitchOn_Setting.Req management section」在 Description 中無對應 —— 該分支指向另一章節，本 leaf 未涵蓋。

**本章全文**（不截斷，1045 字元）：

```
4941706: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]
For the case of LTM High Radio not present, the user can select SwitchOff_Timeout_Setting.Req value equal to "00 minutes" OR equal to the value specified by PROXI parameter "Switch_Off_Time". For case of LTM High Radio present, see Auto_SwitchOn_Setting.Req management section
4941707: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]
Timeout1 parameter is equal to the value set by the user through SwitchOff_Timeout_Setting.Req.
4941708: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, LTM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid]
So, user can set SwitchOff_Timeout_Setting.Req to "00 minutes" OR to "20 minutes" IF PROXI parameter "Switch_Off_Time" is equal to "20 minutes".
```

### §1.8.1.1.1 — ID 1 Description　`{4941812}`

**所屬 leaf**：SWE-PM-057　**判定：涵蓋**

**逐字依據**：

本章逐條為 `Switch_Off_Time` = 20 / 60 / 180 分鐘時之 `SwitchOff_Timeout_Setting.Req` 可選值。`SWE-PM-057` 之 Verification Method 逐字列出 Case1（00 或 20 min）、Case2（00 或 60 min）、Case3（00 或 180 min），且 Verification Criteria 為「"Switch_Off_Time" parameter is set to "20 or 60 or 180 minutes" in PROXI」。**三個 case 完全對應**。

**本章全文**（不截斷，1498 字元）：

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
