# NR1L-RVC-098 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1578`（來源列 `SYS-RA-VF551_V2-491`）

## test_item 上半（verbatim，SYS2 逐字）

> · When any of the preceding conditions occur, the Head Unit shall switch back to non-camera display operation.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-491` 之「任一前述退出條件成立時，HU 切回非相機顯示」。**本列為退出條件之共同後果**（切回非相機），各退出條件之觸發面已由 batch01 之 `NR1L-RVC-017`（點火離開 RUN）／`-018`（排檔入 P）／`-013`／`-014`（Delay Off）承接 —— 依 §8.2.1 本列不重複驗觸發，只驗其共同結果，故取最單純之一個觸發（排檔入 P）為載體。Delay 設為 Off 使「立即切回」可判（審閱 CAM-05 §二-2 之同型）。**錨不取 `SYS-RA-VF551_V2-496`** —— 該退出清單同為 `SWE-CAM-015` 所引，依 R-CAM10 委派。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The camera delay setting is set to "Off"
4. The rear view camera image is displayed in Automatic Display Mode
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
1. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent
2. The rear view camera image is closed and the HU shows the previous non-camera screen
```
