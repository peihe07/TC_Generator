# INDEX — b01a（`Activation and Exit` 前 23 leaf，下放包 CAM-14 §3 ＋ CAM-15 §3）

B 本首批。`SWE1-RVC-041`～`-052`（HeadUnitCameraSystems §6.1.2–§6.10.1，14 列）
＋ `SWE1-RVC-007`／`-008` 家族（RVC+PAM §7.1–§7.2.6，9 列）＝ **23 列**｜
TC ID `NR1L-RVCHMI-001`～`-023`｜計畫 `features/camera/data/b01a_plan.tsv`。

Test Group：`Rear View Camera`｜Test Set：全 23 列 `Activation and Exit`。
`specification_reference` ＝ `{SYS1 檔名}_{章節號}`（DECISIONS 6-48 之 token 化：只換空白）；
`-008-0n` 六列依 **CAM-14 審閱 §一-3**（**A-CA33**）寫該 TC 直接驗證之章節 `…_7.2.1`～`…_7.2.6`，
037 收摺為 `_7.2` 之事實只反映於 D 欄之 `req_id`。
`test_item` 上半為 SYS1 `Description` 逐字（母體依 **R-CAM6** 取 `spec-index/cache/` 兩本）。

**CAM-15 §3 補列**：`-008-06`（§7.2.6）生成 `NR1L-RVCHMI-023`，B01a 由 22 列改 23 列
（CAM-14 審閱 §一-4：不切開 §7.2 家族）。`Activation and Exit` 之其餘 20 leaf 落 `b01b/`。

umbrella 列不生成，記於 `features/camera/data/coverage_b.tsv`。

| TC ID | req | SYS1 章節 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVCHMI-001` | `SWE1-RVC-041` | §6.1.2 | camera delay option not offered when the X exit button c | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-002` | `SWE1-RVC-042` | §6.1.3 | camera feed not available in the OFF and ACC ignition st | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-003` | `SWE1-RVC-043` | §6.1.5 | rear view is non-persistent when the Enhanced Camera App | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-004` | `SWE1-RVC-044` | §6.1.6 | rear view follows the general camera activation and deac | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-005` | `SWE1-RVC-048-01` | §6.5.1 | manual activation via the controls page | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-g | P1 |
| `NR1L-RVCHMI-006` | `SWE1-RVC-048-02` | §6.5.1 | manual activation via the apps drawer | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-007` | `SWE1-RVC-048-03` | §6.5.1 | manual activation via the camera app home page | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P1 |
| `NR1L-RVCHMI-008` | `SWE1-RVC-049` | §6.5.2 | rear view soft control in the view corner without Surrou | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-009` | `SWE1-RVC-050` | §6.5.3 | rear view not accessible on the controls page when the c | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-g;DR-CAM-r | P2 |
| `NR1L-RVCHMI-010` | `SWE1-RVC-051-01` | §6.7.1 | rear view via the controls page with enhanced camera app | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-g;DR-CAM-r | P2 |
| `NR1L-RVCHMI-011` | `SWE1-RVC-051-02` | §6.7.1 | rear view via the apps drawer with enhanced camera app a | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-012` | `SWE1-RVC-051-03` | §6.7.1 | SVC bar present in the rear view with enhanced camera ap | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-013` | `SWE1-RVC-051-04` | §6.7.1 | X exit control offered in P, N and D and not in R | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-014` | `SWE1-RVC-052` | §6.10.1 | soft control access in the corner of each equipped camer | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-015` | `SWE1-RVC-007-01` | §7.1 | camera display takes priority over the screen currently  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-016` | `SWE1-RVC-007-02` | §7.1 | wake up from thermal protection display off to show the  | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-s | P2 |
| `NR1L-RVCHMI-017` | `SWE1-RVC-008` | §7.2 | layout does not appear when none of the enumerated trigg | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-018` | `SWE1-RVC-008-01` | §7.2.1 | layout appears when R is engaged | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-019` | `SWE1-RVC-008-02` | §7.2.2 | layout stays on the R to D transition when the RVC delay | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-020` | `SWE1-RVC-008-03` | §7.2.3 | camera feed displayed immediately after the shift into R | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-021` | `SWE1-RVC-008-04` | §7.2.4 | camera feed stays displayed until the vehicle is shifted | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-022` | `SWE1-RVC-008-05` | §7.2.5 | layout launched from the associated button in the Contro | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-g | P2 |
| `NR1L-RVCHMI-023` | `SWE1-RVC-008-06` | §7.2.6 | layout launched from the Camera shortcut icon in the Sta | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-g | P2 |

## 自檢與 lint

- `selfcheck_camera.py` 十項：**全 0**（TC 23 筆、錨 23 個、反查失敗 0）。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `U` 18／`I-cross` 23／`X` 5。
  `X` 五列之導航標的為 `Controls screen`／`Status bar Shortcut menu`，其入口即 **DR-CAM-g**。
- `Z`（Vehicle Model 七欄，R-CAM2）：**0**｜`J`：**0**。
