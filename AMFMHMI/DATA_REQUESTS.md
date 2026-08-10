# DATA REQUESTS — AMFM (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`AMFMHMI/inputs/`; each landing closes or advances the linked anomaly.
Ordered by when a batch actually needs it. Names are verbatim from the
citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

| # | File — full name | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| 1 | **`CIP_Radio_Tables_v6.7.xlsx`** — 已入 `inputs/`（2026-08-10），hash 驗證為 25PI3.5 來源（SHA256 `05e5a1f2…`），與 CFTS024 基線同 release。四 release 內容有差（Default ROW Market Presets、Weather Icons），提醒：若日後基線升版，CIP 要同步換同 release 那份。已驗工作表：`SEEK Cancel_Stop Transitions`、`PI Seek Ordering`、`TA-PTY31 station list cancel e`、Preset Defaults | ✅ 已入 `inputs/` | 005, 006, 010, 011 (+context) | Seek 批 State Transition 狀態列 | A-AM09 | — |
| 1b | **`SR24 R1 Market Configuration Table v1.6.xlsx`** — 已定位：`…/25PI3.5/Reference Docs/ECU Specific Reference Documents/`（四 release 均 v1.6，位元層未驗）。已驗工作表：`Radio Tuner Configuration`、`R1 Tuner Layout`、`Market Config - R1` | ⚠️ 已定位 — **尚未複製入 `inputs/`**（2026-08-10 盤點缺席） | 081–085 (5) | Market Configuration 批需求內容 | A-AM09 | **Market Configuration 批前** |
| 2 | CFTS004 General Diagnostic Requirements — ✅ 已入 `inputs/`（2026-08-10）：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_004_General Diagnostic Requirements_SR26_20250909-1658.docx`（SYS3 引的是較新的 `26PI1.5 Mar Release 20260310`；id 全對得上，Diagnostics 批逐條核對，有 delta 再要 Mar 版） | ✅ 已入 `inputs/` | 097–104 (8) | Diagnostics 批 | A-AM07 RESOLVED | — |
| 2b | 逐需求附件 `4874050- 4595376- CFTSMV024_CIP_R3_O1965_Excel_Document.xls`（DTC 定義表）；其餘 O 附件在 `…/Reference Docs/CFTS024/`（已全數驗明：9 件天線 DTC 表 + 2 件交通圖示表 + 1 件內嵌註記） | ⚠️ 尚未入 `inputs/` | Diagnostics 批 context | DTC 細節 | A-AM07 | Low — Diagnostics 批前 |
| 3 | CFTS011 — ✅ 已入 `inputs/`（2026-08-10）：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_011_Radio Engineering Mode_SR26_20250909-1658.docx` | ✅ 已入 `inputs/` | 087, 089–096 (9) | Engineering Mode 批 | A-AM06 RESOLVED | — |
| 4 | CFTS028 — ✅ 已入 `inputs/`（2026-08-10）：`R1LR_Atl-H_25PI3.5_Speech and Personal Assistant_CFTS_28 Voice Recognition_SR26_20250909_1250.docx`。**檔案不回答範圍問題**：VR 觸發路徑歸屬仍待 Pei 裁（A-AM09 VR class） | ✅ 已入 `inputs/` — 範圍裁決待下 | 003, 009, 025, 027 (4) | VR 補充路徑 | A-AM09 | Medium（裁決） |
| 5 | Radio 用 HMI L&F — **確認無獨立 Radio 版**；Radio 相關 HMI 內容散在四份既有 deck（`…/25PI3.5/HMI/`）：`Media HMI Logic and Flow R1 SR24 Post 2A (July 25th, 2023).pdf`（radio 播放畫面；Media feature 已用過）、`Announcements HMI Logic and Flow R1 SR24 1A (May 3, 2021).pdf`（TA/PTY31 彈窗 — RDS Features 批直接相關）、`Hard Controls HMI Logic and Flow R1 SR24 2A (June 6 2022) CR21100.pdf` + `Steering Wheel Controls HMI Logic and Flow SR24 DCR21423 (august 3 2022).xlsx`（ICS/SWC 輸入路徑）、`APAC Tuner HMI Logic and Flow Logic and Flow SR24 1A (May 27 2021).pdf`（APAC 市場 tuner 畫面） | ✅ 身分已解 — 需用時再引 | 散布 pointer leaves | 畫面/彈窗文字保真度 | A-AM09 | Low |
| 5b | HMI pop-up list — ✅ 已入 `inputs/`（2026-08-10）：`Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` | ✅ 已入 `inputs/` | 彈窗類 leaves | popup 文字 | A-AM09 | — |
| 6 | CFTS019 — ✅ 已入 `inputs/`（2026-08-10）：`R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.docx` | ✅ 已入 `inputs/` | Presets 批部分 | rejection tone 細節 | A-AM09 | — |

已除名：~~CFTS024-707~~ — 是 CFTS024 自身的條款編號（radiotext 行為），非缺檔；條款查找屬 batch context 工作。

Not requested: SWRA-A02-related material (R1/R5 closed it); SYS2/SYSRA
(R6 — not in trace chain).

Standing rule: any newly discovered external reference gets a row HERE at
registration time, not only an anomaly entry — the anomaly records the gap,
this file asks for the data.
