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
| 6 | CAN 網段依據 —— DBC 或 EE 架構文件 | **Atlantis High 已解除；Atlantis Mid 未解除** —— 見下節之狀態更正 | 全部含 CAN 訊號斷言之 leaf | Atl-Mid 側 11 個 LID 有訊號而網段未載 | R-TM49 / A-TM26 | **中（Atl-Mid 側）** |
| 11 | ~~35 個 Atl-Mid 專屬物件之 Atl-H 對應需求~~ | **CANCELLED（2026-08-22，R-TM75(2)）** —— 其所登記之缺件不存在：該 35 個物件之 Radio 標籤 35/35 含 R1L/R1L-R，即本專案；Atl-Mid 為本專案之另一 EE architecture 變體。約 40 處佔位改為真值。**不刪除本列**（軌跡，R-TM13） | 該 35 個條目之 spec_reference；**020 / 021 兩片之全部條目** | 不阻塞生成（寫佔位）；阻塞該等條目之最終值 | A-TM27 | **High** |
| 12 | UI 標籤之正式名稱 | **RESOLVED（2026-08-22）** — 新版 HMI Settings List R1L-R (2026-02-13) §7-5 `Show Time in Status Bar`（Technical Ref CFTS015） | 含 UI 操作之步驟措辭 | 見 `11` 上繳 §4 | — | **High** |
| 13 | Logical Identifiers and CAN Mapping v1_76.xlsx | **RECEIVED（2026-08-22，Pei 補入）** | 全部含 CAN 訊號斷言之 leaf | 解除 DR-6 之來源 | A-TM26 | — |
| 14 | CFTS015 inline RTF 三份（`4814254-…_O833_116`、`4814255-…_O882_117`、`4814256-…_O922_118`）| **RECEIVED（2026-08-22，Pei 補入）** | 未定 —— 內容未解析 | 未評估 | — | — |
| 15 | CFTS015 ReqIF 匯出（`…_20250910_1122.reqifz`）| **RECEIVED（2026-08-22，Pei 補入）** | 全 22 片（結構化來源）| 未評估 | — | — |
| 16 | SR24 R1 Market Configuration Table v1.6 | **RECEIVED（2026-08-22，Pei 補入）** | 012 / 013（市場別時區規則之候選來源）| 未評估 | — | — |
| 17 | HMI Settings List R1 SR24 Post 2A (June 15 2023) | **SUPERSEDED（2026-08-22）** — 由 DR-21 之 R1L-R (Feb 13 2026) 取代；**不刪除**（R-TM13）| 001 / 002 / 011 / 015 / 016（UI 標籤）| **已用於 `11` T4** | — | — |
| 18 | CFTS_036 HMI Framework | **RECEIVED（2026-08-22，Pei 補入）** | 007（HMI requirements）| 未評估 | — | — |
| 19 | CFTS_014 Internationalization Localization | **RECEIVED（2026-08-22，Pei 補入）** | 003 / 012 / 013（地區別時間日期格式）| 未評估 | — | — |
| 20 | 注入無效／缺失時間訊號之操作方式（G2）| MISSING / 待答 | 009 / 010 / 022 | 不阻塞生成（步驟寫佔位）；**阻塞該類 TC 之實際執行** | — | **High** |
| 8 | ECU 軟體重置（不斷電）之操作方式 —— 測試團隊之 Bench 操作說明 | MISSING / 待答 | 018（連帶 008 / 011 / 021 之 reset 情境）| 不阻塞生成（步驟寫佔位）；**阻塞該情境 TC 之實際執行** | — | **High** |
| 9 | CAN sleep 之可觀察終止條件 —— 診斷工具之匯流排狀態判準 | MISSING / 待答 | 021 / 011（sleep→wake 情境）| 同上 | — | **High** |
| 7 | （未使用之空號）| —— | —— | 分析層於 `09` 包指定 DR-8/9/10 時未查既有最大號（時為 6），致 7 被跳過。**非遺失之登記**（R-TM60 包 §3：維持現配，因號碼已寫入兩處而空號成本僅一行註記，成本不對稱）| — | — |
| 10 | Bench 之 GPS 訊號控制能力 —— **四項分列**（見下節） | MISSING / 待答 | (i)(ii) 004 / 005；**(iii) 003 / 012；(iv) 003 / 013** | 同上；**(iii)(iv) 為 003 / 012 / 013 三片之關鍵路徑，不具該能力即不可測** | — | **High** |

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

