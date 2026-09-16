# NR1L-RVC-006 — SWE-CAM-016

- **Test Group**：Rear View Camera
- **Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：情境 / 用例 (Scenario / Use Case Testing)
- **specification_reference**：`SYS-RA-VF551_V2-549`

## test_item 上半（verbatim，SYS2 逐字）

> · HU shall acquire the HU touch screen coordinates pressed by the driver to defeat Rear View Camera View via RVC Image soft button and set internal Signal RVC_ImageDefeat.Req = Pressed.

## reasoning

驗證目標為手動模式下按 "X" 關閉 RVC 並回到前一畫面內容，即 SYS-RA-VF551_V2-549 之 "defeat Rear View Camera View via RVC Image soft button" 與其 RVC_ImageDefeat.Req = Pressed。**錨不取 CFTS092 SYS-RA-CAM-082** —— 該來源同為 SWE-CAM-001 所引，依 R-CAM10 由 SWE ID 較小者承接，故本列委派 SWE-CAM-001，只以 -016 獨有之 V2-549 為錨。關鍵情境條件為已以手動方式開啟 RVC（沿用 NR1L-RVC-005 之入口 hop），排檔不在 R —— "X" 鍵僅於非 R 檔時疊加（SYS-RA-VF551_V2-533、V4-115、V42-299 三本同義）。回前一畫面之行為以 SYS1 RVC+PAM §8.3.2（SWE1-RVC-029）為互參寫法，依 R-CAM1(c) 不複製其 spec_reference，本列之錨仍為 CFTS092 SYS-RA-CAM-082。本列與 NR1L-RVC-005 同 req_id，依 §8.3 之 mode 軸拆為開啟／關閉兩 sibling。「X 鍵於 DRIVE 檔無法顯示時不支援 camera delay」之約束（SYS1 §6.1.2）不屬本列，屬 SWE-CAM-018 之 delay 線（crossref 已判 -021／-023 × RVC-030 為 REJECTED）。

## pre_conditions

```
1. PROXI Rear_View_Camera = 1 (Present)
2. The Head Unit is in the RUN power state
3. The shift lever is in P
4. The rear view camera image is already shown in Manual Display Mode
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Rear View Camera" in the App Drawer
3. Press "X" on the top right corner of the rear view camera image
4. Read the Head Unit display and check that the content shown before the camera was opened is restored
```

## expected_result

```
1. The App Drawer is displayed
2. The rear view camera image is shown with the "X" exit button overlaid
3. The rear view camera image is closed
4. The Head Unit shows the content that was displayed before the camera image was opened
```
