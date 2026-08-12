# ANOMALIES — FW036 Projection

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-PJnn]`. PENDING entries block their batch until a Pei
ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

A-PJ01 … A-PJ08 arrived with the Phase 0 下放包 §8. A-PJ09 … A-PJ16 were
found by Phase 0 recon. A-PJ17 … A-PJ21 were found during Phase 2 —
A-PJ17/A-PJ18 by lint verification, A-PJ19 by the L-PJ6 word-boundary fix,
and A-PJ20/A-PJ21 by the PCTS on-device capture (§6). Findings that
contradict a stated premise of a 下放包 are registered, never reconciled
(§0.5).

Phase 2 (2026-08-12) closed 11 and retracted 1; **9 remain PENDING**.

---

## From the 下放包 §8

### A-PJ01 — 兩份 037 內容互異 · PENDING

兩份 037 需求集 ID 完全相同（171/171 交集），但內容互異：Verification
Criteria 171/171 全數不同、description 相異。

**Evidence** — recon 逐條比對（CPAA `Basic Report` F/T 欄 vs MD
`Analysis Report` E/AI 欄，MD 表頭第 8 列）：ID 交集 **171/171**，任一側皆無
對方所缺的 id；Verification Criteria 相異 **171/171** ✅；description 相異
**105/171**（下放包稱 127/171，見 RECON §14 #10 — 計數口徑差異，不改變
結論）。CPAA 有 4 條 Verification Criteria 為空，MD 為 0 條。

**Disposition** — 已依 R-P2 取 CPAA 為主線；差異入 RD-1。MD 版保留為副線，
供 QA 分頁與品質屬性欄使用。

---

### A-PJ02 — `SWE1 HMI Source ID` 全空 · **CLOSED** (2026-08-12)

CPAA_0521 的 `SWE1 HMI Source ID` 欄 **0/171 全空**，canon Tier 0「由 037
HMI Source ID 推導缺件清單」的機制在本 feature 失效。

**Evidence** — 欄位掃描確認 D 欄 0/171 filled。

**Disposition** — 改用 `Source Requirement ID`（C 欄）回推。實測家族分布為
`SYS-RA-PROJ` 145 / `SYS-RA-HUIG4.5` 16 / `SYS-RA-CP_R10` 9 /
`CP-R10-3.2.7.2` 1 —— **與下放包所述的家族標籤不符，見 A-PJ09**。

備援機制另有一條下放包未提到、實測更有力的路徑：workbook 自身
`Specification Reference` 欄逐列具名引用文件與章節（CFTS085 473 列、
Projection Device HMI 126 列、CarPlay Addendum R10 82 列、HUIG 79 列、
Device Manager HMI 75 列、Pop Up List 34 列、CFTS025 24 列、CFTS019 16 列）。
缺件清單由此可直接導出，且正是 A-PJ14 / A-PJ15 / A-PJ16 的來源。

**Phase 2 處置（2026-08-12）— CLOSED**。`Specification Reference` 欄（558/559
具名引用）正式取代失效的 HMI Source ID，作為缺件推導的基礎。機制已有替代
物，本條不再是缺陷。

---

### A-PJ03 — 037 使用 SWE1 分析層邏輯名 · PENDING

037 與 workbook 使用 SWE1 分析層的邏輯名（`$token$` 形式），需經 mapping 表
轉為匯流排實名方可執行。

**Evidence** — 10 個 distinct token 對兩份 DBC 直查全滅；經 mapping 表
（Atlantis High 欄）後 **9/10 解析**（下放包稱 8/10，見 A-PJ13）。

**Disposition** — 對照表已建於 `data/signal_map.json`，每列均經 DBC / PROXI
實查。餘一條 `$HCP_DISP2.Est_Range_BEV$` 無對映 → R-P9 / DATA_REQUESTS #2。

---

### A-PJ04 — `VC_VEH_Line = 332` · **CLOSED by R-P8′** (2026-08-12)

`$VC_VEH_Line$ = 332` 與 `Vehicle_Line_Configuration` 的關係。

**下放包所述** — 332 不在 `Vehicle_Line_Configuration` 列舉值內；332 疑為
車型代號（mapping 表另有 `332BEV Specific Signals` 分頁）。

**Evidence（實測，與所述不同）** — 332 **在**列舉值內，但身分是**標籤**而非
值：PROXI `Car_Configuration_15.Vehicle_Line_Configuration` 逐字列出
`… 104 = WS (68 Hex) 105 = 332 (69 Hex) 106 = 560 (6A Hex) …`。所以 workbook
寫的 `= 332` 是在指稱車型線 332，而配置字實際應取 **105**。這是標籤與代碼
混用，不是超出列舉範圍。詳見 A-PJ10。

**Phase 2 處置（2026-08-12）— CLOSED by R-P8′**。Pei 未採 Phase 0 的
「保留原文」提案，改為逕行更正。R-P8′ 逐字：

> `$VC_VEH_Line$ = 332` 解除保留，更正為 `Car_Configuration_15.Vehicle_Line_Configuration = 105 (332)`。依據為 PROXI `Format` 分頁 row 466 col9 之列舉 `105 = 332 (69 Hex)`。DR#3 關閉。

PROXI Format **row 466** 經實測確認即為 `Vehicle_Line_Configuration` 所在
列，裁決所引之列號與列舉文字完全吻合。DR#3 關閉。

---

### A-PJ05 — 037 引用未提供的外部需求文件 · **RETRACTED by R-P13** (2026-08-12)

**下放包所述** — 037 引用 `AA-V4.5*` 16 條、`CP-R46*` 4 條，來源文件未提供；
未覆蓋 leaf 中的 184 / 190 / 195 正落此區間。

**Evidence（實測，與所述不符）** — 字串 `AA-V4.5` 與 `CP-R46` 在 037 全檔
（Source Requirement ID 欄、D–U 全部欄位）出現 **0 次**，在 workbook 559 列
36 欄中亦出現 **0 次**。184 / 190 / 195 三條的 source id 分別為
`SYS-RA-PROJ-184` / `-190` / `-195`，全在主幹家族，**不在**所述區間。

**Phase 2 處置（2026-08-12）— RETRACTED by R-P13**。原文與撤銷理由一併
保留供審計軌跡。R-P13 逐字：

> 037 的來源家族更正為 `SYS-RA-PROJ` 145 / `SYS-RA-HUIG4.5` 16 / `SYS-RA-CP_R10` 9 / `CP-R10` 1。原判之 `AA-V4.5` 與 `CP-R46` 於 CPAA_0521 全檔 0 次，係分析端誤判。A-PJ05 撤銷，DR#4、DR#5 關閉——對應之 SYS2 報告（`SYS2_HUIG_4_5`、`SYS2_CP.R10`）已在 `inputs/`，缺件不存在。

**撤銷理由**：本條所述之缺件不存在 —— 就其**命名**而言。所指的兩個家族實為
HUIG 4.5 與 CP R10。

**2026-08-12 R-P21 部分撤銷 R-P13**：當時「其對應文件已在 `inputs/`」這句
只對了一半。在 `inputs/` 的是 SYS.2 **安全分析報告**，不是 SYS.1 **規格本文**；
workbook 的 79 列引的是後者。**DR#4 因此重開並已補件**（A-PJ24 / R-P22）。
DR#5（CP R10）維持關閉。本條之 RETRACTED 狀態不變 —— 撤銷的是 `AA-V4.5` /
`CP-R46` 這兩個名稱，那部分仍然成立。

---

### A-PJ06 — Test Group 欄有 10 個值 · PENDING

Test Group 欄有 10 個不同值，與 canon §4.1.1「Test Group = 單一模組名」不符。

**Evidence** — Device Manager 192 / Carplay Wired and Wireless 60 /
Android Auto Wired and Wireless 58 / Touch 57 / Bluetooth 53 / WiFi 51 /
Audio Management 31 / GPS 30 / Media Player 23 / SSE / ECNR 4（合計 559，
與預驗值逐項相符）。

**Disposition** — Phase 0 只登記，歸 Phase 3 framework 議題。本 pipeline 在
FULL_REFINE 下不寫這一欄，所以不阻塞任何批次。

**Phase 3 結論（2026-08-12）—— CLOSED by R-P33。** 獨立分析輪完成，
結論是 **A-PJ06 不是「值太多要合併」，而是一欄承載了三個維度**：功能域、
投屏協定、傳輸，外加一個硬體特性標籤（`SSE / ECNR` 4 列）。180 格僅 46 格
非零即其結果。

**且此欄不可能靠改欄解決** —— `Test Group` 與 `Test Set` 皆在 profile §1 的
凍結區內，387/559 列（69%）已有執行紀錄，改欄即斷追溯。處置為
`docs/fw036/framework.md` **Part V** 記錄真實三層並附 §N.6 對映表回指凍結欄。

**Layer 2 定案（R-P33，2026-08-12）：16 乾淨 + 1 橫切（`Performance`）+
1 綑綁（`HMI Display`）。** 兩個暫定 Set 分別由 R-P26（`HMI Display` 確定
綑綁）與 R-P33（`Projection Audio` 收為乾淨）結案。

結案歷程本身值得留存 —— `Projection Audio` 的判定翻過三次：Phase 3 初判
「暫定乾淨」（RD 側 68%）→ R-P27「存疑」（HUIG 證據反向）→ R-P33「乾淨」
（CFTS019 補入後涵蓋率 32% → 97%）。**三次都不是改判準，是補證據**。
真正讓它結案的是 CFTS019 那 16 列落在單一章節 `1.3.3.1 Source Priorities`，
而該來源被 SYSAD 的假集中遮蔽了三輪（A-PJ29）。

相關裁決：R-P23 / R-P24 / R-P25 / R-P26 / R-P27 / R-P29 ~ R-P33。

---

### A-PJ07 — 跨 feature 範式來源欄位錯置 · PENDING

跨 feature 範式來源 SWC 簿欄位錯置：執行步驟寫在 Expected Result 欄、
Procedure 欄填 `NA`。

**Disposition** — 僅記錄；跨 feature 不處置。取其 CAN 步驟**寫法**，不取其
**欄位配置**。已在 `feature.yaml → paths.cross_feature_scope` 標記
`style only`。注意其寫法本身亦有一處需修正，見 A-PJ12。

---

### A-PJ08 — 欄位系統性留白 · **CLOSED by R-P19** (2026-08-12)

`Estimated Test Time` 欄 0/559 全空；`Test Case Author` 41 列空白；
1 列完全空白。

**Evidence** — 填充率掃描：`estimated_test_time` **0/559** ✅、
`author` **518/559**（41 空）✅、完全空白列 **1**（第 562 列）✅，三項與預驗值
相符。第 562 列的實情：序號 559、`SWE1-PROJ-227`、Test Group
`Carplay Wired and Wireless`、Test Item 與 `tc_ref_id` 皆有值，但九個 TC 內容
欄（Test Set / Pre-Conditions / Procedure / Expected Result / Specification
Reference / Priority / Design Method / Functional Safety）全空 —— 是一列有
追溯而無測試案例的殘樁。另有 3 列缺 `tc_id`（48、53、562）、1 列缺
`tc_ref_id`（152）。

**Phase 2 處置（2026-08-12）— CLOSED by R-P19**。三項分別處置，逐字：

> `Estimated Test Time` 全 559 列空白為既有慣例，**維持空白**，不補。
> `Test Case Author` 空白 41 列補為 `PeiPYHsu`。
> 第 562 列殘樁刪除。

**對不變式的影響**：第 562 列刪除使 profile §1 的「列數與列序不變」出現一個
受裁決授權的例外 —— 資料列由 559 降為 558，末列由 562 變為 561。`Test Case
Author` 補 41 列則使可寫欄位由 2 欄（Pre-Conditions / Test procedure）增為
3 欄。兩者皆已寫入 profile §1 與 §6。實際執行屬 Phase 4 以後，本包不動任何
一列。

---

## Phase 0 recon 新增

### A-PJ09 — 037 來源家族標籤與下放包不符 · **CLOSED by R-P13** (2026-08-12)

下放包 §4 / §9 以 `AA-V4.5`（16 條）與 `CP-R46`（4 條）指稱 037 的兩個來源
家族。這兩個字串在來源檔中都不存在。

**Evidence** — 037 全 171 leaf 的 `Source Requirement ID` 實際家族分布：

| family | count | leaf id 範圍 |
|---|---|---|
| `SYS-RA-PROJ` | 145 | SWE1-PROJ-071-001 … SWE1-PROJ-198 |
| `SYS-RA-HUIG4.5` | 16 | SWE1-PROJ-208 … SWE1-PROJ-225 |
| `SYS-RA-CP_R10` | 9 | SWE1-PROJ-201 … SWE1-PROJ-227 |
| `CP-R10-3.2.7.2` | 1 | SWE1-PROJ-203（格式與其餘 170 條不同） |

`SYS-RA-PROJ 145` 與預驗值相符。16 條的計數與下放包的 `AA-V4.5 16` 完全
一致，指向同一批 leaf，只是名字不同 —— 實際是 HUIG 4.5（HU Integration
Guide），不是 Android Auto V4.5。所述的 `CP-R10 6 / CP-R46 4` 合計 10，實際
是 `SYS-RA-CP_R10` 9 + 異格式 1。

**牽連** —— `SYS2_HUIG_4_5_…_V01.xlsx` 與 `SYS2_CP.R10_…_V01.xlsx` 兩份
安全分析報告**已在 `inputs/`**，且 workbook 的 spec_reference 有 79 列引
`HUIG_4_5`。若真正的來源是 HUIG 4.5 與 CP R10，則 DATA_REQUESTS #4 / #5 所
求的「未提供文件」可能根本不是缺件，而是已在手上的另一份東西。

**Phase 2 處置（2026-08-12）— CLOSED by R-P13**。提案獲採納並更進一步：
不僅撤銷 A-PJ05，DR#4 / DR#5 亦直接關閉 —— 裁定所需之 SYS2 報告已在
`inputs/`，缺件不存在。家族計數以本條實測為準（`CP-R10` 於裁決文字中簡記為
1 條，即實測的 `CP-R10-3.2.7.2`）。

---

### A-PJ10 — `Vehicle_Line_Configuration` 的 332 是標籤不是值 · **CLOSED by R-P8′** (2026-08-12)

**Evidence** — PROXI `Format` 分頁，參數 `Vehicle_Line_Configuration`
（group `Car_Configuration_15`，coding `Table`）的值表逐字：

```
0 = Invalid   51 = 343   52 = 327FL   53 = 226   80 = PF   81 = KL/K4
82 = UF  83 = UT  84 = 334  85 = 520  86 = 551 /M1  87 = 338  88 = 521
89 = 636 VM  90 = 356  91 = 952  92 = 341  93 = 552/MP  94 = 949  95 = 523
96 = 358  97 = 359  98 = 553/M4  99 = 556/M6  100 = K8  101 = WL  102 = 281
103 = 363  104 = WS  105 = 332  106 = 560  124 = DT  130 = HDCC
```

332 出現在 `105 = 332 (69 Hex)`。workbook 內含 `332` 的列為第 151–166 列
（16 列連續）。

**Phase 2 處置（2026-08-12）— CLOSED by R-P8′**。提案的保守選項未獲採納；
Pei 逕採本條末段所列的正確寫法，`$VC_VEH_Line$ = 332` 更正為
`Car_Configuration_15.Vehicle_Line_Configuration = 105 (332)`。已寫入
`data/signal_map.json` 的 `write_as` 欄。DR#3 關閉。

---

### A-PJ11 — leaf 133 在兩份 037 之間狀態不一致 · **CLOSED by R-P14** (2026-08-12)

MD 版 037 的修訂履歷 V1.1（2026-01-21）記載
`Change SYS-RA-PROJ-133 to unavailable`，但 `SWE1-PROJ-133` 在 R-P2 所裁的
主線 CPAA_0521 中**仍是 171 條 live leaf 之一**，未同步下架。

**Evidence** — `proj_133_in_cpaa: true`、`proj_133_in_md: true`；MD
`ChangeHistory 修訂履歷` 第 7 列逐字如上。CPAA_0521 檔內無對應的修訂記錄。

**影響** —— 下放包 §4 提出「若已同步下架，實質缺口為 6 條」。實測結論是
**未同步，缺口維持 7 條**。

**Phase 2 處置（2026-08-12）— CLOSED by R-P14**。提案獲採納。逐字：

> leaf `SWE1-PROJ-133` 於 MD 版 037 標記 unavailable 不拘束主線。R-P2 已定 CPAA_0521 為權威，副線之下架不得撤銷主線之 live leaf。未覆蓋缺口維持 **7 條**。

---

### A-PJ12 — 下放包 §5 CAN 範式的列舉標籤在 DBC 中不存在 · **CLOSED by R-P15** (2026-08-12)

下放包 §5 的 CAN 步驟範式寫
`Send CAN: BCM_FD_14.Command_02Sts = 1 (PSD)` 與 `= 0 (NOT_PSD)`。

**Evidence** — `BCM_FD_14.Command_02Sts` 確實存在於 `PHDCC27_E2A_R1_FDCAN8.dbc`，
其 `VAL_` 表為 `0 "Not_Pressed" / 1 "Pressed" / 3 "SNA"`。字串 `PSD` 與
`NOT_PSD` 在兩份 DBC 中皆不存在。

**影響** —— L-PJ1 要求送出的值必須存在於該 signal 的 `VAL_` 表。範式若照抄，
會被它自己的 gate ABORT。這是範式的缺陷，不是 gate 的缺陷。

**Proposed** — 範式改用 DBC 自身的標籤（`Pressed` / `Not_Pressed`），已寫入
`data/signal_map.json → can_step_pattern`；`correction` 欄記錄了原文與更動
理由。四要素結構（PROXI 前置 → `message.signal = 值 (標籤)` → 明確持續
時間 → 釋放後讀值比對）完全不變。

**Phase 2 處置（2026-08-12）— CLOSED by R-P15**。提案獲採納並推廣為通則。
逐字：

> CAN 送值標籤一律以 DBC `VAL_` 表為準。`Command_02Sts` 之合法標籤為 `Not_Pressed` / `Pressed` / `SNA`；`PSD` / `NOT_PSD` 於兩份 DBC 皆不存在，不得使用。
> SWC 跨 feature 範式之引用原則更正為：**取其結構（PROXI 前置 → `message.signal = 值 (標籤)` → 明確持續時間 → 讀值比對），不取其字面標籤**。

`PSD` / `NOT_PSD` 已列入 `data/signal_map.json` 的
`_meta.forbidden_value_labels`。跨 feature 引用原則的更正亦回寫至 A-PJ07。

---

### A-PJ13 — `$Screen_Size$` 其實可由 mapping 表解析 · **CLOSED — R-P7 升格為雙來源** (2026-08-12)

下放包 §4 列 `$Screen_Size$` 為未解析之一（未解析 2）；§5 以 R-P7 裁定其
目標。

**Evidence** — mapping 表 `Proxi & Configuration` 分頁第 95 列，Logical
Identifier `Head_Unit_Screen_Size`，Atlantis High 欄給出 `Radio_Display_Type`
—— 正是 R-P7 所裁的同一目標。字面 token `Screen_Size` 不是 LID，
`Head_Unit_Screen_Size` 才是。

**影響** —— 真正未解析的 token 是 **1** 個（`$HCP_DISP2.Est_Range_BEV$`），
不是 2 個。R-P7 由「裁決指定」升格為「裁決 + mapping 表雙來源」。

**Phase 2 處置（2026-08-12）— CLOSED**。R-P7 由「裁決指定」升格為
**雙來源**：mapping LID `Head_Unit_Screen_Size`（名稱）+ PROXI
`Radio_Display_Type`（列舉）。裁決本身不變，證據基礎加強。
`data/signal_map.json` 中該 token 已標 `status: resolved`，未解析 token 降為
**1 個**。

---

### A-PJ14 — `Accessory_Interface_Specification_CarPlay_Addendum_R10` 未落地 · **CLOSED by R-P16** (2026-08-12，素材已補入)

workbook 的 `Specification Reference` 欄在 **82 列**具名引用此規格（含
`§3.2.6`、`§3.3.5` 等章節錨點），該檔不在 `inputs/`，下放包 §3.2 亦未列入。

**Evidence** — spec_reference 欄逐列掃描：`Accessory_Interface_Specification_
CarPlay_Addendum_R10` 命中 82 列，其中 10 列指 `§3.2.6`、9 列指 `§3.3.5`、
6 列無章節。

**檔案已在專案樹內定位，但不在 R-P5 所裁的素材根目錄下**：

```
1_Customer_Requirement/CPAA_spec/Accessory Interface Specification CarPlay Addendum R10.pdf
9_ASPICE/01_SYS.1 Requirement Elicitation/CPAA/Accessory Interface Specification CarPlay Addendum R10.docx
9_ASPICE/01_SYS.1 Requirement Elicitation/CPAA/SYS1_Accessory Interface Specification CarPlay Addendum R10.xlsx
（另 10_Reviewing/00_TestCase/Bluetooth/REF/ 亦有同名 PDF）
```

**未複製** —— R-P5 把素材根目錄釘在 Projection 目錄，從別處取檔是範圍決定，
屬 Tier 2。路徑列在此處，讓 Phase 2 只需一句裁決即可。

**Phase 2 處置（2026-08-12）— CLOSED by R-P16，素材已補入**。逐字：

> CarPlay Addendum R10 納入 `inputs/`（82 列引用，帶 §3.2.6、§3.3.5 等錨點）。授權跨出 R-P5 根目錄取檔。

四處「副本」經 hash 比對實為**三件不同產物**，不是三個版本，§4.1 的異 hash
分支未觸發：兩份 PDF 位元相同（`b8d4d6e1…`），依規則取
`1_Customer_Requirement/CPAA_spec/` 者；另有 `.docx`（`6fc6d1fc…`）與 SYS.1
匯出 `.xlsx`（`5665820f…`）。三種格式全部落地，寫入
`feature.yaml → paths.carplay_addendum_*`。DR#6 關閉。

---

### A-PJ15 — Projection Device HMI 規格版本與 workbook 引用不符 · **CLOSED by R-P17** (2026-08-12，素材已補入)

`inputs/` 內的 Projection Device HMI Logic and Flow 是 **(February 5 2026)**
版（SYS1 匯出 + PDF 各一）。workbook 的 spec_reference 引用的是
**`R1_SR24_Post_2A_(May_3_2023)`**，共 **116 列**帶此版本戳記（該文件合計被
126 列引用）。

**Evidence** — spec_reference 欄版本戳記分布：`(May_3_2023)` 116 列、
`(March_13_2023)` 75 列、`(Dec_15_2023)` 34 + 6 列。後兩者分別對應 Device
Manager 與 Pop Up List，**與 `inputs/` 內的檔案版本相符**；只有 Projection
Device 這一份對不上。

**May 3 2023 版已在專案樹內定位，同樣不在 R-P5 根目錄下**：

```
1_Customer_Requirement/R1LR SR26 ATL-H/25PI3.5/HMI/Projection Device HMI Logic and Flow R1 SR24 Post 2A (May 3 2023).pdf
1_Customer_Requirement/R1LR SR26 ATL-H/25PI3.5/HMI/Projection Device HMI Change Log R1 SR24 Post 2A (May 3 2023).xlsx
```

**為何重要** —— O-1 要求改寫後的步驟「不牴觸基本 spec」。若拿 2026 版去核
2023 版寫成的 116 列步驟，任何差異都無法分辨是「原步驟錯」還是「版本演進」。
Change Log 同時在該目錄下，可直接量化兩版差距。

**Phase 2 處置（2026-08-12）— CLOSED by R-P17，素材已補入**。提案獲採納，
並明確指定核對基準。逐字：

> Projection Device HMI Logic and Flow 兩版併存。**核對基準為 `(May 3 2023)` 版**——workbook 116 列引用該版，且對照組（Device Manager `(March 13 2023)`、Pop Up List）版本皆相符，僅此一份對不上。`(February 5 2026)` 版保留於 `inputs/` 作版本演進參照。O-1 之「不牴觸基本 spec」以 May 3 2023 版為核對對象。

PDF（`36e585c3…`）與 Change Log（`61338e3b…`）各僅一處副本，無 hash 衝突。
另補入下放包未點名的同版 SYS1 匯出（`530274f8…`，取自
`9_ASPICE/…/SYS1_HMI/Archive/`），使核對基準版與 Feb 2026 版一樣具備
outline —— **此件屬自行判斷補入，待 Pei 覆核**。全部寫入
`feature.yaml → spec_baseline`。DR#7 關閉。

---

### A-PJ16 — CFTS025 未落地 · PENDING

workbook 的 spec_reference 在 **24 列**引用 `CFTS025`；未覆蓋 leaf
`SWE1-PROJ-146` 的條文亦逐字寫
`For Definition of HMI USB Source refer to CFTS025-4660`。該檔不在
`inputs/`，下放包 §3.2 未列入。

**Evidence** — spec_reference 掃描命中 24 列；037 leaf 146 description 逐字
如上。專案樹內僅找到 CFTS025 的**測試用例簿**與 SYS.2 目錄，未確認需求本文
`.doc/.docx/.reqifz` 是否存在：

```
6_SW_Test/CFTS025-PlayerFunctions/…_SWQT_CFTS025_PlayerFunctions_20260626.xlsx
9_ASPICE/02_SYS.2 System Requirements Analysis/CFTS 025 Player Functions/
```

**影響** —— leaf 146 是 7 條未覆蓋 leaf 之一，且它唯一的內容就是轉指
CFTS025-4660。沒有 CFTS025，146 的補列只能寫成 BLOCKED 佔位。

**Phase 2 處置（2026-08-12）— 維持 PENDING**。R-P18 逐字：

> CFTS025 開 DR#8，**不阻塞** Phase 3 / Phase 4。leaf `SWE1-PROJ-146` 全文轉指 `CFTS025-4660`，需求本文未確認存在，維持未覆蓋。

與 Phase 0 提案的差別：146 **不補 BLOCKED 佔位列**，而是維持未覆蓋。7 條
未覆蓋 leaf 的補列工作中，146 不在其列。DR#8 維持 OPEN 但不阻塞。

---

---

## Phase 2 新增

### A-PJ17 — mapping 表列舉值截斷，不具權威性 · **CLOSED by R-P20** (2026-08-12)

`Logical Identifiers and CAN Mapping v1_76.xlsx` 的列舉值與 PROXI 不一致，
且是**截斷**而非相異 —— 若拿 mapping 做值域檢查，合法值會被判為違規。

**Evidence** — `VC_VEH_LINE` 的 `Format` 欄（`Proxi & Configuration` 分頁
第 433 列，Atlantis High 區塊）逐字結尾為：

```
… 100 = K8 (64 Hex) 101 = WL (65 Hex) # = Not Used
```

止於 **101**，其後以 `# = Not Used` 收尾。PROXI `Format` 分頁 **row 466**
同一參數則列至 `130 = HDCC`。mapping 所缺者恰為
**102 / 103 / 104 / 105 / 106 / 124 / 130** 七個代碼。

