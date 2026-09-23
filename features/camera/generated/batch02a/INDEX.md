# INDEX — batch02a（Startup and Shutdown，下放包 CAM-07 §3）

`SWE-CAM-001`（22）＋ `SWE-CAM-012`（3）＋ `SWE-CAM-014`（1）＝ **26 列**｜TC ID `NR1L-RVC-047`～`-072`｜計畫 `features/camera/data/batch02_plan.tsv`（CAM-07 §2 修訂後）

Test Group：`Rear View Camera`。Test Set 除 `NR1L-RVC-048` 為 `Additional Cameras`（來源屬 SVC 節，R-CAM13(c)）外，其餘 25 列皆為 `Startup and Shutdown`。

| TC ID | req | 來源列 | tc_title | 軸 | Vehicle Model = 1 | spec_reference | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVC-047` | `SWE-CAM-001` | `SYS-RA-CAM-082` | X closes the rear image | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `CFTS092-4781647` | P1 |
| `NR1L-RVC-048` | `SWE-CAM-001` | `SYS-RA-CAM-088` | Surround View default is OFF | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | `CFTS092-4781653` | P2 |
| `NR1L-RVC-049` | `SWE-CAM-001` | `SYS-RA-VF551_V2-528` | Camera Not in Position overlay, Atl-Hi | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_505` | P1 |
| `NR1L-RVC-050` | `SWE-CAM-001` | `SYS-RA-VF551_V3-252` | Camera Not in Position overlay, Atl-Mi | 狀態轉換 | VF(ProMaster)637, Fastack (376) | `VF551_V3_P363_VF_505` | P1 |
| `NR1L-RVC-051` | `SWE-CAM-001` | `SYS-RA-VF551_V33-226` | Camera Not in position overlay, 2261 | 狀態轉換 | Toro(2261) | `VF551_V33_P226MCA_VF_514` | P1 |
| `NR1L-RVC-052` | `SWE-CAM-001` | `SYS-RA-VF551_V33-228` | Camera Not in position with bed extender clear, 2261 | 決策表 | Toro(2261) | `VF551_V33_P226MCA_VF_1624` | P2 |
| `NR1L-RVC-053` | `SWE-CAM-001` | `SYS-RA-VF551_V2-531` | Check Entire Surroundings on entering camera display, Atl-Hi | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_507` | P1 |
| `NR1L-RVC-054` | `SWE-CAM-001` | `SYS-RA-VF551_V3-251` | Check Entire Surroundings on entering camera display, 376 | 狀態轉換 | Fastack (376) | `VF551_V3_P363_VF_507` | P1 |
| `NR1L-RVC-055` | `SWE-CAM-001` | `SYS-RA-VF551_V3-251` | overlay removed when the display lasted under 5 s | 邊界值分析 | Fastack (376) | `VF551_V3_P363_VF_507` | P2 |
| `NR1L-RVC-056` | `SWE-CAM-001` | `SYS-RA-VF551_V42-230` | Check Entire Surroundings for T_INITDISPLAY, 637 | 狀態轉換 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2197` | P2 |
| `NR1L-RVC-057` | `SWE-CAM-001` | `SYS-RA-VF551_V33-233` | Check surroundings for safety overlay, 2261 | 狀態轉換 | Toro(2261) | `VF551_V33_P226MCA_VF_1142` | P2 |
| `NR1L-RVC-058` | `SWE-CAM-001` | `SYS-RA-VF551_V33-213` | LTM starts reading Rear_Camera.Data at Ignition_On | 狀態轉換 | Toro(2261) | `VF551_V33_P226MCA_VF_303` | P1 |
| `NR1L-RVC-059` | `SWE-CAM-001` | `SYS-RA-VF551_V33-214` | init default Rear_Camera_Enable.Info is FALSE | 功能測試 | Toro(2261) | `VF551_V33_P226MCA_VF_1137` | P2 |
| `NR1L-RVC-060` | `SWE-CAM-001` | `SYS-RA-VF551_V33-216` | LTM starts reading the delay and grid line requests at Ignition_On | 狀態轉換 | Toro(2261) | `VF551_V33_P226MCA_VF_820` | P2 |
| `NR1L-RVC-061` | `SWE-CAM-001` | `SYS-RA-VF551_V33-219` | stored delay and grid line values survive an ignition cycle | 狀態轉換 | Toro(2261) | `VF551_V33_P226MCA_VF_1139` | P1 |
| `NR1L-RVC-062` | `SWE-CAM-001` | `SYS-RA-VF551_V33-221` | grid lines request ON sets DynamicGrid_Req ON | 決策表 | Toro(2261) | `VF551_V33_P226MCA_VF_822`<br>`VF551_V33_P226MCA_VF_823` | P1 |
| `NR1L-RVC-063` | `SWE-CAM-001` | `SYS-RA-VF551_V33-223` | grid lines request OFF sets DynamicGrid_Req OFF | 決策表 | Toro(2261) | `VF551_V33_P226MCA_VF_824`<br>`VF551_V33_P226MCA_VF_825` | P1 |
| `NR1L-RVC-064` | `SWE-CAM-001` | `SYS-RA-VF551_V33-420` | values stored to NVM at Ignition_Pre_Off | 狀態轉換 | Toro(2261) | `VF551_V33_P226MCA_VF_320` | P1 |
| `NR1L-RVC-065` | `SWE-CAM-001` | `SYS-RA-VF551_V33-426` | repetition data shown for T_INITDISPLAY then Enable cleared | 狀態轉換 | Toro(2261) | `VF551_V33_P226MCA_VF_447` | P2 |
| `NR1L-RVC-066` | `SWE-CAM-001` | `SYS-RA-VF551_V42-217` | delay request restored on ignition transition, 637 | 狀態轉換 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_1835` | P1 |
| `NR1L-RVC-067` | `SWE-CAM-001` | `SYS-RA-VF551_V42-221` | delay request selectable as ON or OFF, 637 | 功能測試 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2336` | P2 |
| `NR1L-RVC-068` | `SWE-CAM-001` | `SYS-RA-VF551_V42-223` | swing doors check selectable as ON or OFF, 637 | 功能測試 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2338` | P2 |
| `NR1L-RVC-069` | `SWE-CAM-012` | `SYS-RA-VF551_V2-550` | IGN_LK triggers Power_Down True and Tpower | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_549` | P1 |
| `NR1L-RVC-070` | `SWE-CAM-012` | `SYS-RA-VF551_V2-553` | Power_Down False transmitted | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1353` | P1 |
| `NR1L-RVC-071` | `SWE-CAM-012` | `SYS-RA-VF551_V3-205` | power to the RVCM within 500 ms, Atl-Mi | 邊界值分析 | VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V3_P363_VF_527` | P1 |
| `NR1L-RVC-072` | `SWE-CAM-014` | `SYS-RA-VF551_V3-206` | IGN_LK triggers Power_Down True and Tpower, Atl-Mi | 狀態轉換 | VF(ProMaster)637, Toro(2261), Fastack (376) | `VF551_V3_P363_VF_549` | P1 |

全部 26 列之 `Commander (598)` 與 `Regengade (5210)` 皆為 `0`（R-CAM2(b)）。

**多錨之兩列**：`NR1L-RVC-062`／`-063` 依 **R-CAM10(b)** 將 IF 來源（`V33-221`／`-223`，承接列 `SWE-CAM-001`）與 THEN 來源（`V33-222`／`-224`，承接列 `SWE-CAM-003`）合為一個 TC，`specification_reference` 兩行；`SWE-CAM-003` 於 plan 記委派。

**lint `J` 之五列豁免**：`-051`／`-052`／`-055`／`-056`／`-070` 之 test_item 上半為來源逐字，其首字本即小寫（`when`／`a)`／`implement`／`a.`）。逐字忠實（§4.3.1）優先於版面規則；交付語料 2223 筆中有 10 筆同型前例。逐列 reasoning 已具名。
