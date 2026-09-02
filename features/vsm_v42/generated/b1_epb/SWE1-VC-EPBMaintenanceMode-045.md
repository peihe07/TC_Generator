# SWE1-VC-EPBMaintenanceMode-045

- Test Group: Vehicle Setup Management R1 Low
- Test Set: EPB Maintenance Mode
- TC 數: 1

**reasoning**：驗證 PROXI 參數 EPB_Maintenance_Menu 為 Present 時，TLM 顯示 EPB Maintenance Mode 選單項且允許使用者修改設定。關鍵情境為 PROXI 值 1 (Present) 之組態分支。本 Req 只述單一 PROXI 值之結果，1 條即足；Absent 分支由 -044 覆蓋。依 §7 supported 與 negative 成對，本條與 -044 即為該對。

## TC 1 — EPB Maintenance Mode menu shown when PROXI is Present

### test_item
```
TLM receives the value as "Present" via signal, $EPB_Maintenance_Menu$ Then TLM shall display the EPB Maintenance Mode menu item in the Vehicle Settings menu and allow the customer to modify the setting
(PROXI Present branch: menu item shown and operable)
```

### pre_conditions
1. PROXI EPB_Maintenance_Menu = 1 (Present)
2. The TLM is in the Vehicle Settings menu

### input_test_data
NA

### test_procedure
1. Read the named UI element "Vehicle Settings" menu list and check that it contains "EPB Maintenance Mode"
2. Select "EPB Maintenance Mode" in the "Vehicle Settings" menu list
3. Read the named UI element "EPB Maintenance Mode" setting control and check that it is enabled

### expected_result
1. The named UI element "EPB Maintenance Mode" is present in the "Vehicle Settings" menu list
2. The named UI element "EPB Maintenance Mode" setting screen is displayed
3. The named UI element "EPB Maintenance Mode" setting control is enabled for the customer

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19
- design_method: 功能測試 (Functional based ; no specific technique)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — PROXI EPB_Maintenance_Menu = 1 (Present)，與 -044 之 0 (Absent) 對偶
