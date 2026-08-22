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
| 6 | CAN 網段依據 —— DBC 或 EE 架構文件 | MISSING | 全部含 CAN 訊號斷言之 leaf | **阻塞訊號三件組之 segment 一件**（canon §8.7.5 / R-TM49）| R-TM49 | **High** |
| 8 | ECU 軟體重置（不斷電）之操作方式 —— 測試團隊之 Bench 操作說明 | MISSING / 待答 | 018（連帶 008 / 011 / 021 之 reset 情境）| 不阻塞生成（步驟寫佔位）；**阻塞該情境 TC 之實際執行** | — | **High** |
| 9 | CAN sleep 之可觀察終止條件 —— 診斷工具之匯流排狀態判準 | MISSING / 待答 | 021 / 011（sleep→wake 情境）| 同上 | — | **High** |
| 10 | Bench 之 GPS 訊號控制能力 —— 使不可用／恢復／**位置設定**三項 | MISSING / 待答 | 001–005 / 012 / 014 / 015 / 019 | 同上；**若位置不可設，003 整片不可測** | — | **High** |

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

### #6 CAN 網段依據 — High（2026-08-21 新增）

canon §8.7.5（R-TM48 使其於本 feature 生效）要求 CAN 訊號斷言寫三件組
`<Signal> in <MESSAGE> on <segment>`，且**網段須有 DBC 或架構文件依據，
查無者標 PENDING 不得杜撰**。

本 feature 之 intake 素材為三份 —— CFTS015 docx、SYS2 匯出、037 分析報告
（見 A-TM02a），**無 DBC，亦無 EE 架構文件**。

**三件組之前兩件有來源**：CFTS015 內文確有 MESSAGE 名
（`TELEMATIC_TIME_DATE`、`TIME_DATE` 等）。**只有 segment 一件缺。**

**例外（R-TM49）**：CFTS015 內文若對某訊號明確敘明其網段
（如物件 4814098 之「set a BH-CAN message」），該敘述即為來源，得直接用，
並於 reasoning 註明其物件 id。**B1 生成時逐訊號判定，不得一律標 PENDING
亦不得一律填。**

## `PENDING: DR-{n}` 之錨對照（canon §8.4.3 / R-TM48）

依 canon §8.4.3，欄位因來源缺失無法填寫時寫 `PENDING: DR-{n}`，
不得留空、不得填 NA。本 feature 現行之三處佔位與其 DR 號：

| 佔位字串 | 欄位 | DR | 對應 anomaly |
|---|---|---|---|
| `PENDING: DR-2 037 正式報告檔名` | D5 範圍 Scope | **DR-2**（既有）| A-TM02a / A-TM11 |
| `PENDING: DR-5 CFTS015 缺件物件 6151328 / 6151331` | 005 / 002 之 spec_reference 與 Remarks | **DR-5**（既有）| A-TM13 |
| `PENDING: DR-6 CAN 網段依據（無 DBC／架構文件）` | 訊號三件組之 segment | **DR-6**（本次新增）| R-TM49 |
| `PENDING: DR-8 ECU 軟體重置之操作方式` | `ECU_RESET` 步驟常數 | **DR-8**（09 新增）| — |
| `PENDING: DR-9 CAN sleep 之可觀察終止條件` | `CAN_SLEEP` 步驟常數 | **DR-9**（09 新增）| — |
| `PENDING: DR-10 Bench 使 GPS 訊號不可用／恢復之操作方式` | `GPS_LOST` / `GPS_RESTORE` 步驟常數 | **DR-10**（09 新增）| — |

**前兩筆復用既有號碼，未重複登記** —— `05Z` T2 之表列前兩項
（037 正式報告、CFTS015 缺件物件）與既有 DR-2、DR-5 為同一缺件，
另立新號會使同一缺件有兩個 DR，`PENDING` 佔位之指向即不唯一。

**`NA` 之界線**：canon §8.4.3 明訂 `NA` 僅限「確認不適用」。故
`input_test_data` 之 `NA`（canon §4.5：資料已屬 PC/Procedure 者）仍合法，
其為「確認不適用」而非「缺件」。**兩者不得混用。**

## DR-8 / DR-9 / DR-10 —— 設備能力三問（2026-08-22，下放包 `09` §3.2）

三者皆為**設備能力**之缺件，非文件缺件：分析層 `08` §3.4 之常數表 v1
所寫之 `Remove the GPS antenna …` 為對 Bench 設備之推測、無來源，
依 canon §8.4.1 不得寫入，故 v2 改為 `PENDING: DR-n`（`09` §3.2）。

**三者不阻塞 B1 之生成**（步驟寫佔位，DR 答覆後替換），
**但阻塞該三類情境 TC 之實際執行**，故 Urgency 一律 High。

### DR-10 須一併問「位置設定」（`09` §3.3）

常數表 v2 之 `CROSS_TIME_ZONE = 'Move the vehicle position across a time
zone boundary'` 假設 Bench 可模擬車輛位置。分析層保留該具體措辭而非改
佔位，理由為「GPS 模擬器之位置設定為 GPS 測試之基本能力，若連位置都不能
設，003（GPS Time Calculation）整片皆不可測 —— 該假設若不成立，
問題大於一個常數」。**故 DR-10 之三問須一併答**：使不可用、恢復、位置設定。

### **DR-7 為空號** —— 執行層回報

本 feature 之既有 DR 最大號為 **6**（實測：全 feature 目錄下曾用之號為
DR-2 / DR-5 / DR-6），故下一個可用號本應為 **7**。
下放包 `09` §5 T5 明文指定 8 / 9 / 10，執行層**依令配號**，
未自行前移 —— DR 號為識別碼，改動指定值須經裁定。

**DR-7 因此成為未使用之空號。** 於此明記，使日後讀者不會將其誤認為
遺失之登記。**提請裁定**：是否改配 7 / 8 / 9，或維持並保留此註記。
（空號本身不影響指向唯一性，故執行層未逕改。）
