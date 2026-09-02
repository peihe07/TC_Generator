# SWE1-VC-DynamicGridlines-030

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Camera Gridlines
- TC 數: 1

**reasoning**：驗證 PROXI 參數 Rear_View_Camera 為 Present 時，TLM 顯示 Dynamic Grid 設定且使用者可設定。關鍵情境為 PROXI 組態分支，屬功能可用性之閘門。本 Req 只述單一 PROXI 值之結果，1 條即足；其對偶值由同族另一條覆蓋（§8.2.1 委任）。Rear_View_Camera 之段 1 命中 PROXI Format r401 逐字（0 = Absent／1 = Present），依 R-P375(c) 走 PROXI 路徑，不加 $。

## TC 1 — Dynamic Grid setting shown when rear camera PROXI is Present

### test_item
```
If $Rear_View_Camera$ = [Present], the TLM shall display the corresponding customer setting and the user can perform the setting
(PROXI Present branch: the Dynamic Grid setting is offered and operable)
```

### pre_conditions
1. PROXI Rear_View_Camera = 1 (Present)
2. The TLM is in the Vehicle Settings menu

### input_test_data
NA

### test_procedure
1. Read the named UI element "Vehicle Settings" menu list and check that it contains "Dynamic Grid"
2. Select "Dynamic Grid" in the "Vehicle Settings" menu list
3. Read the named UI element "Dynamic Grid" control and check that it is enabled

### expected_result
1. The named UI element "Dynamic Grid" is present in the "Vehicle Settings" menu list
2. The named UI element "Dynamic Grid" setting screen is displayed
3. The named UI element "Dynamic Grid" control is enabled for the customer

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.31
- design_method: 功能測試 (Functional based ; no specific technique)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — PROXI Rear_View_Camera = 1 (Present)，與 -029 之 0 (Absent) 對偶
- remarks: PROXI anchor: PROXI_HDCC27_R3 Format r401 column F is "Rear_View_Camera" with 0 = Absent and 1 = Present (verbatim match). UI element names are taken from the setting wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List
