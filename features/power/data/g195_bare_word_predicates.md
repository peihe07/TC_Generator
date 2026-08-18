# G195 —— 裸詞謂詞之逐一實測（R-P280）

> **本檔只實測與呈；不改任何 TC 值**（R-P280(d)）。
> **判準**：一個命中為**偽陽性**，若該裸詞於命中處之語義**與該謂詞之用途無關**。
> 抽樣種子 `random.Random(41)`；每謂詞抽 3 條，不足者全取。

## 一、彙總（28 個謂詞）

| 模組.謂詞 | 語料 | 命中 | 裸詞 |
|---|---|---|---|
| `audit_precond_state.MODE_RE` | TC | 1482 | `mode`、`state`、`status` |
| `audit_precond_state.BENCH_RE` | TC | 532 | `available`、`awake`、`bench`、`clock`、`connected`、`equipped`、`injection`、`network` |
| `build_dangling.WRAPPER_RE` | 文字層 | 62 | `docx`、`xlsx` |
| `build_dangling_rulecheck.RESOURCE_RE` | 文字層 | 62 | `docx`、`xlsx` |
| `confirm_row4.COND_RE` | 規格 | 226 | `case`、`conditions`、`following`、`long` |
| `g113_buckets.ILLUSTRATIVE_RE` | 規格 | 10 | `example`、`like`、`rather`、`refer`、`specification`、`than` |
| `lint_tcs.ENV_STABILITY_RE` | TC | 0 | `configured`、`connected`、`from`、`functioning`、`normal`、`normally`、`operating`、`power` |
| `lint_tcs.TABLE_RE` | TC | 0 | `table` |
| `lint_tcs.PRECOND_BEHAVIOUR_RE` | TC | 280 | `been`、`begins`、`changes`、`completed`、`completes`、`elapses`、`expires`、`finishes` |
| `lint_tcs.TEST_QUANTITY_RE` | TC | 72 | `burst`、`cycles`、`events`、`injection`、`interval`、`intervals`、`iterations`、`level` |
| `lint_tcs.FINAL_STEP_INTENT_RE` | TC | 264 | `check`、`confirm`、`that`、`verif`、`verify`、`whether` |
| `lint_tcs.TIME_TOKEN_RE` | TC | 146 | `duration`、`elapsed`、`measured`、`milliseconds`、`minutes`、`recorded`、`seconds`、`time` |
| `lint_tcs.TIME_EQUALITY_RE` | TC | 14 | `equal`、`equals`、`exactly`、`matches` |
| `rejudge_axis.TIMING_RE` | TC | 302 | `minutes`、`seconds`、`time` |
| `rejudge_axis.BOUNDARY_RE` | TC | 34 | `least`、`most`、`than` |
| `rejudge_design_method.NO_TRANSITION_RE` | TC | 36 | `change`、`does`、`pass`、`reads`、`remains`、`reset`、`stays`、`still` |
| `rejudge_design_method.ROW1_RE` | TC | 1 | `allowed`、`attempt`、`illegal`、`invalid` |
| `rejudge_design_method.ROW2_RE` | TC | 2 | `disconnect`、`fault`、`inject`、`injection` |
| `rejudge_design_method.POSITIVE_RE` | TC | 218 | `back`、`enters`、`from`、`full`、`goes`、`idle`、`leaves`、`mode` |
| `rejudge_design_method.ROW6_RE` | TC | 14 | `after`、`before`、`boundary`、`date`、`greater`、`less`、`limit`、`passes` |
| `rejudge_design_method.BENCH_RE` | TC | 526 | `available`、`bench`、`carries`、`clock`、`connected`、`equipped`、`factory`、`injection` |
| `rejudge_design_method.ROW5_RE` | TC | 28 | `other`、`range`、`than`、`value` |
| `rejudge_priority.COSMETIC_RE` | TC | 573 | `animation`、`brand`、`colou`、`customi`、`font`、`icon`、`image`、`screen` |
| `rejudge_priority.BENCH_RE` | TC | 247 | `available`、`bench`、`carries`、`clock`、`connected`、`equipped`、`factory`、`paired` |
| `reverse_coverage.SPLIT_RE` | 規格 | 269 | `until` |
| `reverse_probe_rows.PARAM_RE` | TC | 299 | `carries`、`equal`、`greater`、`reads`、`than` |
| `reverse_probe_rows.REMOVE_RE` | TC | 2 | `broadcast`、`cease`、`ceases`、`cuts`、`disable`、`disables`、`disconnect`、`disconnects` |
| `scan_clause_patterns.ENUM_RE` | 規格 | 46 | `following` |

