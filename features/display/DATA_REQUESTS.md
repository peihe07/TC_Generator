# DATA REQUESTS — Display (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/display/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

**R-G14（2026-08-24，全域）**：凡屬「某訊號／參數查無」之 DR，開立前須先
滿足 R-G13 三要件並登入 `forms/LOOKUP_MISSES.md`。台帳防重複發現、
本表綁上游提問、`ANOMALIES.md` 綁批次 —— 三處各有其職，不互相取代。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| DR-DM12 | `SWE1-DM-007` 之 `static vehicle condition` 與 `SWE1-DM-008` 之 `dynamic vehicle state transition`，**其區分軸為何**？三個候選：(i) 車輛靜止 vs 行進；(ii) 顯示器前態穩定 vs 過渡；(iii) 其他。**附本層現行切分之對照表**（007＝前態 `DCSD Screen ON`、釋放後還原回 ON，`{4819642}`／`{4819645}`；008＝前態非 ON 或過渡畫面、釋放後目的態不同，`{4819668}`／`{4819671}`／`{4820265}`），請確認或更正。實測依據：CFTS_020 全文 `static` **0 命中**、`dynamic` **1 命中**；SYS2 之 12 列 RVC **同時錨到兩個 leaf 且錨據完全相同** | **待 Pei 發**（收件方同 DR-DM8，037 作者） | `rvc-01` 六條之 `leaf_id` 欄 | 切分為分析層之分類（R-DM55）；**錯誤可逆 —— 只需改 `leaf_id` 一欄，TC 內容不受影響** | R-DM55 | HIGH |
| DR-DM11 | `SWE-DM-007` 之觸發訊號 —— 037 逐字為 `when reverse gear signal is detected under static vehicle condition`，而 **CFTS_020 之 RVC 諸條（24 條適用本專案者）一律以抽象之 `if the Rear View Camera is to be displayed` 為觸發，全文查無倒車檔訊號之定義**。請提供：(a) 該訊號之名稱與其 DBC 定義；(b) `static vehicle condition` 之判準（車速門檻？排檔？）；(c) 其與 `$TGW_DISP_STAT$ = [DISP_REAR_CAMERA]` 之關係（何者為因） | OPEN | SWE-DM-007（`rvc-01` 六條之觸發皆為「RVC 被請求」，非倒車檔） | 007 之倒車檔面向未被驗證；交付時不得以「007 有 TC」表述該面向已驗 | — | HIGH |
| DR-DM10 | Display Hot 之關閉階段：(a) `1.11.2.2` 之組 A（`{4820282}`–`{4820288}`，HU 判定後下令關背光、關後續送 `[DISP_HOT]`）與組 B（`{4820289}`–`{4820292}`，DCSD 自主關背光並送 `[DISP_OFF]`、無警示階段）**兩者皆宣告適用於 `Radio:R1H`／`Atlantis High`且互相排斥，請裁定何者為準**；(b) **【問法更新，下放包 24 §2.3】** `{4820283}` 之 `has finished displaying the Display Hot warning screen` 之終止準據 —— **原問「時長為何」，改問「DCSD 側之 warning → off 是否亦為溫度分段？若是，其第二門檻為何？」**。依據：CFTS013 SYSRA 顯示 **HU 側**之同型流程以**溫度分段**而非時長觸發（`>=51 且 <=55` 每度降 5%／`>=56 且 <60` 顯示警示不再降亮度／`>=60` 螢幕關閉／`>50` 降回 `<=50` 恢復正常）。**該五列為 Associated Display（HU 側）之事實，非 DCSD 側之事實，依 R-DM51(a) 不得代入**；引之僅為指出「分段變數可能是溫度而非時間」。**【指標，26 §四.3／26a §三】A6 已於 26a 解除，CFTS013 已落 `inputs/`。惟該五列（`>=51`／`>=56`／`>=60`／`>50`→`<=50` 之分段）之獨立重算**尚未執行** —— 24-6 於 `EE Architecture` 一項不符而依停止條件 67 停手，24-4／24-5 連同本項之重算一併待裁。本問法之成立不依賴該五列之數字（其改變的是問題之變數：溫度而非時間），但其**引為依據之五列仍未經本層驗證**。A6 關閉之複核於此一併記明**；(c) `{CFTS013-XXX}`（本文出現 5 次之未填佔位符）之實際條號與內容 | SENT (2026-08-25) | **SWE-DM-004 之 popup 側（`PU0517`，22 包 §二）**；SWE-DM-005（保護性關閉，原 pilot-01 #2）；`PU0130` | #2 已 deferred；四條查證路徑（組 A／組 B／組 C／Pop Up List）皆不產生可觀測之區分準據，warning 與 OFF 兩階段在測試步驟上無法區分（False Fail 風險）。**22 包增列**：#1 之 popup 側亦受同一矛盾波及 —— 組 B `{4820289}` 於越過門檻時即關背光，使 `PU0517` 之顯示不可觀測，該 ER 在組 B 之實作上恆為 False Fail | A-DM33 | HIGH |

