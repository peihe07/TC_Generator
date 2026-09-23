# NR1L-RVCHMI-178 — SWE1-RVC-031-01

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.4`（來源列 `NRL-142638`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC3) The “X” exit button and any banners (check entire surroundings) will be white with a background to provide contrast/legibility across ALL radios.

## reasoning

§8.4 之前半。`across ALL radios` 為適用範圍之陳述，其逐機型複驗屬交付後之事，本列於一台驗其形制。`white with a background` 為逐字之可觀察屬性；**不造具體色碼**（§8.4.1）。與 `-179` 之分工：後者驗**透明度**（60% ±5%）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is On
4. The shift lever is in D
5. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the "X" exit button and check its colour and whether it has a background
2. Read the Check Entire Surroundings banner and check its colour and whether it has a background
```

## expected_result

```
1. The "X" exit button is white and has a background
2. The Check Entire Surroundings banner is white and has a background
```
