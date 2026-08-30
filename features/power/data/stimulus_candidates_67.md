# 刺激訊號候選（67 包 / R-P390(a)(c)）

> **執行層供料，不擇定**（R-P390(b)：由分析層以 `CM_` 是否**明述**該功能擇定；
> `CM_` 無明述者不選；全無者開 DR）。

> 判準：規格只述功能（「有 chime」「ICS 可用」）而未指名訊號 —— 屬**測試刺激之設計選擇**，R-P368(b) 之逐字要件不適用（R-P390 明示）。
> 候選以**規格用語**之關鍵詞掃 forms 二本 DBC，非以訊號名語意挑選。

## chime（`-055`：ANC/ACN/chime 可用之驗證刺激）

候選 **38** 個。

| DBC | `MESSAGE.Signal` | `CM_` 註解全文 | 發送節點 | 接收節點 | `VAL_` |
|---|---|---|---|---|---|
| BHCAN2 | `GW_B_1.PAM_CHIME_TYPE` | Pam chime type | `SGW` | `ETM,LTM` | 0 "None" 1 "Type_1" 2 "Type_2" 3 "Type_3" 4 "Type_4" 5 "Type_5" 6 "Typ |
| BHCAN2 | `GW_B_3.PAM_CHIME_REP_RATESts` | PAM chime repetition rate | `SGW` | `ETM,LTM` | 0 "Continuous_0_Hz" 2 "Slow_2_Hz" 3 "Slow_3_Hz" 4 "Fast_4_Hz" 5 "Fast_ |
| BHCAN2 | `GW_B_5.Chime_Priority` | Chime Priority | `SGW` | `ETM,LTM` | 0 "A" 1 "B" 2 "C" 3 "D" 4 "E" |
| BHCAN2 | `GW_B_5.Chime_RepRate` | DASM Chime Repetition Rate | `SGW` | `ETM,LTM` | — |
| BHCAN2 | `GW_B_5.Chime_TypSts` | DASM Chime Type Status | `SGW` | `ETM,LTM` | 0 "Default" 1 "Chime 1" 2 "Chime 2" 3 "Chime 3" 4 "Chime 4" 5 "Chime 5 |
| BHCAN2 | `GW_B_5.LF_Chime_RqSts` | DASM_LF_Chime_RqSts | `SGW` | `ETM,LTM` | 0 "No_Request" 1 "Request" |
| BHCAN2 | `GW_B_5.LR_Chime_RqSts` | BSM Left rear chime on request | `SGW` | `ETM,LTM` | 0 "No_left_rear_chime_on_req" 1 "Left_rear_chime_on_req" |
| BHCAN2 | `GW_B_5.RF_Chime_RqSts` | DASM_RF_Chime_RqSts | `SGW` | `ETM,LTM` | 0 "No_Request" 1 "Request" |
| BHCAN2 | `GW_B_5.RR_Chime_RqSts` | BSM right rear chime on request | `SGW` | `ETM,LTM` | 0 "No_rght_rear_chime_on_req" 1 "Right_rear_chime_on_req" |
| BHCAN2 | `IPC_VEHICLE_SETUP.PamChimeVolumeFront` | This signal is used to give information about the PAM  Chime Volume selected | `SGW` | `ETM,LTM` | 0 "Low" 1 "Medium" 2 "High" |
| BHCAN2 | `IPC_VEHICLE_SETUP.PamChimeVolumeRear` | This signal is used to give information about the PAM 8Ch Chime Volume selected | `SGW` | `ETM,LTM` | 0 "Low" 1 "Medium" 2 "High" |
| BHCAN2 | `PARK_INFO.ChimeActivation_LHF` | This signal indicates the chime activation request for the left hand, front audio speaker, or rear hardwired buzzer. | `SGW` | `ETM,LTM` | 0 "NotActive" 1 "Active" |
| BHCAN2 | `PARK_INFO.ChimeActivation_LHR` | This signal indicates the chime activation request for the left hand, rear audio speaker, or rear hardwired buzzer. | `SGW` | `ETM,LTM` | 0 "NotActive" 1 "Active" |
| BHCAN2 | `PARK_INFO.ChimeActivation_RHF` | This signal indicates the chime activation request for the right hand, front audio speaker, or rear hardwired buzzer. | `SGW` | `ETM,LTM` | 0 "NotActive" 1 "Active" |
| BHCAN2 | `PARK_INFO.ChimeActivation_RHR` | This signal indicates the chime activation request for the right hand, rear audio speaker, or rear hardwired buzzer. | `SGW` | `ETM,LTM` | 0 "NotActive" 1 "Active" |
| FDCAN8 | `ADAS_FD_HMI.Chime_Priority` | Chime Priority | `SGW` | `ETM,LTM,TBM` | 0 "A" 1 "B" 2 "C" 3 "D" 4 "E" |
| FDCAN8 | `ADAS_FD_HMI.Chime_RepRate` | DASM Chime Repetition Rate | `SGW` | `ETM,LTM,TBM` | — |
| FDCAN8 | `ADAS_FD_HMI.Chime_TypSts` | DASM Chime Type Status | `SGW` | `ETM,LTM,TBM` | 0 "Default" 1 "Chime_1" 2 "Chime_2" 3 "Chime_3" 4 "Chime_4" 5 "Chime_5 |
| FDCAN8 | `ADAS_FD_HMI.LF_Chime_RqSts` | DASM_LF_Chime_RqSts | `SGW` | `ETM,LTM,TBM` | 0 "No_Request" 1 "Request" |
| FDCAN8 | `ADAS_FD_HMI.LR_Chime_RqSts` | BSM Left rear chime on request | `SGW` | `ETM,LTM,TBM` | 0 "No_left_rear_chime_on_req" 1 "Left_rear_chime_on_req" |
| FDCAN8 | `ADAS_FD_HMI.RF_Chime_RqSts` | DASM_RF_Chime_RqSts | `SGW` | `ETM,LTM,TBM` | 0 "No_Request" 1 "Request" |
| FDCAN8 | `ADAS_FD_HMI.RR_Chime_RqSts` | BSM right rear chime on request | `SGW` | `ETM,LTM,TBM` | 0 "No_rght_rear_chime_on_req" 1 "Right_rear_chime_on_req" |
| FDCAN8 | `ADAS_FD_HMI_C2.Chime_Priority_C2` | Chime_Priority_C2 | `SGW` | `ETM,LTM,TBM` | 0 "A" 1 "B" 2 "C" 3 "D" 4 "E" |
| FDCAN8 | `ADAS_FD_HMI_C2.Chime_RepRate_C2` | Chime_RepRate_C2 | `SGW` | `ETM,LTM,TBM` | — |
| FDCAN8 | `ADAS_FD_HMI_C2.Chime_TypSts_C2` | Chime_TypSts_C2 | `SGW` | `ETM,LTM,TBM` | 0 "Default" 1 "Chime_1" 2 "Chime_2" 3 "Chime_3" 4 "Chime_4" 5 "Chime_5 |
| FDCAN8 | `ADAS_FD_HMI_C2.LF_Chime_RqSts_C2` | LF_Chime_RqSts_C2 | `SGW` | `ETM,LTM,TBM` | 0 "No_Request" 1 "Request" |
| FDCAN8 | `ADAS_FD_HMI_C2.LR_Chime_RqSts_C2` | LR_Chime_RqSts_C2 | `SGW` | `ETM,LTM,TBM` | 0 "No_left_rear_chime_on_req" 1 "Left_rear_chime_on_req" |
| FDCAN8 | `ADAS_FD_HMI_C2.RF_Chime_RqSts_C2` | RF_Chime_RqSts_C2 | `SGW` | `ETM,LTM,TBM` | 0 "No_Request" 1 "Request" |
| FDCAN8 | `ADAS_FD_HMI_C2.RR_Chime_RqSts_C2` | RR_Chime_RqSts_C2 | `SGW` | `ETM,LTM,TBM` | 0 "No_rght_rear_chime_on_req" 1 "Right_rear_chime_on_req" |
| FDCAN8 | `ENGINE_FD_3.OIL_TEMP_CHM_RQ` | Oil temperature chime request | `SGW` | `ETM,LTM,TBM` | 0 "NONE" 1 "SINGLE" 2 "SLOW" 3 "FAST" |
| FDCAN8 | `IPC_VEHICLE_SETUP.Active_Park_Prox_Chime` | Active Parksense Proximity Chime setting | `SGW` | `ETM,LTM` | 0 "Off" 1 "On" |
| FDCAN8 | `IPC_VEHICLE_SETUP.PamChimeVolumeFront` | This signal is used to give information about the PAM  Chime Volume selected | `SGW` | `ETM,LTM,TBM` | 0 "Low" 1 "Medium" 2 "High" |
| FDCAN8 | `IPC_VEHICLE_SETUP.PamChimeVolumeRear` | This signal is used to give information about the PAM 8Ch Chime Volume selected | `SGW` | `ETM,LTM,TBM` | 0 "Low" 1 "Medium" 2 "High" |
| FDCAN8 | `IPC_VEHICLE_SETUP.PLGAlert` | Setting to turn on/off the power liftgate chime | `SGW` | `ETM,LTM` | 0 "Off" 1 "On" |
| FDCAN8 | `TELEMATIC_VEHICLE_SETUP.Active_Park_Prox_Chime_Req` | Active Parksense Proximity Chime setting request | `ETM` | `SGW` | 0 "Off" 1 "On" |
| FDCAN8 | `TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req` | This signal is managed when the driver request a  setting of the of Chime Volume  of the PAM | `ETM` | `SGW` | 0 "Low" 1 "Medium" 2 "High" |
| FDCAN8 | `TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req` | This signal is managed when the driver request a  setting of the of Chime Volume  of the PAM  8  Channels | `ETM` | `SGW` | 0 "Low" 1 "Medium" 2 "High" |
| FDCAN8 | `TELEMATIC_VEHICLE_SETUP.PLGAlert_Req` | Setting to turn on/off the power liftgate chime | `ETM` | `SGW` | 0 "Off" 1 "On" |

