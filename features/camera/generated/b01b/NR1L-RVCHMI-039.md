# NR1L-RVCHMI-039 — SWE1-RVC-024-02

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.1`（來源列 `NRL-142631`）

## test_item 上半（verbatim，SYS1 逐字）

> When selected, the head unit will revert to displaying the last known screen.

## reasoning

§8.1 之後半。`revert to displaying the last known screen` 為逐字；以 Radio 顯示為「last known」之具體值（沿 B01a `-015` 之同一取法）。與 `-038` 之分工：後者驗按鍵之**位置與存在**，本列驗按下後之**行為**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is On
4. The Radio display was the last display shown before the camera image
5. The shift lever is in D
6. The rear view camera image is displayed during the delay
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "X" exit button on the camera image
2. Read the HU display and check that the Radio display is shown again
```

## expected_result

```
1. The "X" exit button registers the press
2. The rear view camera image is removed and the Radio display is shown again
```