## DR-10 敘述更新（2026-08-22，下放包 `10` §2）

原敘述「Bench 之 GPS 訊號控制能力（使不可用／恢復／位置設定）」
**四項分列**，且影響片數由 1 更正為 3：

```
DR-10 敘述更新（2026-08-22）

  (i)   使 GPS 訊號不可用          → 004 GPS Fallback、005 Internal Clock
  (ii)  恢復 GPS 訊號               → 同上
  (iii) 設定 GPS 位置（跨時區邊界）  → **003、012**
  (iv)  設定 GPS 時間（跨 DST 切換點）→ **003、013**

**(iii)(iv) 為 003 / 012 / 013 三片之關鍵路徑** —— 若 Bench 不具該能力，
該三片無可執行之觸發操作，屬不可測而非待補措辭。

Urgency 維持 High；影響片數由 1 更正為 **3**（另 (i)(ii) 影響 2 片）。
```

**成因（分析層自陳）**：v1 之 `Remove the GPS antenna …` 是對設備之推測，
v2 之 `SET_TIME_ZONE` / `DST_ON/OFF` 是對 UI 之推測，
且第二次還為 `CROSS_TIME_ZONE` 寫了一段不必改佔位之辯護。
**兩者皆為「照常識推、未回查 spec 或設備」**（R-TM60）。

## DR-7 —— 未使用之空號（2026-08-22 定案）

`09` 上繳 §4 提請裁定是否改配 7/8/9。**分析層裁定維持現配**：
DR 號已寫入常數表之佔位字串與本檔兩處，改號需同步兩處，
而空號之成本僅為一行註記 —— **成本不對稱**。

**成因為分析層之配號錯誤**（指定 8/9/10 時未查既有最大號，時為 6），
非執行層之處置錯誤：執行層依令配號且明確回報空號，處置正確。

## DR-6 之解除條件（2026-08-22，下放包 `11` §3）

LID 表已到，其 `CAN` 欄即 segment 之權威來源。**解除有兩個前提**：

1. 取值須來自 **Atlantis High 欄**（A-TM26 —— `CAN Mapping` 分頁為欄 26–30）
2. 該 LID 在 Atlantis High 欄**有值**

實測（`11` T3）：**14 個時間日期 LID 全部有值，CAN 一律為 `FD`**。
故 DR-6 對該 14 個 LID **已解除**，其 segment 取自
`data/lid_atlantis_high.tsv`。

**`R-TM49` 之例外條款與 LID 表併行時，以 LID 表優先**（`11` §3）——
前者是敘述，後者是對映表。若兩者衝突，回報不逕採。

### DR-6b —— **未登記**（依 R-TM62 取消）

`11` T2 原指派新增 DR-6b（Atlantis High 欄無值之 LID 之處置）。
**下放包 `12` §1 之 R-TM62 明文取消該登記**：五個 `TLM_MANAGED_TIME_DATE_*`
為「本架構無此對映」而非缺件，不列 PENDING。

執行順序為 `11` → `12`，但兩包已同時在手，故執行層**不建立隨即被取消
之登記**。此處記其始末，使日後讀者不會以為 DR-6b 遺漏。

### **但另有一個 Atl-H 欄為空、且不在 R-TM62 射程內者**

```
DateTmFormat2   Atlantis High 欄（26-30）全空
                Powernet 欄 = 'Radio_A3.DateTmFormat2'
                Usage Comment = 'For PHEV'
                來源列 408
```

**R-TM62 之射程明文限於五個 `TLM_MANAGED_TIME_DATE_*`**，不含本項。
執行層**不逕行套用**（射程擴張屬條文範圍），於
`data/lid_atlantis_high.tsv` 記為 `(EMPTY)` 而非 `N/A (R-TM62)`。
**提請裁定其處置** —— 詳見 `docs/upstream/11_lid.md` §3.2。

