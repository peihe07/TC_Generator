# B4 —— `axis` 映射提案之複核素材（R-P262(a)）

> **本檔不作判定、不作摘要，逐字呈現。**
> 三大群各抽 ≥ 16.7%，種子 `random.Random(38)`。

| 群 | 母體 | 抽樣 | 率 |
|---|---|---|---|
| `input_data` | 92 | **16** | 17.4% |
| `trigger_state` | 68 | **12** | 17.6% |
| `mode` | 42 | **8** | 19.0% |

---

## 群 `input_data`（16 條）

複核之問題：**該 TC 與其對照姊妹之區分軸，是否確為本群之軸？**

### 1 / 16 —— `NR1L-PowerManagement-018`（`SWE-PM-057`）

**`tc_title`**：Timeout1 options follow PROXI "Switch_Off_Time" set to 20 minutes

**執行層之依據**：對照 `019`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-019`**：Timeout1 options follow PROXI "Switch_Off_Time" set to 60 minutes

**四欄 token 差（逐字）**：
```
20 60
```

**`pre_conditions`**

本條：
```
1. An LTM High Radio is absent from the bench configuration
2. The PROXI parameter "Switch_Off_Time" is at 20 minutes
3. The TLM is in Full-Operation status
```

對照：
```
1. An LTM High Radio is absent from the bench configuration
2. The PROXI parameter "Switch_Off_Time" is at 60 minutes
3. The TLM is in Full-Operation status
```

**`expected_result`**

本條：
```
1. The timeout setting entry is shown in the TLM menu
2. The offered values are "00 min" and "20 min" and no other value is offered
3. Timeout1 reads "00 min" after the first selection and "20 minutes" after the second
```

對照：
```
1. The timeout setting entry is shown in the TLM menu
2. The offered values are "00 min" and "60 min" and no other value is offered
3. Timeout1 reads "00 min" after the first selection and "60 minutes" after the second
```


### 2 / 16 —— `NR1L-PowerManagement-021`（`SWE-PM-060`）

**`tc_title`**：LTM or ETM Radio offers one timeout parameter

**執行層之依據**：對照 `022`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-022`**：Radio other than LTM or ETM offers two timeout parameters

**四欄 token 差（逐字）**：
```
A An ETM absent are both one only or other parameter than
```

**`pre_conditions`**

本條：
```
1. An LTM Radio is present in the bench configuration
2. The TLM is in Full-Operation status
```

對照：
```
1. A Radio other than LTM or ETM is present in the bench configuration
2. The TLM is in Full-Operation status
```

**`test_procedure`**

本條：
```
1. Open the timeout setting entry in the TLM menu
2. Read the parameters offered for user selection to check that only one is present
```

對照：
```
1. Open the timeout setting entry in the TLM menu
2. Read the parameters offered for user selection to check that both are present
```

**`expected_result`**

本條：
```
1. The timeout setting entry is shown in the TLM menu
2. Auto_SwitchOn_Setting.Req is the only parameter offered and SwitchOff_Timeout_Setting.Req is absent
```

對照：
```
1. The timeout setting entry is shown in the TLM menu
2. SwitchOff_Timeout_Setting.Req and Auto_SwitchOn_Setting.Req are both offered for selection
```


### 3 / 16 —— `NR1L-PowerManagement-038`（`SWE-PM-038`）

**`tc_title`**：Case 3: call already ended at Timeout1 expiry

**執行層之依據**：對照 `039`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-039`**：Case 3 with RemStartFail cleared at Timeout1 expiry

**四欄 token 差（逐字）**：
```
4 False RemStartFail True
```

**`pre_conditions`**

本條：
```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. Phone_Call.Info is at "Not_Active"
```

對照：
```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. RemStartFail is at "True"
4. Phone_Call.Info is at "Not_Active"
```

**`test_procedure`**

本條：
```
1. Let Timeout1 run to its expiration with no call active
2. Read TLM_Status.Info and the TLM state to check the transition to Standby
```

對照：
```
1. Let Timeout1 run to its expiration with no call active
2. Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby
```

**`expected_result`**

本條：
```
1. No call is active when Timeout1 expires
2. TLM_Status.Info reads "Standby" and the TLM is in Standby state
```

對照：
```
1. No call is active when Timeout1 expires
2. RemStartFail reads "False", TLM_Status.Info reads "Standby" and the TLM is in Standby state
```


### 4 / 16 —— `NR1L-PowerManagement-053`（`SWE-PM-013`）

**`tc_title`**：Remote Start Active reports Partial_Operation in Ignition Pre_Start

**執行層之依據**：對照 `052`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-052`**：Remote Start Active reports Partial_Operation

