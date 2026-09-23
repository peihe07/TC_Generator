# NR1L-RVCHMI-116 — SWE1-RVC-105-03

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.7.2`（來源列 `NRL-188112`）

## test_item 上半（verbatim，SYS1 逐字）

> User selects Edit image to access the “Rotate 90”, “Mirror Image” and “Reset” soft controls

## reasoning

§28.7.2 之第三個控制項。本列只驗其**存在與可達**；其**作用**（影像回復）由 `-112`（§28.7.1.2）承接，兩者之來源列不同（`NRL-188112` vs `NRL-188111`），依 **R-CAM10** 不合併。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. A wireless AUX camera is connected
7. The wireless AUX camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select "Edit image" in the camera view
2. Read the soft controls and check that "Reset" is offered
```

## expected_result

```
1. The "Edit image" control registers the selection
2. The "Reset" soft control is shown
```
