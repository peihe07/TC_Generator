# NR1L-RVCHMI-205 — SWE1-RVC-101

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.6.1.1`（來源列 `NRL-188106`）

## test_item 上半（verbatim，SYS1 逐字）

> When in reverse, the “More Cams” will allow users out of camera views when in Neutral or Drive,

## reasoning

**補生成之由**：拆解審計 **CAM-22 §5 #5**（`confidence = M`）—— §28.6.1.1 逐字為 `when in Neutral or Drive`，母列 `NR1L-RVCHMI-109` 只驗 **Neutral** 一側。本列驗 **Drive** 側。verbatim 為該列 Description 之保序子序列（刪 `and it will function as a quick select way …` 之後段，該段之 R 檔內切換由母列承接）。`Surround_View_Camera` 缺於 Toro → **R-CAM18(b)** `Toro(2261)` 判 `0`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Surround_View_Camera = 1 (Present)
3. Two wired AUX cameras are connected
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The shift lever is in R
6. The AUX 1 camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 4 (D)
2. Press the "More Cams" button and select the option that leaves the camera views
3. Read the HU display and check that no camera view is displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 4 (D) is sent
2. The option that leaves the camera views registers the selection
3. No camera view is displayed and the previous HU display is shown again
```