**四欄 token 差（逐字）**：
```
On Pre_Start
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. The ignition working condition is Ignition Pre_Start
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The ignition working condition is Ignition On
```


### 5 / 16 —— `NR1L-PowerManagement-160`（`SWE-PM-059`）

**`tc_title`**：A network sleep request in Standby passes the TLM to Sleep

**執行層之依據**：對照 `161`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-161`**：A network sleep request during boot is served only after the boot ends

**四欄 token 差（逐字）**：
```
after at been before behavior completed end ended for has not only passes passing resulting wait waits
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
3. The boot of the TLM has been completed
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
3. The boot of the TLM is not ended
```

**`test_procedure`**

本條：
```
1. Send the request listed in Input Test Data
2. Read the TLM state and the shutdown counter to check the resulting behavior
```

對照：
```
1. Send the request listed in Input Test Data
2. Read the TLM state and the shutdown counter at the end of the boot to check the wait
```

**`expected_result`**

本條：
```
1. TLM_Status.Info and $Telematic_Power$ read "Sleep" and the TLM passes to Sleep state
2. Shutdown_Time starts
```

對照：
```
1. The TLM waits for the end of the boot before passing to Sleep state
2. Shutdown_Time starts only after the end of the boot
```


### 6 / 16 —— `NR1L-PowerManagement-163`（`SWE-PM-066`）

**`tc_title`**：An Assist call is treated as a phone call becoming active

**執行層之依據**：對照 `162`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-162`**：An SOS call is treated as a phone call becoming active

**四欄 token 差（逐字）**：
```
Assist SOS
```

**`input_test_data`**

本條：
```
An Assist call is placed
```

對照：
```
An SOS call is placed
```


### 7 / 16 —— `NR1L-PowerManagement-167`（`SWE-PM-069`）

**`tc_title`**：The HU returns to IDLE when the call ends on the phone projection call UI

**執行層之依據**：對照 `166`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-166`**：The HU returns to IDLE when the call ends on the phone main screen

**四欄 token 差（逐字）**：
```
UI main projection screen
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The display is on the phone projection call UI
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The display is on the phone main screen
```


### 8 / 16 —— `NR1L-PowerManagement-169`（`SWE-PM-074`）

**`tc_title`**：A Radio FOTA update at Body OFF brings the HU to Timed for the pop-up

**執行層之依據**：對照 `170`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-170`**：A TBM FOTA update at Body OFF brings the HU to Timed for the pop-up

**四欄 token 差（逐字）**：
```
Radio TBM
```

**`input_test_data`**

本條：
```
A FOTA update available for the Radio
```

對照：
```
A FOTA update available for the TBM
```


### 9 / 16 —— `NR1L-PowerManagement-191`（`SWE-PM-099`）

**`tc_title`**：The once a day setting plays the startup sound on the first startup of the day

**執行層之依據**：對照 `193`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-193`**：Passing midnight allows the startup sound to play again

**四欄 token 差（逐字）**：
```
Bring Let accompaniment again against already at begins clock for granted midnight new not pass plays same through time whether yet
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. $Themed_Sound$ reads "Fiat Latam"
3. The "Welcome Onboard Sound" setting reads "Once a Day"
4. The HU has not yet played the startup sound that day
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. $Themed_Sound$ reads "Fiat Latam"
3. The "Welcome Onboard Sound" setting reads "Once a Day"
4. The HU has already played the startup sound that day
```

**`test_procedure`**

本條：
```
1. Bring the HU through a startup that plays the animation
2. Read the audio output against the animation start to check the accompaniment
```

對照：
```
1. Let the clock pass midnight and start the HU again
2. Read the audio output to check whether a new day is granted
```

**`expected_result`**

本條：
```
1. The HU startup animation is played
2. A startup sound accompanies the animation and begins at the same time
```

對照：
```
1. The HU startup animation is played
2. A startup sound accompanies the animation for the new day
```


### 10 / 16 —— `NR1L-PowerManagement-192`（`SWE-PM-099`）

**`tc_title`**：A change of the customer selected date allows the sound to play again

**執行層之依據**：對照 `194`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-194`**：An automatic time zone adjustment allows the startup sound to play again

**四欄 token 差（逐字）**：
```
An Daylight Savings Time automatic changes customer date due manual or selected zones
```

