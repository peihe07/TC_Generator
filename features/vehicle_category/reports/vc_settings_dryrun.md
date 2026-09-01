# VehicleCategory 設定項 dry-run 摘要（下放包 VS-SL-01 §5）

日期：2026-09-01　性質：**dry-run，未寫回**　明細：`vc_settings_dryrun.tsv`（126 列）
本 feature **不套 §2 任務 1 之 `path` 段**（入口為 App Drawer／Vehicle Category 畫面）。

## §A　實測

| 項 | 數 |
|---|---:|
| 工作簿資料列 | **126**（`output/…_VehicleCategory_20260827_working.xlsx` r10–r135） |
| 報告列 | **126**（自檢 PASS） |
| `Pre-Condition` 含 `PROXI` 之列 | **0** |
| `PROSE_PRECOND` | 71 |
| `NO_MAPPING` | 53 |
| `ALWAYS_FALSE` | 4 |

## §B　散文存在性條件之對應

| 散文 | 列數 | 對應 | 提議 |
|---|---:|---|---|
| `The vehicle is equipped with the Vehicle Category feature` | **16** | 总控表**無**對應列 | **`PENDING: DR-49`**。`proxi_values` 雖有 `Vehicle_Category` `{0:M1, 1:M2 max mass, 2:M2 max mass, 3:N1, 4:N2}`，但「equipped with the feature」**≠ 該參數某值**，依 R-13 不得代入 |
| `The Glove Box feature is activated with a known 4-digit PIN` | **5** | `Glove_Box_Soft_Button` = 1 (Present) | `PROXI Glove_Box_Soft_Button = 1 (Present)`；**啟用狀態仍為步驟內操作**，不入 Pre |
| `The Glove Box feature is not activated` | **7** | 同上 | 同上 |
| `equipped with an Electrochromic Controls item` | **2** | 总控表 No.24 `Mirror Dimmer` | `PROXI EC_Mirror = 1 (Present) ; PROXI EC_Mirror_Hard_Button_Present = 0 (Absent)` |
| `equipped with a Headrest Fold Controls item` | **2** | 总控表 No.18 `Headrest Fold` = `Always false` | 依 R-VS{live+1} **不出負向**；正向列之 PROXI 只能依需求原文 → 現為 `PENDING: DR-49` |
| `equipped with the Camera App` | **2** | 总控表 No.196 `Cam App` = `Always false` | 同上。**另須先確認 TC 指的是 `Cam App` 還是 `Backup Cam`**（後者為 `Rear_View_Camera` = 1 (Present)） |
| `equipped with the Controls buttons under test` | **4** | 总控表 No.10 `Controls` = `Always true` | 無條件可加；建議保留散文 |
| `equipped with the Specialty features …` | **4** | 無 PROXI 對應 | `NO_MAPPING`，保留散文或開 DR |
| `equipped with a portrait display` | **4** | 螢幕方向無 PROXI 對應 | 同上 |
| `equipped with a landscape display` | **3** | 同上 | 同上 |

## §C　待 Pei 決

1. `Vehicle Category feature` 之「具備與否」無 PROXI 表述 —— **併入 DR-49**（16 列）。
2. `Camera App` 究指 `Cam App`（`Always false`）或 `Backup Cam`（`Rear_View_Camera`）—— 2 列懸置。
3. `Specialty features`／螢幕方向共 11 列無對應：保留散文，或開新 DR。
