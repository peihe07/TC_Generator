# NR1L-RVCHMI-054 — SWE1-RVC-063

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.2.4.1`（來源列 `NRL-188045`）

## test_item 上半（verbatim，SYS1 逐字）

> Personalization settings to be grouped within the “Cameras” line

## reasoning

§27.2.4.1 之 `“Cameras” line` 為逐字。實測 `forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` `Settings` 分頁：該群組之標題為 row 464 之 **`13. Camera`**（單數），其下 row 474／475 為 `Aux Cameras`；SYS1 寫 `“Cameras”`（複數）而設定表寫 `Camera`，差異記於 `remarks`（profile §10 第二類）。ER 依設定表之實際標籤書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Read the "Camera" list and check that the AUX camera personalization entries are grouped there
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. The AUX camera personalization entries are listed under the "Camera" line and not elsewhere
```

## remarks

SYS1 27.2.4.1 names the group "Cameras"; the HMI Settings List heading is "13. Camera" (singular). ER follows the Settings List.
