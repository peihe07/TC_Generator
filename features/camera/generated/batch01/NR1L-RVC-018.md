# NR1L-RVC-018 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1576`（來源列 `SYS-RA-VF551_V2-496`）

## test_item 上半（verbatim，SYS2 逐字）

> · When any of the following conditions hold true: - BCM_FD_10.CmdIgnSts != RUN, - BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX, - Shift Lever status change to "Park" from other gears ShiftLeverPosition = P - RVC_ImageDefeat.Req = Pressed. the Head Unit shall switch back to non-camera display.

## reasoning

驗證目標為 SYS-RA-VF551_V2-496 之 any-of 退出條件中「Shift Lever status change to "Park"」一支。raw 與 label 取 PDT27_E2A_R1_FDCAN8.dbc BO_ 1450 之 VAL_ 1 "P"；Atl-Mi 側以 STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted) 代換（CAN source 行）。本列與 NR1L-RVC-013 之差別在於後者退至 D 檔（Delay 判斷路徑），本列直接入 P（any-of 立即退出，不經 Delay）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. The rear view camera image is displayed in Automatic Display Mode
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
2. Read the HU display and check that the rear view camera image is no longer displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent
2. The rear view camera image is no longer displayed and the previous screen is shown again
```
