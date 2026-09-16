# NR1L-RVC-016 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V3_P363_VF_1099`（來源列 `SYS-RA-VF551_V3-261`）

## test_item 上半（verbatim，SYS2 逐字）

> When Head Unit in Automatic Display Mode, gear shifted out of Reverse to Gear_Stat.Info != [PARK OR REVERSE] AND Camera Delay Enabled: IPC_VEHICLE_SETUP2.Backup_Cam_Delay = [ON] then the Head Unit shall display RVC image associated with the selected gear for a cumulative time period of Ttimer1

## reasoning

驗證目標同 NR1L-RVC-015，為 Atl-Mi 半邊。上半為摘句（§4.3.1）：原句 87 RE_TOKEN，保留條件與 Ttimer1 結果子句，刪去其後之 unless 退出清單（該四項分由 NR1L-RVC-017／-018、-009／-010 與 SWE-CAM-016 之 X 鍵承接），摘後 43 RE_TOKEN。V3 之速度訊號逐字為 BRAKE1.VehicleSpeedVSOSig，該 message 不在四本 DBC（見 A-CA23 同族，DR-CAM-f），故本列不以速度為觸發。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The camera delay setting is set to "On"
4. The rear view camera image is displayed in Automatic Display Mode
5. The vehicle speed is below 8 mph
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted)
2. Read the HU display and check that the rear view camera image is still displayed
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted) is sent
2. The rear view camera image stays displayed for the Ttimer1 period associated with the selected gear
```
