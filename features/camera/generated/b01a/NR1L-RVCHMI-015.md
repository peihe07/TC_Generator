# NR1L-RVCHMI-015 — SWE1-RVC-007-01

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.1`（來源列 `NRL-142613`）

## test_item 上半（verbatim，SYS1 逐字）

> ATTENTION: Camera display has higher priority than any other screen.

## reasoning

驗證目標為 §7.1 首句之優先權。verbatim 取該句逐字（Description 之保序子序列，刪熱保護之第二句 —— 該句由 `-016` 承接）。以 Radio 顯示中入 R 檔驗「覆蓋既有畫面」。與 A 本 `SWE-CAM-015`（`NR1L-RVC-011` 等）之分工：後者驗**自動活化之判準**，本列驗**相對於其他畫面之優先權**；兩者來源與承接列皆不同（**R-CAM10**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. The Radio display is shown
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the rear view camera image has replaced the Radio display
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The rear view camera image is displayed in place of the Radio display
```
