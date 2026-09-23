# NR1L-RVC-062 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_822`／`VF551_V33_P226MCA_VF_823`（來源列 `SYS-RA-VF551_V33-221`）

## test_item 上半（verbatim，SYS2 逐字）

> IF (LTM_OperationalModeSts.Info ==(equal)"Ignition_On" OR LTM_OperationalModeSts.Info ==(equal)"Ignition_Engine_On") AND Rear_Camera_Grid_Lines_Off.Req==(equal)"ON" ) THEN

## reasoning

驗證目標為 `SYS-RA-VF551_V33-221`（條件側：Ignition_On／Ignition_Engine_On 且 `Rear_Camera_Grid_Lines_Off.Req = "ON"`）與 `SYS-RA-VF551_V33-222`（動作側：LTM 設 `TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req="Dynamic Gridlines ON"`）之合一。**依 R-CAM10(b)**（CAM-06 審閱 §二-4）：兩來源描述同一行為之 IF 與 THEN，承接列分屬 `SWE-CAM-001`（`-221`）與 `SWE-CAM-003`（`-222`），合為一個 TC 並以兩行 `specification_reference` 承載；TC 歸 SWE ID 較小之 `SWE-CAM-001`，`SWE-CAM-003` 於 plan 記委派。test_item 上半取條件側之逐字（`-221`，10 token）——動作側之逐字已於 ER 第 5 項以訊號與值完整表達。訊號實測：`TELEMATIC_VEHICLE_SETUP`（`BO_ 158`，四本 DBC 皆有）之 `VAL_ 0 "Dynamic Gridlines OFF" 1 "Dynamic Gridlines ON"`，raw 可逐字書寫。**設定 label 之品牌軸**：`HMI Settings List` `Settings` row 468 之基礎 label 為 `Rear View Camera Active Guidelines*`，`*` 不入 hop（R-CAM5(a)）；2261 於 `Brand-Specific Names` 之 Fiat 欄為空，回落基礎 label（R-CAM5(c)′），Pre-Condition 依 R-CAM5(e) 書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)
4. The vehicle brand is not Ram (2261 Fiat, 376 Abarth)
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Select "Rear View Camera Active Guidelines" and set it to on
5. Read the bus analyzer recording and check TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" settings screen is displayed
4. The "Rear View Camera Active Guidelines" setting is on
5. TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req = 1 (Dynamic Gridlines ON) is transmitted
```
