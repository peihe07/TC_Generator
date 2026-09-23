# NR1L-RVCHMI-164 — SWE1-RVC-152-02

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.9.5`（來源列 `NRL-188193`）

## test_item 上半（verbatim，SYS1 逐字）

> With a limit of 2 lines 14 characters. Once character limit is reached, truncate.

## reasoning

§34.9.5 之第二個判準。`Follow Core Truncation rules` 指向**外部規格**，依 §8.4.2 不測其內容。分工同 `-163`。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

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
1. Type 14 characters and read the name field
2. Type a 15th character and read the name field
```

## expected_result

```
1. The 14 characters are shown on two lines
2. The 15th character is not accepted and the name is truncated at 14 characters
```
