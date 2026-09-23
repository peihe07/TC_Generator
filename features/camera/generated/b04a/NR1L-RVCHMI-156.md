# NR1L-RVCHMI-156 — SWE1-RVC-125-02

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_31.1.6`（來源列 `NRL-188141`）

## test_item 上半（verbatim，SYS1 逐字）

> There is a total character limit of 14 characters. Once character limit is reached, truncate.

## reasoning

§31.1.6 之第二個判準。`14 characters` 與 `truncate` 為逐字；以第 14 與第 15 字驗其邊界。`Follow Core Truncation rules` 指向**外部規格**（Core HMI 之截斷規則），依 §8.4.2 不測其內容，ER 只判「不再接受且截斷於 14 字」。

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
1. Type 14 characters and read the name field
2. Type a 15th character and read the name field
```

## expected_result

```
1. The 14 characters are shown on two lines
2. The 15th character is not accepted and the name is truncated at 14 characters
```
