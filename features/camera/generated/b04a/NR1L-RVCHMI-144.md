# NR1L-RVCHMI-144 — SWE1-RVC-118

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_30.1.5`（來源列 `NRL-188132`）

## test_item 上半（verbatim，SYS1 逐字）

> Once the user exits the AUX Cam settings menu, there will be a star shown in that camera’s line item now to signify that is the favorite camera

## reasoning

§30.1.5 逐字。`to signify that is the favorite camera` 之驗證須有**對照** ——若只有一台相機則無從判該星號是否專屬最愛，故前提佈兩台並驗非最愛者無星號。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. Two wired AUX cameras are connected
3. AUX 1 has been made favorite
4. The individual AUX Cam settings pop-up for AUX 1 is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Exit the AUX Cam settings pop-up
2. Read the AUX Cam settings menu and check that a star is shown in the AUX 1 line item
3. Read the AUX Cam settings menu and check that no star is shown in the AUX 2 line item
```

## expected_result

```
1. The AUX Cam settings menu is displayed
2. A star is shown in the AUX 1 line item
3. No star is shown in the AUX 2 line item, which shows that the star signifies the favorite camera
```
