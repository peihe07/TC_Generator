# SWE1-VC-RearParkSenseVolume/ParkSenseVolume-013

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Park Sense
- TC 數: 1

**reasoning**：驗證 Rear Park Sense Volume 之功能不支援時，TLM 不顯示該選單項且使用者無法存取或修改。關鍵情境為功能不可用之負向分支（規格段 1227–1228 之 ELSE）。本 Req 只述不支援之結果，1 條即足；可用分支由 -008 覆蓋（§8.2.1 委任）。不可用之條件以「功能不受車輛組態支援」之狀態表達 —— 037 只述 based on the corresponding vehicle configuration or feature availability，未指名 PROXI 值；規格段 1217 之 AND 條件無法僅由 PAM_Configuration 否定（其值域恰為 Rear 與 Front And Rear 兩值），該邏輯缺口列 §K，不臆測。

## TC 1 — Rear Park Sense Volume menu hidden when unsupported

### test_item
```
If the feature is not supported, the HMI layer shall not display the **Rear Park Sense Volume** menu item, and the user shall not be able to access or modify the setting
(Unsupported rear volume keeps the menu item hidden and unreachable)
```

### pre_conditions
1. The Rear Park Sense Volume feature is not supported by the vehicle configuration
2. The TLM is in the Vehicle Settings menu

### input_test_data
NA

### test_procedure
1. Read the named UI element "Vehicle Settings" menu list and check that it does not contain "Rear Park Sense Volume"
2. Attempt to select "Rear Park Sense Volume" in the "Vehicle Settings" menu list

### expected_result
1. The named UI element "Rear Park Sense Volume" is not present in the "Vehicle Settings" menu list
2. The named UI element "Rear Park Sense Volume" cannot be selected and no setting screen is displayed

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.29; Sys-RA-VF665_V42_VSM-801
- design_method: 負向測試 (Negative / Invalid)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — Rear 不支援之負向分支，與 -008 之可用分支對偶
- remarks: UI element names are taken from the menu item wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. specification_reference uses the upstream Sys-RA id per R-VL19(b): the spec has no chapter heading for this family (upstream package 04 W-8 measured zero headings containing "Volume"). The unsupported state is stated as a feature-availability condition because the 037 description says only "based on the corresponding vehicle configuration or feature availability" without naming PROXI values. The spec's own condition for this branch (paragraph 1217: node 24 Present AND PAM_Configuration Rear OR Front And Rear) cannot be falsified through PAM_Configuration alone, whose domain is exactly those two values — see section K
