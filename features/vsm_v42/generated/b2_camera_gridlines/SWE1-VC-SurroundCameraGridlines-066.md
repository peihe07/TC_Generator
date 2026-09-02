# SWE1-VC-SurroundCameraGridlines-066

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Camera Gridlines
- TC 數: 1

**reasoning**：驗證使用者將 Surround View Camera (SVC) Gridlines 設為 Off 時，TLM 送出規格所載之請求訊號並更新顯示之設定。關鍵情境為單一設定值之等價分割。本 Req 只述一個值，依 §8.2.2 一 Req 一條。規格所載之 TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req 於主 DBC 查無，其正確拼法 SVC_Guidelines_Req 存在（BO_1291），依 R-VL16(a) 記「規格拼字疑誤」—— 本條保留規格原名不加 $、不附 label，並以具名 UI 元件為可觀察面（R-P353 白名單 (ii)）。

## TC 1 — SVC Gridlines set to Off

### test_item
```
The HMI layer shall capture the customer selection for the **Surround View Camera (SVC) Gridlines** setting and send the request using CarPropertyManager.setProperty() with the TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req signal value set to **Off**
(SVC Gridlines set to Off is requested and displayed)
```

### pre_conditions
1. PROXI Surround_View_Camera = 1 (Present)
2. The named UI element "Surround View Camera (SVC) Gridlines" setting screen is displayed

### input_test_data
NA

### test_procedure
1. Select "Surround View Camera (SVC) Gridlines" = "Off"
2. Read the named UI element "Surround View Camera (SVC) Gridlines" control and check that it is "Off"
3. PENDING: DR-VL4 TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req

### expected_result
1. The named UI element "Surround View Camera (SVC) Gridlines" control accepts the selection "Off"
2. The named UI element "Surround View Camera (SVC) Gridlines" control is "Off"
3. PENDING: DR-VL4 TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.38
- design_method: 等價劃分 (Equivalence Partitioning, EP)
- priority: P2
- split_flag: False
- distinguishing_axis: input_data — SVC Gridlines = Off，與同族另一值為等價類之不同分割
- remarks: UI element names are taken from the setting wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. The spec and the 037 name the request signal TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req, which the ATL-Mi DBC does not define; the DBC spells it SVC_Guidelines_Req (BO_1291, VAL_ 0 = Off, 1 = On). Classified as spec spelling suspect per R-VL16(a), so the spec name is kept without $ and no label is written; see section K
