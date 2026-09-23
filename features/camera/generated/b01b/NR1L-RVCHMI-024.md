# NR1L-RVCHMI-024 — SWE1-RVC-015

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.3`（來源列 `NRL-142621`）

## test_item 上半（verbatim，SYS1 逐字）

> RVCPAM2) RVC only layout will appear when:

## reasoning

`SWE1-RVC-015` 於 037 為 leaf，其 Description 為列舉之標題句 `RVCPAM2) RVC only layout will appear when:`；兩款觸發各自為 cache 本 §7.3.1／§7.3.2，由 `-025`／`-026` 承接。故本列之**獨有驗證點為排他性** —— 兩款皆不成立時不落 RVC-only。形制同 B01a `NR1L-RVCHMI-017`（§7.2 標題句）。反例之配備取 `CVPAM_Presence = 1`（byte 173 bit 1，`0=Absent`／`1=Present`）與 `Radio_Display_Type = 3`（byte 185 bit 0–3，`3 = 10.1" 1920x1200`，非 7"／8.4"）。兩個 byte 於 `Toro_ATL_MI` 皆 0 命中 → **R-CAM18(b)** `Toro(2261)` 判 `0`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 1 (Present)
4. PROXI Radio_Display_Type = 3 (10.1" 1920x1200)
5. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
6. The shift lever is in P
7. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the RVC+PAM layout is displayed and that no RVC-only layout is displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The RVC+PAM layout is displayed and the RVC-only layout is not displayed
```
