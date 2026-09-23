# NR1L-RVCHMI-022 — SWE1-RVC-008-05

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.2.5`（來源列 `NRL-142619`）

## test_item 上半（verbatim，SYS1 逐字）

> By pressing the associated button in the «Controls» screen (Vehicle Page);

## reasoning

驗證目標為 §7.2 之第五款（cache 本 §7.2.5 逐字）。hop label 逐字取該列之 `«Controls» screen (Vehicle Page)`（含法文引號，**不改寫**為 `Controls page`）；進入該頁之路徑仍無來源 → **DR-CAM-g**。第六款（`«Camera» shortcut icon, in the Status bar Shortcut menu`，§7.2.6／`SWE1-RVC-008-06`）落於 B01b —— B01a 之 22 列切點落在 §7.2 家族內，見上繳 §3-3。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. PENDING: DR-CAM-g the entry path to the Controls screen (Vehicle Page) is not sourced
2. Select the associated button in the «Controls» screen (Vehicle Page)
3. Read the HU display and check that the RVC+PAM layout is displayed
```

## expected_result

```
1. PENDING: DR-CAM-g the Controls screen (Vehicle Page) is displayed
2. The associated button registers the selection
3. The RVC+PAM layout is displayed
```
