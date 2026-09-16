# NR1L-RVC-029 — SWE-CAM-018

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1765`（來源列 `SYS-RA-VF551_V2-489`）

## test_item 上半（verbatim，SYS2 逐字）

> · If the Timer has not timed out, then the Ttimer2 shall reset to zero when BRAKE_FD_2.VehicleSpeedVSOSig < c_VEHSPD_MAX.

## reasoning

驗證目標為 SYS-RA-VF551_V2-489 之「Ttimer2 未到期前，速度低於 c_VEHSPD_MAX 即歸零」。步 1 使 Ttimer2 起算（V2-490，NR1L-RVC-009 之錨），步 2 於到期前降速。raw 值換算見 DECISIONS 6-10。訊息名依 R-CAM3(e) 分寫於 CAN source 行。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
4. The rear view camera image is displayed in Manual Display Mode
5. The shift lever is in D
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h)
3. Read the HU display and check that the rear view camera image is still displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent and Ttimer2 starts
2. BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h) is sent
3. The rear view camera image stays displayed and Ttimer2 is reset to zero
```
