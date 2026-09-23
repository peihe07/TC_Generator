# NR1L-RVCHMI-207 — SWE1-RVC-023-02

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.5.3`（來源列 `NRL-142629`）

## test_item 上半（verbatim，SYS1 逐字）

> Vehicle speed reaches the speed threshold (8mph)

## reasoning

**補正之由**：**CAM-24 審閱 §一-1** —— canon **§8.3**（boundary 每點一 TC）與**§5.7**（不同觸發須拆）勝於本 feature 之既有前例；母列 `NR1L-RVCHMI-036` 原含多點／多觸發，已原地收斂為單點，本列承接其餘者。母列之 reasoning 已註本列之 ID。分析層記一筆：該形制經批次審閱而未抓（**A-CA37**）。本列為門檻之 **off-point**（raw 205 ＝ 12.8125 km/h，門檻下方最近之可注入點）；母列留 **on-point**（raw 206 ＝ 12.875 km/h）。8 mph ＝ 12.874752 km/h，解析度 0.0625 之下無恰等於之 raw（**A-CA30**），故兩點皆為最近之可注入點而非門檻值本身。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is On
4. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
5. The shift lever has just been moved from R to D
6. The rear view camera image is displayed during the delay
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h)
2. Read the HU display and check that the camera image is still displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h) is sent
2. The camera image is still displayed
```
