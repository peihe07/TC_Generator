# B1 —— 第 4 / 8 列之分析層複核素材（R-P252）

> **本檔不作判定、不作摘要，逐字呈現。**
> 第 4 列母體 **79** 條（79 條 = 80 − `…-099`）；抽樣 **14** 條 = **17.7%**，種子 `random.Random(36)`。
> 第 8 列 **7** 條**全取**（其「跨功能」未機械化）。

**抽樣清單**：`…-009`、`…-014`、`…-029`、`…-031`、`…-032`、`…-075`、`…-096`、`…-103`、`…-106`、`…-133`、`…-139`、`…-191`、`…-223`、`…-228`

---

## 一、第 4 列抽樣（14 / 79）

複核之問題：**該 TC 之結果是否確由二個以上條件共同決定？**

### 第 4 列 1 / 14 —— `NR1L-PowerManagement-009`（`SWE-PM-073`）

**`tc_title`**：Battery Critical minimizes draw and keeps ACN active

**`source_clause` 逐字**（全文，未截斷）：
```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

**clause 之條件子句**（`COND_RE` 所命中者，11 處）：
- `When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received b`
- `if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall`
- `If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. U`
- `Under fault condition of missing load shed signals on the CAN bus, the last values of load`
- `If the load shed signals do not recover, the on-going load shed action shall be maintained`
- `While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], t`
- `when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw wh`
- `while keeping only the display on and controls active for HVAC controls, and active phone`
- `if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall`
- `If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the cal`
- `Unless defined otherwise, TLM shall stay in this state until either voltage out of range c`

**`pre_conditions` 逐字**：
```
1. A LIN and CAN simulation tool is connected
2. The TLM is in BODY ON mode
3. Ecall, ACN and chimes modes are inactive
```

**實質前提**（扣除 bench 環境列，2 項）：
- 2. The TLM is in BODY ON mode
- 3. Ecall, ACN and chimes modes are inactive

**`input_test_data` 逐字**：
```
STATUS_LIN.Batt_ST_Crit = [1h]
Starting volume level: 25
```

**`test_procedure` 逐字**：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the Battery Critical signal listed in Input Test Data
3. Read the display, HVAC controls, ACN phone state and AUD_LVL to check the current minimization
```

**`expected_result` 逐字**：
```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts the Battery Critical signal without a bus error
3. The display stays on, HVAC controls and ACN phone stay active, the maximum volume for Ecall, ACN, chimes, beeps and alerts is reduced to 20 and the TLM is muted
```

**執行層所判之「二個以上條件」**：2. The TLM is in BODY ON mode；3. Ecall, ACN and chimes modes are inactive

**現值 `design_method`**：決策表 (Decision Table Testing)

### 第 4 列 2 / 14 —— `NR1L-PowerManagement-014`（`SWE-PM-073`）

**`tc_title`**：Battery Critical minimizes draw in BODY OFF-TIMED mode

**`source_clause` 逐字**（全文，未截斷）：
```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

**clause 之條件子句**（`COND_RE` 所命中者，11 處）：
- `When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received b`
- `if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall`
- `If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. U`
- `Under fault condition of missing load shed signals on the CAN bus, the last values of load`
- `If the load shed signals do not recover, the on-going load shed action shall be maintained`
- `While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], t`
- `when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw wh`
- `while keeping only the display on and controls active for HVAC controls, and active phone`
- `if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall`
- `If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the cal`
- `Unless defined otherwise, TLM shall stay in this state until either voltage out of range c`

**`pre_conditions` 逐字**：
```
1. A LIN and CAN simulation tool is connected
2. The TLM is in BODY OFF-TIMED mode
3. Ecall, ACN and chimes modes are inactive
```

**實質前提**（扣除 bench 環境列，2 項）：
- 2. The TLM is in BODY OFF-TIMED mode
- 3. Ecall, ACN and chimes modes are inactive

**`input_test_data` 逐字**：
```
STATUS_LIN.Batt_ST_Crit = [1h]
Starting volume level: 25
```

**`test_procedure` 逐字**：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the Battery Critical signal listed in Input Test Data
3. Read the display, HVAC controls, ACN phone state and AUD_LVL to check the current minimization
```

**`expected_result` 逐字**：
```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts the Battery Critical signal without a bus error
3. The display stays on, HVAC controls and ACN phone stay active, the maximum volume for Ecall, ACN, chimes, beeps and alerts is reduced to 20 and the TLM is muted
```

**執行層所判之「二個以上條件」**：2. The TLM is in BODY OFF-TIMED mode；3. Ecall, ACN and chimes modes are inactive

**現值 `design_method`**：決策表 (Decision Table Testing)

### 第 4 列 3 / 14 —— `NR1L-PowerManagement-029`（`SWE-PM-064`）

**`tc_title`**：MaxCallTimeout starts on ignition off with Timeout1 at 00 min

**`source_clause` 逐字**（全文，未截斷）：
```
MaxCallTimeout starts in the following two conditions: Timeout1 == 00 min: IF Phone_Call.Info is equal to “Active” in TLM Full-Operation state, AND the Ignition working condition switches to "Ignition Pre Off" OR to "Ignition Off";   Timeout1 <> 00 min: at Timeout1 expiration, only IF Phone_Call.Info is still equal to “Active”;
```

