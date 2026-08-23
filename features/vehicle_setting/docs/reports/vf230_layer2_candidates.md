# VF230 Layer 2 候選 —— spec 目次 ∩ 037 分組（canon §4.1.2）

**未鎖。** 本表為候選，`framework.md` 未動（61 包 §4.2）。
Part 1 之 Layer 1/2/3 於本輪未觸及。

## 0. 量測條件

- spec：`C-VF230_V1_R5_PDT27.doc` —— **實為 OOXML**（`Microsoft Word 2007+`），
  python-docx 直讀，無需轉檔（推翻 61 包 §6 第 2 項之前提）
- spec Heading 段落：**192**（層級分布 {1: 1, 2: 17, 3: 34, 4: 11, 5: 99, 6: 30}）
- 037 分組來源：`data/vf230_leaves.tsv`（619 leaf，11 份分報告）
- 037 之 Requirement Title 簇：**106**，涵蓋 **619** leaf
- 交集判準：Title 與 Heading 正規化（小寫、非英數字摺空白）後**全等**；
  不做子字串容錯

## 1. Layer 1

spec 之 L1 Heading 逐字：`Vehicle Setup Management [VF230_V1_]`

依 canon §4.1.2 步驟 1 與 R-C6（feature 身分取自 spec 模組名），
Layer 1 候選為 **Vehicle Setup Management**。
**此與 W-104（Test Group 判定）為同一停下項，本層不決。**

## 2. 交集結果：exact **104** ／ 無對應 **2**

### 2.1 無對應之簇（spec 目次查無同名章）

| 037 Requirement Title | leaf | 分報告族群 |
|---|---:|---|
| `E-Save` | 6 | 6 Aux Switches, SWITCH 1 Power Mode and E-Save features |
| `CHMSL CAMERA DYNAMIC CENTERLINE` | 5 | STLA_Trailer_Name - Max_Power_Level_Report |

→ 此三簇之 Layer 2 歸屬**無 spec 依據**，登記為待判。

## 3. 粒度 A（粗）—— spec L4 章 **（交集法於 VF230 失效）**

候選數 **2**。spec 之 99 個 L5 章中 **95** 掛於同一 L4 章
（`LTM or ETM Algorithm Requirements`），致本粒度塌成 97.4% ／ 2.6% 之二分。
canon §4.1.2 步驟 2 之交集法在此**不產生可用之 Layer 2**。

| spec L4 章 | 簇數 | leaf | 佔比 |
|---|---:|---:|---:|
| LTM or ETM Algorithm Requirements | 104 | 608 | 98.2% |
| (無對應章) | 2 | 11 | 1.8% |

### 3.1 同名章歧義（spec 目次多處同名）

| 037 Requirement Title | leaf | 同名章數 | 分屬 L4 章 |
|---|---:|---:|---|
| `Charge Power Level` | 8 | 2 | IPC Algorithim Requirements for Remote Operation／LTM or ETM Algorithm Requirements |
| `Speed Unit` | 4 | 2 | IPC Algorithm Requirements／LTM or ETM Algorithm Requirements |

→ 上表各簇之 spec 歸屬**未定**；表 §5 所列之 L4 章為首見者，僅供對照，不構成裁定。


## 4. 粒度 B（中）—— spec L3 章

候選數 **2**（同 §3 之塌陷）。

| spec L3 章 | 簇數 | leaf | 佔比 |
|---|---:|---:|---:|
| LTM or ETM Vehicle Setup Management | 104 | 608 | 98.2% |
| (無對應章) | 2 | 11 | 1.8% |

## 4b. 粒度 D（替代切分源）—— 037 之 11 份分報告族群

spec 目次既不產生可用粒度，另備此源：037 之分檔本身即為
上游 SWE.1 作者之分群（canon §4.1.2 步驟 2 之第二個來源）。

候選數 **11**。

