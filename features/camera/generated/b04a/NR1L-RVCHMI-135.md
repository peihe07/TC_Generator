# NR1L-RVCHMI-135 — SWE1-RVC-112-02

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_29.2.2`（來源列 `NRL-188124`）

## test_item 上半（verbatim，SYS1 逐字）

> From this pop-up the user can: -Edit the name of the selected camera

## reasoning

§29.2.2 之第二項。與 `-129`（§29.1.2 之同名項）之分工：**有線 vs 無線**之設定彈窗，兩者之父題與來源列皆不同（**R-CAM10**）；§29.2.2 之列舉另含 `Delete`（§29.1.2 無），即兩個彈窗之項目集本即不同。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. A wireless AUX camera is connected
7. The individual AUX Cam settings pop-up for the wireless camera is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the pop-up and check that "Edit Name" is offered
2. Select "Edit Name"
3. Read the HU display and check that the name can be edited
```

## expected_result

```
1. "Edit Name" is shown in the pop-up
2. "Edit Name" registers the selection
3. A full QWERTY keyboard is displayed for editing the camera name
```
