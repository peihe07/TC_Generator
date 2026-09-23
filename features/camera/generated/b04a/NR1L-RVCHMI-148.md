# NR1L-RVCHMI-148 — SWE1-RVC-120

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_31.1.1`（來源列 `NRL-188136`）

## test_item 上半（verbatim，SYS1 逐字）

> From the AUX Cam settings menu, the user presses “Edit Name”.

## reasoning

§31 之父題逐字為 `Editing a camera name- Camera App`，§31.1 為 `Editing AUX Cam Name`。本列為該流程之起點；鍵盤之內容由 `-149`（§31.1.2）承接。與 `-129`／`-135`（§29.1.2／§29.2.2 之 `Edit the name`）之分工：後兩者只驗該項**被提供**，本列為**流程之起點**；三列之來源列皆不同（**R-CAM10**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The individual AUX Cam settings pop-up for the wired camera is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "Edit Name" soft control
2. Read the HU display and check that the name edit has started
```

## expected_result

```
1. The "Edit Name" soft control registers the press
2. The pop-up updates to show the name edit
```
