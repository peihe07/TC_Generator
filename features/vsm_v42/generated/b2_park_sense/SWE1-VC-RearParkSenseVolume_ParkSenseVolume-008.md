# SWE1-VC-RearParkSenseVolume/ParkSenseVolume-008

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Park Sense
- TC 數: 1

**reasoning**：驗證 PROXI 之 CAN node 24 (PAM) 為 Present 且 PAM_Configuration 為 0 (Rear) or 1 (Front And Rear) 時，TLM 顯示 Rear Park Sense Volume 選單項且使用者可設定。關鍵情境為兩個 PROXI 參數之組合條件（規格段 1217–1218）。本 Req 只述可用之分支，1 條即足；不可用之分支由同族之不支援條覆蓋（§8.2.1 委任）。PAM_Configuration 之段 1 命中 PROXI Format r516 逐字（0 = Rear／1 = Front And Rear），依 R-P375(c) 走 PROXI 路徑不加 $。

## TC 1 — Rear Park Sense Volume menu shown for the matching PAM configuration

### test_item
```
If $CAN node 24 (PAM)$ = [Present], the TLM shall display the corresponding customer setting and the user can perform the setting
(Rear volume menu available when the PAM configuration covers the rear)
```

### pre_conditions
1. PROXI CAN node 24 (PAM) = 1 (Present)
2. PROXI PAM_Configuration = 0 (Rear) or 1 (Front And Rear)
3. The TLM is in the Vehicle Settings menu

### input_test_data
NA

### test_procedure
1. Read the named UI element "Vehicle Settings" menu list and check that it contains "Rear Park Sense Volume"
2. Select "Rear Park Sense Volume" in the "Vehicle Settings" menu list
3. Read the named UI element "Rear Park Sense Volume" control and check that it is enabled

### expected_result
1. The named UI element "Rear Park Sense Volume" is present in the "Vehicle Settings" menu list
2. The named UI element "Rear Park Sense Volume" screen is displayed
3. The named UI element "Rear Park Sense Volume" control is enabled for the customer

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.29; Sys-RA-VF665_V42_VSM-796
- design_method: 決策表 (Decision Table Testing)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — PAM_Configuration ∈ {0 (Rear), 1 (Front And Rear)}；與 -015 之 037 文字逐字相同，見 §K K-7，本條為該對之 Rear 側
- remarks: PROXI parameter name is written as the spec names it. The verbatim entry in PROXI_HDCC27_R3 Format r30 column F is "CAN node 24 (PAM/CVADAS)" with 0 = Absent and 1 = Present; the spec writes "CAN node 24 (PAM )". The spec name is kept per R-13 and the PROXI anchor is recorded here rather than substituted. UI element names are taken from the menu item wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. specification_reference uses the upstream Sys-RA id per R-VL19(b): the spec has no chapter heading for this family (upstream package 04 W-8 measured zero headings containing "Volume")