**clause 之條件子句**（`COND_RE` 所命中者，2 處）：
- `IF Phone_Call.Info is equal to “Active” in TLM Full-Operation state, AND the Ignition work`
- `IF Phone_Call.Info is still equal to “Active”;`

**`pre_conditions` 逐字**：
```
1. Timeout1 is at "00 min"
2. The TLM is in Full-Operation state
3. Phone_Call.Info is at "Active"
```

**實質前提**（扣除 bench 環境列，3 項）：
- 1. Timeout1 is at "00 min"
- 2. The TLM is in Full-Operation state
- 3. Phone_Call.Info is at "Active"

**`input_test_data` 逐字**：
```
Ignition working condition: "Ignition Pre Off"
```

**`test_procedure` 逐字**：
```
1. Switch the ignition working condition to the value listed in Input Test Data
2. Read the MaxCallTimeout counter to check that it started
```

**`expected_result` 逐字**：
```
1. The TLM leaves Full-Operation state without dropping the active call
2. The MaxCallTimeout counter is running from the moment of the ignition change
```

**執行層所判之「二個以上條件」**：1. Timeout1 is at "00 min"；2. The TLM is in Full-Operation state；3. Phone_Call.Info is at "Active"

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 4 列 4 / 14 —— `NR1L-PowerManagement-031`（`SWE-PM-065`）

**`tc_title`**：Call ends before Timeout1 expiry: previous source is restored

**`source_clause` 逐字**（全文，未截斷）：
```
Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN TLM has to restore the active source managed by TLM before the call (for example entertainment features like DAB Tuner, rather than USB or BT streaming audio) staying still in Timed state.
In this case, TLM is still able to manage other possible phone calls within Timeout1 expiration.
```

**clause 之條件子句**（`COND_RE` 所命中者，2 處）：
- `IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” e`
- `IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN TLM has to res`

**`pre_conditions` 逐字**：
```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. A DAB Tuner source was active before the call
4. Phone_Call.Info is at "Active"
```

**實質前提**（扣除 bench 環境列，4 項）：
- 1. Timeout1 is at a value other than "00 min"
- 2. The TLM is in Timed state
- 3. A DAB Tuner source was active before the call
- 4. Phone_Call.Info is at "Active"

**`input_test_data` 逐字**：
```
NA
```

**`test_procedure` 逐字**：
```
1. Set Phone_Call.Info to "Not_Active" before Timeout1 expires
2. Read the active audio source and the TLM state to check that the previous source returned
```

**`expected_result` 逐字**：
```
1. Phone_Call.Info reads "Not_Active" before Timeout1 expires
2. The DAB Tuner source is active again and the TLM remains in Timed state
```

**執行層所判之「二個以上條件」**：1. Timeout1 is at a value other than "00 min"；2. The TLM is in Timed state；3. A DAB Tuner source was active before the call；4. Phone_Call.Info is at "Active"

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 4 列 5 / 14 —— `NR1L-PowerManagement-032`（`SWE-PM-065`）

**`tc_title`**：Further calls are still managed within Timeout1

**`source_clause` 逐字**（全文，未截斷）：
```
Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN TLM has to restore the active source managed by TLM before the call (for example entertainment features like DAB Tuner, rather than USB or BT streaming audio) staying still in Timed state.
In this case, TLM is still able to manage other possible phone calls within Timeout1 expiration.
```

**clause 之條件子句**（`COND_RE` 所命中者，2 處）：
- `IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” e`
- `IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN TLM has to res`

**`pre_conditions` 逐字**：
```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. One call has already ended before Timeout1 expiry
```

**實質前提**（扣除 bench 環境列，3 項）：
- 1. Timeout1 is at a value other than "00 min"
- 2. The TLM is in Timed state
- 3. One call has already ended before Timeout1 expiry

**`input_test_data` 逐字**：
```
NA
```

**`test_procedure` 逐字**：
```
1. Place a second bluetooth call while Timeout1 is still running
2. Read the call audio routing and the TLM state to check that the second call is served
```

**`expected_result` 逐字**：
```
1. The second call is connected and is managed by the TLM
2. The TLM remains in Timed state while the second call runs
```

**執行層所判之「二個以上條件」**：1. Timeout1 is at a value other than "00 min"；2. The TLM is in Timed state；3. One call has already ended before Timeout1 expiry

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 4 列 6 / 14 —— `NR1L-PowerManagement-075`（`SWE-PM-019`）

**`tc_title`**：Front_Panel_OnOff.Req press is ignored while the rear camera is enabled

