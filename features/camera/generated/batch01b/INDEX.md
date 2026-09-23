# INDEX — batch01b（Auxiliary Cameras，下放包 CAM-06 §2-4）

A-CA28 之 12 列（`SWE-CAM-016` 所引之 Cargo/CHMSL、Surround View、Forward Facing 三節條文），
依 **R-CAM13** 全數生成。Test Group：`Rear View Camera`｜Test Set：**`Auxiliary Cameras`**
（framework Part VIII 第 10 組，CAM-06 重開）｜TC ID `NR1L-RVC-034`～`-046`（**13 列**）
｜計畫 `features/camera/data/batch01b_plan.tsv`

| TC ID | 來源列 | 節 | tc_title | 軸 | Vehicle Model = 1 | spec_reference | P |
|---|---|---|---|---|---|---|---|
| `NR1L-RVC-034` | `SYS-RA-CAM-063` | Cargo/CHMSL | CHMSL softkey on Controls screen | 功能測試 | HDCC27, DT27 | `CFTS092-4781628` | P2 |
| `NR1L-RVC-035` | `SYS-RA-CAM-067` | Cargo/CHMSL | CHMSL softkey enables the image | 功能測試 | HDCC27, DT27 | `CFTS092-4781632` | P1 |
| `NR1L-RVC-036` | `SYS-RA-CAM-068` | Cargo/CHMSL | CHMC IMAGE ON shows the cargo area | 功能測試 | HDCC27, DT27 | `CFTS092-4781633` | P1 |
| `NR1L-RVC-037` | `SYS-RA-CAM-084` | SVC | SVC_SK_PRSNT activates the virtual button | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | `CFTS092-4781649` | P1 |
| `NR1L-RVC-038` | `SYS-RA-CAM-085` | SVC | SVC_SoftBtn_Rq sent on keypress | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | `CFTS092-4781650` | P1 |
| `NR1L-RVC-039` | `SYS-RA-CAM-089` | SVC | SVC softkey on Controls screen | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | `CFTS092-4781654` | P2 |
| `NR1L-RVC-040` | `SYS-RA-CAM-090` | SVC | SVC image below the speed threshold | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | `CFTS092-4781655` | P1 |
| `NR1L-RVC-041` | `SYS-RA-CAM-092` | SVC | SVC button greyed out at or above 8 MPH | 邊界值分析 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | `CFTS092-4781657` | P1 |
| `NR1L-RVC-042` | `SYS-RA-CAM-093` | SVC | SVC button retained when speed is SNA | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | `CFTS092-4781658` | P2 |
| `NR1L-RVC-043` | `SYS-RA-CAM-091` | SVC | TGW_DISP_STAT sent on SVC keypress | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | `CFTS092-4781656` | P2 |
| `NR1L-RVC-044` | `SYS-RA-CAM-095` | FFC | OFFroad_Camera activates the virtual FFC button | 決策表 | HDCC27, DT27, VF(ProMaster)637, Fastack (376) | `CFTS092-4781660` | P1 |
| `NR1L-RVC-045` | `SYS-RA-CAM-096` | FFC | CameraDisplaySts View_3 on FFC keypress | 功能測試 | HDCC27, DT27, VF(ProMaster)637 | `CFTS092-4781661` | P1 |
| `NR1L-RVC-046` | `SYS-RA-CAM-076` | **Rear** | Rear Camera softkey on Controls screen | 功能測試 | HDCC27, DT27, VF(ProMaster)637, Toro(2261), Fastack (376) | `CFTS092-4781641` | P2 |

`-034`～`-045` 十二列之 `Commander (598)`、`Regengade (5210)` 與 `Toro(2261)` 皆為 `0` ——
前二者依 R-CAM2(b)，`Toro(2261)` 因其 PROXI 表（`forms/proxi/Toro_ATL_MI`，2019 本）止於 byte 172，
`Digital_CHMSL_Camera_Prsnt`（byte 222）與 `Surround_View_Camera`／`Forward_Facing_Camera`（byte 177）
三個參數皆查無（升級條件第 4 項之回報）。

`NR1L-RVC-045` 之 `Fastack (376)` 另勾 `0` —— `forms/P363_BH-CAN [07338]_3A_R2.dbc` 有 `BO_ 1283 RADIO_B3`
但全本無 `CameraDisplaySts` 訊號，該平台之 ER 不可觀察。

**`NR1L-RVC-046` 為追加列（CAM-07 §2，DECISIONS 6-17）** —— 來源 `SYS-RA-CAM-076` 屬 **Rear Camera 節**，故其 **Test Set 為 `Display Arbitration`**，非本目錄其餘列之 `Auxiliary Cameras`；五車型全勾（`PROXI Rear_View_Camera` 六本皆有）。落於本目錄只是落檔批次之便（framework VIII.2 註之反向例）。
