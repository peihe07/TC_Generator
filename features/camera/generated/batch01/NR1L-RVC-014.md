# NR1L-RVC-014 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V3_P363_VF_1098`（來源列 `SYS-RA-VF551_V3-262`）

## test_item 上半（verbatim，SYS2 逐字）

> · When Head Unit in Automatic Display Mode, gear shifted out of Reverse: Gear_Stat.info != [REVERSE] AND Camera Delay Disabled: IPC_VEHICLE_SETUP2.Backup_Cam_Delay = [OFF] then the Head Unit shall switch back to non-camera display.

## reasoning

驗證目標同 NR1L-RVC-013，為 Atl-Mi 半邊；verbatim 取 SYS-RA-VF551_V3-262（V3 §1.10.2.2），其設定名為 IPC_VEHICLE_SETUP2.Backup_Cam_Delay（V3 之寫法）。退出觸發依 §8.7.5(f) 取 STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted)。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The camera delay setting is set to "Off"
4. The rear view camera image is displayed in Automatic Display Mode
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted)
2. Read the HU display and check that the rear view camera image is no longer displayed
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted) is sent
2. The rear view camera image is no longer displayed and the previous screen is shown again
```
