# pilot 素材 — 規格節 `1.11.1.1.19 EPB Maintenance Mode`

來源：`sources/extracted/vf665_v42_spec_r6/document_paragraphs.tsv`（自 docx `word/document.xml` 抽取）。
切法：起＝標題段 1047（`1.11.1.1.19`）；迄＝下一同級標題段 1118（`1.11.1.1.20 Auto Park Brake`）之前一段。
**逐字照錄，含段號；未改寫、未省略。**

| 段號 | 層級 | 內容 |
|---|---|---|
| 1047 | H5 1.11.1.1.19 | EPB Maintenance Mode |
| 1048 |  | IF"EPB_Maintenance_Menu" PROXI parameter is equal to "Absent" |
| 1049 |  | THENTLM shall not display the EPB Maintance Mode  menu item and the user can not perform any setting. |
| 1050 |  | IF" EPB_Maintenance_Menu " PROXI parameter is equal to "Present" |
| 1051 |  | THENTLM shall display the EPB Maintance Mode menu item and the user can perform setting. |
| 1052 |  | IFthe user sets "Maintenance_Mode_Enable.Req" internal signals equal to " On" |
| 1053 |  | THENTLM shall: |
| 1054 |  |  Set "TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req" B-CAN signal equal to " On  " and sends this signal to IPC |
| 1055 |  | activate and display the Popup related to "  initializing "  like described in the "Human Machine Interface logic &  flow" document |
| 1056 |  | Start T_EPB_MM  |
| 1057 |  | T_EPB_MM  is the timeout for the EPB Maintenance Mode setting |
| 1058 |  | IF  T_EPB_MM  is not expired |
| 1059 |  | IF        "IPC_VEHICLE_SETUP2.EPB_MaintenanceMode" B CAN signal  change from "Off"  to "On"    |
| 1060 |  | THEN TLM shall: |
| 1061 |  | activate and display the  Popup related to " the user selected yes to exiting service mode and the first step is to step on the brake pedal " like described in the "Human Machine Interface logic &  flow" document |
| 1062 |  |  reset T_EPB_MM |
| 1063 |  |  |
| 1064 |  | IF TLM receives "IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk" set to " 2 " |
| 1065 |  | THEN TLM sall: |
| 1066 |  | activate and display the  Popup related to "  the user elected yes to entering service mode but he vehicle speed is not at 0mph "  like described in the "Human Machine Interface logic &  flow" document |
| 1067 |  | Reset T_EPB_MM |
| 1068 |  |  |
| 1069 |  | IF TLM receives "IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk" set to " 3 " |
| 1070 |  | THEN TLM sall: |
| 1071 |  | activate and display the Popup related to "the user selected yes to entering service mode but the vehicle is not in park or neutral"  like described in the "Human Machine Interface logic &  flow" document.  |
| 1072 |  | Reset T_EPB_MM |
| 1073 |  |  |
| 1074 |  | IF TLM receives "IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk" set to " 4 " |
| 1075 |  | THEN TLM sall: |
| 1076 |  | activate and display the Popup related to "the user selected yes to entering service mode but the EPB switch is currently engaged"  like described in the "Human Machine Interface logic &  flow" document |
| 1077 |  | Reset T_EPB_MM |
| 1078 |  |  |
| 1079 |  | IF TLM receives "IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk" set to " 5 " |
| 1080 |  | THEN TLM sall: |
| 1081 |  | activate and display the Popup related to " the user selected yes to entering service mode but the EPB switch is currently engaged" "  like described in the "Human Machine Interface logic &  flow" document |
| 1082 |  | Reset T_EPB_MM |
| 1083 |  |  |
| 1084 |  | IF TLM receives "IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk" set to " 6 " |
| 1085 |  | THEN TLM sall: |
| 1086 |  | activate and display the Popup related to " the user selected yes to entering service mode but the brake pedal is currently pressed"  like described in the "Human Machine Interface logic &  flow" document |
| 1087 |  | Reset T_EPB_MM |
| 1088 |  |  |
| 1089 |  | ELSE |
| 1090 |  | THEN    TLM shall: |
| 1091 |  | activate and display the Popup related to " no response from EPB module " like described in the "Human Machine Interface logic &  flow" document |
| 1092 |  |  |
| 1093 |  | IF TLM receives "IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk" set to " 8 " |
| 1094 |  | THEN TLM sall: |
| 1095 |  | activate and display the  Popup related to " Brake Service Park Brake Retracted. To reset, press brake pedal and activate Park Brake switch."  like described in the "Human Machine Interface logic &  flow" document |
| 1096 |  |  |
| 1097 |  | IF TLM receives "IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk" set to " 9 " |
| 1098 |  | THEN TLM sall: |
| 1099 |  | activate and display the Popup related to "  the user selected yes to exiting service mode but the vehicle speed is not at 0mph "  like described in the "Human Machine Interface logic &  flow" document |
| 1100 |  |  |
| 1101 |  | IF TLM receives "IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk" set to " 10  " |
| 1102 |  | THEN TLM sall: |
| 1103 |  | activate and display the  Popup related to “Brake Service To exit Service Mode, vehicle must not be in motion.”  like described in the "Human Machine Interface logic &  flow" document |
| 1104 |  |  |
| 1105 |  | IF TLM receives "IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk" set to " 11  " |
| 1106 |  | THEN TLM sall: |
| 1107 |  | activate and display the Popup related to " once the Service Mode exit process is complete"  like described in the "Human Machine Interface logic &  flow" document |
| 1108 |  |  |
| 1109 |  | IF        "IPC_VEHICLE_SETUP2.EPB_MaintenanceMode" B CAN signal  is equal  to "On"   |
| 1110 |  | THEN |
| 1111 |  | IF  "STATUS_CCAN3.VehicleSpeedVSOSig" B CAN signal changes from a value  ≤  "V_Car_Moving" to a value  >  "V_Car_Moving" OR  in case of  transition from "Ignition Off" to "Inigtion On" |
| 1112 |  |  |
| 1113 |  | THEN  TLM shall activate and display the PopUp related to " the user selected yes to exiting service mode and the first step is to step on the brake pedal" like described in the "Human Machine Interface logic &  flow" document. |
| 1114 |  |  |
| 1115 |  | WHEN TLM receives "IPC_VEHICLE_SETUP2.EPB_MaintenanceMode" message   |
| 1116 |  | THEN TLM shall update the EPB Maintenance Mode information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal |
| 1117 |  | Fore more information about the Popup visualizzation for the EPB Maintenance Mode settings, refer to  "Service Mode Pop-up Messages " session of the "Human Machine Interface logic &  flow" document |
