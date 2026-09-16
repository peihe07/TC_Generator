# NR1L-RVC-003 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P0｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1378`（來源列 `SYS-RA-VF551_V2-498`）

## test_item 上半（verbatim，SYS2 逐字）

> · When all of the following conditions hold true: - BCM_FD_10.CmdIgnSts = RUN, - ShiftLeverPosition = R > Reverse_Deb. the Head Unit shall display the RVC image as operating in Automatic Display Mode.

## reasoning

驗證目標為 Atl-Hi 車型在 RVC 影像已顯示（手動模式）時排檔進入 R 逾 Reverse_Deb，畫面續顯並切入 Automatic Display Mode，即 SYS-RA-VF551_V2-488 之逐字條件。關鍵情境條件為 PROXI Rear_View_Camera = 1 (Present) 與 Rear_View_Camera_Type = 1 (Digital)（HDCC28_ATL_HI／DT28_ATL_HI 兩本 PROXI 之 Sheet1!I400 與 I931 實測值）。CmdIgnSts = RUN 為 Pre-Condition 之 Full-Operation 態所涵蓋，依 §4.4 不再入 Procedure（CAM-03 審閱 §二-1）。觸發訊號 TRANSM_FD_4.ShiftLeverPosition 取自 PDT27_E2A_R1_FDCAN8.dbc BO_ 1450，VAL_ 2 "R"。本列依 R-CAM3 之車型軸拆為 Atl-Hi 半邊 —— Atl-Mi 之同一驗證點其觸發訊號與條文皆異（NR1L-RVC-004，V3 §1.10.2.2 之 STATUS_CCAN4.ReverseGearSts），故兩列各只勾自己的車型。上半 29 RE_TOKEN，未逾 §4.3.1 之 50 上限，無須摘句。「影像已顯示 → 進 R → 續顯並切自動」為另一驗證點（V2-488／V3-266），列入全量之 -015 sibling 清單。手動入口之啟動由 SWE-CAM-016 承接，延遲退出由 SWE-CAM-018 承接（§8.2.1）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Rear_View_Camera_Type = 1 (Digital)
4. No camera image is displayed
5. The shift lever is in P
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the rear view camera image is displayed in Automatic Display Mode
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The rear view camera image is displayed in Automatic Display Mode after the Reverse_Deb debounce
```
