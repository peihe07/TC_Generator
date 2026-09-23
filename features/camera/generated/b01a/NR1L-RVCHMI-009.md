# NR1L-RVCHMI-009 — SWE1-RVC-050

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.5.3`（來源列 `NRL-187349`）

## test_item 上半（verbatim，SYS1 逐字）

> If the camera app is present, the Rear View Camera will not be accessible on the controls page

## reasoning

驗證目標為 §6.5.3 之否定條件。verbatim 為 Description 去除影像 token 後之保序子序列。互參 A 本 `SWE-CAM-016`（`crossref_a_b.tsv` 判 `precondition-or-hop`）—— 該列之 hop 選擇受本條約束。H 本 §27.7.2（`If the camera app is present, the soft controls will not be on the controls page`）與 §15.6.2 為同型條文，佐證其為通則而非 RVC 專屬。否定句式用 `check that no …`（**不用 `check whether`**，CAM-11 審閱所禁）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
4. The shift lever is in P
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. PENDING: DR-CAM-g open the Controls screen
2. Read the Controls screen and check that no Rear View Camera soft control is offered
```

## expected_result

```
1. PENDING: DR-CAM-g the Controls screen is displayed
2. No Rear View Camera soft control is present on the Controls screen
```