**`source_clause` 逐字**（全文，未截斷）：
```
IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” valueTHEN
IF PROXI parameter Rear_View_Camera == "Present" AND Rear_Camera_Enable.Info == True THEN TLM ignores this transition ELSE
TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization" logics, for Response_Wait_Time AND TLM has to set VPLastStatus to “ON” value and TLM_Status.Info and $Telematic_Power$ to "Full-Operation" value and then it passes to TLM Full-Operation state.
IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal CLIMATIC_PANEL.Radio_Btn0 has a transition from “Not_Pressed” value to “Pressed” valueTHEN
IF PROXI parameter Rear_View_Camera == "Present" AND Rear_Camera_Enable.Info == True THEN TLM ignores this transition ELSE
TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization" logics, for Response_Wait_Time AND TLM has to set VPLastStatus to “ON” value and TLM_Status.Info and $Telematic_Power$ to "Full-Operation" value and then it passes to TLM Full-Operation state.
```

**clause 之條件子句**（`COND_RE` 所命中者，4 處）：
- `IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal Front_Panel_OnOff.Req has a t`
- `IF PROXI parameter Rear_View_Camera == "Present" AND Rear_Camera_Enable.Info == True THEN`
- `IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal CLIMATIC_PANEL.Radio_Btn0 has`
- `IF PROXI parameter Rear_View_Camera == "Present" AND Rear_Camera_Enable.Info == True THEN`

**`pre_conditions` 逐字**：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. Rear_View_Camera reads "Present" and Rear_Camera_Enable.Info reads "True"
```

**實質前提**（扣除 bench 環境列，2 項）：
- 2. TLM_Status.Info and $Telematic_Power$ read "Idle"
- 3. Rear_View_Camera reads "Present" and Rear_Camera_Enable.Info reads "True"

**`input_test_data` 逐字**：
```
NA
```

**`test_procedure` 逐字**：
```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read TLM_Status.Info and the screen to check that the transition is ignored
```

**`expected_result` 逐字**：
```
1. The TLM receives the press transition
2. TLM_Status.Info still reads "Idle" and no Splash Screen is shown
```

**執行層所判之「二個以上條件」**：2. TLM_Status.Info and $Telematic_Power$ read "Idle"；3. Rear_View_Camera reads "Present" and Rear_Camera_Enable.Info reads "True"

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 4 列 7 / 14 —— `NR1L-PowerManagement-096`（`SWE-PM-026`）

**`tc_title`**：Door open with Standby as the previous state keeps the TLM in Timed

**`source_clause` 逐字**（全文，未截斷）：
```
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND proxi parameter Brand_Configuration_2 == "Jeep" AND
AND SWITCH_OFF_DOOR is equal to “enable”
AND (STATUS_BH_BCM1.DriverDoorSts passes to "Open" OR STATUS_BH_BCM1.PsngrDoorSts passes to "Open")
STATUS_BH_BCM1.DriverDoorSts passes to "Open"THEN
IF previous internal state TLM_Status.Info == "Full-Operation" AND PhoneCall.Info == "Not_Active"THEN TLM has to stop its active functionality (Media audio streaming, tuner, etc) and to set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state
IF PhoneCall.Info == "Active"OR IF previous internal state TLM_Status.Info == StandbyTHEN TLM shall stay in Timed state.
```

**clause 之條件子句**（`COND_RE` 所命中者，4 處）：
- `IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND proxi parameter Brand_Configuration`
- `IF previous internal state TLM_Status.Info == "Full-Operation" AND PhoneCall.Info == "Not_`
- `IF PhoneCall.Info == "Active"OR IF previous internal state TLM_Status.Info == StandbyTHEN`
- `IF previous internal state TLM_Status.Info == StandbyTHEN TLM shall stay in Timed state.`

**`pre_conditions` 逐字**：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable"
4. The previous internal state was Standby
```

**實質前提**（扣除 bench 環境列，3 項）：
- 2. TLM_Status.Info and $Telematic_Power$ read "Timed"
- 3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable"
- 4. The previous internal state was Standby

**`input_test_data` 逐字**：
```
STATUS_BH_BCM1.DriverDoorSts = "Open"
```

**`test_procedure` 逐字**：
```
1. Send the signal listed in Input Test Data
2. Read TLM_Status.Info to check that Timed state is kept
```

**`expected_result` 逐字**：
```
1. The TLM registers the door signal without a bus error
2. TLM_Status.Info still reads "Timed" and the TLM stays in Timed state
```

**執行層所判之「二個以上條件」**：2. TLM_Status.Info and $Telematic_Power$ read "Timed"；3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable"；4. The previous internal state was Standby

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 4 列 8 / 14 —— `NR1L-PowerManagement-103`（`SWE-PM-028`）

**`tc_title`**：Antitheft success on LTM High takes Timeout1 from PROXI

**`source_clause` 逐字**（全文，未截斷）：
```
IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activation.Req back to "False" value and following logic must be guaranteed:
IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req =="Active ", when  Timeout1 == 00 MIN" for LTM High Radio): THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (for example 20 minutes if Switch_Off_Time == 20 minutes), only for this case,  restoring it to "00 minutes" at next Ignition On event.
AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it passes to TLM Timed state.
```

**clause 之條件子句**（`COND_RE` 所命中者，5 處）：
- `IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activation.Req ba`
- `IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req =="Active ",`
- `If Auto_SwitchOn_Setting.Req =="Active ", when Timeout1 == 00 MIN" for LTM High Radio): T`
- `when Timeout1 == 00 MIN" for LTM High Radio): THENTLM has to set Timeout1 to the value sp`
- `if Switch_Off_Time == 20 minutes), only for this case, restoring it to "00 minutes" at ne`

