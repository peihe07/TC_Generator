# NR1L-RVCHMI-082 — SWE1-RVC-130

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.1.2.1`（來源列 `NRL-188157`）

## test_item 上半（verbatim，SYS1 逐字）

> Icons will exist for “AUX Cameras” in the camera views

## reasoning

本列與 §27.2.2.1（`NR1L-RVCHMI-051`）逐字全等。§34 之章標題逐字為 **`R1 Low Wired AUX Cameras`**（`NRL-188152`），與 §27 之 `R1 High Wired &Wireless Auxiliary Cameras`（`NRL-188027`）成對 —— 兩章之差別為 **HU 等級**（R1 Low 只有有線 AUX；§27.3.1 逐字 `Technical hardware requirements – (R1 High only due to architecture)`）。HU 等級**無 PROXI 編碼** —— 掃描字串 `Radio_Type`／`Trim_Level`／`Head_Unit_Type`／`Infotainment_Level`／`R1_Low`／`Uconnect` 於六本各 0 命中，故依下放包 §2 **不以此判車型**，前提以散文書寫（profile §7.3）。分工同 `-081`：`-051` 為 R1 High，本列為 R1 Low（ER 之標的為**有線** AUX 視角）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Rear_View_Camera = 1 (Present)
6. A wired AUX camera is connected
7. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the rear view camera image and check that an "AUX Cameras" icon is present
2. Select the "AUX Cameras" icon
3. Read the HU display and check that the wired AUX camera view is displayed
```

## expected_result

```
1. The "AUX Cameras" icon is shown in the rear view camera image
2. The "AUX Cameras" icon registers the selection
3. The wired AUX camera view is displayed
```
