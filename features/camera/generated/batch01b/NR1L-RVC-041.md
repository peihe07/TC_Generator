# NR1L-RVC-041 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Additional Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`CFTS092-4781657`（來源列 `SYS-RA-CAM-092`）

## test_item 上半（verbatim，SYS2 逐字）

> If the $Speedometer$ >= [8 MPH], the HU shall grey-out the Surround View Camera soft button, as specified by HMI, within <Tdisplay>.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-092`（ObjectID 4781657，Surround View Camera 節）之「`$Speedometer$ >= [8 MPH]` 時將 SVC 軟鍵灰階」之達標側。供試值取 raw 206 = 12.875 km/h = 8.000154 mph —— 8 mph = 12.874752 km/h 非 0.0625 之整數倍，恰等於 8 mph 之 raw 不存在，raw 206 為**可送之最小達標值**（A-CA30 之同一量測，本列之判準為 `>=`，該不可判性不影響本列之 ER）。`<Tdisplay>` 之值無來源，ER 因而只判灰階之成立而不判其時限（§6 可判性）；未達側（低於門檻）由 `NR1L-RVC-040` 之 raw 205 承接。本列依 **R-CAM13(c)** 落 Test Set `Additional Cameras`（framework Part VIII 第 10 組，CAM-06 重開）；其 SWE 列 `SWE-CAM-016` 於 Layer 2 仍歸 `Display Arbitration`，「組 ↔ SWE 列」與「TC ↔ Test Set」於本組分離。A-CA28 之「不生成」處置作廢。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Surround_View_Camera = 1 (Present)
3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
4. The virtual Surround View Camera button is shown in the available state
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Read the HU display and check the state of the Surround View Camera soft button
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent
2. The Surround View Camera soft button is greyed out
```