**`pre_conditions` 逐字**：
```
1. A LIN and CAN simulation tool is connected
2. An LTM High Radio is present in the bench configuration
3. Auto_SwitchOn_Setting.Req reads "Active " and Timeout1 reads "00 MIN"
4. Switch_Off_Time reads 20 minutes
```

**實質前提**（扣除 bench 環境列，2 項）：
- 3. Auto_SwitchOn_Setting.Req reads "Active " and Timeout1 reads "00 MIN"
- 4. Switch_Off_Time reads 20 minutes

**`input_test_data` 逐字**：
```
Antitheft_Result.Info = "Successfully"
```

**`test_procedure` 逐字**：
```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```

**`expected_result` 逐字**：
```
1. Timeout1 reads 20 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```

**執行層所判之「二個以上條件」**：3. Auto_SwitchOn_Setting.Req reads "Active " and Timeout1 reads "00 MIN"；4. Switch_Off_Time reads 20 minutes

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 4 列 9 / 14 —— `NR1L-PowerManagement-106`（`SWE-PM-029`）

**`tc_title`**：Timeout1 follows PwrAccDelayAct when the setting is zero

**`source_clause` 逐字**（全文，未截斷）：
```
IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activation.Req back to "False" value and following logic must be guaranteed:
IF SwitchOff_Timeout_Setting.Req == 00 min  THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (for example 20 minutes if Switch_Off_Time == 20 minutes), only for this case,  restoring it to "00 minutes" at next Ignition On event.
IF SwitchOff_Timeout_Setting.Req == 00 min  THEN TLM has to set Timeout1 to the value specified by $PwrAccDelayAct$ (for example 10  minutes if $PwrAccDelayAct$ == 10 minutes), only for this case,  restoring it to "00 minutes" at next Ignition  On event.
AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it passes to TLM Timed state.
```

**clause 之條件子句**（`COND_RE` 所命中者，5 處）：
- `IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activation.Req ba`
- `IF SwitchOff_Timeout_Setting.Req == 00 min THENTLM has to set Timeout1 to the value speci`
- `if Switch_Off_Time == 20 minutes), only for this case, restoring it to "00 minutes" at ne`
- `IF SwitchOff_Timeout_Setting.Req == 00 min THEN TLM has to set Timeout1 to the value spec`
- `if $PwrAccDelayAct$ == 10 minutes), only for this case, restoring it to "00 minutes" at n`

**`pre_conditions` 逐字**：
```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req reads "00 min"
3. $PwrAccDelayAct$ reads 10 minutes
```

**實質前提**（扣除 bench 環境列，2 項）：
- 2. SwitchOff_Timeout_Setting.Req reads "00 min"
- 3. $PwrAccDelayAct$ reads 10 minutes

**`input_test_data` 逐字**：
```
Antitheft_Result.Info = "Successfully"
```

**`test_procedure` 逐字**：
```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```

**`expected_result` 逐字**：
```
1. Timeout1 reads 10 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```

**執行層所判之「二個以上條件」**：2. SwitchOff_Timeout_Setting.Req reads "00 min"；3. $PwrAccDelayAct$ reads 10 minutes

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 4 列 10 / 14 —— `NR1L-PowerManagement-133`（`SWE-PM-044`）

**`tc_title`**：Front panel press in Sleep arms the antitheft and shows the Splash Screen

**`source_clause` 逐字**（全文，未截斷）：
```
IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” value with Engineering Line deactivatedTHENTLM has to set signal Antitheft_Activation.Req to "True" value AND TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization", for Response_Wait_Time. For Splash Screen logo, refer to TLM HMI Specification
IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND CLIMATIC_PANEL.Radio_Btn0 has a transition from “Not_Pressed” value to “Pressed” value with Engineering Line deactivatedTHENTLM has to set signal Antitheft_Activation.Req to "True" value AND TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization", for Response_Wait_Time. For Splash Screen logo, refer to TLM HMI Specification
```

**clause 之條件子句**（`COND_RE` 所命中者，2 處）：
- `IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND Front_Panel_OnOff.Req`
- `IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND CLIMATIC_PANEL.Radio_B`

