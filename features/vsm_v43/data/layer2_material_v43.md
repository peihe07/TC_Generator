# Layer 2 暫代材料 — vsm_v43（下放包 06 W-2，R-VT18(e)）

**執行層產出材料，不聚類、不命名**（06 包 §四：任何聚類命名出現於執行層產出即升級）。
來源：`data/leaves_interim.tsv`（暫代母體 295 列）。

> **標題欄實測**：SYSRA `Basic Report` **無專用之需求標題欄**。
> `SYS2 Melco ID`（C）於 507 列全空（A-VT9）；`Description`（D）為需求全文（中位 191 字元、最長 438）。
> 本材料之「標題例」即取 `Description` 逐字（`_x000D_` 為 Excel 之 CR 編碼形，已正規化為空白）。
> `子分類`（V）／`功能一～三階`（W／X／Y）各僅 2 個相異值（294 : 1），**無分組鑑別力**。
> 有分組鑑別力者僅 `chapter_for_vf`（K）。

## 一、`chapter_for_vf` 完整值分組

| # | chapter_for_vf | 列數 | 前二階 | 含 v5 訊號名之列 | 含「解得」訊號之列 |
|---|---|---|---|---|---|
| 1 | `01.14.01` | 38 | `01.14` | 29 | 0 |
| 2 | `01.11.01.01.06` | 15 | `01.11` | 15 | 12 |
| 3 | `01.11.01.01.24` | 15 | `01.11` | 11 | 11 |
| 4 | `01.11.01.01.08.03` | 11 | `01.11` | 10 | 0 |
| 5 | `01.11.01.01.05` | 10 | `01.11` | 10 | 8 |
| 6 | `01.11.01.01.26` | 10 | `01.11` | 9 | 8 |
| 7 | `01.11.01.01.03` | 9 | `01.11` | 9 | 7 |
| 8 | `01.11.01.01.04` | 9 | `01.11` | 9 | 7 |
| 9 | `01.11.01.01.10.02` | 9 | `01.11` | 8 | 5 |
| 10 | `01.11.01.01.10.04` | 6 | `01.11` | 6 | 4 |
| 11 | `01.11.01.01.13` | 6 | `01.11` | 6 | 4 |
| 12 | `01.11.01.01.14` | 6 | `01.11` | 5 | 5 |
| 13 | `01.11.01.01.15` | 6 | `01.11` | 4 | 0 |
| 14 | `01.11.01.01.01` | 5 | `01.11` | 5 | 2 |
| 15 | `01.11.01.01.02` | 5 | `01.11` | 5 | 3 |
| 16 | `01.11.01.01.07` | 5 | `01.11` | 5 | 0 |
| 17 | `01.11.01.01.08.01` | 5 | `01.11` | 4 | 0 |
| 18 | `01.11.01.01.09` | 5 | `01.11` | 5 | 3 |
| 19 | `01.11.01.01.10.01` | 5 | `01.11` | 5 | 3 |
| 20 | `01.11.01.01.10.03` | 5 | `01.11` | 5 | 3 |
| 21 | `01.11.01.01.12` | 5 | `01.11` | 5 | 3 |
| 22 | `01.11.01.01.16` | 5 | `01.11` | 5 | 3 |
| 23 | `01.11.01.01.17` | 5 | `01.11` | 5 | 1 |
| 24 | `01.11.01.01.18` | 5 | `01.11` | 5 | 3 |
| 25 | `01.11.01.01.19` | 5 | `01.11` | 5 | 3 |
| 26 | `01.11.01.01.20` | 5 | `01.11` | 5 | 3 |
| 27 | `01.11.01.01.25` | 5 | `01.11` | 5 | 3 |
| 28 | `01.11.01.01.27` | 5 | `01.11` | 5 | 3 |
| 29 | `01.11.01.01.08.02` | 4 | `01.11` | 3 | 3 |
| 30 | `01.11.01.01.11` | 4 | `01.11` | 3 | 2 |
| 31 | `01.11.01.01.21` | 4 | `01.11` | 4 | 0 |
| 32 | `01.11.01.01.31` | 4 | `01.11` | 4 | 4 |
| 33 | `01.11.01.01.32` | 4 | `01.11` | 4 | 0 |
| 34 | `01.11.01.01.28` | 3 | `01.11` | 2 | 2 |
| 35 | `01.11.01.01.29` | 3 | `01.11` | 2 | 2 |
| 36 | `01.11.01.01.30` | 3 | `01.11` | 2 | 2 |
| 37 | `01.13.02.01.03` | 3 | `01.13` | 2 | 0 |
| 38 | `01.11.01.01` | 2 | `01.11` | 1 | 0 |
| 39 | `01.11.01.01.22` | 2 | `01.11` | 2 | 2 |
| 40 | `01.11.01.01.23` | 2 | `01.11` | 2 | 2 |
| 41 | `01.11.01.01.10` | 1 | `01.11` | 0 | 0 |
| 42 | `01.13.02.01.01` | 1 | `01.13` | 0 | 0 |
| 43 | `01.13.02.01.02` | 1 | `01.13` | 1 | 0 |
| 44 | `01.14.02.01.01` | 1 | `01.14` | 1 | 0 |
| 45 | `01.14.02.01.02` | 1 | `01.14` | 1 | 0 |
| 46 | `01.14.02.01.03` | 1 | `01.14` | 1 | 0 |
| 47 | `01.14.02.01.04` | 1 | `01.14` | 1 | 0 |
| 48 | `01.14.02.01.05` | 1 | `01.14` | 1 | 0 |
| 49 | `01.14.02.01.06` | 1 | `01.14` | 1 | 0 |
| 50 | `01.14.02.01.07` | 1 | `01.14` | 1 | 0 |
| 51 | `01.14.02.01.08` | 1 | `01.14` | 1 | 0 |
| 52 | `01.14.02.01.09` | 1 | `01.14` | 1 | 0 |
| 53 | `01.14.02.01.10` | 1 | `01.14` | 1 | 0 |
| 54 | `01.14.02.01.11` | 1 | `01.14` | 1 | 0 |
| 55 | `01.14.02.01.12` | 1 | `01.14` | 0 | 0 |
| 56 | `01.14.02.01.13` | 1 | `01.14` | 0 | 0 |
| 57 | `01.14.02.01.14` | 1 | `01.14` | 1 | 0 |
| 58 | `01.14.02.01.15` | 1 | `01.14` | 1 | 0 |
| 59 | `01.14.02.01.16` | 1 | `01.14` | 1 | 0 |
| 60 | `01.14.02.01.17` | 1 | `01.14` | 1 | 0 |
| 61 | `01.14.02.01.18` | 1 | `01.14` | 1 | 0 |
| 62 | `01.14.02.01.19` | 1 | `01.14` | 1 | 0 |
| 63 | `01.14.02.01.20` | 1 | `01.14` | 0 | 0 |
| 64 | `01.14.02.01.21` | 1 | `01.14` | 1 | 0 |
| 65 | `01.14.02.01.22` | 1 | `01.14` | 1 | 0 |
| 66 | `01.14.02.01.23` | 1 | `01.14` | 1 | 0 |
| 67 | `01.14.02.01.24` | 1 | `01.14` | 1 | 0 |
| 68 | `01.14.02.01.25` | 1 | `01.14` | 1 | 0 |
| 69 | `01.14.02.01.26` | 1 | `01.14` | 1 | 0 |
| 70 | `01.14.02.01.27` | 1 | `01.14` | 1 | 0 |
| 71 | `01.14.02.01.28` | 1 | `01.14` | 1 | 0 |
| 72 | `01.14.02.01.29` | 1 | `01.14` | 1 | 0 |

