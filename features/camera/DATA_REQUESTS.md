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
| DR-CAM-b | `SYS2_VF551_V4 …_V01.xlsx` **之 `VF章節`(I) 欄補齊版**（或上游確認該欄可由 `Description` 前導號取代）| MISSING | A 本引用之 44 列 V4（Layer 3 來源）| Layer 3 於 V4 來源之列無法逐字取號 | A-CA02 | **中** —— 已提替代判法（DECISIONS §6-5），Pei 採納即可降為「不需補件」 |
| DR-CAM-c | `SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)` **之版本確認** —— 兩本同名異體並存，請上游確認何者為現行 | OPEN（無需新檔，需裁定）| B 本 `SWE1-RVC-016`／`-017`／`-018`（引 `7.3.1`–`7.3.3`）| 用 REF 本則此 3 列追溯 BLOCKED（對映率 98.70%）；用 cache 本則 100% | A-CA14 | **中** —— 已提議用 cache 本，Pei 裁即解 |
| DR-CAM-d | **Camera Settings 之導航 hop label 出處** —— SYS1 匯出中給出「進入 Settings 後選取 Camera 類別」之 hop 者 | MISSING | 凡 procedure 需進 Camera 設定之 leaf（B 本 `Camera Settings` Test Set 5 列，及 A 本引設定 hop 者）| §5.3 常數 `ENTER_CAMERA_SETTINGS` 之第 3 hop 無 SYS1 權威，依 §5.8(d) 不得臆造 | DECISIONS §6-7 | **中** |

## §5.3 常數之 PENDING 承接（R-G71）

R-G71 明文：`§5.3` 三常數之 `PENDING` 二條**不得直接複製到新 feature 而不登 DR**。
本 feature 之承接狀態：

| 常數 | 本 feature 是否使用 | `status:` |
|---|---|---|
| `ENTER_SETTINGS_APP`（2 hops，已鎖定，非 PENDING）| **是** —— 為 `ENTER_CAMERA_SETTINGS` 之第 1–2 hop | `status: RESOLVED（沿用既有鎖定值，不複製 PENDING）` |
| `ENTER_VEHICLE_SETTINGS`（first hop PENDING）| 否 —— Camera 之設定位於 Settings App 之 `13. Camera` 類別，非 Vehicle Settings | `status: NOT_APPLICABLE` |
| `ENTER_HOME_SCREEN`（PENDING）| 否 —— 本 feature 現無需自 Home Screen 起步之 procedure | `status: NOT_APPLICABLE` |
| `ENTER_CAMERA_SETTINGS`（本 feature 新增候選）| 是 | `status: PENDING — DR-CAM-d`；第 3 hop label 現僅有 `HMI Settings List` 分頁 `Settings` 列 464 之類別名 `13. Camera` 為據 |
