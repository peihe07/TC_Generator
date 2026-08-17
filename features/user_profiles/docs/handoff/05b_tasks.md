# 05b 下放包 — 作業指示（執行層）

裁決見 `05a_rulings.md`（R-U21～R-U24、R-G7）。04 輪核可，無退回項。

## 作業

1. **條文入庫** — R-U21～R-U24、R-G7 逐字追加於 `RULINGS.md`；
   R-G7 併入全域條文段。

2. **R-U24 跨 feature 掃描（唯讀，先辦）** —
   對 `comfort`／`sxm`／`amfm`／`projection` 之
   `data/spec_id_to_outline.tsv` 讀欄名、列數、第一欄形態，
   判斷其為 build_outline_map 形態（spec 側索引）或 recon 形態
   （037 leaf 對映）或第三種。
   **唯讀，不得寫入他 feature 任何檔。** 發現污染者逐一具名，處置另裁。
   本項優先於其餘作業：若已有 feature 帶著 §7.2 之錯答案，
   愈早知道愈好。

3. **R-U24 home 實跑驗證（repo 外複本）** —
   複製 `features/home` 全樹至 tempfile 目錄，於複本上跑改名後之
   `recon.py`，確認兩讀者（`lint_tcs.py`、`make_batch_context.py`）
   仍正常。**不得對 repo 內之 home 執行任何寫入。**
   複本用完即刪。04 包 §7.2 之危害係推導所得，本項是要把它變成觀察。

4. **R-U23 圖片抽取能力** — 自 spec xlsx 試抽 `8.2` 之內嵌圖
   （zipfile → `xl/media/`，並比對 drawing 關聯以定位該節之圖）。
   抽得出且可判讀 → 記其內容摘要，不開 DR；
   抽不出或判讀不能 → 具名列 DR 候選。
   同法施於部分依賴 5 節（4.6、6.2、9.1、10.2、11.4），逐節具名結果。
   **本項之結論直接改寫 04 包 §6 之分類**，若分類有變請明列前後對照。

5. **R-U22 PLP 表可讀性** — 讀 spec `3.1`–`3.5` 之 Description 全文，
   回報：是否為文字、是否含 `(image:` 標記、可讀出之偏好項數。
   可讀 → 一併回報偏好清單（供 PROF-001-01 之 TC 使用）；
   不可讀 → 列 DR 候選。
   **並據此重估 A-UP02**：其為「spec 有而 SWE 未涵蓋」或
   「內容不存在」，兩者處置不同（R-U22）。

6. **framework.md 起草** — Layer 1 = `User Profiles`；
   Layer 2 = R-U20 之八組（逐字，含各組 leaf 數）；
   Layer 3 = spec 章 4–14 之對映。
   生成集合以 **133**（R-U19）為分母，並具名其與 135 之別。
   **草案即可，定稿待覆核**。

## 不在本包授權範圍

- 刪除 `inputs/` 之 spec 副本（R-U17，屬 Pei）
- 對他 feature 之任何寫入（R-U24 唯讀）
- 任何 git 操作，含 checkout／restore／stash／clean（R-G5）
- spec 4.1.1 相關之 TC 生成（R-U15）
- 寫回實作（R-U14：x14 DV gate 未立前不得開工）
- TC 生成本身 —— 本輪仍為 Phase 1

## 上繳

`docs/upstream/05_framework_draft.md`，更新 `docs/INDEX.md`，
附「本包是否仍有該驗而未驗者」之獨立判斷，每個數字標明量測條件。
動作清單須與 git 陳述逐項對得起來，唯讀與改狀態之 git 分列（R-G6）。

## 承前之未決

- **A-UP09 / R-U14** —— x14 DV gate 仍未立，寫回不得開工
- **DR #4**（PU1087／PU1088）—— 阻斷 spec 4.1.1（R-U15）
- **DR #3**（A-UP02 之 8 條 → RD-1）—— 其性質可能因作業 5 而改變
- **R-U17** —— `inputs/` spec 副本之刪除待 Pei 執行
