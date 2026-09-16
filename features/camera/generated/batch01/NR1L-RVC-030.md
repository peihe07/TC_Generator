# NR1L-RVC-030 — SWE-CAM-018

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V33_P226MCA_VF_532`（來源列 `SYS-RA-VF551_V33-247`）

## test_item 上半（verbatim，SYS2 逐字）

> IF ( (STATUS_CCAN3.VehicleSpeedVSOSig>(greater) MAX_SPEED AND LTM_OperationalModeSts.Info ="Ignition_On_EngOn" ) OR (after T_DISPLAY time STATUS_CCAN4.ReverseGearSts==(equal) "Not_Inserted" ) THEN

## reasoning

驗證目標為 VF551_V33（Toro 2261）之速度門檻達標側，其逐字判準為 `STATUS_CCAN3.VehicleSpeedVSOSig >(greater) MAX_SPEED`（**嚴格大於**，與 V2／V4 之 `>=` 相斥，A-CA21）。**本包實測之新發現**：8 mph = 12.874752 km/h 非 0.0625 km/h 之整數倍，故「恰等於 8 mph」之 raw 不存在 —— raw 205 必低於、raw 206 必高於門檻，`>` 與 `>=` 之分歧在 CAN 匯流排上不可觀察。本列與 NR1L-RVC-009 因而在測試層同值，差別只在車型與訊息名。未達側由 NR1L-RVC-031 承接。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The camera delay setting is set to "On"
4. The rear view camera image is displayed in Automatic Display Mode
5. The calibration MAX_SPEED corresponds to 8 mph per CFTS092 4781643
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted)
2. Send CAN: STATUS_CCAN3.VehicleSpeedVSOSig = 206 (12.875 km/h)
3. Read the HU display and check that the rear view camera image is no longer displayed
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted) is sent and the rear view camera image stays displayed
2. STATUS_CCAN3.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent
3. The rear view camera image is no longer displayed
```