## 二、逐一之抽樣實例

### `audit_precond_state.MODE_RE` —— 命中 1482（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `TLM` | `l.Info values Ignition off in Idle passes the TLM to Standby Ignition off in Idle passes` |
| `is in Standby state` | `. Rear_View_Camera reads "Present" 3. The TLM is in Standby state Rear_Camera_Enable.Info: "False" then "` |
| `CAN` | `nd to RAM starts the 8 day timer 1. A LIN and CAN simulation tool is connected 2. Suspend` |

### `audit_precond_state.BENCH_RE` —— 命中 532（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `is connected` | `n to Standby 1. A LIN and CAN simulation tool is connected 2. TLM_Status.Info and $Telematic_Power` |
| `simulation tool` | `o brand adds the Sirius logo 1. A LIN and CAN simulation tool is connected 2. SDARS_Presence reads "P` |
| `simulation tool` | `llowed in Ignition Pre_Start 1. A LIN and CAN simulation tool is connected 2. The TLM is in an Igniti` |

### `build_dangling.WRAPPER_RE` —— 命中 62（語料：文字層）

| 命中字串 | 語境 |
|---|---|
| `CFTSMV009_CIP_R4_O1583_1_inline.rtf WrapperResource` | `R1L, VP2R7] [EE Architecture:CUSW, PowerNet] CFTSMV009_CIP_R4_O1583_1_inline.rtf WrapperResource 4941027: [Artifact Type:Subsystem F` |
| `CFTSMV009_CIP_R4_O1302_7_inline.rtf WrapperResource` | `EE Architecture:Atlantis High, Atlantis Mid] CFTSMV009_CIP_R4_O1302_7_inline.rtf WrapperResource 4941740: [Artifact Type:Subsystem F` |
| `CFTSMV010_CIP_R3_O419_Excel_Document.xls WrapperResource` | `o:allSys] [EE Architecture:CUSW, PowerNet]** CFTSMV010_CIP_R3_O419_Excel_Document.xls WrapperResource **1.5.2.2.1.2 ECU Local Voltage {494` |

### `build_dangling_rulecheck.RESOURCE_RE` —— 命中 62（語料：文字層）

| 命中字串 | 語境 |
|---|---|
| `CFTSMV010_CIP_R3_O708_Excel_Document.xls WrapperResource` | `io:allSys] [EE Architecture:Atlantis High]** CFTSMV010_CIP_R3_O708_Excel_Document.xls WrapperResource **1.9 Configuration Parameters {4942` |
| `CFTSMV010_CIP_R3_O374_Excel_Document.xls WrapperResource` | `ltage threshold has a tolerance of +/- 0.5V) CFTSMV010_CIP_R3_O374_Excel_Document.xls WrapperResource 4942205: [Artifact Type:Subsystem F` |
| `CFTSMV010_CIP_R3_O362_Excel_Document.xls WrapperResource` | `l] [Radio:allSys] [EE Architecture:PowerNet] CFTSMV010_CIP_R3_O362_Excel_Document.xls WrapperResource 4942321: [Artifact Type:Subsystem F` |

### `confirm_row4.COND_RE` —— 命中 226（語料：規格）

| 命中字串 | 語境 |
|---|---|
| `When` | `soon as possible, depending on boot timings. When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS` |
| `IF` | `$ to “Idle” and then it passes to Idle state. IF Antitheft_Result.Info == "Successfully"` |
| `if` | `r screen and geolocation pop up listed below, if the configuration parameter $Ecall_Butt` |

### `g113_buckets.ILLUSTRATIVE_RE` —— 命中 10（語料：規格）

| 命中字串 | 語境 |
|---|---|
| `for example` | `active source managed by TLM before the call (for example entertainment features like DAB Tuner,` |
| `for example` | `active source managed by TLM before the call (for example entertainment features like DAB Tuner,` |
| `refer to TLM HMI Specification` | `fer the call in order to turn off TLM or not (refer to TLM HMI Specification) In this case, IF user accepts, TLM sha` |

### `lint_tcs.ENV_STABILITY_RE` —— 命中 0（語料：TC）

| 命中字串 | 語境 |
|---|---|
| （命中 0） | |

### `lint_tcs.TABLE_RE` —— 命中 0（語料：TC）

| 命中字串 | 語境 |
|---|---|
| （命中 0） | |

