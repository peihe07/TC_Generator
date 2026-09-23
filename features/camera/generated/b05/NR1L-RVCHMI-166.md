# NR1L-RVCHMI-166 — SWE1-RVC-153

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.9.6`（來源列 `NRL-188194`）

## test_item 上半（verbatim，SYS1 逐字）

> The pop-up updates to show a full QWERTY keyboard. The user uses this to edit the name of the camera. The camera name begins to overwrite the default name as soon as the user begins typing, or presses backspace.

## reasoning

§34.9.6（47 token）為 R1 Low 側之單一 leaf，**037 未拆子列**，故其三個驗證點（鍵盤、覆寫、backspace）合一列驗之 —— 與 R1 High 側 §31.1.2 之**三個子列**（`-149`～`-151`）相對。兩節之 Description 非逐字全等（49 vs 47 token）。本列不驗 `OK` 確認（§34.9.6 之末句 `The user presses OK to confirm the change` 於本節與 §31.1.2 同，惟其後果由 §34.9.7 之 `-167` 承接）。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. A wired AUX camera is connected
6. The camera name is the default name
7. "Edit Name" has been pressed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the pop-up and check that a full QWERTY keyboard is shown
2. Type one character on the keyboard
3. Read the name field and check that the default name has been overwritten
4. Clear the field, reopen the name edit and press backspace
5. Read the name field and check that the default name has been overwritten
```

## expected_result

```
1. A full QWERTY keyboard is shown in the pop-up
2. The character is entered
3. The name field no longer shows the default name
4. The backspace is registered
5. The name field no longer shows the default name
```