**`pre_conditions` 逐字**：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Sleep"
3. The Engineering Line is deactivated
```

**實質前提**（扣除 bench 環境列，2 項）：
- 2. TLM_Status.Info and $Telematic_Power$ read "Sleep"
- 3. The Engineering Line is deactivated

**`input_test_data` 逐字**：
```
Front_Panel_OnOff.Req: "Not_Pressed" to "Pressed"
```

**`test_procedure` 逐字**：
```
1. Send the transition listed in Input Test Data
2. Read the antitheft request and the screen to check the resulting behavior
```

**`expected_result` 逐字**：
```
1. Antitheft_Activation.Req reads "True"
2. A proper Splash Screen is shown for Response_Wait_Time
```

**執行層所判之「二個以上條件」**：2. TLM_Status.Info and $Telematic_Power$ read "Sleep"；3. The Engineering Line is deactivated

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 4 列 11 / 14 —— `NR1L-PowerManagement-139`（`SWE-PM-046`）

**`tc_title`**：Rear view camera is provided after an unsuccessful antitheft

**`source_clause` 逐字**（全文，未截斷）：
```
IF Rear_View_Camera PROXI parameter == "Present" AND Rear_Camera_Enable.Info == "True" THENeven IF Antitheft_Result.Info is still equal to "In_Progress" or "Not_Successfully", TLM shall provide audio and video for rear view camera component, as soon as the images are available on TLM and as long as Rear_Camera_Enable.Info == "True".Refer to VF551 for details about video availability requirements on TLM screen
```

**clause 之條件子句**（`COND_RE` 所命中者，3 處）：
- `IF Rear_View_Camera PROXI parameter == "Present" AND Rear_Camera_Enable.Info == "True" THE`
- `IF Antitheft_Result.Info is still equal to "In_Progress" or "Not_Successfully", TLM shall`
- `as long as Rear_Camera_Enable.Info == "True".Refer to VF551 for details about video availa`

**`pre_conditions` 逐字**：
```
1. A LIN and CAN simulation tool is connected
2. The Rear_View_Camera PROXI parameter reads "Present"
3. Rear_Camera_Enable.Info reads "True"
```

**實質前提**（扣除 bench 環境列，2 項）：
- 2. The Rear_View_Camera PROXI parameter reads "Present"
- 3. Rear_Camera_Enable.Info reads "True"

**`input_test_data` 逐字**：
```
Antitheft_Result.Info: "Not_Successfully"
```

**`test_procedure` 逐字**：
```
1. Send the value listed in Input Test Data
2. Read the screen and the audio path to check the rear view camera component
```

**`expected_result` 逐字**：
```
1. The TLM registers the value without a bus error
2. The TLM provides audio and video for the rear view camera component as long as Rear_Camera_Enable.Info reads "True"
```

**執行層所判之「二個以上條件」**：2. The Rear_View_Camera PROXI parameter reads "Present"；3. Rear_Camera_Enable.Info reads "True"

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 4 列 12 / 14 —— `NR1L-PowerManagement-191`（`SWE-PM-099`）

**`tc_title`**：The once a day setting plays the startup sound on the first startup of the day

**`source_clause` 逐字**（全文，未截斷）：
```
If $Themed_Sound$ = [Fiat Latam] AND the "Welcome Onboard Sound" setting is set to "Once a Day" AND the HU has not yet played the startup sound yet that day, the HU startup animation shall be accompanied by a startup sound that begins at the same time.
For the purposes of CFTS009-2299, the HU shall consider it a new "day" to allow the sound to be played any time the customer selected date changes; including manual time adjustments from the user, the time passing midnight, or automatic adjustments due to time zones or Daylight Savings Time.
```

**clause 之條件子句**（`COND_RE` 所命中者，2 處）：
- `If $Themed_Sound$ = [Fiat Latam] AND the "Welcome Onboard Sound" setting is set to "Once a`
- `Once a Day" AND the HU has not yet played the startup sound yet that day, the HU startup a`

**`pre_conditions` 逐字**：
```
1. A LIN and CAN simulation tool is connected
2. $Themed_Sound$ reads "Fiat Latam"
3. The "Welcome Onboard Sound" setting reads "Once a Day"
4. The HU has not yet played the startup sound that day
```

**實質前提**（扣除 bench 環境列，3 項）：
- 2. $Themed_Sound$ reads "Fiat Latam"
- 3. The "Welcome Onboard Sound" setting reads "Once a Day"
- 4. The HU has not yet played the startup sound that day

**`input_test_data` 逐字**：
```
NA
```

**`test_procedure` 逐字**：
```
1. Bring the HU through a startup that plays the animation
2. Read the audio output against the animation start to check the accompaniment
```

**`expected_result` 逐字**：
```
1. The HU startup animation is played
2. A startup sound accompanies the animation and begins at the same time
```

**執行層所判之「二個以上條件」**：2. $Themed_Sound$ reads "Fiat Latam"；3. The "Welcome Onboard Sound" setting reads "Once a Day"；4. The HU has not yet played the startup sound that day

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 4 列 13 / 14 —— `NR1L-PowerManagement-223`（`SWE-PM-109`）

**`tc_title`**：A GDPR market with the TBM present follows the GDPR non Maserati startup flow

**`source_clause` 逐字**（全文，未截斷）：
```
If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Present$ = [Present]  AND $Country_Code$ is marked as "Countries which need the combined Geolocation plus SOS Popup" (see market configuration table) then the HU shall follow the GDPR Non-Maserati startup flow in the HMI.
```

**clause 之條件子句**（`COND_RE` 所命中者，1 處）：
- `If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Present$ = [Present] AND $Country_Code$ is marke`

**`pre_conditions` 逐字**：
```
1. A LIN and CAN simulation tool is connected
2. $VC_VEH_BRAND$ reads a value other than "Maserati"
3. $TBM_Present$ reads "Present"
4. $Country_Code$ is marked as a country needing the combined Geolocation plus SOS Popup
```

