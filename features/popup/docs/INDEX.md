# Popup — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-27（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-27 | Phase 0 intake → `sources/` 落檔 → scaffold → Phase 1 RECON → 工作簿起建 | [handoff/01_intake_recon.md](handoff/01_intake_recon.md) | [upstream/01_intake_recon.md](upstream/01_intake_recon.md) | （無新條文；R-POP1~R-POP5 為下放包同包新立） | A-POP1 ~ A-POP4 | **PASS（作業面 6/6）；4 項待裁已由 R-POP6~R-POP11 處分，見 §2** |
| 02 | 2026-08-27 | P2 簽署 → R-POP11／R-POP10／R-POP9 工具三支 → 值來源接線 → **Pilot 全量批** | [handoff/02_wiring_tooling_pilot.md](handoff/02_wiring_tooling_pilot.md) | [upstream/02_wiring_tooling_pilot.md](upstream/02_wiring_tooling_pilot.md) | （無新條文；R-POP6~R-POP11 為前一輪覆核所立） | A-POP5 ~ A-POP8 | **4 條 TC，lint 21 項全 0**；`-002-05` 觸發 §八 升級停下 |
| 03 | 2026-08-28 | pilot 六件修正（R-POP15 F1~F6）→ TC ID 重排（R-POP13）→ `-002-05` 補生成（R-POP14）→ 工具二修（R-POP16 乙丙／R-POP17-2）→ 台帳一致性 | [handoff/03_pilot_fixes.md](handoff/03_pilot_fixes.md) | [upstream/03_pilot_fixes.md](upstream/03_pilot_fixes.md) | （無新條文；R-POP12~R-POP17 為前一輪覆核所立） | A-POP10、A-POP11 | **5 條 TC 齊，lint 21 項全 0，x14 DV 存活**；`rulings_hash` 轉綠（既有列 sha 變動 0）；§十升級條件命中 1 項（sxm 兩筆假陽性，未代改）|
| 04 | 2026-08-28 | F7 回調（R-POP20）→ 主表辨識改內容判準（R-POP18）→ A-POP6 甲類訂正（R-POP19）→ 台帳收斂 ＋ 03 §十三 逐項複驗 | [handoff/04_f7_ledger_close.md](handoff/04_f7_ledger_close.md) | [upstream/04_f7_ledger_close.md](upstream/04_f7_ledger_close.md) | （無新條文；R-POP18~R-POP20 新立、R-POP13／R-POP15 修訂，皆分析層本輪落檔） | （無新登）—— A-POP10／A-POP11 於本輪結案 | **五條 Final Step 全 ≤ 18 words 且全含 check that，ER 一字未減**；判準回收 74 筆漏檢（sxm 4／audio_mgmt 7／projection 63 → 0），新浮現 3 筆真缺陷已只造清單（vehicle_setting 31 項未複驗未寫入，回報）；升級條件 5 項全未命中；`gates_tsv` 由綠轉紅屬他 feature 未登錄之新腳本 |
| 05 | 2026-08-28 | 交付候選簿產出 → TestRail 空表 → `DELIVERY_NOTE.md` → **R-POP25 第 3 點：兩件 Pop Up 補登 `forms/FORMS.md`**（Pei 附加，不另開包） | [handoff/05_delivery_prep.md](handoff/05_delivery_prep.md) | [upstream/05_delivery_prep.md](upstream/05_delivery_prep.md) | （無新條文；R-POP21~R-POP25 新立、R-POP5／13／18／20 修訂，皆分析層本輪落檔） | （無新登）—— 本包未開任何 anomaly／DR | **交付候選已出**（sha256 `dc0963d7…`，與 sandbox 版位元相同）；15 項回讀複驗全符、lint 21 項全 0、x14 DV 存活；`canon_refs` **本包 +0**；§八升級條件命中 1 項（R-POP5／R-POP13 之 sha，成因已逐條具名，未停下）|

## 2. 上繳包 01 之覆核結果（Pei，2026-08-27）

分析層於本包上繳後落 **R-POP6 ～ R-POP11**（全文見 `features/popup/RULINGS.md`，
R-G13：引用者自 repo 讀原文）。四件 anomaly 全數處分：

