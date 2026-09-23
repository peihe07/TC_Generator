# NR1L-RVCHMI-202 — SWE1-RVC-053

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.1.1`（來源列 `NRL-188029`）

## test_item 上半（verbatim，SYS1 逐字）

> When “Enhanced Camera App” Feature is present, wired and wireless Auxiliary cameras are non-persistent, latching views

## reasoning

**補生成之由**：拆解審計 **CAM-22 §5 #2**（`confidence = H`）—— §27.1.1 逐字為 `wired and wireless Auxiliary cameras`，而母列 `NR1L-RVCHMI-044` 之前提只佈**有線** AUX；本列佈**無線**側（§27.3.1.x 之硬體要求 ＋ `Enable Wireless Cameras` 設定）。latching／non-persistent 之可觀察定義同母列（H 本 §21.4／§21.5）。**既有 197 列不改**（DECISIONS 6-74）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. PENDING: DR-CAM-r the equipment flag for the "Enhanced Camera App" feature is not sourced
6. The "Enable Wireless Cameras" setting is On
7. A wireless AUX camera is connected
8. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
9. The shift lever is in P
10. The wireless AUX camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the wireless AUX camera view is still displayed
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
4. Read the HU display and check that the wireless AUX camera view is no longer displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The wireless AUX camera view remains displayed, which is the latching behaviour
3. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent
4. The wireless AUX camera view is no longer displayed, which is the non-persistent behaviour
```
