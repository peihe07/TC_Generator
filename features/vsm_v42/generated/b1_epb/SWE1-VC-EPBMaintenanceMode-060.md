# SWE1-VC-EPBMaintenanceMode-060

- Test Group: Vehicle Setup Management R1 Low
- Test Set: EPB Maintenance Mode
- TC 數: 1

**reasoning**：驗證 TLM 收到 IPC_VEHICLE_SETUP2.EPB_MaintenanceMode 訊息時，經內部訊號 TLM_Vehicle_Setup_Menu.Info 更新 Vehicle Setup 選單畫面之文字與圖示狀態。關鍵情境為訊息接收後之選單畫面更新。本 Req 與 -058 之差別在下游對象（選單畫面 vs 顯示控制器），故各自一條，不合併。TLM_Vehicle_Setup_Menu.Info 段 1 未解，該步 PENDING；畫面更新以具名 UI 元件觀察（R-P353 白名單 (ii)）。

## TC 1 — Vehicle Setup menu updated on EPB_MaintenanceMode message reception

### test_item
```
When the TLM receives the message via signal (IPC_VEHICLE_SETUP2.EPB_MaintenanceMode), Then TLM shall update and send the display information to the menu sub-system through the internal signal (TLM_Vehicle_Setup_Menu.Info)
(Menu status text tracks the received EPB_MaintenanceMode value in both directions)
```

### pre_conditions
1. PROXI EPB_Maintenance_Menu = 1 (Present)
2. The EPB Maintenance Mode menu item is displayed

### input_test_data
NA

### test_procedure
1. Send the signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On)
2. Read the named UI element "EPB Maintenance Mode" status text in the "Vehicle Settings" menu and check that it is "On"
3. Send the signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 0 (Off)
4. Read the named UI element "EPB Maintenance Mode" status text in the "Vehicle Settings" menu and check that it is "Off"
5. PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info

### expected_result
1. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On) is registered without a bus error
2. The named UI element "EPB Maintenance Mode" status text in the "Vehicle Settings" menu is "On"
3. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 0 (Off) is registered without a bus error
4. The named UI element "EPB Maintenance Mode" status text in the "Vehicle Settings" menu is "Off"
5. PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19
- design_method: 狀態轉換 (State Transition Testing)
- priority: P2
- split_flag: False
- distinguishing_axis: mode — 下游對象為 Vehicle Setup 選單畫面，與 -058 之顯示控制器不同
- remarks: TLM_Vehicle_Setup_Menu.Info is unresolved at stage 1; observation method requested under DR-VL4
