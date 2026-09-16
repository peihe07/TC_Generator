# NR1L-RVC-006 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_548`（來源列 `SYS-RA-VF551_V2-549`）

## test_item 上半（verbatim，SYS2 逐字）

> · HU shall acquire the HU touch screen coordinates pressed by the driver to defeat Rear View Camera View via RVC Image soft button and set internal Signal RVC_ImageDefeat.Req = Pressed.

## reasoning

驗證目標為手動模式下按 "X" 關閉 RVC 並回到前一畫面，即 SYS-RA-VF551_V2-549 之 "defeat Rear View Camera View via RVC Image soft button" 與 RVC_ImageDefeat.Req = Pressed。錨不取 CFTS092 SYS-RA-CAM-082 —— 該來源同為 SWE-CAM-001 所引，依 R-CAM10 由 SWE ID 較小者承接，本列委派 SWE-CAM-001。關鍵情境條件為排檔不在 R —— "X" 鍵僅於非 R 檔時疊加（SYS-RA-VF551_V2-533、V4-115、V42-299 三本同義）。開啟為本列之 setup 步驟而非前提（§4.4），故 Pre-Condition 不再宣告影像已顯示（CAM-03 審閱 §二-2）。回前一畫面之行為以 SYS1 RVC+PAM §8.3.2（SWE1-RVC-029）為互參寫法，依 R-CAM1(c) 不複製其 spec_reference。design_method 取狀態轉換：本列驗相機顯示態 → 非顯示態之轉換與其還原（CAM-03 審閱 §二-7 擇一）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)
4. The shift lever is in P
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Rear View Camera" in the App Drawer
3. Press "X" on the rear view camera image
4. Read the HU display and check that the screen shown before the camera was opened is restored
```

## expected_result

```
1. The App Drawer is displayed
2. The rear view camera image is displayed with the "X" exit button overlaid
3. The rear view camera image is closed
4. The screen that was displayed before the camera image was opened is shown again
```
