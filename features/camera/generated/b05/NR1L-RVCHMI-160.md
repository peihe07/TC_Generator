# NR1L-RVCHMI-160 — SWE1-RVC-150-01

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.9.2.2`（來源列 `NRL-188189`）

## test_item 上半（verbatim，SYS1 逐字）

> Reset Camera- Deletes the edited saved name of the camera, returning the name to “AUX Camera 1” or “AUX Camera 2”.(“AUX 1” and “AUX 2” on the soft controls)

## reasoning

§34.9.2.2 之前半。預設名之逐字取該列之 `“AUX Camera 1” or “AUX Camera 2”`；本列佈 AUX 1，故 ER 判 `AUX Camera 1`。與 `-131`（§29.1.2 之 `Reset the selected camera`）之分工：後者只驗該項**被提供**（其作用當時即引本列之定義），本列驗**回復後之逐字名稱**。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. A wired AUX camera is connected as AUX 1
6. The AUX 1 camera name has been edited to a name other than the default
7. The individual AUX Cam settings pop-up is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select "Reset Camera"
2. Read the camera line item and check the name
```

## expected_result

```
1. "Reset Camera" registers the selection
2. The camera name reads "AUX Camera 1"
```
