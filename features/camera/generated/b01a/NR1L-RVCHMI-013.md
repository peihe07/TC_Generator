# NR1L-RVCHMI-013 — SWE1-RVC-051-04

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.7.1`（來源列 `NRL-187352`）

## test_item 上半（verbatim，SYS1 逐字）

> Note: <X> only available in P, N, or D

## reasoning

驗證目標為 §6.7.1 末之 `Note: <X> only available in P, N, or D`（Description 逐字）。P 為正例、R 為反例（唯一不在列舉內之常見檔位），N／D 與 P 同屬列舉內而可觀察結果相同，不另拆（**profile §5** 之同結果不拆）。raw 與 label 取 `PDT27_E2A_R1_FDCAN8.dbc` 之 `VAL_ … ShiftLeverPosition 1 "P" 2 "R"`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-r the equipment flag for the "Enhanced Camera App" feature is not sourced
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
2. Read the rear view camera image and check that the "X" exit control is available
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
4. Read the rear view camera image and check that the "X" exit control is not available
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent and the "X" exit control is shown
2. The "X" exit control can be selected
3. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
4. The "X" exit control is not shown
```
