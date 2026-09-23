# NR1L-RVCHMI-107 — SWE1-RVC-099

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.4.1`（來源列 `NRL-188100`）

## test_item 上半（verbatim，SYS1 逐字）

> When Wireless Auxiliary cameras are not available (not present or not available for use), the associated soft controls will be greyed out

## reasoning

§28.4 之父題逐字為 `Accessing Wireless AUX – Cameras Not Available`（`NRL-188099`）。來源以括號逐字界定不可用之兩態 `(not present or not available for use)`；取「不在範圍內或未開機」為其可佈之形式，該形式之逐字依據為 `PU0851` 之文字欄 `Camera Unavailable . Please go to camera settings and connect the wireless camera.`與 `PU0459` 之 `Make sure camera is ON and within range`（皆 module `Aux Camera`）。與 B02a `-053`（§27.2.3.2）之分工：後者為 `Indications for System States` 節之**`“AUX Cameras”` 按鍵**灰階，本列為 §28.4 之**各該無線視角 soft control** 灰階；兩列之來源節與承接列皆不同（**R-CAM10**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. No wireless camera is within range or powered on
7. A wired AUX camera is connected
8. The AUX camera list is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the AUX camera list and check that the wireless AUX soft controls are greyed out
2. Read the AUX camera list and check that the wired AUX soft control is not greyed out
```

## expected_result

```
1. The wireless AUX soft controls are greyed out
2. The wired AUX soft control is not greyed out, which shows that the greying is bound to the wireless cameras being unavailable
```
