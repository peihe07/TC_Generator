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

## 4. 仍未結

| 項 | 內容 | 待誰 |
|---|---|---|
| R-POP5 | Heading 列之台帳處置 [DEFAULT]，待 Pei 追認 | Pei |
| DR-POP2／DR-POP3 | 已登記，未送出 | Pei（Tier 3）|
| `DECISIONS.md` | [PROPOSED]／[PEI] 未裁，Sign-off 未填 —— **P2 未過，P3 以後不得起跑** | Pei |
