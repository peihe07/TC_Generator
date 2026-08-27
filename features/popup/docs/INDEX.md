# Popup — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-27（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-27 | Phase 0 intake → `sources/` 落檔 → scaffold → Phase 1 RECON → 工作簿起建 | [handoff/01_intake_recon.md](handoff/01_intake_recon.md) | [upstream/01_intake_recon.md](upstream/01_intake_recon.md) | （無新條文；R-POP1~R-POP5 為下放包同包新立） | A-POP1 ~ A-POP4 | **PASS（作業面 6/6）；4 項待裁已由 R-POP6~R-POP11 處分，見 §2** |

## 2. 覆核結果（Pei，2026-08-27，上繳包 01 之後）

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

## 3. 下一包（02）待辦 —— 本包未做，逐項列明

| # | 事項 | 依據 | 現況 |
|---|---|---|---|
| 1 | `feature.yaml` 之 `paths.popup_list` 指向 `forms/Pop Up List HMI R1 (26PI).xlsx` | R-POP6 | **仍為 `null`** —— 本包 commit 之內容早於該裁 |
| 2 | `DATA_REQUESTS.md`：DR-POP1 改結案、DR-POP2 改記新措辭 | R-POP6／R-POP7 | 未改 |
| 3 | `spec_reference_template` 之併列規則落實 | R-POP8 | 未改 |
| 4 | 抽取類腳本之名稱正規化函式傳染性掃描 | R-POP9 | 未做 |
| 5 | `lint_docs036.py` 前綴自動抽取 ＋ 注入跳號之轉紅實證 | R-POP10 | 未做 |
| 6 | `rulings_hash.py` 擴範圍 ＋ 重產 tsv ＋ R-G sha 不變之 invariant | R-POP11 | 未做 |
| 7 | `sources/` 版控條文之 R- 取號（本包已落 `.gitignore`＋`README.md`，條文無號）| Pei 2026-08-27 口裁 | 待分析層取號 |

## 4. 仍未結

| 項 | 內容 | 待誰 |
|---|---|---|
| R-POP5 | Heading 列之台帳處置 [DEFAULT]，待 Pei 追認 | Pei |
| DR-POP2／DR-POP3 | 已登記，未送出 | Pei（Tier 3）|
| `DECISIONS.md` | [PROPOSED]／[PEI] 未裁，Sign-off 未填 —— **P2 未過，P3 以後不得起跑** | Pei |
