# NR1L-RVCHMI-045 — SWE1-RVC-054

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.1.2`（來源列 `NRL-188030`）

## test_item 上半（verbatim，SYS1 逐字）

> Auxiliary Camera features will follow the general camera activation/deactivation strategies

## reasoning

「一般啟用／停用策略」之逐字內容不在本節，而在 RVC+PAM 本 §7.5 之退出條件族（B01b `-029`／`-030` 所驗）。本列取其中**速度門檻**一支施於 AUX 視角，驗 AUX 是否同受該策略支配。門檻值見 **profile §9**：8 mph ＝ 12.874752 km/h，raw 206 ＝ 12.875 為門檻上方最近之可注入點（**A-CA30**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
4. The shift lever is in D
5. The AUX 1 camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Read the HU display and check that the AUX 1 camera view is no longer displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent
2. The AUX 1 camera view is no longer displayed and the last known HU display is shown again
```
