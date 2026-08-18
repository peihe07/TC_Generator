# 第五批素材（R-P181）—— 逐字原文

> 範圍取自 **G121 對帳表**，依 R-P177(b) **逐一列出 leaf ID 全集，不以區間表述**。

## 納入 —— **29 leaf**

`SWE-PM-066` `SWE-PM-067` `SWE-PM-068` `SWE-PM-069` `SWE-PM-070` `SWE-PM-074` `SWE-PM-075` `SWE-PM-076` `SWE-PM-093` `SWE-PM-094` `SWE-PM-095` `SWE-PM-097` `SWE-PM-098` `SWE-PM-099` `SWE-PM-100` `SWE-PM-101` `SWE-PM-102` `SWE-PM-103` `SWE-PM-104` `SWE-PM-105` `SWE-PM-106` `SWE-PM-107` `SWE-PM-108` `SWE-PM-109` `SWE-PM-110` `SWE-PM-111` `SWE-PM-113` `SWE-PM-114` `SWE-PM-115` 

## 排除 —— 15 leaf

| leaf | Test Set | 理由 |
|---|---|---|
| `SWE-PM-001` | Power State | 受阻斷：DR-PW6 |
| `SWE-PM-002` | Power State | 受阻斷：DR-PW6 |
| `SWE-PM-003` | Power State | 受阻斷：DR-PW6 |
| `SWE-PM-004` | Power State | 受阻斷：DR-PW6 |
| `SWE-PM-005` | Power State | 受阻斷：DR-PW6 |
| `SWE-PM-006` | Power State | 受阻斷：DR-PW6 |
| `SWE-PM-007` | Power State | 受阻斷：DR-PW6 |
| `SWE-PM-008` | Power State | 受阻斷：DR-PW6,DR-PW11 |
| `SWE-PM-009` | Power State | 受阻斷：DR-PW6 |
| `SWE-PM-010` | Power State | 受阻斷：DR-PW11 |
| `SWE-PM-053` | Startup Display | 已於第 004 批產出（R-P177(a) 不重做） |
| `SWE-PM-054` | Startup Display | 已於第 004 批產出（R-P177(a) 不重做） |
| `SWE-PM-055` | Startup Display | 已於第 004 批產出（R-P177(a) 不重做） |
| `SWE-PM-056` | Startup Display | 已於第 004 批產出（R-P177(a) 不重做） |
| `SWE-PM-112` | Startup Display | 撞上 live DR 影響面：DR-PW9（R-P165 / R-P181(c)） |

## 素材前置檢查（R-P172）

**全部 item 於 CFTS 文字層皆有內文，無 R-P144(b) 之阻斷情形。**

## 逐字原文

### `SWE-PM-066` —— Power State；CFTS 009；章節 1.9.4（item 1）

- 錨點：`4941873`

```
The HU shall consider SOS and Assist calls as Phone calls becoming active.
```

### `SWE-PM-067` —— Power State；CFTS 009；章節 1.9.4（item 1）

- 錨點：`4941874`

```
The HU shall consider Projection device calls as Phone calls becoming active.
```

### `SWE-PM-068` —— Power State；CFTS 009；章節 1.9.4（item 1）

- 錨點：`4941876`

```
IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone call, THEN the HU shall bypass the disclaimer screen if it has not yet been shown.
```

### `SWE-PM-069` —— Power State；CFTS 009；章節 1.9.4（item 1）

- 錨點：`4941877`

```
IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone call AND the phone call becomes inactive AND the HU display is on the phone main screen or phone projection call UI, THEN the HU shall transition back to IDLE.
```

### `SWE-PM-070` —— Power State；CFTS 009；章節 1.9.4（item 1）

- 錨點：`4941878`

```
IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone call, the HU shall bypass the disclaimer.  THEN if the HU returns to IDLE when the phone call becomes inactive, the HU shall show the disclaimer at the next transition to FULL OPERATION.
```

### `SWE-PM-074` —— Startup Display；CFTS 009；章節 1.9.10（item 1）

- 錨點：`4941976`

```
If there is a FOTA update available for the Radio, TBM, or ROV (see CFTS057) when the vehicle enters Body OFF mode and the HU transitions to Standby mode, the HU shall then transition to Timed mode to display the FOTA update available pop-up. See HMI for pop-up details.
```

### `SWE-PM-075` —— Startup Display；CFTS 009；章節 1.9.10（item 1）

- 錨點：`4941977`

```
If the HU Transitions to Timed mode due to the condition described in CFTS009-1809, the HU shall transition to Standby mode after: -1 minute has passed without the user interacting with the pop-up -The FOTA pop up is dismissed -$ACCDlyAct$ transitions from active to inactive
```

### `SWE-PM-076` —— Power State；CFTS 009；章節 1.9.3（item 4）

- 錨點：`4941858,4941860,4941861,4941867`

