# W-VF35 —— 提案 C 之逐筆列舉（R-VF41）

**不設通則，不用任何詞相交判準**（R-VF41）。每筆之依據為該簇之
**條文主旨**（自其 leaf 之 `desc` 取），非自章名推。

## 0. 錨點（R-VF21 ／ R-VF28 ／ R-VF41 第 5 項）

| 錨點 | 簇 | 期望 | 實測 |
|---|---|---|---|
| 必移動 | `Suspension Default Ride Height` | 移入 `Suspension and Comfort` | ✅ |
| 必不移動 | `Pressure Unit` | 留置 | ✅ |
| **鑑別** | `Power Unit` | **留置** —— 其為上一版規則之已知失效點（量測單位被移入 `Switch Power Mode`） | ✅ **未移動** |
| 合計 | — | 627（R-VF16） | 627 ✅ |

## 1. 移動（19 筆）

| 簇 | leaf | 原 → 新 | 條文主旨 | 為何原屬不當 / 為何新屬適當 |
|---|---:|---|---|---|
| `Rear Guidance Lights with Cargo Lights` | 5 | Switch Power Mode → **Auxiliary Switches** | 取得 Utility_Light 配置以決定後方導引燈與貨廂燈之連動 | 其非開關之電源模式／其二姊妹簇 `Rear Guidance Lighting with Approach` 與 `Rear Guidance Light Status` 皆已在此 |
| `SWITCH 1 Hold Last State` | 3 | Switch Type and State → **Auxiliary Switches** | The HMI layer shall capture the customer selection for the SWITCH 1 Ho | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `SWITCH 1 Power Mode` | 3 | Switch Power Mode → **Auxiliary Switches** | When the customer chooses to set the SWITCH 1 Power Mode setting to Ig | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `SWITCH 1 Type` | 3 | Switch Type and State → **Auxiliary Switches** | The HMI layer shall capture the customer selection for the SWITCH 1 Ty | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `SWITCH 2 Hold Last State` | 3 | Switch Type and State → **Auxiliary Switches** | The HMI layer shall capture the customer selection for the SWITCH 2 Ho | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `SWITCH 2 Power Mode` | 3 | Switch Power Mode → **Auxiliary Switches** | When the customer chooses to set the SWITCH 2 Power Mode setting to Ig | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `SWITCH 2 Type` | 3 | Switch Type and State → **Auxiliary Switches** | The HMI layer shall capture the customer selection for the SWITCH 2 Ty | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `SWITCH 3 Hold Last State` | 3 | Switch Type and State → **Auxiliary Switches** | The HMI layer shall capture the customer selection for the SWITCH 3 Ho | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `SWITCH 3 Power Mode` | 3 | Switch Power Mode → **Auxiliary Switches** | When the customer chooses to set the SWITCH 3 Power Mode setting to Ig | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `SWITCH 3 Type` | 3 | Switch Type and State → **Auxiliary Switches** | The HMI layer shall capture the customer selection for the SWITCH 3 Ty | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `SWITCH 4 Hold Last State` | 3 | Switch Type and State → **Auxiliary Switches** | The HMI layer shall capture the customer selection for the SWITCH 4 Ho | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `SWITCH 4 Power Mode` | 3 | Switch Power Mode → **Auxiliary Switches** | When the customer chooses to set the SWITCH 4 Power Mode setting to Ig | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `SWITCH 4 Type` | 3 | Switch Type and State → **Auxiliary Switches** | The HMI layer shall capture the customer selection for the SWITCH 4 Ty | 其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條 |
| `4 AUX Switches` | 2 | Switch Power Mode → **Auxiliary Switches** | 取得 AUX_Switch_Type 配置以決定輔助開關之數量與型別 | 其為輔助開關本身之配置，與「電源模式」此一單一屬性不相稱／`6 Aux Switches` 已在此，二者為同一功能之不同車型配置 |
| `Suspension Auto Entry or Exit` | 6 | Units and Cameras → **Suspension and Comfort** | 取得配置以決定上下車時懸吊之自動升降 | 其與單位顯示、攝影機無共同之 setup 型態／為懸吊之自動行為，與 `Suspension Service Mode` 同族 |
| `Suspension Default Ride Height` | 6 | Switch Power Mode → **Suspension and Comfort** | 取得 Hybrid_Type 等配置以定懸吊之預設車高 | 其與開關之電源模式無任何共同之 setup 或 UI 進入路徑／`Suspension Service Mode`／`Suspension Display Messages` 已在此，同為懸吊之設定 |
| `Suspension Flash Lights With Lower` | 5 | Switch Power Mode → **Suspension and Comfort** | 取得 CAN node 27 配置，控制車身降低時之閃燈行為 | 同上 —— 其為懸吊動作之附隨行為，非開關設定／與其餘懸吊簇同一能力叢集 |
| `Suspension Sound Horn With Lower` | 5 | Switch Power Mode → **Suspension and Comfort** | 取得 CAN node 27 配置，控制車身降低時之鳴笛行為 | 同上 |
| `Trailer Number` | 8 | Approach and Tailgate → **Trailer and Signage** | 取得配置以決定可登錄之拖車組數 | 其與 approach 照明、電動尾門無關／`Trailer Name`(22)／`Trailer Brake Type`(13)／`Automatic Trailer Light Check`／`Blind Spot with Trailer Detection` 皆在此 |

