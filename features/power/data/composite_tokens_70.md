# 複合觀察目標之原子 token（70 包 / R-P395(a)）

> **執行層供料，不判定、不預填代理量**（R-P395(a) / §I）。
> **不合併同義** —— `HU mode` 與 `TLM state` 為二 token，是否同物由分析層判（§I）。

> 母體：三閘未歸零之條（G245 家族 A 上界 ∪ G250 `Read the HU mode/state`
> ∪ G247 Proc/ER 非 PENDING 之內部訊號句）＝ **170** 條。
> 拆分符：` and ` / ` against ` / `, `。**已為白名單之原子不入母體**
> （`$MESSAGE.Signal$`、引號具名元件、音訊詞、log 詞）。

## 相異 token **59** 個（出現 303 次）

> 末欄「既裁之解」**非本層指定之代理量**，僅引**既有條文**供分析層對照；
> 空白者即無既裁，須於 71 包裁（R-P395(b)）。

| token | 出現 | TC 數 | tc_id（前 8）| 代表錨點 | 既裁之解（引條文，非本層指定）|
|---|---|---|---|---|---|
| `screen` | 50 | 50 | 044、045、046、074、075、076、077、085 | `CFTS009-4941375` | — |
| `TLM_Status.Info` | 40 | 40 | 059、060、061、062、063、064、066、067 | `CFTS009-4941504` | `$STATUS_TELEMATIC.PowerSts_Telematic$`（R-P368 段 1–3 解得） |
| `$Telematic_Power$` | 28 | 28 | 051、052、053、054、059、060、061、062 | `CFTS009-4941391` | `$STATUS_TELEMATIC.PowerSts_Telematic$`（R-P368；LID r2069 `Telematic_Power` 逐字） |
| `TLM state` | 21 | 21 | 030、033、112、113、114、115、133、134 | `CFTS009-4941720` | — |
| `antitheft request` | 19 | 19 | 111、112、113、115、124、126、129、130 | `CFTS009-4941638` | — |
| `HU mode` | 13 | 13 | 044、045、046、162、163、164、166、167 | `CFTS009-4941375` | — |
| `VPLastStatus` | 9 | 9 | 066、067、068、069、075、077、078、083 | `CFTS009-4941540` | — |
| `applied theme` | 7 | 7 | 227、231、246、251、252、253、254 | `CFTS009-4942013` | — |
| `audio path` | 6 | 6 | 135、136、198、199、200、201 | `CFTS009-4941601` | — |
| `AMP` | 5 | 5 | 261、267、273、275、277 | `CFTS009-4941354` | — |
| `ICS` | 5 | 5 | 261、267、273、275、277 | `CFTS009-4941354` | — |
| `shown Splash Screen` | 4 | 4 | 153、154、196、197 | `CFTS009-4941678` | `"Splash Screen"`（R-P387(b)；`4941453` 之 `(*)` 註腳） |
| `display` | 4 | 4 | 198、199、200、201 | `CFTS009-4941364` | — |
| `$Radio_Theme$` | 4 | 4 | 231、232、246、247 | `CFTS009-4942017` | `$RADIO_B4.Radio_Theme$`（R-P368；LID r1531） |
| `season the HU determines` | 4 | 4 | 255、256、257、258 | `CFTS009-4942091` | — |
| `TLM` | 4 | 4 | 261、273、275、277 | `CFTS009-4941354` | — |
| `active source` | 3 | 3 | 033、062、071 | `CFTS009-4941722` | — |
| `active functionality` | 3 | 3 | 088、092、093 | `CFTS009-4941569` | — |
| `HU reaction` | 3 | 3 | 159、160、161 | `CFTS009-4941873` | — |
| `power mode` | 3 | 3 | 178、179、180 | `CFTS009-4941301` | — |
| `screen sequence` | 3 | 3 | 183、203、204 | `CFTS009-4941942` | — |
| `audio output` | 3 | 3 | 188、189、190 | `CFTS009-4941944` | — |
| `startup flow` | 3 | 3 | 219、220、221 | `CFTS009-4941962` | — |
| `HMI` | 3 | 3 | 219、220、221 | `CFTS009-4941962` | — |
| `avatar list in the profile screen` | 3 | 3 | 239、240、241 | `CFTS009-4942027` | — |
| `shown seat graphic` | 3 | 3 | 244、245、248 | `CFTS009-4942033` | — |
| `TLM power indication` | 3 | 3 | 261、273、275 | `CFTS009-4941354` | — |
| `DTV functionality availability` | 3 | 3 | 261、273、275 | `CFTS009-4941354` | — |
| `TLM display through SplashScreen_Time` | 2 | 2 | 002、003 | `CFTS009-4942337` | — |
| `volume limit` | 2 | 2 | 010、014 | `CFTS009-4942354` | — |
| `audio output state` | 2 | 2 | 010、014 | `CFTS009-4942354` | — |
| `audio` | 2 | 2 | 045、046 | `CFTS009-4941375` | — |
| `its duration` | 2 | 2 | 105、106 | `CFTS009-4941600` | — |
| `display backlight` | 2 | 2 | 127、128 | `CFTS009-4941895` | — |
| `stored last status` | 2 | 2 | 145、146 | `CFTS009-4941624` | — |
| `its timing` | 2 | 2 | 232、247 | `CFTS009-4942017` | — |
| `played animation` | 2 | 2 | 259、260 | `CFTS009-4942091` | — |
| `TLM display` | 2 | 2 | 263、265 | `CFTS009-4941354` | — |
| `DTV states` | 2 | 2 | 267、277 | `CFTS009-4941354` | — |
| `network state` | 2 | 2 | 273、275 | `CFTS009-4941354` | — |
| `FPDM` | 2 | 2 | 273、275 | `CFTS009-4941354` | — |
| `TLM display before` | 1 | 1 | 001 | `CFTS009-4942337` | — |
| `after SplashScreen_Time` | 1 | 1 | 001 | `CFTS009-4942337` | — |
| `active audio source` | 1 | 1 | 030 | `CFTS009-4941720` | — |
| `entertainment audio` | 1 | 1 | 044 | `CFTS009-4941375` | — |
| `HU timer` | 1 | 1 | 122 | `CFTS009-4941990` | — |
| `its power mode` | 1 | 1 | 122 | `CFTS009-4941990` | — |
| `HU behavior` | 1 | 1 | 173 | `CFTS009-4941858` | — |
| `configured value` | 1 | 1 | 227 | `CFTS009-4942013` | — |
| `TLM audio output state` | 1 | 1 | 263 | `CFTS009-4941354` | — |
| `ICS functionality availability` | 1 | 1 | 264 | `CFTS009-4941354` | — |
| `DTV state` | 1 | 1 | 264 | `CFTS009-4941354` | — |
| `audio output for ANC` | 1 | 1 | 268 | `CFTS009-4941354` | — |
| `ACN` | 1 | 1 | 268 | `CFTS009-4941354` | — |
| `chimes` | 1 | 1 | 268 | `CFTS009-4941354` | — |
| `SwitchOff_Timeout_Setting.Req` | 1 | 1 | 278 | `CFTS009-4941354` | — |
| `Auto_SwitchOn_Setting.Req` | 1 | 1 | 278 | `CFTS009-4941354` | — |
| `Antitheft_Activation.Req` | 1 | 1 | 278 | `CFTS009-4941354` | — |
| `RemStartFail` | 1 | 1 | 278 | `CFTS009-4941354` | — |

