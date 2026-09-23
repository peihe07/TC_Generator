# NR1L-RVCHMI-050 — SWE1-RVC-059

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.2.1.1`（來源列 `NRL-188038`）

## test_item 上半（verbatim，SYS1 逐字）

> Second surface (AUX Cam controls within camera view – back up and CHMSL)

## reasoning

§27.2.1.1 為 `Control priority` 節下之 `Second surface` 一句 —— `second surface` 即控制項置於相機視角**之內**（相對於 first surface 之 Controls 頁／App Drawer）。條文只點名 `back up and CHMSL` 兩個視角，故兩者皆驗。`Digital_CHMSL_Camera_Prsnt`（byte 222 bit 7）於 `forms/proxi/` 六本中**只有 Atl-Hi 三本有**（`Fastback_ATL_MI`／`Promaster_ATL_MI`／`Toro_ATL_MI` 各 0）→ 依 **R-CAM18(b)** 三個 Atl-Mi 欄判 `0`（CAM-14 證據 5 已定）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
4. A wired AUX camera is connected
5. The rear view camera image is displayed
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