組數 **72**；列數合計 **295**。

## 二、每組 3 個標題例（首／中／末列，逐字取 `Description`）

### 1. `01.14.01`（38 列）
- **首** `r813` `Sys-RA-VF665_V43_VSM-812`：1 Cornering_Light ** ** ** ** LTM PROXI No N.A. Range value is indicated in the standard PROXI. First Trial Value depends on the project Configuration
- **中** `r832` `Sys-RA-VF665_V43_VSM-831`：23 Tyre_Pressure_Unit_Menu ** ** ** ** LTM PROXI No N.A. Range value is indicated in the standard PROXI. First Trial Value depends on the project Configuration
- **末** `r1212` `Sys-RA-VF665_V43_VSM-1211`：37 V_Car_Moving 4 [0;7] 0,5 km/h LTM DEFINE No N.A. Speed threshold for car moving

### 2. `01.11.01.01.06`（15 列）
- **首** `r454` `Sys-RA-VF665_V43_VSM-453`：IF "Forward_Collision_Mitigation" PROXI parameter is equal to "Full Speed Forward Collision Warning with Mitigation" THEN TLM shall display the "Forward Collision Warinig Setting" and "Forward Collision Warning Sensitivity" menu item and the user can perform setting.
- **中** `r462` `Sys-RA-VF665_V43_VSM-461`：IF the user sets "FSCWPlus_Setting.Req" internal signals to "Off " THEN TLM shall set "TELEMATIC_VEHICLE_SETUP2.FSFCWPlusSetting_Req" B-CAN signal equal to "Off " and sends this signal to IPC
- **末** `r470` `Sys-RA-VF665_V43_VSM-469`：WHEN TLM receives "IPC_VEHICLE_SETUP2.FSFCWPlusActivationMode " message THEN TLM updates the Forward Collision Warning information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 3. `01.11.01.01.24`（15 列）
- **首** `r626` `Sys-RA-VF665_V43_VSM-625`：IF " CAN node 24 (PAM ) " PROXI parameter is equal to "Present" THEN TLM shall display the "Park Sense Setting " menu item and the user can perform setting.
- **中** `r635` `Sys-RA-VF665_V43_VSM-634`：WHEN TLM receives "IPC_VEHICLE_SETUP.PamChimeVolumeRear" message THEN TLM updates the Rear Park Sense Volume information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal
- **末** `r644` `Sys-RA-VF665_V43_VSM-643`：ELSE THEN TLM shall not display the "Park Sense Setting ", "Rear Park Sense Volume" and "Front Park Sense Volume" menu items and the user can not perform any setting.

### 4. `01.11.01.01.08.03`（11 列）
- **首** `r494` `Sys-RA-VF665_V43_VSM-493`：IF "Cluster_Display_Type" proxi parameter is equal to "Base Display" THEN TLM shall not display the Set Data menu item and the user can not perform any setting.
- **中** `r502` `Sys-RA-VF665_V43_VSM-501`：IF the user sets "Month2_Setting.Req" internal signals THEN TLM updates and sends the Month information to VF456 through "Month2_Setting.Info" internal signal
- **末** `r512` `Sys-RA-VF665_V43_VSM-511`：TLM receives "Time_Date_Setting_Feedback.Info" from VF456 to update time and date information in the setup menu.

### 5. `01.11.01.01.05`（10 列）
- **首** `r441` `Sys-RA-VF665_V43_VSM-440`：IF "Side_Distance_Warning" PROXI parameters is equal to "Absent" THEN TLM shall not display the Side Distance Warning menu item and the user can not perform any setting.
- **中** `r447` `Sys-RA-VF665_V43_VSM-446`：WHEN TLM receives "IPC_VEHICLE_SETUP.Sdw" message THEN TLM updates the Side Distance Warning information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal
- **末** `r452` `Sys-RA-VF665_V43_VSM-451`：WHEN TLM receives "IPC_VEHICLE_SETUP.SdwChimeVolume" message THEN TLM updates the Side Distance Warning information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 6. `01.11.01.01.26`（10 列）
- **首** `r652` `Sys-RA-VF665_V43_VSM-651`：IF "Ambient_Lighting_Function" PROXI parameter is equal to "Present" AND "Ambient_Dimmer_Switch"PROXI parameter is equal to "absent" THEN TLM shall display the Interior Ambient Lights Level menu item and the user can perform setting.
- **中** `r657` `Sys-RA-VF665_V43_VSM-656`：IF the user sets "Ambient_Lighting_level_Setting.Req" equal to "Level_5 " THEN TLM shal set "TELEMATIC_VEHICLE_SETUP.AmbientLightingLevel_Req" B-CAN signal equal to "Level_5 " and sends this signal to IPC
- **末** `r662` `Sys-RA-VF665_V43_VSM-661`：THEN TLM shall not display the Ambient Light Level menu item and the user can not perform any setting.

