# NR1L-RVCHMI-030 — SWE1-RVC-019-03

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.4`（來源列 `NRL-142625`）

## test_item 上半（verbatim，SYS1 逐字）

> Otherwise the soft button will be greyed out.

## reasoning

§7.4 之第三句（`Otherwise` 即速度不低於門檻之分支）。raw 206 ＝ 12.875 km/h 為**門檻上方最近之可注入點**（8 mph ＝ 12.874752 km/h，Atl-Hi 側無恰等於之 raw，A-CA30）。與 `-029` 成一對邊界值。

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
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Read the camera soft button and check that it is greyed out
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent
2. The camera soft button is greyed out
```