**實質前提**（扣除 bench 環境列，3 項）：
- 2. $VC_VEH_BRAND$ reads a value other than "Maserati"
- 3. $TBM_Present$ reads "Present"
- 4. $Country_Code$ is marked as a country needing the combined Geolocation plus SOS Popup

**`input_test_data` 逐字**：
```
NA
```

**`test_procedure` 逐字**：
```
1. Bring the HU through the startup sequence
2. Read the startup flow against the HMI to check which flow is followed
```

**`expected_result` 逐字**：
```
1. The HU reaches the startup presentation
2. The HU follows the GDPR Non-Maserati startup flow in the HMI
```

**執行層所判之「二個以上條件」**：2. $VC_VEH_BRAND$ reads a value other than "Maserati"；3. $TBM_Present$ reads "Present"；4. $Country_Code$ is marked as a country needing the combined Geolocation plus SOS Popup

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 4 列 14 / 14 —— `NR1L-PowerManagement-228`（`SWE-PM-113`）

**`tc_title`**：A geolocation and SOS market adds the ADAS and SOS text

**`source_clause` 逐字**（全文，未截斷）：
```
For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Present$ = [Present]  AND $Country_Code$ requires geolocation and SOS in the disclaimer then the HU shall add the ADAS and SOS to the geolocation pop-up or disclaimer. See HMI for different statup conditions to determine when to add geolocation + SOS Pop-up or add geolocation and SOS text to Disclaimer.
```

**clause 之條件子句**（`COND_RE` 所命中者，2 處）：
- `If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Present$ = [Present] AND $Country_Code$ requires`
- `when to add geolocation + SOS Pop-up or add geolocation and SOS text to Disclaimer.`

**`pre_conditions` 逐字**：
```
1. A LIN and CAN simulation tool is connected
2. The screen size is other than 7 inch
3. $VC_VEH_BRAND$ reads a value other than "Maserati"
4. $TBM_Present$ reads "Present"
5. $Country_Code$ requires geolocation and SOS in the disclaimer
```

**實質前提**（扣除 bench 環境列，4 項）：
- 2. The screen size is other than 7 inch
- 3. $VC_VEH_BRAND$ reads a value other than "Maserati"
- 4. $TBM_Present$ reads "Present"
- 5. $Country_Code$ requires geolocation and SOS in the disclaimer

**`input_test_data` 逐字**：
```
NA
```

**`test_procedure` 逐字**：
```
1. Bring the HU to the disclaimer presentation
2. Read the shown wording to check what the HU adds
```

**`expected_result` 逐字**：
```
1. The geolocation pop-up or the disclaimer is shown
2. The HU adds the ADAS and SOS to the geolocation pop-up or disclaimer
```

**執行層所判之「二個以上條件」**：2. The screen size is other than 7 inch；3. $VC_VEH_BRAND$ reads a value other than "Maserati"；4. $TBM_Present$ reads "Present"；5. $Country_Code$ requires geolocation and SOS in the disclaimer

**現值 `design_method`**：狀態轉換 (State Transition Testing)

---

## 二、第 8 列全 7 條

複核之問題：**該 TC 之 ≥ 3 步是否確為「跨功能」？**
（現行謂詞只驗步數，「跨功能」未機械化 —— 35 §7.3）

### 第 8 列 1 / 7 —— `NR1L-PowerManagement-007`（`SWE-PM-073`）

**`tc_title`**：Load Shed limits volume and mutes TLM

**`source_clause` 逐字**（全文，未截斷）：
```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

**clause 之條件子句**（`COND_RE` 所命中者，11 處）：
- `When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received b`
- `if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall`
- `If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. U`
- `Under fault condition of missing load shed signals on the CAN bus, the last values of load`
- `If the load shed signals do not recover, the on-going load shed action shall be maintained`
- `While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], t`
- `when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw wh`
- `while keeping only the display on and controls active for HVAC controls, and active phone`
- `if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall`
- `If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the cal`
- `Unless defined otherwise, TLM shall stay in this state until either voltage out of range c`

**`pre_conditions` 逐字**：
```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. Ecall, ACN and chimes modes are inactive
```

**實質前提**（扣除 bench 環境列，1 項）：
- 3. Ecall, ACN and chimes modes are inactive

**`input_test_data` 逐字**：
```
STATUS_LIN.PN14_LS_Actv = [1h]
STATUS_LIN.PN14_LS_Lvl7 = [1h]
Starting volume level: 25
```

**`test_procedure` 逐字**：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the two Load Shed signals listed in Input Test Data
3. Read AUD_LVL, the audio output and the ICS power state to check the Load Shed action
```

**`expected_result` 逐字**：
```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts both Load Shed signals without a bus error
3. The maximum volume for Ecall, ACN, chimes, beeps and alerts is reduced to 20, AUD_LVL carries the updated level, the TLM is muted and the ICS module powers down
```

**執行層所判之「二個以上條件」**：3. Ecall, ACN and chimes modes are inactive

**現值 `design_method`**：決策表 (Decision Table Testing)

