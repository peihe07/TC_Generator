# INDEX — pilot01（下放包 CAM-03 §3）

Test Group：`Rear View Camera`（R-CAM4(a)）｜TC ID：`NR1L-RVC-001` ～ `NR1L-RVC-009`（R-CAM4(b)）

| TC ID | req_id | Test Set | tc_title | 軸 | Vehicle Model = 1 | priority |
|---|---|---|---|---|---|---|
| `NR1L-RVC-001` | `SWE-CAM-001` | Startup and Shutdown | NormalCameraDaemon starts the camera data path after ignition RUN | — | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | P0 |
| `NR1L-RVC-002` | `SWE-CAM-001` | Startup and Shutdown | NormalCameraDaemon tears down the camera data path at ignition pre-off | mode（開機／關機） | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | P1 |
| `NR1L-RVC-003` | `SWE-CAM-015` | Display Arbitration | Atl-Hi, automatic activation on TRANSM_FD_4 gear R | 車型（Atl-Hi） | HDCC27, DT27 | P0 |
| `NR1L-RVC-004` | `SWE-CAM-015` | Display Arbitration | Atl-Mi, automatic activation on STATUS_CCAN4 reverse gear | 車型（Atl-Mi） | VF(ProMaster)637, Toro(2261), Fastack (376) | P0 |
| `NR1L-RVC-005` | `SWE-CAM-016` | Display Arbitration | manual activation via App Drawer while not in reverse | mode（手動開啟） | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | P1 |
| `NR1L-RVC-006` | `SWE-CAM-016` | Display Arbitration | manual close via the X exit button returns to the previous content | mode（手動關閉） | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | P1 |
| `NR1L-RVC-007` | `SWE-CAM-018` | Display Arbitration | Ram brand label, camera delay holds the image for 10 s below 8 mph | 品牌（RAM 系） | HDCC27, DT27, VF(ProMaster)637 | P1 |
| `NR1L-RVC-008` | `SWE-CAM-018` | Display Arbitration | Fiat brand label, camera delay holds the image for 10 s below 8 mph | 品牌（基礎） | Toro(2261), Fastack (376) | P1 |
| `NR1L-RVC-009` | `SWE-CAM-018` | Display Arbitration | Atl-Hi, timer starts at the first raw speed value that reaches c_VEHSPD_MAX | 邊界（車速門檻） | HDCC27, DT27 | P1 |

全部 9 列之 `Commander (598)` 與 `Regengade (5210)` 皆為 `0`（R-CAM2(b)）。
