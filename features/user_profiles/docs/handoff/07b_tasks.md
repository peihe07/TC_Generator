# 07b 下放包 — 作業指示（執行層）

裁決見 `07a_rulings.md`（R-U31～R-U34、R-G8）。06 輪核可，無退回項。

**本輪之目的：把 2.9% 這個下界變成量值，並把 R-U21 之未量邊補上。**
framework 定稿排在其後。

## 作業

1. **條文入庫** — R-U31～R-U34、R-G8 逐字追加於 `RULINGS.md`；
   R-G8 併全域段。

2. **R-U34 跨頁反向驗證（最優先）**
   取 140 節之 xlsx Description **結尾句**，查其是否出現於 PDF 次頁頁首。
   - 有命中者即為跨頁條款，逐節具名
   - 據此重算掉句率，**三個比率一併重報**，各附其分子定義（R-G8）
   - 本項之對照向（R-G7）：以 PDF 段落自比，差額須全為 0
   本項先辦之理由：其結果會改變 §3 之 13 節殘留分類，
   後續作業若先做會白做。

3. **R-U33 29 個無標籤之節**
   以章節位置定位其 PDF 段落，量有無內容、有無掉句，逐節具名。
   其中章 3 為 PLP 表章、其餘多為章標題 —— 若章標題本無內容，
   標「無內容可比」而非 PASS（canon：不可能失敗者不標 PASS）。

4. **R-U31 之落地（依作業 2／3 之結果）**
   - `outline_map.json` 增 `pdf_text`、`divergence` 兩欄，
     **原 `text` 欄不動**
   - 新建 `data/xlsx_missing_clauses.tsv`：outline／掉句原文／
     查證方式／影響之判讀
   - **全量列 PDF 中 `**` 起首之註記**（現測 10 條），
     逐條標 xlsx 側有無，缺者入補句表
   - 補句表之每一條須標明它影響哪些既有判讀

5. **R-U32 Service 22 條 PDF 複查**
   逐條以 PDF 文字層複查其可觀察端。**不預設維持 R-U21 之結論**。
   分群有變者具名，並列出其 xlsx 側與 PDF 側之差異原文。

6. **重建影響面清點**（06 包 §7 第 5 項）
   即使不重建，補句表與 `pdf_text` 欄之加入仍會影響既有產物。
   清點哪些檔之哪些欄依賴 xlsx 側之文字：
   `expected_cited_sections.tsv` 之 `chars`、`generation_sections.tsv`、
   03 輪之長度分布與圖片參照數（04 包已知會變）。
   **只清點，不改**。

## 不在本包授權範圍

- **整份重建 `outline_map.json`**（R-U31 明文駁回）
- framework 定稿（待本輪結果）
- 寫入 comfort 或任何他 feature 之檔（R-U24／R-U30）
- 刪除 `inputs/` 之 spec 副本（R-U17，屬 Pei）
- 任何 git 操作，含 checkout／restore／stash／clean（R-G5）
- 寫回實作（R-U14：x14 DV gate 未立前不得開工）
- TC 生成本身 —— 本輪仍為 Phase 1

## 上繳

`docs/upstream/07_baseline_audit_2.md`，更新 `docs/INDEX.md`，
附「本包是否仍有該驗而未驗者」之獨立判斷。
**每個比率須附其分子定義（R-G8）**；動作清單須與 git 陳述逐項對得起來，
唯讀與改狀態之 git 分列（R-G6）。

## 承前之未決（不因本包改變）

- **A-UP09 / R-U14** —— x14 DV gate 未立，寫回不得開工
- **R-U17** —— `inputs/` spec 副本之刪除待 Pei 執行
- **DR #3**（上游覆蓋缺口）、**DR #4**（PU1087／1088 之 popup 內文，MEDIUM）
- **永久限制** —— home 之 `lint_tcs` 危害無法觀察（`features/home/inputs/` 已清空）
- **N-XF01** —— comfort 孤兒檔，待 Comfort 下次開輪次
