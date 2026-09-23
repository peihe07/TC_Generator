# NR1L-RVC-045 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Auxiliary Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781661`（來源列 `SYS-RA-CAM-096`）

## test_item 上半（verbatim，SYS2 逐字）

> When the Forward Facing Camera soft button pressed, the HU shall send an on-change $CameraDisplaySts$ = [View 3] to the CVPM within <Tsend> of keypress.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-096`（ObjectID 4781661，Forward Facing Camera 節）之「按下 FFC 軟鍵後於 <Tsend> 內送 on-change `$CameraDisplaySts$ = [View 3]` 給 CVPM」。**訊號與值有來源** —— `RADIO_B3.CameraDisplaySts`（`BO_ 1283`）之 `VAL_ … 3 "View_3"`，見 `forms/PDT27_E2A_R1_BHCAN2.dbc` 與 `forms/Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc`，故 raw 3 可逐字書寫。**376 勾 0** —— `forms/P363_BH-CAN [07338]_3A_R2.dbc` 有 `BO_ 1283 RADIO_B3` 但全本無 `CameraDisplaySts` 訊號（字面掃描零命中），該平台之 ER 不可觀察；2261 勾 0 之由同其餘各列（PROXI 查無）。`<Tsend>` 之值無來源，標 `PENDING: DR-CAM-j`。本列之 `$CameraDisplaySts$` 與 `SWE-CAM-017` 所引之 `SYS-RA-CAM-097`／`-098`（同節、`= [Default]` 側）為不同值之不同驗證點，`-017` 屬 batch02。本列依 **R-CAM13(c)** 落 Test Set `Auxiliary Cameras`（framework Part VIII 第 10 組，CAM-06 重開）；其 SWE 列 `SWE-CAM-016` 於 Layer 2 仍歸 `Display Arbitration`，「組 ↔ SWE 列」與「TC ↔ Test Set」於本組分離。A-CA28 之「不生成」處置作廢。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Forward_Facing_Camera = 1 (Present)
3. CAN source: RADIO_B3.CameraDisplaySts (HDCC27, DT27) / RADIO_B3.CameraDisplaySts (637)
4. The shift lever is in P
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Connect a bus analyzer to the vehicle bus and start recording
2. Press the virtual Forward Facing Camera button on the HU display
3. Read the bus analyzer recording and check RADIO_B3.CameraDisplaySts and the time between the keypress and its transmission
```

## expected_result

```
1. The bus analyzer is recording the vehicle bus
2. The virtual Forward Facing Camera button registers the press
3. RADIO_B3.CameraDisplaySts = 3 (View_3) is transmitted on change and PENDING: DR-CAM-j within Tsend of the keypress
```
