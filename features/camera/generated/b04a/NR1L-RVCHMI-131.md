# NR1L-RVCHMI-131 — SWE1-RVC-110-03

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_29.1.2`（來源列 `NRL-188120`）

## test_item 上半（verbatim，SYS1 逐字）

> From this pop-up the user can: -Reset the selected camera

## reasoning

§29.1.2 之第三項。`Reset the selected camera` 之**作用**取 §34.9.2.2 之逐字定義 `Reset Camera- Deletes the edited saved name of the camera, returning the name to “AUX Camera 1” or “AUX Camera 2”` —— 該列屬 B04b（§34.9），本列只驗其**於本彈窗被提供**並以「名稱回復預設」為可觀察結果；預設名之逐字由 B04b 之 `-150-0n` 承接。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The camera name has been edited to a name other than the default
4. The individual AUX Cam settings pop-up for the wired camera is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the pop-up and check that the reset control is offered
2. Select the reset control
3. Read the camera line item and check that the name has returned to its default
```

## expected_result

```
1. The reset control is shown in the pop-up
2. The reset control registers the selection
3. The camera name has returned to its default
```
