# INDEX — batch05（A 本拆解審計之補生成，下放包 CAM-24 §2）

CAM-23 §3 之 A 本覆核查得 **H 1／M 2**，依 **DECISIONS 6-78** 補生成 **5 列**
（下放包預估 4，亮度一項實出兩列，見下）｜TC ID `NR1L-RVC-241`～`-245`｜
計畫 `features/camera/data/batch05_plan.tsv`。**既有 240 列不改**。

| 審計項 | 母列 | 來源列 | 補列 | 驗證點 |
|---|---|---|---|---|
| §3 #1（H）| `NR1L-RVC-017` | `SYS-RA-VF551_V2-496` | `-241` | any-of 之 `VehicleSpeedVSOSig >= c_VEHSPD_MAX` 退出 |
| §3 #1（H）| `NR1L-RVC-017` | 同上 | `-242` | any-of 之 `RVC_ImageDefeat.Req = Pressed` 退出 |
| §3 #2（M）| `NR1L-RVC-201` | `SYS-RA-VF551_V42-226` | `-243` | `Rear_Camera_Repetition.Data` 之複製 |
| §3 #3（M）| `NR1L-RVC-214` | `SYS-RA-VF551_V33-234` | `-244`／`-245` | 亮度 51 %（on-point）／49 %（off-point）|

**`-242` 不掛 DR-CAM-g**（下放包 §6-1 之升級條件不成立）——
`RVC_ImageDefeat.Req` 之 HMI 面已查得逐字來源：`SYS-RA-VF551_V2-549` 之
`… to defeat Rear View Camera View via **RVC Image soft button** and set internal Signal
RVC_ImageDefeat.Req = Pressed.`

**`-244`／`-245` 出兩列而非一列**：依下放包 §2 之「49% 併入同列之對照步不可（§8.3）」；
惟既有前例為一列兩點（`NR1L-RVCHMI-036`／`-111`），兩形制之取捨待裁（上繳 §7-1）。

`coverage.tsv` 之 3 個母 leaf 其 `tc_count`／`tc_ids`／`batch` 已同步（`SWE-CAM-015` 14→16、
`SWE-CAM-006` 17→18、`SWE-CAM-019` 2→4）；A 本 `tc_count` 合計 240 → **245**。

| TC ID | req | 來源 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVC-241` | `SWE-CAM-015` | §— | speed threshold exit, read the HU display and check that | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVC-242` | `SWE-CAM-015` | §— | image defeat exit, press the RVC Image soft button and c | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVC-243` | `SWE-CAM-006` | §— | video copy, read the camera service status and check tha | 功能測試 | VF(ProMaster)637 | — | P1 |
| `NR1L-RVC-244` | `SWE-CAM-019` | §— | brightness on-point, set the display brightness to 51 %  | 邊界值分析 | Toro(2261) | — | P2 |
| `NR1L-RVC-245` | `SWE-CAM-019` | §— | brightness off-point, set the display brightness to 49 % | 邊界值分析 | Toro(2261) | — | P2 |

## 自檢與 lint

- `selfcheck_camera.py`：ERROR 級十項**全 0**；第 10 項（WARN）候選 **0**。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `I-cross` 5、`J` 1。
  `J` 一列（`-243`）為 **profile §5.1 之逐字豁免** —— 其上半**自來源首 token 起**
  （`SYS-RA-VF551_V42-226` 全文即以小寫 `copy` 起首），符 6-65(a) 之要件，reasoning 已具名。
