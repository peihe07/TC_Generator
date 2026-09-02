# SWE1-VC-RearParkSenseVolume/ParkSenseVolume-013

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Park Sense
- TC 數: 1

**reasoning**：驗證 Rear Park Sense Volume 之功能不支援時，TLM 不顯示該選單項且使用者無法存取或修改。關鍵情境為功能不可用之負向分支（規格段 1227–1228 之 ELSE）。本 Req 只述不支援之結果，1 條即足；可用分支由 -008 覆蓋（§8.2.1 委任）。不可用之條件以 PROXI PAM_Configuration 表達（規格段 1217 之 AND 條件不成立）。

## TC 1 — Rear Park Sense Volume menu hidden when unsupported

### test_item
```
If the feature is not supported, the HMI layer shall not display the **Rear Park Sense Volume** menu item, and the user shall not be able to access or modify the setting
(Unsupported rear volume keeps the menu item hidden and unreachable)
```

### pre_conditions
1. PROXI CAN node 24 (PAM) = 1 (Present)
2. PROXI PAM_Configuration = 1 (Front And Rear) is not set and the rear configuration is absent
3. The TLM is in the Vehicle Settings menu

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
- remarks: UI element names are taken from the menu item wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. specification_reference uses the upstream Sys-RA id per R-VL19(b): the spec has no chapter heading for this family (upstream package 04 W-8 measured zero headings containing "Volume")
