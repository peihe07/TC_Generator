# NR1L-RVCHMI-117 — SWE1-RVC-106-01

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.7.3`（來源列 `NRL-188113`）

## test_item 上半（verbatim，SYS1 逐字）

> User can extend the view an additional 10 seconds above thresholds by pressing the AUX soft control

## reasoning

§28.7.3 之前半。`10 seconds` 與 `above thresholds` 為逐字；門檻值取 **profile §9** 之 `c_VEHSPD_MAX` = 8 mph（＝ 12.874752 km/h），raw 206 ＝ 12.875 為門檻上方最近之可注入點（**A-CA30**）。以 9／11 秒兩點驗該 10 秒窗之起訖。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
4. The shift lever is in D
5. The AUX camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Press the AUX soft control and record the timestamp
3. Read the HU display 9 seconds after the recorded timestamp and check that the AUX view is still displayed
4. Read the HU display 11 seconds after the recorded timestamp and check that the AUX view is no longer displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent, which is above the threshold
2. The AUX soft control registers the press
3. The AUX camera view is still displayed 9 seconds after the press
4. The AUX camera view is no longer displayed 11 seconds after the press
```
