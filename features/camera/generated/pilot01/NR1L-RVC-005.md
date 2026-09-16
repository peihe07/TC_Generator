# NR1L-RVC-005 — SWE-CAM-016

- **Test Group**：Rear View Camera
- **Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：情境 / 用例 (Scenario / Use Case Testing)
- **specification_reference**：`SYS-RA-VF551_V2-545`

## test_item 上半（verbatim，SYS2 逐字）

> · HU shall acquire the HU touch screen coordinates pressed by the driver to enable Rear View Camera View via app drawer soft button and set internal Signal APP_Menu_BACKUP.Req= Pressed.

## reasoning

驗證目標為使用者自 App Drawer 手動開啟 RVC，即 SYS-RA-VF551_V2-545 之 "enable Rear View Camera View via app drawer soft button"。關鍵情境條件為點火 RUN（SYS-RA-VF551_V2-534 明定軟鍵僅於 CmdIgnSts = RUN 時可用）且排檔不在 R，以與 NR1L-RVC-003／004 之自動模式區隔。導航 hop 之來源：第一 hop 為 §5.3 已鎖定之 ENTER_APP_DRAWER；第二 hop "Rear View Camera" 逐字取自 SYS1 Menu Bar and App Drawer §4.1 naming table（NRL-127734，Feature Name ／ Drawer Name 欄），符合 §5.8(c) 之 HMI 來源。**未走 controls page 路徑** —— SYS1 HeadUnitCameraSystems §6.5.1（NRL-187347）只列舉「controls page, apps drawer, or camera app」三入口而無可逐字引用之 label，依 §5.8(d) 不得臆造，已登 A-CA24／DR-CAM-g；apps drawer 亦為該條所列之入口，故不受阻。關閉行為由 NR1L-RVC-006 承接（§8.2.1）。

## pre_conditions

```
1. PROXI Rear_View_Camera = 1 (Present)
2. The Head Unit is in the RUN power state
3. The shift lever is in P
4. No camera image is shown
5. On Atl-Mi vehicles the ignition signal is STATUS_BH_BCM2.CmdIgnSts instead of BCM_FD_10.CmdIgnSts
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)
2. Press "Apps" on Menu Bar to open App Drawer
3. Select "Rear View Camera" in the App Drawer
4. Read the Head Unit display and check that the rear view camera image is shown in Manual Display Mode
```

## expected_result

```
1. The Head Unit stays in the RUN power state
2. The App Drawer is displayed
3. The rear view camera image is shown
4. The rear view camera image is shown in Manual Display Mode and the "X" exit button is overlaid on the image
```
