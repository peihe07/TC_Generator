# NR1L-RVCHMI-153 — SWE1-RVC-123

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_31.1.4`（來源列 `NRL-188139`）

## test_item 上半（verbatim，SYS1 逐字）

> The updated name also is reflected in the settings menu line item for that camera.

## reasoning

§31.1.4 逐字。加「另一台不受影響」一步 —— 該判準驗 `for that camera` 之限定，否則無從分辨全域改名與單台改名。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. Two wired AUX cameras are connected
3. The AUX 1 camera name has just been changed and confirmed
```

## input_test_data

`NA`

## test_procedure

```
1. Exit the individual AUX Cam settings pop-up
2. Read the AUX Cam settings menu and check the line item of the renamed camera
3. Read the AUX Cam settings menu and check the line item of the other camera
```

## expected_result

```
1. The AUX Cam settings menu is displayed
2. The line item of the renamed camera reads the new name
3. The line item of the other camera still reads its own name
```
