# NR1L-RVCHMI-118 — SWE1-RVC-106-02

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.7.3`（來源列 `NRL-188113`）

## test_item 上半（verbatim，SYS1 逐字）

> User can extend the view an additional 10 seconds above thresholds by pressing the extend view soft control when enhanced camera app feature is present

## reasoning

§28.7.3 之後半 —— 其條件句 `when enhanced camera app feature is present` 只繫於**extend view soft control** 一支（AUX soft control 一支無此條件），故兩支分列。「Enhanced Camera App」配備旗標六本 PROXI 零命中 → **DR-CAM-r**。本列不重驗 10 秒之終點（已由 `-117` 驗），只驗該控制項之**存在與生效**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PENDING: DR-CAM-r the equipment flag for the "Enhanced Camera App" feature is not sourced
3. A wired AUX camera is connected
4. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
5. The shift lever is in D
6. The AUX camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Read the AUX camera view and check that the extend view soft control is offered
3. Press the extend view soft control and record the timestamp
4. Read the HU display 9 seconds after the recorded timestamp and check that the AUX view is still displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent, which is above the threshold
2. The extend view soft control is shown in the AUX camera view
3. The extend view soft control registers the press
4. The AUX camera view is still displayed 9 seconds after the press
```
