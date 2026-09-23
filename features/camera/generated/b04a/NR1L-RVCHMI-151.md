# NR1L-RVCHMI-151 — SWE1-RVC-121-03

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_31.1.2`（來源列 `NRL-188137`）

## test_item 上半（verbatim，SYS1 逐字）

> The user presses OK to confirm the change.

## reasoning

§31.1.2 之第三個驗證點。`in effect` 之各處反映由 §31.1.3～§31.1.5（`-152`～`-154`）承接，本列只驗**確認動作本身**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The full QWERTY keyboard is shown for editing the camera name
4. A new name has been typed
```

## input_test_data

`NA`

## test_procedure

```
1. Press OK
2. Read the HU display and check that the pop-up has closed and the new name is in effect
```

## expected_result

```
1. OK registers the press
2. The name edit pop-up closes and the new name is in effect
```
