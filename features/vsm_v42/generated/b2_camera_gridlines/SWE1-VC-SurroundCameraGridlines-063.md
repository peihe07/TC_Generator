# SWE1-VC-SurroundCameraGridlines-063

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Camera Gridlines
- TC 數: 1

**reasoning**：本 leaf 於 037 之 Requirement Description **只有家族標題「Surround Camera Gridlines」一句，無需求文本**，故無可驗之行為、無可取之 verbatim 句。依 §8.4.1 不得造需求，依 privacy R34-3 之先例仍寫入一列而非略過 —— leaf 自交付件消失會在追溯表留下無說明之洞。本列四欄全為 PENDING，錨 DR-VL2(c)。另佐證：其 Source ID 於 SYSRA 之 Category 為 Heading（A-VL7），與此互相印證為上游誤標。

## TC 1 — Surround Camera Gridlines requirement text absent upstream

### test_item
```
Surround Camera Gridlines
(Blocked: the 037 description carries only the family title, so no behaviour is specified)
```

### pre_conditions
1. PENDING: DR-VL2 SWE1-VC-SurroundCameraGridlines-063

### input_test_data
NA

### test_procedure
1. PENDING: DR-VL2 SWE1-VC-SurroundCameraGridlines-063
2. PENDING: DR-VL2 SWE1-VC-SurroundCameraGridlines-063

### expected_result
1. PENDING: DR-VL2 SWE1-VC-SurroundCameraGridlines-063
2. PENDING: DR-VL2 SWE1-VC-SurroundCameraGridlines-063

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.38
- design_method: 功能測試 (Functional based ; no specific technique)
- priority: P3
- split_flag: False
- distinguishing_axis: mode — 本列為 BLOCKED —— 037 描述僅家族標題、無需求文本，故無可驗行為；與同族其餘五條（皆有具體 PROXI 分支或設定值）在可驗性上即為不同類。依 §4.6 不設 axis=none —— 該值蘊含 duplicate_of，而本列非任何列之重複
- remarks: BLOCKED. The 037 Requirement Description for this leaf is the family title only, with no requirement sentence, so no behaviour can be derived without fabricating one (IN 8.4.1). The row is written rather than skipped so the traceability table shows the gap (privacy R34-3 precedent). Its Source Requirement ID is categorised Heading in the SYSRA (A-VL7), which corroborates an upstream mislabel. Anchored to DR-VL2(c)
