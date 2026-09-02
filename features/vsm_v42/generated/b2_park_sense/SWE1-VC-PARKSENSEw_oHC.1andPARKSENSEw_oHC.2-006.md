# SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-006

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Park Sense
- TC 數: 1

**reasoning**：驗證 PROXI 參數 CAN node 24 (PAM) 為 Present 時，TLM 顯示 Park Sense Setting 選單項且使用者可設定。關鍵情境為 PROXI 組態分支，屬功能可用性之閘門（規格段 1203–1204）。本 Req 只述單一 PROXI 值之結果，1 條即足；不支援之對偶由 -021 覆蓋（§8.2.1 委任）。本條與 -002 之 037 Description 逐字相同，依 §8.2.2 各出一條不合併，括號下半區分（§K K-7）。

## TC 1 — Park Sense Setting menu shown when PAM node is Present

### test_item
```
If $CAN node 24 (PAM )$ = [Present], the TLM shall display the corresponding customer setting and the user can perform the setting
(PROXI Present branch re-stated by a second requirement id)
```

### pre_conditions
1. PROXI CAN node 24 (PAM) = 1 (Present)
2. The TLM is in the Vehicle Settings menu

### input_test_data
NA

### test_procedure
1. Read the named UI element "Vehicle Settings" menu list and check that it contains "Park Sense Setting"
2. Select "Park Sense Setting" in the "Vehicle Settings" menu list
3. Read the named UI element "Park Sense Setting" control and check that it is enabled

### expected_result
1. The named UI element "Park Sense Setting" is present in the "Vehicle Settings" menu list
2. The named UI element "Park Sense Setting" screen is displayed
3. The named UI element "Park Sense Setting" control is enabled for the customer

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.29
- design_method: 功能測試 (Functional based ; no specific technique)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — 同 -002 之 PROXI 條件；本條為同文對之第二列（§K K-7），括號下半以「第二個需求 id」區分
- remarks: PROXI parameter name is written as the spec names it. The verbatim entry in PROXI_HDCC27_R3 Format r30 column F is "CAN node 24 (PAM/CVADAS)" with 0 = Absent and 1 = Present; the spec writes "CAN node 24 (PAM )". The spec name is kept per R-13 and the PROXI anchor is recorded here rather than substituted. UI element names are taken from the menu item wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List
