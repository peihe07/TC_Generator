# NR1L-RVCHMI-026 — SWE1-RVC-017

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.3.2`（來源列 `NRL-142623`）

## test_item 上半（verbatim，SYS1 逐字）

> Any of the RVC+PAM conditions are met but the Head Unit is 7” or 8.4”;

## reasoning

§7.3.2 只存在於 cache 本（A-CA14／**R-CAM6**）。兩個尺寸之 raw 取 PROXI `Radio_Display_Type`（byte 185 bit 0–3）之值域逐字：`1 = 7" 1280x768`、`2 = 8.4" 1024x768`。PAM 配備設為 Present 以隔離本條之變因（尺寸），與 `-025`（PAM 缺）分工。`Radio_Display_Type` 於六本中五本有、**`Toro_ATL_MI` 0 命中** → **R-CAM18(b)** `Toro(2261)` 判 `0`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 1 (Present)
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The shift lever is in P
6. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Set PROXI Radio_Display_Type = 1 (7" 1280x768)
2. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
3. Read the HU display and check that the RVC-only layout is displayed
4. Set PROXI Radio_Display_Type = 2 (8.4" 1024x768)
5. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
6. Read the HU display and check that the RVC-only layout is displayed
```

## expected_result

```
1. PROXI Radio_Display_Type = 1 (7" 1280x768) is applied
2. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
3. The RVC-only layout is displayed
4. PROXI Radio_Display_Type = 2 (8.4" 1024x768) is applied
5. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
6. The RVC-only layout is displayed
```
