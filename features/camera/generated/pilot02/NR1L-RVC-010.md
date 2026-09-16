# NR1L-RVC-010 — SWE-CAM-018

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1577`（來源列 `SYS-RA-VF551_V2-490`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Ttimer2 shall start when BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX.

## reasoning

驗證目標為車速門檻之邊界，即 SYS-RA-VF551_V2-490 之 "The Ttimer2 shall start when BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX"（含等於）。錨不取 SYS-RA-VF551_V2-496 —— 該退出條文同為 SWE-CAM-015 所引，依 R-CAM10 委派 SWE-CAM-015。邊界換算：BRAKE_FD_2.VehicleSpeedVSOSig 於 PDT27_E2A_R1_FDCAN8.dbc BO_ 258 之 SG_ 為 (0.0625,0) [0|511.875] "Km/h"，VAL_ 僅 8191 "SNA"；8 mph = 12.874752 km/h 非 0.0625 之整數倍，故 raw 205 = 12.8125 km/h = 7.9614 mph 為 off-point、raw 206 = 12.875 km/h = 8.000154 mph 為 on-point（A-CA22）。本列承 off-point：raw 205 未達門檻，Ttimer2 不起算，影像於 10 s 延遲期內續顯；on-point 由 NR1L-RVC-009 承接（§8.3 每點一 TC）。本列只勾 Atl-Hi —— VF551_V33（2261）之同一判準逐字為 "STATUS_CCAN3.VehicleSpeedVSOSig >(greater) MAX_SPEED"（不含等於），邊界 ER 與本列相反；V3（376）為 BRAKE1.VehicleSpeedVSOSig（異名同判準），V42（637）只見 reset 語意。全量時依 VF 家族分寫（CAM-03 審閱 §一-7）。CFTS092 SYS-RA-CAM-078 以 "above 8 mph" 且與 10 s 為 all-of，與 VF 之 >= 相斥（A-CA21），於此具名。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Rear_View_Camera_Type = 1 (Digital)
4. The "Rear View Camera Delay" setting is set to "On"
5. The rear view camera image is displayed in Automatic Display Mode
6. The calibration c_VEHSPD_MAX corresponds to 8 mph per CFTS092 4781643
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 4 (D)
2. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h)
3. Read the HU display within 10 s of leaving reverse and check that the rear view camera image is still displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 4 (D) is sent and the rear view camera image stays displayed
2. BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h) is sent
3. The rear view camera image is still displayed within 10 s of leaving reverse
```
