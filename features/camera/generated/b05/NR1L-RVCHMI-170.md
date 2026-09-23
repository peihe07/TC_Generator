# NR1L-RVCHMI-170 — SWE1-RVC-157

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.10.1`（來源列 `NRL-188199`）

## test_item 上半（verbatim，SYS1 逐字）

> The user can access AUX cameras that have been connected to the system

## reasoning

§34.10 之父題逐字為 `Accessing AUX Cameras Camera app`（`NRL-188198`）。`that have been connected` 之限定須有**未連線者之對照**方驗得，故前提佈一連一未連。與 `-096`（§34.8.2，未連線之藍畫面）之分工：後者驗**按下未連線之 AUX 後之畫面**，本列驗**清單只列已連線者**。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
6. AUX 1 is connected
7. AUX 2 is not connected
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Read the AUX filter and check which AUX cameras are offered
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. AUX 1 is offered and AUX 2 is not offered
```