## 代表錨點段落全文（逐字，供分析層建字典時引用）

### `CFTS009-4941375`

```
While the HU is in IDLE mode, the HU shall transition to Full-Operation mode if the VR button is pressed. Refer to CFTS042 for VR button press definition.
```

### `CFTS009-4941504`

```
IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation" AND STATUS_BH_BCM2.RemStActvSts has a transition  from "Remote Start Active" to "Remote Start Not Active"THEN IF LTM_OperationalModeSts.Info is equal to "Ignition Pre Off" OR to "Ignition Off", TLM has to set RemStartFail = "True" THEN IF Phone_Call.Info == "Not Active", TLM has to set RemStartFail ="False" AND TLM_Status.Info and $Telematic_Power$ to "Standby" value and it passes to TLM Standby state.IF Phone_Call.Info == "Active" TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it passes to TLM Timed state.In this case, TLM has to stay in this state until Phone_Call.Info becomes equal to "Not_Active", OR at maximum until MaxCallTimeout expiration. See par. “Phone call management in Timed state” .ELSE IF LTM_OperationalModeSts.Info is not equal to "Ignition Pre Off" OR to "Ignition Off"  THEN TLM has to set RemStartFail = "False" AND TLM has to stay in the original state (Full Operation).IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal LTM_OperationalModeSts.Info has a transition to "Ignition Pre Off" OR to "Ignition Off" valueAND STATUS_BH_BCM2.RemStActvSts is equal to "Remote Start Not Active"AND RemStartFail == "False"THENaccording to a time setting selectable in the TLM menu it is possible to have two different behaviours
```

