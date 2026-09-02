# SWE1-VC-EPBMaintenanceMode-056

- Test Group: Vehicle Setup Management R1 Low
- Test Set: EPB Maintenance Mode
- TC 數: 1

**reasoning**：驗證已發起退出 Service Mode 請求後，$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ 收到 10（退出時車輛移動中）時 TLM 顯示對應 popup。關鍵情境為單一回饋值之等價分割，且須先建立退出請求態 —— popup 文義為 user selected yes to exiting service mode，直接送 Fdbk 而無請求態有 FF 風險（§7），該態為步驟控制態不得入 Pre-Condition（§4.4），故以 Procedure 發起步建立（R-VL21(f)）。規格段只載進入側之請求訊號（1054），退出側無逐字依據，故發起步 ER 以 UI 設定狀態書寫、不臆造訊號（§8.4.1），此點列 §K；回讀步依 R-VL21(f) 末句削去。該值於 DBC 之 VAL_ 1486 無 label，依 §8.4.1 不造 label，寫 = 10 並於 remarks 揭露。

## TC 1 — EPB Maintenance feedback = 10: exit blocked while vehicle in motion

### test_item
```
When the TLM receives the value 10 via signal, $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$, the TLM shall activate and display the popup: "Brake Service – To exit Service Mode, vehicle must not be in motion."
(Fdbk = 10: exit blocked while the vehicle is in motion)
```

### pre_conditions
1. PROXI EPB_Maintenance_Menu = 1 (Present)
2. The EPB Maintenance Mode menu item is displayed
3. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 1 (On)

### input_test_data
NA

### test_procedure
1. Select "EPB Maintenance Mode" = "Off" to request the exit from Service Mode
2. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 10
3. Read the named UI element "Brake Service - To exit Service Mode" and check that it is displayed

### expected_result
1. The named UI element "EPB Maintenance Mode" setting control is "Off"
2. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 10 is registered without a bus error
3. The named UI element "Brake Service - To exit Service Mode" is displayed

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19
- design_method: 等價劃分 (Equivalence Partitioning, EP)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — Fdbk 值 10（退出時車輛移動中），與同族其他 Fdbk 值為等價類之不同分割
- remarks: DBC has no VAL_ entry for this raw value (VAL_ 1486 EPB_Maintenance_Fdbk defines 0 and 31 only), so no label is written. UI element names are taken from the menu item and popup wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. The exit request path is not stated verbatim in the spec section: paragraph 1054 states the entry request only, so the exit step is asserted through the UI control state and not through a request signal (see section K)
