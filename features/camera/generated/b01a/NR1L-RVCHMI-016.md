# NR1L-RVCHMI-016 — SWE1-RVC-007-02

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.1`（來源列 `NRL-142613`）

## test_item 上半（verbatim，SYS1 逐字）

> In case the head unit display is off due to the thermal protection strategy, the head unit shall wake up to display the camera image.

## reasoning

驗證目標為 §7.1 第二句之熱保護喚醒。verbatim 為 Description 之保序子序列（刪首句）。熱保護關顯示之**進入手段**無來源：`forms/` 四本 DBC 掃描字串 `therm` 零命中（命令 `grep -ic therm forms/*.dbc`，四本各 0），CameraEventHal 表亦無對應訊號 → **DR-CAM-s**，並記入 `bench_verify.md`。喚醒後之 ER 仍可判，故不整列 BLOCKED（**R-CAM13** 之「已引來源須落地」）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-s the method to place the HU display into the thermal protection off state is not sourced
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The HU display is off due to the thermal protection strategy
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that it has woken up and that the rear view camera image is displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The HU display wakes up and the rear view camera image is displayed
```
