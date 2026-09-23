# NR1L-RVCHMI-134 — SWE1-RVC-112-01

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_29.2.2`（來源列 `NRL-188124`）

## test_item 上半（verbatim，SYS1 逐字）

> From this pop-up the user can: -Enable wireless cameras

## reasoning

§29.2.2 列舉四項，四列各驗一項（`-134`～`-137`）。設定名之拼法依 **DECISIONS 6-61**（取彈窗表 `PU1517`／`PU1518` 之 `Enable Wireless Cameras`）。與 B02a `-063`（§27.4.1）之分工：後者自 **Aux Cameras 清單**操作該設定，本列自**個別相機之設定彈窗**操作；兩列之來源節與承接列皆不同（**R-CAM10**）。前提設「無投影」以避開 `PU1518`（該分支由 B02a `-064`～`-066` 承接）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. No wireless projection session is active
7. A wireless AUX camera is within range and powered on
8. The individual AUX Cam settings pop-up for the wireless camera is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the pop-up and check that "Enable Wireless Cameras" is offered
2. Set "Enable Wireless Cameras" = "On"
3. Read the pop-up and check that the setting reads On
```

## expected_result

```
1. "Enable Wireless Cameras" is shown in the pop-up
2. The "Enable Wireless Cameras" setting is On
3. The wireless camera entries are available
```
