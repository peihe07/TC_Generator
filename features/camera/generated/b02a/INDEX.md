# INDEX — b02a（`AUX Camera Access` 前 31 leaf，下放包 CAM-16 §2）

B 本第 3 批。`SWE1-RVC-053`～`-082-02`（HeadUnitCameraSystems §27.1.1–§27.6.1）＝ **31 leaf**，
產 **30 TC**｜TC ID `NR1L-RVCHMI-044`～`-073`｜計畫 `features/camera/data/b02a_plan.tsv`。

**切點併入 §27.6.1 家族** —— 下放包所定之「前 30 leaf」其第 30 列為 `SWE1-RVC-082-01`、
第 31 列為 `-082-02`，兩者同屬 §27.6.1；依下放包 §2 末之指示併入該家族，故取 **31 leaf**（≤ 33）。
其餘 29 leaf（§27.7.1–§27.8.5、§34.1–§34.8）落 B02b。

**`SWE1-RVC-069`（§27.3.2）不生成 TC** —— 其 Description 逐字為 `First surface needs: N/A`，
無可驗證之行為（**A-CA35**，提請分析層裁）。`coverage_b.tsv` 已記其處置。

`test_item` 上半為 SYS1 `Description` 逐字（母體：`spec-index/cache/` 之 HeadUnitCameraSystems 本）。
`specification_reference` ＝ `{SYS1 檔名}_{章節號}`（DECISIONS 6-48）。

**`Vehicle Model`（R-CAM18）**：28 列五款全 `1`；**2 列**（`-050`／`-056`）因
`Digital_CHMSL_Camera_Prsnt`（byte 222 bit 7）與 `Auxiliary_Trailer_Camera`（byte 211 bit 2）
於三本 Atl-Mi PROXI 零命中，三個 Atl-Mi 欄判 `0`。
**無線 AUX 無 PROXI 旗標**（`Wireless_Camera`／`Wireless_Aux`／`Aux_Camera`／`Hotspot` 六本各 0）——
SYS1 以 §27.3.1.x 之硬體條件與 §27.4.1 之設定為替代條件，依 **R-CAM18(a)** 五款全 `1`，
升級條件 §4-3 不成立。

| TC ID | req | SYS1 章節 | tc_title | 軸 | Vehicle Model = 1 | PENDING | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVCHMI-044` | `SWE1-RVC-053` | §27.1.1 | wired and wireless AUX views are non-persistent latching | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P2 |
| `NR1L-RVCHMI-045` | `SWE1-RVC-054` | §27.1.2 | AUX camera follows the general camera activation and dea | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-046` | `SWE1-RVC-055` | §27.1.3 | the soft control of the selected view is highlighted | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-047` | `SWE1-RVC-056` | §27.1.4 | AUX camera settings are locked out while the vehicle is  | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-048` | `SWE1-RVC-057` | §27.1.5 | wireless AUX is limited to four MOPAR-provided cameras | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-049` | `SWE1-RVC-058` | §27.1.5.1 | wireless AUX authentication passes a token through a QR  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-050` | `SWE1-RVC-059` | §27.2.1.1 | AUX camera controls appear on the second surface of the  | 功能測試 | HDCC27, DT27 | — | P2 |
| `NR1L-RVCHMI-051` | `SWE1-RVC-060` | §27.2.2.1 | AUX Cameras icons exist in the camera views | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-052` | `SWE1-RVC-061` | §27.2.3.1 | the wired AUX camera is always a selectable field | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-053` | `SWE1-RVC-062` | §27.2.3.2 | the AUX Cameras button is greyed out when wireless camer | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-054` | `SWE1-RVC-063` | §27.2.4.1 | camera personalization settings are grouped under the Ca | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-055` | `SWE1-RVC-064` | §27.2.5.1 | the AUX camera soft control behaves as a push button con | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-056` | `SWE1-RVC-065` | §27.2.6.1 | the equipped camera feature set is offered in the AUX ca | 決策表 | HDCC27, DT27 | — | P2 |
| `NR1L-RVCHMI-057` | `SWE1-RVC-066` | §27.2.6.2 | AUX cameras are accessible from the Apps Drawer | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-058` | `SWE1-RVC-067` | §27.2.6.3 | AUX cameras are accessible from the Camera app home page | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-r | P1 |
| `NR1L-RVCHMI-059` | `SWE1-RVC-068` | §27.2.6.4 | the selected view soft control is highlighted on the sec | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-060` | `SWE1-RVC-070` | §27.3.3 | camera pop-up text matches the R1 HMI pop-up list | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-061` | `SWE1-RVC-071` | §27.3.4.1 | the camera connection process is locked out while the ve | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-062` | `SWE1-RVC-072` | §27.3.5.1 | the head unit passes WiFi network credentials to the cam | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-063` | `SWE1-RVC-073` | §27.4.1 | wireless cameras are enabled by activating the enable wi | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-064` | `SWE1-RVC-074` | §27.4.2 | a popup is displayed when the setting is selected during | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-065` | `SWE1-RVC-075` | §27.4.2.1 | pressing Yes enables wireless AUX cameras and disconnect | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-066` | `SWE1-RVC-076` | §27.4.2.2 | pressing No keeps the projection session and leaves wire | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-067` | `SWE1-RVC-077` | §27.4.3 | the setting activates silently when no wireless projecti | 負向測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-068` | `SWE1-RVC-078` | §27.4.4 | the enable wireless cameras setting updates dynamically | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P2 |
| `NR1L-RVCHMI-069` | `SWE1-RVC-079` | §27.4.5 | plugging in a projection device displays the wireless ca | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-070` | `SWE1-RVC-080` | §27.5.1 | a connecting message is shown while a sleeping wireless  | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | DR-CAM-h | P2 |
| `NR1L-RVCHMI-071` | `SWE1-RVC-081` | §27.5.2 | selecting a wireless AUX camera auto-enables the setting | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-072` | `SWE1-RVC-082-01` | §27.6.1 | a popup is displayed when a wireless AUX camera is selec | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |
| `NR1L-RVCHMI-073` | `SWE1-RVC-082-02` | §27.6.1 | pressing YES on the popup automatically enables the sett | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | — | P1 |

## 自檢與 lint

- `selfcheck_camera.py` 十項：**全 0**（TC 30 筆、錨 30 個、反查失敗 0）。
- `lint036 --profile camera`：ERROR 類 **全 0**；非致命 `U` 3／`I-cross` 30／`X` 1。
  `X` 一列（`-068`）之導航標的為 `screen focus` —— 該詞為 SYS1 §27.4.5 之逐字，不改寫。
- `Z`（Vehicle Model 七欄，R-CAM2）：**0**｜`J`：**0**。
