# SWE1-VC-FrontParkSenseVolume-019

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Park Sense
- TC 數: 1

**reasoning**：驗證 TLM 收到 $IPC_VEHICLE_SETUP.PamChimeVolumeFront$ 時，經內部訊號 TLM_Vehicle_Setup_Menu.Info 更新 Front Park Sense Volume 之顯示。關鍵情境為 IPC 回報後之畫面更新（規格段 1238–1239）。本條驗三個音量值之顯示，其為同一機制之不同輸入，依 §8.2.2 不拆。TLM_Vehicle_Setup_Menu.Info 於 v3 為未解得(止於段1)，依 R-P355(c) 該步寫 PENDING。

## TC 1 — Front volume display follows the IPC reported value

### test_item
```
The HMI layer shall evaluate the received `IPC_VEHICLE_SETUP.PamChimeVolumeFront signal, update the TLM_Vehicle_Setup_Menu.Info internal signal, and display the **Front Park Sense Volume** setting information accordingly within <TDisplay>
(Reported front volume drives the displayed control at both ends of the range)
```

### pre_conditions
1. PROXI CAN node 24 (PAM) = 1 (Present)
2. The named UI element "Front Park Sense Volume" screen is displayed

### input_test_data
NA

### test_procedure
1. Send the signal $IPC_VEHICLE_SETUP.PamChimeVolumeFront$ = 0 (Low)
2. Read the named UI element "Front Park Sense Volume" control and check that it is "Low"
3. Send the signal $IPC_VEHICLE_SETUP.PamChimeVolumeFront$ = 2 (High)
4. Read the named UI element "Front Park Sense Volume" control and check that it is "High"
5. PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info

### expected_result
1. The signal $IPC_VEHICLE_SETUP.PamChimeVolumeFront$ = 0 (Low) is registered without a bus error
2. The named UI element "Front Park Sense Volume" control is "Low"
3. The signal $IPC_VEHICLE_SETUP.PamChimeVolumeFront$ = 2 (High) is registered without a bus error
4. The named UI element "Front Park Sense Volume" control is "High"
5. PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.29; Sys-RA-VF665_V42_VSM-807
- design_method: 狀態轉換 (State Transition Testing)
- priority: P2
- split_flag: False
- distinguishing_axis: trigger_state — 由 IPC 回報之 PamChimeVolumeFront 驅動顯示，與同族之 HMI 送出方向相反
- remarks: UI element names are taken from the menu item wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. TLM_Vehicle_Setup_Menu.Info is unresolved at stage 1 in signal_chain_v42_v3.tsv; observation method requested under DR-VL4. specification_reference uses the upstream Sys-RA id per R-VL19(b): the spec has no chapter heading for this family (upstream package 04 W-8 measured zero headings containing "Volume")