### `CFTS009-4941391`

```
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On, Ignition Off Ignition Pre-Off
```

### `CFTS009-4941720`

```
Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN TLM has to restore the active source managed by TLM before the call (for example entertainment features like DAB Tuner, rather than USB or BT streaming audio) staying still in Timed state.
```

### `CFTS009-4941638`

```
IF TLM_Status.Info and $Telematic_Power$ == "Partial Operation"
```

### `CFTS009-4941540`

```
IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” valueTHEN IF Phone_Call.Info == Not_Active TLM has to set VPLastStatus to “OFF” value and to set TLM_Status.Info and $Telematic_Power$ to "Idle" value and then it passes to TLM Idle state.
```

### `CFTS009-4942013`

```
$VC_SpecialPKG$ shall be used to determine which theme will be used by the HU. See the latest version of [PDO Theme Configuration]  for value definitions.
```

### `CFTS009-4941601`

```
IF Rear_View_Camera PROXI parameter == "Present" AND Rear_Camera_Enable.Info == "True" THENeven IF Antitheft_Result.Info is still equal to "In_Progress" or "Not_Successfully", TLM shall provide audio and video for rear view camera component, as soon as the images are available on TLM and as long as Rear_Camera_Enable.Info == "True".Refer to VF551 for details about video availability requirements on TLM screen
```

### `CFTS009-4941354`

```
CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource
```

### `CFTS009-4941678`

```
The ETM shall use $VC_SpecialPKG_IC$ = [Tungsten (147)] to display the Klipsch Splash Screen if $VC_MODEL_YEAR$ =    [2025] and $VC_VEH_LINE$ = [DT].      The ETM shall use $SplashScreen_Type$ = [Klipsch (7)]  to display the Klipsch Splash Screen if $VC_MODEL_YEAR$ > [2025] and $VC_VEH_LINE$ = [DT].
```

### `CFTS009-4941364`

```
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On,
```

### `CFTS009-4942017`

```
When the CAN network is awake, the HU shall send the special package value associated with that theme in $Radio_Theme$. if the theme has changed, the HU will update and send the new $Radio_Theme$ within <Tsend> See the $VC_SpecialPKG$ column of the [PDO Theme Configuration] reference document for the value to send in $Radio_Theme$.
```

### `CFTS009-4942091`

```
At Ignition On the HU shall determine if there has been a change in season based on the below dates.
```

### `CFTS009-4941722`

```
Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN
```

### `CFTS009-4941569`

```
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” valueTHENIF Phone_Call.Info == ActiveTHEN TLM shall show a popup to the user, asking whether to transfer the call in order to turn off TLM or not (refer to TLM HMI Specification)
```

### `CFTS009-4941873`

```
The HU shall consider SOS and Assist calls as Phone calls becoming active.
```

### `CFTS009-4941301`

```
While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when driver door ajar status ($Door_Ajar_Status$) is changed to CLOSED, HU shall play a start-up animation as defined per HMI. The startup animation will be unique for each vehicle or/and brand as defined per PDO/HMI. If driver door is not present or removed for current vehicle ($DriverDoorOnOffSts$ = [DOOR_OFF]), or if HU changes mode (due to ignition event or to due to HU power mode status change to BODY ON or to TIMED MODE while driver door ajar status ($Door_Ajar_Status$) is OPEN, the HU shall skip start-up animation. While HU is playing a start-up animation and HU changes mode (due to ignition event or to HU power mode status changes to BODY ON or to TIMED MODE) or if an ignition crank event ($PowerMode$ = [IGN_START ]), then HU shall cancel current start-up animation and switch required power mode as defined. Once a start-up animation is played, HU shall not play the next start-up animation until the next CAN wakeup cycle OR at least 30 minutes passed from last time the start-up animation was played ;whichever is greater; given all other conditions are met for startup animation to play as defined here.
```