**這條的殺傷力**：R-P8′ 要寫的 `= 105 (332)` **正落在 mapping 缺漏的區段
內**。若 L-PJ2 對 mapping 執行值域檢查，R-P8′ 這條裁決的產出會被自己的 gate
判為違規。兩條裁決在同一天下達，衝突點只有實測才看得見。

**Phase 2 處置 — CLOSED by R-P20**。逐字：

> PROXI 之列舉值為權威來源；`Logical Identifiers and CAN Mapping` 僅供 Logical Identifier → 訊號／配置字名稱之對映，其列舉值不具權威性。
> 依據：mapping v1_76 之 `VC_VEH_LINE` 列舉截斷於 `101 = WL`，缺 `102/103/104/105/106/124/130`；PROXI `Format` row 466 完整列至 `130 = HDCC`。
> L-PJ2 之值域檢查一律對 PROXI 執行，不得對 mapping 執行。

裁決所引之截斷處、缺漏代碼清單與 PROXI 列號**逐項經實測確認相符**。已寫入
`feature.yaml → enum_authority`、`data/signal_map.json → _meta.enum_authority_rule`
與 profile §5 的 L-PJ2。

---

### A-PJ18 — L-PJ6 詞界缺陷造成假陽性 · **CLOSED** (2026-08-12)

