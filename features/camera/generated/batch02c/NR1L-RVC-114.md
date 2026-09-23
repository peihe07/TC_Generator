# NR1L-RVC-114 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V4_PHDCC27_VF_1680`（來源列 `SYS-RA-VF551_V4-130`）

## test_item 上半（verbatim，SYS2 逐字）

> The Head unit shall implement Transition_time as performance variable with value less than 2 seconds.

## reasoning

驗證目標為 `SYS-RA-VF551_V4-130` 之「`Transition_time` 之效能值小於 2 秒」。`Transition_time` 於 V2 §1.13.2.1.8 載 `less than 1000 ms`、V4 載 `less than 2 seconds` ——**兩本之值不同**，故 `-102` 與 `-113` 分列而非同義列（R-CAM3 之 ER 可觀察結果相異）。V4 為類比相機之變體，故 Pre-Condition 以 `Rear_View_Camera_Type = 0 (Analogic)` 區別於 `-102`（V2，數位，< 1000 ms）。**兩列之 anchor 亦不同**（`VF551_V4_PHDCC27_VF_1680` vs `VF551_V2_PHDCC27_VF_1680` —— 兩本之 F 欄號碼相同而本不同，於此具名以免誤判為同錨）。**只勾 HDCC27** —— V4 本之 anchor 前綴只有 `PHDCC27`（R-CAM11），RULINGS 平台表亦只將 V4 對應 `HDCC27 Atl-Hi`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Rear_View_Camera_Type = 0 (Analogic)
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Measure the time between step 1 and the moment the rear view camera image is fully displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The measured time is less than 2 seconds
```
