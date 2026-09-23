# NR1L-RVCHMI-130 — SWE1-RVC-110-02

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_29.1.2`（來源列 `NRL-188120`）

## test_item 上半（verbatim，SYS1 逐字）

> From this pop-up the user can: -Add/Remove as a favorite

## reasoning

§29.1.2 之第二項（`-Add/Remove as a favorite`）。其**兩個方向**皆須可得，故以「按下後標籤翻轉」驗之。兩個 label 之逐字分別取 §30.1.2 之 `“Make Favorite”` 與 §30.1.4 之 `“Remove as favorite”`。與 `-143`（§30.1.4）之分工：後者驗**按下 Remove 之後果**（favorite designation 移除），本列只驗兩向**皆被提供**。

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
1. Read the pop-up and check that "Make Favorite" is offered
2. Select "Make Favorite"
3. Read the pop-up and check that the control now reads "Remove as favorite"
```

## expected_result

```
1. "Make Favorite" is shown in the pop-up
2. "Make Favorite" registers the selection
3. The control reads "Remove as favorite", which shows that both add and remove are offered
```
