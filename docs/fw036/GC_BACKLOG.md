# GC 全域待辦

各 feature 線執行中查得、**須改全域工具或 canon** 而該線不得自改者。
立檔於 2026-09-17（下放包 `CDD-03 §2 T0(c)`）。

登記規則：一項一列；`來源`記其被查出之包；`狀態`只由全域包（GC 線）更新，feature 線不改他人之列。

| # | 項 | 來源 | 影響面 | 建議 | 狀態 |
|---:|---|---|---|---|---|
| 1 | **`lint036.py` 無 `specification_reference` 升冪檢查** —— IN §10.7 要求同文件內 ObjectID 升冪，而 `spec` 欄現只被 `M`（空欄三態）與 `Q`（不可見字元）掃到，**無順序檢查**。CDD-02 pilot01 之 `NR1L-DIAG-009` 四個錨未升冪（`4940473/4940478/4940477/4940474`），lint 全綠而未攔 | CDD-03 §2 T0(c)（成因：CDD-02 審閱 §三-1）| 全 feature 之 `spec` 欄 | 新增全域檢查項：同前綴之錨依數值升冪 | **OPEN** |
| 2 | **`scripts/new_feature.py` 之 ABBR 取法** —— `abbr = feature[:2].upper()`，對任何 ABBR ≠ 前二字之 feature 皆產生錯誤之 anomaly 標記（Diagnostics 得 `A-DI` 而非 `A-DIAG`，已於該 feature 手動修正）| CDD-01 §2（審閱 §五-6 排入全域待辦）| 新 feature 之 scaffold | ABBR 改由參數或 feature.yaml 指定 | **OPEN** |
| 3 | **`docs/fw036/RULINGS.sha.tsv` 之維護歸屬與併發寫入** —— 該檔表頭自稱「單一全域檔，重生掃描全部 canon 與各 feature」，實際為各線逐次 append；`--check` 長期 FAIL（全 repo 現 846 錨點，表內 57 列）。CDD 線 2026-09-17 一日內實測**五次**：四次整檔覆寫（第二次發生於 commit 之後、第四次發生於已正確寫入之後），一次表頭錯位 | CDD-01_A §9.1-1、CDD-02 §1.2（`[A-DIAG15]`）| 全 repo 之 R-G52 引用制 | **GC-16**：單 session 全 repo 重生 ＋ 指定單一維護者；在此之前 R-G75 為過渡。**另須加結構檢查**（表頭須為第一個非註解行、不得重複）—— 第五次事件為表頭錯位，列數不變，R-G75(b) 之集合比對查不出 | **OPEN（CDD-02 審閱 §五-1 建議提前至 SEC-13 上繳後）** |
