# NR1L-RVCHMI-077 — SWE1-RVC-087

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.8.1`（來源列 `NRL-188083`）

## test_item 上半（verbatim，SYS1 逐字）

> When “More Aux” button is pressed a popup opens up with all available aux cameras as selectable buttons

## reasoning

§27.8 之父題逐字為 `Accessing Aux Cameras – from Rear View Camera`（`NRL-188082`），故前提取 `Rear_View_Camera = 1` 與「後視影像顯示中」。`all available aux cameras` 之 `all` 須以**兩台**以上才驗得，故前提佈兩台。`“More Aux”` 為逐字按鍵名（§28.1 另有 `More Cams Button`，屬 `Camera View Switching` 組，非本列）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. Two wired AUX cameras are connected
4. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "More Aux" button in the rear view camera image
2. Read the pop-up and check that both connected AUX cameras are offered as selectable buttons
```

## expected_result

```
1. The "More Aux" button registers the press and a pop-up opens
2. Both connected AUX cameras are shown in the pop-up as selectable buttons
```
