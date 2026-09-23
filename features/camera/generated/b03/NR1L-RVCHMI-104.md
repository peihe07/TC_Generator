# NR1L-RVCHMI-104 — SWE1-RVC-097

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.3.1`（來源列 `NRL-188097`）

## test_item 上半（verbatim，SYS1 逐字）

> If AUX camera is not connected, display blue screen “camera system unavailable”

## reasoning

§28.3 之父題逐字為 `Accessing Wired AUX – Cameras Not Connected`（`NRL-188096`）。本條與 §34.8.2（`NR1L-RVCHMI-096`）**逐字全等**，惟**父題相異** ——後者之父為 `Accessing AUX – Cameras Not Connected`（§34，R1 Low），本列之父為 §28.3（R1 High 之 Wired AUX）；依 **R-CAM16(c)** 父題相異者各自出 TC。彈窗表之 `Camera System Unavailable` 命中 6 筆皆非 `Aux Camera` module，惟文字由來源自載，**不掛 DR-CAM-h**（同 `-096` 之理）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. No AUX camera is connected
3. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Press the AUX camera button in the App Drawer
3. Read the HU display and check the screen colour and the message text
```

## expected_result

```
1. The App Drawer is displayed
2. The AUX camera button registers the press
3. The display is a blue screen and reads "camera system unavailable"
```
