# ANOMALIES — FW036 Camera

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-CAnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

本批全部由下放包 CAM-01 任務 3-6／3-7 登記，**皆為候選，非裁定**。
每條之「實測」欄為執行層自量，母體與查詢條件見
`docs/fw036/handoff/up/20260916_CAM-01.md` §3–§4。

---

## A. 缺件

| # | 事由 | 實測 | 影響 | 狀態 |
|---|---|---|---|---|
| A-CA01 | **`VF617_V5` 缺件**（SYS2 xlsx ＋ VF docx 皆無）| A 本 541 個來源引用中 **119 個**不可解析，prefix 全為 `SYS-RA-VF617_V5`（117）＋ `SYS-RA-VF617V5`（2）| `SWE-CAM-024`（AUX Camera）12/12 全數不可追，整條 PENDING；`-003`／`-015`／`-018` 部分來源不可追 | PENDING（DR-CAM-a）|
| A-CA02 | **SYS2 `VF551_V4` 之 `VF章節`(I) 欄全空** | 321/321 空。對照 V2 752/752、V3 747/747、V33 662/662、V42 801/801 皆有值 | A 本引用之 44 列 V4 無法直接取 Layer 3 | PENDING（DR-CAM-b；已提替代判法，見 DECISIONS §6-5）|

## B. A 本 RD 品質（037 `SWRA_V02`，母體 25 列）

| # | 事由 | 實測（逐字） | 提議 | 狀態 |
|---|---|---|---|---|
| A-CA03 | **`SWE-CAM-017` 之描述與 VC/VM 不對齊** | 037 Description 逐字：「The daemon shall manage the camera display state and transmit the `CameraDisplaySts = [Default]` signal to the vehicle network within `<Tsend>` upon a display state change, and continuously maintain this status until the next keypress trigger.」其來源 CFTS092 `SYS-RA-CAM-097`（`4781662`）／`-098`（`4781663`）屬 Forward Facing Camera 節，原文為 HU 側訊號行為；而該列之 VC/VM 講 Air Suspension PROXI 與 4X→1X reset | 依描述暫歸 Layer 2 `State Handling`；RD 對齊後可能改歸 `HMI Overlays` | PENDING |
| A-CA04 | **`SWE-CAM-018` 把硬門檻標成「e.g.」** | 037 Description 逐字：「…or the vehicle exceeds the speed threshold (**e.g., 8 mph**) for the defined 10s duration.」CFTS092 `SYS-RA-CAM-078`（`4781643`）原文逐字：「Rear Camera display image shall remain displayed until display timer is greater than 10s AND vehicle speed is above 8 mph.」—— 為**合取之硬條件**，非舉例。VF551_V2-492 為 Manual mode 之退出條件，與之不同 | 生成時以 CFTS092 原文為準，`8 mph`／`10s` 不加 `e.g.` | PENDING |
| A-CA05 | **`VF617V5` 與 `VF617_V5` 拼寫並存** | `SWE-CAM-003` 之 `Source ID` 欄逐字：`CFTS092, VF551_V2, VF551_V33, VF551_V4, VF551_V42, VF617V5, VF617_V5` —— 同一份文件出現兩種拼法；`Source Requirement ID` 側對應 `SYS-RA-VF617V5-*` 2 個、`SYS-RA-VF617_V5-*` 117 個 | 視為同一文件；DR-CAM-a 補件時一併請上游統一 | PENDING |
| A-CA06 | **重疊列（同一批來源被兩列瓜分）** | 實測兩兩交集：`-004 ∩ -009` = **20**（母體 24／27）；`-015 ∩ -018` = **9**（42／35）；`-012 ∩ -014` = **5**（6／6）；`-020 ∩ -025` = **1/1**（`SYS-RA-VF551_V33-227`，兩列唯一來源完全相同，僅分屬 Daemon 與 App）| 逐組判其為「同一驗證點之分層」抑或「應併」；`-020`／`-025` 一組建議以 sibling 處理 | PENDING |
| A-CA07 | **下放包未列之重疊列**（本包全量掃出，交集 ≥3）| `-002 ∩ -010` = 9；`-009 ∩ -023` = 7；`-003 ∩ -022` = 5；`-001 ∩ -023`／`-003 ∩ -016`／`-008 ∩ -023`／`-010 ∩ -023`／`-016 ∩ -023`／`-017 ∩ -023` 各 4；`-001 ∩ -003`／`-002 ∩ -003`／`-004 ∩ -023`／`-010 ∩ -017` 各 3 | 與 A-CA06 同案處置；`SWE-CAM-023` 與 6 列有交集，宜優先釐清 | PENDING |
| A-CA08 | **`Sub Categorization` 與 `Description` 相斥** | `SWE-CAM-014` 之 Sub Cat 為 `NormalCameraDaemon`，其 Description 逐字以「**NCD HAL** shall manage the power shutdown notifications…」起首 | Layer 2 歸屬以何者為準，待裁 | PENDING |
| A-CA09 | **`Sub Categorization` 之混合值** | `SWE-CAM-019` 逐字 `NormalCameraApp, NormalCameraDaemon`（25 列中唯一之混合值；另注意此處寫 `NormalCameraApp` 無空格，他列為 `NormalCamera App`）| 拆 sibling 或擇一，待裁 | PENDING |
| A-CA10 | **037 標題之拼寫** | `SWE-CAM-012` Title 逐字 `Message: PowerShutDownNotifcation`（`Notifcation` 缺 `i`），`-014` Description 同拼法 | 若為 LVDS 訊息名之原文即照抄，否則更正；須對 VF551_V2-550 原文核對 | PENDING |

