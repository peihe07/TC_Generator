# NR1L-RVC-242 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1576`（來源列 `SYS-RA-VF551_V2-496`）

## test_item 上半（verbatim，SYS2 逐字）

> · When any of the following conditions hold true: - BCM_FD_10.CmdIgnSts != RUN, - BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX, - Shift Lever status change to "Park" from other gears ShiftLeverPosition = P - RVC_ImageDefeat.Req = Pressed. the Head Unit shall switch back to non-camera display.

## reasoning

**補生成之由**：拆解審計 **CAM-23 §3 #1**（`confidence = H`）—— `SYS-RA-VF551_V2-496` 之 any-of 退出條件**四款**，而該來源列原只有 `NR1L-RVC-017`（點火）與 `-018`（P 檔）**兩個** TC；本列承接其中一款。母列不改（**DECISIONS 6-74** 之同一形制）。本列取 **`RVC_ImageDefeat.Req = Pressed`** 一款。`RVC_ImageDefeat.Req` 為**內部訊號**（非 CAN）——`forms/` 四本 DBC 之 `SG_` 掃描只得 `ImageDefeatRQSts`／`TrailerImageDefeatRQSts`，皆非本訊號名；故**不寫 `Send CAN` 步**（§8.7.5(f)：內部訊號保留來源名於 ER，觸發改取其 HMI 面）。**HMI 面之逐字來源已查得**：`SYS-RA-VF551_V2-549` 逐字 `HU shall acquire the HU touch screen coordinates pressed by the driver to defeat Rear View Camera View via **RVC Image soft button** and set internal Signal RVC_ImageDefeat.Req = Pressed.`—— 故 Procedure 之觸發寫 `Press the RVC Image soft button`，**不掛 DR-CAM-g**（下放包 §6-1 之升級條件因而不成立）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera image is displayed in Automatic Display Mode
```

## input_test_data

`NA`

## test_procedure

```
1. Press the RVC Image soft button on the camera image
2. Read the HU display and check that the rear view camera image is no longer displayed
```

## expected_result

```
1. The RVC Image soft button registers the press and the HU sets RVC_ImageDefeat.Req = Pressed
2. The rear view camera image is no longer displayed and the previous screen is shown again
```
