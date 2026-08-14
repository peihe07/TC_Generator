# DATA REQUESTS — Comfort (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/comfort/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（下放包 01 §5.5；沿用 AMFM／Privacy）**：任何新發現之外部
引用，登記 anomaly 的同時**必須**新增一列於此表；且每次 session opener 與
batch gate 都要按 Urgency 回報。

> 建檔時（2026-08-14 Phase 1）**無已知缺檔** —— 037 所引用之唯一文件
> （SR24 CR24879）已在 `spec-index/`，129 節逐一查得，miss = 0。本表非空，
> 但列的是「非檔案」與「環境」兩類請求，不是缺檔。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| 1 | Comfort 之 FM-WI-FSM-036-A01 TC workbook | ⚠️ **以空白通用範本代替** —— `inputs/…_SWQT_20260121.xlsx`，rev C，SHA256 `cd876c202c71e74b…`（與 Privacy 同一份）。`workbook_state` = BLANK，P4 未阻塞。殘留：非 Comfort 專屬，封面／Scope／Purpose／Reviewer 待填；第 10–11 列樣本待清 | 全 403 leaves | P4 起全部批次 | A-CF07 | Low（僅待確認交付形態） |
| 2 | Scope / Purpose / Reviewer / Project Name / Date 五格之填入值 | ⏳ **待 Pei 給值** —— 非檔案，屬 Tier 2 賦值。執行層提案 Scope = `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1`，其餘不自填 | 交付件表頭 | P7 寫回前必須有值 | A-CF07 | **Medium —— P7 之前** |
| 3 | `pymupdf`（Python 套件，非客戶檔案） | ❌ **未安裝** —— `pip install pymupdf` 即可，無需改碼；裝後重跑 recon 該行自動變為實測值。專案無 requirements 檔宣告此相依 | 0（不阻塞） | 僅在 P4 需自 PDF 取圖說／座標時 | A-CF06 | Low |
| 4 | 客戶交付夾之 SR24 附件回填 | ⏳ **待 Pei 決定** —— 交付夾現放 SR25（PDF 13.86 MB / SYS1 xlsx 72.80 KB），與 R-C1 基線不一致。**執行層未複測**（該樹於本 session 不可達） | 0（不影響取材） | P7 交付一致性 | A-CF02 | Low（P7 之前） |

## 已量測、無需索取

- **SR24 spec 素材三件**：`spec-index/cache/` 之 SYS1 export（68.40 KB 級，
  SHA256 `6982d37db81b36e4…`）與 JSON（10.57 MB）、`spec-index/sources/` 之
  PDF（6.16 MB，SHA256 `fc5d3cd1d524f4d5…`）。三者齊備，outline map 已建，
  129/129 查得。**不搬入 `inputs/`** —— 共用語料庫留在 `spec-index/`，
  `feature.yaml` 以相對路徑回指。
- **SR25 CR29359**：同目錄存在，但 R-C1 定其為 out-of-scope 參考資料。
  **不索取、不引用、不作為查得依據**（A-CF01）。

## Not requested

- SYS.2 / SYSRA 安全分析件 —— recon 實測 037 **無 ASIL/FTTI 欄位**，
  安全分析層在本 feature 之 403 leaves 上無附著點，不進 trace chain
  （比照 AMFM R6 / Privacy 前例）。
- Pop Up List —— 037 未引用；`paths.popup_list` 為 null。若 Phase 4 之條文
  出現 PU 編號，依 standing rule 當場登記 anomaly 並補列於本表。
