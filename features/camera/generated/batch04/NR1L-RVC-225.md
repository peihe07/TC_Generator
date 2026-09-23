# NR1L-RVC-225 — SWE-CAM-021

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V4_PHDCC27_VF_1725`（來源列 `SYS-RA-VF551_V4-122`）

## test_item 上半（verbatim，SYS2 逐字）

> · HU display shall not flicker in each of the following scenarios: 1. Head Unit displays the RVC image 2. Head Unit display transitions between RVC image and non camera modes.

## reasoning

驗證目標為 `SYS-RA-VF551_V4-122` 之類比側「不閃爍」。與 `NR1L-RVC-104`（`V2-523`，數位側，`SWE-CAM-003`）逐字同句而**本與承接列皆不同**，依 R-CAM10 各歸其列。V4 為 HDCC27 之**類比相機變體**，Pre-Condition 以 `PROXI Rear_View_Camera_Type = 0 (Analogic)` 與 V2 之數位側區別（`HDCC27_initial` row 931 實測 `0=Analogic`）。**只勾 HDCC27** —— V4 本之 anchor 前綴只有 `PHDCC27`（R-CAM11）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Rear_View_Camera_Type = 0 (Analogic)
4. The camera delay setting is set to "Off"
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display while the rear view camera image is shown and check for flicker
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
4. Read the HU display during the transition back to the non-camera display and check for flicker
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the rear view camera image is displayed
2. The HU display does not flicker while the RVC image is displayed
3. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent and the rear view camera image is closed
4. The HU display does not flicker during the transition between RVC and non camera modes
```
