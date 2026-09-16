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
| DR-CAM-e | **車型 ↔ 品牌之權威對照表**（R-CAM5(c) 所指定之 `SR24 R1 Market Configuration Table v1.6.xlsx` 無此欄）| OPEN（需裁定或補件）| 凡帶 `*` 設定之 hop（R-CAM5(b) 之品牌分支）| 品牌分支之切法無權威來源；本包以 PROXI `Brand_Configuration_2` 實測替代，待核可 | A-CA19、DECISIONS §6-8 | **中** —— 已提替代來源與逐格實測，Pei 核可即解 |

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
