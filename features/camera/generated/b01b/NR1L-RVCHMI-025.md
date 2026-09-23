# NR1L-RVCHMI-025 — SWE1-RVC-016

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.3.1`（來源列 `NRL-142622`）

## test_item 上半（verbatim，SYS1 逐字）

> Any of the RVC+PAM conditions are met but the vehicle do no offer any PAM capability;

## reasoning

§7.3.1 **只存在於 cache 本**（A-CA14／**R-CAM6**）。PAM 配備旗標取 PROXI `CVPAM_Presence`（byte 173 bit 1，`0 = Absent`）—— `PAM_Configuration`（byte 118 bit 4–5）之值域只有 `0 = Rear`／`1 = Front And Rear`，無「無 PAM」之值，故不取。`CVPAM_Presence` 於 `forms/proxi/` 六本中五本有、**`Toro_ATL_MI` 0 命中**，依 **R-CAM18(b)** `Toro(2261)` 判 `0`。觸發款取 §7.2.1 之 R 檔（最簡之 RVC+PAM 條件）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 0 (Absent)
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The shift lever is in P
6. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the RVC-only layout is displayed and that no PAM sensor area is displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The RVC-only layout is displayed and no PAM sensor area is shown
```
