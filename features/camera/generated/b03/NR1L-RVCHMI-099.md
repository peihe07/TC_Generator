# NR1L-RVCHMI-099 — SWE1-RVC-092

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.1`（來源列 `NRL-188090`）

## test_item 上半（verbatim，SYS1 逐字）

> More Cams Button is present in the More AUX row of buttons. It will provide access to the camera app popup as defined in the camera app section.

## reasoning

§28 之父題逐字為 `Accessing More Cams – from Aux Cameras`（`NRL-188089`）。彈窗逐字取 `forms/Pop Up List HMI R1 (26PI).xlsx` `Main` 之 **`PU0853`**（module `Aux Camera`；觸發欄 `In reverse with surround view when more cams is selected this displays`；文字欄 `More Vehicle Cameras <X>` ＋ `available preset cameras listed` ／`available wireless cameras listed`），故前提加 `Surround_View_Camera = 1`。`as defined in the camera app section` 指向 §19～§22（`Camera App` 章），**HU 章 18–22 為 B 本 230 列一列未引之範圍**（**A-CA12**），依 §8.4.2 不測其內容。`Surround_View_Camera` 於 `Toro_ATL_MI` 零命中 → **R-CAM18(b)** `Toro(2261)` 判 `0`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Surround_View_Camera = 1 (Present)
3. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
4. Two wired AUX cameras are connected
5. The AUX 1 camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the More AUX row of buttons and check that the "More Cams" button is present
2. Press the "More Cams" button
3. Read the pop-up and check that the available camera views are listed
```

## expected_result

```
1. The "More Cams" button is shown in the More AUX row of buttons
2. The "More Cams" button registers the press and the camera app pop-up opens
3. The pop-up reads "More Vehicle Cameras" with the available preset cameras and the available wireless cameras listed (PU0853)
```
