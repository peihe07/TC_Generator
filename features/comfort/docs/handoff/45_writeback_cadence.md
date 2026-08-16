# 45 — Comfort HMI / 寫回節奏裁定與第二次寫回

- 產出層：分析層｜2026-08-15｜對象：執行層
- 裁定：Pei，2026-08-15（「就依照你的建議」）—— 採分析層 32 §7 之建議：
  **每批寫回**

---

## 1. 裁定

寫回節奏採**每批寫回**（32 §7 之分析層建議）。

理由（該建議之原文）：A-CF19（多節 `specification_reference` 於儲存格之
呈現）與 `write_back.py` 於較大規模之行為皆未實測，**越早遇到越便宜**。

**成本落在 Pei**（每次寫回後之 Excel 四項確認屬 Tier 3），此點於建議時
已明載，裁定即為接受該成本。

---

## 2. 第二次寫回 —— 追平累積

pilot 之 14 條已寫回（`…_pilot.xlsx`，ENTRY 002）。自批次 2 起累積未寫回。

**本次寫回之範圍為全部現存 TC**，而非增量 —— 因既有 TC 於歷次覆核中
多次修改（EMEA PC 移除 11 條、`-019` 補 PC、`-036` 拆條致 30 條順移、
`reasoning` 多輪更新），**`…_pilot.xlsx` 內之 14 列已與現行 JSON 不同**。

故：**自 prepared 檔重新寫入全部 TC**，不在 pilot 檔上追加。

| 項 | 值 |
|---|---|
| 來源 | `output/…_Comfort_20260815_prepared.xlsx`，SHA256 `b68117a2…` |
| 目標列 | row 10 起，連續 |
| TC 數 | 依批次 7 完成後之實際數，**不預填**；上繳包載其實測 |
| 產出 | `output/` 新檔，不覆寫 prepared、不覆寫 pilot 檔 |

`…_pilot.xlsx` **保留不刪** —— `DELIVERY.sha256` ENTRY 002 為其身分記錄，
刪除會使台帳指向不存在之檔（R-C14 之反面：不得使已記錄之身分失去對象）。
其狀態欄增記 `superseded by ENTRY 003`。

---

## 3. 三段作業，逐段驗

### 3.1 前置 gate（任一不過即停）

1. `BASELINE.sha256` 8 檔 `shasum -c` 全 OK
2. `DELIVERY.sha256` `--ignore-missing` OK
3. 來源 prepared 檔 SHA256 相符（**Pei 於 2026-08-15 於 Excel 確認過之
   同一份位元組**）
4. lint 全數 PASS（含批次 7 後之全部 gate）

### 3.2 splice

- 唯一寫入路徑 `backend/xlsx_surgical.py`（R18-3）
- **B 欄不寫入**（公式自動編號）
- 留白欄依 profile §3.7／§3.8／§3.9
- BLOCKED row 與 `[COVERED-BY]` row 之 L／M 為空

### 3.3 寫回後 assertion（自產出檔讀回）

沿用 16 §5 之九項，**另加三項**：

10. **A-CF19 之實測**：多節 `specification_reference` 之儲存格內容完整
    （逐字元比對 JSON 與儲存格值），並回報該欄最長者之字元數與其
    於列高 14.0 下之可見行數
11. `[BLOCKED-SPEC]`／`[BLOCKED-NON-HMI]`／`[COVERED-BY]` 三類列之
    Remarks 首 60 字元符合各自之規則
12. 列數 == 現行 TC 數；row(10 + N) 起無殘留內容

### 3.4 台帳與停下

`DELIVERY.sha256` 增 **ENTRY 003**（append-only）：操作、來源 hash、
產出 hash、列範圍、TC 數（含各類 BLOCKED／COVERED 之分計）、
狀態記「未經 Excel 確認」。

**產出後停下** —— Excel 四項確認由 Pei 執行（profile §0.1）：
無修復提示、R 欄下拉九項可用、D5 Scope 正確、row 10 起內容與編號正確。

### 3.5 不做

- 不複製至客戶交付路徑（交付另裁；A-CF02 已處置但交付時點未定）
- 不刪 pilot 檔、不改 ENTRY 001／002 之 hash 與內容
- 不執行 git

---

## 4. 往後之節奏

自 ENTRY 003 起，**每批 review 通過後寫回一次**：
生成 → lint → 分析層 review → 修正 → 寫回（全量重寫，非追加）→
Pei 之 Excel 確認 → 下一批。

**全量重寫而非追加**之理由同 §2：既有 TC 會因後續批次之發現而修改
（EMEA PC、軸之增減、sibling 回填），追加會使工作簿內容落後於 JSON。

---

## 5. 本包產生之新條文清單（自檢）

無新條文。§1 為節奏裁定，§2～§4 為作業授權。
