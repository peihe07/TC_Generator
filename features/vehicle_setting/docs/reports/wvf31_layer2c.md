# W-VF31 —— Layer 2 提案 C 之表（R-VF36）

**逐簇過規則，不批次移動**（R-VF36）。合計自各 Test Set 重算。

## 0. 錨點（R-VF21 ＋ R-VF28：以內容定錨）

| 錨點 | 簇 | 實測 |
|---|---|---|
| 必移動 | `Suspension Default Ride Height` | `Switch Power Mode` → `Suspension and Comfort`（相交：suspension）✅ |
| 必不移動 | `Pressure Unit` | 留於 `Measurement Units` ✅ |
| **鑑別** | `Power Unit`（量測單位，與 `Switch Power Mode` 僅共用泛用詞 `power`） | **移至 `Switch Power Mode` —— 錨點不符，規則以單一泛用詞誤配** ❌ |
| 合計 | — | 627（R-VF16）✅ |

## 1. 主題詞之操作型定義（R-VF36：須可檢查，不得臨場裁量）

```
主題詞(s) = { 小寫切詞(s) } − 停用詞 − 純數字
停用詞 = and, with, or, the, of, for, a, to, in, on, &, -,
         features, report, setting, settings
```
簇之主題詞取自其 **spec 章名**；無 spec 對應者（R-VF34 之 2 簇）
以**簇名**代之，並於下表標記。

## 2. 移動清單（33 筆）

