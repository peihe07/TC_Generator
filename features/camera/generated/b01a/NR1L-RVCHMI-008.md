# NR1L-RVCHMI-008 — SWE1-RVC-049

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.5.2`（來源列 `NRL-187348`）

## test_item 上半（verbatim，SYS1 逐字）

> When not equipped with Vehicle Surround View and equipped with any of the following; FFCTL, the Rear View will be accessible Via a soft control in the corner of the view

## reasoning

驗證目標為 §6.5.2 之配備組合（無 Surround View ＋ 有 TRG／CHMSL／FFCTL 任一）。verbatim 為保序子序列（三款配備只留 `FFCTL` 一款）—— 取 FFCTL 之由為 **PROXI 實測**：`Auxiliary_Trailer_Camera`（TRG）與 `Digital_CHMSL_Camera_Prsnt`（CHMSL）於三本 Atl-Mi 本皆零命中，只有 `Forward_Facing_Camera` 六本中五本有（Toro 缺 byte 177，**DR-CAM-l**），故 `Toro(2261)` 判 0（**R-CAM3** 車型軸）。TRG／CHMSL 兩支俟 DR-CAM-l 結後於 B 本後續批補列。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Surround_View_Camera = 0 (Absent)
3. PROXI Forward_Facing_Camera = 1 (Present)
4. The Forward Facing Camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the corner of the Forward Facing Camera view and check that the Rear View soft control is present
2. Select the Rear View soft control in the corner of the view
3. Read the HU display and check that the rear view camera image is displayed
```

## expected_result

```
1. The Rear View soft control is shown in the corner of the Forward Facing Camera view
2. The Rear View soft control registers the selection
3. The rear view camera image is displayed
```
