# NR1L-RVCHMI-129 — SWE1-RVC-110-01

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_29.1.2`（來源列 `NRL-188120`）

## test_item 上半（verbatim，SYS1 逐字）

> From this pop-up the user can: -Edit the name of the selected camera

## reasoning

§29.1.2 列舉四項，四列各驗一項（`-129`～`-132`）。控制項之逐字 label 取 §31.1.1 之 `“Edit Name”`（同一控制項於該節具名）。與 `-148`（§31.1.1）之分工：後者之驗證點為**自設定選單按下該鍵**之流程起點，本列為**該項於本彈窗中被提供**；兩列之來源列不同（**R-CAM10**）。

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
1. Read the pop-up and check that "Edit Name" is offered
2. Select "Edit Name"
3. Read the HU display and check that the name can be edited
```

## expected_result

```
1. "Edit Name" is shown in the pop-up
2. "Edit Name" registers the selection
3. A full QWERTY keyboard is displayed for editing the camera name
```
