# NR1L-RVCHMI-161 — SWE1-RVC-150-02

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.9.2.2`（來源列 `NRL-188189`）

## test_item 上半（verbatim，SYS1 逐字）

> Reset Camera- Deletes the edited saved name of the camera, returning the name to “AUX Camera 1” or “AUX Camera 2”.(“AUX 1” and “AUX 2” on the soft controls)

## reasoning

§34.9.2.2 之括號句 —— **設定選單之線項**與**軟鍵**用兩套名稱：前者為 `AUX Camera 1`／`AUX Camera 2`（`-160` 所驗），後者為 `AUX 1`／`AUX 2`（本列）。兩者須分列，否則無從分辨該差異。**兩列之 verbatim 皆取全文**（29 token ≤ 50）——其 `2”.(“AUX` 為黏字（句點與括號黏於前字），摘句必留孤懸標點，依 **DECISIONS 6-65(b)** 取全文；各列所驗之項由下半括號句指明。§34 之章標題逐字為 `R1 Low Wired AUX Cameras`（`NRL-188152`）；HU 等級**無 PROXI 編碼**（六串六本各 0 命中，CAM-17 證據 5），依 **DECISIONS 6-64** 不以此判車型，前提以散文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. Two wired AUX cameras are connected
6. Both camera names have been edited to names other than the default
7. The individual AUX Cam settings pop-up is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select "Reset Camera" for each of the two cameras
2. Read the AUX camera soft controls and check their labels
```

## expected_result

```
1. "Reset Camera" registers the selection for both cameras
2. The soft controls read "AUX 1" and "AUX 2"
```
