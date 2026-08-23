# W-VF25 —— VF230 之 Layer 2 名稱與 Layer 3 對照（提案，待核可）

**`framework.md` 未寫入**（R-VF25：本條只裁粒度，不等於 framework 已鎖）。
**Test Set 名為本層之提案，逐一待 Pei 核可。**

## 0. 錨點（R-VF21 ＋ R-VF28：以內容定錨，不以行號）

| 錨點 | 內容 | 實測 |
|---|---|---|
| 必命中（跨族群） | `SWITCH 1 Type` | 跨 2 族 ✅ |
| 必不命中（不跨族群） | `Pressure Unit` | 不跨族 ✅ |
| 合計 | leaf 總數 | 627（R-VF16）✅ |

## 1. ⚠ 粒度 D 之一項未被預見之後果 —— 12 個簇被邊界對切

**12 個 Title 簇跨兩個分報告族群**，合計 72 leaf。
**每一個皆恰好 3 / 3 對切。**

| 簇 | leaf | 分裂 |
|---|---:|---|
| `SWITCH 1 Hold Last State` | 6 | `Auxiliary Switches` 3／`Switch Type and State` 3 |
| `SWITCH 1 Power Mode` | 6 | `Auxiliary Switches` 3／`Switch Power Mode` 3 |
| `SWITCH 1 Type` | 6 | `Auxiliary Switches` 3／`Switch Type and State` 3 |
| `SWITCH 2 Hold Last State` | 6 | `Auxiliary Switches` 3／`Switch Type and State` 3 |
| `SWITCH 2 Power Mode` | 6 | `Auxiliary Switches` 3／`Switch Power Mode` 3 |
| `SWITCH 2 Type` | 6 | `Auxiliary Switches` 3／`Switch Type and State` 3 |
| `SWITCH 3 Hold Last State` | 6 | `Auxiliary Switches` 3／`Switch Type and State` 3 |
| `SWITCH 3 Power Mode` | 6 | `Auxiliary Switches` 3／`Switch Power Mode` 3 |
| `SWITCH 3 Type` | 6 | `Auxiliary Switches` 3／`Switch Type and State` 3 |
| `SWITCH 4 Hold Last State` | 6 | `Auxiliary Switches` 3／`Switch Type and State` 3 |
| `SWITCH 4 Power Mode` | 6 | `Auxiliary Switches` 3／`Switch Power Mode` 3 |
| `SWITCH 4 Type` | 6 | `Auxiliary Switches` 3／`Switch Type and State` 3 |

→ **依粒度 D 之字面（11 份分報告），`SWITCH 1 Type` 等 12 個功能
會被切成兩個 Test Set 各 3 條。** 一個功能之 TC 分屬兩個 Test Set，
Test Set 欄之索引價值因而受損。

**此為 R-VF25 作成時未有之量測**（V07 §5.3 與 R-VF25 皆以
「12–131 leaf、中位 52」論其均勻度，未測簇之跨界）。

## 2. 提案 A —— 11 個 Test Set（依 R-VF25 字面）

| # | Test Set 名（提案） | leaf | 簇 | 命名依據（該族群最大之三簇） |
|---:|---|---:|---:|---|
| 1 | **Trailer and Signage** | 131 | 12 | `Traffic Sign Assist Offset - NAFTA Setting` 33／`Traffic Sign Assist Offset - non-NAFTA Setting` 23／`Trailer Name` 22 |
| 2 | **Driver Convenience** | 99 | 19 | `Blind Spot Alert` 6／`Horn With Lock` 6／`Park Sense Rear Volume` 6 |
| 3 | **Units and Cameras** | 79 | 15 | `Time and Date Settings` 7／`Consumption Unit` 7／`Unit Energy` 6 |
| 4 | **Auxiliary Switches** | 72 | 22 | `E-Save` 6／`Rear Guidance Lighting with Approach` 5／`Rear Guidance Light Status` 5 |
| 5 | **Approach and Tailgate** | 57 | 9 | `Charge Power Level` 8／`Trailer Number` 8／`Illuminated Approach` 7 |
| 6 | **Suspension and Comfort** | 52 | 10 | `Engine Off Power Delay` 7／`Suspension Service Mode` 5／`Suspension Display Messages` 5 |
| 7 | **Lane and Lighting** | 49 | 9 | `Lane Sense Warning` 6／`Lane Sense Strength` 6／`Forward Collision Warning` 6 |
| 8 | **Switch Power Mode** | 35 | 9 | `Suspension Default Ride Height` 6／`Suspension Flash Lights With Lower` 5／`Suspension Sound Horn With Lower` 5 |
| 9 | **Switch Type and State** | 24 | 8 | `SWITCH 1 Type` 3／`SWITCH 2 Type` 3／`SWITCH 3 Type` 3 |
| 10 | **Measurement Units** | 17 | 3 | `Pressure Unit` 6／`Power Unit` 6／`Torque Unit` 5 |
| 11 | **Daytime Lighting** | 12 | 2 | `Headlights Off Delay` 7／`Daytime Running Lights` 5 |

