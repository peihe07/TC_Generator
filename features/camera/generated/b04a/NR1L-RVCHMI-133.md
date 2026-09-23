# NR1L-RVCHMI-133 — SWE1-RVC-111

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_29.2.1`（來源列 `NRL-188123`）

## test_item 上半（verbatim，SYS1 逐字）

> The user can access the individual AUX Cam settings pop-up by pressing anywhere on the camera line item in the settings menu

## reasoning

§29.2 之父題逐字為 `Wireless AUX Cam Settings`。與 `-128`（§29.1.1）之關係見該列 reasoning（父題相異，R-CAM16(c) 不適用委派）；本列之前提為**無線**相機，故加 §27.3.1.x 之硬體要求與 `Enable Wireless Cameras` 設定。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. A wireless AUX camera is connected
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Select "Aux Cameras"
5. Press the wireless AUX camera line item anywhere on the line
6. Read the HU display and check that the individual AUX Cam settings pop-up is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. The "Aux Cameras" settings menu is displayed
5. The camera line item registers the press
6. The individual AUX Cam settings pop-up for that camera is displayed
```