### `lint_tcs.PRECOND_BEHAVIOUR_RE` —— 命中 280（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `passes to` | `haviour 2 on a Jeep with the driver door open passes to Standby Behaviour 2 on a Jeep with the` |
| `transition to` | `tatus.Info and $Telematic_Power$ to check the transition to Standby 1. The TLM registers both the d` |
| `occurred` | `he LTM_OperationalModeSts.Info transition has occurred Antitheft_Result.Info: "Successfully" 1` |

### `lint_tcs.TEST_QUANTITY_RE` —— 命中 72（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `event` | `1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while t` |
| `intervals` | `nch Event burst: 20 events injected at 100 ms intervals during boot 1. Start the TLM boot seque` |
| `measurement window` | `uced to 20 and the TLM stays muted before the measurement window elapses 2. The volume limit returns to` |

### `lint_tcs.FINAL_STEP_INTENT_RE` —— 命中 264（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `to check` | `ta 3. Read the CAN trace and the volume level to check that AUD_LVL is not updated 1. The TLM` |
| `to check` | `2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby 1. The TLM re` |
| `to check` | `n cycles 2. Read the screen across the cycles to check how often the disclaimer appears 1. The` |

### `lint_tcs.TIME_TOKEN_RE` —— 命中 146（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `10 seconds` | `conds after recovery Normal operation resumes 10 seconds after recovery 1. A LIN and CAN simulat` |
| `00 min` | `meout starts on ignition off with Timeout1 at 00 min 1. Timeout1 is at "00 min" 2. The TLM i` |
| `00 MIN` | `ing.Req and Timeout1 read a value other than "00 MIN" 3. Brand_Configuration _2 reads "Jeep"` |

### `lint_tcs.TIME_EQUALITY_RE` —— 命中 14（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `equal` | `al to "2025" 3. The ETM carries $VC_VEH_LINE$ equal to "DT" $VC_SpecialPKG_IC$: "Tungsten (` |
| `matches` | `accepts the configuration 2. The recirc icon matches the assignment for that vehicle line an` |
| `matches` | `he configuration 2. The settings seat graphic matches the assignment for that vehicle line an` |

### `rejudge_axis.TIMING_RE` —— 命中 302（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `00 min` | `wn in the TLM menu 2. The offered values are "00 min" and "180 min" and no other value is of` |
| `20 minutes` | `g.Req reads "00 min" 3. Switch_Off_Time reads 20 minutes Antitheft_Result.Info = "Successfully"` |
| `timeout` | `The ex-factory default sets a zero switch off timeout The ex-factory default sets a zero swit` |

### `rejudge_axis.BOUNDARY_RE` —— 命中 34（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `other than` | `TM or ETM offers two timeout parameters Radio other than LTM or ETM offers two timeout parameter` |
| `other than` | `ged within Timeout1 1. Timeout1 is at a value other than "00 min" 2. The TLM is in Timed state 3` |
| `other than` | `d passes to Standby 1. Timeout1 is at a value other than "00 min" 2. The TLM is in Timed state w` |

### `rejudge_design_method.NO_TRANSITION_RE` —— 命中 36（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `no change` | `e parameter reads back its previous value and no change is stored Auto_SwitchOn_Setting.Req can` |
| `still at` | `hat the TLM stays Timed 1. Phone_Call.Info is still at "Active" when Timeout1 expires and the` |
| `stays in` | `udio paths to check the active set 1. The TLM stays in Partial Operation without further trans` |

### `rejudge_design_method.ROW1_RE` —— 命中 1（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `Attempt to` | `the timeout setting entry in the TLM menu 2. Attempt to change the offered timeout parameter an` |

### `rejudge_design_method.ROW2_RE` —— 命中 2（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `disconnect` | `tting.Req hold known values 3. The battery is disconnected NA 1. Reconnect the battery and let t` |
| `disconnect` | `ting.Req read their values before the battery disconnection TLM starts from Sleep state after le` |

### `rejudge_design_method.POSITIVE_RE` —— 命中 218（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `is in BODY OFF-TIMED mode` | `d CAN simulation tool is connected 2. The TLM is in BODY OFF-TIMED mode 3. Ecall, ACN and chimes modes are inac` |
| `is in a state` | `nd CAN simulation tool is connected 2. The HU is in a state that reacts to a phone call becoming ac` |
| `is in IDLE mode` | `nd CAN simulation tool is connected 2. The HU is in IDLE mode 3. The display is on the phone main scr` |

### `rejudge_design_method.ROW6_RE` —— 命中 14（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `the day before` | `n tool is connected 2. The HU clock is set to the day before the Summer start date An Ignition On af` |
| `after the date passes` | `day before the Fall start date An Ignition On after the date passes March, 20th 1. Bring the HU through the` |
| `after the date passes` | `y before the Winter start date An Ignition On after the date passes June, 21st 1. Bring the HU through the` |

