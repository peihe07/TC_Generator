# NR1L-RVCHMI-003 — SWE1-RVC-043

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.1.5`（來源列 `NRL-187336`）

## test_item 上半（verbatim，SYS1 逐字）

> Rear view camera is a non-persistent camera view When equipped with “Enhanced Camera App” feature

## reasoning

驗證目標為 §6.1.5 之「non-persistent」。非持續之可觀察定義取 **H 本 §21.4**（`“Enhanced Camera App Feature” Non-persistent views with Timer`）與 §21.5 之對照（latching 為持續）—— 即觸發條件消失後該 view 自行退出。「Enhanced Camera App」之配備旗標於 `forms/proxi/` 六本零命中（掃描字串 `Enhanced_Camera`，命令 `proxi_have.py`，六本各 0）→ **DR-CAM-r**，依 **profile §7.5** 掛於前提之項首。gear 訊號沿 A 本 `NR1L-RVC-018` 之寫法（**R-CAM1(b)**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-r the equipment flag for the "Enhanced Camera App" feature is not sourced
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
3. Read the HU display and check that the rear view camera image is no longer displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the rear view camera image is displayed
2. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent
3. The rear view camera image is no longer displayed and the previous display is shown again
```
