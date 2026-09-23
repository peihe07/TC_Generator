# NR1L-RVC-223 — SWE-CAM-021

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1572`（來源列 `SYS-RA-VF551_V2-529`）

## test_item 上半（verbatim，SYS2 逐字）

> - When duration of the Rear Camera display is less than 5 seconds and Head Unit transitions to non camera display, the head unit shall remove the warning text overlay.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-529` 之「Rear Camera 顯示不足 5 秒而切回非相機畫面時，移除警示文字」。`SYS-RA-VF551_V4-118` 與本列**逐字同句**，依同義列不另出 TC，plan 記 covered_by。**與 `NR1L-RVC-055`（`V3-251` 之 `a)` 子句，376）之分工**：本列為 Atl-Hi 之獨立條文（V2 之 `-529` 為整句而非子句），兩者平台與本皆不同。Delay 設為 Off 使「5 秒內切回」可構造（同 `-055` 之處置）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The camera delay setting is set to "Off"
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P) less than 5 s after step 1
3. Read the HU display and check the warning text and the camera image
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the rear view camera image is displayed with the warning text overlaid
2. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent
3. The warning text overlay is removed together with the camera image
```
