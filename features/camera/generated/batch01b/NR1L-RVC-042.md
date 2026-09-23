# NR1L-RVC-042 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Auxiliary Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`CFTS092-4781658`（來源列 `SYS-RA-CAM-093`）

## test_item 上半（verbatim，SYS2 逐字）

> If the $Speedometer$ = [SNA], the HU shall retain the current setting of the Surround View Camera soft button, as specified by HMI, within <Tdisplay>.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-093`（ObjectID 4781658，Surround View Camera 節）之「`$Speedometer$ = [SNA]` 時保持 SVC 軟鍵之現狀」。`SNA` 之 raw 取四本 DBC 之 `VAL_ … 8191 "SNA"`（`VehicleSpeedVSOSig` 為 13 bit，其 VAL 只有 8191 一項，與 `NR1L-RVC-009` 所載同源）。「保持現狀」之可判化：Pre-Condition 4 先把該鍵釘在 available 態，ER 因而為「仍為 available」之具體可讀結果，而非抽象之「retain the current setting」（§6 可判性）。`<Tdisplay>` 無來源，不入 ER。本列依 **R-CAM13(c)** 落 Test Set `Auxiliary Cameras`（framework Part VIII 第 10 組，CAM-06 重開）；其 SWE 列 `SWE-CAM-016` 於 Layer 2 仍歸 `Display Arbitration`，「組 ↔ SWE 列」與「TC ↔ Test Set」於本組分離。A-CA28 之「不生成」處置作廢。

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
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 8191 (SNA)
2. Read the HU display and check the state of the Surround View Camera soft button
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 8191 (SNA) is sent
2. The Surround View Camera soft button is still shown in the available state
```
