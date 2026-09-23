# INDEX — batch03b（LVDS Messaging，下放包 CAM-11 §3）

`SWE-CAM-011` 全 **29 列**｜TC ID `NR1L-RVC-150`～`-178`｜計畫 `features/camera/data/batch03_plan.tsv`

Test Group：`Rear View Camera`｜Test Set：全 29 列 `LVDS Messaging`。
本批為 `vehicleUpdate_2` 群之 **CAN → LVDS gating**，多數列成「gating ／ 缺失→SNA」一對。

| TC ID | 來源列 | tc_title | 軸 | Vehicle Model = 1 | spec_reference | P |
|---|---|---|---|---|---|---|
| `NR1L-RVC-150` | `SYS-RA-VF551_V2-461` | gate VehicleSpeedVSOSig to VehicleSpeedVSOSig | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_616` | P1 |
| `NR1L-RVC-151` | `SYS-RA-VF551_V2-460` | VehicleSpeedVSOSig = SNA when VehicleSpeedVSOSig is missing | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1711` | P1 |
| `NR1L-RVC-152` | `SYS-RA-VF551_V2-459` | gate LwsAngle_SCCM to LwsAngle | 功能測試 | HDCC27 | `VF551_V2_PHDCC27_VF_1883` | P2 |
| `NR1L-RVC-153` | `SYS-RA-VF551_V2-458` | LwsAngle = SNA when LwsAngle_SCCM is missing | 決策表 | HDCC27 | `VF551_V2_PHDCC27_VF_1884` | P2 |
| `NR1L-RVC-154` | `SYS-RA-VF551_V2-745` | gate LwsAngle to LwsAngle | 功能測試 | DT27 | `VF551_V2_PDT27_VF_615` | P2 |
| `NR1L-RVC-155` | `SYS-RA-VF551_V2-746` | LwsAngle = SNA when LwsAngle is missing | 決策表 | DT27 | `VF551_V2_PDT27_VF_1712` | P2 |
| `NR1L-RVC-156` | `SYS-RA-VF551_V2-457` | gate ShiftLeverPosition to ShiftLeverPosition | 功能測試 | HDCC27 | `VF551_V2_PHDCC27_VF_2035` | P1 |
| `NR1L-RVC-157` | `SYS-RA-VF551_V2-456` | ShiftLeverPosition = SNA when ShiftLeverPosition is missing | 決策表 | HDCC27 | `VF551_V2_PHDCC27_VF_2036` | P1 |
| `NR1L-RVC-158` | `SYS-RA-VF551_V2-747` | gate ShiftLeverPosition to ShiftLeverPosition | 功能測試 | DT27 | `VF551_V2_PDT27_VF_614` | P1 |
| `NR1L-RVC-159` | `SYS-RA-VF551_V2-748` | ShiftLeverPosition = SNA when ShiftLeverPosition is missing | 決策表 | DT27 | `VF551_V2_PDT27_VF_1713` | P1 |
| `NR1L-RVC-160` | `SYS-RA-VF551_V2-453` | gate ASCM_Stat to ASCM_Stat | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_613` | P2 |
| `NR1L-RVC-161` | `SYS-RA-VF551_V2-452` | ASCM_Stat = SNA when ASCM_Stat is missing | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1714` | P2 |
| `NR1L-RVC-162` | `SYS-RA-VF551_V2-483` | ZoomViewReq is never SNA | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1158` | P2 |
| `NR1L-RVC-163` | `SYS-RA-VF551_V2-442` | gate PROXI PAM_Tuning_Set to PAM_Tuning_Set | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1925` | P2 |
| `NR1L-RVC-164` | `SYS-RA-VF551_V2-448` | gate PROXI Steering_Ratio_Rack_Pinion_Type to VC_Steering_Cfactor | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_624` | P2 |
| `NR1L-RVC-165` | `SYS-RA-VF551_V3-285` | gate PROXI Steering_Ratio_Rack_Pinion_Type to VC_Steering_Cfactor | 決策表 | Fastack (376) | `VF551_V3_P363_VF_624` | P2 |
| `NR1L-RVC-166` | `SYS-RA-VF551_V3-285` | VC_Steering_Cfactor on the other PROXI values | 決策表 | Fastack (376) | `VF551_V3_P363_VF_624` | P2 |
| `NR1L-RVC-167` | `SYS-RA-VF551_V3-280` | gate VehicleSpeedVSOSig to VehicleSpeedVSOSig | 功能測試 | Fastack (376) | `VF551_V3_P363_VF_616` | P1 |
| `NR1L-RVC-168` | `SYS-RA-VF551_V3-280` | VehicleSpeedVSOSig = SNA when VehicleSpeedVSOSig is missing | 決策表 | Fastack (376) | `VF551_V3_P363_VF_616` | P1 |
| `NR1L-RVC-169` | `SYS-RA-VF551_V3-281` | gate LWSAngle to LwsAngle | 功能測試 | Fastack (376) | `VF551_V3_P363_VF_615` | P1 |
| `NR1L-RVC-170` | `SYS-RA-VF551_V3-281` | LwsAngle = SNA when LWSAngle is missing | 決策表 | Fastack (376) | `VF551_V3_P363_VF_615` | P1 |
| `NR1L-RVC-171` | `SYS-RA-VF551_V3-282` | gate ShiftLeverPosition to ShiftLeverPosition | 功能測試 | Fastack (376) | `VF551_V3_P363_VF_614` | P1 |
| `NR1L-RVC-172` | `SYS-RA-VF551_V3-282` | ShiftLeverPosition = SNA when ShiftLeverPosition is missing | 決策表 | Fastack (376) | `VF551_V3_P363_VF_614` | P1 |
| `NR1L-RVC-173` | `SYS-RA-VF551_V3-283` | gate ReverseGearSts to ReverseGearSts | 功能測試 | Fastack (376) | `VF551_V3_P363_VF_613` | P1 |
| `NR1L-RVC-174` | `SYS-RA-VF551_V3-283` | ReverseGearSts = SNA when ReverseGearSts is missing | 決策表 | Fastack (376) | `VF551_V3_P363_VF_613` | P1 |
| `NR1L-RVC-175` | `SYS-RA-VF551_V42-308` | ShiftLeverPosition = SNA when ShiftLeverPosition is missing | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2020` | P1 |
| `NR1L-RVC-176` | `SYS-RA-VF551_V42-310` | ReverseGearSts = SNA when ReverseGearSts is missing | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2298` | P1 |
| `NR1L-RVC-177` | `SYS-RA-VF551_V42-312` | VehicleSpeedVSOSig = SNA when VehicleSpeedVSOSig is missing | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2475` | P1 |
| `NR1L-RVC-178` | `SYS-RA-VF551_V42-314` | LwsAngle = SNA when LwsAngle is missing | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2022` | P2 |

全部 29 列之 `Commander (598)`／`Regengade (5210)`／`Toro(2261)` 皆為 `0` ——
前二者依 R-CAM2(b)；`Toro(2261)` 因 `SWE-CAM-011` 之 30 個來源無一出自 VF551_V33。

**29 列全部未逾 50 token，無摘句。**

**CAN 訊息於四本 DBC 查無者 5 列**（升級條件第 2 項之回報）：
`-152`／`-153`（`STEERING1`）、`-175`（`TRANSM2`）、`-176`（`ENGINE1`）、`-178`（`GE`）——
皆標 `PENDING: DR-CAM-f`；惟「停送該訊息」之動作不需知其 raw，四個缺失側之 ER 仍可執行。

**RDF-08／09 之兩列**：`-169`／`-170`（`V3-281`）與 `-173`／`-174`（`V3-283`）之來源標的誤植，
verbatim 逐字不改、ER 以正確標的書寫（CAM-09 審閱 §一-6）。

**`J` 六列豁免**：`-151`／`-153`／`-155`／`-157`／`-159`／`-161` 之上半首字為來源子句編號 `a.`（profile §5.1）。