| 037 分報告族群 | Title 簇數 | leaf | 佔比 |
|---|---:|---:|---:|
| STLA_Trailer_Name - Max_Power_Level_Report | 12 | 131 | 21.2% |
| Blind Spot Alert_Passive Entry_Phone Repetition_Park Sense_features | 19 | 99 | 16.0% |
| Time_Date_Autodoor_Camera_features | 15 | 79 | 12.8% |
| 6 Aux Switches, SWITCH 1 Power Mode and E-Save features | 22 | 64 | 10.3% |
| STLA_Illuminated_Approach - Trailer_Number_Report | 9 | 57 | 9.2% |
| STLA_Suspension_Service_Mode - Headlights_with_Wipers Features_Report | 10 | 52 | 8.4% |
| Cornering Lights_lane_features | 9 | 49 | 7.9% |
| STLA_Suspension_Flash_Lights_With_Lower - SWITCH 4_Power_Mode Features_Report | 9 | 35 | 5.7% |
| STLA_SWITCH_1_Type - SWITCH 4 Hold_Last_State Features_Report | 8 | 24 | 3.9% |
| Pressure_Unit , Power_Unit And Torque_Unit features | 3 | 17 | 2.7% |
| Daytime_Running_Light And Headlights_Off_Delay features^ | 2 | 12 | 1.9% |

分布：最小 12 leaf、最大 131 leaf，中位約 52。
較 §3 之二分均勻，較 §5 之 106 簇為粗。**本層建議以此為起點，惟不決。**


## 5. 粒度 C（細）—— 037 Title 簇逐一為 Layer 2

候選數 **106**。canon §4.1.3「Too granular」：
Test Set 欄將近乎 TC ID 欄之複本，索引價值歸零。**不建議**。

