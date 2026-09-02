# SWE1-VC-EPBMaintenanceMode-059

- Test Group: Vehicle Setup Management R1 Low
- Test Set: EPB Maintenance Mode
- TC 數: 1

**reasoning**：驗證車速自 <= V_Car_Moving 上升至 > V_Car_Moving 時，TLM 經 ServiceMode_Popup_Trigger.Info 送出版面請求並顯示對應 popup。關鍵情境為車速跨越門檻之邊界；V_Car_Moving = 4 km/h、容差 0.5 km/h 取自規格常數表（段 1662），故取 raw 64 與 65 兩點（後者為 DBC 解析度 0.0625 km/h 之最小上跨）。test_item 上半為 037 Requirement Description 之完整原句 verbatim（R-VL23(a)），其所含之 ignition Off→On 或分支本 TC 未涵蓋 —— 037 寫 (Ignition_{S}tatus) 為佔位符殘留、規格段 1111 拼作 Inigtion，皆非合法訊號名，依 §8.4.1 不臆造，揭露見 remarks 與 §K K-3。內部訊號 ServiceMode_Popup_Trigger.Info 於 v3 為未解得(止於段1)，依 R-P355(c) 該步寫 PENDING，不得以 Set X.Info 假裝可執行。

## TC 1 — Vehicle speed crosses V_Car_Moving upward

### test_item
```
When the TLM receives a value changing from <= [V_Car_Moving] to > [V_Car_Moving], or a transition from [Ignition Off] to [Ignition On] via signals (STATUS_CCAN3.VehicleSpeedVSOSig) | (Ignition_{S}tatus), Then TLM shall send a layout request to the display manager through internal signal (ServiceMode_Popup_Trigger.Info)
(Boundary crossing of V_Car_Moving raises the brake-pedal popup)
```

### pre_conditions
1. PROXI EPB_Maintenance_Menu = 1 (Present)
2. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 1 (On)
3. The vehicle is stationary

### input_test_data
NA

### test_procedure
1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 64
2. Read the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ and check that it is 64
3. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 65
4. Read the named UI element "Step on the brake pedal" pop-up and check that it is displayed
5. PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info

### expected_result
1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 64 is registered without a bus error
2. The signal value $STATUS_CCAN3.VehicleSpeedVSOSig$ = 64 is received
3. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 65 is registered without a bus error
4. The named UI element "Step on the brake pedal" pop-up is displayed
5. PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19
- design_method: 邊界值分析 (Boundary Value Analysis, BVA)
- priority: P1
- split_flag: False
- distinguishing_axis: boundary — 車速 raw 64 (= V_Car_Moving 4 km/h) 與 65 (> 門檻)，為門檻上跨之最小步進
- remarks: V_Car_Moving = 4 km/h per the spec constant table; raw 64 = 4 km/h and raw 65 = 4.0625 km/h at the DBC factor 0.0625 km/h. The ignition Off to On alternative branch is not covered: the spec names no signal for ignition status (see section K). ServiceMode_Popup_Trigger.Info is unresolved at stage 1; observation method requested under DR-VL4