L-PJ6 以子字串比對搜尋模糊語，`content area while maintaining` 之中的
`area while` 被誤判為 `a while`。

**Evidence** — 修正前的 11 處命中中，`a while` 2 處（row 431、433）全為假
陽性，兩列的 Expected Result 皆為同一句型
`… fills the projection content area while maintaining …`。真正的 `a while`
在全簿 **0 次**。

**修正** —— 改為詞界比對，並依 §5.2 擴充詞彙表：

```python
PATTERN = re.compile(r'\b(?:correctly|normally|properly|successfully|as expected|reasonable|a while)\b', re.I)
```

**修正後重跑結果 — 與 §5.2 預期完全相符**：真陽性 **10 處**（**ER 9 /
PROC 1**），假陽性 **0**。分布：`correctly` 8 處、`normally` 2 處；
`properly` / `successfully` / `as expected` / `reasonable` / `a while` 各
**0 處**。涵蓋 **9 個實體列**（row 520 於 Procedure 與 Expected Result 各命中
一次，故 10 處落在 9 列上）。

| row | tc_id | 欄位 | 詞 |
|---|---|---|---|
| 424 | NR1L-PROJ-423 | ER | correctly |
| 425 | NR1L-PROJ-424 | ER | correctly |
| 426 | NR1L-PROJ-425 | ER | correctly |
| 427 | NR1L-PROJ-426 | ER | correctly |
| 428 | NR1L-PROJ-427 | ER | correctly |
| 429 | NR1L-PROJ-428 | ER | correctly |
| 434 | NR1L-PROJ-433 | ER | normally |
| 435 | NR1L-PROJ-434 | ER | normally |
| 520 | NR1L-PROJ-519 | PROC + ER | correctly |

新增的 `as expected` 與 `reasonable` 兩詞在現有 559 列中皆無命中，作用是
對 Phase 4 以後新寫的文字設防。

---

### A-PJ19 — R-P12 的 RD-1 列號無一種讀法能全對 · **CLOSED** (2026-08-12)

R-P12 的窄口清單與 RD-1 清單使用了兩種不同的列號慣例，且無論採哪一種，
RD-1 清單都有一項對不上。

**Evidence** —

- **窄口清單 `row 424–429`** — 與實測**完全相符**。六列皆為 Expected Result
  內的 `correctly`（見 A-PJ18 表）。此段無疑義。
- **RD-1 清單 `433 / 434 / 520`** — 兩種讀法各對一半：

| 讀法 | 433 | 434 | 520 | 結果 |
|---|---|---|---|---|
| 實體列號 | row 433：詞界修正後**無任何違規**（其原 `a while` 正是 A-PJ18 的假陽性） | row 434：`normally` ✅ | row 520：`correctly` ✅ | 誤含 433、**漏掉 row 435**（`normally`） |
| tc_id 尾碼 | `NR1L-PROJ-433` = row 434 ✅ | `NR1L-PROJ-434` = row 435 ✅ | `NR1L-PROJ-520` = row 521，PCTS/MT1 測項，**不含任何模糊語** | 前兩項全對，520 落空 |

**成因推測**：RD-1 清單像是在詞界修正**之前**、以混合慣例整理出來的 ——
`433 / 434` 取自 tc_id（當時 434 是 `normally`、433 是假陽性 `a while` 所在
列的 tc_id 鄰居），`520` 取自實體列號。

**未自行調和**（下放包 §0.5）。兩種讀法皆未套用；`er_narrow_gate` 的白名單
目前只實作已無疑義的 `row 424–429`。

**Phase 2 補裁（2026-08-12）— CLOSED**。提案獲採納，逐字：

> 434/435/520 採實體列號

R-P12 的 RD-1 清單因此定為**實體列 434 / 435 / 520**；窄口清單 424–429 不變。
九個真陽性列自此完全分割：**六列走窄口純刪除，三列入 RD-1**，無重疊、無遺漏。
`er_narrow_gate` 的白名單與 RD-1 清單皆已可完整實作（profile §5）。

---

### A-PJ20 — row 441 要求的 refresh rate 在 D5 之外 · **CLOSED** (2026-08-12)

row 441（`NR1L-PROJ-440`）的 Procedure 為：

```
1. Open Android Auto projection on the HU
2. Start PCTS-D5 in the PCTS tool
3. Read color depth from the PCTS tool
4. Read refresh rate from the PCTS tool
5. Check that color depth is 24-bit RGB per pixel
6. Check that refresh rate is 60 Hz
```

**Evidence（實機取證，2026-08-12）** —— PCTS Verifier `5.1-prod.922397802`
內，D5 的完整標題逐字為 **`D5 - Confirm HU Displays 24-Bit Color`**，只涵蓋
色深。`DisplayTests` 全 17 項（D2–D6、D8–D19，無 D1／D7）中**沒有任何一項
處理 refresh rate**。步驟 4 與步驟 6 因此無測項支撐。

能對應 60 Hz 者不在 DisplayTests 而在 **VideoTests**：

- `V59 - Video Config 60 FPS`（config 面，與「讀取設定值」的語意較近）
- `V8 - 60 FPS Rendering`（rendering 面）

Test Item 原文為 `Color shall be 24 bits of RGB color per pixels with a
60 Hz refresh.` —— 需求本身確實同時要求色深與更新率，所以缺的是**步驟少指
了一個測項**，不是需求寫錯。

**未自行修改步驟**（下放包 §8 第 4 點）。row 441 在 `pcts_evidence.json` 中
維持 locked。

**Phase 2 補裁（2026-08-12）— CLOSED，提案未獲採納**。逐字：

> A-PJ20 不指定 V59/V8

**不得指派 `V59` 或 `V8`**。row 441 維持不動，入 RD-1；DR#9（V59 取證）撤銷。

**理由與先例**：`V59 - Video Config 60 FPS` 與 `V8 - 60 FPS Rendering` 是兩個
不等價的候選（config 面 vs rendering 面），二選一即在來源之外指認對象。與
R-P9 對 `$HCP_DISP2.Est_Range_BEV$`（三候選）、R-P18 對 leaf 146 的處置同型。
需求本身仍要求 60 Hz —— 缺的是誰來驗，那是 RD-1 要問的，不是這裡能補的。

---

### A-PJ21 — row 443 引用的測項在 PCTS 中不存在 · **CLOSED** (2026-08-12)

row 443（`NR1L-PROJ-442`）步驟 2 寫 `Run the PCTS video / display
configuration test`，未帶測項編號。

**Evidence（實機取證，2026-08-12）** —— app 內 431 個測項中**無任何一項以此
命名**。已逐項展開比對 `DisplayTests`（17 項）與 `VideoTests`（V4–V15、
V45–V47、V50–V57、V59、V60）兩個分類。

row 443 的 Test Item 逐字為 `All pixels must be visible to the end user.
Square pixels are recommended.`，語意最接近者為
**`V45 - Video Config Pixel Aspect Ratio`**（方形像素 = pixel aspect ratio
1:1）。同分類另有 `V46 - Video Config Viewing Distance`、
`V47 - Video Config Preferred Resolution`、`V50 - Complex video test`。

**未逕行認定**。指認測項編號等同填補來源未明述之內容（O-4），且四個候選
彼此不等價 —— 與 `$HCP_DISP2.Est_Range_BEV$` 的三候選情形同型。

**Phase 2 補裁（2026-08-12）— CLOSED，走提案的後半**。逐字：

> A-PJ21 不指定 V45

**不得認定為 `V45`**。row 443 比照 R-P18 對 leaf 146 的處置，維持不動並入
RD-1；DR#10 撤銷。四個候選（V45 / V46 / V47 / V50）互不等價，指認任一即編造
（O-4）。

---

### A-PJ23 — Phase 2 自行判斷補入 SYS1 匯出（May 3 2023）· **CLOSED — 追認留用** (2026-08-12)

Phase 2 §4.2 點名補入 `(May 3 2023)` 版的 PDF 與 Change Log 兩件。執行時另補入
**第三件未經點名者**：

```
9_ASPICE/01_SYS.1 Requirement Elicitation/SYS1_HMI/Archive/
  SYS1_HMI_Projection_Device_HMI _Logic_and_Flow_R1_SR24_Post_2A_(May_3_2023).xlsx
SHA256 530274f8c0afed9a12e2b1445b7fc6c06e3e09d6096fcb53720e325683de4f7c
```

**補入理由（執行端判斷，非裁決）** —— repo 內既有慣例是「SYS1 匯出 + PDF 成對」
（mode A/B），`inputs/` 的 Feb 2026 版正是這樣成對存在。R-P17 把核對基準定在
May 3 2023 版，若該版只有 PDF 而無 outline，核對基準就比參照版少一層工具。
補入使兩版對稱。

**性質** —— 這是 Tier 1 執行端在裁決文字之外自行擴大取檔範圍，即使方向有利，
仍屬應登記事項；Phase 2 上繳包已列為「待 Pei 覆核」。

**Phase 2 補裁（2026-08-12）— 追認留用**。逐字：

> SYS1 匯出留用（登 A-PJ23）

該檔留在 `inputs/`，並登記於 `feature.yaml → spec_baseline.projection_hmi_verify_sys1`。
本條之所以留存而非直接關閉了事：**它記錄的是一次「執行端自行判斷」被事後追認
的過程**，不是檔案本身的問題。日後若再出現同型判斷，這條是先例。

---

### A-PJ22 — Phase 2 下放包 §6.1 與 §6.2 互斥 · **CLOSED — 規則設計缺陷，歸屬分析層** (2026-08-12)

裁決逐字：

> 規則設計缺陷 — Phase 2 下放包 §6.1 與 §6.2 互斥。
> §6.2 禁止「執行任何 PCTS 測項本身」；§6.1 同時要求取得 MT1 的「量測值顯示位置」、D5 的「color depth 與 refresh rate 顯示位置」、WP43 的「提示流程」。這三項只在測項頁開啟後才可見，而開啟該頁即觸發 TestRunnerService。兩條規則在此三測項上無法同時滿足。
> 執行方於觸及界線後立即停止、改用唯讀路徑、並將三測項照實留為 partial 而未以推測補足（O-4），處置正確。實際後果為零：`Car not connected or lost focus`，session 未建立、10 秒逾時中止、無結果產生、HU 無狀態改變。
> **責任歸屬：規則撰寫方（分析層），非執行方。** 本條不計入執行方之偏差紀錄。
> 處置：R-P11 已預留「佐以人工確認補足 adb 無法取得之項目」之出路；依本輪裁決，該三測項之缺口併入首次實機執行時回填（DR#11）。
> 註：本條與 A-PJ19（R-P12 列號混用實體列號與 tc_id 兩種慣例）同屬分析層規則缺陷，但為不同事件，不合併。

**執行端佐證** —— logcat 逐字：

```
08-12 08:37:10  E PCTS.SERVICE: Car not connected or lost focus.
08-12 08:37:20  E PCTS.SERVICE: Could not restore ReceiverTestActivity on primary display
                java.util.concurrent.TimeoutException: Waited 10000 milliseconds
                  at …pctsverifier.testrunner.TestRunnerService.an(…)
```

事後查核：MT1 仍無 `Last test results` 鈕、全清單無新增結果記錄、logcat 無任何
`Finished` / `PASSED` / `FAILED`。與裁決所述「實際後果為零」相符。

