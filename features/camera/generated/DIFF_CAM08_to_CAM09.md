# 欄級 diff — CAM-08 → CAM-09（五目錄之點火句式與電源態修正）

下放包 `down/20260923_CAM-09.md` §1-5 ／ 審閱 `down/20260923_CAM-08_review.md` §一-2、§二。
**變動 14 列**（batch01b 2／batch02b 12，其中 `-082`／`-087` 為執行層自查）；
pilot02／batch01／batch02a 三目錄未動。

---

## 型 1 —— 點火動作改 CAN 式（selfcheck 第 7 項，12 列）

掃描五目錄 94 列，第 7 項命中 **12 列**：
`-037`／`-044`（batch01b）、`-073`～`-078`／`-085`～`-087`／`-091`（batch02b）。

| 欄 | CAM-08 | CAM-09 |
|---|---|---|
| `test_procedure` 步 1 | `Cycle the ignition to RUN so that the HU reads the PROXI configuration`（`-037`／`-044` 另前綴 `Set PROXI … and`）| **`Send CAN: <MSG>.CmdIgnSts = 4 (RUN)`** |
| `expected_result` 項 1 | `The HU completes start-up and reads the PROXI configuration` | **`<MSG>.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration`**（目的子句移入 ER）|

`<MSG>` 依平台：`BCM_FD_10.CmdIgnSts`（`-037`／`-044`／`-073`／`-074`／`-075`／`-085`／`-086`／`-087`）、
`STATUS_BH_BCM2.CmdIgnSts`（`-076`／`-077`／`-078`／`-091`）。

**`-037`／`-044` 另刪步 1 之 `Set PROXI … (Present) and` 前綴** —— PROXI 組態已由
Pre-Condition 2 承載，procedure 不重複設定。

## 型 2 —— 開機類 TC 之首行改 Standby（profile §4.1，9 列）

`-037`／`-044`／`-073`／`-074`／`-075`／`-076`／`-077`／`-078`／`-091`：

| 欄 | CAM-08 | CAM-09 |
|---|---|---|
| `pre_conditions` 第 1 行 | `The HU is in the Full-Operation state` | **`The HU is in Standby state`** |

`-085`／`-086`／`-087` 之首行原即 `Standby`，未動（其第 3b 項之命中係因當時無點火步，
型 1 之修正一併解消）。

## 型 3 —— 補 CAN source 行（R-CAM3(f)，3 列）

`-037`／`-044`／`-085` 於型 1 取得 `Send CAN` 步後，其 Vehicle Model 同時勾兩 EE，
**兩條件皆成立**，依 R-CAM3(f) 補：

```
3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)
```

其後各行順延。其餘 9 列為單一 EE，不加該行。

## 型 4 —— `Body_Types` 改 label 式（DECISIONS 6-24，2 列）

| TC | CAM-08 | CAM-09 |
|---|---|---|
| `-073` | `PROXI Body_Types = 4 (Type 4 - DJ)` | **`PROXI Body_Types = Type 4 - DJ`** |
| `-074` | `PROXI Body_Types = 1 (Type 1 - D2)` | **`PROXI Body_Types = Type 1 - D2`** |

`reasoning` 之對應段改寫，指向 **DR-CAM-n**。
`PROXI Vehicle_Line_Configuration = 130 (HDCC (82 Hex))` 之巢狀括號**不改**
（審閱 §二-3：PROXI 表 label 逐字為 `HDCC (82 Hex)`，逐字優先）。

## 型 5 —— V4 列之 `DT27` 改勾 0（執行層自查，2 列）

| TC | 欄 | CAM-08 | CAM-09 |
|---|---|---|---|
| `-082` | `vehicle_model.DT27` | `1` | **`0`** |
| `-087` | `vehicle_model.DT27` | `1` | **`0`** |

依據：V4 本之 anchor 前綴只有 `PHDCC27`（R-CAM11），RULINGS 平台表亦只將 V4 對應
`HDCC27 Atl-Hi`；DT27 之 V 本為 `V2 (PDT27 anchor)`。
實測佐證：`DT28_ATL_HI` row 931 之 `Rear_View_Camera_Type = 1 (Digital)` ——
該平台本無類比相機之組態。兩列之 `reasoning` 已加註。

---

## 未動之目錄

`pilot02`（10 列）、`batch01`（23 列）、`batch02a`（26 列）逐字未動 ——
三者於第 3／7 項掃描皆零命中。