| 簇 | leaf | 原 Test Set | 新 Test Set | spec 章名 | 相交之主題詞 |
|---|---:|---|---|---|---|
| `Charge Power Level` | 8 | Approach and Tailgate | **Switch Power Mode** | `Charge Power Level` | power |
| `Trailer Number` | 8 | Approach and Tailgate | **Trailer and Signage** | `Trailer Number` | trailer |
| `Engine Off Power Delay` | 7 | Suspension and Comfort | **Switch Power Mode** | `Engine Off Power Delay` | power |
| `Power Unit` | 6 | Measurement Units | **Switch Power Mode** | `Power Unit` | power |
| `Suspension Auto Entry or Exit` | 6 | Units and Cameras | **Suspension and Comfort** | `Suspension Auto Entry or Exit` | suspension |
| `Suspension Default Ride Height` | 6 | Switch Power Mode | **Suspension and Comfort** | `Suspension Default Ride Height` | suspension |
| `Turn Signal Activated Blind Spot Camera View with Trailer Option` | 6 | Units and Cameras | **Trailer and Signage** | `Turn Signal Activated Blind Spot Camera View with Trailer Option` | trailer |
| `Driver Easy Exit Seat` | 5 | Suspension and Comfort | **Driver Convenience** | `Driver Easy Exit Seat` | driver |
| `Power Side Step` | 5 | Trailer and Signage | **Switch Power Mode** | `Power Side Step` | power |
| `Rear Guidance Lighting with Approach` | 5 | Auxiliary Switches | **Daytime Lighting** | `Rear Guidance Lighting with Approach` | lighting |
| `Suspension Flash Lights With Lower` | 5 | Switch Power Mode | **Suspension and Comfort** | `Suspension Flash Lights With Lower` | suspension |
| `Suspension Sound Horn With Lower` | 5 | Switch Power Mode | **Suspension and Comfort** | `Suspension Sound Horn With Lower` | suspension |
| `Hour Mode` | 4 | Units and Cameras | **Switch Power Mode** | `Hour Mode` | mode |
| `Max Power Level` | 4 | Trailer and Signage | **Switch Power Mode** | `Max Power Level` | power |
| `SWITCH 1 Hold Last State` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 1 Hold Last State` | state／switch |
| `SWITCH 1 Power Mode` | 3 | Auxiliary Switches | **Switch Power Mode** | `SWITCH 1 Power Mode` | mode／power／switch |
| `SWITCH 1 Type` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 1 Type` | switch／type |
| `SWITCH 2 Hold Last State` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 2 Hold Last State` | state／switch |
| `SWITCH 2 Power Mode` | 3 | Auxiliary Switches | **Switch Power Mode** | `SWITCH 2 Power Mode` | mode／power／switch |
| `SWITCH 2 Type` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 2 Type` | switch／type |
| `SWITCH 3 Hold Last State` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 3 Hold Last State` | state／switch |
| `SWITCH 3 Power Mode` | 3 | Auxiliary Switches | **Switch Power Mode** | `SWITCH 3 Power Mode` | mode／power／switch |
| `SWITCH 3 Type` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 3 Type` | switch／type |
| `SWITCH 4 Hold Last State` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 4 Hold Last State` | state／switch |
| `SWITCH 4 Power Mode` | 3 | Auxiliary Switches | **Switch Power Mode** | `SWITCH 4 Power Mode` | mode／power／switch |
| `SWITCH 4 Type` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 4 Type` | switch／type |
| `SWITCH 5 Hold Last State` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 5 Hold Last State` | state／switch |
| `SWITCH 5 Power Mode` | 3 | Auxiliary Switches | **Switch Power Mode** | `SWITCH 5 Power Mode` | mode／power／switch |
| `SWITCH 5 Type` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 5 Type` | switch／type |
| `SWITCH 6 Hold Last State` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 6 Hold Last State` | state／switch |
| `SWITCH 6 Power Mode` | 3 | Auxiliary Switches | **Switch Power Mode** | `SWITCH 6 Power Mode` | mode／power／switch |
| `SWITCH 6 Type` | 3 | Auxiliary Switches | **Switch Type and State** | `SWITCH 6 Type` | switch／type |
| `4 AUX Switches` | 2 | Switch Power Mode | **Auxiliary Switches** | `4 AUX Switches` | switches |

## 3. 過規則而不移動（85 筆）

**R-VF36 令「過規則而不移動者亦須列出並具名理由」。**

| 簇 | leaf | Test Set | 不移動之理由 |
|---|---:|---|---|
| `Traffic Sign Assist Offset - NAFTA Setting` | 33 | Trailer and Signage | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Traffic Sign Assist Offset - non-NAFTA Setting` | 23 | Trailer and Signage | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Trailer Name` | 22 | Trailer and Signage | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：trailer |
| `Trailer Brake Type` | 13 | Trailer and Signage | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：trailer |
| `Consumption Unit` | 7 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Headlights Off Delay` | 7 | Daytime Lighting | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Illuminated Approach` | 7 | Approach and Tailgate | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：approach |
| `Time and Date Settings` | 7 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Auto On Driver Comfort - 3 Option` | 6 | Driver Convenience | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：driver |
| `Blind Spot Alert` | 6 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `E-Save` | 6 | Auxiliary Switches | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Enhanced Display Synchronization` | 6 | Trailer and Signage | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Forward Collision Warning` | 6 | Lane and Lighting | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Forward Collision Warning Sensitivity` | 6 | Lane and Lighting | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Horn With Lock` | 6 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Lane Sense Strength` | 6 | Lane and Lighting | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：lane |
| `Lane Sense Warning` | 6 | Lane and Lighting | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：lane |
| `New Speed Zone Indication` | 6 | Approach and Tailgate | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Park Sense Front Volume` | 6 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Park Sense Rear Volume` | 6 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Power Liftgate/Tailgate Alert` | 6 | Approach and Tailgate | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：tailgate |
| `Power Tailgate` | 6 | Approach and Tailgate | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：tailgate |
| `Pressure Unit` | 6 | Measurement Units | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Traffic Sign Warning` | 6 | Approach and Tailgate | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Unit Energy` | 6 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Auto Door Locks` | 5 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Auto Fold Mirrors` | 5 | Suspension and Comfort | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Auto High Beam` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Auto On Driver Comfort - 2 Option` | 5 | Driver Convenience | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：driver |
| `Auto Park Brake` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Auto Unlock on Exit` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Automatic Trailer Light Check` | 5 | Trailer and Signage | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：trailer |
| `Blind Spot with Trailer Detection` | 5 | Trailer and Signage | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：trailer |
| `CHMSL CAMERA DYNAMIC CENTERLINE` | 5 | Trailer and Signage | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Cornering Lights` | 5 | Lane and Lighting | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Daytime Running Lights` | 5 | Daytime Lighting | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：daytime |
| `Flash Light With Lock` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Greeting Lights` | 5 | Lane and Lighting | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Headlights with Wipers` | 5 | Suspension and Comfort | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Hill Start Assist` | 5 | Suspension and Comfort | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Horn With Remote Start` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Navigation Turn by Turn` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Paddle Shifter` | 5 | Approach and Tailgate | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Park Sense` | 5 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `ParkSense Based Camera Activation` | 5 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Passive Entry` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Pedestrian Emergency Braking or Warning & Active Braking` | 5 | Lane and Lighting | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Phone Repetition` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `RKE Linked to Memory` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Rain Sensing Wipers` | 5 | Lane and Lighting | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Ready to Drive Pop-Up` | 5 | Suspension and Comfort | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Rear Guidance Light Status` | 5 | Auxiliary Switches | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Rear Guidance Lights with\nCargo Lights` | 5 | Switch Power Mode | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Rear Seat Reminder` | 5 | Approach and Tailgate | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Rearview Camera Delay` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Rearview Camera Dynamic Guidelines` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Remote Door Unlock` | 5 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Signature Lighting` | 5 | Lane and Lighting | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：lighting |
| `Surround View Camera Delay` | 5 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Surround View Camera Guidelines` | 5 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Suspension Display Messages` | 5 | Suspension and Comfort | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：suspension |
| `Suspension Service Mode` | 5 | Suspension and Comfort | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：suspension |
| `Temperature Unit` | 5 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Tilt Mirror in Reverse` | 5 | Suspension and Comfort | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Tire Fill Alert` | 5 | Suspension and Comfort | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Torque Unit` | 5 | Measurement Units | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Turn Signal Activated Blind Spot Camera View` | 5 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Warnings for Low Fuel Inverter Shutdown - Audible Warning` | 5 | Trailer and Signage | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Warnings for Low Fuel Inverter Shutdown - Visual Warning` | 5 | Trailer and Signage | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Distance Unit` | 4 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Language` | 4 | Driver Convenience | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `Speed Unit` | 4 | Units and Cameras | (ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，依 R-VF36 留原處，不得新設 |
| `SWITCH 1 Hold Last State` | 3 | Switch Type and State | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：state／switch |
| `SWITCH 1 Power Mode` | 3 | Switch Power Mode | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：mode／power／switch |
| `SWITCH 1 Type` | 3 | Switch Type and State | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：switch／type |
| `SWITCH 2 Hold Last State` | 3 | Switch Type and State | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：state／switch |
| `SWITCH 2 Power Mode` | 3 | Switch Power Mode | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：mode／power／switch |
| `SWITCH 2 Type` | 3 | Switch Type and State | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：switch／type |
| `SWITCH 3 Hold Last State` | 3 | Switch Type and State | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：state／switch |
| `SWITCH 3 Power Mode` | 3 | Switch Power Mode | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：mode／power／switch |
| `SWITCH 3 Type` | 3 | Switch Type and State | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：switch／type |
| `SWITCH 4 Hold Last State` | 3 | Switch Type and State | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：state／switch |
| `SWITCH 4 Power Mode` | 3 | Switch Power Mode | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：mode／power／switch |
| `SWITCH 4 Type` | 3 | Switch Type and State | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：switch／type |
| `6 Aux Switches` | 2 | Auxiliary Switches | (i) 不成立 —— 章名主題詞與現屬 Test Set 名相交：switches |

## 4. 12 個跨界簇之整併（R-VF36 起點二）

跨兩個 Test Set 之簇 **12** 個，依 R-VF36 整併入 **Auxiliary Switches**：

- `SWITCH 1 Hold Last State`（6 leaf）
- `SWITCH 1 Power Mode`（6 leaf）
- `SWITCH 1 Type`（6 leaf）
- `SWITCH 2 Hold Last State`（6 leaf）
- `SWITCH 2 Power Mode`（6 leaf）
- `SWITCH 2 Type`（6 leaf）
- `SWITCH 3 Hold Last State`（6 leaf）
- `SWITCH 3 Power Mode`（6 leaf）
- `SWITCH 3 Type`（6 leaf）
- `SWITCH 4 Hold Last State`（6 leaf）
- `SWITCH 4 Power Mode`（6 leaf）
- `SWITCH 4 Type`（6 leaf）

## 5. 提案 C 之 Layer 2 表

| # | Test Set | leaf | 簇 |
|---:|---|---:|---:|
| 1 | **Trailer and Signage** | 136 | 12 |
| 2 | **Driver Convenience** | 104 | 20 |
| 3 | **Auxiliary Switches** | 87 | 16 |
| 4 | **Units and Cameras** | 63 | 12 |
| 5 | **Suspension and Comfort** | 62 | 12 |
| 6 | **Lane and Lighting** | 49 | 9 |
| 7 | **Switch Power Mode** | 45 | 9 |
| 8 | **Approach and Tailgate** | 41 | 7 |
| 9 | **Daytime Lighting** | 17 | 3 |
| 10 | **Switch Type and State** | 12 | 4 |
| 11 | **Measurement Units** | 11 | 2 |

**合計 627**（自各 Test Set 重算，未沿用前案差值）。

**消失之 Test Set（0）**：


## 6. canon §4.1.3 兩項反面型態

| 型態 | 實數 | 判 |
|---|---|---|
| **過細**（Test Set 欄近乎 TC ID 欄之複本） | 11 set／627 leaf，平均 57，最小 11 | **否** |
| **過粗**（`Misc`／`General`／`Unclassified` 收容簇） | 無此類名 | **否** |

## 7. R-VF34 之 2 簇（Layer 3 留空且可見）

| 簇 | leaf | 所屬 Test Set | Layer 3 |
|---|---:|---|---|
| `CHMSL CAMERA DYNAMIC CENTERLINE` | 5 | Trailer and Signage | **（無 spec 對應 —— R-VF34，不自創章名）** |
| `E-Save` | 6 | Auxiliary Switches | **（無 spec 對應 —— R-VF34，不自創章名）** |

**其 leaf 仍計入母體 627 與其所屬 Test Set**（R-VF34 第 2 項）。
**DR-31 已登記**（見 `DATA_REQUESTS.md`）；送出屬 Pei（R-VF27）。

## 8. R-VF37 之 (a)/(b) 判斷

- 既有 11 名之集合外**新出現之名：0**（無）
- 消失之名：0

→ **判 (b)**

## 9. 語義範圍是否實質改變（R-VF37(a) 之第二個條件）

| Test Set | 移入 | 移出 | 判 |
|---|---|---|---|
| Approach and Tailgate | 0 | 16 | 無移入，語義未變 |
| Auxiliary Switches | 2 | 59 | **須人工判** |
| Daytime Lighting | 5 | 0 | **須人工判** |
| Driver Convenience | 5 | 0 | **須人工判** |
| Lane and Lighting | 0 | 0 | 無移入，語義未變 |
| Measurement Units | 0 | 6 | 無移入，語義未變 |
| Suspension and Comfort | 22 | 12 | **須人工判** |
| Switch Power Mode | 52 | 18 | **須人工判** |
| Switch Type and State | 36 | 0 | **須人工判** |
| Trailer and Signage | 14 | 9 | **須人工判** |
| Units and Cameras | 0 | 16 | 無移入，語義未變 |

**本節之判斷本層不機械化** —— 「語義範圍實質改變」非詞集可決。
有移入者逐一於上繳具名，**有疑義走 (b)**（R-VF37 末句）。

