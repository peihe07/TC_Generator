# NR1L-RVCHMI-027 — SWE1-RVC-018

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.3.3`（來源列 `NRL-142624`）

## test_item 上半（verbatim，SYS1 逐字）

> For 10.1 Portrait head units RVC only will also provide all the available vehicle controls

## reasoning

§7.3.3 只存在於 cache 本（A-CA14／**R-CAM6**）。10.1 Portrait 之 raw 取 `Radio_Display_Type = 4`（`4 = 10.1" 1200x1920`，寬 < 高即 Portrait；`3 = 10.1" 1920x1200` 為橫向，不取）。條文末之 `as described on the HMI Logic & Flow Core specification (for SR21)` 為**外部規格**，其控制項之列舉不在本 feature 之 037 所引範圍，依 canon **§8.4.2**（R-CAM13(b)）不測其內容；本列只驗該區之**存在與可操作**。`Radio_Display_Type` 缺於 Toro → `Toro(2261)` 判 `0`（**R-CAM18(b)**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 0 (Absent)
4. PROXI Radio_Display_Type = 4 (10.1" 1200x1920)
5. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
6. The shift lever is in P
7. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the RVC-only layout and check that the vehicle controls area is present
3. Select a vehicle control in the RVC-only layout
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the RVC-only layout is displayed
2. The vehicle controls area is shown in the RVC-only layout
3. The selected vehicle control registers the selection
```
