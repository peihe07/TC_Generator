# NR1L-RVCHMI-020 — SWE1-RVC-008-03

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.2`（來源列 `NRL-142617`）

## test_item 上半（verbatim，SYS1 逐字）

> Camera feed shall be displayed IMMEDIATELY after vehicle is shifted into REVERSE

## reasoning

驗證目標為 §7.2 之第三款（cache 本 §7.2.3 逐字）。`IMMEDIATELY` 無數值，取 **profile §9 標定常數表**之 `Reverse_Deb` = 750 ms（V2 §1.8.13 實測）為觀察窗上界 ——該值為 reverse 訊號之去彈跳窗，即「立即」在本系統可達之下界，非自造。與 `-018` 之分工：後者驗**是否出現**，本列驗**出現之時限**。時戳量測依 A 本 `NR1L-RVC-108` 之前例須 bus analyzer，一併記入 `bench_verify.md`。

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
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R) and record the bus timestamp
2. Read the HU display and record the timestamp at which the camera feed appears
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and its timestamp is recorded
2. The camera feed is displayed and the interval from the recorded send timestamp does not exceed Reverse_Deb = 750 ms
```
