# NR1L-RVCHMI-006 — SWE1-RVC-048-02

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.5.1`（來源列 `NRL-187347`）

## test_item 上半（verbatim，SYS1 逐字）

> The Rear View Camera can be manually activated via the apps drawer,

## reasoning

驗證目標為 §6.5.1 之 apps drawer 一支。verbatim 為該列 Description 之保序子序列（刪 `controls page,` 與 `, or camera app`）。App Drawer 之進入句式沿 A 本 `NR1L-RVC-113` 逐字（**R-CAM1(b)**），故本支不需 DR-CAM-g。H 本 §18.3.1.1 逐字載 `Feature will be accessible through the head unit via an app from the apps drawer`，佐證該入口之存在。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Rear View Camera soft control in the App Drawer
3. Read the HU display and check that the rear view camera image is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The Rear View Camera soft control registers the selection
3. The rear view camera image is displayed
```
