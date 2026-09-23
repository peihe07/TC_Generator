# INDEX — b06（拆解審計之補生成，下放包 CAM-23 §2）

CAM-22 之拆解審計查得 **H 2 列／M 4 列**，依 **DECISIONS 6-74** 全數補生成，
追加 **9 列**｜TC ID `NR1L-RVCHMI-198`～`-206`｜計畫 `features/camera/data/b06_plan.tsv`。
**既有 197 列不改**，本批皆為新列（保持一列一驗證點）。

| 審計項 | 母列 | 章 | 補列 | 事由 |
|---|---|---|---|---|
| §5 #1（H）| `NR1L-RVCHMI-056` | §27.2.6.1 | `-198`～`-201`（4）| 五款配備之列舉以單一 ER 概括；母列留 RVC，四款各一列 |
| §5 #2（H）| `NR1L-RVCHMI-044` | §27.1.1 | `-202` | `wired and wireless` 而母列只佈有線；本列佈無線 |
| §5 #3（M）| `NR1L-RVCHMI-033` | §7.5.1 | `-203` | 10 秒窗只驗上界；本列驗 9 秒之下界 |
| §5 #4（M）| `NR1L-RVCHMI-085` | §34.1.5.1 | `-204` | `Apps Page` 只被當入口用；本列以其為驗證標的 |
| §5 #5（M）| `NR1L-RVCHMI-109` | §28.6.1.1 | `-205` | `Neutral or Drive` 只驗 Neutral；本列驗 Drive |
| §5 #6（M）| `NR1L-RVCHMI-196` | §6.2.2.3 | `-206` | `fixed guidelines or no guidelines` 只驗 On；本列驗 Off |

`coverage_b.tsv` 之母 leaf 其 `tc_id` 欄已追加本批之 TC ID（6 列），`batch` 欄加 `;b06`。

| TC ID | req | SYS1 章節 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVCHMI-198` | `SWE1-RVC-065` | §27.2.6.1 | the CHMSL Cargo Camera is offered on the Camera app home | 決策表 | HDCC27, DT27 | — | P2 |
| `NR1L-RVCHMI-199` | `SWE1-RVC-065` | §27.2.6.1 | Trailer Reverse Guidance is offered on the Camera app ho | 決策表 | HDCC27, DT27 | — | P2 |
| `NR1L-RVCHMI-200` | `SWE1-RVC-065` | §27.2.6.1 | the FFCTL camera is offered on the Camera app home page  | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-201` | `SWE1-RVC-065` | §27.2.6.1 | Vehicle Surround View is offered on the Camera app home  | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-202` | `SWE1-RVC-053` | §27.1.1 | the wireless AUX view is non-persistent and latching wit | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-203` | `SWE1-RVC-021` | §7.5.1 | the layout is still displayed 9 seconds after the manual | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-204` | `SWE1-RVC-133` | §34.1.5.1 | the Apps Page is offered as one of the R1 Low camera acc | 功能測試 | HDCC27, DT27 | — | P2 |
| `NR1L-RVCHMI-205` | `SWE1-RVC-101` | §28.6.1.1 | More Cams allows leaving the camera views when the gear  | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P1 |
| `NR1L-RVCHMI-206` | `SWE1-RVC-047-01` | §6.2.2.3 | setting Rear View Camera Fixed Guidelines to Off removes | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |

## 自檢與 lint

- `selfcheck_camera.py`：ERROR 級十項**全 0**；第 10 項（WARN）之候選見全案統計。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `U` 1／`I-cross` 9。
- `Z`／`J`／`X`：**0**。