### 7. `01.11.01.01.03`（9 列）
- **首** `r421` `Sys-RA-VF665_V43_VSM-420`：IF "Half_Torque_Sensibility" PROXI parameter is equal to "Leve 3" THEN TLM shall display the " Lanse Sense Warning 1 " menu item and the user can perform setting with the following options: Early, Late
- **中** `r425` `Sys-RA-VF665_V43_VSM-424`：IF "Half_Torque_Sensibility" PROXI parameter is equal to "Leve 2" THEN TLM shall display the " Lanse Sense Warning 2" menu item and the user can perform setting with the following options: Early, Med, Late
- **末** `r429` `Sys-RA-VF665_V43_VSM-428`：WHEN TLM receives "IPC_VEHICLE_SETUP2.LDW_Sensibility" message THEN TLM updates the LDW Sensibility information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 8. `01.11.01.01.04`（9 列）
- **首** `r431` `Sys-RA-VF665_V43_VSM-430`：IF "Half_HMI_Setting" PROXI parameter is equal to "Leve 3" THEN TLM shall display the " Lanse Sense Strenght 1 " menu item and the user can perform setting with the following options: Low, High
- **中** `r435` `Sys-RA-VF665_V43_VSM-434`：IF "Half_HMI_Setting" PROXI parameter is equal to "Leve 2" THEN TLM shall display the " Lanse Sense Strenght 2" menu item and the user can perform setting with the following options: Low, Med, High
- **末** `r439` `Sys-RA-VF665_V43_VSM-438`：WHEN TLM receives "IPC_VEHICLE_SETUP2.LDW_Intensity" message THEN TLM updates the LDW Sensibility information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 9. `01.11.01.01.10.02`（9 列）
- **首** `r528` `Sys-RA-VF665_V43_VSM-527`：IF "Fuel_Type" PROXI parameter is different to "CNG" or "GPL" THEN TLM shall display the Consumption Measurement Unit menu item and the user can perform setting.
- **中** `r532` `Sys-RA-VF665_V43_VSM-531`：IF "Odo_Units_Change" PROXI parameter is equal to "present" AND "Distance_Unit_Setting.Req" is equal to "miles" THEN TLM shall display only the Consumption Unit menu item related to "mpg"
- **末** `r537` `Sys-RA-VF665_V43_VSM-536`：ELSE THEN TLM shall not display the Consumption Measurement Unit menu item and the user can not perform setting.

### 10. `01.11.01.01.10.04`（6 列）
- **首** `r545` `Sys-RA-VF665_V43_VSM-544`：IF "Tyre_Pressure_Unit_Menu" PROXI parameter is equal to "Absent" THEN TLM shall not display the Tyre Pressure Unit menu item and the user can not perform any setting.
- **中** `r548` `Sys-RA-VF665_V43_VSM-547`：IF the user sets "Tyre_Pressure_Unit_Setting.Req" internal signals to " psi" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP2.TyrePressureUnit_Req" B-CAN signal equal to " psi" and sends this signal to IPC
- **末** `r550` `Sys-RA-VF665_V43_VSM-549`：WHEN TLM receives "IPC_VEHICLE_SETUP2.TyrePressureUnit" message THEN TLM updates the Tyre Pressure Unit information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 11. `01.11.01.01.13`（6 列）
- **首** `r564` `Sys-RA-VF665_V43_VSM-563`：IF "Twilight_Sensor" PROXI parameter is equal to "absent" THEN TLM shall not display the External Light Sensor menu item and the user can not perform any setting.
- **中** `r567` `Sys-RA-VF665_V43_VSM-566`：IF the user sets "External_Light_Sensor_Level_Setting.Req" internal signal to "Level_2" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.ExternalLightSensorLevel_Req" B-CAN signal equal to "Level_2" and sends this signal to IPC
- **末** `r569` `Sys-RA-VF665_V43_VSM-568`：WHEN TLM receives "IPC_VEHICLE_SETUP.ExternalLightSensorLevel" message THEN TLM updates the External light Sensor information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 12. `01.11.01.01.14`（6 列）
- **首** `r571` `Sys-RA-VF665_V43_VSM-570`：TLM shall display the Headlights Off Delay menu item and the user can perform setting.
- **中** `r574` `Sys-RA-VF665_V43_VSM-573`：IF the user sets "Headlights_Off_Delay_Setting.Req " internal signal to " 60 " THEN TLM shall set "TELEMATIC_VEHICLE_SETUP2.HeadlightsOffDelay_Req " B-CAN signal equal to " 60 " and sends this signal to IPC
- **末** `r576` `Sys-RA-VF665_V43_VSM-575`：WHEN TLM receives "IPC_VEHICLE_SETUP2.HeadlightsOffDelay" message THEN TLM updates the Headlights Off Delay information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 13. `01.11.01.01.15`（6 列）
- **首** `r578` `Sys-RA-VF665_V43_VSM-577`：IF "CAN node 51 (LBSS)" == "Absent" OR "CAN node 52 (RBSS)" == "Absent" THEN TLM shall not display the Blind Spot Detection menu item and the user can not perform any setting.
- **中** `r581` `Sys-RA-VF665_V43_VSM-580`：IF the user sets "Blind_Spot_Detection_Setting.Req" internal signal to "Enable_ LED_Chime" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.BSDEnable_Req" B-CAN signal equal to "Enable_ LED_Chime" and sends this signal to IPC
- **末** `r583` `Sys-RA-VF665_V43_VSM-582`：WHEN TLM receives "IPC_VEHICLE_SETUP.BSDEnable" message THEN TLM updates the Blind Spot information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 14. `01.11.01.01.01`（5 列）
- **首** `r408` `Sys-RA-VF665_V43_VSM-407`：IF "Cornering_Lights" PROXI parameter is equal to "absent" THEN TLM shall not display the Cornering Light menu item and the user can not perform any setting.
- **中** `r410` `Sys-RA-VF665_V43_VSM-409`：IF the user sets "Cornering_Enable.Req" internal signals to "Enable" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.CorneringEnable_Req" B-CAN signal equal to "True" and sends this signal to IPC
- **末** `r412` `Sys-RA-VF665_V43_VSM-411`：WHEN TLM receives "IPC_VEHICLE_SETUP.CorneringLightsEnable" message THEN TLM updates the Cornering information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 15. `01.11.01.01.02`（5 列）
- **首** `r415` `Sys-RA-VF665_V43_VSM-414`：IF "Greeting_Lights_Menù" PROXI parameter is equal to "Absent" THEN TLM shall not display the Greeting Light menu item and the user can not perform any setting.
- **中** `r417` `Sys-RA-VF665_V43_VSM-416`：IF the user sets "GreetingLights_Enable.Req" internal signals to "Enable" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.GreetingLightsEnable_Req" B-CAN signal equal to "True" and sends this signal to IPC
- **末** `r419` `Sys-RA-VF665_V43_VSM-418`：WHEN TLM receives "IPC_VEHICLE_SETUP.GreetingLightsEnable" message THEN TLM updates the Greeting Lights information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 16. `01.11.01.01.07`（5 列）
- **首** `r472` `Sys-RA-VF665_V43_VSM-471`：IF "Rain_Sensor" PROXI parameter is equal to "present" THEN TLM shall display the Rain Sensor menu item and the user can perform setting.
- **中** `r474` `Sys-RA-VF665_V43_VSM-473`：IF the user sets "Rain_Sensor_Level_Setting.Req" internal signals to "Not_Enable" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.RainSensorLevel_Req" B-CAN signal equal to "Not_Enable" and sends this signal to IPC
- **末** `r476` `Sys-RA-VF665_V43_VSM-475`：WHEN TLM receives "IPC_VEHICLE_SETUP.RainSensorLevel" message THEN TLM updates the Rain Sensor information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 17. `01.11.01.01.08.01`（5 列）
- **首** `r479` `Sys-RA-VF665_V43_VSM-478`：TLM shall display the Clock Setting menu item and the user can perform setting.
- **中** `r482` `Sys-RA-VF665_V43_VSM-481`：IF the user sets "Hour2_Setting.Req" internal signals THEN TLM updates and sends the Hour information to VF456 through "Hour2_Setting.Info" internal signal
- **末** `r486` `Sys-RA-VF665_V43_VSM-485`：IF the user sets "Minute2_Setting.Req" internal signals THEN TLM updates and sends the Minute information to VF456 through "Minute1_Setting.Info" internal signal

