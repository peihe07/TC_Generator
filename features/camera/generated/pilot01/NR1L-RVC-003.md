# NR1L-RVC-003 — SWE-CAM-015

- **Test Group**：Rear View Camera
- **Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P0｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS-RA-VF551_V2-498`

## test_item 上半（verbatim，SYS2 逐字）

> · When all of the following conditions hold true: - BCM_FD_10.CmdIgnSts = RUN, - ShiftLeverPosition = R > Reverse_Deb. the Head Unit shall display the RVC image as operating in Automatic Display Mode.

## reasoning

驗證目標為 Atl-Hi 車型在點火 RUN 且排檔進入 R 逾 Reverse_Deb 後，Head Unit 以 Automatic Display Mode 顯示 RVC 影像，即 SYS-RA-VF551_V2-498 之逐字條件。關鍵情境條件為 PROXI Rear_View_Camera = 1 (Present) 與 Rear_View_Camera_Type = 1 (Digital)（HDCC28_ATL_HI／DT28_ATL_HI 兩本 PROXI 之 Sheet1!I400 與 I931 實測值），觸發訊號 TRANSM_FD_4.ShiftLeverPosition 取自 PDT27_E2A_R1_FDCAN8.dbc（BO_ 1450），raw 與 label 逐字自該檔 VAL_ 列：1 "P"、2 "R"。本列依 R-CAM3 之車型軸拆為 Atl-Hi 半邊 —— 觸發訊號名因 EE 而異（Atl-Mi 側為 STATUS_CCAN4.ReverseGearSts，見 NR1L-RVC-004），故兩列各只勾自己的車型，括號下半以 EE ＋ 訊息名為區分 token。手動入口之啟動由 SWE-CAM-016 承接（NR1L-RVC-005），延遲退出由 SWE-CAM-018 承接（§8.2.1）。

## pre_conditions

```
1. PROXI Rear_View_Camera = 1 (Present)
2. PROXI Rear_View_Camera_Type = 1 (Digital)
3. The Head Unit is in the RUN power state
4. No camera image is shown
5. The last selected audio source is active
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)
2. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
4. Read the Head Unit display and check that the rear view camera image is shown in Automatic Display Mode
```

## expected_result

```
1. The Head Unit stays in the RUN power state
2. No camera image is shown and the previous content remains
3. The rear view camera image appears once the Reverse_Deb debounce has elapsed
4. The rear view camera image is shown in Automatic Display Mode
```
