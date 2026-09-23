# NR1L-RVCHMI-021 — SWE1-RVC-008-04

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.2`（來源列 `NRL-142618`）

## test_item 上半（verbatim，SYS1 逐字）

> Must stay displayed until vehicle is shifted out of REVERSE

## reasoning

驗證目標為 §7.2 之第四款（cache 本 §7.2.4 逐字）之**持續性**。以「R 檔中按 Radio 硬鍵」驗其不被使用者操作中斷 —— 該不中斷之通則取 §7.1 之優先權句（`-015` 所驗）。退出以入 P 檔驗（而非 D），以避開 §7.2.2 之 R→D delay 分支；`Rear View Camera Delay` 設為 Off 亦為此。與 `-004`（`SWE1-RVC-044`）之分工：後者驗**進出往返**，本列驗**持續至離開 R 為止**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is Off
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The shift lever is in R
6. The RVC+PAM layout is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press the Radio hard key on the HU
2. Read the HU display and check that the RVC+PAM layout is still displayed
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
4. Read the HU display and check that the RVC+PAM layout is no longer displayed
```

## expected_result

```
1. The Radio hard key registers the press
2. The RVC+PAM layout remains displayed
3. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent
4. The RVC+PAM layout is no longer displayed
```
