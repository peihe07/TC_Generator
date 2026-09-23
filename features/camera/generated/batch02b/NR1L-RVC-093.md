# NR1L-RVC-093 — SWE-CAM-017

- **Test Group**：Rear View Camera｜**Test Set**：Auxiliary Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`CFTS092-4781662`（來源列 `SYS-RA-CAM-097`）

## test_item 上半（verbatim，SYS2 逐字）

> The HU shall follow this signal with an on-change $CameraDisplaySts$ = [Default] signal within a time period of <Tsend>.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-097`（ObjectID 4781662，**Forward Facing Camera 節**）之「HU 於 <Tsend> 內以 on-change 送 `$CameraDisplaySts$ = [Default]`」。**Test Set `Auxiliary Cameras`** —— `SWE-CAM-017` 於 framework VIII.2 已改歸該組（CAM-06 重開）。訊號與值實測：`RADIO_B3.CameraDisplaySts`（`BO_ 1283`）之 `VAL_ … 0 "Default"`，見 `forms/PDT27_E2A_R1_BHCAN2.dbc` 與 `forms/Project__637MCA_BH-CAN_R1_…dbc`。**376 勾 0** —— `forms/P363_BH-CAN [07338]_3A_R2.dbc` 有 `BO_ 1283 RADIO_B3` 但全本無 `CameraDisplaySts` 訊號，ER 不可觀察（同 `NR1L-RVC-045`）；2261 之 PROXI 無 `Forward_Facing_Camera`（DR-CAM-l）故亦勾 0。`<Tsend>` 之值無來源，標 `PENDING: DR-CAM-j`。觸發取 `[View 3]` → `[Default]` 之狀態變化，其去程（按鍵送 `View 3`）由 `NR1L-RVC-045` 承接。**VC／VM 欄之 Air Suspension 與 4X→1X 不生成** —— 對應不到 `-017` 所引之任一來源（R-CAM13(d)、RDF-02）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Forward_Facing_Camera = 1 (Present)
3. The Forward Facing Camera image is displayed
4. A bus analyzer is connected to the vehicle bus
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "X" exit button on the top right corner of the HU display
2. Read RADIO_B3.CameraDisplaySts and check that it is 0 (Default), and check the time between step 1 and its transmission
```

## expected_result

```
1. The Forward Facing Camera image is closed
2. RADIO_B3.CameraDisplaySts = 0 (Default) is sent on change and PENDING: DR-CAM-j within Tsend of the state change
```