| # | 037 Requirement Title | leaf | 交集 | spec L4 章 |
|---:|---|---:|---|---|
| 1 | Traffic Sign Assist Offset - NAFTA Setting | 33 | exact | LTM or ETM Algorithm Requirements |
| 2 | Traffic Sign Assist Offset - non-NAFTA Setting | 23 | exact | LTM or ETM Algorithm Requirements |
| 3 | Trailer Name | 22 | exact | LTM or ETM Algorithm Requirements |
| 4 | Trailer Brake Type | 13 | exact | LTM or ETM Algorithm Requirements |
| 5 | Charge Power Level | 8 | exact | LTM or ETM Algorithm Requirements |
| 6 | Trailer Number | 8 | exact | LTM or ETM Algorithm Requirements |
| 7 | Headlights Off Delay | 7 | exact | LTM or ETM Algorithm Requirements |
| 8 | Time and Date Settings | 7 | exact | LTM or ETM Algorithm Requirements |
| 9 | Consumption Unit | 7 | exact | LTM or ETM Algorithm Requirements |
| 10 | Illuminated Approach | 7 | exact | LTM or ETM Algorithm Requirements |
| 11 | Engine Off Power Delay | 7 | exact | LTM or ETM Algorithm Requirements |
| 12 | Blind Spot Alert | 6 | exact | LTM or ETM Algorithm Requirements |
| 13 | Horn With Lock | 6 | exact | LTM or ETM Algorithm Requirements |
| 14 | Park Sense Rear Volume | 6 | exact | LTM or ETM Algorithm Requirements |
| 15 | Park Sense Front Volume | 6 | exact | LTM or ETM Algorithm Requirements |
| 16 | Auto On Driver Comfort - 3 Option | 6 | exact | LTM or ETM Algorithm Requirements |
| 17 | Lane Sense Warning | 6 | exact | LTM or ETM Algorithm Requirements |
| 18 | Lane Sense Strength | 6 | exact | LTM or ETM Algorithm Requirements |
| 19 | Forward Collision Warning | 6 | exact | LTM or ETM Algorithm Requirements |
| 20 | Forward Collision Warning Sensitivity | 6 | exact | LTM or ETM Algorithm Requirements |
| 21 | Pressure Unit | 6 | exact | LTM or ETM Algorithm Requirements |
| 22 | Power Unit | 6 | exact | LTM or ETM Algorithm Requirements |
| 23 | Unit Energy | 6 | exact | LTM or ETM Algorithm Requirements |
| 24 | Turn Signal Activated Blind Spot Camera View with Trailer Option | 6 | exact | LTM or ETM Algorithm Requirements |
| 25 | Suspension Auto Entry or Exit | 6 | exact | LTM or ETM Algorithm Requirements |
| 26 | SWITCH 1 Power Mode | 6 | exact | LTM or ETM Algorithm Requirements |
| 27 | SWITCH 2 Power Mode | 6 | exact | LTM or ETM Algorithm Requirements |
| 28 | SWITCH 4 Power Mode | 6 | exact | LTM or ETM Algorithm Requirements |
| 29 | SWITCH 1 Type | 6 | exact | LTM or ETM Algorithm Requirements |
| 30 | SWITCH 2 Type | 6 | exact | LTM or ETM Algorithm Requirements |
| 31 | SWITCH 4 Type | 6 | exact | LTM or ETM Algorithm Requirements |
| 32 | SWITCH 1 Hold Last State | 6 | exact | LTM or ETM Algorithm Requirements |
| 33 | SWITCH 4 Hold Last State | 6 | exact | LTM or ETM Algorithm Requirements |
| 34 | E-Save | 6 | none | (無對應章) |
| 35 | Power Liftgate/Tailgate Alert | 6 | exact | LTM or ETM Algorithm Requirements |
| 36 | Power Tailgate | 6 | exact | LTM or ETM Algorithm Requirements |
| 37 | Traffic Sign Warning | 6 | exact | LTM or ETM Algorithm Requirements |
| 38 | New Speed Zone Indication | 6 | exact | LTM or ETM Algorithm Requirements |
| 39 | Suspension Default Ride Height | 6 | exact | LTM or ETM Algorithm Requirements |
| 40 | Enhanced Display Synchronization | 6 | exact | LTM or ETM Algorithm Requirements |
| 41 | Passive Entry | 5 | exact | LTM or ETM Algorithm Requirements |
| 42 | Remote Door Unlock | 5 | exact | LTM or ETM Algorithm Requirements |
| 43 | Auto Park Brake | 5 | exact | LTM or ETM Algorithm Requirements |
| 44 | Horn With Remote Start | 5 | exact | LTM or ETM Algorithm Requirements |
| 45 | Auto Unlock on Exit | 5 | exact | LTM or ETM Algorithm Requirements |
| 46 | Flash Light With Lock | 5 | exact | LTM or ETM Algorithm Requirements |
| 47 | Navigation Turn by Turn | 5 | exact | LTM or ETM Algorithm Requirements |
| 48 | Phone Repetition | 5 | exact | LTM or ETM Algorithm Requirements |
| 49 | Auto High Beam | 5 | exact | LTM or ETM Algorithm Requirements |
| 50 | RKE Linked to Memory | 5 | exact | LTM or ETM Algorithm Requirements |
| 51 | Auto On Driver Comfort - 2 Option | 5 | exact | LTM or ETM Algorithm Requirements |
| 52 | Rearview Camera Delay | 5 | exact | LTM or ETM Algorithm Requirements |
| 53 | Rearview Camera Dynamic Guidelines | 5 | exact | LTM or ETM Algorithm Requirements |
| 54 | Cornering Lights | 5 | exact | LTM or ETM Algorithm Requirements |
| 55 | Greeting Lights | 5 | exact | LTM or ETM Algorithm Requirements |
| 56 | Signature Lighting | 5 | exact | LTM or ETM Algorithm Requirements |
| 57 | Pedestrian Emergency Braking or Warning & Active Braking | 5 | exact | LTM or ETM Algorithm Requirements |
| 58 | Rain Sensing Wipers | 5 | exact | LTM or ETM Algorithm Requirements |
| 59 | Daytime Running Lights | 5 | exact | LTM or ETM Algorithm Requirements |
| 60 | Torque Unit | 5 | exact | LTM or ETM Algorithm Requirements |
| 61 | Auto Door Locks | 5 | exact | LTM or ETM Algorithm Requirements |
| 62 | Temperature Unit | 5 | exact | LTM or ETM Algorithm Requirements |
| 63 | Surround View Camera Delay | 5 | exact | LTM or ETM Algorithm Requirements |
| 64 | Surround View Camera Guidelines | 5 | exact | LTM or ETM Algorithm Requirements |
| 65 | Turn Signal Activated Blind Spot Camera View | 5 | exact | LTM or ETM Algorithm Requirements |
| 66 | ParkSense Based Camera Activation | 5 | exact | LTM or ETM Algorithm Requirements |
| 67 | Park Sense | 5 | exact | LTM or ETM Algorithm Requirements |
| 68 | SWITCH 3 Power Mode | 5 | exact | LTM or ETM Algorithm Requirements |
| 69 | SWITCH 3 Type | 5 | exact | LTM or ETM Algorithm Requirements |
| 70 | SWITCH 2 Hold Last State | 5 | exact | LTM or ETM Algorithm Requirements |
| 71 | SWITCH 3 Hold Last State | 5 | exact | LTM or ETM Algorithm Requirements |
| 72 | Rear Guidance Lighting with Approach | 5 | exact | LTM or ETM Algorithm Requirements |
| 73 | Rear Guidance Light Status | 5 | exact | LTM or ETM Algorithm Requirements |
| 74 | Paddle Shifter | 5 | exact | LTM or ETM Algorithm Requirements |
| 75 | Rear Seat Reminder | 5 | exact | LTM or ETM Algorithm Requirements |
| 76 | Suspension Flash Lights With Lower | 5 | exact | LTM or ETM Algorithm Requirements |
| 77 | Suspension Sound Horn With Lower | 5 | exact | LTM or ETM Algorithm Requirements |
| 78 | Rear Guidance Lights with\nCargo Lights | 5 | exact | LTM or ETM Algorithm Requirements |
| 79 | Suspension Service Mode | 5 | exact | LTM or ETM Algorithm Requirements |
| 80 | Suspension Display Messages | 5 | exact | LTM or ETM Algorithm Requirements |
| 81 | Tilt Mirror in Reverse | 5 | exact | LTM or ETM Algorithm Requirements |
| 82 | Tire Fill Alert | 5 | exact | LTM or ETM Algorithm Requirements |
| 83 | Ready to Drive Pop-Up | 5 | exact | LTM or ETM Algorithm Requirements |
| 84 | Auto Fold Mirrors | 5 | exact | LTM or ETM Algorithm Requirements |
| 85 | Driver Easy Exit Seat | 5 | exact | LTM or ETM Algorithm Requirements |
| 86 | Hill Start Assist | 5 | exact | LTM or ETM Algorithm Requirements |
| 87 | Headlights with Wipers | 5 | exact | LTM or ETM Algorithm Requirements |
| 88 | Automatic Trailer Light Check | 5 | exact | LTM or ETM Algorithm Requirements |
| 89 | Blind Spot with Trailer Detection | 5 | exact | LTM or ETM Algorithm Requirements |
| 90 | Power Side Step | 5 | exact | LTM or ETM Algorithm Requirements |
| 91 | Warnings for Low Fuel Inverter Shutdown - Visual Warning | 5 | exact | LTM or ETM Algorithm Requirements |
| 92 | Warnings for Low Fuel Inverter Shutdown - Audible Warning | 5 | exact | LTM or ETM Algorithm Requirements |
| 93 | CHMSL CAMERA DYNAMIC CENTERLINE | 5 | none | (無對應章) |
| 94 | Language | 4 | exact | LTM or ETM Algorithm Requirements |
| 95 | Hour Mode | 4 | exact | LTM or ETM Algorithm Requirements |
| 96 | Distance Unit | 4 | exact | LTM or ETM Algorithm Requirements |
| 97 | Speed Unit | 4 | exact | LTM or ETM Algorithm Requirements |
| 98 | Max Power Level | 4 | exact | LTM or ETM Algorithm Requirements |
| 99 | SWITCH 5 Power Mode | 3 | exact | LTM or ETM Algorithm Requirements |
| 100 | SWITCH 5 Hold Last State | 3 | exact | LTM or ETM Algorithm Requirements |
| 101 | 6 Aux Switches | 2 | exact | LTM or ETM Algorithm Requirements |
| 102 | SWITCH 6 Power Mode | 2 | exact | LTM or ETM Algorithm Requirements |
| 103 | SWITCH 5 Type | 2 | exact | LTM or ETM Algorithm Requirements |
| 104 | SWITCH 6 Type | 2 | exact | LTM or ETM Algorithm Requirements |
| 105 | SWITCH 6 Hold Last State | 2 | exact | LTM or ETM Algorithm Requirements |
| 106 | 4 AUX Switches | 2 | exact | LTM or ETM Algorithm Requirements |

