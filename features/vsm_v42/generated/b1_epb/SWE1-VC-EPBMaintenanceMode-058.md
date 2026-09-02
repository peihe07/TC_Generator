# SWE1-VC-EPBMaintenanceMode-058

- Test Group: Vehicle Setup Management R1 Low
- Test Set: EPB Maintenance Mode
- TC 數: 1

**reasoning**：驗證 $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ 為 1 (On) 時，TLM 經內部訊號 EPB_MaintenanceMode_Active.Info 將狀態送至顯示控制器。關鍵情境為 On 狀態下之內部狀態傳遞。該內部訊號於 v3 為未解得(止於段1)：LID／HMI Settings／PROXI 三處皆無段 1 依據，依 R-P355(c) 該步寫 PENDING，不得以 Set X.Info 假裝可執行。可觀察之上游 CAN 訊號仍逐步驗證，故本條非全 PENDING。

## TC 1 — EPB Maintenance Mode active state forwarded to the display controller

### test_item
```
When the TLM receives the value [On] via signal (IPC_VEHICLE_SETUP2.EPB_MaintenanceMode), the TLM shall update and send the status to the display controller through the internal signal (EPB_MaintenanceMode_Active.Info)
(Steady On state propagates to the display controller over an internal signal)
```

### pre_conditions
1. PROXI EPB_Maintenance_Menu = 1 (Present)
2. The EPB Maintenance Mode menu item is displayed

### input_test_data
NA

### test_procedure
1. Send the signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On)
2. Read the signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ and check that it is 1 (On)
3. PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info

### expected_result
1. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On) is registered without a bus error
2. The signal value $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On) is received
3. PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19
- design_method: 功能測試 (Functional based ; no specific technique)
- priority: P2
- split_flag: False
- distinguishing_axis: trigger_state — IPC_VEHICLE_SETUP2.EPB_MaintenanceMode 持續為 1 (On)，與 -047 之 Off→On 變遷不同
- remarks: EPB_MaintenanceMode_Active.Info is unresolved at stage 1 in signal_chain_v42_v3.tsv; observation method requested under DR-VL4
