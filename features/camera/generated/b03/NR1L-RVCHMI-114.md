# NR1L-RVCHMI-114 — SWE1-RVC-105-01

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.7.2`（來源列 `NRL-188112`）

## test_item 上半（verbatim，SYS1 逐字）

> User selects Edit image to access the “Rotate 90”, “Mirror Image” and “Reset” soft controls

## reasoning

§28.7.2 列舉三個 soft control，三列各驗一個（`-114`／`-115`／`-116`）。`90 degrees` 之角度取同章 §28.7.1.2 之逐字 `rotate image 90 degrees`。三列之 verbatim 皆為該列 Description 之**全文**（15 token）—— 其三個控制項以 `,`／`and` 相連，逐字摘句會留下孤懸之標點（`“Rotate 90”,` 之逗號黏字），故不摘；各列所驗之控制項由 `test_item` 下半之括號句（`split_reason`）指明。

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
2. Read the soft controls and check that "Rotate 90" is offered
3. Select the "Rotate 90" soft control
4. Read the camera image and check that it has rotated by 90 degrees
```

## expected_result

```
1. The "Edit image" control registers the selection
2. The "Rotate 90" soft control is shown
3. The "Rotate 90" soft control registers the selection
4. The camera image is rotated by 90 degrees
```
