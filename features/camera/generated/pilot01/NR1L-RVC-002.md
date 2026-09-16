# NR1L-RVC-002 — SWE-CAM-001

- **Test Group**：Rear View Camera
- **Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS-RA-VF551_V33-220`

## test_item 上半（verbatim，SYS2 逐字）

> When LTM_OperationalModeSts.Info pass into "Ignition_Pre_Off: LTM stops to read the Rear_Camera.Data it stops to copy the Rear_Camera.Data into Rear_Camera_Repetition.Data Rear_Camera_Enable.Info="False". LTM sets RVC_ACTIVE=True internal variable.

## reasoning

驗證目標為點火離開 RUN 後 NormalCameraDaemon 停止讀取 Rear_Camera.Data 並關閉資料路徑，即 SYS-RA-VF551_V33-220 之 "Ignition_Pre_Off" 轉態。關鍵情境條件為已完成初始化之 RUN 態，再將 CmdIgnSts 由 4 (RUN) 降為 1 (IGN_LK)（VAL_ 逐字取自 PDT27_E2A_R1_FDCAN8.dbc BO_ 1153；Atl-Mi 同名訊號於 BO_ 1132）。本列與 NR1L-RVC-001 同 req_id 而為關機側之反向轉態，依 §8.3 之 mode 軸拆為 sibling。刻意不涵蓋 PowerShutDownNotifcation.Power_Down 之送出 —— CAM-03 §3 明文委派 SWE-CAM-012（§8.2.1）；該訊息名之拼法依 R-13 以 VF551_V2 docx 原文為準（A-CA10 已 RESOLVED）。

## pre_conditions

```
1. PROXI Rear_View_Camera = 1 (Present)
2. The Head Unit is in the RUN power state with the NormalCameraDaemon initialized
3. On Atl-Mi vehicles the ignition signal is STATUS_BH_BCM2.CmdIgnSts instead of BCM_FD_10.CmdIgnSts
4. adb tool is available on HU
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 1 (IGN_LK)
2. Read the NormalCameraDaemon log and check that the daemon reports the camera data path closed
   $ adb logcat -d -s NormalCameraDaemon
3. Read the camera service status and check that no Rear_Camera data path remains open
   $ adb shell dumpsys media.camera
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 1 (IGN_LK) is accepted and the Head Unit leaves the RUN power state
2. The NormalCameraDaemon teardown entry is present in the log and no camera data is copied any more
3. The camera service reports no open Rear_Camera data path
```
