# NR1L-RVCHMI-001 — SWE1-RVC-041

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.1.2`（來源列 `NRL-187333`）

## test_item 上半（verbatim，SYS1 逐字）

> If the system technological constraints prevent the camera from displaying the “X” exit button on the camera image while in DRIVE, the camera delay option will not be supported

## reasoning

驗證目標為 §6.1.2 之「X 不可顯示時不支援 camera delay 選項」。設定名逐字取 `forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` `Settings` 分頁 row 467 之 `Rear View Camera Delay*`；依 **R-CAM5(a)** 星號不入 hop label，故寫 `Rear View Camera Delay`。同列之備註欄逐字載 `Not shown if backup cam cannot support showing X button on screen`，即本條之可觀察結果（**不顯示**，非灰階）。設定路徑沿 A 本 `NR1L-RVC-113` 之 App Drawer → Settings 句式（**profile §7.2**）。前提 3 為車輛配置事實、非可注入之訊號，故不寫 `Send CAN`，改記入 `features/camera/data/bench_verify.md` 由實機確認。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera cannot display the "X" exit button on the camera image while in DRIVE
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Read the "Camera" list and check that "Rear View Camera Delay" is not offered
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. "Rear View Camera Delay" is not present in the "Camera" list
```
