# NR1L-RVCHMI-044 — SWE1-RVC-053

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.1.1`（來源列 `NRL-188029`）

## test_item 上半（verbatim，SYS1 逐字）

> When “Enhanced Camera App” Feature is present, wired and wireless Auxiliary cameras are non-persistent, latching views

## reasoning

`latching` 與 `non-persistent` 之可觀察定義取 H 本 **§21.4**（`Non-persistent views with Timer`）與 **§21.5**（`Latching Views`）之對照：latching ＝ 觸發條件改變時仍保持該視角、non-persistent ＝ 觸發條件消失後自行退出。故以 P → R（latching 不被 reverse 搶走）→ P（non-persistent 退出）之往返驗之。「Enhanced Camera App」配備旗標六本 PROXI 零命中 → **DR-CAM-r**（CAM-14 已開）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PENDING: DR-CAM-r the equipment flag for the "Enhanced Camera App" feature is not sourced
3. A wired AUX camera is connected
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The shift lever is in P
6. The AUX 1 camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the AUX 1 camera view is still displayed
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
4. Read the HU display and check that the AUX 1 camera view is no longer displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The AUX 1 camera view remains displayed, which is the latching behaviour
3. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent
4. The AUX 1 camera view is no longer displayed, which is the non-persistent behaviour
```
