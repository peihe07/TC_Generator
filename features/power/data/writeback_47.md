# B4 —— 寫回紀錄（R-P310）

> **授權**：54 包 §E（R-P323 → R-P331 → 54 包 §E）—— Pei 逐字「授權」，
> 其效力範圍為**授權當時之 283 條內容**。
> ⚠ 本檔由 `write_back_47.py` 產生，其授權字串原寫死為 R-P309（47 包，260 條）——
> **該授權不及於本次之 283 條版本**；已於 54 包改為常數並更新。
> 寫入路徑為 `surgical_save()`；**全域無 `Workbook.save()`**。
> **未對 `inputs/` 之原始檔寫入**。
> **送達為獨立之一步，已於 54 包執行** —— 見交付說明 §8.1。

## 一、寫入對象

| 項 | 值 |
|---|---|
| 來源（唯讀） | `features/power/inputs/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerManagement_20260816.xlsx` |
| 來源 SHA256（寫入前） | `ce93174794d0d43c03d25dcd577c2811b85a8ebb2fd754a5201e5d6979297eda` |
| 來源 SHA256（寫入後） | `ce93174794d0d43c03d25dcd577c2811b85a8ebb2fd754a5201e5d6979297eda` |
| **交付副本** | `output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerManagement_20260816.xlsx` |
| 副本 SHA256 | `def0983b8ca89c171166345cfb509c28d56b72416a24f4a73b7cad659b8dc328` |
| 副本大小 | 120,515 bytes |
| 寫入列數 | **284**（TC 283 ＋ 留白 1） |
| 列範圍 | 10 – 293 |

## 二、寫入後驗證

| 項 | 結果 |
|---|---|
| DV（含 x14）未變 | **PASS** |
| 合併儲存格未變 | **PASS** |
| 條件式格式未變 | **PASS** |
| 分頁清單未變 | **PASS** |
| 壓縮成員清單未變 | **PASS** |
| 凍結窗格未變（G95） | **PASS** |
| 欄寬未變（G95） | **PASS** |
| B 欄序號逐列相符 | **PASS** |
| 列序依 (SWE-PM ID, split_index) | **PASS** |
| 最終 tc_id 逐列相符（001–260 連號） | **PASS** |
| **來源原始檔未被改動** | **PASS** |

## 三、XML 層 diff —— 相異之 part

壓縮成員之增減：**無**

DV 條數：5 → 5（x14：1 → 1）
