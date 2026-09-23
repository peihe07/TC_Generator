# NR1L-RVC-241 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1576`（來源列 `SYS-RA-VF551_V2-496`）

## test_item 上半（verbatim，SYS2 逐字）

> · When any of the following conditions hold true: - BCM_FD_10.CmdIgnSts != RUN, - BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX, - Shift Lever status change to "Park" from other gears ShiftLeverPosition = P - RVC_ImageDefeat.Req = Pressed. the Head Unit shall switch back to non-camera display.

## reasoning

**補生成之由**：拆解審計 **CAM-23 §3 #1**（`confidence = H`）—— `SYS-RA-VF551_V2-496` 之 any-of 退出條件**四款**，而該來源列原只有 `NR1L-RVC-017`（點火）與 `-018`（P 檔）**兩個** TC；本列承接其中一款。母列不改（**DECISIONS 6-74** 之同一形制）。本列取 **`BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX`** 一款。門檻值取 **profile §9**：`c_VEHSPD_MAX` ＝ 8 mph ＝ 12.874752 km/h；raw 206 ＝ 12.875 km/h 為門檻上方最近之可注入點（**A-CA30**：解析度 0.0625 下無恰等於之 raw）。兩 EE 皆勾且有 `Send CAN` 步 → 依 **R-CAM3(f)** 寫 CAN source 行，訊號對照沿 A 本既有寫法（`NR1L-RVC-026` 等）。與 `NR1L-RVC-040`／`-041`（`SYS-RA-VF551_V2-139` 等之速度門檻列）之分工：後者驗**門檻值本身之標定**，本列驗**該門檻作為 any-of 退出條件之一**；兩者之來源列與承接列皆不同（**R-CAM10**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
4. The rear view camera image is displayed in Automatic Display Mode
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Read the HU display and check that the rear view camera image is no longer displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent
2. The rear view camera image is no longer displayed and the previous screen is shown again
```
