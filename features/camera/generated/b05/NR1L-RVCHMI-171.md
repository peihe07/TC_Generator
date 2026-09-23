# NR1L-RVCHMI-171 — SWE1-RVC-158

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.10.2`（來源列 `NRL-188200`）

## test_item 上半（verbatim，SYS1 逐字）

> The user simply taps on the Soft controls in the Camera App AUX and the associated factory camera view will be displayed full screen,

## reasoning

verbatim 為該列 Description 之保序子序列（刪句中之 `(image: Image_3960.png)` 與末之 `, as shown below (image: …)`；末之逗號黏於 `screen,` 故保留）。`the associated factory camera view` 之 `associated` 須以**兩台**驗得（點 AUX 2 須得 AUX 2 而非 AUX 1），故前提佈兩台。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
6. Two wired AUX cameras are connected
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Select the AUX filter on the Camera app home page
4. Tap the AUX 2 soft control
5. Read the HU display and check that the AUX 2 camera view is displayed full screen
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. The AUX filter is displayed
4. The AUX 2 soft control registers the tap
5. The AUX 2 camera view is displayed full screen
```