| anomaly | 處分 | 條 |
|---|---|---|
| A-POP2 甲 | `forms/Pop Up List HMI R1 (26PI).xlsx` **納入素材**，引用原位不搬；**DR-POP1 結案** | R-POP6 |
| A-POP2 乙 | Priority Matrix（SR24 1A）**不納入**；DR-POP2 保持開啟，改記「repo 存舊版，向上游索 SR24 Post 2A 現版」 | R-POP7 |
| A-POP3 | 採甲案：`-002-02` 之 spec_reference **併列 `_5.5`＋`_5.6`** 兩行；其餘 leaf 單行 `_5.6` | R-POP8 |
| A-POP1 | **追認**修正；另派傳染性掃描（抽取類腳本之同型名稱正規化函式）入 02 包 backlog | R-POP9 |
| A-POP4 | `lint_docs036.py` 跳號前綴改**自動抽取**（非硬寫加 POP），須以注入跳號實證轉紅 | R-POP10 |
| （本包 §七）| `rulings_hash.py` 預設範圍納 `features/*/RULINGS.md`，重產 `RULINGS.sha.tsv`，invariant：既有 R-G 條 sha 不得因擴範圍而變 | R-POP11 |

R-POP10／R-POP11 標「全域效力之工具政策，候升格 R-G」。

## 3. 上繳包 01 待辦七項之結案對帳（下放包 02 執行）

| # | 事項 | 依據 | 現況 |
|---|---|---|---|
| 1 | `paths.popup_list` 指向 Pop Up List | R-POP6 | **完** —— glob 自 feature 目錄實測命中 1 |
| 2 | DR-POP1 結案、DR-POP2 改措辭 | R-POP6／R-POP7 | **完**（分析層已改，執行層另附回報段）|
| 3 | `spec_reference` 併列規則落實 | R-POP8 | **完** —— `newR1L-POP-002` 之 N 欄兩行，回讀實測 |
| 4 | sanitizer 傳染性掃描 | R-POP9 | **完** —— D1∧D2 於 `scripts/` 僅 1 支（已修），範圍外 0 |
| 5 | lint 前綴自動抽取 ＋ 注入轉紅實證 | R-POP10 | **完** —— 迴歸兩向實跑；副作用登 A-POP6 |
| 6 | `rulings_hash` 擴範圍 ＋ invariant | R-POP11 | **完** —— 246→548 列，既有列 sha 變動 **0** |
| 7 | `sources/` 版控條文之 R- 取號 | Pei 2026-08-27 口裁 | **未** —— 待分析層取號 |

## 3b. 下一包（03）待辦

| # | 事項 | 待誰 |
|---|---|---|
| 1 | A-POP8 三提案擇一 → `-002-05` 之第 5 條 TC | Pei |
| 2 | A-POP7 → hard-button 分支是否併入 RD-1、是否補第 6 條 TC | Pei |
| 3 | A-POP6 → `編號重複` 與前綴抽取之判準精修範圍 | Pei |
| 4 | Priority P1／P0、Estimated Test Time 欄之政策 | Pei |
| 5 | pilot review（唯一人工閘，無 done region 可仲裁）| Pei |
| 6 | `sources/` 版控條文取號 | 分析層 |

## 3c. 下放包 03 待辦六項之結案對帳（上繳包 03）

| # | 事項 | 待誰 | 現況 |
|---|---|---|---|
| 1 | A-POP8 三提案擇一 → `-002-05` 之第 5 條 TC | Pei | **完** —— R-POP14 採乙案改良，`NR1L-Popup-005` 已生成（不引 PU、不落 PENDING）|
| 2 | A-POP7 → hard-button 分支是否併入 RD-1 | Pei | **完** —— R-POP12 判不拆、不開 DR；語料 reasoning 已改寫（F6）|
| 3 | A-POP6 → 判準精修範圍 | Pei | **完（但生 A-POP10／A-POP11）** —— R-POP16 乙丙已落實，實測顯示「首個表格」判準另丟掉真陽性 |
| 4 | Priority P1／P0、Estimated Test Time 欄之政策 | Pei | **未** —— Q 欄本包未寫入 |
| 5 | pilot review（唯一人工閘）| Pei | **未** |
| 6 | `sources/` 版控條文取號 | 分析層 | **未** |

## 3d. 下放包 04 之結案對帳（上繳包 04）

