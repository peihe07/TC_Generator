# SWE1-VC-EPBMaintenanceMode-047

- Test Group: Vehicle Setup Management R1 Low
- Test Set: EPB Maintenance Mode
- TC 數: 1

**reasoning**：驗證 $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ 由 0 (Off) 變為 1 (On) 時，TLM 顯示「選擇 Yes 退出 Service Mode 且第一步為踩煞車踏板」之 popup 並重設 T_EPB_MM。關鍵情境為 IPC 側狀態變遷，屬狀態轉換型。本 Req 明述單一變遷（Off→On），依 §8.2.1 不擴入 On→Off。該訊號 v3 解得（BO_1486／VAL_ 0=Off、1=On），label 逐字取 DBC。

## TC 1 — IPC EPB_MaintenanceMode Off → On

### test_item
```
When TLM detects that the value of $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ has changed from "Off" to "On", TLM shall activate and display the popup indicating that the user selected Yes to exit Service Mode and that the first step is to step on the brake pedal
(IPC state transition Off to On drives the brake-pedal popup and T_EPB_MM reset)
```

### pre_conditions
1. PROXI EPB_Maintenance_Menu = 1 (Present)
2. The EPB Maintenance Mode menu item is displayed
3. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 0 (Off)

### input_test_data
NA

### test_procedure
1. Send the signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On)
2. Read the named UI element "Step on the brake pedal" pop-up and check that it is displayed
3. Read the signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ and check that it is 1 (On)

### expected_result
1. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On) is registered without a bus error
2. The named UI element "Step on the brake pedal" pop-up is displayed
3. The signal value $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On) is received

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19
- design_method: 狀態轉換 (State Transition Testing)
- priority: P1
- split_flag: False
- distinguishing_axis: trigger_state — IPC_VEHICLE_SETUP2.EPB_MaintenanceMode 由 0 (Off) 變 1 (On) 之變遷，與 -058 之持續 On 狀態不同
