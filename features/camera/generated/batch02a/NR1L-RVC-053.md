# NR1L-RVC-053 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_507`（來源列 `SYS-RA-VF551_V2-531`）

## test_item 上半（verbatim，SYS2 逐字）

> · When Head Unit transitions from non camera display to camera display, the Head Unit shall implement the warning text overlay that displays the text, "Check Entire Surroundings" for five seconds in the upper center of the display per the HMI definition.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-531` 之「自非相機畫面切入相機畫面時，於上方中央疊加 "Check Entire Surroundings" 五秒」。觸發取排檔入 R（自動模式之進入，來源見 `NR1L-RVC-003`），本列只驗疊加文字，不重複驗影像之顯示（§8.2.1 委派 `-003`）。`SYS-RA-VF551_V4-116` 與本列來源**逐字同句**且同平台（HDCC27），依同義列不另出 TC，plan 已記 covered_by。Atl-Mi 之同一行為：376 由 `-054`／`-055`、637 由 `-056`、2261 由 `-057` 承接（四本之條文逐字皆異）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the upper center of the HU display within 5 s and check the warning text
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the rear view camera image is displayed
2. The text "Check Entire Surroundings" is overlaid on the upper center of the display
```