### 18. `01.11.01.01.09`（5 列）
- **首** `r514` `Sys-RA-VF665_V43_VSM-513`：IF "Auto_Close_Menu" PROXI parameter is equal to "Disabled" THEN TLM shall not display the Speed Lock Door menu item and the user can not perform any settin
- **中** `r516` `Sys-RA-VF665_V43_VSM-515`：IF the user sets "Speed_Lock_Door_Enable.Req" internal signals to "Enable" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.SpeedLockDoorEnable_Req" B-CAN signal equal to "Enable" and sends this signal to IPC
- **末** `r518` `Sys-RA-VF665_V43_VSM-517`：WHEN TLM receives "IPC_VEHICLE_SETUP.SpeedLockDoorEnable" message THEN TLM updates the Speed Lock Door information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 19. `01.11.01.01.10.01`（5 列）
- **首** `r522` `Sys-RA-VF665_V43_VSM-521`：IF "Odo_Units Change" PROXI parameter is equal to "absent" THEN TLM shall not display the Distance Measurement Unit menu item and the user can not perform any setting.
- **中** `r524` `Sys-RA-VF665_V43_VSM-523`：IF the user sets "Distance_Unit_Setting.Req" internal signals to "Km" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.DistanceUnit_Req" B-CAN signal equal to "Km" and sends this signal to IPC
- **末** `r526` `Sys-RA-VF665_V43_VSM-525`：WHEN TLM receives "IPC_VEHICLE_SETUP.DistanceUnit" message THEN TLM updates the Distance Measurement Unit information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 20. `01.11.01.01.10.03`（5 列）
- **首** `r539` `Sys-RA-VF665_V43_VSM-538`：IF "External_Temperature_Sensor" PROXI parameter is equal to "absent" THEN TLM shall not display the External Temperature Measurement Unit menu item and the user can not perform any setting.
- **中** `r541` `Sys-RA-VF665_V43_VSM-540`：IF the user sets "Temperature_Unit_Setting.Req" internal signals to "°C" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.TemperatureUnit_Req" B-CAN signal equal to "°C" and sends this signal to IPC
- **末** `r543` `Sys-RA-VF665_V43_VSM-542`：WHEN TLM receives "IPC_VEHICLE_SETUP.TemperatureUnit" message THEN TLM updates the External TemperatureMeasurement Unit information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 21. `01.11.01.01.12`（5 列）
- **首** `r558` `Sys-RA-VF665_V43_VSM-557`：IF "DRL_Menù_Enable" PROXI parameter is equal to "Disabled" THEN TLM shall not display the DRL menu item and the user can not perform any setting.
- **中** `r560` `Sys-RA-VF665_V43_VSM-559`：IF the user sets "DRL_Enable.Req" internal signals to "Enable" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.DRLEnable_Req" B-CAN signal equal to "True" and sends this signal to IPC
- **末** `r562` `Sys-RA-VF665_V43_VSM-561`：WHEN TLM receives "IPC_VEHICLE_SETUP.DRLEnable" message THEN TLM updates the DRL information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 22. `01.11.01.01.16`（5 列）
- **首** `r585` `Sys-RA-VF665_V43_VSM-584`：IF "Passive_Entry_Menu" PROXI parameter is equal to "Absent" THEN TLM shall not display the Passive Entry menu item and the user can not perform any setting.
- **中** `r587` `Sys-RA-VF665_V43_VSM-586`：IF the user sets "Passive_Entry_Enable.Req" internal signals to "On" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req" B-CAN signal equal to "On" and sends this signal to IPC
- **末** `r589` `Sys-RA-VF665_V43_VSM-588`：WHEN TLM receives "IPC_VEHICLE_SETUP.PassiveEntry" message THEN TLM updates the Passive Entry information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 23. `01.11.01.01.17`（5 列）
- **首** `r591` `Sys-RA-VF665_V43_VSM-590`：IF "Remote_Door_Unlock_Menu" PROXI parameter is equal to "Absent" THEN TLM shall not display the Remote Door Unlock menu item and the user can not perform any setting.
- **中** `r593` `Sys-RA-VF665_V43_VSM-592`：IF the user sets "Remote_Door_Unlock_Setting.Req" internal signals to "Driver" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock._Req" B-CAN signal equal to "Driver" and sends this signal to IPC
- **末** `r595` `Sys-RA-VF665_V43_VSM-594`：WHEN TLM receives "IPC_VEHICLE_SETUP.RemoteDoorUnlock" message THEN TLM updates the Remote Door Unlock information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 24. `01.11.01.01.18`（5 列）
- **首** `r597` `Sys-RA-VF665_V43_VSM-596`：IF "Horn_Chirp_Menu" PROXI parameter is equal to "Absent" THEN TLM shall not display the Sound Horn with Lock Unlock menu item and the user can not perform any setting.
- **中** `r599` `Sys-RA-VF665_V43_VSM-598`：IF the user sets "Sound_Horn_Lock_Unlock_Setting.Req" internal signals to "Off" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP3.SoundHornLockUnlock_Req" B-CAN signal equal to "Off" and sends this signal to IPC
- **末** `r601` `Sys-RA-VF665_V43_VSM-600`：WHEN TLM receives "IPC_VEHICLE_SETUP3.SoundHornLockUnlock" message THEN TLM updates the Sound Horn with Lock Unlock information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 25. `01.11.01.01.19`（5 列）
- **首** `r603` `Sys-RA-VF665_V43_VSM-602`：IF "Auto_Door_Unlock_Menu" PROXI parameter is equal to "Absent" THEN TLM shall not display the Auto Unlock Door Exit menu item and the user can not perform any setting.
- **中** `r605` `Sys-RA-VF665_V43_VSM-604`：IF the user sets "Auto_Unlock_Door_Exit_Enable.Req" internal signals to " Enable" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP2.AutoUnlockDoorExit_Req" B-CAN signal equal to "Enable" and sends this signal to IPC
- **末** `r607` `Sys-RA-VF665_V43_VSM-606`：WHEN TLM receives "IPC_VEHICLE_SETUP2.AutoUnlockDoorExit" message THEN TLM updates the Auto Unlock Door Exit information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 26. `01.11.01.01.20`（5 列）
- **首** `r609` `Sys-RA-VF665_V43_VSM-608`：IF "Flash_Light_With_Lock_Menu" PROXI parameter is equal to "Absent" THEN TLM shall not display the Flash Light With Lock menu item and the user can not perform any setting.
- **中** `r611` `Sys-RA-VF665_V43_VSM-610`：IF the user sets " Flash_Light_With_Lock_Enable.Req " internal signal to " Off" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP2.FlashLightWLock_Req" B-CAN signal equal to "Off" and sends this signal to IPC
- **末** `r613` `Sys-RA-VF665_V43_VSM-612`：WHEN TLM receives "IPC_VEHICLE_SETUP2.FlashLightWLock" message THEN TLM updates the Flash Light With Lock information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 27. `01.11.01.01.25`（5 列）
- **首** `r646` `Sys-RA-VF665_V43_VSM-645`：IF “AHBM_Feature_Menu ” PROXI parameter is equal to "Absent" THEN TLM shall display the Auto High Beam menu item and the user can not perform any setting.
- **中** `r648` `Sys-RA-VF665_V43_VSM-647`：IF the user sets "Auto_High_Beam_Enable.Req" equal to "Enable" THEN TLM shall to set "TELEMATIC_VEHICLE_SETUP.AutoHighBeamEnable_Req" B-CAN signal equal to "Enable" and sends this signal to IPC
- **末** `r650` `Sys-RA-VF665_V43_VSM-649`：WHEN TLM receives "IPC_VEHICLE_SETUP.AutoHighBeamEnable" message THEN TLM updates the Auto High Beam information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 28. `01.11.01.01.27`（5 列）
- **首** `r664` `Sys-RA-VF665_V43_VSM-663`：IF “CAN Node 35 (TBM)” PROXI parameter is equal to "Absent" OR IF “Geolocation_Menu” PROXI parameter is equal to "Absent" THEN TLM shall not display the Geolocation menu item and the user can not perform any setting.
- **中** `r666` `Sys-RA-VF665_V43_VSM-665`：IF the user sets "Geolocation_Enable.Req" equal to "Off" TLM shall set "TELEMATIC_SERVICE_SETUP.PrivacyModeReq" BH-CAN signal equal to "Active" and sends this signal to TBM
- **末** `r668` `Sys-RA-VF665_V43_VSM-667`：WHEN TLM receives "SERVICE_SETUP.PrivacyMode" message THEN TLM updates the Privacy Mode information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 29. `01.11.01.01.08.02`（4 列）
- **首** `r489` `Sys-RA-VF665_V43_VSM-488`：TLM shall display the Hour Mode menu item and the user can perform setting.
- **中** `r491` `Sys-RA-VF665_V43_VSM-490`：IF the user sets "Hour_Mode_Setting.Req" internal signals to "0_12_h" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.HourMode_Req" B-CAN signal equal to "0_12_h" and sends this signal to IPC
- **末** `r492` `Sys-RA-VF665_V43_VSM-491`：WHEN TLM receives "IPC_VEHICLE_SETUP.HourMode" message THEN TLM updates the Hour Mode information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