**`input_test_data`**

本條：
```
A manual time adjustment that changes the customer selected date
```

對照：
```
An automatic adjustment due to time zones or Daylight Savings Time
```


### 11 / 16 —— `NR1L-PowerManagement-198`（`SWE-PM-101`）

**`tc_title`**：SDARS present without audio brand adds the Sirius logo

**執行層之依據**：對照 `199`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-199`**：SDARS present with beats brand white adds both logos

**四欄 token 差（逐字）**：
```
Audio Beats Both No White are
```

**`input_test_data`**

本條：
```
Audio_Brand: "No Audio Brand"
```

對照：
```
Audio_Brand: "Beats Brand White"
```

**`expected_result`**

本條：
```
1. The brand logo screen is presented
2. The Sirius logo is shown in addition to the vehicle brand logo
```

對照：
```
1. The brand logo screen is presented
2. Both the Sirius and the Beats logos are shown in addition to the vehicle brand logo
```


### 12 / 16 —— `NR1L-PowerManagement-237`（`SWE-PM-081`）

**`tc_title`**：The Chrysler brand selects the Chrysler font

**執行層之依據**：對照 `238`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-238`**：The Jeep brand selects the Jeep font

**四欄 token 差（逐字）**：
```
Chrysler Jeep
```

**`input_test_data`**

本條：
```
$VC_VEH_BRAND$: "Chrysler"
```

對照：
```
$VC_VEH_BRAND$: "Jeep"
```

**`expected_result`**

本條：
```
1. The HU accepts the signal value
2. The HU displays the Chrysler font
```

對照：
```
1. The HU accepts the signal value
2. The HU displays the Jeep font
```


### 13 / 16 —— `NR1L-PowerManagement-239`（`SWE-PM-081`）

**`tc_title`**：The Fiat brand selects the default Fiat font

**執行層之依據**：對照 `238`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-238`**：The Jeep brand selects the Jeep font

**四欄 token 差（逐字）**：
```
DEFAULT Fiat Jeep as marks specification that
```

**`input_test_data`**

本條：
```
$VC_VEH_BRAND$: "Fiat"
```

對照：
```
$VC_VEH_BRAND$: "Jeep"
```

**`expected_result`**

本條：
```
1. The HU accepts the signal value
2. The HU displays the Fiat font that the specification marks as DEFAULT
```

對照：
```
1. The HU accepts the signal value
2. The HU displays the Jeep font
```


### 14 / 16 —— `NR1L-PowerManagement-243`（`SWE-PM-083`）

**`tc_title`**：The Jeep brand offers the Jeep avatars in the profile screen

**執行層之依據**：對照 `245`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-245`**：The Abarth brand is mapped to the Fiat avatars

**四欄 token 差（逐字）**：
```
Abarth Fiat Jeep an rather than
```

**`input_test_data`**

本條：
```
$VC_VEH_BRAND$: "Jeep"
```

對照：
```
$VC_VEH_BRAND$: "Abarth"
```

**`expected_result`**

本條：
```
1. The HU accepts the signal value
2. The profile screen offers the Jeep avatars
```

對照：
```
1. The HU accepts the signal value
2. The profile screen offers the Fiat avatars rather than an Abarth set
```


### 15 / 16 —— `NR1L-PowerManagement-256`（`SWE-PM-090`）

**`tc_title`**：The auto theme mode follows the day night signal into the night theme

**執行層之依據**：對照 `255`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-255`**：The auto theme mode follows the day night signal into the day theme

**四欄 token 差（逐字）**：
```
Day Night day night
```

**`input_test_data`**

本條：
```
$Day_Night_Mode$: the value indicating night
```

對照：
```
$Day_Night_Mode$: the value indicating day
```

**`expected_result`**

本條：
```
1. The HU accepts the signal value
2. The HU shows the Night theme
```

對照：
```
1. The HU accepts the signal value
2. The HU shows the Day theme
```


### 16 / 16 —— `NR1L-PowerManagement-262`（`SWE-PM-096`）

**`tc_title`**：The season changes to Spring at the September date

**執行層之依據**：對照 `260`，差異為其餘輸入之取值

**對照條 `NR1L-PowerManagement-260`**：The season changes to Fall at the March date

**四欄 token 差（逐字）**：
```
20 23 Fall March September Spring rd th
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. The HU clock is set to the day before the Spring start date
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The HU clock is set to the day before the Fall start date
```

**`input_test_data`**

本條：
```
An Ignition On after the date passes September, 23rd
```

對照：
```
An Ignition On after the date passes March, 20th
```

**`expected_result`**

本條：
```
1. The HU determines the season at Ignition On
2. The HU determines that Spring has started
```

對照：
```
1. The HU determines the season at Ignition On
2. The HU determines that Fall has started
```


---

## 群 `trigger_state`（12 條）

複核之問題：**該 TC 與其對照姊妹之區分軸，是否確為本群之軸？**

### 1 / 12 —— `NR1L-PowerManagement-050`（`SWE-PM-012`）

**`tc_title`**：User settings are restored after a battery reconnection

**執行層之依據**：對照 `051`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req`

