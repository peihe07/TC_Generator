# 下放包 15 — vsm_v43：寫回 dry-run（54 TC，R-VT27(e)）

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–13，取 15（14 為無下放包作業佔用，K-22）
台帳不重生（已重生，PASS）；DR 不代發；**寫入僅限 `sandbox/wb_trial/` 與 `data/`**；`sandbox/base/` 一位元不動；`delivered/` 不建（重錨前不得交付，R-VT18(c)）。

## 一、W 清單

**W-0 微修**：-433／-438 之 reasoning 各補一句（規格 para 539／553 誤寫 Sensibility、ER 依該節實際訊號 LDW_Intensity 之揭露，R-VT27(a)）；json＋md 同步；E56 重跑該二列。

**W-1 writeback_map 建檔**：`data/writeback_map_v43_interim.tsv` —— 54 列（b1 Ambient 11＋FCW 15＋SDW 10＋LDW 18），列序依 `leaves_interim_v2.tsv` 表序；TC ID `NR1L-VSM43-001` 起依列位；D 欄 Sys-RA 實名；C 概念留空；Q／AB／車型欄留空、S = NA、E 留空（R-VT27(e)）；Remarks 含 Provisional 句（R-VT18(c)）。欄映射逐欄列（沿 V42 `writeback_map_b1.tsv` 型，`feature.yaml` columns 對照）。

**W-2 trial 出件**：`sandbox/base/` 副本 → openpyxl 計算層填 54 列 → `surgical_save` → `sandbox/wb_trial/trial_v43_54.xlsx`；三斷言（x14 逐字、member 集、differing 僅目標分頁）＋全格回讀比對 JSON（不符 0 為要件）。

**W-3 lint 實跑**：`lint036.py trial_v43_54.xlsx --profile vsm_v43`（profile 無則以無 profile 跑並記明）；輸出全文；**逐紅三分歸因**（工法產物／判準假設／內容缺陷——內容缺陷逐列引出交裁，不自修：三批已凍）。VAL_ 缺值型 P 紅若現，起 `data/lint_p_waivers_v43.tsv` 對銷（要件：remarks 已揭露）。

**W-4 「資料檔＝條文」斷言首跑**（R-VT27(b)）：Layer 2 十九組名／status 四類／`test_set` 值域逐項對條文（R-VT23(d)／R-VT24）斷言，全等回報。

## 二、E

| # | 項 | 判準 |
|---|---|---|
| E89v | W-0 | 2 列 reasoning 補句；其餘 106 檔 diff = 0 |
| E90v | 回讀 | 54 列全格不符 0；三斷言 True |
| E91v | lint | 全文＋逐紅三分；內容缺陷數（0 則綠色通道連跑即可啟動） |
| E92v | 斷言首跑 | 全等；不等者逐項列 |
| E93v | 禁區 | base sha 不變；三批凍結件除 W-0 二列外 cmp 0 |

## 三、上繳（`docs/upstream/15_dryrun.md`）

E89v–E93v；lint 全文；map 全欄；獨立判斷；gate_all 歸因一句式。**E91v 內容缺陷 = 0 → 綠色通道連跑生效，b2-4 EPB Maintenance Mode 19 leaf 起自動連跑（一批一上繳，彙報式覆核；任何缺陷即停並重置計數）。**