**這條缺陷的可推廣形式**：`data/pcts_evidence.json` 的 `_meta.deviation` 已
逐項記錄。往後凡「唯讀取證」類授權，須先確認**所求資訊是否存在於唯讀路徑
可達的範圍內** —— §6.1 要的三項資訊在 §6.2 的授權邊界之外，這在下放前就
可判定，不需等執行時才發現。

---

### A-PJ24 — HUIG 4.5 規格本文缺件，且曾被 SYSRA 分析報告誤代 · **CLOSED by R-P22** (2026-08-12)

裁決逐字：

> HUIG 4.5 規格本文缺件，且曾被 SYSRA 分析報告誤代。
> 服務範圍：workbook 79 列（43 僅引規格本文、36 兼引）+ 037 之 16 條 SYS-RA-HUIG4.5 leaf。
> 誤代成因與 A-PJ05 同型：以名稱相近之文件當作同一件（A-PJ05 為記憶拼湊之文件名，本條為分析報告 vs 規格本文之層級混淆）。
> 處置：R-P21 重開 DR#4、R-P22 授權補入。補入並通過 hash 檢查後關閉。

**Evidence（實測複驗，2026-08-12）** —— 79 / 43 / 36 / **0** 四個數字逐項
重現，詳見 `DECISIONS.md` §0.3。「僅引 SYSRA 零列」成立：SYSRA 從未單獨作為
引用終點，永遠與規格本文並列。

**補入並通過 hash 檢查** —— `HUIG 4.5.pdf`（`4cad6608…`，三處副本位元全同）
與 `SYS1_HUIG4.5.xlsx`（`5df67a2a…`，單一副本），異 hash 分支未觸發。DR#4
關閉，本條關閉。

**與 A-PJ05 的關係** —— 兩條同型但不同錯法，值得並列記住：

| | A-PJ05 | A-PJ24 |
|---|---|---|
| 錯的東西 | 文件**名稱**（`AA-V4.5` / `CP-R46` 在來源中 0 次） | 文件**層級**（把 SYS.2 分析報告當成 SYS.1 規格本文） |
| 偵測方式 | 字串比對 —— 名稱根本不存在 | 引用形式分析 —— 名稱對得上，但引用的是 §/R-ID 條款錨點，分析報告沒有那種錨點 |
| 結果 | 缺件不存在，撤銷 | 缺件確實存在，補入 |

第二種比第一種難抓：`SYS2_HUIG_4_5_…SYSRA…xlsx` 檔名含 `HUIG_4_5`，在
`inputs/` 清單上看起來就是「HUIG 4.5 已到位」。**只有看引用的形式**
（`HUIG_4_5 §7.15 R07-326` 這種條款錨點）才會發現到位的那份給不出被引用的
東西。Phase 0 的缺件推導用的是「檔名是否出現」，抓不到這一類；往後應改以
**引用錨點形式**作判準。

---

### A-PJ25 — `额外来源需求`（70 列）非能力叢集，不可作 Layer 2 推導來源 · **PENDING（RD-1）** (2026-08-12)

裁決逐字：

> 037 Sub Categorization 之 `额外来源需求`（70 列）非能力叢集，作為 Layer 2 推導來源時不可用。依 §8.2 不由 TC 側重整，排除於交集推導並列入 RD-1 供 RD 作者評估。

**Evidence** —— 該組 70 列散在 `HMI Display` 40 + `Projection Audio` 25 +
`Projection Launch` 4 + `Connection` 1。組名本身描述的是「需求的來源出處」而
非「系統的一項能力」，與同層其他 12 組（`蓝牙配对与连接管理`、`导航与TBT`、
`语音控制` 等皆為能力名）不同構。

**執行端曾提出而被退回的處置** —— Phase 3 分析時建議「在交集階段直接拆掉」。
**該建議逾越 §8.2**：上游 RD 分析報告對「什麼算一個需求單元」有權威，TC 側
不得再拆解、合併或發明 RD 項目。組名不像能力叢集是事實，但那是 RD 作者的
判斷，不是 TC 作者可代為修正的東西。建議已撤回。

**處置** —— 排除於 Layer 2 交集推導之外，**不重整**；列入 RD-1 供 RD 作者
評估是否重分。這 70 列在 TC 側照常歸屬其現有的 `HMI Display` / `Projection
Audio` 等 Layer 2，不受影響。

**這條的普遍形式**：RD 側的分組即使明顯不合邏輯，TC 側的處置一律是「排除於
推導 + 上報」，不是「代為修正」。與 R-P9 / R-P18 / 補裁 #2 / 補裁 #3 的
「候選不唯一即不選」是同一種克制的不同面向 —— 前者管的是不編造，這條管的
是不越權。

---

### A-PJ26 — CFTS085 §1.3.2.14–18 為版本沿革章節，非功能章節 · **CLOSED by R-P23 / R-P24** (2026-08-12)

Layer 3 同構檢驗時發現：CFTS085 的五個章節依 **release 分章**而非依功能分章，
與同層的功能章節不同構，直接混用會使多個 Layer 2 誤判為「綑綁」。

**Evidence** —— 章節標題逐字：

| 章節 | 標題 | 服務列 | 散在幾個 Test Set |
|---|---|---|---|
| 1.3.2.14 | `SR20+ Apple Certification Changes` | 85 | 4 |
| 1.3.2.15 | `SR21+ Apple Carplay Certification` | 3 | 1 |
| 1.3.2.16 | `SR21+ Android Auto Certification` | 10 | 1 |
| 1.3.2.17 | `SR22+ Android Auto Certification` | 15 | 2 |
| 1.3.2.18 | `SR22+ Apple Carplay Certification` | 2 | 1 |
| | **合計** | **115** | |

這 115 列佔 CFTS085 全部 473 列引用的 **24%**。章節名帶 `SR20+` / `SR21+` /
`SR22+`，是「某個 release 新增的認證需求」的集合 —— 它按時間切，必然橫跨功能。

**影響（實測）** —— 把這五章一併計入時，`Projection Launch` 的主導章節是
`1.3.2.14`（49%）、`Projection Detection` 是 `1.3.2.14`（55%），兩者都被判為
「散在多個章節 = 仍綑著」。**排除版本沿革章節後重算，兩者的功能章節數分別
降到 4 與 2**，性質完全改變 —— 它們不是綑綁，只是有很大一部分需求來自
release 增補。`Disconnection` 更明顯：49 列中 26 列來自版本章節，剩下 23 列
有 87% 落在 `1.3.2.11.5 Disconnecting from Wireless Projection`，是乾淨的。

**處置 — CLOSED by R-P23（兩點皆裁准）**：五碼為 Layer 3 粒度、四碼僅作
相鄰性父層；§1.3.2.14–18 排除於同構檢驗，另記為 **version-track**。

⚠️ **R-P23 的補充條款是本條最重要的一句**，且是裁決端主動加上的：

> version-track 這 115 列在 Phase 4 修訂時的 spec 核對對象**仍是那些版本章節**——排除只在框架推導階段生效，不能讓後人以為這批列沒有 spec 依據。

「排除於同構檢驗」與「沒有 spec 依據」是兩件事。前者是框架推導的方法選擇，
後者會讓 115 列（佔 CFTS085 引用 24%）在 Phase 4 失去核對基準。已於 profile
§3d 與 `data/layer2_isomorphism.json` 的 `_meta` 兩處明文標示。

**R-P24 一併裁定相鄰性判準**：同構度以**共同父章節**計算，單一章節佔比僅在
跨父章時才構成綑綁證據。這條救回兩個原本被誤判的叢集 —— `Connection`
（`.11.2`+`.11.3` 同屬 `.11`，四碼即 100%）與 `Vehicle Signal Forwarding`
（`.10.2`／`.10.3` 同屬 Location Data 樹）。

**附帶發現：Layer 3 的正確粒度是五碼，不是四碼。** `1.3.2.11`（120 列）在
四碼層散在 7 個 Set，展開到五碼後幾乎一一對應：

```
1.3.2.11.2 Pairing to Wireless Projection        27 → Connection 19, Pairing 8
1.3.2.11.3 Connecting to Wireless Projection     55 → Connection 35, Device Manager 18
1.3.2.11.4 Active Wireless Projection            18 → Performance 10, Wireless Coexistence 4, Projection Launch 4
1.3.2.11.5 Disconnecting from Wireless Projection 20 → Disconnection 20（100%）
```

`1.3.2.10`（88 列）同理：`.10.1 Vehicle Sensor Data` 71 列 → Knob 42 +
Day/Night Mode 22，`.10.2/.10.3 Location Data` 17 列 → Vehicle Signal
Forwarding 100%。**四碼層會把「車輛感測資料」與「定位資料」壓成一格**，
五碼層才分得開。

---

### A-PJ27 — Part N §N.3／§N.5 引用計數單位混用 · **CLOSED** (2026-08-12)

裁決逐字：

> Part N §N.3／§N.5 引用計數單位混用。
> §N.3「未解 85 列之來源：HUIG 75…」係逐**引用行**計數；§N.5「兩者未解的 75 列幾乎全部引 HUIG」將其當作逐**列**計數使用。實測逐列為 SYS3_PROJ 71 (84%) / CarPlay Addendum 44 (52%) / HUIG 39 (46%)。
> 錯誤不易察覺之成因：HUIG 之行計數 75 與 `HMI Display` 50 + `Projection Audio` 25 之列數和恰好相同，使誤用在表面上自洽。
> 影響：待辦優先序誤判——真正最大缺口為 SYSAD 而非 HUIG（R-P28 修正）。
> 責任歸屬：分析層。與 A-PJ19（實體列號 vs tc_id）同型，皆為座標系／單位未言明所致。
> 處置：Part N 加註「引用計數一律以列為單位」；§N.3／§N.5 依 R-P26 ~ R-P28 更新。

**巧合的殺傷力值得記一筆**：75 這個數字在兩種單位下都存在（HUIG 的行計數
75、兩個爭議 Set 的列數和 50+25=75），所以誤用不會產生任何看起來不對勁的
地方。**單位未言明時，數字自洽不構成正確的證據。**

Part N §N.3 已加註計數單位，§N.5 已依 R-P28 更新。

---

### A-PJ28 — 裁決條文未落檔即被引用 · **CLOSED** (2026-08-12)

裁決逐字：

> 裁決條文未落檔即被引用。
> R-P25 於分析層以散文形式產出，未整理為可貼區塊，致未傳達至執行層。Part N §N.2 兩處引用該條，而 `DECISIONS.md` 無正文。
> 依 Operating Charter「a ruling not written to the repo did not happen」，此期間 Part N 該兩處等同無依據。
> 處置：分析層此後所有裁決一律以獨立可貼區塊產出，不夾在散文中。執行層發現引用無正文時，維持不代擬並回報——本次處置正確。

**發生兩次，第二次才被登記**。第一次是 `R-P21` / `R-P22` / `A-PJ22` /
`A-PJ24` 那批（僅編號到達、條文夾在散文中），第二次是 R-P25。兩次的執行端
處置相同：不代擬、回報、編號保留。R-P25 的正文已於同日補發，落於
`DECISIONS.md` §0.5。

---

### A-PJ29 — SYSAD 的 `NRL-xxxxxx` 是章節 id，鑑別力不足以支撐 Layer 3 · **CLOSED by R-P29 / R-P30** (2026-08-12)

R-P28 指定 SYSAD 為優先推導來源，前提是「`Projection Audio` 剩餘 14 列的
Layer 3 只可能來自 SYSAD ——它是唯一能結案的來源」。推導已完成，**機械上成功
但實質上無法結案**。

**Evidence** —— SYSAD 的結構與 CFTS085／HUIG 不同類：

| 來源 | id 的性質 | 粒度 |
|---|---|---|
| CFTS085 | `{4935xxx}` = **需求條款 id**，一條一個 | 85 個 id / 473 列 |
| HUIG | `Rnn-xxx` = **需求 id**，前綴即章號 | 1,028 個 id 可用 / 62 列 |
| **SYSAD** | `NRL-xxxxxx` = **章節 id，一節一個** | **99 個 id / 500 列** |

驗證方式：在 docx 中該 id 出現在標題段落內，形式為
`NR1L/NRL-154702NRL-154702 - 4.6.1 設計目標與需求對映` —— id 標記的是**章節
本身**，不是章節內的某條需求。全檔 254 個 NRL id 對應 254 個章節。

**鑑別力實測** —— 500 列引用只落在 99 個 distinct 章節 id 上，且高度集中：

| section id | 章節 | 服務列 | 橫跨 Test Set |
|---|---|---|---|
| `NRL-154702` | `4.6.1 設計目標與需求對映` | **190** | **10 個** |
| `NRL-154519` | `4.3.2 高階系統架構` | 67 | 3 |
| `NRL-154418` | `4.2.1 設計目標與需求對映` | 50 | 3 |
| `NRL-154533` | `4.3.2 高階系統架構` | 42 | 1 |
| `NRL-154724` | `4.6.3 模組職責與主要介面` | 42 | 1 |

前 5 個 id 覆蓋 1,085 次引用中的 391 次。**`NRL-154702` 一個章節就服務 190 列、
橫跨 10 個 Test Set，其中包含 `HMI Display` 全部 67 列與 `Projection Audio`
全部 37 列。**

