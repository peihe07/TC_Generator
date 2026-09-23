# NR1L-RVC-094 — SWE-CAM-017

- **Test Group**：Rear View Camera｜**Test Set**：Additional Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781663`（來源列 `SYS-RA-CAM-098`）

## test_item 上半（verbatim，SYS2 逐字）

> The HU shall continue to send $CameraDisplaySts$ = [Default] signal until next keypress.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-098`（ObjectID 4781663，Forward Facing Camera 節）之「持續送 `$CameraDisplaySts$ = [Default]` 直到下一次按鍵」。**ER 避開不可判之 `until`**（CAM-06 審閱 §二-3 之同型）—— 以「保持 10 秒不按鍵後讀取」之定點觀察表達持續性；`10 s` 為觀察窗而非來源之標定值，故不入 test_item。「下一次按鍵後之改變」屬去程（`NR1L-RVC-045` 之 `View 3`），本列只驗維持（§8.2.1 分工）。車型與訊號之依據同 `NR1L-RVC-093`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Forward_Facing_Camera = 1 (Present)
3. RADIO_B3.CameraDisplaySts = 0 (Default) is being sent
4. A bus analyzer is connected to the vehicle bus
```

## input_test_data

`NA`

## test_procedure

```
1. Hold for 10 s without pressing any button on the HU
2. Read RADIO_B3.CameraDisplaySts and check that it is still 0 (Default)
```

## expected_result

```
1. No button is pressed for 10 s
2. RADIO_B3.CameraDisplaySts = 0 (Default) is still sent
```