## DR-11 —— Atl-Mid 專屬物件之 Atl-H 對應需求（2026-08-22，R-TM63）

**與 DR-5 之區別（逐字，下放包 `13` §2 末段）**：

```
DR-5 是「物件不在 CFTS015 內」，DR-11 是「物件在 CFTS015 內但標為
他架構」。**兩者之上游答覆方向不同**，不得合併登記。
```

DR-5 之答覆方向為「該物件遷移到哪裡／哪個版本有它」；
DR-11 之答覆方向為「Atl-H 架構下對應之需求是哪一個，或確認 Atl-H
不含此需求」。**前者找同一物件，後者找不同物件。**

佔位字串：`PENDING: DR-11 Atl-H 對應需求（CFTS015-{objid} 標為 Atlantis Mid）`

**涵蓋 35 個物件**（`data/ee_architecture_by_leaf.tsv` 中
`is_atl_hi = False` 且標籤為 `Atlantis Mid` 者），
其中 020（4 個）與 021（1 個）為該片之全部錨點。

## DR-12 —— UI 標籤之正式名稱（2026-08-22）

候選來源 `HMI Settings List R1 SR24 Post 2A` **已到並已查證**（`11` T4）。
三項中**二項有正式來源、一項不符**：

| v3 之標籤 | 結果 |
|---|---|
| `"Time and Date"`（設定頁名） | **不符** —— 正式為 `Clock`（Set Date 實作後改為 `Clock & Date`） |
| `"Sync Time with GPS"` | **逐字相符**，該表標來源為 CFTS015 |
| 12/24 小時項名 | **近似** —— 項名 `Time Format`，值為 `12 hrs` / `24 hrs` |

**故 B1 生成時，此三者不必寫 `PENDING: DR-12` 佔位**，改用該表之逐字值
（`13` §4 之佔位規則於此三項不適用 —— 其前提為「未見於 CFTS015 或
HMI Settings List」，而三者皆已見）。

**DR-12 未結案**：其餘 UI 標籤（若 B1 生成時出現）仍適用佔位規則。

## DR-20 —— 注入無效訊號之操作方式（2026-08-22，B1 生成時登記）

`10` 上繳 §1.2 之缺口 **G2**（注入無效／越界／缺失之訊號，影響 009 / 010 /
022 三片）。B1 之 010 三條 TC 需要此操作，故於生成時登記。

**登記緣由須記明**：B1 生成首版誤用 **DR-9** 承載此佔位，
而 DR-9 之定義為「CAN sleep 之可觀察終止條件」——**兩者意義不同**。
佔位之 DR 號若指向不相干之缺件，答覆回來時無法對應，
與 `DATA_REQUESTS` 既有之「同一缺件不得有兩個 DR」為一體兩面
（前者是一號多義，後者是一義多號）。已於生成物中更正為 DR-20。

**與 DR-9 之區別**：DR-9 問「CAN sleep 何時算完成」（觀察面），
DR-20 問「如何使訊號變成無效」（注入面）。

## DR-12b —— 設定頁名（2026-08-22，A-TM28）

| DR | 缺件 | 阻塞 | Urgency |
|---|---|---|---|
| **12b** | 設定頁名為 `Clock` 或 `Clock & Date` —— 須看實機或問 HMI 團隊 | 凡 `Open the "Clock" settings` 之 TC（實測 21 條） | **High** |

**與 DR-12 之區別**：DR-12 問「該設定項叫什麼」（已由新版文件答覆）；
DR-12b 問「該設定**頁**叫什麼」——文件本身給了兩個候選而未指明何者為
R1L-R 之現況。**前者文件能答，後者文件答不了。**

佔位字串：`PENDING: DR-12b 設定頁名（Clock 或 Clock & Date）待確認`

**值照留 `Clock` 不改**（A-TM28 未裁前，`Clock` 為文件字面值）。
本佔位之目的是使「已寫入之值可能需改」成為**可見狀態**，
而非宣告該值為缺件 —— 此與其餘 DR 之佔位語意不同，故其值欄有值而非空。