**為何無法結案** —— 一個橫跨 10 個 Set 的章節不能用來區分 Set。`Projection
Audio` 的 SYSAD 證據全部落在該章節，等同沒有證據。且該章節屬
`4.6 車輛狀態與導航數據`，與 `HMI Display`／`Projection Audio` 語意亦不相符
—— `設計目標與需求對映` 是需求對映表，表內列舉大量跨領域需求。

**與 A-PJ26 的關係：同類、反向。**

| | A-PJ26（CFTS085 version-track） | A-PJ29（SYSAD 需求對映表） |
|---|---|---|
| 章節性質 | 按 release 切分 | 需求對映表 |
| 造成的假象 | **假分散** —— 乾淨叢集看似綑綁 | **假集中** —— 綑綁看似乾淨 |
| 若不處理 | 誤殺 `Disconnection` 等 | 誤放 `HMI Display`（SYSAD 側 100% 單一章節） |

**假集中比假分散危險**：假分散會讓人多切一刀（成本可回收），假集中會讓綑綁
通過檢驗（缺陷留在框架裡）。若逕採 SYSAD 結果，`HMI Display` 的 SYSAD 側
同構度是 **67/67 = 100% 單一章節**，正好與 R-P26 的定案相反。

**處置 — CLOSED by R-P29（升格為通則）+ R-P30（結案來源改指）。**

執行端原提議「三個 `設計目標與需求對映` 型章節全數排除」**被通則取代且證明為
過度排除** —— R-P29 的鑑別力閘門實測只排除其中 2 個（`4.6.1` 跨 10 Set、
`4.2.1` 跨 6 Set），第三個 `4.5.1`（11 列、跨 3 Set）通過閘門且確有鑑別力。
**通則比黑名單精準**，這一點當場獲得驗證。

### 補充（Pei，逐字）—— 假集中的次生危害

> 假集中的次生危害：對映表型 id 以高覆蓋率遮蔽真正具鑑別力的來源。本案中 SYSAD 對 `Projection Audio` 覆蓋 37/37 = 100%，使其看似唯一結案路徑（R-P28），實則 CFTS019（16 列，Audio Management 之 CFTS，語意直接對應）才是應優先採用者。排除後可達涵蓋率不減反明——非 SYSAD 來源合計仍為 100%。

**此判斷已由實測完全證實**：CFTS019 的 16 列全數落在單一章節
`1.3.3.1 Source Priorities`（跨 1 個 Set），是 `Projection Audio` 最乾淨的
Layer 3 證據。SYSAD 那個 100% 覆蓋不但沒有幫助，還把它遮住了三輪。

**教訓的可推廣形式**：覆蓋率高的來源不必然是好來源。挑 Layer 3 來源時，
**先算鑑別力再看覆蓋率**；覆蓋率 100% 而跨 10 個 Set 的來源，其資訊量低於
覆蓋率 43% 而跨 1 個 Set 的來源。

---

### A-PJ30 — 定案／暫定之門檻在絕對列數，非百分比 · **CLOSED** (2026-08-12)

裁決逐字：

> 定案／暫定之門檻在**絕對列數**，非百分比。`HMI Display` 49/76 定案、`Projection Audio` 23/37 維持暫定，差別不在 64% vs 62% 兩個百分點，而在 **49 列 vs 23 列**。小樣本上的「雙來源同向」不足以定案。
> 本條往後可直接援用為框架判定之通用門檻。

**成因（Pei 自陳）** —— R-P26／R-P27 的裁決理由寫的是百分比，實際的判斷依據
是列數。**理由與依據不一致的裁決，後人會照著寫下來的理由套用**，於是在小樣本
上以 62% 這種看似及格的百分比作出定案。

與 A-PJ19（列號慣例未言明）、A-PJ27（計數單位未言明）同屬一類：**判準的
「單位」未明示**。三者合起來指向同一條可推廣的紀律 —— 凡涉及數字的裁決，
須同時寫明「量什麼」與「以什麼為單位」。

---

### A-PJ31 — R-P29 閘門不涵蓋 version-track，兩者為不同機制 · **CLOSED by R-P31 / R-P32** (2026-08-12)

R-P29 立論之一為「A-PJ26 與 A-PJ29 是同一個缺陷的兩種表現，不該逐案列黑名單」。
**實測不支持這一句**，但不影響 R-P29 本身的價值。

**Evidence** —— 在 R-P23 裁定的五碼粒度下，version-track 五章全部**通過**
R-P29 的閘門：

| 章節 | 列數 | 跨 Set 數 | 門檻 6 |
|---|---|---|---|
| `1.3.2.14 SR20+ Apple Certification Changes` | 85 | **4** | 通過 |
| `1.3.2.15` / `1.3.2.16` / `1.3.2.17` / `1.3.2.18` | 3 / 10 / 15 / 2 | 1 / 1 / 2 / 1 | 通過 |

**兩者是不同機制**：

| | A-PJ26 version-track | A-PJ29 需求對映表 |
|---|---|---|
| 排除理由 | **語意** —— 按 release 切分而非按功能 | **結構** —— 無鑑別力 |
| 偵測方式 | 讀章節標題（`SR20+ …Changes`） | 計算跨 Set 數（機械可算） |
| 造成 | 假分散 | 假集中 |
| R-P29 閘門 | **抓不到** | 抓得到 |

version-track 之所以抓不到，是因為它**確實有鑑別力**（4 個 Set 之內），只是
它劃出的界線是時間而非功能。鑑別力閘門量的是「界線夠不夠細」，量不到
「界線是不是沿著功能切」。

**影響** —— R-P23 的 version-track 排除條款**仍須獨立存在**，不能由 R-P29
取代。若誤以為 R-P29 已涵蓋而撤下 R-P23，`Disconnection` 等會重新被誤判為
綑綁（計入 version-track 時其主導章佔比由 87% 掉到 41%）。

**處置 — CLOSED by R-P31（兩閘門並存）+ R-P32（語意閘門定為通則但不自動化）。**

提案的前半獲採納：兩條併行、不得合併、不得以其一涵蓋其二（R-P31）。

提案的後半**被明文否決**：我曾建議把語意性排除也寫成規則（「章節標題含
release／版本標記者排除」）。R-P32 禁止此路 —— 字串啟發式**會誤傷標題含
版本標記的真功能章節**，且**無法涵蓋未預期的非功能切分維度**。語意閘門一律
人工閱讀、逐案登記理由，須記載章節 id、列數、切分維度、以及為何該維度非功能。

**這是本輪第二次「通則 vs 規則」的分野**，方向卻相反：A-PJ29 那次是**通則
勝過黑名單**（鑑別力可量化，機械閘門比人列清單精準）；這次是**人工判定勝過
規則**（切分維度不可窮舉，字串規則必然誤傷）。**可量化者機械化，不可窮舉者
人工化** —— 兩次的判準其實是同一條。

---

### A-PJ32 — `mobile GAL log` 無任何手冊，4 列無法完成 · **PENDING**（DR#12）(2026-08-12)

r231–r234（`NR1L-PROJ-229` ~ `232`）的 Procedure 以 `mobile GAL log` 為擷取
工具（Android Auto 裝置端 log capture）。

**Evidence** —— 該工具不在 `inputs/` 所涵蓋的三個工具目錄（`ATS 8.10.0`、
`PCTS`、`CarPlay TestApp`）之內，`inputs/` 亦無任何相關手冊或 README。
四列的步驟第 1 句皆為 `Start mobile GAL log capture on the Android Auto
device`，未載明啟動方式、log 位置、過濾條件。

**處置 —— 步驟維持現況不動**（O-3「無手冊者不得推測」）。開 DR#12。

**這 4 列在 pilot 中標為「已知不可完成」，非失敗。** 它們證明的是 O-3 會擋住
無依據的工具步驟 —— 與證明 gate 會放行有依據的工具（r219–r229 的 CarPlay /
ATS）價值相同。

---

### A-PJ33 — 既有簿內已標示、但因欄位凍結而無法更正之缺陷 · **PENDING**（RD-1）(2026-08-12)

r219–r224 共 6 列的 Remarks 載有 `*Section 35 應該修改為Section 15`，指
`Specification Reference` 欄所引章節編號有誤（Test Item 亦寫 `See section 35
Location...`）。

**該欄依 profile §1 凍結，本包不得修改。**

**這是 FULL_REFINE 特有的一類缺陷**：簿子自己已經標出錯誤，卻因為錯誤落在
凍結欄而無法在本 pipeline 內更正。與 L-PJ4 vs L-PJ6 的衝突同型（模糊語落在
凍結的 Expected Result 欄時只能轉 RD-1）。處置提案入 RD-1，不在 Phase 4 處理。

---

### A-PJ34 — r230 查無可觀察判準之 spec 依據，L-PJ5 殘留 1 處 · **PENDING** (2026-08-12)

r230（`NR1L-PROJ-228`）Procedure 全文為 `1. Inspect the vehicle hardware`，
ER 為 `The vehicle hardware includes GPS antenna and module.`。`inspect` 命中
L-PJ5。

**Evidence —— 三份 spec 皆查無可觀察的檢查方式**：

| 來源 | 命中 | 內容 |
|---|---|---|
| CFTS085 | 2 | `All vehicles that support CarPlay will be equipped with a GPS antenna and module.` —— 陳述配備事實，非檢查方式 |
| Projection Device HMI **(May 3 2023)**（O-1 核對基準） | **0** | —— |
| SYSAD | 6 | `GNSS module initialization and status monitoring` 等架構層敘述，無使用者可讀之頁面 |

**處置 —— 維持不動**（§2.4「找不到則維持不動並開 anomaly，不得自行發明查看
方式」）。**L-PJ5 因此殘留 1 處命中**，與下放包 §5 之「消除後 0 命中」不符。

**這正是 Pei 在下放時預期的那一類列**：ER 無可觀察判準且依 O-1 凍結，
Procedure 可改但改成什麼都缺乏依據 —— **「怎麼改都無法完全可執行」的列**。
它是有效的 pilot 結果，不是修訂失敗。

**Proposed** —— 入 RD-1，請 RD 作者補「GPS 天線與模組如何驗證」之依據；
或裁定此列改以整車配置文件（非 HMI）為核對對象。

---

### A-PJ35 — `logcat` 無手冊，過濾條件不得補 · **PENDING** (2026-08-12)

r222 / r223 / r224 的 Procedure 以 `logcat` 擷取，下放包 §2.5 要求「檢查是否
需補過濾條件」。

**Evidence** —— `logcat` 雖為 Android 平台標準工具，但 `inputs/` 三個工具目錄
內無任何 logcat 文件；本 feature 亦無任何 spec 載明應以何 tag／關鍵字過濾
Android Auto 的位置資料。

**處置 —— 步驟維持不動。** 依 O-3「無手冊者不得推測」，補過濾條件等同發明。
與 A-PJ32（mobile GAL）同型但程度較輕：logcat 的**啟動方式**是公知的，缺的
只有**過濾條件**。

**處置 — R-P38（2026-08-12）：不豁免，但維持現況為正確處置。**

> 平台標準工具（`logcat`、`adb` 等）之啟動與讀取方式屬公知，不需手冊即可撰寫；但其產品專屬參數（過濾 tag、訊息格式、欄位名稱）仍受 O-3 拘束，無依據不得填寫。

r222–224 的步驟**已寫到公知介面所能支持的層級**，缺的是產品專屬過濾條件。
DR#12 保留該項。本條由 PENDING 轉為**已裁但待補件**。

---

### A-PJ36 — pilot §4 之模糊語預期數 2 係跨欄計數 · **CLOSED** (2026-08-12)

下放包 §4 預期 `L-PJ6 模糊語 2`，實測 pilot 22 列於 **Procedure + Expected
Result** 範圍內為 **0**。

**Evidence** —— 那 2 處在 **`Test Item` 欄**：r228 與 r229 各一個
`correctly`。`Test Item` 依 profile §1 凍結，且 L-PJ6 的裁定掃描範圍是
Procedure + Expected Result（profile §5 實作註記，Phase 0 已記錄「widening to
Test Item inflates the totals」）。

**結論** —— 兩個數字都對，量的是不同範圍。**pilot 可修訂範圍內的模糊語確實
是 0，且那 2 處落在凍結欄，本來就改不了。**

與 A-PJ27（計數單位）、A-PJ19（列號慣例）、A-PJ30（門檻單位）同屬 canon §5a
「數字紀律」所管的類型 —— 這次未言明的是**掃描的欄位範圍**。canon §5a 的三條
分項（列號／計數／門檻）建議增列第四條：**掃描範圍須標明涵蓋哪些欄位**。

---

### A-PJ37 — `\bCAN\b` 加 `re.I` 命中英文助動詞 `can` · **CLOSED** (2026-08-12)

**Evidence（實測，逐項重現下放包所述）** —— 於 `Test Item + Pre-Conditions +
Procedure + Expected Result` 範圍：

| Test Set | 大小寫敏感 | 忽略大小寫 | 虛增 |
|---|---|---|---|
| `HMI Display` | **0** | **17** | 17 |
| `Knob` | **0** | **20** | 20 |

兩個數字逐字吻合。Phase 0 首次掃描即遭遇此缺陷（CAN 計數 86 vs 正確的 39），
當時已改為大小寫敏感並記於 recon 腳本註解，但**未升格為 canon 條款** ——
本輪補上。

