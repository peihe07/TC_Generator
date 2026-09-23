# NR1L-RVC-106 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_509`（來源列 `SYS-RA-VF551_V2-534`）

## test_item 上半（verbatim，SYS2 逐字）

> · The soft key button control for the RVC shall be in the available state only when BCM_FD_10.CmdIgnSts = RUN.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-534` 之「RVC 軟鍵僅於 `BCM_FD_10.CmdIgnSts = RUN` 時為可用態」。**本列為 `SWE-CAM-003` 之承接列** —— 該來源為 `-003` 所引，`NR1L-RVC-023`（`SWE-CAM-016`）當時即因 R-CAM10 而改錨 `CFTS092-4781638`（CAM-05 §5-1 之自報）。本列取**不成立側**（離開 RUN）以與 `-023`（成立側，CFTS092 錨）分工；供試值 `3 (ACC)` 取 `VAL_ … 3 "ACC"`（FDCAN8 `BO_ 1153`），寫法沿 `NR1L-RVC-024`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 3 (ACC)
2. Press "Apps" on Menu Bar to open App Drawer
3. Read the App Drawer and check the state of the "Rear View Camera" entry
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 3 (ACC) is sent
2. The App Drawer is displayed
3. The "Rear View Camera" entry is not in the available state
```
