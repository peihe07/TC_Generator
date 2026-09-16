# NR1L-RVC-024 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`CFTS092-4781639`（來源列 `SYS-RA-CAM-074`）

## test_item 上半（verbatim，SYS2 逐字）

> When the signal $PowerMode$ <> [IGN_RUN], the HU shall follow the HMI Logic & Flow to update the state of the Rear View Camera soft button.

## reasoning

驗證目標為 CFTS092 SYS-RA-CAM-074（ObjectID 4781639）之「$PowerMode$ <> [IGN_RUN] 時依 HMI L&F 更新軟鍵狀態」。錨取 Rear Camera 節（R-CAM12）。來源之 $PowerMode$ 為設定／參數標記（§8.7.5(f)），其 CAN 對應依 VF551_V2-534 為 BCM_FD_10.CmdIgnSts，故以 3 (ACC) 表達非 RUN 態。成立側由 NR1L-RVC-023 承接。

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
1. Send CAN: BCM_FD_10.CmdIgnSts = 3 (ACC)
2. Press "Apps" on Menu Bar to open App Drawer
3. Read the App Drawer and check that "Rear View Camera" is not selectable
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 3 (ACC) is sent
2. The App Drawer is displayed
3. The "Rear View Camera" entry is shown in the unavailable state and cannot be selected
```
