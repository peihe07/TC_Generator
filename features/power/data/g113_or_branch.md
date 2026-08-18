# G113 —— OR 分支涵蓋（R-P161）

> **不判 FAIL**：未覆蓋之分支入 R-P76 之待人工裁決類，逐支裁決三選一。
> 正規化限於分隔符層（黏連之 `OR` 補回空白、大小寫統一），**不擴及語義**。

## 批次 `batch_001_power_down`

### `SWE-PM-071` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | shown on TLM display (only if TLM has not to pass to Sta | `display`、`only`、`pas`、`shown`、`standby`、`tlm` | `only`、`pas` | **部分未覆蓋** |
| 1 | 2 | to Bench status | `bench` | — | 已覆蓋 |

### `SWE-PM-073` —— 分支 4

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | While in BODY ON | — | — | 無獨有實詞 —— 不判 |
| 1 | 2 | BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_S | `current`、`display`、`h`、`keep`、`mimimize`、`mode` | `mimimize`、`only`、`receiv`、`withdraw` | **部分未覆蓋** |
| 2 | 1 | Unless defined otherwise, TLM shall stay in this state u | `condition`、`defin`、`either`、`otherwise`、`range`、`satisfi` | `defin`、`either`、`otherwise`、`satisfi`、`thi`、`unles` | **部分未覆蓋** |
| 2 | 2 | shall go back to normal behavior 10 seconds after STATUS | `after`、`back`、`becom`、`behavior`、`go`、`h` | `back`、`becom`、`behavior`、`go` | **部分未覆蓋** |

**合計分支 6，未覆蓋 **4**。**

## 批次 `batch_002_timeout_settings`

### `SWE-PM-057` —— 分支 28

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | the user can select SwitchOff_Timeout_Setting.Req to "00 | `select`、`switchoff_timeout_setting.req`、`user` | `user` | **部分未覆蓋** |
| 1 | 2 | to "20 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 2 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 2 | 2 | 20 minutes" respectively. | `minut`、`respectively.` | `respectively.` | **部分未覆蓋** |
| 3 | 1 | the user can select SwitchOff_Timeout_Setting.Req to "00 | `select`、`switchoff_timeout_setting.req`、`user` | `user` | **部分未覆蓋** |
| 3 | 2 | to "60 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 4 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 4 | 2 | 60 minutes" respectively. | `minut`、`respectively.` | `respectively.` | **部分未覆蓋** |
| 5 | 1 | the user can select SwitchOff_Timeout_Setting.Req to "00 | `select`、`switchoff_timeout_setting.req`、`user` | `user` | **部分未覆蓋** |
| 5 | 2 | to "180 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 6 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 6 | 2 | 180 minutes" respectively. | `minut`、`respectively.` | `respectively.` | **部分未覆蓋** |
| 7 | 1 | For the case of LTM High Radio not present, the user can | `case`、`high`、`ltm`、`minut`、`present`、`radio` | `case`、`present`、`user` | **部分未覆蓋** |
| 7 | 2 | equal to the value specified by PROXI parameter "Switch_ | `parameter`、`proxi`、`specifi`、`switch_off_time` | `specifi` | **部分未覆蓋** |
| 8 | 1 | So, user can set SwitchOff_Timeout_Setting.Req to "00 mi | `set`、`switchoff_timeout_setting.req`、`user` | `user` | **部分未覆蓋** |
| 8 | 2 | to "20 minutes" IF PROXI parameter "Switch_Off_Time" is  | `equal`、`parameter`、`proxi`、`switch_off_time` | `equal` | **部分未覆蓋** |
| 9 | 1 | the user can select SwitchOff_Timeout_Setting.Req to "00 | `select`、`switchoff_timeout_setting.req`、`user` | `user` | **部分未覆蓋** |
| 9 | 2 | to "20 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 10 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 10 | 2 | 20 minutes" respectively. | `minut`、`respectively.` | `respectively.` | **部分未覆蓋** |
| 11 | 1 | the user can select SwitchOff_Timeout_Setting.Req to "00 | `select`、`switchoff_timeout_setting.req`、`user` | `user` | **部分未覆蓋** |
| 11 | 2 | to "60 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 12 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 12 | 2 | 60 minutes" respectively. | `minut`、`respectively.` | `respectively.` | **部分未覆蓋** |
| 13 | 1 | the user can select SwitchOff_Timeout_Setting.Req to "00 | `select`、`switchoff_timeout_setting.req`、`user` | `user` | **部分未覆蓋** |
| 13 | 2 | to "180 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 14 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 14 | 2 | 180 minutes" respectively | `minut`、`respectively` | `respectively` | **部分未覆蓋** |