### 第 8 列 2 / 7 —— `NR1L-PowerManagement-008`（`SWE-PM-073`）

**`tc_title`**：Load Shed signals lost: last values retained

**`source_clause` 逐字**（全文，未截斷）：
```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

**clause 之條件子句**（`COND_RE` 所命中者，11 處）：
- `When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received b`
- `if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall`
- `If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. U`
- `Under fault condition of missing load shed signals on the CAN bus, the last values of load`
- `If the load shed signals do not recover, the on-going load shed action shall be maintained`
- `While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], t`
- `when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw wh`
- `while keeping only the display on and controls active for HVAC controls, and active phone`
- `if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall`
- `If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the cal`
- `Unless defined otherwise, TLM shall stay in this state until either voltage out of range c`

**`pre_conditions` 逐字**：
```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. The Load Shed condition is already active
```

**實質前提**（扣除 bench 環境列，1 項）：
- 3. The Load Shed condition is already active

**`input_test_data` 逐字**：
```
NA
```

**`test_procedure` 逐字**：
```
1. Stop the broadcast of the two Load Shed signals on the bus
2. Read the AUD_LVL signal and the audio output state
3. Keep the broadcast stopped to the end of the ignition cycle to check that Load Shed is maintained
```

**`expected_result` 逐字**：
```
1. The two Load Shed signals are absent from the bus trace
2. AUD_LVL still carries the reduced level and the TLM stays muted
3. The Load Shed action is maintained for the rest of the current ignition key cycle
```

**執行層所判之「二個以上條件」**：3. The Load Shed condition is already active

**現值 `design_method`**：基礎故障注入 (Fault Injection Lite)

### 第 8 列 3 / 7 —— `NR1L-PowerManagement-016`（`SWE-PM-073`）

**`tc_title`**：Load Shed with volume already below the cap: no AUD_LVL update

**`source_clause` 逐字**（全文，未截斷）：
```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

**clause 之條件子句**（`COND_RE` 所命中者，11 處）：
- `When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received b`
- `if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall`
- `If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. U`
- `Under fault condition of missing load shed signals on the CAN bus, the last values of load`
- `If the load shed signals do not recover, the on-going load shed action shall be maintained`
- `While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], t`
- `when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw wh`
- `while keeping only the display on and controls active for HVAC controls, and active phone`
- `if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall`
- `If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the cal`
- `Unless defined otherwise, TLM shall stay in this state until either voltage out of range c`

**`pre_conditions` 逐字**：
```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. Ecall, ACN and chimes modes are inactive
```

**實質前提**（扣除 bench 環境列，1 項）：
- 3. Ecall, ACN and chimes modes are inactive

**`input_test_data` 逐字**：
```
STATUS_LIN.PN14_LS_Actv = [1h]
STATUS_LIN.PN14_LS_Lvl7 = [1h]
Starting volume level: 15
```

