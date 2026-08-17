# B1 — `SWE-PM-008` 之 Test Set 裁定素材（R-P26(c)）

> 依 R-P15(b) 與 04 §I：本檔**不含任何建議歸屬**。
> `SWE-PM-057` 之素材已於 03 上繳包 §七備齊，本檔不重複產出。

## 1. 037 欄位

**Requirement Title**：`Logistic Mode`

> **訂正**：04 下放包 §B1 稱「03 §四實測為空」。實測**不為空**，值為 `Logistic Mode`。
> 03 上繳包 §四之概覽表以「—」代替標題係執行層之簡寫，非實測為空；
> 據此所寫之 03 §九第 4 項為錯誤陳述。全欄空值率見 G19（18 欄皆 0 空值）。

**Requirement Description**（全文）：

```
* HW supplier shall notify Logistic state (Logistic Idle/ Logistic Standby / Lgistic Sleep) though custom power state interface
* subcomponents shall ensure no features are availabel and prepare to shutdown
```

**Verification Criteria**（全文）：

```
Vehicle equiped with CAN
```

**Verification Method**（全文）：

```
Change signal STATUS_BH_BCM1.PowerModeSts to "Logistic_Mode_On"

HU shall shutdown and no functionalities available
```

**Sub Categorization**：`'Service\nHMI'`　**Priority**：`Medium`

## 2. Source Requirement ID —— 完整 token 清單（13 個）

```
Sys-RA-PM-0013
Sys-RA-PM-0014
Sys-RA-PM-0040
Sys-RA-PM-0041
Sys-RA-PM-0042
Sys-RA-PM-0043
Sys-RA-PM-0044
Sys-RA-PM-0045
Sys-RA-PM-0056
Sys-RA-PM-0184
Sys-RA-PM-0185
Sys-RA-PM-0186
Sys-RA-PM-0187
```

## 3. 每個 token → (CFTS, 章節號, 章節標題)

| token | item id | 章節 |
|---|---|---|
| `Sys-RA-PM-0013` | `4941354` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0014` | `4941355` | §1.6.2.1 — TLM algorithm requirements |
| `Sys-RA-PM-0040` | `4941425` | **未解析** |
| `Sys-RA-PM-0041` | `4941426` | §1.6.2.1.9 — Logistic Idle |
| `Sys-RA-PM-0041` | `4941427` | §1.6.2.1.9 — Logistic Idle |
| `Sys-RA-PM-0041` | `4941428` | §1.6.2.1.9 — Logistic Idle |
| `Sys-RA-PM-0042` | `4941430` | **未解析** |
| `Sys-RA-PM-0043` | `4941431` | §1.6.2.1.10 — Logistic Standby |
| `Sys-RA-PM-0043` | `4941432` | §1.6.2.1.10 — Logistic Standby |
| `Sys-RA-PM-0044` | `4941433` | **未解析** |
| `Sys-RA-PM-0045` | `4941434` | §1.6.2.1.11 — Logistic Sleep |
| `Sys-RA-PM-0045` | `4941435` | §1.6.2.1.11 — Logistic Sleep |
| `Sys-RA-PM-0056` | `4941453` | §1.6.2.1.14 — TLM modules and functionalities depending on operative state |
| `Sys-RA-PM-0184` | `4941755` | §1.6.7.1 — TLM algorithm requirements |
| `Sys-RA-PM-0185` | `4941756` | §1.6.7.1 — TLM algorithm requirements |
| `Sys-RA-PM-0186` | `4941757` | §1.6.7.1 — TLM algorithm requirements |
| `Sys-RA-PM-0187` | `4941758` | §1.6.7.1 — TLM algorithm requirements |

## 4. 六個相異章節之標題與內文首段

### §1.6.2.1 — TLM algorithm requirements　`{4941353}`　（命中 2 次）

```
4941354: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:R1H, VP2R84, VP3, R1L-R, VP2R7, VP2, VP1, VP465, VP5R120, High, VP0, VP2R5, VP4R7, VP484, VP384, CTS1_2, VP365, VP2.5, VP4, R1M, VP4R84, VP1.5, R1L] [EE Architecture:Atlantis High, Atlantis Mid]
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
4941355: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM, RRM] [Market:All] [Radio:R1L-R, VP2R7, R1L, VP2R5, VP2R84] [EE Architecture:Atlantis High, Atlantis Mid]
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### §1.6.2.1.9 — Logistic Idle　`{4941425}`　（命中 3 次）

```
4941426: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, RRM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On,
4941427: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, FPDM, LTM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
This status is related to TLM, FPDM AMP, ICS, and DTV OFF with Logistic Mode active.
4941428: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, ETM, AMP, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
TLM and AMP has not to reproduce any audio source and the user can't do any setting.
4941429
```

### §1.6.2.1.10 — Logistic Standby　`{4941430}`　（命中 2 次）

```
4941431: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, ETM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
4941432: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:RRM, LTM, ETM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network active
```

### §1.6.2.1.11 — Logistic Sleep　`{4941433}`　（命中 2 次）

```
4941434: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, RRM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
4941435: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, RRM, ETM, FPDM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network off.
```

### §1.6.2.1.14 — TLM modules and functionalities depending on operative state　`{4941451}`　（命中 1 次）

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
ON Refer to {VF654} fo
```

### §1.6.7.1 — TLM algorithm requirements　`{4941754}`　（命中 4 次）

```
4941755: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, RRM, LTM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis Mid]
When the Logistic Mode is active (signal PowerModeSts_Telematic == "Logistic_Mode_On"), so when TLM_Status.Info is equal to "Logistic Idle" OR "Logistic Standby" OR "Logistic Sleep", TLM has to remain always switched off:
4941756: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:ETM, LTM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis Mid, Atlantis High]
All functions, user settings and also front panel illumination must be disabled.TLM shall reduce its performances.
4941757: [Artifact Type:Subsystem Functional Requirement] [State:Under Review] [ECU:LTM, RRM] [Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:Atlantis High, Atlantis 
```

## 5. 歸屬後果

`SWE-PM-008` 之 Test Set 歸屬為兩選一。其餘四個 Test Set 不受影響。

| 情形 | Power State | Startup Display | Branding and Theme | Timeout Settings | Power Down |
|---|---|---|---|---|---|
| 歸 **Power State** | 63 | 24 | 16 | 7 | 3 |
| 歸 **Timeout Settings** | 62 | 24 | 16 | 8 | 3 |

（上表以 `SWE-PM-057` 歸 Power State 為基準。`SWE-PM-057` 之歸屬另計，
兩條交叉之四種組合見 04 下放包 §E。此處僅陳述本條之邊際效果：
歸 Timeout Settings 使 Power State −1、Timeout Settings +1。）
