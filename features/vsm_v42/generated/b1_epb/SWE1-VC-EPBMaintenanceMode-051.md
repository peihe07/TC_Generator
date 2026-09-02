# SWE1-VC-EPBMaintenanceMode-051

- Test Group: Vehicle Setup Management R1 Low
- Test Set: EPB Maintenance Mode
- TC 數: 1

**reasoning**：驗證 $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ 收到 5 時，TLM 顯示對應之拒絕進入 Service Mode popup 並重設 T_EPB_MM。關鍵情境為單一回饋值之等價類。本 Req 只述一個 Fdbk 值，依 §8.2.2 一 Req 一條，不與其他 Fdbk 值合併。該訊號 v3 解得，惟 DBC 之 VAL_ 1486 只定義 0 與 31，值 5 無 label，依 IN §8.4.1 不造 label，寫 = 5 並於 Remarks 揭露。

## TC 1 — EPB Maintenance feedback = 5: EPB switch is currently engaged

### test_item
```
When TLM receives the value "5" via signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$, TLM shall activate and display the popup indicating that the user selected Yes to enter Service Mode, but the EPB switch is currently engaged
(Fdbk = 5: second refusal code carrying the same EPB switch text as Fdbk = 4)
```

### pre_conditions
1. PROXI EPB_Maintenance_Menu = 1 (Present)
2. The EPB Maintenance Mode menu item is displayed
3. The TLM is in the Vehicle Settings menu

### input_test_data
NA

### test_procedure
1. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 5
2. Read the named UI element "EPB switch is currently engaged" and check that it is displayed
3. Read the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ and check that it is 5

### expected_result
1. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 5 is registered without a bus error
2. The named UI element "EPB switch is currently engaged" is displayed
3. The signal value $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 5 is received

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19
- design_method: 等價劃分 (Equivalence Partitioning, EP)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — Fdbk 值 5（規格文字與 4 相同，見 §K K-2），與同族其他 Fdbk 值為等價類之不同分割
- remarks: DBC has no VAL_ entry for this raw value (VAL_ 1486 EPB_Maintenance_Fdbk defines 0 and 31 only), so no label is written
