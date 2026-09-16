# INDEX — batch01（Display Arbitration，下放包 CAM-05 §3）

Test Group：`Rear View Camera`｜TC ID `NR1L-RVC-011`～`-033`（23 列）｜計畫 `features/camera/data/batch01_plan.tsv`

| TC ID | req | tc_title | 軸 | Vehicle Model = 1 | spec_reference | P |
|---|---|---|---|---|---|---|
| `NR1L-RVC-011` | `SWE-CAM-015` | Atl-Hi | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_484` | P1 |
| `NR1L-RVC-012` | `SWE-CAM-015` | Atl-Mi | 狀態轉換 | VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V3_P363_VF_484` | P1 |
| `NR1L-RVC-013` | `SWE-CAM-015` | Atl-Hi | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1065` | P1 |
| `NR1L-RVC-014` | `SWE-CAM-015` | Atl-Mi | 狀態轉換 | VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V3_P363_VF_1098` | P1 |
| `NR1L-RVC-015` | `SWE-CAM-015` | Atl-Hi | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_479` | P1 |
| `NR1L-RVC-016` | `SWE-CAM-015` | Atl-Mi | 狀態轉換 | VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V3_P363_VF_1099` | P1 |
| `NR1L-RVC-017` | `SWE-CAM-015` | ignition exit | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V2_PHDCC27_VF_1576` | P1 |
| `NR1L-RVC-018` | `SWE-CAM-015` | park exit | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V2_PHDCC27_VF_1576` | P1 |
| `NR1L-RVC-019` | `SWE-CAM-015` | Reverse_Deb met | 邊界值分析 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1378` | P1 |
| `NR1L-RVC-020` | `SWE-CAM-015` | Reverse_Deb not met | 邊界值分析 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1378` | P2 |
| `NR1L-RVC-021` | `SWE-CAM-015` | X overlaid out of R | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V2_PHDCC27_VF_1442` | P2 |
| `NR1L-RVC-022` | `SWE-CAM-015` | no interrupt in R | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V2_PHDCC27_VF_1442` | P2 |
| `NR1L-RVC-023` | `SWE-CAM-016` | soft key gated by RUN | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `CFTS092-4781638` | P1 |
| `NR1L-RVC-024` | `SWE-CAM-016` | soft key not IGN_RUN | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `CFTS092-4781639` | P1 |
| `NR1L-RVC-025` | `SWE-CAM-016` | RVC_SK_PRSNT present | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `CFTS092-4781637` | P2 |
| `NR1L-RVC-026` | `SWE-CAM-016` | manual mode above threshold | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V3_P363_VF_1100` | P1 |
| `NR1L-RVC-027` | `SWE-CAM-016` | zoom soft button | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V2_PHDCC27_VF_534` | P3 |
| `NR1L-RVC-028` | `SWE-CAM-018` | softkey disable | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `CFTS092-4781642` | P1 |
| `NR1L-RVC-029` | `SWE-CAM-018` | Ttimer2 reset | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V2_PHDCC27_VF_1765` | P2 |
| `NR1L-RVC-030` | `SWE-CAM-018` | 2261 on-point | 邊界值分析 | Toro(2261) | `VF551_V33_P226MCA_VF_532` | P1 |
| `NR1L-RVC-031` | `SWE-CAM-018` | 2261 off-point | 邊界值分析 | Toro(2261) | `VF551_V33_P226MCA_VF_532` | P1 |
| `NR1L-RVC-032` | `SWE-CAM-020` | bed extender active | 決策表 | Toro(2261) | `VF551_V33_P226MCA_VF_1603` | P1 |
| `NR1L-RVC-033` | `SWE-CAM-020` | incomplete bed extender | 決策表 | Toro(2261) | `VF551_V33_P226MCA_VF_1603` | P1 |

全部 23 列之 `Commander (598)` 與 `Regengade (5210)` 皆為 `0`（R-CAM2(b)）。
