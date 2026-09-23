# NR1L-RVCHMI-162 — SWE1-RVC-151

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.9.4`（來源列 `NRL-188192`）

## test_item 上半（verbatim，SYS1 逐字）

> From the AUX Cam settings menu, the user presses “Edit Favorite”

## reasoning

§34.9.4 之控制項逐字為 `“Edit Favorite”` —— 與 R1 High 側 §30.1.2 之 `“Make Favorite”` **用語不同**（同一動作於兩章之 label 相異），故兩列不合併；兩者之來源本章與承接列皆不同（**R-CAM10**）。該用語差異已於 `b05_plan.tsv` 之 note 記。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. A wired AUX camera is connected
6. The individual AUX Cam settings pop-up is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the pop-up and check that "Edit Favorite" is offered
2. Press "Edit Favorite"
3. Read the HU display and check that the favorite edit has started
```

## expected_result

```
1. "Edit Favorite" is shown in the pop-up
2. "Edit Favorite" registers the press
3. The pop-up updates to show the favorite edit
```
