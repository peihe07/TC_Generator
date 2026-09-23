# NR1L-RVCHMI-183 — SWE1-RVC-038

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_9.2.2`（來源列 `NRL-142648`）

## test_item 上半（verbatim，SYS1 逐字）

> RVCF2.2) Display “Camera System Unavailable” message for any event which creates a blue screen condition

## reasoning

§9.2.2 之條件為 `blue screen condition`。`PU0169` 之觸發欄逐字即 `Display “Camera System Unavailable” message for any event which creates a “blue screen” condition.` —— 與本條**逐字對應**（該欄另載 `[v.SR12]` 之版本註）。分工見 `-182`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in R
4. A blue screen condition has been created on the camera feed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the HU display and check the screen colour
2. Read the HU display and check the message text
```

## expected_result

```
1. The display shows the blue screen
2. The display reads "Camera System Unavailable" (PU0169 of the R1 HMI pop-up list)
```
