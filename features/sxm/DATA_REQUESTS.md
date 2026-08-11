# DATA_REQUESTS — FW036 SXM

Files the corpus needs but did not arrive with the drop, and files whose
identity or version had to be established before use. One row per file.

Standing rule (carried from AMFM): any newly discovered external reference
gets a row HERE at the moment it is found, with the citing leaves named — not
after the batch that needs it stalls.

| # | File — full name | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| 1 | **`SYS3_SXM_FM-WI-FSM-011-A01 系統架構設計 System Architectural Design_SYSAD_v0.2_20260629.docx`** — 已入 `inputs/`（2026-08-10；1,202,688 bytes；SHA256 `9acb9eb2…`）。038 的 `Source Requirement ID` 欄逐條指 `SYSAD_SXM_APP` / `_PAL` / `_HAL`，此檔即其定義來源（三者各出現 1 次，於 24 張表格的架構分解中）。**三版並存，內容互異**：`20260323` `52d7528f…`（899,697 B）／`20260511` `145ecac1…`（1,023,382 B）／`v0.2_20260629` `9acb9eb2…`（1,202,688 B）。取 v0.2 版與 DECISIONS §1 的裁決一致，亦與 AMFM 取的 SYSAD 版次同日（AMFM 用 `SYS3_AMFM_…v0.2_20260629`）。版次差異未逐段比對——若 Phase 4 的元件追溯出現對不上的情形，先比三版再開 anomaly | ✅ 已入 `inputs/` | 全部 202（source 欄） | Phase 4 元件追溯；leaf→component→spec 鏈 | A-SX06（同版號異 hash 類） | — |
| 2 | **`SiriusXM 360L HMI Logic and Flow R1.pdf`**（26PI2.5 資料夾，內部標題 `…SR24 Post 2A (December 15 2021)`）+ 同目錄 `…Change Log.xlsx` — 已入 `inputs/`，但**僅作版本 diff 素材，不在 spec 主線**（DECISIONS §1 裁決：SR24 1A SAT Only 留在主線）。230 頁完整 360L 規格 vs 基線 85 頁 SAT-only 子集；頁標題精確重疊 19、僅存於新檔 211、基線無對應 21。Change Log 僅一筆 CR0002（2026-05-20，SOA Implementation 新增一頁），不足以解釋 145 頁差距 | ✅ 已入 `inputs/` — reference-only, off spec line | 0（不供任何 leaf 引用） | 無；若日後改裁新檔為主線，屬**重新界定範圍**而非重跑 | — | — |
| 3 | `CIP_Radio_Tables_v6.7.xlsx` — 由 `AMFMHMI/inputs/` 同源複製，兩側 SHA256 `05e5a1f2…` 位元相同。引用者：009 / 012 / 017（`'SEEK Cancel_Stop Transitions'` 工作表）、036（預設台演算法，原文誤植為 `'CIP_ Radio_Tables'`）。工作表存在確認：`SEEK Cancel_Stop Transitions` ✅；預設台演算法對應 `Preset Defaults- R1` 或 ` Predefined Presets -X65 chip  `，何者為指涉對象屬 Phase 3 問題 | ✅ 已入 `inputs/` | 009, 012, 017, 036 (+Seek Down 對偶) | Seek 批 cancel/stop 判準；Presets 批預設值 | — | — |
| 4 | `R1LR_Atl-H_25PI3.5_…CFTS 024_Specific HU Radio Functions_20250910_1239.docx` — 由 `AMFMHMI/inputs/` 同源複製，兩側 SHA256 `e5c12e9e…` 位元相同。191/202 leaf 的 id 尾標精確命中此檔條款錨點（§1.5.x SAT 章節） | ✅ 已入 `inputs/` | 191 / 202 | 全批次的 spec 主線（DECISIONS §1 裁定 mode D） | — | — |
| 4b | **`R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.docx`** — 由 `AMFMHMI/inputs/` 同源複製，雙側 SHA256 `5a549719a8c6ac03…` 位元相同（2026-08-10）。引用者：leaf **107**（`CFTS019-494`、`CFTS019-496`，短碼，A-SX02 類）。AMFM 已驗此檔的條款為 7 位錨點（486xxxx），短碼 494/496 在其中**不存在** — 檔案到位不等於引用可解，處置走 R11 引用式 | ✅ 已入 `inputs/` | 107 | Browse Presets 批（§1.5.12.1） | A-SX02 | — |
| 4c | **`R1LR_Atl-H_25PI3.5_Cabin_CFTS_020 ICS and DCSD _SR26_20250909-1852.doc`**（1,438,720 B；SHA256 `f2004bd7…`）+ **`…_20250910_1124.reqifz`**（1,790,642 B；SHA256 `c9bbd3b8…`）。CFTS020 = Cabin 子系統的 ICS 硬鍵與 DCSD，leaf **137** 引 `CFTS020-138` 合理。**`.reqifz` 探測成功**：2,644 個 spec object，全數帶 7 位 `ReqIF.ForeignID`（4819125–4822056，與 CFTS024 範圍完全不相交），2,170 筆同時具備 outline 編號與全文 → **id ↔ 條款 ↔ 章節可直接映射，不需 .doc 轉檔**。但短碼 `138` 在 ForeignID / Source Id / Name 三個欄位皆**不存在**，A-SX02 的升級條件因此**未達成** | ✅ 兩件已入 `inputs/` | 137 | Scroll/List 批（§1.5.13）context | A-SX02 | — |
| 4d | **`…CFTS 024_Specific HU Radio Functions_20250910_1224.reqifz`**（1,263,447 B；SHA256 `325dba60d1c91760…`）+ **`…CFTS 019_Audio Management_20250910_1226.reqifz`**（6,398,573 B；SHA256 `6a5b81a5f8bf9b62…`），皆取自 25PI3.5，與現用 .docx 同 release、同日相隔 15 分鐘匯出。CFTS024 ReqIF：1,604 clauses；CFTS019 ReqIF：1,989 clauses。用途有二 —— (a) 短碼終判的第四格式證據（見 A-SX02）；(b) CFTS024 條款來源換源評估（見 `docs/reqif-vs-docx.md`，202/202 一致） | ✅ 已入 `inputs/` | 全部 202 | Phase 4 建圖機制 | A-SX02 | — |
| 7 | **SDARS Predefined Presets 表** — leaf 036 引 `"Pre-defined Presets Algorithm" defined in 'CIP_ Radio_Tables*'`；追查所供 CIP v6.7：`Preset Defaults- VP3&4` 第 13 列轉指 SDARS 工作表，而 ` Predefined Presets -X65 chip  ` **只有一格註記、無表格無演算法**（類比側的 `Preset Defaults- R1` 則完整）。History 列記載該工作表確為 X65 晶片新增 | ⚠️ **內容缺失**（檔案在、工作表在、內容空） | 036 | Presets 批已生成，但預設台**內容**未覆蓋 | A-SX13 | Presets 批複審前 |
| 8 | `SX-9845-0166 - Channel Graphics Service Protocol Specification (XM Band)` — leaf 001 條文要求符合此規格。**未在 inputs/**，其規則面（影像格式、傳輸協定、更新時序）無從驗證；001 的 TC 只驗影像對應目前頻道而顯示，不驗協定符合性（§8.4.2）。同節另有 11 條供應商規格符合性條款各引不同 SX/RX 文件（見 A-SX14），全數未提供 | ⚠️ 未提供 — 依 §8.4.2 不納入驗證範圍 | 001（+§1.5 的 11 條無 leaf 條款） | 無阻塞 | A-SX14 | Low |
| 5 | Pop Up List — **未被引用**：202 條 leaf 標題內無 PU 編號。AMFM 有 `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx`，SXM 若日後出現彈窗字串比對需求再引 | — 不需要 | 0 | — | — | — |
| 6 | Market Configuration Table — **未被引用**：202 條 leaf 標題內零次提及。與 AMFM 不同（AMFM 的 039/081–085 依賴它） | — 不需要 | 0 | — | — | — |

## Cross-feature same-source policy

第 3、4 列的檔案是從 `AMFMHMI/inputs/` 複製而非另行取得。兩側 SHA256 皆已比對
為位元相同，複製動作與來源路徑記錄於此列。**同版號異 hash 的風險見 A-SX06**：
`SR24 R1 Market Configuration Table v1.6` 在四個 release 下有四種內容，SYSAD
亦三版並存，所以「檔名相同」不足以證明「內容相同」，跨 feature 引用一律以
hash 對齊。
