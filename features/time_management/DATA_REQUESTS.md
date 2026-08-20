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
| 1 | ~~FW036 工作簿（客戶預填件）~~ | **CLOSED** — R-TM5 改以 R-G1 母本為之 | — | 已解除（`workbook_state` = BLANK 實測確認） | A-TM07 (RESOLVED) | — |
| 2 | FW036-037-A03 正式釋出件 — (pattern) `SWE1_<Feature>_FM-WI-FSM-037-A03_…_<YYYYMMDD>.xlsx`（對照 SXM：`SWE1_SXM_FM-WI-FSM-037-A03 …_20260406.xlsx`） | UNCONFIRMED — 手上 `SWE1_Secure_Date&Time.xlsx` 是否即為此件待裁 | 22（`SWE-RA-TIME&DATE-001`–`-022`） | 不阻塞 recon；分母已由 R-TM6 定為 SYS2 FR 126，故本列不再阻塞分母 | **A-TM02a** | **High** |
| 3 | Pop Up List — 全名未知 | NOT REQUESTED | — | 無 | — | 低（見下註） |
| 4 | 涵蓋全部 126 筆 SYS2 FR 之 037（或「48 筆不在 SW 範圍」之書面依據） | MISSING / 待答 | 48 筆 SYS-RA FR 無對應 SWE leaf | **阻塞覆蓋稽核之分母認定** | A-TM09 | **High** |
| 5 | 含物件 `6151328` / `6151331` 之 CFTS 版本（或該二物件之遷移去向說明） | MISSING / 待答 | 2 筆（SYS-RA-221 / -224），連帶 SWE leaf 005 / 002 之部分引用 | 該二筆之 `specification_reference` 無章節可寫 | A-TM13 | 中 |

## 逐項說明

### #1 FW036 工作簿 — **CLOSED（2026-08-20）**

R-TM5 裁定本 feature 不索取客戶預填件，036 以 R-G1 全域母本為之。
母本複本已落於 `inputs/`（SHA256 與母本相同，`cmp` identical），
recon 實測 `workbook_state = BLANK`，欄位對映 15 欄由表頭文字解析、
零衝突。原列之五項阻塞逐項解除，交代見 A-TM07 末節。

**本列保留為軌跡，不再回報。**

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

執行層於 Phase 0 交叉比對 037 與 SYS2 後發現：037 只引用 78 筆
`SYS-RA-TIME&DATE` 功能需求，SYS2 共 126 筆，**48 筆無對應 SWE leaf**
（覆蓋率 61.9%）。首版誤報 75/51/59.5%，經 00R §2 更正；完整量測條件、
78 筆與 48 筆之 id 清單、更正經過見 A-TM09。

懸空引用為 0 —— 037 沒有引用任何 SYS2 不存在的 id，故此非 037 引錯，
而是 037 **少做**。

**所需之答覆有二，任一即可解鎖**：

1. 提供涵蓋全部 126 筆 FR 之 037 版本
2. 書面依據說明該 48 筆為何不在 SW 範圍 —— 並須解釋為何其在 SYS2 標為
   `Functional Requirement` 而非 `Out of Scope`（該欄非虛設，全表有 1 筆
   實際使用了 `Out of Scope`）

與 #2 同源，建議合併一次查詢。在此之前，覆蓋率數字不得寫入任何交付物。

### #5 CFTS 基線缺口 — 中

SYS2 之 `SYS-RA-TIME&DATE-221` / `-224` 引用來源物件 `6151328` / `6151331`，
該二 id 在現行 CFTS（SR26 `20250909-1851`）**零命中**（全檔 `615\d{4}`
形態搜尋，執行層對原始 docx 實測）。詳見 A-TM13。

**Urgency 定為中而非 High 之理由**：不阻塞 recon，亦不阻塞 leaf 005 / 002
之整體生成 —— 兩 leaf 之其餘引用皆有章節可達。僅該二筆對應無章節可寫，
且處置明確（不得以鄰近章節填充，§8.4.1）。

與 #2（037 版本身分）同屬上游版本對齊，**建議併入 RD-1 一次問**。