> **補充二（下放包 31 §四，待 Pei 發）—— 補充一不撤回，兩者並列。**
> 上列原文與補充一皆依 R-TM13 不刪不改。
>
> **Supplement 2 to DR-DM10 — the two documents appear to divide the work**
>
> Further to our previous supplement, we have now traced the three clauses
> that CFTS_013 `{4943104}` defers the shutdown behaviour to
> (`{4821589}`, `{4821590}`, `{4821591}`), together with `{4821587}` and
> `{4821592}`.
>
> **All five are declared `[Radio:VP4R84] [EE Architecture:CUSW]`**, in
> section `1.15.5.5.2`. They do not apply to R1H / Atlantis High.
>
> However, the same five sentences recur verbatim across **five parallel
> "Multi-stage' DCSD Display Hot Algorithm" sections** (`1.8.2.5.2`,
> `1.15.1.5.2`, `1.15.2.5.2`, `1.15.4.5.2`, `1.15.5.5.2`). Examining the
> variants that **do** carry `R1H` and `Atlantis High`:
>
> | Role in the sequence | Clause | Applies to R1H / Atlantis High |
> |---|---|---|
> | DCSD decides to turn off its backlight, sends `[DISP_OFF]` | `{4819862}` / `{4820951}` | **No — `Radio:noSys`** |
> | HU sees `[DISP_HOT]` → `[DISP_OFF]`, sends `$TGW_DISP_STAT$ = [DISP_OFF]` and `$RQ_DISP_INTS$ = [0% Intensity]` | **`{4819863}` / `{4820952}`** | **Yes** |
> | DCSD sees the HU's `[DISP_OFF]`, stops displaying and turns off backlight | `{4819864}` / `{4820953}` | **No — `Radio:noSys`** |
>
> That is: **within CFTS_020, the multi-stage algorithm's HU side is defined
> for this programme and its DCSD side is marked `noSys`.** Meanwhile
> CFTS_013 §1.5.3 — thirteen clauses, all `[EE Architecture:All]` and all
> naming `R1H` — defines exactly that DCSD side: the once-per-minute
> monitoring, the 50 / 51–55 / 56–below-60 staging, the 10 second timer, and
> `Note: Only DCSD shall implement 10 sec timer.`
>
> **Revised question (a):** are CFTS_020 and CFTS_013 intended to **compose**
> for R1H / Atlantis High — CFTS_020 defining the HU side and CFTS_013 §1.5.3
> the DCSD side — with `{4820289}`–`{4820292}` (the single 85 °C threshold)
> being an alternative rather than the governing behaviour? Or does
> `{4820289}` govern and CFTS_013 §1.5.3 not apply despite its `All`?
>
> **New question (e):** `{4820283}` states that the HU sends
> `$TGW_DISP_STAT$ = [DISP_OFF]` when it `has finished displaying the Display
> Hot warning screen and determines that the DCSD display should now be
> 'Turned Off'`. `{4821590}` states the **same consequent, word for word**,
> with the antecedent `When the HU sees the transition from
> $DCSD_DISP_STAT$ = [DISP_HOT] to $DCSD_DISP_STAT$ = [DISP_OFF]`.
> Is the latter the criterion the former leaves unstated?
>
> **本層之補測（上繳 31 §二 T4）**：以 R-G37 新判準重跑三項既有量測 ——
> RVC × `$DCSD_DISP_STAT$` 24→**24**、組 A 7→**7**／組 B 4→**4**、
> `turn off … backlight` 2→**2**，**皆不變**；`pilot-01`／`rvc-01` 所引之
> 11 個條號其適用性判定**無一改變**（停止條件 84 未觸發）。
> **另新發現一條**：`{4819273}`（§1.4.1.2.6 `Disassociated Center Stack
> Display (DCSD) - Display Hot`，`[Radio:R1M, R1H, R1L, R1L-R] [EE:All]`，
> **適用本專案**）逐字為 `Execute 'Display is Hot' portion of DCSD Display
> Hot Algorithm - See CFTS013-629.` —— **該條被舊判準排除十輪，
> 且其轉指正是 DR-DM4 之標的。**
| DR-DM9 | SYS2／CFTS 之值標籤 `[DISP_OFF]`／`[DISP_ON]`／`[DISP_NORMAL]`／`[DISP_REAR_CAMERA]` 各對應 `DCSD_DISP_STAT` 之哪一個 raw 值，並提供其並列出處 | SENT (2026-08-25) | SWE-DM-005（#2／#3 之訊號值）、007／008 | ER 目前只驗行為不寫訊號值（R-DM48）；取得後依 R-DM22 建值標籤 glossary，得於既有 ER **增列**訊號值（增列不改變行為驗證，非回修） | A-DM32 | HIGH |

