# NR1L-RVC-130 — SWE-CAM-009

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_595`（來源列 `SYS-RA-VF551_V2-485`）

## test_item 上半（verbatim，SYS2 逐字）

> · When all of the following conditions hold true: - RVC display active on the Radio vehicleUpdate_1.TGW_CAMERA_DISP_STAT = DISP_DIGITAL_RVC_CAMERA - Vehicle speed above c_VEHSPD_MAX BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX - for each value of systemStatus.ZoomViewRes. the Head Unit shall: - grayout Zoom Soft Button - send vehicleUpdate_2.ZoomViewReq = Not_Pressed

## reasoning

驗證目標為 `SYS-RA-VF551_V2-485` 之「RVC 已於 Radio 顯示且車速達 `c_VEHSPD_MAX` 時，**不論 `systemStatus.ZoomViewRes` 為何值**，HU 將 Zoom 軟鍵灰階並送 `ZoomViewReq = Not_Pressed`」。原句 47 token，未逾 50，無須摘句。供試 raw 206 = 12.875 km/h（首個 ≥ 8 mph 之 raw，profile §9 之 `c_VEHSPD_MAX` 與 A-CA30 同一量測）。**`for each value of systemStatus.ZoomViewRes` 使本列不需注入該訊號** —— 其為全稱條件，任一值皆成立，故本列不受下述之 LVDS 注入風險影響。未達門檻側之五項行為由 `-131`～`-135` 承接（`V2-486`）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The RVC display is active on the Radio
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Read the HU display and check the state of the Zoom soft button
3. Read vehicleUpdate_2.ZoomViewReq and check that it is Not_Pressed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent
2. The Zoom soft button is greyed out
3. vehicleUpdate_2.ZoomViewReq = Not_Pressed is sent over LVDS
```
