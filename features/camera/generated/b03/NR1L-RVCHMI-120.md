# NR1L-RVCHMI-120 — SWE1-RVC-108-01

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.8.1`（來源列 `NRL-188116`）

## test_item 上半（verbatim，SYS1 逐字）

> From the AUX camera video feed, the user can Edit the image as in the landscape version in the Wireless Camera view

## reasoning

§28.8 之父題逐字為 `AUX Camera 12 Inch Portrait`（`NRL-188115`），故前提取 PROXI `Radio_Display_Type = 7`（byte 185 bit 0–3，值域逐字 `7 = 12" 1200x1920`，寬 < 高即 Portrait；`6 = 12" 1920x1200` 為橫向，不取）。`as in the landscape version` 之比較基準即 §28.7.2 之三個控制項（`-114`～`-116`），故 ER 驗該三項齊備。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. PROXI Radio_Display_Type = 7 (12" 1200x1920)
7. A wireless AUX camera is connected
8. The wireless AUX camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select "Edit image" in the camera view
2. Read the soft controls and check that "Rotate 90", "Mirror Image" and "Reset" are all offered
```

## expected_result

```
1. The "Edit image" control registers the selection
2. The "Rotate 90", "Mirror Image" and "Reset" soft controls are all shown, which is the same set as in the landscape version
```
