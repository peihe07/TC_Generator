# NR1L-RVCHMI-108 — SWE1-RVC-100

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.4.2`（來源列 `NRL-188101`）

## test_item 上半（verbatim，SYS1 逐字）

> When attempted to activate when greyed out, a popup appears

## reasoning

§28.4.2 只寫「出現一個 popup」而未載其文字；逐字取 **`PU0851`**（module `Aux Camera`；觸發欄逐字 `Message displays when trying to push the AUX camera button and a wireless camera is not connected (applies to all wireless cameras)`）——與本條之情境（無線不可用時嘗試啟用）相符。`PU0459`（`No camera connected …`）之觸發欄為 `a camera is not connected`（不限無線），已由 B02a `-060` 用於 §27.3.3，兩者不重複。ER 形制依 **profile §7.8**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. No wireless camera is within range or powered on
7. The AUX camera list is displayed with the wireless AUX soft controls greyed out
```

## input_test_data

`NA`

## test_procedure

```
1. Select the greyed out wireless AUX soft control
2. Read the pop-up text on the HU display
```

## expected_result

```
1. The greyed out soft control registers the selection and a pop-up appears
2. The pop-up reads "Camera Unavailable . Please go to camera settings and connect the wireless camera." (PU0851 of the R1 HMI pop-up list)
```
