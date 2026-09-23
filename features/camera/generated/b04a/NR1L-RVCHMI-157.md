# NR1L-RVCHMI-157 — SWE1-RVC-125-03

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_31.1.6`（來源列 `NRL-188141`）

## test_item 上半（verbatim，SYS1 逐字）

> Do not truncate if full word can fit.

## reasoning

§31.1.6 之第三個判準（截斷之例外）。以「第二個字為 6 字、可容於一行」之名稱驗之 ——6 < 7（每行上限，`-155` 所驗），故該字必可整字容下。與 `-156` 成一對：前者驗**逾限即截斷**，本列驗**未逾限不截斷**。

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
1. Type a name whose second word is 6 characters long and fits within the line
2. Read the name field and check that the second word is shown in full
```

## expected_result

```
1. The name is entered
2. The second word is shown in full and is not broken across the lines
```
