# NR1L-RVC-105 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_520`（來源列 `SYS-RA-VF551_V2-524`）

## test_item 上半（verbatim，SYS2 逐字）

> · HU display shall not go blank in each of the following scenarios: 1. Head Unit displays the RVC image 2. Head Unit display transitions between RVC image and non camera modes.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-524` 之「HU 畫面於其所列兩情境中不得變黑」。來源明列兩情境（1. 顯示 RVC 影像時、2. RVC 與非相機模式之切換間），故 procedure 兩情境各一觀察步、ER 各一項（§5.7 同一驗證目標之多行 ER）。**兩情境不拆列** —— 其為同一負向性質（不得閃爍／不得變黑）之兩個取樣時機，非兩個驗證點（§8.3 無新軸）。`-104` 與 `-105` 則因性質不同而分列。

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
2. Read the HU display while the rear view camera image is shown and check for blank
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
4. Read the HU display during the transition back to the non-camera display and check for blank
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the rear view camera image is displayed
2. The HU display does not go blank while the RVC image is displayed
3. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent and the rear view camera image is closed
4. The HU display does not go blank during the transition between RVC and non camera modes
```
