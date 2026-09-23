# NR1L-RVCHMI-018 — SWE1-RVC-008-01

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.2.1`（來源列 `NRL-142615`）

## test_item 上半（verbatim，SYS1 逐字）

> R is engaged;

## reasoning

驗證目標為 §7.2 列舉之第一款。verbatim 取 cache 本 **§7.2.1** 之 Description 逐字（`R is engaged;`）—— 037 之 `HMI Source ID` 只到 `_7.2`，`specification_reference` 因而仍寫 `…_7.2`（037 為錨之權威），逐字母體則取可定址之 §7.2.1（**R-CAM6**：B 本追溯母體為 `spec-index/cache/` 本）。此分立見上繳 §3-2。

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
2. Read the HU display and check that the RVC+PAM layout is displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The RVC+PAM layout is displayed
```
