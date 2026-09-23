# NR1L-RVCHMI-194 — SWE1-RVC-045

- **Test Group**：Rear View Camera｜**Test Set**：Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.2.2.1`（來源列 `NRL-187341`）

## test_item 上半（verbatim，SYS1 逐字）

> Rear View Camera Delay (on/off) – maintain camera image after shifting out of REVERSE for up to 10 sec or until vehicle speed reaches 8 mph Factory Default => OFF

## reasoning

§6.2 之父題逐字為 `Rear View Camera: Head Unit Settings`，§6.2.2 為 `System Settings`。本列之三個逐字事實皆驗：設定名（`Rear View Camera Delay`，與 HMI Settings List row 467 之 `Rear View Camera Delay*` 相符，`*` 依 **R-CAM5(a)** 不入 hop）、`up to 10 sec`／`8 mph` 之判準、`Factory Default => OFF`。10 秒之終點取 11 秒觀察（同 B01b `-035` 之形制）；8 mph 一支由 B01b `-036` 承接，本列不重驗。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. The HU has been reset to its factory defaults
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Read the "Camera" list and check the state of "Rear View Camera Delay"
5. Set "Rear View Camera Delay" = "On"
6. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
7. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P) and record the timestamp
8. Read the HU display 11 seconds after the recorded timestamp
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. "Rear View Camera Delay" is Off, which is the factory default
5. The "Rear View Camera Delay" setting is On
6. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the rear view camera image is displayed
7. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent and the camera image is maintained
8. The camera image is no longer displayed 11 seconds after the shift out of REVERSE
```
