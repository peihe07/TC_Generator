# NR1L-RVC-085 — SWE-CAM-002

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_935`（來源列 `SYS-RA-VF551_V2-536`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall enable Digital Rear View Camera behavior when PROXI Rear_View_Camera = Present.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-536` 之「PROXI `Rear_View_Camera = Present` 時啟用 Digital Rear View Camera 行為」。`SYS-RA-VF551_V3-212`（逐字同句）與 `SYS-RA-VF551_V42-209`（同一前提之宣告式）依同義列不另出 TC，plan 記 covered_by；**本列因而承全五車型** —— 該 PROXI 參數六本皆有（byte 86 bit 0）。**不生成 Absent 側**（DECISIONS 6-18／RDF-06）—— `-002` 之 20 個 in-scope 來源逐字掃描，`Absent`／`= 0`／`not present` 三串零命中，無 negative 之需求可依。「已啟用」之可判後果取 App Drawer 之項目可選（沿 `NR1L-RVC-025` 之既定寫法）。R-CAM3(f)：本列無 `Send CAN` 步，不寫 CAN source 行。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
```

## input_test_data

`NA`

## test_procedure

```
1. Cycle the ignition to RUN so that the HU reads the PROXI configuration
2. Press "Apps" on Menu Bar to open App Drawer
3. Read the App Drawer and check that "Rear View Camera" is present and selectable
```

## expected_result

```
1. The HU completes start-up and reads the PROXI configuration
2. The App Drawer is displayed
3. The "Rear View Camera" entry is present in the App Drawer and can be selected
```
