# NR1L-RVCHMI-158 — SWE1-RVC-148

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.9.1`（來源列 `NRL-188186`）

## test_item 上半（verbatim，SYS1 逐字）

> The user can access the individual AUX Cam settings pop-up by pressing anywhere on the camera line item in the settings menu

## reasoning

§34.9 之父題逐字為 `AUX Cam Settings`。本列與 §29.1.1（`NR1L-RVCHMI-128`）／§29.2.1（`-133`）之 Description **僅 image token 不同**（正規化後仍相異），且三者之父題各異（`AUX Cam Settings`／`Wired AUX Cam Settings`／`Wireless AUX Cam Settings`）——依 **R-CAM16(c)** 父題相異者各自出 TC。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. A wired AUX camera is connected
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Select "Aux Cameras"
5. Press the AUX camera line item anywhere on the line
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
