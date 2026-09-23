# NR1L-RVCHMI-132 — SWE1-RVC-110-04

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_29.1.2`（來源列 `NRL-188120`）

## test_item 上半（verbatim，SYS1 逐字）

> From this pop-up the user can: -User can also access AUX settings by pressing the pencil icon in the camera app home Page AUX filter

## reasoning

§29.1.2 之第四項。與 `-138`（§29.2.3）之關係：該列之 Description **全文**即本項之同一句，惟兩者之**來源列不同**（`NRL-188120` 之第四項 vs `NRL-188125` 之全文）且父題不同（§29.1 `Wired AUX Cam Settings` vs §29.2 `Wireless AUX Cam Settings`）——依 **R-CAM16(c)** 不適用委派（該款要求 Description **全文**逐字全等），故各自出 TC；分工為：本列自**有線**相機之設定脈絡進入，`-138` 自**無線**相機之脈絡進入。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
3. A wired AUX camera is connected
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Select the AUX filter on the Camera app home page
4. Press the pencil icon in the AUX filter
5. Read the HU display and check that the AUX settings are displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. The AUX filter is displayed
4. The pencil icon registers the press
5. The AUX settings are displayed
```
