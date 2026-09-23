# RD_FEEDBACK — Camera（FW036 A 本 037，SWRA_V02）

建檔依據：下放包 `docs/fw036/handoff/down/20260923_CAM-06.md` §1
（CAM-05 審閱 §三-1「登 RD 反饋清單」，Pei 2026-09-23）。

**本檔之用途與界線**：供 Pei 回 037 之 RD 作者；**TC 側不承接**，
即本檔任一條皆不改 TC 之生成範圍，亦不作 `specification_reference` 之依據。
每條之格式為「觀察 → 證據（可複驗之座標）→ TC 側現行處置 → 請求之動作」。

母本：`SWE1_CAMERA_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_V02.xlsx`
（doc_id `camera_037_swra_v02`，sha16 `cae0df17016b3532`，`Analysis Report` 分頁，
標題列為第 7 列，資料自第 8 列起）。

---

## RDF-01 —— `SWE-CAM-016` 之 CFTS092 來源混引四個相機節

**觀察**：`SWE-CAM-016`（`Camera Manual Mode Arbitration Logic`，Sub Cat `NormalCamera App`）
之 `Source Requirement ID` 列有 18 個 CFTS092 來源，橫跨 CFTS092 之四個相機節，
其中**只有 6 個屬 Rear Camera 節**，其餘 12 個分屬 Cargo/CHMSL、Surround View、
Forward Facing 三節，與該 SWE 列之題名（Rear 之手動模式仲裁）不同題。

**證據**（節界依 R-CAM12 之實測，五個 `Heading` 列）：

| 節 | 節界 | `-016` 所引 |
|---|---|---|
| Cargo/CHMSL Camera（§1.3.5）| `-060`(4781625) 起 | `-063`、`-067`、`-068` |
| **Rear Camera（§1.3.6）** | `-070`(4781635) 起 | `-072`、`-073`、`-074`、`-076`、`-080`、`-081` |
| Surround View Camera（§1.3.7）| `-083`(4781648) 起 | `-084`、`-085`、`-089`、`-090`、`-091`、`-092`、`-093` |
| Forward Facing Camera（§1.3.8）| `-094`(4781659) 起 | `-095`、`-096` |

**TC 側現行處置**：依 **R-CAM13** 全數生成，12 列落 Test Set `Auxiliary Cameras`
（`batch01b/`，`NR1L-RVC-034` 起），不再以 Test Group 不符為由略過。
A-CA28 之「不生成」處置因而作廢。

**請求之動作**：確認 `-016` 是否應拆為四列（每個相機節一列），或其題名／
Sub Categorization 應改寫為涵蓋四相機之軟鍵行為。現況下 Layer 2 之
「組 ↔ SWE 列」與「TC ↔ Test Set」被迫分離（framework VIII.2 註）。

---

## RDF-02 —— `SWE-CAM-017` 之 Description 與 VC／VM 講兩件不同的事

**觀察**：`-017` 之 `Requirement Description` 講 `CameraDisplaySts` 訊號之送出與維持，
而同列之 `Verification Criteria`／`Verification Method` 兩欄講 Air Suspension PROXI
組態與 4X → 1X 縮放重置 —— 兩者無交集。

**證據**（`Analysis Report` 之 `SWE-CAM-017` 列）：

- `[4] Requirement Description`：`The daemon shall manage the camera display state and
  transmit the CameraDisplaySts = [Default] signal to the vehicle network within <Tsend>
  upon a display state change, and continuously maintain this status until the next
  keypress trigger.`
- `[18] Verification Criteria`：`Verify that the system handles various hardware
  configurations correctly without crashing, and resets the 4X view to 1X when dictated
  by the camera module.`
- `[19] Verification Method`：`Configure the PROXI to simulate an Air Suspension setup and
  power cycle the system. Confirm no system crash occurs. Trigger a 4X zoom, then send the
  reset command from the camera module and verify the UI returns to 1X zoom.`
- 其 `Source Requirement ID` 六個來源（`SYS-RA-CAM-097`／`-098`／`VF551_V2-569`／
  `-578`／`-580`／`VF551_V3-185`）**全數對應 Description 側**，無一講 Air Suspension
  或 4X → 1X；`-578`／`-580` 另為 `Out of Scope`（R-CAM9）。

**TC 側現行處置**：依 **R-CAM13(d)**「VC／VM 不是來源」，`-017` 之 TC 依 Description
與其六個來源生成；VC／VM 所述之 Air Suspension／4X→1X 因**對應不到任一所引來源**
而不生成，登本條。原 A-CA03 不因 framework 重開而結。

**請求之動作**：確認 VC／VM 兩欄是否誤植自他列（4X→1X 之重置條文實為
`SYS-RA-VF551_V2-586`／`VF551_V3-142`，由 `SWE-CAM-021`／`-023` 線所引）。

---

## RDF-03 —— 速度門檻之標定：三份文件三個值，且 037 未指定何者為準

**觀察**：Rear View Camera 之速度退出門檻在三份被引文件中各有標定，**單位皆有載明**
（原提報所疑之「無單位」不成立），但**值不相同**，037 之 `-018` 未指定以何者為準。

**證據**（逐格實測）：

