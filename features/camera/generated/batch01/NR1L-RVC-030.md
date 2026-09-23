# NR1L-RVC-030 — SWE-CAM-018

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V33_P226MCA_VF_532`（來源列 `SYS-RA-VF551_V33-247`）

## test_item 上半（verbatim，SYS2 逐字）

> IF ( (STATUS_CCAN3.VehicleSpeedVSOSig>(greater) MAX_SPEED AND LTM_OperationalModeSts.Info ="Ignition_On_EngOn" ) OR (after T_DISPLAY time STATUS_CCAN4.ReverseGearSts==(equal) "Not_Inserted" ) THEN

## reasoning

驗證目標為 VF551_V33（Toro 2261）之速度門檻達標側，其逐字判準為 `STATUS_CCAN3.VehicleSpeedVSOSig >(greater) MAX_SPEED`（**嚴格大於**，與 V2／V4 之 `>=` 相斥，A-CA21）。**本包實測之新發現**：8 mph = 12.874752 km/h 非 0.0625 km/h 之整數倍，故「恰等於 8 mph」之 raw 不存在 —— raw 205 必低於、raw 206 必高於門檻，`>` 與 `>=` 之分歧在 CAN 匯流排上不可觀察。本列與 NR1L-RVC-009 因而在測試層同值，差別只在車型與訊息名。未達側由 NR1L-RVC-031 承接。【CAM-06 §2-1／§2-3】(1) 依審閱 §二-4 補 Pre-Condition `LTM_OperationalModeSts.Info = "Ignition_On_EngOn"` —— V33 逐字之條件含引擎運轉態，原 Pre-Condition 未表達（§8.7.1）；來源名保留（§8.7.5(f)），其 CAN 對應同 DR-CAM-i 之範圍。(2) **供試值改正**：原 Pre-Condition `MAX_SPEED corresponds to 8 mph per CFTS092 4781643` 為無來源之推定。本包逐格實測 VF551_V33 §1.14.1 常數表 —— `MAX_SPEED`（`SYS-RA-VF551_V33-503`）值 `13,0`（`-504`）、單位 `Km/h`（`-507`）、容差 `0,5`（`-506`）、範圍 `[10,0;18,0]`（`-505`）。13.0 ÷ 0.0625 = 208 為整數，**等值 raw 存在**，故 `>(greater)` 於門檻點可判：raw 209 = 13.0625 km/h 嚴格大於、raw 208 = 13.0 km/h 不大於。供試值因而由 206／205 改為 209／208。A-CA30 之「不可判」只對 Atl-Hi（`c_VEHSPD_MAX = 8 mph`，12.874752 km/h 非 0.0625 之倍數）成立；本列與 NR1L-RVC-009／-010 之差別不再是運算子，而是**兩平台之標定本不同數**（A-CA31、RDF-03）。容差 ±0,5 km/h 為 EOL 標定之範圍，208／209 為規格標稱之門檻點。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. LTM_OperationalModeSts.Info = "Ignition_On_EngOn"
4. The camera delay setting is set to "On"
5. The rear view camera image is displayed in Automatic Display Mode
6. The calibration MAX_SPEED = 13,0 Km/h per VF551_V33 1.14.1
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted)
2. Send CAN: STATUS_CCAN3.VehicleSpeedVSOSig = 209 (13.0625 km/h)
3. Read the HU display and check that the rear view camera image is no longer displayed
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted) is sent and the rear view camera image stays displayed
2. STATUS_CCAN3.VehicleSpeedVSOSig = 209 (13.0625 km/h) is sent
3. The rear view camera image is no longer displayed
```
