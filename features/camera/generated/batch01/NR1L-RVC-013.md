# NR1L-RVC-013 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1065`（來源列 `SYS-RA-VF551_V2-495`）

## test_item 上半（verbatim，SYS2 逐字）

> · When Head Unit is in Automatic Display Mode AND all of the following conditions hold true: - Gear shifted out of Reverse: ShiftLeverPosition != R - Camera Delay Disabled: IPC_VEHICLE_SETUP.Backup_Cam_Delay = OFF. the Head Unit shall switch back to non-camera display

## reasoning

驗證目標為自動模式下退出 R 檔且 Camera Delay 為 Off 時立即回到非相機畫面，即 SYS-RA-VF551_V2-495 之逐字條件（IPC_VEHICLE_SETUP.Backup_Cam_Delay = OFF）。Delay 不走 CAN（CameraEventHal 表該訊號 Harman = N／Not yet），以 HMI 設定表達其狀態，設定本身之操作由 NR1L-RVC-007／-008 承接（§8.2.1）。Delay 為 On 之對應行為由 NR1L-RVC-015 承接。Atl-Mi 半邊見 NR1L-RVC-014。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Rear_View_Camera_Type = 1 (Digital)
4. The camera delay setting is set to "Off"
5. The rear view camera image is displayed in Automatic Display Mode
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 4 (D)
2. Read the HU display and check that the rear view camera image is no longer displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 4 (D) is sent
2. The rear view camera image is no longer displayed and the previous screen is shown again
```
