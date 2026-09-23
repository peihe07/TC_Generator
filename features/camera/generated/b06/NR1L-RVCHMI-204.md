# NR1L-RVCHMI-204 — SWE1-RVC-133

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.1.5.1`（來源列 `NRL-188163`）

## test_item 上半（verbatim，SYS1 逐字）

> RearView Camera, Cargo Camera, and Apps Page

## reasoning

**補生成之由**：拆解審計 **CAM-22 §5 #4**（`confidence = M`）—— §34.1.5.1 列舉三項（`RearView Camera, Cargo Camera, and Apps Page`），母列 `NR1L-RVCHMI-085` 驗前兩項之並存，而 `Apps Page` 只被當作**入口**用（Procedure 之第 1 步），未被當作**被列舉之項**驗。本列以該項為驗證標的。`Digital_CHMSL_Camera_Prsnt` 只存在於 Atl-Hi 三本 → **R-CAM18(b)** 三個 Atl-Mi 欄判 `0`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Rear_View_Camera = 1 (Present)
6. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
7. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Read the App Drawer and check that a camera entry for the Apps Page access point is present
3. Select that camera entry
4. Read the HU display and check that the camera view is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. A camera entry is present in the App Drawer, which is the Apps Page access point
3. The camera entry registers the selection
4. The camera view is displayed
```
