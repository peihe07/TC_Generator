# 欄級 diff — CAM-06 → CAM-07（`-023`／`-030`／`-031` ＋ 新增 `-046`）

下放包 `down/20260923_CAM-07.md` §2。**三列改動 ＋ 一列新增**；
batch01 其餘 20 列、batch01b `-034`～`-045` 十二列、pilot02 十列逐字未動。

---

## 1. `NR1L-RVC-023`（batch01）—— DECISIONS 6-15

| 欄 | CAM-06 | CAM-07 |
|---|---|---|
| `pre_conditions` | 5 行；第 3 行 `CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)` | **4 行** —— 刪第 3 行，其後兩行順延為 3／4 |
| `reasoning` | 「Pre-Condition 3 之 CAN source 行保留…」 | 改為「**已刪**（DECISIONS 6-15）…CAM-06 上繳 §5-5 所請之確認到此結案」 |
| 其餘欄 | — | 不動 |

## 2. `NR1L-RVC-030`／`-031`（batch01）—— R-CAM14(b)

| 欄 | CAM-06 | CAM-07 |
|---|---|---|
| `vehicle_model` | `VF(ProMaster)637` = `0` | **`1`**（其餘六欄不動：Atl-Hi 兩欄 0、`Toro(2261)` 1、`Fastack (376)` 0）|
| `specification_reference` | `VF551_V33_P226MCA_VF_532`（單行）| **兩行** —— 加 `VF551_V42_P637MCA_VF_960`（`SYS-RA-VF551_V42-656`）|
| `pre_conditions` 第 6 行 | `The calibration MAX_SPEED = 13,0 Km/h per VF551_V33 1.14.1` | `… per VF551_V33 1.14.1 **and VF551_V42 1.14.1**` |
| `test_procedure`／`expected_result` | raw 209／208 | **不動** —— 兩平台之標定同數，供試值不變 |
| `reasoning` | — | ＋【CAM-07 §2】段（併入依據、V42 無退出條文、常數錨之性質）|

**CAN source 行未加**（下放包 §2 明載「不需（同訊息）」）—— 637 與 2261 之速度訊號同為
`STATUS_CCAN3.VehicleSpeedVSOSig`，R-CAM3(e) 之分寫句式無適用對象。

## 3. `NR1L-RVC-046`（batch01b，新增）—— DECISIONS 6-17 ／ A-CA32

| 欄 | 值 |
|---|---|
| `req_id`／`test_group` | `SWE-CAM-016`／`Rear View Camera` |
| **`test_set`** | **`Display Arbitration`**（非 `Additional Cameras` —— 來源屬 Rear Camera 節）|
| `source_object_id`／`specification_reference` | `SYS-RA-CAM-076`／`CFTS092-4781641` |
| `test_item_verbatim` | `The Rear Camera Softkey button shall be accessible from the Controls screen.`（12 token）|
| `vehicle_model` | HDCC27 1／DT27 1／637 1／2261 1／376 1（`PROXI Rear_View_Camera` 六本皆有）|
| `priority`／`design_method` | P2／功能測試 |
| PENDING | `DR-CAM-g`（proc 步 1 ＋ ER 1）|

CAM-05 §3.1 之「不生成」與 batch01_plan 該列之 `tc_count = 0` 併同作廢。

---

## 未動之列

batch01：`-011`～`-022`、`-024`～`-029`、`-032`、`-033`（20 列）
batch01b：`-034`～`-045`（12 列）
pilot02：`-001`～`-010`（10 列）
