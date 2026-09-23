# NR1L-RVCHMI-032 — SWE1-RVC-020

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.5`（來源列 `NRL-142626`）

## test_item 上半（verbatim，SYS1 逐字）

> RVCPAM4) RVC+PAM layout will disappear when (last know Head Unit visualized screen):

## reasoning

`SWE1-RVC-020` 於 037 為 leaf，其 Description 為列舉之標題句；三款退出條件各自為 cache 本 §7.5.1／§7.5.2／§7.5.3，由 `-033`～`-037` 承接。故本列之**獨有驗證點為排他性** —— 三款皆不成立（檔位仍在 R、速度低於門檻、未逾時）時不退出。等待 30 秒之由：三款中最長之計時為 §7.5.3 之 **10 秒**，30 秒為其三倍，足以判「未逾時退出」；該 10 秒為來源逐字（§7.5.3 `After 10 seconds`，與 Pop Up List `PU0361` 之 timeout 欄 `10` 相符）。形制同 B01a `NR1L-RVCHMI-017`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. The shift lever is in R
5. The RVC+PAM layout is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h)
2. Read the HU display and check that the RVC+PAM layout is still displayed
3. Wait 30 seconds without changing the gear
4. Read the HU display and check that the RVC+PAM layout is still displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h) is sent
2. The RVC+PAM layout remains displayed
3. The gear stays in R for 30 seconds
4. The RVC+PAM layout remains displayed
```
