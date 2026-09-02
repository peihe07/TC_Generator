# SWE1-VC-FrontParkSenseVolume-021

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Park Sense
- TC 數: 1

**reasoning**：驗證 Park Sense Setting、Rear Park Sense Volume、Front Park Sense Volume 三項功能皆不支援時，TLM 三個選單項皆不顯示、皆不可存取，且不發出任何屬性請求。關鍵情境為 PROXI CAN node 24 (PAM) 不存在之總 ELSE 分支（規格段 1242–1243）。本 Req 明述三個選單項為同一條件下之同時結果，依 §8.2.2 不拆為三條，以多階段 ER 表達。「不發出屬性請求」以匯流排上無請求訊號觀察（R-P353 白名單 (i)）。

## TC 1 — All three Park Sense menu items hidden when PAM node is Absent

### test_item
```
If the features are not supported, shall not display the **Park Sense Setting**, **Rear Park Sense Volume**, and **Front Park Sense Volume** menu items. The user shall not be able to access or modify these settings, and the HMI shall not issue any property request for these features
(PAM node absent suppresses all three menu items and the request signal)
```

### pre_conditions
1. PROXI CAN node 24 (PAM) = 0 (Absent)
2. The TLM is in the Vehicle Settings menu

### input_test_data
NA

### test_procedure
1. Read the named UI element "Vehicle Settings" menu list and check that it does not contain "Park Sense Setting"
2. Read the named UI element "Vehicle Settings" menu list and check that it does not contain "Rear Park Sense Volume"
3. Read the named UI element "Vehicle Settings" menu list and check that it does not contain "Front Park Sense Volume"
4. Read the signal $TELEMATIC_VEHICLE_SETUP.PamAlertMode_Req$ and check that it is not transmitted

### expected_result
1. The named UI element "Park Sense Setting" is not present in the "Vehicle Settings" menu list
2. The named UI element "Rear Park Sense Volume" is not present in the "Vehicle Settings" menu list
3. The named UI element "Front Park Sense Volume" is not present in the "Vehicle Settings" menu list
4. No value of $TELEMATIC_VEHICLE_SETUP.PamAlertMode_Req$ is received

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.29; Sys-RA-VF665_V42_VSM-809
- design_method: 負向測試 (Negative / Invalid)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — CAN node 24 (PAM) = 0 (Absent) 之總 ELSE，涵蓋三個選單項，與 -013／-020 之單一功能不支援不同範圍
- remarks: PROXI parameter name is written as the spec names it. The verbatim entry in PROXI_HDCC27_R3 Format r30 column F is "CAN node 24 (PAM/CVADAS)" with 0 = Absent and 1 = Present; the spec writes "CAN node 24 (PAM )". The spec name is kept per R-13 and the PROXI anchor is recorded here rather than substituted. UI element names are taken from the menu item wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. specification_reference uses the upstream Sys-RA id per R-VL19(b): the spec has no chapter heading for this family (upstream package 04 W-8 measured zero headings containing "Volume")
