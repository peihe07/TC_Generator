# NR1L-RVCHMI-004 — SWE1-RVC-044

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.1.6`（來源列 `NRL-187337`）

## test_item 上半（verbatim，SYS1 逐字）

> Rear view camera follows general camera activation and deactivation strategies

## reasoning

驗證目標為 §6.1.6 之「遵循一般啟用／停用策略」。該策略之逐字內容不在 SYS1 本，而在 A 本 SYS2 之 `SYS-RA-VF551_V2-496`（any-of 退出條件，承接列 `SWE-CAM-015`，TC `NR1L-RVC-018`）—— 依 `crossref_a_b.tsv` 為 `same-point` 之鄰接。本列因而以「入 R 檔顯示、入 P 檔退出」之最小往返驗之；與 B01a `-021`（`SWE1-RVC-008-04`）之分工：後者驗**持續顯示至離開 R**，本列驗**進出**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the rear view camera image is displayed
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
4. Read the HU display and check that the rear view camera image is no longer displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The rear view camera image is displayed
3. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent
4. The rear view camera image is no longer displayed
```
