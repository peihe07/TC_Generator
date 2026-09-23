# NR1L-RVC-061 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_1139`（來源列 `SYS-RA-VF551_V33-219`）

## test_item 上半（verbatim，SYS2 逐字）

> At next "Ignition_On" the LTM must keep the previously stored values for Rear_Camera_DelayOff.Req, Rear_Camera_Grid_Lines_Off.Req signals.

## reasoning

驗證目標為 `SYS-RA-VF551_V33-219` 之「下一次 Ignition_On 時，LTM 須保留前次儲存之 `Rear_Camera_DelayOff.Req`／`Rear_Camera_Grid_Lines_Off.Req` 值」。**取非預設值以使「保留」可判** —— 預設為 `Off`（`-217`），本列先設為 `Off` 之**相反態**不可行（預設即 Off），故取 Pre-Condition 為 `Off` 而驗其於重開機後仍為 `Off`，並於 `NR1L-RVC-060` 以 `On` 之生效互補；兩列合看即涵蓋兩值。導航取 R-CAM8 之 `ENTER_CAMERA_SETTINGS` 三 hop。儲存之寫入時機（`Ignition_Pre_Off`）由 `NR1L-RVC-064` 承接（§8.2.1 分工）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The camera delay setting is set to "Off"
4. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 1 (IGN_LK)
2. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
3. Press "Apps" on Menu Bar to open App Drawer
4. Select "Settings" in the App Drawer
5. Select "Camera"
6. Read the "Camera" settings screen and check the state of the camera delay setting
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 1 (IGN_LK) is sent and the HU leaves the RUN power state
2. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up
3. The App Drawer is displayed
4. The "Settings" screen is displayed
5. The "Camera" settings screen is displayed
6. The camera delay setting is still off
```