**對照條 `NR1L-PowerManagement-051`**：TLM starts from Sleep state after leaving INIT

**四欄 token 差（逐字）**：
```
3 Auto_SwitchOn_Setting.Req Let Reconnect Sleep SwitchOffSetting.Req TLM_Status.Info VPLastStatus an been before being disconnected disconnection error exit from has hold its just known let machine once previous read reads reconnected reported returned settle starting starts stored that their three thresholds values variables voltage within without
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. VPLastStatus, SwitchOffSetting.Req and Auto_SwitchOn_Setting.Req hold known values
3. The battery is disconnected
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The battery has just been reconnected
```

**`test_procedure`**

本條：
```
1. Reconnect the battery and let the voltage settle within its thresholds
2. Read the three stored variables to check that their previous values returned
```

對照：
```
1. Let the TLM exit INIT state
2. Read TLM_Status.Info and the state machine to check the starting state
```

**`expected_result`**

本條：
```
1. The TLM leaves INIT state once the voltage is within its thresholds
2. VPLastStatus, SwitchOffSetting.Req and Auto_SwitchOn_Setting.Req read their values before the battery disconnection
```

對照：
```
1. The TLM leaves INIT state without an error being reported
2. TLM_Status.Info reads "Sleep" and the TLM starts from Sleep state
```


### 2 / 12 —— `NR1L-PowerManagement-064`（`SWE-PM-014`）

**`tc_title`**：Behaviour 1 reached through Auto_SwitchOn_Setting.Req on LTM High

**執行層之依據**：對照 `060`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req`

**對照條 `NR1L-PowerManagement-060`**：Behaviour 1 with no active call passes the TLM to Standby

**四欄 token 差（逐字）**：
```
4 Active An Auto_SwitchOn_Setting.Req High LTM Radio SwitchOff_Timeout_Setting.Req bench configuration in present
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. An LTM High Radio is present in the bench configuration
3. Auto_SwitchOn_Setting.Req reads "Active" and Timeout1 reads "00 MIN"
4. Phone_Call.Info reads "Not_Active"
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req and Timeout1 read "00 MIN"
3. Phone_Call.Info reads "Not_Active"
```


### 3 / 12 —— `NR1L-PowerManagement-070`（`SWE-PM-015`）

**`tc_title`**：CLIMATIC_PANEL.Radio_Btn0 press with the rear camera not active passes the TLM to Idle

**執行層之依據**：對照 `069`，差異落在觸發訊號：`Front_Panel_OnOff.Req`

**對照條 `NR1L-PowerManagement-069`**：Front_Panel_OnOff.Req press with the rear camera not active passes the TLM to Idle

**四欄 token 差（逐字）**：
```
CLIMATIC_PANEL.Radio_Btn0 Front_Panel_OnOff.Req
```

**`test_procedure`**

本條：
```
1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed"
2. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition to Idle
```

對照：
```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition to Idle
```


### 4 / 12 —— `NR1L-PowerManagement-096`（`SWE-PM-026`）

**`tc_title`**：Door open with Standby as the previous state keeps the TLM in Timed

**執行層之依據**：對照 `095`，差異落在觸發訊號：`PhoneCall.Info`

**對照條 `NR1L-PowerManagement-095`**：Door open with an active call keeps the TLM in Timed

**四欄 token 差（逐字）**：
```
Active PhoneCall.Info STATUS_BH_BCM1.DriverDoorSts STATUS_BH_BCM1.PsngrDoorSts Standby internal previous was
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable"
4. The previous internal state was Standby
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable"
4. PhoneCall.Info reads "Active"
```

**`input_test_data`**

本條：
```
STATUS_BH_BCM1.DriverDoorSts = "Open"
```

對照：
```
STATUS_BH_BCM1.PsngrDoorSts = "Open"
```


### 5 / 12 —— `NR1L-PowerManagement-100`（`SWE-PM-028`）

**`tc_title`**：Antitheft success clears the activation request

**執行層之依據**：對照 `102`，差異落在觸發訊號：`$Telematic_Power$`

**對照條 `NR1L-PowerManagement-102`**：Antitheft success passes the TLM to Timed state

**四欄 token 差（逐字）**：
```
$Telematic_Power$ False TLM_Status.Info Timed back it passes read set state that transition
```

**`test_procedure`**

本條：
```
1. Send the signal listed in Input Test Data
2. Read Antitheft_Activation.Req to check that it is set back
```

對照：
```
1. Send the signal listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Timed
```

**`expected_result`**

本條：
```
1. The TLM accepts the signal without a bus error
2. Antitheft_Activation.Req reads "False"
```

對照：
```
1. The TLM accepts the signal without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the TLM passes to TLM Timed state
```


### 6 / 12 —— `NR1L-PowerManagement-101`（`SWE-PM-028`）

**`tc_title`**：Antitheft success with a zero timeout takes Timeout1 from PROXI

**執行層之依據**：對照 `103`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req`

