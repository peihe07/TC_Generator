# NR1L-RVCHMI-081 — SWE1-RVC-129

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.1.1.1`（來源列 `NRL-188155`）

## test_item 上半（verbatim，SYS1 逐字）

> Second surface (AUX Cam controls within camera view – back up and CHMSL)

## reasoning

本列與 §27.2.1.1（`NR1L-RVCHMI-050`）**逐字全等**（原始格亦全等，見上繳 §3 證據 2）。§34 之章標題逐字為 **`R1 Low Wired AUX Cameras`**（`NRL-188152`），與 §27 之 `R1 High Wired &Wireless Auxiliary Cameras`（`NRL-188027`）成對 —— 兩章之差別為 **HU 等級**（R1 Low 只有有線 AUX；§27.3.1 逐字 `Technical hardware requirements – (R1 High only due to architecture)`）。HU 等級**無 PROXI 編碼** —— 掃描字串 `Radio_Type`／`Trim_Level`／`Head_Unit_Type`／`Infotainment_Level`／`R1_Low`／`Uconnect` 於六本各 0 命中，故依下放包 §2 **不以此判車型**，前提以散文書寫（profile §7.3）。故兩列不合併：`-050` 為 R1 High（有線＋無線），本列為 R1 Low（只有有線），前提之 AUX 種類因而不同。`Digital_CHMSL_Camera_Prsnt`（byte 222 bit 7）只存在於 Atl-Hi 三本 → **R-CAM18(b)** 三個 Atl-Mi 欄判 `0`。

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
1. Read the rear view camera image and check that the AUX camera soft control is present within the view
2. Select the CHMSL camera soft control
3. Read the CHMSL camera view and check that the AUX camera soft control is present within the view
```

## expected_result

```
1. The AUX camera soft control is shown within the rear view camera image
2. The CHMSL camera view is displayed
3. The AUX camera soft control is shown within the CHMSL camera view
```
