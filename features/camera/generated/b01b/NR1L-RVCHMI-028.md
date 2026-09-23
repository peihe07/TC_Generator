# NR1L-RVCHMI-028 — SWE1-RVC-019-01

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.4`（來源列 `NRL-142625`）

## test_item 上半（verbatim，SYS1 逐字）

> RVCPAM3) When activation occurs, the initial view will be the default view (associated with current gear state).

## reasoning

§7.4 之第一句。`default view (associated with current gear state)` 為逐字；以 R 檔活化驗其初始視角即該檔之預設視角。與 B01a `-018`（§7.2.1）之分工：後者驗 layout **是否出現**，本列驗出現時之**初始視角**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. The shift lever is in P
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the view shown is the default view for the REVERSE gear
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The RVC+PAM layout is displayed and the initial view is the default view associated with the REVERSE gear
```
