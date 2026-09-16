# NR1L-RVC-020 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1378`（來源列 `SYS-RA-VF551_V2-498`）

## test_item 上半（verbatim，SYS2 逐字）

> · When all of the following conditions hold true: - BCM_FD_10.CmdIgnSts = RUN, - ShiftLeverPosition = R > Reverse_Deb. the Head Unit shall display the RVC image as operating in Automatic Display Mode.

## reasoning

驗證目標為 SYS-RA-VF551_V2-498 之去彈跳門檻之未達側（off-point）：R 檔停留短於 Reverse_Deb 即回 P，影像不應出現。與 NR1L-RVC-019 成 on／off 一對（§8.3 每點一 TC）。`Reverse_Deb` 依 §8.4.1 以符號保留。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Rear_View_Camera_Type = 1 (Digital)
4. No camera image is displayed
5. The shift lever is in P
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Hold for less than Reverse_Deb
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
4. Read the HU display and check that no camera image is displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The signal is held for less than Reverse_Deb
3. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent
4. No camera image is displayed and the previous screen stays unchanged
```
