# NR1L-RVC-043 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Auxiliary Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781656`（來源列 `SYS-RA-CAM-091`）

## test_item 上半（verbatim，SYS2 逐字）

> When the user presses the Surround View Camera Softkey button, the HU shall send the $TGW_DISP_STAT$ signal. See {CFTS020} for the signal value the HU shall set it to.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-091`（ObjectID 4781656，Surround View Camera 節）之「按下 SVC 軟鍵後送出 `$TGW_DISP_STAT$`，其值見 {CFTS020}」。依 **R-CAM13(b)**，本條文為 037 所引，不受 §8.4.2 之「不測外部規格」所擋，故生成。**值查無** —— 承載訊號為 `TELEMATIC_DISPLAY2.TGW_DISP_STATSts`（四本 DBC 皆有，`BO_ 1500`），其 `VAL_` 十六項中無 Surround View 之項（最近者為 `7 "Rear_Camera_Display"`）；CFTS020（`R1LR_Atl-H_25PI3.5_Cabin_CFTS_020 ICS and DCSD_20250910_1124.reqifz`）全文之 `$TGW_DISP_STAT$` 值域為 `DISP_OFF`／`DISP_NORMAL`／`DISP_BLANK`／`DISP_ON`／`DISP_SPLSH`／`DISP_TMF`／`DISP_TMP`／`DISP_REAR_CAMERA`／`DISP_VES_*`／`DISP_DTV_*`／`ON_BLANK`／`SNA`，**亦無 Surround View 之項**（`SVC` 零命中）。值因而標 `PENDING: DR-CAM-j`。本列依 **R-CAM13(c)** 落 Test Set `Auxiliary Cameras`（framework Part VIII 第 10 組，CAM-06 重開）；其 SWE 列 `SWE-CAM-016` 於 Layer 2 仍歸 `Display Arbitration`，「組 ↔ SWE 列」與「TC ↔ Test Set」於本組分離。A-CA28 之「不生成」處置作廢。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Surround_View_Camera = 1 (Present)
3. PENDING: DR-CAM-j CFTS020 defines no TGW_DISP_STAT value for the Surround View Camera
4. The shift lever is in P
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Connect a bus analyzer to the vehicle bus and start recording
2. Press the Surround View Camera Softkey button on the HU display
3. Read the bus analyzer recording and check the TELEMATIC_DISPLAY2.TGW_DISP_STATSts signal
```

## expected_result

```
1. The bus analyzer is recording the vehicle bus
2. The Surround View Camera Softkey button registers the press
3. PENDING: DR-CAM-j the HU transmits TELEMATIC_DISPLAY2.TGW_DISP_STATSts with the value that CFTS020 defines for the Surround View Camera
```