### 30. `01.11.01.01.11`（4 列）
- **首** `r553` `Sys-RA-VF665_V43_VSM-552`：display the "Language" menu item. display the language SETS described in "Market Configuration Table" document according to "Country_Code" PROXI parameter
- **中** `r555` `Sys-RA-VF665_V43_VSM-554`：WHEN TLM receives "IPC_VEHICLE_SETUP.LanguageSelection" message THEN TLM updates the Language information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal
- **末** `r556` `Sys-RA-VF665_V43_VSM-555`：IF TLM receives a negative Ack from IPC THEN the TLM has to maintain the language previously selected.

### 31. `01.11.01.01.21`（4 列）
- **首** `r615` `Sys-RA-VF665_V43_VSM-614`：IF "NAV_Presence" PROXI parameter is equal to "Absent" THEN TLM shall not display the GPS Automatic Time Adjustment menu item and the user can not perform any setting.
- **中** `r617` `Sys-RA-VF665_V43_VSM-616`：IF the user sets "GPS_Automatic_Time_Adj_Enable.Req" internal signals to "Not_Enable" THEN TLM updates and sends the GPS Time Adjustment information to VF456 through "GPS_Automatic_Time_Adj_Setup.Info" internal signal
- **末** `r618` `Sys-RA-VF665_V43_VSM-617`：IF the user sets "GPS_Automatic_Time_Adj_Enable.Req" internal signals to "Enable" THEN TLM updates and sends the GPS Time Adjustment information to VF456 through "GPS_Automatic_Time_Adj_Setup.Info" internal signal

### 32. `01.11.01.01.31`（4 列）
- **首** `r682` `Sys-RA-VF665_V43_VSM-681`：IF TLM sends a request of vehicle setup to IPC through "TELEMATIC_VEHICLE_SETUP" message THEN TLM has to wait for the "Acnowledge" through "IPC_VEHICLE_SETUP.TelematicSetupACK" from IPC to confirm the corrected reception and storage of the settings requested
- **中** `r684` `Sys-RA-VF665_V43_VSM-683`：IF TLM receives "IPC_VEHICLE_SETUP.TelematicSetupACK"equal to "ACK_KO" value. THEN TLM has to visualize a message related to the failure (see HMI document).
- **末** `r685` `Sys-RA-VF665_V43_VSM-684`：IF TLM receives "IPC_VEHICLE_SETUP.TelematicSetupACK"equal to "ACK_OK" value. THEN TLM has to visualize the new parameters transmitted by IPC ("IPC_VEHICLE_SETUP" message).

### 33. `01.11.01.01.32`（4 列）
- **首** `r687` `Sys-RA-VF665_V43_VSM-686`：IF TLM sends a request of vehicle setup to TBM through "TELEMATIC_SERVICE_SETUP" message THEN TLM has to wait for the "Acnowledge" through "SERVICE_SETUP.TelematicSetupACK" from TBM to confirm the corrected reception and storage of the settings requested
- **中** `r689` `Sys-RA-VF665_V43_VSM-688`：IF TLM receives "SERVICE_SETUP.TelematicSetupACK"equal to "ACK_KO" value. THEN TLM has to visualize a message related to the failure (see HMI document).
- **末** `r690` `Sys-RA-VF665_V43_VSM-689`：IF TLM receives "SERVICE_SETUP.TelematicSetupACK"equal to "ACK_OK" value. THEN TLM has to visualize the new parameters transmitted by TBM ("SERVICE_SETUP" message).

### 34. `01.11.01.01.28`（3 列）
- **首** `r670` `Sys-RA-VF665_V43_VSM-669`：IF “CAN Node 35 (TBM)” PROXI parameter is equal to "Absent" THEN TLM shall not manage "TELEMATIC_SERVICE_SETUP.ClearPersonalDataReq" and "SERVICE_SETUP.ClearPersonalData" BH-CAN signals.
- **中** `r671` `Sys-RA-VF665_V43_VSM-670`：IF “CAN Node 35 (TBM)” PROXI parameter is equal to "Present" THEN TLM shall manage the Clear Personal Data feature and the user can perform the service setup reset.
- **末** `r672` `Sys-RA-VF665_V43_VSM-671`：IF the user performs "ClearPersonalData_Enable.Req" request TLM shall only send "TELEMATIC_SERVICE_SETUP.ClearPersonalDataReq" BH-CAN signal equal to "Active" to TBM.

