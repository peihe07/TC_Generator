# NR1L-RVCHMI-215 — SWE1-RVC-136

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.4.2`（來源列 `NRL-188170`）

## test_item 上半（verbatim，SYS1 逐字）

> Below screen is also accessed when shifting to REVERSE, but <X> is not present

## reasoning

**R-CAM19(c) 追溯補齊**（CAM-26 §2）：§34.4.2 與 §34.3.2（`SWE1-RVC-134`，**TC `NR1L-RVCHMI-086`**）逐字全等，父題亦全等（§34.4 與 §34.3 皆 `Accessing Aux Cameras – Backup Cam Only`，只 image token 不同；A-CA36／RDF-14）。下放包 §2 令「前提改 R1 Low（DECISIONS 6-64 散文前提），其餘沿母 TC」—— 惟本列與母列同在 §34（`R1 Low Wired AUX Cameras`，`NRL-188152`），母列 `-086` 之前提**已為** R1 Low，故前提、步驟與 ER 皆**沿母列**，兩列之差只在來源章節（`spec_reference` §34.4.2）。來源本身無可分辨兩節之文字（逐字全等、父題全等），本列不造差異（§8.4.1）；此一重複即 RDF-14 所報。Pre-Condition 九行（含 CAN source 行之位置）逐字沿母列。車型同母列（R-CAM18(a)）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Rear_View_Camera = 1 (Present)
6. A wired AUX camera is connected
7. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
8. The shift lever is in P
9. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the back-up camera view is displayed
3. Read the back-up camera view and check that no <X> control is present
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The back-up camera view is displayed
3. No <X> control is shown in the back-up camera view
```