**合計 627**（自各族群重算）。

**命名之合規性（canon §4.2）**：11 個名皆為 1–3 字名詞片語、
無 `Vehicle Setting` 前綴（R-VF25 配套 2）、無括號標籤、
無 `Report`／`features`／`^`／` - ` 等檔名殘留（配套 1）。

**須具名之異質性**：`Trailer and Signage`(131)／`Driver Convenience`(99)／
`Approach and Tailgate`(57) 三者之內容異質度較高 ——
其族群內最大簇僅佔 25%／6%／14%。**名只能取其較大之主題，
無法涵蓋全部。** 若 Pei 認為不可接受，須改粒度而非改名。

## 3. 提案 B —— 9 個 Test Set（三個 SWITCH 族群合併）

將 `Auxiliary Switches`(72)＋`Switch Type and State`(24)＋
`Switch Power Mode`(35) 併為單一 Test Set **`Auxiliary Switches`**（131 leaf）。

**合併後跨族群之簇 = 0**（實測）。

| # | Test Set | leaf |
|---:|---|---:|
| 1 | **Auxiliary Switches**（合併） | 131 |
| 2 | Trailer and Signage | 131 |
| 3 | Driver Convenience | 99 |
| 4 | Units and Cameras | 79 |
| 5 | Approach and Tailgate | 57 |
| 6 | Suspension and Comfort | 52 |
| 7 | Lane and Lighting | 49 |
| 8 | Measurement Units | 17 |
| 9 | Daytime Lighting | 12 |

**合計 627**。

**代價**：偏離 R-VF25 之「11 份分報告族群」字面；
`Auxiliary Switches` 成為最大 Test Set（131，與 `Trailer and Signage` 並列）。
**收益**：無功能被邊界對切。

**本層不擇一**（R-VF25 §1 令逐一列出待核）。

## 4. canon §4.1.3 兩項反面型態

| 型態 | 提案 A | 提案 B |
|---|---|---|
| **過細**（Test Set 欄近乎 TC ID 欄之複本） | 11 set／627 leaf，平均 57 → **否** | 9 set，平均 70 → **否** |
| **過粗**（出現 `Misc`／`General`／`Unclassified` 收容簇） | 無此類名 → **否** | 無 → **否** |

（對照：106 簇之粒度平均 5.9 leaf，**屬過細**，R-VF25 已排除。）

## 5. Layer 3 對照（各 Test Set → spec 之自有章名）

**不自創標籤**（R-VF25 配套 3）。章名取自 spec 目次之逐字，
其對應以 W-VF7 複驗後之交集（exact 104 ／ 無對應 2）為準。

### Trailer and Signage（131 leaf，11 個 spec 章）

- `Automatic Trailer Light Check`／`Blind Spot with Trailer Detection`／`Enhanced Display Synchronization`／`Max Power Level`／`Power Side Step`／`Traffic Sign Assist Offset - NAFTA Setting`／`Traffic Sign Assist Offset - non-NAFTA Setting`／`Trailer Brake Type`／`Trailer Name`／`Warnings for Low Fuel Inverter Shutdown - Audible Warning`／`Warnings for Low Fuel Inverter Shutdown - Visual Warning`

### Driver Convenience（99 leaf，19 個 spec 章）

- `Auto High Beam`／`Auto Park Brake`／`Auto Unlock on Exit`／`Auto on Driver Comfort - 2 Option`／`Auto on Driver Comfort - 3 Option`／`Blind Spot Alert`／`Flash Light With Lock`／`Horn With Lock`／`Horn With Remote Start`／`Language`／`Navigation Turn by Turn`／`Park Sense Front Volume`／`Park Sense Rear Volume`／`Passive Entry`／`Phone Repetition`／`RKE Linked to Memory`／`Rearview Camera Delay`／`Rearview Camera Dynamic Guidelines`／`Remote Door Unlock`

### Units and Cameras（79 leaf，15 個 spec 章）