## 6. spec 目次（逐字）

| lvl | 章名 |
|---:|---|
| 1 | Vehicle Setup Management [VF230_V1_] |
| 2 | 　Vehicle Function Data |
| 3 | 　　Vehicle Function Area |
| 3 | 　　Vehicle Function Group |
| 3 | 　　Vehicle Function Owner |
| 2 | 　Revision notes |
| 2 | 　Introduction |
| 2 | 　Functional Diagram |
| 2 | 　External Interfaces |
| 3 | 　　External Inputs |
| 3 | 　　External Outputs |
| 2 | 　Control Unit |
| 3 | 　　ECU |
| 3 | 　　EMCU |
| 3 | 　　External Device |
| 3 | 　　Additional Component |
| 2 | 　I/O |
| 2 | 　Signal |
| 3 | 　　Hardwire |
| 3 | 　　Internal |
| 3 | 　　B/BH-CAN |
| 3 | 　　C-CAN |
| 3 | 　　LIN |
| 3 | 　　B-CAN2 |
| 3 | 　　FD-CAN3 |
| 3 | 　　PROXI Parameters |
| 3 | 　　C-CAN1 |
| 3 | 　　C-CAN2 |
| 3 | 　　FD-CAN1 |
| 3 | 　　FD-CAN2 |
| 3 | 　　FD-CAN8 |
| 2 | 　Indication |
| 2 | 　Functional Requirements |
| 3 | 　　LTM or ETM Vehicle Setup Management |
| 4 | 　　　LTM or ETM Algorithm Requirements |
| 5 | 　　　　Cornering Lights |
| 5 | 　　　　Greeting Lights |
| 5 | 　　　　Lane Sense Warning |
| 5 | 　　　　Signature Lighting |
| 5 | 　　　　Lane Sense Strength |
| 5 | 　　　　Forward Collision Warning |
| 5 | 　　　　Forward Collision Warning Sensitivity |
| 5 | 　　　　Pedestrian Emergency Braking or Warning & Active Braking |
| 5 | 　　　　Rain Sensing Wipers |
| 5 | 　　　　Time and Date Settings |
| 5 | 　　　　Hour Mode |
| 5 | 　　　　Auto Door Locks |
| 5 | 　　　　Distance Unit |
| 5 | 　　　　Speed Unit |
| 5 | 　　　　Consumption Unit |
| 5 | 　　　　Unit Energy |
| 5 | 　　　　Temperature Unit |
| 5 | 　　　　Pressure Unit |
| 5 | 　　　　Power Unit |
| 5 | 　　　　Torque Unit |
| 5 | 　　　　Language |
| 5 | 　　　　Daytime Running Lights |
| 5 | 　　　　Headlights Off Delay |
| 5 | 　　　　Blind Spot Alert |
| 5 | 　　　　Passive Entry |
| 5 | 　　　　Remote Door Unlock |
| 5 | 　　　　Auto Park Brake |
| 5 | 　　　　Horn With Remote Start |
| 5 | 　　　　Horn With Lock |
| 5 | 　　　　Auto Unlock on Exit |
| 5 | 　　　　Flash Light With Lock |
| 5 | 　　　　Navigation Turn by Turn |
| 5 | 　　　　Phone Repetition |
| 5 | 　　　　Park Sense |
| 5 | 　　　　Park Sense Rear Volume |
| 5 | 　　　　Park Sense Front Volume |
| 5 | 　　　　Auto High Beam |
| 5 | 　　　　RKE Linked to Memory |
| 5 | 　　　　Auto on Driver Comfort - 3 Option |
| 5 | 　　　　Auto on Driver Comfort - 2 Option |
| 5 | 　　　　Rearview Camera Delay |
| 5 | 　　　　Rearview Camera Dynamic Guidelines |
| 5 | 　　　　Auto Fold Mirrors |
| 5 | 　　　　Driver Easy Exit Seat |
| 5 | 　　　　Engine Off Power Delay |
| 5 | 　　　　Hill Start Assist |
| 5 | 　　　　Headlights with Wipers |
| 5 | 　　　　Illuminated Approach |
| 5 | 　　　　Paddle Shifter |
| 5 | 　　　　Power Liftgate/Tailgate Alert |
| 5 | 　　　　Power Tailgate |
| 5 | 　　　　Surround View Camera Delay |
| 5 | 　　　　Surround View Camera Guidelines |
| 5 | 　　　　Suspension Auto Entry or Exit |
| 5 | 　　　　Suspension Service Mode |
| 5 | 　　　　Suspension Display Messages |
| 5 | 　　　　Tilt Mirror in Reverse |
| 5 | 　　　　Tire Fill Alert |
| 5 | 　　　　Ready to Drive Pop-Up |
| 5 | 　　　　4 AUX Switches |
| 6 | 　　　　　SWITCH 1 Power Mode |
| 6 | 　　　　　SWITCH 2 Power Mode |
| 6 | 　　　　　SWITCH 3 Power Mode |
| 6 | 　　　　　SWITCH 4 Power Mode |
| 6 | 　　　　　SWITCH 1 Type |
| 6 | 　　　　　SWITCH 2 Type |
| 6 | 　　　　　SWITCH 3 Type |
| 6 | 　　　　　SWITCH 4 Type |
| 6 | 　　　　　SWITCH 1 Hold Last State |
| 6 | 　　　　　SWITCH 2 Hold Last State |
| 6 | 　　　　　SWITCH 3 Hold Last State |
| 6 | 　　　　　SWITCH 4 Hold Last State |
| 5 | 　　　　6 Aux Switches |
| 6 | 　　　　　SWITCH 1 Power Mode |
| 6 | 　　　　　SWITCH 2 Power Mode |
| 6 | 　　　　　SWITCH 3 Power Mode |
| 6 | 　　　　　SWITCH 4 Power Mode |
| 6 | 　　　　　SWITCH 5 Power Mode |
| 6 | 　　　　　SWITCH 6 Power Mode |
| 6 | 　　　　　SWITCH 1 Type |
| 6 | 　　　　　SWITCH 2 Type |
| 6 | 　　　　　SWITCH 3 Type |
| 6 | 　　　　　SWITCH 4 Type |
| 6 | 　　　　　SWITCH 5 Type |
| 6 | 　　　　　SWITCH 6 Type |
| 6 | 　　　　　SWITCH 1 Hold Last State |
| 6 | 　　　　　SWITCH 2 Hold Last State |
| 6 | 　　　　　SWITCH 3 Hold Last State |
| 6 | 　　　　　SWITCH 4 Hold Last State |
| 6 | 　　　　　SWITCH 5 Hold Last State |
| 6 | 　　　　　SWITCH 6 Hold Last State |
| 5 | 　　　　Traffic Sign Information |
| 5 | 　　　　Forward Facing Camera Guidelines |
| 5 | 　　　　Proximity Wakeup |
| 5 | 　　　　Drowsy Driver Alert |
| 5 | 　　　　Active Lane Management |
| 5 | 　　　　Active Lane Management Strength |
| 5 | 　　　　Traffic Sign Warning |
| 5 | 　　　　New Speed Zone Indication |
| 5 | 　　　　Charge Power Level |
| 5 | 　　　　Rear Seat Reminder |
| 5 | 　　　　Trailer Number |
| 5 | 　　　　Trailer Name |
| 5 | 　　　　Trailer Brake Type |
| 5 | 　　　　Automatic Trailer Light Check |
| 5 | 　　　　Suspension Flash Lights With Lower |
| 5 | 　　　　Suspension Sound Horn With Lower |
| 5 | 　　　　Blind Spot with Trailer Detection |
| 5 | 　　　　Power Side Step |
| 5 | 　　　　Traffic Sign Assist Offset - NAFTA Setting |
| 5 | 　　　　Traffic Sign Assist Offset - non-NAFTA Setting |
| 5 | 　　　　Active ParkSense Mode |
| 5 | 　　　　Active ParkSense Proximity Chimes |
| 5 | 　　　　Rear Guidance Lights with Cargo Lights |
| 5 | 　　　　Turn Signal Activated Blind Spot Camera View |
| 5 | 　　　　Turn Signal Activated Blind Spot Camera View with Trailer Option |
| 5 | 　　　　ParkSense Based Camera Activation |
| 5 | 　　　　Fuel Saver |
| 5 | 　　　　Warnings for Low Fuel Inverter Shutdown - Visual Warning |
| 5 | 　　　　Warnings for Low Fuel Inverter Shutdown - Audible Warning |
| 5 | 　　　　Suspension Default Ride Height |
| 5 | 　　　　Rear Guidance Lighting with Approach |
| 5 | 　　　　Rear Guidance Light Status |
| 5 | 　　　　Enhanced Display Synchronization |
| 5 | 　　　　Max Power Level |
| 3 | 　　Vehicle Setup Management Between IPC and LTM or ETM |
| 3 | 　　IPC Vehicle Setup Management |
| 4 | 　　　IPC Algorithm Requirements |
| 5 | 　　　　Speed Warning Enable or Disable |
| 5 | 　　　　Speed Unit |
| 4 | 　　　IPC Algorithim Requirements for Remote Operation |
| 5 | 　　　　Charge Power Level |
| 5 | 　　　　Max SOC Level |
| 3 | 　　Gateway Management |
| 4 | 　　　BCM Algorithm Requirements |
| 4 | 　　　SGW Algorithm Requirements |
| 2 | 　Non-Customer Functional Modes |
| 3 | 　　Logistics Mode Requirements |
| 4 | 　　　Logistics Mode Functionality Table |
| 4 | 　　　Logistics Mode Functionality Table Description |
| 3 | 　　Other Non-Customer Functional Modes |
| 4 | 　　　Other Non-Customer Functional Modes Table |
| 4 | 　　　Other Non-Customer Functional Modes Table Description |
| 2 | 　Indication Management |
| 2 | 　Diagnosis and Recovery |
| 3 | 　　Diagnosis Table |
| 3 | 　　Diagnosis Table and Recovery Description |
| 3 | 　　Diagnostic Requirements |
| 4 | 　　　IPC Diagnostic Requirements |
| 4 | 　　　BCM Diagnostic Requirements |
| 2 | 　Configuration Parameters |
| 3 | 　　Configuration Parameters Table |
| 2 | 　Wake Up Stay Active |
| 3 | 　　Wake Up and Stay Active Event Table |
| 3 | 　　Wake Up and Stay Active Event Table Description |
| 2 | 　Acronyms and Glossary |
| 2 | 　Reference Documents |
