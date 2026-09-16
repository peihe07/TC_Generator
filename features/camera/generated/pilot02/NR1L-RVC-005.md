# NR1L-RVC-005 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_532`（來源列 `SYS-RA-VF551_V2-545`）

## test_item 上半（verbatim，SYS2 逐字）

> · HU shall acquire the HU touch screen coordinates pressed by the driver to enable Rear View Camera View via app drawer soft button and set internal Signal APP_Menu_BACKUP.Req= Pressed.

## reasoning

驗證目標為使用者自 App Drawer 手動開啟 RVC，即 SYS-RA-VF551_V2-545 之 "enable Rear View Camera View via app drawer soft button"。關鍵情境條件為 Full-Operation 態（涵蓋 SYS-RA-VF551_V2-534 所定之 CmdIgnSts = RUN 軟鍵可用前提）且排檔不在 R，以與 NR1L-RVC-003／004 之自動模式區隔。導航 hop 之來源：第一 hop 為 §5.3 已鎖定之 ENTER_APP_DRAWER；第二 hop "Rear View Camera" 逐字取自 SYS1 Menu Bar and App Drawer §4.1 naming table（NRL-127734，Feature Name／Drawer Name 欄），符合 §5.8(c)。未走 controls page —— SYS1 HeadUnitCameraSystems §6.5.1（NRL-187347）只列舉三入口而無 label，依 §5.8(d) 不得臆造（A-CA24／DR-CAM-g）。design_method 依 §12 tie-break 取功能測試：步驟 3 步、單一 feature，不構成 Scenario（CAM-03 審閱 §二-7）。關閉行為由 NR1L-RVC-006 承接（§8.2.1）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)
4. The shift lever is in P
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Rear View Camera" in the App Drawer
3. Read the HU display and check that the rear view camera image is displayed in Manual Display Mode
```

## expected_result

```
1. The App Drawer is displayed
2. The rear view camera image is displayed
3. The rear view camera image is displayed in Manual Display Mode with the "X" exit button overlaid
```
