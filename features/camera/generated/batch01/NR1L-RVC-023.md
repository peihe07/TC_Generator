# NR1L-RVC-023 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`CFTS092-4781638`（來源列 `SYS-RA-CAM-073`）

## test_item 上半（verbatim，SYS2 逐字）

> The Rear View Camera soft button shall be selectable only when the signal $PowerMode$ = [IGN_RUN].

## reasoning

驗證目標為 CFTS092 SYS-RA-CAM-073（ObjectID 4781638，Rear Camera 節）之「軟鍵僅於 $PowerMode$ = [IGN_RUN] 時可選取」之成立側。$PowerMode$ 為設定／參數標記（§8.7.5(f)），其 CAN 對應依 VF551_V2-534 為 BCM_FD_10.CmdIgnSts，故以 4 (RUN) 表達。**錨不取 VF551_V2-534** —— 該來源同為 SWE-CAM-003 所引，依 R-CAM10 委派 SWE-CAM-003。入口 hop 取 §5.3 已鎖定之 ENTER_APP_DRAWER 與 Menu Bar §4.1 naming table 之 "Rear View Camera"（NRL-127734）。不成立側（PowerMode != IGN_RUN）由 NR1L-RVC-024 承接。訊息名依 R-CAM3(e) 分寫於 CAN source 行。【CAM-06 §2-1】步 1 之 `Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)` 已刪 —— Pre-Condition 1 之 Full-Operation 其定義已含 IGN RUN，重送為重複（審閱 §二-1，§4.4）；ER 隨之重編為兩項。Pre-Condition 3 之 CAN source 行保留，其用途改為 $PowerMode$ 之 EE 對照（R-CAM3(e) 之訊息名分寫），不再對應任何 Send CAN 步。

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
2. Read the App Drawer and check that "Rear View Camera" is selectable
```

## expected_result

```
1. The App Drawer is displayed
2. The "Rear View Camera" entry is shown in the available state and can be selected
```
