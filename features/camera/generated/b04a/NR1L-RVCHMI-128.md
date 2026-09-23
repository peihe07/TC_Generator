# NR1L-RVCHMI-128 — SWE1-RVC-109

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_29.1.1`（來源列 `NRL-188119`）

## test_item 上半（verbatim，SYS1 逐字）

> The user can access the individual AUX Cam settings pop-up by pressing anywhere on the camera line item in the settings menu

## reasoning

§29 之父題逐字為 `Auxiliary Camera Settings`，§29.1 為 `Wired AUX Cam Settings`，故前提取有線 AUX。`anywhere on the camera line item` 為逐字 —— 驗證重點在於**整列皆可按**（非只按某個小圖示）。設定路徑取 **profile §3.0** 之 `ENTER_CAMERA_SETTINGS`（三 hop）＋ `forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` `Settings` 分頁 **row 474**（`10. Aux Cameras`）／**row 475**（`10.1 Aux Cameras`）之逐字。該表於 `Aux Cameras` 之下**無任何子項**（row 476 已是 `11. Trailer Reverse Guidance`），row 475 之備註逐字為 `See Head Unit Camera Systems Logic & Flow` —— 即子項之 label 由本 SYS1 章承載，故以來源之逐字為準（見上繳 §2-4）。與 `-133`（§29.2.1）之關係：兩列之 Description **僅 image token 不同**（正規化後亦相異），且父題分別為 `Wired AUX Cam Settings` 與 `Wireless AUX Cam Settings` —— 依 **R-CAM16(c)** 父題相異者各自出 TC。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Select "Aux Cameras"
5. Press the wired AUX camera line item anywhere on the line
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