**`test_procedure` 逐字**：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the two Load Shed signals listed in Input Test Data
3. Read the CAN trace and the volume level to check that AUD_LVL is not updated
```

**`expected_result` 逐字**：
```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts both Load Shed signals without a bus error
3. No AUD_LVL signal carrying a new volume level appears in the trace and the volume level is unchanged
```

**執行層所判之「二個以上條件」**：3. Ecall, ACN and chimes modes are inactive

**現值 `design_method`**：決策表 (Decision Table Testing)

### 第 8 列 4 / 7 —— `NR1L-PowerManagement-025`（`SWE-PM-062`）

**`tc_title`**：Auto_SwitchOn_Setting.Req can be set to Active

**`source_clause` 逐字**（全文，未截斷）：
```
User can select Auto_SwitchOn_Setting.Req value equal to "Active" (If LTM High is present: "Timeout1" = "00 minutes");"Not_Active (If LTM High is present:"Timeout1" <> "00 minutes");"Recall_Last" (If LTM High is present:"Timeout1 = "00 minutes")
```

**clause 之條件子句**（`COND_RE` 所命中者，3 處）：
- `If LTM High is present: "Timeout1" = "00 minutes");"Not_Active (If LTM High is present:"Ti`
- `If LTM High is present:"Timeout1" <> "00 minutes");"Recall_Last" (If LTM High is present:"`
- `If LTM High is present:"Timeout1 = "00 minutes")`

**`pre_conditions` 逐字**：
```
1. An LTM High Radio is present in the bench configuration
2. The TLM is in Full-Operation status
```

**實質前提**（扣除 bench 環境列，1 項）：
- 2. The TLM is in Full-Operation status

**`input_test_data` 逐字**：
```
NA
```

**`test_procedure` 逐字**：
```
1. Open the timeout setting entry in the TLM menu
2. Select "Active" for Auto_SwitchOn_Setting.Req
3. Read Auto_SwitchOn_Setting.Req and Timeout1 to check the stored selection
```

**`expected_result` 逐字**：
```
1. The timeout setting entry is shown in the TLM menu
2. The TLM accepts the selection without reverting it
3. Auto_SwitchOn_Setting.Req reads "Active" and Timeout1 reads "00 minutes"
```

**執行層所判之「二個以上條件」**：2. The TLM is in Full-Operation status

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 8 列 5 / 7 —— `NR1L-PowerManagement-026`（`SWE-PM-062`）

**`tc_title`**：Auto_SwitchOn_Setting.Req can be set to Not_Active

**`source_clause` 逐字**（全文，未截斷）：
```
User can select Auto_SwitchOn_Setting.Req value equal to "Active" (If LTM High is present: "Timeout1" = "00 minutes");"Not_Active (If LTM High is present:"Timeout1" <> "00 minutes");"Recall_Last" (If LTM High is present:"Timeout1 = "00 minutes")
```

**clause 之條件子句**（`COND_RE` 所命中者，3 處）：
- `If LTM High is present: "Timeout1" = "00 minutes");"Not_Active (If LTM High is present:"Ti`
- `If LTM High is present:"Timeout1" <> "00 minutes");"Recall_Last" (If LTM High is present:"`
- `If LTM High is present:"Timeout1 = "00 minutes")`

**`pre_conditions` 逐字**：
```
1. An LTM High Radio is present in the bench configuration
2. The TLM is in Full-Operation status
```

**實質前提**（扣除 bench 環境列，1 項）：
- 2. The TLM is in Full-Operation status

**`input_test_data` 逐字**：
```
NA
```

**`test_procedure` 逐字**：
```
1. Open the timeout setting entry in the TLM menu
2. Select "Not_Active" for Auto_SwitchOn_Setting.Req
3. Read Auto_SwitchOn_Setting.Req and Timeout1 to check the stored selection
```

**`expected_result` 逐字**：
```
1. The timeout setting entry is shown in the TLM menu
2. The TLM accepts the selection without reverting it
3. Auto_SwitchOn_Setting.Req reads "Not_Active" and Timeout1 holds a value other than "00 minutes"
```

**執行層所判之「二個以上條件」**：2. The TLM is in Full-Operation status

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 8 列 6 / 7 —— `NR1L-PowerManagement-027`（`SWE-PM-062`）

**`tc_title`**：Auto_SwitchOn_Setting.Req can be set to Recall_Last

**`source_clause` 逐字**（全文，未截斷）：
```
User can select Auto_SwitchOn_Setting.Req value equal to "Active" (If LTM High is present: "Timeout1" = "00 minutes");"Not_Active (If LTM High is present:"Timeout1" <> "00 minutes");"Recall_Last" (If LTM High is present:"Timeout1 = "00 minutes")
```

**clause 之條件子句**（`COND_RE` 所命中者，3 處）：
- `If LTM High is present: "Timeout1" = "00 minutes");"Not_Active (If LTM High is present:"Ti`
- `If LTM High is present:"Timeout1" <> "00 minutes");"Recall_Last" (If LTM High is present:"`
- `If LTM High is present:"Timeout1 = "00 minutes")`

**`pre_conditions` 逐字**：
```
1. An LTM High Radio is present in the bench configuration
2. The TLM is in Full-Operation status
```

**實質前提**（扣除 bench 環境列，1 項）：
- 2. The TLM is in Full-Operation status

**`input_test_data` 逐字**：
```
NA
```

**`test_procedure` 逐字**：
```
1. Open the timeout setting entry in the TLM menu
2. Select "Recall_Last" for Auto_SwitchOn_Setting.Req
3. Read Auto_SwitchOn_Setting.Req and Timeout1 to check the stored selection
```

**`expected_result` 逐字**：
```
1. The timeout setting entry is shown in the TLM menu
2. The TLM accepts the selection without reverting it
3. Auto_SwitchOn_Setting.Req reads "Recall_Last" and Timeout1 reads "00 minutes"
```

**執行層所判之「二個以上條件」**：2. The TLM is in Full-Operation status

**現值 `design_method`**：狀態轉換 (State Transition Testing)

### 第 8 列 7 / 7 —— `NR1L-PowerManagement-028`（`SWE-PM-063`）

**`tc_title`**：Bluetooth calls can be made and received in Timed state

**`source_clause` 逐字**（全文，未截斷）：
```
In Timed state, it is possible either to make and to receive one or more bluetooth phone calls according to following logics that depend on Timeout1 and on MaxCallTimeout time parameters.
```

**clause 之條件子句**（`COND_RE` 所命中者，0 處）：
- （無）

**`pre_conditions` 逐字**：
```
1. A paired bluetooth phone is available on the bench
2. The TLM is in Timed state
```

**實質前提**（扣除 bench 環境列，1 項）：
- 2. The TLM is in Timed state

**`input_test_data` 逐字**：
```
NA
```

**`test_procedure` 逐字**：
```
1. Place an outgoing bluetooth call from the paired phone through the TLM
2. End that call and receive an incoming bluetooth call
3. Read the call audio routing and the TLM state to check that both calls were served
```

**`expected_result` 逐字**：
```
1. The outgoing call is connected
2. The incoming call is presented and can be answered
3. Both calls were served and the TLM remains in Timed state
```

**執行層所判之「二個以上條件」**：2. The TLM is in Timed state

**現值 `design_method`**：狀態轉換 (State Transition Testing)
