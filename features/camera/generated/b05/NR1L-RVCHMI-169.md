# NR1L-RVCHMI-169 — SWE1-RVC-156

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.9.9`（來源列 `NRL-188197`）

## test_item 上半（verbatim，SYS1 逐字）

> The updated name also is reflected on the camera app homepage, in that camera’s soft button.

## reasoning

§34.9.9 與 §31.1.5（`-154`）之 Description 差一個句點（18 vs 18 token 而分群相異），且父題相異（R1 Low ↔ R1 High）→ 各自出 TC。camera app 之配備旗標六本 PROXI 零命中 → **DR-CAM-r**。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
6. A wired AUX camera is connected
7. The camera name has just been changed and confirmed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Read that camera's soft button on the Camera app home page
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. That camera's soft button reads the new name
```
