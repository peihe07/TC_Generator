# SWE1-VC-FrontParkSenseVolume-020

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Park Sense
- TC 數: 1

**reasoning**：驗證 Front Park Sense Volume 之功能不支援時，TLM 不顯示該選單項，且在收到表示支援之有效可用性狀態前不發出任何屬性請求。關鍵情境為功能不可用之負向分支（規格段 1240–1241 之 ELSE）。本 Req 只述 Front 單一功能之不支援，1 條即足；三功能同時不支援之情形由 -021 覆蓋（§8.2.1 委任）。「不發出屬性請求」以匯流排上無該請求訊號觀察（R-P353 白名單 (i)）。

## TC 1 — Front Park Sense Volume menu hidden when unsupported

### test_item
```
if the **Front Park Sense Volume** feature is not supported, shall not display the **Front Park Sense Volume** menu item. The user shall not be able to access or modify the setting, and the HMI shall not issue any property request for this feature
(Unsupported front volume hides the item and suppresses the request signal)
```

### pre_conditions
1. PROXI CAN node 24 (PAM) = 1 (Present)
2. PROXI PAM_Configuration = 0 (Rear)
3. The TLM is in the Vehicle Settings menu

### input_test_data
NA

### test_procedure
1. Read the named UI element "Vehicle Settings" menu list and check that it does not contain "Front Park Sense Volume"
2. Attempt to select "Front Park Sense Volume" in the "Vehicle Settings" menu list
3. Read the signal $TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req$ and check that it is not transmitted

### expected_result
1. The named UI element "Front Park Sense Volume" is not present in the "Vehicle Settings" menu list
2. The named UI element "Front Park Sense Volume" cannot be selected and no setting screen is displayed
3. No value of $TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req$ is received

### 其他
- specification_reference: Sys-RA-VF665_V42_VSM-808
- design_method: 負向測試 (Negative / Invalid)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — Front 單一功能不支援，與 -021 之三功能同時不支援不同範圍
- remarks: UI element names are taken from the menu item wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. specification_reference uses the upstream Sys-RA id per R-VL19(b): the spec has no chapter heading for this family (upstream package 04 W-8 measured zero headings containing "Volume")