> **重擬（下放包 27 §1.4，2026-08-25）—— 上列原文依 R-TM13 不刪不改。**
> 原問「四個標籤各對應 `DCSD_DISP_STAT` 之哪一個 raw 值」之前提為誤：
> 其中 `[DISP_NORMAL]`／`[DISP_REAR_CAMERA]` **從未用於 `$DCSD_DISP_STAT$`**，
> 兩者是 `$TGW_DISP_STAT$`（HU 側）之值（A-DM35，已採認結案）。**改為三問**：
>
> **(a)** `[DISP_ON]`／`[DISP_OFF]` 與 `[ON]`／`[OFF]` 是否為同一狀態之
> 兩種書寫（規格內部之別名），或為不同狀態？
> **(b)** `$TGW_DISP_STAT$`（HU 側）之值標籤（`[DISP_NORMAL]`／
> `[DISP_REAR_CAMERA]`／`[DISP_OFF]`…）對其 DBC `VAL_` 之對應為何？
> （`TGW_DISP_STATSts` 之 `VAL_` 為 `2 "Normal_mode"`／`7 "Rear_Camera_Display"`…
> —— **與規格側之標籤逐字不等**）
> **(c)** 規格自帶之雙記法（`DISP_NORMAL / Normal_mode`、
> `DISP_REAR_CAMERA / Rear_Camera_Display` 等）是否為權威對照？
>
> **附件（機器輸出，`cfts_doc` 綁定 MATCH；配對式**
> **`\$([A-Za-z0-9_]+)\$\s*=\s*\[([^\]]+)\]`）**：
>
> | 標籤 | 於 `$DCSD_DISP_STAT$` | 於 `$TGW_DISP_STAT$` | DBC `DCSD_DISP_STAT` | 判定 |
> |---|---:|---:|---|---|
> | `[OFF]` | **85** | 0 | `0 "OFF"` | 解得 raw 0 |
> | `[ON]` | **53** | 0 | `1 "ON"` | 解得 raw 1 |
> | `[BLANK]` | **20** | 0 | `2 "BLANK"` | 解得 raw 2 |
> | `[RR_CMRA]` | **72** | 0 | `3 "RR_CMRA"` | 解得 raw 3 |
> | `[DISP_HOT]` | **46** | 0 | `4 "DISP_HOT"` | 解得 raw 4 |
> | `[SNA]` | **8** | 0 | `7 "SNA"` | 解得 raw 7 |
> | `[DISP_ON]` | 23 | 0 | 查無 | **逐字查無** |
> | `[DISP_OFF]` | 12 | **146** | 查無 | **逐字查無** |
> | `[DISP_REAR_CAMERA]` | **0** | **107** | — | **非本訊號之值** |
> | `[DISP_NORMAL]` | **0** | **99** | — | **非本訊號之值** |
>
> 阻斷範圍隨之修正：**用短拼法之條款不受阻**（007／008 之 RVC 諸條
> 逐字為 `$DCSD_DISP_STAT$ = [RR_CMRA]`）；**用長拼法者仍受阻**
> （`{4820287}` 逐字為 `= [DISP_ON]`，即本批 #3 只驗行為之理由）。
| DR-DM1 | CFTS_009（條號 `{CFTS009-722}`，定義 `Start Up Sequence - Splash/Disclaimer Screen` 之時段）— 檔名待查（pattern：`…CFTS_009…docx`） | SENT (2026-08-25) | SWE-DM-003 | splash/sleep 時長之預期結果無法寫 | — | HIGH |
| DR-DM2 | Popup 優先序仲裁規則與 timeout 之來源（CFTS 本文僅有 RVC「high priority」語句，無仲裁順序表或 timeout 值） | SENT (2026-08-25) | SWE-DM-006 | popup 仲裁之預期結果無法寫 | — | HIGH |

