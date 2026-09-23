# NR1L-RVCHMI-010 — SWE1-RVC-051-01

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.7.1`（來源列 `NRL-187352`）

## test_item 上半（verbatim，SYS1 逐字）

> When not equipped with a camera app but equipped with “enhanced camera app” the rear view can be accessed via the controls page

## reasoning

驗證目標為 §6.7.1 之 controls page 一支。verbatim 為保序子序列（刪 `and apps drawer …` 之後段）。本列與 B01a `-005`（`SWE1-RVC-048-01`）之分工：後者為**一般配備**下之 controls page 入口，本列為**無 camera app 而有 enhanced camera app**之配備分支（§6.7 母題即此）。兩配備旗標皆於六本 PROXI 零命中 → **DR-CAM-r**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-r the equipment flags for the "Camera App" and "Enhanced Camera App" features are not sourced
4. The shift lever is in P
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. PENDING: DR-CAM-g open the Controls screen
2. Select the Rear View Camera soft control on the Controls screen
3. Read the HU display and check that the rear view camera image is displayed
```

## expected_result

```
1. PENDING: DR-CAM-g the Controls screen is displayed
2. The Rear View Camera soft control registers the selection
3. The rear view camera image is displayed
```
