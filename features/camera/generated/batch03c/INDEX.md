# INDEX — batch03c（Diagnostics ＋ Video Pipeline，下放包 CAM-12 §3）

`SWE-CAM-004`（17）＋ `-006`（17）＋ `-019`（2）＝ **36 列**｜TC ID `NR1L-RVC-179`～`-214`｜計畫 `features/camera/data/batch03_plan.tsv`

Test Group：`Rear View Camera`｜Test Set：`-179`～`-195` `Diagnostics`；`-196`～`-214` `Video Pipeline`。

| TC ID | req | 來源列 | tc_title | 軸 | Vehicle Model = 1 | spec_reference | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVC-179` | `SWE-CAM-004` | `SYS-RA-VF551_V2-221` | InternalErrorStatus = True sets the DTC | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_123` | P1 |
| `NR1L-RVC-180` | `SWE-CAM-004` | `SYS-RA-VF551_V2-220` | InternalErrorStatus = False clears the DTC | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1589` | P1 |
| `NR1L-RVC-181` | `SWE-CAM-004` | `SYS-RA-VF551_V2-218` | ExternalErrorStatus = True sets the DTC | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_926` | P1 |
| `NR1L-RVC-182` | `SWE-CAM-004` | `SYS-RA-VF551_V2-217` | ExternalErrorStatus = False clears the DTC | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1590` | P1 |
| `NR1L-RVC-183` | `SWE-CAM-004` | `SYS-RA-VF551_V2-215` | Communications_Timeout = True sets the DTC | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_927` | P1 |
| `NR1L-RVC-184` | `SWE-CAM-004` | `SYS-RA-VF551_V2-214` | Communications_Timeout = False clears the DTC | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1591` | P1 |
| `NR1L-RVC-185` | `SWE-CAM-004` | `SYS-RA-VF551_V2-205` | ignition On and gear no longer SNA heals the DTC | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1821` | P1 |
| `NR1L-RVC-186` | `SWE-CAM-004` | `SYS-RA-VF551_V3-527` | InternalErrorStatus sets and clears the DTC (Atl-Mi) | 決策表 | Fastack (376) | `VF551_V3_P363_VF_123` | P1 |
| `NR1L-RVC-187` | `SWE-CAM-004` | `SYS-RA-VF551_V3-529` | ExternalErrorStatus sets and clears the DTC (Atl-Mi) | 決策表 | Fastack (376) | `VF551_V3_P363_VF_926` | P1 |
| `NR1L-RVC-188` | `SWE-CAM-004` | `SYS-RA-VF551_V3-531` | Communications_Timeout sets and clears the DTC (Atl-Mi) | 決策表 | Fastack (376) | `VF551_V3_P363_VF_927` | P1 |
| `NR1L-RVC-189` | `SWE-CAM-004` | `SYS-RA-VF551_V33-429` | speed fail beyond the threshold sets the DTC (2261) | 邊界值分析 | Toro(2261) | `VF551_V33_P226MCA_VF_351` | P2 |
| `NR1L-RVC-190` | `SWE-CAM-004` | `SYS-RA-VF551_V42-583` | InternalErrorStatus = True sets the DTC (637) | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_628` | P1 |
| `NR1L-RVC-191` | `SWE-CAM-004` | `SYS-RA-VF551_V42-584` | InternalErrorStatus = False clears the DTC (637) | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_1993` | P1 |
| `NR1L-RVC-192` | `SWE-CAM-004` | `SYS-RA-VF551_V42-586` | ExternalErrorStatus = True sets the DTC (637) | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_617` | P1 |
| `NR1L-RVC-193` | `SWE-CAM-004` | `SYS-RA-VF551_V42-587` | ExternalErrorStatus = False clears the DTC (637) | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_1994` | P1 |
| `NR1L-RVC-194` | `SWE-CAM-004` | `SYS-RA-VF551_V42-589` | Communications_Timeout = True sets the DTC (637) | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_1088` | P1 |
| `NR1L-RVC-195` | `SWE-CAM-004` | `SYS-RA-VF551_V42-595` | STATUS_BH_BCM1 timeout falls back and sets the DTC | 邊界值分析 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2132` | P2 |
| `NR1L-RVC-196` | `SWE-CAM-006` | `SYS-RA-VF551_V2-539` | the listed LVDS signals are received | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1662` | P2 |
| `NR1L-RVC-197` | `SWE-CAM-006` | `SYS-RA-VF551_V2-212` | no video and no cable signal sets the DTC and the HMI | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_931` | P1 |
| `NR1L-RVC-198` | `SWE-CAM-006` | `SYS-RA-VF551_V2-211` | video restored heals the DTC | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1592` | P1 |
| `NR1L-RVC-199` | `SWE-CAM-006` | `SYS-RA-VF551_V3-533` | no video and no cable signal sets the DTC (Atl-Mi) | 決策表 | Fastack (376) | `VF551_V3_P363_VF_931` | P1 |
| `NR1L-RVC-200` | `SWE-CAM-006` | `SYS-RA-VF551_V42-210` | image scaled per Radio_Display_Type | 功能測試 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2271` | P2 |
| `NR1L-RVC-201` | `SWE-CAM-006` | `SYS-RA-VF551_V42-226` | cable video copied and displayed within RESPONSE_TIME | 邊界值分析 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_1164` | P1 |
| `NR1L-RVC-202` | `SWE-CAM-006` | `SYS-RA-VF551_V42-253` | cable video copied and the image displayed | 功能測試 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2357` | P1 |
| `NR1L-RVC-203` | `SWE-CAM-006` | `SYS-RA-VF551_V42-274` | cable video not copied and no image | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2378` | P2 |
| `NR1L-RVC-204` | `SWE-CAM-006` | `SYS-RA-VF551_V42-262` | Ignition_Off stops the copy | 狀態轉換 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2366` | P1 |
| `NR1L-RVC-205` | `SWE-CAM-006` | `SYS-RA-VF551_V42-263` | ImageDefeat pressed stops the copy | 狀態轉換 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2367` | P1 |
| `NR1L-RVC-206` | `SWE-CAM-006` | `SYS-RA-VF551_V42-266` | copy continues with Enable and RVC_ACTIVE true | 狀態轉換 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2370` | P2 |
| `NR1L-RVC-207` | `SWE-CAM-006` | `SYS-RA-VF551_V42-268` | copy stops and the flags are cleared | 狀態轉換 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2372` | P1 |
| `NR1L-RVC-208` | `SWE-CAM-006` | `SYS-RA-VF551_V42-301` | copy stops with ImageDefeat set | 狀態轉換 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2396` | P2 |
| `NR1L-RVC-209` | `SWE-CAM-006` | `SYS-RA-VF551_V42-216` | power up sends Power_Down False and starts reading the cable | 邊界值分析 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_1777` | P1 |
| `NR1L-RVC-210` | `SWE-CAM-006` | `SYS-RA-VF551_V42-219` | power down sends Power_Down True and holds power for Tpower | 狀態轉換 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_1836` | P1 |
| `NR1L-RVC-211` | `SWE-CAM-006` | `SYS-RA-VF551_V42-592` | cable not received sets the DTC (637) | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_1090` | P1 |
| `NR1L-RVC-212` | `SWE-CAM-006` | `SYS-RA-VF551_V42-593` | video received clears the DTC (637) | 狀態轉換 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_1996` | P1 |
| `NR1L-RVC-213` | `SWE-CAM-019` | `SYS-RA-VF551_V33-243` | copy stops and no rearview image (FMVSS 111) | 狀態轉換 | Toro(2261) | `VF551_V33_P226MCA_VF_1119` | P1 |
| `NR1L-RVC-214` | `SWE-CAM-019` | `SYS-RA-VF551_V33-234` | displayed brightness is above 50 % | 功能測試 | Toro(2261) | `VF551_V33_P226MCA_VF_1115` | P2 |

全部 36 列之 `Commander (598)` 與 `Regengade (5210)` 皆為 `0`（R-CAM2(b)）。

**摘句七列**：`-189`（65 → 33）、`-199`（69 → 33）、`-201`（59 → 41）、`-205`（73 → 47）、
`-206`（51 → 43）、`-210`（57 → 31）、`-211`（58 → 32）。其餘 29 列未逾 50 token。

**PENDING 17 處**：`DR-CAM-q`（DTC 識別碼，14 列之 pre）、`DR-CAM-f`（`TRANSM2`，`-201`／`-205`）、
`DR-CAM-i`（`Ignition_Off` 之 `CmdIgnSts`，`-204`）。

**`J` 七列豁免**：`-201`／`-202`／`-203`／`-207`／`-208`／`-210`／`-213` 之上半為來源逐字，
其首字本即小寫（`copy`／`not`／`stop`／`send`／`the`）—— profile §5.1。

**`systemStatus.*` 之注入須 LVDS 模擬器**（`-179`～`-188`／`-190`～`-194`／`-196`）——
該能力之確認已在 `bench_verify.md`。