## C. SYS2 匯出之資料品質

| # | 事由 | 實測 | 影響 | 狀態 |
|---|---|---|---|---|
| A-CA11 | **`Category`(K) 欄大小寫不一致** | A 本已解析之 422 個來源，其 Category 分佈為 `Functional Requirement` 309 ＋ `Functional requirement` 77；`Out of Scope` 22 ＋ `Out of scope` 10；`Non Functional Requirement` 2 ＋ `Non Functional requirement` 2 | 任何以字面比對 Category 之篩選皆會漏算。本包之 §6 對帳採**大小寫歸一後**之數（386／32／4），與下放包預期一致 | 已知，量測一律歸一 |

## D. B 本 framework 草案之落差

| # | 事由 | 實測 | 狀態 |
|---|---|---|---|
| A-CA12 | **§5 B 本 Layer 2 之章節前提與 037 實際引用不符** | B 本 230 列實際只引 HeadUnitCameraSystems 章 `6, 27, 28, 29, 30, 31, 33, 34` 與 RVC+PAM 章 `6, 7, 8, 9, 11`。草案所據之 HU 章 `1`／`3`／`4`／`18`–`22`／`26`／`32` **一列未引**，故 Test Set `Camera App`（HU 18–22）實測 **0 列** | PENDING（歸 Pei，本包不改名稱）|
| A-CA13 | **10 列未落入任何草案 Test Set** | HU `6.10`（`Non Surround View Vehicles access to Cameras:`）1 列；RVC+PAM `8.1`（`RVC1)` X 退出鍵）6 列、`8.6`／`8.7`／`8.8` 各 1 列 | PENDING |

## E. 同名異體

| # | 事由 | 實測 | 狀態 |
|---|---|---|---|
| A-CA14 | **SYS1 RVC+PAM 同名兩本** | REF 本 sha16 `5a1c0ab24991dcb1`（55 列）vs `spec-index/cache/` 本 `1a0bef53c6de975c`（64 列）。cache 本獨有 `7.2.1`–`7.2.6`、`7.3.1`–`7.3.3` 九列；其餘 11 列差異僅為換行編碼；Polarion ID 全同。B 本 `SWE1-RVC-016/-017/-018` 引 `7.3.1`–`7.3.3`，**只有 cache 本解得開**（對映率 100% vs REF 本 98.70%）| PENDING（DECISIONS §6-4，已提議用 cache 本）|

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-CAnn]`.
