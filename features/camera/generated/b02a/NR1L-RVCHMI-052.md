# NR1L-RVCHMI-052 — SWE1-RVC-061

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.2.3.1`（來源列 `NRL-188042`）

## test_item 上半（verbatim，SYS1 逐字）

> Wired AUX cam will always be a selectable field

## reasoning

§27.2.3.1 之 `always` 為本列之驗證重點 —— 單一狀態下之可選不足以判 `always`，故以兩個檔位驗之。與 `-053`（§27.2.3.2）成對：後者為**無線**側之灰階條件，本列為**有線**側之恆可選；兩者同在 `Indications for System States` 節下。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. The shift lever is in P
5. The AUX camera list is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the AUX camera list and check that the wired AUX entry is selectable
2. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
3. Read the AUX camera list and check that the wired AUX entry is still selectable
```

## expected_result

```
1. The wired AUX entry is selectable while the gear is P
2. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
3. The wired AUX entry is still selectable while the gear is R
```
