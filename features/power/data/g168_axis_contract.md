# G168 —— `distinguishing_axis` 契約檢查（R-P247）

> **⚠ §4.6 之契約原文於本庫查無**，`duplicate_of` 欄亦不存在於任何 TC；
> 故 `axis` 之**列舉值清單無從取得，執行層不自行擬定**。
> 本閘只檢可查證之結構（C1–C5）。

## 一、結構違規（C1–C4）—— **0** 條

**無。**

**C4 之現況**：`axis="none"` 者 **0** 條 ——該項現**不觸發**，故其正確性**未經本批語料檢驗**（fixture 已另行證明其會 FAIL）。

## 二、`axis` 之值分布

| axis | 條數 |
|---|---|
| `behaviour` | 245 |
| `trigger_state` | 6 |
| `branch` | 6 |
| `timing` | 3 |
| `trigger` | 3 |
| `input_data` | 1 |

## 三、C5 同 leaf 內 `delta` 逐字相同 —— **1** 組

> **觸發不等於違規** —— 逐組之判定屬人工。

| leaf | TC | `delta` |
|---|---|---|
| `SWE-PM-071` | `…-002`、`…-003` | 本條驗抑制分支：轉往 Standby 或 Bench 時不得顯示 splash，與 -01 為互斥條件 |