| 文件 | 常數 | 值 | 單位 | 座標 |
|---|---|---|---|---|
| CFTS092 | （無常數名，條文逐字）| `8 mph` | mph | `SYS-RA-CAM-078`（ObjectID 4781643）|
| VF551_V2（Atl-Hi）| `c_VEHSPD_MAX` | **8** | **mph** | §1.8.13 表；`SYS-RA-VF551_V2-139` 名、`-138` 值、`-135` 單位 |
| VF551_V33（2261）| `MAX_SPEED` | **13,0** | **Km/h** | §1.14.1 表；`SYS-RA-VF551_V33-503` 名、`-504` 值、`-507` 單位；容差 `0,5`（`-506`）、範圍 `[10,0;18,0]`（`-505`）|

8 mph ＝ 12.874752 km/h，與 13,0 km/h 相差 0.125 km/h —— **落在 V33 所載之 ±0,5 容差內**，
故兩者應為同一門檻之兩種標定。CFTS092 `-078` 之 `Verification Criteria` 亦自寫
`Vehicle speed exceeds 8 mph (≈ 13 km/h)`。

**此發現對 A-CA30 之影響（須併看）**：CAM-05 §3.4 判「`>` 與 `>=` 之分歧不可觀察」，
其前提為門檻 ＝ 8 mph（12.874752 km/h，非 0.0625 km/h 解析度之整數倍，等值 raw 不存在）。
以 V33 之 `MAX_SPEED = 13,0 km/h` 計，**13.0 ÷ 0.0625 ＝ 208 為整數，等值 raw 存在**，
2261 之嚴格大於（`>`）於門檻點因而**可判**。A-CA30 之「不可判」只對 Atl-Hi（8 mph）成立。
`NR1L-RVC-030`／`-031` 之供試值依此由 raw 206／205 改為 **raw 209／208**（CAM-06 §2 自報）。

**TC 側現行處置**：各平台以各自所屬 VF 本之標定書寫；跨本不換算。

**請求之動作**：於 `-018` 之 Description 或 VC 指定門檻之權威標定
（建議以 VF 本之常數為準、CFTS092 之 `8 mph` 標為 informative），
並確認 V2 之 `c_VEHSPD_MAX = 8 mph` 與 V33 之 `MAX_SPEED = 13,0 Km/h` 是否確為同一門檻。

---

## RDF-04 —— `SWE-CAM-018` 以 `e.g.` 書寫門檻值，使其不可作驗收判準

**觀察**：`-018` 之 Description 將 8 mph 寫為 `e.g.`（舉例），
其 VC／VM 卻以 8 mph／10 mph 作具體判準 —— 同一列內「舉例」與「判準」互斥。

**證據**（`Analysis Report` 之 `SWE-CAM-018` 列）：

- `[4] Requirement Description`：`The NormalCameraDaemon shall enforce camera display exit
  conditions, maintaining the video feed until the user manually closes it, or the vehicle
  exceeds the speed threshold (e.g., 8 mph) for the defined 10s duration.`
- `[18] Verification Criteria`：`Simulate the vehicle speed > 8 mph …`
- `[19] Verification Method`：`… simulate a vehicle speed of 10 mph …`
- 同型措辭另見 `SWE-CAM-016` `[4]`：`… default vehicle speed restrictions
  (e.g., VehicleSpeedVSOSig).` —— 訊號名亦以 `e.g.` 書寫。

**TC 側現行處置**：門檻值不取 037 之 `e.g.` 句，一律回 SYS2 來源之常數／條文
（見 RDF-03 之表）；037 之 Description 只作題意判讀，不作 literal 來源。

**請求之動作**：將 `e.g.` 改為確定之引用（指向 VF 常數名或 CFTS092 條文），
或明文標示該括號為 informative。

---

## RDF-05 —— `SWE-CAM-003` 之 `VF617V5` 拼寫缺底線，造成第三類追不到之來源

**觀察**：全本 `VF617_V5` 之寫法一致，**惟 `SWE-CAM-003` 一列作 `VF617V5`**（缺底線），
`Source Requirement ID` 與 `Source ID` 兩欄同犯。該拼寫使機器對映多出一個 miss 類，
與 DR-CAM-a（`VF617_V5` 整本缺件）之成因不同，易被誤併為同一類。

**證據**（`Analysis Report` 之 `SWE-CAM-003` 列）：

- `[1] Source Requirement ID` 含 `SYS-RA-VF617V5-406`、`SYS-RA-VF617V5-407`
- `[2] Source ID` 含 `VF617V5`
- 全本其餘各列（`-002`／`-005`／`-006`／`-015`／`-016`／`-018`／`-021`／`-023`／`-024`）
  皆作 `VF617_V5`
- 落地痕跡：`features/camera/data/layer2_assign.tsv` 之 `SWE-CAM-003` 列
  `source_book` 欄同時出現 `VF617V5, VF617_V5` 兩形

**TC 側現行處置**：兩形視為同一本；該兩個來源與其餘 `VF617_V5` 來源同以
DR-CAM-a（缺件）處理，不生成。

**請求之動作**：更正為 `VF617_V5`（兩欄共三處）。

---

## 索引

| # | 標的列 | 類 | 對應 anomaly／DR |
|---|---|---|---|
| RDF-01 | `SWE-CAM-016` | 來源混引跨節 | A-CA28（處置經 R-CAM13 作廢）|
| RDF-02 | `SWE-CAM-017` | Description ↔ VC/VM 錯位 | A-CA03 |
| RDF-03 | `SWE-CAM-018` | 標定值跨文件不一 | A-CA21／A-CA22／A-CA30 |
| RDF-04 | `SWE-CAM-018`（`-016` 同型）| `e.g.` 使判準不確定 | —— |
| RDF-05 | `SWE-CAM-003` | 來源代號拼寫 | DR-CAM-a（須分類）|