### 35. `01.11.01.01.29`（3 列）
- **首** `r674` `Sys-RA-VF665_V43_VSM-673`：IF “CAN Node 35 (TBM)” PROXI parameter is equal to "Absent" THEN TLM shall not manage "TELEMATIC_SERVICE_SETUP.RestoreDefaultSettingReq" and "SERVICE_SETUP.RestoreDefaulSetting" BH-CAN signals.
- **中** `r675` `Sys-RA-VF665_V43_VSM-674`：IF “CAN Node 35 (TBM)” PROXI parameter is equal to "Present" THEN TLM shall manage the Restore Default Setting feature and the user can perform the service setup reset.
- **末** `r676` `Sys-RA-VF665_V43_VSM-675`：IF the user performs "RestoreDefaultSetting_Enable.Req" request TLM shall only send "TELEMATIC_SERVICE_SETUP.RestoreDefaultSettingReq" BH-CAN signal equal to "Active" to TBM

### 36. `01.11.01.01.30`（3 列）
- **首** `r678` `Sys-RA-VF665_V43_VSM-677`：IF “CAN Node 35 (TBM)” PROXI parameter is equal to "Absent" THEN TLM shall not manage "TELEMATIC_SERVICE_SETUP.RestoreAppReq" and "SERVICE_SETUP.RestoreApp" BH-CAN signals.
- **中** `r679` `Sys-RA-VF665_V43_VSM-678`：IF “CAN Node 35 (TBM)” PROXI parameter is equal to "Present" THEN TLM shall manage the Restore App feature and the user can perform the service setup reset.
- **末** `r680` `Sys-RA-VF665_V43_VSM-679`：IF the user performs "RestoreApp_Enable.Req" request TLM shall only send "TELEMATIC_SERVICE_SETUP.RestoreAppReq" BH-CAN signal equal to "Active" to TBM

### 37. `01.13.02.01.03`（3 列）
- **首** `r795` `Sys-RA-VF665_V43_VSM-794`：In the following Ignition Working Condition: "Ignition Off" "Ignition On" "Ignition On Engine On" IF TLM does not receive the SERVICE_SETUP message for a time equal to T_REC_TBM AND IF CAN Node 35 (TBM) PROXI Parameter is equals to "Present" AND FOTA_State.Info internal signal is equal to "NO_FOTA_State" THEN TLM shall set the DTC, according to "TLM Diagnostic Requirement" document.
- **中** `r796` `Sys-RA-VF665_V43_VSM-795`：IF TLM doesn't receive "SERVICE_SETUP.TelematicSetupACK" within "TimeOut1" THEN TLM has to resend the new vehicle setup request (This logic must be implemented for a max of three times after TLM has to visualize a message to the user about the failure of request )
- **末** `r797` `Sys-RA-VF665_V43_VSM-796`：As soon as TLM receives again SERVICE_SETUP message, TLM shall: heal the DTC, according to the requirements specified in the "TLM Diagnostic Requirement" document.

### 38. `01.11.01.01`（2 列）
- **首** `r404` `Sys-RA-VF665_V43_VSM-403`：In the following Ignition Working Conditions: Ignition On Ignition Pre Start Ignition Start Ignition Cranking Ignition On Engine On the user can mange the vehicle setup menu through TLM_Display.GUI.
- **末** `r405` `Sys-RA-VF665_V43_VSM-404`：In case of transition FROM "Ignition On" or "Ignition Pre Start" or "Ignition Start" or "Ignition Cranking" or "Ignition On Engine On" TO "Ignition Pre Off" or "Ignition Off" Ignition Working Conditions: TLM shall store the last setup settings.

### 39. `01.11.01.01.22`（2 列）
- **首** `r620` `Sys-RA-VF665_V43_VSM-619`：IF TLM receives "IPC_VEHICLE_SETUP.PhoneRepetition"set to "Present" THEN TLM updates and sends the information for enabling the Phone repetition to VF464 through "PhoneRepetition.Info" internal signal
- **末** `r621` `Sys-RA-VF665_V43_VSM-620`：IF TLM receives "IPC_VEHICLE_SETUP.PhoneRepetition"set to "Absent" THEN TLM updates and sends the information for disabling the Phone repetition to VF464 through "PhoneRepetition.Info" internal signal

### 40. `01.11.01.01.23`（2 列）
- **首** `r623` `Sys-RA-VF665_V43_VSM-622`：IF TLM receives "IPC_VEHICLE_SETUP.NavRepetition"set to "Present" THEN TLM updates and sends the information for enabling the Navigation repetition to VF176 through "NavigationRepetition.Info" internal signal
- **末** `r624` `Sys-RA-VF665_V43_VSM-623`：IF TLM receives "IPC_VEHICLE_SETUP.NavRepetition"set to "Absent" THEN TLM updates and sends the information for disabling the Navigation repetition to VF176 through "NavigationRepetition.Info" internal signal

### 41. `01.11.01.01.10`（1 列）
- **末** `r520` `Sys-RA-VF665_V43_VSM-519`：The LTM/ETM shall display the Unit Custom setting to allow the customer the ability to modify the measurement units setting.

### 42. `01.13.02.01.01`（1 列）
- **末** `r790` `Sys-RA-VF665_V43_VSM-789`：In case absence of IPC_VEHICLE_SETUP or IPC_VEHICLE_SETUP2 B-CAN message in Key On, TLM has to store an appropriate DTC in according to validation requirements defined in the CDD document. IF TLM doesn't receive these messages within "TimeOut1" THEN TLM has to resend the new vehicle setup request (This logic must be implemented for a max of three times after TLM has to visualize a message to the user about the failure of request )

### 43. `01.13.02.01.02`（1 列）
- **末** `r793` `Sys-RA-VF665_V43_VSM-792`：WHEN "LTM_OperationalModeSts.Info" == "SNA" THEN LTM shall: keep the last valid value that has been recognized.

### 44. `01.14.02.01.01`（1 列）
- **末** `r876` `Sys-RA-VF665_V43_VSM-875`：The "Cornering_Light" PROXI parameter is used to show or hide the "Cornering Lights" menu item.

### 45. `01.14.02.01.02`（1 列）
- **末** `r878` `Sys-RA-VF665_V43_VSM-877`：The "Odo_Units Change" PROXI parameter is used to show or hide the "Distance" menu item (only for Japanese market if forseen).

### 46. `01.14.02.01.03`（1 列）
- **末** `r880` `Sys-RA-VF665_V43_VSM-879`：The "Fuel_Type" PROXI parameter is used to show or hide the "Consumption" menu item for the alternative fuel versions (CNG or LPG).

