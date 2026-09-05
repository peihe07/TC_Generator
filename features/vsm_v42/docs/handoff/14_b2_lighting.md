# 下放包 14 — vsm_v42：b2-3 生成 —— Lighting（11 leaf，R-VL25(a) 序）

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–13，取 14
台帳不重生；DR 不送。凍結件（b1／b2-PS 修訂後／b2-Camera）不動；`delivered/` 不動（出貨模式 A／C 待 Pei，裁前交付凍於 b1 舊件）。

## 一、契約

全同 13 包（Camera）契約，含 4.4 補強後之預檢全判準（J 含 test_item 上下半、R 含單 and 型）。D 欄 SWE ID／C 概念留空；spec_reference 章節號單錨（無標題家族若有，依 R-VL19(b) 雙錨）。VAL_ 缺值遇則記 `lint_p_waivers_b2.tsv`（現 0 列）。

## 二、本批

1. 母體：`leaves.tsv` 之 `test_set = Lighting` **11 列**（實測家族組成與 leaf 序回報；若含 Heading 型誤標列，照 -063 之 BLOCKED 先例寫列不剔除並列 §K）。
2. 規格節依 framework Layer 3 分切；訊號 v3＋val_tables；內部形 UI／PROXI 或 `PENDING: DR-VL4`。
3. 輸出 `generated/b2_lighting/`；E38–E45／E56（11/11）／E86 型。
4. **累積簿寫回**：本批覆核通過前**不寫**；分析層覆核後之下包併 b2-Camera＋b2-Lighting 一次寫累積簿（省 surgical 次數）。

## 三、上繳（`docs/upstream/15_b2_lighting.md`；取號續 14 後）

同 13 包結構；§K 不猜；獨立判斷；gate_all 歸因一句式。**綠色通道計數第 2 批（承 Camera 1/3）。**
