# SWE1-VC-RearParkSenseVolume/ParkSenseVolume-009

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Park Sense
- TC 數: 1

**reasoning**：驗證使用者將 Rear Park Sense Volume 設為 Low 時，TLM 送出 $TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req$ = 0 (Low) 至 IPC。關鍵情境為單一音量值之等價分割。本 Req 只述一個值，依 §8.2.2 一 Req 一條，不與其他值合併。規格觸發為內部訊號，依 R-P355 不得直接 Set，改以 UI 選擇觸發並驗其下游 CAN 訊號。label 逐字取 DBC VAL_（0 = Low），與規格原文一致。

## TC 1 — Rear Park Sense Volume set to Low

### test_item
```
The HMI layer shall capture the customer selection for the PAM Chime Volume Rear setting and send the requestusing CarPropertyManager.setProperty() with the TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req signal value set to Low
(Rear chime volume Low is transmitted to the IPC)
```

### pre_conditions
1. PROXI CAN node 24 (PAM) = 1 (Present)
2. The named UI element "Rear Park Sense Volume" screen is displayed

### input_test_data
NA

### test_procedure
1. Select "Rear Park Sense Volume" = "Low" to trigger $TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req$ signal transmission
2. Read the named UI element "Rear Park Sense Volume" control and check that it is "Low"

### expected_result
1. The signal value $TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req$ = 0 (Low) is received
2. The named UI element "Rear Park Sense Volume" control is "Low"

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.29; Sys-RA-VF665_V42_VSM-797
- design_method: 等價劃分 (Equivalence Partitioning, EP)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — Rear 音量 = 0 (Low)，與同族其他值為等價類之不同分割
- remarks: UI element names are taken from the menu item wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. specification_reference uses the upstream Sys-RA id per R-VL19(b): the spec has no chapter heading for this family (upstream package 04 W-8 measured zero headings containing "Volume")
