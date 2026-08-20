# DATA REQUESTS — Time Management (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/time_management/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。回報對象為本表，不涉其他 feature。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| 1 | FW036 工作簿（本 feature 之客戶原件）— 全名未知，(pattern) `*_SWQT_*.xlsx` 或客戶指定名 | MISSING | 全部 22（分母之被除數無從取得） | **阻塞 Phase 1 recon 全部**；Phase 2 以後全數不可起 | A-TM07 | **High** |
| 2 | FW036-037-A03 正式釋出件 — (pattern) `SWE1_<Feature>_FM-WI-FSM-037-A03_…_<YYYYMMDD>.xlsx`（對照 SXM：`SWE1_SXM_FM-WI-FSM-037-A03 …_20260406.xlsx`） | UNCONFIRMED — 手上 `SWE1_Secure_Date&Time.xlsx` 是否即為此件待裁 | 22（`SWE-RA-TIME&DATE-001`–`-022`） | **阻塞覆蓋稽核**（分母不得認定）；不阻塞 recon 之工作簿測繪 | A-TM02 | **High** |
| 3 | Pop Up List — 全名未知 | NOT REQUESTED | — | 無 | — | 低（見下註） |
| 4 | 涵蓋全部 126 筆 SYS2 FR 之 037（或「51 筆不在 SW 範圍」之書面依據） | MISSING / 待答 | 51 筆 SYS-RA FR 無對應 SWE leaf | **阻塞覆蓋稽核之分母認定** | A-TM09 | **High** |

## 逐項說明

### #1 FW036 工作簿 — High

缺此件之連鎖後果非「少一個檔」，而是 Phase 1 recon 的五項產出全數無從
取得，詳見 A-TM07 之逐項列舉。特別注意第 3 項：`feature.yaml` 之
`workbook.columns` 現值**全為模板預設、未經實測**。同型先例
`vehicle_setting` 實測後 `design_method` 由 `Q` 位移至 `R`、`author` 由
`Z` 位移至 `AA`。在本件落地前，任何依賴欄位字母之操作都不得執行。

036 母本不需另行索取：R-G1（全域）已固定為
`forms/…_SWQT_20260817_ext.xlsx`。本列所求為**本 feature 之客戶原件**，
非母本。

### #2 037 正式件 — High

手上 `SWE1_Secure_Date&Time.xlsx` 之封面為 `Project Name = New R1L`、
`Date = 2020/09/05`、**Reviewer 欄空白**，且列 6 之模板佔位說明列未清除
（實測見 A-TM02）。日期早於 SYS2 之 SR26 釋出甚多。三項合觀，本件像
未經審查之工作稿。

**所需之答覆有二，任一即可解鎖**：

1. 提供正式釋出件 → 比對其 leaf 集合是否亦為 22 筆連號
2. Pei 明裁「本件即為權威 037」→ 則以其 22 筆為覆蓋稽核分母，本列關閉

在此之前，22 這個數字可用於作業規劃，**但不得寫入任何覆蓋率之分母**。

### #3 Pop Up List — 不主動索取

`intake.py` 之命中測試未在本 feature 之素材中偵測到 popup 引用
（`String/Popup Message` 表頭與 PU-number id 皆未命中）。下放包 §2(3)
明訂「是否被引用由 intake 之命中測試決定，不必預先索取」。若 Phase 1
之 CFTS 全文掃描出現 PU 編號，屆時再登記並升 Urgency。

### #4 037 之覆蓋缺口 — High

執行層於 Phase 0 交叉比對 037 與 SYS2 後發現：037 只引用 75 筆
`SYS-RA-TIME&DATE` 功能需求，SYS2 共 126 筆，**51 筆無對應 SWE leaf**
（覆蓋率 59.5%，且 75 為上界故 59.5% 為上界）。完整量測條件、可靠性論證
與缺口序號清單見 A-TM09。

懸空引用為 0 —— 037 沒有引用任何 SYS2 不存在的 id，故此非 037 引錯，
而是 037 **少做**。

**所需之答覆有二，任一即可解鎖**：

1. 提供涵蓋全部 126 筆 FR 之 037 版本
2. 書面依據說明該 51 筆為何不在 SW 範圍 —— 並須解釋為何其在 SYS2 標為
   `Functional Requirement` 而非 `Out of Scope`（該欄非虛設，全表有 1 筆
   實際使用了 `Out of Scope`）

與 #2 同源，建議合併一次查詢。在此之前，覆蓋率數字不得寫入任何交付物。