### `SWE-PM-063` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | to receive one | `one`、`receive` | `one` | **部分未覆蓋** |
| 1 | 2 | more bluetooth phone calls according to following logics | `accord`、`bluetooth`、`call`、`depend`、`follow`、`logic` | `accord`、`depend`、`follow`、`logic`、`more`、`timeout1` | **部分未覆蓋** |

### `SWE-PM-064` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | the Ignition working condition switches to "Ignition Pre | `condition`、`pre`、`switch`、`work` | — | 已覆蓋 |
| 1 | 2 | to "Ignition Off | — | — | 無獨有實詞 —— 不判 |

### `SWE-PM-065` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | TLM has to restore the active source managed by TLM befo | `active`、`before`、`call`、`dab`、`entertainment`、`example` | `entertainment`、`example`、`featur`、`like`、`rather`、`restore` | **部分未覆蓋** |
| 1 | 2 | BT streaming audio) staying still in Timed state. | `audio`、`bt`、`state.`、`stay`、`stream`、`tim` | `bt`、`state.`、`stay`、`stream` | **部分未覆蓋** |

### `SWE-PM-038` —— 分支 12

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | ELSE TLM has to restore the active source managed by TLM | `active`、`before`、`call`、`dab`、`else`、`entertainment` | `else`、`entertainment`、`example`、`featur`、`like`、`rather` | **部分未覆蓋** |
| 1 | 2 | BT streaming audio) staying still in Timed state. | `audio`、`bt`、`state.`、`stay`、`stream`、`tim` | `bt`、`state.` | **部分未覆蓋** |
| 2 | 1 | stays still in Timed state until Phone_Call.Info passes  | `not_active`、`pass`、`phone_call.info`、`state`、`stay`、`tim` | — | 已覆蓋 |
| 2 | 2 | at maximum until MaxCallTimeout expiration. | `expiration.`、`maxcalltimeout`、`maximum` | `expiration.`、`maximum` | **部分未覆蓋** |
| 3 | 1 | WHEN Phone_Call.Info passes to "Not_Active | `not_active`、`pass`、`phone_call.info` | — | 已覆蓋 |
| 3 | 2 | at MaxCallTimeout expiration, TLM sets TLM_Status.Info t | `expiration`、`maxcalltimeout`、`set`、`standby`、`tlm`、`tlm_status.info` | — | 已覆蓋 |
| 4 | 1 | WHEN Phone_Call.Info passes to "Not_Active | `not_active`、`pass`、`phone_call.info` | — | 已覆蓋 |
| 4 | 2 | at MaxCallTimeout expiration, TLM has to set RemStartFai | `expiration`、`false`、`maxcalltimeout`、`remstartfail`、`set`、`tlm` | — | 已覆蓋 |
| 5 | 1 | the ignition working condition passes to "Ignition Pre O | `condition`、`pass`、`pre`、`work` | — | 已覆蓋 |
| 5 | 2 | to "Ignition Off"THENTLM has to pass in Timed state star | `counter.`、`maxcalltimeout`、`pas`、`start`、`state`、`thentlm` | `counter.`、`pas`、`thentlm` | **部分未覆蓋** |
| 6 | 1 | to stay in Timed state until Phone_Call.Info passes to " | `not_active`、`pass`、`phone_call.info`、`state`、`stay`、`tim` | — | 已覆蓋 |
| 6 | 2 | at maximum until MaxCallTimeout expires. | `expires.`、`maxcalltimeout`、`maximum` | `expires.`、`maximum` | **部分未覆蓋** |

**合計分支 46，未覆蓋 **31**。**