> **補充函（下放包 29 §3.3，待 Pei 發）—— 上列原文依 R-TM13 不刪不改。**
>
> **(a) `Cat. SL` 之優先位置**：矩陣 page 4 之明序清單置其於 `Cat. X` **之下**；
> page 9 逐字稱其 `This category is maximum priority`；page 10 稱
> `Cat. SL is stacked under RVC`。**三處說法不同，請裁定其正確位置。**
> （`data/popup_priority.tsv` 之 26 列 SL 現標 `PENDING: DR-DM2 Cat SL precedence`。）
>
> **(b) 2021 之 SR24 1A 矩陣對 26PI 是否仍為權威？** 佐證：其六個類別 token
> （`1T`／`1P`／`SL`／`RVC`／`VR`／`X`）與 26PI Pop Up List 欄 5 之值域**完全相符**，
> 即**詞彙未漂移**；惟**語意是否漂移無法以逐字比對證明**。
>
> **本 DR 之狀態自此由「索件」降為「確認」**（29 包 §三.1）：
> `popup_priority.tsv` 已建（1341 列，1272 已解析／69 `UNRESOLVED`），
> 帶三項強制揭露（B17／B18／B19）。
| DR-DM3 | `SYS-RA-DISP-*` ↔ SYS2 之對應表，或含 `DISP` id 之 SYS2 版本 | SENT (2026-08-25)（**沿革保留**：2026-08-25 曾兩度被指定而皆不答：① CFTS043 SYSRA —— 實測為 HVAC（`SYS-RA-HVAC-*` × 405，`SYS-RA-DISP` 0 次），見 A-DM31；② SYS3 SYSAD —— 本 feature 之素材且有其他用途，不登為異常，其不答本 DR 一事記於此）| 追溯鏈斷；spec_reference 無 id 路徑 | A-DM2 / A-DM10 | MEDIUM |
| DR-DM4 | CFTS_013（條號 `CFTS013-629` Standard/`-633` Standard/`-952` Multi-stage，載 DCSD Display Hot 演算法本體與其分級溫度門檻）— 檔名待查（pattern：`…CFTS_013…docx`） | SENT (2026-08-25) — 或由 28 包任務 A 之抽取先行結案，以先到者為準。**28 輪任務 A2 之實測：該檔之條號全為 7 位，`629`／`633`／`952` 以條號錨定皆查無**（A-DM39）—— 兩條路徑皆未結，**結案之裁定屬分析層**，執行層不逕結 | SWE-DM-005（004 部分） | multi-stage 之分級判準無法寫；單級 85 °C 行為可寫 | A-DM13 | HIGH |

