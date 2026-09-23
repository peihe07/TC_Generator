# NR1L-RVCHMI-040 — SWE1-RVC-025-01

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.1.1`（來源列 `NRL-142632`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC1.1) RVC feed will not turn off as long as vehicle stays in REVERSE gear

## reasoning

§8.1.1 之前半。以**逾速度門檻**（raw 206）與**逾計時**（30 秒，10 秒之三倍）兩者同時施加，驗其在 R 檔下皆不關閉 —— 此即 `will not turn off as long as vehicle stays in REVERSE` 之強度。與 B01a `-021`（§7.2.4）之分工：後者驗**持續至離開 R 為止**（含離開後之退出），本列驗**留在 R 時他因不使其關閉**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
4. The shift lever is in R
5. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Read the HU display and check that the rear view camera image is still displayed
3. Wait 30 seconds without changing the gear
4. Read the HU display and check that the rear view camera image is still displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent
2. The rear view camera image is still displayed
3. The gear stays in R for 30 seconds
4. The rear view camera image is still displayed
```
