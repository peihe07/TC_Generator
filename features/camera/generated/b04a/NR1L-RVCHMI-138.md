# NR1L-RVCHMI-138 — SWE1-RVC-113

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_29.2.3`（來源列 `NRL-188125`）

## test_item 上半（verbatim，SYS1 逐字）

> User can also access AUX settings by pressing the pencil icon in the camera app home Page AUX filter

## reasoning

§29.2.3 之全文。與 `-132`（§29.1.2 之第四項，同一句）之分工見該列 reasoning；本列自**無線**相機之脈絡（§29.2）進入，其 ER 之標的為無線相機之設定。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
6. The "Enable Wireless Cameras" setting is On
7. A wireless AUX camera is connected
8. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Select the AUX filter on the Camera app home page
4. Press the pencil icon in the AUX filter
5. Read the HU display and check that the AUX settings for the wireless camera are displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. The AUX filter is displayed
4. The pencil icon registers the press
5. The AUX settings for the wireless camera are displayed
```
