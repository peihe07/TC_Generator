# INDEX — b08（R-CAM19 追溯補齊，下放包 CAM-26 §2）

**R-CAM19(c)** 撤銷 R-CAM16(c) 之零 TC 形制（逐字重複／純交叉引用），R-CAM16(b)（自陳 N/A）之列亦須出 TC。
B 本原零 TC 之 **6 列**各出一列｜TC ID `NR1L-RVCHMI-211`～`-216`｜計畫 `features/camera/data/b08_plan.tsv`。
**既有 210 列不改**。

| 需求 | 章 | 原處置 | 本批 | 驗證角度 | 被引／母列 |
|---|---|---|---|---|---|
| `SWE1-RVC-069` | §27.3.2 | 自陳 N/A（R-CAM16(b)，A-CA35）| `-211` | 父題 §27.3 之 R1 High 硬體條件 → `Enable Wireless Cameras` 設定之提供 | `NR1L-RVCHMI-063`（路徑）|
| `SWE1-RVC-086` | §27.7.3 | 純交叉引用（R-CAM16(c)(ii)）| `-212` | App Drawer 入口 × §27.5.2（自動啟用、無彈窗）| `NR1L-RVCHMI-071` |
| `SWE1-RVC-091` | §27.8.5 | 純交叉引用 | `-213` | 後視影像 `More Aux` 入口 × §27.6.1（投影中 → `PU1518`）| `NR1L-RVCHMI-072` |
| `SWE1-RVC-102` | §28.6.1.2 | 純交叉引用 | `-214` | R 檔 `More Cams` 入口 × §27.5.1（休眠 → `connecting`，`PENDING: DR-CAM-h`）| `NR1L-RVCHMI-070` |
| `SWE1-RVC-136` | §34.4.2 | 逐字重複 §34.3.2（R-CAM16(c)(i)）| `-215` | 沿母列（父題亦全等，來源無可分辨之文字）| `NR1L-RVCHMI-086` |
| `SWE1-RVC-139` | §34.6.1 | 逐字重複 §34.4.1 | `-216` | 沿母列之否定命題；**父題相異**（`Backup and Cargo Cam`）記於 reasoning | `NR1L-RVCHMI-087` |

**與下放包 §2 之出入**：`-136`／`-139` 之「前提改 R1 Low」—— 兩列與母列同在 §34（`R1 Low Wired AUX Cameras`），
母列前提已為 R1 Low，故全沿母列。`-216` 之車型依 R-CAM18(b) 實測為 HDCC27／DT27 兩款
（`Digital_CHMSL_Camera_Prsnt` 只在 Atl-Hi 三本），與母列 `-087` 之五款不同 —— 母列不改，登 **A-CA39**。

`coverage_b.tsv` 之 6 列改為 `PRODUCED`；B 本 210 → **216**。

| TC ID | req | 來源 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVCHMI-211` | `SWE1-RVC-069` | §27.3.2 | the Enable Wireless Cameras setting is offered on a head | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-212` | `SWE1-RVC-086` | §27.7.3 | a wireless AUX camera selected from the App Drawer enabl | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-213` | `SWE1-RVC-091` | §27.8.5 | a wireless AUX camera selected from the More Aux pop-up  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-214` | `SWE1-RVC-102` | §28.6.1.2 | a connecting message is shown when a sleeping wireless A | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | DR-CAM-h | P2 |
| `NR1L-RVCHMI-215` | `SWE1-RVC-136` | §34.4.2 | the X control is not present in the back-up camera only  | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-216` | `SWE1-RVC-139` | §34.6.1 | no camera entry is offered for a CHMSL camera only confi | 負向測試 | HDCC27, DT27 | — | P2 |

## 自檢與 lint

- `selfcheck_camera.py`：ERROR 級十項**全 0**；第 10 項（WARN）候選 1（`-216` `negative`，同母列 `-087` 之型）。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `U` 1（`-214`）、`I-cross` 6。
