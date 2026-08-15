# 25 — Comfort HMI / 列高裁定、pilot 定案、寫回下放

- 產出層：分析層｜2026-08-15｜對象：執行層
- 裁定：Pei，2026-08-15（列高第二半之提問，答「沒有」）
- 承接：下放包 24（同一次覆核，拆檔）

---

## 1. 列高 —— 採方向 3（維持現狀）

23 §2 之判定規則首項為「既有交付件同樣受限**且未見客戶反映**」。

- **前半（可證）**：執行層實測 —— Privacy 與 Comfort 同用空白範本
  `SWQT_20260121`，兩者皆 `customHeight=True, height=14.0` 且
  `wrapText=True`；Privacy 之受限檔即其實際交付件（`DELIVERY.sha256`
  ENTRY 003 標「已交付」，hash 與量測對象逐位元組相符）。
  home／SXM 起自已調版之 instance，不構成反例。
- **後半（repo 外）**：Pei 2026-08-15 答**「沒有」** ——
  Privacy 交付件交出後，評閱方未曾就列高／內容需點選儲存格方能閱讀
  提出意見。

**判定規則兩半皆滿足 → 採方向 3。**

不改動範本之列高、不清除 `customHeight`、不逐列設定顯式高度。

依據（不對稱錯誤成本）：方向 1／2 改動範本呈現，影響及於日後所有 feature，
而本案無支撐該擴大之證據；方向 3 之代價為一項已知、已記錄、且有同範本
已交付前例之可讀性損失。

**R-C27 已消除其中最嚴重的一段**：BLOCKED row 之 Remarks 首行現為
`[BLOCKED-SPEC] Owner: …`，marker 與擁有者皆在可見範圍內。餘留者為長
procedure／ER 之列表視圖只見首行，儲存格值完整、點選即見。

**A-CF16 由 PENDING 轉 RESOLVED**，處置記為「方向 3，Pei 2026-08-15
裁定；同範本前例為 Privacy 交付件」。條目須同時載明**未來若評閱方提出
意見，本裁定即需重審** —— 它成立於一個當下為真的事實，非永久性質。

---

## 2. pilot 內容定案

14 條（12 條 TC ＋ 2 條 `[BLOCKED-SPEC]` row）**內容定案**，
非因寫回而生之問題不再改動。

歷次 defect 共 6 項，逐項已修：單步 procedure（§10.5）、`duplicate_of`
誤用（§10.6）、PC 落點 ×3（§4.5／§4.4）、PC 出處 ×1（§7 FF）、
ER 主詞 ×2 輪（§6／§5.6）、Remarks 順序（R-C27）。

lint 由 25 gate 增至 32。**新增之 7 個當時皆為實際違反**，非預防性補強：
`required-keys`（14 條全缺 split_flag／split_reason）、`reasoning-sentences`
（7 份全超長）、`proc-min-steps`（TC-004）、`duplicate-of-format`
（值本身違反 digits-only）、`blocked-row-empty`、`blocked-remarks`、
`marker-whitelist`。

---

## 3. 寫回下放 —— 執行 splice，止於 Excel 確認前

授權執行 write-back。**分三段，逐段驗，不合併。**

### 3.1 前置 gate（任一不過即停，不進 3.2）

1. `BASELINE.sha256` 8 檔全數 `shasum -c` OK
2. `DELIVERY.sha256` `--ignore-missing` OK，且仍為 2 筆（無 ENTRY 002）
3. 來源檔為 `output/…_Comfort_20260815_prepared.xlsx`，
   SHA256 `b68117a211b08009…` 相符（**A-CF07 經 Pei 於 Excel 確認之
   同一份位元組**；不符即停）
4. lint 32/32 PASS

### 3.2 splice

- 唯一寫入路徑 `backend/xlsx_surgical.py`（R18-3；**四個既有 feature 之
  `write_back.py` 為隔離品，不得作為起點**，R20-5）
- 目標列 **row 10–23**，append from first data row
- **B 欄不寫入** —— 其公式 `=IF(ISBLANK($D10),"",ROW()-9)` 自動編號 1–14
- 留白欄依 dry-run 之具名清單留白，不填 `NA` 以外之佔位
- 產出新檔於 `output/`，**不覆寫** prepared 檔

### 3.3 寫回後之 assertion（自產出檔讀回，非自記憶體）

以 PASS/FAIL ＋ 實測值輸出：

1. zip member 數與來源相同；差異僅限預期之 sheet xml
2. DV counts 與來源相同（`sheet5`／`sheet6` 各自之 (n,m)）
3. row 10–23 之 14 列，逐列比對其 D／F／G／H／I／J／K／L／M／N／P／R 之值
   與生成之 JSON 一致
4. Q／S／T–Z／AH 之留白與 `NA` 依 profile §3.7／§3.8／§3.9
5. **B 欄 row 10–23 之公式存在且未被值取代**
6. 兩個 BLOCKED row 之 L／M 為**空**（非空白字元），Remarks 首 60 字元
   含 `Owner:`
7. row 24 起無殘留內容

### 3.4 台帳

`DELIVERY.sha256` 增 **ENTRY 002**（append-only，不改 ENTRY 001）：
操作、來源 hash、產出 hash、目標列範圍、TC 數（14，含 2 BLOCKED row）、
**狀態記「未經 Excel 確認」**。

### 3.5 停下

**Excel 四項確認由 Pei 執行**（profile §0.1，同 A-CF07 前例）：
無修復提示、R 欄下拉九項可用、D5 Scope 正確、row 10–23 內容與編號正確。

**程式層檢查不能代替 Excel 自身之檔案完整性判定。** 執行層產出檔案後停下。

### 3.6 不做

- **不複製至客戶交付路徑**（`10_Reviewing/…/ComfortHMI/`）——
  交付形式、位置、送達屬 Tier 3，Pei 於 Excel 確認後另裁
- 不動 prepared 檔；不改 ENTRY 001；不執行 git

---

## 4. 上繳

`docs/upstream/16_writeback.md`，含 3.1／3.3 之全部 assertion 結果、
產出檔 hash、ENTRY 002 內容，及「本包是否仍有該驗而未驗者」之獨立判斷。

---

## 5. 本包產生之新條文清單（自檢）

無新條文。§1 為裁定與 anomaly 狀態變更，§3 為作業授權。
