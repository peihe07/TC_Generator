# NR1L-RVCHMI-152 — SWE1-RVC-122

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_31.1.3`（來源列 `NRL-188138`）

## test_item 上半（verbatim，SYS1 逐字）

> After the name change has been confirmed, the settings menu is updated to read “NEW NAME” Settings (NEW NAME = whatever name the user adjusted to) as shown above.

## reasoning

§31.1.3 逐字。`“NEW NAME”` 為佔位符（其括號內已逐字定義 `NEW NAME = whatever name the user adjusted to`），故 ER 以「使用者所設之名」書寫，**不造具體名稱**（§8.4.1）。`as shown above` 指該列之圖（`image165.png`），內容不可抽，不引。第二步之對照（另一台之標題不變）驗 `NEW NAME = whatever name the user adjusted to` 之**單台限定**。與 §34.9.7（B04b）之關係：兩列之 Description **非逐字全等**（本列 31 token，§34.9.7 亦 31 token 而分群結果相異，見上繳 §3 證據 3），故非 R-CAM16(c) 之委派款。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. Two wired AUX cameras are connected
4. The AUX 1 camera name has just been changed and confirmed with OK
```

## input_test_data

`NA`

## test_procedure

```
1. Read the AUX Cam settings menu title and check that it reads the new name followed by Settings
2. Open the settings menu of another AUX camera and read its title
```

## expected_result

```
1. The settings menu title reads the new name followed by "Settings"
2. The other camera's settings menu title still reads its own name followed by "Settings"
```
