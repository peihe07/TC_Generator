# NR1L-RVCHMI-141 — SWE1-RVC-115

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_30.1.2`（來源列 `NRL-188129`）

## test_item 上半（verbatim，SYS1 逐字）

> From the AUX Cam settings menu, the user presses “Make Favorite”.

## reasoning

§30.1.2 為 §30.1 流程之第一步（其後 §30.1.3～§30.1.6 為後續各步）。與 `-139`（§30.1.1）之分工：後者為**能力陳述**（可經此入口設為最愛），本列為**流程之起點**（按下後出現確認彈窗）；兩列之來源列不同（**R-CAM10**）。確認彈窗之內容由 `-142`（§30.1.3）承接。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The wired camera is not currently a favorite
4. The individual AUX Cam settings pop-up for the wired camera is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "Make Favorite" soft control
2. Read the HU display and check that a confirmation pop-up is displayed
```

## expected_result

```
1. The "Make Favorite" soft control registers the press
2. A confirmation pop-up is displayed
```
