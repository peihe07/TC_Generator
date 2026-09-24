# INDEX — batch06（R-CAM19 追溯補齊，下放包 CAM-26 §2）

Pei 2026-09-24 裁定「**有需求就要有產出**」（**R-CAM19**）：037 每一 leaf 列至少一列 TC 掛自己的 ID，
D 欄佔位列作廢（DECISIONS 6-52／6-73）。A 本原零 TC 之 **4 列**各出一列｜TC ID `NR1L-RVC-246`～`-249`｜
計畫 `features/camera/data/batch06_plan.tsv`。**既有 245 列不改**。

| 需求 | 原處置 | 本批 | 驗證角度 | 同源／被引 |
|---|---|---|---|---|
| `SWE-CAM-007`（NCD HAL）| 全委派 `-006`（R-CAM16）| `-246` | `V42-210` 之「影像經 LVDS 自 RVCM 送達」之接收（bus analyzer）| `SWE-CAM-006`：`NR1L-RVC-200` |
| `SWE-CAM-013`（NCD HAL）| 全委派 `-006`／`-004`（R-CAM16）| `-247` | DTC 讀取時 LVDS 上之 `diagnosticRequest`／`diagnosticResponse`（訊息面 `PENDING: DR-CAM-t`）| `-006`：`-211`／`-212`；`-004`：`-195` |
| `SWE-CAM-024`（App）| BLOCKED D 欄空列 | `-248` | **R-CAM19(d) 六欄佔位** `PENDING: DR-CAM-a` | — |
| `SWE-CAM-025`（App）| 全委派 `-020`（R-CAM16）| `-249` | 影像顯示中收到 bed extender active → 影像移除＋警示疊層（App 側，狀態轉換）| `SWE-CAM-020`：`-032`／`-033` |

**與下放包 §2 之出入**（A-CA38，上繳 CAM-26 §6）：`-025` 之委派對象為 `-020`（非 `-023`）；`-013` 之三來源
兩個委派 `-006`、一個委派 `-004`（非「全委派 `-004`」）；`-007` 之「握手序列」與 `-013` 之「訊息名／值逐字」
於來源無載，不造 —— 前者改驗來源所載之 LVDS 影像接收，後者訊息內容標 `PENDING: DR-CAM-t`（本包新開）。

`coverage.tsv` 之 4 列改為 `PRODUCED`、`tc_count = 1`；A 本 `tc_count` 合計 245 → **249**。

| TC ID | req | 來源 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVC-246` | `SWE-CAM-007` | §— | LVDS image reception, read the LVDS link and check that  | 功能測試 | VF(ProMaster)637 | — | P2 |
| `NR1L-RVC-247` | `SWE-CAM-013` | §— | DTC read over LVDS, read the DTC list and check that the | 功能測試 | VF(ProMaster)637 | DR-CAM-t | P1 |
| `NR1L-RVC-248` | `SWE-CAM-024` | §— | AUX camera softkeys, view transitions and timers, pendin | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-a | P1 |
| `NR1L-RVC-249` | `SWE-CAM-025` | §— | bed extender active while the image is shown, read the H | 狀態轉換 | Toro(2261) | DR-CAM-f, DR-CAM-h | P1 |

## 自檢與 lint

- `selfcheck_camera.py`：ERROR 級十項**全 0**；第 1 項**共引錨 3**（`-246`／`-247`／`-249`，R-CAM19(b)）、**缺件佔位 1**（`-248`，R-CAM19(d)）——
  兩類為本包新增之計數類別（selfcheck 修訂見上繳 CAM-26 §2-3）。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `U` 11（`-247` 2／`-248` 6／`-249` 3）、`I-cross` 4。