**注意本條同時示範了 canon §5a 的兩條**：虛增只在 `TI+PRE+PROC+ER` 這個
**範圍**下才是 17／20；若只掃 Procedure 欄，`HMI Display` 的虛增是 2、
`Knob` 是 0。**大小寫（第五條）與掃描範圍（第四條）必須一起言明，數字才可
重現。**

---

### A-PJ38 — `inspect` 子字串命中專有名詞 `Car Inspector`，L-PJ5 基線虛增 2 · **CLOSED** (2026-08-12)

L-PJ5 以子字串比對搜尋禁用動詞，`Car Inspector` 之中的 `Inspector` 被誤判為
`inspect`。

**Evidence** —— 全簿 Procedure 欄逐詞掃描：

| 詞 | 子字串 | 詞界 | 假陽性 |
|---|---|---|---|
| `observe` | 1（r150） | 1 | — |
| `check whether` | 3（r89, r98, r542） | 3 | — |
| `inspect` | **3**（r169, r170, r230） | **1**（r230） | **r169, r170** |

r169/r170 的原文為
`Check that the night-mode characteristic value listed by Car Inspector matches…`
—— `Car Inspector` 是 CarPlay Tests App 的 Vehicle State Protocol 檢視名稱
（手冊 p47 `Vehicle State Protocol`），是**專有名詞，不是動詞**。

**影響 —— L-PJ5 的基線一直是錯的。** Phase 0 報告「禁用動詞 7 處
（check whether 3 / inspect 3 / observe 1）」並與下放包預驗值**逐項相符**，
但兩者都含這 2 個假陽性。**真值為 5 處**（check whether 3 / inspect 1 /
observe 1）。B2 的預期禁詞數 0 因此是正確的，我方測到的 2 才是缺陷產物。

**與 A-PJ18 同型**：A-PJ18 是 L-PJ6 的 `a while` 誤判 `area while`，本條是
L-PJ5 的 `inspect` 誤判 `Car Inspector`。**兩個 gate 有同一個缺陷，各自獨立
被發現，相隔三輪。** 修正一個 gate 的詞界時，應同時檢查所有以字串比對實作
的 gate。

**修正** —— L-PJ5 改為詞界比對：

```python
re.search(r'\b' + re.escape(verb) + r'\b', procedure, re.I)
```

profile §5 之 L-PJ5 條文已加註。修正後 B2 禁詞命中 **0**，與下放包預期相符。

---

### A-PJ39 — 泛稱量測設備：gate 未命中但不可執行 · **PENDING**（DR#13）(2026-08-12)

7 列之 Pre-Conditions 以泛稱描述量測設備，未指明何種設備，導致步驟無法執行。
**全簿此型 7 列全部落在 B3 的 `Performance` 組。**

| 列 | 泛稱原文 | 投屏側 |
|---|---|---|
| r110 | `Test equipment for measuring mode-update response time is available` | CarPlay |
| r113 | `Test equipment for measuring audio setup response time is available` | CarPlay |
| r114 | `Test equipment for measuring AAP video setup latency is available` | Android Auto |
| r115 | `A video sync pattern test setup for measuring HU input-to-display latency is available` | Android Auto |
| r116 | `A sync pattern test setup for measuring end-to-end input-to-UI latency is available` | Android Auto |
| r117 | `Test equipment for measuring audio output latency is available` | Android Auto |
| r118 | `Test equipment for measuring round-trip time and allocated bandwidth is available` | Android Auto |

**已查手冊，無一可解**：CarPlay Tests User Manual R2.19.4 確有
`Performance Tests > Touch Latency`（p26，判準 ≤140 ms）與
`Connectivity Utilities > CarPlay Network Tests`（p36，含 iPerf 與頻寬），
但 **r114–r118 皆為 Android Auto 列，CarPlay Tests App 不適用**；r110／r113
為 CarPlay 列但手冊無對應之 mode-update／audio-setup 量測工具。

同組另有 3 列（r109／r111／r112）**具體指名 CarPlay Tests App 路徑且與手冊
相符** —— 同一個 Test Set 內，指名與泛稱並存。

**處置 —— 7 列全部維持不動**（O-3／O-4）。開 DR#13。

**R-P42（2026-08-12）：採用 L-PJ9 為 flag gate。** 條件為 PRE 含泛稱設備詞
**且** Procedure 無具名工具路徑 —— 雙條件缺一不可。r112 即證明：其 PRE 有
泛稱但 Procedure 具名 `Utilities > Audio Utilities > Sample Rate`（手冊 p32），
單看 PRE 會誤抓。全簿 PRE 泛稱 8 列，扣除 r112 後為 7 列。

**DR#13 為列級阻塞，非階段阻塞**（依 R-P35 同型邏輯）—— `Performance` 批
照常結案，這 7 列列為「正確地不動」。

**這是 gate 覆蓋面的缺口**：L-PJ1～L-PJ8 全數不命中，但這 7 列確實無法執行。
現有 gate 檢查的是「寫出來的東西對不對」，不檢查「該寫的東西有沒有寫」。

---

### A-PJ40 — `<佔位符>` 型未解值：gate 未命中 · **PENDING**（RD-1）(2026-08-12)

全簿 **11 列**於可編輯欄含 `<…>` 形式之佔位符。分兩類，**處置不同**：

| 類型 | 列 | 內容 | 性質 |
|---|---|---|---|
| **未解值** | r36, r111, r124, r149, r225 | `<configured paging interval>`、`<configured pass threshold>`×2、`<TBD>`×2 | **缺陷** —— 判準未定，步驟無法判定通過與否 |
| 參數化 | r317–r322 | `<Device Name>`×3、`<Apple CarPlay OR Android Auto>`×3 | **非缺陷** —— 測試資料之參數位，執行時由測試者代入 |

B3 內僅 r111 一列（`<configured pass threshold>`）。

**處置 —— 未解值 5 列維持不動**，入 RD-1 請求判準（R-P43）。

**參數類由 6 列更正為 8 列**：另有 r60 / r61 的 `<Device Name>`，出現在
**ER 欄**（凍結）。執行層上輪只掃可編輯欄故漏計 —— 又是 canon §5a 第四條
的掃描範圍差異，兩邊都對。因 ER 凍結，此 2 列即使判為缺陷亦無從處置，
歸入參數類不影響結論。**缺陷類仍為 5 列。**

**白名單以列舉維護，不以樣式推斷**（R-P43）—— 新增參數形式須逐案登記。
理由：`<Device Name>` 與 `<TBD>` 樣式完全相同，只能靠語意分辨。

**同屬 gate 盲區**：`<TBD>` 在 Procedure 欄不觸發任何 gate，但它明確宣告
「這裡的值還沒定」。

---

### A-PJ41 — 前置條件未涵蓋步驟所需之資料狀態 · **PENDING** (2026-08-12)

4 列之 Procedure 需要清單中存在資料，但 Pre-Conditions 未保證：

| 列 | 步驟所需 | Pre-Conditions 保證 |
|---|---|---|
| r444 | `the recent calls list is displayed` | 僅「手機可用」「CarPlay 已連線」 |
| r446 | `Tap a conversation in the list` | 同上 |
| r449 | `the recent calls list is displayed` | 僅「手機可用」「Android Auto 已連線」 |
| r451 | `Tap a conversation in the list` | 同上 |

若通話紀錄或訊息清單為空，步驟 4 無法執行。

**對照組**：`USB Device` 的 r458 已正確保證 ——
`A USB flash drive containing playable audio files is available`。**同一個簿子
裡兩種寫法並存**，證明這是疏漏而非慣例。

**處置 —— 維持不動。** 補「至少一則對話存在」屬測試環境前提，非產品行為
斷言，但下放包 §3.1 明訂「前提是 spec 有依據」，而 spec 未載明此類前提，
故不自補。入 RD-1。

**gate 盲區之第三型**：前兩型是「該寫而未寫」（設備、判準），此型是
「前置與步驟不相稱」—— 三者皆無法以現有 gate 的字串比對檢出。

**R-P44（2026-08-12）：L-PJ11 暫緩，改為 B5 人工檢核。** 執行層報 4 列，
分析層測得 16 列（`Knob` 14 + `Projection Apps` 2）。複驗後兩者皆非錯誤 ——
**命中數完全取決於規則怎麼寫**：

| 規則形式 | PRE 無保證之列數 | Knob 命中 |
|---|---|---|
| 名詞列舉（6 名詞） | 5 | 0 |
| 名詞列舉 + `song` | 19 | 14 |
| 以 `in the list` 錨定 | **16** | **14** |

執行層漏掉 `Knob` 14 列的原因是名詞清單無 `song` ——
`Tap a song in the list to highlight it` 在 `Knob` 出現 14 次。分析層的 16
在第三種寫法下完全重現。

**這使 R-P44 的理由比原先更強**：不是「樣本太小所以規則不準」，而是
**規則的寫法本身決定樣本大小**。三個數字量的是三件不同的事。在樣本到齊前
定規則，等於先射箭再畫靶。B5 執行時樣本增至 18 列且集中於單一能力叢集，
屆時可判斷該寫法是慣例或疏漏。

---

### A-PJ42 — Pre-Conditions 與 Procedure／ER 內部矛盾 · **PENDING** (2026-08-12)

B4 發現 3 列之 Pre-Conditions 與同列的 Procedure 或凍結 ER 直接矛盾。
**證據強度不同，處置因此不同。**

| 列 | 矛盾 | ER 是否明述 | 處置 |
|---|---|---|---|
| **r139** | PRE 3 `A Siri session is active` vs PROC 1 `Confirm no Siri session is active` | **明述** —— ER 1 逐字為 `No Siri session is active on CarPlay` | **已更正**（改對了） |
| r140 | PRE 無 Siri 啟動前提，但 PROC/ER 要求 `dismissed`、`VR active indicator is removed` | **未明述**，僅邏輯蘊含 | 維持不動 |
| r561 | PRE 2 `The phone has never connected to the HU` vs PRE 3 `OOB Bluetooth pairing is established via the prior wired connection` | 未明述；ER 顯示有線連線發生於步驟 1 | 維持不動 |

**分界線在「ER 是否逐字陳述」**。r139 的 ER 直接寫出正確狀態，更正有明述依據；
r140 的 ER 只說「被關閉」，需由「能關閉必先開啟」推得前提 —— 那是推論不是明述，
依 O-4 不自補。r561 有兩種可讀法（刪除 PRE 3、或改寫 `prior` 之時序），
不自行選擇。

**r140 另有旁證但仍不採**：同型的 Android Auto 列 r145 之 PRE 3 為
`An Android Auto VR session is active on the HU` —— 兄弟列有、CarPlay 列無，
高度像是疏漏。**但兄弟列不是 spec**，依 O-4 仍不足以構成依據。此點記錄供
RD-1 提問。

**這是 gate 盲區之第四型**：前三型是「該寫而未寫」（設備／判準／前置），
此型是「寫了但自相矛盾」。同樣無法以字串比對檢出 —— 矛盾需要語意理解。

---

### A-PJ43 — r131 / r132 之 PRE／PROC／ER 完全相同 · **PENDING**（RD-1）(2026-08-12)

r131（`NR1L-PROJ-129`）與 r132（`NR1L-PROJ-130`）的 `Requirement or Design
ID`、`Pre-Conditions`、`Test procedure`、`Expected Result`、`Specification
Reference` **五欄完全相同**，僅 `Test Item` 相異。

兩列的 Procedure 逐字皆為：

```
1. Inject a simulated voice button event into the HU without setting the user action flag
2. Check that the HU does not forward a requestSiri message to the mobile device
3. Check that the Siri voice assistant interface is not displayed on the CarPlay screen
```

**Test Item 為凍結欄，無從由本 pipeline 判斷兩列的區別意圖。** 可能是同一需求
的兩種表述、或一列為冗餘。入 RD-1。

---

### A-PJ44 — L-PJ9 的樣式清單不完備 · **PENDING** (2026-08-12)

R-P42 定義 L-PJ9 之泛稱樣式為 `Test equipment for` / `test setup for` /
`analyzer for` / `equipment for measuring`，全簿命中 7 列。B4 發現該清單**漏掉
另一族泛稱**：

| 樣式 | 列 | 實例 |
|---|---|---|
| `trace tool` | r141, r142, r147 | `A trace tool capturing requestSiri events is available` |
| `capture tool` | r177, r188, r225, r270, r272, r375, r435, r480 | `capture tool (60 fps or higher) is available` |
| `simulator` | r221 | `simulator is connected and controllable` |

以擴充樣式重跑**雙條件**（PRE 泛稱 **且** Procedure 無具名路徑），全簿命中
由 7 列增為 **10 列** —— 新增 r141 / r142 / r147，皆在 B4 的
`Voice Recognition`。其餘 9 列因 Procedure 具名（ATS／CAN tool）而正確排除，
**再次驗證雙條件設計**。

**這與 A-PJ38（L-PJ5 詞界）、A-PJ18（L-PJ6 詞界）同屬一類：字串比對 gate 的
樣式清單不可能一次窮舉。** canon §5a 第六條（傳染性）管的是「同一缺陷跨 gate
複製」，本條指出的是另一面 —— **同一 gate 的樣式清單會隨批次推進而增補**。

**Proposed** —— L-PJ9 樣式清單改為**可增補清單**，每批發現新樣式即登記並
重跑全簿；不追求一次寫全。r141/r142/r147 於本批列為「正確地不動」並入 DR#13。
待 Pei 裁。

