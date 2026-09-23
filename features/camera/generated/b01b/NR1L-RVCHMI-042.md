# NR1L-RVCHMI-042 — SWE1-RVC-033

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.6`（來源列 `NRL-142641`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC5) When the radio is turned off/screen is off, the rear view camera shall still be displayed when rear view camera (RVC) on conditions are met

## reasoning

§8.6。`RVC on conditions` 取 §7.2.1 之 R 檔（最簡之一款）。與 B01a `-016`（§7.1 之熱保護喚醒）之分工：後者之顯示關閉**因熱保護**且進入法無來源（DR-CAM-s），本列之關閉為**使用者關收音機**，屬可操作之前提，故不掛 PENDING。與 B01a `-015`（優先權）之分工：`-015` 驗覆蓋既有畫面，本列驗**無畫面時之喚醒**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. The shift lever is in P
5. The radio is turned off
6. The HU display is off
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the rear view camera image is displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The HU display turns on and the rear view camera image is displayed
```
