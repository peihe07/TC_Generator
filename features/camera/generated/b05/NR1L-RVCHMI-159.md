# NR1L-RVCHMI-159 — SWE1-RVC-149

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.9.2.1`（來源列 `NRL-188188`）

## test_item 上半（verbatim，SYS1 逐字）

> Edit the name of the selected camera

## reasoning

§34.9.2 之父句逐字為 `From this pop-up the user can:`（`NRL-188187`），本列為其第一項。控制項之 label 取 §34.9.4 之 `“Edit Favorite”` 同節形制與 §31.1.1 之 `“Edit Name”`。與 `-129`／`-135`（§29.1.2／§29.2.2 之同名項）之分工：本列為 **R1 Low** 側之彈窗，其項目集只有兩項（§34.9.2.1／§34.9.2.2），無 favorite／delete。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

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
1. Read the pop-up and check that "Edit Name" is offered
2. Select "Edit Name"
3. Read the HU display and check that a full QWERTY keyboard is displayed
```

## expected_result

```
1. "Edit Name" is shown in the pop-up
2. "Edit Name" registers the selection
3. A full QWERTY keyboard is displayed for editing the camera name
```
