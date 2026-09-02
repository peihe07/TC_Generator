# SWE1-VC-SurroundCameraGridlines-064

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Camera Gridlines
- TC 數: 1

**reasoning**：驗證 PROXI 參數 Surround_View_Camera 為 Absent 時，TLM 不顯示 Surround View Camera (SVC) Gridlines 設定。關鍵情境為 PROXI 組態分支。本 Req 只述單一 PROXI 值之結果，1 條即足；對偶值由同族另一條覆蓋（§8.2.1）。Surround_View_Camera 之段 1 命中 PROXI Format r761 逐字（0 = Absent／1 = Present），走 PROXI 路徑不加 $。

## TC 1 — SVC Gridlines setting hidden when surround camera PROXI is Absent

### test_item
```
If $Surround_View_Camera$ = [Absent], the TLM shall not display the corresponding customer setting
(PROXI Absent branch: the SVC Gridlines setting is not offered)
```

### pre_conditions
1. PROXI Surround_View_Camera = 0 (Absent)
2. The TLM is in the Vehicle Settings menu

### input_test_data
NA

### test_procedure
1. Read the named UI element "Vehicle Settings" menu list and check that it does not contain "Surround View Camera (SVC) Gridlines"
2. Attempt to select "Surround View Camera (SVC) Gridlines" in the "Vehicle Settings" menu list

### expected_result
1. The named UI element "Surround View Camera (SVC) Gridlines" is not present in the "Vehicle Settings" menu list
2. The named UI element "Surround View Camera (SVC) Gridlines" cannot be selected and no setting screen is displayed

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.38
- design_method: 負向測試 (Negative / Invalid)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — PROXI Surround_View_Camera = 0 (Absent)，與 -065 之 1 (Present) 對偶
- remarks: PROXI anchor: PROXI_HDCC27_R3 Format r761 column F is "Surround_View_Camera" with 0 = Absent and 1 = Present (verbatim match). UI element names are taken from the setting wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List