## 2. 過檢視而留置（87 筆；其中 7 筆具名）

**R-VF41 令不移動者亦須列，附一句理由。** 未具名者為「其簇名與其所屬
Test Set 之主題相符，無移動之理由」——逐簇檢視過，不逐筆重述。

### 2.1 具名者

| 簇 | leaf | Test Set | 理由 |
|---|---:|---|---|
| `Charge Power Level` | 8 | Approach and Tailgate | 主旨為充電功率等級。**與 `Approach and Tailgate` 之名不相稱**，惟無更適當之既有 Test Set；依 R-VF41「不設通則」亦不得為其新設。**具名為異質性殘留**（R-VF37 已裁其為已接受之狀態）。 |
| `Engine Off Power Delay` | 7 | Suspension and Comfort | 主旨為熄火後電源延時。其屬 `Suspension and Comfort` 之「Comfort」一側，可辯護惟非理想。**具名。** |
| `Power Unit` | 6 | Measurement Units | **鑑別錨點**。主旨為功率單位（kW／hp）之顯示配置 —— 其為**量測單位**，非開關之電源模式。上一版規則僅因共用 `power` 一詞而誤移之，本方案不移。 |
| `Power Side Step` | 5 | Trailer and Signage | 主旨為電動側踏板之啟閉。與 `Signage` 不相稱，無更適之處。**具名。** |
| `Rear Guidance Lighting with Approach` | 5 | Auxiliary Switches | 與其二姊妹簇同處 `Auxiliary Switches`，不動。 |
| `Hour Mode` | 4 | Units and Cameras | 主旨為 12／24 小時制之顯示格式，與 `Time and Date Settings` 同組，留於 `Units and Cameras` 正確。上一版規則因 `mode` 一詞誤移。 |
| `Max Power Level` | 4 | Trailer and Signage | 主旨為最大輸出功率等級。同上。**具名。** |

### 2.2 未具名者（逐 Test Set 計數）

| Test Set | 留置簇數 |
|---|---:|
| Driver Convenience | 19 |
| Units and Cameras | 13 |
| Trailer and Signage | 10 |
| Auxiliary Switches | 9 |
| Suspension and Comfort | 9 |
| Lane and Lighting | 9 |
| Approach and Tailgate | 7 |
| Daytime Lighting | 2 |
| Measurement Units | 2 |

## 3. 提案 C 之 Layer 2 表

| # | Test Set | leaf | 簇 |
|---:|---|---:|---:|
| 1 | **Trailer and Signage** | 139 | 13 |
| 2 | **Auxiliary Switches** | 115 | 24 |
| 3 | **Driver Convenience** | 99 | 19 |
| 4 | **Suspension and Comfort** | 74 | 14 |
| 5 | **Units and Cameras** | 73 | 14 |
| 6 | **Approach and Tailgate** | 49 | 8 |
| 7 | **Lane and Lighting** | 49 | 9 |
| 8 | **Measurement Units** | 17 | 3 |
| 9 | **Daytime Lighting** | 12 | 2 |

**合計 627**（自各 Test Set 重算）。

**消失之 Test Set（2）**：`Switch Power Mode`／`Switch Type and State`

→ **V11 §7 之論證於此實現**：`Switch Power Mode` 與
`Switch Type and State` 二名確已消失，其內容各歸其實。

**新出現之名：0**（無）

## 4. canon §4.1.3 兩項反面型態

| 型態 | 實數 | 判 |
|---|---|---|
| **過細** | 9 set／627 leaf，平均 69，最小 12、最大 139 | **否** |
| **過粗**（`Misc`／`General`／`Unclassified` 收容簇） | 無此類名 | **否** |

## 5. R-VF37 之判斷

- 新名 **0** ／ 消失 **2**
- 名之集合為已核可 11 名之**子集** → 形式合 (a)

**惟本輪不適用 R-VF37(a) 之逕鎖條款** —— R-VF41 明定其前提為
「依既有規則機械產出」，而本表為**逐筆列舉、含判斷**。
**回報待分析層覆核**（R-VF41 核可路徑）。**`framework.md` 未寫入。**

