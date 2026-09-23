# NR1L-RVC-049 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_505`（來源列 `SYS-RA-VF551_V2-528`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall implement the warning text overlay that displays the text, "Camera Not in Position" for five seconds in the upper center part of the display of the event followed by ''check entire surroundings'' per the HMI definition when BCM_FD_9.RHatchSts = Open.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-528` 之「`BCM_FD_9.RHatchSts = Open` 時於畫面上方中央疊加 "Camera Not in Position" 五秒，其後接 ''check entire surroundings''」。訊號實測：`RHatchSts` 於 `forms/PDT27_E2A_R1_FDCAN8.dbc` `BO_ 1066 BCM_FD_9`，`VAL_ 0 "Closed" 1 "Open"`，可注入。Atl-Mi 之同一行為由 `NR1L-RVC-050`（V3，637／376）與 `-051`（V33，2261）承接 —— 三本之訊息名相異（`BCM_FD_9`／`STATUS_BH_BCM1`／`STATUS_BH_BCM`）**且條文逐字相異**（V3 多 ISO 字型句、V33 以 `T_INITDISPLAY` 表時長），故依 R-CAM3 拆列而非 R-CAM3(e) 折行。畫面文字之權威性另見 A-CA20／DR-CAM-h（`Camera Not in position` 於 Pop Up List 查無）；本列依 §8.4.1 以來源原文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera image is displayed
4. BCM_FD_9.RHatchSts = 0 (Closed)
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_9.RHatchSts = 1 (Open)
2. Read the upper center part of the HU display within 5 s and check the warning text
3. Read the upper center part of the HU display after the first text is removed and check the following text
```

## expected_result

```
1. BCM_FD_9.RHatchSts = 1 (Open) is sent
2. The text "Camera Not in Position" is overlaid on the upper center part of the display
3. The text "check entire surroundings" is overlaid after the first text
```
