# DATA REQUESTS — Camera (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`_intake/Camera/`；落點為 `sources/raw/<doc_id>/`（R-G66）。
each landing closes or advances the linked anomaly. Ordered by when a batch
actually needs it. Names are verbatim from the citing source where the source
gives one; otherwise the expected naming pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| DR-CAM-a | `SYS2_VF551_V5_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA …_SYSRA_VF617_V5_V01.xlsx`（pattern，比照 V2/V3/V33/V4/V42 之命名）**＋** `…_VF617_V5_Rn.docx`（pattern，比照 `Video_Parking_Assistance_…_VF551_Vn_Rn.docx`）| MISSING | A 本 `SWE-CAM-024` 全條（12/12 來源）；`-003`／`-015`／`-018` 之部分來源。合計 **119 個來源引用** | `AUX Camera` Test Set（單列）整組 BLOCKED；`State Handling`／`Display Arbitration` 追溯不完整 | A-CA01、A-CA05 | **高** —— A 本先寫，此件不到則 A 本無法收尾 |
| ~~DR-CAM-b~~ | `SYS2_VF551_V4 …_V01.xlsx` 之 `VF章節`(I) 欄補齊版 | **CLOSED**（2026-09-16）| — | — | A-CA02 | — —— **R-CAM7** 裁定改以 `D` 欄前導號向下繼承（321/321、60 章），不需補件 |
| ~~DR-CAM-c~~ | `SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)` 之版本確認 | **CLOSED**（2026-09-16）| — | — | A-CA14 | — —— **R-CAM6** 裁定以 `spec-index/cache/` 本為追溯母體，不需補件 |
| ~~DR-CAM-d~~ | Camera Settings 之導航 hop label 出處 | **CLOSED**（2026-09-16）| — | — | DECISIONS §6-7 | — —— **R-CAM8** 裁定 HMI Settings List `Settings` row 464 為足夠權威（canon §5.8(c)），不需補件 |
| ~~DR-CAM-e~~ | 車型 ↔ 品牌之權威對照表 | **CLOSED**（2026-09-16，確認型）| — | — | A-CA19 | — —— **R-CAM5(c)′** 以 PROXI `Brand_Configuration_2` 之實測值為據，不需補件 |
| DR-CAM-f | **Atl-Mi 之 `TRANSM2` DBC**（含 `ShiftLeverPosition` 之 `VAL_` 列舉）—— 檔名待上游給，`forms/` 現有四本皆無 `TRANSM*` message 於 Atl-Mi 側 | MISSING | A 本 `-015`／`-018` 之 Atl-Mi 分支（pilot `NR1L-RVC-004`）；全量後凡引 `SYS-RA-VF551_V42-302` 者 | Atl-Mi 之 gear 訊號 raw 值與 label 須標 `PENDING`；候選替代為 `STATUS_CCAN5.ShiftLeverPosition`（`BO_ 998`，`2 "R"`，P363／637MCA 皆有）待上游確認是否同一訊號 | A-CA23 | **高** —— 車型軸之 Atl-Mi 半邊全受影響 |
| DR-CAM-g | **「Controls page」之 HMI entry path** —— SYS1 匯出中給出進入 Controls 頁之逐字 hop label 者 | MISSING | A 本 `-016`（手動入口之 controls page 分支）；B 本 `Activation and Exit` 中凡走 controls page 者 | pilot `NR1L-RVC-005`／`-006` 改走 App Drawer 路徑而不受阻；controls page 分支之 TC 須待此件 | A-CA24 | **中** |
| DR-CAM-i | **`LTM_OperationalModeSts` ↔ `CmdIgnSts` 之值對應表**（V33／V42 之 I/O 表或 LID 對應文件）| MISSING | A 本 `-001` 之關機側（pilot `NR1L-RVC-002`）；全量後凡以 `LTM_OperationalModeSts.Info` 為條件之 V33／V42 列 | 關機序列之 CAN 觸發值無來源，TC 以 `PENDING: DR-CAM-i` 標記 | A-CA25 | **中** |
| DR-CAM-h | **Pop Up List 之 camera out-of-position 條目** —— `Camera Not in position`／`Camera Out of Position` 於 `forms/Pop Up List HMI R1 (26PI).xlsx` 兩串皆 0 命中 | MISSING | A 本 `-025`、B 本 `SWE1-RVC-039`（`Warning Banners`）| 最終畫面文字無權威；A-CA20 無法依 DECISIONS 6-9 之裁定結案 | A-CA20 | **中** —— pilot 不觸及 `-025`，不阻塞本包 |

## §5.3 常數之 PENDING 承接（R-G71）

R-G71 明文：`§5.3` 三常數之 `PENDING` 二條**不得直接複製到新 feature 而不登 DR**。
本 feature 之承接狀態：

| 常數 | 本 feature 是否使用 | `status:` |
|---|---|---|
| `ENTER_SETTINGS_APP`（2 hops，已鎖定，非 PENDING）| **是** —— 為 `ENTER_CAMERA_SETTINGS` 之第 1–2 hop | `status: RESOLVED（沿用既有鎖定值，不複製 PENDING）` |
| `ENTER_VEHICLE_SETTINGS`（first hop PENDING）| 否 —— Camera 之設定位於 Settings App 之 `13. Camera` 類別，非 Vehicle Settings | `status: NOT_APPLICABLE` |
| `ENTER_HOME_SCREEN`（PENDING）| 否 —— 本 feature 現無需自 Home Screen 起步之 procedure | `status: NOT_APPLICABLE` |
| `ENTER_CAMERA_SETTINGS`（本 feature 新增，**R-CAM8 已鎖定**）| 是 | `status: RESOLVED`（2026-09-16）—— 3 hops：`Press "Apps" on Menu Bar to open App Drawer` → `Select "Settings" in the App Drawer` → `Select "Camera"`；ER `The "Camera" settings screen is displayed`。第 3 hop 來源 `HMI Settings List` 分頁 `Settings` row 464 `13. Camera`（序號非 label），canon §5.8(c) |

**FO §4 [ADD] 之 §5.3 承接：完成**（R-G71）—— 四項全部有 `status:`，無 PENDING 複製。
