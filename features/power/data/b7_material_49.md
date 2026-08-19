# 49 包素材 —— `SWE-PM-001`–`009` 之錨點原文

> 逐字抄錄，未摘要。`4941354` / `4941355` 為 WrapperResource（圖），其判讀依 R-P320 之界線。

## SWE-PM-001

### §1.6.2.1 TLM algorithm requirements（2 個錨點）

**`4941354`**（50 字元）

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**`4941355`**（51 字元）

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### §1.6.2.1.1 Full-Operation（3 個錨點）

**`4941357`**（138 字元）

```
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On,
```

**`4941358`**（33 字元）

```
This status is related to TLM ON.
```

**`4941360`**（51 字元）

```
All TLM, AMP/ICS/DTV functionalities are available.
```

### §1.6.2.1.14 TLM modules and functionalities depending on operative state（1 個錨點）

**`4941453`**（4259 字元）

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

## SWE-PM-002

### §1.6.2.1 TLM algorithm requirements（2 個錨點）

**`4941354`**（50 字元）

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**`4941355`**（51 字元）

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### §1.6.2.1.2 Idle（7 個錨點）

**`4941364`**（138 字元）

```
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On,
```

**`4941365`**（161 字元）

```
This status is related to TLM audio is OFF. TLM shall allow only Splash Screen visualization on its display.  ICS functionalities are available.  DTV shall be OFF.
```

**`4941366`**（53 字元）

```
Rear View Camera images shall be available if needed.
```

**`4941369`**（83 字元）

```
TLM and AMP has not to reproduce any audio source, with exception of the following:
```

**`4941371`**（41 字元）

```
In this state, user cannot do any setting
```

**`4941372`**（115 字元）

```
All TLM functionalities run in background and are ready, but no HMI interaction is enabled, except TLM Power button
```

**`4941373`**（161 字元）

```
All TLM functionalities run in background and are ready, but no HMI interaction is enabled, except TLM Power button or rear camera images activation/deactivation
```

### §1.6.2.1.14 TLM modules and functionalities depending on operative state（1 個錨點）

**`4941453`**（4259 字元）

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

## SWE-PM-003

### §1.6.2.1 TLM algorithm requirements（2 個錨點）

**`4941354`**（50 字元）

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**`4941355`**（51 字元）

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### §1.6.2.1.3 Partial Operation（5 個錨點）

**`4941391`**（168 字元）

```
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On, Ignition Off Ignition Pre-Off
```

**`4941392`**（254 字元）

```
In this mode TLM shall shall report $Telematic_Power$ = " Partial_Operation". This mode shall exist for AMP, ICS, and DTV when STATUS_BH_BCM2.RemStActvSts is equal to "Remote Start Active" is recieved and TLM sends $Telematic_Power$ = "Partial_Operation"
```

**`4941393`**（136 字元）

```
This status is related to TLM OFF. AMP/ICS/DTV shall be OFF. Audio for ANC, ACN, and chimes (if equipped) shall be active in this state)
```

**`4941394`**（185 字元）

```
All TLM, AMP, ICS, and DTV functionalities run in background and are ready but not HMI interaction is enabled within this status, except for the interaction that permit a change status.
```

**`4941396`**（81 字元）

```
See paragraph “TLM_Status.Info and $Telematic_Power$ signal setting” for details.
```

### §1.6.2.1.4 Stolen Vehicle Mode（1 個錨點）

**`4941400`**（65 字元）

```
the R1 HU shall not enter stolen vehicle mode under any condition
```

### §1.6.2.1.14 TLM modules and functionalities depending on operative state（1 個錨點）

**`4941453`**（4259 字元）

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

## SWE-PM-004

### §1.6.2.1 TLM algorithm requirements（2 個錨點）

**`4941354`**（50 字元）

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**`4941355`**（51 字元）

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### §1.6.2.1.5 Timed（5 個錨點）

**`4941402`**（79 字元）

```
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
```

**`4941403`**（33 字元）

```
This status is related to TLM ON.
```

**`4941404`**（66 字元）

```
All TLM AMP/ICS/DTV shall be ON and functionalities are available.
```

**`4941406`**（172 字元）

```
Entering this state, TLM is ON for a limited time. See par. Phone Call management in Timed state for further details and par. Configuration parameters for Timeout1 details.
```

**`4941407`**（70 字元）

```
TLM AMP/ICS/DTV functionalities are available only for a limited time.
```

### §1.6.2.1.14 TLM modules and functionalities depending on operative state（1 個錨點）

**`4941453`**（4259 字元）

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

### §1.6.2.1.15.1 ICS Wakeup Reasons by POWER Button Pressed（1 個錨點）

**`4941663`**（63 字元）

```
In “Timed Mode” the Customer setting screens shall be disabled.
```

## SWE-PM-005

### §1.6.2.1 TLM algorithm requirements（2 個錨點）

**`4941354`**（50 字元）

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**`4941355`**（51 字元）

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### §1.6.2.1.6 Standby（4 個錨點）

**`4941410`**（79 字元）

```
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
```

**`4941411`**（49 字元）

```
This status is related to TLM OFF with Network on
```

**`4941412`**（59 字元）

```
No TLM, FPDM, AMP, ICS, and DTV functionality is available.
```

**`4941413`**（78 字元）

```
Entering this state, TLM has to set Antitheft_Activation.Req to "False" value.
```

### §1.6.2.1.14 TLM modules and functionalities depending on operative state（1 個錨點）

**`4941453`**（4259 字元）

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

## SWE-PM-006

### §1.6.2.1 TLM algorithm requirements（2 個錨點）

