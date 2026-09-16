# NR1L-RVC-009 — SWE-CAM-018

- **Test Group**：Rear View Camera
- **Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`SYS-RA-VF551_V2-490`

## test_item 上半（verbatim，SYS2 逐字）

> · The Ttimer2 shall start when BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX.

## reasoning

驗證目標為車速恰達門檻時之邊界，即 SYS-RA-VF551_V2-490 之 "The Ttimer2 shall start when BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX"（含等於）。**錨不取 SYS-RA-VF551_V2-496** —— 該退出條文同為 SWE-CAM-015 所引，依 R-CAM10 由 SWE ID 較小者承接，本列委派 SWE-CAM-015；影像於門檻處移除之可觀察結果即 V2-496 之 any-of 退出，於此具名而不重複作錨。關鍵情境條件為 Delay = On 且已退出 R 檔、計時尚未到期。邊界值之選取：門檻以 mph 表示而 DBC 單位為 km/h —— BRAKE_FD_2.VehicleSpeedVSOSig 於 PDT27_E2A_R1_FDCAN8.dbc（BO_ 258）之 SG_ 為 (0.0625,0) [0|511.875] "Km/h"，VAL_ 僅 8191 "SNA" 而無列舉 label；8 mph = 12.874752 km/h 非 0.0625 之整數倍，raw 205 = 12.8125 km/h（7.9614 mph，未達）、raw 206 = 12.875 km/h（8.000154 mph，首個達標值），故以 205／206 為 off-point／on-point（A-CA22）。本列只勾 Atl-Hi —— VF551_V33（Toro 2261）之同一判準逐字為 "STATUS_CCAN3.VehicleSpeedVSOSig >(greater) MAX_SPEED"（不含等於），其邊界 ER 與本列相反，依 R-CAM3 須另立 sibling；CAM-03 §0 限定 9 TC，故該列未生成並回報。CFTS092 SYS-RA-CAM-078 以 "above 8 mph" 且與 10 s 為 all-of，與 VF 之 any-of／>= 相斥（A-CA21）；本列依 VF 原文寫 ER 並於此具名衝突。

## pre_conditions

```
1. PROXI Rear_View_Camera = 1 (Present)
2. PROXI Rear_View_Camera_Type = 1 (Digital)
3. The Head Unit is in the RUN power state
4. The camera delay setting is set to "On"
5. The calibration c_VEHSPD_MAX corresponds to 8 mph per CFTS092 4781643
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)
2. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 4 (D)
4. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h)
5. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
6. Read the Head Unit display within 10 s of leaving reverse and check that the rear view camera image is no longer shown
```

## expected_result

```
1. The Head Unit stays in the RUN power state
2. The rear view camera image is shown in Automatic Display Mode
3. The rear view camera image is still shown because the camera delay setting is "On"
4. The rear view camera image is still shown at 205 (12.8125 km/h)
5. The rear view camera image is removed at 206 (12.875 km/h)
6. The rear view camera image is no longer shown and the previous content is restored
```