## 批次 `batch_003_power_state_a`

### `SWE-PM-011` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | If the CarPlay Device does not request audio control | `audio`、`carplay`、`device`、`doe`、`request` | `doe` | **部分未覆蓋** |
| 1 | 2 | video control | `video` | — | 已覆蓋 |

### `SWE-PM-014` —— 分支 14

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | IF LTM_OperationalModeSts.Info is equal to "Ignition Pre | `equal`、`ltm_operationalmodests.info`、`pre` | `equal` | **部分未覆蓋** |
| 1 | 2 | to "Ignition Off", TLM has to set RemStartFail = "True | `remstartfail`、`set`、`tlm`、`true` | — | 已覆蓋 |
| 2 | 1 | it passes to TLM Timed state.In this case, TLM has to st | `becom`、`case`、`equal`、`not_active`、`pass`、`phone_call.info` | `case`、`equal`、`state.in`、`thi` | **部分未覆蓋** |
| 2 | 2 | at maximum until MaxCallTimeout expiration | `expiration`、`maxcalltimeout`、`maximum` | `expiration`、`maxcalltimeout`、`maximum` | **未覆蓋** |
| 3 | 1 | “Phone call management in Timed state” .ELSE IF LTM_Oper | `call`、`else`、`equal`、`ltm_operationalmodests.info`、`management`、`phone` | `else`、`equal`、`management`、`phone` | **部分未覆蓋** |
| 3 | 2 | to "Ignition Off | — | — | 無獨有實詞 —— 不判 |
| 4 | 1 | signal LTM_OperationalModeSts.Info has a transition to " | `ltm_operationalmodests.info`、`pre`、`signal`、`transition` | — | 已覆蓋 |
| 4 | 2 | to "Ignition Off" valueAND STATUS_BH_BCM2.RemStActvSts i | `active`、`equal`、`remote`、`start`、`status_bh_bcm2.remstactvst`、`valueand` | `equal`、`valueand` | **部分未覆蓋** |
| 5 | 1 | SwitchOff_Timeout_Setting.Req == Timeout1 == 00 MIN | `switchoff_timeout_setting.req` | — | 已覆蓋 |
| 5 | 2 | If Auto_SwitchOn_Setting.Req =="Active", when  Timeout1  | `active`、`auto_switchon_setting.req`、`high`、`ltm`、`radio` | — | 已覆蓋 |
| 6 | 1 | In this case, TLM has to stay in this state until Phone_ | `becom`、`case`、`equal`、`not_active`、`phone_call.info`、`state` | `case`、`equal`、`thi` | **部分未覆蓋** |
| 6 | 2 | at maximum until MaxCallTimeout expiration | `expiration`、`maxcalltimeout`、`maximum` | `expiration`、`maxcalltimeout`、`maximum` | **未覆蓋** |
| 7 | 1 | SwitchOff_Timeout_Setting.Req == Timeout1 <> 00 MIN | `switchoff_timeout_setting.req` | — | 已覆蓋 |
| 7 | 2 | If Auto_SwitchOn_Setting.Req =="Not_Active ", when  Time | `auto_switchon_setting.req`、`high`、`ltm`、`not_active`、`radio` | — | 已覆蓋 |

### `SWE-PM-018` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | signal LTM_OperationalModeSts has a transition to "Ignit | `ltm_operationalmodest`、`pre`、`signal`、`transition` | `signal` | **部分未覆蓋** |
| 1 | 2 | to "Ignition Off" valueTHENTLM has to set TLM_Status.Inf | `set`、`tlm_status.info`、`valuethentlm` | `set`、`valuethentlm` | **部分未覆蓋** |

