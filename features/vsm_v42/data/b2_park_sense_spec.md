# pilot 素材 — 規格節 `1.11.1.1.29 PARK SENSE w/o HC.1 and PARK SENSE w/o HC.2`

來源：`sources/extracted/vf665_v42_spec_r6/document_paragraphs.tsv`。
切法：起＝標題段 1202；迄＝下一同級標題段 1244 之前一段。**逐字照錄，含段號。**

| 段號 | 層級 | 內容 |
|---|---|---|
| 1202 | H5 1.11.1.1.29 | PARK SENSE w/o HC.1 and PARK SENSE w/o HC.2 |
| 1203 |  | IF            " CAN node 24 (PAM ) " PROXI parameter  is equal to "Present" |
| 1204 |  | THEN      TLM shall display the "Park Sense Setting "  menu item  and the user can perform setting. |
| 1205 |  | IF              the user sets "Pam_AlertMode_Setting.Req" internal signals to "Sound" |
| 1206 |  | THENTLM shall set "TELEMATIC_VEHICLE_SETUP.PamAlertMode_Req" B-CAN signal equal to "Sound" and sends this signal to IPC |
| 1207 |  |  |
| 1208 |  | IF              the user sets "Pam_AlertMode_Setting.Req" internal signals to "Sound+Display" |
| 1209 |  | THENTLM shall set "TELEMATIC_VEHICLE_SETUP.PamAlertMode_Req" B-CAN signal equal to "Sound+Display" and sends this signal to IPC |
| 1210 |  |  |
| 1211 |  | WHEN TLM receives "IPC_VEHICLE_SETUP.PamAlertMode" message |
| 1212 |  | THEN TLM updates the Park Sense Setting information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal |
| 1213 |  |  |
| 1214 |  | IF            " CAN node 24 (PAM ) " PROXI parameter  is equal to "Present"   |
| 1215 |  | THEN      TLM shall display the "Park Sense Setting "  menu item  and the user can perform setting. |
| 1216 |  | Rear Park Sense Volume/ ParkSense Volume |
| 1217 |  | IF "CAN node 24 (PAM)"  PROXI parameter  is equal to "Present"  AND ( "PAM_Configuration" PROXI parameter is equal to  "Rear" OR "Front And Rear" ) |
| 1218 |  | THEN IPC shall display the "Rear Park Sense Volume" menu item and the user can perform setting. |
| 1219 |  | IF                the user sets "Pam_Chime_Volume_Rear_Setting.Req" internal signals to "Low" |
| 1220 |  | THEN        TLM shall set "TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req" B-CAN signal equal to "Low" and sends this signal to IPC |
| 1221 |  | IF                the user sets "Pam_Chime_Volume_Rear_Setting.Req" internal signals to "Med" |
| 1222 |  | THEN        TLM shall set "TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req" B-CAN signal equal to "Med" and sends this signal to IPC |
| 1223 |  | IF                the user sets "Pam_Chime_Volume_Rear_Setting.Req" internal signals to "High" |
| 1224 |  | THEN        TLM shall set "TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req" B-CAN signal equal to "High" and sends this signal to IPC |
| 1225 |  | WHEN TLM receives "IPC_VEHICLE_SETUP.PamChimeVolumeRear" message |
| 1226 |  | THEN TLM updates the Rear Park Sense Volume information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal |
| 1227 |  | ELSE |
| 1228 |  | THEN TLM shall not display the "Rear Park Sense Volume"  menu item and the user can not perform any setting. |
| 1229 |  | Front Park Sense Volume |
| 1230 |  | IF "CAN node 24 (PAM)"  PROXI parameter  is equal to "Present"  AND  "PAM_Configuration" PROXI parameter is equal to  "Front And Rear"  |
| 1231 |  | THEN IPC shall display the "Front Park Sense Volume" menu item and the user can perform setting. |
| 1232 |  | IF                the user sets "Pam_Chime_Volume_Front_Setting.Req" internal signals to "Low" |
| 1233 |  | THEN        TLM shall set "TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req" B-CAN signal equal to "Low" and sends this signal to IPC |
| 1234 |  | IF                the user sets "Pam_Chime_Volume_Front_Setting.Req" internal signals to "Med" |
| 1235 |  | THEN        TLM shall set "TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req" B-CAN signal equal to "Med" and sends this signal to IPC |
| 1236 |  | IF                the user sets "Pam_Chime_Volume_Front_Setting.Req" internal signals to "High" |
| 1237 |  | THEN        TLM shall set "TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req" B-CAN signal equal to "High" and sends this signal to IPC |
| 1238 |  | WHEN TLM receives "IPC_VEHICLE_SETUP.PamChimeVolumeFront" message |
| 1239 |  | THEN TLM updates the Front Park Sense Volume information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal |
| 1240 |  | ELSE |
| 1241 |  | THEN TLM shall not display the "Front Park Sense Volume"  menu item and the user can not perform any setting. |
| 1242 |  | ELSE |
| 1243 |  | THEN TLM shall not display the "Park Sense Setting ",  "Rear Park Sense Volume"  and "Front Park Sense Volume"  menu items and the user can not perform any setting. |
