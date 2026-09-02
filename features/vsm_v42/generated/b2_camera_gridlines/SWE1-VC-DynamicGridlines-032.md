# SWE1-VC-DynamicGridlines-032

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Camera Gridlines
- TC 數: 1

**reasoning**：驗證使用者將 Dynamic Grid 設為 On 時，TLM 依所請求之值更新顯示之設定。關鍵情境為單一設定值之等價分割。本 Req 只述一個值，依 §8.2.2 一 Req 一條，不與另一值合併。規格所述之對象 DynamicGrid.Req 為內部訊號，於 v3 為未解得(止於段1) —— LID／HMI Settings／PROXI 三處段 1 皆無依據，依 R-P355 不得直接 Set，故以 UI 選擇為驅動、以具名 UI 元件為觀察（R-P353 白名單 (ii)），並於一步記 PENDING 揭露該內部訊號無觀察面。

## TC 1 — Dynamic Grid set to On

### test_item
```
The HMI layer shall capture the customer selection for the **Dynamic Grid** setting and send the request using CarPropertyManager.setProperty() with the DynamicGrid.Req property value set to **On**
(Dynamic Grid set to On is recorded and displayed)
```

### pre_conditions
1. PROXI Rear_View_Camera = 1 (Present)
2. The named UI element "Dynamic Grid" setting screen is displayed

### input_test_data
NA

### test_procedure
1. Select "Dynamic Grid" = "On"
2. Read the named UI element "Dynamic Grid" control and check that it is "On"
3. PENDING: DR-VL4 DynamicGrid.Req

### expected_result
1. The named UI element "Dynamic Grid" control accepts the selection "On"
2. The named UI element "Dynamic Grid" control is "On"
3. PENDING: DR-VL4 DynamicGrid.Req

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.31
- design_method: 等價劃分 (Equivalence Partitioning, EP)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — Dynamic Grid = On，與同族另一值為等價類之不同分割
- remarks: UI element names are taken from the setting wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. DynamicGrid.Req is unresolved at stage 1; observation method requested under DR-VL4
