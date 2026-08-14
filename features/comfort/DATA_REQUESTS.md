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
>
> **更新 2026-08-14（二）（下放包 08 素材落位後）**：#7 **已解**、
> #6 **限縮至 7" 單一問題**（3 節）。兩者皆**非由 #9 之素材解決** ——
> Market Configuration Table 不承載 R1L-R 亦不承載螢幕尺寸；解答來自
> 037 自身之引用結構（詳 A-CF08）。**現行唯一真正缺檔為 #6**。
>
> **次要候選之處置**：08 §3 列 `VINtoArchitecture decoding v3.xlsx` 與
> `Vehicle Category HMI Logic and Flow R1 SR24 Post 2A`。後者已在
> `spec-index/sources/`，依 08 §3「取用前須先驗其確實承載該資訊」實測
> —— **驗不過**（見 #10），不採用。前者全 repo 搜尋**不存在**，
> 若 Pei 判斷其可能承載螢幕配置，需補入（Tier 3）。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| 1 | Comfort 之 FM-WI-FSM-036-A01 TC workbook | ⚠️ **以空白通用範本代替** —— `inputs/…_SWQT_20260121.xlsx`，rev C，SHA256 `cd876c202c71e74b…`（與 Privacy 同一份）。`workbook_state` = BLANK，P4 未阻塞。殘留：非 Comfort 專屬，封面／Scope／Purpose／Reviewer 待填；第 10–11 列樣本待清 | 全 403 leaves | P4 起全部批次 | A-CF07 | Low（僅待確認交付形態） |
| 2 | Scope / Purpose / Reviewer / Project Name / Date 五格之填入值 | ⏳ **待 Pei 給值** —— 非檔案，屬 Tier 2 賦值。執行層提案 Scope = `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1`，其餘不自填 | 交付件表頭 | P7 寫回前必須有值 | A-CF07 | **Medium —— P7 之前** |
| 3 | `pymupdf`（Python 套件，非客戶檔案） | ⚠️ **未安裝，但已不必要** —— 2026-08-14 改以已安裝之 `pdftotext` 實測，SR24 PDF **具 text layer**（62,874 bytes 文字）。餘留者僅 `recon.py` 仍只試 `pymupdf`，故 RECON.md 印 `unknown`；加 fallback 即可（未在 07／08 作業範圍內，未動） | 0（不阻塞） | 僅在 P4 需自 PDF 取圖說／座標時 | A-CF06 | ~~Low~~ → 建議層級 |
| 4 | 客戶交付夾之 SR24 附件回填 | ⏳ **待 Pei 決定** —— 交付夾現放 SR25（PDF 13.86 MB / SYS1 xlsx 72.80 KB），與 R-C1 基線不一致。**執行層未複測**（該樹於本 session 不可達） | 0（不影響取材） | P7 交付一致性 | A-CF02 | Low（P7 之前） |
| 5 | CFTS043 —— `SYS1_CFTS043-HVAC Controls and Displays_Tree view_R1L-R scope.xlsx`（914,043 bytes）＋ `R1LR_Atl-H_25PI3.5_Cabin_CFTS_043 HVAC Controls and Displays _SR26_20250909-1852.doc`（2,469,376 bytes） | ✅ **已入 `inputs/`**（2026-08-14，Pei 放入）—— 20.x 十節之判讀已據此完成 | 10 節（20.1 ~ 20.4.3） | D-C10 裁定 | A-CF08 | ~~High~~ → 已解 |
| 6 | **R1LR ATL-H 之螢幕配置來源** —— 現已限縮為單一問題：**7" 是否屬本次交付之螢幕配置** | ⚠️ **部分解決** —— 供入之 `SR24 R1 Market Configuration Table v1.6.xlsx`（279,779 bytes，SHA256 gate PASS）**不承載螢幕尺寸軸**（全 8 表 0 命中）。10.25"（18.2–18.4）已由 037 引用 18.1 之結構證據解決；**7" 仍無來源** | ~~6~~ → **3 節**（19.1–19.3） | D-C10 裁定；Phase 3 Part N | A-CF08 | **High** |
| 7 | **EMEA 市場適用性來源** | ✅ **已解 —— 但不是靠本項素材** | 1 節（16.1）→ 已判 `in_scope` | —— | A-CF08 | ~~High~~ → 已解 |
| 9 | `SR24 R1 Market Configuration Table v1.6.xlsx` | ✅ **已入 `inputs/`**（2026-08-14，Pei 放入）—— 279,779 bytes，SHA256 `ae4cf0b929b033ac…`，對 25PI3.5 之 `ae4cf0b9…` **PASS**。**判讀結果：不承載 `R1L-R`（0 命中）、不承載螢幕尺寸（0 命中）**；其 variant 軸為市場別非機型別 | 0（未直接解任何節） | —— | A-CF08 | 已解 |
| 8 | CFTS043 4803259 之 NOTE 效力確認（非檔案，屬上游釐清） | ⏳ NOTE 稱「only applicable to R1H starting on SR22」，與同 item `Radio` 含 R1L-R 矛盾（**主檔內部**矛盾；tree view 為索引層，依 §8.6 不參與選邊）。10 節現依 R-C12 記 `undetermined` pending 本項。**送出屬 Tier 3**，依 07 §4 併入 Comfort 之 RD-1 草稿，不單獨發函 | 10 節（20.1 ~ 20.4.3） | **D-C10 裁定** | A-CF12 | **High** |
| 10 | `VINtoArchitecture decoding v3.xlsx`（08 §3 次要候選） | ❌ **全 repo 不存在** —— 未搜到。同節另一候選 `Vehicle Category HMI Logic and Flow R1 SR24 Post 2A`（已在 `spec-index/sources/`）**已先驗且驗不過**：其僅載「文件涵蓋哪些機種」（R1 Low: 7"／8.4"／10.1"／10.25"／12.3"），與 SR24 §1.1 同型，06 §3 已裁此不構成交付範圍證據；且 `R1L-R` 0 命中、`Atlantis` 0 命中、無配置表 | 3 節（19.1–19.3） | D-C10 裁定 | A-CF08 | Medium（僅在 #6 無其他來源時） |

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
