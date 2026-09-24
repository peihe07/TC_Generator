# INDEX — b02b（`AUX Camera Access` 後 29 leaf，下放包 CAM-17 §2）

B 本第 4 批，**`AUX Camera Access` 組至此 60/60 leaf 全數處置**。
`SWE1-RVC-083`～`-091`（§27.6.2–§27.8.5）＋ `-129`～`-147`（§34.1.1.1–§34.8.4）＝ **29 leaf**，
產 **25 TC**｜TC ID `NR1L-RVCHMI-074`～`-098`｜計畫 `features/camera/data/b02b_plan.tsv`。

**4 列零 TC（A-CA36／RDF-14，提請裁）**：

| 列 | 章 | 事由 |
|---|---|---|
| `SWE1-RVC-086` | §27.7.3 | 純交叉引用 `refer to ‘Wireless cameras connection’ pages`，標的 §27.5／§27.6 已有 TC |
| `SWE1-RVC-091` | §27.8.5 | 同上 |
| `SWE1-RVC-136` | §34.4.2 | 與 §34.3.2（`-086`）逐字全等**且父題全等**（原始格亦全等），委派 |
| `SWE1-RVC-139` | §34.6.1 | 與 §34.4.1（`-087`）逐字全等，委派章節號較小者 |

**§34 ＝ `R1 Low Wired AUX Cameras`**（章標題逐字，`NRL-188152`），與 §27 之
`R1 High Wired &Wireless Auxiliary Cameras` 成對。八群 §27↔§34 逐字同句之列**各自出 TC** ——
HU 等級不同（R1 Low 只有有線 AUX）。HU 等級**無 PROXI 編碼**（六串六本各 0 命中），
依下放包 §2 不以此判車型，前提以散文書寫（profile §7.3）。

**`Vehicle Model`**：18 列五款全 `1`；**7 列**只勾 `HDCC27`／`DT27` ——
`-092`（§34.7.1）**來源逐字點名** `DT and HDCC programs`（**R-CAM3**）；
其餘 6 列因 `Digital_CHMSL_Camera_Prsnt`（byte 222 bit 7）於三本 Atl-Mi 零命中（**R-CAM18(b)**）。

| TC ID | req | SYS1 章節 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVCHMI-074` | `SWE1-RVC-083` | §27.6.2 | a connecting message is shown after the projection popup | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-h | P2 |
| `NR1L-RVCHMI-075` | `SWE1-RVC-084` | §27.7.1 | wired and wireless AUX cameras are accessible from the c | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-g | P1 |
| `NR1L-RVCHMI-076` | `SWE1-RVC-085` | §27.7.2 | AUX soft controls are not on the controls page when the  | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-g;DR-CAM-r | P2 |
| `NR1L-RVCHMI-077` | `SWE1-RVC-087` | §27.8.1 | the More Aux button opens a popup listing all available  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-078` | `SWE1-RVC-088` | §27.8.2 | selecting a new view in the popup switches to that view | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-079` | `SWE1-RVC-089` | §27.8.3 | pressing More AUX again closes the popup | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-080` | `SWE1-RVC-090` | §27.8.4 | signal strength and battery are indicated below the More | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-081` | `SWE1-RVC-129` | §34.1.1.1 | AUX controls on the second surface of the back-up and CH | 功能測試 | HDCC27, DT27 | — | P2 |
| `NR1L-RVCHMI-082` | `SWE1-RVC-130` | §34.1.2.1 | AUX Cameras icons exist in the camera views on R1 Low | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-083` | `SWE1-RVC-131` | §34.1.3.1 | the AUX cam is always a selectable field on R1 Low | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-084` | `SWE1-RVC-132` | §34.1.4.1 | camera personalization settings are grouped under the Ca | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-085` | `SWE1-RVC-133` | §34.1.5.1 | the R1 Low camera feature set is RearView Camera Cargo C | 決策表 | HDCC27, DT27 | — | P2 |
| `NR1L-RVCHMI-086` | `SWE1-RVC-134` | §34.3.2 | the X control is not present when the view is entered by | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-087` | `SWE1-RVC-135` | §34.4.1 | a CHMSL camera only configuration is not offered | 負向測試 | HDCC27, DT27（CAM-27 §2 補正，A-CA39）| — | P2 |
| `NR1L-RVCHMI-088` | `SWE1-RVC-137` | §34.4.3 | the AUX Cam button always lands on the Aux 1 screen | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-089` | `SWE1-RVC-138` | §34.6 | AUX cameras are accessible from the back-up and the carg | 功能測試 | HDCC27, DT27 | — | P2 |
| `NR1L-RVCHMI-090` | `SWE1-RVC-140` | §34.6.2 | the X control is not present when the cargo configuratio | 負向測試 | HDCC27, DT27 | — | P1 |
| `NR1L-RVCHMI-091` | `SWE1-RVC-141` | §34.6.3 | the same AUX access behaviour applies when starting from | 功能測試 | HDCC27, DT27 | — | P2 |
| `NR1L-RVCHMI-092` | `SWE1-RVC-142` | §34.7.1 | DT and HDCC with SVC and camera app have no AUX access v | 負向測試 | HDCC27, DT27 | DR-CAM-r | P2 |
| `NR1L-RVCHMI-093` | `SWE1-RVC-143-01` | §34.7.2 | the X control is not available in REVERSE except when it | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-094` | `SWE1-RVC-143-02` | §34.7.2 | a camera image is always up while the vehicle is in REVE | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-095` | `SWE1-RVC-144` | §34.8.1 | the AUX button always lands on the AUX 1 screen when cam | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-096` | `SWE1-RVC-145` | §34.8.2 | a blue camera system unavailable screen is displayed whe | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-097` | `SWE1-RVC-146` | §34.8.3 | AUX 2 can be selected from the unavailable screen when o | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-098` | `SWE1-RVC-147` | §34.8.4 | the same not-connected behaviour applies when starting f | 功能測試 | HDCC27, DT27 | — | P2 |

## 自檢與 lint

- `selfcheck_camera.py` 十項：**全 0**（TC 25 筆、錨 25 個、反查失敗 0）。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `U` 7／`I-cross` 25／`X` 3。
- `Z`（Vehicle Model 七欄，R-CAM2）：**0**｜`J`：**0**。
