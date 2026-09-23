# INDEX — batch02c（State Handling ＋ Auxiliary Cameras，下放包 CAM-09 §2）

`SWE-CAM-003` 全 23 列｜TC ID `NR1L-RVC-095`～`-117`｜計畫 `features/camera/data/batch02_plan.tsv`

Test Group：`Rear View Camera`。Test Set：`-095`～`-097` 為 `Auxiliary Cameras`（來源屬 Cargo/CHMSL 與 Surround View 節，R-CAM13(c)）；`-098`～`-117` 為 `State Handling`。

| TC ID | 來源列 | tc_title | 軸 | Vehicle Model = 1 | spec_reference | P |
|---|---|---|---|---|---|---|
| `NR1L-RVC-095` | `SYS-RA-CAM-069` | X closes the cargo image | 功能測試 | HDCC27, DT27 | `CFTS092-4781634` | P1 |
| `NR1L-RVC-096` | `SYS-RA-CAM-086` | SVC_SoftBtn_Rq = Not Pressed on release | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | `CFTS092-4781651` | P1 |
| `NR1L-RVC-097` | `SYS-RA-CAM-087` | SVC_SoftBtn_Rq = Not Pressed continues | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | `CFTS092-4781652` | P2 |
| `NR1L-RVC-098` | `SYS-RA-VF551_V2-491` | any exit condition returns to non-camera | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1578` | P1 |
| `NR1L-RVC-099` | `SYS-RA-VF551_V2-501` | image displayed in Audio Mode ON | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1758` | P2 |
| `NR1L-RVC-100` | `SYS-RA-VF551_V2-507` | image displayed in Audio Mode OFF | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1762` | P2 |
| `NR1L-RVC-101` | `SYS-RA-VF551_V2-509` | display refreshed after exiting camera mode | 狀態轉換 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1753` | P2 |
| `NR1L-RVC-102` | `SYS-RA-VF551_V2-513` | Transition_time under 1000 ms | 邊界值分析 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1680` | P1 |
| `NR1L-RVC-103` | `SYS-RA-VF551_V2-514` | softkey transition within Transition_time | 邊界值分析 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1679` | P1 |
| `NR1L-RVC-104` | `SYS-RA-VF551_V2-523` | display does not flicker | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_1725` | P2 |
| `NR1L-RVC-105` | `SYS-RA-VF551_V2-524` | display does not blank | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_520` | P2 |
| `NR1L-RVC-106` | `SYS-RA-VF551_V2-534` | softkey available only in RUN | 決策表 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_509` | P1 |
| `NR1L-RVC-107` | `SYS-RA-VF551_V2-535` | softkey controls per VF664 | 功能測試 | HDCC27, DT27 | `VF551_V2_PHDCC27_VF_526` | P2 |
| `NR1L-RVC-108` | `SYS-RA-VF551_V33-432` | SNA keeps the last values for TIME_W_RVC2 | 狀態轉換 | Toro(2261) | `VF551_V33_P226MCA_VF_1197` | P2 |
| `NR1L-RVC-109` | `SYS-RA-VF551_V33-440` | fallback on fail status | 狀態轉換 | Toro(2261) | `VF551_V33_P226MCA_VF_1642` | P2 |
| `NR1L-RVC-110` | `SYS-RA-VF551_V33-443` | fallback on message timeout | 狀態轉換 | Toro(2261) | `VF551_V33_P226MCA_VF_1646` | P2 |
| `NR1L-RVC-111` | `SYS-RA-VF551_V4-095` | ShiftLeverPosition source for non-hybrid | 決策表 | HDCC27 | `VF551_V4_PHDCC27_VF_1917` | P1 |
| `NR1L-RVC-112` | `SYS-RA-VF551_V4-117` | warning text font and size | 功能測試 | HDCC27 | `VF551_V4_PHDCC27_VF_1573` | P2 |
| `NR1L-RVC-113` | `SYS-RA-VF551_V4-119` | warning text follows the language setting | 決策表 | HDCC27 | `VF551_V4_PHDCC27_VF_523` | P2 |
| `NR1L-RVC-114` | `SYS-RA-VF551_V4-130` | Transition_time under 2 seconds | 邊界值分析 | HDCC27 | `VF551_V4_PHDCC27_VF_1680` | P2 |
| `NR1L-RVC-115` | `SYS-RA-VF551_V4-131` | Audio Mode ON behaviour | 功能測試 | HDCC27 | `VF551_V4_PHDCC27_VF_1684` | P2 |
| `NR1L-RVC-116` | `SYS-RA-VF551_V4-138` | Audio Mode OFF behaviour | 功能測試 | HDCC27 | `VF551_V4_PHDCC27_VF_1682` | P2 |
| `NR1L-RVC-117` | `SYS-RA-VF551_V42-255` | repeated softkey request ignored | 決策表 | VF(ProMaster)637 | `VF551_V42_P637MCA_VF_2359` | P2 |

全部 23 列之 `Commander (598)` 與 `Regengade (5210)` 皆為 `0`（R-CAM2(b)）。

**V4 之六列只勾 `HDCC27`**（`-111`～`-116`）—— V4 本之 anchor 前綴只有 `PHDCC27`（R-CAM11）；
CAM-08 之 `-082`／`-087` 誤勾 DT27，已於本輪一併更正（上繳包 §5-1）。

**PENDING**：`-096`／`-097`（DR-CAM-j）、`-107`（DR-CAM-k，VF664）、`-108`（DR-CAM-i）、
`-109`／`-110`（DR-CAM-f，BED_EXTENDER）、`-113`（DR-CAM-o，LanguageSelection raw）。

**`J` 三列豁免**：`-099`／`-100`／`-101` 之上半為來源逐字，首字為子句編號 `a.`／`c.`（profile §5.1）。

**須審閱確認之判讀**：`-099`／`-100` 之章節歸屬 —— V2 本 `VF章節` 欄於 `-499`～`-511` 區落後一組，
本包據此判 `-501` 屬 Audio Mode ON、`-507` 屬 Audio Mode OFF（否則兩句逐字近同而無從區分）。
