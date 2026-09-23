# NR1L-RVCHMI-088 — SWE1-RVC-137

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.4.3`（來源列 `NRL-188171`）

## test_item 上半（verbatim，SYS1 逐字）

> Pressing the AUX Cam button will always take the user to the Aux 1 screen

## reasoning

§34.4.3 之 `always` 之驗證重點在於**不記憶上次之視角**，故前提設「上次為 AUX 2」。與 `-095`（§34.8.1，`Pressing the AUX button will always take the user to the AUX 1 screen`）之分工：後者之父題為 `Accessing AUX – Cameras Not Connected`（`NRL-188180`），情境為**未連線**；本列之父題為 `Accessing Aux Cameras – Backup Cam Only`，情境為**已連線**。兩列之來源列不同（`NRL-188171` vs `NRL-188181`），依 **R-CAM10** 不合併。§34 之章標題逐字為 **`R1 Low Wired AUX Cameras`**（`NRL-188152`），與 §27 之 `R1 High Wired &Wireless Auxiliary Cameras`（`NRL-188027`）成對 —— 兩章之差別為 **HU 等級**（R1 Low 只有有線 AUX；§27.3.1 逐字 `Technical hardware requirements – (R1 High only due to architecture)`）。HU 等級**無 PROXI 編碼** —— 掃描字串 `Radio_Type`／`Trim_Level`／`Head_Unit_Type`／`Infotainment_Level`／`R1_Low`／`Uconnect` 於六本各 0 命中，故依下放包 §2 **不以此判車型**，前提以散文書寫（profile §7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Rear_View_Camera = 1 (Present)
6. Two wired AUX cameras are connected
7. The AUX 2 camera view was the last AUX view displayed
8. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Press the AUX Cam button in the App Drawer
3. Read the HU display and check that the Aux 1 screen is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The AUX Cam button registers the press
3. The Aux 1 screen is displayed and not the AUX 2 screen
```
