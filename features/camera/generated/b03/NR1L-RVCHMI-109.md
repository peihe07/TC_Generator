# NR1L-RVCHMI-109 — SWE1-RVC-101

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.6.1.1`（來源列 `NRL-188106`）

## test_item 上半（verbatim，SYS1 逐字）

> When in reverse, the “More Cams” will allow users out of camera views when in Neutral or Drive, and it will function as a quick select way for users to swap to a different camera view not available within the view while remaining in reverse

## reasoning

§28.6.1 之父題逐字為 `Top + Rear Automatic camera manual activation, shifted to Reverse, “R”`（`NRL-188105`），其父 §28.6 為 `UI – In Reverse with “Surround View and Camera App”`，故前提取 `Surround_View_Camera = 1`。條文含**兩個**行為：(a) R 檔中以 `More Cams` 切換視角（不退出相機）；(b) 於 N／D 檔時 `More Cams` 可**離開**相機視角。兩者同屬一句之 `and`，可觀察結果相依（同一個按鍵、依檔位而異），故合一列以決策表驗之。`Surround_View_Camera` 缺於 Toro → **R-CAM18(b)** `Toro(2261)` 判 `0`。

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
1. Press the "More Cams" button and select the AUX 2 view
2. Read the HU display and check that the AUX 2 view is displayed and that the gear is still R
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 3 (N)
4. Press the "More Cams" button and select the option that leaves the camera views
5. Read the HU display and check that no camera view is displayed
```

## expected_result

```
1. The AUX 2 view is selected from the pop-up
2. The AUX 2 view is displayed while the gear is still R, which is the swap within reverse
3. TRANSM_FD_4.ShiftLeverPosition = 3 (N) is sent
4. The option that leaves the camera views registers the selection
5. No camera view is displayed and the previous HU display is shown again
```
