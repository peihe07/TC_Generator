# NR1L-RVCHMI-046 — SWE1-RVC-055

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.1.3`（來源列 `NRL-188031`）

## test_item 上半（verbatim，SYS1 逐字）

> Selected View soft control will be highlighted

## reasoning

§27.1.3 為 Feature Assumptions 之一句。以兩個 AUX 視角之切換驗「highlight 隨選取移動」——單看一個視角無法判該 highlight 是否真隨選取而動。`Selected View soft control` 為逐字；§27.2.6.4（`-051`）為同句之第二次出現（`Accessible from` 節下），兩列之分工見該列 reasoning。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The shift lever is in P
4. The AUX 1 camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the AUX camera soft controls and check that the AUX 1 soft control is highlighted
2. Select the AUX 2 soft control
3. Read the AUX camera soft controls and check that the AUX 2 soft control is now highlighted
```

## expected_result

```
1. The AUX 1 soft control is highlighted while the AUX 1 view is displayed
2. The AUX 2 camera view is displayed
3. The AUX 2 soft control is highlighted and the AUX 1 soft control is no longer highlighted
```