**對照條 `NR1L-PowerManagement-103`**：Antitheft success on LTM High takes Timeout1 from PROXI

**四欄 token 差（逐字）**：
```
4 Active An Auto_SwitchOn_Setting.Req High LTM MIN Radio SwitchOff_Timeout_Setting.Req bench configuration min present
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req reads "00 min"
3. Switch_Off_Time reads 20 minutes
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. An LTM High Radio is present in the bench configuration
3. Auto_SwitchOn_Setting.Req reads "Active " and Timeout1 reads "00 MIN"
4. Switch_Off_Time reads 20 minutes
```


### 7 / 12 —— `NR1L-PowerManagement-115`（`SWE-PM-035`）

**`tc_title`**：Antitheft success with auto switch on active passes the TLM to Full-Operation

**執行層之依據**：對照 `117`，差異落在觸發訊號：`Antitheft_Activation.Req`

**對照條 `NR1L-PowerManagement-117`**：Antitheft success with recall last and last status on passes the TLM to Full-Operation

**四欄 token 差（逐字）**：
```
3 Active Antitheft_Activation.Req False Recall_Last a antitheft request
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Active"
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Recall_Last"
3. VPLastStatus reads "On"
```

**`test_procedure`**

本條：
```
1. Send the value listed in Input Test Data
2. Read the antitheft request, the screen and the TLM state to check the resulting behavior
```

對照：
```
1. Send the value listed in Input Test Data
2. Read the screen and the TLM state to check the resulting behavior
```

**`expected_result`**

本條：
```
1. Antitheft_Activation.Req reads "False" and a proper Splash Screen is shown for Response_Wait_Time
2. VPLastStatus reads "On" and TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```

對照：
```
1. A proper Splash Screen is shown for Response_Wait_Time
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```


### 8 / 12 —— `NR1L-PowerManagement-123`（`SWE-PM-039`）

**`tc_title`**：Auto switch on active on LTM High Radio loads Timeout1 from the PROXI value

