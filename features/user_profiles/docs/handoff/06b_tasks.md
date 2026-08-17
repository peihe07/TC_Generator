# 06b 下放包 — 作業指示（執行層）

裁決見 `06a_rulings.md`（R-U25～R-U30、R-G4-1）。05 輪核可，無退回項。

**本輪之主軸為 R-U25：把地基量一遍。** framework 定稿排在其後。

## 作業

1. **條文入庫** — R-U25～R-U30、R-G4-1 逐字追加於 `RULINGS.md`。
   R-G4-1 為既有全域條文之修訂，須置於 R-G4 之後並標明其修訂關係，
   **不得逕行改寫 R-G4 原文**（原文之「兩個讀者」是當時的記載，
   保留才看得出漏數發生過）。

2. **R-U25 —— xlsx / PDF 逐節比對（本輪最優先）**
   對 169 條 outline 逐節取 xlsx 之 Description 與 PDF 文字層之對應段落，
   量出並回報：
   - 每節之 xlsx 字元數、PDF 字元數、差額
   - 掉句之**形態**分類：整節缺、句尾截斷、表格未展開、
     圖內文字未計、標點或空白差異（此類不算掉句）
   - 掉句率（節數比與字元比**分列**，不得只報其一）
   - **是否為系統性**：即掉句是否集中於某種節型（表格節／圖節／長節）
   量測條件須自陳：PDF 段落如何定位到 outline、
   多節同頁時如何切分、比對前做了哪些正規化。
   **不得以抽樣代替全量**；169 條全掃。

3. **R-U25 之後續判定（依作業 2 之結果分支）**
   - 掉句率低且非系統性 → outline_map.json 維持，於檔頭記其限制
   - 系統性掉句 → **停手上報**，不自行重建 outline_map.json；
     重建與否、以何為準，屬 Tier 2
   兩種情形皆須逐節列出「其判讀依據為 xlsx 側」之 04／05 輪結論，
   標示哪些會因重建而改變。

4. **R-U29 PLP3 再試** — `pdfimages` 抽 p5 之 11 張點陣圖，
   逐張視覺判讀，定位 PLP3（Memory Seat Module）之列項。
   讀得出 → 回報清單；讀不出 → 具名列 DR 候選，
   並記其嘗試過的方法（供日後不重複試同一條死路）。

5. **R-U26 PU id 擴充** — `spec_popup_ids.tsv` 擴為 32 列，
   加 `source` 欄（`xlsx_text` / `pdf_only`）。
   12 個 pdf_only id 逐一定位所屬 section 並填入。
   原 20 列之記載不刪、不改其判讀來源標示。

6. **R-U27 落地** — 解除 PROF-002-03 之阻斷標記；
   於 `DATA_REQUESTS.md` 將 DR #4 由 HIGH 降為 MEDIUM，
   並改寫其索取標的為「Pop Up List 中 PU1087／PU1088 兩列之 popup 內文」
   （非整份版本）。記明觸發條件已由 spec p6 提供。

7. **R-U28 落地** — `ANOMALIES.md` 之 A-UP02 改記為
   「spec 有而 SWE 未涵蓋」，形態同 Comfort R-C16，
   並分列 3.1–3.5 與 10.1／11.1／11.2 之不同處置。
   `DATA_REQUESTS.md` 之 DR #3 性質改為「上游覆蓋缺口」。

8. **R-U30 登記** — comfort 孤兒檔登記為跨 feature note
   （寫在本 feature 之 ANOMALIES.md，**不寫 comfort**）。

## 不在本包授權範圍

- **framework 定稿**（待 R-U25 之結果，Tier 2）
- 重建 `outline_map.json`（作業 3 之系統性分支須停手上報）
- 寫入 comfort 或任何他 feature 之檔（R-U24／R-U30）
- 刪除 `inputs/` 之 spec 副本（R-U17，屬 Pei）
- 任何 git 操作，含 checkout／restore／stash／clean（R-G5）
- 寫回實作（R-U14：x14 DV gate 未立前不得開工）
- TC 生成本身 —— 本輪仍為 Phase 1

## 上繳

`docs/upstream/06_baseline_audit.md`，更新 `docs/INDEX.md`，
附「本包是否仍有該驗而未驗者」之獨立判斷，每個數字標明量測條件。
動作清單須與 git 陳述逐項對得起來，唯讀與改狀態之 git 分列（R-G6）。

## 承前之未決（不因本包改變）

- **A-UP09 / R-U14** —— x14 DV gate 未立，寫回不得開工
- **R-U17** —— `inputs/` spec 副本之刪除待 Pei 執行
- **永久限制** —— home 之 `lint_tcs` 危害無法觀察
  （需 home 之 037，而 `features/home/inputs/` 於 2026-08-13 清空且未進版控）
- **PLP3、11.4 table CPA2** —— 記載限制，見 05 包 §7