### 47. `01.14.02.01.04`（1 列）
- **末** `r882` `Sys-RA-VF665_V43_VSM-881`：The "External_Temperature_Sensor" PROXI parameter is used to show or hide the "Temperature" menu item.

### 48. `01.14.02.01.05`（1 列）
- **末** `r884` `Sys-RA-VF665_V43_VSM-883`：The "Rain_Sensor" PROXI parameter is used to show or hide the "Rain sensor" menu item.

### 49. `01.14.02.01.06`（1 列）
- **末** `r886` `Sys-RA-VF665_V43_VSM-885`：The "Twilight_Sensor" PROXI parameter is used to show or hide the "Headlamp sensor" menu item.

### 50. `01.14.02.01.07`（1 列）
- **末** `r888` `Sys-RA-VF665_V43_VSM-887`：The "Auto_Close_Menu" PROXI parameter is used to show or hide the "Autoclose" menu item.

### 51. `01.14.02.01.08`（1 列）
- **末** `r890` `Sys-RA-VF665_V43_VSM-889`：The "Cluster_Display_Type" PROXI parameter is used to inform about the tipe of cluster

### 52. `01.14.02.01.09`（1 列）
- **末** `r892` `Sys-RA-VF665_V43_VSM-891`：The "Country_Code" PROXI parameter is used to to manage consumption and temperature measure unit.

### 53. `01.14.02.01.10`（1 列）
- **末** `r894` `Sys-RA-VF665_V43_VSM-893`：The "DRL_Menù_Enable" PROXI parameter is used to show or hide the "Day lights" menu item.

### 54. `01.14.02.01.11`（1 列）
- **末** `r896` `Sys-RA-VF665_V43_VSM-895`：The "Greeting_Lights_Menù" PROXI parameter is used to show or hide the "Greeting Lights" menu item.

### 55. `01.14.02.01.12`（1 列）
- **末** `r898` `Sys-RA-VF665_V43_VSM-897`：The "CAN node 51 (LBSS)" PROXI parameter is used to show or hide the "Blind Spot Detection" menu item.

### 56. `01.14.02.01.13`（1 列）
- **末** `r900` `Sys-RA-VF665_V43_VSM-899`：The "CAN node 52 (RBSS)" PROXI parameter is used to show or hide the "Blind Spot Detection" menu item.

### 57. `01.14.02.01.14`（1 列）
- **末** `r902` `Sys-RA-VF665_V43_VSM-901`：The "Passive_Entry_Menu" PROXI parameter is used to show or hide the "Passive Entry" menu item.

### 58. `01.14.02.01.15`（1 列）
- **末** `r904` `Sys-RA-VF665_V43_VSM-903`：The "Remote_Door_Unlock _Menu" PROXI parameter is used to show or hide the "Remote Door Unlock" menu item.

### 59. `01.14.02.01.16`（1 列）
- **末** `r906` `Sys-RA-VF665_V43_VSM-905`：The "Sound_Horn_Remote_Start _Menu" PROXI parameter is used to show or hide the "Sound Horn Remote Start" menu item.

### 60. `01.14.02.01.17`（1 列）
- **末** `r908` `Sys-RA-VF665_V43_VSM-907`：The "Horn_Chirp_Menù" PROXI parameter is used to show or hide the "Sound Horn With Lock" menu item (if Model_Year<20) OR "Sound Horn with Lock Unlock" menu item (if Model_Year>=20)

### 61. `01.14.02.01.18`（1 列）
- **末** `r910` `Sys-RA-VF665_V43_VSM-909`：The "Flash_Light_With_Lock_Menu" PROXI parameter is used to show or hide the "Flash Light with Lock" menu item.

### 62. `01.14.02.01.19`（1 列）
- **末** `r912` `Sys-RA-VF665_V43_VSM-911`：The " Tyre_Pressure_Unit_Menu "PROXI parameter is used to show or hide the "Tyre Pressure" menu item.

### 63. `01.14.02.01.20`（1 列）
- **末** `r914` `Sys-RA-VF665_V43_VSM-913`：The "CAN node 24 (PAM) " PROXI parameter is used to detect the presence the "Park Assist Module"

### 64. `01.14.02.01.21`（1 列）
- **末** `r916` `Sys-RA-VF665_V43_VSM-915`：The " Side_Distance_Warning "PROXI parameter is used to show or hide the " Side Distance Warning " menu item.

### 65. `01.14.02.01.22`（1 列）
- **末** `r918` `Sys-RA-VF665_V43_VSM-917`：The "PAM_Configuration" PROXI parameter is used to show or hide the "Park Assist Module" menu item.

### 66. `01.14.02.01.23`（1 列）
- **末** `r920` `Sys-RA-VF665_V43_VSM-919`：The "Auto_Door_Unlock_Menu" PROXI parameter is used to show or hide the "Auto Door Unlock On Exit" menu item.

### 67. `01.14.02.01.24`（1 列）
- **末** `r922` `Sys-RA-VF665_V43_VSM-921`：The " Half_HMI_Setting " PROXI parameter is used to show or hide the " LDW Intensity" menu item.

### 68. `01.14.02.01.25`（1 列）
- **末** `r924` `Sys-RA-VF665_V43_VSM-923`：The " Half_Torque_Sensibility " PROXI parameter is used to show or hide the " LDW Sensibility" menu item.

### 69. `01.14.02.01.26`（1 列）
- **末** `r926` `Sys-RA-VF665_V43_VSM-925`：The " AHBM_Feature_Menu " PROXI parameter is used to show or hide the " Auto High Beam Menu" menu item.

### 70. `01.14.02.01.27`（1 列）
- **末** `r928` `Sys-RA-VF665_V43_VSM-927`：The "NAV_Presence" PROXI parameter identifies the presence of Navigation functionalities

### 71. `01.14.02.01.28`（1 列）
- **末** `r930` `Sys-RA-VF665_V43_VSM-929`：The " Ambient_Lighting_Function" PROXI parameter is used to show or hide the "Interior Ambient Light" menu item.

### 72. `01.14.02.01.29`（1 列）
- **末** `r932` `Sys-RA-VF665_V43_VSM-931`：The " Ambient_Dimmer_Switch" PROXI parameter is used to show or hide the " Interior Ambient Light" menu item.

## 三、標題（`Description`）詞頻前 30

正規化：小寫、取 `[A-Za-z][A-Za-z_]{2,}` 詞元、去停用詞（the/of/and/for/to/is/in/a/be/shall/if/or/on/when/with/as/this/that/it/by）。