> ⚠ 其中 **0 個無 `CM_` 註解** —— 依 R-P390(b)「`CM_` 無明述者不選」，該等候選**不可選**，列此僅為完整性。

## ICS 面板觸控回應（`-202`：ICS 功能可用之驗證刺激）

候選 **73** 個。

| DBC | `MESSAGE.Signal` | `CM_` 註解全文 | 發送節點 | 接收節點 | `VAL_` |
|---|---|---|---|---|---|
| BHCAN2 | `CLIMATIC_PANEL.Radio_btn0` | Indicates the status of  radio button0 | `SGW` | `LTM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `CLIMATIC_PANEL.Radio_btn1` | Indicates the status of  radio button1 | `SGW` | `ETM,LTM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `CLIMATIC_PANEL.Radio_btn2` | Indicates the status of  radio button2 | `SGW` | `ETM,LTM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `CLIMATIC_PANEL.Radio_btn3` | Indicates the status of  radio button3 | `SGW` | `ETM,LTM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `CLIMATIC_PANEL.Radio_btn4` | Indicates the status of  radio button4 | `SGW` | `ETM,LTM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `CLIMATIC_PANEL.Radio_Knob1_DIR` | Knob direction | `SGW` | `ETM,LTM` | 0 "Knob_no_change" 1 "Knob_increment" 2 "Knob_decrement" 3 "Knob_enter |
| BHCAN2 | `CLIMATIC_PANEL.Radio_Knob1_VAL` | Knob value | `SGW` | `ETM,LTM` | — |
| BHCAN2 | `CLIMATIC_PANEL.Radio_Knob2_DIR` | Knob direction | `SGW` | `ETM,LTM` | 0 "Knob_no_change" 1 "Knob_increment" 2 "Knob_decrement" 3 "Knob_enter |
| BHCAN2 | `CLIMATIC_PANEL.Radio_Knob2_VAL` | Knob value | `SGW` | `ETM,LTM` | — |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_AC` | DCSD_AC | `SGW` | `ETM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_Auto` | DCSD_Auto | `SGW` | `ETM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_DISP_STAT` | Remote Display Status | `SGW` | `ETM,LTM` | 0 "OFF" 1 "ON" 2 "BLANK" 3 "RR_CMRA" 4 "DISP_HOT" 7 "SNA" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_Enter` | DCSD Enter | `SGW` | `ETM` | 0 "Enter_Not_Pressed" 1 "Enter_Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_FanSpeedDown` | DCSD_FanSpeedDown | `SGW` | `ETM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_FanSpeedUp` | DCSD_FanSpeedUp | `SGW` | `ETM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_Front_Defrost` | Front defrost request from DCSD | `SGW` | `ETM` | 0 "Not_pressed" 1 "pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_LeftTempDown` | Left temp down button status | `SGW` | `ETM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_LeftTempUp` | Left temp up button status | `SGW` | `ETM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_Mode` | DCSD_Mode | `SGW` | `ETM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_Mute` | Indicates the status of  mute button | `SGW` | `ETM` | 0 "Not_pressed" 1 "pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_Power` | DCSD Power | `SGW` | `ETM` | 0 "Button_Not_Pressed" 1 "Button_Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_Rear_Defrost` | Rear defrost request from DCSD | `SGW` | `ETM` | 0 "Not_pressed" 1 "pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_Recirc` | DCSD_Recirc | `SGW` | `ETM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_RightTempDown` | DCSD_RightTempDown | `SGW` | `ETM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_RightTempUp` | DCSD_RightTempUp | `SGW` | `ETM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_Screen_Off` | DCSD Screen Off | `SGW` | `ETM` | 0 "Screen_Off_Not_Pressed" 1 "Screen_Off_Pressed" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_TUNEKNOB_DIR` | DCSD_TUNEKNOB_DIR | `SGW` | `ETM` | 0 "KNOB_NO_CHNG" 1 "KNOB_INC_POS" 2 "KNOB_DEC_NEG" 3 "KNOB_ENTER" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_TUNEKNOB_VAL` | DCSD TUNEKNOB VAL | `SGW` | `ETM` | — |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_VOLKNOB_DIR` | DCSD VOLKNOB DIR | `SGW` | `ETM` | 0 "KNOB_NO_CHNG" 1 "KNOB_INC_POS" 2 "KNOB_DEC_NEG" 3 "KNOB_ENTER" |
| BHCAN2 | `DIS_CENTERSTACK.DCSD_VOLKNOB_VAL` | DCSD VOLKNOB VAL | `SGW` | `ETM` | — |
| BHCAN2 | `DRIVER_DOOR.MassageSw_DSSM` | Driver Massage switch button status | `SGW` | `ETM,LTM` | 0 "NOT_PRESSED" 1 "PRESSED" |
| BHCAN2 | `PASS_DOOR.MassageSw_PDSSM` | Passenger Massage switch button status | `SGW` | `ETM,LTM` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `RADIO_B4.MassageSw_D_Tlm` | Driver Massage radio button request staus | `ETM` | `SGW` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `RADIO_B4.MassageSw_P_Tlm` | Passenger Massage radio button request staus | `ETM` | `SGW` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `RADIO_B5.Driver_Cushion_Back_Tlm` | Driver independent cusion and back softbutton pressed or not | `ETM` | `SGW` | 0 "Not_Pressed" 1 "Pressed" |
| BHCAN2 | `RADIO_B5.Psngr_Cushion_Back_Tlm` | Passenger independent cusion and back softbutton pressed or not | `ETM` | `SGW` | 0 "Not_Pressed" 1 "Pressed" |
| FDCAN8 | `BCM_FD_10.PANEL_INTS` | Panel-/display intensity | `SGW` | `TBM` | 255 "SNA" |
| FDCAN8 | `BCM_FD_10.SpSt_Pad1` | Stop Start Button Press 1 | `SGW` | `ETM,LTM,TBM` | 0 "Not_Selected" 1 "Sw1_Activated" 2 "Sw2_Activated" 3 "Sw1_and_Sw2_Ac |
| FDCAN8 | `BCM_FD_12.APARequestSts` | It indicates the pressure of Advanced Park Assist pushbutton | `SGW` | `ETM,LTM,TBM` | 0 "Not_Pressed" 1 "Pressed" |
| FDCAN8 | `BCM_FD_12.PAMRequestSts` | It indicates the pressure of Park Assist pushbutton | `SGW` | `ETM,LTM,TBM` | 0 "Not_Pressed" 1 "Pressed" |
| FDCAN8 | `BCM_FD_13.AcceleratorSts` | This signal is used to give information about cruise control accelerator button activation. | `SGW` | `ETM,LTM,TBM` | 0 "Not_Active" 1 "Active" |
| FDCAN8 | `BCM_FD_13.CruiseControlOnOffSts` | This signal is used to give information about cruise control on/off button activation . | `SGW` | `ETM,LTM,TBM` | 0 "Not_Active" 1 "Active" |
| FDCAN8 | `BCM_FD_13.DeceleratorSts` | This signal is used to give information about cruise control decelerator button activation. | `SGW` | `ETM,LTM,TBM` | 0 "Not_Active" 1 "Active" |
| FDCAN8 | `BCM_FD_13.ResumeSwitch` | This signal is used to give information about cruise control RESUME button activation. | `SGW` | `ETM,LTM,TBM` | 0 "Not_Active" 1 "Active" |
| FDCAN8 | `BCM_FD_23.Worksite_Inverter_RadioSwitch` | Inverter Soft Button switch; [1] = ON | `SGW` | `ETM,LTM` | 0 "OFF" 1 "ON" |
| FDCAN8 | `BCM_FD_27.E_Call_Button` | E-Call Button Status | `SGW` | `ETM,LTM,TBM` | 0 "Not_Pressed" 1 "Pressed" 3 "SNA" |
| FDCAN8 | `BCM_FD_27.PANEL_INTS_DISP` | Panel-/display intensity display | `SGW` | `ETM,LTM` | 255 "SNA" |
| FDCAN8 | `BCM_FD_27.U_Call_Button` | U-Call Button Status | `SGW` | `ETM,LTM,TBM` | 0 "Not_Pressed" 1 "Pressed" 3 "SNA" |
| FDCAN8 | `BCM_FD_9.PowerPanelMsg` | Power panel pop ups for the 2kW Inverter | `SGW` | `ETM,LTM` | 0 "No_Msg" 1 "Low_battery_level" 2 "Low_fuel_level" 3 "System_Fault" 4 |
| FDCAN8 | `BRAKE_FD_4.BSM_LnchCtrl_SftBtn_SelectSts` | Soft button launch selected; Launch selected = [1] | `SGW` | `ETM,LTM` | 0 "False" 1 "True" |
| FDCAN8 | `BRAKE_FD_4.ESC_OFF_Hrd_Sft_Button_sts` | ESC hard button status | `SGW` | `ETM,LTM` | 0 "STREET" 1 "SPORT" 2 "TRACK" 3 "OFF" 4 "SNOW" 5 "OFFROAD" 6 "DRAG" 7 |
| FDCAN8 | `DIAGNOSTIC_REQUEST_DCSD.N_PDU` | This signal is used for diagnostic purposes | `TBM` | `SGW` | — |
| FDCAN8 | `DIAGNOSTIC_RESPONSE_DCSD.N_PDU` | This signal is used for diagnostic purposes | `SGW` | `TBM` | — |
| FDCAN8 | `ENGINE_FD_6.TerrainModeInterfaceButton_ECM` | Signal Indicates G/T or TRX Button activated or Not Activated by driver | `SGW` | `ETM` | 0 "Not_Activated" 1 "Activated" 5 "Short_to_Ground_Fault" 6 "Open_Shor |
| FDCAN8 | `IPC_FD_11.NextNavInstructionPanelTheme` | Next Nav Instruction Panel Theme | `SGW` | `ETM` | 0 "Analog" 1 "Digital" 15 "SNA" |
| FDCAN8 | `TELEMATIC_FD_11.HU_AirSusp_DnSw1` | Radio Air Susp Down Button Pressed | `ETM` | `SGW` | 0 "Not_Pressed" 1 "Pressed" |
| FDCAN8 | `TELEMATIC_FD_11.HU_AirSusp_UpSw1` | Radio Air Susp Up Button Pressed | `ETM` | `SGW` | 0 "Not_Pressed" 1 "Pressed" |
| FDCAN8 | `TELEMATIC_FD_11.HU_Front_PAMRequestSts` | Radio Front Park Assist Button Pressed | `ETM` | `SGW` | 0 "Not_Pressed" 1 "Pressed" |
| FDCAN8 | `TELEMATIC_FD_11.HU_Iterate_Gain_Down` | Radio Trailer Brake Gain Down Button Pressed | `ETM` | `SGW` | 0 "Not_Pressed" 1 "Pressed" |
| FDCAN8 | `TELEMATIC_FD_11.HU_Iterate_Gain_Up` | Radio Trailer Brake Gain Up Button Pressed | `ETM` | `SGW` | 0 "Not_Pressed" 1 "Pressed" |
| FDCAN8 | `TELEMATIC_FD_11.HU_Rear_PAMRequestSts` | Radio Rear Park Assist Button Pressed | `ETM` | `SGW` | 0 "Not_Pressed" 1 "Pressed" |
| FDCAN8 | `TELEMATIC_FD_11.HU_TRSC_EnableBtn_Sts` | Radio TRSC Enable Button Pressed | `ETM` | `SGW` | 0 "Not Pressed" 1 "Pressed" 2 "SNA" |
| FDCAN8 | `TELEMATIC_FD_11.Launch_RPM_Selected_Setting` | Soft button driver selected RPM setting | `ETM` | `Vector__XXX` | 30 "30 = DEFAULT" 31 "31 = SNA" |
| FDCAN8 | `TELEMATIC_FD_11.Launch_Sft_Btn_status` | Launch - soft button status; Launch on = [1] | `ETM` | `SGW` | — |
| FDCAN8 | `TELEMATIC_FD_13.HU_Worksite_Inverter_RadioSwitch` | Inverter Soft Button switch; [1] = ON | `ETM` | `SGW` | 0 "OFF" 1 "ON" |
| FDCAN8 | `TELEMATIC_FD_15.Center_Cluster_Button_function` | Value / text to be shown in Center steering wheel button on cluster | `ETM` | `SGW` | 0 "Blank" 1 "Previous" 2 "Next" 3 "Pause/Play" 4 "Tune -" 5 "Tune +" 6 |
| FDCAN8 | `TELEMATIC_FD_15.Left_Cluster_Button_function` | Value / text to be shown in left steering wheel button on cluster | `ETM` | `SGW` | 0 "Blank" 1 "Previous" 2 "Next" 3 "Pause/Play" 4 "Tune -" 5 "Tune +" 6 |
| FDCAN8 | `TELEMATIC_FD_15.Right_Cluster_Button_function` | Value / text to be shown in Right steering wheel button on cluster | `ETM` | `SGW` | 0 "Blank" 1 "Previous" 2 "Next" 3 "Pause/Play" 4 "Tune -" 5 "Tune +" 6 |
| FDCAN8 | `TELEMATIC_FD_5.CM_TCH_PT_VES2` | Touch screen pointer for rear seat entertainment | `ETM` | `Vector__XXX` | — |
| FDCAN8 | `TELEMATIC_FD_5.CM_TCH_STAT` | Touch Screen Status | `ETM` | `SGW` | 0 "TCH_NOT_PSD" 1 "TCH_PSD" 2 "TCH_PS_CAN" 3 "Not_Used" 4 "TCH_CFG_RES |
| FDCAN8 | `TELEMATIC_FD_5.CM_TCH_X_COORD` | Value for the touch screen X axis coordinates | `ETM` | `SGW` | — |
| FDCAN8 | `TELEMATIC_FD_5.CM_TCH_Y_COORD` | Value for the touch screen Y axis coordinates | `ETM` | `SGW` | — |
| FDCAN8 | `TELEMATIC_VEHICLE_SETUP.GreetingLightsEnable_Req` | This signal is managed when the button of block or unblocking of the door is pressed. | `ETM` | `SGW` | 0 "True" 1 "False" |

> ⚠ 其中 **0 個無 `CM_` 註解** —— 依 R-P390(b)「`CM_` 無明述者不選」，該等候選**不可選**，列此僅為完整性。
