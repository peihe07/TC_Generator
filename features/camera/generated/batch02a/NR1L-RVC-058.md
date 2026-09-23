# NR1L-RVC-058 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_303`（來源列 `SYS-RA-VF551_V33-213`）

## test_item 上半（verbatim，SYS2 逐字）

> When LTM_OperationalModeSts.Info ==(equal)"Ignition_On" AND the PROXI parameter Rear_View_Camera==(equal)"Present", LTM starts to read the Rear_Camera.Data.

## reasoning

驗證目標為 `SYS-RA-VF551_V33-213` 之「`LTM_OperationalModeSts.Info = "Ignition_On"` 且 PROXI `Rear_View_Camera = "Present"` 時，LTM 開始讀取 `Rear_Camera.Data`」。`LTM_OperationalModeSts.Info` 為 V33／V42 之來源名，依 §8.7.5(f) 保留；其對 `CmdIgnSts` 之值對應除 `Ignition_Pre_Off` 外皆以 RUN 表達（DR-CAM-i 只及該一值）。觀察手段沿 pilot02 `NR1L-RVC-002` 已用之 `dumpsys media.camera` 兩行式（§5.4）；該句式為本 feature 之既有用例，非新造。PROXI 不成立側（`Absent`）之行為**無來源**（RDF-06 之同型：V33 亦只有成立側），不生成。`Rear_Camera.Data` 為 V33 之內部資料名（四本 DBC 零命中），以資料路徑之開啟為可判後果。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Read the camera service status and check that the Rear_Camera data path is open
   $ adb shell dumpsys media.camera
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up
2. The Rear_Camera data path is open and the HU is reading Rear_Camera.Data
```
