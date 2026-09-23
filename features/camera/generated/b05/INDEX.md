# INDEX — b05（B 本尾批，下放包 CAM-20 §2）

**B 本至此 230/230 列全數處置。** 本批 **40 leaf／40 TC**｜
TC ID `NR1L-RVCHMI-158`～`-197`｜計畫 `features/camera/data/b05_plan.tsv`。

| Test Set | 章 | leaf | TC |
|---|---|---:|---:|
| `AUX Camera Settings`（B04b）| HU §34.9.1–§34.10.3 | 15 | `-158`～`-172` |
| `Warning Banners` | RVC+PAM §8.2–§8.4.1、§9.2–§9.2.3 | 12 | `-173`～`-184` |
| `PAM Integration` | RVC+PAM §6.2–§6.5、§8.8、§11.1 | 9 | `-185`～`-193` |
| `Camera Settings` | HU §6.2.2.1–§6.2.2.3 | 4 | `-194`～`-197` |
| **合計** | | **40** | **40** |

leaf 實測 40 ＝ 40（下放包 §2 之上限），**不切批**，升級條件 §4-1 不成立。
**零 TC：0 列** —— 本批四組之逐字同句掃描（§29/§30/§31/§34 與 RVC+PAM 全本）
**未得任何含本批章節之同句群**，R-CAM16(b)／(c) 皆不觸發。

**`Vehicle Model`**：29 列五款全 `1`；
`-172`（§34.10.3）**來源逐字點名** `DT and HDCC programs` → 只勾 Atl-Hi 兩欄（**R-CAM3**）；
`-185`～`-193`（PAM 九列）因前提用 `CVPAM_Presence`（byte 173 bit 1）而該 byte 於
`Toro_ATL_MI` 零命中 → **R-CAM18(b)** `Toro(2261)` = `0`。

**PENDING：5 列** —— `-169`／`-170`／`-171`／`-172`（`Camera App` 配備旗標，DR-CAM-r）、
`-184`（`Camera Out of Position` 文字查無，**DR-CAM-h**）。

| TC ID | req | SYS1 章節 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVCHMI-158` | `SWE1-RVC-148` | §34.9.1 | the individual AUX Cam settings popup opens from the lin | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-159` | `SWE1-RVC-149` | §34.9.2.1 | the R1 Low AUX settings popup offers Edit the name of th | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-160` | `SWE1-RVC-150-01` | §34.9.2.2 | Reset Camera returns the name to the AUX Camera default | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-161` | `SWE1-RVC-150-02` | §34.9.2.2 | the soft controls read AUX 1 and AUX 2 after the reset | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-162` | `SWE1-RVC-151` | §34.9.4 | pressing Edit Favorite from the R1 Low AUX Cam settings  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-163` | `SWE1-RVC-152-01` | §34.9.5 | the R1 Low camera name is limited to 7 characters per li | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-164` | `SWE1-RVC-152-02` | §34.9.5 | the R1 Low camera name is truncated at 2 lines and 14 ch | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-165` | `SWE1-RVC-152-03` | §34.9.5 | a full word that fits is not truncated on R1 Low | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-166` | `SWE1-RVC-153` | §34.9.6 | the QWERTY keyboard opens and typing overwrites the defa | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-167` | `SWE1-RVC-154` | §34.9.7 | the R1 Low settings menu title reads the new name after  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-168` | `SWE1-RVC-155` | §34.9.8 | the updated name is reflected in the R1 Low settings men | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-169` | `SWE1-RVC-156` | §34.9.9 | the updated name is reflected on the R1 Low camera app h | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-170` | `SWE1-RVC-157` | §34.10.1 | only the AUX cameras connected to the system are accessi | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P1 |
| `NR1L-RVCHMI-171` | `SWE1-RVC-158` | §34.10.2 | tapping a soft control in the Camera App AUX shows that  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P1 |
| `NR1L-RVCHMI-172` | `SWE1-RVC-159` | §34.10.3 | DT and HDCC with SVC and camera app have no AUX access v | 負向測試 | HDCC27, DT27 | DR-CAM-r | P2 |
| `NR1L-RVCHMI-173` | `SWE1-RVC-026` | §8.2 | the Check Entire Surroundings message is displayed for 5 | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-174` | `SWE1-RVC-027` | §8.3 | the banner fades out towards the edges and does not cove | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-175` | `SWE1-RVC-028` | §8.3.1 | the fade out banner applies to any message shown in the  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-176` | `SWE1-RVC-029` | §8.3.2 | turning off the rear view camera returns the user to the | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-177` | `SWE1-RVC-030` | §8.3.3 | the camera delay option is not supported when the X cann | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-178` | `SWE1-RVC-031-01` | §8.4 | the X button and the banners are white with a background | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-179` | `SWE1-RVC-031-02` | §8.4 | objects overlaid on the camera image are 60 percent tran | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-180` | `SWE1-RVC-032` | §8.4.1 | overlaying is used only when the UI elements cannot othe | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-181` | `SWE1-RVC-036` | §9.2 | Check Entire Surroundings is shown for 5 seconds then th | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-182` | `SWE1-RVC-037` | §9.2.1 | Camera System Unavailable is displayed for an event that | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-183` | `SWE1-RVC-038` | §9.2.2 | Camera System Unavailable is displayed for an event that | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-184` | `SWE1-RVC-039` | §9.2.3 | Camera Out of Position is displayed when the camera is o | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-h | P1 |
| `NR1L-RVCHMI-185` | `SWE1-RVC-001` | §6.2 | the PAM content follows the proxy configuration | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P1 |
| `NR1L-RVCHMI-186` | `SWE1-RVC-002-01` | §6.2.1 | the PAM features are not mutually exclusive | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P1 |
| `NR1L-RVCHMI-187` | `SWE1-RVC-002-02` | §6.2.1 | adding a PAM functionality adds its visualization logic | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P1 |
| `NR1L-RVCHMI-188` | `SWE1-RVC-003` | §6.2.2 | the expected PAM feature set is Rear ParkSense Front plu | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-189` | `SWE1-RVC-004` | §6.3 | the flashing lines use the same flash frequency as the c | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-190` | `SWE1-RVC-005` | §6.4 | the ParkSense indications on the HU are consistent with  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-191` | `SWE1-RVC-006` | §6.5 | the audible PAM indications are driven over CAN and foll | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-192` | `SWE1-RVC-035` | §8.8 | the PAM graphic matches the current vehicle configuratio | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P2 |
| `NR1L-RVCHMI-193` | `SWE1-RVC-040` | §11.1 | the PAM visualization graphics adapt to the vehicle prox | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P1 |
| `NR1L-RVCHMI-194` | `SWE1-RVC-045` | §6.2.2.1 | Rear View Camera Delay holds the image for 10 seconds or | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-195` | `SWE1-RVC-046` | §6.2.2.2 | Rear View Camera Active Guidelines toggles the dynamic g | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-196` | `SWE1-RVC-047-01` | §6.2.2.3 | Rear View Camera Fixed Guidelines toggles the fixed guid | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-197` | `SWE1-RVC-047-02` | §6.2.2.3 | only one type of guidelines can be chosen at a time | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |

## 自檢與 lint

- `selfcheck_camera.py` 十項：**全 0**（TC 40 筆、錨 40 個、反查失敗 0）。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `U` 5／`I-cross` 40／`X` 4。
- `Z`（Vehicle Model 七欄，R-CAM2）：**0**｜`J`：**0**。
