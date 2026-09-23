# NR1L-RVCHMI-186 — SWE1-RVC-002-01

- **Test Group**：Rear View Camera｜**Test Set**：PAM Integration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_6.2.1`（來源列 `NRL-142607`）

## test_item 上半（verbatim，SYS1 逐字）

> PAM2.1) PAM features are not mutually exclusive

## reasoning

§6.2.1 之前半。`not mutually exclusive` 之可觀察形制為**兩個 PAM 功能同時顯示**，故取 `PAM_Configuration = 1 (Front And Rear)` 之組態。verbatim 為該列 Description 之保序子序列（刪後半，由 `-187` 承接）。

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
1. Read the RVC+PAM layout and check that the front and the rear PAM visualizations are both shown
2. Read the RVC+PAM layout and check that neither visualization suppresses the other
```

## expected_result

```
1. The front and the rear PAM visualizations are both shown at the same time, which shows that the PAM features are not mutually exclusive
2. Neither visualization is hidden or greyed out while the other is shown
```
