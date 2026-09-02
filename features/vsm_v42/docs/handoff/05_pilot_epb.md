# 下放包 05 — vsm_v42：P4/P5 pilot —— EPB Maintenance Mode（17 leaf）TC 生成

日期：2026-09-02
取號：`docs/handoff/` 實測有 00–04，取 05
對象：執行層。00–04 包續有效。sha8 報 body_sha8；台帳不重生；DR 一律不送。
授權：R-VL20（Pei「皆授權」）—— DECISIONS 已簽（照案成立），P4 開跑。
**本包產出止於 `generated/`（文字形）；不寫工作簿、不寫 delivered/**（R-VL20：寫回待分析層覆核與 Pei 再授權）。

---

## 零、禁區（00 包 §零續有效，加）

1. 不寫 `sandbox/base/` 副本（連 read-write 開啟都不得；讀用 `read_only=True`）。
2. 不生成 pilot 家族以外之任何 TC。
3. `reasoning` 以外之工作簿欄位一律 English only（IN §1）；`reasoning` 繁中。
4. 遇規格語意不明：不臆測，該列 `PENDING` 或列 §K，不得補洞（IN §8.4.1）。

## 一、素材（全部既有，本包不新增來源）

| 件 | 用途 |
|---|---|
| 規格 `1.11.1.1.19 EPB Maintenance Mode` 節（`sources/extracted/vf665_v42_spec_r6/document_paragraphs.tsv` 依 W-8 標題索引切出；含其下全部子段） | 需求原文（test_item 上半、行為） |
| `data/leaves.tsv` 之 `test_set = EPB Maintenance Mode` 17 列 | 母體（req_id＝`SWE-Requirement ID`，D 欄值＝`Source Requirement ID`） |
| 兩份 037 之該 17 列 `Requirement Description` | RD 分解單位（IN §8.2：不得再分解、不得合併） |
| `data/signal_chain_v42_v3.tsv`（現行）＋ `data/val_tables_v42.tsv` | 訊號實名與 `<label>`（R-VL14(d)） |
| `docs/runtime/profiles/FW036_R1L_VSM_V42_Profile.md` | 本線綁定（讀，不寫） |
| `framework.md` | Test Group／Test Set／Layer 3 |

## 二、作業清單

**W-0 GenSigSendType 列舉查證（R-VL18(c)）**：兩本 ATL-Mi DBC 之 `BA_DEF_ … "GenSigSendType"` 列舉逐字取；查得則上繳列舉表，查無則記「查無」，Procedure 一律只依規格行為書寫，不依 SendType。

**W-1 規格節切出**：依標題索引切 `1.11.1.1.19` 全節（起：該標題段；迄：下一同級標題前）；落 `data/pilot_epb_spec.md`（段落逐字，含段號）。17 leaf 逐一對映至節內段落（`req_id → 段號`），對映不上者列出（不硬配）。

**W-2 TC 生成（本包主體）** —— 逐 leaf，依 IN §2–§13 全文＋profile：
- 每 leaf 產出一組 JSON（IN §10.1 十鍵＋`reasoning`；`tcs.length` 依 §8.2.2／§8.3 得 ≥1，split 依據入 `reasoning` 與 `split_reason`）。
- **`test_item` 兩段式（R-S4，硬規則）**：上半 = 需求原句 verbatim（≤50 token，R-3）；下半 = `(...)` 測試目的獨立成行；同 Requirement ID 衍生多列之括號下半不得逐字相同。
- 訊號書寫：v3 之「解得」列寫 `$MESSAGE.Signal$ = <raw> (<label>)`，`<label>` 逐字取 `val_tables_v42.tsv`；`Country_Code` 型無 VAL_ 者寫 `= <raw>` 並於 Remarks 註「DBC 無 VAL_」。內部形未解者：可依 R-P375(b) 走 UI（HMI Settings List 錨點）／PROXI 者走之；否則 `PENDING: DR-VL4 <名>`。R-13／拼字疑誤列保留原名不加 `$`。
- `pre_conditions` 只收狀態（IN §4.4）；PROXI 入 Pre-Condition、UI 操作入 Procedure（R-P375(b)）；`input_test_data` 一律 `NA`（profile 6）。
- `spec_reference`：R-VL19 —— `Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.19`（一號一行；leaf 另涉他節者升冪加列）。
- 格式：無尾句號（含 a./b./c. 子項）、UI 標籤 `"..."`（IN §11）；ER 無 modal（IN §6）；Design Method 依 §12 末定；Priority 依 §10.2。
- 輸出：`generated/b1_epb/{req_id}.md`（人讀形，欄位分節）＋ `generated/b1_epb/{req_id}.json`；另彙總 `generated/b1_epb/INDEX.md`（req_id｜TC 數｜tc_title 清單｜PENDING 數）。

**W-3 自檢與 lint**：逐 TC 過 IN §9 十七項自檢，結果表入 INDEX.md；`lint036.py --profile vsm_v42` 對 b1 輸出跑（可跑則附輸出；不支援 generated/ 文字形則記明並以自檢表代）。

**W-4 sibling／duplicate**：同家族 17 leaf 互為 sibling 候選（IN §4.1.4-2）；每 TC 之 `distinguishing_axis` 依 §4.6 出。

## 三、預期數字

| # | 項 | 判準 |
|---|---|---|
| E38 | 覆蓋 | 17／17 leaf 各 ≥1 TC；無 leaf 落空 |
| E39 | R-S4 括號下半 | 每 TC 有；同 req_id 內不逐字相同（違者 = FAIL 不得上繳） |
| E40 | 尾句號違規 | 0（四欄逐 item 掃） |
| E41 | `[...]`／`'...'`／`<...>` UI 標籤 | 0 |
| E42 | `$…$` 之列 | 全數可回溯 v3「解得」；非解得列出現 `$` = 0 |
| E43 | PENDING 格式 | 全為 `PENDING: DR-VL4 <名>`（或 DR-VL2 型），無裸空欄 |
| E44 | reasoning | 每 req_id 一則，繁中 2–5 句，含切分依據（§10.4） |
| E45 | modal 於 ER／test_item | 0 |

## 四、上繳要求（`docs/upstream/05_pilot_epb.md`）

W-0 列舉表；W-1 對映表與未對映清單；b1 全量產出清單與 TC 總數；E38–E45 逐項；§9 自檢彙總（17 項 × TC 數之未過清單，全過亦列）；PENDING 清單（名／DR 錨）；§K（規格語意不明處）；獨立判斷；gate_all 歸因。

## 五、升級條件

E39 任一 FAIL；E42 ≠ 0；W-1 對映不上之 leaf > 3；規格節內出現本線值域外之訊號形（回報不自創值域）。

## 六、未結 DR 清單

DR-VL1／DR-VL2／DR-VL4（皆 Pei 裁先不送；DR-VL4 為 PENDING 錨）。DR-VL3 結案。
