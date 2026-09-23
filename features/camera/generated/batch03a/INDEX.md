# INDEX — batch03a（LVDS Messaging，下放包 CAM-10 §2）

`SWE-CAM-008`＋`-009`＋`-010`｜TC ID `NR1L-RVC-118`～`-146`（**29 列**）｜計畫 `features/camera/data/batch03_plan.tsv`（本輪修訂，見上繳包 §2-2）

Test Group：`Rear View Camera`｜Test Set：全 29 列 `LVDS Messaging`。

| TC ID | req | 來源列 | tc_title | 軸 | Vehicle Model = 1 | spec_reference | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVC-118` | `SWE-CAM-008` | `SYS-RA-VF551_V2-451` | gate DynamicGrid to DynamicGridRQSts | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1046` | P1 |
| `NR1L-RVC-119` | `SWE-CAM-008` | `SYS-RA-VF551_V2-450` | Default until DynamicGrid is received | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1728` | P1 |
| `NR1L-RVC-120` | `SWE-CAM-008` | `SYS-RA-VF551_V2-477` | DynamicGridRQSts is never SNA | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1666` | P2 |
| `NR1L-RVC-121` | `SWE-CAM-008` | `SYS-RA-VF551_V2-478` | Default when the user has not changed the setting | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1672` | P2 |
| `NR1L-RVC-122` | `SWE-CAM-008` | `SYS-RA-VF551_V2-479` | OFF for two LVDS cycles on user change | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1673` | P1 |
| `NR1L-RVC-123` | `SWE-CAM-008` | `SYS-RA-VF551_V2-480` | ON for two LVDS cycles on user change | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1674` | P1 |
| `NR1L-RVC-124` | `SWE-CAM-008` | `SYS-RA-VF551_V3-284` | DynamicGridRQSts = OFF (Atl-Mi) | 決策表 | Fastack (376) | `VF551_V3_P363_VF_1046` | P1 |
| `NR1L-RVC-125` | `SWE-CAM-008` | `SYS-RA-VF551_V3-284` | DynamicGridRQSts = ON (Atl-Mi) | 決策表 | Fastack (376) | `VF551_V3_P363_VF_1046` | P1 |
| `NR1L-RVC-126` | `SWE-CAM-008` | `SYS-RA-VF551_V3-284` | Default when DynamicGrid is missing (Atl-Mi) | 決策表 | Fastack (376) | `VF551_V3_P363_VF_1046` | P1 |
| `NR1L-RVC-127` | `SWE-CAM-008` | `SYS-RA-VF551_V3-284` | DynamicGridRQSts is never SNA (Atl-Mi) | 功能測試 | Fastack (376) | `VF551_V3_P363_VF_1046` | P2 |
| `NR1L-RVC-128` | `SWE-CAM-008` | `SYS-RA-VF551_V42-319` | internal DynamicGrid.Req = ON -> DynamicGridRQSts = ON | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2225` | P1 |
| `NR1L-RVC-129` | `SWE-CAM-008` | `SYS-RA-VF551_V42-320` | internal DynamicGrid.Req = OFF -> DynamicGridRQSts = OFF | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2226` | P1 |
| `NR1L-RVC-130` | `SWE-CAM-009` | `SYS-RA-VF551_V2-485` | zoom greyed out above the speed threshold | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_595` | P1 |
| `NR1L-RVC-131` | `SWE-CAM-009` | `SYS-RA-VF551_V2-486` | '+' on the Zoom Button at 1X | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_750` | P1 |
| `NR1L-RVC-132` | `SWE-CAM-009` | `SYS-RA-VF551_V2-486` | '-' on the Zoom Button at 4X | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_750` | P1 |
| `NR1L-RVC-133` | `SWE-CAM-009` | `SYS-RA-VF551_V2-486` | Zoom Button greyed out at SNA | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_750` | P2 |
| `NR1L-RVC-134` | `SWE-CAM-009` | `SYS-RA-VF551_V2-486` | ZoomViewReq = Pressed on zoom keypress | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_750` | P1 |
| `NR1L-RVC-135` | `SWE-CAM-009` | `SYS-RA-VF551_V2-486` | ZoomViewReq = Not_Pressed as the default | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_750` | P2 |
| `NR1L-RVC-136` | `SWE-CAM-010` | `SYS-RA-VF551_V2-443` | gate Dual_Rear_Wheels_Present to VC_RR_DuallyPrsnt | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1924` | P2 |
| `NR1L-RVC-137` | `SWE-CAM-010` | `SYS-RA-VF551_V2-444` | gate Wheelbase to VC_WHL_BASE_LENGTH | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1232` | P2 |
| `NR1L-RVC-138` | `SWE-CAM-010` | `SYS-RA-VF551_V2-445` | gate CAN node 27 (ASM/ASCM) to NetCfg_ASCM | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_630` | P2 |
| `NR1L-RVC-139` | `SWE-CAM-010` | `SYS-RA-VF551_V3-286` | VC_WHL_BASE_LENGTH = Not_Used | 決策表 | Fastack (376) | `VF551_V3_P363_VF_1102` | P2 |
| `NR1L-RVC-140` | `SWE-CAM-010` | `SYS-RA-VF551_V3-286` | VC_WHL_BASE_LENGTH = Length_1 | 決策表 | Fastack (376) | `VF551_V3_P363_VF_1102` | P1 |
| `NR1L-RVC-141` | `SWE-CAM-010` | `SYS-RA-VF551_V3-288` | VC_Trans_Equipped = Automatic | 決策表 | Fastack (376) | `VF551_V3_P363_VF_1134` | P1 |
| `NR1L-RVC-142` | `SWE-CAM-010` | `SYS-RA-VF551_V3-288` | VC_Trans_Equipped = Manual | 決策表 | Fastack (376) | `VF551_V3_P363_VF_1134` | P1 |
| `NR1L-RVC-143` | `SWE-CAM-010` | `SYS-RA-VF551_V42-323` | VC_Trans_Equipped = Automatic (637) | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2203` | P1 |
| `NR1L-RVC-144` | `SWE-CAM-010` | `SYS-RA-VF551_V42-323` | VC_Trans_Equipped = Manual (637) | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2203` | P1 |
| `NR1L-RVC-145` | `SWE-CAM-010` | `SYS-RA-VF551_V42-326` | VC_WHL_BASE_LENGTH = Not_Used (637) | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2476` | P2 |
| `NR1L-RVC-146` | `SWE-CAM-010` | `SYS-RA-VF551_V42-326` | VC_WHL_BASE_LENGTH = Length_1 (637) | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2476` | P1 |

全部 29 列之 `Commander (598)`／`Regengade (5210)`／`Toro(2261)` 皆為 `0` ——
前二者依 R-CAM2(b)；`Toro(2261)` 因 `SWE-CAM-008`／`-009`／`-010` 三列之 in-scope 來源
無一出自 VF551_V33（2261 之本），依 R-CAM15 不勾。

**摘句十一列**：`-124`～`-127`（`V3-284` 78 → 24～31）、`-131`～`-135`（`V2-486` 80 → 32～35）、
`-145`／`-146`（`V42-326` 73 → 17）。其餘十八列未逾 50 token。

**`V2-486` 拆為五列**（`-131`～`-135`）—— `a.`～`e.` 為五個獨立驗證點；併為一列則摘句
無法在 50 token 內同時保留條件與五個結果子句（升級條件第 3 項之正解，見上繳包 §2-2）。

**PENDING**：`-122`／`-123`（`DR-CAM-p`，LVDS 訊息週期）。

**`J` 一列豁免**：`-119` 之上半首字為來源子句編號 `a.`（profile §5.1）。
