# NR1L-RVC-087 — SWE-CAM-002

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V4_PHDCC27_VF_935`（來源列 `SYS-RA-VF551_V4-112`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall enable Analog Rear View Camera behavior when PROXI Rear_View_Camera = Present and Rear_View_Camera_Type = Analog

## reasoning

驗證目標為 `SYS-RA-VF551_V4-112` 之「PROXI `Rear_View_Camera = Present` **且** `Rear_View_Camera_Type = Analog` 時啟用 Analog Rear View Camera 行為」。**只勾 Atl-Hi** —— `Rear_View_Camera_Type`（byte 212 bit 6–7）只存在於 Atl-Hi 三本 PROXI（row 931），Atl-Mi 三本查無；比照 R-CAM13(c) 之 PROXI 配備判準，該參數不存在之平台勾 0。實測值：`DT28_ATL_HI` row 931 `1=Digital`、`HDCC27_initial` row 931 `0=Analogic`。與另一型別之列成一對（R-CAM3：PROXI 前提值因型別而異即拆列）。`-085` 驗「配備即啟用」、本列驗「型別決定何種行為」，兩者為不同驗證點（§8.2.1）。【CAM-09 §1 自查】**DT27 改勾 0** —— V4 本之 anchor 前綴只有 `PHDCC27`（R-CAM11），RULINGS 平台表亦只將 V4 對應 `HDCC27 Atl-Hi`；DT27 之 V 本為 `V2 (PDT27 anchor)`。CAM-08 落檔時誤勾 DT27，本輪更正。實測佐證：`DT28_ATL_HI` row 931 之 `Rear_View_Camera_Type = 1 (Digital)`，該平台本無類比相機之組態。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Rear_View_Camera_Type = 0 (Analogic)
4. The shift lever is in P
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)
2. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
3. Read the HU display and check that the rear view camera image is displayed
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
3. The rear view camera image is displayed
```