### `rejudge_design_method.BENCH_RE` —— 命中 526（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `is connected` | `the second call is served 1. The second call is connected and is managed by the TLM 2. The TLM re` |
| `simulation tool` | `a phone call becoming active 1. A LIN and CAN simulation tool is connected 2. The HU is in a state th` |
| `is connected` | `on from Idle 1. A LIN and CAN simulation tool is connected 2. The HU is in Idle mode 3. The discla` |

### `rejudge_design_method.ROW5_RE` —— 命中 28（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `out of range` | `isted in Input Test Data 2. Apply the voltage out of range condition on the bench 3. Read the volu` |
| `out of range` | `gnal is held 2. The TLM registers the voltage out of range condition 3. The TLM leaves the Battery` |
| `a value other than` | `ion tool is connected 2. $VC_VEH_BRAND$ reads a value other than "Maserati" 3. $TBM_Present$ reads "Pres` |

### `rejudge_priority.COSMETIC_RE` —— 命中 573（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `Brand` | `Timeout1 read a value other than "00 MIN" 3. Brand_Configuration _2 reads a value other th` |
| `logo` | `logo screen is presented 2. The vehicle brand logo that depends on the Brand_Configuration` |
| `font` | `Chrysler font The Jeep brand selects the Jeep font The Jeep brand selects the Jeep font 1.` |

### `rejudge_priority.BENCH_RE` —— 命中 247（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `simulation tool` | `es the TLM to Full-Operation 1. A LIN and CAN simulation tool is connected 2. The TLM is running the` |
| `simulation tool` | `tup sound with the animation 1. A LIN and CAN simulation tool is connected 2. $Themed_Sound$ reads "F` |
| `simulation tool` | `the first startup of the day 1. A LIN and CAN simulation tool is connected 2. $Themed_Sound$ reads "F` |

### `reverse_coverage.SPLIT_RE` —— 命中 269（語料：規格）

| 命中字串 | 語境 |
|---|---|
| `

` | `set in case a continuing call is still active While in BODY ON or BODY OFF-TIMED mode,` |
| `
` | `Timed" value and it passes to TLM Timed state. IF Antitheft_Result.Info == "Successfull` |
| `
` | `us logo in addition to the vehicle brand logo; - IF SDARS_Presence == "Present" AND Aud` |

### `reverse_probe_rows.PARAM_RE` —— 命中 299（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `RemStartFail is at "False` | `than "00 min" 2. The TLM is in Timed state 3. RemStartFail is at "False" 4. A DAB Tuner source was active befor` |
| `Phone_Call.Info reads "Not_Active` | `M state to check the transition to Standby 1. Phone_Call.Info reads "Not_Active" before MaxCallTimeout expires 2. TLM_S` |
| `$Telematic_Power$ reads "Partial_Operation` | `TLM accepts the signal without a bus error 2. $Telematic_Power$ reads "Partial_Operation" Remote Start Active reports Partial_Op` |

### `reverse_probe_rows.REMOVE_RE` —— 命中 2（語料：TC）

| 命中字串 | 語境 |
|---|---|
| `Stop the broadcast of the two Load Shed signals on the bus` | `e Load Shed condition is already active NA 1. Stop the broadcast of the two Load Shed signals on the bus 2. Read the AUD_LVL signal and the audi` |
| `Stop the broadcast of the two Load Shed signals on the bus` | `Actv = [0h] STATUS_LIN.PN14_LS_Lvl7 = [0h] 1. Stop the broadcast of the two Load Shed signals on the bus 2. Resume the broadcast with the recove` |

### `scan_clause_patterns.ENUM_RE` —— 命中 46（語料：規格）

| 命中字串 | 語境 |
|---|---|
| `: "SwitchOff_Timeout_Setting` | `call management in Timed state” . Behaviour 2: "SwitchOff_Timeout_Setting.Req == Timeout1 <> 00 MIN" or ( If Auto` |
| `:IF VPLastStatus == On TLM has to show a proper Splash Screen, depending on par` | `3: "Auto_SwitchOn_Setting.Req == Recall_Last":IF VPLastStatus == On TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization" log` |
| `:         After the LTM_OperationalModeSts` | `2: "Auto_SwitchOn_Setting.Req == Not_Active ": After the LTM_OperationalModeSts.Info transition, TLM sets TLM_Status.In` |
