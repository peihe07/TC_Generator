# INDEX — batch04（HMI Overlays，A 本尾批，下放包 CAM-13 §2）

`SWE-CAM-021`（11）＋ `-022`（7）＋ `-023`（8）＝ **26 列**｜TC ID `NR1L-RVC-215`～`-240`｜計畫 `features/camera/data/batch04_plan.tsv`（115 列）

Test Group：`Rear View Camera`｜Test Set：全 26 列 `HMI Overlays`。
**`SWE-CAM-025` 之 TC 數為 0** —— 其唯一來源 `SYS-RA-VF551_V33-227` 依 R-CAM10 委派 `SWE-CAM-020`
（`NR1L-RVC-032`／`-033`），屬 **R-CAM16** 之零 TC 形制，非缺口。

| TC ID | req | 來源列 | tc_title | 軸 | Vehicle Model = 1 | spec_reference | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVC-215` | `SWE-CAM-021` | `SYS-RA-VF551_V2-500` | image not interrupted in Audio Mode ON | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1759` | P2 |
| `NR1L-RVC-216` | `SWE-CAM-021` | `SYS-RA-VF551_V2-504` | image not interrupted in Audio Mode ON | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1760` | P2 |
| `NR1L-RVC-217` | `SWE-CAM-021` | `SYS-RA-VF551_V2-506` | image not interrupted in Audio Mode OFF | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1764` | P2 |
| `NR1L-RVC-218` | `SWE-CAM-021` | `SYS-RA-VF551_V2-511` | image not interrupted while features run | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1751` | P2 |
| `NR1L-RVC-219` | `SWE-CAM-021` | `SYS-RA-VF551_V2-512` | Audio Mode ON behaviour | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1684` | P2 |
| `NR1L-RVC-220` | `SWE-CAM-021` | `SYS-RA-VF551_V2-505` | Audio Mode OFF behaviour | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1682` | P2 |
| `NR1L-RVC-221` | `SWE-CAM-021` | `SYS-RA-VF551_V2-503` | display updates processed after exiting | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1761` | P2 |
| `NR1L-RVC-222` | `SWE-CAM-021` | `SYS-RA-VF551_V2-510` | display updates processed after exiting (second section) | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1752` | P2 |
| `NR1L-RVC-223` | `SWE-CAM-021` | `SYS-RA-VF551_V2-529` | warning text removed when the display lasted under 5 s | 邊界值分析 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1572` | P2 |
| `NR1L-RVC-224` | `SWE-CAM-021` | `SYS-RA-VF551_V3-255` | no blanking or flicker (Atl-Mi) | 功能測試 | Fastack (376) | `VF551_V3_P363_VF_520` | P2 |
| `NR1L-RVC-225` | `SWE-CAM-021` | `SYS-RA-VF551_V4-122` | display does not flicker (analog) | 功能測試 | HDCC27 | `VF551_V4_PHDCC27_VF_1725` | P2 |
| `NR1L-RVC-226` | `SWE-CAM-022` | `SYS-RA-VF551_V4-121` | display does not go blank (analog) | 功能測試 | HDCC27 | `VF551_V4_PHDCC27_VF_520` | P2 |
| `NR1L-RVC-227` | `SWE-CAM-022` | `SYS-RA-VF551_V4-133` | display updates processed after exiting (analog) | 狀態轉換 | HDCC27 | `VF551_V4_PHDCC27_VF_1752` | P2 |
| `NR1L-RVC-228` | `SWE-CAM-022` | `SYS-RA-VF551_V4-140` | display updates processed once exited (analog) | 狀態轉換 | HDCC27 | `VF551_V4_PHDCC27_VF_1761` | P2 |
| `NR1L-RVC-229` | `SWE-CAM-022` | `SYS-RA-VF551_V4-134` | display reflects the changes after exiting (analog) | 狀態轉換 | HDCC27 | `VF551_V4_PHDCC27_VF_1753` | P2 |
| `NR1L-RVC-230` | `SWE-CAM-022` | `SYS-RA-VF551_V4-152` | back to non-camera on any exit condition (analog) | 狀態轉換 | HDCC27 | `VF551_V4_PHDCC27_VF_1578` | P1 |
| `NR1L-RVC-231` | `SWE-CAM-022` | `SYS-RA-VF551_V4-136` | rear camera image displayed (analog, second section) | 決策表 | HDCC27 | `VF551_V4_PHDCC27_VF_1762` | P1 |
| `NR1L-RVC-232` | `SWE-CAM-022` | `SYS-RA-VF551_V4-142` | rear camera image displayed (analog) | 決策表 | HDCC27 | `VF551_V4_PHDCC27_VF_1758` | P1 |
| `NR1L-RVC-233` | `SWE-CAM-023` | `SYS-RA-VF551_V2-526` | warning text follows the language setting | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_523` | P2 |
| `NR1L-RVC-234` | `SWE-CAM-023` | `SYS-RA-VF551_V3-253` | warning text follows the language setting | 決策表 | Fastack (376) | `VF551_V3_P363_VF_523` | P2 |
| `NR1L-RVC-235` | `SWE-CAM-023` | `SYS-RA-VF551_V2-527` | warning text font and size | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1708` | P2 |
| `NR1L-RVC-236` | `SWE-CAM-023` | `SYS-RA-VF551_V2-530` | warning text font and size | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1573` | P2 |
| `NR1L-RVC-237` | `SWE-CAM-023` | `SYS-RA-VF551_V2-540` | zoom request stays Not Pressed when Zoom Out is not pressed | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1707` | P2 |
| `NR1L-RVC-238` | `SWE-CAM-023` | `SYS-RA-VF551_V2-542` | zoom request stays Not Pressed when Zoom In is not pressed | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1705` | P2 |
| `NR1L-RVC-239` | `SWE-CAM-023` | `SYS-RA-VF551_V42-231` | warning text removed before T_INITDISPLAY (non-MTX) | 邊界值分析 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2201` | P2 |
| `NR1L-RVC-240` | `SWE-CAM-023` | `SYS-RA-VF551_V42-232` | warning text removed before T_INITDISPLAY (MTX) | 邊界值分析 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2296` | P2 |

全部 26 列之 `Commander (598)`／`Regengade (5210)`／`Toro(2261)` 皆為 `0`。

**26 列全部未逾 50 token，無摘句；`U` ＝ 0（無 PENDING）。**

**V4（類比側）之十一列**：`-225`～`-232` 與 `-229` 等只勾 `HDCC27`（R-CAM11 之平台表），
Pre-Condition 以 `PROXI Rear_View_Camera_Type = 0 (Analogic)` 與 V2 之數位側區別。

**`J` 十四列豁免**：上半為來源逐字而首字本即小寫（`a.`／`b.`／`c.`／`-`／`·`後之字）—— profile §5.1。

**與既有列之關係**：本批多列與 batch02c／batch03c 之 TC **逐字同句而本與承接列不同**
（V2 數位側 ↔ V4 類比側；`SWE-CAM-003` ↔ `-021`／`-022`／`-023`）——
依 R-CAM10「委派只在同一來源被多列共引時成立」，各歸其列，非重複。
