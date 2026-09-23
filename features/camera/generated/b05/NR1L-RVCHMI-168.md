# NR1L-RVCHMI-168 — SWE1-RVC-155

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.9.8`（來源列 `NRL-188196`）

## test_item 上半（verbatim，SYS1 逐字）

> The updated name also is reflected in the settings menu line item for that camera.

## reasoning

§34.9.8 與 §31.1.4（`-153`）之 Description **逐字全等**（皆 17 token），惟**父題相異** —— 本列之父為 §34.9 `AUX Cam Settings`（R1 Low），`-153` 之父為 §31.1 `Editing AUX Cam Name`（R1 High）——依 **R-CAM16(c)** 父題相異者各自出 TC。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. Two wired AUX cameras are connected
6. The AUX 1 camera name has just been changed and confirmed
```

## input_test_data

`NA`

## test_procedure

```
1. Exit the individual AUX Cam settings pop-up
2. Read the line item of the renamed camera
3. Read the line item of the other camera
```

## expected_result

```
1. The AUX Cam settings menu is displayed
2. The line item of the renamed camera reads the new name
3. The line item of the other camera still reads its own name
```
