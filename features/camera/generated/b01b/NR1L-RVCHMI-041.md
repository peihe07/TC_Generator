# NR1L-RVCHMI-041 — SWE1-RVC-025-02

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.1.1`（來源列 `NRL-142632`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC1.1) RVC feed will not turn off as long as vehicle stays in REVERSE gear so the “X” button will not be available

## reasoning

§8.1.1 之後半（`so the “X” button will not be available`）。以 R 檔（反例）與 D 檔（正例）成對，其正例側與 `-038` 之位置驗證不重複（本列只驗**可用與否**，不驗位置）。否定句式用 `check that no …`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. The shift lever is in R
5. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the camera image and check that no "X" button is offered
2. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 4 (D)
3. Read the camera image and check that the "X" button is now available
```

## expected_result

```
1. No "X" button is shown on the camera image while the gear is R
2. TRANSM_FD_4.ShiftLeverPosition = 4 (D) is sent and the camera image is still displayed
3. The "X" button is shown on the camera image
```
