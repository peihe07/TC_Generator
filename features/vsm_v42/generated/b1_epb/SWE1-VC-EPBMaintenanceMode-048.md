# SWE1-VC-EPBMaintenanceMode-048

- Test Group: Vehicle Setup Management R1 Low
- Test Set: EPB Maintenance Mode
- TC 數: 1

**reasoning**：驗證已發起進入 Service Mode 請求後，$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ 收到 2（車速非 0）時 TLM 顯示對應之拒絕 popup。關鍵情境為單一回饋值之等價分割，且須先建立請求態 —— popup 文義為 user selected yes to entering service mode，直接送 Fdbk 而無請求態有 FF 風險（§7），該態為步驟控制態不得入 Pre-Condition（§4.4），故以 Procedure 發起步建立（R-VL21(f)）。本 Req 只述一個 Fdbk 值，依 §8.2.2 一 Req 一條，不與其他值合併；發起步之 ER 依規格段 1054 之 TLM 送出請求訊號書寫，回讀步依 R-VL21(f) 末句削去（全族一致）。該值於 DBC 之 VAL_ 1486 無 label（只定義 0 與 31），依 §8.4.1 不造 label，寫 = 2 並於 remarks 揭露。

## TC 1 — EPB Maintenance feedback = 2: Vehicle speed is not 0 mph

### test_item
```
When TLM receives the value "2" via signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$, TLM shall activate and display the popup indicating that the user selected Yes to enter Service Mode, but the vehicle speed is not at 0 mph
(Fdbk = 2: entry refused because vehicle speed is not 0 mph)
```

### pre_conditions
1. PROXI EPB_Maintenance_Menu = 1 (Present)
2. The EPB Maintenance Mode menu item is displayed
3. The EPB Maintenance Mode setting is Off

### input_test_data
NA

### test_procedure
1. Select "EPB Maintenance Mode" = "On" to trigger $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ signal transmission
2. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 2
3. Read the named UI element "Vehicle speed is not 0 mph" and check that it is displayed

### expected_result
1. The signal value $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ = 1 (On) is received
2. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 2 is registered without a bus error
3. The named UI element "Vehicle speed is not 0 mph" is displayed

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19
- design_method: 等價劃分 (Equivalence Partitioning, EP)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — Fdbk 值 2（車速非 0），與同族其他 Fdbk 值為等價類之不同分割
- remarks: DBC has no VAL_ entry for this raw value (VAL_ 1486 EPB_Maintenance_Fdbk defines 0 and 31 only), so no label is written. UI element names are taken from the menu item and popup wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. The entry request step is based on spec paragraph 1054