**執行層之依據**：對照 `122`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req`

**對照條 `NR1L-PowerManagement-122`**：A zero switch off timeout loads Timeout1 from the PROXI value

**四欄 token 差（逐字）**：
```
00 3 Active Auto_SwitchOn_Setting.Req High LTM Radio SwitchOff_Timeout_Setting.Req an min unit
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info was equal to "Full-Operation"
3. The unit is an LTM High Radio
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info was equal to "Full-Operation"
```

**`input_test_data`**

本條：
```
Auto_SwitchOn_Setting.Req: "Active"
```

對照：
```
SwitchOff_Timeout_Setting.Req: "00 min"
```


### 9 / 12 —— `NR1L-PowerManagement-184`（`SWE-PM-093`）

**`tc_title`**：A mode change to TIMED MODE cancels a start-up animation in progress

**執行層之依據**：對照 `183`，差異落在觸發訊號：`$PowerMode$`

**對照條 `NR1L-PowerManagement-183`**：An ignition crank event cancels a start-up animation in progress

**四欄 token 差（逐字）**：
```
$PowerMode$ An IGN_START MODE TIMED change status value
```

**`input_test_data`**

本條：
```
An HU power mode status change to TIMED MODE
```

對照：
```
$PowerMode$: "IGN_START"
```

**`test_procedure`**

本條：
```
1. Send the change listed in Input Test Data during the animation
2. Read the screen and the power mode to check the cancellation
```

對照：
```
1. Send the value listed in Input Test Data during the animation
2. Read the screen and the power mode to check the cancellation
```


### 10 / 12 —— `NR1L-PowerManagement-236`（`SWE-PM-080`）

**`tc_title`**：A theme change updates the sent value within the send window

**執行層之依據**：對照 `235`，差異落在觸發訊號：`$VC_SpecialPKG$`

**對照條 `NR1L-PowerManagement-235`**：The theme special package value is sent while the CAN network is awake

**四欄 token 差（逐字）**：
```
$VC_SpecialPKG$ Data Input NA Observe Send Test Tsend a against associated bus change different its listed mapped new of package second special stays that timing traffic update while with within
```

**`input_test_data`**

本條：
```
$VC_SpecialPKG$: a second value mapped to a different theme
```

對照：
```
NA
```

**`test_procedure`**

本條：
```
1. Send the value listed in Input Test Data
2. Read $Radio_Theme$ and its timing to check the update
```

對照：
```
1. Observe the bus traffic while the CAN network stays awake
2. Read $Radio_Theme$ against the applied theme to check the sent value
```

**`expected_result`**

本條：
```
1. The HU sends the new $Radio_Theme$ value
2. The new value is sent within Tsend of the theme change
```

對照：
```
1. The HU sends $Radio_Theme$ on the bus
2. The value sent in $Radio_Theme$ is the special package value associated with that theme
```


### 11 / 12 —— `NR1L-PowerManagement-246`（`SWE-PM-084`）

**`tc_title`**：The recirc icon follows the PROXI parameters on the Atlantis architecture

**執行層之依據**：對照 `247`，差異落在觸發訊號：`$Car_Shape_Configuration$`

**對照條 `NR1L-PowerManagement-247`**：The recirc icon follows the body style signal on the PowerNet architecture

**四欄 token 差（逐字）**：
```
$Car_Shape_Configuration$ $Number_of_Doors$ $VC_BODY_STYLE$ Atlantis CUSW PNET PROXI body car or parameters shape signal style
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. The HU runs the CUSW or Atlantis architecture
3. The climate screen showing the recirc icon is reachable
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The HU runs the PNET architecture
3. The climate screen showing the recirc icon is reachable
```

**`input_test_data`**

本條：
```
$VC_VEH_LINE$ with the $Car_Shape_Configuration$ and $Number_of_Doors$ PROXI parameters
```

對照：
```
$VC_VEH_LINE$ with the $VC_BODY_STYLE$ signal
```

**`expected_result`**

本條：
```
1. The HU accepts the configuration
2. The recirc icon matches the assignment for that vehicle line and car shape
```

對照：
```
1. The HU accepts the configuration
2. The recirc icon matches the assignment for that vehicle line and body style
```


### 12 / 12 —— `NR1L-PowerManagement-251`（`SWE-PM-086`）

**`tc_title`**：A theme change on this chapter updates the sent value within the send window

**執行層之依據**：對照 `250`，差異落在觸發訊號：`$VC_SpecialPKG$`

**對照條 `NR1L-PowerManagement-250`**：The theme special package value is sent on this chapter while the network is awake

**四欄 token 差（逐字）**：
```
$VC_SpecialPKG$ Data Input NA Observe Send Test Tsend a against associated bus change different its listed mapped new of package second special stays that timing traffic update while with within
```

**`input_test_data`**

本條：
```
$VC_SpecialPKG$: a second value mapped to a different theme
```

對照：
```
NA
```

**`test_procedure`**

本條：
```
1. Send the value listed in Input Test Data
2. Read $Radio_Theme$ and its timing to check the update
```

對照：
```
1. Observe the bus traffic while the CAN network stays awake
2. Read $Radio_Theme$ against the applied theme to check the sent value
```

**`expected_result`**

本條：
```
1. The HU sends the new $Radio_Theme$ value
2. The new value is sent within Tsend of the theme change
```

對照：
```
1. The HU sends $Radio_Theme$ on the bus
2. The value sent in $Radio_Theme$ is the special package value associated with that theme
```


---

## 群 `mode`（8 條）

複核之問題：**該 TC 與其對照姊妹之區分軸，是否確為本群之軸？**

### 1 / 8 —— `NR1L-PowerManagement-001`（`SWE-PM-071`）

**`tc_title`**：Splash screen shown after SplashScreen_Time on normal boot

**執行層之依據**：對照 `003`，差異落在運作模式／狀態：`Bench`

**對照條 `NR1L-PowerManagement-003`**：No splash screen when TLM passes to Bench

**四欄 token 差（逐字）**：
```
Bench Set Start after any at before elapsed has it loaded no once reaches shown start status target through time
```

**`test_procedure`**

本條：
```
1. Start the suspend-resume boot sequence
2. Read the TLM display before and after SplashScreen_Time to check that the splash screen is loaded
```

對照：
```
1. Set the boot target status to Bench and start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time to check that no splash screen is shown
```

**`expected_result`**

本條：
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen appears before SplashScreen_Time has elapsed, and the splash screen is loaded once it has
```

