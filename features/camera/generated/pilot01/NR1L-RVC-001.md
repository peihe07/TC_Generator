# NR1L-RVC-001 — SWE-CAM-001

- **Test Group**：Rear View Camera
- **Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P0｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS-RA-VF551_V33-213`

## test_item 上半（verbatim，SYS2 逐字）

> When LTM_OperationalModeSts.Info ==(equal)"Ignition_On" AND the PROXI parameter Rear_View_Camera==(equal)"Present", LTM starts to read the Rear_Camera.Data.

## reasoning

驗證目標為點火進入 RUN 後 NormalCameraDaemon 完成初始化並開啟 Rear_Camera 資料路徑，觀察面為 adb log 與 camera service 狀態（§5.4 兩行式，命令不入 ER）。關鍵情境條件為 PROXI Rear_View_Camera = 1 (Present)（五車型實測皆同，byte 86 bit 0）與點火訊號轉為 RUN；來源 SYS-RA-VF551_V33-213 寫作 LTM_OperationalModeSts.Info = "Ignition_On"，該值為 LTM 內部狀態，依 §8.7.5(f) 轉為其 CAN 驅動訊號 CmdIgnSts —— Atl-Hi 取 BCM_FD_10.CmdIgnSts（PDT27_E2A_R1_FDCAN8.dbc，BO_ 1153，VAL_ 4 "RUN"，CameraEventHal 表 Y／verified），Atl-Mi 取 STATUS_BH_BCM2.CmdIgnSts（P363_BH-CAN [07338]_3A_R2.dbc，BO_ 1132，同一 VAL_ 列舉）。本列只述一個狀態轉換與其單一可觀察結果，依 §5.7 一觸發多同時結果屬同一 TC，故一條足夠；兩 EE 之訊息名雖異而 ER 相同，依 CAM-03 §3 之判準（ER 相同不拆）合為一列，訊息名分寫於 Pre-Condition。關機側之 teardown 由 NR1L-RVC-002 承接；PowerShutDownNotifcation 之送出依 CAM-03 §3 委派 SWE-CAM-012（§8.2.1）。

## pre_conditions

```
1. PROXI Rear_View_Camera = 1 (Present)
2. PROXI Rear_View_Camera_Type = 1 (Digital) on Atl-Hi vehicles only
3. The ignition is OFF
4. The Head Unit is in its powered-down state
5. On Atl-Mi vehicles the ignition signal is STATUS_BH_BCM2.CmdIgnSts instead of BCM_FD_10.CmdIgnSts
6. adb tool is available on HU
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)
2. Read the NormalCameraDaemon start-up log and check that the daemon reports a completed initialization
   $ adb logcat -d -s NormalCameraDaemon
3. Read the camera service status and check that the Rear_Camera data path is open
   $ adb shell dumpsys media.camera
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 4 (RUN) is accepted and the Head Unit enters the RUN power state
2. The NormalCameraDaemon initialization-complete entry is present in the log
3. The camera service reports the Rear_Camera data path as open
```