## DR-21 —— HMI Settings List R1L-R (Feb 13 2026)

| DR | 檔案 | Status | 服務 |
|---|---|---|---|
| **21** | `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | **RECEIVED（2026-08-22）** | 001/002/007/011/015/016 之 UI 標籤與值域 |

**來源有兩份同名檔案，內容不同**（`26PI1.5` 之副本另有一個尾隨空格，
SHA256 相異，大小差 1436 B）。**執行層取 `26PI2.5`**（PI 版本較新），
並實測**兩份之 §7 Clock 節逐列相同** —— 故本次全部結論不受選擇影響。
此事記於此，因日後若需引用該檔之他節，兩份之差異須先釐清。

複本 SHA256 與來源一致（`41daac0048d2afe15fe9aeee…`）。

## DR-6 之狀態更正（2026-08-22，`21` §2）

先前記為「已由 LID 表解除」。**該記載只對 Atlantis High 成立。**

`20` T2 對 `CAN Mapping` 兩組架構欄之實測（19 LID × 2 架構 = 38 列）：

```
無訊號         8 列  → 不寫任何斷言（該架構無此對映）
有訊號無網段  11 列  → **全部在 Atlantis Mid 側**；訊號可寫，
                        segment 寫 `PENDING: DR-6`
有訊號有網段  19 列  → 照用
```

**Atlantis Mid 側僅 6 個 LID 有網段**（`GPSDateTmSecond` 與五個
`TLM_MANAGED_*`，皆為 `CAN-B`），其餘 11 個之 CAN 欄為空。

**故 DR-6 對 Atlantis Mid 未解除。** 現行生成物中其佔位僅 1 處，
因多數 Atl-Mid 片未涉該等訊號 —— **但該數會隨 017 之拆分而增加**
（`21` T4）。

**併記一項來源訂正**：下放包 `18` §5 T4 稱「`$DateTmHour$` 在 Atl-Mid 為
`TIME_DATE.Hour1` **on CAN-B**」—— 訊號名正確，**`on CAN-B` 無來源**，
該 LID 之 Atl-Mid 側 CAN 欄實測為空。分析層已於 `21` §2 自陳
「是我從別的 LID 之網段推的」，並記為**第四次同型**
（推設備 → 推 UI 開關 → 推 UI 標籤 → 推網段），
且發生在已立 R-TM49（不得杜撰網段）之後。


---

## DR-6 降轉為追溯用（2026-08-25，W-TM-26 T4 / R-TM82）

**狀態：MISSING / 待答 → 僅供追溯，不再阻塞。本列不刪（R-TM13）。**

DR-6 所問者為「Atlantis Mid 側 11 個 LID 有訊號而 CAN 網段未載」。
該問之所以成立，前提是 canon §8.7.5 之 v1 記法要求寫出網段
（`$LID$ in <MESSAGE>.<Signal> on <SEGMENT>`）—— 網段是斷言的必填件，
缺件即成佔位。

canon 已於 2026-08-21 撤銷 v1/v2 改行 v3，v3 之形式為

```
$<MESSAGE>.<Signal>$ = <raw> (<label>)
```

**網段一律不寫**。依 R-TM82，本 feature 從現行 v3。**故網段不再是斷言之
必填件，缺件亦不再構成佔位** —— DR-6 之待答對象隨其提問前提一併消滅。

W-TM-26 T4 實測：改寫後工作簿之 `PENDING: DR-6` 佔位由 1 處（#035）
歸零，且全部 29 處 v1 三件組之網段字樣（`on FD` ×25、`on CAN-B` ×3、
本佔位 ×1）皆已移除。

**保留本列之理由**：Atl-Mid 側 CAN 欄為空一事仍為 LID 表之實測事實，
日後若有任何用途需要網段（例如 DBC 比對或他 feature 之 v1 遺留件），
該事實與其發現經過須仍可追。**降轉不等於解除** —— 未取得答覆，
只是本 feature 不再因它而阻塞。
