# NR1L-RVCHMI-101 — SWE1-RVC-094

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.2.2`（來源列 `NRL-188093`）

## test_item 上半（verbatim，SYS1 逐字）

> Accessing aux camera does not reset“Check Entire Surroundings” timer.

## reasoning

§28.2.2 之驗證點為**計時器不重置**：於原視角已跑 3 秒後切換，若不重置則再 2 秒（合計 5 秒）即消失；若重置則 5 秒後才消失。故觀察點取切換後 2 秒。5 秒之值取同節 §28.2.1（`-100`）之來源逐字。否定句式用 `does not`／`no longer`，不用 `check whether`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. A wired AUX camera is connected
4. The rear view camera image is displayed
5. The "Check Entire Surroundings" message has been shown for 3 seconds
```

## input_test_data

`NA`

## test_procedure

```
1. Select the AUX camera soft control within the view
2. Read the HU display 2 seconds after the selection and check that the message is no longer shown
```

## expected_result

```
1. The AUX camera view is displayed
2. The "Check Entire Surroundings" message is no longer shown, which shows that the timer continued from the earlier view and was not restarted
```
