# NR1L-RVCHMI-155 — SWE1-RVC-125-01

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_31.1.6`（來源列 `NRL-188141`）

## test_item 上半（verbatim，SYS1 逐字）

> The Character limit for an Aux camera name is 2 lines with 7 characters.

## reasoning

§31.1.6 載三個判準，三列各驗一個（`-155`～`-157`）。本列驗**每行 7 字**之邊界（第 7 與第 8 字），為邊界值分析。與 §34.9.5（B04b，`There is a 7 character limit per each line. With a limit of 2 lines 14 characters.`）之關係：兩列之 Description **非逐字全等**（41 vs 37 token），故非 R-CAM16(c) 之委派款；其分工於 B04b 之 reasoning 具名。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The full QWERTY keyboard is shown for editing the camera name
```

## input_test_data

`NA`

## test_procedure

```
1. Type 7 characters and read the name field
2. Type an 8th character and read the name field
```

## expected_result

```
1. The 7 characters are shown on one line
2. The 8th character starts a second line
```
