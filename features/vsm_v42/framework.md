# framework — Vehicle Setup Management R1 Low（vsm_v42）

鎖定：Layer 1／Layer 2 於 2026-09-02 由 Pei 裁定（「准」，R-VL17）。
Layer 3 之規格章節號欄由執行層自 V42 R6 docx 標題實測回填（P3 包 W-8），
回填為量測非裁決，不解鎖 Layer 2。
依 IN §4.1.5：Layer 1／2 寫入工作簿（Test Group／Test Set 欄），Layer 3 僅存本檔。

## Layer 1 — Test Group

`Vehicle Setup Management R1 Low`（R-VL3）

## Layer 2 — Test Set（10 組，leaf 合計 128）

| # | Test Set | leaf | Layer 3（037 家族；括號 = leaf） | 規格章節號（待 W-8 實測） |
|---|---|---|---|---|
| 1 | Park Sense | 18 | PARK SENSE w/o HC.1 and PARK SENSE w/o HC.2 (5)、Rear Park Sense Volume/ ParkSense Volume (6)、Front Park Sense Volume (7) | PARK SENSE w/o HC.1 and PARK SENSE w/o HC.2 = 1.11.1.1.29；Rear Park Sense Volume/ ParkSense Volume = **未對映**；Front Park Sense Volume = **未對映** |
| 2 | Camera Gridlines | 10 | Dynamic Gridlines (4)、Surround Camera Gridlines (6) | Dynamic Gridlines = 1.11.1.1.31；Surround Camera Gridlines = 1.11.1.1.38 |
| 3 | Lighting | 11 | Auto High Beam (5)、Headlight Sensitivity (6) | Auto High Beam = 1.11.1.1.30；Headlight Sensitivity = 1.11.1.1.13 |
| 4 | Speed Assist | 21 | Traffic Sign Recognition (5)、Traffic Sign Assist Warning (6)、Intelligent Speed Limiter with Confirmation (4＋1 未分類)、New Speed Zone (6) | Traffic Sign Recognition = 1.11.1.1.32；Traffic Sign Assist Warning = 1.11.1.1.33；Intelligent Speed Limiter with Confirmation = 1.11.1.1.35；New Speed Zone = 1.11.1.1.36 |
| 5 | Driver Warning | 13 | Side Distance Warning (10)、Audio Repetition (3) | Side Distance Warning = 1.11.1.1.5；Audio Repetition = 1.11.1.1.28 |
| 6 | Wiper and Sensor | 5 | Rain Sensor (5) | Rain Sensor = 1.11.1.1.7 |
| 7 | Units | 15 | Units (1)、Distance (5)、Fuel Consumption (9) | Units = 1.11.1.1.10；Distance = **未對映**；Fuel Consumption = 1.11.1.1.10.5.2 |
| 8 | EPB Maintenance Mode | 17 | EPB Maintenance Mode (17) | EPB Maintenance Mode = 1.11.1.1.19 |
| 9 | Personal Data and Defaults | 14 | Personal Profile Management (3)、Clear Personal Data (3)、Restore Default Setting (3)、Geolocation (5) | Personal Profile Management = 1.11.1.1.37；Clear Personal Data = 1.11.1.1.40／1.11.2.1.2；Restore Default Setting = 1.11.1.1.41／1.11.2.1.3；Geolocation = 1.11.1.1.39／1.11.2.1.1 |
| 10 | Time and Navigation | 4 | GPS Automatic Time Adjustment (2)、Nav Turn by Turn (2) | GPS Automatic Time Adjustment = 1.11.1.1.25；Nav Turn by Turn = 1.11.1.1.27 |

leaf 合計 = 128（`data/leaves.tsv` 實測；`-051` 未分類列不入合計，見 DR-VL2(a)）。
偏小組（#6 = 5、#10 = 4）經 Pei 准照案保留，不併鄰組。

## 規則

- Test Set 拼寫逐字依上表，大小寫敏感，無尾空白（IN §4.2）；不得帶 Test Group 前綴。
- 新 leaf（DR 回覆或 037 增補）先對映入上表；無處可放者先修本檔再寫 TC（IN §4.1）。
- TC 依 Layer 3 家族連續書寫（IN §4.1.4-1）；sibling 判定以同家族為先驗（-2）；
  覆蓋完備性以家族為單位（-3）；Pre-Condition 範圍依家族界線（-4，IN §8.5）。
- 判別力備忘（上繳 03 實測）：037 `Sub Categorization` 僅二值（＝來源檔）、SYSRA
  `Chapter for VF` 前二階全 `01.11`，皆不得作 Layer 2／3 依據；本表以家族語意聚合（Pei 准）。

## Pilot（P5）

分析層提案：**EPB Maintenance Mode**（17 leaf，單家族成組，共用 setup 與 UI 入口；
訊號鏈上 `IPC_VEHICLE_SETUP2.EPB_MaintenanceMode` 等已解得）。開跑前 Pei 可改指。