- `Auto Door Locks`／`Consumption Unit`／`Distance Unit`／`Hour Mode`／`Park Sense`／`ParkSense Based Camera Activation`／`Speed Unit`／`Surround View Camera Delay`／`Surround View Camera Guidelines`／`Suspension Auto Entry or Exit`／`Temperature Unit`／`Time and Date Settings`／`Turn Signal Activated Blind Spot Camera View`／`Turn Signal Activated Blind Spot Camera View with Trailer Option`／`Unit Energy`

### Auxiliary Switches（72 leaf，21 個 spec 章）

- `6 Aux Switches`／`Rear Guidance Light Status`／`Rear Guidance Lighting with Approach`／`SWITCH 1 Hold Last State`／`SWITCH 1 Power Mode`／`SWITCH 1 Type`／`SWITCH 2 Hold Last State`／`SWITCH 2 Power Mode`／`SWITCH 2 Type`／`SWITCH 3 Hold Last State`／`SWITCH 3 Power Mode`／`SWITCH 3 Type`／`SWITCH 4 Hold Last State`／`SWITCH 4 Power Mode`／`SWITCH 4 Type`／`SWITCH 5 Hold Last State`／`SWITCH 5 Power Mode`／`SWITCH 5 Type`／`SWITCH 6 Hold Last State`／`SWITCH 6 Power Mode`／`SWITCH 6 Type`

### Approach and Tailgate（57 leaf，9 個 spec 章）

- `Charge Power Level`／`Illuminated Approach`／`New Speed Zone Indication`／`Paddle Shifter`／`Power Liftgate/Tailgate Alert`／`Power Tailgate`／`Rear Seat Reminder`／`Traffic Sign Warning`／`Trailer Number`

### Suspension and Comfort（52 leaf，10 個 spec 章）

- `Auto Fold Mirrors`／`Driver Easy Exit Seat`／`Engine Off Power Delay`／`Headlights with Wipers`／`Hill Start Assist`／`Ready to Drive Pop-Up`／`Suspension Display Messages`／`Suspension Service Mode`／`Tilt Mirror in Reverse`／`Tire Fill Alert`

### Lane and Lighting（49 leaf，9 個 spec 章）

- `Cornering Lights`／`Forward Collision Warning`／`Forward Collision Warning Sensitivity`／`Greeting Lights`／`Lane Sense Strength`／`Lane Sense Warning`／`Pedestrian Emergency Braking or Warning & Active Braking`／`Rain Sensing Wipers`／`Signature Lighting`

### Switch Power Mode（35 leaf，9 個 spec 章）

- `4 AUX Switches`／`Rear Guidance Lights with Cargo Lights`／`SWITCH 1 Power Mode`／`SWITCH 2 Power Mode`／`SWITCH 3 Power Mode`／`SWITCH 4 Power Mode`／`Suspension Default Ride Height`／`Suspension Flash Lights With Lower`／`Suspension Sound Horn With Lower`

### Switch Type and State（24 leaf，8 個 spec 章）

- `SWITCH 1 Hold Last State`／`SWITCH 1 Type`／`SWITCH 2 Hold Last State`／`SWITCH 2 Type`／`SWITCH 3 Hold Last State`／`SWITCH 3 Type`／`SWITCH 4 Hold Last State`／`SWITCH 4 Type`

### Measurement Units（17 leaf，3 個 spec 章）

- `Power Unit`／`Pressure Unit`／`Torque Unit`

### Daytime Lighting（12 leaf，2 個 spec 章）

- `Daytime Running Lights`／`Headlights Off Delay`

## 6. 無 spec 對應之 2 簇（W-VF7 複驗後之真缺口）

| 簇 | leaf | 所屬 Test Set |
|---|---:|---|
| `E-Save` | 6 | Auxiliary Switches |
| `CHMSL CAMERA DYNAMIC CENTERLINE` | 5 | Trailer and Signage |

**其 Layer 3 無 spec 章可掛。** 依 R-VF25 配套 3「不得自創標籤」，
本層**不為其造章名**。**處置待裁**：(a) 掛於其 Test Set 而 Layer 3 留空；
(b) 待 spec 修訂後補；(c) 另循 DR 向上游確認其章節歸屬。

## 7. framework.md 之現況

**未寫入、未鎖。** R-VF25 之鎖定條件為「Layer 2 名稱表與 Layer 3
對照表齊備並經 Pei 核可」。本檔為該二表之提案，**核可後方得寫入**。
Part 1 之既有 Layer 1／2／3 本輪未觸及。

