# NR1L-RVC-019 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1378`（來源列 `SYS-RA-VF551_V2-498`）

## test_item 上半（verbatim，SYS2 逐字）

> · When all of the following conditions hold true: - BCM_FD_10.CmdIgnSts = RUN, - ShiftLeverPosition = R > Reverse_Deb. the Head Unit shall display the RVC image as operating in Automatic Display Mode.

## reasoning

驗證目標為 SYS-RA-VF551_V2-498 之去彈跳門檻 `ShiftLeverPosition = R > Reverse_Deb` 之達標側（on-point）。`Reverse_Deb` 為標定常數，本包無來源可查其值，依 §8.4.1 以符號保留，Procedure 以 §8.7.5(f) 之 `Hold for <n>` 形態書寫。未達側由 NR1L-RVC-020 承接（§8.3 每點一 TC）。本列只勾 Atl-Hi —— Atl-Mi 之去彈跳以 STATUS_CCAN4.ReverseGearSts 計時，條文與訊號語意皆異，全量另列。

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
2. Hold for Reverse_Deb
3. Read the HU display and check that the rear view camera image is displayed in Automatic Display Mode
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The signal is held for Reverse_Deb
3. The rear view camera image is displayed in Automatic Display Mode
```
