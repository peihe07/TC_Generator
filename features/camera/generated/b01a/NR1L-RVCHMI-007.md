# NR1L-RVCHMI-007 — SWE1-RVC-048-03

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.5.1`（來源列 `NRL-187347`）

## test_item 上半（verbatim，SYS1 逐字）

> The Rear View Camera can be manually activated via camera app

## reasoning

驗證目標為 §6.5.1 之 camera app 一支。verbatim 為保序子序列（刪 `the controls page, apps drawer, or`，並留 `camera app`）。hop label `Camera app home page` 逐字取 H 本 **§27.2.6.3**；入口（自 App Drawer 進 Camera app）取 §18.3.1.1 之逐字。「Camera App」之配備旗標於六本 PROXI 零命中（掃描字串 `Camera_App`，六本各 0）→ **DR-CAM-r**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
4. The shift lever is in P
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Select the Rear View Camera soft control on the Camera app home page
4. Read the HU display and check that the rear view camera image is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. The Rear View Camera soft control registers the selection
4. The rear view camera image is displayed
```
