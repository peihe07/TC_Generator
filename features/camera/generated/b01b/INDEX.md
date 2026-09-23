# INDEX — b01b（`Activation and Exit` 後 20 leaf，下放包 CAM-15 §4）

B 本第 2 批，**`Activation and Exit` 組至此 43/43 leaf 全數產出**。
`SWE1-RVC-015`～`-018`（RVC+PAM §7.3–§7.3.3）、`-019` 家族（§7.4）、`-020`～`-023` 家族（§7.5–§7.5.3）、
`-024`／`-025` 家族（§8.1／§8.1.1）、`-033`（§8.6）、`-034`（§8.7）＝ **20 列**｜
TC ID `NR1L-RVCHMI-024`～`-043`｜計畫 `features/camera/data/b01b_plan.tsv`。

`§7.3.1`～`§7.3.3` 三列（`-025`／`-026`／`-027`）**只存在於 `spec-index/cache/` 本**
（**A-CA14**／**R-CAM6**），REF 本無之。

**PENDING：0 列** —— 本批之配備旗標（`CVPAM_Presence`、`Radio_Display_Type`）與
計時值（10 秒）、門檻值（8 mph）皆有來源，不需 DR。
**`Toro(2261)` = 0 之 5 列**（`-024`／`-025`／`-026`／`-027`／`-031`）：其 PROXI byte
（byte 173 bit 1 `CVPAM_Presence`、byte 185 bit 0–3 `Radio_Display_Type`）於
`Toro_ATL_MI` 之 2019 本零命中，依 **R-CAM18(b)** 判 0。

| TC ID | req | SYS1 章節 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVCHMI-024` | `SWE1-RVC-015` | §7.3 | RVC-only layout does not appear when PAM is offered and  | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-025` | `SWE1-RVC-016` | §7.3.1 | fallback to RVC-only layout when the vehicle offers no P | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P1 |
| `NR1L-RVCHMI-026` | `SWE1-RVC-017` | §7.3.2 | fallback to RVC-only layout on 7 inch and 8.4 inch head  | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P1 |
| `NR1L-RVCHMI-027` | `SWE1-RVC-018` | §7.3.3 | vehicle controls provided in the RVC-only layout on 10.1 | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-028` | `SWE1-RVC-019-01` | §7.4 | initial view on activation is the default view for the c | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-029` | `SWE1-RVC-019-02` | §7.4 | image remains displayed while vehicle speed is below the | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-030` | `SWE1-RVC-019-03` | §7.4 | soft button greyed out when vehicle speed is above the t | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-031` | `SWE1-RVC-019-04` | §7.4 | pushing the button displays both the RVC image and the s | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-032` | `SWE1-RVC-020` | §7.5 | layout does not disappear while none of the dismissal co | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-033` | `SWE1-RVC-021` | §7.5.1 | dismissal in D above the speed threshold and the 10 seco | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-034` | `SWE1-RVC-022` | §7.5.2 | dismissal once the gear is not R and the RVC timeout exp | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-035` | `SWE1-RVC-023-01` | §7.5.3 | 10 second delay timer starts immediately on the shift ou | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-036` | `SWE1-RVC-023-02` | §7.5.3 | auto dismissal when the vehicle speed reaches the 8 mph  | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-037` | `SWE1-RVC-023-03` | §7.5.3 | manual dismissal via the X soft control during the delay | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-038` | `SWE1-RVC-024-01` | §8.1 | X exit button placed in the upper-right corner in gears  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-039` | `SWE1-RVC-024-02` | §8.1 | X exit button reverts the head unit to the last known di | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-040` | `SWE1-RVC-025-01` | §8.1.1 | RVC feed stays on while the vehicle remains in REVERSE | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-041` | `SWE1-RVC-025-02` | §8.1.1 | X button not available while the vehicle is in REVERSE | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-042` | `SWE1-RVC-033` | §8.6 | camera displayed while the radio is off and the on-condi | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-043` | `SWE1-RVC-034` | §8.7 | no camera image in accessory mode and display restored i | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |

## 自檢與 lint

- `selfcheck_camera.py` 十項：**全 0**（TC 20 筆、錨 20 個、反查失敗 0）。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `I-cross` 20（`U`／`X`／`J` 皆 0）。
- `Z`（Vehicle Model 七欄，R-CAM2）：**0**。