### `CFTS009-4941942`

```
The HU shall display the startup animation separately from the Splash screen and disclaimer screen.
```

### `CFTS009-4941944`

```
If $Themed_Sound$ = [Fiat Latam] AND the "Welcome Onboard Sound" setting is set to "Once a Day" AND the HU has not yet played the startup sound yet that day, the HU startup animation shall be accompanied by a startup sound that begins at the same time.
```

### `CFTS009-4941962`

```
If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Present$ = [Present]  AND $Country_Code$ is marked as "Countries which need the combined Geolocation plus SOS Popup" (see market configuration table) then the HU shall follow the GDPR Non-Maserati startup flow in the HMI.
```

### `CFTS009-4942027`

```
The HU shall use the $VC_VEH_BRAND$  signal to determine the list of the branded avatars available in the profile screen.$VC_VEH_BRAND$  = [Chrysler] shall indicate Chrysler avatars. $VC_VEH_BRAND$  = [Dodge] shall indicate Dodge avatars. $VC_VEH_BRAND$  = [Jeep] shall indicate Jeep avatars.$VC_VEH_BRAND$  = [Alpha Romeo] shall indicate Alfa Romeo avatars.$VC_VEH_BRAND$  = [Fiat] shall indicate Fiat avatars. (DEFAULT)$VC_VEH_BRAND$  = [Maserati] shall indicate Maserati avatars.$VC_VEH_BRAND$  = [Ram] shall indicate Ram avatars.$VC_VEH_BRAND$  = [Abarth] shall indicate Fiat avatars.$VC_VEH_BRAND$  = [Opel] shall indicate  Fiat avatars.$VC_VEH_BRAND$  = [Vauxhall] shall indicate  Fiat avatars.$VC_VEH_BRAND$  = [Citroen] shall indicate Fiat avatars.$VC_VEH_BRAND$  = [Peugeot] shall indicate  Fiat avatars.
```

### `CFTS009-4942033`

```
CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the $Car_Shape_Configuration$ and $Number_of_Doors$ PROXI parameters to determine the correct settings seat graphic to display. See HMI release and PDO graphics files for settings seat graphic assignments.PNET:The HU shall use the $VC_VEH_LINE$ and the $VC_BODY_STYLE$ signals to determine the correct settings seat graphic to display. See HMI release and PDO graphics files for settings seat graphic assignments.
```

### `CFTS009-4942337`

```
TLM boot requires following timings:
After SplashScreen_Time the splash screen is loaded and shown on TLM display (only if TLM has not to pass to Standby status nor to Bench status: in these cases no splash screen has to be shown);
 After StandardScreen_Time the standard screen is visualized on TLM screen
```

### `CFTS009-4942354`

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

### `CFTS009-4941600`

```
IF Auto_SwitchOn_Setting.Req == Active OR IF Auto_SwitchOn_Setting.Req == Recall_Last AND VPLastStatus == OnTHEN TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization" logics, for Response_Wait_Time.
```

### `CFTS009-4941895`

```
The HU shall keep the backlight OFF during Standby mode except if it is required to display an HMI screen.
```

### `CFTS009-4941624`

```
ELSE TLM sets VPLastStatus to "Off" value and sets TLM_Status.Info and $Telematic_Power$ to “Idle” and then it passes to Idle state.
```

### `CFTS009-4941990`

```
When the HU shall power down in a normal sequence into Suspend to RAM. The following action shall be taken:If Suspend to RAM is allowed, HU shall start an 8 day timer and shall enter low power mode.
```

### `CFTS009-4941858`

```
When the HU Receives $ICSPowerButton$ = [Pressed] for 10 seconds consecutively, the HU shall perform a radio reset
```
