# NR1L-RVCHMI-188 — SWE1-RVC-003

- **Test Group**：Rear View Camera｜**Test Set**：PAM Integration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_6.2.2`（來源列 `NRL-142608`）

## test_item 上半（verbatim，SYS1 逐字）

> PAM2.2) Are expected PAM features Rear ParkSense, Front+Rear ParkSense and Side Distance Warning.

## reasoning

§6.2.2 逐字列舉三款 PAM 功能，三者皆驗。`Front+Rear ParkSense` 於 PROXI 之對應值為 `PAM_Configuration = 1 (Front And Rear)`；`Side Distance Warning`（SDW）於 §11.1 之註逐字載其偵測條件（`When SDW is not capable of detecting ... vehicle must move forward`），該條件之測試由 `-193` 承接，本列只驗其**視覺存在**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 1 (Present)
4. PROXI PAM_Configuration = 1 (Front And Rear)
5. The RVC+PAM layout is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the RVC+PAM layout and check that the Rear ParkSense visualization is present
2. Read the RVC+PAM layout and check that the Front ParkSense visualization is present
3. Read the RVC+PAM layout and check that the Side Distance Warning visualization is present
```

## expected_result

```
1. The Rear ParkSense visualization is shown
2. The Front ParkSense visualization is shown
3. The Side Distance Warning visualization is shown
```