---

### A-PJ45 — B5 之 PROXI 值全數不在列舉內：`VC_Veh_Line` 用的是測試矩陣車型代號 · **PENDING — 停下條件** (2026-08-12)

R-P20 定 PROXI 為值域權威，B5（`Knob` 42 列）是其唯一的批量檢驗機會。
**檢驗結果為全數不合格，且不合格的方式與 R-P8′ 同型但規模大得多。**

**Evidence** —— B5 全 42 列的 Pre-Conditions 皆含 `PROXI VC_Veh_Line = <值>`，
共 7 個相異值，各 6 列：

| 值 | PROXI 列舉 | mapping 列舉 | workbook 車型欄（第 3 列） |
|---|---|---|---|
| `376` | ❌ 無 | ❌ 無 | 欄 Y `Fastack (376) Atl-Mi` |
| `637` | ❌ 無 | ❌ 無 | 欄 U `VF(ProMaster)637 Atl-Mi` |
| `598` | ❌ 無 | ❌ 無 | 欄 V `Commander (598) Atl-Mi` |
| `5210` | ❌ 無 | ❌ 無 | 欄 W `Regengade (5210) Atl-Mi` |
| `2261` | ❌ 無 | ❌ 無 | 欄 X `Toro(2261) Atl-Mi` |
| `HDCC27` | ❌ 無（列舉標籤為 `HDCC` = 130） | ❌ 無 | 欄 S `HDCC27 Atl-Hi` |
| `DT27` | ❌ 無（列舉標籤為 `DT` = 124） | ❌ 無 | 欄 T `DT27 Atl-Hi` |

**7 個值沒有一個在 PROXI 或 mapping 的列舉內。** PROXI `Format` row 466 的
33 個標籤全集為：
`Invalid, 343, 327FL, 226, PF, KL/K4, UF, UT, 334, 520, 551 /M1, 338, 521,
636 VM, 356, 952, 341, 552/MP, 949, 523, 358, 359, 553/M4, 556/M6, K8, WL,
281, 363, WS, 332, 560, DT, HDCC`。

**來源已查明**：這 7 個值**逐一對應 workbook 自身第 3 列的 7 個車型欄標題**
（欄 S–Y，即該簿的測試矩陣車型）。所以 `PROXI VC_Veh_Line = 376` 寫的不是
PROXI 配置字的值，而是**測試矩陣的車型代號**。

**與 R-P8′ 的關係 —— 同型但更嚴重**：

| | R-P8′（`= 332`） | 本條（7 值 × 6 列） |
|---|---|---|
| 值的身分 | PROXI 列舉的**標籤**（`105 = 332`） | 測試矩陣的**車型欄標題** |
| 可更正性 | **可** —— 標籤對應代碼 105 | **5 值不可** —— PROXI 列舉內根本沒有對應標籤 |
| 規模 | 1 個值 | 7 個值、42 列（全簿 PROXI 用量的大宗） |

`HDCC27` / `DT27` 或可對應標籤 `HDCC`(130) / `DT`(124)，但 `27` 這個後綴的
意義未明（車型年份？平台版本？）；其餘 5 值在 PROXI 列舉中**無任何近似標籤**
（`376` vs 列舉的 `356`／`358`／`359`／`363` 皆為不同車型，猜測即編造）。

**停下，不自行調和**（下放包 §0.5、B5 §重點一）。**42 列的 PRE 之 PROXI 行
全部維持不動。**

**根因（R-P47，2026-08-12）—— 比「代號寫錯位置」深一層。**

PROXI `Header` 第 4 列逐字為 **`HDCC27 - Draft`**：它是**單一車型的配置檔**，
不是全車系字典。所以 `PROXI VC_Veh_Line = 376` 不是「值寫錯」，而是
**「這條測項要在 376 那台車上跑」** —— 它天生對不進 HDCC27 的 PROXI，
因為 376 有自己的 PROXI。

**架構分層完全吻合，非巧合**：5 個對不上的全是 **Atl-Mid**，2 個對得上輪廓
的全是 **Atl-Hi**。profile §4 明訂訊號解析取 mapping 表的 **Atlantis High**
欄，**Atl-Mid 車型從一開始就在本專案的解析基礎之外**。

**影響範圍複驗：止於 `Knob` 42 列。** 全簿 `PROXI VC_Veh_Line = <值>` 命中
42 列全在 `Knob`（Atl-Mid 30 / Atl-Hi 12）。B6／B7 的 PROXI 為不同型
（`Projection_Mode` / `Wi-Fi_Cfg` / `USB_Presence`），全部在 HDCC27 檔內
可解，**不連帶阻塞**。

**DR#14 改為三層提問**（見 DATA_REQUESTS）——(b) 為關鍵且最省事：若 Atl-Mid
不在 SWQT 範圍，阻塞由 42 列縮為 12 列。

---

### A-PJ41 — 前置條件未涵蓋步驟所需之資料狀態 · **CLOSED by R-P48** (2026-08-12)

R-P44 將 L-PJ11 緩至 B5 人工檢核，判準為「**一致性本身就是判準**」：
14 列寫法一致則為慣例，參差則為疏漏。

**檢核結果 —— 完全一致。**

- 命中列：r192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216,
  218（14 列，全為偶數列）
- **Procedure 逐字相同**：`Tap a song in the list to highlight it`，14/14
- 結構僅 4 種變體，差異只在 CarPlay／Android Auto 與
  `The HU supports knob functionality` / `does not support`
- **PRE 保證清單內容者：0/14**

**判定 —— `Knob` 內為慣例，非疏漏。** 依 R-P44 的判準，L-PJ11 **不成立**為
該叢集的缺陷 gate。

**但跨叢集仍不一致**：B3 的 `USB Device` r458 明確寫
`A USB flash drive containing playable audio files is available`，而
`Projection Apps` r444/r446 與 `Knob` 14 列皆無。**同一簿內兩種慣例並存**。

**處置 — CLOSED by R-P48**：L-PJ11 **不採用**為 gate；跨叢集不一致改列
**RD-1 風格問題**，不作缺陷。同簿內兩種慣例並存屬既有書寫差異，非本 phase
可裁。

**方法論註**：只看 `Knob` 內部得「慣例」，只看 `USB Device` 得「疏漏」——
**兩個結論都對但範圍不同**。這是 canon §5a 第四條（掃描範圍）第一次作用在
**分析結論**上而非數字上。

---

### A-PJ47 — 分析層預期錯誤：以執行狀態預測步驟品質 · **CLOSED** (2026-08-12)

裁決逐字：

> Phase 5 B6 下放包預期「實車阻塞列步驟較粗、三型缺口密集」。實測 PROC 平均字元數 **268**（阻塞 33 列）vs **269**（非阻塞 16 列），L-PJ9／L-PJ10／L-PJ11 型皆 **0** 命中。
> 正確歸因：**步驟具體度取決於測項性質（量測型需外部設備規格）而非執行狀態**。B3 之 `Performance` 粗糙係因量測設備未指定，非因未實跑。
> 責任歸屬：分析層。**此後不得以執行狀態預測步驟品質。**

**成因（Pei 自陳）** —— 該假設背後是「沒跑過就沒被檢驗過，所以品質差」的
直覺。但這個簿子的品質決定於**寫的時候有沒有可依的工具規格**，跟後來跑沒跑
無關。

**可推廣形式** —— 預測步驟品質時，該問的是「這一列依賴什麼外部規格，那份
規格在不在手上」，不是「這一列跑過沒有」。B3 的 `Performance` 7 列與 B6 的
33 列實車阻塞列，執行狀態相同（皆未實跑），品質卻天差地別 —— 差別在前者
需要量測設備規格而該規格不在 `inputs/`，後者只需 HU 上的選單路徑。

**這是分析層的第五個預期錯誤**，但與前四個不同型：A-PJ19／A-PJ27／A-PJ30／
A-PJ37 皆為**量測條件未言明**（canon §5a 所管），本條是**因果假設錯誤** ——
用一個不相干的變數（執行狀態）去預測結果（步驟品質）。前者靠寫明條件可防，
後者只能靠實測推翻。

---

### A-PJ48 — 執行端 L-PJ5 掃描漏 `re.I`，被下放包預期值當場攔下 · **CLOSED** (2026-08-12)

B8 下放包預期 L-PJ5 禁用動詞 **2 列**，執行端實測 **0**。查明為執行端掃描器
缺陷，非簿子問題。

**成因** —— A-PJ38 將 L-PJ5 由子字串改為詞界比對時，修正式為
`re.search(r'\b'+re.escape(v)+r'\b', proc, re.I)`。但 B6／B7／B8 的批次掃描
腳本重寫該式時**漏了 `re.I`**，而禁用動詞出現在步驟開頭必為大寫
（`Check whether` / `Observe` / `Inspect`），故全部落空。

**全簿複驗（詞界 + 忽略大小寫）**：

| 詞 | 大小寫敏感 | 忽略大小寫 | 漏掉 |
|---|---|---|---|
| `observe` | 0 | **1** | r150 |
| `check whether` | 1 | **3** | r89, r98 |
| `inspect` | 0 | **1** | r230 |
| **合計** | **1** | **5** | — |

忽略大小寫之總數 **5** 與 A-PJ38 修正後的基線完全一致 ✅。

**影響範圍 —— 僅 B8。** 逐批以正確口徑複驗：B2 / B3a / B3b / B4a / B4b /
B6 / B7 的禁詞在兩種口徑下**皆為 0**，無批次被誤判；B8 的 2 列已於本批修訂。

**這是 canon §5a 第五條（文字比對須標明大小寫）在執行端自身工具上的實例。**
前幾次（A-PJ37 / A-PJ18 / A-PJ38）都是**簿子的資料**被誤判，這次是
**執行端的掃描器**出錯 —— 同一條紀律，兩種受害者。

**攔下它的是下放包的預期值**，不是任何 gate。§4 預期數字表在此發揮了設計
用途：**gate 檢查簿子，預期值檢查檢查器**。若當初 B8 未附預期值，這 2 列會被
列為「核實無誤」而漏改，且**任何 lint 都抓不到 —— 因為 lint 本身就是壞的**。

**與 A-PJ37 方向相反、根因相同**：

| | 錯誤 | 效果 |
|---|---|---|
| A-PJ37 | **多了** `re.I` | 假陽性（`CAN` 命中助動詞 `can`） |
| A-PJ48 | **少了** `re.I` | 假陰性（`Check whether` 大寫落空） |

**處置 — R-P49（2026-08-12）**：真正的根因不是漏了一個參數，是**批次腳本
重新實作了比對式**。只要重寫就會再漏一次，且下次可能漏在別處。比對式改為
**單一實作、跨批共用**（`features/projection/scripts/lint_defs.py`），
批次腳本一律 import 不得重寫。八項基線已複驗全數重現。

---

### A-PJ49 — VF176 訊號不在兩份 DBC 內：L-PJ1 的權威範圍問題 · **CLOSED by R-P51** (2026-08-12)

B10′ 之 `Cluster Navigation` 9 列（r370, r372–r379）的 Procedure 使用
`TELEMATIC_NAV_INFO.*` 與 `TELEMATIC_DISPLAY_INFO.*`，**兩份 DBC 皆無**。

| 訊號 | FDCAN8 | BHCAN |
|---|---|---|
| `TELEMATIC_NAV_INFO.Direction` / `.DistToTurn` / `.ResolutionDistToTurn` / `.Unit` | ❌ | ❌ |
| `TELEMATIC_DISPLAY_INFO.UTF_Text_1/2/3` | ❌ | ❌ |

DBC 內含 `TELEMATIC` 的訊息共 28 個（FDCAN8 21 / BHCAN 7），**無一為
`_NAV_INFO` 或 `_DISPLAY_INFO`**；BHCAN 有 `TELEMATIC_DISPLAY2`，名稱相近但
不同。mapping 表兩個分頁亦**零命中**。

**但它們不是憑空寫出來的** —— 定義在 `inputs/` 的
`Navigation_Repetition_on_IPC-LTM_(R1L)_VF176_V42_R5.docx`：
`TELEMATIC_NAV_INFO` 出現 **52 段**、`TELEMATIC_DISPLAY_INFO` **33 段**，
且該文件明文將其列為 **B/BH-CAN 訊號**（逐字：
`"TELEMATIC_DISPLAY_INFO.Infocode" B CAN signal`、
`"…TotalFrameNumber" BH CAN signal`）。

**這是 L-PJ1 的權威範圍問題，不是簿子的缺陷。** L-PJ1 規定「必須在
`PHDCC27_E2A_R1_FDCAN8.dbc` 或 `PHDCC27_E2A_R1_BHCAN.dbc` **其一**解析成功」
—— 該規定隱含假設「本簿所有 CAN 訊號都來自這兩份 DBC」，而 Cluster Navigation
這一支來自 VF176 儀表投影規格。

**與 R-P47 同型 —— 這是同一個盲點的第三次**：

| | 誤當作全部的那份 | 實際涵蓋範圍 |
|---|---|---|
| R-P8′ | mapping 列舉 | 截斷於 `101 = WL` |
| R-P47 | `PROXI_HDCC27_R3` | 單一車型 HDCC27 |
| **A-PJ49** | **兩份 PHDCC27 DBC** | **不含 VF176 儀表訊號** |