### `SWE-PM-025` —— 分支 4

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | Front_Panel_OnOff.Req has a transition from “Not_Pressed | `activethen`、`ask`、`call`、`front_panel_onoff.req`、`not_press`、`off` | `activethen`、`off`、`order`、`turn`、`value`、`valuethenif` | **部分未覆蓋** |
| 1 | 2 | not (refer to TLM HMI Specification | `hmi`、`refer`、`specification` | `hmi`、`refer`、`specification` | **未覆蓋** |
| 2 | 1 | CLIMATIC_PANEL.Radio_Btn0 has a transition from “Not_Pre | `activethen`、`ask`、`call`、`climatic_panel.radio_btn0`、`not_press`、`off` | `activethen`、`off`、`order`、`turn`、`value`、`valuethenif` | **部分未覆蓋** |
| 2 | 2 | not (refer to TLM HMI Specification | `hmi`、`refer`、`specification` | `hmi`、`refer`、`specification` | **未覆蓋** |

### `SWE-PM-026` —— 分支 4

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | STATUS_BH_BCM1.DriverDoorSts passes to "Open | `status_bh_bcm1.driverdoorst` | — | 已覆蓋 |
| 1 | 2 | STATUS_BH_BCM1.PsngrDoorSts passes to "Open | `status_bh_bcm1.psngrdoorst` | — | 已覆蓋 |
| 2 | 1 | IF PhoneCall.Info == "Active | `active`、`phonecall.info` | — | 已覆蓋 |
| 2 | 2 | IF previous internal state TLM_Status.Info == StandbyTHE | `internal`、`previou`、`standbythen`、`state`、`stay`、`tim` | `standbythen` | **部分未覆蓋** |

### `SWE-PM-028` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | IF SwitchOff_Timeout_Setting.Req == 00 min | `switchoff_timeout_setting.req` | — | 已覆蓋 |
| 1 | 2 | If Auto_SwitchOn_Setting.Req =="Active ", when  Timeout1 | `active`、`auto_switchon_setting.req`、`high`、`ltm`、`radio`、`timeout1` | — | 已覆蓋 |

### `SWE-PM-030` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | IF Auto_SwitchOn_Setting.Req == Active | `active` | — | 已覆蓋 |
| 1 | 2 | IF Auto_SwitchOn_Setting.Req == Recall_Last | `recall_last` | — | 已覆蓋 |

### `SWE-PM-031` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | IF Rear_View_Camera PROXI parameter == "Present", accord | `accord`、`parameter`、`present`、`proxi`、`rear_camera_enable.info`、`rear_view_camera` | `accord`、`parameter`、`proxi`、`show`、`value` | **部分未覆蓋** |
| 1 | 2 | not rear view camera images regardless of TLM_Status.Inf | `camera`、`imag`、`rear`、`regardles`、`tlm_status.info`、`view` | — | 已覆蓋 |

**合計分支 32，未覆蓋 **16**。**

## 批次 `batch_004_power_state_b`

### `SWE-PM-033` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | signal LTM_OperationalModeSts has a transition to "Ignit | `ltm_operationalmodest`、`pre`、`signal`、`transition` | `signal` | **部分未覆蓋** |
| 1 | 2 | to "Ignition Off" valueTHEN | `valuethen` | `valuethen` | **未覆蓋** |

### `SWE-PM-039` —— 分支 4

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | TLM has to behave as an Ignition Pre Off | `behave`、`pre`、`tlm` | `behave` | **部分未覆蓋** |
| 1 | 2 | Ignition Off event occurs, according to par | `accord`、`event`、`occur`、`par` | `accord`、`occur`、`par` | **部分未覆蓋** |
| 2 | 1 | SwitchOff_Timeout_Setting.Req was equal to "00 min | `equal`、`min`、`switchoff_timeout_setting.req` | — | 已覆蓋 |
| 2 | 2 | Auto_SwitchOn_Setting.Req == Active for LTM High Radio | `active`、`auto_switchon_setting.req`、`high`、`ltm`、`radio` | — | 已覆蓋 |

### `SWE-PM-045` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | to stay in the original state (Standby | `original`、`standby`、`state`、`stay` | — | 已覆蓋 |
| 1 | 2 | Sleep), showing proper HMI Antitheft screens if needed,  | `antitheft`、`equal`、`hmi`、`maximum`、`need`、`proper` | `equal`、`maximum`、`need`、`show`、`time` | **部分未覆蓋** |

### `SWE-PM-046` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | Rear_Camera_Enable.Info == "True" THENeven IF Antitheft_ | `antitheft_result.info`、`equal`、`in_progres`、`rear_camera_enable.info`、`theneven`、`true` | `equal`、`theneven` | **部分未覆蓋** |
| 1 | 2 | Not_Successfully", TLM shall provide audio | `audio`、`not_successfully`、`provide`、`tlm` | `provide` | **部分未覆蓋** |

### `SWE-PM-047` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | to stay in the original state (Standby | `original`、`standby`、`state`、`stay` | — | 已覆蓋 |
| 1 | 2 | Sleep),  showing proper HMI Antitheft screens, if needed | `antitheft`、`hmi`、`need`、`proper`、`screen`、`see` | `see`、`vf210` | **部分未覆蓋** |

