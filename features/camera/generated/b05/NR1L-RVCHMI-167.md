# NR1L-RVCHMI-167 — SWE1-RVC-154

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.9.7`（來源列 `NRL-188195`）

## test_item 上半（verbatim，SYS1 逐字）

> After the name change has been confirmed, the settings menu is updated to read “NEW NAME” Settings (NEW NAME = whatever name the user adjusted to) as shown above

## reasoning

§34.9.7 與 §31.1.3（`NR1L-RVCHMI-152`）**非逐字全等**（CAM-19 證據 3 實測不同群 ——本列末為 `as shown above` 而 §31.1.3 為 `as shown above.` 加句點），故各自出 TC；其分工為 R1 Low ↔ R1 High。`“NEW NAME”` 為佔位符（括號內已逐字定義），ER 以「使用者所設之名」書寫，**不造具體名稱**（§8.4.1）。該列之唯一文字來源為其圖（不可抽），依 **DECISIONS 6-69**：ER 只判結構性可觀察項，**不造其文字、不掛 DR-CAM-h**。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. Two wired AUX cameras are connected
6. The AUX 1 camera name has just been changed and confirmed with OK
```

## input_test_data

`NA`

## test_procedure

```
1. Read the AUX Cam settings menu title and check that it reads the new name followed by Settings
2. Open the settings menu of the other AUX camera and read its title
```

## expected_result

```
1. The settings menu title reads the new name followed by "Settings"
2. The other camera's settings menu title still reads its own name followed by "Settings"
```
