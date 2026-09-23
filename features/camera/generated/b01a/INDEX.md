# INDEX — b01a（`Activation and Exit` 前 22 leaf，下放包 CAM-14 §3）

B 本首批。`SWE1-RVC-041`～`-052`（HeadUnitCameraSystems §6.1.2–§6.10.1，14 列）
＋ `SWE1-RVC-007`／`-008` 家族（RVC+PAM §7.1–§7.2，8 列）＝ **22 列**｜
TC ID `NR1L-RVCHMI-001`～`-022`｜計畫 `features/camera/data/b01a_plan.tsv`。

Test Group：`Rear View Camera`｜Test Set：全 22 列 `Activation and Exit`。
`specification_reference` ＝ `{SYS1 檔名}_{章節號}`（DECISIONS 6-48 之 token 化：只換空白）。
`test_item` 上半為 SYS1 `Description` 逐字（母體依 **R-CAM6** 取 `spec-index/cache/` 兩本）。

**切點落在 §7.2 家族內** —— `Activation and Exit` 之 43 leaf 依 SYS1 章節序取前 22，
第 23 列為 `SWE1-RVC-008-06`（§7.2.6，Camera shortcut icon 一支），落 B01b。
下放包 §3 所列之 `7.3.1`～`7.3.3`（`SWE1-RVC-016`／`-017`／`-018`）依同一章節序為第 25～27 列，
**不在 B01a**；見上繳 §3-3。

umbrella 列（`SWE1-RVC-007`／`-047`／`-048`／`-051`）不生成，記於 `features/camera/data/coverage_b.tsv`。

| TC ID | req | SYS1 章節 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVCHMI-001` | `SWE1-RVC-041` | §6.1.2 | camera delay option not offered when the X exit butt | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-002` | `SWE1-RVC-042` | §6.1.3 | camera feed not available in the OFF and ACC ignitio | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-003` | `SWE1-RVC-043` | §6.1.5 | rear view is non-persistent when the Enhanced Camera | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-004` | `SWE1-RVC-044` | §6.1.6 | rear view follows the general camera activation and  | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-005` | `SWE1-RVC-048-01` | §6.5.1 | manual activation via the controls page | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-g | P1 |
| `NR1L-RVCHMI-006` | `SWE1-RVC-048-02` | §6.5.1 | manual activation via the apps drawer | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-007` | `SWE1-RVC-048-03` | §6.5.1 | manual activation via the camera app home page | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P1 |
| `NR1L-RVCHMI-008` | `SWE1-RVC-049` | §6.5.2 | rear view soft control in the view corner without Su | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-009` | `SWE1-RVC-050` | §6.5.3 | rear view not accessible on the controls page when t | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-g;DR-CAM-r | P2 |
| `NR1L-RVCHMI-010` | `SWE1-RVC-051-01` | §6.7.1 | rear view via the controls page with enhanced camera | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-g;DR-CAM-r | P2 |
| `NR1L-RVCHMI-011` | `SWE1-RVC-051-02` | §6.7.1 | rear view via the apps drawer with enhanced camera a | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-012` | `SWE1-RVC-051-03` | §6.7.1 | SVC bar present in the rear view with enhanced camer | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-013` | `SWE1-RVC-051-04` | §6.7.1 | X exit control offered in P, N and D and not in R | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-014` | `SWE1-RVC-052` | §6.10.1 | soft control access in the corner of each equipped c | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-015` | `SWE1-RVC-007-01` | §7.1 | camera display takes priority over the screen curren | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-016` | `SWE1-RVC-007-02` | §7.1 | wake up from thermal protection display off to show  | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-s | P2 |
| `NR1L-RVCHMI-017` | `SWE1-RVC-008` | §7.2 | layout does not appear when none of the enumerated t | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-018` | `SWE1-RVC-008-01` | §7.2（逐字 §7.2.1） | layout appears when R is engaged | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-019` | `SWE1-RVC-008-02` | §7.2（逐字 §7.2.2） | layout stays on the R to D transition when the RVC d | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-020` | `SWE1-RVC-008-03` | §7.2（逐字 §7.2.3） | camera feed displayed immediately after the shift in | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-021` | `SWE1-RVC-008-04` | §7.2（逐字 §7.2.4） | camera feed stays displayed until the vehicle is shi | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-022` | `SWE1-RVC-008-05` | §7.2（逐字 §7.2.5） | layout launched from the associated button in the Co | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-g | P2 |

## 自檢與 lint

- `selfcheck_camera.py` 十項：**全 0**（TC 22 筆、錨 22 個、反查失敗 0）。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `U` 16／`I-cross` 22／`X` 4。
  `X` 四列之成因同 batch01b —— 導航標的為 `Controls screen` 而入口本身即 **DR-CAM-g**。
- `Z`（Vehicle Model 七欄，R-CAM2）：**0**。
