# INDEX — batch02b（Configuration ＋ Additional Cameras，下放包 CAM-08 §3）

`SWE-CAM-002`（19）＋ `SWE-CAM-005`（1）＋ `SWE-CAM-017`（2）＝ **22 列**｜TC ID `NR1L-RVC-073`～`-094`｜計畫 `features/camera/data/batch02_plan.tsv`

Test Group：`Rear View Camera`。Test Set：`-073`～`-092` 為 `Configuration`；`-093`／`-094` 為 `Additional Cameras`（`SWE-CAM-017` 已於 framework VIII.2 改歸該組）。

| TC ID | req | 來源列 | tc_title | 軸 | Vehicle Model = 1 | spec_reference | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVC-073` | `SWE-CAM-002` | `SYS-RA-VF551_V2-446` | VC_VehLineRVCM = VEH_DJ | 決策表 | HDCC27 | `VF551_V2_PHDCC27_VF_1922` | P2 |
| `NR1L-RVC-074` | `SWE-CAM-002` | `SYS-RA-VF551_V2-447` | VC_VehLineRVCM = VEH_D2 | 決策表 | HDCC27 | `VF551_V2_PHDCC27_VF_1921` | P2 |
| `NR1L-RVC-075` | `SWE-CAM-002` | `SYS-RA-VF551_V2-751` | VC_VehLineRVCM = VEH_DT | 決策表 | DT27 | `VF551_V2_PDT27_VF_629` | P2 |
| `NR1L-RVC-076` | `SWE-CAM-002` | `SYS-RA-VF551_V3-287` | VC_VehLineRVCM = VEH_363 | 決策表 | Fastack (376) | `VF551_V3_P363_VF_629` | P2 |
| `NR1L-RVC-077` | `SWE-CAM-002` | `SYS-RA-VF551_V3-287` | VC_VehLineRVCM = VEH_376 | 決策表 | Fastack (376) | `VF551_V3_P363_VF_629` | P2 |
| `NR1L-RVC-078` | `SWE-CAM-002` | `SYS-RA-VF551_V42-327` | VC_VehLineRVCM = VEH_637MCA | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2024` | P2 |
| `NR1L-RVC-079` | `SWE-CAM-002` | `SYS-RA-VF551_V2-484` | ZoomViewReq = Default when RVC not active | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V2_PHDCC27_VF_599` | P2 |
| `NR1L-RVC-080` | `SWE-CAM-002` | `SYS-RA-VF551_V2-519` | DISP_NON_CAMERA on both buses | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1574` | P1 |
| `NR1L-RVC-081` | `SWE-CAM-002` | `SYS-RA-VF551_V2-520` | DISP_DIGITAL_RVC_CAMERA when active | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1575` | P1 |
| `NR1L-RVC-082` | `SWE-CAM-002` | `SYS-RA-VF551_V4-125` | DISP_ANALOG_RVC_CAMERA when active | 狀態轉換 | HDCC27, DT27 | `VF551_V4_PHDCC27_VF_1575` | P2 |
| `NR1L-RVC-083` | `SWE-CAM-002` | `SYS-RA-VF551_V3-257` | RADIO_B2 status = DISP_DIGITAL_RVC_CAMERA | 狀態轉換 | VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V3_P363_VF_563` | P1 |
| `NR1L-RVC-084` | `SWE-CAM-002` | `SYS-RA-VF551_V3-257` | RADIO_B2 status = DISP_NON_CAMERA | 狀態轉換 | VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V3_P363_VF_563` | P1 |
| `NR1L-RVC-085` | `SWE-CAM-002` | `SYS-RA-VF551_V2-536` | PROXI Present enables the RVC behaviour | 決策表 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V2_PHDCC27_VF_935` | P1 |
| `NR1L-RVC-086` | `SWE-CAM-002` | `SYS-RA-VF551_V2-555` | Type = Digital enables the Digital behaviour | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1919` | P1 |
| `NR1L-RVC-087` | `SWE-CAM-002` | `SYS-RA-VF551_V4-112` | Type = Analog enables the Analog behaviour | 決策表 | HDCC27, DT27 | `VF551_V4_PHDCC27_VF_935` | P1 |
| `NR1L-RVC-088` | `SWE-CAM-002` | `SYS-RA-VF551_V2-538` | the listed LVDS signals are sent | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1663` | P2 |
| `NR1L-RVC-089` | `SWE-CAM-002` | `SYS-RA-VF551_V3-258` | Rear_Camera_Enable.Info = FALSE | 狀態轉換 | VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V3_P363_VF_1455` | P2 |
| `NR1L-RVC-090` | `SWE-CAM-002` | `SYS-RA-VF551_V3-258` | Rear_Camera_Enable.Info = TRUE | 狀態轉換 | VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V3_P363_VF_1455` | P2 |
| `NR1L-RVC-091` | `SWE-CAM-002` | `SYS-RA-VF551_V42-322` | Gear_Box_Type gated to VC_Trans_Equipped | 功能測試 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_1792` | P2 |
| `NR1L-RVC-092` | `SWE-CAM-005` | `SYS-RA-VF551_V3-254` | RVCM image resolution is 1280 x 800 | 功能測試 | VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V3_P363_VF_522` | P2 |
| `NR1L-RVC-093` | `SWE-CAM-017` | `SYS-RA-CAM-097` | CameraDisplaySts = Default follows the state change | 狀態轉換 | HDCC27, DT27, VF(ProMaster)637 | `CFTS092-4781662` | P1 |
| `NR1L-RVC-094` | `SWE-CAM-017` | `SYS-RA-CAM-098` | CameraDisplaySts = Default continues until next keypress | 功能測試 | HDCC27, DT27, VF(ProMaster)637 | `CFTS092-4781663` | P2 |

全部 22 列之 `Commander (598)` 與 `Regengade (5210)` 皆為 `0`（R-CAM2(b)）。

**R-CAM15 之逐列適用**：(a) 三平台 —— `-079`（另含 Atl-Hi，全五）、`-083`／`-084`／`-089`／`-090`／`-092`；
(b) 只 376 —— `-076`／`-077`（V42 有對應之 `-078`）；(c) V42 承 637 —— `-078`／`-091`。

**只勾 Atl-Hi 之三類**：`TELEMATIC_FD_14` 只在 Atl-Hi 本 DBC（`-080`／`-081`／`-082`）；
`Rear_View_Camera_Type` 只在 Atl-Hi 三本 PROXI（`-086`／`-087`）；V2 本之清單條文（`-088`）。

**摘句兩列**：`-083`（60 → 33 token）／`-084`（60 → 38 token），各刪另一分支之子句。

**PENDING**：`-092`（`DR-CAM-m`，EVS HAL 影像格式）、`-093`（`DR-CAM-j`，`<Tsend>`）。