> **重擬（下放包 29 §3.4，待 Pei 發）—— 上列原文依 R-TM13 不刪不改。**
>
> 標的由 3 位條號改為：CFTS_013（`26PI2.5 Jun Release`，2026-06-08）之
> **§1.5.1 `Activating the DCSD Display Hot Algorithm {4943080}`** 與
> **§1.5.3 `Multi-stage HU and DCSD Display Hot' … {4943095}`** 之內容，
> 是否即 CFTS_020 所引之 `{CFTS013-629}`／`{-633}`／`{-952}`？
>
> 附實測：CFTS_013 docx 之條號 **117 個相異、全為 7 位**（`4819633`…`5423093`），
> **其中含 `4820282`（CFTS_020 之條號）**，即兩份共用同一 Polarion 編號空間；
> 而 CFTS013 SYSRA 之 `Document ID` 欄為 3 位形態（`CFTS013-602` 等）。
> **請提供 3 位 ↔ 7 位之對應，或確認 3 位號已作廢。**
>
> **29 輪 A3 之實測（停止條件 76 觸發，見上繳 29 §二）**：§1.5.3 之 13 條
> **全部適用本專案**（`Radio` 含 `R1H`、`EE Architecture:All`），其門檻為
> **50／51–55／56–<60 degrees C**，與 CFTS_020 `{4820289}` 之 **85 degrees C** 不符。
> **本層未併算、未判何者為準**（屬 DR-DM10(a)）。
| DR-DM8 | 確認 037 之 `DISPLAY_ON`／`DISPLAY_OFF`（`SWE-DM-001`／`002`）與 SYS2／DBC 之 `DISP_ON`／`DISP_OFF` 是否為同一狀態 | SENT (2026-08-25) | SWE-DM-001、SWE-DM-002 | 狀態名無法對應，TC 之預期結果無法引用 DBC 之 `VAL_` 標籤 | A-DM18 | HIGH |
| DR-DM7 | 本專案（R1LR Atl-H）之 VF 代碼，或其 PROXI 實例檔（已填值之 PROXI，非 `_R3` 空白格式檔） | **CLOSED（R-DM44，16 輪）**（下放包 30 §四.4 之更正）—— 其所求之用途已由 R-DM33 消滅（PROXI 改需求驅動），**非取得所求之物**。28a §2.1(c) 之對帳判定為**全案結案而非部分結案**（R-DM44 引的就是本列原文，所求之物與所求之用途兩項逐字相同）。**Pei 2026-08-25 曾於封 4 發出本 DR** —— 該發信事實記此，惟本 DR 自 16 輪起即已結案。**重開條件（R-DM44）**：某參數之值域在 PROXI 中依 VF 而異時，以新編號重開 | 全 8 leaf 之前置條件 | `Used by NODE(VFXXX)` 無法用於篩選；PROXI 446 列母體無法收斂 | A-DM20 | MEDIUM |
| DR-DM6 | `Display_OFF_SoftKey_Prsnt` 之 PROXI 定義；或確認其與 `PROXI_HDCC27_R3` `Format` r692 之 `Display_OFF_SoftKey` 為同一參數（LID r63 `DSP_SK_PRSNT`） | SENT (2026-08-25) | SWE-DM-001（Screen Off 行為之配備前提） | 該 leaf 之前置條件是否需帶軟鍵存在旗標，無法判定 | A-DM17／`forms/LOOKUP_MISSES.md` M-3 | MEDIUM |
| DR-DM5 | `RADIO_B4.CCDMF_RQ_DISP_INTS` 之 DBC 定義（訊息 `RADIO_B4` 存在於 `PDT27_E2A_R1_BHCAN2.dbc`，該 `SG_` 不存在）；一併確認 `GW_B_5.Mute_Button` | SENT (2026-08-25) | 用到 `$CCDMF_RQ_DISP_INTS$` 之 SYS2 FR 列 | 該訊號之值域與位元定義無法寫 | A-DM10a／`forms/LOOKUP_MISSES.md` M-1、M-2 | MEDIUM |

## R-DM8 之查證結果（先查 CFTS 與 SYS3，查得者記章節）

R-DM8 列四處缺值。實測（`scripts/probe_missing_values.py`）：

