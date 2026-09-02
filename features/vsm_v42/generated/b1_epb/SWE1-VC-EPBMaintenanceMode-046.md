# SWE1-VC-EPBMaintenanceMode-046

- Test Group: Vehicle Setup Management R1 Low
- Test Set: EPB Maintenance Mode
- TC 數: 1

**reasoning**：驗證使用者於 TLM 啟用 EPB Maintenance Mode 時，TLM 送出 $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ = 1 (On)、設定狀態顯示 On、並顯示 Initializing popup。關鍵情境為 UI 觸發之送出行為，該訊號 v3 判定解得（BO_162／VAL_ 2 項）。本 Req 之同時效果依 IN §5.7 與 R-VL21(b) 收於一條，以多階段 ER 表達，不拆。T_EPB_MM 之到期效果不在本條驗（timer 為內部態、不可觀察，§6），由 -053 驗（§8.2.1 委任）。test_item 上半之 037 文字寫 TLM receives，係自 TLM 應用層視角描述收到使用者偏好；依 DBC 該訊號 BO_162 之發送方為 TLM、接收節點為 IPC，故本 TC 之方向為 TLM 送出，兩者不矛盾。

## TC 1 — EPB Maintenance Mode enabled from HMI → request sent and Initializing popup shown

### test_item
```
TLM receives the value as "On" via signal, $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ Then TLM shall: Update the EPB Maintenance Mode setting status to On. Activate and display the "Initializing" popup
(HMI On request: outgoing signal, Initializing popup and T_EPB_MM start)
```

### pre_conditions
1. PROXI EPB_Maintenance_Menu = 1 (Present)
2. The EPB Maintenance Mode menu item is displayed
3. The EPB Maintenance Mode setting is Off

### input_test_data
NA

### test_procedure
1. Select "EPB Maintenance Mode" = "On" to trigger $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ signal transmission
2. Read the named UI element "EPB Maintenance Mode" setting control and check that it is "On"
3. Read the named UI element "Initializing" pop-up and check that it is displayed

### expected_result
1. The signal value $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ = 1 (On) is received
2. The named UI element "EPB Maintenance Mode" setting control is "On"
3. The named UI element "Initializing" pop-up is displayed

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19
- design_method: 情境 / 用例 (Scenario / Use Case Testing)
- priority: P1
- split_flag: False
- distinguishing_axis: trigger_state — HMI 觸發送出 EPB_MaintenanceMode_Req = 1 (On)，與 -047 之接收 IPC 回報不同向
- remarks: UI element names are taken from the menu item and popup wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List
