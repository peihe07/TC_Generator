# NR1L-RVC-017 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1576`（來源列 `SYS-RA-VF551_V2-496`）

## test_item 上半（verbatim，SYS2 逐字）

> · When any of the following conditions hold true: - BCM_FD_10.CmdIgnSts != RUN, - BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX, - Shift Lever status change to "Park" from other gears ShiftLeverPosition = P - RVC_ImageDefeat.Req = Pressed. the Head Unit shall switch back to non-camera display.

## reasoning

驗證目標為 SYS-RA-VF551_V2-496 之 any-of 退出條件中「BCM_FD_10.CmdIgnSts != RUN」一支：點火離開 RUN 即回非相機畫面。raw 與 label 取 PDT27_E2A_R1_FDCAN8.dbc BO_ 1153 之 VAL_ 3 "ACC"。同條之其餘三支分由 NR1L-RVC-018（排檔入 P）、-009／-010（速度門檻）與 SWE-CAM-016 之 X 鍵（RVC_ImageDefeat.Req）承接（§8.2.1）。訊息名因 EE 而異而 PROXI 值與 ER 皆同，依 R-CAM3(e) 不拆列，分寫於 CAN source 行。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)
4. The rear view camera image is displayed in Automatic Display Mode
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 3 (ACC)
2. Read the HU display and check that the rear view camera image is no longer displayed
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 3 (ACC) is sent
2. The rear view camera image is no longer displayed and the previous screen is shown again
```
