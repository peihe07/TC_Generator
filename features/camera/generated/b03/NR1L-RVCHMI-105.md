# NR1L-RVCHMI-105 — SWE1-RVC-098-01

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.3.2`（來源列 `NRL-188098`）

## test_item 上半（verbatim，SYS1 逐字）

> If a Wired AUX is connected, but Wired AUX 1 is not connected, system shall display blue screen “camera system unavailable” with customer option to select More AUX, then an available AUX.

## reasoning

§28.3.2 之前半（兩步選取：`More AUX` → `an available AUX`）。與 §34.8.3（`NR1L-RVCHMI-097`）之分工：後者之選項為**直接選 AUX 2**（一步），本列為 `More AUX` 再選（兩步），且父題相異（§28.3 R1 High vs §34.8 R1 Low）。verbatim 為該列 Description 之保序子序列（刪末句，由 `-106` 承接）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera other than AUX 1 is connected
3. Wired AUX 1 is not connected
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Press the AUX camera button in the App Drawer
3. Read the HU display and check the screen colour, the message text and the offered option
4. Select "More AUX" and then the available AUX camera
5. Read the HU display and check that the available AUX camera view is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The AUX camera button registers the press
3. The display is a blue screen, reads "camera system unavailable" and offers "More AUX"
4. "More AUX" opens the list and the available AUX camera is selected
5. The available AUX camera view is displayed
```
