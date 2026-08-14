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
>
> **更新 2026-08-14（下放包 06 §3 判讀後）**：**現有兩項真正的缺檔**
> —— #6（R1LR ATL-H 機種／螢幕尺寸配置）與 #7（EMEA 市場適用性）。
> 兩者各自阻擋 6 節與 1 節之適用性判定，合計 7 節維持 `undetermined`。
> **此為缺料，非判定** —— 依 06 §3，讀不到即 `undetermined`，
> 不得以讀不到判 `out_of_scope`。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| 1 | Comfort 之 FM-WI-FSM-036-A01 TC workbook | ⚠️ **以空白通用範本代替** —— `inputs/…_SWQT_20260121.xlsx`，rev C，SHA256 `cd876c202c71e74b…`（與 Privacy 同一份）。`workbook_state` = BLANK，P4 未阻塞。殘留：非 Comfort 專屬，封面／Scope／Purpose／Reviewer 待填；第 10–11 列樣本待清 | 全 403 leaves | P4 起全部批次 | A-CF07 | Low（僅待確認交付形態） |
| 2 | Scope / Purpose / Reviewer / Project Name / Date 五格之填入值 | ⏳ **待 Pei 給值** —— 非檔案，屬 Tier 2 賦值。執行層提案 Scope = `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1`，其餘不自填 | 交付件表頭 | P7 寫回前必須有值 | A-CF07 | **Medium —— P7 之前** |
| 3 | `pymupdf`（Python 套件，非客戶檔案） | ❌ **未安裝** —— `pip install pymupdf` 即可，無需改碼；裝後重跑 recon 該行自動變為實測值。專案無 requirements 檔宣告此相依 | 0（不阻塞） | 僅在 P4 需自 PDF 取圖說／座標時 | A-CF06 | Low |
| 4 | 客戶交付夾之 SR24 附件回填 | ⏳ **待 Pei 決定** —— 交付夾現放 SR25（PDF 13.86 MB / SYS1 xlsx 72.80 KB），與 R-C1 基線不一致。**執行層未複測**（該樹於本 session 不可達） | 0（不影響取材） | P7 交付一致性 | A-CF02 | Low（P7 之前） |
| 5 | CFTS043 —— `SYS1_CFTS043-HVAC Controls and Displays_Tree view_R1L-R scope.xlsx`（914,043 bytes）＋ `R1LR_Atl-H_25PI3.5_Cabin_CFTS_043 HVAC Controls and Displays _SR26_20250909-1852.doc`（2,469,376 bytes） | ✅ **已入 `inputs/`**（2026-08-14，Pei 放入）—— 20.x 十節之判讀已據此完成 | 10 節（20.1 ~ 20.4.3） | D-C10 裁定 | A-CF08 | ~~High~~ → 已解 |
| 6 | **R1LR ATL-H 之機種／螢幕尺寸配置來源** —— 能回答「7" 與 10.25" 是否屬本交付範圍」者。預期形態：PROXI／Market Configuration Table，或 R1L-R 之機種配置表（pattern） | ❌ **未入 `inputs/`** —— CFTS043 全篇無 `Comfort Widget`／`Home screen`／`10.25` 字串，**不涵蓋**此判準（非否定）。SR24 §1.1 列有 7" 機種，但「spec 有寫」不等於在交付範圍內（06 §3） | 6 節（18.2–18.4、19.1–19.3） | **D-C10 裁定；Phase 3 Part N** | A-CF08 | **High** |
| 7 | **EMEA 市場適用性來源** —— 能回答「EMEA ICS CARRYOVER 是否屬本交付範圍」者。預期形態：Market Configuration Table 或含 EMEA 值之 SYS1 對照表（pattern） | ❌ **未入 `inputs/`** —— CFTS043 主檔 442 頁 `EMEA` 命中 **0**，tree view Description 亦 0；其 `Market` 欄全部相異值僅 `All`／`NAFTA`／`NAFTA - Mexico`／`NAFTA - United States, Canada`，**無 EMEA 值可比對** | 1 節（16.1） | **D-C10 裁定** | A-CF08 | **High** |
| 8 | CFTS043 4803259 之 NOTE 效力確認（非檔案，屬上游釐清） | ⏳ NOTE 稱「only applicable to R1H starting on SR22」，與同 item `Radio` 含 R1L-R 及 `Scope=Yes` 白名單矛盾。本次判讀採結構化欄位，**此為選擇非推導** | 10 節（20.1 ~ 20.4.3） | D-C10 裁定 | A-CF12 | **Medium** |

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
