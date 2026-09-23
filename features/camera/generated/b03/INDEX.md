# INDEX — b03（`Camera View Switching` ＋ `Wireless Camera Pairing`，下放包 CAM-18 §2）

B 本第 5 批，**兩組皆完結**。
`Camera View Switching`（HU 28）**25 leaf**（產 24 TC）＋
`Wireless Camera Pairing`（HU 33）**5 leaf**（產 5 TC）＝ **30 leaf／29 TC**｜
TC ID `NR1L-RVCHMI-099`～`-127`｜計畫 `features/camera/data/b03_plan.tsv`。

**列數口徑之更正**：下放包 §2 之「31 leaf ＋ 6 leaf ＝ 37」為兩組之**全列**數
（含 umbrella 6 ＋ 1）；實測 **leaf 為 25 ＋ 5 ＝ 30**。30 ≤ 40，升級條件 §4-1 不成立。

**1 列零 TC**：`SWE1-RVC-102`（§28.6.1.2）全文為交叉引用句
（`For details about wireless cameras connection please refer to ‘Wireless cameras connection’ pages`），
標的 §27.5／§27.6 已有 TC → **R-CAM16(c)(ii)**。

**Test Set 分兩組**：`-099`～`-122` 為 `Camera View Switching`；`-123`～`-127` 為 `Wireless Camera Pairing`。

**`Vehicle Model`**：27 列五款全 `1`；**2 列**（`-099`／`-109`）因其前提用
`Surround_View_Camera`（byte 177 bit 0）而該 byte 於 `Toro_ATL_MI` 零命中 → **R-CAM18(b)**，`Toro(2261)` = `0`。

| TC ID | req | SYS1 章節 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVCHMI-099` | `SWE1-RVC-092` | §28.1 | the More Cams button in the More AUX row opens the camer | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | DR-CAM-r | P1 |
| `NR1L-RVCHMI-100` | `SWE1-RVC-093` | §28.2.1 | the check entire surroundings message is shown for 5 sec | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-101` | `SWE1-RVC-094` | §28.2.2 | accessing the AUX camera does not reset the check entire | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-102` | `SWE1-RVC-095` | §28.2.3 | WiFi signal strength and battery level are shown after t | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-103` | `SWE1-RVC-096` | §28.2.4 | pressing X returns to the display from which the AUX cam | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-104` | `SWE1-RVC-097` | §28.3.1 | a blue camera system unavailable screen is shown when no | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-105` | `SWE1-RVC-098-01` | §28.3.2 | More AUX is offered on the unavailable screen when AUX 1 | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-106` | `SWE1-RVC-098-02` | §28.3.2 | the same unavailable behaviour applies with and without  | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-107` | `SWE1-RVC-099` | §28.4.1 | wireless AUX soft controls are greyed out when the camer | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-108` | `SWE1-RVC-100` | §28.4.2 | a popup appears when a greyed out wireless AUX control i | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-109` | `SWE1-RVC-101` | §28.6.1.1 | More Cams swaps views while in reverse and allows exit i | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | — | P1 |
| `NR1L-RVCHMI-110` | `SWE1-RVC-103-01` | §28.7.1.1 | the pan functionality is a drag or swipe on the wireless | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-111` | `SWE1-RVC-103-02` | §28.7.1.1 | the zoom functionality is a pinch on the wireless AUX vi | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-112` | `SWE1-RVC-104-01` | §28.7.1.2 | the manipulated image can be reset | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-113` | `SWE1-RVC-104-02` | §28.7.1.2 | manipulated image settings latch across view changes | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-114` | `SWE1-RVC-105-01` | §28.7.2 | Edit image gives access to the Rotate 90 soft control | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-115` | `SWE1-RVC-105-02` | §28.7.2 | Edit image gives access to the Mirror Image soft control | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-116` | `SWE1-RVC-105-03` | §28.7.2 | Edit image gives access to the Reset soft control | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-117` | `SWE1-RVC-106-01` | §28.7.3 | pressing the AUX soft control extends the view by 10 sec | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-118` | `SWE1-RVC-106-02` | §28.7.3 | the extend view soft control extends the view when the E | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-119` | `SWE1-RVC-107` | §28.7.4 | signal strength and battery are available on the wireles | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-120` | `SWE1-RVC-108-01` | §28.8.1 | image editing on the 12 inch portrait AUX feed works as  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-121` | `SWE1-RVC-108-02` | §28.8.1 | the other AUX views are accessible below the camera feed | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-122` | `SWE1-RVC-108-03` | §28.8.1 | the other AUX views are accessible via the more aux butt | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-123` | `SWE1-RVC-126` | §33.1.1 | Add camera auto-enables the setting and starts pairing w | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-124` | `SWE1-RVC-127-01` | §33.1.2 | a popup is displayed when Add camera is selected during  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-125` | `SWE1-RVC-127-02` | §33.1.2 | pressing YES disconnects projection enables wireless cam | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-126` | `SWE1-RVC-127-03` | §33.1.2 | pressing NO keeps the projection session and stops the p | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-127` | `SWE1-RVC-128` | §33.2.1 | the pairing function is not available while the vehicle  | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |

## 自檢與 lint

- `selfcheck_camera.py` 十項：**全 0**（TC 29 筆、錨 29 個、反查失敗 0）。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `U` 3／`I-cross` 29。
- `Z`（Vehicle Model 七欄，R-CAM2）：**0**｜`J`：**0**｜`X`：**0**。
