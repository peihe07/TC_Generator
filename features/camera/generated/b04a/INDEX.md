# INDEX — b04a（`AUX Camera Settings` 之 §29–§31，下放包 CAM-19 §2）

B 本第 6 批。`SWE1-RVC-109`～`-125-03`（HeadUnitCameraSystems §29.1.1–§31.1.6）＝ **30 leaf／30 TC**｜
TC ID `NR1L-RVCHMI-128`～`-157`｜計畫 `features/camera/data/b04a_plan.tsv`。

**leaf 實測與切法**：`AUX Camera Settings` 全 53 列（leaf **45**／umbrella 8），45 > 40 故切兩批。
**切點取 §31.1.6 ↔ §34.9.1 之章界** —— 即 **§29–§31（R1 High，30 leaf）** 對
**§34.9–§34.10（R1 Low，15 leaf）**；非取「第 40 列」之機械切點。
其由：(a) 該處為 `R1 High` ↔ `R1 Low` 之章界，與 **DECISIONS 6-64** 之判準同軸；
(b) 第 40 列（`SWE1-RVC-154`，§34.9.7）落在 §34.9 之名稱編輯流程中段，切之會拆散該流程。
30 ≤ 43，升級條件 §4-1 不成立。**B04b ＝ §34.9.1–§34.10.3，15 leaf。**

**零 TC：0 列** —— 本批 30 列皆有獨有驗證點。
`§29.1.1` 與 `§29.2.1` 之 Description 僅 image token 不同（正規化後仍相異），
且父題分別為 `Wired AUX Cam Settings`／`Wireless AUX Cam Settings` ——
依 **R-CAM16(c)** 父題相異者各自出 TC（`-128`／`-133`）。

設定路徑：**profile §3.0** 之 `ENTER_CAMERA_SETTINGS`（三 hop）＋ `Select "Aux Cameras"`
（HMI Settings List `Settings` 分頁 **row 474**／**row 475**）。
該表於 `Aux Cameras` 之下**無任何子項**（row 476 已是 `11. Trailer Reverse Guidance`），
row 475 備註逐字 `See Head Unit Camera Systems Logic & Flow` —— 子項 label 由本 SYS1 章承載。

**`Vehicle Model`**：30 列**五款全 `1`** —— 本批無 PROXI 配備前提（皆為設定與 HMI 行為）。

| TC ID | req | SYS1 章節 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVCHMI-128` | `SWE1-RVC-109` | §29.1.1 | the wired AUX cam settings popup opens by pressing the c | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-129` | `SWE1-RVC-110-01` | §29.1.2 | the wired AUX settings popup offers Edit the name of the | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-130` | `SWE1-RVC-110-02` | §29.1.2 | the wired AUX settings popup offers Add and Remove as a  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-131` | `SWE1-RVC-110-03` | §29.1.2 | the wired AUX settings popup offers Reset the selected c | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-132` | `SWE1-RVC-110-04` | §29.1.2 | AUX settings are reachable from the pencil icon in the c | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-133` | `SWE1-RVC-111` | §29.2.1 | the wireless AUX cam settings popup opens by pressing th | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-134` | `SWE1-RVC-112-01` | §29.2.2 | the wireless AUX settings popup offers Enable wireless c | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-135` | `SWE1-RVC-112-02` | §29.2.2 | the wireless AUX settings popup offers Edit the name of  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-136` | `SWE1-RVC-112-03` | §29.2.2 | the wireless AUX settings popup offers Add and Remove as | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-137` | `SWE1-RVC-112-04` | §29.2.2 | the wireless AUX settings popup offers Delete the select | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-138` | `SWE1-RVC-113` | §29.2.3 | AUX settings are reachable from the pencil icon for a wi | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-139` | `SWE1-RVC-114-01` | §30.1.1 | an AUX cam is made favorite from the AUX Cam settings me | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-140` | `SWE1-RVC-114-02` | §30.1.1 | an AUX cam is made favorite from the Star on the camera  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-141` | `SWE1-RVC-115` | §30.1.2 | pressing Make Favorite from the AUX Cam settings menu op | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-142` | `SWE1-RVC-116` | §30.1.3 | the favorite confirmation clears on OK on X or automatic | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-143` | `SWE1-RVC-117` | §30.1.4 | the button reads Remove as favorite and pressing it remo | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-144` | `SWE1-RVC-118` | §30.1.5 | a star is shown in the favorite camera line item after e | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-145` | `SWE1-RVC-119-01` | §30.1.6 | the favorites star is shown inside the camera icon circl | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-146` | `SWE1-RVC-119-02` | §30.1.6 | the favorite camera icon is moved to the favorite filter | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-147` | `SWE1-RVC-119-03` | §30.1.6 | the non favorite cameras are labeled 2 3 4 and so on | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-148` | `SWE1-RVC-120` | §31.1.1 | pressing Edit Name from the AUX Cam settings menu starts | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-149` | `SWE1-RVC-121-01` | §31.1.2 | a full QWERTY keyboard is shown for editing the camera n | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-150` | `SWE1-RVC-121-02` | §31.1.2 | the default name is overwritten as soon as typing or bac | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-151` | `SWE1-RVC-121-03` | §31.1.2 | pressing OK confirms the camera name change | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-152` | `SWE1-RVC-122` | §31.1.3 | the settings menu title reads the new name after the cha | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-153` | `SWE1-RVC-123` | §31.1.4 | the updated name is reflected in the settings menu line  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-154` | `SWE1-RVC-124` | §31.1.5 | the updated name is reflected on the camera app homepage | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-155` | `SWE1-RVC-125-01` | §31.1.6 | the camera name is limited to 2 lines of 7 characters | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-156` | `SWE1-RVC-125-02` | §31.1.6 | the name is truncated once the total limit of 14 charact | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-157` | `SWE1-RVC-125-03` | §31.1.6 | a full word that fits is not truncated | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |

## 自檢與 lint

- `selfcheck_camera.py` 十項：**全 0**（TC 30 筆、錨 30 個、反查失敗 0）。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `U` 7／`I-cross` 30／`X` 10。
  `X` 十列之導航標的為 `AUX Cam settings menu`／`settings pop-up` —— 該用語為 SYS1 §29–§31 之逐字，
  其入口為 `ENTER_CAMERA_SETTINGS`（profile §3.0）；lint 之啟發式不認該常數為固定入口。
- `Z`（Vehicle Model 七欄，R-CAM2）：**0**｜`J`：**0**。
