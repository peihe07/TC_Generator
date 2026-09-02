# SWE1-VC-EPBMaintenanceMode-044

- Test Group: Vehicle Setup Management R1 Low
- Test Set: EPB Maintenance Mode
- TC 數: 1

**reasoning**：驗證 PROXI 參數 EPB_Maintenance_Menu 為 Absent 時，TLM 不顯示 EPB Maintenance Mode 選單項且使用者無法設定。關鍵情境為 PROXI 值 0 (Absent) 之組態分支，屬功能可用性之閘門。本 Req 只述單一 PROXI 值之結果，故 1 條即足；其對偶值 Present 由 -045 覆蓋（§8.2.1 不擴入兄弟）。EPB_Maintenance_Menu 之段 1 命中 PROXI Format r585c F 逐字，依 R-P375(c) 走 PROXI 路徑，不寫 $。

## TC 1 — EPB Maintenance Mode menu hidden when PROXI is Absent

### test_item
```
TLM receives the value as "Absent" via signal, $EPB_Maintenance_Menu$ Then TLM shall not display the EPB Maintenance Mode menu item in the Vehicle Settings menu, and the customer shall not be able to perform any setting
(PROXI Absent branch: menu item suppressed and not operable)
```

### pre_conditions
1. PROXI EPB_Maintenance_Menu = 0 (Absent)
2. The TLM is in the Vehicle Settings menu

### input_test_data
NA

### test_procedure
1. Read the named UI element "Vehicle Settings" menu list and check that it does not contain "EPB Maintenance Mode"
2. Attempt to select "EPB Maintenance Mode" in the "Vehicle Settings" menu list

### expected_result
1. The named UI element "EPB Maintenance Mode" is not present in the "Vehicle Settings" menu list
2. The named UI element "EPB Maintenance Mode" cannot be selected and no setting screen is displayed

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19
- design_method: 負向測試 (Negative / Invalid)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — PROXI EPB_Maintenance_Menu = 0 (Absent)，與 -045 之 1 (Present) 對偶