canon §5a 第九條（單一來源的涵蓋範圍 ≠ 其類別）第三次命中，且這次命中的是
**gate 自身的權威來源**。

**處置 —— 9 列全部維持不動**（其中 r376–379 另因 frozen 無論如何不動）。

**處置 — CLOSED by R-P51**：採提案 (a)，L-PJ1 權威擴充為 **DBC ∪ VF176
逐訊號登記表**，7 個訊號已人工登記於
`signal_map.json → vf176_signals`。負向驗證通過（未登記者仍 ABORT）。

**Pei 補述（逐字）**：

> 來源文件 `Navigation_Repetition_on_IPC-LTM_(R1L)_VF176_V42_R5.docx` 於 Phase 0 即已落地 `inputs/`，本 anomaly 成因確認為 **L-PJ1 權威清單不完整**，非缺件。不另開 DR。

**這一點的分辨很重要**：前兩次（R-P8′ / R-P47）的處置方向都是**限縮**權威，
這次是**擴充** —— 因為缺的不是資料而是 gate 的認識範圍。同一條 canon §5a
第九條，三次命中、兩種相反的修法。

**5 列最終零變更**：它們全是 READ 操作，訊號名稱本就正確；R-P51 解決的是
gate 會誤 ABORT 它們。

---

### A-PJ50 — L-PJ9 樣式清單第二次不完備 · **CLOSED by R-P46** (2026-08-12)

r542（HMI Display）之 PRE 第 2 項為
`A method to read the AAP ByeByeRequest message and ByeByeReason is available`
—— 泛稱工具，但 **L-PJ9 未命中**：現行樣式清單（`Test equipment for` /
`test setup for` / `analyzer for` / `equipment for measuring` / `trace tool` /
`capture tool` / `measurement tool` / `test tool` / `simulator`）不含
`A method to`。

**這是 R-P46「可增補清單」機制第二次生效** —— 第一次是 A-PJ44（B4 發現
`trace tool` / `capture tool` / `simulator`），本次是 `A method to`。

**未自行增補樣式** —— 依 R-P46，樣式擴充須記錄「新增樣式、擴充前後命中數、
新增命中列」，屬需要重跑全簿的動作，本批不逕行。r542 之 Procedure 已依
L-PJ5 修訂（`check whether` → 純讀取），PRE 之泛稱維持不動。

**處置 — CLOSED by R-P46（可增補清單機制第二次生效）**：`A method to` 已併入
`lint_defs.GENERIC_TOOL_PATTERNS`，全簿重跑，基線 **10 → 15**，新增命中
**r541 / r542 / r543 / r544 / r545**（皆為 HMI Display 之 AAP ByeByeRequest
與 video focus state 讀取方法）。

**連帶效應**：r541／r543／r544／r545 原分在 B11′，因此次擴充**重分類**併入
B10′ —— 屬 gate 擴充導致，非分類條件錯誤。R-P46 之「每次擴充須記錄新增樣式、
擴充前後命中數、新增命中列」已落於 `DECISIONS.md` §0.16 之擴充記錄表第二筆。

---

### A-PJ51 — 跨輪次進度數字未回頭對帳，`剩餘 173` 連續三輪傳遞 · **CLOSED** (2026-08-12)

裁決逐字：

> 跨輪次沿用之進度數字未回頭與總數對帳，致 `剩餘列數 = 173` 連續三輪傳遞，實際為 195。
> 責任歸屬：**分析層（下放包數字）與執行層（上繳包數字）共同**。
> 處置：進度數字每輪須以 `總數 − 已處理 − 阻塞` 重算，不得沿用前輪差值。

**成因** —— 差額 22 為 **B1 之 22 列被重複扣除**。雙方均未察，因**雙方皆沿用
前輪結論而非自總數重算**。

**正確基數**（本輪起一律以此重算）：

```
總資料列                    559
r562 殘樁（R-P19 刪除）      −1  → 558
已處理 B1–B4, B6–B10′        365
B5 阻塞                       42
B11′                        151
                          ─────
校驗              365 + 42 + 151 = 558 ✅
```

**這與前面十一條分析層錯誤都不同型**：A-PJ19／27／30／37 是量測條件未言明，
A-PJ47 是因果假設錯誤，A-PJ48 是工具實作缺陷 —— **本條沒有任何一方犯錯，
錯的是「沿用」這個動作本身**。數字第一次算錯之後，每一輪都忠實地把它傳下去，
而且**每一輪的內部運算都是正確的**（173 − 已處理 = 剩餘，算術無誤）。

**累計錯誤不會自行暴露，只會持續傳遞。** 已升格為 canon §5a 第十條。

## Assumption markers

None yet. Phase 0 wrote no test-case content, so no `[ASSUMPTION A-PJnn]`
marker has been emitted. Inline format in generated JSON reasoning:
`[ASSUMPTION A-PJnn]`.

## Status summary

51 條登記；**36 條 CLOSED、1 條 RETRACTED、14 條 PENDING**。

| ID | 狀態 | 阻塞 | 處置 |
|---|---|---|---|
| A-PJ01 | PENDING | 0（已依 R-P2 處置） | RD-1 |
| A-PJ02 | **CLOSED** | 0 | 由 `Specification Reference` 欄取代 |
| A-PJ03 | PENDING | 2 列（Est_Range_BEV） | RD-1；9/10 已解 |
| A-PJ04 | **CLOSED** | 0 | R-P8′ |
| A-PJ05 | **RETRACTED** | 0 | R-P13（原文保留） |
| A-PJ06 | **CLOSED** | 0 | R-P33 — Layer 2 定案：16 乾淨 + 1 橫切 + 1 綑綁 |
| A-PJ07 | PENDING | 0 | 記錄；引用原則經 R-P15 更正 |
| A-PJ08 | **CLOSED** | 0 | R-P19 |
| A-PJ09 | **CLOSED** | 0 | R-P13 |
| A-PJ10 | **CLOSED** | 0 | R-P8′ |
| A-PJ11 | **CLOSED** | 0 | R-P14 — 缺口維持 7 條 |
| A-PJ12 | **CLOSED** | 0 | R-P15 |
| A-PJ13 | **CLOSED** | 0 | R-P7 升格雙來源 |
| A-PJ14 | **CLOSED** | 0 | R-P16 — 素材已補入 |
| A-PJ15 | **CLOSED** | 0 | R-P17 — 素材已補入 |
| A-PJ16 | PENDING | 24 列 + leaf 146 | R-P18 — 不阻塞；DR#8 |
| A-PJ17 | **CLOSED** | 0 | R-P20 |
| A-PJ18 | **CLOSED** | 0 | 詞界修正；真陽性 10 處 |
| A-PJ19 | **CLOSED** | 0 | 補裁 #1 — RD-1 清單 = 實體列 434/435/520 |
| A-PJ20 | **CLOSED** | row 441 維持不動 | 補裁 #2 — 不指定 V59/V8，入 RD-1 |
| A-PJ21 | **CLOSED** | row 443 維持不動 | 補裁 #3 — 不指定 V45，入 RD-1 |
| A-PJ22 | **CLOSED** | 0 | 規則設計缺陷，歸屬分析層；不計入執行方偏差 |
| A-PJ23 | **CLOSED** | 0 | 補裁 #5 — SYS1 匯出追認留用 |
| A-PJ24 | **CLOSED** | 0 | R-P21 重開 DR#4、R-P22 補件；hash 全同 |
| A-PJ25 | **PENDING** | 0（不影響 TC 歸屬） | 排除於 Layer 2 推導；RD-1 |
| A-PJ27 | **CLOSED** | 0 | 計數單位混用；Part N 已加註「一律以列為單位」 |
| A-PJ28 | **CLOSED** | 0 | 裁決未落檔即被引用；R-P25 正文已補發 |
| A-PJ29 | **CLOSED** | 0 | R-P29 鑑別力閘門 + R-P30 來源改指 |
| A-PJ30 | **CLOSED** | 0 | 門檻在絕對列數非百分比；通用判準 |
| A-PJ31 | **CLOSED** | 0 | R-P31 兩閘門並存；R-P32 語意閘門不自動化 |
| A-PJ32 | **PENDING** | 4 列（r231–234） | mobile GAL 無手冊；DR#12 |
| A-PJ33 | **PENDING** | 6 列（r219–224，僅凍結欄） | Section 35 誤植，欄凍結；RD-1 |
| A-PJ34 | **PENDING** | 1 列（r230） | 查無 spec 依據；L-PJ5 殘留 1 |
| A-PJ35 | **CLOSED by R-P38** | 3 列待補件 | 平台工具不豁免；介面公知、參數受 O-3 拘束 |
| A-PJ36 | **CLOSED** | 0 | §4 模糊語 2 係跨欄計數；範圍內實為 0 |
| A-PJ37 | **CLOSED** | 0 | `\bCAN\b`+`re.I` 虛增；canon §5a 第五條 |
| A-PJ38 | **CLOSED** | 0 | L-PJ5 詞界缺陷；基線 7→**5**，B2 禁詞實為 0 |
| A-PJ39 | **PENDING** | 7 列（Performance） | 泛稱量測設備；DR#13 |
| A-PJ40 | **PENDING** | 5 列（未解值） | `<TBD>` 型佔位符；RD-1 |
| A-PJ41 | **CLOSED by R-P48** | 0 | L-PJ11 不採用；跨叢集不一致轉 RD-1 風格 |
| A-PJ42 | **PENDING** | 2 列（r140/r561） | PRE 與 PROC/ER 矛盾；r139 已更正 |
| A-PJ43 | **PENDING** | 0 | r131/r132 五欄相同；RD-1 |
| A-PJ44 | **CLOSED by R-P46** | 3 列（併 DR#13） | L-PJ9 改為可增補清單；7→10 列 |
| A-PJ49 | **CLOSED by R-P51** | 0 | L-PJ1 權威擴充為 DBC ∪ VF176 登記表 |
| A-PJ50 | **CLOSED by R-P46** | 5 列（併 DR#13） | L-PJ9 樣式增補；基線 10→15 |
| A-PJ51 | **CLOSED** | 0 | 進度數字跨輪傳遞；canon §5a 第十條 |
| A-PJ48 | **CLOSED** | 0 | 執行端掃描漏 `re.I`；僅影響 B8，已修訂 |
| A-PJ47 | **CLOSED** | 0 | 分析層預期錯誤：不得以執行狀態預測步驟品質 |
| **A-PJ45** | **PENDING — 停下** | **42 列（B5 全批）** | PROXI 值為測試矩陣車型代號，7 值全不在列舉內；DR#14 |
| A-PJ26 | **CLOSED** | 0 | R-P23 粒度改五碼 + version-track；R-P24 相鄰性判準 |
| A-PJ06 | ↑ 見上 | | `Projection Audio` 一結案即可關 |

### 尚待處理的 PENDING（6 條）

1. **A-PJ06** — Test Group 10 值 vs canon §4.1.1。獨立分析輪進行中；五份切法
   已產出，待 chat 出可簽版三層框架。
2. **A-PJ25** — `额外来源需求` 排除於 Layer 2 推導；入 RD-1，不阻塞。
2. **A-PJ16** — CFTS025；依 R-P18 不阻塞。
3. **A-PJ01 / A-PJ03 / A-PJ07** — 記錄性質，入 RD-1，不阻塞任何批次。

### RD-1 累積項目

Phase 2 結束時，RD-1 已累積下列各項（皆為「來源未明述、不得自行指認」）：

| 來源 | 內容 | 影響列／leaf |
|---|---|---|
| R-P9 / A-PJ03 | `$HCP_DISP2.Est_Range_BEV$` 無 LID 對映，三候選不等價 | 2 列 |
| 補裁 #2 / A-PJ20 | row 441 的 refresh rate 60 Hz 由誰驗 | 1 列 |
| 補裁 #3 / A-PJ21 | row 443 的無名測項身分 | 1 列 |
| 補裁 #1 / A-PJ19 | RD-1 三列（434 / 435 / 520）的模糊語落在凍結欄位 | 3 列 |
| R-P18 / A-PJ16 | CFTS025 需求本文 | 24 列 + leaf 146 |
| A-PJ01 | 兩份 037 內容互異（VC 171/171、description 105/171） | 全域 |
| A-PJ07 | SWC 簿欄位錯置（跨 feature，不處置） | 0 |

**一條貫穿的先例**：R-P9 → R-P18 → 補裁 #2 → 補裁 #3，四次都是同一個判準 ——
**候選不唯一即不選，該列維持不動並入 RD-1**。這條線現在夠穩，Phase 4 遇到同型
情形可直接援用，不必逐次上呈。

### 分析層規則缺陷（兩條，不合併）

| ID | 缺陷 | 偵測時機 |
|---|---|---|
| A-PJ19 | R-P12 的列號混用實體列號與 tc_id 兩種慣例 | 執行時比對實測發現 |
| A-PJ22 | 下放包 §6.1（要三項資訊）與 §6.2（禁執行測項）互斥 | 執行時觸及界線發現 |

兩條都是**下放前可判定、卻等到執行時才浮現**的規則衝突。共同的預防形式：
下放包成形時檢查「所求資訊是否落在所授權路徑的可達範圍內」、以及「同一份
文件內的列號／識別碼是否採單一慣例」。
