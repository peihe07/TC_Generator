# 欄級 diff — CAM-05 → CAM-06（batch01 ＋ pilot02 之 `-009`／`-010`）

下放包 `down/20260923_CAM-06.md` §2。**七列變動**（batch01 五列、pilot02 二列）；
其餘 16 列 batch01 與 8 列 pilot02 逐字未動。

---

## 1. `NR1L-RVC-023`（batch01）—— 審閱 §二-1，RUN 重複

| 欄 | CAM-05 | CAM-06 |
|---|---|---|
| `test_procedure` | 1. `Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)`<br>2. `Press "Apps" …`<br>3. `Read the App Drawer …` | **（刪步 1）**<br>1. `Press "Apps" on Menu Bar to open App Drawer`<br>2. `Read the App Drawer and check that "Rear View Camera" is selectable` |
| `expected_result` | 1. `BCM_FD_10.CmdIgnSts = 4 (RUN) is sent`<br>2. `The App Drawer is displayed`<br>3. `The "Rear View Camera" entry …` | **（刪 ER1，重編）**<br>1. `The App Drawer is displayed`<br>2. `The "Rear View Camera" entry is shown in the available state and can be selected` |
| `pre_conditions` | （不動）| （不動）—— 第 3 行 CAN source 保留為 `$PowerMode$` 之 EE 對照 |
| `reasoning` | — | ＋【CAM-06 §2-1】段 |

## 2. `NR1L-RVC-021`（batch01）—— 審閱 §二-2，Delay 前提

| 欄 | CAM-05 | CAM-06 |
|---|---|---|
| `pre_conditions` | 4 行（1 Full-Operation／2 PROXI／3 CAN source／4 影像已顯示）| **5 行** —— 新增 `4. The camera delay setting is set to "On"`，原第 4 行順延為 5 |
| `reasoning` | — | ＋【CAM-06 §2-1】段 |

## 3. `NR1L-RVC-026`（batch01）—— 審閱 §二-3，ER 可判性

| 欄 | CAM-05 | CAM-06 |
|---|---|---|
| `expected_result` 第 2 項 | `The rear view camera image stays displayed until Ttimer2 maxes out` | `The rear view camera image is still displayed` |
| `reasoning` | — | ＋【CAM-06 §2-1】段（Ttimer2 到期委派 `-029`／`-028`）|

## 4. `NR1L-RVC-030`／`-031`（batch01）—— 審閱 §二-4 ＋ 標定值改正

| 欄 | CAM-05 | CAM-06 |
|---|---|---|
| `pre_conditions` | 5 行；第 5 行 `The calibration MAX_SPEED corresponds to 8 mph per CFTS092 4781643` | **6 行** —— 新增 `3. LTM_OperationalModeSts.Info = "Ignition_On_EngOn"`；末行改為 `6. The calibration MAX_SPEED = 13,0 Km/h per VF551_V33 1.14.1` |
| `test_procedure` 步 2 | `-030`：`= 206 (12.875 km/h)`<br>`-031`：`= 205 (12.8125 km/h)` | `-030`：**`= 209 (13.0625 km/h)`**<br>`-031`：**`= 208 (13.0 km/h)`** |
| `expected_result` 第 2 項 | 同上之 raw／km/h | 同上之新 raw／km/h |
| `reasoning` | — | ＋【CAM-06 §2-1／§2-3】段（A-CA31、RDF-03）|

## 5. `NR1L-RVC-009`／`-010`（pilot02）—— R-CAM14 改錨

| 欄 | CAM-05 | CAM-06 |
|---|---|---|
| `source_object_id` | `SYS-RA-VF551_V2-490` | **`SYS-RA-CAM-078`** |
| `specification_reference` | `VF551_V2_PHDCC27_VF_1577` | **`CFTS092-4781643`** |
| `test_item_verbatim` | `· The Ttimer2 shall start when BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX.` | **`Rear Camera display image shall remain displayed until display timer is greater than 10s AND vehicle speed is above 8 mph.`** |
| `test_item` | 上半同上 ＋ 括號下半 | 上半隨錨改；**括號下半逐字不動** |
| `vehicle_model` | `Fastack (376)` = `0` | **`1`** |
| `pre_conditions` | 6 行；第 3 行 `PROXI Rear_View_Camera_Type = 1 (Digital)`；末行 `The calibration c_VEHSPD_MAX corresponds to 8 mph per CFTS092 4781643` | **6 行** —— 刪 `Rear_View_Camera_Type`（Atl-Hi 專屬參數，376 之 PROXI 查無）；新增 `3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)`；末行改為 `6. The calibration c_VEHSPD_MAX = 8 mph per VF551_V2 1.8.13 and VF551_V3 1.14.1` |
| `test_procedure`／`expected_result` | （不動，raw 206／205 對 Atl-Hi 與 376 皆成立）| （不動）|
| `reasoning` | — | ＋【CAM-06 §2-3】段（376 加勾之依據、637 仍勾 0 之依據、`BRAKE1` 不取之依據）|

---

## 未動之列

`NR1L-RVC-011`～`-020`、`-022`、`-024`、`-025`、`-027`～`-029`、`-032`、`-033`（batch01 16 列）
與 `NR1L-RVC-001`～`-008`（pilot02 8 列）逐字未動。
