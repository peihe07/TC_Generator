# SWE1-VC-FrontParkSenseVolume-017

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Park Sense
- TC 數: 1

**reasoning**：驗證使用者將 Front Park Sense Volume 設為 Med 時，TLM 送出 $TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req$ = 1 (Medium) 至 IPC。關鍵情境為單一音量值之等價分割。本 Req 只述一個值，依 §8.2.2 一 Req 一條，不與其他值合併。規格觸發為內部訊號，依 R-P355 不得直接 Set，改以 UI 選擇觸發並驗其下游 CAN 訊號。規格與 037 寫 Med，DBC 之 VAL_ label 為 Medium，步驟採 DBC 寫法而 verbatim 上半保留來源原文（R-6）。

## TC 1 — Front Park Sense Volume set to Med

### test_item
```
The HMI layer shall capture the customer selection for the **PAM Chime Volume Front** setting and send the request using CarPropertyManager.setProperty() with the TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req` signal value set to **Med**
(Front chime volume Med is transmitted to the IPC)
```

### pre_conditions
1. PROXI CAN node 24 (PAM) = 1 (Present)
2. The named UI element "Front Park Sense Volume" screen is displayed

### input_test_data
NA

### test_procedure
1. Select "Front Park Sense Volume" = "Med" to trigger $TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req$ signal transmission
2. Read the named UI element "Front Park Sense Volume" control and check that it is "Med"

### expected_result
1. The signal value $TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req$ = 1 (Medium) is received
2. The named UI element "Front Park Sense Volume" control is "Med"

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.29; Sys-RA-VF665_V42_VSM-805
- design_method: 等價劃分 (Equivalence Partitioning, EP)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — Front 音量 = 1 (Medium)，與同族其他值為等價類之不同分割
- remarks: UI element names are taken from the menu item wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. The spec and the 037 description write the value as "Med"; the DBC VAL_ label is "Medium", so the step uses the DBC spelling while the verbatim half keeps the source wording (R-6). specification_reference uses the upstream Sys-RA id per R-VL19(b): the spec has no chapter heading for this family (upstream package 04 W-8 measured zero headings containing "Volume")
