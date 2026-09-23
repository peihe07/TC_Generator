# NR1L-RVCHMI-019 — SWE1-RVC-008-02

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.2`（來源列 `NRL-142616`）

## test_item 上半（verbatim，SYS1 逐字）

> There is a transition from R to D gear and the RVC delay setting is active;

## reasoning

驗證目標為 §7.2 之第二款（cache 本 §7.2.2 逐字）。`RVC delay setting` 之逐字設定名取 `HMI Settings List` `Settings` 分頁 row 467 之 `Rear View Camera Delay*`（星號不入，**R-CAM5(a)**）。持續時長（10 秒／8 mph）屬 §7.5.3，由 B01b 承接，本列不驗。互參 A 本 `SWE-CAM-015`（`crossref_a_b.tsv` 判 `same-point`）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is On
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The shift lever is in R
6. The RVC+PAM layout is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 4 (D)
2. Read the HU display and check that the RVC+PAM layout is still displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 4 (D) is sent
2. The RVC+PAM layout remains displayed
```
