# NR1L-RVCHMI-185 — SWE1-RVC-001

- **Test Group**：Rear View Camera｜**Test Set**：PAM Integration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_6.2`（來源列 `NRL-142606`）

## test_item 上半（verbatim，SYS1 逐字）

> PAM2) PAM feature have multiple configurations and scopes and actual vehicle content should be defined by proxy configurations.

## reasoning

§6.2 之 `defined by proxy configurations` 須以**兩個不同之 proxy 值**驗得，故取 PROXI `PAM_Configuration`（byte 118 bit 4–5）之值域逐字 `0 = Rear`／`1 = Front And Rear`（實測 637 本，值域二項，**DECISIONS 6-56** 已定）。PAM 之**有無**則取 `CVPAM_Presence`（byte 173 bit 1，6-56）。`CVPAM_Presence` 於 `Toro_ATL_MI` 零命中 → **R-CAM18(b)** `Toro(2261)` 判 `0`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 1 (Present)
4. PROXI PAM_Configuration = 0 (Rear)
5. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
6. The shift lever is in P
7. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the RVC+PAM layout and check which PAM sensor zones are shown
3. Set PROXI PAM_Configuration = 1 (Front And Rear)
4. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
5. Read the RVC+PAM layout and check which PAM sensor zones are shown
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the RVC+PAM layout is displayed
2. Only the rear PAM sensor zones are shown
3. PROXI PAM_Configuration = 1 (Front And Rear) is applied
4. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the RVC+PAM layout is displayed
5. Both the front and the rear PAM sensor zones are shown
```
