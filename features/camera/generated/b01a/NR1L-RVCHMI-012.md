# NR1L-RVCHMI-012 — SWE1-RVC-051-03

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.7.1`（來源列 `NRL-187352`）

## test_item 上半（verbatim，SYS1 逐字）

> When not equipped with a camera app but equipped with “enhanced camera app” the rear view will have the SVC bar present in the view

## reasoning

驗證目標為 §6.7.1 之 SVC bar 一支。`SVC bar` 為該列 Description 之逐字用語；其可選性取 H 本 **§22.2.13**（`All views listed above will have the black bar with all soft controls present when accessed via Vehicle Surround View, soft control via the controls page, or apps drawer`）。SVC bar 之存在以 `PROXI Surround_View_Camera = 1` 為前提；Toro 缺 byte 177（**DR-CAM-l**）→ `Toro(2261)` 判 0。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Surround_View_Camera = 1 (Present)
4. PENDING: DR-CAM-r the equipment flag for the "Enhanced Camera App" feature is not sourced
5. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the rear view camera image and check that the SVC bar is present in the view
2. Read the SVC bar and check that its soft controls are selectable
```

## expected_result

```
1. The SVC bar is shown in the rear view camera image
2. The soft controls in the SVC bar can be selected
```
