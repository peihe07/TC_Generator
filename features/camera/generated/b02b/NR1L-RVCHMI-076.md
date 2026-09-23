# NR1L-RVCHMI-076 — SWE1-RVC-085

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.7.2`（來源列 `NRL-188080`）

## test_item 上半（verbatim，SYS1 逐字）

> If the camera app is present, the soft controls will not be on the controls page

## reasoning

§27.7.2 為 §27.7.1 之條件分支。驗其**否定側**（Controls 頁無）之外亦驗**替代入口仍在**（Camera app）—— 否則無從分辨「被移走」與「整個不存在」。本條與 H 本 §6.5.3（`NR1L-RVCHMI-009`）、§15.6.2 為同型條文（RVC／SVC／AUX 三者各一），三列之來源節與承接列皆不同（**R-CAM10**）。否定句式用 `check that no …`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
3. A wired AUX camera is connected
4. The shift lever is in P
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. PENDING: DR-CAM-g the entry path to the Controls screen is not sourced
2. Read the Controls screen and check that no AUX camera soft control is offered
3. Press "Apps" on Menu Bar to open App Drawer
4. Select the Camera app in the App Drawer
5. Read the Camera app home page and check that the AUX camera soft control is present
```

## expected_result

```
1. PENDING: DR-CAM-g the Controls screen is displayed
2. No AUX camera soft control is present on the Controls screen
3. The App Drawer is displayed
4. The Camera app home page is displayed
5. The AUX camera soft control is shown on the Camera app home page
```
