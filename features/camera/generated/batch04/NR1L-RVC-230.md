# NR1L-RVC-230 — SWE-CAM-022

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V4_PHDCC27_VF_1578`（來源列 `SYS-RA-VF551_V4-152`）

## test_item 上半（verbatim，SYS2 逐字）

> · When any of the preceding conditions occur, the Head Unit shall switch back to non-camera display operation.

## reasoning

驗證目標為 `SYS-RA-VF551_V4-152`。與 `NR1L-RVC-098`（`V2-491`，數位側，`SWE-CAM-003`）逐字同句而本與承接列皆不同。V4 為 HDCC27 之**類比相機變體**，Pre-Condition 以 `PROXI Rear_View_Camera_Type = 0 (Analogic)` 與 V2 之數位側區別（`HDCC27_initial` row 931 實測 `0=Analogic`）。**只勾 HDCC27** —— V4 本之 anchor 前綴只有 `PHDCC27`（R-CAM11）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Rear_View_Camera_Type = 0 (Analogic)
4. The camera delay setting is set to "Off"
5. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
2. Read the HU display and check that the HU is in non-camera display operation
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent and the rear camera image is closed
2. The rear view camera image is closed and the HU shows the previous non-camera screen
```
