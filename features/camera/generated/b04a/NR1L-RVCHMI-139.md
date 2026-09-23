# NR1L-RVCHMI-139 — SWE1-RVC-114-01

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_30.1.1`（來源列 `NRL-188128`）

## test_item 上半（verbatim，SYS1 逐字）

> The User can make an AUX cam a favorite by selecting the camera in AUX Cam settings menu, and pressing the “Make Favorite” soft control.

## reasoning

§30 之父題逐字為 `Favorite a camera – Camera App`，§30.1 為 `Favorite an AUX Cam`。條文以 `Or` 並列**兩個入口**（設定選單 vs camera app 頁之星號），兩者之可觀察路徑不同故分列（`-139`／`-140`）。設定路徑取 **profile §3.0** 之 `ENTER_CAMERA_SETTINGS`（三 hop）＋ `forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` `Settings` 分頁 **row 474**（`10. Aux Cameras`）／**row 475**（`10.1 Aux Cameras`）之逐字。該表於 `Aux Cameras` 之下**無任何子項**（row 476 已是 `11. Trailer Reverse Guidance`），row 475 之備註逐字為 `See Head Unit Camera Systems Logic & Flow` —— 即子項之 label 由本 SYS1 章承載，故以來源之逐字為準（見上繳 §2-4）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The wired camera is not currently a favorite
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Select "Aux Cameras"
5. Select the wired AUX camera in the AUX Cam settings menu
6. Press the "Make Favorite" soft control
7. Read the HU display and check that the camera has been made favorite
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. The "Aux Cameras" settings menu is displayed
5. The individual AUX Cam settings pop-up for that camera is displayed
6. The "Make Favorite" soft control registers the press
7. The camera is marked as the favorite camera
```