對照：
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen appears at any time through SplashScreen_Time, and the TLM reaches the Bench boot target
```


### 2 / 8 —— `NR1L-PowerManagement-061`（`SWE-PM-014`）

**`tc_title`**：Behaviour 1 with an active call passes the TLM to Timed

**執行層之依據**：對照 `060`，差異落在運作模式／狀態：`Standby`

**對照條 `NR1L-PowerManagement-060`**：Behaviour 1 with no active call passes the TLM to Standby

**四欄 token 差（逐字）**：
```
Active Standby Timed becomes goes state stays there until
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req and Timeout1 read "00 MIN"
3. Phone_Call.Info reads "Active"
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req and Timeout1 read "00 MIN"
3. Phone_Call.Info reads "Not_Active"
```

**`test_procedure`**

本條：
```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Timed
```

對照：
```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```

**`expected_result`**

本條：
```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the TLM stays there until Phone_Call.Info becomes "Not_Active"
```

對照：
```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM goes to TLM Standby state
```


### 3 / 8 —— `NR1L-PowerManagement-137`（`SWE-PM-045`）

**`tc_title`**：A failed antitheft keeps the TLM in the original Sleep state

**執行層之依據**：對照 `136`，差異落在運作模式／狀態：`Sleep`

**對照條 `NR1L-PowerManagement-136`**：A failed antitheft keeps the TLM in the original Standby state

**四欄 token 差（逐字）**：
```
Sleep Standby
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Sleep"
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
```

**`expected_result`**

本條：
```
1. Antitheft_Activation.Req reads "False"
2. The TLM stays in the original Sleep state for at most Timeout1, with proper HMI Antitheft screens
```

對照：
```
1. Antitheft_Activation.Req reads "False"
2. The TLM stays in the original Standby state for at most Timeout1, with proper HMI Antitheft screens
```


### 4 / 8 —— `NR1L-PowerManagement-140`（`SWE-PM-047`）

**`tc_title`**：A failed antitheft keeps the TLM in Standby and shows the antitheft screens

**執行層之依據**：對照 `141`，差異落在運作模式／狀態：`Sleep`

**對照條 `NR1L-PowerManagement-141`**：A failed antitheft keeps the TLM in Sleep and shows the antitheft screens

**四欄 token 差（逐字）**：
```
Sleep Standby
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Sleep"
```

**`expected_result`**

本條：
```
1. Antitheft_Activation.Req reads "False"
2. The TLM stays in the original Standby state and proper HMI Antitheft screens are shown if needed
```

對照：
```
1. Antitheft_Activation.Req reads "False"
2. The TLM stays in the original Sleep state and proper HMI Antitheft screens are shown if needed
```


### 5 / 8 —— `NR1L-PowerManagement-143`（`SWE-PM-048`）

**`tc_title`**：Antitheft success with auto switch on not active reaches Idle after the mode transition

**執行層之依據**：對照 `142`，差異落在運作模式／狀態：`Full-Operation`

**對照條 `NR1L-PowerManagement-142`**：Antitheft success with auto switch on active reaches Full-Operation after the mode transition

**四欄 token 差（逐字）**：
```
Active Full-Operation Idle Not_Active
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Not_Active"
3. The LTM_OperationalModeSts.Info transition has occurred
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Active"
3. The LTM_OperationalModeSts.Info transition has occurred
```

**`expected_result`**

本條：
```
1. Antitheft_Activation.Req reads "False"
2. TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
```

對照：
```
1. Antitheft_Activation.Req reads "False"
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```


### 6 / 8 —— `NR1L-PowerManagement-178`（`SWE-PM-093`）

**`tc_title`**：Closing the driver door in SLEEP MODE plays the start-up animation

**執行層之依據**：對照 `179`，差異落在運作模式／狀態：`SLEEP`

**對照條 `NR1L-PowerManagement-179`**：Closing the driver door in STANDBY MODE plays the start-up animation

**四欄 token 差（逐字）**：
```
SLEEP STANDBY
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. The HU is in SLEEP MODE
3. A driver door is present for the vehicle
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The HU is in STANDBY MODE
3. A driver door is present for the vehicle
```


### 7 / 8 —— `NR1L-PowerManagement-179`（`SWE-PM-093`）

**`tc_title`**：Closing the driver door in STANDBY MODE plays the start-up animation

**執行層之依據**：對照 `178`，差異落在運作模式／狀態：`SLEEP`

**對照條 `NR1L-PowerManagement-178`**：Closing the driver door in SLEEP MODE plays the start-up animation

**四欄 token 差（逐字）**：
```
SLEEP STANDBY
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. The HU is in STANDBY MODE
3. A driver door is present for the vehicle
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The HU is in SLEEP MODE
3. A driver door is present for the vehicle
```


### 8 / 8 —— `NR1L-PowerManagement-180`（`SWE-PM-093`）

**`tc_title`**：Closing the driver door in PARTIAL OPERATION MODE plays the start-up animation

**執行層之依據**：對照 `178`，差異落在運作模式／狀態：`SLEEP`

**對照條 `NR1L-PowerManagement-178`**：Closing the driver door in SLEEP MODE plays the start-up animation

**四欄 token 差（逐字）**：
```
OPERATION PARTIAL SLEEP
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. The HU is in PARTIAL OPERATION MODE
3. A driver door is present for the vehicle
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The HU is in SLEEP MODE
3. A driver door is present for the vehicle
```


---

## 「無對應」40 條之三個選項與其後果（R-P262(b)）

> 其 leaf 僅產出 1 條 TC，無他條可區分；§4.6 之六值皆預設「與他條之區分」。
> **本檔只呈選項與後果，不裁。**

| 選項 | 後果 |
|---|---|
| 新增列舉值（如 `single`） | 須改 §4.6，**屬 canon 層**，影響全部 feature；其利為語義正確、不需犧牲既有契約 |
| 以 `none` 表之 | **與 §4.6 之 `none` ⇔ `duplicate_of` 雙向契約衝突**（G174 之 C4 / C7）—— 該 40 條並非重複，設 `duplicate_of` 即為不實；不設則 C4 觸發 40 次 |
| 留空 | 違反 G168 之 C2（`axis` 非空字串），全批 40 條觸發；且「留空」與「未填」無從分辨 |

**逐條**

| tc | leaf |
|---|---|
| `…-028` | `SWE-PM-063` |
| `…-071` | `SWE-PM-016` |
| `…-072` | `SWE-PM-017` |
| `…-082` | `SWE-PM-021` |
| `…-083` | `SWE-PM-022` |
| `…-084` | `SWE-PM-023` |
| `…-085` | `SWE-PM-024` |
| `…-110` | `SWE-PM-031` |
| `…-111` | `SWE-PM-032` |
| `…-114` | `SWE-PM-034` |
| `…-119` | `SWE-PM-036` |
| `…-120` | `SWE-PM-037` |
| `…-125` | `SWE-PM-040` |
| `…-147` | `SWE-PM-049` |
| `…-148` | `SWE-PM-050` |
| `…-149` | `SWE-PM-051` |
| `…-150` | `SWE-PM-052` |
| `…-151` | `SWE-PM-053` |
| `…-158` | `SWE-PM-056` |
| `…-159` | `SWE-PM-058` |
| `…-164` | `SWE-PM-067` |
| `…-165` | `SWE-PM-068` |
| `…-168` | `SWE-PM-070` |
| `…-187` | `SWE-PM-094` |
| `…-188` | `SWE-PM-095` |
| `…-189` | `SWE-PM-097` |
| `…-190` | `SWE-PM-098` |
| `…-195` | `SWE-PM-100` |
| `…-220` | `SWE-PM-106` |
| `…-221` | `SWE-PM-107` |
| `…-222` | `SWE-PM-108` |
| `…-223` | `SWE-PM-109` |
| `…-228` | `SWE-PM-113` |
| `…-229` | `SWE-PM-114` |
| `…-230` | `SWE-PM-115` |
| `…-231` | `SWE-PM-077` |
| `…-234` | `SWE-PM-079` |
| `…-254` | `SWE-PM-088` |
| `…-257` | `SWE-PM-091` |
| `…-258` | `SWE-PM-092` |