| # | 詞 | 次數 |
|---|---|---|
| 1 | `tlm` | 280 |
| 2 | `signal` | 237 |
| 3 | `then` | 214 |
| 4 | `can` | 173 |
| 5 | `equal` | 167 |
| 6 | `user` | 165 |
| 7 | `proxi` | 156 |
| 8 | `internal` | 140 |
| 9 | `req` | 106 |
| 10 | `sends` | 103 |
| 11 | `display` | 102 |
| 12 | `sets` | 99 |
| 13 | `set` | 95 |
| 14 | `setting` | 93 |
| 15 | `menu` | 92 |
| 16 | `parameter` | 89 |
| 17 | `telematic_vehicle_setup` | 87 |
| 18 | `ipc` | 87 |
| 19 | `item` | 84 |
| 20 | `value` | 78 |
| 21 | `signals` | 77 |
| 22 | `perform` | 61 |
| 23 | `through` | 57 |
| 24 | `not` | 56 |
| 25 | `info` | 55 |
| 26 | `information` | 53 |
| 27 | `updates` | 52 |
| 28 | `receives` | 47 |
| 29 | `message` | 45 |
| 30 | `ipc_vehicle_setup` | 44 |

## 四、295 列 ∩ v5「解得」訊號之分組分布（P4 可執行度預估）

- 295 列中，`Description` 含 v5 事實表訊號名者：**263** 列
- 其中含**「解得」**訊號（可寫 `$MESSAGE.Signal$`）者：**126** 列
- 兩者皆無者：**32** 列

| chapter_for_vf | 列數 | 含訊號 | 含解得 | 含解得占比 |
|---|---|---|---|---|
| `01.14.01` | 38 | 29 | 0 | 0% |
| `01.11.01.01.06` | 15 | 15 | 12 | 80% |
| `01.11.01.01.24` | 15 | 11 | 11 | 73% |
| `01.11.01.01.08.03` | 11 | 10 | 0 | 0% |
| `01.11.01.01.05` | 10 | 10 | 8 | 80% |
| `01.11.01.01.26` | 10 | 9 | 8 | 80% |
| `01.11.01.01.03` | 9 | 9 | 7 | 78% |
| `01.11.01.01.04` | 9 | 9 | 7 | 78% |
| `01.11.01.01.10.02` | 9 | 8 | 5 | 56% |
| `01.11.01.01.10.04` | 6 | 6 | 4 | 67% |
| `01.11.01.01.13` | 6 | 6 | 4 | 67% |
| `01.11.01.01.14` | 6 | 5 | 5 | 83% |
| `01.11.01.01.15` | 6 | 4 | 0 | 0% |
| `01.11.01.01.01` | 5 | 5 | 2 | 40% |
| `01.11.01.01.02` | 5 | 5 | 3 | 60% |
| `01.11.01.01.07` | 5 | 5 | 0 | 0% |
| `01.11.01.01.08.01` | 5 | 4 | 0 | 0% |
| `01.11.01.01.09` | 5 | 5 | 3 | 60% |
| `01.11.01.01.10.01` | 5 | 5 | 3 | 60% |
| `01.11.01.01.10.03` | 5 | 5 | 3 | 60% |
| `01.11.01.01.12` | 5 | 5 | 3 | 60% |
| `01.11.01.01.16` | 5 | 5 | 3 | 60% |
| `01.11.01.01.17` | 5 | 5 | 1 | 20% |
| `01.11.01.01.18` | 5 | 5 | 3 | 60% |
| `01.11.01.01.19` | 5 | 5 | 3 | 60% |
| `01.11.01.01.20` | 5 | 5 | 3 | 60% |
| `01.11.01.01.25` | 5 | 5 | 3 | 60% |
| `01.11.01.01.27` | 5 | 5 | 3 | 60% |
| `01.11.01.01.08.02` | 4 | 3 | 3 | 75% |
| `01.11.01.01.11` | 4 | 3 | 2 | 50% |
| `01.11.01.01.21` | 4 | 4 | 0 | 0% |
| `01.11.01.01.31` | 4 | 4 | 4 | 100% |
| `01.11.01.01.32` | 4 | 4 | 0 | 0% |
| `01.11.01.01.28` | 3 | 2 | 2 | 67% |
| `01.11.01.01.29` | 3 | 2 | 2 | 67% |
| `01.11.01.01.30` | 3 | 2 | 2 | 67% |
| `01.13.02.01.03` | 3 | 2 | 0 | 0% |
| `01.11.01.01` | 2 | 1 | 0 | 0% |
| `01.11.01.01.22` | 2 | 2 | 2 | 100% |
| `01.11.01.01.23` | 2 | 2 | 2 | 100% |
| `01.11.01.01.10` | 1 | 0 | 0 | 0% |
| `01.13.02.01.01` | 1 | 0 | 0 | 0% |
| `01.13.02.01.02` | 1 | 1 | 0 | 0% |
| `01.14.02.01.01` | 1 | 1 | 0 | 0% |
| `01.14.02.01.02` | 1 | 1 | 0 | 0% |
| `01.14.02.01.03` | 1 | 1 | 0 | 0% |
| `01.14.02.01.04` | 1 | 1 | 0 | 0% |
| `01.14.02.01.05` | 1 | 1 | 0 | 0% |
| `01.14.02.01.06` | 1 | 1 | 0 | 0% |
| `01.14.02.01.07` | 1 | 1 | 0 | 0% |
| `01.14.02.01.08` | 1 | 1 | 0 | 0% |
| `01.14.02.01.09` | 1 | 1 | 0 | 0% |
| `01.14.02.01.10` | 1 | 1 | 0 | 0% |
| `01.14.02.01.11` | 1 | 1 | 0 | 0% |
| `01.14.02.01.12` | 1 | 0 | 0 | 0% |
| `01.14.02.01.13` | 1 | 0 | 0 | 0% |
| `01.14.02.01.14` | 1 | 1 | 0 | 0% |
| `01.14.02.01.15` | 1 | 1 | 0 | 0% |
| `01.14.02.01.16` | 1 | 1 | 0 | 0% |
| `01.14.02.01.17` | 1 | 1 | 0 | 0% |
| `01.14.02.01.18` | 1 | 1 | 0 | 0% |
| `01.14.02.01.19` | 1 | 1 | 0 | 0% |
| `01.14.02.01.20` | 1 | 0 | 0 | 0% |
| `01.14.02.01.21` | 1 | 1 | 0 | 0% |
| `01.14.02.01.22` | 1 | 1 | 0 | 0% |
| `01.14.02.01.23` | 1 | 1 | 0 | 0% |
| `01.14.02.01.24` | 1 | 1 | 0 | 0% |
| `01.14.02.01.25` | 1 | 1 | 0 | 0% |
| `01.14.02.01.26` | 1 | 1 | 0 | 0% |
| `01.14.02.01.27` | 1 | 1 | 0 | 0% |
| `01.14.02.01.28` | 1 | 1 | 0 | 0% |
| `01.14.02.01.29` | 1 | 1 | 0 | 0% |
