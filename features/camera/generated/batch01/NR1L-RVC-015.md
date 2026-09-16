# NR1L-RVC-015 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_479`（來源列 `SYS-RA-VF551_V2-497`）

## test_item 上半（verbatim，SYS2 逐字）

> When Head Unit is in Automatic Display Mode AND Gear shifted out of Reverse to ShiftLeverPosition != "P" or "R", Camera Delay Enabled: IPC_VEHICLE_SETUP.Backup_Cam_Delay = ON. the Head Unit shall display RVC image associated with the selected gear for the cumulative time period of Ttimer1.

## reasoning

驗證目標為自動模式下退出 R 檔且 Camera Delay 為 On 時，影像依 Ttimer1 續顯，即 SYS-RA-VF551_V2-497 之逐字條件。上半為摘句（§4.3.1）：原句 52 RE_TOKEN 逾限，刪行首列點符號與「all of the following condition hold true:」之贅語，保留條件（Gear shifted out of Reverse、Backup_Cam_Delay = ON）與結果（display RVC image … Ttimer1）子句，摘後 43 RE_TOKEN，全文以 spec_reference 指回。Ttimer1 之 10 s 到期退出由 NR1L-RVC-007／-008 承接；速度門檻提前退出由 -009／-010 承接（§8.2.1）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Rear_View_Camera_Type = 1 (Digital)
4. The camera delay setting is set to "On"
5. The rear view camera image is displayed in Automatic Display Mode
6. The vehicle speed is below 8 mph
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 4 (D)
2. Read the HU display and check that the rear view camera image is still displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 4 (D) is sent
2. The rear view camera image stays displayed for the Ttimer1 period associated with the selected gear
```
