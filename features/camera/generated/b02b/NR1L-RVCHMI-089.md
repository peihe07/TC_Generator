# NR1L-RVCHMI-089 — SWE1-RVC-138

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.6`（來源列 `NRL-188173`）

## test_item 上半（verbatim，SYS1 逐字）

> Accessing Aux Cameras – Backup and Cargo Cam

## reasoning

§34.6 於 037 為 **leaf**（其 `Categorization` 非 Heading），故須出 TC；其 Description 即父題 `Accessing Aux Cameras – Backup and Cargo Cam`，驗證點為**兩個來源視角皆可進入 AUX**（與 §34.3／§34.4 之 `Backup Cam Only` 相對）。`Digital_CHMSL_Camera_Prsnt`（Cargo）只存在於 Atl-Hi 三本 → **R-CAM18(b)** Atl-Mi 三欄 `0`。§34 之章標題逐字為 **`R1 Low Wired AUX Cameras`**（`NRL-188152`），與 §27 之 `R1 High Wired &Wireless Auxiliary Cameras`（`NRL-188027`）成對 —— 兩章之差別為 **HU 等級**（R1 Low 只有有線 AUX；§27.3.1 逐字 `Technical hardware requirements – (R1 High only due to architecture)`）。HU 等級**無 PROXI 編碼** —— 掃描字串 `Radio_Type`／`Trim_Level`／`Head_Unit_Type`／`Infotainment_Level`／`R1_Low`／`Uconnect` 於六本各 0 命中，故依下放包 §2 **不以此判車型**，前提以散文書寫（profile §7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Rear_View_Camera = 1 (Present)
6. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
7. A wired AUX camera is connected
8. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select the AUX camera soft control in the rear view camera image
2. Read the HU display and check that the AUX camera view is displayed
3. Return to the cargo camera view and select the AUX camera soft control there
4. Read the HU display and check that the AUX camera view is displayed
```

## expected_result

```
1. The AUX camera soft control in the rear view registers the selection
2. The AUX camera view is displayed
3. The AUX camera soft control in the cargo camera view registers the selection
4. The AUX camera view is displayed
```
