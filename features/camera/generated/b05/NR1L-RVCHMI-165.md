# NR1L-RVCHMI-165 — SWE1-RVC-152-03

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.9.5`（來源列 `NRL-188193`）

## test_item 上半（verbatim，SYS1 逐字）

> Do not truncate if full word can fit.

## reasoning

§34.9.5 之第三個判準（截斷之例外）。6 < 7（每行上限，`-163` 所驗）故該字必可整字容下。與 `-164` 成一對：前者驗逾限即截斷，本列驗未逾限不截斷。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. A wired AUX camera is connected
6. The full QWERTY keyboard is shown for editing the camera name
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
