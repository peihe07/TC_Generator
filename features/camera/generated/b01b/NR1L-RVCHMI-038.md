# NR1L-RVCHMI-038 — SWE1-RVC-024-01

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.1`（來源列 `NRL-142631`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC1) In ANY OTHER GEAR different from REVERSE an “X” exit button will be placed in the upper-right corner of the screen (PU0170)

## reasoning

§8.1 之前半。位置 `upper-right corner` 為來源逐字。`PU0170` 取 `forms/Pop Up List HMI R1 (26PI).xlsx` `Main` 分頁（module `Rearview Camera`），其文字欄載 `A clear ‘X’ exit button will be placed in the bottom right corner while the user is in Drive and camera delay is active.` —— **位置與 SYS1 相反**（SYS1 `upper-right` vs 彈窗 `bottom right`）。依 **§4.3.1** 以 SYS1 之逐字為準，差異記於 `remarks` 並登 **A-CA34**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is On
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The shift lever is in R
6. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 4 (D)
2. Read the camera image and check that the "X" exit button is placed in the upper-right corner
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 4 (D) is sent and the camera image is still displayed
2. The "X" exit button is shown in the upper-right corner of the camera image
```

## remarks

SYS1 7.5/8.1 places the X exit button in the upper-right corner; popup PU0170 in the Pop Up List says bottom right. ER follows SYS1. See A-CA34.