```
When the HU Receives $ICSPowerButton$ = [Pressed] for 10 seconds consecutively, the HU shall perform a radio reset
At the time of the reset the HU shall collect and save logs
the HU shall reset both the main CPU and the CAN micro at the time of the reset
If the HU is currently installing a firmware image the HU shall not reset due to a power button reset.
```

### `SWE-PM-093` —— Startup Display；CFTS 009；章節 1.3.5、1.9.8（item 2）

- 錨點：`4941301,4941941`

```
While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when driver door ajar status ($Door_Ajar_Status$) is changed to CLOSED, HU shall play a start-up animation as defined per HMI. The startup animation will be unique for each vehicle or/and brand as defined per PDO/HMI. If driver door is not present or removed for current vehicle ($DriverDoorOnOffSts$ = [DOOR_OFF]), or if HU changes mode (due to ignition event or to due to HU power mode status change to BODY ON or to TIMED MODE while driver door ajar status ($Door_Ajar_Status$) is OPEN, the HU shall skip start-up animation. While HU is playing a start-up animation and HU changes mode (due to ignition event or to HU power mode status changes to BODY ON or to TIMED MODE) or if an ignition crank event ($PowerMode$ = [IGN_START ]), then HU shall cancel current start-up animation and switch required power mode as defined. Once a start-up animation is played, HU shall not play the next start-up animation until the next CAN wakeup cycle OR at least 30 minutes passed from last time the start-up animation was played ;whichever is greater; given all other conditions are met for startup animation to play as defined here.
While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when driver door ajar status ($Door_Ajar_Status$) is changed to CLOSED, HU shall play a start-up animation as defined per HMI. The startup animation will be unique for each vehicle or/and brand as defined per PDO/HMI. If driver door is not present or removed for current vehicle ($DriverDoorOnOffSts$ = [DOOR_OFF]), or if HU changes mode (due to ignition event or to due to HU power mode status change to BODY ON or to TIMED MODE while driver door ajar status ($Door_Ajar_Status$) is OPEN, the HU shall skip start-up animation. While HU is playing a start-up animation and HU changes mode (due to ignition event or to HU power mode status changes to BODY ON or to TIMED MODE) or if an ignition crank event ($PowerMode$ = [IGN_START ]), then HU shall cancel current start-up animation and switch required power mode as defined. Once a start-up animation is played, HU shall not play the next start-up animation until the next CAN wakeup cycle OR at least 30 minutes passed from last time the start-up animation was played ;whichever is greater; given all other conditions are met for startup animation to play as defined here.
```

### `SWE-PM-094` —— Startup Display；CFTS 009；章節 1.9.8（item 1）

- 錨點：`4941942`

```
The HU shall display the startup animation separately from the Splash screen and disclaimer screen.
```

### `SWE-PM-095` —— Power State；CFTS 009；章節 1.7.1.1.1（item 1）

- 錨點：`4941784`

```
As soon as signal LTM_OperationalModeSts.Info becomes different from "SNA" value again, TLM has still to behave following the state diagram, considering the updated value of LTM_OperationalModeSts.Info signal and avoiding the possible visualization of the splash screen
```

### `SWE-PM-097` —— Startup Display；CFTS 009；章節 1.6.2.1.16（item 1）

- 錨點：`4941680`

```
If DID "Startup Animation Selection" = [Fiat Latam] then the HU shall replace the vehicle brand logo with the Fiat Latam Logo regardless of the value of $VC_Veh_Brand$
```

### `SWE-PM-098` —— Startup Display；CFTS 009；章節 1.9.8（item 1）

- 錨點：`4941943`

```
If $Themed_Sound$ = [Fiat Latam] and the "Welcome Onboard Sound" setting is set to "Always", the HU startup animation shall be accompanied by a startup sound that begins at the same time.
```

### `SWE-PM-099` —— Startup Display；CFTS 009；章節 1.9.8（item 2）

- 錨點：`4941944,4941945`

```
If $Themed_Sound$ = [Fiat Latam] AND the "Welcome Onboard Sound" setting is set to "Once a Day" AND the HU has not yet played the startup sound yet that day, the HU startup animation shall be accompanied by a startup sound that begins at the same time.
For the purposes of CFTS009-2299, the HU shall consider it a new "day" to allow the sound to be played any time the customer selected date changes; including manual time adjustments from the user, the time passing midnight, or automatic adjustments due to time zones or Daylight Savings Time.
```

### `SWE-PM-100` —— Startup Display；CFTS 009；章節 1.9.8（item 1）

- 錨點：`4941947`

```
If $Themed_Sound$ = [Fiat Latam] AND the "Welcome Onboard Sound" setting is set to "Never", the HU startup animation shall not be accompanied by a startup sound that begins at the same time.
```

### `SWE-PM-101` —— Startup Display；CFTS 009；章節 1.6.2.1.16（item 4）

- 錨點：`4941673,4941674,4941675,4941676`

