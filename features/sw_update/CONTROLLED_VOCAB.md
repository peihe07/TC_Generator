# CONTROLLED_VOCAB — 036 母本受控詞彙欄之值域（SW Update）

**R-SU40(d)**：首次於本 feature 使用某受控欄前，須實測其清單並落於台帳，其後逐次比對。
**R-SU40(b)**：IN 之對照表為**分類之判準**，不是**字面之來源** ——
判準指向哪一類，即取本表中對應該類之**該筆逐字值**。

> ⚠ **本表為 T47c 之一次性補做**（下放包 34）。其成因為一次實害：
> 下放包 33 為六個 TC 指定 `故障注入 (Fault Injection)` —— **該值不在任何清單內**，
> 且於 2,163 列已交付簿普查中出現 **0 次**。**自譯之產物形態上像清單成員。**

---

## 一、母本之資料驗證盤點（全簿）

| 分頁 | 範圍 | 型 | 來源 |
|---|---|---|---|
| `sheet5.xml` | `B7:C7` | 標準 DV | `"Confidential, Top Secret"` |
| `sheet6.xml` | `P10:Q1411` | 標準 DV | `"P0,P1,P2,P3"` |
| `sheet6.xml` | `T10:Z1411` | 標準 DV | `"0,1"` |
| `sheet6.xml` | `AF10:AF1411` | 標準 DV | `"Pass, Fail, Pending,Block,NA"` |
| `sheet6.xml` | `R10:R1411` | **x14 DV** | `下拉選單!$A$1:$A$9` |

**共 5 處。** 標準 DV 與 x14 DV 須分別掃 —— **只掃 `<dataValidation>` 會漏掉 `R` 欄**（其為 x14），而 `R` 正是出事的那一欄。

---

## 二、逐欄之值域全文

### `R` —— Test Case Design Methods 測試用例設計方法（x14 DV → `下拉選單!$A$1:$A$9`）

合法值 **9** 個（逐字，含空白與括號）：

1. `功能測試 (Functional based ; no specific technique)`
2. `狀態轉換 (State Transition Testing)`
3. `決策表 (Decision Table Testing)`
4. `等價劃分 (Equivalence Partitioning, EP)`
5. `邊界值分析 (Boundary Value Analysis, BVA)`
6. `組合測試 (Combinatorial Testing ; Pairwise / t-wise)`
7. `情境 / 用例 (Scenario / Use Case Testing)`
8. `負向測試 (Negative / Invalid)`
9. `基礎故障注入 (Fault Injection Lite)`

> **本 feature 已用**：`1`（batch 1 全部 10 列）、`9`（batch 2a 全部 7 列）。
> `8 負向測試 (Negative / Invalid)` 於 pilot v1–v2 曾用於 `newR1L-SU-004`，
> **v4 起改 `1`** —— 其步驟 2 依 R-SU36(c) 改寫後不再為負向式。

### `B` —— No.# 序號（標準 DV，範圍 `B7:C7`）

合法值 **2** 個（逐字，含空白與括號）：

1. `Confidential`
2. ` Top Secret`

### `P` —— Test Case Priority 測試用例優先級別（標準 DV，範圍 `P10:Q1411`）

合法值 **4** 個（逐字，含空白與括號）：

1. `P0`
2. `P1`
3. `P2`
4. `P3`

### `T` —— HDCC27 Atl-Hi（標準 DV，範圍 `T10:Z1411`）

合法值 **2** 個（逐字，含空白與括號）：

1. `0`
2. `1`

### `AF` —— Test Result 測試結果（標準 DV，範圍 `AF10:AF1411`）

合法值 **5** 個（逐字，含空白與括號）：

1. `Pass`
2. ` Fail`
3. ` Pending`
4. `Block`
5. `NA`

---

## 三、拘束

1. **值一律逐字取自本表**（R-SU40(a)(c)）——不自譯、不自造括號格式、不沿用他文件寫法。
2. **寫入後逐字元比對**，不靠目視（`gen_batch02a.py` 已內建：不符即 `sys.exit`）。
3. **全覽做過不蘊含值域已知**（R-SU40(e)）——`SOURCE_COLUMNS.md` 管「有哪些欄」，本表管「該欄能填什麼」。
4. 母本更版時**本表須重測** ——其為母本之實測快照，非約定。