**`4941354`**（50 字元）

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**`4941355`**（51 字元）

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### §1.6.2.1.7 Sleep（4 個錨點）

**`4941416`**（79 字元）

```
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
```

**`4941417`**（50 字元）

```
This status is related to TLM OFF with Network off
```

**`4941418`**（58 字元）

```
No TLM, FPDM AMP, ICS, and DTV functionality is available.
```

**`4941419`**（78 字元）

```
Entering this state, TLM has to set Antitheft_Activation.Req to "False" value.
```

### §1.6.2.1.14 TLM modules and functionalities depending on operative state（1 個錨點）

**`4941453`**（4259 字元）

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

## SWE-PM-007

### §1.6.2.1 TLM algorithm requirements（2 個錨點）

**`4941354`**（50 字元）

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**`4941355`**（51 字元）

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### §1.6.2.1.8 Bench（2 個錨點）

**`4941422`**（51 字元）

```
In the "Ignition Working Conditions" "Ignition Off"
```

**`4941423`**（146 字元）

```
This status is related to TLM AMP, ICS, and DTV ON only for testing, diagnostics and development of TLM component, relatively to Engineering Line.
```

### §1.6.2.1.14 TLM modules and functionalities depending on operative state（1 個錨點）

**`4941453`**（4259 字元）

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

## SWE-PM-008

### §1.6.2.1 TLM algorithm requirements（2 個錨點）

**`4941354`**（50 字元）

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**`4941355`**（51 字元）

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### §1.6.2.1.9 Logistic Idle（3 個錨點）

**`4941426`**（138 字元）

```
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On,
```

**`4941427`**（84 字元）

```
This status is related to TLM, FPDM AMP, ICS, and DTV OFF with Logistic Mode active.
```

**`4941428`**（84 字元）

```
TLM and AMP has not to reproduce any audio source and the user can't do any setting.
```

### §1.6.2.1.10 Logistic Standby（2 個錨點）

**`4941431`**（79 字元）

```
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
```

**`4941432`**（103 字元）

```
This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network active
```

### §1.6.2.1.11 Logistic Sleep（2 個錨點）

**`4941434`**（79 字元）

```
In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off,
```

**`4941435`**（101 字元）

```
This status is related to TLM, FPDM, AMP, ICS, and DTV OFF with Logistic Mode active AND network off.
```

### §1.6.2.1.14 TLM modules and functionalities depending on operative state（1 個錨點）

**`4941453`**（4259 字元）

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

### §1.6.7.1 TLM algorithm requirements（4 個錨點）

**`4941755`**（221 字元）

```
When the Logistic Mode is active (signal PowerModeSts_Telematic == "Logistic_Mode_On"), so when TLM_Status.Info is equal to "Logistic Idle" OR "Logistic Standby" OR "Logistic Sleep", TLM has to remain always switched off:
```

**`4941756`**（114 字元）

```
All functions, user settings and also front panel illumination must be disabled.TLM shall reduce its performances.
```

**`4941757`**（130 字元）

```
TLM shall guarantee the CAN network communication and interface, and avoid every network wake-up request by Front_Panel_OnOff.Req.
```

**`4941758`**（134 字元）

```
TLM shall guarantee the CAN network communication and interface, and avoid every network wake-up request by CLIMATIC_PANEL.Radio_Btn0.
```

## SWE-PM-009

### §1.6.2.1 TLM algorithm requirements（2 個錨點）

**`4941354`**（50 字元）

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

**`4941355`**（51 字元）

```
CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource
```

### §1.6.2.1.13 TLM initialization: Init state（8 個錨點）

**`4941441`**（354 字元）

```
First default values for TLM are: TLM_Status.Info, $Telematic_Power$ equal to "Sleep" value; VPLastStatus equal to "On" value; SwitchOff_Timeout_Setting.Req equal to "00 min" == Timeout1 equal to 00 minutes; Timeout1 equal to 00 minutes for LTM High Auto_SwitchOn_Setting.Req equal to "Recall_Last" value; Antitheft_Activation.Req equal to "False" value.
```

**`4941442`**（36 字元）

```
RemStartFail equal to “False” value;
```

**`4941443`**（137 字元）

```
TLM is able to guarantee its functionalities and its behaviour only IF the voltage is limited within certain thresholds described in SIS.
```

**`4941445`**（121 字元）

```
In this case, TLM has to behave according to requirements of par. "TLM_Status.Info and $Telematic_Power$ signal setting".
```

**`4941446`**（245 字元）

```
IF the voltage exceeds the higher or the lower voltage threshold for a certain time, or also at every battery disconnection event,THEN TLM has to set itself in a INIT state, until certain conditions that allow TLM to exit from this status occur.
```

**`4941447`**（97 字元）

```
For voltage threshold values and for timings relative to enter and exit INIT state, refer to SIS.
```

**`4941449`**（388 字元）

```
After a battery reconnection and also when TLM has to exit INIT state (as soon as the voltage is limited within certain thresholds), TLM is able to work properly again and it has to restore the last user settings and the last variables values: VPLastStatus, SwitchOffSetting.Req, Auto_SwitchOn_Setting.Req shall be restored to their values before the battery disconnection / battery reset
```

**`4941450`**（185 字元）

```
Then, TLM has to behave according to requirements of par. "TLM_Status.Info and $Telematic_Power$ signal setting", setting TLM_Status.Info to "Sleep" first and starting from Sleep state.
```

### §1.6.2.1.14 TLM modules and functionalities depending on operative state（1 個錨點）

**`4941453`**（4259 字元）

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
