# NR1L-RVCHMI-150 — SWE1-RVC-121-02

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_31.1.2`（來源列 `NRL-188137`）

## test_item 上半（verbatim，SYS1 逐字）

> The camera name begins to overwrite the default name as soon as the user begins typing, or presses backspace.

## reasoning

§31.1.2 之第二個驗證點。來源以 `or` 並列**兩個**觸發（開始輸入／按 backspace），兩者皆驗 —— backspace 一支尤須驗，因其直覺上是刪除既有字而非覆寫。verbatim 為該列 Description 之保序子序列（刪首句與末句）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The camera name is the default name
4. The full QWERTY keyboard is shown for editing the camera name
```

## input_test_data

`NA`

## test_procedure

```
1. Type one character on the keyboard
2. Read the name field and check that the default name has been overwritten
3. Clear the field and reopen the name edit
4. Press backspace on the keyboard
5. Read the name field and check that the default name has been overwritten
```

## expected_result

```
1. The character is entered
2. The name field no longer shows the default name
3. The name edit is reopened with the default name
4. The backspace is registered
5. The name field no longer shows the default name
```