```
- IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the vehicle brand logo only, that depends on Brand_Configuration_2 parameter value;
- IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM has to show the Beats Brand White logo in addition to the vehicle brand logo;
- IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has to show the Sirius logo in addition to the vehicle brand logo;
- IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to show both the Sirius and the Beats logos in addition to the vehicle brand logo.
```

### `SWE-PM-102` —— Startup Display；CFTS 009；章節 1.6.2.1.16（item 1）

- 錨點：`4941678`

```
The ETM shall use $VC_SpecialPKG_IC$ = [Tungsten (147)] to display the Klipsch Splash Screen if $VC_MODEL_YEAR$ =    [2025] and $VC_VEH_LINE$ = [DT].      The ETM shall use $SplashScreen_Type$ = [Klipsch (7)]  to display the Klipsch Splash Screen if $VC_MODEL_YEAR$ > [2025] and $VC_VEH_LINE$ = [DT].
```

### `SWE-PM-103` —— Power State；CFTS 009；章節 1.6.2.1.2（item 2）

- 錨點：`4941364,4941365`

```
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On,
This status is related to TLM audio is OFF. TLM shall allow only Splash Screen visualization on its display.  ICS functionalities are available.  DTV shall be OFF.
```

### `SWE-PM-104` —— Startup Display；CFTS 009；章節 1.9.9（item 2）

- 錨點：`4941950,4941952`

```
The splash screen and disclaimer screen shall be shown the first time each bus cycle the HU transitions to Timed or Full Operation modes.
If the disclaimer screen needs to be shown it shall be shown the first time each bus cycle the HU transitions from Idle, Standby, or Partial Operation to Timed or Full Operation modes.
```

### `SWE-PM-105` —— Startup Display；CFTS 009；章節 1.9.9（item 1）

- 錨點：`4941951`

```
The disclaimer and splash screen can be temporarily skipped for incoming/outgoing/ongoing calls, climate pop-ups, backup camera, SOS and Assist calls, and FOTA pop ups, but must be displayed at the next transition to Timed or Full Operation modes during that bus cycle. See HMI logic and Flow "Startup" requirements for details.
```

### `SWE-PM-106` —— Startup Display；CFTS 009；章節 1.9.9（item 1）

- 錨點：`4941955`

```
For all variations of the disclaimer screen and geolocation pop up listed below, if the configuration parameter $Ecall_Button_Variant$ = [SOS] the HU shall use the SOS text for the disclaimer.
```

### `SWE-PM-107` —— Startup Display；CFTS 009；章節 1.9.9（item 1）

- 錨點：`4941956`

```
For all variations of the disclaimer screen and geolocation pop up listed below, if the configuration parameter $Ecall_Button_Variant$ = [Help] the HU shall replace the "SOS" text with the "Help" version of the disclaimer.
```

### `SWE-PM-108` —— Startup Display；CFTS 009；章節 1.9.9（item 1）

- 錨點：`4941958`

```
If $VC_VEH_BRAND$ <> [Maserati] the R1 Head Unit shall only show the core disclaimer screen once every 30 ignition cycles
```

### `SWE-PM-109` —— Startup Display；CFTS 009；章節 1.9.9（item 1）

- 錨點：`4941962`

```
If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Present$ = [Present]  AND $Country_Code$ is marked as "Countries which need the combined Geolocation plus SOS Popup" (see market configuration table) then the HU shall follow the GDPR Non-Maserati startup flow in the HMI.
```

### `SWE-PM-110` —— Startup Display；CFTS 009；章節 1.9.9（item 1）

- 錨點：`4941963`

```
If  $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Present$ = [Not Present] OR $Country_Code$ is not marked as "Countries which need the combined Geolocation plus SOS Popup" in the Market Configuration Table), the HU shall follow the Non-GDPR/Non-Maserati Startup flow in the HMI.
```

### `SWE-PM-111` —— Startup Display；CFTS 009；章節 1.9.9（item 1）

- 錨點：`4941964`

```
For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Present$ = [Not Present] OR$Country_Code$  does not require SOS or Geolocation) then the HU shall add the ADAS text to the disclaimer
```

### `SWE-PM-113` —— Startup Display；CFTS 009；章節 1.9.9（item 1）

- 錨點：`4941968`

```
For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Present$ = [Present]  AND $Country_Code$ requires geolocation and SOS in the disclaimer then the HU shall add the ADAS and SOS to the geolocation pop-up or disclaimer. See HMI for different statup conditions to determine when to add geolocation + SOS Pop-up or add geolocation and SOS text to Disclaimer.
```

### `SWE-PM-114` —— Power State；CFTS 009；章節 1.9.4（item 1）

- 錨點：`4941876`

```
IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone call, THEN the HU shall bypass the disclaimer screen if it has not yet been shown.
```

### `SWE-PM-115` —— Power State；CFTS 009；章節 1.9.4（item 1）

- 錨點：`4941878`

```
IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone call, the HU shall bypass the disclaimer.  THEN if the HU returns to IDLE when the phone call becomes inactive, the HU shall show the disclaimer at the next transition to FULL OPERATION.
```
