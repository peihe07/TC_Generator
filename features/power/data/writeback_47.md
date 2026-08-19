# B4 —— 寫回紀錄（R-P310）

> **授權**：R-P309（Pei 逐字「授權啊」）。
> 寫入路徑為 `surgical_save()`；**全域無 `Workbook.save()`**。
> **未對 `inputs/` 之原始檔寫入**；**未送達客戶目錄**；**未執行任何 git 操作**。

## 一、寫入對象

| 項 | 值 |
|---|---|
| 來源（唯讀） | `features/power/inputs/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerManagement_20260816.xlsx` |
| 來源 SHA256（寫入前） | `ce93174794d0d43c03d25dcd577c2811b85a8ebb2fd754a5201e5d6979297eda` |
| 來源 SHA256（寫入後） | `ce93174794d0d43c03d25dcd577c2811b85a8ebb2fd754a5201e5d6979297eda` |
| **交付副本** | `output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerManagement_20260816.xlsx` |
| 副本 SHA256 | `dc0d2ee0d46e75180add963be130eb59e66669202477716cfe44d7e46eefdb99` |
| 副本大小 | 106,319 bytes |
| 寫入列數 | **261**（TC 260 ＋ 留白 1） |
| 列範圍 | 10 – 270 |

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
