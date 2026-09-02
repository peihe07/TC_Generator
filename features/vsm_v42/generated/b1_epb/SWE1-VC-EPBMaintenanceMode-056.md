# SWE1-VC-EPBMaintenanceMode-056

- Test Group: Vehicle Setup Management R1 Low
- Test Set: EPB Maintenance Mode
- TC 數: 1

**reasoning**：驗證 $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ 收到 10 時 TLM 顯示對應 popup。關鍵情境為單一回饋值之等價類（退出 Service Mode 相關分支）。本 Req 只述一個 Fdbk 值，依 §8.2.2 一 Req 一條。該值於 DBC 之 VAL_ 1486 無 label（只定義 0 與 31），依 §8.4.1 不造 label，寫 = 10 並於 Remarks 揭露。

## TC 1 — EPB Maintenance feedback = 10: exit blocked while vehicle in motion

### test_item
```
When the TLM receives the value 10 via signal, $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$, the TLM shall activate and display the popup: "Brake Service – To exit Service Mode, vehicle must not be in motion."
(Fdbk = 10: exit blocked while the vehicle is in motion)
```

### pre_conditions
1. PROXI EPB_Maintenance_Menu = 1 (Present)
2. The EPB Maintenance Mode menu item is displayed
3. The TLM is in the Vehicle Settings menu

### input_test_data
NA

### test_procedure
1. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 10
2. Read the named UI element "Brake Service - To exit Service Mode" and check that it is displayed
3. Read the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ and check that it is 10

### expected_result
1. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 10 is registered without a bus error
2. The named UI element "Brake Service - To exit Service Mode" is displayed
3. The signal value $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 10 is received

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19
- design_method: 等價劃分 (Equivalence Partitioning, EP)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — Fdbk 值 10（退出時車輛移動中），與同族其他 Fdbk 值為等價類之不同分割
- remarks: DBC has no VAL_ entry for this raw value (VAL_ 1486 EPB_Maintenance_Fdbk defines 0 and 31 only), so no label is written
