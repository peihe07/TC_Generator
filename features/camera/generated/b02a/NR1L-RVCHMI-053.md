# NR1L-RVCHMI-053 — SWE1-RVC-062

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.2.3.2`（來源列 `NRL-188043`）

## test_item 上半（verbatim，SYS1 逐字）

> Wireless AUX Cams “AUX Cameras” button will be greyed out when wireless cameras are not available

## reasoning

§27.2.3.2 之條件為 `when wireless cameras are not available`；其可觀察之不可用態取 `forms/Pop Up List HMI R1 (26PI).xlsx` `Main` 之 `PU0459` 逐字 `No camera connected. Camera unavailable. Make sure camera is ON and within range`，故前提寫「不在範圍內或未開機」。無線 AUX 相機**無 PROXI 配備旗標** —— 掃描字串 `Wireless_Camera`／`Wireless_Aux`／`Aux_Camera`／`Hotspot` 於 `forms/proxi/` 六本**各 0 命中**；SYS1 以 §27.3.1.x 之硬體條件與 §27.4.1 之 `Enable Wireless Cameras` 設定為替代條件，故依 **R-CAM18(a)** 五款平台皆 `1`，不掛 DR（升級條件 §4-3 不成立）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. No wireless camera is within range or powered on
7. The AUX camera list is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the AUX camera list and check that the "AUX Cameras" button for the wireless camera is greyed out
2. Select the greyed out "AUX Cameras" button
```

## expected_result

```
1. The "AUX Cameras" button for the wireless camera is greyed out
2. The button does not register the selection and no wireless camera view is displayed
```
