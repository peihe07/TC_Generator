# 46 — Comfort HMI / DR #35 範本容量、A-CF26 跨 feature

- 產出層：分析層｜2026-08-15｜對象：執行層／Pei
- 覆核對象：`docs/upstream/33_batch7.md` §9
- 判定：**DR #35 為交付前之硬阻塞，且其影響跨 feature。**

---

## 1. 由 Pei 於 Excel 擴充，不由 pipeline 延伸

實測：B 欄編號公式至 row 59、R 欄下拉至 row 59、**P 欄下拉僅至 row 11**；
`T–Z` 與 `AF` 同樣僅至 row 11。Comfort 需 403 列以上。

**擇 Excel 之理由**：以 `xlsx_surgical.py` 延伸 DV 之 `sqref` 並補 400 列
公式，是對範本結構之大幅改動；而 profile §0.1 之 Excel 四項確認之所以存在，
正是因為**程式層檢查不能代替 Excel 自身之檔案完整性判定**。
在最可能損壞檔案的一次改動上放棄那道確認，方向相反。
Excel 原生之「選取範圍後延伸驗證」與「公式下拉」為其設計內操作。

### 1.1 Pei 之作業（Tier 3）

自 `output/…_Comfort_20260815_prepared.xlsx`（`b68117a2…`，已確認過之
位元組）擴充至 **row 420**（403 ＋ 餘裕）：

1. B 欄編號公式下拉
2. R 欄下拉（design_method 九項）延伸
3. **P 欄下拉延伸** —— 現僅至 row 11
4. `T–Z` 與 `AF` 之 DV 一併延伸（現留白不影響，成因相同，不另立項）

存為新檔，檔名沿用日期規則。

### 1.2 執行層之驗證（Pei 完成後）

DV `sqref` 涵蓋 ≥ row 412；B 欄公式存在且未被值取代；zip member 數與來源
相同；九項下拉內容逐字元相同。驗畢登 `DELIVERY.sha256` **ENTRY 005**
（`type: template-extension`），記來源與產出 hash。

---

## 2. A-CF26 —— 跨 feature，須立即登記

**P 欄下拉只到 row 11 是通用空白範本 `SWQT_20260121` 之性質，
非 Comfort 之產物。**

Privacy 以同一份範本交付 11 條（row 10–20），其 **row 12–20 之 P 欄同樣無
下拉約束**，且該檔已交付。

依 **R-C21** 登於 Comfort 之 `ANOMALIES.md` 與 `DATA_REQUESTS.md`，
具名對象為 privacy 及其他以該範本為母本之 feature。
**不代改 privacy 之任何檔案** —— 其處置由 Pei 決定是否回溯。

**性質為「內容正確而約束缺失」**：已寫入之值不受影響，故非交付件之內容
錯誤；但下拉之缺失使後續人工編輯不受保護。

---

## 3. 擴充完成前之處置

**所有寫回產物不可交付**（含日後各批）。

生成、lint、review、寫回照常執行，產出檔標「範本容量待擴充」，
**不送 Pei 之 Excel 四項確認** —— 該確認之對象應為擴充後範本所產者，
於現行範本上確認一次，擴充後仍須重做，徒增一次成本。

`DELIVERY.sha256` 之 ENTRY 004 狀態欄增記
`not confirmed — pending template extension (DR #35)`。

---

## 4. 執行層作業指示

1. 依 §2 登 A-CF26 並列 `DATA_REQUESTS.md`（High），具名對象 feature；
   **不改 privacy 任何檔案**。
2. 依 §3 於 ENTRY 004 增記狀態；現有寫回產物標「範本容量待擴充」。
3. Pei 完成擴充後，依 §1.2 驗證並登 ENTRY 005。
4. 其餘作業見下放包 47。

---

## 5. 本包產生之新條文清單（自檢）

無新條文。
