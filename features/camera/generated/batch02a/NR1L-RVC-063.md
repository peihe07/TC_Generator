# NR1L-RVC-063 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_824`／`VF551_V33_P226MCA_VF_825`（來源列 `SYS-RA-VF551_V33-223`）

## test_item 上半（verbatim，SYS2 逐字）

> IF (LTM_OperationalModeSts.Info ==(equal)"Ignition_On" OR LTM_OperationalModeSts.Info ==(equal)"Ignition_Engine_On") AND Rear_Camera_Grid_Lines_Off.Req==(equal)"OFF") THEN

## reasoning

驗證目標為 `SYS-RA-VF551_V33-223` ＋ `-224` 之合一，形制與 `NR1L-RVC-062` 相同（R-CAM10(b)），本列承 OFF 側。兩列成 on／off 一對（§8.3 每點一 TC）。raw 0 取 `TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req` 之 `VAL_ 0 "Dynamic Gridlines OFF"`。

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
4. Select "Rear View Camera Active Guidelines" and set it to off
5. Read the bus analyzer recording and check TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" settings screen is displayed
4. The "Rear View Camera Active Guidelines" setting is off
5. TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req = 0 (Dynamic Gridlines OFF) is transmitted
```
