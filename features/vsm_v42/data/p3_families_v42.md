# P3 前置 — 037 家族實測（下放包 03 §三，不鎖 Layer 2）

來源：`data/leaves.tsv`（152 列）。leaf ＝ `tc_status == leaf`（Functional Requirement）。

| Requirement Title（037 家族） | leaf | Heading | 未分類 | 037 檔 | Sub Categorization（計數） | SYSRA Chapter for VF 前二階（計數） |
|---|---|---|---|---|---|---|
| EPB Maintenance Mode | **17** | 1 | 0 | sdw | Display (including HAL)×17 | 01.11×18 |
| Side Distance Warning | **10** | 1 | 0 | sdw | Display (including HAL)×10 | 01.11×11 |
| Fuel Consumption | **9** | 1 | 0 | sdw | Display (including HAL)×9 | 01.11×10 |
| Front Park Sense Volume | **7** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×7 | 01.11×8 |
| Rear Park Sense Volume/ ParkSense Volume | **6** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×6 | 01.11×7 |
| Traffic Sign Assist Warning | **6** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×5 | 01.11×7 |
| New Speed Zone | **6** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×5 | 01.11×7 |
| Surround Camera Gridlines | **6** | 0 | 0 | parksense | Vehicle Setting Management (VSM)×6 | 01.11×6 |
| Headlight Sensitivity | **6** | 1 | 0 | sdw | Display (including HAL)×6 | 01.11×7 |
| PARK SENSE w/o HC.1 and PARK SENSE w/o HC.2 | **5** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×5 | 01.11×6 |
| Auto High Beam | **5** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×4 | 01.11×6 |
| Traffic Sign Recognition | **5** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×5 | 01.11×6 |
| Geolocation | **5** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×5 | 01.11×6 |
| Rain Sensor | **5** | 1 | 0 | sdw | Display (including HAL)×5 | 01.11×6 |
| Distance | **5** | 1 | 0 | sdw | Display (including HAL)×5 | 01.11×6 |
| Dynamic Gridlines | **4** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×4 | 01.11×5 |
| Intelligent Speed Limiter with Confirmation | **4** | 1 | 1 | parksense | Vehicle Setting Management (VSM)×4 | 01.11×6 |
| Personal Profile Management | **3** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×3 | 01.11×4 |
| Clear Personal Data | **3** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×3 | 01.11×4 |
| Restore Default Setting | **3** | 1 | 0 | parksense | Vehicle Setting Management (VSM)×3 | 01.11×4 |
| Audio Repetition | **3** | 1 | 0 | sdw | Display (including HAL)×3 | 01.11×4 |
| GPS Automatic Time Adjustment | **2** | 1 | 0 | sdw | Display (including HAL)×2 | 01.11×3 |
| Nav Turn by Turn | **2** | 1 | 0 | sdw | Display (including HAL)×2 | 01.11×3 |
| Units | **1** | 1 | 0 | sdw | Display (including HAL)×1 | 01.11×2 |

**24 家族，leaf 合計 128，與 00 包 §九 草案數逐項相符。**

兩處標題在 00 包為縮寫，實測全名為：
- `PARK SENSE w/o HC.1 and HC.2` → **`PARK SENSE w/o HC.1 and PARK SENSE w/o HC.2`**（5）
- `Rear Park Sense Volume` → **`Rear Park Sense Volume/ ParkSense Volume`**（6）
