# NR1L-RVCHMI-029 — SWE1-RVC-019-02

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.4`（來源列 `NRL-142625`）

## test_item 上半（verbatim，SYS1 逐字）

> Image will be displayed while in that gear as long as vehicle speed remains less than the threshold.

## reasoning

§7.4 之第二句。門檻值取 **profile §9 標定常數表**：`c_VEHSPD_MAX` = 8 mph（＝ 12.874752 km/h，Atl-Hi V2／376 V3）／`MAX_SPEED` = 13,0 Km/h（2261 V33／637 V42）。raw 205 ＝ 12.8125 km/h 為**門檻下方最近之可注入點**（解析度 0.0625，A-CA30／A-CA31）。訊號與句式沿 A 本 `NR1L-RVC-026`（**R-CAM1(b)**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
4. The shift lever is in D
5. The RVC+PAM layout is displayed in Manual Display Mode
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h)
2. Read the HU display and check that the RVC+PAM layout is still displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h) is sent
2. The RVC+PAM layout remains displayed
```
