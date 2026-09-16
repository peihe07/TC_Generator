# NR1L-RVC-026 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V3_P363_VF_1100`（來源列 `SYS-RA-VF551_V3-265`）

## test_item 上半（verbatim，SYS2 逐字）

> When Head Unit in Manual Display mode AND RVC image active, the Head Unit shall continue to display RVC image unless one of these conditions occur: STATUS_BH_BCM2.CmdIgnSts != [RUN] OR Shift Lever status change to "Park" from other gears: Gear_Stat.Info = [PARK] OR max out Ttimer2 OR RVC_ImageDefeat.Req = [Pressed].

## reasoning

驗證目標為 SYS-RA-VF551_V3-265 之「手動模式下 RVC 影像續顯，直至 Ttimer2 到期或其他三條件之一成立」，即手動啟動對速度限制之旁路。上半為摘句（§4.3.1）：原句 93 RE_TOKEN，保留主句與其 unless 四條件清單，刪去其後之 a) Ttimer2 起停細則（該細則由 NR1L-RVC-029 承接），摘後 48 RE_TOKEN。速度值之換算見 DECISIONS 6-10（raw 206 = 12.875 km/h = 8.000154 mph）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
4. The rear view camera image is displayed in Manual Display Mode
5. The shift lever is in D
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Read the HU display and check that the rear view camera image is still displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent
2. The rear view camera image stays displayed until Ttimer2 maxes out
```
