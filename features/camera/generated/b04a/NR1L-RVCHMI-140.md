# NR1L-RVCHMI-140 — SWE1-RVC-114-02

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_30.1.1`（來源列 `NRL-188128`）

## test_item 上半（verbatim，SYS1 逐字）

> The User can make an AUX cam a favorite by selecting the Star in the corner of the soft control on the camera app page

## reasoning

§30.1.1 之第二個入口（`Or by selecting the Star in the corner of the soft control on the camera app page`）。verbatim 為該列 Description 之保序子序列（刪第一個入口之片語）。camera app 之配備旗標六本 PROXI 零命中 → **DR-CAM-r**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
3. A wired AUX camera is connected
4. The wired camera is not currently a favorite
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Select the Star in the corner of the AUX camera soft control
4. Read the HU display and check that the camera has been made favorite
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. The Star registers the selection
4. The camera is marked as the favorite camera
```