| SWE-DM | 缺值 | CFTS_020 | SYS3 SYSAD | 處置 |
|---|---|---|---|---|
| 003 | Splash / sleep 之時長門檻 | 命中 9 段「splash」，惟時段定義一律轉指外部條號 `{CFTS009-722}`；`sleep` + 數值+單位 0 段 | 命中 10 段，含數值+單位 0 段 | **DR-DM1** |
| 004 | thermal warning threshold 之門檻值與單位 | **查得**：`1.11.2.2 DCSD Display Hot Behavior {4820281}`，另 `1.15.1.5 {4820659}` / `1.15.2.5 {4820937}` / `1.15.4.x` 為各架構之對應節 | 含數值+單位 0 段 | 記章節，不開 DR |
| 005 | thermal protection 之 critical 判準與回復條件 | **部分查得**：回復條件在 `{4820290}`／`{4820287}`／`{4820288}`；**分級（multi-stage）之 critical 判準轉指 `{CFTS013-952}`，不在手上** | 含數值+單位 0 段 | 回復條件記章節；分級判準 → **DR-DM4** |
| 006 | popup priority arbitration 之優先序規則與 timeout | 命中 70 段，惟皆為「high priority Rear View Camera screen」之個別語句；無仲裁順序表、無 timeout 值 | 命中 6 段，含數值+單位 0 段 | **DR-DM2** |

> **R-DM27（2026-08-25）：缺值範圍由四處改為八條全稱。** 上繳 06 §8 之
> 全文精讀實測 —— 八條之「數值＋單位」0/8、`$Signal$` 0/8、外部引用 0/8。
> 上表之四處為抽樣所得之低估。逐條之未給值抽象量詞見
> `data/leaf_value_gaps.tsv`（例 `SWE-DM-001` 之 `timeout`、
> `SWE-DM-002` 之 `previous`／`valid`，二者原不在四處之列）。
> R-DM8 之禁止回填規定不變，適用範圍擴及八條全部。

> 004/005 之章節為**位置登記**，非值之確認。門檻值之讀出與採用屬 Phase 2，
> 依 R-DM8 不得由本輪回填（canon §8.4.1）。

## R-DM8 之再判定（2026-08-24，下放包 03 §4.1 / 步驟 9）

上繳包 02 §14b 之查證只回 CFTS 與 SYS3，**未查 SYS2** —— 而 SYS2
r31–r34 正是該行為之狀態機定義。本輪已補查並將兩側併讀
（`scripts/hot_behaviour_join.py`，全文見上繳包 03 §6）：

| SWE-DM | 缺值 | 再判定 | 證據位置 |
|---|---|---|---|
| 004 | thermal warning threshold 之門檻值與單位 | **不缺**（就單級門檻而言） | CFTS `{4820289}`／`{4820290}`（同段落載 `> 85 degrees C` 與 `<= 85 deg C`；該兩段之 `[Radio:R1H] [EE Architecture:Atlantis High]` 與本專案 R1LR Atl-H 相符）。SYS2 r30–r34 **不含**任何溫度數值 |
| 005 | critical 判準 | **仍缺** | CFTS `1.15.1.5 {4820660}`／`1.15.4.5 {4821298}` 明載 multi-stage 版本「有較低之溫度門檻」並轉指 `{CFTS013-952}`；`{4820282}` 亦轉指 `{CFTS013-629}` → **DR-DM4** |
| 005 | 回復條件 | **不缺** | CFTS `{4820287}`（DCSD 送 `DISP_ON`）／`{4820288}`（HU 恢復正常顯示）／`{4820290}`（背光與觸控恢復、DTC de-mature）；SYS2 r34 為 `{4820288}` 之逐字同語句 |

**溫度門檻在全文之出現位置：CFTS 僅 2 段，皆在 `1.11.2.2 {4820281}` 之下
（`{4820289}`、`{4820290}`）。SYS2 r30–r34 為 0 段。**

訊號／值 token 之兩側逐字對照（非相似度）：`$DCSD_DISP_STAT$`、
`$TGW_DISP_STAT$`、`$RQ_DISP_INTS$` 三者兩側皆有、無單側；值
`[DISP_HOT]`／`[DISP_OFF]`／`[DISP_ON]`／`[0% Intensity]` 亦兩側皆有。
即 **SYS2 之 hot 四列為 CFTS `1.11.2.2` 之 HU 側子集**，非另一組需求。

> 本節仍未回填任何值。上表之 `> 85 degrees C` 係為指出「該值存在於何處」
> 而引其位置，Phase 2 方得讀出採用（R-DM8、canon §8.4.1）。