| # | 事項 | 現況 |
|---|---|---|
| §二 | F7 回調（R-POP20）| **完** —— 31/19/29/29/17 → 16/17/16/16/17，皆 ≤ 18 且皆含 `check that`；ER 五條全同前輪 |
| §三 | 判準改內容判準（R-POP18）| **完** —— 迴歸四向全過；(d) 回收 74 筆；測試 23 → 29 支全綠 |
| §三-(d) | 回收後之新缺陷只造清單 | **完** —— audio_mgmt `A-AM12`、projection `A-PJ46`／`A-PJ06` 入其 BACKLOG；**vehicle_setting 31 項未複驗未寫入，回報** |
| §四 | A-POP6 甲類訂正（R-POP19）| **完** —— 三數並陳、sxm 一列劃線保留；A-POP10／11 主表與明細節同步 RESOLVED |
| §五 | `ledger_xref` 處置 | **完** —— 追認、未接入 gate_all、續用 `--feature popup`（PASS）|
| §六 | 03 §十三 複驗 | **完** —— 12 項逐項複驗，**僅第 9 項失準**，無第二項；歷史文未改 |
| §七 | 寫回與 gate | **完** —— x14 DV 存活、lint036 21 項全 0、tsv 新增 3／變動 2／其餘 0 |

## 3e. 下放包 05 之結案對帳（上繳包 05）

| # | 事項 | 現況 |
|---|---|---|
| §二 | 交付簿產出 | **完** —— `features/popup/output/…_SWQT_Popup_20260828.xlsx`；產出前 `list_directory` 實測為空，未觸發覆寫升級條件；15 項回讀複驗全符 |
| §三 | TestRail 對映表 | **完** —— 空表加說明（BLANK 起建，五條皆 NEW，E 欄待建號回填）|
| §四 | `DELIVERY_NOTE.md` | **完** —— 五項必載齊；§3 之 queue／priority 範圍缺口以引言塊醒目上報（R-POP2）|
| §五 | gate 與複驗 | **完** —— lint036 21 項全 0、`ledger_xref` PASS、tsv 重產；`gates_tsv`／`lint_paths` 之紅為 driver_distraction，非本包 |
| — | **R-POP25 第 3 點（Pei 附加）** | **完** —— 兩件 Pop Up 已補登 `forms/FORMS.md`；另 3 件未登錄者具名回報，未代登 |

## 4. 仍未結（2026-08-28 逐項複驗後重寫，非沿用）

| 項 | 內容 | 待誰 |
|---|---|---|
| 交付候選 | `output/…_SWQT_Popup_20260828.xlsx`（sha256 `dc0963d7…`）之**人工抽查** —— 上繳包 05 之唯一出口 | Pei |
| tsv | R-POP5／R-POP13 之額外 sha 變動，執行層判「成因具名而未停下」（上繳包 05 §六-2）| Pei（得否決）|
| `forms/` | 另 3 件未登錄（HMI Settings List／Market Configuration Table／Default Settings），R-POP25 第 3 點未竟之部分 | 各該 feature 之首個採用者 |
| E 欄 | TestRail 建號後之回填時點與負責人 | Pei |
| DR-POP2／3／4 | 已登記，未送出；皆不阻斷交付，已載於 `DELIVERY_NOTE.md` §4 | Pei（Tier 3）|

**已結，自本表移除**（附結案依據，供追溯）：

| 原項 | 結案 |
|---|---|
| R-POP5 [DEFAULT] 待追認 | **Pei 追認 2026-08-28**（R-POP5 現行文之「追認」段）|
| `DECISIONS.md` 未簽 | **實測已簽** —— `Reviewed by: PeiPYHsu  Date: 2026-08-27`；§6 兩筆 `[PEI 2026-08-27]` 已回填（上繳包 04 §六）|
| `-002-05` 之 design_method | R-POP23 —— 維持狀態轉換 |
| `ledger_xref` 合併／接入 | R-POP24 —— 不合併、不接入 `gate_all.py` |
| Q 欄政策 | R-POP22 —— 留空（875/875 實測）|
| `forms/` 落點政策 | R-POP25 —— 承認現狀、補登記，不搬檔 |
| **交付產物是否入 git** | **Pei 口裁 2026-08-28：不入 git，維持現狀**（`features/popup/.gitignore` 之 `output/` 不動）。連帶：交付簿之唯一入庫紀錄為其 sha256（`DELIVERY_NOTE.md` §6、上繳包 05 §二-2／§六 三處）；檔案遺失只能以 `scripts/gen_delivery.py` 自 `sandbox/pilot01/` 重產，重產物之 sha256 須與該值相等。**待分析層取 R- 號** |

**純他 feature，不入本表**：vehicle_setting 31 項、`gates_tsv` 之
driver_distraction 未登錄（連帶使 `test_gates_tsv::test_check_detects_drift`
轉紅）、`lint_paths` 之 driver_distraction 在製品、`media` 之 G-D 盲區、
`R-DD6` 同號兩體、tsv 內 14 列 R-DD 之未凍結狀態。
