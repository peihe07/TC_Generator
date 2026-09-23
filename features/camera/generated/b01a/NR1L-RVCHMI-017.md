# NR1L-RVCHMI-017 — SWE1-RVC-008

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.2`（來源列 `NRL-142614`）

## test_item 上半（verbatim，SYS1 逐字）

> RVCPAM1) RVC+PAM layout will appear when:

## reasoning

`SWE1-RVC-008` 於 037 為 **leaf**（非 Heading），其 `HMI Source ID` 與六個 `-008-0n` 子列同為 `…_7.2`；而 cache 本之 §7.2 Description 僅為列舉之**標題句**，六款觸發各自為 §7.2.1～§7.2.6（一一對應，見上繳 §3-2 之對照）。故本列之**獨有驗證點為排他性** ——六款觸發皆不成立時 layout 不出現；六款各支由 `-018`～`-022` 及 B01b 之 `-008-06` 承接，本列不重複任一支。反例取 D 與 N 兩檔（皆非 R、無 delay、無手動入口），`Rear View Camera Delay` 設為 Off 以排除 §7.2.2 之 R→D delay 支。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is Off
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The shift lever is in P
6. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 4 (D)
2. Read the HU display and check that no RVC+PAM layout is displayed
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 3 (N)
4. Read the HU display and check that no RVC+PAM layout is displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 4 (D) is sent
2. No RVC+PAM layout is displayed
3. TRANSM_FD_4.ShiftLeverPosition = 3 (N) is sent
4. No RVC+PAM layout is displayed
```