**合計分支 12，未覆蓋 **8**。**

## 批次 `batch_005_startup_display`

### `SWE-PM-069` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | the HU display is on the phone main screen | `display`、`hu`、`main`、`screen` | — | 已覆蓋 |
| 1 | 2 | phone projection call UI | `call`、`projection`、`ui` | — | 已覆蓋 |

### `SWE-PM-074` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | If there is a FOTA update available for the Radio, TBM | `available`、`fota`、`radio`、`tbm`、`update` | — | 已覆蓋 |
| 1 | 2 | ROV (see CFTS057) when the vehicle enters Body OFF mode | `body`、`cfts057`、`enter`、`mode`、`off`、`rov` | `cfts057`、`see` | **部分未覆蓋** |

### `SWE-PM-093` —— 分支 26

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | While HU is in SLEEP MODE, STANDBY MODE | `hu`、`sleep`、`standby` | — | 已覆蓋 |
| 1 | 2 | in PARTIAL OPERATION MODE | `operation`、`partial` | — | 已覆蓋 |
| 2 | 1 | If driver door is not present | `present` | — | 已覆蓋 |
| 2 | 2 | removed for current vehicle ($DriverDoorOnOffSts$ = [DOO | `current`、`door_off`、`driverdooronoffsts$`、`remov`、`vehicle` | — | 已覆蓋 |
| 2 | 3 | if HU changes mode (due to ignition event | `chang`、`event`、`ignition` | — | 已覆蓋 |
| 2 | 4 | to due to HU power mode status change to BODY ON | `body`、`change`、`power` | — | 已覆蓋 |
| 2 | 5 | to TIMED MODE while driver door ajar status ($Door_Ajar_ | `ajar`、`animation`、`door_ajar_status$`、`open`、`skip`、`start-up` | `ajar` | **部分未覆蓋** |
| 3 | 1 | HU changes mode (due to ignition event | `due` | `due` | **未覆蓋** |
| 3 | 2 | to HU power mode status changes to BODY ON | `body`、`power`、`statu` | — | 已覆蓋 |
| 3 | 3 | to TIMED MODE | `tim` | — | 已覆蓋 |
| 3 | 4 | if an ignition crank event ($PowerMode$ = [IGN_START ] | `crank`、`ign_start`、`powermode$` | — | 已覆蓋 |
| 4 | 1 | Once a start-up animation is played, HU shall not play t | `cycle`、`hu`、`next`、`once`、`wakeup` | `once` | **部分未覆蓋** |
| 4 | 2 | at least 30 minutes passed from last time the start-up a | `greater`、`last`、`least`、`minut`、`pass`、`time` | `last`、`least`、`pass` | **部分未覆蓋** |
| 5 | 1 | While HU is in SLEEP MODE, STANDBY MODE | `hu`、`sleep`、`standby` | — | 已覆蓋 |
| 5 | 2 | in PARTIAL OPERATION MODE | `operation`、`partial` | — | 已覆蓋 |
| 6 | 1 | If driver door is not present | `present` | — | 已覆蓋 |
| 6 | 2 | removed for current vehicle ($DriverDoorOnOffSts$ = [DOO | `current`、`door_off`、`driverdooronoffsts$`、`remov`、`vehicle` | — | 已覆蓋 |
| 6 | 3 | if HU changes mode (due to ignition event | `chang`、`event`、`ignition` | — | 已覆蓋 |
| 6 | 4 | to due to HU power mode status change to BODY ON | `body`、`change`、`power` | — | 已覆蓋 |
| 6 | 5 | to TIMED MODE while driver door ajar status ($Door_Ajar_ | `ajar`、`animation`、`door_ajar_status$`、`open`、`skip`、`start-up` | `ajar` | **部分未覆蓋** |
| 7 | 1 | HU changes mode (due to ignition event | `due` | `due` | **未覆蓋** |
| 7 | 2 | to HU power mode status changes to BODY ON | `body`、`power`、`statu` | — | 已覆蓋 |
| 7 | 3 | to TIMED MODE | `tim` | — | 已覆蓋 |
| 7 | 4 | if an ignition crank event ($PowerMode$ = [IGN_START ] | `crank`、`ign_start`、`powermode$` | — | 已覆蓋 |
| 8 | 1 | Once a start-up animation is played, HU shall not play t | `cycle`、`hu`、`next`、`once`、`wakeup` | `once` | **部分未覆蓋** |
| 8 | 2 | at least 30 minutes passed from last time the start-up a | `greater`、`last`、`least`、`minut`、`pass`、`time` | `last`、`least`、`pass` | **部分未覆蓋** |

### `SWE-PM-099` —— 分支 3

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | including manual time adjustments from the user, the tim | `includ`、`manual`、`midnight`、`pass`、`user` | `includ`、`user` | **部分未覆蓋** |
| 1 | 2 | automatic adjustments due to time zones | `automatic`、`due`、`zon` | — | 已覆蓋 |
| 1 | 3 | Daylight Savings Time | `daylight`、`saving` | — | 已覆蓋 |

### `SWE-PM-104` —— 分支 5

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | disclaimer screen shall be shown the first time each bus | `bus`、`cycle`、`disclaimer`、`first`、`hu`、`screen` | — | 已覆蓋 |
| 1 | 2 | Full Operation modes. | `full`、`modes.`、`operation` | `modes.` | **部分未覆蓋** |
| 2 | 1 | If the disclaimer screen needs to be shown it shall be s | `bus`、`cycle`、`disclaimer`、`first`、`hu`、`idle` | — | 已覆蓋 |
| 2 | 2 | Partial Operation to Timed | `partial`、`tim` | — | 已覆蓋 |
| 2 | 3 | Full Operation modes | `full`、`mod` | `mod` | **部分未覆蓋** |

### `SWE-PM-105` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | FOTA pop ups, but must be displayed at the next transiti | `but`、`display`、`fota`、`next`、`pop`、`tim` | `but`、`ups` | **部分未覆蓋** |
| 1 | 2 | Full Operation modes during that bus cycle | `bus`、`cycle`、`dur`、`full`、`mod`、`operation` | `dur`、`mod` | **部分未覆蓋** |

### `SWE-PM-110` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | $TBM_Present$ = [Not Present] | `present`、`tbm_present$` | — | 已覆蓋 |
| 1 | 2 | $Country_Code$ is not marked as "Countries which need th | `combin`、`configuration`、`countri`、`country_code$`、`flow`、`follow` | — | 已覆蓋 |

### `SWE-PM-111` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | $TBM_Present$ = [Not Present] | `present`、`tbm_present$` | — | 已覆蓋 |
| 1 | 2 | $Country_Code$  does not require SOS | `country_code$`、`doe`、`require`、`sos` | — | 已覆蓋 |

### `SWE-PM-113` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | See HMI for different statup conditions to determine whe | `condition`、`determine`、`different`、`hmi`、`pop-up`、`see` | `condition`、`determine`、`different`、`hmi`、`see`、`statup` | **部分未覆蓋** |
| 1 | 2 | add geolocation | — | — | 無獨有實詞 —— 不判 |

**合計分支 46，未覆蓋 **15**。**

## 批次 `batch_006_branding_theme`

### `SWE-PM-078` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | If $VC_SpecialPKG$ = [none] | `none`、`vc_specialpkg$` | — | 已覆蓋 |
| 1 | 2 | indicates a value that is not supported by the HU, the d | `bas`、`default`、`hu`、`indicat`、`signal`、`support` | `indicat` | **部分未覆蓋** |

**合計分支 2，未覆蓋 **1**。**
